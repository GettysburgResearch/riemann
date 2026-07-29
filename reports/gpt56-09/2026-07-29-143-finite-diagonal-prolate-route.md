# Positive-direction research pass: finite diagonal prolate–Weil route

Authoring agent: `gpt56-09`  
Date: 2026-07-29  
Issue: #143  
Branch: `agent/gpt56-09/143-finite-diagonal-prolate`  
Status: research program and proved conditional implication; no RH claim

## Executive finding

The repository has developed unusually strong proof engineering for finite
localized-Weil matrices, but nearly all active paths use it to search for a
negative Rayleigh witness or another finite obstruction to RH.  A genuinely
positive use of the same infrastructure is available:

> construct a diagonal sequence of **finite** truncated-Weil ground states,
> prove each one is globally simple and even, and certify that its
> Fourier–Mellin transform approaches the explicit Connes–Consani–Moscovici
> prolate approximant in a Hardy-strip source norm.

The resulting criterion, T-14301, implies RH by a short closure argument:
finite transforms have only real zeros, the weighted norm forces local-uniform
convergence to `Xi`, and Hurwitz prevents a nonreal zero from appearing in the
limit.

The main technical refinement found in this pass is that ordinary `L2`
approximation is the wrong metric.  A crude support estimate pays almost
`lambda^(1/2)` at the edge of the critical strip.  The weighted norm

\[
 \int |f(u)|^2\left(u^{2\tau}+u^{-2\tau}\right)d^*u
\]

controls every smaller strip with a constant independent of `lambda`.  This
turns the positive target from an implausibly strong global support bound into
a localization-sensitive Hardy-space approximation problem.

## Repository map and novelty boundary

The default branch is primarily the collaboration protocol; the mathematical
work is distributed across issue and PR branches.  The active architectures I
found are dominated by:

- finite Weil/carrier witnesses and exact negative Rayleigh searches;
- direct-`xi` moment and Loewner-cone separation;
- `xi'/xi` Pick, passivity, and deflation localizers;
- arithmetic equivalent criteria and explicit-formula witnesses;
- screw-function and finite-metric negative-type searches.

Issue #142, opened concurrently, asks for existential completeness of the
negative localized-Weil search.  The present route is independent: it gives a
positive sufficient criterion and does not rely on a hypothetical negative
witness.

Searches of the repository issues and PRs found no existing prolate-ground
state, Hardy-strip, or finite-diagonal positive program.  The literature does
contain the prolate conjecture itself; the new content here is the following
synthesis:

1. bypass the unresolved infinite fixed-support Weil ground state;
2. use one diagonal sequence of finite matrices instead;
3. replace support-weighted ordinary `L2` by a Hardy-strip source norm;
4. turn simple-even status and target distance into residual, parity-gap,
   weighted-Gram, and projection-tail certificates;
5. state explicitly the asymptotic theorem still required beyond every finite
   prefix.

This report does not claim that the prolate idea itself is new, nor that RH has
been proved.

## Literature synthesis

### Connes–Consani–Moscovici, *Zeta Spectral Triples*

The paper proves a finite theorem: if the smallest eigenvalue of
`QW_lambda^N` is simple and its eigenvector is even, the eigenvector's
Fourier–Mellin transform is entire and has only real zeros (Theorem 5.10).
Proposition 5.7 supplies the nonzero boundary functional needed to normalize
the eigenvector.  The same paper constructs an explicit prolate candidate
`k_lambda`; Lemma 7.3 proves that its transform converges to Riemann's `Xi`
uniformly on closed substrips of `|Im z|<1/2`.

The authors identify two missing steps: prove that the infinite localized Weil
ground state is simple-even and prove that it approaches `k_lambda`.  The
finite diagonal route removes the first infinite limit and combines the two
steps into one finite approximation sequence.

Reference: A. Connes, C. Consani, H. Moscovici, *Zeta Spectral Triples*,
arXiv:2511.22755 (2025), especially Proposition 5.7, Theorem 5.10, Lemma 7.3,
and Section 8.

