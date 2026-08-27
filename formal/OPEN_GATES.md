# formal-v0.1 open gates

The Riemann Hypothesis remains unproved. This file separates missing library
infrastructure from genuinely open mathematics and from results deliberately
outside the release cutoff.

## Analytic library gates

### Tail-Mellin Landau boundary singularity

The exact nonnegative, locally integrable tail-transform theorem required by
the reviewed Mellin consumer is represented by the proposition
`MellinLandauBoundarySingularity`. It is not currently discharged by the
pinned Mathlib or Zeta23 libraries.

The desired theorem concerns the actual transform on `[1,∞)`, including local
integrability, initial convergence, finite abscissa, eventual nonnegativity,
nonzero density and continuation through the positive real boundary point.
Similar Zeta23 files named `Landau` prove different zero-count and explicit-
formula estimates.

### Subpower negative-mass holomorphy

`SubpowerNegativeMassHolomorphy` states the exact result converting subpower
logarithmic negative mass into holomorphy of the negative-part tail transform
in the open right half-plane. It remains an explicit theorem parameter.

### Reciprocal order and zero-localization adapters

Several shifted reciprocal-zeta order and admissible-zero-strip inputs remain
explicit in the top-level conditional consumer. They should be discharged by
precise adapters to the pinned analytic-order infrastructure rather than by
new axioms.

## Arithmetic RH-bearing gates

The principal unresolved producer targets are:

- both literal native fixed rows 2 and 3 with the required signed or
  holomorphic-defect control;
- one fixed `5:3` detector with subpower logarithmic negative mass;
- a fixed native detector negative-mass estimate sufficient for the formal
  consumer;
- the complete labelled sequential first-owner theorem;
- the full source/provenance ledger preventing every reviewed promotion;
- the actual ratio-eight `√2` wavelet with factor-67 antisymmetric copy and
  endpoint conventions;
- the complete compact Abel–Mertens frame and quantitative same-`K1`
  translation;
- the exact half-divisor `b_U/h_U` fields, ratio-four kernel, Hardy bound,
  endpoint localization and signed near-collision theorem.

The finite algebra presently formalized does not prove any of these estimates.

## Xi and operator gates

The actual-Xi order-three theorem remains conditional on external and analytic
inputs. A future unconditional formal proof must formalize or certificate-wrap:

- the exact published verified-height result and its artifact/source lock;
- the grouped actual-Xi zero expansion with local `C²` convergence;
- multiplicity and reflected-orbit bookkeeping;
- the reciprocal-square tail inequality and numerical reserve budget;
- the source-faithful paid-prefix limit.

Order four remains open and is not stated as a proved theorem. The release
makes no all-order Pick, Loewner, heat, Q4 or Fredholm positivity claim.

## Canonical corpus still awaiting exact statements or proofs

The release registry represents all 139 canonical semantic IDs, but most are
not yet exact Lean propositions. Wave two must distinguish:

```text
UNSTATED
STATED
PROVED
PROVED_CONDITIONAL
UPSTREAM_PROVED
BLOCKED_LIBRARY
BLOCKED_MATHEMATICS
REFUTED_FORMALIZED
SUPERSEDED
```

without asserting an open proposition as true.

Major still-unformalized reviewed families include SHARP `m≥2`, critical
variation, the full minimal-wavelet spectral-abscissa theorem,
Dickman–Stieltjes, hereditary Bellman, XD/HCNC/BPOE, First-Hermite and heat,
Q4, Brownian/Weil/Fredholm, carry and endpoint packets, and retained finite
certificates.

## Deliberate release exclusions

- every research result after PR #707;
- PRs #756 and #757 and the later beta/family/sheaf programmes;
- historical heavy computations and external numerical campaigns;
- claims that were only proposed, empirical, superseded or refuted;
- any unconditional theorem concluding RH;
- any unconditional actual-Xi order-three theorem.

Post-cutoff work may be prepared experimentally, but it must receive its own
scientific review and integration before entering the canonical trusted
formalization track.
