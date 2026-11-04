# Créqui-Montfort & Rivet 1913: Kaničana (Canichana) vocabulary

**Source.** Créqui-Montfort, Georges de & Paul Rivet. 1913. "Linguistique bolivienne.
La langue Kaničana." *Mémoires de la Société de Linguistique de Paris* 18: 354–377.
The article has three parts:
- a source list and notation note (p. 355);
- a grammatical sketch (pp. 355–364);
- **"I. Vocabulaire"** (pp. 364–376), transcribed here.

It is followed by "II. Textes" (pp. 376–377), which is not used. The vocabulary is
alphabetical by French headword. Some headwords have indented species sub-entries
(Oiseau, Poisson, Serpent, Singes). Each Kaničana form is followed by the number of the
source it comes from (p. 355, note 2):

| Tag | Source (as listed by the authors) | Variety row here |
|---|---|---|
| (1) | d'Orbigny, *L'homme américain* (1839), p. 80 [23 words], **plus the unpublished remainder of d'Orbigny's vocabulary, printed here for the first time** | `cmrivet1913_dOrbigny` |
| (2) | Heath 1883, *Kansas City Review* 6(12): 683–687 [165 words] | `cmrivet1913_Heath` |
| (3) | Cardús, *Las misiones franciscanas entre los infieles de Bolivia* (Barcelona 1886), pp. 316–317 [48 words and phrases] | `cmrivet1913_Cardus` |
| (4) | Teza 1868, *Saggi inediti di lingue americane*, p. 129 [religious texts] | `cmrivet1913_Teza` |

All four rows have the Glottocode `cani1243`. They are not dialects: they are the
authors' four documentary sources, kept apart so that provenance stays explicit.
Forms tagged with two sources, such as `(1-3)` or `(1-2)`, give one row in each source's
variety, and `Comment` says so.

**Scan.** https://archive.org/details/mmoiresling18soci (the whole of MSL t. 18,
University of Toronto Robarts Library copy). The PDF has sha256
`d08a071aea2f01c45fcc975ee839d6fde7582e55fc5bc50c23d7a19657a4fe2b` and is 30,944,752
bytes. Printed page = PDF index (0-based) − 15. `pages/` has 110-dpi greyscale
renderings of pp. 354–355 and 364–376. An earlier offprint on archive.org
(`rosettaproject_caz_morsyn-1`, sha256
`32978f36e5fcd2f295b9e6bdf8234080711cd26f474073b4689228a6a44dba64`) covers only pp.
354–364 and has no vocabulary. Persée, which hosts the JSA, is blocked from the working
machine, so no JSA version was checked.

**Who and how.** The forms were transcribed by an AI agent from page images on
2026-11-04 and verified by a second, independent reading. The second reader read every
form from the images, given only the skeleton (page, French headword, source tag), not
the first transcription. All 16 disagreements were settled against the image (see
VERIFY.md).

## Notation

The authors write the forms "in our phonetic notation" and refer to Créqui-Montfort &
Rivet, "Linguistique bolivienne. Le groupe Otukè", *JSA* n.s. 9 (1912): 317–337,
p. 318 n. 2, for its key. That key was not consulted. The notation uses:
- č, š, ž;
- x (velar fricative);
- acute accents;
- an apostrophe after l (`ni-čal'a`, `kol'exa`), apparently palatalisation;
- dot below on vowels (`eu-čeku-taulẹ`);
- ô (`ni-kôl`).

**These are respellings by the authors, not the original sources' orthography.** For
example, Heath's `Hio-chá-ma` 'Man' reappears as (2) `hiočáma`. **`Segments` is empty.**

## Conventions

- NFC. `Value` is the form exactly as printed, including Cardús's context words in
  square brackets. `Form` removes the bracketed context words: for example
  `[euxali] cev-atixigi [ni-koxolani ni-suera]` under Tuer gives `cev-atixigi`. It also
  removes a trailing `?` or `,`. The French translation printed with a Cardús phrase is
  in `Comment` as `tr: …`. When a whole sentence is printed without brackets for a
  single-concept headword (e.g. Chercher `naku een-axgue`), it is kept as the form:
  11 multi-word forms, all Cardús.
- Printed misprints are kept as printed and noted: `nel-siclo` for `nel-sielo`, `cev-`
  vs `eev-`, `nihuus` vs `nihuas`, `ercrets`. A hyphen that only marks a line break
  inside a word was dropped (3 cases, noted). Hyphens at line ends that coincide with
  morpheme boundaries were kept.
- Sense qualifiers printed next to a form, Latin/Spanish species names, cross-references
  `[cf. …]` and footnotes are in `Comment`.
- `Parameter.Name` is `French headword as printed | English`. There are 404 headwords
  and sub-entries; 307 are mapped to Concepticon, conservatively.
- `Source` is `cmrivet1913_CrequiMontfortRivet1913[page]`.
- No `Loan` flags are set. Cardús phrases contain Spanish *Dios*, recorded as part of
  the phrase.

## Exclusions

- 609 printed form tokens give 612 rows: four `(1-x)` doubles and one exclusion.
- `kukurulu` under Rivière ("au Nord de San Pedro", fn. "Cf. p. 354, note 1") has no
  source number and is excluded.
- The Cardús jaguar phrase under Jaguar, which also has no number, is assigned to
  Cardús (3). It is the same phrase printed under Flèche/Tuer with (3).
- No form was unreadable. No names were skipped; "Indien" is kept as a common noun and
  is unmapped.

| Variety | Forms | Distinct glosses | Mapped |
|---|---|---|---|
| d'Orbigny (1) | 366 | 339 | 247 |
| Heath (2) | 161 | 158 | 148 |
| Cardús (3) | 82 | 52 | 46 |
| Teza (4) | 3 | 3 | 2 |

## Licence

Published in 1913 in France. It is US public domain (pre-1931). It is not yet public
domain in the EU: Rivet died in 1958, and Créqui-Montfort died in 1966, if that year
is right, which would put the end of the EU term at the end of 2036. **The maintainer
has accepted US public domain for this source.** Licence:
`https://creativecommons.org/publicdomain/mark/1.0/`.

## Known issues and identity

- **Not independent data.**
  - The (2) rows are Heath 1883 respelled; the same forms are in extension
    `heath1883` in Heath's own spelling.
  - The (1) rows are the only access here to d'Orbigny's unpublished vocabulary
    (c. 1830s Moxos), and they are CMR's respelling of it.
  - Crevels 2012 and the existing Arca Canichana rows (northperulex) may derive from
    these same sources, so check them before counting them as independent.
- 15 rows carry `unclear:` comments, for example the italic c vs e in `chu-uku` / `chué`
  and `titidii` vs `titilii`.
