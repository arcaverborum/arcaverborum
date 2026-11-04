# Tessmann 1930: Aewa (Auischiri) and Omurano (Omurana) lexical data

**Source.** Tessmann, Günter. 1930. *Die Indianer Nordost-Perus: grundlegende
Forschungen für eine systematische Kulturkunde.* Hamburg: Friederichsen, de Gruyter &
Co. (Veröffentlichung der Harvey-Bassler-Stiftung, Völkerkunde 2). Each tribe chapter
has numbered sections §1–§76, and §76 is the language sample. Two chapters are used:

| Variety | Chapter | Word list (§76) | Ethnographic text (§§1–75) | Glottocode |
|---|---|---|---|---|
| `tessmann1930_Auischiri`, "Auischiri" | pp. 475–486 | p. 486 (printed at the top of the next chapter, above "Ssimaku.") | pp. 475–484 | `abis1238` (Aewa / Aʔɨwa) |
| `tessmann1930_Omurana`, "Omurana" | pp. 444–458 | pp. 455–458 (the last unnumbered entries at the top of p. 458, above "Chibito.") | pp. 444–453 | `omur1241` (Omurano) |

The rows come from two kinds of material:
- **Word lists:** numbered German glosses, given as numbered by Tessmann.
- **Native words cited in the ethnographic prose**, where Tessmann explicitly equates
  a native word with a German term (e.g. "Tabak = *wa̱n*", "Cohabitare in anum heißt
  *wawayī́nĕ*"). Every such row has `Tessmann §<n> ethnographic text` and a short
  `ctx:` quote in `Comment`. List rows have `Tessmann §76 word list`, and `Local_ID`
  ends in `-no<n>` with Tessmann's list number.

The Auischiri word list has only 33 numbered items plus 4 unnumbered ones, so about
two thirds of the Aewa data come from the prose. This matches the "≈112 items" usually
cited for Tessmann's Aewa material; there are 113 forms here.

**Scan.** https://archive.org/details/tessmann-die-indianer-nordost-perus (uploaded
2026-10-08 and tagged PDM by the uploader). The PDF has sha256
`af30afc74fe912c6b4826e906fb7ecd2781ce25314d1778897f58a538159c067` and is 101,363,415
bytes, with 1035 PDF pages; the native scan is about 330 dpi. PDF index (0-based):
Omurana 513–529, Auischiri 547–559, key p. 47 = PDF 57. `pages/` holds 120-dpi
greyscale renderings of those PDF pages, named `pdfNNNN.png`. The plates at PDF 518,
519 and 553 are left out.

**Who and how.** The forms were transcribed by an AI agent from page images on
2026-11-04 and verified by a second, independent reading. Each list and each set of
prose items was re-read by a second reader from the images, given only the gloss
skeleton (for prose, the German term plus the sentence with the native word masked).
Every disagreement was settled against the image at 600–2000 dpi (see VERIFY.md).

## Tessmann's notation (p. 47, "Abkürzungen und Aussprache der kursiv gedruckten Eingeborenenwörter")

**Vowels and vowel marks**
- length is a macron above (ā), shortness a breve above (ă);
- open vowels have a line below (a̱, U+0331);
- close vowels have a dot below (ẹ ọ̈), marked only when the closeness is strong;
- nasality is a tilde;
- an arc below a vowel (U+032F) means it is only breathed; under a consonant it means
  the consonant is not sharply articulated.

**Other marks**
- letters in parentheses are fleeting (kept in `Form`);
- `'` is the glottal stop;
- a tie below joins sounds into one unit (U+035C, e.g. a͜u).

**Consonants**
- `s` is sharp and `z` voiced;
- `š` = German sch, `ž` = French j;
- `ϑ` is close to English th in *thief*; `ţ` is the same sound but more hissing; `ð` is
  the voiced one;
- `r` is lightly rolled, an r with a mark below is a hissing cerebral r
  (transcribed `ṛ`, because the mark reads as a dot at this scan resolution), and `ḍ` is a cerebral d close to l;
- `ṅ` is a slightly nasal ng and `v̱` is bilabial v;
- `j` is as in German *Jammer* and `y` is a semivowel;
- `γ` is fricative g and `x` is German ach-Laut.

