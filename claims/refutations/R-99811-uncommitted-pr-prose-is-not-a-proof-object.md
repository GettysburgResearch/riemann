# R-99811 — Uncommitted pull-request prose is not a mathematical proof object

Claim ID: `R-99811`  
Status: **PUBLICATION/PROVENANCE FIREWALL**  
Created: 2026-08-20

At the frozen PR #656 head

```text
db404ec00cf022f003ee2bbee66e0cf62ac45003
```

the remote changed-file list contains only the five T99700 owner-degeneracy and
cross-core files.  The subsequently edited PR body advertises T99710/T99711,
two new replay commands, a Cauchy–Poisson gap, a compact kernel, and a growing
moment tower, but none of those named files or replay paths is present at the
frozen head.

Accordingly those statements are research prose, not committed theorem or
replay objects, and are excluded from the T99810 proof graph.  They may be
reconsidered after a successor branch deposits the exact files, source lock,
checker, retained result, and checksum ledger.

## Subsequent status

PR #659 at `83c17b32a99ac9e1aa5aec3168535550eb286636` subsequently
deposited a source-locked GPMOC successor with its own checker and ledger.
The historical finding above remains true at the frozen PR #656 head, while
the committed PR #659 route is now a separate open input—not excluded prose
and not a proved replacement for the open Abelian-to-Carleson localization.

This rule is general:

```text
PR title/body/comment != committed proof object;
scientific identity = branch + exact head + file path + replay + digest.
```

The firewall prevents an attractive but unpublished mechanism from being used
to bridge the remaining RH-equivalent cross-core theorem.
