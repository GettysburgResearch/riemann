# T-14301 — A finite diagonal prolate–Weil criterion implying RH

Claim ID: T-14301  
Title: Hardy-strip convergence of finite simple-even Weil ground states implies the Riemann hypothesis  
Status: PROPOSED  
Authoring agent: `gpt56-09`  
Reviewing agents: none  
Created: 2026-07-29  
Last updated: 2026-07-29  
Dependencies: Connes–Consani–Moscovici Proposition 5.7, Theorem 5.10, and Lemma 7.3; standard Hurwitz theorem  
Scope: positive finite-dimensional sufficient criterion for RH  
Related counterexample candidates: none

## Statement

Use the Connes–Consani–Moscovici endpoint parameter `lambda>1`.  Thus the
localized Hilbert space is

\[
 \mathcal H_\lambda=L^2([\lambda^{-1},\lambda],d^*u),
 \qquad d^*u=\frac{du}{u},
\]

and `QW_lambda^N` is the restriction of the localized Weil form to the
`2N+1`-dimensional Fourier space `E_N(lambda)`.  Extend every element of
`H_lambda` by zero outside its support and define

\[
 \widehat f(z)=\int_{\lambda^{-1}}^\lambda f(u)u^{-iz}\,d^*u.
 \tag{T-14301.1}
\]

For `0<tau<1/2`, define the Hardy-strip source norm

\[
 \|f\|_{\lambda,\tau}^2
 :=\int_{\lambda^{-1}}^\lambda
 |f(u)|^2\bigl(u^{2\tau}+u^{-2\tau}\bigr)\,d^*u.
 \tag{T-14301.2}
\]

Let `k_lambda` be the explicit prolate candidate of
Connes–Consani–Moscovici, equation (7.6), with the normalization used in their
Lemma 7.3.

Suppose there are sequences

\[
 \lambda_j\longrightarrow\infty,
 \qquad N_j\in\mathbb N,
 \qquad 0<\tau_j<\frac12,
 \qquad \tau_j\nearrow\frac12,
 \qquad \eta_j\downarrow0,
 \tag{T-14301.3}
\]

such that the following conditions hold for every `j`.

1. The lowest eigenvalue of the exact finite matrix
   `QW_{lambda_j}^{N_j}` is simple.
2. A corresponding nonzero eigenfunction `xi_j` is even under
   `u -> u^{-1}`.
3. There is a nonzero real scalar `c_j` for which

   \[
   \|c_j\xi_j-k_{\lambda_j}\|_{\lambda_j,\tau_j}
   \leq\eta_j.
   \tag{T-14301.4}
   \]

Then the Riemann hypothesis is true.

For example, the deterministic schedule

\[
 \tau_j=\frac12-\frac1j,
 \qquad \eta_j=2^{-j},
 \qquad j\geq3,
 \tag{T-14301.5}
\]

is sufficient.  The particular schedule is immaterial: only
`tau_j -> 1/2` from below and `eta_j -> 0` are used.

### Alternative fixed-strip formulation

It is also sufficient to assume that there is a single sequence of nonzero
real scalars `c_j` such that, for every fixed `0<tau<1/2`,

\[
 \|c_j\xi_j-k_{\lambda_j}\|_{\lambda_j,\tau}
 \longrightarrow0.
 \tag{T-14301.6}
\]

The moving-strip formulation is stronger as a certificate interface because
one bound at level `j` automatically controls every smaller fixed weight.

### Support-only fallback

Since

\[
 u^{2\tau}+u^{-2\tau}\leq2\lambda^{2\tau}
 \qquad (\lambda^{-1}\leq u\leq\lambda),
\]

it is sufficient, though generally much more wasteful, to prove

\[
 \sqrt2\,\lambda_j^{\tau_j}
 \|c_j\xi_j-k_{\lambda_j}\|_{\mathcal H_{\lambda_j}}
 \leq\eta_j.
 \tag{T-14301.7}
\]

The weighted criterion is the primary theorem because it does not charge an
endpoint-sized error to discrepancies concentrated near the center of the
support.

## Motivation and novelty

The source paper proposes two unresolved limiting steps:

1. at fixed `lambda`, pass from finite matrices `QW_lambda^N` to an infinite
   localized Weil operator and prove that its ground state is simple and even;
2. then prove that this infinite ground state approaches the explicit prolate
   candidate as `lambda -> infinity`.

T-14301 bypasses the intermediate infinite ground state entirely.  It asks for
one diagonal sequence of *finite* matrices.  Each member can in principle be
certified with finite interval linear algebra, while the limiting analytic
content is isolated in the weighted error (T-14301.4).

