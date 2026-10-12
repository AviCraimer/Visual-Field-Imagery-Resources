# Search log, stream christian

## 2026-10-11 start
- Warm-up: WebSearch worked (see warmup.md). No WebFetch in this stream. Texts come from archive.org / Gutenberg / CCEL by bash download.
- `il.py status`: 0 candidates at start; fresh run, not a resume.
- Tool probe: archive.org advancedsearch works. Lending-library scans (collection inlibrary) refuse `_djvu.txt` (files flagged private). archive.org full-text search (`be-api.us.archive.org/fts/v1/search?q=..&identifier=..`) works and returns short highlighted fragments (about 15-20 words each) with a scan-leaf number. Decision: for in-copyright books with no freely offered text, save only such short search fragments (labelled as fragments, not continuous text) so that anchors can be checked; never the book text. `fulltext/inside.php` returns 403.

## Plan: sub-areas and leads
A. Hesychast method (induction instructions): pseudo-Symeon "Three Methods of Prayer"; Nikephoros "On Watchfulness"; Gregory of Sinai; Kallistos and Ignatios Xanthopoulos; The Way of a Pilgrim. English translations are in copyright (Kadloubovsky and Palmer 1951; Philokalia vol. 4, 1995). Look for public-domain conduits that quote the method (Fortescue's Catholic Encyclopedia article 1910; Gibbon ch. 63; Hausherr 1927).
B. Hesychast light testimony and defence: Symeon the New Theologian (Discourses, Hymns); Palamas, Triads; Seraphim of Sarov and Motovilov; modern Athonite testimony (Sophrony, Joseph the Hesychast) as own leads.
C. Eastern warnings: Evagrius, Diadochos, Gregory of Sinai on not accepting lights; Brianchaninov and Theophan on prelest.
D. Early Eastern sources in public-domain English (own leads): Pseudo-Macarius, Fifty Spiritual Homilies (Mason 1921); Isaac of Nineveh, Mystic Treatises (Wensinck 1923).
E. Western visionaries' own accounts: Hildegard (letter to Guibert); Teresa (Life 27-29, Interior Castle VI); Ignatius of Loyola (Autobiography, Spiritual Diary); Julian of Norwich; Angela of Foligno; Suso; Rolle; Boehme.
F. Western warnings and classification of visions: John of the Cross, Ascent; Hilton, Scale of Perfection; Cloud of Unknowing; Poulain, Graces of Interior Prayer (own lead: manual with rules for directors).
G. Quakers: Fox's Journal and early tracts; Rex Ambler's Experiment with Light (check seen vs metaphorical).
H. Swedenborg, Spiritual Diary (breathing and lights). Seed lead sits in this stream; western-esoteric's lead list does not name it, so it is catalogued here.

## Actions
- 07:58 CANDIDATE chr-macarius-fifty-homilies (fulltext_saved, p2): Macarius Homily VIII read; full text saved from archive.org (803k chars).
- 08:00 CANDIDATE chr-isaac-of-nineveh-mystic-treatises (fulltext_saved, p3): Isaac of Nineveh, Wensinck 1923, full text saved; skimmed treatises XX-XXII.
- 08:00 CANDIDATE chr-poulain-graces-of-interior-prayer (fulltext_saved, p2): Poulain 1910 full text saved (1.75M chars); Part IV chs XX-XXIII located.
- 08:00 CANDIDATE chr-hilton-scale-of-perfection (fulltext_saved, p1): Hilton, Underhill ed. 1923, full text saved; Book I ch. 11 read.
- 08:00 CANDIDATE chr-john-of-the-cross-ascent (fulltext_saved, p1): Ascent, Lewis/Zimmerman 1906, full text saved; Book II chs X-XI read.
- 08:00 CANDIDATE chr-ignatius-autobiography (fulltext_saved, p1): Ignatius Autobiography 1900 full text saved; Manresa passages read; translation looseness noted.
- 08:00 CANDIDATE chr-angela-of-foligno-divine-consolation (fulltext_saved, p3): Angela of Foligno 1909 full text saved; Sacrament visions read.
- 08:05 CANDIDATE chr-teresa-life (fulltext_saved, p1): Teresa, Life (Lewis 1904) full text saved; ch. XXVIII sections 5-9 read.
- 08:05 CANDIDATE chr-teresa-interior-castle (fulltext_saved, p1): Interior Castle (Stanbrook 1921) full text saved; VI.9 sections 1-3 read.
- 08:05 CANDIDATE chr-cloud-of-unknowing (fulltext_saved, p1): Cloud of Unknowing (Underhill 1922) full text saved; chs 4 and 52 read.
- 08:05 CANDIDATE chr-julian-revelations (fulltext_saved, p2): Julian (Warrack 1901) full text saved; ch. III read.
- 08:05 CANDIDATE chr-boehme-illumination-martensen (fulltext_saved, p3): Boehme pewter-dish episode saved via Martensen 1885; Hartmann and 1764 edition rejected.
- 08:05 CANDIDATE chr-rolle-fire-of-love (fulltext_saved, p3): Rolle (Comper 1914) full text saved; Mending of Life ch. XII read: says no seen light.
- 08:05 CANDIDATE chr-fox-journal (fulltext_saved, p3): Fox, Journal (Everyman 1924) full text saved; searched for seen light: figurative only on first pass.
- 08:05 Removed alt_urls I had written from memory (Gutenberg 8120, 52456 and CCEL paths): 52456 resolved to an unrelated book and the CCEL paths could not be confirmed. Kept Gutenberg 24534 and 52958, both confirmed by archive.org mirror identifiers.
- gap pass 2: Nikephoros On Watchfulness, Greek Philokalia 1893 vol 2 (archive.org Dobrotolyubie1793) saved; dropped (no seen light).
- gap pass 2: Gregory of Sinai, Greek Philokalia 1893 vol 2, saved and read: keep (warnings).
- gap pass 2: Diadochos and Evagrius On Prayer from Greek Philokalia 1893 vol 1 (archive.org Philokalia1893GreekAthens) saved and read: keep. Xanthopoulos and Symeon chapters from vol 2 saved and read. Kadloubovsky-Palmer and Palamas Triads: citation_only (in copyright; Triads not in Migne). WebSearch worked once (warmup2).
- gap pass 2: Seraphim-Motovilov conversation, Russian text (archive.org B-001-031-884-ALL, 2011 brochure of 1903 text) saved and read: keep.
- gap pass 2: Hildegard letter to Guibert, Latin, Pitra Analecta Sacra VIII 1882 (archive.org jjoannesbaptist00hildgoog; the other copy analectasanctae00hildgoog returned HTTP 500) saved and read: keep.
- gap pass 2 log: WebSearch worked (warmup2); all texts by curl from archive.org and Sefaria; one archive.org 500 on analectasanctae00hildgoog, used other copy.
