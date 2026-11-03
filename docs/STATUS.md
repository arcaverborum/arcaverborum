# Current project state

**Baseline for schema A (carried over from `tresoldi/arcaverborum`, 2026-11-02).**
Curation is frozen until release `A` is published; see [LAUNCH](LAUNCH.md).

| Measure | Accepted value |
| --- | ---: |
| Accepted constructions / lexical / recording-only | 7,371 / 7,369 / 2 |
| Lexical records / recordings | 2,120,263 / 755 |
| Supplied or upstream-converted / profile-backed readings | 1,750,036 / 22,178 |
| Supported core / all-concept slots | 470,153 / 1,209,325 |
| GLED primaries | 1,552 |
| Concepts with accepted WordNet links | 1,350 |
| Sources (by declared licence: CC BY / BY-SA / BY-NC / BY-NC-SA / GPL / PD / undeclared) | 194 / 6 / 13 / 8 / 2 / 1 / 2 |

- **Build integrity.** `build.py update --all` exits non-zero on any failed
  variety; `aggregate` refuses unbuilt or stale constructions. Three registered
  identities without source rows are explicitly `dormant`. Glottolog and
  Concepticon are frozen inputs, never downloaded implicitly; merkmal and all
  dependencies are locked (`requirements.lock`).
- **Rebuild guarantee.** The accepted-inputs snapshot of each release, unpacked
  into a clean checkout, re-derives the release's outputs offline;
  `scripts/verify_rederivation.py` checks this byte for byte. Release
  `A-2026-11-03` (commit `ac575639`): 32,511 of 32,511 derived files identical
  (variety builds, aggregate and the full site) from its 127 MB snapshot
  ([report](evidence/rederivation/A-2026-11-03.json); pre-release proof of
  2026-11-02 [here](evidence/rederivation/pre-release_2026-11-02.json)).
- **Licensing.** Reviewed overrides bind legacy English Wiktionary (CC BY-SA 4.0,
  snapshot identified by checksum, dump date unknown) and `luangthongkumkaren`
  (CC BY 4.0, confirmed by the author; upstream declared ND in error). The 20 largest
  sources were re-audited on 2026-11-02 with no discrepancies
  ([audit](evidence/source-terms/top20_terms_audit_2026-11-02.json)).
  `kogansemitic` and `williamsonbenuecongo` remain undeclared and appear only in
  the `full` tier.
- **Review status.** Recent semantic reviews are model-assisted, not
  independent expert gold; the baseline was built by the maintainer with
  extensive AI assistance.

Earlier states, batch reports and their evidence are in the archived
repository [tresoldi/arcaverborum](https://github.com/tresoldi/arcaverborum).
