# Yurumanguí vocabulary of Fr. Christoval Romero (1768)

**What it is.** The only record of Yurumanguí (`yuru1243`, an isolate). It is a list of
words and short phrases that Fr. **Christoval Romero** wrote down in 1768. It accompanies
the expedition diary of Capt. Sebastián Lanchas de Estrada. The manuscript is in the
Archivo Nacional, Bogotá, *Curas y Obispos* t. 44, fol. 218v–221r, and a second copy is
in the same volume. Its heading (printed by Rivet, p. 10) reads:

> "Lengua de los Yndios Gentiles que havitan los Rios de Yurumangui, Cajambre, Naya,
> San Vicente, San Nicolas, el Palmar, y San Carlos; Traducida por los Padres
> Missioneros a cuyo cargo esta esta Mission"

Some secondary literature names the author "Dadey". Rivet, Urban (2019) and the
manuscript heading do not support that name. The author is Romero.

**Edition used.** Rivet, Paul. 1942. "Un dialecte hoka colombien: le Yurumangí."
*Journal de la Société des Américanistes* n.s. 34: 1–59. The vocabulary is on
**pp. 10–19**, and Rivet's statement of his conventions is on pp. 9–10.

- **Scan:** https://archive.org/download/societe-des-americanistes-journal_1942_32/societe-des-americanistes-journal_1942_32.pdf
  (the archive.org item is mislabelled "Vol 32"; the title page reads *Nouvelle série,
  tome XXXIV*). The scan's sha256 is
  `6c6648e1a4af3faeb4f1d2bc4b4f3945c715cddcd7e7f47fc1b5398748bd079a`. Printed page =
  PDF page (1-based) − 4.
- **Page images:** the pages used are in `pages/` as `page_009.png` … `page_019.png`
  (150 dpi greyscale).
- **Transcription:** an AI agent transcribed the list from page images on 2026-11-04.
  A second, independent reading verified it (see `VERIFY.md`).

## What was taken from Rivet, and what was not

Rivet reordered Romero's list alphabetically by **French** gloss and cross-listed many
entries under several headings. For each entry he printed three things:

1. his own "notation phonétique", an italic respelling with `k` for c/qu, `x` for g/j,
   `č` for ch, added accents, and hyphens that segment the word into what he took to be
   morphemes;
2. **Romero's original spelling in square brackets**;
3. a French translation. He added the **Spanish original gloss** in brackets only
   "quand cette traduction a prêté à doute" (p. 9).

Asterisks mark the variants of the second manuscript copy.

This extension takes **only the 1768 layer**:

- **Forms** are Romero's bracketed spellings, exactly as printed.
- **Glosses** are the Spanish originals wherever Rivet printed them.

It **never** takes Rivet's notation as a form, nor his segmentation, his "[cf. …]" and
"[= …]" cross-references and analyses, his footnotes (including his correction of a
supposed sense inversion on p. 19), his comparisons, or his Hokan material.

**Known limits of this approach. These need the maintainer's review.**

1. **Most glosses are in French, not Spanish.** Rivet printed the Spanish original
   for only 38 of the 159 kept entries.
   - Where Spanish is printed, `parameters.csv` `Name` is the Spanish gloss as printed
     (e.g. `guadua`, `colino de platano`, `esta lexos`).
   - For the other 121, the only printed gloss is Rivet's French translation, and
     `Name` gives it as printed (e.g. `aiguille | needle`). A translated one-word gloss
     identifies a meaning; it is not Rivet's analysis. However, it is the editor's
     wording, not Romero's. If the maintainer rules that only Spanish glosses may be
     used, these 121 parameters (and their forms) must be dropped. They can also be
     re-glossed from another witness of the Spanish (Ortiz 1946, Arcila Robledo 1940,
     or the manuscript).
   - The section "Gloss language by parameter" below lists every Spanish-glossed
     parameter. All the others are French.
2. **Unbracketed forms (37 rows in 31 entries, 28 of them with no bracketed form at all; `Doubt = true`).** For some entries Rivet printed
   only his italic form, with no bracketed original (e.g. *aia* 'eau', *yaa* 'sang',
   *maa* 'père', *minni* 'terre').
   - He does not explain this. The obvious reading is that the manuscript spelling is
     identical apart from his hyphens. Such forms contain no `k`/`x`/`č` respellings.
   - However, the brackets show that his notation sometimes also adds accents and
     spaces that the manuscript lacks (*nom-sub-si-à* = [*nomsubsia*]; *kua tua-me* =
     [*cuatuame*]).
   - These forms are therefore kept with his hyphens removed. Each is flagged
     `Doubt = true` with a Comment.
   - They can be dropped by filtering on `Doubt` if the maintainer prefers only
     bracketed originals.
3. **Gloss–form pairing.** The pairing is Romero's, and Rivet already noted it is
   loose (p. 9). Romero elicited by pointing and by overheard phrases. Urban (2019)
   adds that the material may contain foreigner talk.

## Conventions

- **One variety:** `romero1768_yurumangui`, Glottocode `yuru1243`. The heading covers
  several rivers. Neither copy tags any form by river, so no dialect split is
  possible.
