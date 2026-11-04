# Verification log: tessmann1930

Pages: Omurana PDF 513–529 (pp. 444–458) and Auischiri PDF 547–559 (pp. 475–486).
Pass 1 and pass 2 were done by different readers from crops at 400–2400 dpi (the
native scan is about 330 dpi).
- For the word lists, each pass-2 reader got only the skeleton (page, column, row,
  German gloss).
- For the prose items, each pass-2 reader got the German term and the context sentence
  with the native word replaced by `___`.

Before comparing, two encoding variants were canonicalised in both passes; these are
encodings, not readings:
- dotless `ı` under a mark above → `i`: 3 Auischiri-list and 7 Omurana-list pass-2 rows;
- U+0330 tilde below → U+0331 line below: 8 Omurana-list pass-1 rows.

| | Auischiri list | Auischiri prose | Omurana list | Omurana prose |
|---|---|---|---|---|
| Rows checked in both passes | 37 (p. 486) | 85 | 195 (455:20 456:82 457:74 458:19) | 90 |
| Discrepancies adjudicated | 4 | 13 | 14 | 17 |
| Skipped: no word (`—`) | 2 | – | 2 | – |
| Skipped: ethnonym / spirit name | – | 5 / 1 | – | 9 / 1 |
| Skipped: other-language word | – | 1 | – | 0 |
| Skipped: unreadable / not found | 0 | 0 | 0 | 0 |
| Forms kept | 35 | 78 | 193 | 80 |

Totals:
- Auischiri: 113 forms, 110 distinct glosses, 67 mapped, 58 forms with `unclear:`.
- Omurana: 273 forms, 268 distinct glosses, 180 mapped, 53 forms with `unclear:`.
- Dataset: 386 forms, 324 distinct glosses (`parameters.csv`), 203 mapped.

The four ethnonym rows that the passes disagreed on (Andoa, Kokama, Stamm, Kichos) were
excluded and not adjudicated further.

## Auischiri word list (§76, p. 486)

No skeleton problems.

Discrepancies between the passes: 4 of 37 rows. Each was settled against the image; the format is page/col/row, gloss, pass 1, pass 2, final, reason.

```
559/1/5	Kopf	P1=awarēkĕ́	P2=awarēkĕ	FINAL=awarēkĕ	2nd reading: final ĕ has a breve only, no acute
559/1/10	Mond	P1=ṓ̱sa	P2=ȫ̱́sa	FINAL=ȫ̱́sa	2nd reading at 1600 dpi: o with diaeresis, macron and acute above and a line below
559/1/12	Stein	P1=noklo̯ā́xẹ	P2=noklo̯ā́xe̯	FINAL=noklo̯ā́xẹ	2nd reading: dot (not arc) below the final e
559/1/18	Huhn	P1=- (aắ)	P2=- (aā́)	FINAL=- (aắ)	2nd reading: breve+acute over the second a; printed with a short dash before the bracketed form
```

## Auischiri ethnographic text (§§1–75, pp. 475–484)

All 85 passages were found by pass 2.

Discrepancies between the passes: 13 of 85 rows. Each was settled against the image; the format is page/col/row, gloss, pass 1, pass 2, final, reason.

