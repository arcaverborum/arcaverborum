# Slice additions

A release's accepted-inputs snapshot contains only the `(glottocode, dataset)`
groups of the intake that accepted constructions read when the release was cut.
A pull request that needs another group of a dataset the snapshot already
contains (for example IDS rows for a language that so far used another
source) commits that group here, exactly as it is in the full intake:

```
slices/lexibank/
    datasets.csv          Dataset, Repository_Version (must equal the intake metadata)
    forms.csv             whole groups of intake forms rows, intake column order
    parameters_raw.csv    the intake parameter rows those forms use
```

Create them on a workspace with the full intake (the maintainer's):

```bash
python scripts/add_slices.py cofa1242/idssegmented paez1247/hubercolumbian
```

The build (`build.py update`, `build.py extensions`) then:

- in a snapshot workspace (CI, contributors), adds the groups the intake lacks
  under `intake/slices/`, read after the Lexibank and Wiktionary intake;
- in a full workspace, adds nothing, after checking that each committed group is
  identical, row for row and in order, to the intake.

Anything else fails closed: a different dataset version, a partial or changed
group, an unknown language or parameter. New datasets are not slices; add them
as [source extensions](../extensions/README.md). The next release's snapshot
contains these groups; the committed rows are then redundant and still checked.
