#!/usr/bin/env python3
"""Build ui/dist/inner-light-library.html from ui/template.html and the library inputs.
Works on any partial state: only library/library.json is required."""
import json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)

def text(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except Exception:
        return None

lib = json.load(open(P("library", "library.json"), encoding="utf-8"))
data = {
    "streams": lib.get("streams") or [],
    "vocab": lib.get("vocab") or {},
    "families": lib.get("families") or [],
    "items": lib.get("items") or [],
    "generated": lib.get("generated"),
    "report": text(P("report", "report.md")),
    "gaps": text(P("library", "gaps.md")),
    "overview": text(P("library", "overview.md")),
    "dropped": text(P("library", "dropped.md")),
}
blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
tpl = open(P("ui", "template.html"), encoding="utf-8").read()
out = tpl.replace("/*__DATA__*/null", blob, 1)
os.makedirs(P("ui", "dist"), exist_ok=True)
dest = P("ui", "dist", "inner-light-library.html")
open(dest, "w", encoding="utf-8").write(out)
print("wrote", dest, round(len(out) / 1024), "KB", len(data["items"]), "items")