```
548/1/3	Kichos	P1=aϑaắkĕ	P2=aϑaā́kĕ	FINAL=aϑaắkĕ	ethnonym row, excluded from forms; not adjudicated further
548/1/7	Bixa	P1=uϑlawắn	P2=uϑlawā́n	FINAL=uϑlawắn	unclear: acute over a short mark; flat (macron) vs curved (breve) base is at the limit of the scan (read breve+acute, as in ắsa on p. 478)
550/1/10	Angel	P1=osö̱́ū́	P2=osȫ̱ū́	FINAL=osȫ̱ū́	2nd reading at 2000 dpi: o with diaeresis and macron above and line below, no acute; u with macron+acute
550/1/17	Makabo	P1=ắsa	P2=ā́sa	FINAL=ắsa	2nd reading at 2000 dpi: curved base under the acute (breve+acute)
550/1/19	Guilelma-Palme	P1=ắrō	P2=ā́rō	FINAL=ắrō	unclear: acute over a short mark; flat (macron) vs curved (breve) base is at the limit of the scan (read breve+acute, as in ắsa)
550/1/21	Eisenaxt	P1=aksakū́ka	P2=aksakŭ́ka	FINAL=aksakŭ́ka	2nd reading at 2000 dpi: curved base under the acute (breve+acute)
551/1/13	Kalebassen	P1=ă'orḗki	P2=ā'orḗki	FINAL=ā'orḗki	2nd reading at 2000 dpi: macron (not breve) over the first a
552/1/3	Schnüre	P1=ake̯rī́ṅ	P2=ake̯rĩ́ṅ	FINAL=ake̯rī́ṅ	unclear: acute over a short mark; flat (macron) vs curved (breve) base is at the limit of the scan; could be tilde+acute
552/1/7	Baumwollfaden	P1=noku̯é	P2=noku̯ḗ	FINAL=noku̯é	unclear: mark over e read as acute (pass 2: macron+acute)
552/1/8	Körbe	P1=haŏ́	P2=haṓ	FINAL=haŏ́	unclear: acute over a short mark; flat (macron) vs curved (breve) base is at the limit of the scan
552/1/9	Carloduvica trigona	P1=rĭ́ō	P2=rĩ́ō	FINAL=rĩ́ō	unclear: mark under the acute on i read as tilde (pass 1: breve)
554/1/1	Längsflöte	P1=wāli-wā́li	P2=wãli-wã́li	FINAL=wãli-wã́li	2nd reading: tildes (not macrons) over the a's
556/1/2	Coitieren	P1=kokā́a	P2=kokắa	FINAL=kokắa	2nd reading: curved base under the acute (breve+acute)
```

## Omurana word list (§76, pp. 455–458)

No skeleton problems. Both passes put the unnumbered entries at the top of p. 458 (above 'Chibito.') in the Omurana list.

Discrepancies between the passes: 14 of 195 rows. Each was settled against the image; the format is page/col/row, gloss, pass 1, pass 2, final, reason.

```
527/2/12	Speise	P1=njiyanī́	P2=njiyanî	FINAL=njiyanî	unclear: rounded cap over the final i read as circumflex (could be a damaged macron+acute)
527/2/19	Blitz	P1=ṛūviḗ̱	P2=rūviĕ̱́	FINAL=ṛūviḗ̱	unclear: dot below r faint; mark over final e read as macron+acute (could be breve+acute)
527/2/21	Regen	P1=a ϑn̄́	P2=aϑń	FINAL=a ϑn̄́	unclear: space before ϑ as printed; mark over n read as macron+acute (could be acute only)
527/2/23	Nacht	P1=nṓpei,	P2=nṓpei	FINAL=nṓpei,	comma printed after the form (punctuation; removed from Form)
528/1/24	Ei	P1=ū͜ū́n	P2=ū͜ŭ́n	FINAL=ū͜ŭ́n	2nd reading: second u has breve+acute; tie below joins the two u
528/1/26	Ara chloroptera	P1=be̱ṓli	P2=bē̱ṓli	FINAL=bē̱ṓli	unclear: faint macron above the underlined e
528/1/28	Papagei	P1=tī'wḗ̱	P2=tī'wĕ̱́	FINAL=tī'wḗ̱	2nd reading: macron+acute (cross-shaped) over e
528/1/32	Arapaima (paiche L.)	P1=paitsḗ	P2=paitsĕ́	FINAL=paitsḗ	unclear: mark over e read as macron+acute (could be breve+acute)
528/2/4	Eunectes (boa)	P1=tá̱à̯u	P2=tá̱a̯ù	FINAL=tá̱a̯ù	2nd reading: arc below the second a, grave over u
528/2/6	Milbe (isangüe)	P1=i ϑū́nắ	P2=iϑū́nắ	FINAL=i ϑū́nắ	2nd reading: space before ϑ as printed
528/2/10	Feuerholz	P1=n̄́jāo̯	P2=ńjāo̯	FINAL=ńjāo̯	2nd reading: acute only over n, no macron
529/1/7	Hemd	P1=íma	P2=íma'	FINAL=íma	unclear: faint broken mark after the a (speck, colon or apostrophe?), not transcribed
529/2/2	Spinne, bissig	P1=áawuei̯	P2=áawueị	FINAL=áawueị	unclear: small mark below the final i read as dot below (could be an arc)
529/2/7	essen (Form ?)	P1=pḗ̱nē̱iṅ	P2=pḗ̱nē̱īṅ	FINAL=pḗ̱nē̱īṅ	2nd reading: one bar spans e and i (transcribed as macron on both); dot above the final n
```

