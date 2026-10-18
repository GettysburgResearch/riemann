# Complete packet validation

The packet contains written component proofs, their exact finite
certificates, and separately authored review reports. All component
acceptance predicates were executed during development. The coordinated
publication procedure additionally runs the following single entry point
against the complete frozen packet before creating its commit:

```bash
python3 verify_packet.py --replay --report /tmp/riemann-theta18-replay.json
```

Use Python 3.12 with its standard library. No numerical optimizer,
network access, third-party Python package or supplied moment oracle is
required. The report path must be outside this packet, since it is an
execution receipt rather than a change to the frozen input.

## Authentication

`python3 verify_packet.py` verifies the complete payload inventory,
byte lengths, SHA-256 values and Git blob identities in `MANIFEST.json`.
It rejects symlinks, duplicated or unsafe manifested paths, missing files
and unmanifested non-cache files. The manifest excludes itself to avoid
self-reference. Python cache directories are not publication payload.
The Git tree authenticates the manifest at publication.

Full replay authenticates the same bytes both before and after execution.
Component-generated outputs are written to temporary directories, and
the mutation runner is staged in a temporary copy. Neither procedure
updates a frozen report in place. A PASS report requires every stage
below to succeed and the packet to remain unchanged.

## Executed stages

| Stage | Acceptance requirement | What it establishes |
| --- | --- | --- |
| All-order checker, normal and optimized | Both runs reproduce the exact stored report and all 908 explicit checks. | Rational supporting certificates, the declared affine identities and complete finite masks, convolution and prefix fixtures. |
| Nine all-order corrupted processes | Every separately launched optimized process fails at its declared gate; the complete report agrees with the frozen report. | The indicated omitted-factor and altered-budget controls are actually rejected with Python assertions disabled. |
| Newton checker, normal and optimized | Both runs reproduce the exact stored report and all 10,364 predicates. | Every declared strict output cell, exact balances, original product weights, complete rational periods, source-tuple inclusion and 27 internal negative-control predicates. |
| Theta contraction, normal and optimized | The actual source is regenerated, the complete certificate is recomputed and compared, and all explicit acceptance predicates pass. | The directed existence certificate for the exact degree-18 root, complete source tails through order 20, positivity and the strict degree-20 gap. |
| Independent full graph, normal and optimized | All raw moments 0 through 20 agree exactly with the authored model; the complete report matches. | A second rational probability-transfer encoding of the 281-spin graph at the center, plus a separate complete 128-state control. |

The full theta certificate has SHA-256
`df51d1773b151b6f89b316faa84416507b90cebb6d068ad6bd4947d1ddaac964`.
The independent graph checker has SHA-256
`9ecfb99250d2c2fad5c5bfc6002d84a2d8755738d32437c3b33bee88166d788c`.
All report and source identities are also present in the complete manifest.

The theta source receipt `theta_tight.json` is retained for the graph
check's center diagnostics. It is not the source of the contraction
checker's target: that checker reconstructs the original density moments,
normalization, all six time tails, the omitted-index tail and Taylor
remainder afresh. Agreement of the center moments with target intervals
does not by itself prove an exact root.

## Mathematical interpretation

The all-order and Newton infinite estimates follow from their written
proofs; finite predicate counts cannot establish them by sampling. The
theta existence theorem combines its analytic source bounds, included
directed arithmetic and a whole-box contraction. Normal and optimized
runs exercise the same implementation and are not independent
transcendental calculations.

The component validation notes give the complete fixtures and precise
limitations: [critical](critical/SOURCES_AND_VALIDATION.md),
[Newton](newton/VALIDATION.md), and [Lee–Yang](lee_yang/VALIDATION.md).
The distinction between mathematical review and replay is set out in
[REVIEW.md](REVIEW.md).

## Remote publication verification

After local replay, the publication procedure checks every created blob
against its locally calculated Git identity, checks the complete packet
tree, and preserves every inherited base entry. After creating the draft
PR, it reads back the branch and commit, verifies the sole parent, root
tree and complete changed-file inventory, and compares remote blob IDs
and byte lengths with the frozen local inventory. The PR records the
exact publication head and completed verification result.

This describes local replay and explicit remote object verification.
It does not claim GitHub Actions execution, external mathematical
acceptance, integration into main, or a proof of RH.
