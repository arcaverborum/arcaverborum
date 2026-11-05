# South American isolates — 2026-11-04

Baseline: release `A-2026-11-03`. Scope: the 64 South American languages that
the frozen Glottolog marks as isolates (`Is_Isolate`). Release A covers 43 of
them; 21 have no construction, and 15 covered ones have fewer than 100 records.

## Track 1: gap fills from sources already in the snapshot

Four isolate constructions gain **2,331 forms**: 1,068 → 3,246 concepts. The
additions are all outside the 161-concept core, which these four already cover
well (598 supported core slots, unchanged). Every added row carries segments
supplied by its source (`Segments_Source = source`). No earlier record was lost
(checked per construction by source form and concept). Primary sources, their
cognacy and all release A evidence are unchanged; supplements fill only
concepts the construction lacked. Per-construction counts are in the
[metrics](south_america_isolates_2026-11-04_metrics.json).

| Construction | Forms | Concepts | Core | Added from |
| --- | ---: | ---: | ---: | --- |
| Puinave | 346 → 1,282 | 316 → 1,164 | 159 → 159 | IDS 249 (Richardson); Huber and Reed 1992 |
| Hoti | 317 → 1,050 | 268 → 961 | 148 → 148 | IDS 250 (Rodman and Rodman) |
| Puelche | 319 → 844 | 262 → 771 | 145 → 145 | IDS 312 (Casamiquela and Viegas Barros) |
| Camsá | 234 → 371 | 222 → 350 | 146 → 146 | Huber and Reed 1992 |

**Eight more constructions, admitted through slice additions.** The same review
admits 3,582 forms for Cofán, Páez, Pumé, Movima, Urarina, Waorani, Trumai and
Warao (core 1,065 → 1,174 across the eight; see the
[ledger](south_america_isolates_2026-11-04_slices.csv)). Their intake groups
(IDS Cofán and others) are not in the A-2026-11-03 snapshot, so they are
committed as slice additions (`slices/lexibank/`: 11 whole groups, 5,732 intake
rows, pinned to the intake dataset versions). A clean checkout with only the
snapshot and these slices rebuilds the eight byte-identically to the full
workspace.

| Construction | Forms | Concepts | Core |
| --- | ---: | ---: | ---: |
| Cofán | 345 → 1,488 | 297 → 1,177 | 133 → 140 |
| Páez | 336 → 1,376 | 304 → 1,265 | 133 → 158 |
| Pumé | 312 → 1,212 | 274 → 1,149 | 127 → 138 |
| Movima | 320 → 597 | 295 → 572 | 135 → 153 |
| Urarina | 298 → 355 | 264 → 320 | 129 → 149 |
| Waorani | 1,230 → 1,299 | 1,196 → 1,265 | 147 → 156 |
| Trumai | 682 → 725 | 562 → 605 | 135 → 142 |
| Warao | 316 → 369 | 258 → 311 | 126 → 138 |

### Decision rules

The [ledger](south_america_isolates_2026-11-04_supplements.csv) records the four
admitted constructions: 2,331 admissions and 153 holds, each with its reason. It was compiled with
`scripts/compile_supplements.py`, which guards spelling, source sense, member
and evidence hash.

* **Mapping.** 98% of candidate rows (6,248 of 6,357) use a source parameter that already maps to
  the same concept in accepted constructions; these inherit that mapping and add
  no new semantic judgement. The 57 new pairings (all from Chacon's Colombian
  dataset) were reviewed against the frozen label and definition; six are held
  (crown of head, plant leaf, cane, paddle, rattle, blow).
* **One source per gap.** When several secondary sources fill the same concept,
  one is admitted in this order: IDS (segmented), Blum et al., Huber and Reed,
  NorthPeruLex, Hunter-Gatherer, Chacon, Joo. A second source is not a second
  gain; its rows are held as alternatives.
* **Earlier decisions stand.** Exact source forms held by earlier batches stay
  held, as do source senses held for the same source on semantic grounds.
  Unqualified egg, day and old are not admitted for food-egg, daylight and
  old-person.
* **Johansson et al. (2020).** Rows in that sound-symbolism representation stay
  behind the existing source gate, including NorthPeruLex rows that cite it
  (Johansson 2021): this removes all candidates for Candoshi-Shapra and Taushiro.
* **Identity.** Only rows whose source Glottocode is the construction's own are
  admitted.

