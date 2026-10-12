# Visual Field Imagery Resources

A cross-tradition library of practical sources on developing **visual field imagery (VFI)**: light or form that appears in the visual field, behind closed lids or before open eyes, as distinct from **mind's eye imagery (MEI)**. Both terms are neutral on whether the imagery is willed or spontaneous, and on whether it is fantasy or true perception.

## What is here

| Path | Contents |
|---|---|
| `report/report.md` | The synthesis report: technique families, breaking through versus developing, physical induction, cautions, starting protocols. |
| `index.html` | The navigator, served by GitHub Pages: browse, filter and search the library. Also at `ui/dist/visual-field-imagery-library.html`. |
| `library/CATALOGUE.md` | Readable catalogue of every source with practice summaries and key passages. |
| `library/library.json` | The full built library (all records, curation, families). |
| `library/curation.json`, `library/gaps.md` | Tiers, technique families, and the gap report. |
| `data/<stream>/candidates/` | One metadata record per source (12 streams by tradition). |
| `data/<stream>/readings/` | One reading record per source read: mode (VFI / MEI), eyes, onset pathway, techniques, stages, cautions, key passages with locators. |
| `data/<stream>/sources/` | Saved texts, **public-domain sources only**. In-copyright texts are withheld; their records keep locators and short anchor phrases so the passages can be found in your own copy. |
| `tools/il.py` | Bookkeeping: validate records, build the library, check anchors against saved texts. |
| `tools/digest.py`, `tools/pack.py` | Digest and condensed-pack builders used by the reading agents. |
| `ui/template.html`, `ui/build.py` | Navigator template and build script. |
| `BRIEF.md`, `prompts/`, `streams.json`, `vocab.json` | The research brief, agent instructions, stream definitions and controlled vocabulary. |

## Rebuilding

```
python3 tools/il.py build        # rebuild library/library.json and CATALOGUE.md
python3 ui/build.py              # rebuild the navigator
python3 tools/make_index.py      # refresh index.html (GitHub Pages) from the navigator
python3 tools/il.py validate --stream <stream>
```

Paths inside the tools still use the working name `inner-light`; this does not affect the output.

## Notes

- Most records were read from keyword digests or in full in the original language (Arabic, Persian, Chinese, Hebrew, Aramaic, Sanskrit, German, French, Greek, Latin, Russian, Spanish); each reading record states what was read and its confidence.
- Records are scholarly notes, not endorsements of any practice. Several practices described (sun gazing, eye pressure, breath retention, prolonged darkness, fasting) carry real risks, flagged in the records and the report.
