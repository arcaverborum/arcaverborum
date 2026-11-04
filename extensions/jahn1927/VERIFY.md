# Verification log: jahn1927

Date: 2026-11-04.

## Method

**Pass 1.** I transcribed the lists from 300 dpi renderings of PDF pages 458–484
(printed pp. 379–405), each page split into two strips. Doubtful letters were checked
on 500–600 dpi zooms. The OCR text layer was used only to locate words and to read the
running-text source discussion (pp. 6–7, 261–262, 272–273, 325–327). It was not used
for list readings.

**Pass 2 (independent).** A separate agent, with no access to the pass-1 files or the
text layer, re-transcribed every entry line of the four lists from the same images:
- Ayomán: 247 lines, including Frases.
- Jirajara: 98 lines.
- Gayón: 75 lines, including Frases.
- Timote: 322 lines.

It also transcribed Jahn's alphabet paragraph independently, and the copy in
`README.md` agrees with it. The files were compared line by line with `difflib`.

## Results

**Pages:** 379–405.

**Ayomán (230 lexical lines).** All identical except three lines where pass 2 used
the ASCII apostrophe and pass 1 the typographic ’ (`t’bóp`, `k’sísh-kichsíso`,
`sh’cut`). The print has a typographic apostrophe, so ’ (U+2019) is kept. Pass 2 also
recorded:
- the comment line on p. 383 ("Los criollos de Parupano…"), which is not data;
- the 16 Frases lines, which pass 1 had deliberately not tabulated.

**Jirajara (98 lines).** Three differences:
1. *Venado*. Pass 1 read "agüi" in both columns, pass 2 "agüí". At 600 dpi the final i
   carries an acute in both columns. **Corrected to agüí.**
2. *Danta (Tapirus sp.)*. The print has no space: "Tapirussp.". **Gloss corrected to
   the printed form.**
3. *Escardilla*. The footnote text was carried differently in the two files. There is
   no reading difference.

**Gayón (69 lexical lines).** Identical. The only differences are the footnote
carrier on *Cunaguaro* and the 6 Frases lines, which pass 1 had not tabulated.

**Timote (322 lines).** Identical except *mi hermano* "kushík." vs "kushík,". The
final mark is damaged punctuation and does not affect `Form`.

**Unclear readings agreed by both passes and flagged in `Comment`:**
- Timote *Las manos* "tit-kuñem": the letter after k is blotted. Read u; i or ü are
  possible. The text layer reads "kiñem".
- Gayón *Oreja* "himigüí": the final í may be i.
- Ayomán *Pecho* "na-baeni": there is a vertical mark between the dash and the n.
- Ayomán *Teta de mujer* "in-hunhán": the first h has a stroke through it.

**Minor type damage.** Raised periods, stray commas and vertical marks between the
dash and the first letter do not affect the letters. They are noted in pass 2 and not
flagged.

**Unreadable rows skipped:** none.

## Counts

| Item | Count |
|---|---|
| Form rows: total | 843 |
| Form rows: Ayomán (Jahn) | 263 |
| Form rows: Ayomán (Oramas) | 58 |
| Form rows: Freitez Pineda | 4 |
| Form rows: Jirajara | 96 |
| Form rows: Gayón | 72 |
| Form rows: Timote | 350 |
| Distinct variety+form pairs | 831 |
| Distinct glosses | 603 |
| Concepticon-mapped glosses | 408 (306 distinct concepts) |
| Loan = true | 32 |
| Doubt = true | 3 |
| Skipped: phrases/sentences | 219 lines |
| Skipped: toponyms | 6 |
| Skipped: comparison-column repeats | 112 cells |
| Skipped: repeated identical entries | 2 |
| Skipped: printer's duplicate line | 1 |
| Skipped: comment line | 1 |

The 219 phrase lines are: Ayomán 16, Jirajara 12, Gayón 6, Timote 1 in section L, and
≈184 Timote Frases lines (pp. 406–411). The Timote Frases count was made from the text
layer by counting dash-separated lines, because those pages were not transcribed.

The list of every skipped item is in the build log
(`scratch/tx/skips_jahn1927.tsv` in the staging work directory).

## Integrity checks

- CSVs were written with Python's `csv` module and are UTF-8 NFC.
- IDs are unique.
- Every `Language_ID` and `Parameter_ID` resolves.
- Every `Source` key is in `sources.bib`.
- Every Concepticon ID and Glottocode exists in the frozen tables.
- `arcaverborum.extensions.validate` (temporary root) reported no problems.