IDS segments are a provisional CLTS conversion by Lexibank, not newly certified
phonetic fieldwork. Bound forms (stems written with a hyphen) and multiword
compounds are kept as the source gives them. This is a model-assisted draft
review, not specialist certification.

### Not done in this track

* IDS lists without supplied segments (Cayubaba 477, Itonama 487, Movima 812
  candidate concepts) need a source-specific orthographic profile first.
* Johansson-derived rows (Kwaza, Lule, Andoque, Candoshi-Shapra, Taushiro and
  others) remain gated.
* Thin constructions whose only alternative is GLED or DiACL (Aikanã, Leco,
  Vilela, Arutani) await the original-source research of track 2.

## Track 2a: machine-readable sources and primary changes (batch 2)

Three new source extensions: `asjp` (ASJP v21.1, CC BY 4.0: Puquina, Betoi,
Taruma lists), `cerronpalominomochica` (Cerrón-Palomino 1995, CLDF edition,
CC BY 4.0) and `majeled` (MaJeLeD Kipeá and Dzubukuá, CC BY 4.0). Per-construction
counts are in the [batch-2 metrics](south_america_isolates_2026-11-04_batch2_metrics.json);
decisions in the [batch-2 ledger](south_america_isolates_2026-11-04_batch2.csv).

| Construction | Forms | Concepts | Core | Change |
| --- | ---: | ---: | ---: | --- |
| Puquina (new) | 0 → 39 | 0 → 34 | 0 → 32 | ASJP placeholder; no open original wordlist |
| Betoi (new) | 0 → 21 | 0 → 20 | 0 → 18 | ASJP placeholder (from Zamponi 2003) |
| Dzubukuá (new) | 0 → 611 | 0 → 87 | 0 → 51 | MaJeLeD (Nantes 1709), written-only |
| Mochica | 39 → 247 | 37 → 175 | 35 → 71 | Cerrón-Palomino primary with profile; GLED preserved |
| Kipeá | 38 → 153 | 23 → 123 | 12 → 66 | MaJeLeD gap fill, written-only |
| Leco | 7 → 48 | 7 → 44 | 4 → 39 | GLED (van de Kerke via ASJP) primary; DiACL preserved |
| Aikanã | 1 → 41 | 0 → 39 | 0 → 37 | GLED primary (see note) |
| Taruma | 1 → 17 | 1 → 16 | 1 → 16 | ASJP (Farabee 1918) primary; Wiktionary preserved |

* **Mochica readings** come from the CLDF edition's own grapheme mapping, used as
  a variety-scoped profile (32 graphemes, one value each), so they are
  profile-derived; all 39 earlier GLED forms remain as attributed supplements.
* **ASJP CUICA is not used.** It is Jahn's (1927) Timote vocabulary with the noun
  prefixes stripped (13 of 33 forms identical, the rest prefix-less), not a
  Cuica sample; Timote will be taken from Jahn directly.
* **Aikanã:** the release-A record (Hunter-Gatherer, peach palm) had no concept
  mapping and cannot be carried as a sense-reviewed supplement; it remains in
  the intake. DiACL's 283 Aikanã rows stay held (mixed notation, unresolved
  provenance); Silva 2012 is all rights reserved.
* Written-only supplements carry `transcription_policy = orthographic_only`.
* New family codes for the remaining South American isolate families
  (`family_codes.csv`); new av_ids frozen in `varieties.csv`.

## Track 2b: transcribed original sources (batch 3)

Ten source extensions transcribed from page images or extracted from
born-digital lexica: `guamo1788`, `jahn1927`, `kochgrunberg1928`, `heath1883`,
`cmrivet1913`, `tessmann1930` (public domain; Tessmann and Créqui-Montfort and
Rivet are public domain in the US, accepted for all tiers by the maintainer),
`chacon2024arutani` (CC BY 4.0), `bacelar2010kanoe`, `dangelis2010arara` and
`pereira1964irantxe` (CC BY 3.0, now a reviewed licence in all three tiers).
Each extension's README and VERIFY.md record the pages, scan hashes, notation,
exclusions and the verification: an independent second reading of every list
(historical sources) or a re-read sample of 150 to 365 rows (born-digital
lexica, 0 to 0.8% errors, all corrected). Page images are kept outside git.
Counts: [batch-3 metrics](south_america_isolates_2026-11-04_batch3_metrics.json);
decisions: [batch-3 ledger](south_america_isolates_2026-11-04_batch3.csv).

