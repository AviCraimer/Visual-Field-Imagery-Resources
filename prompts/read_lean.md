# Reading agent instructions (lean pass)

This one file is all you need. Do not read BRIEF.md or other prompt files. Work economically: few tool calls, no exploration beyond what is described here. No WebSearch, no WebFetch, no sub-agents.

## The job

The user wants **practical techniques for developing inner light or lights in the visual field**: light actually *seen*, behind closed eyes or with eyes open, as opposed to mind's-eye imagery. Practical guidance from traditions and first-person testimony; no academic framing. The user is an expert practitioner-scholar.

For each source in your queue you read a **digest** (the passages of the saved text densest in light-and-seeing vocabulary, in the source's own words) and write one reading record. You did not gather these sources: the search agent's summary at the top of each digest is unverified.

## Inclusion test

**Keep** a source if it gives instructions, troubleshooting, or first-person reports about seen light together with what the person did. Also keep a tradition's warnings against seeking or trusting the light.
- Visualization counts only where the source says the image becomes *perceived* (`imaginal_crossing`).
- Physical induction (afterimage, eye pressure, breath, sound, movement, darkness, flicker) counts when the practice aims at or leads to light that persists or arises *without the ongoing stimulus*. Purely stimulus-bound: drop as `stimulus_bound_only`; unsure: `keep_marginal`.

**Drop** if: light is only metaphor or doctrine (`metaphorical_light`); imagery never leaves the mind's eye (`imaginal_only`); no practice or testimony (`no_practical_content`); academic analysis only (`academic_only`); psychedelic (`psychedelic_only`); spontaneous with no account of practice (`spontaneous_no_practice_context`); machine-written or content-farm (`ai_or_low_quality`); otherwise irrelevant (`off_topic`).

## The two questions that matter most

1. **Mode:** `perceptual` (seen in the visual field), `imaginal_crossing`, or `ambiguous`. Give the evidence.
2. **Onset pathway:** does the source give a way to *break through* for someone who sees nothing (`induction`), only a way to work with light that has already arisen (`development_only`), `both`, or `unclear`? Record what it says to the person who sees nothing, prerequisites, claimed time scales, and any statement that light cannot be forced or comes only by grace or transmission.

## Procedure

1. `python3 tools/il.py todo --stream <stream> --max-priority 1` lists your queue (run once per stream you were given).
2. Take sources **two at a time**: in one message Read both `data/<stream>/digests/<id>.md`; in the next message Write both `data/<stream>/readings/<id>.json`. Do not hold more than two unwritten.
3. If a digest plainly misses something you need (for example the onset question), you may run at most **two** targeted `grep -n -i -C 8 "<term>" data/<stream>/sources/<file> | head -120` lookups for that source. Otherwise work from the digest.
4. When the queue is empty: `python3 tools/il.py validate --stream <stream> --stage read`. Fix every ERROR on reading records (usually an anchor that is not verbatim: copy it again exactly from the digest, or remove the passage). Ignore warnings.
5. Write `data/<stream>/READ_DONE.md`, five lines: counts by verdict; best sources for induction; best for development; a disagreement worth noting; what was thin.
6. Final reply under 80 words.

## Record format

```json
{
  "id": "<id>", "stream": "<stream>",
  "verdict": "keep",
  "drop_reason": null, "drop_note": "",
  "relevance": 5, "practicality": 4,
  "text_read": "digest; plus grep for 'eyelid'",
  "mode": "perceptual",
  "mode_evidence": "How the source itself marks the light as seen.",
  "eyes": "closed",
  "onset_pathway": "both",
  "onset_evidence": "What it offers someone who sees nothing; prerequisites; time scale; cannot-be-forced statements.",
  "stimulus_independence": "not_applicable",
  "techniques": ["concentration_nonvisual"],
  "conditions": {"posture": "", "gaze_or_eye_position": "", "setting": "", "duration_and_schedule": "", "prerequisites": "", "other": ""},
  "phenomena": ["smoke_mist_cloud", "white"],
  "stages": [{"label": "source's own term", "description": "what is seen; what marks the transition"}],
  "what_to_do_with_light": "ignore / stabilise / merge / enlarge / examine / refuse, as the source says",
  "obstacles_and_fixes": ["..."],
  "cautions": ["the source's own warnings"],
  "safety_flags": [],
  "interpretation": "One or two sentences: what the source says the light is.",
  "practice_summary": "100 to 180 words. A plain how-to distilled from this source alone, faithful to it.",
  "key_passages": [
    {"locator": "chapter or section heading seen in the digest, and the source-line range, e.g. 'Ch. IV, source lines 1210-1240'",
     "about": "onset",
     "anchor": "ten to twenty words copied EXACTLY from the digest text",
     "paraphrase": "Faithful restatement.",
     "quote": "",
     "source_file": "sources/<file>.txt"}
  ],
  "cross_refs": [], "new_leads": [],
  "reader_confidence": "high", "confidence_note": ""
}
```

Rules:
- `verdict`: `keep`, `keep_marginal`, or `drop`. A dropped source needs only `id`, `stream`, `verdict`, `drop_reason`, and a one-sentence `drop_note`.
- `relevance`, `practicality`: 0 to 5 (practicality 5 = could be followed tomorrow; 1 = bare report).
- Allowed values. `eyes`: closed, open, both, unspecified. `stimulus_independence`: yes, no, unclear, not_applicable. `reader_confidence`: high, medium, low.
- `techniques` only from: concentration_nonvisual, concentration_visual_object, afterimage_retention, gazing_fixed_point, sky_or_space_gazing, light_source_gazing, darkness_exposure, eye_pressure_or_sense_closure, eye_position, breath_control, sound_or_mantra, movement, posture_or_body_lock, visualization_crossing, letter_or_symbol_contemplation, sleep_threshold, sensory_restriction, fasting_or_austerity, devotion_or_transmission, scrying_surface, flicker_or_device, attention_to_spontaneous_phenomena, energy_work, other.
- `safety_flags` only from: eye_pressure, sun_gazing, breath_retention, sleep_deprivation, prolonged_darkness, flicker_seizure_risk, fasting, transmission_required_by_tradition, tradition_warns_against_seeking.
- `phenomena`: free terms; prefer sparks_or_points, fireflies, stars, smoke_mist_cloud, mirage_shimmer, lamp_or_flame, moon_disc, sun_disc, lightning_flashes, colour_fields, white, gold_yellow, blue, red, green, violet, black_light, geometric_patterns, sphere_pearl_bindu, chains_or_strings, rainbow, figures_or_forms, all_pervading_light, light_in_the_room, body_or_objects_luminous.
- `key_passages`: two to five per kept source. `about` is one of onset, method, development, stages, mode, caution, testimony, interpretation. Try to include one for onset and one for mode.
- **Anchors** are checked by script against the saved text, word for word. Copy from the digest; do not correct OCR errors inside an anchor; avoid spanning a window break.
- `quote` (verbatim, up to about 200 words) may be filled **only** when the digest header says `Rights: public_domain`. Otherwise leave it empty and let the paraphrase carry the content.
- If the digest header says `Access: reader_extract_saved`, the text is a model's summary of a web page: say so in `confidence_note` and set confidence no higher than medium.
- Never invent a locator, quotation or claim. If the digest does not show it, say the source was read in digest and the point could not be confirmed.
- Do not harmonise: record what this source says, even where it contradicts others.
