# Verification log: romero1768

Date: 2026-11-04.

## Method

**Pass 1.** I transcribed the list from renderings of PDF pages 14–23 (1-based),
which are printed pp. 10–19.
- Each page was read at 300 dpi in four overlapping horizontal strips.
- Every accent, special letter and doubtful glyph was then re-read on 500–2400 dpi
  zooms of the right-hand column.
- The OCR text layer (`_djvu.txt`) was not used for any reading.
- Pass 1 also fixed the selection of entries: 159 single-concept entries were kept,
  and the phrases were logged below.

**Pass 2 (blind, independent).** A separate sub-agent received only two inputs:
- the page images (300 dpi strips and 150 dpi full pages of pp. 10–18; p. 19 has no
  kept entries);
- the list of the 159 kept glosses (page plus the French and Spanish gloss line).

It never saw the pass-1 forms, the OCR or any other file. It recorded, for every
entry, the bracketed original spelling, Rivet's italic notation and its doubts. The
two readings were compared form by form with a script (`compare.py`). Every
disagreement was then settled on a 1200–2400 dpi zoom of the scan.

## Results

**Entries compared:** 159, with 181 form rows.

**Agreement:** 154 of 159 entries are letter-for-letter identical, including accents,
asterisks and spaces. The script also flagged 3 entries that are not real
disagreements: an unbracketed extra form after a bracket (*cœur* … *b-ibas-pa*,
*el abentador* … *\*pipi*, *moi, je* … *asa*). Both passes read them the same way.

**Disagreements (5), all resolved against the image:**

| # | Gloss | Pass 1 | Pass 2 | Resolution |
|---|---|---|---|---|
| 27 | chapeau | `sipanà` | `sipaná` | Kept `sipanà`. At 1600 dpi the mark is a small detached tick over the a. It has the same shape as the clear grave in *bisià* (p. 18), not the tall acute fused to the a (as in *lamá* and *auciá*). Flagged `unclear` in Comment. |
| 98 | marmite | `lictinà` | `lictiná` | Same as 27. Kept `lictinà`, flagged `unclear`. |
| 51 | dormir | `angasa` | `angàsa` | Pass 2 is right. A small tick stands over the second a at 1200 dpi, and pass 1 had missed it. Changed to `angàsa`, flagged `unclear`. |
| 81 | jour (2nd line) | `baisa` | `baiśa` | A stray mark sits between the s and the a, not centred on either; it reads as a blemish. Kept `baisa`, with the Comment `unclear`. |
| 32 | chonta | `auma` (unbracketed) | `aumá` | At 1200 dpi the final a is plain. The supposed accent is the a's own stroke. Kept `auma`. |

**Doubts raised by pass 2 on agreed readings.** These were all checked and kept, with
a Comment where the doubt is real:
- `[titi]` 'froid' could look like *liti*. The crossbars are lost in the scan, and
  Rivet's notation *ti-ti* supports t. Commented.
- `[sobesa]` could look like *sohesa*. Commented.
- `[yuiua]` could look like *vuiua*. The descender is the italic y used throughout,
  so no comment.
- `[vecaluta]`: the fifth letter is l, read the same way by both passes.
- `[tamais]` has a speck near the a/i, and `[cauba]` a speck over the a. Both taken as
  blemishes.
- `[*cauzà]`: the tick is near-vertical and read as grave. Both passes gave grave;
  commented.
- `[bicaïsa]` (*calentura ó calor fuerte*) prints a diaeresis that the same form lacks
  under *chauffer* and *calentura*. Both passes agree; transcribed as printed and
  commented.
- `[niniluša]` and `[maiša]` print š. Both passes agree.
- `[ataiza, ataisa]` (*sœur*) prints no asterisk on the second form. Both passes
  agree; commented.
- The italic z is printed with a descender (ʒ-like). Both passes read it as z.

**Unreadable rows skipped:** none.

## Selection log (skipped printed lines)

Phrases and sentences: 85 printed gloss lines. Lines marked (x) are Rivet's
cross-listed repeats.

