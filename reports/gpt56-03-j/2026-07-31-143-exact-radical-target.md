# Session report — exact radical targets and auxiliary-factor positive criterion

Agent: `gpt56-03-j`  
Date: 2026-07-31  
Stacked base: draft PR #152  
Branch: `agent/gpt56-03-j/143-exact-radical-target`  
Status: major positive-path reduction; no proof of RH

## Executive result

The newest repository and literature audit exposed two separable issues in the
CCM positive route:

1. a source chosen only to have zero integral need not lie in the exact
   codimension-two domain of the global arithmetic radical map;
2. identifying the repaired source with one specific `Xi` coefficient ratio is
   stronger than necessary.

This branch resolves both at theorem level.

### Source/domain repair

`L-15301` starts from the self-dual CCM Hermite source `h`, smoothly cuts it off,
and repairs its tiny integral error with one fixed even bump whose value at zero
is zero and whose integral is one. The resulting compact source `f_R` satisfies
exactly

```text
f_R(0) = 0
integral f_R = 0
```

and converges to `h` in Schwartz topology. Its Fourier defect also tends to zero
in Schwartz topology.

The global vector `E(f_R)` is therefore an exact Weil-form radical vector. By
Poisson summation, its entire exterior low tail is the reflected arithmetic
image of `hat(f_R)-f_R`. A smooth multiplicative cutoff produces a compact
localized target whose tail tends to zero in the actual Schwartz/form topology,
not merely in ordinary `L2`.

The localized transform converges locally uniformly to `Xi`, after the fixed
normalization audit.

### Weaker endpoint

`T-15301` proves that even convergence specifically to `Xi` is unnecessary. If
finite real-rooted functions converge locally uniformly to

```text
zeta(1/2-iz) * Phi(z)
```

for any holomorphic `Phi` with nonzero product, RH follows by Hurwitz. Auxiliary
zeros cannot cancel zeta zeros because the limit is a product.

This removes the need to prove a delicate fixed-mode prolate defect-ratio
asymptotic solely to recover the exact `h_0/h_4` coefficient ratio.

## Exact finite source repair

`L-15302` gives a three-mode repair. For

```text
v_j = p_j(0)
m_j = integral p_j
```

set

```text
a_0 = v_1 m_2 - v_2 m_1
a_1 = v_2 m_0 - v_0 m_2
a_2 = v_0 m_1 - v_1 m_0.
```

Then the combination `sum a_j p_j` annihilates both source functionals exactly.
For an orthonormal finite-Fourier packet with eigenvalues `chi_j`, the exact
leakage identity is

```text
||Ff-f||^2 = 2 sum_j a_j^2 (1-chi_j).
```

`X-15301` checks this algebra with standard-library rational arithmetic.

Synthetic retained packet:

```text
v                        (1,2,3)
chi                      (9/10,4/5,1/2)
a                        (-9/5,6/5,-1/5)
norm squared             118/25
Fourier defect squared   158/125
normalized defect        79/295
```

Verification SHA-256:

```text
365a4d600bd0e7a0029f53c595c7ec521cf8202ca95aff60cbd8fdb9e2b50b49
```

Six mutation tests cover functional drift, proportional functionals, invalid
eigenvalues, Boolean integer confusion, and missing orthonormality gates.

## Growing block breakthrough

`L-15303` observes that inside a self-dual Fourier-Hermite sector, value at zero
and integral are the same functional. From `H_0,H_4,...,H_(4M)`, the combinations

```text
phi_j = H_0(0) H_(4j) - H_(4j)(0) H_0
```

give `M` independent exact source-domain vectors. Applying `L-15301` to all of
them produces a localized near-radical block of any prescribed finite rank.

A diagonal choice of support gives growing packets whose complete low-block form
and residual matrices tend to zero entrywise. This is the correct input shape
for `L-14308`; the positive route is not intrinsically one-dimensional and does
not need a simple isolated ground direction.

## Latest literature matching

The following primary sources were located and used:

- Connes--Consani, arXiv:2106.01715 / L'Enseignement Mathématique 69 (2023):
  codimension-two source map and prolate arithmetic near-radicals;
- Connes--Consani--Moscovici, arXiv:2511.22755 (2025): finite spectral triples,
  real-zero mechanism, and the stated convergence bottleneck;
- Suzuki, arXiv:2606.09096 (June 2026): continuous screw-function realization
  of the localized Weil form and explicit operator framework;
- Kulikov, arXiv:2603.07407 (March 2026): sharp pre-plunge eigenvalue estimates;
- Kulikov--Dam Larsen, arXiv:2603.23832 (March 2026): sharp localization
  eigenvalue counting estimates;
- Azimifard, arXiv:2607.23016 (July 2026): an independent one-dimensional
  plunge-region bound.

The new localization estimates improve scheduling and packet-size control. They
do not replace the arithmetic complement coercivity or low-subspace comparison.

## Revised remaining theorem

The remaining positive blocker is now sharply stated:

```text
low dangerous prolate/multiband packet
        is asymptotically contained in
exact repaired Hermite-radical packet,
```

in a metric strong enough for the Weil form, with a certified complement floor.

Equivalently, prove a vanishing principal angle or graph distance between the two
packets and compose it with the block Schur floor. If the resulting cofinal lower
bound is `-epsilon(lambda)` with `epsilon(lambda)->0`, `T-14302` proves RH.

## What was not proved

- No principal-angle estimate was obtained.
- No production complement floor was certified.
- No cofinal lower envelope was completed.
- No finite ground-state sequence was proved to approach the repaired target.
- The imported `E`, Poisson, Mellin, and CCM normalization interfaces still need
  independent line-by-line review.
- No proof of RH is claimed.

## Review order

1. `claims/lemmas/L-15301-exact-compact-radical-target.md`
2. `claims/theorems/T-15301-auxiliary-factor-hurwitz-implies-rh.md`
3. `claims/lemmas/L-15303-growing-hermite-radical-packets.md`
4. `claims/lemmas/L-15302-three-mode-codimension-two-repair.md`
5. `experiments/X-15301-codimension-two-source-repair/verify.py`
6. `claims/methodology/M-15301-exact-radical-block-lower-floor-pipeline.md`
7. `claims/observations/O-15301-july-2026-positive-path-literature-audit.md`

## Immediate handoff

Compute exact principal angles between the first repaired Hermite packets and
the low prolate packets at several support levels. The only useful empirical
trend is one that can be upgraded to a symbolic graph/form-norm bound. If that
angle does not shrink, abandon the packet identification rather than polishing
finite spectra.