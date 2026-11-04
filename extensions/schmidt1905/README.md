# schmidt1905: Guató vocabulary in Max Schmidt, *Indianerstudien in Zentralbrasilien* (1905)

## Source

Schmidt, Max. 1905. *Indianerstudien in Zentralbrasilien: Erlebnisse und ethnologische
Ergebnisse einer Reise in den Jahren 1900 bis 1901.* Berlin: Dietrich Reimer.
Kapitel IX "Guató. Sprachliches", section III.B "Vokabular. In sachlicher Anordnung",
numbered entries 1-507 (plus 383a), **printed pp. 262-279** (PDF pp. 307-324).

- Scan: Wellcome Library copy on archive.org, `https://archive.org/download/b2488358x/b2488358x.pdf`
- sha256: `8f81d427301ced695fb5362e611220775f84a0c700887629086f21826e3e1668`
- Page offset: **PDF page = printed page + 45 (0-based page index; +46 in 1-based viewer numbering, confirmed by the 2026-11-04 blind check)** (printed p. 244 = PDF 289; p. 262 = PDF 307;
  p. 279 = PDF 324). The `+46` given in `sources/guat1253/SOURCES.tsv` is off by one.
- `pages/` holds 120-dpi renders of PDF pp. 305-324 (printed 260-279: the Vokabular
  introduction and the whole vocabulary).

Schmidt recorded the language during three weeks among the Guató of the Gaíba and
Uberaba lakes (upper Paraguay, Mato Grosso) in October-November 1901. Most words were
fixed by pointing at objects/actions and then checked with the Guató woman Rosa via
Portuguese (p. 244). The vocabulary is thematic: body parts (1-47), nature (48-77),
ethnographica (78-190), kinship (191-225), animals (226-363), plants (364-390),
adjectives (391-419), numerals (420-442), particles (443-459), verbs (460-507).

Transcribed by an AI agent from page images on 2026-11-04; verified by a second
independent reading (see `VERIFY.md`).

## Castelnau items (excluded)

Schmidt states (p. 260, III.A.2) that Castelnau's words (1851, vol. V, pp. 283-285) were
inserted for comparison and marked with a prefixed "C.". Those forms belong to the
Castelnau list (extension `castelnau1851`) and are **not** transcribed here:

- 60 entries consist of a Castelnau form only and are skipped entirely (listed below);
  No. 437 (achtzehn, "tchoum-ai-quachoibo") lacks the printed "C." but is Castelnau's
  French spelling in the Castelnau numeral series 434-442, and is skipped too.
- 94 entries print Schmidt's own form plus a "C." form; only Schmidt's form is kept, and
  the row's `Comment` says that a Castelnau form was omitted.

- 2 Gehirn: C. toori
- 3 Stirn: C. toori
- 4 Zunge: C. chagi
- 6 Lippe: C. iguai-o
- 12 Kehle: C. yotorito
- 13 Kinn: C. ebo
- 28 Brust: C. daapé
- 34 Bauch: C. ipo
- 35 Herz: C. acogo
- 37 Speck: C. magunpo
- 38 Fleisch: C. madeu
- 59 Tag: C. machuo
- 60 Nacht: C. mafi
- 66 Wasserfall: C. apowakou
- 73 Wald: C. modj-ao
- 74 Grasland: C. madjo-ougeu
- 75 Weg: C. maouvi
- 79 Ansiedlung: C. thajou
- 136 Keule: C. maragueu
- 153 Bekleidung: C. maré
- 166 Pfeil: C. machie
- 219 Greis, Greisin: C. meou
- 220 Neger: C. mibaia-chou
- 221 Weisser: C. akua-chou
- 222 Indianer: C. magueu-chou
- 223 Mulatte: C. noupirego-chou
- 224 Gott: C. ochewekin
- 225 Teufel: C. moukelengui
- 227 Affe: C. macpo
- 242 Wolf: C. mougouteu
- 252 Vogel: C. madjahé
- 275 Jabiru: C. nicko
- 322 Klapperschlange: C. mijii
- 323 Schlange: C. mojijipao
- 325 Fisch: C. megenti
- 372 Batate: C. mouka
- 410 hübsch: C. nitou
- 412 hässlich: C. mifau
- 414 schwer: C. itavo
- 415 leicht: C. nitaan
- 418 faul: C. eiguaoraea
- 434 fünfzehn: C. quinoibo
- 435 sechzehn: C. tchenai-ai-quachoibo
- 436 siebenzehn: C. douounai-ai-quachoibo
- 437 achtzehn: C. tchoum-ai-quachoibo
- 438 neunzehn: C. dekai-ai-quachoibo
- 439 zwanzig: C. quinoui-quachoibo
- 440 einundzwanzig: C. tchenai-jiga
- 441 sechsundzwanzig: C. dechagiga
- 442 dreissig: C. tchenai-jiga-caicaira
- 457 ja: C. ii
- 466 festmachen: C. ooutchai (Französisch: attacher)
- 472 laufen: C. niguouai
- 478 jagen: C. yavarou
- 487 beissen: C. eta
- 488 sprechen: C. mouteu
- 492 untertauchen: C. afeugua
- 496 vergnügt sein: C. atarijou
- 504 ermüden: C. acoura
- 506 Fieber: C. apouja