- p. 10 (10): où vas-tu ?; je vais déféquer; je vais le voir [voy a verlo]; je m'en vais [me voy ya]; tu t'en vas; il s'en est allé [se fue ó no esta aqui]; va-t'en avec Dieu !; celui-ci m'a amené [este me llevo]; sommes-nous amis ?; oui, nous sommes amis.
- p. 11 (12): comment t'appelles-tu ?; comment s'appelle ceci ou cela ?; je t'apporterai [te traeré]; apporte-moi ceci ou cela !; apporte-moi une banane ! (twice); apporte-moi du chontaduro !; apporte-moi du feu !; je viendrai après (under après [despues]); non, au revoir [no, hasta luego]; je n'ai pas; je suis en train de me baigner.
- p. 12 (6): tu veux boire [quieres veber]; boire du masato; comment t'appelles-tu ? (x); comment s'appelle ceci ou cela ? [como se llama esto o aquello ?] (x); apporte-moi du chontaduro ! (x); j'ai compris.
- p. 13 (12): j'ai compris ce que tu me dis; que dis-tu que je ne te comprends pas ?; il est couché; couper cela; il y a ceci ou cela coupé [hay cortado esto o aquello]; ne crains rien, il ne t'arrivera rien [no tengas cuidado que nada te susedera]; qu'on le cuise vite !; je vais déféquer (x); tu me dois [me debes]; j'ai compris ce que tu me dis (x); que dis-tu … (x); donne-moi !.
- p. 14 (12): je suis encouragé (under encouragé [alentado]); j'ai entendu [yo he oido o entendido]; je n'entends pas; il est là; il n'est pas ici; il n'est pas ici [no esta aqui o no ha venido aqui]; où es-tu ?; où est-il ?; que fais-tu ?; femme (menteuse); ferme la porte !; apporte-moi du feu ! (x).
- p. 15 (2): tu veux manger; tu ne manges pas.
- p. 16 (9): ce n'est pas un mensonge [no es mentira]; femme menteuse [mujer embustera]; deux mois; il est mort [ya murió]; non, au revoir (x); où es-tu ? (x); où est-il ? (x); où vas-tu ? (x); d'où viens-tu ?.
- p. 17 (7): ne pleure pas !; ferme la porte ! (x); pose-le ! [ponlo tu]; que fais-tu ? (x); que veux-tu ? [que se ofrece o que quieres ?]; que dis-tu … (x); pour ordonner de répéter la même chose.
- p. 18 (8): je ne reviens plus; viens ici !; viens avec moi !; je viendrai après (x); d'où viens-tu ? (x); il n'est pas venu ici; voici [ai está]; — [ahi tienes].
- p. 19 (7): oui, je l'ai vu; je ne l'ai pas vu; je veux voir [quiero ver o mirar]; je vais le voir (x); je veux voir (x); tu veux boire (x); tu veux manger (x).

Borderline lines skipped as phrases: *il est couché*, *il est mort [ya murió]*,
*boire du masato*, *deux mois*, *femme menteuse [mujer embustera]*, *voici [ai está]*
and *[ahi tienes]*.

Cross-listed repeats of kept entries, with no extra row (4):
- *banane mûre* (p. 16);
- *planche de bambou* (p. 17);
- *plant de bananier* (p. 17);
- *tabac allumé* (p. 18).

## Integrity checks

Run with `tools/validate_ext.py romero1768`. It wraps the repository validator
`arcaverborum.extensions.validate` and adds the spec checks. It passes with 0 problems:
- CSV well-formed and NFC;
- IDs unique;
- every `Language_ID` and `Parameter_ID` resolves;
- every `Source` key is in `sources.bib`;
- `Segments` empty;
- every `Concepticon_ID` exists in the frozen table with a matching gloss;
- every `Name` contains ` | `;
- licence PDM-1.0 is on the reviewed list.

## Counts

| Item | Count |
|---|---|
| Pages | 10–19 (conventions on pp. 9–10) |
| Kept entries = distinct glosses (`parameters.csv`) | 159 |
| Glosses in Spanish (printed by Rivet) | 38 |
| Glosses in French (Rivet's translation; see README) | 121 |
| Concepticon-mapped glosses | 108 |
| Form rows | 181 |
| Bracketed original spellings | 144 |
| Unbracketed (Rivet printed no bracket; `Doubt = true`) | 37 |
| Second-copy (`*`) variant rows | 17 |
| Distinct form strings | 176 |
| Skipped: phrases and sentences (printed lines) | 85 |
| Skipped: cross-listed repeats of kept entries | 4 |
| Skipped: proper names, toponyms, ethnonyms | 0 |
| Skipped: unreadable | 0 |
