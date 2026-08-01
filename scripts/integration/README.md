# Integration utilities

## `capture_snapshot.py`

This optional read-only utility queries the GitHub API and records:

- PRs that appear open at a declared cutoff from PR creation/close timestamps;
- the present head at capture time;
- commit metadata;
- one **heuristic historical head candidate** selected from commit author/committer timestamps;
- post-cutoff commits visible in the PR commit list.

The heuristic candidate is not an exact historical PR head. GitHub's PR commit endpoint does not expose the time at which a head became visible, force-push history may be absent, and author/committer timestamps may differ from push time. Exact historical review heads must come from independently recorded review reports or another authoritative capture.

The workflow artifact is temporary transport with a configured retention period. It is not immutable storage. The checked-in timestamped ledger and exact review reports are the authority.

## `validate_integration.py`

This standard-library checker validates only integration metadata:

- cutoff population and verdict aggregate;
- reviewed SHA syntax;
- known delta markers;
- canonical/alias ID uniqueness;
- JSON and schema parseability;
- stable README and workflow wording.

It performs no mathematical, prime, zero, interval, spectral, or special-function computation.
