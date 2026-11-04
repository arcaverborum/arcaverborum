# Koch-Grünberg 1928: Auaké (Arutani), Kaliána (Sapé) and Máku wordlists

**Source.** Koch-Grünberg, Theodor. 1928. *Vom Roroima zum Orinoco: Ergebnisse einer
Reise in Nordbrasilien und Venezuela in den Jahren 1911–1913.* Band IV: *Sprachen.*
Stuttgart: Strecker und Schröder. The volume was published posthumously and edited by
Dr. Hestermann. This extension uses Section III, "Isolierte Sprachen", first group:

| Variety (`languages.csv`) | Printed list | Pages | Glottocode |
|---|---|---|---|
| `kochgrunberg1928_Auake`, "Auaké" | AUAKE | 308–313 | `awak1251` (Awake, a dialect of Arutani `arut1244`) |
| `kochgrunberg1928_Kaliana`, "Kaliána" | KALIANA | 313–317 | `sape1238` (Sapé) |
| `kochgrunberg1928_Maku`, "Máku" | MÁKU | 317–324 | `maku1246` (Máku of the Uraricoera/Auari, ISO `xak`) |

The glosses are German, arranged by semantic field (A. Körperteile … Q. Verben). The
Fremdwörter and pronoun comparisons that follow on pp. 324ff. are not transcribed.

**Scan.** https://archive.org/details/bub_br_1918_01011140 (Biblioteca Brasiliana Guita
e José Mindlin copy, marked Public Domain Mark). The PDF has sha256
`2f686ea3b1add4fc03c18170626f3755420e9b91718439a0283a2fb6d86519f5` and is 11,444,581
bytes. Printed page = PDF index (0-based) − 13. `pages/` has 150-dpi renderings of
pp. 2–3 (the transcription key) and pp. 308–324.

**Who and how.** The forms were transcribed by an AI agent from page images on
2026-11-04 and verified by a second, independent reading. For each language a second
reader read every form from the images, given only the gloss skeleton (page, column,
row, German gloss) and not the first transcription. Every disagreement was settled
against the image (see VERIFY.md).

## Koch-Grünberg's notation (vol. IV, pp. 2–3, "Zur Transskription")

The transcription "follows in essence the Anthropos alphabet" (P. W. Schmidt 1907). The
key gives:

- vowel length: a colon after the vowel (`a:`);
- very short vowel: a breve (`ĭ`);
- all vowels can be nasal (tilde);
- `o` is usually open;
- `a̱` lies between a and o (English *walk*); `u̱` lies between u and o;
- `ẹ` is a reduced front e, tending to i, especially word-finally;
- `e̱` = German ä, French è;
- a further e "dumpf, fast wie u in englisch *hut*" (its diacritic is not legible in
  the scan);
- `a`/`o` followed by `i`/`u` are separate syllables unless the i/u carries the arc
  below (`i̯`, `u̯`) or an accent, which makes a diphthong;
- `w` = English w, `y` = English y in *youth*;
- `d` and `g` are weaker word-finally; `fʰ` lies between f and h;
- `x` = ch in German *nach*, `x̭` = ch in *nicht*;
- an `l` variant lies between l and r; `r` is rolled; a `z` variant is softer than
  English th;
- **sounds in parentheses are strongly reduced**, so the parentheses are part of the
  notation and are kept in `Form`;
- the apostrophe marks a laryngeal "Stocken" (glottal catch).

Notes in the lists add the following:

- the raised dot `·` marks a very short preceding vowel (Máku, p. 318, fn. 1);
- in Kaliána, ẹ "is everywhere reduced, … hardly distinguishable from reduced i" (p. 315);
- an acute printed after ẽ̱ / ũ̱ ("Akzent hinter ẽ̱ und ũ̱", p. 308) is written as a
  spacing acute `´` (U+00B4) at that position.

This is an era-specific phonetic notation, not IPA. **`Segments` is empty.** A reviewed
profile is a later step.

## Conventions

- **Unicode.** NFC throughout, with these choices:
  - a short line below = U+0331 (`e̱ a̱ u̱`);
  - a dot below = U+0323 (`ẹ`, also `ạ ọ ḥ ṇ ỵ ḍ`);
  - a caret below = U+032D (`x̭ z̭`);
  - the non-syllabic arc below = U+032F (`i̯ u̯ a̯`);
  - tilde and acute stacked on one vowel = tilde then acute (`ã́`);
  - ASCII `'` for the glottal hook and `:` for length.

  Small rings under e, printed alongside solid dots on the same pages, are written as
  dot below and say "ring-shaped" in `Comment`. A few vowels show a dot above a short
  line (`ẹ̱`), and these are kept.
