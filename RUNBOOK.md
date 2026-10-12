# Runbook for the orchestrator

For Claude, running or resuming this job. Everything needed to continue is on disk; the conversation is not required.

## Principles

- All state lives in files under `/home/claude/inner-light`. Agents write one record per source as they go. Nothing important exists only in an agent's reply or in this conversation.
- `python3 tools/il.py status` shows where the run stands, at any time.
- `python3 tools/il.py build` produces a usable library and catalogue from whatever exists, at any time.
- The user is away. Do not stop to ask. Decide, record the decision in `DECISIONS.md`, carry on. The one exception is anything irreversible outside this workspace, and nothing in this run is.
- Keep the orchestrator's context small: never read source texts or whole record sets; use the tool's summaries and the agents' short replies.

## Kickoff prompts

Generate every agent's prompt with the tool and pass its output verbatim; do not write prompts by hand. Use `subagent_type: "general-purpose"`.

```
python3 tools/il.py kickoff --stage search --stream <stream>                 # user present: includes the permission warm-up
python3 tools/il.py kickoff --stage search --stream <stream> --resume-away   # relaunch while the user is away: no web tools
python3 tools/il.py kickoff --stage read --stream <stream> [--shard i/n]
python3 tools/il.py kickoff --stage <provenance|librarian|gapfill|synthesizer|reportcheck|ui|ui-polish>
```
For gap-fill, append the stream and the list of leads.

## Permissions: the one thing that needs the user

The user's approval of a website applies to a single agent, and a request raised when they are away goes unanswered (it is withdrawn after a wait and returns an error). So:

- Each website has exactly one owning search agent (`python3 tools/il.py sites`). Each search agent's kickoff prompt makes it request all its permissions in its very first action.
- Only the first launch of the search agents may use WebFetch or WebSearch. Every relaunch, and every later stage, uses no web tools. The orchestrator itself makes no WebFetch calls during the run.
- Immediately before launching the search agents, send the user (SendUserMessage): "Launching now. About 19 website approvals plus possibly one search approval per agent will appear over the next two or three minutes; choose 'always allow' on each. Once they stop, you can leave. Anything left unanswered is skipped, not retried."

## Stages

Set up the task list at the start (Gather sources, Screen provenance, Deep reading, Catalogue, Report and navigator, Final check). At every stage boundary: run status, build, snapshot; send the progress update with `SendUserMessage`; send files with `SendUserFile`.

### 0. Preflight (orchestrator, under a minute, no agents)
```
python3 tools/il.py status && python3 tools/il.py sites
curl -s -m 30 -o /dev/null -w "%{http_code}\n" "https://archive.org/advancedsearch.php?q=title%3A%28candle+of+vision%29&fl%5B%5D=identifier&rows=1&output=json"
curl -s -m 30 -o /dev/null -w "%{http_code}\n" "https://www.sefaria.org/api/texts/Zohar%2C_Shemot.1?context=0"
```
If the archives are unreachable, stop and tell the user: the run depends on them.

### 1. Gather (12 search agents, one message, in parallel)
Send the permissions message above, then launch all twelve at once so the approval requests arrive together.

