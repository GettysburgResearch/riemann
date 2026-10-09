# Upstream snapshot comparison

The core import in PR #908 is frozen at
`openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a`.
This companion's combined source view is frozen at
`openai/math@fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`.
The original core directory and its historical manifest are preserved unchanged.

## Result of the complete tree comparison

Across the entire upstream repository, the two Git trees differ at **1,185
paths**: 1,135 additions, 31 deletions, and 19 modifications. This count comes
from complete Git trees, not a capped web diff.

Within this contribution's **11,940 selected source files**, there are only
**six modified metadata files and one added metadata file**. Every selected
manuscript and all **11,576 selected implementation modules** have the same
Git blob and mode at both upstream commits.

| Logical upstream path | Change in the new view |
| --- | --- |
| `CONTENTS.md` | Updated catalogue |
| `README.md` | Updated repository overview |
| `lean/ComparatorChallenges/README.md` | Updated comparison guidance |
| `lean/formalization.yaml` | Updated formalization catalogue |
| `overview.pdf` | Updated global overview |
| `overview.tex` | Updated global overview source |
| `history.md` | Newly added upstream change history |

The original three family-003 manuscripts and 3,232 core implementation
modules are unchanged upstream. The 22 companion manuscript directories, six
new scope documents, and eight new comparator specifications/mappings are
also unchanged. The selected licenses, toolchain, Lake files and compatibility
patches retain their original bytes and modes.

The upstream history records changes and withdrawals elsewhere in the
catalogue. That history is retained as source context. An unchanged selected
proof is a source-fidelity observation, not evidence that its mathematics has
been independently accepted.

## Storage consequence

The logical selected view contains **99,623,900 bytes**. Of these:

- **3,280 files / 39,507,819 bytes** are reused from the immutable core.
- **8,660 files / 60,116,081 bytes** reside in this companion's supplement.

The six changed metadata files live in the supplement; their old versions stay
in the core. Reuse is permitted only for matching upstream path, Git blob and
mode. The assembler creates a fresh directory from the exact combined manifest,
so stale files cannot remain from an old-tree overlay.

## Reproduce the comparison

After the source-integrity verification in [REPRODUCE.md](REPRODUCE.md), run:

```sh
python checks/audit_upstream_drift.py --source /tmp/openai-math-reference --output /tmp/upstream-drift.json
```

The script reads both hardcoded Git trees, checks every selected manifest entry
against the new tree, computes the complete repository change counts, and
records the old/new blob and mode for each changed selected path. The result
recorded for this contribution is
[checks/artifacts/upstream-drift.json](checks/artifacts/upstream-drift.json).
It does not compare or verify external dependency repositories.
