# Jahn 1927: Ayomán, Jirajara, Gayón and Timote vocabularies

**What it is.** These are the vocabularies in the Apéndice of:

> Jahn, Alfredo. 1927. *Los aborígenes del occidente de Venezuela: su historia,
> etnografía y afinidades lingüísticas.* Caracas: Lit. y Tip. del Comercio.

| Printed pages | PDF (0-based) | List |
|---|---|---|
| 379–387 | 458–466 | Vocabulario Ayomán (sections A–M; N. Frases) |
| 388–391 | 467–470 | Vocabulario Jirajara de Siquisique (Estado Lara) comparado con el Ayomán (3-column table) |
| 392–395 | 471–474 | Vocabulario Gayón comparado con el Ayomán y el Jirajara (sections A–G; H. Frases) |
| 396–405 | 475–484 | Vocabulario de la Lengua Timote, sections A–N (lexical). O. Frases (pp. 406–411) and P. Nombres geográficos (p. 412) are not transcribed. |

- **Scan:** https://archive.org/download/losaborgenesdelo00jahn/losaborgenesdelo00jahn.pdf
  (UNC Chapel Hill copy), sha256
  `d63b387f9485ad4ae84b21436f997e69e6f54a7f88ba43ffb15605821801083a`.
- **Page images:** the transcribed pages are in `pages/` (150 dpi greyscale,
  `page_379.png` … `page_405.png`).
- **Transcription:** transcribed by an AI agent from page images on 2026-11-04 and
  verified by a second independent reading (see `VERIFY.md`).
- **Background:** Jahn discusses his sources on pp. 6–7, 261–262, 272–273 and 325–327.

## Varieties

Jahn keeps the collectors apart, so each collector has its own row.

| ID | Name | Glottocode | Basis | Rows |
|---|---|---|---|---|
| `jahn1927_ayoman` | Ayomán (Jahn 1910) | `ayom1234` | Jahn's own forms, the first forms of each entry in the Ayomán vocabulary. Informant Carmen Ramos (d. 1913, aged 86), San Miguel, Lara, August 1910. Also 18 forms printed only in the Ayomán columns of the two comparison tables (see below). | 263 |
| `jahn1927_ayoman_oramas` | Ayomán (Oramas 1916, as quoted by Jahn) | `ayom1234` | Forms marked **(O)**: L. R. Oramas 1916, who combined his own 1916 notes from Distrito Urdaneta with Párraga's vocabularies. | 58 |
| `jahn1927_freitezpineda` | Ayamán vocabulary of Freitez Pineda 1907 | `jira1235` | Forms marked **(F)**. Jahn shows (pp. 6–7, 261–262) that this "Vocabulario Ayamán" mixes Jirajara words of Siquisique (Párraga) with Ayomán words of San Miguel, so only the language-level code is used. | 4 |
| `jahn1927_jirajara` | Jirajara (Siquisique) | `jira1249` | Jirajara column of the Jirajara table. Jahn traces the Siquisique words to Gen. Octaviano Párraga's list of c. 1880, printed by J. T. Pérez in 1886. Also 9 forms printed only in the Jirajara column of the Gayón table. | 96 |
| `jahn1927_gayon` | Gayón (Jahn 1910) | `gayo1245` | Gayón forms of the Gayón table. Informant Antolino Dobobuto, an old man of El Docoré (Bobare), 1910 (p. 273). | 72 |
| `jahn1927_timote` | Timote (Urrecheaga 1875–78; Jahn 1910) | `timo1263` | Timote vocabulary; see below. | 350 |

There is no Ajagua material in the source.

**Timote.** Jahn "classified and ordered" the words in the manuscript of bachiller R.
M. Urrecheaga, recorded 1875–78 among the Timotes of Timotes and the Mesa de
Esnujaque. He extended it with his own 1910 notes from two old speakers at the Mesa de
Esnujaque. He does **not** mark which words are his, so there is one row.

The Glottocode is `timo1263` (Timote), not `cuic1235` (Cuica). A. Fonseca published
the same Urrecheaga material in 1911 as "dialecto Cuicas". Jahn (p. 326) rejects that
label: "Lo que el doctor Fonseca ha llamado impropiamente dialecto 'Cuicas' es en
realidad la lengua de los Timotes".

One Timote form is marked "(F)": *El viento* "huer kúch (F)". Jahn gives no key for
(F) in the Timote list (in the Ayomán list it means Freitez Pineda; here Tulio Febres
Cordero is more likely). The form is kept on the Timote row and the Comment says so.

