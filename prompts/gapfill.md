# Gap-fill agent instructions

One extra pass on specific leads the librarian identified. You both gather and read. The user is away: no WebSearch and no WebFetch, whatever `prompts/search.md` says about websites; archive downloads only.

Read `BRIEF.md`, `prompts/search.md` and `prompts/read.md`. The orchestrator's message names your stream and lists the leads. For each lead: find the source, save its text, write the candidate record (`"found_via": "gapfill"`), then read it and write the reading record, exactly as those two instruction files describe. One source at a time, written before starting the next. If a lead cannot be obtained, add a line to `data/<stream>/excluded_leads.md` saying so.

Finish with `python3 tools/il.py validate --stream <stream>` and fix every error. Reply in under 80 words.