## Omurana ethnographic text (§§1–75, pp. 444–453)

All 90 passages were found by pass 2.

Discrepancies between the passes: 17 of 90 rows. Each was settled against the image; the format is page/col/row, gloss, pass 1, pass 2, final, reason.

```
514/1/4	Andoa	P1=otū́ba	P2=otū́bạ	FINAL=otū́ba	ethnonym row, excluded from forms; not adjudicated further
514/1/5	Kokama	P1=tabikī́ṅ	P2=tabikĩ́ṅ	FINAL=tabikī́ṅ	ethnonym row, excluded from forms; not adjudicated further
514/1/8	Stamm	P1=enḗmēnĕ̱dos	P2=enḗmēnĕ̱́dos	FINAL=enḗmēnĕ̱dos	ethnonym row, excluded from forms; not adjudicated further
514/1/10	Bixa	P1=rā́bĕ̱	P2=rắbĕ̱	FINAL=rā́bĕ̱	2nd reading at 1500 dpi: flat base under the acute (macron+acute), unlike the curved breve on ĕ
515/1/3	Matten	P1=ō̆pigó̱tšŏ̱	P2=ōpigṓ̱tšŏ̱	FINAL=ōpigṓ̱tšŏ̱	2nd reading at 1200 dpi: first o macron only; second o macron+acute with line below
516/1/8	Visier	P1=wiţzána	P2=wiţẓána	FINAL=wiţẓána	unclear: hook under t and small dot under z, both faint
517/1/5	Maisrauschgetränk	P1=aítšia-tšua	P2=aítšia-tšuạ	FINAL=aítšia-tšua	2nd reading: no dot below the final a
517/1/6	Tabak	P1=wa̱n	P2=wā̱n	FINAL=wa̱n	2nd reading: line below only, no macron above
517/1/11	Holzlöffeln	P1=atsē̱tsĕ̱	P2=atsḗ̱tsẹ̱̆	FINAL=atsē̱tsĕ̱	unclear: first e macron above and line below (no acute seen); second e breve above, mark below read as line
517/1/12	Kalebassen	P1=tóu̯wă	P2=tóy̯wă	FINAL=tóu̯wă	2nd reading: u with arc below (not y)
520/1/2	Schnüre	P1=ŏ́wi	P2=ðwi	FINAL=ŏ́wi	2nd reading: o with breve+acute (no ascender as on ð)
520/1/5	Aufbewahrungskörbe	P1=nē̱tŭ́	P2=nḗ̱tŭ́	FINAL=nē̱tŭ́	unclear: acute over a short mark; flat (macron) vs curved (breve) base is at the limit of the scan
521/1/2	Schnurrscheibe	P1=bufū́na	P2=bu-fū́na	FINAL=bufū́na	printed with a line-break hyphen (bu-/fū́na); hyphen treated as typographic and dropped
521/1/6	Ringkampf	P1=lē̱mī́ne	P2=lē̱mĭ́ne	FINAL=lē̱mī́ne	unclear: acute over a short mark; flat (macron) vs curved (breve) base is at the limit of the scan
522/1/2	Kauz	P1=ϑarā́ra	P2=ϑarắra	FINAL=ϑarắra	2nd reading at 2000 dpi: curved base under the acute (breve+acute)
523/1/3	Cyperus spec.	P1=pirī́p	P2=pirī́pi	FINAL=pirī́pi	2nd reading: final i present (pirī́pi)
524/1/1	Cohabitare in anum	P1=wawai̯ī́nĕ	P2=wawayī́nĕ	FINAL=wawayī́nĕ	2nd reading: fifth letter is y (descender)
```

## Integrity checks

- The CSVs were written with Python's csv module.
- IDs are unique in forms, parameters and languages; every `Language_ID` and `Parameter_ID` resolves; every `Source` key is in `sources.bib`.
- Every Concepticon_ID exists in the frozen Concepticon table, and the Glottocodes exist in the frozen Glottolog table.
- `arcaverborum.extensions.validate` was run against a temporary root that links the frozen reference tables: no problems.
