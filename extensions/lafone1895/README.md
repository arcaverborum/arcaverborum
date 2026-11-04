# lafone1895: Vilela ("Chulupí"), Pelleschi's vocabulary in Lafone Quevedo 1895

**Source.** Lafone Quevedo, Samuel A. 1895. "La lengua Vilela ó Chulupí: estudio de filología chaco-argentina fundado sobre los trabajos de Hervás, Adelung y Pelleschi." *Boletín del Instituto Geográfico Argentino* 16: 37–124. This extension covers only the **Vocabulario Chulupí ó Vilela** on pp. 113–121:

* Chulupí–Español, pp. 113–117 (Vilela headword in bold, Spanish gloss, usually an English gloss);
* Español–Chulupí, pp. 118–121 (Spanish headword in bold, Vilela forms in roman).

Lafone says the vocabulary "es copia fiel de los apuntes de Pelleschi", alphabetised in both directions (p. 40). It is the word list of the Italian engineer Juan (Giovanni) Pelleschi. In a letter quoted on p. 53, Pelleschi says he met Vilelas living among "tame" Matacos at Fuerte Gorriti near Rivadavia on the Bermejo river, and that their chief was a Vilela. Lafone's own analyses are on pp. 64–112, outside this extension. Their glosses, readings and comparisons were not transcribed.

**Scan.** `https://upload.wikimedia.org/wikipedia/commons/f/f1/BaANH50369_Boletin_del_Instituto_Geogr%C3%A1fico_Argentino_%28Tomo_XVI_1895%29.pdf` (BaANH scan of tomo XVI on Wikimedia Commons). sha256 `fc0f9a0986b1026f9133ba19ccc38a953728a4662629c6e9a64a6131733f1b4b`. The PDF page number equals the printed page number (PDF p. 113 = printed p. 113). The scan has an OCR text layer, but it is unreliable for accents (é/ó confusions, especially on pp. 120–121). Page images at 150 dpi are in `pages/`.

**Preparation.** Transcribed by an AI agent from page images (400–1000 dpi crops) on 2026-11-04 and verified by a second reading from fresh crops (not strictly blind; see `VERIFY.md`).

## Identity

"Chulupí" in this work means **Vilela** (Chunupí/Chulupí of the Bermejo–Salado region; vile1241). It is **not** Nivaclé, the Matacoan language that is also called "Chulupí". Lafone's title equates the two names, and Pelleschi reports that "Vilela y Chulupy eran la misma cosa" (p. 53). There is one variety (`lafone1895_vilela`). The vocabulary does not distinguish sub-sources. A handful of entries carry "(P.)" or "P." for Pelleschi, which is recorded in `Comment`. Lafone's key on p. 65 reads "P ó Pell = Pelleschi".

## Notation (all from the vocabulary itself; no general key is printed)

Pelleschi uses a Spanish/Italian-based spelling. The printed notes are kept in `Comment` as "source note":

* *c = k* (Calticq); *c = c toscana* (Nomcopé); *h como c toscana* (Chihi), i.e. the Tuscan aspirated [h]/[x]-like *c*;
* *ii = j toscana* (Niiéh);
* *l mojada* (Calticq, Quighelé), *ch mojado/mojada* (Jchumi), *tch mojada* (Tchurubép), all meaning "wet" (palatalised);
* *l rápida* (Uljhui);
* *s dulce* (Húsebépp);
* *th con aliento cortado* (Nihthemuí), *con aliento adentro el chu* (Chuhpi);
* *(lengua para atras del paladar)* (Hujqué);
* footnote to Nij-tziss: *La ts—sibilante. P.*;
* *(=d)*, *(-d)* after Tacáj/tacaj;
* acute accents mark stress. Doubled letters (*bépp*, *mm*, *ss*) and *cqu*, *qu*, *j*, *jch* are printed as they stand.

None of this is IPA. `Segments` is empty. Any profile is a later, reviewed step.

## Conventions

