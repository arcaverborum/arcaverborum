# Guamo word list of 1788 (*Lenguas de América*, 1928)

**What it is.** "Traduccion de algunas voces de la lengua Guama": an anonymous
Spanish–Guamo list. It answers the Spanish questionnaire of the Real Orden of 1787
(the Catherine II / Pallas comparative list as circulated in New Granada). The
printed title page reads "Año de M. DCC. LXXXVIII", and the colophon reads "Copiado á
la letra en Santa Fé de Bogotá … Hoy Martes 9 de Diciembre de 1788, por F. X. C.".
The list is therefore dated **1788**. The "1778" found in Glottolog, Wikipedia and
Wiktionary is an error. The manuscript is in the Real Biblioteca, Madrid, and was
printed diplomatically in:

> [Real Biblioteca]. 1928. *Lenguas de América. Manuscritos de la Real Biblioteca*,
> tomo I (Catálogo de la Real Biblioteca, t. VI). Madrid: Gráficas Reunidas
> (colophon 21 June 1927), pp. 381–393.

- **Pages:** title p. 381; list pp. 382–392 (PDF pages 397–407, 0-based); compiler's
  notes pp. 392–393. The pages used are in `pages/` (150 dpi greyscale,
  `page_381.png` … `page_393.png`).
- **Scan:** https://archive.org/download/lenguasdeamerica01spai/lenguasdeamerica01spai.pdf
  (University of Illinois copy), sha256
  `9d55f11aeb0f15cd29aae4e6745432ee583d3d9d5174abf0edd5590203999f88`.
- **Transcription:** transcribed by an AI agent from page images on 2026-11-04 and
  verified by a second independent reading (see `VERIFY.md`).

## Varieties and the dialect convention

The compiler states the convention for doublets on p. 392:

> "En esta version van algunas voces duplicadas, esto es, como las traducen los Guamos
> de un Pueblo y los de otro. Las primeras son del Pueblo de Santa Rosa, a las margenes
> del Rio Masparro; y las segundas, del de San Josef, a las de este Rio Santo Domingo."

| ID | Name | Glottocode | Content |
|---|---|---|---|
| `guamo1788_santarosa` | Guamo (Santa Rosa) | `sant1461` | first member of every `A ô B` entry (179 rows) |
| `guamo1788_sanjose` | Guamo (San José) | `sanj1287` | second member of every `A ô B` entry (178 rows) |
| `guamo1788_unspecified` | Guamo (village not stated) | `guam1236` | single-form entries and the third member of the one three-way entry (136 rows) |

**Forms without a doublet.** The note assigns only duplicated words. It does not say
whether a single form belongs to one village or to both. The compiler also writes
that Guamo of different villages "varian bastantes voces, pero se entienden
reciprocamente", so a single form cannot be assumed to be shared. These forms are
therefore attached to a third row with the language-level Glottocode `guam1236`. A
plausible but unstated reading is that they are common to both villages. A later
reviewer may adopt it. The one three-way entry is *Pesado* "Quiestaman ô Maquiestaquê
ô Cuerá". Its first two members follow the convention, and *Cuerá* goes to the
unspecified row with a comment.

## Conventions

- `Value` is the full printed Guamo entry, including the final period. `Form` is one
  alternative. Entries are split on the printed separator `ô`, which is a circumflex o
  on every page (both readers agree), and on a comma (only *Cerca*: "Tista, ascocam ô
  Tistá"). Capitalisation, accents and circumflexes are kept as printed (`Texê`,
  `Sagarû`, `Napüe`). The text is Unicode NFC.
- **Ditto entries.** The list uses *dicho/dicha* ("the same") in two ways:
  - `X ô dicho`: the San José form equals the Santa Rosa form. The San José row
    repeats `X`, and the Comment records the ditto. There are 8 such entries.
  - A whole entry `Dicho.`: the form of the preceding printed entry. *Helada* and
    *Hielo* follow *Frio* (Tauchista), and *Plomo* follows *Estaño* (Catarafú). The
    form is materialised on the same variety row as the preceding entry, with a
    Comment.
  - `Discú ô dicha Cataruscu` (*Palo (Raiz)*): the San José form is given as
    `Cataruscu`, with `Doubt = true` and a Comment. It may mean "Discú Cataruscu".
- **Segments is empty** for every row. The spelling is colonial Spanish orthography.
  The compiler says (pp. 392–393) that the Guamo have nasal and guttural aspirations
  and "sonsonetes" that the spelling cannot represent ("sin ser posible descifrarlos
  sino a viva voz"). The copy is "escritas con la misma ortografia que estaban en el
  original", that is, a copy of a copy.
- **Glosses.** `parameters.csv` `Name` is the Spanish gloss as printed (`Hermanc`,
  `Muger`, `Yr`, `Oja`, `Agugero`, `Hibierno` and so on), then ` | ` and an English
  translation.
  - Two printed glosses occur twice with different senses and are kept as separate
    parameters: *Mañana* (p. 387 'morning', p. 392 'tomorrow') and *Baxo* (p. 385
    'low', p. 391 'under').
  - 263 of 313 glosses are mapped to Concepticon. The mapping is conservative:
    person-marked verb forms (*Yo como*, *Tu eres* …), imperatives, abstract sense
    nouns (*Oido*, *Vista*, *Gusto* …) and ambiguous glosses (*Muger*, *Viejo*,
    *Tarde*, *Sombra* …) are unmapped.
  - *Verano* and *Hibierno* are translated "summer (dry season)" and "winter (rainy
    season)", following the compiler's own explanation (p. 392).
- **Loans.** `Loan = true` only where the form is identical to the Spanish gloss:
  *Mesa* (Mesa), *Pan* (Pan) and *Rey* (Rei). This is 3 rows. Other probable loans,
  such as *Buei* "Guei", *Vaca* "Paca", *Asno* "Mura" and *Semana* "Misa", are not
  flagged.
- **Source.** Each row cites `guamo1788_anon1788;guamo1788_realbiblioteca1928[page]`.

## Exclusions

| Class | Count |
|---|---|
| Printed gloss lines with an empty Guamo column ("Los vocablos que no llevan version, es porque no los usan", p. 392) | 125 |
| Repeated printed entry identical to an earlier one (*Frio* "Tauchista." on p. 386, already given on p. 385) | 1 |
| Phrases, proper names | 0 (none in the list) |

## Counts

- 439 printed gloss lines, of which 314 are filled.
- 493 form rows (479 distinct variety+form pairs).
- 313 distinct glosses, of which 263 are Concepticon-mapped. Mapped concepts per row:
  Santa Rosa 154, San José 154, unspecified 110.

## Licence

The list was written in 1788 and the manuscript is anonymous. The 1928 printing is a
diplomatic institutional edition with no individual editor-author, published before
1931, so it is in the US public domain. The original text is public domain
worldwide. Only the 1788 forms and Spanish glosses are transcribed here; no editorial
material from 1928 is taken. Licence:
https://creativecommons.org/publicdomain/mark/1.0/.

## Known issues

- **Copy errors.** This is a copy of a copy, and copyist errors are likely. Some
  pairings look odd but are printed as given: *Número* "Quete"; *Dos* "Quete ô
  Diquiampa"; *Mil* "Taugui", although the compiler says the Guamo count only to
  five; *Lobo* "Catapenx" and *Liebre* "Catapeux".
- **Substituted concepts.** The compiler says some concepts were substituted or left
  blank because no equivalent was used (Oveja, Camello and others are blank).
- **Not independent sources.** The Wiktionary "Appendix:Guamo word list" and ASJP
  "GUAMO" derive from this same list.
