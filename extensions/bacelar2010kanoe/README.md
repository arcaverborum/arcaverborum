# bacelar2010kanoe — Kanoê (Kanoé), Bacelar's comparative tables

## Source

Bacelar, Laércio Nora. [2010]. *Língua Kanoé: tabelas demonstrativas da evolução das
transcrições (Zack 1942, Nimuendajú 1955, Becker-Donner 1955, Loukotka 1963, Bontkes
1967, Rodrigues 1986, Bacelar 1992–2008).* Etnolinguistica.Org, page `data:kanoe`.

* File: `http://etnolinguistica.wdfiles.com/local--files/data:kanoe/vocabulario_kanoe_comparado.pdf`
  (85 pp., PDF created 2010-02-05 with Acrobat Distiller; born-digital, landscape pages).
* sha256 `255bc99018f7bdfa3e21e71ce578942c6a79395dc2e045fbb594815bc7d79de0`.
* Pages used: all, pp. 1–85 (86 semantic tables, items numbered 1–1100; 1101–1106 are
  empty rows). `Source` gives the printed page number (= PDF page index + 1).

Each table row gives a Portuguese gloss and the forms of eight earlier/other columns.
**Only Bacelar's own three columns (1992–2008) were transcribed**:

| column | used as |
|---|---|
| *fonológica* (phonological) | `Form` (one row per `/`-separated alternative); full cell in `Value` |
| *fonética* (phonetic, IPA, blue) | `Segments` (see below); full cell copied into `Comment` as `phonetic: [...]` |
| *ortográfica* (orthographic, red) | `Comment` as `orthographic: ...` |

The third-party columns (Zack 1942, Nimuendajú 1955, Becker-Donner 1955, Loukotka 1963
*kapišana* and *kanoê*, Bontkes 1967, Rodrigues 1986) are **not** imported: they are other
authors' material (and Bacelar argues that Loukotka's Kapišana is not Kanoê).

## Transcription

Transcribed by an AI agent from the PDF text layer with explicit glyph remapping, checked
against page images on 2026-11-04; verified by a second, independent reading of 240 rows
from rendered page images (see `VERIFY.md`). Scripts:
`work/sa-isolates/scripts/ext/kanoe_extract.py` (cell extraction by the table rulings),
`kanoe_join.py` (line-wrap resolution), `kanoe_build.py` (CSV build), `kanoe_glosses.tsv`
(English translations and Concepticon mappings), `kanoe_vsheets.py` (verification sheets).

### Legacy-font glyph map

The phonetic column is set in **SILManuscriptIPA93** (a symbol font: its glyphs reach the
text layer as U+F0xx private-use codes) and, on pp. 43 and 48, in the older 8-bit
**SILManuscriptIPA** (glyphs reach the text layer as ASCII/Latin-1 letters). Every code
that occurs was located, rendered at 300–600 dpi and identified visually:

| SILManuscriptIPA93 | → | | SILManuscriptIPA (8-bit) | → |
|---|---|---|---|---|
| U+F045 | ɛ | | `E` | ɛ |
| U+F08D | ɔ | | `ç` | ɔ |
| U+F052 | ɾ | | `R` | ɾ |
| U+F0F6 | ɨ | | `ˆ` | ɨ |
| U+F0F8 | ɲ | | `¯` | ɲ |
| U+F053 | ʃ | | `S` | ʃ |
| U+F03F | ʔ | | `Q` | æ |
| U+F029 | combining tilde ◌̃ | | `)` | combining tilde ◌̃ |
| U+F02B | combining plus below ◌̟ | | `+` | combining plus below ◌̟ |
| U+F030 | combining tilde below ◌̰ | | `'` | ’ (stress) |
| U+F024 | combining grave ◌̀ | | | |
| U+F05F | combining diaeresis ◌̈ | | | |
| U+F0F9 | ː | | | |
| U+F042 | β | | | |
| U+F048 | ʰ | | | |
| U+F049 | ɪ | | | |
| U+F055 | ʊ | | | |
| U+F057 | ʷ | | | |
| U+F0AB | ə | | | |
| U+F0E3 | ɯ (see below) | | | |
| U+F0F5 | ʙ | | | |
| U+F02D | `..` (zero-width glyph drawn as two baseline dots) | | | |

ASCII letters, `æ` and `’` in the SIL93 font are themselves. The combining glyphs have zero
width and follow their base in the content stream; they are kept with that base (sorting
characters by x position alone misplaces them, which was found and fixed before
verification). In the IPA93 font `r` (trill) and `ɾ` (U+F052) are different glyphs that look
almost the same on screen; the code in the file was trusted (see VERIFY.md).
U+F0E3 is a turned-m/turned-w shaped glyph that occurs only in vowel position (items 625–629,
orthographic `ã`); it is read as ɯ and flagged `unclear` in `Comment`. U+F0F5 occurs once
(item 1092 `mõw mʙw`, a probable slip for `mõw mõw`) and is flagged.

The phonological and orthographic columns (Times New Roman) and the glosses (Courier) have
correct Unicode text layers. The reported "dropped vowel glyphs" were PUA codes that a plain
text extraction prints as nothing; they are all recovered by the map above.

### Conventions

