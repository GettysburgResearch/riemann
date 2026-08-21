# R-21702 — Generic probability structure does not prove the final saturation

Claim ID: `R-21702`  
Title: Symmetry, characteristic-function positivity, reciprocal size bias, additive GGC structure, finite zero verification, and ordinary log-concavity do not imply SAT  
Status: **PROPOSED PENDING INDEPENDENT REVIEW — exact counterexamples and scope barriers supplied**  
Authoring agent: `gpt56-pro-global-01`  
Created: 2026-08-07  
Dependencies: `T-21703`, `L-21704`; elementary characteristic-function algebra  
Scope: adversarial guardrail for independent review of the proposed RH proof

## 1. The load-bearing statement

The final saturation is

\[
\operatorname{Var}_{1/2}(\log Y)
\le
2\sum_{\gamma\in\Gamma_L}\frac{m_\gamma}{\gamma^2}.
\tag{R-21702.1}
\]

By `T-21703`, this statement is equivalent to RH. Consequently no generic
probability property may be promoted to (R-21702.1) without an exact theorem
special to the Brownian/gamma law and the actual line-zero set.

## 2. An entire characteristic function with only complex zeros

Fix

\[
\frac12<a<1,
\qquad b>0,
\]

and define

\[
\boxed{\phi_{a,b}(t)=a+(1-a)\cos(bt).}
\tag{R-21702.2}
\]

This is the characteristic function of the centered three-point law

\[
\mathbb P(X=0)=a,
\qquad
\mathbb P(X=\pm b)=\frac{1-a}{2}.
\]

For real `t`,

\[
\phi_{a,b}(t)\ge2a-1>0,
\]

so it has no real zero. Its complex zeros solve

\[
\cos(bt)=-\frac{a}{1-a}<-1,
\]

and are nonreal. Thus an even entire characteristic function may carry complex
zeros while remaining strictly positive on the real axis.

Multiplying (R-21702.2) by any characteristic function with real zeros gives a
probability law whose characteristic function has both the inherited real zeros
and the new complex zeros. For example,

\[
\left(\frac{\sin(ct)}{ct}\right)^{2N}\phi_{a,b}(t)
\tag{R-21702.3}
\]

is the characteristic function of a compactly supported, arbitrarily
high-finite-regularity density convolved with the three-point law. It has
infinitely many real zeros and infinitely many nonreal zeros.

Therefore none of the following is sufficient:

```text
characteristic function
+ symmetry
+ entire continuation
+ compact support or very rapid tails
+ infinitely many real zeros.
```

## 3. Reciprocal size-bias symmetry is generic

Let `p(z)` be any symmetric probability density on the real line satisfying

\[
\int e^{-z/2}p(z)dz<\infty.
\]

Define

\[
q(z)=\frac{e^{-z/2}p(z)}
          {\int e^{-u/2}p(u)du},
\qquad
Y=e^Z\quad(Z\sim q).
\tag{R-21702.4}
\]

Under the half-size-biased law of `Y`, the density of `log Y` is exactly `p`.
Moreover symmetry of `p` gives

\[
q(-z)=e^zq(z),
\tag{R-21702.5}
\]

which is the logarithmic form of

\[
\mathbb E[g(1/Y)]=\mathbb E[Yg(Y)].
\tag{R-21702.6}
\]

Hence the reciprocal size-bias symmetry used in the Brownian representation is
not by itself restrictive enough to force real zeros or saturation.

## 4. Additive GGC does not imply multiplicative real-rootedness

The variable

\[
\Sigma_2=\frac2{\pi^2}\sum_{n\ge1}\frac{\Gamma(2)_n}{n^2}
\]

is an additive generalized gamma convolution. This controls its ordinary
Laplace transform. The RH endpoint concerns the Fourier transform of
`log Sigma_2` under a fractional size bias, which is a multiplicative/Mellin
object.

There is no general implication

```text
additive GGC
=> fractional-size-biased log law is PF_infinity
=> Mellin transform has only critical-line zeros.
```

Indeed, an infinitely divisible characteristic function is zero-free on the
real axis, whereas the half-tilted Brownian log law has the known critical-line
zeros of `Xi`. Thus its logarithmic law is not an ordinary infinitely divisible
law whose Levy--Khintchine representation could settle RH automatically.

The off-center GGC representation valid in the Euler-product half-plane cannot
be analytically continued to the center while retaining a positive Thorin
measure without proving an RH-equivalent zero-free statement. The separate
report `2026-08-07-polson-thorin-gap-audit.md` records this boundary.

## 5. Factorwise convex order is not the completion

`L-21704` proves

\[
C\preceq_{\rm cx}U
\]

for the complete cosine-bell and uniform line-zero noises. But the final target
is

\[
Z+C\preceq_{\rm cx}U.
\]

Adding an independent nondegenerate `Z` increases variance and generally makes a
law less concentrated. Therefore the first convex-order statement cannot be
iterated or tensorized into the second one.

A valid completion must use the specific dependence or coupling supplied by the
Brownian bridge, the gamma perpetuity, or an exact arithmetic identity. An
independent-noise comparison is structurally incapable of proving SAT.

## 6. Finite verified height cannot force equality

Suppose every zero through height `H` has been certified on the critical line.
The complete unknown defect satisfies an explicit tail bound tending to zero as
`H` tends to infinity. This proves near saturation at every finite verified
height.

It cannot prove exact saturation. A hypothetical quartet at ordinate `T>H`
with fixed `0<delta<1/2` contributes

\[
4m\frac{T^2-\delta^2}{(T^2+\delta^2)^2}
=\frac{4m}{T^2}+O(T^{-4}),
\tag{R-21702.7}
\]

which is strictly positive but arbitrarily small. No finite numerical precision
or finite zero table can round this possibility to zero.

## 7. Log-concavity and low-order total positivity are insufficient

Strict log-concavity is a `TP_2` property. The real-zero conclusion required by
SAT is a full Laguerre--Polya or `TP_infinity` statement. The gap between these
orders is load bearing.

Even for admissible rapidly decreasing kernels, strict logarithmic concavity
alone does not force the Fourier transform into the Laguerre--Polya class; the
higher associated positive-definiteness or Laguerre inequalities remain
necessary. Therefore a proof of log-concavity of the Riemann kernel is useful
structure, but it cannot be substituted for SAT.

## 8. Circularity checklist

An independent proof of SAT must not invoke any of the following, explicitly or
through an equivalent reformulation:

1. all zeros of `Xi` are real;
2. `Xi` lies in the Laguerre--Polya class;
3. the xi kernel is `PF_infinity` or totally positive of all orders;
4. the complete central Hausdorff hierarchy is nonnegative;
5. the centered reciprocal xi function is a GGC Laplace transform;
6. the xi scattering ratio is inner or its Hankel defect vanishes;
7. the completed annihilator residual is zero;
8. the off-line canonical factor is constant;
9. finite verified-height near saturation is exact saturation.

Any one of items 1--8 already contains RH. Item 9 loses the global quantifier.

## 9. Valid remaining targets

The following would be genuine, noncircular completions if proved directly from
Brownian/gamma or prime arithmetic data:

\[
\operatorname{Var}_{1/2}(\log Y)
\le2\sum_\gamma m_\gamma/\gamma^2,
\]

\[
Z+C\preceq_{\rm cx}U,
\]

\[
\mathbb E[U\mid Z+C]=Z+C
\quad\text{under an explicit coupling},
\]

or the corrected completed prime identity

\[
R_\infty\equiv0.
\]

This refutation does not weaken those targets. It prevents generic probability
terminology from being mistaken for the missing theorem.