## Conventions

- `Value` = Schmidt's printed form(s) for the entry, with his own parenthetical notes
  (e.g. `maforáta (=Feuererde)`, `mavaká (vom Bras vacca, Kuh)`); the Castelnau part and
  the "Vgl." cross-references are not included.
- `Form` = one form. Entries with several forms get one row each (114, 161, 449, 465).
  Parentheses inside a form are Schmidt's own (barely audible sounds, e.g. `mik(í)r̊`,
  `kũ(ng)vuír`) and are kept as printed.
- `Local_ID` = Schmidt's entry number. `Source` gives the printed page.
- Glosses in `parameters.csv` are Schmidt's German glosses as printed (with his Tupi /
  Portuguese / Latin parentheticals), followed by an English translation. Entries with an
  identical printed gloss (e.g. three "Taube (spec.)") share one parameter; their
  `Local_ID`s differ.
- Spelling is reproduced exactly (Unicode NFC), including Schmidt's diacritics:
  acute, breve, breve+acute (e.g. `ắ`, `ŏ́`), macron, macron+acute (`ḗ`, `ṓ`, `ū́`),
  tilde (`ũ`, `ẽ`, `ĩ`, `õ`), háček (`š`, `ž`, `tš`, `dž`), `æ` with a breve below
  (`æ̮`, U+032E, often with acute or macron), a ring over r (`r̊`), an acute over n
  (`ń`, as in `digń`), and a tie below two vowels (`a͜e`, U+035C).
- `Segments` is empty: these are Schmidt's spellings, not IPA. A profile is a later,
  reviewed step.
- Person-marked verb forms (461, 463, 476, 490, 497, 503, 465) are kept with a `Comment`
  stating Schmidt's translation, and their glosses are not mapped to Concepticon.
- `Loan = true` only where Schmidt says so: 233 mavaká (from Portuguese *vaca*) and
  110 tšitša ("Uebernommenes Wort").

### Schmidt's notes on the sounds (pp. 255-256, summarised)

- Typical syllable: simple consonant + simple vowel or vowel sequence.
- `l`, `s` and `z` do not occur as simple consonants; the simple consonants are
  b, d, f, g, h, k, m, n, p, r, t, v, š, ž, y. The only consonant clusters are `tš`,
  `dž` and `dy`, which alternate with each other. `gn` has a "vocalic" sound and is not
  treated as a cluster.
- Syllable-final consonants: n, less often m, frequently r.
- Vowels: a, æ, e, i, o, u, and the vowel sequences aa, ai, ea, ee, eu, ia, ie, iu, oa,
  ua, ue, ui; i and u also occur nasalised (printed with a tilde).
- Bracketed letters mark sounds that are barely audible (e.g. the `(i)` before r,
  p. 259: "nur als ganz kurzer Laut").
- Accent placement distinguishes otherwise homophonous stems (p. 251).
- Schmidt equates Castelnau's French `eu` with his `ir`, and Castelnau's `chie` with his `tši`
  (pp. 247-248, footnotes).
- Schmidt gives no explicit key for the breve, macron and other diacritics; they are
  transcribed as printed without interpretation.

## Exclusions (counts)

| Reason | Entries |
|---|---|
| Castelnau-only entries ("C.") | 60 |
| Castelnau forms inside mixed entries (Schmidt form kept) | 94 forms omitted |
| Phrases / multi-word expressions not a single lexical concept | 3 |
| Possessed forms of nouns given as sub-entries | 4 |
| Inflected forms in notes (471, 482) | kept in `Value`/`Comment` only |
| Proper names, ethnonyms | 0 (Castelnau's ethnonym entries 220-223 are already excluded) |

Phrases skipped:
- 445 Wie verhält es sich?: diruadé
- 454 niemals wieder: nianinǣ̮so virmara
- 507 Furcht haben: montaguagagátu, er hat Furcht vor dem Gewehr

Possessed forms skipped:
- 78a unser Haus: ahiovír (10)
- 78b sein Haus: ehiovir
- 78c dein Haus: guahiovir
- 191a deine Mutter: guagi

## Licence

Published 1905, so it is in the public domain in the US (published before 1931), and
Schmidt died in 1950, so it is in the public domain in Brazil and Germany since 2021.
`License` = Public Domain Mark 1.0. The archive.org item shows a generic
rightsstatements "In Copyright" notice that does not reflect the author's term.

## Identity

- Guató (guat1253), upper Paraguay river. Schmidt's own 1901 record; not the Castelnau
  1851 list (separate extension) and not the modern Ferreira 2026 dictionary.
- A caption in Castelnau that confuses Guachi and Guató has no bearing on this list.