### Suzuki, *Weil's quadratic form via the screw function*

Suzuki proves lower-bounded/discrete spectral structure for the localized
Weil operator and proves positivity, simplicity, and evenness of the ground
state for sufficiently small support.  This is valuable local evidence, but it
does not supply the large-support regime needed for RH.  It suggests that a
continuation/coercivity theorem in the support parameter may be a productive
analytic attack on Gate 9 of M-14301.

Reference: M. Suzuki, *Weil's quadratic form via the screw function*,
arXiv:2606.09096 (2026), Theorem 1.4.

### Groskin, high-precision finite-Weil computations

The public computations report monotone improvement of the first reconstructed
zero from roughly `2e-55` error at cutoff `c=13` to roughly `1.5e-168` at
`c=67`, and 307–329 matching digits for the first ten zeros at `c=100`,
`N=250`.  More relevant to this project, all 105 pairwise ground-vector
overlaps across cutoffs `13,...,67` are at least `0.9498`, with minimum
`0.94985` at the most separated pair.

These observations motivate a stable target vector, but neither zero accuracy
nor cross-cutoff overlap identifies the explicit prolate function or proves an
asymptotic rate.

Reference: A. Groskin, *High-Precision Approximation of Riemann Zeros via the
Truncated Weil Form*, arXiv:2605.20224 (2026), Sections 8.2–8.3.

### Groskin, finite Guinand–Weil dictionary and tail order

The paper gives an exact finite vector-to-test-function dictionary and a
one-sided archimedean tail budget.  Those are directly reusable for matrix
identity, cutoff-free enclosure, and provenance in Gate 1.  They do not by
themselves control the prolate residual or weighted target distance.

Reference: A. Groskin, *A finite Guinand–Weil dictionary and archimedean tail
order for the truncated Weil quadratic form*, arXiv:2607.02828 (2026).

### Other positive criteria

Recent Beurling/Báez-Duarte reformulations and older de Branges/canonical-system
programs remain important comparison classes.  They typically relocate RH to
a density, positivity, or continuation statement without giving a finite
proof-producing bridge to the repo's current matrix artifacts.  The chosen
route is preferred here because it can reuse the repository's directed matrix,
rational-vector, LDL, perturbation, and provenance machinery immediately.

## New theorem: Hardy-strip finite diagonal criterion

For

\[
 \|f\|_{\lambda,\tau}^2
 =\int_{\lambda^{-1}}^\lambda
 |f(u)|^2(u^{2\tau}+u^{-2\tau})d^*u,
 \qquad 0<\tau<1/2,
\]

T-14301 proves the exact evaluation bound

\[
 \sup_{|\Im z|\leq\sigma}|\widehat f(z)|
 \leq
 \left(\frac{\pi}{4\tau\cos(\pi\sigma/(2\tau))}\right)^{1/2}
 \|f\|_{\lambda,\tau},
 \qquad 0\leq\sigma<\tau,
\]

and the simpler upper bound `(tau-sigma)^(-1/2)`.  The proof uses `u=e^t`,
Cauchy–Schwarz with `2 cosh(2 tau t)`, and the Euler beta integral.  The
constant is independent of the support length.

Consequently, suppose `lambda_j -> infinity`, the finite matrices
`QW_{lambda_j}^{N_j}` have simple-even ground states `xi_j`, and for nonzero
real scalars `c_j`

\[
 \|c_j\xi_j-k_{\lambda_j}\|_{\lambda_j,\tau_j}\leq\eta_j,
 \qquad
 \tau_j\nearrow1/2,
 \qquad
 \eta_j\to0.
\]

Then the finite transforms converge locally uniformly to `Xi` throughout the
open critical strip.  The finite real-zero theorem and Hurwitz imply RH.

This is a genuine implication, not an empirical heuristic.  Its unresolved
premise is isolated cleanly.

## New finite certificate: residual, parity gaps, and projective scaling