- **`Value`** is the 1768 layer of the entry: the bracket content as printed (e.g.
  `aumisa, *aumissa`).
  - Multi-line entries are joined with ` ; ` (*jaguar*, *jour*).
  - For an unbracketed form, `Value` is Rivet's printed italic form, hyphens included,
    because that is all that is printed.
  - **`Form`** is one alternative, without asterisk or hyphens. Spaces inside a
    bracket are kept (`sipia sinaisa`, `cayen yepa`, `cueba canana`).
- **Second-copy variants** (`*`) get their own row with the Comment "variant of the
  second manuscript copy".
  - *sœur*: the bracket reads `[ataiza, ataisa]` with no asterisk, although Rivet's
    notation stars the second form. It is transcribed as printed, and the Comment
    records the mismatch.
- **Accents and special letters are kept as printed:** `chumaé`, `conoteá`, `lamá`,
  `caienaiè`, `acá`, `auciá`, `yaré`, `bisià`.
  - The italic `z` is printed with a descender (ʒ-like). It is the ordinary letter z;
    the Spanish glosses *azote* and *dar azote* use the same glyph.
  - Two forms print `š` (*maiša* 'nuit', *niniluša* 'refregar'). Both are transcribed
    as printed. The manuscript letter behind it
    is unknown.
- **`Segments` is empty for every row.** The spelling is 18th-century Spanish
  missionary orthography, and Urban (2019: 3) shows it is too inconsistent for
  phonological inference. Rivet's notation is not adopted as a reading. An
  orthographic profile, if one is ever made, is a later reviewed step.
- **`Source`** for every row is `romero1768_romero1768;romero1768_rivet1942[p]`, with
  p the printed page.
- **`Loan`** is empty everywhere. The source marks no loans, and no form is
  identical to its Spanish gloss.
- **Cross-listed forms.** When the same original spelling is printed under several
  different glosses, each gloss gets its own row, and the Comment names the other
  glosses. Examples: *bicaisa* under 'calentura ó calor fuerte', 'chauffer' and
  'calentura'; *sipia sinaisa* under 'âme' and 'respiration'; *baisina* under
  'cuchillo, navaja' and 'navaja'; *sicona* under 'jour' and 'soleil'. These may be one
  manuscript entry that Rivet listed twice. When the *same* gloss and form are printed
  twice (Rivet's cross-listing), only one row is made.

## Exclusions (counts in `VERIFY.md`)

- **Phrases and sentences (85 printed lines):** questions, person-marked clauses,
  negated forms, requests with objects ("apporte-moi une banane", "tu veux manger",
  "il n'est pas ici", "je ne l'ai pas vu" …), including Rivet's cross-listed repeats of
  them.
  - Kept as single concepts: infinitives, nouns and noun compounds, "être + adjective"
    and "chose + adjective" predicates, impersonal *être en train de pleuvoir*,
    single-verb imperatives without object pronouns (*bois !*, *mange !*, *entre !*,
    *prends !*, the reflexives *assieds-toi !*, *éloigne-toi !*, *lève-toi !*), and the
    Spanish predicates *esta lexos* and *esta rota con agujeros*.
  - Borderline items skipped: *il est couché* (*umu, uma, \*umu buma*), *il est mort
    [ya murió]* (*saibai*), *boire du masato* (*sisa*), *deux mois* (*digia digia*), and
    *voici [ai está]* / *[ahi tienes]*. They are listed in `VERIFY.md`.
- **Duplicate cross-listings of kept items (4):** *banane mûre* (p. 16), *planche de
  bambou* and *plant de bananier* (p. 17), *tabac allumé* (p. 18).
- **Proper names, toponyms, ethnonyms:** none in the list.
- **Unreadable rows:** none.

## Licence

`https://creativecommons.org/publicdomain/mark/1.0/`.

- **The 1768 forms and Spanish glosses are in the public domain.** Romero wrote them
  in 1768.
- **Rivet's 1942 article is still in copyright** (Rivet died in 1958, so it is
  protected in France until the end of 2028).
- Under the maintainer's decision for this batch, public-domain original forms may be
  taken from a later copyrighted edition if *only* the original layer is transcribed.
  That is what is done here (see above). Both the 1768 manuscript and Rivet 1942 are
  cited. The French glosses are the open question, raised under "Known limits", item 1.

## Gloss language by parameter

The **38 Spanish-glossed parameters** (Spanish printed by Rivet) are, by `ID` suffix:

8 guadua, 12 colino de platano, 13 bordón, 14 dar azote, 15 muchisimo, 20 cualquier
palo, 22 cogollo de palma, 23 mate, 26 calentura ó calor fuerte, 35 cualquier puro,
41 coser, 42 azote, 44 cuchillo, navaja, 45 colmillo, 47 dardo, 48 asco, 58 el
abentador, 63 la candela o fuego, 64 calentura, 71 refregar, 74 dar de bofetones,
84 levantarse, 85 levantate, 87 esta lexos, 91 tusa, 99 malo, 102 embustero,
106 rezungar, 114 gavilán, 116 oidos, 117 cualquier papel o carta, 126 navaja,
133 afeitar, 135 sacar alguna cosa, 136 volverse, 145 asiento, 154 las trompas,
155 esta rota con agujeros.

All other parameters carry Rivet's French gloss as printed.

**Maintainer decision (2026-11-04):** rows for which Rivet prints only his own respelling (no bracketed 1768 original; 37 rows) are removed: they are the editor's readings, which the rule for later editions excludes. French glosses are kept: they are Rivet's translation of the meaning and serve only for concept mapping; every form is Romero's.
