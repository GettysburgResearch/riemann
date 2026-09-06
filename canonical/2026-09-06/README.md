# Current canonical view: September 6, 2026

This release uses an explicit overlay rather than silently rewriting the historical tables.

Input: the immutable 139-claim/36-edge August 22 registry. Control: [RELEASE.json](../../integration/2026-09-06/RELEASE.json), the 43 source-qualified [decisions](../../integration/2026-09-06/DECISIONS.json), eight [review claim tables](../../integration/2026-09-06/REVIEW_TABLES.json), eleven programmes, and exact frozen review trees. The full review tables retain their own component verdicts and omissions; they are not treated as unconditional proof seeds.

From a complete checkout:

```sh
python3 -I -S integration/2026-09-06/validate.py --output /tmp/riemann-current
python3 -I -S -O integration/2026-09-06/validate.py --output /tmp/riemann-current-optimized
diff -r /tmp/riemann-current /tmp/riemann-current-optimized
```

The outputs include `claims_current.tsv`, `edges_current.tsv`, `review_dispositions.json` and `validation.json`. Current claim rows preserve the previous verdict and attach matching repairs/evidence; broken original uses are blocked. Never consume the old historical table alone as the current verdict table.

The new frontier graph is a navigation record with explicit open leaves, not silently accepted cross-packet adapters. Its edges are nontraversable. Historical graph reachability is only restricted; no new reviewed-only RH path can appear by this update.

`--payload-only` is a separate limited check and emits `PASS_RELEASE_PAYLOAD_NOT_FULL_CHECKOUT`. It does not authenticate the actual checkout or resolve its full registry. See the [execution boundary](../../integration/2026-09-06/VALIDATION.md). No mode proves RH, runs Lean or executes the historical large campaigns.
