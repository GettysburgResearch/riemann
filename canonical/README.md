# Canonical integration layer

This directory indexes reviewed objects without copying or rewriting the whole research tree.

The canonical layer is deliberately small. A registry entry binds a source PR, exact commit, source paths, scope, review, dependencies, and provenance. The underlying proof or artifact normally remains in its original location.

Files:

- `registry.yaml` — initial reviewed packet candidates selected by the first integration pass;
- `aliases.yaml` — append-only collision, rename, repair, and supersession records;
- `provenance.schema.json` — typed contract for future canonical and proof-producing objects.

A registry entry does not broaden a review verdict. Entries with `promotion: metadata_only` have been indexed for integration but their source theorem files have not yet been extracted or merged.

Exploratory work does not need to satisfy the full schema. The contract applies when an object seeks canonical or proof-producing status.
