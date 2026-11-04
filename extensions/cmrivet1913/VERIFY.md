# Verification log: cmrivet1913

Pages: pp. 364–376 (PDF 379–391), with the source list on p. 355 (PDF 370). Pass 1 and
pass 2 were done by different readers from crops at 400–1200 dpi. The pass-2 reader got
only the skeleton (one row per form: page, French headword, source tag, parent of
sub-entries), not the pass-1 forms.

| | |
|---|---|
| Form tokens checked in both passes | 609 (364:8 365:59 366:49 367:51 368:56 369:53 370:55 371:54 372:54 373:53 374:55 375:53 376:9) |
| Headwords + sub-entries | 404 (334 headwords, 70 sub-entries) |
| Source tags | (1) 362, (2) 159, (3) 79, (4) 3, (1-3) 2, (1-2) 2, none 2 |
| Discrepancies adjudicated | 16 |
| Rows with `unclear:` | 15 |
| Skipped: no source number (kukurulu) | 1 |
| Skipped: unreadable / name / phrase | 0 |
| `forms.csv` rows | 612 (four doubled (1-x) forms) |
| Distinct glosses (`parameters.csv`) | 404, 307 Concepticon-mapped |

Pass 2 confirmed the per-page counts, the alignment of every form with its source tag,
and the two rows with no printed number.

## Vocabulaire (pp. 364–376)

Readings settled at 500–700 dpi.

Discrepancies between the passes: 16 of 609 rows. Each was settled against the image; the format is page/col/row, gloss, pass 1, pass 2, final, reason.

```
380/1/4	Aller	P1=eu-xale au-xa-tuigi [hu-axatissi Dios nel-sielo]	P2=eu-xale au-xa-tuigi [hu-axatissi Dios nel-siclo]	FINAL=eu-xale au-xa-tuigi [hu-axatissi Dios nel-siclo]	2nd reading: printed nel-siclo (misprint for nel-sielo, cf. the other Cardús phrases), kept as printed
380/1/54	Bon	P1=ercrets	P2=ererets	FINAL=ercrets	2nd reading: printed ercrets
381/1/26	Cheveu	P1=eu-tċokh	P2=eu-tčokh	FINAL=eu-tčokh	unclear: the caron over c is skewed and grave-like; read as č
381/1/47	Comprendre	P1=[em-assota] enko-phurúnue	P2=[em-assota] enko-phu-rúnue	FINAL=[em-assota] enko-phurúnue	printed with a line-break hyphen (enko-phu-/rúnue); hyphen treated as typographic and dropped
381/1/48	Comprendre	P1=[nihuas em-assota] enko-phurúnue	P2=[nihuus em-assota] enko-phurúnue	FINAL=[nihuus em-assota] enko-phurúnue	2nd reading: printed nihuus (cf. nihuas elsewhere), kept as printed
382/1/8	Coude	P1=eu-čeku-taulẹ	P2=eu-čeku-taule	FINAL=eu-čeku-taulẹ	2nd reading: dot below the final e visible at 500 dpi
382/1/15	Couteau	P1=[ev-ariva] ni-kurtapi	P2=[ev-ariva] ni-kur-tapi	FINAL=[ev-ariva] ni-kurtapi	printed with a line-break hyphen (ni-kur-/tapi); hyphen treated as typographic and dropped
385/1/5	Loup rouge (Canis jubatus)	P1=ni-čimakeyu	P2=ni-činakeyu	FINAL=ni-činakeyu	2nd reading: -čina- (n, not m)
386/1/3	Nom	P1=ehu-uku	P2=chu-uku	FINAL=chu-uku	unclear: first letter read c (no loop); could be e
388/1/6	Petit	P1=titidii	P2=titilii	FINAL=titidii	unclear: third syllable read di (pass 2: li); worn italic
389/1/29	Scorpion	P1=ni-činite	P2=ni-čimite	FINAL=ni-čimite	2nd reading: -čimite (m, not n)
390/1/1	Tante	P1=ehué	P2=chué	FINAL=chué	unclear: first letter read c (no loop); could be e
390/1/11	Terre, pays	P1=[yekita yematikore nel-sielo čaunexe] kassuixi-taule	P2=[yekita yematikore nel-sielo čaunexe] kas-suixi-taule	FINAL=[yekita yematikore nel-sielo čaunexe] kassuixi-taule	printed with a line-break hyphen (kas-/suixi-taule); hyphen treated as typographic and dropped
390/1/27	Tuer	P1=[euxali] eev-atixigi [ni-koxolani ni-suera]	P2=[euxali] cev-atixigi [ni-koxolani ni-suera]	FINAL=[euxali] cev-atixigi [ni-koxolani ni-suera]	2nd reading: printed cev- here (eev- under Flèche), kept as printed
390/1/35	Ventre	P1=eu-tsutsa	P2=eu-tsatsa	FINAL=eu-tsatsa	2nd reading: eu-tsatsa
390/1/38	Vert	P1=ne-kečaza	P2=ne-kečaža	FINAL=ne-kečaza	unclear: the italic z has a caron-like stroke; read plain z (same glyph shape as other z in the list)
```

## Integrity checks

- The CSVs were written with Python's csv module.
- IDs are unique in forms, parameters and languages; every `Language_ID` and `Parameter_ID` resolves; every `Source` key is in `sources.bib`.
- Every Concepticon_ID exists in the frozen Concepticon table, and the Glottocodes exist in the frozen Glottolog table.
- `arcaverborum.extensions.validate` was run against a temporary root that links the frozen reference tables: no problems.
