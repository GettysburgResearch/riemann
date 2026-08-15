# PR #497 independent-review handoff

## Frozen graph

```text
proposal PR:      #497
proposal head:    bd2a3c32ab50d8a8cec39c4b51ccd63349b23a74
proposal base:    9e2ae6d26a7920055e1f11327dc0ddeb7b855c61
review branch:    review/pr497-target-lorenz-frozen-bd2a3c32-20260815
```

## Verdict

```text
L-93600 Euler-ramp theorem                    VERIFIED
L-93601 tail event reduction                  VERIFIED WITH FIXES
L-93601 retained numerical proof              NOT EXACT-CERTIFIED
L-93602 compact/tail join                     VERIFIED CONDITIONAL
L-93603 common-parent producer                UNPROVEN / GAP
L-93604 q<K and all-column theorem            VERIFIED CONDITIONAL
L-93605 direct native cost                    VERIFIED CONDITIONAL
T-93600/T-93601                               UNPROVEN / CONDITIONAL
Riemann Hypothesis                            UNPROVEN
```

## Two first boundaries

```text
first proof-object break:
L-93601.4 / X-93600 uses undirected long-double arithmetic.

first structural break even granting the tail:
L-93603.2 does not instantiate the endpoint fibre, initial source
coefficients, actual leaf weights, or the full typed leaf packet.
```

## Surviving chain

Once a genuine common parent is supplied, `L-91733` does cover every physical column, including `2<=q<K`; the thinning identity and terminal margin give native feasibility, and the direct `Y4` charge is below `60989`.

## Review files

```text
reports/integration-wave/20260815-pr497-target-lorenz-frozen-head-review.md
audits/integration-wave/20260815-pr497-claim-status.tsv
audits/integration-wave/20260815-pr497-certificate-audit.md
integration/2026-08-15/pr497-target-lorenz-review-handoff.md
```

## Repair order

1. directed tail certificate;
2. exact endpoint-fibre-to-tree identity;
3. authenticated actual leaf weights;
4. full typed Target-Lorenz leaf packet;
5. actual common-parent replay;
6. existing all-column and endpoint composition.

PR #495 is independent and is not confirmation; its Volterra packet has its own failed causal interface.
