# Offline archival and validation tools

No GitHub workflow is attached to these tools.

## `capture_snapshot.py`

An optional read-only archival utility that queries GitHub when run manually with a token. It records current PR metadata and one explicitly uncertain historical-head candidate reconstructed from commit timestamps.

Limitations:

- commit author/committer timestamps are not push times;
- force-push history may be unavailable;
- the reconstructed candidate is not an exact historical PR head;
- exact review heads must come from independently recorded review reports;
- generated output is supporting metadata, not an authoritative mathematical snapshot.

## `validate_front_door.py`

The normal checkout command is:

```bash
python internal/tools/validate_front_door.py
```

The established compatibility command is:

```bash
python scripts/integration/validate_integration.py
```

Both commands take no arguments in a normal Git checkout. The validator is a standard-library, offline checker for:

- the final root and research layout;
- curated relative links;
- explicit RH-unsolved language;
- absence of temporary task language;
- exact packet source/review/scope headings;
- the results index’s local-versus-source-pinned distinction;
- stable committed Git blob identities for the canonical registry, aliases, and schema;
- absence of duplicate internal registry copies;
- syntax and target behavior of the compatibility wrappers;
- absence of the retired integration snapshot workflow.

Canonical identities are computed with `git hash-object --path=...`. This applies the repository’s Git clean and end-of-line conversion rules, so a normal Windows checkout with `core.autocrlf=true` validates the same committed blobs as an LF checkout while substantive working-tree edits still fail. Raw `Path.read_bytes()` hashes are deliberately not used.

The optional `--canonical-sha PATH=GIT_BLOB_SHA` override is reserved for a deliberate non-Git mirror whose identities were independently queried. It is not needed for ordinary validation.

The validator performs no zero, prime, interval, spectral, special-function, Robin, or matrix-production computation.

## `archive/validate_integration_20260801.py`

The original first-integration metadata checker is preserved for historical reconstruction. Its old paths describe the merged 2026-08-01 layout and are not the current validator.
