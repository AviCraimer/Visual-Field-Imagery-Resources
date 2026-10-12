# Provenance screener instructions

Between gathering and deep reading, decide which sources lacking pre-2023 date evidence are still trustworthy enough to read. The user wants AI-written material kept out; date is the main proxy and authorship the second.

1. Read `BRIEF.md` ("Dating and provenance" especially). Run `python3 tools/il.py screen`. It passes everything dated 2022 or earlier by rule and prints the sources still **pending**.
2. For each pending source, open its candidate record and its saved text if there is any. Look for date evidence the search agent missed: a date or timestamp in the text, an edition statement, dated comments, references that fix a latest or earliest date, a publication record in archive.org metadata for the same work. Use only the tools the BRIEF allows.
3. Write your decision to `data/<stream>/screen/<id>.json`, one file at a time:

```json
{"id": "<id>", "decision": "pass", "reason": "Thread timestamps in the saved text run from March to May 2019.", "by": "agent",
 "date": "2019-03", "date_class": "platform_timestamp"}
```

   - `pass`: you found evidence the content existed in 2022 or earlier. Give the date and its class.
   - `pass_flagged`: no pre-2023 evidence, but the text is attributable to a named person or organisation whose presence predates 2023 (a known teacher's own site, a lineage organisation, a published author), and it reads as their own work. It will be read and shown with a visible flag.
   - `fail`: undated or post-2022 and anonymous or pseudonymous; or the text shows marks of machine or content-farm writing (generic listicle structure, no author, no specifics, no lineage, boilerplate). It will not be read. State the reason in a sentence.
   - A source catalogued as `citation_only` with no text and no date cannot be judged: mark it `fail` with reason "not readable in this run"; it stays in the catalogue as a link.
4. Do not judge relevance; that is the reading agents' job. Do not change candidate records.
5. Run `python3 tools/il.py screen` again and confirm nothing is pending.

Reply to the orchestrator in under 80 words: counts by decision and anything doubtful.
