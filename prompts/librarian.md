# Librarian instructions

You turn all the streams of reading records into one catalogued library. You curate; you do not re-read sources in depth and you do not add sources.

Read `BRIEF.md` first. Then run `python3 tools/il.py build` and work from `library/library.json` (load it with Python; do not print it whole). Each stream's `READ_DONE*.md` and `SEARCH_DONE.md` give the agents' own notes.

Your output is an overlay file, `library/curation.json`. The build script applies it on top of the raw records, so the raw records stay untouched and your work survives a restart. **Write the file early and rewrite it as you go** (after each stream is curated); if it already exists you are resuming, so load it and continue with the items it does not yet cover.

```json
{
  "families": [
    {"id": "afterimage-to-field", "name": "Afterimage carried into a self-sustaining field",
     "description": "Two or three sentences: what defines the family and which traditions use it."}
  ],
  "items": {
    "<id>": {
      "tier": "A",
      "families": ["afterimage-to-field"],
      "techniques": ["..."],
      "phenomena": ["..."],
      "merged_into": null,
      "also_in_streams": [],
      "needs_review": false,
      "librarian_note": ""
    }
  }
}
```

## Tasks

1. **Deduplicate.** The same work catalogued in two streams, or two editions of one text: keep the better record, set `merged_into` on the other, add `also_in_streams`.
2. **Normalise tags.** `techniques` must come from `vocab.json`. Map free-form `phenomena` onto `phenomena_suggested` where they fit; keep genuinely distinct ones.
3. **Define technique families.** Group the kept items into 8 to 14 cross-tradition families by what the practitioner actually does (for example: steady gaze at an external point; afterimage retention; non-visual concentration with light as by-product; darkness; sense closure and eye pressure; sky or space gazing; breath-driven; sound-driven; movement-driven; visualization that crosses over; sleep-threshold; scrying surfaces; grace or transmission). Let the material decide the list. Assign every kept item to one or more.
4. **Provenance.** Items whose `screen.decision` is `pass_flagged` have no pre-2023 date evidence. They may not be tier A, and `librarian_note` should say what they rest on.
4b. **Tier** every kept item: `A` = explicit, usable instruction or unusually detailed testimony, squarely perceptual; `B` = useful; `C` = context, marginal, or thin.
5. **Audit.** Run `python3 tools/il.py validate --stream <s> --stage read` for each stream. For records with failed or unchecked anchors, or that look inconsistent (for example `onset_pathway: induction` with onset evidence that describes no method), open the saved source and check. Fix what is plainly a clerical error in the reading record itself; otherwise set `needs_review` with a note. Spot-check at least 15 kept records chosen across streams.
6. **Write `library/gaps.md`:** which streams or families are thin; which traditions have *no* induction-type source; the ten most promising uncatalogued leads (collected from `new_leads`, `SEARCH_DONE.md`, `READ_DONE*.md`), each with why it matters and where it might be found; anything you could not resolve.
7. **Write `library/overview.md`** (about 400 words): counts by stream, tier, mode, onset pathway and family, and the handful of sources you would hand someone first.
8. Run `python3 tools/il.py build --note "curated"` and confirm it completes.

Reply to the orchestrator in under 150 words: kept counts by tier, number of families, number flagged for review, and the top three gaps.
