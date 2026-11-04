# boggiani1900 — Payaguá vocabulary of Guido Boggiani (1900)

**Source.** Boggiani, Guido. 1900. "Lingüística sudamericana. Datos para el estudio de
los idiomas Payaguá y Machicuí." *Primera reunión del Congreso Científico Latino
Americano, Trabajos de la 4a sección*, 203–282. Buenos Aires: Compañía Sud-Americana
de Billetes de Banco.

**Pages transcribed (Payaguá part only).** Spelling key "Letras y signos
convencionales" pp. 207–208; "Idioma Payaguá" Castellano–Payaguá vocabulary
pp. 208–220; "Frases" pp. 220–223; "Numerales" pp. 223–224 (with "Nota explicativa");
"Vocabulario Payaguá–Castellano" pp. 225–238. The Machicuí part (Parte II, from
p. 239) is a different language and is **not** included.

**Scan.** archive.org item `primera-reunion-del-congreso-cientifico-latino-americano-trabajos-de-la-4ta-seccion-1900`
(Google scan, with an unreliable OCR text layer that loses the special letters):
<https://archive.org/download/primera-reunion-del-congreso-cientifico-latino-americano-trabajos-de-la-4ta-seccion-1900/PRIMERA%20REUNION%20DEL%20CONGRESO%20CIENTIFICO%20LATINO%20AMERICANO%20TRABAJOS%20DE%20LA%204ta%20SECCION%201900.pdf>,
sha256 `030d209b1c221a15f894d020c1ceda59a093ae6e2e820293ec932781d8175157`.
PDF page = printed page + 9 (1-based). The pages used are in `pages/` (120 dpi).

**Variety.** One `languages.csv` row, `paya_boggiani` → Payaguá (`paya1236`):
Payaguá of Paraguay recorded by Boggiani "directamente de boca de unos individuos de
la tribu" (p. 205), 1890s. This is a 19th-century stage, distinct from the 18th-century
Payaguá of Aguirre 1793 (extension `aguirre1793`); the two are not pooled.

**Preparation.** Transcribed by an AI agent from page images on 2026-11-04; verified
by a second independent reading (see `VERIFY.md`). Not checked by a human yet.

## Boggiani's spelling key (verbatim, pp. 207–208)

> Letras y signos convencionales para la transcripción de vocablos de los idiomas
> PAYAGUÁ y MACHICUÍ ("Lengua" del Siglo XIX)
>
> *Se recomienda siempre la consulta de los dos Vocabularios*
>
> ´ ……… Este acento indica la vocal sobre la que cae la más fuerte acentuación del vocablo.
> \- ……… Indica una pequeña sincopación entre las dos letras.
> *l-l* ……… Indica que las dos *l* van pronunciadas como una *l* doble y no como una *ll* española.
> *th* ……… Tiene sonido de la *th* inglesa.
> *r*<sub>g</sub> ……… Pronúnciase gutural, exageradamente á la francesa.
> *g*<sub>r</sub> ……… Tiene sonido parecido al de la *r*<sub>g</sub>, más fuertemente hacia *g*.
> *a*<sub>a</sub>, *e*<sub>e</sub>, *i*<sub>i</sub>, *o*<sub>o</sub>, *u*<sub>u</sub>, Indica que sobre aquellas vocales hay que apoyar un tanto la voz, prolongándolas.
> *jh* ……… Tiene el sonido de la *ch* alemana, como una *j* española suavizada.
> *è* ……… Tiene sonido abierto como en *es* del verbo *ser*.
> *a, b, c, d,* etc. Una pequeña letra puesta al pie á la derecha de una letra, indica que esta última participa del sonido de aquélla.
> *o*<sub>u</sub> ……… Tiene sonido cerrado, con alguna tendencia á *u*.
> *Bastardilla* Una letra bastardilla indica que es casi muda.
> *s* ……… Pronúnciase siempre con sonido á la italiana en *rosa, casa,* etc.
> *z* ……… Tiene el sonido de la *z* italiana en *pezzo, tizzone,* etc.
> *z'* ……… Tiene el sonido de la *z* italiana en *mezzo, bazza, gazza,* etc.
> *y* ……… Tiene el sonido de *g* italiana delante de *i* y *e*.
> (?) ……… Indica que la ortografía ó la significación del vocablo es incierta.
> *ü* ……… Tiene el sonido de la *u* francesa ó de la *ü* alemana.
> *güe* ……… Indica que debe pronunciarse también la *u* como en diptongo.
> *o*<sub>e</sub> ……… Tiene el sonido de la *e* francesa en *je* y de la *ö* alemana.
> *w* ……… Sonido entre *u* y *v*, como la *w* inglesa.
> *s*<sub>x</sub> ……… Pronúnciase esta letra *s* apoyando la lengua al paladar.
> *ch* ……… Tiene el sonido de la *ch* española ó de la *c* italiana delante *e* é *i*.
> *x* ……… Se pronuncia como la *sh* inglesa ó como *sc* italiana delante de *i* y *e*.

