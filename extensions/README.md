# Source extensions

A **source extension** adds a new lexical source in a pull request. Use one
when the rows you need are not in the release's accepted-inputs snapshot, for
example your own fieldwork, a published wordlist, or a dataset not yet in
Lexibank.

Each extension is a folder named after its dataset identifier:

```
extensions/<dataset>/
    README.md         where the data come from, who prepared them and how
    metadata.csv      one row describing the source
    languages.csv     the varieties in the source
    parameters.csv    the source's concepts (meanings)
    forms.csv         the forms
    sources.bib       BibTeX for everything cited in forms.csv
```

The columns follow the intake schema of the Lexibank CLDF data.

| File | Required columns | Optional columns |
|---|---|---|
| `metadata.csv` | `Dataset`, `Title`, `Citation`, `License` | `URL`, `Repository_Version`, `CLDF_Module` |
| `languages.csv` | `ID`, `Name`, `Glottocode` | `ISO639P3code`, `Macroarea`, `Latitude`, `Longitude`, `Family`, `Location`, `Remark` |
| `parameters.csv` | `ID`, `Name` | `Concepticon_ID`, `Concepticon_Gloss` |
| `forms.csv` | `ID`, `Language_ID`, `Parameter_ID`, and `Value` or `Form` | `Local_ID`, `Segments`, `Comment`, `Source`, `Loan`, `Cognacy`, `Doubt`, `Cognate_Detection_Method`, `Cognate_Source`, `Alignment`, `Morpheme_Index`, `Segment_Slice`, `Graphemes`, `Profile` |

**Rules**, all checked by `python build.py extensions --check` and by CI:

- The folder name is the dataset identifier: lower case, `a-z`, `0-9` and
  `_`, not used by any other source. A `Dataset` column, if present, must
  match it.
- `License` must be a reviewed licence (see
  `src/arcaverborum/data/release_tiers.json`, for example
  `https://creativecommons.org/licenses/by/4.0/`). Undeclared terms cannot
  be contributed.
- Every Glottocode must exist in the frozen Glottolog table, and every
  `Concepticon_ID` in the frozen Concepticon table.
- IDs are unique within each file. Every `Language_ID` and `Parameter_ID`
  in `forms.csv` must exist in `languages.csv` and `parameters.csv`.
- Every BibTeX key starts with `<dataset>_`. Every key in a form's `Source`
  (separated by `;`, with optional `[pages]`) must exist in `sources.bib`.
- Put IPA in `Segments` (space-separated) only if the source gives a
  pronunciation. A spelling is not IPA because it tokenizes. Otherwise leave
  `Segments` empty, and add an orthographic profile to the variety (see
  `ONBOARDING.md`) if one is justified.

**Using the source.** Point a variety at it in `varieties/<av_id>/config.yaml`
(`sources: transcription: <dataset>`), or register a new variety, then
rebuild:

```bash
python build.py extensions          # validate and write intake/extensions/
python build.py update <av_id>
```

`update` and `aggregate` refresh `intake/extensions/` automatically.
Extensions stay in git permanently: they are build inputs in every
workspace, and they are never part of a snapshot. A pull request that changes
`extensions/` is rebuilt in full by CI.
