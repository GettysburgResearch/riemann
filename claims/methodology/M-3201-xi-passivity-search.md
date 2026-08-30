# M-3201 — Proof-producing passivity search for `xi'/xi`

Claim ID: M-3201  
Title: Reconnaissance, rationalization, and independent checking for positive-real violations  
Status: PROPOSED  
Authoring agent: `gpt56-06`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: D-3201; L-3201; L-3202; contour exclusion through height `3*10^12` from PR #21  
Scope: direct point and finite-matrix RH counterexample search  
Related counterexample candidates: none

## Research objective

Search for either

\[
\operatorname{Re}\frac{\xi'(s)}{\xi(s)}<0,
\qquad \operatorname{Re}s>1/2,
\]

or a finite Pick matrix from L-3202 with a negative exact-vector Rayleigh
quotient. Either rigorously certified event is an unconditional finite
disproof of RH.

## Why this route is operationally different

The direct rectangle route must enclose an entire contour and compute a winding
number. The passivity route evaluates finitely many points and a real sign.
It asks the theorem to infer the hidden right-half-plane zero instead of
isolating it.

The systems-theory transfer also supplies mature proposal mechanisms:
positive-real interpolation, passivity indices, rational transfer-function
fitting, and Hamiltonian/Loewner diagnostics. These mechanisms may rank sample
regions, but only direct ball evaluation of `xi'/xi` enters a proof.

## Layer 1 — reconnaissance

1. Work above height `3*10^12` for discovery; use lower heights only for
   calibration.
2. Parameterize points as

   \[
   s=1/2+2^{-b}r+it,
   \]

   with exact dyadic positive offset and initially floating `t`.
3. Evaluate `F(s)` nonrigorously with a high-throughput Riemann--Siegel or
   approximate-functional-equation backend.
4. Prioritize negative or very small `Re F`, strong local variation, and
   clusters whose Pick matrices have negative midpoint eigenvalues.
5. Fit low-degree rational/Loewner models only to choose the next points. Any
   model pole or passivity violation is a proposal, not evidence.
6. Keep scalar and matrix searches separate in logs. A scalar negative should
   be promoted first because its certificate is smallest.

## Layer 2 — exact rationalization

For a promising sample:

1. replace every coordinate by an exact dyadic value;
2. for a matrix candidate, rationalize one floating eigenvector to a dyadic
   vector `v` using a precision ladder;
3. reevaluate the exact points at increasing precision;
4. retain a candidate only if the direct midpoint margin remains negative
   under coordinate perturbation and increasing precision.

This layer remains non-proof-grade but prevents fragile candidates from
reaching the expensive verifier.

## Layer 3 — Arb producer

FLINT/Arb exposes the required proof primitives:

- `acb_t` complex rectangular balls;
- `acb_dirichlet_zeta_jet` for `zeta` and `zeta'`;
- `acb_dirichlet_zeta_jet_rs` for length-one or length-two Riemann--Siegel jets;
- `acb_digamma`;
- exact `acb_dirichlet_xi` values for cross-checks.

At each point, evaluate the corrected D-3201 formula. Explicitly prove that the
`zeta` ball excludes zero before division. Escalate precision until one of:

- `CERTIFIED_NEGATIVE_SCALAR`;
- `CERTIFIED_NEGATIVE_RAYLEIGH`;
- `CERTIFIED_POSITIVE_SCALAR` for a calibration point;
- `UNRESOLVED`.

For a matrix candidate, evaluate only the fixed dyadic vector's quadratic
form. Do not certify an interval eigenpair.

## Layer 4 — independent checker

The checker should:

1. parse exact dyadic points and vector components;
2. reject points not strictly in `H_{1/2}`;
3. independently evaluate the D-3201 formula with a separately structured
   code path or second ball library;
4. reject every division whose denominator contains zero;
5. reconstruct the scalar or `O(m^2)` Rayleigh interval;
6. accept only an upper endpoint strictly below zero;
7. emit a deterministic digest over inputs, library version, and final balls.

For any decisive witness, require reproduction with another implementation or
library before project-level promotion.

## Adaptive search ideas imported from systems theory

### Positive-real interpolation

Sample data can be tested for consistency with a positive-real interpolant.
Negative Pick directions identify combinations of points with maximal
nonpassivity margin. Use this to adapt the next sample cluster.

### Loewner realization

Loewner matrices construct low-order rational models directly from transfer
samples. A model can cheaply predict poles and bands where passivity may fail.
Because interpolation error is not automatically rigorous, this remains a
reconnaissance layer unless accompanied by a separate uniform residual bound.

### Passivity distance

Control algorithms optimize distance to nonpassivity through structured
Hamiltonian eigenvalue problems. Here the analogous empirical score is the
smallest Pick eigenvalue divided by an enclosure-aware conditioning penalty.
It ranks clusters; it is not a theorem about unsampled points.

## Certificate format sketch

```json
{
  "schema": "riemann.xi-passivity.v1",
  "kind": "scalar" | "pick-rayleigh",
  "points": [{"sigma_dyadic": [num, exp], "t_dyadic": [num, exp]}],
  "vector": [{"real_dyadic": [num, exp], "imag_dyadic": [num, exp]}],
  "precision_bits": 256,
  "xi_or_zeta_balls": [],
  "f_balls": [],
  "rayleigh_interval": ["upper/lower exact export"],
  "status": "CERTIFIED_NEGATIVE_RAYLEIGH",
  "producer_fingerprint": "..."
}
```

The exact ball serialization must use unambiguous binary endpoints or Arb text
round-tripping, not approximate decimal midpoints alone.

## Falsification audit

The route is rejected or downgraded if any of the following occurs:

- Lagarias's corrected theorem does not apply to the chosen `xi`
  normalization;
- the evaluator formula fails `F(1-s)=-F(s)` enclosures;
- a claimed negative disappears under exact point rationalization;
- a denominator ball includes zero;
- the direct checker cannot reproduce the sign;
- a matrix negative exists only after midpoint symmetrization;
- the candidate lies below the already certified critical-line height.

## First implementation milestone

Mirror X-3201 in C or Python bindings to FLINT:

- certify the six low-height calibration points;
- certify the positive synthetic on-line kernel using exact rational zeros in a
  separate toy checker;
- certify the synthetic off-line negative control;
- benchmark scalar and `4x4` Pick evaluation at a modest high point;
- only then begin reconnaissance above `3*10^12`.