(Footnote 1 on p. 227 adds: "La *Z'* suena algo como *dz*, no como *c* en *ce, ci*.")

## Transcription conventions

* Forms are printed in small capitals with an initial full capital. Small capitals
  carry no case contrast, so `Form`/`Value` give them as an initial capital plus lower
  case (`IAMÁaRgA` → `Iamáᵃrᵍa`). Phrase-internal words in lower case as printed.
* **Small letters** ("una pequeña letra puesta al pie á la derecha"): Boggiani prints
  a reduced lower-case letter immediately after the letter it modifies. These are
  rendered with Unicode modifier (superscript) letters: ᵃ ᵉ ⁱ ᵒ ᵘ ᵍ ʳ ᶜ ᶻ ʰ ᵗ ᵇ ᵛ ʸ ˣ.
  This is a typographic convention of this extension, not an IPA claim. Thus
  `rᵍ` = his guttural r (key "r<sub>g</sub>"), `gʳ` = his "g<sub>r</sub>", `aᵃ` etc. =
  lengthened vowels, `oᵘ`/`oᵉ` the vowel qualities of the key, `sˣ` the palatal s.
  Where a small letter carries its own diacritic (e.g. small ü with acute), the
  diacritic is placed on the modifier letter (`ᵘ̈`, `ᵘ́`).
