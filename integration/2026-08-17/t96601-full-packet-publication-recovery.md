# T-96601 full-packet publication recovery

This additive publication repair restores the claim-level decomposition,
verifier, retained result, test, report, checksum ledger, standalone front
doors, and handoff that were present in the author's deterministic packet but
absent from the first remote publication of PR #556.

No mathematical text already present on the PR branch was overwritten. The
remote branch had four condensed or publication-finalized files whose content
differs from the corresponding packet files:

```text
claims/theorems/T-96601-source-complete-annular-rh-candidate.md
experiments/X-96600-annular-factor67/README.md
integration/2026-08-17/t96601-annular-factor67-lock.json
standalone/2026-08-17-annular-factor67/PROOF.md
```

Those live versions remain the PR front doors. The exact packet variants and
the author's original content ledger are retained under
`integration/2026-08-17/t96601-original-author-variants/`. The root
`T96601_CONTENT_SHA256SUMS` was updated only to authenticate the actual live
root files after recovery.

Provenance:

```text
frozen base PR:       #547
frozen base commit:   d60f93b0e207a83a283fb229eb988aa4c404765d
packet ZIP bytes:     43241
packet ZIP SHA-256:   cc1d7c7d4594f6e923811521fce4a636b35b20f6b2fa13fa9885a5bf72805477
replay verdict:       PASS_SOURCE_COMPLETE_ANNULAR_FACTOR67_CANDIDATE
proof-object SHA-256: ee02d2c5bbefda69f658f4f1475e2be1c1a85db9354fde5cf93a69d0c6526b58
scientific status:    candidate complete; hostile reconstruction required
RH established:       false
```

The recovery changes publication completeness and provenance only. It does not
strengthen, weaken, or otherwise edit any mathematical claim.
