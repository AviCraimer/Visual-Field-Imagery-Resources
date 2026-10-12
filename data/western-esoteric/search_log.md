# search log — western-esoteric

2026-10-11 start. Warm-up: WebSearch works; WebFetch approved for hermetic.com (no redirect). No prior candidates; fresh start.

## Plan (sub-areas and leads)
A. Late-antique theurgy / papyri: Iamblichus De Mysteriis III.14 (Taylor 1821 / Wilder 1911); Mithras Liturgy (Mead, A Mithraic Ritual 1907); Demotic Magical Papyrus lamp/vessel divination (Griffith & Thompson 1904); Corpus Hermeticum I/X/XIII (Mead 1906); Chaldean Oracles (Westcott/Mead); Plotinus Enn. V.5.7 (own lead: light seen on closing/pressing the eye); Betz PGM = in copyright, citation only.
B. Scrying manuals and scryers' testimony: N. W. Thomas 1905 (+Lang intro); Goodrich-Freer 1899 / PSPR 1889; Melville 1896; Sepharial; Besterman 1924; Atkinson 1908; Carrington 1920; Frater Achad 1923; P. B. Randolph, Seership (own lead); Barrett's Magus / Dee (low priority); Benjamin Rowe, Short Course in Scrying (hermetic.com, own lead).
C. Golden Dawn / Crowley: Flying Roll XI and tattva-vision papers (hermetic.com?); Regardie's Golden Dawn (in copyright, citation only); Crowley Liber E, Liber O, Book 4 Part I (Equinox, PD).
D. Steiner, Bardon, Theosophy: Steiner Way of Initiation / Initiation and Its Results (PD translations); Bardon IIH (in copyright, citation only); Leadbeater Clairvoyance 1899; AE Candle of Vision 1918.
E. Reichenbach / aura: Reichenbach Researches (Gregory 1850) and Letters on Od (O'Byrne 1926); Kilner Human Atmosphere 1911.
F. Spiritualist development circles: Wallis Guide to Mediumship 1903; Grumbine; Coates Seeing the Invisible; Carrington Your Psychic Powers; others via archive.org search.
G. Own leads: Staudenmaier, Die Magie als experimentelle Naturwissenschaft (1912, German: self-trained optical hallucination); UR Group mirror instructions (citation only); Heindel/AMORC if anything concrete.
Method: archive.org / Gutenberg direct download for PD books; WebSearch(allowed_domains hermetic.com) + WebFetch (max 40) for hermetic.com pages.

## Log
- 08:04 CANDIDATE wes-thomas-crystal-gazing | fulltext_saved | p1 | via: seed lead; WebSearch warm-up query returned the archive.org item
- 08:04 CANDIDATE wes-iamblichus-de-mysteriis | fulltext_saved | p1 | via: seed lead; archive.org search creator Iamblichus
- 08:04 CANDIDATE wes-mead-mithriac-ritual | fulltext_saved | p1 | via: seed lead; archive.org search for Mead, Echoes from the Gnosis
- 08:05 CANDIDATE wes-demotic-magical-papyrus | fulltext_saved | p1 | via: own lead (public-domain counterpart to the seed lead on PGM lamp divination); archive.org title search
- 08:05 CANDIDATE wes-goodrich-freer-essays | fulltext_saved | p1 | via: seed lead; archive.org search
- 08:06 CANDIDATE wes-melville-crystal-gazing | fulltext_saved | p1 | via: seed lead; archive.org title search
- 08:06 CANDIDATE wes-sepharial-how-to-read-the-crystal | fulltext_saved | p1 | via: seed lead; archive.org search (Gutenberg mirror), text taken from gutenberg.org
- 08:06 CANDIDATE wes-randolph-seership | fulltext_saved | p1 | via: own lead; archive.org search creator Randolph title seership
- 08:06 CANDIDATE wes-besterman-crystal-gazing | fulltext_saved | p2 | via: seed lead; archive.org title search
- 08:06 CANDIDATE wes-achad-crystal-vision | fulltext_saved | p2 | via: archive.org title search 'crystal gazing'
- 08:06 CANDIDATE wes-atkinson-practical-psychomancy | fulltext_saved | p3 | via: warm-up WebSearch result (gutenberg.org); archive.org listing
- 08:07 CANDIDATE wes-ae-candle-of-vision | fulltext_saved | p1 | via: seed lead; archive.org title search (the seed's Gutenberg pointer could not be confirmed through Gutenberg's search page)
- 08:07 CANDIDATE wes-leadbeater-clairvoyance | fulltext_saved | p2 | via: seed lead; archive.org search (Gutenberg mirror), text from gutenberg.org
- 08:08 CANDIDATE wes-steiner-way-of-initiation | fulltext_saved | p1 | via: seed lead; Gutenberg search page and archive.org search
- 08:08 CANDIDATE wes-kilner-human-atmosphere | fulltext_saved | p2 | via: seed lead; archive.org search
- 08:08 CANDIDATE wes-reichenbach-researches | fulltext_saved | p1 | via: seed lead; archive.org search creator Reichenbach
- archive.org downloads so far (all OK unless noted): Thomas 1905; Iamblichus (Taylor 1895 repr., Wilder 1911); Demotic Magical Papyrus 1904; Goodrich-Freer 1899; Melville 1910; Randolph 1870; Mead Mithriac Ritual 1907; Kilner 1911; Reichenbach/Gregory 1850; Besterman 1924; Achad 1923; AE 1918; Steiner 1909; Wallis 1903; Grumbine 1897; Coates 1906; Mead Thrice-Greatest Hermes v2. Gutenberg: Sepharial 26622, Leadbeater 29399, Atkinson 43954, Steiner 39986.
- FAILED: archive.org odic-magnetic-letters-baron-charles-von-reichenbach (HTTP 500, then hang) -> Letters on Od not obtained.
- archive.org bookfour00crow turned out to be Book Four Part II (Magick), not Part I; discarded. Part I sought on hermetic.com instead.
- NOTE: shared scratchpad bin/ia.py was overwritten by another agent; switched to private helper scratchpad/wes/wia.py.
- WebSearch (allowed_domains hermetic.com) "Flying Roll XI Clairvoyance tattwa vision Golden Dawn" -> gdlibrary/flying-rolls index, Flying Roll 'Clairvoyance', 'An Example of a Mode of Attaining to Spirit Vision', Rowe 'A Short Course in Scrying'.
- WebSearch (hermetic.com) "Benjamin Rowe A Short Course in Scrying" -> hermetic.com/norton/ashort.
- WebSearch (hermetic.com) "Crowley Book 4 Part I Dharana phenomena lights" -> crowley/book-4/aba1; Temple of Solomon the King IV (Equinox I:4).
- WebFetch #2-#4 (parallel): hermetic.com/gdlibrary/flying-rolls/clairvoyance, /gdlibrary/flying-rolls/index, /norton/ashort -> all three "CLIENT_ERROR source target: error while fetching" (not a permission refusal).
- WebFetch #5: retry hermetic.com/norton/ashort -> same CLIENT_ERROR. WebFetch #6: hermetic.com/crowley/book-4/aba1 -> same CLIENT_ERROR. Only the home page (warm-up, #1) has succeeded. Pausing hermetic.com; will make one more attempt later, otherwise deep pages are unobtainable.
- gap pass 2: Corpus Hermeticum I, X, XIII in Mead, Thrice-Greatest Hermes vol. II (1906), archive.org, saved and read: keep_marginal (noetic light, sense withdrawal).
