# dangelis2010arara — Arara do Rio Branco lexicon (D'Angelis 2010)

## Source

D'Angelis, Wilmar da Rocha. 2010. *Arara do Rio Branco (MT), tb Arara do Aripuanã:
tentativa de estabelecer algumas raízes, morfemas e relações semânticas.*
Etnolinguistica.Org, page `data:arara`, file `arara_lexico.pdf` (7 pp., PDF dated
2010-02-01, "Página 1"–"Página 7"; all pages used).

* URL: <http://etnolinguistica.wdfiles.com/local--files/data:arara/arara_lexico.pdf>
* sha256 `81b06ea82e27e737b1185be09f14749d62452bdf54f3650f8a9e7e59d944f53c`
* Context (not transcribed): `arara_cultura.pdf` on the same page — elicitation
  in 2007 from three rememberers, revising an earlier CIMI list; it also explains
  the exclusion of Tupi-Mondé intrusions.

The PDF is a born-digital spreadsheet export: a table *Português* | *Arara (Raiz)* |
*Itens relacionados* (gloss + form) | marginal notes `(*)`, arranged by theme
(pronouns, body parts, adjectives/kinship, verbs, nature, objects/food, fauna, flora).
Forms are phonetic transcriptions in square brackets.

## Licence

CC BY 3.0 (`https://creativecommons.org/licenses/by/3.0/`): the Etnolinguistica.Org
site footer ("Except where otherwise noted, content on this site is licensed under
CC BY 3.0"); the file was posted by the author on a `data:` page. Accepted by the
maintainer.

## Variety

`ararariobranco` → **mato1253** (Mato Grosso Arára, ISO `axg`). Not the Cariban
Pará Arára, not the Tupi-Mondé Arara of Rondônia, not Kwaza.

## Legacy font: glyph → Unicode map

The transcriptions are set in Helvetica plus the legacy Mac font **IPAKiel**
(regular and bold) and a few Arial glyphs. Every IPAKiel glyph occurring in the file
was rendered in context (≥ 800 dpi for the diacritics) and mapped explicitly
(`scripts/ext/arara_extract.py`):

| text layer | printed | Unicode |
|---|---|---|
| `"` | primary stress | ˈ U+02C8 |
| `Æ` | secondary stress | ˌ U+02CC |
| `)` | tilde over the preceding letter | U+0303 |
| `0` | tilde **below** the preceding letter | U+0330 (creaky) |
| `}` | unreleased mark | U+031A |
| `°` | tie bar between two letters | U+0361 |
| `§` | up tack below | U+031D |
| `/` | ʔ | U+0294 |
| `E I N O S U Z` | ɛ ɪ ŋ ɔ ʃ ʊ ʒ | |
| `|` | ɾ | U+027E |
| `´` | ə | U+0259 |
| `È` | ɨ | U+0268 |
| `å` | ɐ | U+0250 |
| `√` | ʋ | U+028B |
| `≠` | ɲ | U+0272 |
| `]`, space | `]`, space | |
| Arial U+F022 | dot below the preceding letter | U+0323 |

Combining glyphs are zero-width and drawn back over the preceding letter, so they
follow their base in the text layer. Superscript letters (smaller size, raised
baseline) are written as modifier letters: ᵐ ⁿ ᵑ ᵇ ᵈ ᵘ ᵋ, and a superscript ʔ as ˀ.
Plain Helvetica `r` is printed (and kept) where the author did not use ɾ
(e.g. *pau em pé* `[murutuˈpi]`, *comer* `[ˈmprajə]`); one cell prints the stress
as a plain `"` (`[murutu"pi]`), kept in Value/Form.

## What a row is

One row per printed (gloss, transcription) pair:

* root-column entries (*Português* gloss + *Arara (Raiz)* form) and related items
  (*Itens relacionados*: italic gloss + form) are both rows; `Comment` says which;
* alternatives in a cell (`~`, `;`, `,`, `ou`, parenthesised variants, a second
  line) are one row each, with the same `Value` (the whole cell as printed);
* `Form` = the transcription without the square brackets;
* marginal notes are quoted in `Comment`; two notes give a form for a new gloss
  (`tb anotei "pênis" = [nụpika]`; `v. "porco grande" = [beˈbɛ]`) and are rows;
* `Parameter.Name` = the Portuguese gloss as printed (the note asterisk removed) |
  English translation.

## Segments

The source prints an explicit phonetic (IPA-based) transcription, so `Segments` is
filled (245 of 246 rows; the exception is *cartucho* `brikati`, printed without
brackets) with `avext.ipa_segments`: stress marks prefixed to the following
segment, spaces → `_`; superscript nasals before a stop are joined to that stop as
prenasalisation (`ᵐb`, `ⁿd`, `ᵑg`); other superscripts stay on the preceding
segment; `:` → `ː`, plain `"` → `ˈ` (Segments only). merkmal (`descriptive`)
rejects tokens in 24 rows: coda superscripts (`ᵇᵐ̚`, `bᵐ̚`, `ᵈⁿ̚`), dot-below
vowels (`ụ`, `ị`, of unknown value), `ᵑg`, `n͡d`, `ᵘ`, `ᵋ`; kept as printed.

## Exclusions and duplicates

* 9 "root" cells marked `*` by the author (`* [nu]` 1sg, `* [tũ]` 3sg, `* [ˈpaj]`
  'grande', `* [tik]` 'pequeno', `* [peb]` 'azul', `* [kuˈpe]` 'negro', `* [baˈja]`
  'masculino', `* [ta] ~ [tak]` 'planta', `* [ᵐbɾi]` 'arma') are the author's
  abstracted roots, not attested words: skipped.
* 43 cells repeat an earlier identical gloss + transcription (the table
  cross-lists items under several roots): transcribed once.
* Cross-reference notes (`ver "ouvido" = [biko]`, `cf. tracajá` …) and the
  author's hypotheses (`provável [biɾip-tuˈpi]`, `seria [mũrũˈʃjɔ̚] ?`) are quoted
  in `Comment` only.
* No proper names; nothing unreadable.

## Concepts

187 glosses, 91 mapped to Concepticon (132 of 246 rows). Possessed forms
(*minha nora*, *meu braço*), species and descriptive glosses are unmapped.

## Who and how

Extracted by an AI agent from the PDF text layer on 2026-11-04 with an explicit
legacy-font map verified against rendered pages; verified by a second independent
reading of every kept row (see `VERIFY.md`). Scripts: `scripts/ext/arara_extract.py`,
`arara_rows.tsv` (curated table), `arara_build.py`.

## Known issues

* Rememberer data, partly tentative (the author's own `?` notes are quoted).
* `nariz` and `nariz (venta)` share `[nuˈɲɐ̃]`, a possessed form.
* Three readings with stacked diacritics are unclear on the page and follow the
  text layer (flagged `unclear:` in `Comment`).
