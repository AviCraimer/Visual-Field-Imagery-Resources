# Reading agent instructions

You read in depth the sources a search agent gathered for **one stream**, decide what stays, and pinpoint the passages that matter. You did not gather these sources and should not trust the search agent's summary: open the text.

## Steps

1. Read `BRIEF.md`. Run `python3 tools/il.py stream <stream>`, then `python3 tools/il.py todo --stream <stream>` (add `--shard i/n` if the orchestrator gave you a shard). That list is your work queue, already ordered by priority. Sources with an existing reading record, and sources screened out on provenance, are not in it.
2. For each source in the queue:
   a. Read its candidate record and open its saved text. For long texts do **not** load the whole file: search it with grep or a short script for the vocabulary of light and seeing (light, luminous, radiance, bright, lamp, flame, spark, star, moon, sun, colour names, eyes, eyelids, darkness, gaze, vision, appear, plus the tradition's own terms in the original language), then read generously around each hit.
   b. If the saved text is missing or too thin, try to obtain more under the BRIEF's tool rules and save it alongside. If nothing can be had, drop with `not_accessible` unless a reliable secondary quotation exists (then record `seen_via`).
   c. Decide the verdict against the inclusion test.
   d. Write `data/<stream>/readings/<id>.json` immediately, then append one line to `read_log.md`.
3. If your reading turns up a clearly important source that is not in the stream, you may add it yourself: write its candidate record (with `"found_via": "reader"`), save its text, and read it. Limit: three such additions. Otherwise put it in `new_leads`.
4. Run `python3 tools/il.py validate --stream <stream> --stage read` and fix every error. Anchors that fail the mechanical check must be corrected or the passage removed.
5. When the queue is empty, write `data/<stream>/READ_DONE.md` (or `READ_DONE.shard<i>.md` if sharded): counts by verdict, the strongest sources for *induction*, the strongest for *development*, notable disagreements inside the stream, and what is missing.

## Reading record

```json
{
  "id": "bud-pa-auk-knowing-and-seeing",
  "stream": "theravada-east-asian",
  "verdict": "keep",
  "drop_reason": null,
  "drop_note": "",
  "relevance": 5,
  "practicality": 5,
  "text_read": "Talk 1 in full; Q&A sections 1 and 2; keyword search of the rest",
  "mode": "perceptual",
  "mode_evidence": "How the source itself marks the light as seen rather than imagined. Cite the passage.",
  "eyes": "closed",
  "onset_pathway": "both",
  "onset_evidence": "What the source offers someone who sees nothing; prerequisites; claimed time scale; whether it says light cannot be forced.",
  "stimulus_independence": "not_applicable",
  "techniques": ["concentration_nonvisual"],
  "conditions": {
    "posture": "", "gaze_or_eye_position": "", "setting": "", "duration_and_schedule": "",
    "prerequisites": "", "other": ""
  },
  "phenomena": ["smoke_mist_cloud", "white", "sphere_pearl_bindu"],
  "stages": [
    {"label": "source's own name for the stage", "description": "what is seen and what marks the transition"}
  ],
  "what_to_do_with_light": "Instructions once it appears: ignore, stabilise, merge with object, enlarge, examine, refuse.",
  "obstacles_and_fixes": ["light vanishes when looked at directly: return to the breath, do not chase"],
  "cautions": ["the source's own warnings"],
  "safety_flags": [],
  "interpretation": "One or two sentences: how the source explains what the light is.",
  "practice_summary": "100 to 200 words. A plain how-to distilled from this source alone, faithful to it, written so the user could try it. No material from elsewhere.",
  "key_passages": [
    {
      "locator": "Talk 1, 'The Nimitta', pp. 44-46 of the 4th ed. PDF",
      "about": "onset",
      "anchor": "eight to twenty-five words copied exactly from the saved text",
      "paraphrase": "Faithful restatement of the passage.",
      "quote": "",
      "source_file": "sources/bud-pa-auk-knowing-and-seeing.txt"
    }
  ],
  "cross_refs": ["other ids or named sources this one cites or resembles"],
  "new_leads": ["sources worth chasing that are not yet catalogued"],
  "reader_confidence": "high",
  "confidence_note": ""
}
```

Rules for the fields:

- `verdict`: `keep`, `keep_marginal` (borderline against the inclusion test, or relevant but thin), or `drop`. A dropped source still gets a record with `drop_reason` (from `vocab.json`) and a one-sentence `drop_note`; the other analytic fields may be left empty.
- `relevance` and `practicality`: 0 to 5. Practicality 5 means a person could follow it tomorrow; 1 means a bare report with no method.
- `key_passages`: one to six per kept source. `about` is one of `onset`, `method`, `development`, `stages`, `mode`, `caution`, `testimony`, `interpretation`. Always try to include a passage for `onset` and one for `mode`; if the source has nothing on either, say so in `onset_evidence` / `mode_evidence`.
- `quote` is filled only when the candidate's `rights` is `public_domain`. Otherwise it stays empty and the `paraphrase` carries the content.
- `stimulus_independence` applies to physically induced methods: does the source claim the light continues or later arises without the stimulus?
- `safety_flags` from `vocab.json`. Always flag eye pressure, sun gazing, long breath retention, sleep deprivation, prolonged darkness, flicker, and the tradition's own requirement of transmission or warning against seeking.
- If, on reading, a text shows clear marks of machine or content-farm writing that the screen missed, drop it as `ai_or_low_quality` and say what the marks were.
- Do not harmonise. If the source contradicts another tradition or itself, record what it says.
