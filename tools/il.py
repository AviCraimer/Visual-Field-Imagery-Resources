#!/usr/bin/env python3
"""il.py: bookkeeping for the inner-light research run.

Deterministic and safe to run at any moment, on any partial state.
Commands: stream, kickoff, sites, status, todo, validate, screen, build, snapshot
"""
import argparse
import datetime as dt
import json
import os
import re
import sys
import tarfile
import unicodedata
from pathlib import Path

ROOT = Path(os.environ.get("IL_ROOT") or Path(__file__).resolve().parent.parent)
DATA = ROOT / "data"
LIB = ROOT / "library"
VOCAB = json.loads((ROOT / "vocab.json").read_text())
STREAMS = json.loads((ROOT / "streams.json").read_text())["streams"]
STREAM_BY_ID = {s["id"]: s for s in STREAMS}
CONFIG = json.loads((ROOT / "config.json").read_text())
CUTOFF = CONFIG.get("cutoff_year", 2022)

CAND_REQUIRED = ["id", "stream", "title", "author", "year", "source_type", "rights", "access",
                 "url", "source_files", "summary", "why_relevant", "priority", "medium", "date_evidence"]
READ_REQUIRED_KEEP = ["mode", "mode_evidence", "eyes", "onset_pathway", "onset_evidence", "techniques",
                      "practice_summary", "key_passages", "relevance", "practicality", "reader_confidence"]
ABOUT = ["onset", "method", "development", "stages", "mode", "caution", "testimony", "interpretation"]


# ---------- helpers ----------

def now():
    return dt.datetime.now().strftime("%Y-%m-%d %H:%M")


def load_json(path):
    try:
        return json.loads(path.read_text()), None
    except Exception as e:  # noqa: BLE001
        return None, f"{type(e).__name__}: {e}"


def records(stream, kind):
    d = DATA / stream / kind
    out = {}
    if d.is_dir():
        for p in sorted(d.glob("*.json")):
            obj, err = load_json(p)
            out[p.stem] = (obj, err, p)
    return out


def words(text):
    text = unicodedata.normalize("NFKC", text).replace("­", "")
    text = re.sub(r"-\s*\n\s*", "", text)  # rejoin words hyphenated across lines
    return re.findall(r"\w+", text.lower())


_norm_cache = {}


def norm_file(path):
    if path not in _norm_cache:
        try:
            _norm_cache[path] = " " + " ".join(words(path.read_text(errors="replace"))) + " "
        except Exception:  # noqa: BLE001
            _norm_cache[path] = None
    return _norm_cache[path]


def check_anchor(stream, cand, passage):
    """True / False / None (None = no local source to check against)."""
    anchor = (passage.get("anchor") or "").strip()
    if not anchor:
        return False
    files = []
    if passage.get("source_file"):
        files.append(passage["source_file"])
    files += [f for f in (cand or {}).get("source_files", []) if f not in files]
    needle = " " + " ".join(words(anchor)) + " "
    seen_any = False
    for f in files:
        p = DATA / stream / f
        if not p.is_file():
            continue
        hay = norm_file(p)
        if hay is None:
            continue
        seen_any = True
        if needle in hay:
            return True
    return False if seen_any else None


def wc(s):
    return len((s or "").split())


def need_stream(name):
    if name not in STREAM_BY_ID:
        sys.exit(f"unknown stream '{name}'. Known: {', '.join(STREAM_BY_ID)}")
    return STREAM_BY_ID[name]


def evidence_year(cand):
    m = re.match(r"\s*(\d{4})", str(((cand or {}).get("date_evidence") or {}).get("date") or ""))
    return int(m.group(1)) if m else None


def screen_rule(cand):
    """Deterministic first pass. Returns (decision, reason)."""
    de = cand.get("date_evidence") or {}
    cls, yr = de.get("class"), evidence_year(cand)
    if cls in ("published_record", "platform_timestamp", "self_reported") and yr is not None and yr <= CUTOFF:
        return "pass", f"{cls}: {de.get('date')}"
    if cls in ("published_record", "platform_timestamp", "self_reported") and yr is not None and yr > CUTOFF:
        cls = "post_2022"
    return "pending", f"{cls or 'no date evidence'}: needs a provenance decision"