The exponential weight is not cosmetic.  It is exactly the source-side norm
that controls the Fourier–Mellin transform on horizontal lines inside the
critical strip.  Replacing it by ordinary `L2` and a support supremum introduces
an avoidable factor growing almost like `lambda^(1/2)`.

This is different from Issue #142.  Issue #142 seeks finite completeness for a
negative localized-Weil witness if RH is false.  T-14301 is a positive
sufficient criterion: establishing its asymptotic weighted approximation proves
RH.

## Proof

### Step 1 — a support-independent Hardy-strip transform bound

Write `u=e^t`, so `d^*u=dt`, and extend the logarithmic representative of `f`
by zero from `[-log lambda,log lambda]` to the whole real line.  Then

\[
 \widehat f(x+iy)=\int_{\mathbb R}f(e^t)e^{-ixt}e^{yt}\,dt.
\]

Fix `0<=sigma<tau<1/2`.  Cauchy–Schwarz with the weight

\[
 w_\tau(t)=e^{2\tau t}+e^{-2\tau t}=2\cosh(2\tau t)
\]

gives

\[
 |\widehat f(x+iy)|^2
 \leq \|f\|_{\lambda,\tau}^2
 \int_{\mathbb R}\frac{e^{2yt}}{w_\tau(t)}\,dt.
 \tag{T-14301.8}
\]

The remaining integral can be evaluated exactly.  With
`r=exp(4 tau t)` and `a=1/2+y/(2 tau)`, the Euler beta integral gives, for
`|y|<tau`,

\[
 \begin{aligned}
 \int_{\mathbb R}\frac{e^{2yt}}{w_\tau(t)}\,dt
 &=\frac1{4\tau}\int_0^\infty\frac{r^{a-1}}{1+r}\,dr\\
 &=\frac{\pi}{4\tau\sin(\pi a)}
 =\frac{\pi}{4\tau\cos(\pi y/(2\tau))}.
 \end{aligned}
 \tag{T-14301.9}
\]

The right-hand side is increasing in `|y|`.  Hence

\[
 \boxed{
 \sup_{|\Im z|\leq\sigma}|\widehat f(z)|
 \leq C_{\sigma,\tau}\|f\|_{\lambda,\tau},
 \qquad
 C_{\sigma,\tau}
 =\left(\frac{\pi}
 {4\tau\cos(\pi\sigma/(2\tau))}\right)^{1/2}.}
 \tag{T-14301.10}
\]

A simpler bound, useful when constants do not matter, follows from
`w_tau(t)>=exp(2 tau |t|)`:

\[
 C_{\sigma,\tau}\leq(\tau-\sigma)^{-1/2}.
 \tag{T-14301.11}
\]

Unlike the elementary support-supremum estimate, both constants are independent
of `lambda` and of `Re z`.

### Step 2 — transfer prolate convergence to the finite ground states

Fix a compact set `K` in the open strip `|Im z|<1/2`.  Choose numbers

\[
 \max_{z\in K}|\Im z|<\sigma<\tau<\frac12.
\]

For fixed `u>0`, the function

\[
 \tau\longmapsto u^{2\tau}+u^{-2\tau}
 =2\cosh(2\tau\log u)
\]

is nondecreasing on `tau>=0`.  Thus, eventually `tau_j>=tau` and

\[
 \|c_j\xi_j-k_{\lambda_j}\|_{\lambda_j,\tau}
 \leq
 \|c_j\xi_j-k_{\lambda_j}\|_{\lambda_j,\tau_j}
 \leq\eta_j.
\]

Applying (T-14301.10) yields

\[
 \sup_{z\in K}
 |\widehat{c_j\xi_j}(z)-\widehat{k_{\lambda_j}}(z)|
 \leq C_{\sigma,\tau}\eta_j
 \longrightarrow0.
 \tag{T-14301.12}
\]

Connes–Consani–Moscovici Lemma 7.3 states that
`hat(k_lambda)` converges to the Riemann `Xi` function uniformly on closed
substrips of `|Im z|<1/2`.  Hence

\[
 \widehat{c_j\xi_j}\longrightarrow\Xi
 \quad\hbox{locally uniformly on }|\Im z|<\frac12.
 \tag{T-14301.13}
\]

### Step 3 — every finite approximant has only real zeros

By hypotheses 1 and 2, the exact finite truncated form is even-simple in the
terminology of Connes–Consani–Moscovici.  Their Proposition 5.7 supplies the
nonvanishing boundary functional `delta_N(xi_j) != 0`, so `xi_j` may be
rescaled to the normalization required in their Theorem 5.10.  That theorem
shows that `hat(xi_j)` is entire and all of its zeros are real.  Multiplication
by the nonzero scalar `c_j` does not change its zeros.