## Orthography (basis for a later profile; Segments left empty)

Jahn's key, printed at the head of the Ayomán vocabulary (p. 379), copied verbatim:

> El siguiente vocabulario fué tomado por nosotros de boca de la india Carmen Ramos,
> en San Miguel, en agosto de 1910.
>
> Hemos empleado en su escritura un alfabeto combinado, fonético, en el cual tienen
> los signos los siguientes sonidos:
>
> La h corresponde a la h aspirada alemana o la j española, la sh tiene el sonido de
> la inglesa o de la sch alemana, la ch tiene el sonido de la alemana, como en "ach",
> "nicht", ä ö tienen el sonido como en el alemán.
>
> Las voces anotadas y publicadas por los otros autores van marcadas así: (O) las de
> Oramas; (F) las de Freitez Pineda, y están a continuación de las nuestras que
> están en primer lugar.

**Scope of the key.**

- It is printed only with the Ayomán list.
- The Gayón list was taken down by Jahn in the same year (1910), and its spelling
  uses the same devices (h, sh, ch, ü, accents).
- The Oramas (O), Freitez Pineda (F) and Párraga/Pérez (Jirajara) forms use Spanish
  orthography (x, gu, qu, c), not Jahn's key.

**Timote spelling.** Jahn writes (p. 326): "La ortografía empleada es la original
[de] Urrecheaga y es la misma que hemos adoptado en las voces de nuestra propia
cosecha, a fin de dar uniformidad al presente estudio." There is no separate key. The
spelling uses k, sh, ch, ts, tch, w, f, ä/ö/ü and acute accents.

**Notation kept in `Form`.**

- Jahn's attached parentheses mark optional or weak sounds: `batá(h)`, `a-kíng(e)`,
  `s(h)pa shiú`, `tschég(h)`, `koñír(i)`, `im(i)na-shé`, `iñ(i)-gét`. These are part
  of his notation, not editorial brackets, so they are kept in `Form`.
- Hyphens (Jahn's morpheme divisions, e.g. the possessive `a-`, the Timote articles
  `ki-`/`kiu-`/`ti-`/`tit-`) and the apostrophe ’ (`t’bóp`, `k’sísh-kichsíso`,
  `sh’cut`) are kept as printed.

**Segments** are empty for every row.

## Conventions

- **Value and Form.** `Value` is the printed entry after the dash, or the table cell.
  `Form` is one form.
  - Entries are split on `;` (collector or alternative boundary) and `,`
    (alternatives).
  - Markers (O)/(F) select the variety row and are removed from `Form`.
  - Annotations printed after a space in parentheses are removed from `Form` and
    recorded in `Comment` with a note "printed annotation". Examples: "(cocui)",
    "(una mano)", "(cielo claro)", "(plural)", "(tener vergüenza)", "(no ya)",
    "(véase carbón)", "(tinaja)", "(flecha)".
- **Two glosses on one Timote line.** These are split into two glosses. For example
  `El padre—kiu-taita; mi padre—kustaita.` becomes `El padre` and `mi padre`.
- **Comparison tables.** The Ayomán column of the Jirajara and Gayón tables and the
  Jirajara column of the Gayón table mostly repeat the main lists, sometimes with
  different accents or hyphens.
  - A cell is **skipped** when its form, ignoring accents, hyphens and spaces, is
    already present for the same variety and concept. There are 112 such cells.
  - Otherwise it is kept, with Comment "from the … column of the … table". This
    applies to new glosses or new forms, for example Ayomán *Id. cascabel*
    huhí-tan-ña and Jirajara *Oreja* siguegá.
  - "(F)" in these columns sends the form to the Freitez Pineda row.
- **Glosses.**
  - `parameters.csv` `Name` is the Spanish gloss exactly as printed, including Latin
    names and Jahn's spellings (`Cathtartes`, `Tapirussp.`, `Lapa Coelogenys paca)`),
    then ` | ` and an English translation.
  - Identical gloss strings in different lists share one parameter (*Agua* in
    Ayomán, Jirajara and Gayón).
  - Ayomán *Verde* occurs as 'unripe' (adjectives, J) and 'green' (colours, K). These
    are two parameters.
