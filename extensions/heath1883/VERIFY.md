# Verification log: heath1883

Pages: printed pp. 683–687 (PDF 8–12, 0-based), Canichana column. Pass 1 and pass 2
were done by different readers from rotated page crops at 300–1400 dpi. The pass-2
reader got only the English row skeleton (page, row, gloss), not the pass-1 forms.

## Counts

| | |
|---|---|
| English rows checked (both passes) | 194 (35 / 47 / 56 / 46 / 10 per page) |
| Rows with a form | 165 |
| Forms (`forms.csv` rows) | 165 (no entry lists alternatives) |
| Distinct glosses (`parameters.csv`) | 165 |
| Concepticon-mapped glosses | 154 |
| Skipped: empty Canichana cell | 29 |
| Skipped: unreadable / phrase / name | 0 |
| Rows with an `unclear:` comment | 16 |

## Discrepancies between the passes (8 of 194 rows)

Each was settled by re-reading crops at 450–1200 dpi. The format is
page/col/row, gloss, pass 1, pass 2, final, reason.

```
8/1/19	My younger sister.	P1=Eu-cau-la-mam-bu-vi-u-li	P2=Eu-cau-la-mam-bu-vi-u-li.	FINAL=Eu-cau-la-mam-bu-vi-u-li.	2nd reading: final full stop faintly visible after the overrun [vi-u-li
8/1/25	Forehead.	P1=Eu-shi-ti-daú-le.	P2=Eu-shi-ti-daŭ-le.	FINAL=Eu-shi-ti-daŭ-le.	unclear: mark over u is curved (breve-like) unlike the clear acutes elsewhere; read as breve; could be a damaged acute
8/1/31	Teeth.	P1=Eu-hùti.	P2=Eu-hŭti.	FINAL=Eu-hŭti.	unclear: mark over u is curved (breve-like); read as breve; could be a damaged acute or grave
9/1/4	Body.	P1=Eu-hei-e-tó-io.	P2=Eu-hel-e-tó-io.	FINAL=Eu-hel-e-tó-io.	unclear: third letter read l (no dot visible); first reading had i
9/1/6	Belly.	P1=Em-an-ca-ar-ëú.	P2=Em-an-ca-ar-ëŭ.	FINAL=Em-an-ca-ar-ëŭ.	unclear: mark over u curved (breve-like); read as breve
10/1/49	Warm—hot.	P1=Meu-hal-lie.	P2=Meu-hal-lic.	FINAL=Meu-hal-lie.	unclear: final letter read e (crossbar visible); could be c
11/1/6	Near.	P1=Co-iió.	P2=Co-hió.	FINAL=Co-iió.	unclear: damaged letter after Co- shows a dot, read i; could be h
11/1/43	To See.	P1=Au jar-co-iv-óe.	P2=Au-jar-co-iv-óe.	FINAL=Au-jar-co-iv-óe.	unclear: faint worn mark between Au and jar read as hyphen (cf. Au-jar- in the other verbs)
```

Both passes agreed on the overrun joins, including the layout-based assignment of
**My elder sister** (see README), and on the printed "T." for "I.".

## Integrity checks

- The CSVs were written with Python's csv module and re-read.
- IDs are unique in forms, parameters and languages. Every `Language_ID` and
  `Parameter_ID` resolves, and every `Source` key is in `sources.bib`.
- Every Concepticon_ID exists in the frozen Concepticon table.
- The Glottocode `cani1243` exists in the frozen Glottolog table.
- `arcaverborum.extensions.validate` was run against a temporary root that links the
  frozen reference tables: no problems.