| Construction | Forms | Concepts | Core | Source |
| --- | ---: | ---: | ---: | --- |
| Guamo, Santa Rosa (new) | 0 → 179 | 0 → 154 | 0 → 63 | Anon. 1788 |
| Guamo, San José (new) | 0 → 178 | 0 → 154 | 0 → 63 | Anon. 1788 |
| Guamo, village not stated (new) | 0 → 136 | 0 → 110 | 0 → 38 | Anon. 1788 |
| Ayomán (new) | 0 → 263 | 0 → 156 | 0 → 60 | Jahn 1927 |
| Jirajara (new) | 0 → 96 | 0 → 70 | 0 → 28 | Jahn 1927 |
| Gayón (new) | 0 → 72 | 0 → 50 | 0 → 26 | Jahn 1927 |
| Timote (new) | 0 → 350 | 0 → 224 | 0 → 83 | Jahn 1927 |
| Auaké, historical (new) | 0 → 328 | 0 → 212 | 0 → 79 | Koch-Grünberg 1928 |
| Arara do Rio Branco (new) | 0 → 246 | 0 → 91 | 0 → 31 | D'Angelis 2010, IPA |
| Manoki (new) | 0 → 652 | 0 → 357 | 0 → 100 | Pereira 1964 |
| Arutani | 78 → 1,139 | 78 → 540 | 70 → 132 | Chacon et al. 2024, IPA (primary) |
| Kanoê | 263 → 1,322 | 205 → 518 | 113 → 130 | Bacelar, IPA (primary) |
| Canichana | 87 → 347 | 87 → 327 | 70 → 112 | Heath 1883; Créqui-Montfort and Rivet 1913 |
| Máku | 112 → 372 | 100 → 321 | 75 → 108 | Koch-Grünberg 1928 |
| Sapé | 78 → 191 | 78 → 178 | 70 → 92 | Koch-Grünberg 1928 |
| Omurano | 60 → 190 | 60 → 184 | 54 → 71 | Tessmann 1930 |
| Aewa | 18 → 68 | 18 → 66 | 17 → 20 | Tessmann 1930 |

* Historical lists are **written-only**: spelling kept exactly, no reading
  inferred. Jahn's and Koch-Grünberg's documented notations are copied into the
  extension READMEs as the basis for future reviewed profiles.
* Guamo follows the compiler's own doublet convention (first form Santa Rosa,
  second San José); single forms are not assigned to a village.
* Créqui-Montfort and Rivet's Heath rows repeat `heath1883` and are not used
  again; Ayomán forms that Jahn quotes from Oramas carry no Glottocode and are
  not admitted.
* Kanoê: 58 Johansson release-A forms without a concept mapping cannot be
  carried as supplements and stay in the intake.

## Track 2c: transcribed original sources (batch 4)

Fifteen more extensions, all public domain except `spruce1863` (Urban 2015's
edition, CC BY 4.0): `borba1908`, `quadros1892`, `nimuendaju1925`,
`castelnau1851`, `boggiani1900`, `schmidt1905`, `lafone1895`, `branner1887`,
`nimuendaju1935`, `nimuendaju1949`, `estevao1958`, `seler1902`,
`martinezcompanon1790`, `spruce1863` and `romero1768`. `aguirre1793` was
transcribed but is held (an older Payaguá stage needing its own construction).
Counts: [batch-4 metrics](south_america_isolates_2026-11-04_batch4_metrics.json);
decisions: [batch-4 ledger](south_america_isolates_2026-11-04_batch4.csv).

**Blind spot-check.** The second readings of these lists were not independent,
so a separate reader transcribed 25 sampled rows per source (359 rows) from the
page images without seeing the forms. No gloss–form pairing errors; nine sources
matched exactly, four had diacritic-level differences (now flagged), and for
the Martínez Compañón plate and Spruce's manuscript the low-resolution scans
cannot decide a few letters: those rows follow Urban's published readings with
`Doubt = true` and the alternative. One Atacame form was corrected (*yr-e*);
Schmidt's æ forms are flagged for a possibly unrecorded macron. Yurumanguí had
its own blind second reading (154 of 159 entries identical, five settled on the
image); Rivet's respellings without a 1768 original (37 rows) are excluded.