After they return:
```
python3 tools/il.py status --write
cat data/*/warmup.md          # which sites were approved, declined, timed out or blocked
for each stream without SEARCH_DONE.md or with fewer than 8 candidates: relaunch once with --resume-away
python3 tools/il.py screen          # rule pass; prints sources pending a provenance decision
```
**Provenance screen** (the user's AI-content filter, placed here at their request): if anything is pending, launch one provenance agent; if more than 60 are pending, two agents, telling one to take streams in the first half of the status table and the other the rest. Then:
```
python3 tools/il.py screen          # confirm nothing pending; anything still pending is read but flagged
python3 tools/il.py build --note "Stage 1: sources gathered and screened, not yet read"
python3 tools/il.py snapshot --label stage1
```
Send: `library/CATALOGUE.md` and the records snapshot (and the sources snapshot if under 25 MB). Progress update 1, including which websites could not be used and how many sources were screened out.

### 2. Deep reading (reading agents plus the UI developer, one message, in parallel)
- One reading agent per stream; if a stream has more than 14 readable candidates (see `todo`), two agents with `--shard 0/2` and `--shard 1/2`.
- At most 12 agents per message; run reading in two waves if there are more, with the UI developer in the first wave.
- The UI developer starts now (`prompts/ui.md`), since it needs only the record structure. This puts a working navigator in the user's hands a stage earlier.

After they return:
```
python3 tools/il.py status --write
relaunch once any reading agent whose stream still has unread sources (python3 tools/il.py todo --stream <s>)
for each stream: python3 tools/il.py validate --stream <s>     (note error counts; the librarian handles leftovers)
python3 tools/il.py build --note "Stage 2: read and filtered, not yet curated"
python3 ui/build.py
python3 tools/il.py snapshot --label stage2
```
Load the `artifact-design` skill, read `ui/dist/inner-light-library.html`, then publish it with the Artifact tool (icon: `library`). Keep the same file path for every later publish so the URL stays the same. Send the records snapshot. Progress update 2.

### 3. Catalogue (one librarian)
After it returns: build with `--note "Stage 3: curated"`. Read `library/gaps.md`.
- **Gap-fill, at most once:** if the gap report names concrete, obtainable leads that matter to the user's question (above all: a tradition with no induction-type source where one plausibly exists), launch up to 4 gap-fill agents in parallel, one stream each, with the named leads. Then relaunch the librarian once with "New items were added by gap-fill; curate only items missing from curation.json and update gaps.md". After this, move on regardless.
- Rebuild, rebuild UI, republish, snapshot `stage3`. Progress update 3.

### 4. Report and navigator
- One message: synthesizer, and the UI polish pass in parallel.
- Then the report checker (`prompts/reportcheck.md`), a fresh agent.
- Then: `python3 tools/il.py build --note "Final"`, `python3 ui/build.py`.
- Own check: confirm in the built page that every report citation resolves (grep the report for `[id]`s and test membership in library.json with a short script); open the page with Playwright at phone width, screenshot, look.
- Republish the navigator. Send `report/report.md`. Snapshot `final` and send the records snapshot.
- Write the report into the attached project with `Projects.project_write` as one new doc (a single write; name it by the project's convention: `October_DD_2026__Inner_Light_Techniques__Cross_Tradition_Survey__Induction_vs_Development.md`).
- Final message: what came out of it, in a few sentences; the navigator card; one next step.

## Progress updates

Sent with `SendUserMessage` at each boundary. Short, concrete, no narration of mechanics. Template:

> **Stage N of 4 done: <name>.** <one sentence of result with numbers>.
> <2 to 4 bullets: the most interesting concrete finds so far, named>
> <one line: anything that went wrong or was decided>
> Next: <stage>.

Include the status table only in the first update.

## Failure handling

- If any orchestrator action is refused or waits on an approval that does not come (publishing the navigator, writing to the project): do not retry in a loop. Send the file with `SendUserFile` instead, note it in the progress update, and carry on.

- An agent that errors or returns without finishing: relaunch **once** (search agents with `--resume-away`); it resumes from its files. If it fails again, continue without it and say so in the next update.
- Rate limiting on parallel launches: halve the wave size and continue.
- Never rerun a completed stage. Never delete records.

## Resuming after a stop

1. `cd /home/claude/inner-light && python3 tools/il.py status`.
2. If the directory is gone (the container was reclaimed): ask the user to attach the latest `inner-light-records-*.tar.gz` and, if they have it, `inner-light-sources-*.tar.gz`; extract both in `/home/claude`. Without the sources archive, reading agents re-download archive texts from the URLs in the candidate records (reader extracts of websites cannot be re-fetched while the user is away; those sources are then read from their candidate summaries only and marked low confidence).
3. Find the stage from the table: streams "not started" or "partial" under Search mean stage 1 is unfinished, and so on down the list in the status output. Relaunch only what is missing. Agents skip finished records by design.
4. Send a one-line update saying where the run resumed.

## Decisions already made

See `DECISIONS.md`.