def screens(stream):
    d = DATA / stream / "screen"
    out = {}
    if d.is_dir():
        for p in sorted(d.glob("*.json")):
            obj, _ = load_json(p)
            if obj:
                out[p.stem] = obj
    return out


def cmd_screen(a):
    """Write a screen overlay for every candidate that has none. Never overwrites an agent's decision."""
    tot = {}
    pending = []
    for s in STREAMS:
        d = DATA / s["id"] / "screen"
        d.mkdir(parents=True, exist_ok=True)
        have = screens(s["id"])
        for cid, (c, err, _) in records(s["id"], "candidates").items():
            if c is None:
                continue
            if cid not in have:
                dec, why = screen_rule(c)
                have[cid] = {"id": cid, "decision": dec, "reason": why, "by": "rule"}
                (d / f"{cid}.json").write_text(json.dumps(have[cid], indent=1))
            dec = have[cid]["decision"]
            tot[dec] = tot.get(dec, 0) + 1
            if dec == "pending":
                de = c.get("date_evidence") or {}
                pending.append(f"  {s['id']}/{cid} | {c.get('medium')} | {de.get('class')} {de.get('date') or ''} | "
                               f"author identifiable: {c.get('author_identifiable')} | {c.get('url', '')}")
    print("Screen: " + ", ".join(f"{k} {v}" for k, v in sorted(tot.items())))
    if pending:
        print(f"\n{len(pending)} pending a provenance decision:")
        print("\n".join(pending))


# ---------- validation ----------

def validate_candidate(stream, cid, obj, err):
    errs, warns = [], []
    if err:
        return [f"invalid JSON ({err})"], warns
    s = STREAM_BY_ID[stream]
    for k in CAND_REQUIRED:
        if obj.get(k) in (None, "", []) and k not in ("source_files", "url"):
            errs.append(f"missing '{k}'")
    if obj.get("id") != cid:
        errs.append(f"id '{obj.get('id')}' does not match file name")
    if not cid.startswith(s["prefix"] + "-"):
        errs.append(f"id must start with '{s['prefix']}-'")
    if obj.get("stream") != stream:
        errs.append("wrong 'stream'")
    for k in ("source_type", "rights", "access"):
        if obj.get(k) not in VOCAB[k]:
            errs.append(f"'{k}'='{obj.get(k)}' not in {VOCAB[k]}")
    if obj.get("priority") not in (1, 2, 3):
        errs.append("'priority' must be 1, 2 or 3")
    if obj.get("medium") not in VOCAB["medium"]:
        errs.append(f"'medium'='{obj.get('medium')}' not in {VOCAB['medium']}")
    de = obj.get("date_evidence") or {}
    if de.get("class") not in VOCAB["date_class"]:
        errs.append(f"date_evidence.class='{de.get('class')}' not in {VOCAB['date_class']}")
    elif de["class"] != "undated" and evidence_year(obj) is None:
        errs.append("date_evidence.date must start with a four-digit year unless class is 'undated'")
    if de.get("class") in VOCAB["date_class"] and not de.get("basis"):
        errs.append("date_evidence.basis is required: say exactly what the date rests on")
    if obj.get("medium") != "book_or_classical_text" and not isinstance(obj.get("author_identifiable"), bool):
        errs.append("'author_identifiable' (true/false) is required for web and forum sources")
    files = obj.get("source_files") or []
    for f in files:
        if not (DATA / stream / f).is_file():
            errs.append(f"source file not found: {f}")
    if obj.get("access") != "citation_only" and not files:
        errs.append("access says text was saved but 'source_files' is empty")
    if wc(obj.get("summary")) < 40:
        warns.append("summary under 40 words")
    return errs, warns


