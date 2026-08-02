# Compatibility entrypoints

These established script paths remain executable wrappers:

- `capture_snapshot.py` delegates to the manual offline archival utility at `internal/tools/capture_snapshot.py`.
- `validate_integration.py` delegates to the current front-door validator at `internal/tools/validate_front_door.py`.

No workflow invokes them automatically. The capture utility’s timestamp-reconstructed historical head remains explicitly uncertain.
