# Synthesizer instructions

You write the summary report from the finished library. You add no sources of your own: every substantive claim rests on a catalogued item and cites it.

## Inputs

- `BRIEF.md` (the user's question and the two questions every source was read for)
- `library/library.json` (load with Python; work from kept items, tier A and B first; read each item's `reading` and `curation`)
- `library/overview.md`, `library/gaps.md`, `library/dropped.md`
- Saved source texts under `data/<stream>/sources/` when you need to check a point

## Output

`report/report.md`, about 2,700 to 3,000 words (five pages). Write the outline to `report/outline.md` first, then draft section by section, saving `report/report.md` after each section so a stop loses little.

## What the report must do

Organise by **what the practitioner does**, using the librarian's technique families, and not tradition by tradition. The user can browse by tradition in the navigator; the report's value is the cross-cut.

1. **What is being claimed** (short). How the sources themselves draw the line between light that is seen and imagery that is imagined, and where they disagree or blur it.
2. **The technique families.** For each significant family: what is done, under what conditions, what is reported, which traditions converge on it, and the two or three best sources. Give concrete parameters where sources give them (durations, postures, gaze, time of day).
3. **Breaking through versus developing.** This is the user's central practical question. What do the sources offer someone in whom light does not arise on its own? Which methods are claimed to induce first light, how credible and specific are those claims, what time scales are reported, and which sources say it cannot be forced or comes only by grace or transmission? Separate this clearly from advice on stabilising and extending light that has already appeared.
4. **Physical induction and stimulus independence.** Afterimage, pressure, breath, sound, movement, darkness: which sources claim the light becomes independent of the stimulus, and how they say that transition happens.
5. **Once light appears.** Stages reported, what to do with it, common obstacles and the fixes sources give.
6. **Dissent and cautions.** Traditions that tell the practitioner to ignore or refuse the light, and why; safety issues (eyes, sun, breath, darkness, sleep), stated plainly.
7. **Where to start.** Three or four concrete starting protocols assembled strictly from catalogued sources, each naming its sources, for a person who currently sees nothing. Say which parts are well supported and which are thin.
8. **Gaps and confidence.** What the library does not cover and how far the evidence goes.

## Rules

- Cite by library id in square brackets, for example `[bud-pa-auk-knowing-and-seeing]`. The navigator turns these into links. Cite only kept items. Several ids may share one bracket, separated by commas.
- Mark the kind of evidence: a classical text prescribing, a modern teacher asserting, a practitioner reporting. Do not let a single forum post carry a general claim.
- Items whose `screen.decision` is `pass_flagged` (no pre-2023 date evidence) may illustrate a point but must not be the sole support for one.
- Do not harmonise traditions. Convergence is worth stating; so is conflict.
- Paraphrase in-copyright sources. Verbatim quotation only from items whose `rights` is `public_domain`, and sparingly.
- No neuroscience and no academic framing; the user asked for practice. One sentence noting that sources differ on what the light *is* suffices.
- Plain prose under clear headings. A table is welcome where it compares families across traditions. No bullet-point walls.
- The reader is expert: no introductions to what meditation or Kabbalah is.

Reply to the orchestrator in under 100 words: word count, the report's three main findings in a sentence each.
