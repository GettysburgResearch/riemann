# Compatibility entrypoints

These established script paths remain executable wrappers:

- `capture_snapshot.py` delegates to the manual offline archival utility at `internal/tools/capture_snapshot.py`.
- `validate_integration.py` delegates to the current front-door validator at `internal/tools/validate_front_door.py`.

Run the validator from a normal Git checkout with no arguments:

```bash
python scripts/integration/validate_integration.py
```

The validator obtains canonical file identities through Git clean-filter semantics (`git hash-object --path`), so the same command works in LF and Windows `core.autocrlf=true` checkouts. A manual canonical-SHA override is only for a deliberate non-Git mirror.

No workflow invokes these entrypoints automatically. The capture utility’s timestamp-reconstructed historical head remains explicitly uncertain.
