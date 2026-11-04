# castelnau1851: Guachi and Guató vocabularies in Castelnau (1851)

## Source

Castelnau, Francis de. 1851. *Expédition dans les parties centrales de l'Amérique
du Sud … Histoire du voyage*, tome cinquième. Paris: P. Bertrand. Appendix
"Vocabulaires des langues indiennes":

| Variety (`languages.csv`) | Glottocode | Vocabulary | Printed pages | PDF pages | Rows |
|---|---|---|---|---|---|
| `guachi`: "Langue des Guachis (Environs de Miranda)" | guac1239 | IXe vocabulaire | 278 (right column) to 280 (left column) | 288–290 | 145 |
| `guato`: "Langue des Guatos (Rio Paraguay)" | guat1253 | XIIe vocabulaire | 283 (right column) to 285 (left column) | 293–295 | 164 |

- Scan: <https://archive.org/download/expditiondansle05lucagoog/expditiondansle05lucagoog.pdf>
  (Google scan, 490 PDF pages, image-only, no text layer). sha256
  `c64547c8f1fec17533924629f1098dc4b53d727d78f9c6f15d7d9147815f5e76`.
  PDF page = printed page + 10.
- The page images used are in `pages/` (150 dpi, named by printed page).
- The entry counts agree with the published figures (145 Guachi entries; Postigo 2011
  counts 164 Guató entries).
- The Castelnau expedition passed through the region c. 1845. There was one collector for
  each list. Castelnau gives no informant names.
- The rest of the appendix was checked: no other vocabulary is Guachi or Guató. The IXe
  list is followed by Guaycurú (Xe), Cayowá (XIe), Bororo (XIIIe), Chiquitos (XIVe) and
  Andean/Amazonian lists.

## Transcription

Transcribed by an AI agent from page images on 2026-11-04. A second, independent
reading verified it (see `VERIFY.md`).

- Each printed entry has the form `Gloss — Form.`.
  - `Value` is the printed form with the list-final period removed.
  - `Form` is the same, minus parenthesised source notes. Two entries have such notes:
    Guachi *Soleil* "O-es (ó long)" and Guató *Bœuf* "Waca (du portugais vaca)".
  - Guató *Cheveux* is printed "Ma- eu". `Value` keeps the gap; `Form` closes it
    ("Ma-eu").
- Spelling, accents, hyphens and capitals follow the printed text, including misprints and
  inconsistencies:
  - Guató *Onze* "Thenai-ai-caibo" (where "Tchenai" would be expected);
  - *Quatorze* "-al-";
  - *Dix-sept* "-quachoibe";
  - the glosses "Lezard" and "Eternuer", printed without accents.
- `Segments` is empty. The spelling is French-based, there is no key, and it is not IPA.
- The scan is heavily inked. 36 forms have doubtful letters. Each has a `Comment` that
  begins `unclear:`, gives the chosen reading and names the alternative reading.
- `Loan` = `true` only for Guató *Bœuf* "Waca", which Castelnau marks "du portugais vaca".
- One `parameters.csv` row exists per distinct printed gloss string. The two lists share
  most glosses, so they share most parameter rows.
  - Spelling variants are kept as separate rows: Epaule/Épaule, Étoile/Étoiles,
    Vêtement/Vêtements, Lezard/Lézard, and Tête/Tète.
  - `Name` = printed French gloss ` | ` English translation.

## Concepticon mapping

175 of the 205 glosses are mapped, to 168 distinct concepts. The mapping is
conservative. These glosses are left unmapped:

- compounds and alternatives: "Lèvres et bouche", "Gorge ou cou", "Mauvais ou laid";
- size-qualified items: petite/grande rivière, grand/petit canot;
- ambiguous French words: Terre, Bois, Jour, Bœuf, Lard, Paresseux (lazy or sloth),
  Fatiguer;
- region-specific animals or plants without an exact concept: Loup (probably the maned
  wolf), Autruche (rhea), Jabiru, Boa, Cocotier/acuri palm;
- Sabre, Eau-de-vie, Prairies;
- the person/colour terms Blanc, Nègre, Indien, Mulâtre (the Guató forms carry *-chou*
  next to Rouge, so these may be colour terms);
- "Ma fille";
- the numerals 21 and 26.

Choices worth noting:

- Cacique and Chef → CHIEFTAIN;
- S'asseoir → SIT DOWN;
- Faire la cuisine → COOK (SOMETHING);
- Pêcher → FISHING;
- Vieillard ou vieille femme → OLD PERSON;
- Patate → SWEET POTATO (French *patate* in 1851);
- Crainte → FEAR (FRIGHT);
- Faim → HUNGER.

## Exclusions

None. Every printed entry is transcribed, and none was unreadable. The following were not
excluded:

- *Dieu* and *Diable*, which are generic concepts;
- *Blanc*, *Nègre*, *Indien (peau rouge)* and *Mulâtre*, which are category nouns or
  colours rather than names of specific peoples.

There are no phrases. Some non-entry text is not data:

- the Guachi remark after *Cinq* ("Ils ne comptent pas plus loin": they count no
  further than five);
- the Guató N.B. on religion at the end of p. 285.

## Licence

Public domain. The work was published in 1851, before 1931, so it is public domain in the
US, and Castelnau died in 1880. Licence: Public Domain Mark 1.0. archive.org marks the
item NOT_IN_COPYRIGHT.

## Identity notes

- **Guachi:** Miranda is in Mato Grosso do Sul, Brazil, not in Argentina, as some mirrors
  say. Castelnau's plate caption "Jeune chef Guachi (Indien Guato)" conflates two peoples.
  It is not language evidence, and the two lists here are clearly distinct. The proposed
  Guaycuruan link is unproven. This is the only primary Guachi source. Viegas Barros 2004
  is secondary.
- **Guachi ambiguous glosses:**
  - "Iten" is printed for both *Fuir* and *Natte*;
  - "Mapo" is printed in Guató for both *Cochon* and *Chauve-souris*;
  - Guató *Bras* is "Mapo" too.
- **Guató:**
  - Schmidt 1905 reprints these Castelnau words with the prefix "C.". Those items belong
    to this extension, not to Schmidt's.
  - Postigo 2011 (*Estudos Linguísticos* 40(1), CC BY-NC) gives a documented phonological
    reading of this list. It could inform a later profile; it is not used here.