* Everything is NFC; the forms are kept as printed, including Bacelar's inconsistencies
  (e.g. `kkykynu` 408/410, phonological `ñ`/`y` inside some phonetic cells, capitals
  `Ĩũkyty`, `Kwaatsie`). Hyphens of bound forms are kept (`-kwæn`, `-nake`).
* Line wraps inside a cell: a line that ends with a space in the text layer is a word
  boundary; a line without a trailing space continues the word, except 11 phonetic cells
  checked on the images (`SPACE_OVERRIDES` in `kanoe_join.py`) and wraps after `/`.
  Gloss wraps are joined with a space, without one after a hyphen, and without one for 14
  glosses broken mid-word (e.g. `formiguei|ro`); two line-end hyphenations were removed
  (`sobrance-lhas` → `sobrancelhas`, `borra-chudinho` → `borrachudinho`).
* Item numbers as printed are in `Local_ID`; the source repeats 243 (*fumaça* = 253),
  474 (*papa-formigas*) and 1017 (*tia*) and skips 409, 475, 510, 1042: the repeated
  numbers get a `b` suffix (`243b`, `474b`, `1017b`). One table note printed under the
  orthographic cell of item 210 (`(A sucuri está bonita)`) is left in the `orthographic:`
  comment.
* `Loan` = `true` for 18 forms that are transparently Portuguese (*pãw* 'pão', *kamitsa*
  'camisa', *tsapatu* 'sapato', *bitsicreta* 'bicicleta', *tserevetsa* 'cerveja', …). The
  source does not mark loans.

### Segments policy

The **phonological column is not IPA**: it is a practical phonemic spelling (`y` = /ɨ/,
`ñ` = /ɲ/, `v` for the advanced labial approximant, `ts` for [tʃ]~[ts], no stress). It is
kept as `Form`/`Value` and is **not** used for `Segments`.

`Segments` are filled from Bacelar's **phonetic column**, which the source explicitly prints
in IPA (stress written `’` before the stressed syllable). It is segmented by
`avext.ipa_segments` (base + diacritics/modifiers; stress `’` → `ˈ` kept as a prefix of the
following segment; spaces → `_`; bound-form hyphens dropped). `Segments` are left **empty**
(with the reason in `Comment`) when:

* the phonetic cell is empty or `-` (0 rows here);
* it contains non-IPA material — orthographic `ñ`/`y`, a note, the `..` glyph (14 rows);
* the phonetic and phonological cells give a different number of `/` alternatives (31 rows);
* the phonetic cell is not the same word as the phonological form: different number of
  words or a crude skeleton similarity < 0.8 (68 rows; e.g. item 167 *tsero* vs
  [tʃɛ’ɾɔ ækɨ’mũ], item 755 *tsoækypuae* vs [tsɔækɨpwa’ɛ i’tsɛ]). This includes rows that
  differ only in word division (compound written solid in one column, spaced in the other).

Thus `Segments` is the printed phonetic transcription of exactly the form in `Form`
for 1,004 of 1,117 rows. All filled tokens validate with merkmal (`descriptive`): 0 invalid.
Note that this is a phonetic, not phonemic, layer (e.g. [w̟], [tʃ], [ɔ], [ɛ] variants).

## Concepts

`parameters.csv` has one row per distinct printed gloss + English translation (1,071).
`Name` = the Portuguese gloss as printed ` | ` English translation (by the transcriber).
411 parameters (404 distinct Concepticon IDs, 445 forms) are mapped conservatively:
species names, possessed kin terms (*meu sobrinho*), vocatives, compound or list glosses
with several senses (*homem, macho, marido, masc*; *canoa, barco*), body-part subparts
and items whose form is not the gloss's word (961 *vinho* = liquid classifier *-mũ*) are
left unmapped. Item 124 *cotovelo* listed among the leg terms (form = 'knee'-like
compound) is a separate unmapped parameter.

## Exclusions

| class | rows |
|---|---|
| empty items 1101–1106 | 6 |
| sentence glosses (224 *Está chovendo...*, 225 *Choveu.*, 227 *É dia...*) | 3 |
| gloss not interpretable (1048, gloss cell repeats the Kanoê word *pejake*) | 1 |
| third-party columns (Zack, Nimuendajú, Becker-Donner, Loukotka ×2, Bontkes, Rodrigues) | not imported |

Result: 1,094 items → 1,117 form rows (23 extra rows from `/` alternatives), 754 distinct
forms. No proper names occur.

## Licence

`https://creativecommons.org/licenses/by/3.0/`. The file was posted by the author himself
on Etnolinguistica.Org (`data:kanoe`), whose footer states "Except where otherwise noted,
content on this site is licensed under CC BY 3.0"; the PDF carries no other notice. The
maintainer accepted CC BY 3.0 for these author-posted Etnolinguistica.Org files. The
licence covers Bacelar's own columns only; the third-party columns were not used.

## Identity

Glottocode `kano1245` (Kanoê, ISO 639-3 `kxo`), Rondônia, Brazil. Bacelar's columns
pool his fieldwork of 1992–2008. The Hugging Face "I Speak Kanoê" dataset (CC BY-NC-SA,
derived from Bacelar's works) was **not** used. The rows already in Arca for Kanoê
(johanssonsoundsymbolic, GLED) may themselves derive from Bacelar and are not
independent confirmation.