| Construction | Forms | Concepts | Core | Source |
| --- | ---: | ---: | ---: | --- |
| Atacame (new) | 0 → 440 | 0 → 235 | 0 → 79 | Pallares 1877 via Seler 1902 |
| Payaguá (new) | 0 → 515 | 0 → 243 | 0 → 83 | Boggiani 1900 |
| Matanawí (new) | 0 → 353 | 0 → 203 | 0 → 86 | Nimuendajú 1925 |
| Guachi (new) | 0 → 145 | 0 → 127 | 0 → 52 | Castelnau 1851 |
| Yurumanguí (new) | 0 → 144 | 0 → 93 | 0 → 28 | Romero 1768 via Rivet 1942 |
| Oti (new) | 0 → 100 | 0 → 81 | 0 → 43 | Borba 1908; Quadros 1892 |
| Culli (new) | 0 → 43 | 0 → 42 | 0 → 26 | Martínez Compañón |
| Sechuran (new) | 0 → 31 | 0 → 29 | 0 → 11 | Spruce 1863 via Urban 2015 |
| Sechura, Martínez Compañón (new) | 0 → 43 | 0 → 42 | 0 → 26 | Martínez Compañón |
| Colán (new) | 0 → 43 | 0 → 42 | 0 → 26 | Martínez Compañón |
| Catacaos (new) | 0 → 43 | 0 → 42 | 0 → 26 | Martínez Compañón |
| Xukurú (new) | 0 → 29 | 0 → 29 | 0 → 16 | Nimuendajú (Loukotka 1949; 1935) |
| Tuxá (new) | 0 → 13 | 0 → 11 | 0 → 7 | Estêvão (Pompeu 1958) |
| Guató | 38 → 277 | 38 → 275 | 36 → 99 | Schmidt 1905; Castelnau 1851 |
| Vilela | 73 → 291 | 60 → 161 | 37 → 77 | Lafone Quevedo 1895 |
| Fulniô | 32 → 53 | 30 → 51 | 28 → 31 | Branner 1887; Nimuendajú 1935 |
| Mochica | (247 after batch 2) → 267 | → 194 | → 78 | Martínez Compañón (Yunga) |

Held: Pankararú (the "Macarú = Pankararú" identity is unsettled), Aguirre's
Payaguá (separate stage), Chono (no usable glossed source), Mure (prayers only),
Ramanos (8 words, copyrighted edition only) and Tinigua (Castellví 1940 in
copyright to 2031).

## Profiles — reviewed 2026-11-05

Round 1 reviewed the acquired author keys; round 2 follows the maintainer's
acceptance of Koch-Grünberg's p. 2 explicit adoption of P. W. Schmidt, *Die
Sprachlaute und ihre Darstellung in einem allgemeinen linguistischen Alphabet*,
*Anthropos*2 (1907). Schmidt's original PDF is pinned at SHA256
`d8baff851d819dc40e581642dda6e76d4f3d192f97aebd3ffb20c78083822552`.
Printed glyphs were read from page renders: vowels/diacritics pp. 540–584,
consonants pp. 848–880 and the unnumbered consonant conspectus after p. 1098
(PDF p. 1289). KG IV pp. 2–3 and every local note in pp. 308–324 were also
inspected. KG's own/local statements override the identical-glyph Anthropos
value. This supersedes the earlier KG missing-base-alphabet hold; the other
round-one decisions remain unchanged.

| Source | Primary fully profiled / source rows | Supplement fully profiled / admitted source rows |
| --- | --- | --- |
| Jahn 1927 | Ayomán 0/263; Jirajara 0/96; Gayón 0/72; Timote 0/350 | — |
| Koch-Grünberg 1928 | Awake **228/328** (round 1: 0) | Máku **188/260**; Sapé **78/113** (round 1: 0 each) |
| Boggiani 1900 | Payaguá 1/515 | — |
| Nimuendajú 1925 | Matanawí 0/353 | — |
| Nimuendajú 1949 | Xukurú 0/21 | — |
| Nimuendajú 1935 | — | Fulniô 0/9; Xukurú 0/8 |

