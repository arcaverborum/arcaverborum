# South American isolates — 2026-11-04

Baseline: release `A-2026-11-03`. Scope: the 64 South American languages that
the frozen Glottolog marks as isolates (`Is_Isolate`). Release A covers 43 of
them; 21 have no construction, and 15 covered ones have fewer than 100 records.

## Track 1: gap fills from sources already in the snapshot

Twelve isolate constructions gain **5,913 forms**: 4,518 → 9,910 concepts and
1,663 → 1,772 supported core slots. All added rows carry segments supplied by
their source (`Segments_Source = source`). No earlier record was lost (checked
per construction by source form and concept). Primary sources, their cognacy and
all release A evidence are unchanged; supplements fill only concepts the
construction lacked. Per-construction counts are in the
[metrics](south_america_isolates_2026-11-04_metrics.json).

| Construction | Forms | Concepts | Core | Added from |
| --- | ---: | ---: | ---: | --- |
| Cofán | 345 → 1,488 | 297 → 1,177 | 133 → 140 | IDS 254 (Borman) |
| Páez | 336 → 1,376 | 304 → 1,265 | 133 → 158 | IDS 244 (Gerdel); Huber and Reed 1992; Joo |
| Puinave | 346 → 1,282 | 316 → 1,164 | 159 → 159 | IDS 249 (Richardson); Huber and Reed 1992 |
| Pumé | 312 → 1,212 | 274 → 1,149 | 127 → 138 | IDS 251 (Dyck and Dyck) |
| Hoti | 317 → 1,050 | 268 → 961 | 148 → 148 | IDS 250 (Rodman and Rodman) |
| Puelche | 319 → 844 | 262 → 771 | 145 → 145 | IDS 312 (Casamiquela and Viegas Barros) |
| Movima | 320 → 597 | 295 → 572 | 135 → 153 | Blum et al. Pano-Tacanan (from IDS) |
| Camsá | 234 → 371 | 222 → 350 | 146 → 146 | Huber and Reed 1992 |
| Urarina | 298 → 355 | 264 → 320 | 129 → 149 | NorthPeruLex (Peña 2023 fieldwork) |
| Waorani | 1,230 → 1,299 | 1,196 → 1,265 | 147 → 156 | Hunter-Gatherer database |
| Trumai | 682 → 725 | 562 → 605 | 135 → 142 | Hunter-Gatherer database |
| Warao | 316 → 369 | 258 → 311 | 126 → 138 | Hunter-Gatherer database; Joo |

### Decision rules

The [ledger](south_america_isolates_2026-11-04_supplements.csv) records 5,913
admissions and 444 holds, each with its reason. It was compiled with
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
