# Cataloguing and report (one agent, lean)

Work economically: few tool calls. No WebSearch, no WebFetch, no sub-agents. Do not open source texts or individual records; everything you need is in one file.

## Context

The user asked for a library of **practical techniques for developing inner light or lights in the visual field**: light actually *seen*, eyes closed or open, as opposed to mind's-eye imagery. Practical guidance from traditions and first-person testimony; no academic framing. They are an experienced meditator with graduate training in philosophy and wide reading in comparative mysticism: explain no basics. Their central practical question: **which sources give a way to break through to first light for someone in whom it does not arise spontaneously, and which only develop light that has already appeared?** They also asked that physically induced light (afterimage, pressure, breath, sound, movement, darkness) count where the practice leads to light without the ongoing stimulus.

67 sources were read in depth, mostly from keyword-selected digests, so most records carry medium confidence. 64 more were gathered but not read.

## Input

`library/pack.md` (about 1,200 lines; read it in three or four Read calls using offset and limit). It holds every kept source condensed: mode, eyes, onset pathway with evidence, techniques, conditions, stages, cautions, a practice summary and paraphrased key passages, each under its id in square brackets. The last section lists unread sources.

## Output 1: `library/curation.json`

```json
{
  "families": [
    {"id": "darkness-gazing", "name": "Looking into the darkness behind closed eyes",
     "description": "Two or three sentences: what the practitioner does, and which traditions use it."}
  ],
  "items": {
    "<id>": {"tier": "A", "families": ["darkness-gazing"], "librarian_note": ""}
  }
}
```

- 8 to 12 **technique families**, defined by what the practitioner actually does, cutting across traditions. Let the material decide them.
- Every kept id gets a `tier` and one or more `families`. Tier `A` = explicit usable instruction or unusually detailed testimony about light that is seen; `B` = useful; `C` = context, marginal, or thin. Records marked low confidence, `keep_marginal`, or screen `pass_flagged` cannot be A. Use `librarian_note` only where something needs saying (a doubt, a duplicate edition, a caveat).
- Write this file before starting the report. Then run `python3 tools/il.py build --note "Curated"` and confirm it completes.

## Output 2: `library/gaps.md` (about 300 words)

Which traditions or families are thin; which have no induction-type source; what the digest-based reading left unconfirmed; the eight unread or uncatalogued sources most worth reading next and why.

## Output 3: `report/report.md` (2,700 to 3,000 words)

Organise by **what the practitioner does** (your families), not tradition by tradition.

1. **What is being claimed** (short): how the sources themselves mark light as seen rather than imagined, and where they blur it.
2. **The technique families:** for each significant one, what is done, under what conditions, what is reported, which traditions converge, the best two or three sources. Give concrete parameters where sources give them. Include one table comparing families (rows) on: traditions, eyes open or closed, whether induction is claimed, best sources.
3. **Breaking through versus developing:** the central section. What is offered to someone who sees nothing; how specific and credible; time scales; which sources say it cannot be forced or comes by grace or transmission. Keep this distinct from advice on stabilising light already present.
4. **Physical induction and stimulus independence:** which sources claim the light outlasts the stimulus and how the transition is said to happen; which report it does not.
5. **Once light appears:** stages, what to do with it, obstacles and fixes.
6. **Dissent and cautions:** traditions that say to ignore or refuse the light, and why; safety (eyes, sun, breath, darkness, sleep) stated plainly.
7. **Where to start:** three or four concrete protocols for a person who currently sees nothing, assembled strictly from catalogued sources and naming them; say which parts are well supported and which thin.
8. **Gaps and confidence.**

Rules:
- Cite by id in square brackets, e.g. `[snt-sawan-singh-spiritual-gems]`; several ids may share a bracket, comma-separated. Cite only ids that appear in the pack's kept sections. Every substantive claim carries a citation.
- Say what kind of evidence each claim rests on: a classical text prescribing, a teacher asserting, a practitioner reporting. Do not let one source carry a general claim. `pass_flagged` or low-confidence records may illustrate but not solely support a point.
- Do not harmonise. State convergence and conflict both.
- Paraphrase; no verbatim quotation (the pack holds paraphrases, not source text).
- No neuroscience, no academic framing. Plain prose under clear headings; no bullet-point walls. No em dashes.
- Add nothing from your own knowledge of these traditions: if it is not in the pack, it is not in the report.

Save the report after every two sections so a stop loses little.

Final reply under 120 words: number of families, tier counts, word count, and the report's three main findings in a sentence each.
