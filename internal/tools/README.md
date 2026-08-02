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

A standard-library, offline checker for:

- the final root and research layout;
- curated relative links;
- explicit RH-unsolved language;
- absence of temporary task language;
- exact packet source/review/scope headings;
- the results index’s local-versus-source-pinned distinction;
- stable byte-level Git blob identities for the canonical registry, aliases, and schema;
- absence of duplicate internal registry copies;
- syntax and target behavior of the compatibility wrappers;
- absence of the retired integration snapshot workflow.

It performs no zero, prime, interval, spectral, special-function, Robin, or matrix-production computation.

## `archive/validate_integration_20260801.py`

The original first-integration metadata checker is preserved for historical reconstruction. Its old paths describe the merged 2026-08-01 layout and are not the current validator.
