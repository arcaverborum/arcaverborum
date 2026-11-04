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
