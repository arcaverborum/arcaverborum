# Verification log — boggiani1900

Date: 2026-11-04. Scan sha256 030d209b1c221a15f894d020c1ceda59a093ae6e2e820293ec932781d8175157.

## Pages
Printed pp. 207–238 (PDF 216–247, 1-based). Pass 1 read page halves at 250 dpi with
crops at 400–900 dpi for doubtful letters. Pass 2 re-rendered every page at 300 dpi
(full text block) and re-read every form from the image into separate files
(`cp2.tsv`, `pc2.tsv`) without consulting pass 1; the two passes were then compared
programmatically (NFC, row by row).

## Rows checked
* Castellano–Payaguá + numerals (pp. 208–224): 402 printed entries read twice → 0 discrepancies.
* Payaguá–Castellano (pp. 225–238): 323 non-skipped printed entries read twice → 1 discrepancy:
  p. 232 *Pecho* — pass 1 `Ichaᵃpüⁱ́c` (small accented i), pass 2 `Ichaᵃpüíc`. Re-checked at
  900 dpi: the í is full-size → `Ichaᵃpüíc` adopted. (The Castellano–Payaguá p. 217 form
  `Ichaᵃpüᵘ́c`, with a small accented u, was read identically in both passes and is a separate row.)
* Cross-check between the two vocabularies: 300 Castellano–Payaguá rows are printed
  identically in Payaguá–Castellano (an independent confirmation by the source itself);
  88 forms differ in some detail and are kept as separate rows (see README).

## Corrections made during pass 1 (before pass 2)
* p. 218 *Sobrina/Sobrino*: small letter after "tti" first read as c, confirmed at 700 dpi as e
  (`Iachemmaráttiᵉga`, `Iacheⁱmmarᵍattiᵉcca`).
* p. 215 *Mujer buena ó linda*: `Largá` → `Larᵍá` (small g).

## Unclear readings (kept, flagged in Comment)
* p. 212 *Frío* `Sfᵍal-lác`: second letter looks like F (probably damaged R; p. 237 has `Srᵍal-lác`).
* p. 237 *Miembro ♂* `Sahá`: third letter looks like H (cf. p. 215 `Saüá`).
* pp. 210, 238 *Colorado* `Zᶜiaccá`: small letter after Z is c or e.
* p. 230 *Lengua* `Iacᵍcᵍál`: small letters read as g.
* pp. 213, 225 *Humo* `Alvᵇockéⁱ`: V full-size, b small.
* p. 229 *Madera* `Heᵉnèép`: small letter after He read as e.
* Italic ("almost mute") letters not systematically detectable in small capitals (README).

## Unreadable rows
None.

## Counts
* Rows (forms.csv): 515; distinct forms: 468.
* Concepts (distinct glosses): 391; Concepticon-mapped: 248.
* Skipped: phrases 100 counted (11 Castellano–Payaguá list, 89 Payaguá–Castellano) +
  ≈85 in the "Frases" section (approximate); ethnonyms 8; grammatical notes 2;
  ditto-only numerals 6.

## Validation
`python3 -I tools/validate_ext.py boggiani1900` (repo validator + spec checks: NFC,
empty Segments, Source keys, Concepticon ID/gloss pairs, unique IDs, referential
integrity): 0 problems.

## Caveat on independence (added by the coordinating agent)

The same AI agent did the first transcription and the second reading of this list, in one working session, so its first-pass readings were still in context during the second pass. The second pass used fresh renders and crops, but it was not strictly blind, and the discrepancy count may be optimistic. A blind re-check of a sample by another reader is advisable before promotion.
