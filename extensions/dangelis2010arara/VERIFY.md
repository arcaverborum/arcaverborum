# VERIFY — dangelis2010arara

Date: 2026-11-04. Source: born-digital PDF, 7 pages; text layer with a legacy
phonetic font (IPAKiel), mapped explicitly (README).

## Glyph map verification

Every distinct IPAKiel/Arial glyph (28) was rendered in context (sheet at 150 dpi,
then 800–1000 dpi for the diacritics `§`, `0`, U+F022, `å`, `)`). Result in README.

## Second, independent reading — all kept rows

Each page was rendered (190 dpi, page halves plus the strips above them) and every
kept gloss + transcription cell (199 cells → 246 forms) was typed from the image
(`scripts/ext/arara_verify_readings.tsv`), then compared with the extraction as a
multiset of (gloss, cell) pairs.

| | |
|---|---|
| cells compared | 199 / 199 |
| disagreements, first comparison | 3 |
| **systematic mapping error found** | IPAKiel `0` had been mapped to U+032F (inverted breve below). At 1000 dpi it is a **tilde below** (U+0330). All 22 cells with this glyph (colar, bonito, doendo, céu, chuva, morro, arco, cocar, flecha, paneiro, remédio caseiro, anta, aranha caranguejeira, cutia, macaco prego, mutum, tatu, mamão do mato, mandioca, pupunha …) were corrected and re-read at 400 dpi against the corrected text: all agree. (The reader had also typed U+032F at 190 dpi, biased by the first map; the 1000-dpi check settled it.) |
| remaining disagreements after re-reading | 0 |
| unclear (text layer kept, flagged in Comment) | 3 forms: *aranha caranguejeira* `[kiˈʃɛ̃ɪ̰̃]` (two tildes above overlap), *mutum* `[kũj̃ɲ]` (tilde over j not separable from ũ), *tatu* `[ˈdoj̰]` (tilde below hidden by the descender of j) |

**Error rate of the delivered data in the full check: 0 / 199 cells** (the `0`
glyph error, 22 / 199 cells = 11 % before correction, was found by this pass and
fixed for the whole file).

Other observations confirmed on the page: plain `r` (not ɾ) in *pau em pé*
`[murutuˈpi]`, *comer* `[ˈmprajə]`, *cartucho*; *roçado* is printed `i:ˈga]`
without an opening bracket; *cartucho* `brikati  > [brikatik]`.

## Integrity

`avext.validate()`: no errors. merkmal: 245 rows with Segments, 24 with a token
not accepted (listed in README).

## Counts

| | |
|---|---|
| table cells read (gloss + form) | 251 |
| kept cells | 199 (+2 forms taken from marginal notes, included in the 199) |
| rows (forms.csv) | 246 (233 distinct forms) |
| distinct glosses / parameters | 187 |
| Concepticon-mapped | 91 parameters (91 concept sets, 132 rows) |
| skipped: author's abstracted roots (`*`) | 9 |
| skipped: exact repeats of a gloss + transcription | 43 |
| unreadable | 0 |
