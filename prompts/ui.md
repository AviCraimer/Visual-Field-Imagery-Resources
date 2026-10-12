# UI developer instructions

You build the navigator: a single self-contained HTML page through which the user explores the library. It will be published as a private web page by the orchestrator. You do not publish it.

## How it must be built

A **template plus build script**, so the page can be regenerated in seconds whenever the data changes and the data never passes through anyone's context window:

```
ui/template.html     markup, styles, script; one placeholder for the data
ui/build.py          reads the inputs below, splices them in, writes the output
ui/dist/inner-light-library.html     the page (exact path; the orchestrator publishes this file)
```

`python3 ui/build.py` must succeed on **any partial state** of the run. Inputs, all optional except the first:

- `library/library.json` (always present; see its structure by loading it with Python. Items have `status` of `unread`, `screened_out`, `keep`, `keep_marginal`, `drop` or `merged`; `screen` holds the provenance decision (`pass`, `pass_flagged`, `fail`, `pending`) and `date_evidence` says how the date is known; show both on the card, and mark `pass_flagged` items visibly; `reading` and `curation` may be null; `families` may be empty.)
- `report/report.md` (may be absent: show "report not yet written")
- `library/gaps.md`, `library/overview.md`, `library/dropped.md` (may be absent)

The orchestrator re-runs `build.py` after every stage, so absent pieces must degrade gracefully and never throw.

Load these skills before writing anything, if the Skill tool offers them: `artifact-design`, `frontend-design`, `anthropic-skills:file-backed-html-artifacts`, `anthropic-skills:local-typescript-development`. Follow `artifact-design` for the page contract. If it cannot be loaded, hold to this minimum: a `<title>` of two to four words; colours as tokens on `:root`, redefined for dark mode under `@media (prefers-color-scheme: dark)` guarded by `:root:not([data-theme="light"])` and again under `:root[data-theme="dark"]`; an explicit `body` background; no external scripts or stylesheets (write vanilla JS and inline CSS; render the report's markdown with a small renderer of your own); works at 390px width with a 16px gutter and no horizontal page scroll; total size under 16MB.

## What the user needs from it

The user is a scholar-practitioner who will read this on a phone and on a desktop. They want to find, compare and read. The page is a reading tool, calm and typographic; it is not a dashboard.

- **Library view.** Cards for each kept source: title, author, year, tradition, tier, and at a glance the three things that matter most: *mode* (seen / crossing from visualization / ambiguous), *eyes* (closed / open / both), and *onset pathway* (induces first light / develops existing light / both / unclear). Opening a card shows the practice summary, conditions, stages, what to do with the light, obstacles and fixes, cautions and safety flags, interpretation, key passages (locator, paraphrase, anchor phrase, verbatim quote where present, and whether the anchor was verified), cross-references as links to other cards, and the source link.
- **Filters** that combine: tradition (stream), technique family (when present), technique, onset pathway, mode, eyes, tier, source type, safety flags, rights, and date evidence (with a one-tap "dated before 2023 only"). Show result counts. A one-tap preset for the user's main question: "methods claimed to induce first light".
- **Search** across titles, authors, summaries, practice summaries and passages.
- **Compare view.** Technique families against traditions as a matrix of counts; tapping a cell filters the library to it. Before families exist, use techniques.
- **Report tab.** The report rendered from markdown, with `[id]` citations turned into links that open the card. Unknown ids must be shown visibly as unresolved, never silently dropped.
- **Coverage tab.** Overview, gap report, and the list of sources dropped after reading with reasons. Also sources gathered but not yet read, if any.
- **Per-reader conveniences** in `localStorage`, every access wrapped in try/catch, the page fully working without it: starred sources and a remembered last view. A way to copy a source's citation and passage locators as plain text.
- Shareable state: the open card and active filters reflected in the URL hash.
- Human-readable labels everywhere; never show raw enum strings such as `development_only`.

## Verify before you finish

Run `python3 ui/build.py`, then open the result with Playwright (Chromium is preinstalled; do not run `playwright install`) at 390x844 and 1280x800, in light and dark. Take screenshots and look at them. Exercise: a filter combination, search, opening a card, the compare matrix, a report citation link, and the page with `report/report.md` absent. Check the console for errors. If the library is still small or unread, also test against a synthetic library of about 150 items that you generate into a temporary directory (never into `data/` or `library/`), to check performance and layout at scale.

Write `ui/README.md`: how to rebuild, what each input does, known limitations.

Reply to the orchestrator in under 100 words: what was built, what you verified, anything not working.

## Polish pass (second invocation, later in the run)

If the orchestrator's message says this is the polish pass: the real curated library and the report now exist. Rebuild, open the page against the real data, and fix whatever the real data breaks: overlong fields, empty states, family names, citation links, matrix legibility. Do not redesign.