L-14301 proves an a posteriori theorem for an interval-enclosed finite matrix.
Given an even candidate `v`, midpoint residual `rho_0`, an even-complement gap,
an odd-sector gap, and operator uncertainty `delta`, define

\[
 R=\rho_0+2\delta,
 \qquad
 g_\pm=g_\pm^0-2\delta.
\]

If both effective gaps are positive, then the exact matrix has a unique global
simple even ground state, with

\[
 \tan\angle(v,\xi_0)\leq R/g_+,
\]

and an explicit ground-eigenvalue interval.  The odd gap is essential: an
even-only eigensolve cannot prove globality.

A second refinement uses the scalar freedom correctly.  If the target
projection is `p=qv` and `xi_0=alpha v+w`, choose `c=q/alpha`; this matches the
entire `v` component.  Thus the projective distance costs `q tan(angle)`, not a
`sqrt(2)` unit-vector alignment bound.

For a weighted Gram form with complement factor `kappa`,

\[
 \inf_c\|c\xi_0-k\|_{\tau}
 \leq
 \text{weighted tail}+q\kappa R/g_+.
\]

This is the exact per-level quantity in the positive program.

## Proof-producing experiment

X-14301 implements the finite kernel with Python integers and
`fractions.Fraction` only.  It verifies:

- exact symmetry and parity of the midpoint/radius data;
- complete even-complement and odd-sector bases;
- exact residual domination;
- exact LDL gap certificates;
- robust `2 delta` losses;
- exact eigenvalue, spectral-gap, tangent, and line-distance bounds;
- an optional exact weighted Gram and complement-factor certificate.

The nontrivial synthetic matrix has residual `1/10`, even gap `1`, odd gap `2`,
and yields

```text
ground eigenvalue in [-1/100,0]
tan angle <= 1/10
global spectral gap >= 1
weighted target-line distance <= 31/100
```

All ten adversarial tests pass.  No numerical eigensolver or actual eigenvalue
is used.

## The actual blocker

The route is not closed.  The exact remaining objective is an asymptotic
estimate for

\[
 d_j^+
 =t_j+q_j\kappa_jR_j/g_j,
\]

where:

- `t_j` is the weighted projection tail of the explicit prolate target;
- `q_j` is its finite projection norm;
- `kappa_j` measures weighted geometry of the even complement;
- `R_j` is the exact residual budget;
- `g_j` is the exact even-complement gap.

One must prove `d_j^+ -> 0` for weights `tau_j -> 1/2`.  A finite table is not
enough.

The most promising analytic attacks are:

1. **Prolate coercivity transfer:** compare the Weil complement form with the
   prolate-wave Hamiltonian and inherit its simple-even gap.
2. **Residual identity:** apply the explicit formula directly to
   `(QW-mu)k_lambda` and exploit cancellation rather than entrywise norms.
3. **Resolvent-weighted localization:** bound the actual map from the residual
   direction to the weighted error, replacing worst-case `kappa`.
4. **Hardy-space uniqueness:** combine a uniform weighted energy bound with
   convergence on a uniqueness set, reducing full target convergence to
   finitely many moments or interpolation values per level.

## Recommended immediate computation

Build a discovery-grade adapter for public cutoffs `c=13,...,67` and record,
for several `N` and `tau` values:

```text
weighted tail t,
residual R,
even gap g_even,
odd gap g_odd,
weighted complement factor kappa,
combined budget d_plus.
```

The first goal is not to extrapolate RH.  It is to identify which factor
actually obstructs decay and to test the four analytic attacks above.  Any
candidate law must then be replaced by a proof.

## Claim boundary

- T-14301: proposed theorem; the implication is proved in the file, subject to
  independent review and exact normalization of imported CCM results.
- L-14301: proposed finite lemma; proof and exact checker supplied.
- X-14301: synthetic empirical verification only.
- M-14301: methodology and attack plan.
- No production prolate level is certified.
- No asymptotic closure is proved.
- RH is not claimed resolved.
