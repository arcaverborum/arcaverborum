# VERIFY: schmidt1905

## Pages

Printed pp. 262-279 (PDF 307-324; PDF = printed + 45), plus the introduction pp. 260-261
(PDF 305-306) for the "C." convention. The sound notes (pp. 255-256) were read from the
scan's OCR text layer for the README summary, not re-checked against the images.

## Pass 1

Each page was rendered at 270 dpi as four quarter-page crops (left/right column, upper/lower
half). Every entry was read from these crops, with 600-1000 dpi zooms of words whose
diacritics were unclear. Readings were written per page into working files.

## Pass 2 (how independent it was)

The page was rendered again at a different resolution and crop (330 dpi, column thirds).
Every Schmidt form was re-read from the new images and written to separate files
without opening the pass-1 files. The two sets were then compared mechanically.

**This pass was not strictly blind.** Both passes ran in the same working session, and the
pass-1 readings were still in my context while I re-read the pages. So the second reading
may have been anchored on the first. Agreement between the passes is weaker evidence than
two truly independent transcriptions. The pass did catch real differences, though (see
below): 14 forms were read differently, and each was settled by a fresh 900-1500 dpi zoom.

## Coverage

- Entries with a Schmidt form: 452. All 446 that became rows (excluding 3 phrases and
  the possessed sub-entries 78a-c) were re-read in pass 2. 191a was also re-read.
- Entry numbers 1-507 are all present (plus 383a); none is missing or unreadable.

## Discrepancies and resolutions

| No. | Pass 1 | Pass 2 | Final (after zoom) |
|---|---|---|---|
| 9 | irǽ | irǣ́ | irǽ (unclear, in Comment) |
| 58 | ĕfắgndắnŭ́va͜e | ĕfắgndănŭ́va͜e | ĕfắgndănŭ́va͜e |
| 87 | hihĕ́(e)ir | hihḗ(e)ir | hihĕ́(e)ir (unclear, in Comment) |
| 100 | mắhŏ́džinŏ | măhŏ́džinŏ | mắhŏ́džinŏ (unclear, in Comment) |
| 106 | matŏnyĭ́ko | matŏ́nyĭ́ko | matŏnyĭ́ko |
| 149 | madaakútši | mádaakútši | mádaakútši |
| 157 | mavæ̮rúta | mavǣ̮rúta | mavǣ̮rúta |
| 174 | iétoga | iĕ́toga | iĕ́toga |
| 270 | matōō(g)ōiǽ | matōō(g)ōiǣ́ | matōō(g)ōiǣ́ |
| 281 | mắngáána | mắngáắna | mắngáắna (unclear, in Comment) |
| 293 | máhĕ | mắhĕ | mắhĕ |
| 302 | mōgú | mōgū́ | mōgū́ |
| 357 | mătšõ(ng)tă | mătšõ(ng)tắ | mătšō(ng)tắ (macron, not tilde; in Comment) |
| 362 | miúri | miŭ́ri | miŭ́ri (unclear, in Comment) |

Also corrected during pass 1/2 zooms: 104/105 mătiók(i)r (breve, not breve+acute),
114 mešedšíka (not ĭ́), 290 măkṓdă, 304 mḗdžăha, 307 mŭ́tắkoraắpĕ, 389 mīguā́tă,
390 mudā́da, 475 hŏdṓkiă.

## Unclear readings flagged in `Comment` (23 rows)

9, 76, 87, 100, 111, 142, 202, 213, 281, 294, 295, 309, 311, 319, 329, 357, 359, 362, 363,
398, 419, 458, 501. Most are worn or faint diacritics, or an i printed without its dot.

## Counts

- forms.csv rows: 449, from 445 numbered entries (114 and 161 give two forms each, 449 gives he/hi, 465 gives two forms)
- distinct Form strings: 431
- distinct glosses (parameters): 416
- Concepticon-mapped glosses: 202
- skipped: 60 Castelnau-only entries (incl. No. 437), 3 phrases (445, 454, 507),
  4 possessed sub-entries (78a, 78b, 78c, 191a); 94 Castelnau forms omitted from mixed
  entries; 0 unreadable.

## Validation

`python3 -I tools/validate_ext.py schmidt1905` (the repo's own `extensions.validate` plus
NFC, empty-Segments, Source-prefix and Concepticon-gloss checks): 0 problems (2026-11-04).
