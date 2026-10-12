#!/usr/bin/env python3
"""Compact reading pack for the cataloguing-and-report agent: one markdown file, kept items only."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
L = json.loads((ROOT/'library'/'library.json').read_text())
out = ["# Reading pack: every kept source, condensed\n"]
unread = []
for s in L['streams']:
    its = [i for i in L['items'] if i['stream'] == s['id']]
    kept = [i for i in its if i['status'] in ('keep', 'keep_marginal')]
    if kept: out.append(f"\n# STREAM: {s['name']} ({s['id']})\n")
    for i in kept:
        r = i['reading']; sc = (i.get('screen') or {}).get('decision')
        out.append(f"## [{i['id']}] {i['title']}")
        out.append(f"{i.get('author')}; {i.get('year')}; {i.get('source_type')}; rights {i.get('rights')}; access {i.get('access')}; screen {sc}; {i['status']}; relevance {r.get('relevance')}, practicality {r.get('practicality')}, confidence {r.get('reader_confidence')}" + (f" ({r.get('confidence_note')})" if r.get('confidence_note') else ""))
        out.append(f"- mode: {r.get('mode')}. {r.get('mode_evidence','')}")
        out.append(f"- eyes: {r.get('eyes')}; stimulus independence: {r.get('stimulus_independence')}")
        out.append(f"- ONSET {r.get('onset_pathway')}: {r.get('onset_evidence','')}")
        out.append(f"- techniques: {', '.join(r.get('techniques') or [])}; phenomena: {', '.join(r.get('phenomena') or [])}")
        c = {k: v for k, v in (r.get('conditions') or {}).items() if v}
        if c: out.append("- conditions: " + "; ".join(f"{k}: {v}" for k, v in c.items()))
        if r.get('stages'): out.append("- stages: " + " -> ".join(f"{x.get('label')}: {x.get('description')}" for x in r['stages']))
        if r.get('what_to_do_with_light'): out.append(f"- with the light: {r['what_to_do_with_light']}")
        if r.get('obstacles_and_fixes'): out.append("- obstacles/fixes: " + " | ".join(r['obstacles_and_fixes']))
        if r.get('cautions'): out.append("- cautions: " + " | ".join(r['cautions']))
        if r.get('safety_flags'): out.append("- safety flags: " + ", ".join(r['safety_flags']))
        if r.get('interpretation'): out.append(f"- interpretation: {r['interpretation']}")
        out.append(f"- practice: {r.get('practice_summary','')}")
        for p in r.get('key_passages') or []:
            out.append(f"  - passage ({p.get('about')}; {p.get('locator')}): {p.get('paraphrase')}")
        if r.get('new_leads'): out.append("- new leads: " + " | ".join(map(str, r['new_leads'])))
        out.append("")
    unread += [f"- [{i['id']}] {i['title']} ({i.get('author')}, {i.get('year')}), priority {i.get('priority')}: {(i.get('summary') or '')[:260]}" for i in its if i['status'] == 'unread']
out.append("\n# GATHERED BUT NOT READ (cannot be cited; for the gap report only)\n")
out += unread
(ROOT/'library'/'pack.md').write_text("\n".join(out) + "\n")
print(len("\n".join(out)), "chars")