* `Value` is the full printed entry (headword, gloss, English gloss and notes), with line-break hyphens joined. `Form` is one Vilela form. Entries with alternatives ("a, b", "a vel b", "a; b") give one row per alternative with the same `Value`.
* Some compounds are printed with an internal comma or full stop. These were kept as **one** form, exactly as printed, when the other direction of the vocabulary shows that they are a single compound: *Uambépp, ajtsitiss*; *ni-temú, iajsiss*; *eté. pabhuáj*; *mmaic, bumbápp*; *cquihii, sulumpé*; *umcquéi, quiropaj*; *quihi, quijlé*; *sú,bél-l*.
* Cross-references ("Ver X", "ver X") are left in `Value` and `Comment`. The cross-referenced form is not added as a row unless it is printed as an entry or alternative itself.
* `Parameter`: one parameter per distinct printed Spanish gloss. Glosses are compared case- and accent-insensitively, ignoring punctuation. A few spelling or index variants of the same gloss are merged explicitly: frazada = frasada, ligero = lijero, vestite = vistete, "Natura h" = "natura de hembra", "Ojo, s" = "ojo, y ojos", "Palma de la mano" = "palmas de la mano", "oreja (mi)" = "mi Oreja", "Vuestro etc." = "vuestro, de vos", "cinco etc." = "cinco", "Voy" = "me voy". `Name` is the first printed occurrence, followed by ` | ` and an English translation. Pelleschi's printed English is reported in `Value`.
* **Duplicates across the two directions.** There is one row per distinct (form, gloss) pair. If the same form, compared exactly apart from the capitalised first letter of a CE headword, appears under the same gloss in both directions, it is one row. `Form` and `Value` come from the first occurrence (normally Chulupí–Español), `Source` lists both pages, and `Comment` quotes the other entry ("also Español-Chulupí p. N: '…'"). Forms that differ in any letter or accent (e.g. *Hilát* / *hilat*, *La-huue* / *la-huué*, *Tucá-hupp* / *tacá-hupp*) are separate rows. 172 rows are attested in both directions, 119 only in Chulupí–Español and 119 only in Español–Chulupí.
* `Comment` begins with the direction the row comes from.
* **Loans.** `Loan = true` is set only for *Gato* 'gato', *Vaca/vaca* 'vaca' and *Tahuaco* 'tabaco', which are obviously identical with the Spanish gloss, and for *Ajbulún* 'vístete', which the source marks "(es mataco)", i.e. a Mataco word.
* **Kept as single concepts:** imperatives and other single-verb glosses (*bañate*, *andate*, *hablad*, *vamos*, *durmamos*, *me voy*, *he comido*, *copulam habere* …) and possessed nouns (*mi padre*, *tu oreja*, *penis mio* …). These are unmapped unless the plain concept fits.
* **Concepticon** (128 of 221 parameters) was mapped conservatively. Plural body-part glosses (*dientes*, *ojos*, *labios*, *orejas*, *dedos*) map to the singular concept. Ambiguous glosses are unmapped: *alto* (high/tall), *pecho* (breast/chest), *tierra*, *sombra* (shadow/shade), *laguna*, *cuero*, *cáscara*, *mucho*, *no*, *vos*, possessed forms and imperatives.

## Counts and exclusions

The two lists have 654 printed entries (Chulupí–Español 341, Español–Chulupí 313). They yield 410 rows (407 distinct forms) and 221 parameters, of which 128 are Concepticon-mapped. Excluded (logged in `VERIFY.md`):

* 141 phrases or sentences whose gloss is not a single lexical concept (CE 65, EC 76): e.g. *no mates los perros*, *tengo hambre*, *¿quieres comer?*, *boca del gato*, *hombre grande*, *casa grande*, *mi padre viejo*, negative imperatives such as *no te bañes*, and *no hay*;
* 10 proper names, toponyms or ethnonyms: *Rio Bermejo* ×2, *Tobas* ×4, *Matacos* ×2, *Chiriguano(s)* ×2;
* 7 pure cross-references with no form of their own ("Nuj quiiribá, ver Ajbulin", …);
* 2 editorial entries: "Lule maslup, ver tu oreja, dudoso" (Machoni's Lule form) and "Yulo-naptorit, yulos-naptorita úhué, pájaros lacustres grandes y zancudos" (an explanation of the gloss *yulo*; its forms are already rows under *yulo/yulos*);
* 1 mis-indexed entry: "Grande, uamcquiimbápp" (the form is *Uamcquiimbápp* 'casa grande').

**Not done:** the Apéndice "Vocabularios de los indios Chunupíes" (pp. 122–123), Ambrosetti's, Fontana's and Pelleschi's comparative lists of about 40 concepts. It is outside pp. 113–121 and comes from different collectors, so it would need its own sample rows. The Padre-nuestro (Hervás/Adelung) and Lafone's grammatical examples elsewhere in the article were not transcribed either.

## Licence

Published in 1895, so it is public domain in the US (published before 1931). Lafone Quevedo died in 1920. Pelleschi's death year was not checked; the maintainer's rule makes it irrelevant for a pre-1931 publication. The Commons file is tagged public domain. Licence: Public Domain Mark 1.0.

## Known problems

* This is a single amateur collector's notes, edited by Lafone, who admits that "reina algo de confusión en los apuntes de Pelleschi" (p. 69). The two directions disagree in many accents and letters; all such variants are kept as printed.
* Several pronoun glosses are inconsistent in the source: *Ni-te-laj* is glossed both 'yo' and 'nosotros', and *Nam-quié* both 'tú' and 'vosotros'. They are kept as printed.
* Unclear readings are flagged in `Comment` ("unclear: …"): *mina* (EC 'Agua', possibly a damaged *mma*), *lœc nitemui*, *ajeté*, *ni-tuichué*, *tacá-hupp*, *mmaic*, *núhú*, *olöh* and *ücope* (two dots, possibly a damaged acute), *gále-moyáj* (initial g), and the italic gloss *copulum/copulam habere*.
