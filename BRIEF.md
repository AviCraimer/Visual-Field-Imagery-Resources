# Inner light research run: shared brief

Every agent in this run reads this file first. Working directory: `/home/claude/inner-light`.

## What the user asked for

A catalogued library of **practical techniques for developing inner light, or lights in the external visual field**: light that is actually *seen*, behind closed eyes or with eyes open, as opposed to imagery held in the mind's eye. They want practical guidance from spiritual traditions and modern first-person testimony. They do not want academic studies.

The reader is an experienced meditator with graduate training in philosophy and wide reading in comparative mysticism. They already know kasina and nimitta basics and the distinction between mind's-eye imagery and imagery that appears in perceptual space (they call the latter "prophantasia"). Do not explain basics. Be exact about what a source says and how sure you are.

## Inclusion test

**In:** instructions, troubleshooting advice, or first-person reports about light seen in the closed-eye field or the open-eye visual field, together with what the person did.

- **Visualization** counts only where the source says or shows the image becoming *perceived* (tag `imaginal_crossing`).
- **Physical induction** counts when the practice aims at, or leads to, light that persists or arises *without the ongoing physical stimulus*. This covers afterimages from flame, lamp or sun; eye pressure and sense closure; breath; sound; movement; darkness; flicker. A method whose effect exists only while the stimulus is applied, with no claimed development beyond it, is out (`stimulus_bound_only`). If you cannot tell, keep it as `keep_marginal` and say why.
- **Warnings count.** A tradition telling practitioners to ignore, refuse or distrust the light is practical guidance, and the report needs the dissent.

**Out:**
- Psychedelic or plant-medicine induced light. Do not catalogue; add one line to `data/<stream>/excluded_leads.md`.
- "Light" used only as metaphor or doctrine, with no practice and no report of seeing.
- Academic studies as catalogue items. An academic work that translates or quotes primary instructions or testimony at length may be used as a `secondary_conduit`: catalogue the primary source it carries and record the conduit in `seen_via`. Academic works may always be mined for leads.
- Spontaneous or near-death light with no account of what the person was practising.
- AI-generated or content-farm pages.

## The two questions every source is read for

1. **Mode.** Is the light `perceptual` (seen in the visual field), `imaginal_crossing` (a deliberate image the source says becomes seen), or `ambiguous`? Give the evidence.
2. **Onset pathway.** Does the source give a way to *break through* for someone who sees nothing, or only a way to *develop* light that has already appeared on its own?
   - `induction`: describes steps that are claimed to produce first light in someone who had none.
   - `development_only`: assumes light has arisen (spontaneously or as a by-product) and says what to do with it.
   - `both`: does both; say which parts are which.
   - `unclear`: cannot tell from the text.
   Record what the source says to the person who sees nothing, any prerequisites, and any claimed time scale. If the source says first light cannot be forced, or comes only by grace or transmission, that is an important finding: record it.

## Tools and sources

The user approves permissions during the first minutes of the gathering stage and then leaves. A permission request raised later goes unanswered and clogs the run. So the rules are strict.

**Every agent, every stage**

- **Direct download from bash (curl or python requests), these domains only:** archive.org, www.gutenberg.org, *.wikisource.org, *.wikipedia.org, www.ccel.org, *.sefaria.org, www.mechon-mamre.org, github.com, raw.githubusercontent.com. Other domains are blocked from bash; do not retry them. `web.archive.org` (the Wayback Machine) does not work from this network; do not try it.
  - archive.org search: `advancedsearch.php?q=...&fl[]=identifier&fl[]=title&fl[]=year&rows=10&output=json`. Full text: `https://archive.org/download/<identifier>/<identifier>_djvu.txt` (file names are listed at `https://archive.org/metadata/<identifier>`, which also gives the publication year). Space requests a second or two apart; back off on HTTP 429.
  - Sefaria: `https://www.sefaria.org/api/texts/<Ref>?context=0` (e.g. `Zohar%2C_Shemot.1`), and `POST https://www.sefaria.org/api/search-wrapper` for search.
  - GitHub hosts some corpora as plain files, for example SuttaCentral's translations (`suttacentral/bilara-data`).
  - Wikisource's API is rate-limiting this network; prefer archive.org and Gutenberg.
- Never use any Tavily tool. Do not spawn further agents.
- If a tool is unavailable, write the fact in your log and carry on with what works. Never substitute a guess for a source you could not open.

**Search agents only (gathering stage)**

- `WebSearch` (mode `standard`) for discovery. It returns titles and links only, with no dates. Use `allowed_domains` to search inside one of your sites.
- `WebFetch`, **only on the hosts your kickoff message lists as yours, and only those your warm-up found approved.** Each website in this run has exactly one owning agent, because the user's approval applies to one agent at a time. Your first action, set out in your kickoff message, requests every permission at once while the user is watching. After that:
  - never call WebFetch on a host that is not on your approved list, including a host a page redirects to;
  - never retry a host that was declined, timed out or blocked (a retry raises a new request after the user has left);
  - at most 40 WebFetch calls in your whole task; log each one.