def validate_reading(stream, rid, obj, err, cand):
    errs, warns = [], []
    if err:
        return [f"invalid JSON ({err})"], warns
    if cand is None:
        errs.append("no matching candidate record")
    if obj.get("id") != rid:
        errs.append("id does not match file name")
    v = obj.get("verdict")
    if v not in VOCAB["verdict"]:
        return errs + [f"'verdict'='{v}' not in {VOCAB['verdict']}"], warns
    if v == "drop":
        if obj.get("drop_reason") not in VOCAB["drop_reason"]:
            errs.append(f"'drop_reason'='{obj.get('drop_reason')}' not in vocab")
        if not obj.get("drop_note"):
            errs.append("dropped record needs a 'drop_note'")
        return errs, warns
    for k in READ_REQUIRED_KEEP:
        if obj.get(k) in (None, "", []):
            errs.append(f"missing '{k}'")
    for k in ("mode", "eyes", "onset_pathway"):
        if obj.get(k) is not None and obj.get(k) not in VOCAB[k]:
            errs.append(f"'{k}'='{obj.get(k)}' not in {VOCAB[k]}")
    si = obj.get("stimulus_independence")
    if si is not None and si not in VOCAB["stimulus_independence"]:
        errs.append(f"'stimulus_independence'='{si}' not in vocab")
    for t in obj.get("techniques") or []:
        if t not in VOCAB["techniques"]:
            errs.append(f"technique '{t}' not in vocab")
    for f in obj.get("safety_flags") or []:
        if f not in VOCAB["safety_flags"]:
            errs.append(f"safety flag '{f}' not in vocab")
    if wc(obj.get("practice_summary")) < 50:
        warns.append("practice_summary under 50 words")
    rights = (cand or {}).get("rights", "unknown")
    for i, p in enumerate(obj.get("key_passages") or [], 1):
        tag = f"passage {i}"
        if not p.get("locator"):
            errs.append(f"{tag}: missing locator")
        if p.get("about") not in ABOUT:
            errs.append(f"{tag}: 'about' must be one of {ABOUT}")
        if not p.get("paraphrase"):
            errs.append(f"{tag}: missing paraphrase")
        n = wc(p.get("anchor"))
        if n == 0:
            errs.append(f"{tag}: missing anchor")
        elif n < 6 or n > 30:
            warns.append(f"{tag}: anchor is {n} words (aim for 8 to 25)")
        if p.get("quote"):
            if rights != "public_domain":
                errs.append(f"{tag}: 'quote' must be empty because the source is not public domain; use paraphrase + anchor")
            elif wc(p["quote"]) > 300:
                warns.append(f"{tag}: quote over 300 words")
        res = check_anchor(stream, cand, p) if n else False
        if res is False and n:
            errs.append(f"{tag}: anchor not found verbatim in the saved source text")
        elif res is None:
            warns.append(f"{tag}: no saved source text to verify the anchor against")
    return errs, warns


def cmd_validate(a):
    need_stream(a.stream)
    cands = records(a.stream, "candidates")
    reads = records(a.stream, "readings")
    n_err = 0
    stages = [a.stage] if a.stage else ["search", "read"]
    if "search" in stages:
        for cid, (obj, err, _) in cands.items():
            errs, warns = validate_candidate(a.stream, cid, obj, err)
            for e in errs:
                print(f"ERROR  candidates/{cid}: {e}")
            for w in warns:
                print(f"warn   candidates/{cid}: {w}")
            n_err += len(errs)
    if "read" in stages:
        for rid, (obj, err, _) in reads.items():
            cand = cands.get(rid, (None, None, None))[0]
            errs, warns = validate_reading(a.stream, rid, obj, err, cand)
            for e in errs:
                print(f"ERROR  readings/{rid}: {e}")
            for w in warns:
                print(f"warn   readings/{rid}: {w}")
            n_err += len(errs)
    print(f"\n{a.stream}: {len(cands)} candidates, {len(reads)} readings, {n_err} errors")
    sys.exit(1 if n_err else 0)


# ---------- stream / todo / status ----------

