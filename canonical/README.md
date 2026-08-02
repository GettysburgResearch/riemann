# Stable canonical machine contract

This directory is backstage machine data. It is not the human front door.

The established paths remain authoritative and compatibility-stable:

- `registry.yaml` — the first integration’s 18 reviewed metadata candidates;
- `aliases.yaml` — append-only claim-ID collision, supersession, and historical identity records;
- `provenance.schema.json` — the typed canonical/proof-producing provenance contract.

The files retain their original schemas and bytes from the merged first integration. In particular, the JSON Schema keeps the canonical `$id` at this path.

A registry row does not itself place a proof body on `main` or broaden a review. Readable mathematics lives under [`research/integrated/`](../research/integrated/README.md), and the wider reviewed state is in [`research/RESULTS_INDEX.md`](../research/RESULTS_INDEX.md).
