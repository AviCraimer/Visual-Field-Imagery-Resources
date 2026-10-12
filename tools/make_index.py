#!/usr/bin/env python3
"""Wrap the built navigator (ui/dist/visual-field-imagery-library.html, page-content form) into a full
standalone document at the repository root as index.html, for GitHub Pages. Run after ui/build.py."""
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
src = ROOT / "ui" / "dist" / "inner-light-library.html"
body = src.read_text()
doc = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
       '<meta name="description" content="A cross-tradition library of practical sources on developing visual field imagery (VFI): light seen behind closed lids or before open eyes.">\n'
       '<style>[hidden]{display:none!important}img{max-width:100%}</style>\n'
       '</head>\n<body>\n' + body + '\n</body>\n</html>\n')
(ROOT / "index.html").write_text(doc)
(ROOT / "ui" / "dist" / "visual-field-imagery-library.html").write_text(doc)
(ROOT / ".nojekyll").write_text("")
print("wrote index.html", len(doc) // 1024, "KB")
