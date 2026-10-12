# Search log: practitioner-forums

## 2026-10-11 session 1

Warm-up done (see warmup.md). WebSearch works (site: operator not honoured; will use allowed_domains). WebFetch works only on discourse.suttacentral.net. Seven of eight owned sites are off limits for WebFetch: DhO, Dhamma Wheel, Dao Bums, Astral Pulse, tulpa.info (target-side fetch errors), Buddhism SE and Reddit (SITE_BLOCKED by the tool).
WebFetch budget: 40 total; 8 spent in warm-up (counted conservatively); 32 left, all for discourse.suttacentral.net.

### Plan
Sub-areas and how each will be reached:
1. Theravada breath-nimitta / aloka-sanna threads with monastics answering: SuttaCentral Discourse via WebFetch (reader extracts). Main readable body of the stream.
2. Dharma Overground fire-kasina logs, nimitta threads: WebFetch failed. Discover titles via WebSearch (allowed_domains) -> citation_only records; look for any archive.org / GitHub copies.
3. Dhamma Wheel nimitta/kasina threads: same as 2.
4. Buddhism Stack Exchange: tool-blocked. citation_only from WebSearch. NOTE: an official SE data dump exists on archive.org, but BRIEF says a tool-blocked site is off limits and "do not look for another route to it", so the dump is NOT used. Flag for orchestrator.
5. Dao Bums (neigong first light, dark room, Golden Flower reports): WebFetch failed; citation_only + archive.org search for compiled PDFs.
6. Astral Pulse (closed-eyelid seeing, hypnagogic light): WebFetch failed; citation_only; archive.org for Usenet alt.out-of-body etc. (Usenet is a practice forum with Date headers = platform timestamps).
7. Tulpa imposition guides/logs: WebFetch failed; look on GitHub / archive.org for the community guides; citation_only otherwise.
8. Reddit (r/Prophantasia, r/CureAphantasia, r/streamentry, r/TheMindIlluminated, r/kundalini): tool-blocked; citation_only from WebSearch; no dump route.
9. Own lead: Usenet archives on archive.org (alt.meditation, alt.out-of-body, alt.yoga, alt.consciousness.*, talk.religion.buddhism) for pre-2010 first-person light reports.
10. Own lead: GitHub-hosted community guides (prophantasia, tulpa, lucid dreaming hypnagogia).

### Archive probe
- archive.org advancedsearch `usenet alt.out-of-body` -> item `usenet-alt.out-of-body` (Giganews Usenet captures, uploaded 2014). Checked sibling items: usenet-alt.meditation (incl. .qigong, .shabda, .quanyin, .transcendental), usenet-alt.yoga, usenet-alt.consciousness (.mysticism), usenet-alt.dreams, usenet-alt.religion (.buddhism.theravada, .eckankar), usenet-alt.philosophy (.taoism), usenet-alt.magick, usenet-alt.zen. Decision: Usenet practice newsgroups are pre-2015 practice forums with Date headers; mine them for first-person light threads. Downloading mbox.gz files to scratchpad.

### WebSearch discovery (allowed_domains)
- [discourse.suttacentral.net] "nimitta light appeared breath meditation what to do" -> A Cold Case? The Missing Mystery of The Breath Nimitta (t/26513, 2+ pages); Sensory deprivation, Nimitta and Jhana (t/12661, 2 pages); We perceived both light and a vision of forms (t/263, 2 pages); What nimitta in EBT means (t/6104); Does the Buddha ever mention Nimittas (t/26438); Vimuttimagga chapter on 16 APS (t/5932).
- [discourse.suttacentral.net] "perception of light aloka sanna practice how to see light eyes closed" -> What is meant by perception of light in DN 33 (t/22935); Aloka & Obhasa difference (t/33971); Did the Buddha instruct us to close the eyes (t/3766).
- [dharmaoverground.org] "fire kasina practice log" -> Siavash's Practice Log (msg 13519742); Anna's Fire Kasina Practice Log (7259611); Fire Kasina in daily life log (23362346); Basic questions about fire kasina (24756899); Basic Instructions for Practising Fire Kasina (6760422); Denman Island Fire Kasina FAQ Project (12257658); Papa Che's Fire Kasina Journal (19494476); New to Fire Kasina, Checking-In (22641761).
- [dharmaoverground.org] "nimitta not appearing no light after months of anapanasati" -> Help with nimitta (24189374); Question on Nimitta and Entry into first jhana (355026); Nimittas for Jhanas? (3806419); How to attain "hard" Jhana? (3710799); Malcolm's practice log (8334133).
- [dhammawheel.com] "nimitta light seeing light in meditation Pa Auk experience" -> Ajahn Brahmavamso's Dark Jhana (t=38577); Mistaking the Patibhaga Nimitta (t=42539); Deep Absorption in Gold and White Lights During Meditation (t=39644); Third Eye Meditation (t=32507); Pali Term: Nimitta (t=2770); What are your ideas about Pa Auk method (t=33660).
- [buddhism.stackexchange.com] "seeing light in meditation nimitta kasina" -> no links returned.
- [thedaobums.com] "seeing light upper dantian first time neigong dark room golden flower practice report" -> Upper dantian (topic 54252); Secret of the Golden Flower (7795, 12+ pages); Upper Dantian 101 (38351); Golden Flower beginner journey (49568); Signs of Verification of Turning Around the Light (47181).
- [astralpulse.com] "seeing through closed eyelids hypnagogic light third eye practice" -> Seeing through closed eyelids (forum t35592); Projection & Meditation: seeing through closed eyelids (2013/11/16 blog); Steps to open the third eye (t39899); printpage topic 34775.
- [tulpa.info] "visual imposition guide open eye progress" -> Method for imposing and open eye visuals (topic 11919); How to see your tulpa and distortions (4561); JD's Tulpa Method (1438); Implanting Guide; Potential easy path to visual imposition (16224); List of Guides (11498); Maxyp's Tips and Tricks (2454).
- [reddit.com] "prophantasia training guide autogogia closed eye visuals" -> WebSearch proxy rejected the request (HTTP 400). Reddit not searchable with allowed_domains.
- [discourse.suttacentral.net] "I see a bright white light when meditating what should I do nimitta experience"; "Ajahn Brahm nimitta dull unstable no nimitta how long practice report"; "kasina practice experience light kasina afterimage"; "light appears in my meditation bright eyes closed what is it advice"; "Ajahn Brahmali nimitta light mind how to develop beautiful breath forum answer"; "obhasa luminous mind pabhassara seeing light meditation experience personal"; "meditation visions lights colours seen during sitting should I ignore" -> new: Ajahn Brahmavamso's Dark Jhana (t/17987); Phenomenology of meditation objects / pre-nimitta experiences (t/13150); Fire Kasina and madness (t/14435); Kasina practice in the EBTs (t/30599); 10 kasinas EBT or not (t/7565); Aphantasia and meditation (t/16051); Is Meditation a form of Hallucination (t/25070); VISUALIZATION in Buddhist Meditation (t/19657); The mind is luminous (t/20276).
- [open web] "reddit Prophantasia guide how to train projecting images open eyes" -> only third-party Reddit mirror hosts (not mine, not fetched): r/CureAphantasia "Prophantasia training guide" (u/Ok-Cancel3263, Nov 03 '24), "Image questioning exercise" (May 03 '23), posts of Aug-Sep 2022.

