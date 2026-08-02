# Machine-registry documentation

The authoritative machine files remain at their established stable paths:

- [`canonical/registry.yaml`](../../canonical/registry.yaml)
- [`canonical/aliases.yaml`](../../canonical/aliases.yaml)
- [`canonical/provenance.schema.json`](../../canonical/provenance.schema.json)

They are deliberately de-emphasized by navigation rather than relocated. This preserves existing parsers, the registry and alias schemas, and the JSON Schema `$id`.

There is no second mutable copy in this directory. Human-readable proof residency is under [`research/integrated/`](../../research/integrated/README.md); the registry remains a metadata and provenance contract.