def cmd_stream(a):
    s = need_stream(a.stream)
    print(f"# Stream: {s['name']}\nid: {s['id']}    id prefix: {s['prefix']}-\n")
    ws = s.get("web_sites") or []
    print("Websites you own (WebFetch allowed only on those your warm-up found approved): "
          + (", ".join(ws) if ws else "none; you have no WebFetch at all") + "\n")
    print(f"Scope: {s['scope']}\n\nBoundary notes: {s['boundary']}\n")
    print("Seed leads (UNVERIFIED pointers from memory; verify, drop freely, and go beyond them):")
    for lead in s["seed_leads"]:
        print(f"  - {lead}")
    print("\nOther streams in this run (do not duplicate their territory):")
    for o in STREAMS:
        if o["id"] != s["id"]:
            print(f"  - {o['id']}: {o['name']}")


def todo_ids(stream, shard=None, maxprio=3):
    cands = records(stream, "candidates")
    reads = records(stream, "readings")
    ids = sorted(cands)
    if shard:
        i, n = (int(x) for x in shard.split("/"))
        ids = [x for k, x in enumerate(ids) if k % n == i]
    scr = screens(stream)
    rest = [x for x in ids if x not in reads and scr.get(x, {}).get("decision") != "fail"
            and (cands[x][0] or {}).get("priority", 3) <= maxprio]
    rest.sort(key=lambda x: ((cands[x][0] or {}).get("priority", 3), x))
    return rest, cands


def cmd_todo(a):
    need_stream(a.stream)
    rest, cands = todo_ids(a.stream, a.shard, a.max_priority)
    if not rest:
        print("Nothing left to read for this stream" + (f" (shard {a.shard})" if a.shard else "") + ".")
        return
    print(f"{len(rest)} sources still to read:")
    for x in rest:
        c = cands[x][0] or {}
        print(f"  [{c.get('priority', '?')}] {x}  |  {c.get('title', '?')}  ({c.get('author', '?')})  |  {c.get('access', '?')}")


def stream_stats(stream):
    cands = records(stream, "candidates")
    reads = records(stream, "readings")
    d = DATA / stream
    verdicts = {"keep": 0, "keep_marginal": 0, "drop": 0}
    for _, (obj, err, _) in reads.items():
        if obj and obj.get("verdict") in verdicts:
            verdicts[obj["verdict"]] += 1
    with_text = sum(1 for _, (o, _, _) in cands.items() if o and o.get("source_files"))
    scr = screens(stream)
    failed = {c for c in cands if scr.get(c, {}).get("decision") == "fail"}
    unread = len([c for c in cands if c not in reads and c not in failed])
    return {
        "cands": len(cands), "with_text": with_text, "screened_out": len(failed),
        "reads": len(reads), "unread": unread, **verdicts,
        "search_done": (d / "SEARCH_DONE.md").is_file(),
        "read_done": bool(list(d.glob("READ_DONE*.md"))) and unread == 0 and len(cands) > 0,
    }


