# M-29201 — Positive parity-cycle Mersenne lift review protocol

Status: **FAIL-CLOSED PRODUCTION AND ADVERSARIAL REVIEW PROTOCOL**  
Target: `T-29201`  
Date: 2026-08-08

## Frozen dependencies

Review the following scopes, not mutable prose summaries:

```text
PR #285  eta source, carry image, Mersenne localization;
PR #272  split divergence, Pascal cycles, dyadic commutator;
PR #291  cofinal shell one-crossing (context only, not imported);
PR #254  monotone-cover refutation;
PR #274  prime-density-drift refutation;
PR #280  central residual and two-pass theorem;
research/gpt56-sol/280-mellin-commutator-closure
         fixed Abel and compact-boundary counterexamples.
```

## Review order

1. `L-29201`: prove `chi_(n,n)=1` and reconstruct the logarithmic collar bound.
2. `L-29202` Sections 1--3: check all floor identities by hand.
3. Reconstruct the odd-multiple Möbius inversion.
4. Derive the shared-capacity support function in (L-29202.14).
5. Verify binary-window preservation for every ordinary lower edge.
6. Reconstruct the complete upper MCF edge set and the linear map to all even carry columns.
7. Verify every claimed generator of the zero-even-column kernel against all even columns.
8. Express each generator in the PR #272 Pascal/fundamental-cycle basis; reject opaque nullspace vectors.
9. Isolate every lower Mersenne edge and the top endpoint before testing any induction.
10. Review a proposed primal or dual certificate for the combined sibling-plus-cycle polytope.
11. Review the positive Mersenne boundary reconstruction.
12. Replay every upper carry column independently from the emitted final flow.
13. Only then invoke `T-28001`'s Mellin--Landau consumer.

## Mandatory production object

For every retained endpoint, emit:

```text
lower complete flow;
upper support menu;
baseline upper flow;
all ordinary sibling masses x_e,y_e;
all shared capacity slacks;
odd target h_X and decoded charge z_X;
complete zero-even correction c_X;
Pascal/fundamental-cycle coordinates of c_X;
replay that c_X annihilates every even column;
replay that sibling plus cycle correction realizes z_X;
final nonnegative upper split coefficients;
Mersenne boundary source and reconstruction;
bottom and top endpoint rows;
full carry-column replay;
parent masses on all Mersenne rows;
eta-source pairing.
```

## Automatic rejection

Reject upon any:

```text
negative final split coefficient;
missing ordered orientation;
even column changed by the final correction;
odd divisor incidence replaced by a norm;
separate capacities x_e<=c and y_e<=c used instead of x_e+y_e<=c;
sibling-only feasibility silently assumed;
zero-even nullspace vector not decomposed into declared cycles;
forbidden lift of a lower Mersenne extreme edge;
unavailable parent 2Y+1 used at the endpoint;
undeclared Pascal cycle;
collar mass estimated without first proving exact feasibility;
finite LP feasibility promoted to the recursive theorem;
lost 2/3 Mertens or same-sign Mobius-cube mutation.
```

## Acceptance boundary

The collar and local sibling algebra can be accepted independently. `PPMFL` is
accepted only after one source-complete recursive certificate or a proof of all
combined sibling/cycle cut inequalities. Until then RH remains unproved.
