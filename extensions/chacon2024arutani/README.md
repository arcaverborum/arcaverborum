# chacon2024arutani — Arutani dictionary (Chacon, Rosés Labrada et al. 2024)

## Source

Chacon, Thiago, Jorge Emilio Rosés Labrada, Juanita Martinez, Albino Xiriana,
Gabriel F. Soares, Gabriel F. Barros & Diego Cabral. 2024. *Dicionário Arutani -
Português - Español - English*. Zenodo. doi:10.5281/zenodo.14210239.

* File: `dic_arutani_portugues.pdf` (538 pp., born-digital, XeTeX 2022),
  <https://zenodo.org/records/14210239/files/dic_arutani_portugues.pdf>,
  sha256 `33184c812b32d2401c7e8eea2c0c24c3e83c7ef3763affd2c1c595f998e2b4a5`
  (md5 matches the Zenodo record).
* Pages used: the **Arutani–Português alphabetical section**, printed pp. 1–33
  (PDF pp. 4–36, 1-based). The Arutani–Español (pp. 35–61) and Arutani–English
  (pp. 63–88) alphabetical sections were parsed in parallel and are quoted in
  `Comment`. The reverse indexes, the thematic sections and the Ninam sections
  were not used.
* Speaker: Juanita Martinez (the dictionary's single voice), born in Makô on the
  upper Paragua (Venezuela), living in Saúba on the Uraricaá (Roraima, Brazil).
  Team: T. Chacon (compiler), J. E. Rosés Labrada (Spanish/English translation),
  A. Xiriana, G. F. Soares, G. F. Barros, D. Cabral.

## Licence

CC BY 4.0, as declared on the Zenodo record
(`https://creativecommons.org/licenses/by/4.0/`).

## Variety

One variety, `arutani` → **arut1244** (ISO `atx`). Glottolog's dialect nodes Uruak
(urua1245) and Awake (awak1251) are not used: the dictionary does not identify the
speaker's variety with either.

## What a row is

One row per **sense** of a headword in the Arutani–Português section (numbered
senses `1.`, `2.` … become separate rows; `Local_ID` = entry.sense, counting
entries in printed order, homographs included).

* `Form` = the headword as printed (bold), bound-form hyphens kept.
* `Value` = headword + every bracketed transcription as printed, e.g.
  `aay [aˈʔaj] [ɾaˈʔajni] [ɾaʔaj]`.
* `Parameter`: `Name` = the Portuguese gloss as printed (final full stop removed)
  `|` an English translation made from the Portuguese. The English is not the
  dictionary's English section: that section (and the Spanish one) often has
  missing glosses and **numbers the senses of polysemous entries in a different
  order** from the Portuguese (e.g. *aman* pt 1 *suave*, 2 *cansado*; en 1 *tired*,
  2 *soft*), and occasionally mistranslates (*akwap* 'galho' → en "rooster").
  The Spanish and English glosses of the whole entry are therefore quoted
  verbatim in `Comment` (`es: …; en: …`, `—` for an empty sense) instead of being
  paired with a Portuguese sense.
* `Comment` also gives the part of speech as printed (`POS: nome`), the sense
  number (`sense 2 of 3`) and loan notes.
* Examples and their translations are not transcribed.

## Segments

The dictionary prints a phonetic transcription in square brackets for every
headword (IPA, stress `ˈ`/`ˌ`, `ʔ`, `ʃ`, `ɾ`, `ɲ`, `ɐ̃`, `j̃`, `ʷ`, `ʰ`, `ˀ`,
superscript transitional vowels). `Segments` is filled from the **first** bracketed
transcription (`Comment` says so when there are several; for `[a / b]` the first
alternative), segmented with `scripts/ext/avext.py::ipa_segments`:

* a segment is a base character plus following combining diacritics and modifier
  letters (`ʷ ʰ ʲ ˀ ː`, superscript vowels); stress marks are prefixed to the
  following segment (`a ˈkʷ a n`); syllable dots are dropped; a space becomes `_`;
  edge hyphens (`[-pa-]`) are dropped.
* 80 rows have a bracketed transcription identical to the spelling and without
  stress (e.g. `akoan [akoan]`). Where every letter of the spelling is also an IPA
  symbol with the same value, Segments are filled and `Comment` notes
  "bracketed transcription identical to the spelling". Where the spelling uses
  orthographic letters (`x y ñ r ë nh ch`, acute accents), Segments are left empty
  (2 rows: *akanho*, *ië*).
* 1,059 of 1,061 rows have Segments. merkmal (`descriptive`) rejects 4 tokens, all
  printed superscript transitional vowels (`kᵄ`, `kᵉ`, `mⁱ`, `sᵄ`); they are kept
  as printed.
* The transcription is printed as is: it is sometimes inconsistent with the
  spelling (e.g. *kitoho taxo* `[taˈʃɐ̃n]`, *tio* `[matiˈo]`, *nai* `[kĩnãˈãj]`).

## Text-layer repairs (born-digital PDF)

The text was taken from the PDF text layer (`scripts/ext/arutani_parse.py`,
PyMuPDF raw characters with fonts and positions). The following were found by
comparison with rendered pages and repaired:

| text layer | printed glyph | repair | where |
|---|---|---|---|
| `ᖯ` U+15AF | ʃ | → `ʃ` | IPA brackets (wrong ToUnicode for the esh glyph) |
| `ϐ` U+03D0, `ϔ` U+03D4 | f (roman / italic) | → `f` | Portuguese/Spanish/English text (*flecha*, *ficar*, *fish*) |
| `ı` + combining mark | ĩ, í | → `i` + mark | dotless i with tilde/acute |
| `ȷ` + combining tilde | j̃ | → `j` + tilde | nasal glide in IPA |
| U+2011 | - | → `-` | non-breaking hyphen |
| gap without space | word space | insert space | justified lines with no space character |

Combining diacritics follow their base in the text layer and render over it;
they needed no reordering (checked: no mark follows a space or bracket). The
glyph shown for `ɐ` (U+0250, Cambria glyph 6283) looks like `e` at low resolution;
the embedded font outline was inspected and it is a turned `a`, so `ɐ` is correct.
Line-final hyphens were removed when joining hyphenated words, except at real
compound hyphens (list `KEEP_HYPHEN` in the parser: *pica-pau*, *gavião-real*,
*tamanduá-bandeira*, *esquecer-se* …). Page folios that interrupt a hyphenated
word were dropped.

Printed oddities kept as printed: *tubeŕrculo* (akwa), *pedaços47;peças* (kaxa,
a stray HTML entity in the original), *utensí́lio* (raiyu hani), *ma ndioca*
(õya ĩhã), and the headwords *ãrãk ã aˈtsa* and *arutaˈniñu* (stress mark
printed inside the bold headword).

## Exclusions (69 senses)

| reason | senses |
|---|---|
| grammatical morphemes / labels (OBJ, DIR, copulas, person prefixes, FUT, causative, negative future, reportative …) | 39 |
| toponyms (rivers, waterfalls, villages) | 11 |
| ethnonyms | 9 |
| unknown meaning (`?`, `????`) | 4 |
| proper names | 2 |
| glossonym (*Arutani kiwa*) | 1 |
| gloss is a native plant name only (*anipa* "Mõrãmãhĩ") | 1 |
| unclear gloss (*arikawan* 1. "yekuana") | 1 |
| no Portuguese gloss (*naaika* 4.) | 1 |

Example sentences and their translations are not transcribed; descriptive glosses
(e.g. "fruta da família do cacau; peludinha …") are kept, unmapped.

## Concepts

982 distinct (gloss, translation) parameters; 556 mapped to Concepticon (527
distinct concept sets; 617 of 1,061 rows). Mapping was done by hand from the
Portuguese sense, conservatively: species names, possessed kin terms (*meu pai*),
mixed senses (*argila, panela de barro*), and descriptive glosses are unmapped;
kin terms are mapped only to the exact Concepticon set (e.g. *tio paterno, mais
novo que o pai* → PATERNAL UNCLE (FATHER'S YOUNGER BROTHER); *tia, irmã mais nova
da mãe* unmapped). The reviewed decisions are in
`scripts/ext/arutani_decisions.tsv`.

## Loans

`Loan = true` for 11 rows whose identity with the Portuguese/Spanish gloss is
obvious: *arotsa* 'arroz', *asuka* 'açúcar' (not the homograph 'lagarta'),
*kutxaraya* 'cuchara', *mahtera* 'martelo/martillo', *mareta* 'maleta', *motoro*
'motor', *parito* 'palito', *rimaw* 'limão', *sambrero* 'sombrero' (2 senses),
*teosi* 'Dios'.

## Who and how

Extracted by an AI agent from the PDF text layer on 2026-11-04, with glyph repairs
verified against rendered pages; verified by a second independent reading of a
stratified sample and of every repaired row (see `VERIFY.md`). Scripts:
`work/sa-isolates/scripts/ext/arutani_parse.py`, `arutani_build.py`, `avext.py`.

## Known issues

* Single speaker, a rememberer-level situation (about 20 people of the ethnic
  group; the dictionary says Juanita Martinez is fluent).
* Spanish/English sense numbering differs from the Portuguese for some
  polysemous entries; see above.
* Some bracketed transcriptions simply repeat the spelling (80 rows) and are
  unanalysed.
* Koch-Grünberg's 1911–13 Auake list (1928) is a separate, historical source and
  is not included here.
