# Gap pass: find and read named leads

You both gather and read. Read `BRIEF.md` (tools, dating, rights), `prompts/search.md` (candidate record format) and `prompts/read_full.md` (reading procedure; it points you to `prompts/read_lean.md` for the record format). No sub-agents. No Tavily.

Web tools: you made your permission requests in your first action. Afterwards use WebSearch only if it worked then, and WebFetch only on hosts recorded as approved in your warm-up file; never on any other host, never retry a failed one. Prefer direct downloads (curl) from archive.org, Gutenberg, Sefaria, CCEL, Wikisource, GitHub; space requests and back off on HTTP 429.

For each lead in your list, in order:
1. Find the best free text. Save it under `data/<stream>/sources/<id>.txt` and write the candidate record (`"found_via": "gap pass 2"`, `"priority": 1`). For a large book, save it whole and note the relevant part in `locator_hints`.
2. Read it in its original language per `read_full.md` and write the reading record. Drop it with a reason if it fails the inclusion test.
3. If a lead cannot be obtained free, write a `citation_only` candidate with a summary of what it is and why it matters, so it appears in the library as a gap, and move on.
Finish one lead before starting the next. Budget: about 20 tool calls per lead; skip ahead rather than stall.

Finally run `python3 tools/il.py validate --stream <s>` for every stream you touched and fix all ERRORs. Reply in under 200 words: per lead, found or not, verdict, onset pathway, one line on what it adds.
