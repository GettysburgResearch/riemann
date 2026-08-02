# Historical machine registry

This directory contains the machine-oriented registry created by the first major integration pass.

- `registry.yaml` indexes reviewed packet candidates.
- `aliases.yaml` preserves claim-ID collisions, supersessions, and historical identities.
- `provenance.schema.json` is an optional typed contract for canonical or proof-producing objects.

These files are backstage. The original registry was explicitly metadata-only and did not copy proof bodies. Current proof residency is under [`research/integrated/`](../../research/integrated/README.md).

The registry is retained for provenance and collision work. Its `promotion: metadata_only` fields describe the first integration snapshot and should not be mistaken for the current human-readable packet layer. Exploration does not need to use the schema.