The KG profile retains vowel nasality, colon/macron quantity, very-short breve,
nonsyllabic arc, nucleus-attached stress and analytical/word boundaries. Plain
`o` uses KG's stated **typical** open `ɔ` value; this is not a claim about every
surface realization. Schmidt's A degrees remain distinct (`a→ä`, `ạ→a`,
`a̱→ɑ`); underlined `u̱→ʊ` has an identical-glyph value in Schmidt compatible
with KG's u–o interval. Explicit KG `e̱→ɛ`, `w→w`, `y→j`, rolled `r`,
`x→x`, `x̭→ç` and apostrophe→ʔ take precedence. Reduced ẹ is not Schmidt's
ordinary closed e. Intermediate fʰ/z̭, uncertain ĺ/ị and local palate/hesitation /
indistinct-vowel readings remain unresolved. Parentheses denote strongly reduced
sounds; the existing profile machinery provides no corresponding convention,
so their forms stay written. No mark is silently deleted and no value is
borrowed from later language scholarship. KG p. 3 says a/o followed by an accented i/u is a diphthong (even across a hyphen) but not which member is the nucleus; Schmidt §242 (unaccented member nonsyllabic) would contradict KG's equivalent arc notation, and a hiatus reading would contradict KG. These forms are held as exact whole-form guards.

Awake uses a primary profile with 110 finite rules plus 39 exact empty
whole-form guards (34 of them the diphthong hold). Converted Máku/Sapé admissions use separate exact `^Form$`
supplement profiles, with a per-admission file SHA256; only 188/78 rows clear
`orthographic_only`. The remaining 72/35 KG admissions retain it. Other-source
primary/supplement readings and evidence hashes remain unchanged. Unknown
notation counts (occurrences, not distinct forms) are:

| Scope | Unmapped units and occurrence counts | Additional local whole-form holds |
| --- | --- | --- |
| Awake | `(`65, `)`65, `ĺ`1, `ẹ`2, `ẹ́`1, `ị`1 | 39: 34 a/o + accented i/u diphthongs; final-vowel notes pp. 311/313 and three-dash notation |
| Máku KG supplements | `(`57, `)`57, `z̭`9, `·`1, `ʰ`2 (within fʰ), `ẹ`12, `ẹ́`2 | 3: two a/o + accented i/u diphthongs; hesitant ai, p. 321 fn1 |
| Sapé KG supplements | `(`9, `)`9, `:`3 (after unsupported ẹ clusters), `ẹ`8, `ẹ́`9, `ẹ̃`8, `ẹ̃́`2 | 11: ten a/o + accented i/u diphthongs; palate-specific u, p. 314 fn2 |

Jahn's p. 379 key remains scoped to Ayomán (`sh→ʃ` only). His p. 339
introduction allows different conventions; Párraga/Siquisique Jirajara and
Gayón do not explicitly adopt that key. Timote retains Urrecheaga's spelling
(p. 326). These three remain guarded written-only. Ayomán's selector excludes
all 58 Oramas and four Freitez Pineda rows; no admission or identity changed.
Nimuendajú's 1925 p. 148 Torá table is not established for Matanawí; its local
hooked-stress notes supply no full key. The 1935 typescript and 1949 printing
have no applicable authorial key. Matanawí/Xukurú retain their written guards.
Boggiani's eight comparisons, including initial-capital equivalents, still
cover only the unmapped first-person prefix `S→z`; its affix sense is unchanged.

Reproduce with `scripts/sa_isolates_profile.py --write --review-output PATH`.
The private handoff directory `work/sa-isolates/profiles/kochgrunberg1928.md`
contains both sources' exact page/image locations, transcribed table,
per-grapheme justification, counts and ten samples per variety. Other per-source
packets are preserved. `REPORT.md` gives the current closure; historical round 1
packets and its verification remain separate.

Round2: all three affected CLI builds passed (891 output rows); full pytest
**661 passed**, exit 0 (99 pre-existing warnings), using existing optional CLDF
test support. Intake rebuilding was explicitly blocked before writes. Stable-ID
comparison proves every form, value, concept, identity, loan, provenance and
cognacy field unchanged, except converted supplements' explicit reading-provenance
comments. Only 494 new `Segments`/`Segments_Source` pairs change. The existing
supplement mechanism regroups rows by profile file, so Máku/Sapé CSV row order
changes; Awake order does not. All other-source rows are byte-equivalent as
records. Compiler rerun is byte-idempotent; Ruff/whitespace checks pass. Intake
size/inode/mtime and `extensions/`, `slices/`, `src/` are unchanged. No aggregate /
site refresh, commit, push or PR was made. Round1's removal of 746 accidental
generic tokenizer readings remains intact. Remaining gates are in
[HELD](planning/HELD.md#south-american-isolate-profiles-2026-11-05).