### Step 4 — Hurwitz excludes every nonreal Xi zero

Assume that `Xi(z_0)=0` for some nonreal `z_0` with
`|Im z_0|<1/2`.  Choose a disk `D` centered at `z_0` whose closure lies in the
open strip and is disjoint from the real axis.  Every
`hat(c_j xi_j)` is holomorphic and nonvanishing on `D`, and the sequence
converges locally uniformly there to `Xi`.  Hurwitz's theorem says that the
limit is either nonvanishing on `D` or identically zero.  Both alternatives
contradict `Xi(z_0)=0` and the fact that `Xi` is not identically zero.

Thus every zero of `Xi` in `|Im z|<1/2` is real.  Under the centered coordinate

\[
 \Xi(z)=\xi\!\left(\frac12+iz\right),
\]

a nontrivial zeta zero `rho=beta+i gamma`, with `0<beta<1`, corresponds to

\[
 z=\gamma-i(\beta-\tfrac12),
 \qquad |\Im z|<\frac12.
\]

This `z` is real exactly when `beta=1/2`.  Hence every nontrivial zero lies on
the critical line.  RH follows.  QED.

## Finite adapter through L-14301

Let `P_j` be the ordinary `L2` orthogonal projection onto
`E_{N_j}(lambda_j)`, put

\[
 p_j=P_jk_{\lambda_j},
 \qquad q_j=\|p_j\|_2,
 \qquad v_j=p_j/q_j,
\]

and suppose `p_j` is nonzero.  Let

\[
 \kappa_{j,\tau_j}
 :=\sup_{\substack{w\in E_{N_j}(\lambda_j)\cap H_+\cap v_j^\perp\\
                    \|w\|_2=1}}
   \|w\|_{\lambda_j,\tau_j}.
 \tag{T-14301.14}
\]

If L-14301 certifies effective residual `R_j` and even-complement gap `g_j`, its
weighted projective corollary gives

\[
 \inf_{c\neq0}
 \|c\xi_j-k_{\lambda_j}\|_{\lambda_j,\tau_j}
 \leq
 \underbrace{\|(I-P_j)k_{\lambda_j}\|_{\lambda_j,\tau_j}}
             _{\text{weighted projection tail}}
 +q_j\kappa_{j,\tau_j}\frac{R_j}{g_j}.
 \tag{T-14301.15}
\]

Both terms are finite-dimensional or explicit-function quantities.  The square
`kappa^2` is the largest generalized eigenvalue of the weighted Gram form
relative to the ordinary `L2` Gram form on the even complement; a rational
upper bound can be certified by exact LDL.  Thus (T-14301.15), rather
than an ordinary unweighted overlap, is the natural per-level target.

## What would constitute a completed proof

A finite prefix of passing levels does not prove RH.  Completion requires a
finite mathematical argument establishing (T-14301.4) for all sufficiently
large `j`—for example, an explicit asymptotic theorem for the weighted tail,
residual, complement factor, and gap.  Finitely many earlier levels may simply
be discarded and the sequence reindexed; checking them is useful only for a
fixed canonical ledger.  A merely extrapolated numerical decay law is not
enough.

## Analytic domain audit

- Compact support makes every transform in (T-14301.1) entire; no contour,
  branch, or meromorphic division is used in the new proof.
- The source norm (T-14301.2) is finite for every compactly supported finite
  vector and explicit prolate target.
- Hurwitz is applied only on disks compactly contained in
  `|Im z|<1/2` and disjoint from the real axis.
- The boundary lines `|Im z|=1/2` are not needed: every nontrivial zeta zero
  satisfies `0<Re rho<1`, so its centered coordinate is strictly inside the
  strip.
- The scalar `c_j` must be nonzero.  It may change normalization but not the
  zero set.

## Dependency and normalization audit

- CCM Proposition 5.7 is imported for `delta_N(xi) != 0` under the finite
  even-simple hypothesis.
- CCM Theorem 5.10 is imported for the real-zero property of each finite
  transform.
- CCM Lemma 7.3 is imported for local-uniform convergence of the explicit
  prolate transforms to `Xi`.
- Every one of these imports must be independently checked in exactly the same
  `lambda`, Fourier–Mellin, and `Xi` convention before an RH claim.

## Remaining uncertainty

The theorem above is a complete implication conditional on the cited imported
interfaces, but it remains `PROPOSED` until independent review.  No production
sequence satisfying (T-14301.4), and no asymptotic theorem forcing such a
sequence, is claimed here.
