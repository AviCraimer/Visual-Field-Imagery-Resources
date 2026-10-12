# Search agent instructions

You gather documents for **one stream**. You do not judge them in depth; a separate reading agent does that. Your job is breadth, accurate metadata, and getting the actual text onto disk.

## Steps

1. Read `BRIEF.md`. Run `python3 tools/il.py stream <stream>` and `python3 tools/il.py status --stream <stream>`. If candidates already exist, read `data/<stream>/search_log.md` and resume; do not repeat queries already logged.
2. Plan in your log: list the sub-areas of your stream and the leads you will chase, including leads of your own.
3. For each promising source:
   a. Confirm it exists and find the best openly available text.
   b. Save the text to `data/<stream>/sources/<id>.txt` (plain text; for large public-domain books save the whole book; for pages on websites you own, save the reader extract as the BRIEF describes; for in-copyright books save only freely offered excerpts). Establish how the source's date is known (BRIEF, "Dating and provenance"). If the relevant part is one chapter of a big file, also note where it is in `locator_hints`.
   c. Skim enough to write an honest summary and to check it passes the inclusion test at first glance.
   d. Write `data/<stream>/candidates/<id>.json` immediately.
   e. Append a line to `search_log.md`.
4. Aim for **15 to 25 candidates** covering the stream's sub-areas. Prefer: explicit step-by-step instruction; troubleshooting addressed to people who see nothing; first-person reports that say what the person did and for how long; the tradition's own warnings. Include at least a few sources of each type the stream offers (classical text, modern teacher, practitioner testimony).
5. Things found but out of scope go in `excluded_leads.md`, one line each with the reason.
6. Run `python3 tools/il.py validate --stream <stream> --stage search` and fix every error.
7. Write `data/<stream>/SEARCH_DONE.md`: counts by source type, sub-areas covered, sub-areas thin or missing, leads you could not obtain, tool problems.

## Candidate record

```json
{
  "id": "bud-pa-auk-knowing-and-seeing",
  "stream": "theravada-east-asian",
  "title": "Knowing and Seeing",
  "author": "Pa-Auk Tawya Sayadaw",
  "translator": null,
  "year": "1998 talks; 4th rev. ed. 2010",
  "edition_cited": "4th revised edition, free distribution PDF",
  "tradition": "Burmese Theravada, Pa Auk lineage",
  "language": "English",
  "source_type": "teacher_manual",
  "rights": "in_copyright",
  "access": "partial_saved",
  "url": "https://...",
  "alt_urls": [],
  "source_files": ["sources/bud-pa-auk-knowing-and-seeing.txt"],
  "seen_via": null,
  "locator_hints": ["Talk 1, section on the nimitta", "Q&A 1.3"],
  "summary": "80 to 150 words: what this source says about seen light and what it tells the practitioner to do.",
  "why_relevant": "One or two sentences against the inclusion test.",
  "expected_mode": "perceptual",
  "expected_onset_pathway": "both",
  "expected_techniques": ["concentration_nonvisual"],
  "priority": 1,
  "medium": "book_or_classical_text",
  "date_evidence": {"date": "2010", "class": "published_record", "basis": "edition statement on the title page of the PDF"},
  "author_identifiable": true,
  "author_basis": "",
  "found_via": "seed lead / query text",
  "notes": ""
}
```

- `priority`: 1 = must read, 2 = should read, 3 = read if time.
- `access`: `fulltext_saved`, `partial_saved`, `reader_extract_saved` (a WebFetch extract, see BRIEF), or `citation_only` (nothing readable: a link for the user to follow; it will not be read).
- **Websites you own.** No later agent can open them, so what you save is all the reading agent will have. Extract thoroughly: follow threads onto their later pages, and ask for specifics. Find pages with `WebSearch` restricted by `allowed_domains`, or by fetching the site's own index or search pages. Stay within 40 WebFetch calls; spend them on the richest pages.
- A page on a website you do not own cannot be read by anyone in this run. If it looks valuable, catalogue it as `citation_only` with `date_evidence.class: "undated"` and a summary limited to what the search result shows.
- `expected_*` fields are your first impression; `unknown` is allowed for the two `expected_` enum fields.
- `medium`, `date_evidence` and (for anything that is not a book or classical text) `author_identifiable` are required. Record what you find; do not skip a good source because it is recent or undated, since the screening step decides that. Do skip pages that read as content-farm or machine-written filler.
- Web search here returns no dates and cannot filter by date. Unless you own websites, expect the archives to supply your stream; use web search mainly to learn what exists and what it is called, then look for it in the archives.
