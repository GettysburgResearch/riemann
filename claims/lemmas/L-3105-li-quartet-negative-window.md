# L-3105 — A bounded negative window for one off-line Li quartet

Claim ID: L-3105  
Title: Every off-critical functional-equation zero quartet has a negative algebraic Li contribution in an explicit bounded index window  
Status: PROPOSED  
Authoring agent: `gpt56-05`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: D-0301 and L-0340  
Scope: target selection for Li-coefficient searches  
Related counterexample candidates: negative Li coefficients

## Statement

Let `rho` be a nonreal nontrivial zeta zero with `Re(rho)<1/2`, and define

\[
 z=1-\frac1\rho=re^{i\theta}.
\]

By L-0340, `r>1`. The functional-equation/conjugation orbit

\[
 \mathcal O(\rho)=\{\rho,\bar\rho,1-\rho,1-\bar\rho\}
\]

maps under `sigma -> 1-1/sigma` to

\[
 \{z,\bar z,z^{-1},\bar z^{-1}\}.
\]

Define the finite algebraic quartet contribution at Li index `n` by

\[
 Q_n(\rho)=\sum_{\sigma\in\mathcal O(\rho)}
 \left[1-\left(1-\frac1\sigma\right)^n\right].
\]

Then

\[
 Q_n(\rho)=4-2(r^n+r^{-n})\cos(n\theta).
\]

Let

\[
 N_0=\left\lfloor\frac{\log4}{\log r}\right\rfloor+1,
\]

so that `r^{N_0}>4`. There exists an integer

\[
 n\in\{N_0,2N_0,\ldots,6N_0\}
\]

for which

\[
 \cos(n\theta)\ge\frac12
 \qquad\text{and hence}\qquad
 Q_n(\rho)<0.
\]

Thus one off-line quartet always has a negative algebraic contribution at some
index between `N_0` and `6N_0`.

This statement concerns one finite orbit only. It does **not** assert that the
complete Li coefficient `lambda_n` is negative at that index.

## Motivation

L-0340 identifies radial amplification but does not account exactly for the
reflected zeros or give an index target. L-0403 shows that a zero above the
verified height would require enormous indices before substantial radial
amplification. The present lemma complements that barrier: once a candidate
`rho` is specified, it produces a concrete factor-six search window in which
its complete symmetry quartet contributes negatively.

## Proof

The transformed values are immediate except for the reflected pair:

\[
 1-\frac1{1-\rho}=\frac{\rho}{\rho-1}=z^{-1},
\]

and conjugation gives the fourth value. Therefore

\[
 \begin{aligned}
 Q_n
 &=4-z^n-\bar z^n-z^{-n}-\bar z^{-n}\\
 &=4-2r^n\cos(n\theta)-2r^{-n}\cos(n\theta)\\
 &=4-2(r^n+r^{-n})\cos(n\theta).
 \end{aligned}
\]

It remains to choose `n`. Consider the seven points

\[
 0,N_0\theta,2N_0\theta,\ldots,6N_0\theta
\]

modulo `2pi`. Partition the circle into six half-open arcs of length `2pi/6`.
Two of the seven points lie in the same arc. Their difference is `qN_0 theta`
for some `1<=q<=6`, and its distance to an integer multiple of `2pi` is at most
`2pi/6=pi/3`. Hence, for `n=qN_0`,

\[
 \cos(n\theta)\ge\cos(\pi/3)=\frac12.
\]

Also `n>=N_0`, so `r^n+r^{-n}>r^{N_0}>4`. Consequently,

\[
 Q_n
 \le4-(r^n+r^{-n})<0.
\]

This proves the bounded-window claim. ∎

## Analytic domain audit

The proof is finite algebra on one zero orbit. The logarithms defining `N_0`
are real because `r>1`. No rearrangement of the full conditionally convergent
Li zero sum is used.

## Dependency audit

D-0301 supplies the zeta-zero symmetry conventions. L-0340 proves `r>1` for a
left-of-line zero. Li's full criterion is not needed for the finite orbit
identity, but it is needed by Issue #14 to interpret a certified total negative
coefficient as an RH counterexample.

## Gap audit

- A negative quartet contribution can be outweighed by all other zero orbits.
- The complete Li zero sum has a symmetric limiting convention; this lemma does
  not justify truncating or regrouping the infinite sum beyond isolating one
  finite orbit algebraically.
- A right-of-line zero should first be replaced by its reflected left-of-line
  partner so that `r>1`.
- The bound is intentionally coarse; it guarantees a window but does not locate
  the best phase-aligned index.
- A numerical candidate `rho` needs rigorous enclosure before `r` and `N_0` can
  be used in a certificate.

## Adversarial tests

1. Substitute a critical-line zero geometry `r=1`; the definition of `N_0`
   correctly breaks down because the lemma excludes this case.
2. Use `theta=pi`; even multiples produce perfect alignment and the window
   contains one.
3. Use an irrational `theta/(2pi)` and verify the six-bin pigeonhole step
   numerically for random examples.
4. Let `r` approach `1` from above and confirm that `N_0` diverges, matching the
   scale barrier in L-0403.

## Remaining uncertainty

No mathematical gap is known. Its value is strategic rather than dispositive:
the hard problem remains rigorous evaluation of the complete `lambda_n` at
indices of this scale.

## Suggested next attack

For any future certified off-line zero box, interval-enclose `r`, derive a safe
upper bound for `N_0`, and focus arithmetic or contour extraction of Li
coefficients on the resulting factor-six window rather than scanning linearly
from small indices.
