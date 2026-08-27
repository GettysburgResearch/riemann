# M-105320 — Hostile review contract for compression and the moving Xi saddle

Claim ID: `M-105320`  
Status: **REVIEW PROTOCOL**  
Created: 2026-08-23  
RH status: **unproved**

Review in the following order.

1. `L-105320`, Sections 1–3: root compression, Schur formula, residue weights.
2. `X-105320`: exact rational replay and its explicit exclusions.
3. `L-105320`, Sections 4–5: uniform versus physical compression and the
   spectral perturbation constant.
4. `L-105321`: moving complex saddle and shifted-contour dominance.
5. `L-105322`: phase cells, real-rootedness, residue calculation and
   height/order inversion.
6. `R-105320`: every scope firewall.
7. `T-105320`: composition and remaining cut.

## Mandatory finite-algebra checks

Reject `L-105320` unless all of the following are verified:

- the compression acts on `e^perp`, with the normalized vector
  `e=n^(-1/2)(1,...,1)`;
- `det(zI-C)=p'(z)/n` is monic on both sides;
- the Schur complement has the factor `1/n` exactly;
- the residue sign is `b^*E_jb=-n rho_j`;
- the quotient-algebra operator is transported by functional calculus, not by
  an unproved basis identification;
- the compression vector producing `p''` has equal **squared** spectral
  weights; eigenvector signs may be chosen only because the compressed
  characteristic polynomial is sign-independent;
- the Weyl bound compares operators on one common pulled-back subspace.

The replay checks the first three bullets on exact rational fixtures. It does
not authenticate the angle or Weyl argument.

## Mandatory moving-saddle checks

Reject `L-105321` unless the proof provides:

- a fixed zero-free complex neighbourhood of the real saddle, derived from
  first-summand domination of the explicit Xi kernel;
- a unique analytic moving saddle uniformly for every `m>=M`;
- an allowed contour deformation for complex `z`, including the connector at
  zero and the connector at infinity;
- a global comparison showing that every shifted-contour complement is small
  **relative to the moving saddle contribution**, whose modulus may be
  `exp(-c kappa_m)`;
- one fixed analytic square-root branch for the curvature prefactor;
- derivative control on a strictly larger buffered box;
- no replacement of the exact phase by a finite cumulant truncation at the
  `m/log m` scale.

The smallest analytic failure is a competing shifted saddle or a tail with
larger real action.

## Mandatory Rouché and residue checks

Reject `L-105322` upon any of the following:

- model cells defined by the linear phase `w_mx` rather than the exact phase;
- an `O(1)` linear-lattice count error at height `m/log m`;
- failure to prove `Re Theta_m'>0` on the complete buffered complex box;
- reality inferred without conjugation plus a one-zero multiplicity count;
- critical residues computed from three unrelated normalizations instead of
  the identity `Xi^(m+2)=(Xi^(m))''` or an equally explicit normalization;
- use of the outer box for critical-point sums without an inner buffer.

## Mandatory logical boundary

The review must preserve all three separate assertions:

```text
finite compression theorem                         proposed exact;
near-linear high-derivative Xi entry                proposed analytic;
low-order coherence and boundary budget             open.
```

No high-order result may be described as fixed-order control. No finite replay
may be described as authenticating the Xi contour theorem. `CRDB105200` and RH
remain unproved.