**Also seen in the material**
- macron+acute stacked (printed like a small cross: ā́ ḗ ī́ ṓ ū́, n̄́);
- breve+acute (ắ ĕ́ ŏ́ ŭ́);
- o with diaeresis plus macron (ȫ, ȫ̱́);
- ditto marks `,,` (same as the preceding form);
- `—` for a missing word.

This is a pre-IPA phonetic notation. **`Segments` is empty.**

## Conventions

- NFC throughout. Line below = U+0331. Two encodings were canonicalised before the two
  readings were compared:
  - a dotless `ı` under a mark above was written as `i`;
  - U+0330 (tilde below), which a reader had used for the line below, became U+0331.
- `Value` is the printed entry. Spaces inside a form are kept as printed: Tessmann
  often sets a gap before the script ϑ (`na ϑṓro`, `a ϑn̄́`). Prose compounds keep
  their printed hyphens (`wan-dăwašín`); a hyphen that only marks a line break was
  dropped (`bufū́na`).
- `Form` changes from `Value` as follows:
  - `,,` is resolved to the preceding form, and `Comment` says so;
  - `- (atrḗwa)` / `- (aắ)` (Auischiri Kanu, Huhn) become the bracketed form, and
    `Comment` notes the printed dash;
  - a trailing comma is removed (`nṓpei,`);
  - Tessmann's `(?)` after a form is moved to `Comment`.
- `Parameter.Name` is `German term as printed | English`. Concepticon mapping is
  conservative: 203 of 324 glosses are mapped. Tessmann's "(Form ?)" verbs and
  "(?)" glosses are left unmapped.
- `Source` is `tessmann1930_Tessmann1930[page]`.
- Loans:
  - `Loan = true` for Omurana `wā́la` 'Kuh' (obvious identity with Spanish *vaca*) and
    Omurana `tiī́natšă` 'Krüge' (Tessmann compares Loreto *tinaja*).
  - Auischiri `aksakŭ́ka` 'Eisenaxt' is not flagged; Tessmann only says "vielleicht von
    hacha", and this is recorded in `Comment`.

## Exclusions

| | Auischiri | Omurana |
|---|---|---|
| Word-list rows read (both passes) | 37 | 195 |
| … `—` (no word): Hund, Tabak / Jahr, Affe allg. | 2 | 2 |
| Prose items read (both passes) | 85 | 90 |
| … ethnonyms (tribe names, self-name, "Weißen", "Stamm") | 5 | 9 |
| … spirit names (Einzeldämon `axḍaxĕ`; Dämonen `arḗne`) | 1 | 1 |
| … other-language word (Auischiri `wī́to` 'Genipa', "wohl Ketschuawort") | 1 | 0 |
| Forms | 113 | 273 |
| Distinct glosses | 110 | 268 |
| Concepticon-mapped glosses | 67 | 180 |

Loreto-Spanish words printed as `(xyz L.)`, Latin binomials and the other tribes'
lists were never transcribed. No row was unreadable.

## Licence

Published in 1930, so it is in the US public domain (pre-1931 publication; it entered
the US public domain on 1 Jan 2026). Tessmann died in 1969, so the book is still
protected in Germany and the EU until the end of 2039. **The maintainer has accepted US
public domain for this source.** Licence:
`https://creativecommons.org/publicdomain/mark/1.0/`. The archive.org PDM tag is the
uploader's claim and is not relied on.

## Known issues

- Diacritics are at the limit of the scan. 111 forms carry `unclear:` comments. Most
  concern whether the base under an acute is flat (macron+acute) or curved
  (breve+acute), the ð versus ṓ shape, and tilde versus macron over n.
- Identity:
  - **Auischiri** here is Tessmann's name for the Aʔɨwa/Aewa isolate (`abis1238`, ISO
    `ash`; self-name *tĕkirắka*). Keep it apart from Zaparoan "Aushiri" (`avs`); the
    names are conflated in catalogues.
  - The Aewa data come from **one informant** whom Tessmann describes as uncooperative
    (§73, §75), with no second informant to check against.
  - Omurana has two informants (§75); one had forgotten less common words.
- The existing northperulex rows for Omurano and Aewa (and the Wiktionary Omurano
  list, via O'Hagan) probably derive from this same Tessmann material, so they are not
  independent confirmation.
