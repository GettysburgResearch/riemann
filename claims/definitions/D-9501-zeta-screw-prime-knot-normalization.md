# D-9501 — Zeta screw function and prime-knot normalization

Claim ID: D-9501  
Title: Zeta screw function, finite kernels, and prime-knot normalization  
Status: PROPOSED  
Authoring agent: `gpt56-08`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: Suzuki, arXiv:2206.03682v4, especially (1.1), (1.4), Theorems 1.1, 1.2, and 1.7  
Scope: Issue #95 and all `95xx` claims  
Related counterexample candidates: none yet

## Definitions

We use the completed zeta normalization

\[
 \xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

For `t >= 0`, define Suzuki's function

\[
\begin{aligned}
 \Psi(t)={}&4\left(e^{t/2}+e^{-t/2}-2\right)
 -\sum_{n\le e^t}\frac{\Lambda(n)}{\sqrt n}(t-\log n)\\
 &+\frac t2\left(\psi\!\left(\frac14\right)-\log\pi\right)
 +\frac14\left(C-e^{-t/2}\Phi(e^{-2t},2,1/4)\right),
\end{aligned}
\tag{D-9501.1}
\]

where

\[
 \Lambda(p^k)=\log p,\qquad
 C=\pi^2+8G,
\]

`G` is Catalan's constant, `psi=Gamma'/Gamma`, and

\[
 \Phi(z,2,a)=\sum_{m=0}^{\infty}\frac{z^m}{(m+a)^2}.
\]

Extend `Psi` evenly to the real line and put

\[
 g(t)=-\Psi(t).
\]

For exact real nodes `t_1,...,t_m`, define three finite matrices:

\[
 S_{ij}=\Psi(t_i)+\Psi(t_j)-\Psi(t_i-t_j),
\tag{D-9501.2}
\]

\[
 D_{ij}=\Psi(t_i-t_j),
\tag{D-9501.3}
\]

and, for exact `lambda>0`,

\[
 K^{(\lambda)}_{ij}=\exp(-\lambda D_{ij}).
\tag{D-9501.4}
\]

We call them respectively the **anchored screw matrix**, the **screw-distance
matrix**, and the **Schoenberg-Gaussian matrix**.

## Imported source interfaces

The following statements are imported from Suzuki and are not silently
reproved by this definition.

1. Formula (D-9501.1) is continuous on `[0,infinity)`, satisfies `Psi(0)=0`,
   and has the unconditional zero expansion
   \[
      \Psi(t)=\sum_\gamma\frac{1-\cos(\gamma t)}{\gamma^2},
   \]
   with Suzuki's symmetric zero convention.
2. RH is equivalent to `g=-Psi` being a Krein screw function, meaning that
   \[
      G_g(t,u)=g(t-u)-g(t)-g(-u)+g(0)
   \]
   is a nonnegative-definite kernel on the real line.
3. RH is equivalent to the pointwise condition `Psi(t)>=0` for every real
   `t`; under RH, `Psi(t)>0` for `t!=0`.

The finite consequences used by this branch are proved separately in
`L-9501` and `L-9502` so that the exact sign conventions can be reviewed
without importing any distance-geometry folklore.

## Prime-knot notation

List all prime powers in strictly increasing order,

\[
 2=q_1<q_2<\cdots,
 \qquad q_j=p_j^{k_j},
\]

and put

\[
 \tau_j=\log q_j,
 \qquad
 w_j=\frac{\Lambda(q_j)}{\sqrt{q_j}}
     =\frac{\log p_j}{\sqrt{q_j}}.
\]

Define the directed-prefix targets

\[
 P_{0,j}=\sum_{r\le j}w_r,
 \qquad
 P_{1,j}=\sum_{r\le j}w_r\tau_r.
\tag{D-9501.5}
\]

The only nonsmooth points of the prime term in (D-9501.1) are the knots
`t=tau_j`.  The newly deposited summand vanishes at its own knot, so `Psi` is
continuous there; its first derivative jumps downward by exactly `w_j`.

## Exact input conventions for future certificates

A proof candidate must encode every node and coefficient in one of the
following ways.

- A dyadic rational is stored by its signed numerator and denominator power.
- A knot `log(q)` is stored symbolically by the integer `q`, not by a decimal.
- A Gaussian parameter `lambda` and Rayleigh vector are exact rationals or
  dyadics.
- Comparisons between a dyadic node and `log(q)` are decided by directed
  logarithm enclosures.  A rounded comparison is not accepted.
- A prime-power manifest row stores `(q,p,k)` and is checked both for
  `q=p^k` and for contiguous, duplicate-free coverage.

## Motivation

The explicit prime side of `Psi` has no huge oscillatory phases.  Between two
successive prime-power knots it is merely affine.  Consequently a global
scalar search can be reduced to two streaming prefix sums and one monotone
one-dimensional equation per susceptible cell.  The matrices above then
turn the same scalar table into conditional-negative-type and nonlinear
Gaussian certificates that are structurally different from the repository's
current carrier and `xi'/xi` tables.

## Analytic domain audit

- `xi` is entire with precisely the nontrivial zeta zeros.
- Formula (D-9501.1) is used only for real `t`.
- `Phi(e^{-2t},2,1/4)` is represented by an absolutely convergent series for
  `t>0`; `t=0` is handled by the continuous value `Psi(0)=0`.
- `sqrt(q)` is the positive real square root.
- `log(q)` is the real logarithm of a positive integer.
- No contour, logarithm branch in the complex plane, or division by `xi`
  occurs in the finite evaluator.

## Dependency audit

The equivalences with RH are imported from the cited primary source.  The
prime-knot calculus in `L-9503` starts directly from (D-9501.1).  The finite
PSD, conditional-negative-type, metric, and Gaussian implications are proved
in `L-9501` and `L-9502`.

## Gap audit

- The zero expansion is not a numerically convergent recipe for this branch;
  the prime formula is the computational definition.
- Pointwise positivity at finitely many sampled points does not prove RH.
- A negative floating-point eigenvalue is not a witness.
- The condition `n<=exp(t)` must not be decided using a rounded exponential.
- Prime powers, not only primes, occur in the manifest.
- At a knot the function is continuous but the one-sided derivatives differ.
- The imported equivalence must be checked against the exact `xi` and Fourier
  normalizations before any counterexample status is advanced.

## Adversarial tests

1. Verify `Psi(0)=0` by `Phi(1,2,1/4)=C`.
2. At `t=log(q)`, evaluate with and without the new `q` term and confirm exact
   equality.
3. Check the right-minus-left derivative jump `-Lambda(q)/sqrt(q)`.
4. Compare the prime formula with Suzuki's one-sided Fourier identity at safe
   complex points using an independent special-function implementation.
5. Reconstruct a small manifest by trial division and by a sieve and require
   exact agreement.

## Remaining uncertainty

The source theorem has not yet received an independent repository
normalization audit.  No directed implementation is included in this first
commit.

## Suggested next attack

Independently translate Suzuki's Fourier and zero conventions into the
repository's standard `xi` card, then implement the `L-9503` cell certificate
with Arb intervals and a streaming prime-power manifest.
