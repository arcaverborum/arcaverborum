# Releases

## Identifiers

A release is identified as `<schema letter>-<YYYY-MM-DD>`, for example
`A-2026-11-10`; a second release on the same day is `A-2026-11-10.2`. The same
string is the git tag, the Zenodo version and the archive names.

The **schema letter** changes only on a breaking change to the published
tables: a column removed or renamed, a column's meaning changed (including its
value vocabulary or null convention), an identifier scheme changed, or a file
restructured. Added columns, added records and corrections keep the letter.
Read tables by header, never by column position.

Tags and assets are immutable. Each release has a changelog in its notes, and a
superseded or withdrawn release says so there. Candidates are CI artifacts or
untagged drafts; there are no public release candidates.

## Assets

| Asset | Contents |
| --- | --- |
| `arcaverborum-<id>-full.tar.gz` | every accepted record, including sources whose terms are undeclared (`terms_status = missing_declaration`) |
| `arcaverborum-<id>-redistributable.tar.gz` | records whose source declares redistributable terms (CC BY, BY-SA, BY-NC, BY-NC-SA, GPL-3.0, public domain) |
| `arcaverborum-<id>-by.tar.gz` | CC BY 4.0 and public-domain records only |
| `arcaverborum-<id>-snapshot.tar.gz` | the accepted-inputs snapshot (follows the `full` tier's terms) |
| `arcaverborum-<id>-site.tar.gz` | the explorer, code and data from the release commit (deployed to arcaverborum.org) |
| `SHA256SUMS` | checksums of all of the above |

Tier allowlists live in `src/arcaverborum/data/release_tiers.json`; an
unknown licence string fails the build. A record belongs to a tier only if the
terms of both its transcription source and its cognate source are allowed
there. Curation files (`curation/<av_id>/`) are included only for
constructions whose every source is in the tier.

Each tier archive contains `data/` (native tables: forms, varieties, concepts,
sources, bibliography, recordings), `cldf/` (a CLDF Wordlist of the same rows,
checked for referential integrity), `curation/`, `wordnet/`, `LICENSES.md`,
`README.md`, `CITATION.cff` and `MANIFEST.json` (counts, sources, terms, file
checksums, git commit and snapshot checksum).

## Licensing

Records keep their source's terms (per-row `License`, `terms_status`). Arca's
own work (identifiers, catalogs, concept/WordNet links, scores, code-generated
products) is CC BY 4.0. Adaptations of ShareAlike records keep the source's
terms. Reviewed corrections of source declarations are bound to the exact
accepted records and evidence in `src/arcaverborum/data/source_term_overrides.json`
(evidence under `docs/evidence/source-terms/`). Code is MIT.

## Cutting a release (maintainer)

On the maintainer's full workspace (complete intake):

```bash
python build.py update --all && python build.py aggregate      # must be complete
python build.py snapshot output/snapshot --archive arcaverborum-<id>-snapshot.tar.gz
python scripts/verify_rederivation.py arcaverborum-<id>-snapshot.tar.gz /tmp/rederive --web
ARCA_BUILD_DATE=<date> python scripts/build_research_web.py --with-communities
python build.py release <id> --snapshot-sha256 <sha>
python scripts/build_site_bundle.py release <id> arcaverborum-<id>-site.tar.gz --release-dir output/release/<id>
python scripts/seal_release.py <id> --extra arcaverborum-<id>-snapshot.tar.gz arcaverborum-<id>-site.tar.gz
git tag <id> && git push origin <id>
gh release create <id> output/release/<id>/*.tar.gz output/release/<id>/SHA256SUMS --title "Arca Verborum <id>"
python scripts/zenodo_deposit.py <id> --dry-run
```

The site and snapshot builders write multi-GB temporary files: point `TMPDIR` at a
disk with room (a small in-memory `/tmp` fails with "database or disk is full").

`verify_rederivation.py` exports the committed tree into an empty directory,
unpacks the snapshot, rebuilds offline and compares every derived file with
the reference build byte for byte.