- WebFetch does not return the page. It returns a small model's answer to your prompt about the page. So ask for what the record needs, in one call per page:
  > "I am cataloguing practical instructions and first-person reports about light seen in meditation (eyes closed or open). From this page give: (1) title, author or poster handles, and every date shown (first and last post dates for a thread; publication or revision date for an article), exactly as printed; (2) for each passage that gives instructions, troubleshooting, or a first-person report about seen light: where it is on the page (heading or post number, author, date), a detailed faithful paraphrase keeping all specifics such as durations, postures, gaze, sequence and what was seen, and one exact phrase of 10 to 20 words copied verbatim in quotation marks; (3) whether the page continues on a further page, and that page's URL."
  Save the answer as `data/<stream>/sources/<id>.txt` under a three-line header: the URL, the fetch date, and the line `READER EXTRACT via WebFetch: a model's reading of the page, not the page's own text.` Set `access: "reader_extract_saved"`. For long threads fetch the following pages too (use the next-page URL, or the `offset` parameter) and append.
- A site that the fetch tool itself refuses (`SITE_BLOCKED` or similar) is off limits: log it once and do not look for another route to it.

**Reading, screening, cataloguing and later agents**

- No WebSearch and no WebFetch. You work from what is on disk plus direct downloads from the archive domains above. A source saved as a reader extract cannot be re-fetched: read the extract, take anchors from the verbatim phrases it contains, and say in `confidence_note` that the reading rests on an extract.

## Dating and provenance

The user wants AI-written material kept out. Content that demonstrably existed before 2023 is safe; everything else needs a reason to be trusted. So every candidate records how its date is known:

```json
"medium": "web_article",
"date_evidence": {"date": "2020-06-08", "class": "self_reported", "basis": "date printed under the title; no other date on the page"},
"author_identifiable": true,
"author_basis": "Signed answer by a named minister on the organisation's own site"
```

- `published_record`: a book or text with a publication record (archive.org or library metadata, Gutenberg, Sefaria, a known edition). Give the year of the edition you used. Strong.
- `platform_timestamp`: a forum or Q&A post stamped by the platform. Strong. For a thread give the first post's date and say in `basis` the range the posts span.
- `self_reported`: a date printed on the page by its author or site. Acceptable.
- `post_2022`: dated 2023 or later.
- `undated`: no date found. Say in `basis` what you looked for.

`basis` must state exactly what the date rests on. Never infer a date from how old a page looks. `author_identifiable` is true only when the text is attributable to a named person or organisation with a presence that predates 2023; a pseudonymous forum account does not count. A screening step after the gathering stage passes sources dated 2022 or earlier, and decides the rest on authorship; sources that fail are not read.

## Rights and quoting

- Record `rights` for each source: `public_domain` (published before 1929, or explicitly so), `in_copyright`, or `unknown` (treat as in copyright).
- **Public-domain sources:** save the full text; verbatim passages may be recorded in `quote` (up to about 250 words each).
- **In-copyright sources (including free-distribution books and forum posts):** do not download unauthorised scans of whole books. Save only what the author or publisher makes freely available. Record passages as a precise `locator`, a faithful `paraphrase`, and an `anchor`: a short verbatim phrase of 8 to 25 words that lets the user find the spot in their own copy. Leave `quote` empty.
- Every passage needs an `anchor` that appears verbatim in the saved source file. A script checks this mechanically.

## Honesty rules

- Never invent a citation, page number, chapter number or quotation. A locator must be something you saw in the text you opened.
- If you saw a passage only as quoted in another work, say so in `seen_via` and cite both.
- The seed leads in `streams.json` are unverified pointers from memory. Some will be wrong.
- Uncertainty goes in the record (`reader_confidence`, `notes`), not left out.

## Write as you go

The run may be stopped at any moment. Work must survive that.

- **One file per source, written the moment that source is done.** Never hold several finished records in memory.
- Append to your log after every few actions.
- Before starting, check what already exists. If records are present you are resuming: skip them and continue.
- Write your `*_DONE.md` marker only when the stage is complete for your stream.

## Layout

```
data/<stream>/candidates/<id>.json    search agent: one per source
data/<stream>/sources/<id>*.txt       saved text for that source
data/<stream>/readings/<id>.json      reading agent: one per source
data/<stream>/search_log.md           append-only: queries run, what they yielded
data/<stream>/read_log.md             append-only
data/<stream>/excluded_leads.md       one line each: found but out of scope
data/<stream>/SEARCH_DONE.md          marker plus coverage summary
data/<stream>/READ_DONE.md            marker plus summary
```

`id` = `<prefix>-<short-slug>`, lowercase, hyphens, for example `bud-pa-auk-knowing-and-seeing`. The prefix for each stream is in `streams.json`. Allowed values for every enumerated field are in `vocab.json`.

Helper commands (run from the working directory):

```
python3 tools/il.py stream <stream>                 # your stream's scope and leads
python3 tools/il.py status --stream <stream>        # what exists so far
python3 tools/il.py todo --stream <stream> [--shard i/n]   # sources still to read
python3 tools/il.py validate --stream <stream>      # schema check; fix every error
```

## Your final message

Reply to the orchestrator in under 120 words: counts, the two or three strongest finds, anything that went wrong. Everything else belongs in the files.