### WebFetch log (budget 40; 8 used in warm-up)
- #9 discourse.suttacentral.net/search.json?q=... (URL I constructed) -> PROVENANCE_REQUIRED: permission request not answered, withdrawn. Lesson: only URLs that appeared verbatim in WebSearch results (or in a fetched page) go through without a prompt. No constructed URLs from here on.
- #10 t/12661 Sensory deprivation, Nimitta and Jhana (URL from search results) -> OK. Mostly theoretical (is nimitta a deprivation hallucination?). Saved sources/frm-suttacentral-sensory-deprivation-nimitta.txt.
- #11 t/263 We perceived both light and a vision of forms, page 1 -> OK. Monastics (Sujato, Brahmali) on MN 128 light; first-person reports by waiyin, Russell, Fabiola, raivo. Saved.
- #12 t/13150 Phenomenology of meditation objects (pre-nimitta) page 1 -> OK but thin: one first-person post; moderators say the forum is not for personal practice discussion (explains why SuttaCentral has few practice logs).

### archive.org community-guide finds
- advancedsearch (mediatype texts) for: tulpa imposition; tulpa guide; dharma overground; prophantasia; fire kasina; dao bums; astral pulse; closed eye visuals; image streaming wenger; third eye forum guide; hypnagogic imagery guide. Useful hits: item `tulpamancy` (17 re-archived Google Docs, added 2020-04-14), item `TulpaCreationGuide` (Thunderclap, added 2016-06-16), item `the-fire-kasina` (2017; belongs to theravada-east-asian, not taken), item `Ap-001-locoAustriacosInstructionsOnTummo` (pragmatic dharma tummo compilation, 2012; no light content checked, not taken). Nothing for prophantasia, Dao Bums, Astral Pulse, DhO.
- CANDIDATE frm-tulpa-luigi-tulpamancy-guide (fulltext; Section 15 wall / darkness / sensory-control methods) p1
- CANDIDATE frm-tulpa-methos-creation-guide (fulltext; Part 6, dated 2017) p2
- CANDIDATE frm-tulpa-jdbar-method (fulltext; open-eye visualization + spatial location; chalkboard report) p2
- CANDIDATE frm-tulpa-kiahdaj-absolute-guide (fulltext; consensus/pointer) p3
- archive.org advancedsearch (all media) for: Frank Kepple; phasing astral pulse; Xanth phasing; psipog; kundalini list archive; taobums; thedaobums; pragmatic dharma practice journal; kenneth folk dharma; aphantasia cure; cureaphantasia; ld4all; dreamviews guide; WILD hypnagogic guide; astral dynamics forum; third eye seeing with eyes closed; seeing through closed eyelids; kasina practice log; nimitta; dhammawheel; AYP forum inner light; trataka experience; eyelid movies. Useful: `dream-views-complete-manual` (post-collection PDF, uploaded 2026-08-06); `prophantasia-reddit-series` (media files only for an r/CureAphantasia series, added 2023-07-29; Reddit is tool-blocked so only catalogued as a link). Not useful: Yahoo-groups raw dumps (too large, private lists), audio items, `chapter-20-third-eye-chakra-v-2` (2026 upload, reads as machine-written; excluded).
- CANDIDATE frm-dreamviews-sivason-visualization-training (partial; closed-eye light training from specks, with time scales) p1; date undated (2026 upload only)
- GitHub repository search is not available from this session ("sessions are bound to their configured repositories"); no GitHub discovery possible.
