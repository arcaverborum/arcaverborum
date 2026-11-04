# Verification log — bacelar2010kanoe (2026-11-04)

Source: Bacelar [2010], `vocabulario_kanoe_comparado.pdf`, 85 pp., sha256
`255bc99018f7bdfa3e21e71ce578942c6a79395dc2e045fbb594815bc7d79de0`. Born-digital PDF;
first pass = text layer with the explicit glyph map in README; second pass = independent
visual reading of rendered page images.

## 1. Glyph map check (before the first pass)

Every SILManuscriptIPA93 private-use code and every SILManuscriptIPA (8-bit) character in
the phonetic column was located (first two occurrences of each), rendered at 300–600 dpi
and identified on the image. Result: the map in README. Two problems were found in
development and fixed before the verification pass:

* **Column boundaries.** Header rules are offset from the body rules on some pages; using
  them cut phonological/orthographic cells (e.g. 147 *atititekwa* came out as `tekwa`).
  Fixed by taking column rules from the table body only.
* **Combining-mark order.** The zero-width IPA93 marks (tilde, plus-below, grave, tilde
  below, diaeresis) share their x position with the *next* letter; sorting by x put some
  on the wrong letter (e.g. 359 [ɔ̃kwa] → `ɔk̃wa`, 618 [mũkɨtʃĩ’kwa] → `muk̃ɨtʃi’̃kwa`,
  1019 [w̟aɛna’kɛ] → `wa̟ɛna’kɛ`). Fixed by keeping each zero-width glyph with the
  preceding glyph of the content stream. 38 table rows changed; the 36 that are
  transcribed are all in the verification set below (the other two are the skipped
  sentence items 224, 225).

## 2. Second, independent reading

Rows checked: **240 table rows** (all transcribed rows; read on page images rendered at
170 dpi, without the extracted text; doubtful glyphs re-read at 400–600 dpi):

* stratified sample: 2 random rows from every one of the 85 pages (seed 20261104) — 170
  rows;
* plus every row whose phonetic cell changed under the mark-order fix (36 rows in the
  set, 6 of them also in the stratified sample);
* plus every row with a rare glyph (ʔ β ʰ ɪ ʊ ʷ ə ɯ ʙ ː, combining grave, tilde below,
  diaeresis) — 36 rows in the set;
* plus every row on the two pages set in the 8-bit SILManuscriptIPA font (PDF pp. 43, 48)
  — 25 rows in the set.

For each row the phonetic and phonological cells were typed from the image and then
compared with the extraction (script comparison, NFC). Glosses and the orthographic column
were checked by eye on the same sheets.

### Discrepancies

| page | item | extraction | first visual reading | resolution |
|---|---|---|---|---|
| 4 | 47 | [ikɛɾa’ɔ w̟æj] | [ikɛra’ɔ …] | r/ɾ: extraction kept (see below) |
| 22 | 268 | [uræɲũku’tæ] | [uɾæ…] | r/ɾ: extraction kept |
| 30 | 369 | [pɨpɨɾɨɛ’tʃi] | [pɨpɨɾiɛ’tʃi] | 600-dpi zoom shows ɨ: extraction correct |
| 31, 34 | 390, 434 | [mãmãj̃tɔ’kɔ] | [mãmãjtɔ’kɔ] | zoom shows tilde over j: extraction correct |
| 54 | 699 | [mɨ̃ɾɨkɨ’ɛ] | […ki’ɛ] | zoom shows ɨ: extraction correct |
| 57 | 738 | [aɛrɛti’kwa …] | [aɛɾɛ…] | r/ɾ: extraction kept |
| 61 | 789 | [… βækɔ’rɛ] | [… βækɔ’ɾɛ] | r/ɾ: extraction kept |
| 63 | 818 | [kuwinĩ tʃonũ] | [… tʃɔnũ] | zoom shows o: extraction correct |
| 71 | 920 | [w̟æræ’tæ tɛ’mũ] | [w̟æɾæ…] | r/ɾ: extraction kept |
| 81 | 1055, 1056 | […tsiturɔ’nĩ] | […tsituɾɔ’nĩ] | r/ɾ: extraction kept |
| 64 | 833 | [tʃutʃiraj /tʃutʃiɾa’ɛ] | [… / tʃutʃiɾa’ɛ] | **extraction error** (wrap after `/` lost its space); fixed in `kanoe_join.py` for all cells |
| 74 | 961 | [.mũ (classif. …)] | [..mũ (classif. …)] | **extraction error** (U+F02D draws two dots); map changed to `..` |

r vs ɾ: in SILManuscriptIPA93 the trill `r` (ASCII code) and the flap `ɾ` (U+F052) are
distinct glyphs that look nearly identical at screen resolution, so a visual reading cannot
decide between them; the code point in the file (i.e. the glyph Bacelar typed) is kept.
These 8 cases are reader errors, not extraction errors.

**Error rate of the extraction** in the 240-row set: 2 rows with an error (0.8 %), both
fixed globally (the `/`-wrap rule changed 3 phonetic cells: items 627, 831, 833; the
`..` glyph occurs in 1 Bacelar cell, item 961). After the fixes: 0 known discrepancies. The
phonological column (Times New Roman, standard Unicode) had 0 discrepancies.

## 3. Unclear readings (flagged in `Comment`)

* U+F0E3 read as ɯ (turned-m/turned-w shape in vowel position): items 625, 626, 628, 629.
* U+F0F5 read as ʙ: item 1092 `mõw mʙw` (probably a slip for `mõw mõw`).
* Item 446: the tilde of [p̃ene] is printed over `p` (phonological `pẽne`); kept as printed.

No row was skipped as unreadable.

## 4. Integrity checks

`avext.validate()`: no errors (IDs unique; every Language_ID/Parameter_ID resolves; every
Concepticon_ID exists in the frozen table with the matching gloss; Glottocode `kano1245`
exists; every `Source` key is in `sources.bib`; all files NFC). CSV well-formed
(constant column counts). merkmal `descriptive`: 0 invalid tokens in 1,004 filled
`Segments`.

## 5. Counts

| | n |
|---|---|
| table rows with data (items 1–1100 as printed: 3 numbers repeated, 4 skipped) | 1,098 |
| table rows transcribed | 1,094 |
| form rows | 1,117 |
| distinct forms | 754 |
| parameters (distinct gloss + translation) | 1,071 (1,066 distinct printed glosses) |
| Concepticon-mapped parameters | 411 (404 distinct concepts; 445 form rows) |
| rows with Segments | 1,004 |
| Segments empty: non-IPA material in phonetic cell | 14 |
| Segments empty: alternatives do not align | 31 |
| Segments empty: phonetic ≠ phonological form | 68 |
| loans marked | 18 |
| skipped: empty rows 1101–1106 | 6 |
| skipped: sentence glosses (224, 225, 227) | 3 |
| skipped: uninterpretable gloss (1048 *pejake*) | 1 |
