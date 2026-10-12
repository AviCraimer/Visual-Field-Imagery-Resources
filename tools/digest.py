#!/usr/bin/env python3
"""Cut each source down to the windows densest in light-and-seeing vocabulary.
Writes data/<stream>/digests/<id>.md. Text inside windows is the source's own, unaltered apart from blank-line squeezing."""
import json, re, sys, textwrap
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
BUDGET = 40000
HALF = 18  # lines either side of a peak
STRONG = re.compile(r"nimitt|kasi[nṇ]a|phosphen|after[- ]?image|jyoti|tr[aā][tṭ]ak|thigle|th[oö]d?gal|photism|qaumane|chashmal|hashmal|scry|crystal|eyelid|closed eyes|eyes (?:are |were )?(?:closed|shut)|open eyes|eyes open|eyebrow|third eye|tisra til|bindu|aureole|halo|blue pearl|spiritual eye|inner light|light within|white light|golden light|divine light", re.I)
MID = re.compile(r"\blights?\b|lumin|radian|\bbright|brillian|\blamp|\bflame|\bspark|\bstars?\b|\bmoon|\bsun\b|colou?r|\bglow|shin(?:e|ing)|\bshone|dazzl|\bglitter|flash|\bfire\b|\brays?\b|splend|effulg|\bglory|darkness|\bdark\b|\bnight\b|\bn[uū]r\b|\bobh[aā]sa|[aā]loka|\bor\b ha|tejas|prak[aā]sh", re.I)
WEAK = re.compile(r"\beyes?\b|\bgaz(?:e|ing)|\bsee(?:n|s|ing)?\b|\bsaw\b|\bbehold|\bvision|\bappear|\bvisible|\bconcentrat|\bfix(?:ed|ing)?\b|\bpractice|\bmeditat|\bfirst\b|\bbeginner|\bdays?\b|\bweeks?\b|\bmonths?\b|\bhours?\b", re.I)

ML_STRONG = re.compile(
    r"نور|أنوار|انوار|ضوء|ضياء|إشراق|اشراق|لمعة|لوامع|بريق|برق|شعاع|"            # Arabic
    r"روشنی|روشن|تابش|درخشش|فروغ|"                                                 # Persian
    r"光|明|白|金華|金华|性光|慧光|神光|電|电|閃|闪|"                                  # Chinese
    r"אור|אורה|זוהר|זהר|נהורא|נהירו|בהיר|"                                          # Hebrew / Aramaic
    r"Licht|leucht|Leucht|Glanz|glänz|Schein|Funke|Lichterscheinung|"              # German
    r"lumière|lumineu|lueur|clart|éclat|étincel|rayon")                            # French
ML_MID = re.compile(
    r"لون|ألوان|الوان|عين|أعين|عيون|بصر|ظلمة|ظلام|خلوة|شمس|قمر|كوكب|نار|مشاهدة|"
    r"رنگ|چشم|دیده|تاریکی|خلوت|آفتاب|ماه|ستاره|آتش|"
    r"目|眼|瞳|睛|日|月|星|火|見|见|視|视|觀|观|閉|闭|簾|帘|暗|黑|色|"
    r"עין|עינים|גוון|גוונין|צבע|חשך|חושך|שמש|ירח|כוכב|אש|"
    r"Farbe|farbig|Auge|dunkel|Dunkel|hell|Helle|Sonne|Stern|Flamme|Feuer|sehen|Gesicht|"
    r"couleur|yeux|oeil|œil|obscur|ténèbre|soleil|étoile|flamme|feu|vision")

def score(line):
    return _score_en(line) + 3 * len(ML_STRONG.findall(line)) + len(ML_MID.findall(line))

def _score_en(line):
    return 3 * len(STRONG.findall(line)) + len(MID.findall(line)) + 0.3 * len(WEAK.findall(line))