- **`Value`** is the printed entry for the gloss. Footnote reference numbers are left
  out, and the footnote text goes into `Comment` (`fn<n>: …`).
- **`Form`** gives one alternative per row: alternatives separated by `,` or `;` become
  separate rows with the same `Value`. Hyphens are kept (`ki-takohẽ́`; a footnote says
  `ki-` is probably a pronominal prefix). Three printed gloss additions are moved to
  `Comment`: `(„Wasserjaguar“)`, `(= Holz)` and `(= Hüftschnur)`; the
  `(„Genipapofrucht“)` addition is handled the same way.
- **Line breaks.** A hyphen printed only because a Máku form wraps across a line
  (8 cases, e.g. numerals 8, 9, 10, 20) is treated as typographic and dropped, and
  `Comment` gives the printed split. In Kaliána two hyphens at line ends,
  `kãh(ẽ)-yãũã́` (Fischotter) and `(m)ba-kína`, were kept as printed because they could
  be morpheme boundaries.
- **`Parameter.Name`** is `German gloss as printed | English`. There are 508 distinct
  glosses for the three languages together; the Concepticon mapping is conservative
  (333 glosses mapped).
- **Phrases.**
  - Imperatives and person-marked single-verb entries ("schlage!", "ich schlafe",
    "töte!") are kept as one lexical concept but are not mapped to Concepticon.
  - Entries marked `phrase` in `Comment` that are kept: multi-word but single-concept
    renderings.
- **`Source`** is `kochgrunberg1928_KochGrunberg1928[page]`.
- **Loans.** `Loan = true` is set only for obvious identity with Portuguese/Spanish,
  in Máku only:
  - `tsambẹlélo` 'Hut' (sombrero);
  - `kamitšá, kamidžá` 'Hemd' (camisa);
  - `kau̯alé̱, kawalé̱` 'Pferd' (cavalo);
  - `paká` 'Rind' (vaca).

  Koch-Grünberg's own Fremdwörter lists (pp. 324ff.), which flag Carib and Arawak
  loans such as the gun/powder terms, were not used to set the flag.

## Exclusions (by language)

| | Auaké | Kaliána | Máku |
|---|---|---|---|
| Printed gloss rows (both passes) | 298 | 188 | 406 |
| Skipped: sentence/phrase | 9 | 9 | 0 |
| Skipped: name (Makuschi, an ethnonym) | – | – | 1 |
| Skipped: other-language word | – | – | 1 (Fuchs `mai̯ká`, "Taulipáng-Wort; der Fuchs kommt dort nicht vor") |
| Entries kept | 289 | 179 | 404 |
| Form rows | 328 | 198 | 465 |
| Glosses with a Concepticon mapping | 213 | 140 | 272 |

The skipped sentences are "bring Wasser!", "gib mir Bananen!", "er kommt heute",
"ich will pissen", "laßt uns Kaschiri trinken!", "das Kind weint", "wirf den Stein!",
"willst du Bananen?", "laßt uns alle gehen!", "da kommt Regen!" and "komm her, Tante!",
each where present in that language. No row was unreadable.

## Licence

Published in 1928. Koch-Grünberg died in 1924, so the work is in the public domain:
it is more than 70 years post mortem auctoris, and it is US public domain as a pre-1931
publication. The scan is also marked PDM by archive.org. Licence:
`https://creativecommons.org/publicdomain/mark/1.0/`.

## Known issues

- The scan resolution limits diacritic reading. 56 rows carry `unclear:` comments,
  mostly about worn italic u/n/w/a and the exact mark (tilde vs. macron, dot vs. line
  vs. ring) under or over a vowel. The "dumpf" e of the key could not be identified in
  the lists.
- Identity:
  - Auaké is Arutani (`awak1251`, a dialect of `arut1244`). The modern CC BY 4.0 Arutani
    dictionary (Chacon, Rosés Labrada et al. 2024) is a separate source; this list is
    the 1911–13 historical layer, not independent confirmation of it.
  - Kaliána = Sapé.
  - Máku is the Roraima/Auari isolate (`maku1246`), not the Nadahup "Makú".
- Vol. IV gives no informant or place details for these lists; they are in
  Koch-Grünberg's travel volumes (I–III), which were not consulted.
