# Navigator UI

Rebuild: `python3 ui/build.py` (writes `ui/dist/inner-light-library.html`; safe on any partial state).

Inputs: `library/library.json` (required: items, streams, vocab, families), `report/report.md`, `library/gaps.md`, `library/overview.md`, `library/dropped.md` (all optional; absent pieces show a placeholder). Curation (tier, families, librarian note) appears automatically once present in library.json. `ui/template.html` holds markup, styles and script; the data replaces the `/*__DATA__*/null` placeholder.

Known limitations
- Library tab lists read sources only; unread sources are in Coverage and open as catalogue-only cards.
- Filter chip counts are totals over read sources, not recomputed against other active filters.
- "Dated before 2023" requires a published-record or platform-timestamp date; self-reported dates are excluded.
- The markdown renderer is small: headings, lists, quotes, simple tables, bold, italic, links, `[id]` citations.
- Stars and last view live in localStorage only; the page works without it.