def status_table():
    lines = ["| Stream | Found | Text saved | Screened out | Read | Keep | Marginal | Drop | Search | Reading |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    tot = dict(cands=0, with_text=0, screened_out=0, reads=0, keep=0, keep_marginal=0, drop=0)
    for s in STREAMS:
        st = stream_stats(s["id"])
        for k in tot:
            tot[k] += st[k]
        sd = "done" if st["search_done"] else ("partial" if st["cands"] else "not started")
        rd = "done" if st["read_done"] else ("partial" if st["reads"] else "not started")
        lines.append(f"| {s['id']} | {st['cands']} | {st['with_text']} | {st['screened_out']} | {st['reads']} | {st['keep']} | "
                     f"{st['keep_marginal']} | {st['drop']} | {sd} | {rd} |")
    lines.append(f"| **Total** | {tot['cands']} | {tot['with_text']} | {tot['screened_out']} | {tot['reads']} | {tot['keep']} | "
                 f"{tot['keep_marginal']} | {tot['drop']} |  |  |")
    extras = []
    for label, p in [("Library", LIB / "library.json"), ("Curation", LIB / "curation.json"),
                     ("Gap report", LIB / "gaps.md"), ("Report", ROOT / "report" / "report.md"),
                     ("Navigator", ROOT / "ui" / "dist" / "inner-light-library.html")]:
        extras.append(f"- {label}: {'present' if p.is_file() else 'not yet'}")
    return "\n".join(lines) + "\n\n" + "\n".join(extras)


def cmd_status(a):
    if a.stream:
        need_stream(a.stream)
        st = stream_stats(a.stream)
        print(json.dumps(st, indent=1))
        cands = records(a.stream, "candidates")
        reads = records(a.stream, "readings")
        for cid, (obj, _, _) in cands.items():
            r = reads.get(cid, (None,))[0]
            print(f"  {cid}: {(r or {}).get('verdict', 'unread')}")
        return
    table = f"# Run status ({now()})\n\n{status_table()}\n"
    print(table)
    if a.write:
        (ROOT / "STATUS.md").write_text(table)


# ---------- build ----------

def cmd_build(a):
    LIB.mkdir(exist_ok=True)
    curation, _ = load_json(LIB / "curation.json") if (LIB / "curation.json").is_file() else ({}, None)
    curation = curation or {}
    cur_items = curation.get("items", {})
    items, problems = [], []
    for s in STREAMS:
        cands = records(s["id"], "candidates")
        reads = records(s["id"], "readings")
        scr = screens(s["id"])
        for cid, (c, cerr, _) in cands.items():
            if c is None:
                problems.append(f"{s['id']}/candidates/{cid}: {cerr}")
                continue
            r, rerr, _ = reads.get(cid, (None, None, None))
            if rerr:
                problems.append(f"{s['id']}/readings/{cid}: {rerr}")
            item = dict(c)
            item["stream_name"] = s["name"]
            item["status"] = (r or {}).get("verdict", "unread")
            item["screen"] = scr.get(cid)
            if not r and (item["screen"] or {}).get("decision") == "fail":
                item["status"] = "screened_out"
            ok = bad = 0
            if r:
                for p in r.get("key_passages") or []:
                    res = check_anchor(s["id"], c, p)
                    p["anchor_verified"] = res
                    ok += res is True
                    bad += res is False
            item["reading"] = r
            item["anchors_verified"] = ok
            item["anchors_failed"] = bad
            item["curation"] = cur_items.get(cid)
            if item["curation"] and item["curation"].get("merged_into"):
                item["status"] = "merged"
            items.append(item)
    counts = {}
    for it in items:
        counts[it["status"]] = counts.get(it["status"], 0) + 1
    lib = {
        "generated": now(),
        "note": a.note or "",
        "streams": [{"id": s["id"], "name": s["name"], "prefix": s["prefix"]} for s in STREAMS],
        "vocab": VOCAB,
        "families": curation.get("families", []),
        "counts": counts,
        "items": items,
        "problems": problems,
    }
    (LIB / "library.json").write_text(json.dumps(lib, ensure_ascii=False, indent=1))
    write_catalogue(lib)
    print(f"library.json: {len(items)} items {counts}; {len(problems)} unreadable records")
    print(f"catalogue: {LIB / 'CATALOGUE.md'}")


def write_catalogue(lib):
    out = [f"# Inner light library: catalogue\n\nGenerated {lib['generated']}. {lib['note']}\n",
           "Counts: " + ", ".join(f"{k} {v}" for k, v in sorted(lib["counts"].items())) + "\n"]
    dropped = []
    for s in lib["streams"]:
        its = [i for i in lib["items"] if i["stream"] == s["id"]]
        if not its:
            continue
        out.append(f"\n## {s['name']}\n")
        kept = [i for i in its if i["status"] in ("keep", "keep_marginal")]
        kept.sort(key=lambda i: (-(i["reading"].get("relevance") or 0), -(i["reading"].get("practicality") or 0)))
        for i in kept:
            r = i["reading"]
            tier = (i.get("curation") or {}).get("tier")
            out.append(f"### {i['title']}\n")
            out.append(f"{i.get('author', '')}, {i.get('year', '')}. `{i['id']}`"
                       + (f" Tier {tier}." if tier else "")
                       + (" *Marginal.*" if i["status"] == "keep_marginal" else "") + "\n")
            out.append(f"- Mode: {r.get('mode')}. Eyes: {r.get('eyes')}. Onset pathway: **{r.get('onset_pathway')}**. "
                       f"Relevance {r.get('relevance')}/5, practicality {r.get('practicality')}/5.")
            out.append(f"- Techniques: {', '.join(r.get('techniques') or [])}")
            de, sc = i.get("date_evidence") or {}, i.get("screen") or {}
            out.append(f"- Date: {de.get('date') or 'undated'} ({de.get('class')})"
                       + (" **Flagged: no pre-2023 date evidence.**" if sc.get("decision") == "pass_flagged" else ""))
            if r.get("safety_flags"):
                out.append(f"- Safety flags: {', '.join(r['safety_flags'])}")
            out.append(f"- Onset: {r.get('onset_evidence', '')}")
            out.append(f"\n{r.get('practice_summary', '')}\n")
            for p in r.get("key_passages") or []:
                mark = {True: "verified", False: "NOT FOUND", None: "unchecked"}[p.get("anchor_verified")]
                out.append(f"- *{p.get('about')}* at {p.get('locator')} (anchor {mark}): {p.get('paraphrase')}")
            if i.get("url"):
                out.append(f"\n<{i['url']}>\n")
        unread = [i for i in its if i["status"] == "unread"]
        if unread:
            out.append("\n**Gathered, not yet read**\n")
            for i in sorted(unread, key=lambda i: i.get("priority", 3)):
                out.append(f"- **{i['title']}** ({i.get('author', '')}, {i.get('year', '')}). {i.get('summary', '')} "
                           + (f"<{i['url']}>" if i.get("url") else ""))
        dropped += [i for i in its if i["status"] in ("drop", "screened_out")]
    (LIB / "CATALOGUE.md").write_text("\n".join(out) + "\n")
    d = ["# Dropped (screened out before reading, or dropped after reading)\n"]
    for i in dropped:
        if i["status"] == "screened_out":
            d.append(f"- **{i['title']}** ({i.get('author', '')}) `{i['id']}`: screened out before reading. {i['screen'].get('reason', '')}")
            continue
        r = i["reading"]
        d.append(f"- **{i['title']}** ({i.get('author', '')}) `{i['id']}`: {r.get('drop_reason')}. {r.get('drop_note', '')}")
    (LIB / "dropped.md").write_text("\n".join(d) + "\n")


# ---------- kickoff prompts ----------

def cmd_kickoff(a):
    """Print the exact prompt for an agent, so every launch is consistent."""
    wd = "/home/claude/inner-light"
    if a.stage == "search":
        s = need_stream(a.stream)
        ws = s.get("web_sites") or []
        calls = [f'- WebSearch: query "{s["warmup_query"]}", mode "standard"']
        calls += [f'- WebFetch: url "https://{h}/", prompt "In one sentence, what is this site?"' for h in ws]
        site_rules = (
            "If a fetch reports a redirect to a different host, fetch that host once, now, and from then on use only the "
            "final host. Then write `data/" + s["id"] + "/warmup.md`: one line per call with the outcome (approved, declined, "
            "timed out, blocked by the tool, redirected to X), and whether WebSearch worked. A host that was declined, timed "
            "out or blocked is off limits for the rest of your task: never call WebFetch on it again. Never call WebFetch on "
            "any host that is not in the list above."
        ) if ws else (
            "Then write `data/" + s["id"] + "/warmup.md` saying whether WebSearch worked. You own no websites in this run: "
            "never call WebFetch at all."
        )
        head = f"You are the SEARCH agent for stream `{s['id']}` in a research run. Working directory: {wd}."
        tail = (f"read BRIEF.md and prompts/search.md and follow them exactly. Start with `python3 tools/il.py stream {s['id']}` "
                f"and `python3 tools/il.py status --stream {s['id']}`. If candidate records already exist, continue from them; do not redo.")
        if a.resume_away:
            print(f"""{head}

You are resuming a stopped run and the user is NOT present. A new agent holds no approvals, so make no WebFetch and no WebSearch call under any circumstances, whatever other instructions say about websites you own. Work only from direct downloads from the archive domains. Then {tail}""")
        else:
            print(f"""{head}

FIRST ACTION, before reading any file. The user is at their screen for the next few minutes to approve permissions and will then leave, so every permission you will ever need must be requested now. In ONE message, make all of these tool calls in parallel:
{chr(10).join(calls)}
{site_rules} If WebSearch itself was declined or timed out, do not use it again; work from the archives.

THEN {tail}""")
    elif a.stage == "read":
        s = need_stream(a.stream)
        sh = f" --shard {a.shard}" if a.shard else ""
        print(f"""You are the READING agent for stream `{s['id']}`{' shard ' + a.shard if a.shard else ''} in a research run. Working directory: {wd}. The user is away: make no WebSearch or WebFetch call under any circumstances. Read BRIEF.md, then prompts/read.md, and follow them exactly. Your queue is `python3 tools/il.py todo --stream {s['id']}{sh}`. Sources that already have a reading record are done: skip them.""")
    else:
        extra = " This is the polish pass." if a.stage == "ui-polish" else ""
        f = "ui" if a.stage == "ui-polish" else a.stage
        print(f"""Working directory: {wd}. The user is away: make no WebSearch or WebFetch call under any circumstances. Read prompts/{f}.md and follow it exactly.{extra}""")


def cmd_sites(a):
    """List every website permission the gathering stage will request, by agent."""
    n = 0
    for s in STREAMS:
        ws = s.get("web_sites") or []
        if ws:
            n += len(ws)
            print(f"{s['id']} ({len(ws)}): {', '.join(ws)}")
    print(f"\n{n} site approvals across {sum(1 for s in STREAMS if s.get('web_sites'))} agents; "
          f"{len(STREAMS)} agents each make one web search.")


# ---------- snapshot ----------

def cmd_snapshot(a):
    snap = ROOT / "snapshots"
    snap.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%m%d-%H%M")
    rec = snap / f"inner-light-records-{a.label}-{stamp}.tar.gz"
    src = snap / f"inner-light-sources-{a.label}-{stamp}.tar.gz"

    def is_source(p):
        parts = Path(p).parts
        return "sources" in parts and "data" in parts

    def skip(p):
        parts = Path(p).parts
        return "snapshots" in parts or "__pycache__" in parts or "node_modules" in parts

    with tarfile.open(rec, "w:gz") as t:
        t.add(ROOT, arcname="inner-light", filter=lambda ti: None if (skip(ti.name) or is_source(ti.name)) else ti)
    print(f"{rec}  {rec.stat().st_size / 1e6:.2f} MB")
    if not a.records_only:
        with tarfile.open(src, "w:gz") as t:
            for s in STREAMS:
                d = DATA / s["id"] / "sources"
                if d.is_dir():
                    t.add(d, arcname=f"inner-light/data/{s['id']}/sources")
        print(f"{src}  {src.stat().st_size / 1e6:.2f} MB")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("stream"); p.add_argument("stream"); p.set_defaults(f=cmd_stream)
    p = sub.add_parser("status"); p.add_argument("--stream"); p.add_argument("--write", action="store_true"); p.set_defaults(f=cmd_status)
    p = sub.add_parser("todo"); p.add_argument("--stream", required=True); p.add_argument("--shard"); p.add_argument("--max-priority", type=int, default=3); p.set_defaults(f=cmd_todo)
    p = sub.add_parser("validate"); p.add_argument("--stream", required=True); p.add_argument("--stage", choices=["search", "read"]); p.set_defaults(f=cmd_validate)
    p = sub.add_parser("screen"); p.set_defaults(f=cmd_screen)
    p = sub.add_parser("sites"); p.set_defaults(f=cmd_sites)
    p = sub.add_parser("kickoff"); p.add_argument("--stage", required=True, choices=["search", "read", "provenance", "librarian", "gapfill", "synthesizer", "reportcheck", "ui", "ui-polish"]); p.add_argument("--stream"); p.add_argument("--shard"); p.add_argument("--resume-away", action="store_true"); p.set_defaults(f=cmd_kickoff)
    p = sub.add_parser("build"); p.add_argument("--note"); p.set_defaults(f=cmd_build)
    p = sub.add_parser("snapshot"); p.add_argument("--label", required=True); p.add_argument("--records-only", action="store_true"); p.set_defaults(f=cmd_snapshot)
    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
