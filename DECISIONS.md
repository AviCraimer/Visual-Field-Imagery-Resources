# Decisions

Standing decisions for the run. Append new ones with a date and a one-line reason.

## Set by the user

- Scope is light actually seen, eyes closed or open; mind's-eye imagery is out unless the source says it crosses into perception.
- Practical guidance from traditions and modern testimony; no academic studies.
- Afterimages and other physical induction (light, sound, breathing, movement) are in when the practice leads to light perceived without the ongoing stimulus.
- Shamanic and indigenous traditions are their own stream.
- Reading agents assess whether a source gives a way to break through to first light or only develops light that arose on its own.
- The pipeline must survive being stopped; progress updates between stages; no pauses for approval.
- No Tavily searches (free account; 2026-10-10). AI-written content is filtered by a provenance screen after gathering and before deep reading.
- Sub-agents must never trigger a permission prompt. WebFetch prompts on every site, so no agent uses it.
- Built-in web search did not raise a permission prompt for the orchestrator (user confirmed 2026-10-10).
- Website access (user's plan, 2026-10-10): the search agents for whom a site is relevant request fetch and search permission in their first action, so the user approves everything at once and then leaves. Approval is per agent, so each site has exactly one owner. No Tavily at all.

## Set by the orchestrator (2026-10-10), open to change

- Discovery uses built-in web search (no date filter exists); texts come from archive.org, Gutenberg, Sefaria, CCEL, Wikisource and GitHub by direct download. The Wayback Machine was tested and is unreachable from this workspace.
- A twelfth stream, practitioner-forums, owns all eight forum sites, so forum approvals come from one agent. sacred-texts.com was left out: its public-domain texts come as full raw text from archive.org, which is better than the fetch tool's summary.
- Website pages are saved as reader extracts (the fetch tool returns a model's reading, not the page). Tested on a SuttaCentral thread: it returned post dates, handles, paraphrases and short verbatim phrases.
- An unanswered permission request is withdrawn after a wait and returns an error (observed with reddit.com), so a missed approval costs that site, not the run.
- Eleven streams became twelve.
- Provenance rule: dated 2022 or earlier passes; undated or later passes with a visible flag only when attributable to a named person or organisation predating 2023; otherwise not read. Flagged items cannot be tier A or sole support for a claim in the report.

- Eleven streams (see streams.json). Christian contemplative and Western esoteric were split because the combined stream was by far the largest.
- Psychedelic and plant-medicine induction is out; finds are logged in each stream's excluded_leads.md.
- Published sources only for Dzogchen and Bon; restricted texts are noted, not sought.
- In-copyright sources: locator, paraphrase and a short anchor phrase; no verbatim passages. Public-domain sources: verbatim passages allowed. No unauthorised full-book scans.
- Every key passage carries an anchor phrase checked mechanically against the saved text.
- Ethnographies may carry indigenous practitioners' testimony; academic works that translate primary instructions may serve as conduits.
- The UI developer starts alongside the reading stage, and the navigator is republished after each later stage.
- A fresh agent checks the report against the library before delivery.
- At most one gap-fill round.
- The final report is also written to the Esoteric Work project as a single doc.