def load_lines(path):
    out = []
    for i, raw in enumerate(path.read_text(errors="replace").splitlines(), 1):
        raw = raw.rstrip()
        if len(raw) > 220 and raw.count(" ") < len(raw) / 30:   # unspaced scripts (Chinese): cut by characters
            for k in range(0, len(raw), 80):
                out.append((i, raw[k:k + 80]))
        elif len(raw) > 220:
            for part in textwrap.wrap(raw, 110, break_long_words=False, break_on_hyphens=False) or [""]:
                out.append((i, part))
        else:
            out.append((i, raw))
    return out

def squeeze(lines):
    res, blank = [], 0
    for n, t in lines:
        if not t.strip():
            blank += 1
            if blank > 1:
                continue
        else:
            blank = 0
        res.append((n, t))
    return res

def digest_file(path, budget):
    lines = squeeze(load_lines(path))
    total = sum(len(t) + 1 for _, t in lines)
    if total <= budget:
        return f"[whole file, {len(lines)} lines]\n" + "\n".join(t for _, t in lines), total
    sc = [score(t) for _, t in lines]
    pre = [0.0]
    for s in sc:
        pre.append(pre[-1] + s)
    W = 12
    dens = [pre[min(len(sc), i + W + 1)] - pre[max(0, i - W)] for i in range(len(sc))]
    order = sorted(range(len(sc)), key=lambda i: -dens[i])
    taken = [False] * len(sc)
    used = 0
    head = min(40, len(lines))            # always show the opening (title page, contents)
    for i in range(head):
        taken[i] = True; used += len(lines[i][1]) + 1
    for i in order:
        if dens[i] <= 0 or used >= budget:
            break
        if taken[i]:
            continue
        a, b = max(0, i - HALF), min(len(sc), i + HALF + 1)
        add = sum(len(lines[j][1]) + 1 for j in range(a, b) if not taken[j])
        if used + add > budget * 1.05:
            continue
        for j in range(a, b):
            taken[j] = True
        used += add
    out, i = [], 0
    while i < len(lines):
        if taken[i]:
            j = i
            while j < len(lines) and taken[j]:
                j += 1
            out.append(f"\n----- [source lines {lines[i][0]}-{lines[j-1][0]} of {lines[-1][0]}] -----")
            out.extend(t for _, t in lines[i:j])
            i = j
        else:
            i += 1
    return "\n".join(out), used

def main(maxprio, only=None):
    n = 0
    for cf in sorted(ROOT.glob("data/*/candidates/*.json")):
        c = json.loads(cf.read_text())
        if only and c["id"] not in only:
            continue
        if not only and c.get("priority", 3) > maxprio:
            continue
        sdir = ROOT / "data" / c["stream"]
        files = [sdir / f for f in c.get("source_files", []) if (sdir / f).is_file()]
        if not files:
            continue
        (sdir / "digests").mkdir(exist_ok=True)
        per = BUDGET // len(files)
        parts = [f"# DIGEST of {c['id']}\n",
                 f"Title: {c.get('title')}\nAuthor: {c.get('author')}  Year: {c.get('year')}  Edition: {c.get('edition_cited')}",
                 f"Rights: {c.get('rights')}  Access: {c.get('access')}  Source type: {c.get('source_type')}",
                 f"Search agent's locator hints: {c.get('locator_hints')}",
                 f"Search agent's summary (unverified): {c.get('summary')}",
                 "\nBelow: the passages of the saved text densest in light-and-seeing vocabulary, in document order. "
                 "The text is the source's own. Gaps between windows are omitted text; the full file is at the path shown.\n"]
        for f in files:
            body, used = digest_file(f, per)
            parts.append(f"\n===== FILE {f.relative_to(sdir)} ({f.stat().st_size} bytes) =====\n{body}")
        (sdir / "digests" / f"{c['id']}.md").write_text("\n".join(parts) + "\n")
        n += 1
    print(n, "digests written")

if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--ids":
        main(3, set(a[1:]))
    else:
        main(int(a[0]) if a else 1)
