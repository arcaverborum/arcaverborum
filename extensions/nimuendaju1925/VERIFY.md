# Verification log: nimuendaju1925

Pages: printed pp. 166–171 = PDF pp. 192–197 of the vol. 17 scan
(sha256 dc8929c5…b9d8f5). Page boundaries were checked: p. 166 has the
Mura-Pirahã list above the heading "V. Vocabulario Matanawí"; p. 172 (PDF 198)
starts "VI. Vocabulario Ntogapid".

## Method

* **First pass.** Page images rendered with pymupdf: column strips at 560 dpi,
  plus 600–1100 dpi zooms on doubtful letters. Each gloss/form pair was typed
  into a working file.
* **Second pass.** The pages were re-rendered with a different geometry (column
  strips at 430 dpi, different cut points). Every printed entry was re-read from
  the new images and its form written down before the first-pass form was
  consulted; the two readings were then compared, and discrepancies settled
  against 1100 dpi zooms.
* A calibration step compared the diacritics with the Ntogapid page (p. 172),
  whose footnotes distinguish "langer Vokal" and "tontragender Vokal", and
  compared the italic *h* and *b* at high magnification. The archive.org OCR was
  consulted only as a tie-breaker for *h* versus *b*; no form was taken from it.

## Rows checked

All 299 kept entries (353 form rows) and all 65 excluded entries (to confirm the
exclusion class).

## Discrepancies between the passes and resolution

| Gloss (page) | First pass | Second pass / resolution |
|---|---|---|
| Coxa (166) | aritǫ zį | **aritǫ zį́**: a hook below and an acute above are both visible at 1100 dpi |
| Mulher (168) | mapą̃ | **mapą́**: only an acute above at 1100 dpi |
| meu marido (168) | ma papą̃a zį | **ma papã́a zį**: no hook under the a; stacked bar + acute |
| Indio brabo (168) | rįnĩ amarizí | **rįnĩ amarizį́**: hook below visible |
| Casca (170) | įuñhó | **įuṅhó**: the mark over n reads as a dot (still unclear) |
| Matto (170) | ṳ̃ | **ṳ̂**: the upper mark reads as a circumflex (still unclear) |
| eu (171) | hįzi, hizį | **hį̃zi, hizį́**: bar over the first i, acute on the last |
| logar de dormir (171) | awiši ramųrí | **auiši ramųrí**: both readings of the image show *au*; kept, flagged |
| nos (171) | ñowã | unchanged; a possible mark over the o is flagged |

Discrepancies: 9 entries (8 changed, 1 flagged unchanged).

## Unclear readings (flagged in `Comment` with "unclear:")

Costa (*kisi zi*, the first word blotted on the scan), Ourina (*ñô*, circumflex or
tilde), Lenha (*uã́*, stacked marks), Tapioca (*mimą̀*, accent shape), Taitetú
(*mã́*, stacked marks), Casca (*įuṅhó*), Matto (*ṳ̂*), perto (*atéãsį*,
smudged), nos (*ñowã*), logar de dormir (*auiši*). That is 10 entries
(13 form rows).

Systematic uncertainties, stated in README rather than per row: tilde vs macron
over vowels (all transcribed as tilde); italic i-dot vs acute on *i*; italic *h*
vs *b* (read *h* outside -bm/-bn clusters, e.g. "Campo" *rarįhú*, "Pimenta"
*išihó*).

## Counts

* Entries kept (distinct glosses): 299
* Form rows: 353
* Concepticon-mapped glosses: 204
* Loans marked: 2 (*tušáu*, *tipití*)
* Skipped: 4 toponyms, 14 ethnonyms, 46 phrases/imperatives/inflected forms,
  1 entry with no form (Feijão); 0 unreadable.

## Integrity checks

`python3 -I tools/validate_ext.py nimuendaju1925` (the repository's own
`arcaverborum.extensions.validate`, run against a temporary root, plus checks
for NFC, empty `Segments`, Source keys and Concepticon ID/gloss agreement): see
the result recorded below.

Result (2026-11-04): `checked 1 extension(s): nimuendaju1925; 0 problem(s)`.
All IDs are unique, every Language_ID and Parameter_ID resolves, every Source key is in `sources.bib`, and all text is NFC.

## Caveat on independence (added by the coordinating agent)

The same AI agent did the first transcription and the second reading of this list, in one working session, so its first-pass readings were still in context during the second pass. The second pass used fresh renders and crops, but it was not strictly blind, and the discrepancy count may be optimistic. A blind re-check of a sample by another reader is advisable before promotion.