- **Concepticon.** 408 of 603 glosses are mapped, covering 306 distinct concepts.
  - Possessed body parts ("Cabeza (mi)") and article-plus-noun glosses ("La
    cabeza") are mapped to the bare concept.
  - Person-marked verb glosses ("Comer (yo como)", "yo quiero", imperatives) are
    unmapped.
  - Regional plant and animal names are unmapped unless the Concepticon concept is
    exact.
- **Loans (`Loan = true`, 32 rows).** These are flagged where Jahn marks them
  ("(español)", "(del español)", "(esp.)", and fn. 1 on p. 389 'Del español "asada"'
  for Ayomán *asará*). The Spanish markings in the comparison tables are propagated to
  the matching main-list row (Ayomán *macét*). Loans are also flagged where the form
  is plainly the Spanish gloss word:
  - Ayomán: dios, diáblu, cachimbo, budare, kabayú, pá-ká, murá, kambrú, perú,
    pratán, maranzá, cedrú.
  - Jirajara: perú.
  - Timote: kus-kadera, júnes, nunis, kiu-trikú, kiu-kambure, kiu-pratán.

  Probable loans that are not identical to the gloss, such as Ayomán *buhrú* 'asno'
  (burro), are not flagged.
- **Doubt (3 rows).**
  - Ayomán *busí* is printed with "(?)".
  - Ayomán *Marido* has a second form *yami* after the unexplained abbreviation
    "Ban.".
  - Timote *stingui?* 'encontrar' is printed with "?".
- **Source.** Every row cites `jahn1927_jahn1927[page]`. Oramas, Freitez Pineda,
  Jirajara and Timote rows add the original collector's key (`jahn1927_oramas1916`,
  `jahn1927_freitezpineda1907`, `jahn1927_parraga1886`, `jahn1927_urrecheaga1878`).
  None of these originals was seen.

## Exclusions

| Class | Count |
|---|---|
| Phrases and sentences | 219 lines. Ayomán N. Frases 16 (p. 387). Jirajara phrases 12 (p. 391). Gayón H. Frases 6 (p. 395). Timote "Tengo sed—an marakoy na." in section L (1). Timote O. Frases pp. 406–411 ≈184 lines (counted from the text layer, not transcribed). |
| Toponyms | Timote P. Nombres geográficos, p. 412: 6 entries |
| Comparison-column repeats (see above) | 112 cells |
| Repeated printed entries identical to an earlier one | 2: Gayón *Sal* "chas." (B and G); Timote *Luego* "isméun." (C and N) |
| Printer's duplicate line | 1: Timote "La yerba santa (Chenopodium brosiodes)", a repeat of the preceding line |
| Comment line | 1: "Los criollos de Parupano llaman a este oso guarije." (p. 383) |

## Not included (out of scope, but in the book)

- The Mucuchí, Migurí, Mirripú and Torondoy material (ch. VI).
- The "Comparación de los dialectos andinos de Venezuela con los de Costa Rica, según
  Ernst" (pp. 415–416), which quotes Ernst 1885.

## Counts

- 843 form rows (831 distinct variety+form pairs): Ayomán 263, Oramas 58, Freitez
  Pineda 4, Jirajara 96, Gayón 72, Timote 350.
- 603 distinct glosses, of which 408 are mapped (306 distinct Concepticon concepts).
- Mapped concepts per row: Ayomán 156, Oramas 36, Jirajara 70, Gayón 50, Freitez
  Pineda 2, Timote 224.

## Licence

- **Jahn 1927.** Published in 1927, which is before 1931 and so US public domain.
  Alfredo Jahn died in 1940, more than 70 years ago, so the book is also public domain
  in Venezuela (60 years pma) and the EU (70 years pma). Licence:
  https://creativecommons.org/publicdomain/mark/1.0/.
- **Quoted forms.** The (O), (F) and Jirajara forms quoted by Jahn are factual data
  printed in this public-domain book. Oramas's own 1916 work was not used. His death
  year is unknown.

## Known identity issues

- **Ayomán (O) forms.** Oramas reused Párraga's vocabularies, so some (O) forms may be
  Jirajara rather than Ayomán.
- **Freitez Pineda.** Freitez Pineda's 1907 "Vocabulario Ayamán" is a known mixture;
  its forms are on a separate `jira1235` row.
- **Comparison-table alignments.**
  - The Ayomán column of the Gayón table pairs *kob-pá* (main list: 'muchacha') with
    *Muchacho*.
  - The tables also pair *batá* 'tinaja' with *Totuma grande*.
  - These are kept as printed, each with its comparison-column comment.
- **Timote vs Cuica.** The Timote list could be mislabelled "Cuica" by anyone
  following Fonseca 1911; it is Timote (`timo1263`).
