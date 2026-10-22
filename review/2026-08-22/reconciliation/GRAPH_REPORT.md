# Fail-closed graph report

```text
VALIDATION:                       PASS_REVIEWER_D_COMPLETE_RECONCILIATION
CLAIM ROWS:                       139
EDGE ROWS:                        36
ALIASES:                          19
REFUTATIONS:                      19
COMPUTATIONS:                     22
PR LIFECYCLE ROWS:                333
TARGETED REVIEW REQUIRED:         0
UNRESOLVED ACTIVE CONFLICTS:      0
PROVEN-ONLY PATH TO RH:           false
DIRECT-MAIN COMMITS CLASSIFIED:   85
INTEGRATION READINESS:            READY_WITH_EXPLICIT_EXCLUSIONS
```

## Repairs enforced

- all hyperedge premises are JSON arrays;
- every active endpoint is a registered semantic node;
- open producer hypotheses cannot be hidden in metadata;
- refuted, empirical, superseded, gap-blocked, and RH-equivalent nodes are inactive in proved reachability;
- every PR #375–#707 has a lifecycle row;
- #417 is the sole no-object sequence gap and is administrative;
- Reviewer C final and direct-main audit heads are exact frozen inputs;
- the extraction plan covers every final claim exactly once;
- no unresolved conflict or targeted-review row remains.

## Scientific interpretation

The graph contains several exact consumers, reductions, and conjunctive APIs. It contains **no path to RH composed only of reviewed proved premises**. The open cuts listed in `OPEN_CUTS.md` remain conclusion-facing signed/source-faithful estimates, often equivalent to RH in their full quantified form.
