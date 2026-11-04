# VERIFY — chacon2024arutani

Date: 2026-11-04. Source: born-digital PDF (text layer + glyph repairs), see README.

## Structural checks

* The three alphabetical sections (Arutani–Português, –Español, –English) were
  parsed independently; they were laid out separately by the typesetter, so line
  breaks, columns and page breaks differ. All three yield the same **944 entries**,
  the same headword and bracketed transcription for every entry, and the same
  number of senses (**1,130**). This confirms entry and sense boundaries
  (reading order across the two-column layout with letter headings, which reset
  the column flow, was the main parsing hazard and was fixed before this check).
* `avext.validate()`: no errors (unique IDs, Language_ID/Parameter_ID integrity,
  Glottocode and Concepticon IDs exist, Concepticon glosses match, every Source key
  in sources.bib, NFC).
* merkmal (`descriptive`) on Segments: 1,059 rows with Segments, 4 rows with a
  rejected token (printed superscript vowels `kᵄ kᵉ mⁱ sᵄ`), kept as printed.

## Second, independent reading

Sample (seed 20261104):

* stratified: 5 rows drawn at random from each of the 33 pages of the
  Arutani–Português section among rows without repairs → **165 rows**;
* **every row with a repaired character** in the headword, the bracketed
  transcription or the Portuguese gloss (`ᖯ→ʃ`, `ϐ/ϔ→f`, dotless `ı`/`ȷ` + mark)
  → **200 rows**;
* total **365 rows** (340 entries), on all 33 pages.

Procedure: each sampled entry was cropped from the page and rendered (200 dpi
sheets, 13 sheets); headword, every bracketed transcription and the gloss of the
sampled sense were typed from the image without looking at the extracted row
(`scripts/ext/arutani_verify_readings.tsv`, 366 readings), then compared by script
(NFC; the printed stress glyph read as `ˈ`; final full stop ignored).

Result:

| | count |
|---|---|
| rows compared | 365 (+1 extra sense read) |
| disagreements on first comparison | 4 (rows of 2 entries) |
| of which extraction errors | **0** |
| of which reader errors (resolved at 600–900 dpi) | 4: *awini* `[ãwĩˈnĩ]` (reader added a tilde on w); *xiã* `[ʃĩˈã]` ×3 senses (reader missed the tilde on i) |

**Error rate of the extracted data in the sample: 0 / 365 (0 %; 95 % upper bound
≈ 0.8 %).** Repaired rows: 0 / 200 errors.

Visual issues noted:

* `ɐ` vs `e`: at 200 dpi the Cambria `ɐ` is hard to tell from `e`; the embedded
  font outline of the glyph used (glyph 6283) was rendered and is a turned a. All
  `ɐ` in the text layer use that glyph; `e` uses glyph 135.
* Printed oddities confirmed on the page and kept: *tubeŕrculo* (akwa),
  *pedaços47;peças* (kaxa), *utensí́lio* (raiyu hani), *ma ndioca* (õya ĩhã).

Not separately verified: the Spanish and English glosses quoted in `Comment`
(same extraction method and same repairs; their entry/sense alignment is
confirmed by the structural check above).

## Counts

| | |
|---|---|
| entries in Arutani–Português | 944 |
| senses | 1,130 |
| rows (forms.csv) | 1,061 (898 entries) |
| distinct glosses / parameters | 982 |
| Concepticon-mapped parameters | 556 (527 distinct concept sets; 617 rows) |
| rows with Segments | 1,059 |
| Loan = true | 11 |
| skipped: grammatical | 39 |
| skipped: toponym | 11 |
| skipped: ethnonym | 9 |
| skipped: unknown meaning | 4 |
| skipped: proper name | 2 |
| skipped: glossonym / native-name-only gloss / unclear gloss / no gloss | 1 / 1 / 1 / 1 |
| unreadable rows | 0 |

## Sampled readings that matched (0-based entry index . 1-based sense; Local_ID = index+1 . sense)

2.2 7.1 10.1 12.1 13.1 19.1 22.1 26.1 28.1 28.2 32.1 33.1 35.1 35.2 36.1 42.1 44.1 45.1 46.1 47.1 
47.2 48.1 51.1 52.1 54.1 56.1 60.1 73.1 74.1 76.1 83.1 84.1 84.2 87.2 93.1 110.1 114.1 115.1 119.1 
133.1 135.1 137.1 140.2 141.1 146.3 154.1 154.2 86.1 86.2 90.1 91.1 101.1 118.1 126.3 136.2 136.3 
144.1 148.1 149.1 149.2 151.1 155.1 156.1 158.1 165.1 173.1 174.1 176.1 177.1 184.1 188.1 196.2 
203.1 208.1 208.2 209.1 157.3 160.1 163.2 166.1 175.1 178.1 179.1 186.1 192.1 193.1 198.1 205.1 
210.1 210.2 218.1 218.3 229.1 232.1 233.1 235.2 246.2 247.1 265.1 272.1 282.1 283.1 292.1 295.1 
302.1 314.1 315.1 223.1 237.1 240.1 245.1 259.1 263.1 268.1 269.1 270.1 273.2 288.1 293.1 298.1 
303.1 310.1 310.3 318.1 322.1 343.1 346.1 354.1 368.1 381.1 392.1 393.1 397.1 320.1 321.1 328.1 
331.1 353.1 355.1 358.1 365.1 370.1 378.1 385.1 386.1 387.1 389.1 394.1 399.1 400.1 402.1 406.1 
412.1 424.1 430.1 432.1 440.1 446.1 451.1 453.1 454.1 456.1 465.1 468.2 476.1 478.1 486.1 487.1 
403.1 407.1 416.1 426.1 437.1 445.2 452.1 452.2 455.1 457.1 458.1 466.1 475.1 479.1 481.1 491.1 
494.1 497.1 499.1 501.1 503.1 506.1 508.1 525.1 531.1 535.1 546.1 550.1 556.1 561.1 562.1 495.1 
496.1 502.1 504.1 516.1 523.1 526.1 527.1 534.1 540.2 555.2 559.2 564.1 579.1 583.1 583.2 583.3 
588.1 594.1 602.1 607.1 620.1 625.1 629.1 570.1 571.1 572.1 573.1 574.1 580.1 585.2 595.1 596.1 
601.1 604.1 611.1 624.1 627.1 630.1 635.1 641.1 643.1 646.1 660.1 660.2 663.1 666.1 669.4 680.1 
687.1 688.1 700.2 714.1 631.1 633.1 634.1 637.1 644.1 655.1 661.1 662.1 664.1 670.1 674.1 676.1 
681.1 682.1 707.1 709.1 709.2 717.1 721.1 731.1 735.1 747.1 748.1 749.1 753.1 759.1 762.1 765.1 
768.1 768.2 780.1 718.3 719.1 723.1 733.2 737.1 740.1 743.1 746.3 751.1 754.1 764.2 773.1 778.1 
782.1 784.1 793.1 795.1 796.1 796.2 799.1 803.1 806.1 809.1 815.1 817.1 823.1 825.1 827.1 831.1 
840.1 789.1 791.3 798.1 801.1 801.4 824.1 829.1 838.1 841.1 841.2 856.1 873.1 882.1 885.1 889.1 
890.1 892.1 894.1 897.1 898.1 900.1 902.1 903.1 906.1 908.1 908.2 908.3 917.1 851.1 855.1 860.1 
878.1 881.1 888.1 888.2 888.3 891.1 893.1 895.1 899.1 901.1 904.1 907.1 909.1 916.2 920.1 920.2 
923.1 926.1 937.1 943.1 931.1 938.1 
