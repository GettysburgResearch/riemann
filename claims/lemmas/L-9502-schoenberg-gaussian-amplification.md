# L-9502 — Schoenberg-Gaussian amplification of screw defects

Claim ID: L-9502  
Title: Gaussian PSD witnesses and an explicit negative-type-to-Gaussian transfer moat  
Status: PROPOSED  
Authoring agent: `gpt56-08`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: L-9501  
Scope: nonlinear finite witnesses over the zeta screw-distance table  
Related counterexample candidates: none yet

## Statement

Assume RH.  Let `t_1,...,t_m` be real and let

\[
 D_{ij}=\Psi(t_i-t_j).
\]

Then for every real `lambda>0`, the Schoenberg-Gaussian matrix

\[
 K^{(\lambda)}_{ij}=\exp(-\lambda D_{ij})
\tag{L-9502.1}
\]

is positive semidefinite.

Consequently, exact nodes, an exact positive `lambda`, and an exact vector
`a` satisfying

\[
 a^*K^{(\lambda)}a<0
\tag{L-9502.2}
\]

form a finite RH-disproof witness, subject to directed evaluation and the
normalization audit of `D-9501`.

There is also an explicit transfer from a conditional-negative-type defect.
For any finite real symmetric matrix `D`, suppose an exact real vector `c`
satisfies

\[
 \sum_i c_i=0,
 \qquad
 \delta:=c^TDc>0.
\]

Put

\[
 M=\max_{i,j}|D_{ij}|,
 \qquad
 L=\sum_i|c_i|.
\]

Then every positive `lambda` satisfying

\[
 \lambda M\le1,
 \qquad
 \lambda<\frac{2\delta}{eM^2L^2}
\tag{L-9502.3}
\]

obeys

\[
 c^T\exp[-\lambda D]c<0,
\tag{L-9502.4}
\]

where the exponential is entrywise.  Thus a positive moat in the constrained
quadratic form can always be converted, with an explicit scale, into an
ordinary negative eigenvalue of a normalized kernel with diagonal one.

## Proof of Gaussian positivity under RH

By `L-9501`, for the given finite node set there are vectors `v_i` in a real
Hilbert space such that

\[
 D_{ij}=\|v_i-v_j\|^2.
\]

Therefore

\[
\begin{aligned}
 K^{(\lambda)}_{ij}
 &=e^{-\lambda\|v_i\|^2}
   e^{-\lambda\|v_j\|^2}
   e^{2\lambda\langle v_i,v_j\rangle}.
\end{aligned}
\tag{L-9502.5}
\]

Let `G=(<v_i,v_j>)`, which is positive semidefinite.  The matrix

\[
 H_{ij}=e^{2\lambda G_{ij}}
       =\sum_{r=0}^{\infty}\frac{(2\lambda)^r}{r!}G_{ij}^r
\]

is positive semidefinite: every Hadamard power `G^{circ r}` is positive
semidefinite by the Schur product theorem, every coefficient is nonnegative,
and the finite matrix series converges entrywise and hence in norm.  Equation
(L-9502.5) expresses `K` as a positive diagonal congruence of `H`, so `K` is
positive semidefinite.

## Proof of the explicit transfer moat

For every real `x`, Taylor's theorem gives

\[
 |e^{-x}-1+x|\le\frac{x^2}{2}e^{|x|}.
\tag{L-9502.6}
\]

Because `sum_i c_i=0`,

\[
 c^T\mathbf 1\mathbf 1^Tc=0.
\]

Applying (L-9502.6) entrywise with `x=lambda D_ij` yields

\[
 c^T\exp[-\lambda D]c=-\lambda\delta+R
\]

with

\[
\begin{aligned}
 |R|
 &\le\frac{\lambda^2}{2}e^{\lambda M}
       \sum_{i,j}|c_ic_j|D_{ij}^2\\
 &\le\frac{\lambda^2}{2}e^{\lambda M}M^2L^2.
\end{aligned}
\]

Under (L-9502.3), `e^{lambda M}<=e` and the last upper bound is strictly
smaller than `lambda delta`.  Hence the quadratic form is strictly negative.
QED.

## Motivation

Conditional negative type is tested only on the codimension-one zero-sum
subspace.  Gaussianization removes that constraint and produces a familiar
correlation matrix with exact diagonal `1`.  The free scale `lambda` can be
optimized for numerical separation, while (L-9502.3) prevents that optimization
from becoming an unproved heuristic.

This family is nonlinear in the primitive `Psi` values.  It therefore probes
a different finite cone from linear portfolios of existing `xi'/xi` rows,
even though its validity ultimately comes from the same RH geometry.

## Certificate form

A minimal proof object contains

```text
nodes: exact dyadics or symbolic log(q)
lambda: positive rational or dyadic
vector: exact rational or dyadic entries
psi_intervals[i,j]: directed intervals for Psi(t_i-t_j)
exp_intervals[i,j]: outward-rounded exponentials
rayleigh_interval: directed enclosure of a^* K a
```

The certificate succeeds only when the upper endpoint of `rayleigh_interval`
is strictly negative.  The checker must recompute, not trust, every matrix
entry from the shared `Psi` intervals.

## Analytic domain audit

The proof uses only real exponentials of finite real values.  Under RH,
`D_ij` is a squared Hilbert distance and is nonnegative, but a proof checker
must not assume that sign when evaluating a candidate intended to refute RH.
No complex branch is present.

## Dependency audit

- `L-9501` supplies the finite Hilbert embedding under RH.
- The Schur product theorem and finite Gram factorization are elementary
  matrix facts.
- The transfer moat uses only the scalar exponential remainder bound
  (L-9502.6).

## Gap audit

- The exponential in (L-9502.1) is entrywise, not a matrix exponential.
- A negative eigenvalue caused by asymmetric rounding is invalid; symmetrize
  only after proving that both directed copies enclose the same exact entry.
- Very small `lambda` forces the kernel close to the rank-one all-ones matrix
  and can create severe floating-point cancellation.  Use the explicit moat
  and exact Rayleigh contraction.
- Very large `lambda` can underflow in reconnaissance code; a proof backend
  must evaluate directed exponentials without silent underflow.
- The implication is one-way in this claim.  No assertion is made that one
  fixed `lambda` detects every possible RH failure.

## Adversarial tests

1. At `lambda=0`, the limiting kernel is the all-ones PSD matrix.
2. For two nodes, verify the Gaussian determinant
   `1-exp(-2 lambda Psi(t_1-t_2))>=0` whenever `Psi>=0`.
3. Apply the transfer bound to a synthetic two-point matrix with a known
   conditional-negative-type violation and compare the predicted scale with
   direct exact arithmetic.
4. Replay a candidate at `lambda/2` and `2lambda`; a genuine strict interval
   should behave continuously, not appear at a single rounding-sensitive
   scale.

## Remaining uncertainty

No negative Gaussian candidate is claimed.  The practical value of scale
optimization versus the simpler `L-9501` determinant remains empirical.

## Suggested next attack

Use small exact vectors found from the most negative eigenmodes of binary64
Gaussian scans, then jointly optimize `lambda` and the node offsets inside
prime-knot cells.  Freeze all three before directed replay; do not optimize on
interval endpoints.