* Accents (´ ` ¨) are kept exactly; `è` is Boggiani's open e, frequently in the
  sequence `èé`. Hyphens are kept (they mean "pequeña sincopación" in his key).
  Where a hyphen falls at a line end and may only be a line-break hyphen, the form is
  kept as printed and the `Comment` says so; in two clear cases ("Iguii-/charᵍan",
  "Mareheies-/seré") the line-break hyphen was removed and this is noted.
* Italic ("bastardilla" = almost mute) letters inside the small-capital forms are
  hard to recognise in this scan and were **not** systematically recorded; the one
  clear case (italic initial S of *Somá*) is noted in `Comment`.
* `Value` = the full printed entry (all alternatives, "(?)", footnote markers); `Form` =
  one alternative per row. Alternatives separated by "." or "," in the source give one
  row each. Footnote markers "(1)" are dropped from `Form`; footnotes giving
  equivalents in other languages (Chamacoco, Sanapaná, Kinikinao, Caduveo, …) are not
  transcribed but mentioned in `Comment`.
* `Segments` is empty for every row: this is a written-only, pre-IPA notation.
  A profile, if any, is a later reviewed step (the key above is its documentary basis).
* `Loan` is blank throughout: Boggiani marks no loans.

## The two vocabularies (rule applied)

Boggiani prints a Castellano–Payaguá list (pp. 208–220) and a Payaguá–Castellano list
(pp. 225–238) that largely overlap. Rule:

1. Every entry of the Castellano–Payaguá list is a row (one per alternative form);
   `parameters.csv` has one concept per distinct Spanish gloss as printed there.
2. Each Payaguá–Castellano entry is matched to the Castellano–Payaguá gloss it
   corresponds to (its Spanish gloss, split at "." / "," when it lists several senses).
   If the same form (identical spelling, ignoring only initial capitalisation) is already a
   row for that gloss, **no new row** is made: the page is added to `Source`
   (e.g. `boggiani1900_boggiani1900[209,234]`) and `Comment` says "also in
   Payaguá–Castellano p. N", with the Payaguá–Castellano gloss wording if it differs.
3. If the form differs in any printed detail (accent, small letter, letter), the
   Payaguá–Castellano form is a **separate row** under the same concept, with
   `Comment` "Payaguá–Castellano section only". Such pairs (e.g. *Takíl* p. 208 vs
   *Tackíl* p. 238 'ácido'; *Ueᵉiác* vs *Ueᶜiác* 'agua') are genuine source variants or
   misprints and are left for the reviewer; no reading is preferred.
4. Payaguá–Castellano glosses with no Castellano–Payaguá counterpart get their own
   concept (5: "Subfijo de 2.ª persona", "(Prefijo pronominal de 2.ª Pers. Sing. y
   Plur.)", "Prefijo pronominal de 1.ª pers.", "Estómago", "Probar").

Result: 515 rows (427 from Castellano–Payaguá, 300 of which are confirmed verbatim in
Payaguá–Castellano; 88 Payaguá–Castellano-only rows), 391 concepts.

## Concepts

`Name` = Spanish gloss as printed, " | ", English translation. Possessed paradigms
printed under a headword (*Mi hija*, *Tu madre*, *Mis ojos* …) are kept as separate
concepts named "Headword: subentry" (e.g. `Madre: Tu madre`) and are not mapped.
248 of 391 concepts are mapped to Concepticon, conservatively: glosses with person
marking, possessor, sex/age qualifications of a general term, combined senses
("Sudar. Sudor", "Con (y, con, más)"), ambiguous Spanish ("Día", "Alto") or
culture-specific species are left unmapped. Numerals are mapped (ONE–TEN, …, FIVE HUNDRED);
the printed "1.º … 9.º" are cardinal numerals in a list (Boggiani's "Numerales"), not
ordinals. Two printed glosses can map to one Concepticon concept (Ave/Pájaro → BIRD,
Ciervo/Venado → DEER, Chico/Pequeño → SMALL, Guapo/Valiente → BRAVE, Hurtar/Robar → STEAL).

## Exclusions (with counts)

* Phrases and sentences: 11 in the Castellano–Payaguá list (e.g. "Flaco (tú eres f.)",
  "Mía es esta casa", "Hombre" = *Larᵍá accú* 'good man'), ≈85 in the separate "Frases"
  section pp. 220–223 (approximate count from the text layer; only "¿Qué cosa?" kept as a
  single lexical concept), and 89 in the Payaguá–Castellano list (counted).
* Ethnonyms/proper names: 8 (Chamacóco, Guaná de Miranda, Machicuí/Calaló, Payaguá
  self-name Euébe; each in both lists).
* Grammatical notes without a form ("C", "G" letter notes): 2.
* Numerals printed only as ditto marks ("íd. íd. …": 22–25, 90, 91): 6.
* Machicuí part (from p. 239): entirely out of scope.

## Licence

Published in 1900 in Buenos Aires, i.e. before 1931: public domain in the US
(maintainer's rule); Boggiani died in 1902, so it is also public domain worldwide.
`License` = Public Domain Mark 1.0. The archive.org copy is an uploader-supplied
Google scan; no rights are claimed in it.

## Identity issues

* Payaguá (paya1236) is an isolate (or Guaicuruan-linked, unproven). Historical
  subgroups Sarigué/Cadigué vs Tacumbú/Magach are not distinguished by Boggiani.
* Boggiani (pp. 206–207) argues that Cerviño's "Lengua" vocabulary is in fact Payaguá
  (not Enlhet/Machicuí): a mapping trap for other sources, not for this one.
* "Calaló" (p. 214/226) is the Payaguá name for Chaco peoples (Angaité, Sanapaná,
  Lengua, Toba …), not a language label of this list.
