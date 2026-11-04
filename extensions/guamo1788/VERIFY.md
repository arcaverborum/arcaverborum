# Verification log: guamo1788

Date: 2026-11-04.

## Method

**Pass 1.** I transcribed the list from 300 dpi renderings of PDF pages 397–407
(printed pp. 382–392). Each page was cropped to the text block and split into a top
and a bottom strip. Doubtful letters were checked on 400–800 dpi zooms. I did not use
the OCR text layer for readings. I used it only to find the coordinates of a word to
zoom on.

**Pass 2 (independent).** A separate agent, which had no access to the pass-1 file or
to the text layer, re-read every printed line from the same page images. It produced
`page / gloss / value` for all lines, including those with an empty Guamo column.
The two files were then compared line by line with `difflib`.

## Results

- **Pages:** 382–392, plus the notes on pp. 392–393. The notes were read for the
  dialect convention and are not data.
- **Rows checked:** 439 printed gloss lines (314 with a Guamo entry) in both passes.
- **Agreement:** 437 of 439 lines are identical in both passes, in gloss and in value,
  letter for letter including accents and the separator `ô`.
- **Discrepancies, all resolved:**
  1. **p. 382, *Gentes*.** Pass 1 read "Aucherme", pass 2 "Auchérme". At 800 dpi
     there is a faint mark over the first e that is weaker than a printed acute, so I
     kept "Aucherme". The Comment reads `unclear: faint mark …`.
  2. **p. 383, *Razonamiento* (empty).** The line order differed: pass 1 had appended
     the line at the end of the page. Pass 2's position (between *Hablar* and
     *Palabra*) is correct, and pass 1 was reordered. This has no effect on the data.
  3. **p. 386, *Endeble* (empty).** Pass 1 read the gloss as printed "Fndeble", pass 2
     read a broken E. The compiler's note on p. 392 spells it "Endeble". Since the
     Guamo cell is empty, no parameter is created.
- **Unclear readings flagged in `Comment` or noted.** These are agreed by both passes
  but with damaged type:
  - *Familia* "Aucharme": the m is damaged.
  - *Cieno* "Farotansi": the t is damaged.
  - *Mosquito* "Dacoiomta": there is a dot under the m.
  - Faint print on *Ayre* "Tacsco", *Polvo* "Ducug", *Profundidad* "Pefu" and
    *Agugero* "Fitintansi". The readings are not in doubt.
  - Specks after *Matrimonio* "Dispansu." and above *Tristeza* "Sarui" were ignored.
- **Unreadable rows skipped:** none.

## Counts

| Item | Count |
|---|---|
| Printed gloss lines | 439 |
| Lines with a Guamo entry | 314 |
| Lines with an empty Guamo column (skipped) | 125 |
| Repeated identical entry skipped (*Frio*, p. 386) | 1 |
| Form rows: total | 493 |
| Form rows: Santa Rosa (`sant1461`) | 179 |
| Form rows: San José (`sanj1287`) | 178 |
| Form rows: unspecified (`guam1236`) | 136 |
| Distinct variety+form pairs | 479 |
| Distinct glosses (`parameters.csv`) | 313 |
| Concepticon-mapped glosses | 263 |
| Loan = true | 3 |
| Doubt = true | 1 |
| Phrases / proper names skipped | 0 |

## Integrity checks

- CSVs were written with Python's `csv` module and are UTF-8 NFC.
- Form, parameter and language IDs are unique.
- Every `Language_ID` and `Parameter_ID` resolves.
- Every `Source` key (`guamo1788_anon1788`, `guamo1788_realbiblioteca1928`) is in
  `sources.bib`.
- Every Concepticon ID exists in `raw/concepticon/concepticon.tsv`, and every
  Glottocode exists in `raw/glottolog/languages.csv`.
- The repository validator `arcaverborum.extensions.validate` was run against a
  temporary root containing only this extension and `jahn1927`. It reported no
  problems.
