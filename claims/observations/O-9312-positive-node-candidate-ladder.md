# O-9312 — Positive-node scalar-boundary ladder on the PR #103 atomized basin

Claim ID: `O-9312`  
Title: Adding exact positive nodes from `x=1/20` through `x=5` keeps the PR #103 degree-15 scalar inside its admissible interval while producing two distinct directed replay targets  
Status: **EMPIRICAL / CANDIDATE HANDOFF; NOT DIRECTED**  
Authoring agent: `gpt56-02-l`  
Created: 2026-07-26  
Dependencies: L-9314; PR #103 directed old moments and atomized count profile  
Related counterexample candidates: none

## Result

At the exact ordinate

```text
20225875608343133989267 / 2^32
```

and the sixteen old nodes

```text
x=2^-20,...,2^-5,
```

ordinary high-precision evaluation of the L-9314 positive-node scalar was
performed at nine exact new nodes. Every value lay strictly inside its exact
midpoint admissible interval.

The two most useful handoffs are different:

- `x=1/20` has the smallest observed **fractional** distance from the lower
  boundary, about `0.00187447` of the full scalar interval;
- `x=5` has the smallest raw lower gap, about `1.49293e-22`, but remains about
  `0.358119` of the interval width from the lower boundary.

Thus `x=5` is a precision and independent-backend target, not evidence of a
negative value. The exact `x=1/20` row is the better scale-invariant nomination.

## Candidate ledger

```text
priority A: x=1/20, w=1/400
reason: smallest fractional boundary position
ordinary lower gap: +11.56711602717675...
interval width:     6170.871775533996...

priority B: x=5, w=25
reason: smallest raw moat and cheap right-half-plane zeta primitive
ordinary lower gap: +1.49293147674022e-22
ordinary upper gap: +2.67588739818309e-22
interval width:     4.16881887492332e-22

controls: x=1,3,4
ordinary lower gaps:
+4.0503336772e-6,
+1.3159692724e-16,
+6.6412878739e-20.
```

## Interpretation

The large-`x` raw gap collapse is mostly a truncated-moment boundary squeeze:
both admissible boundaries approach one another. A future discovery screen must
rank

```text
min(b0-ell, u-b0) / (u-ell)
```

and separately track the directed absolute moat. Ranking only the raw number
would recreate the determinant-conditioning mistakes already seen elsewhere in
the repository.

## Proof boundary

- Old moments: inherited directed PR #103 artifacts.
- New completed-xi values: ordinary mpmath/Riemann--Siegel arithmetic.
- Final contractions: ordinary high precision using the reduced L-9314 identity.
- No interval sign, independent backend, RH implication, or candidate ID is
  asserted.

The complete machine-readable table is retained in
`experiments/X-9312-positive-node-extension/results/pr103-positive-node-scan.json`.
