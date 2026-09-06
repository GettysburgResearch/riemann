# Current canonical view: September 6, 2026

This release is an explicit overlay on the immutable August 22 registry: 139 historical claim rows and 36 historical edges. Its controlling inputs are the [release manifest](../../integration/2026-09-06/RELEASE.json), [43 decisions](../../integration/2026-09-06/DECISIONS.json), [eight review claim tables](../../integration/2026-09-06/REVIEW_TABLES.json), eleven programmes, and seven frozen review trees.

The current entry point is [CURRENT.json](../CURRENT.json). It now selects the [authenticated scoped verifier](../../integration/2026-09-06/hardening/verify.py), not the historical payload-only command.

From a complete, clean checkout:

```sh
work="$(mktemp -d)"
python3 -I -S -B integration/2026-09-06/hardening/verify.py --output "$work/normal"
python3 -I -S -B -O integration/2026-09-06/hardening/verify.py --output "$work/optimized"
diff -r "$work/normal" "$work/optimized"
```

The outputs include `claims_current.tsv`, `edges_current.tsv`, `review_dispositions.json`, `validation.json` and `hardening.json`. Claim rows retain previous verdicts and attach current repairs and evidence. Never consume the old table alone as the current verdict table. Review disposition records are not unconditional proof seeds or a count of proved theorems.

The new frontier graph remains navigation with explicit open leaves, not accepted cross-packet adapters. Historical reachability can only be restricted. This hardening pass does not change mathematical verdicts or create an RH path.

The original resolver and its `--payload-only` mode remain preserved for reproduction of PR #800. Their published execution receipt is historical. The new wrapper checks committed versus working bytes before running that pinned resolver, checks its explicit current-page navigation scope, and repeats source authentication afterward.

See [verification scope and actual executions](../../integration/2026-09-06/hardening/README.md) and [release readiness](../../RELEASE_READINESS.md). No mode proves RH, compiles Lean, reruns historical campaigns or provides public-launch clearance.
