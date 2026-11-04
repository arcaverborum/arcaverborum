# Verification log: castelnau1851

Date: 2026-11-04. Scan sha256 `c64547c8f1fec17533924629f1098dc4b53d727d78f9c6f15d7d9147815f5e76`.

## Pages

| Printed | PDF (1-based) | Content |
|---|---|---|
| 278 | 288 | Guachi, right column: Dieu … Pied (31) |
| 279 | 289 | Guachi, both columns: Pierre … Deux (45); Trois … Papillon (43) |
| 280 | 290 | Guachi, left column: Caïman … Nid d'oiseau (26); then the Xe vocabulaire (Guaycurú), not taken |
| 283 | 293 | Guató, right column: Dieu … Aldea (36); the left column is the XIe Cayowá list, not taken |
| 284 | 294 | Guató, both columns: Rivière … S'asseoir (45); Danser … Boa (45) |
| 285 | 295 | Guató, left column: Alligator … Eternuer (38), then the N.B.; the right column is the XIIIe Bororo list, not taken |

To find any other Guachi or Guató vocabulary, I checked contact sheets of PDF pp. 256–320
(all appendix vocabularies). None was found.

## Procedure

1. **First pass.** Column crops at 300 dpi (two halves per column), read and typed into a
   TSV: page, gloss, form.
2. **Second pass.** Independent re-render at 400 dpi in quarter-column crops. Every row
   was re-read from the image and typed without consulting the first-pass form, then the
   two readings were compared.
3. **Third look.** Disputed or blotted lines were rendered at 600 dpi. The scan's own
   resolution limits what this gains.

All 309 rows were checked in both passes.

## Discrepancies between passes and resolution

| Variety | Gloss | Pass 1 | Pass 2 / zoom | Final |
|---|---|---|---|---|
| guachi | Soleil (note) | (ô long) | (ó long) | (ó long), comment notes possible circumflex |
| guachi | Fatiguer | Ya-woul | Ya-weul | Ya-weul (unclear e/o) |
| guachi | Epaule | Iolal-eu | Iolai-eu | Iolal-eu (unclear; tall glyph after "a" read as l) |
| guachi | Coati | Aaat-kaech | Anat-kaech | Aaat-kaech (unclear a/n) |
| guato | Tète (gloss) | Tête | Tète | Tète (the gloss is printed with a grave accent) |
| guato | Petite rivière | Moudioque | Moudieque | Moudieque (unclear e/o) |
| guato | Gorge | Yotorite | Yotorito / Yotoritte | Yotorite (unclear) |
| guato | Dix-sept | Douounai-ai-quachoibo | …-quachoibe | …-quachoibe (as printed) |
| guato | Vingt | Quinoui-quachoibo | Quinoui-quacheibo | Quinoui-quacheibo (unclear) |
| guato | Être joyeux | Aterijou | Atarijoe | Atarijoe (unclear) |

In total there were 10 discrepancies: 4 Guachi, 6 Guató (one of them in a gloss). All
other rows agreed.

## Unclear readings

36 forms carry an `unclear:` comment: 20 Guachi and 16 Guató. Each comment gives the
chosen reading and the alternative. No entry was unreadable, so none was skipped.

Guachi:

- Cheveux, Dents, Oreille, Bras, Cervelle, Main, Doigt, Epaule, Pied, Danser, Jour, Un;
- Indien, Coati, Toucan, Fatiguer, Faire la cuisine, Laver, Papillon, Pleurer.

Guató:

- Dieu, Fils, Fille, Lèvre, Bouche, Gorge, Bras, Petite rivière, Rivière, Feu, Sept;
- Vingt, Vingt-six, Être joyeux, Serpent à sonnettes, Eau-de-vie.

## Counts

| | guachi (guac1239) | guato (guat1253) | total |
|---|---|---|---|
| rows (= forms; no alternatives were printed) | 145 | 164 | 309 |
| distinct glosses | 145 | 164 | 205 parameter rows (shared) |
| Concepticon-mapped glosses | 127 | 139 | 175 parameter rows → 168 concepts |
| loans marked | 0 | 1 (Bœuf "Waca") | 1 |
| skipped: unreadable | 0 | 0 | 0 |
| skipped: phrases | 0 | 0 | 0 |
| skipped: proper names, ethnonyms, toponyms | 0 | 0 | 0 |

Non-entry text was not transcribed:

- the Guachi remark "Ils ne comptent pas plus loin";
- the Guató N.B.

## Integrity checks

`python3 -I tools/validate_ext.py castelnau1851` runs the repository's own
`arcaverborum.extensions.validate` against the frozen Glottolog and Concepticon tables,
then the spec checks:

- NFC;
- `Segments` empty;
- every `Source` key starts with `castelnau1851_` and exists in `sources.bib`;
- each `Concepticon_Gloss` matches its ID;
- every `Name` contains ` | `.

Result: 0 problems.

## Caveat on independence (added by the coordinating agent)

The same AI agent did the first transcription and the second reading of this list, in one working session, so its first-pass readings were still in context during the second pass. The second pass used fresh renders and crops, but it was not strictly blind, and the discrepancy count may be optimistic. A blind re-check of a sample by another reader is advisable before promotion.
