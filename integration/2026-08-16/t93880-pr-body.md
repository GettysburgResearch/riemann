## Frozen downstream and review boundary

```text
frozen base PR:   #494
base branch:      research/gpt56-pro/92890-pr489-review-repaired-one-shot
base SHA:         1468ff62c7377f3f6cc1744ef6eafc3df3172d5c
accepted review:  #502
review SHA:       db45b778d8c26e03ef1ad6b6f48959638be28b7c
```

PR #494 is unchanged. This successor does not repackage its accepted one-shot
closing algebra; it independently reconstructs the shared upstream spine.

## Route redesign

The compatible portions of PRs #508 and #509 are used only after an explicit
sector split:

```text
continuum bulk:
  exact native Volterra marginal;
  rank-one Möbius cancellation;
  no Hall/profile theorem;

anchored finite/rough sector:
  complete directed Target-Lorenz AVLT;
  explicit current-only row bonuses;
  separate global frontier-row theorem;

realization:
  identity on anchored finite rows;
  one B-spline martingale quantizer on the bulk;
  one common thinning;
  no exported children and no matrix port.
```

Shared ancestry is not counted as independent confirmation.

## Controlling claims

```text
R-93880  scope correction and route replacement
L-93880  exact native anchored/bulk/defect marginal
L-93881  complete anchored Target-Lorenz/frontier compiler
L-93882  block-diagonal whole-cell positive realization
L-93883  every ordinary and radix-four column, including q<K and terminal
L-93884  direct Y4 deficit <60989<61000
L-93885  unconditional prime-square occupancy moat
L-93886  one-way exact Mellin/Landau exclusion
T-93880  complete composition
```

## Endpoint conclusion

For every integer `X>=10^12`, the packet constructs a finite nonnegative row
`d_X` with

```text
Xi(d_X)(q) <= Omega_X(q) for every q;
C_d(q) <= w_X(q) for every q;
0 <= J_Lambda(X)-H(d_X) < 61000.
```

The packet then independently reconstructs

```text
bounded complete endpoint
-> positive prime-square moat
-> eventual negativity of the prime endpoint
-> Mellin pole audit + Landau
-> RH proposal.
```

## Replay

```bash
python3 experiments/X-93880-upstream-spine/verify.py --mutations --output experiments/X-93880-upstream-spine/results/verification.json
sha256sum -c T93880_CONTENT_SHA256SUMS
```

Retained verdict:

```text
PASS_UPSTREAM_SPINE_RECONSTRUCTION_PACKET
proof object:
ce096c4b6aa8bcfe7c09babd41a06df13aae2644de632b959ed6ecab9d0e3a83
```

This is a candidate-complete unconditional RH proof proposal under project
terminology. RH remains unproved pending hostile independent reconstruction.
