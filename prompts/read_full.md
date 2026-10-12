# Reading agent instructions (full-text pass, one or two sources)

First read `prompts/read_lean.md` for the job, the inclusion test, the two questions, the record format and its rules. Its **Procedure** section does not apply to you. There is no digest: you read the saved source text itself, in its original language. No WebSearch, no WebFetch, no sub-agents.

## Procedure

1. Read the candidate record `data/<stream>/candidates/<id>.json` (summary and locator hints are the search agent's, unverified; `source_files` are relative to `data/<stream>/`).
2. Read the text.
   - Under about 150 KB: read the whole file in a few large Read calls.
   - Larger: find the table of contents or chapter headings first, then search in the **source's own language** for the vocabulary of light and seeing (for example Arabic نور، أنوار، ضوء، لون، عين، خلوة، ظلمة; Persian نور، روشن، رنگ، چشم; Chinese 光、明、白、目、眼、日、月、見; Hebrew אור، עין، גוון; German Licht, hell, leuchtend, Farbe, Auge, dunkel; French lumière, lueur, couleur, yeux) and for the candidate's locator hints, and read the relevant chapters generously, whole chapters where they are on topic. Do not stop at the first hit: the onset question (what the source offers someone who sees nothing) and the mode question both need an answer or an explicit "not addressed".
   - Aim for under 30 tool calls per source.
3. Write `data/<stream>/readings/<id>.json` in the record format from `read_lean.md`. If a record already exists you are replacing a weaker earlier reading: overwrite it.
   - `text_read`: say exactly which parts you read in full.
   - Read non-English sources in the original. Give paraphrases in English, with key technical terms in the original script in brackets.
   - Anchors must be copied exactly from the saved file, in the original language and with any OCR garbling left as it is. Where OCR noise makes a reading uncertain, say so in the paraphrase.
   - `quote` only for public-domain sources; it may be in the original language (then put the English sense in `paraphrase`).
   - An academic work is a conduit: record which primary text each passage carries.
   - Up to six key passages. Set `reader_confidence` honestly; a full reading of the relevant chapters can be `high`.
4. Run `python3 tools/il.py validate --stream <stream> --stage read` and fix every ERROR on your record(s).
5. Final reply under 100 words: verdict, onset pathway, the single most useful thing the source says, anything unresolved.
