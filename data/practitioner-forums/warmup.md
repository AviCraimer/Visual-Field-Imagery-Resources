# Warmup: practitioner-forums (2026-10-11)

One line per call. "Off limits" means WebFetch must not be called on that host again in this task.

- WebSearch `site:dharmaoverground.org fire kasina log first lights` (standard): approved, WORKED (returned 10 results), but the `site:` operator was not honoured: zero results were from dharmaoverground.org (all unrelated fire/Buddhist news). WebSearch is usable; site-restriction is unreliable.
- WebFetch https://www.dharmaoverground.org/ : FAILED, CLIENT_ERROR at target ("There was an error while fetching"). No redirect reported. Off limits.
- WebFetch https://discourse.suttacentral.net/ : approved, WORKED (returned site description). Usable. No redirect.
- WebFetch https://www.dhammawheel.com/ : FAILED, CLIENT_ERROR at target. No redirect reported. Off limits.
- WebFetch https://buddhism.stackexchange.com/ : BLOCKED BY THE TOOL (SITE_BLOCKED). Off limits.
- WebFetch https://www.thedaobums.com/ : FAILED, CLIENT_ERROR at target. No redirect reported. Off limits.
- WebFetch https://www.astralpulse.com/ : FAILED, CLIENT_ERROR at target. No redirect reported. Off limits.
- WebFetch https://community.tulpa.info/ : FAILED, CLIENT_ERROR at target. No redirect reported. Off limits.
- WebFetch https://www.reddit.com/ : BLOCKED BY THE TOOL (SITE_BLOCKED). Off limits.

## Summary

- WebSearch: works.
- WebFetch-usable hosts: discourse.suttacentral.net only.
- Off limits for WebFetch: www.dharmaoverground.org, www.dhammawheel.com, buddhism.stackexchange.com, www.thedaobums.com, www.astralpulse.com, community.tulpa.info, www.reddit.com.
- No host redirected, so no extra host was fetched.
- None of the calls was declined by the user or timed out; the failures were target-side fetch errors (6 hosts, treated as off limits) and tool-level site blocks (2 hosts).
