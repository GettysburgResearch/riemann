# L-32313 — The SHARP bottom tail is a shifted-zeta Riesz state

Claim ID: `L-32313`  
Title: The continuum bottom-tail reserve is one squared square-root Möbius Riesz mean with Mellin denominator `zeta(s+1)`; its positivity is distinct from the RH-bearing SHARP margin  
Status: **PROPOSED COMPLETE EXACT ANALYTIC REDUCTION — TAIL SIGN OPEN**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `L-32312`; elementary partial summation and Mellin integration  
Scope: continuum/fixed-depth tail state; no positivity claim, no SHARP conclusion, no RH claim

## 1. The bottom tail from the band theorem

Retain

\[
A(x)=\sum_{n\le x}\frac{\mu(n)}{\sqrt n},
\qquad
B(x)=\sum_{n\le x}\frac{\mu(n)}n,
\qquad
M(x)=\sum_{n\le x}\mu(n).
\]

`L-32312` identifies the continuum bottom tail at integer depth `R` as

\[
\mathcal C_R
=B(R-1)-\frac{2A(R-1)}{\sqrt R}+\frac{M(R-1)}R.
\tag{L-32313.1}
\]

The term `n=R`, when present, has zero coefficient in the identity below, so one may freely use `R` in place of `R-1`.

## 2. Exact squared-hinge identity

Expanding one square gives

\[
\left(\frac1{\sqrt n}-\frac1{\sqrt R}\right)^2
=\frac1n-\frac{2}{\sqrt{nR}}+\frac1R.
\]

Therefore

\[
\boxed{
\mathcal C_R
=\sum_{n\le R}\mu(n)
\left(\frac1{\sqrt n}-\frac1{\sqrt R}\right)^2.
}
\tag{L-32313.2}
\]

This is the exact fixed-depth continuum tail used by the outer-band SHARP theorems.  It is a Möbius transform of a **squared** square-root hinge, not the original SHARP hinge.

For real `x>=1` define its continuous version

\[
\boxed{
\mathcal C(x)
=\sum_{n\le x}\mu(n)
\left(\frac1{\sqrt n}-\frac1{\sqrt x}\right)^2.
}
\tag{L-32313.3}
\]

Equivalently,

\[
\boxed{
\mathcal C(x)
=B(x)-\frac{2A(x)}{\sqrt x}+\frac{M(x)}x.
}
\tag{L-32313.4}
\]

At integer `x` the newly entering summand is exactly zero, so `C(x)` is continuous across every arithmetic knot.

## 3. Exact derivative between knots

On every open interval containing no integer, `A,B,M` are constant.  Differentiating (L-32313.4) gives

\[
\boxed{
\mathcal C'(x)
=\frac{A(x)}{x^{3/2}}-\frac{M(x)}{x^2}
=\frac{\sqrt x\,A(x)-M(x)}{x^2}.
}
\tag{L-32313.5}
\]

Thus the bottom-tail state has no jumps; its only local arithmetic control is the simple weighted Mertens combination `sqrt(x) A(x)-M(x)`.

A second useful form follows by partial summation from `A(x)=sum (mu(n)/n)sqrt(n)` and `M(x)=sum (mu(n)/n)n`:

\[
\boxed{
\mathcal C(x)
=\frac1{\sqrt x}\int_1^x\frac{B(t)}{\sqrt t}\,dt
-\frac1x\int_1^x B(t)\,dt.
}
\tag{L-32313.6}
\]

This identity is exact in the Riemann/Stieltjes convention because `B` is piecewise constant.

## 4. Mellin transform

For `Re(s)>0`, absolute convergence permits interchange of the finite endpoint sum and the integral.  For one integer `n`,

\[
\begin{aligned}
&\int_n^\infty
\left(\frac1{\sqrt n}-\frac1{\sqrt x}\right)^2
x^{-s-1}\,dx\\
&\qquad=n^{-s-1}
\left[
\frac1s-\frac2{s+1/2}+\frac1{s+1}
\right]\\
&\qquad=\frac{n^{-s-1}}
{s(s+1)(2s+1)}.
\end{aligned}
\tag{L-32313.7}
\]

Summing against `mu(n)` yields

\[
\boxed{
\int_1^\infty\mathcal C(x)x^{-s-1}\,dx
=\frac{1}
{s(s+1)(2s+1)\zeta(s+1)}.
}
\tag{L-32313.8}
\]

The apparent singularity at `s=0` is removable because

\[
\zeta(s+1)\sim\frac1s,
\]

and the continued value there is exactly

\[
\boxed{
\lim_{s\to0}
\frac{1}{s(s+1)(2s+1)\zeta(s+1)}=1.
}
\tag{L-32313.9}
\]

Every nontrivial zeta zero `rho` appears instead at

\[
s=\rho-1,
\]

strictly to the **left** of the imaginary axis because `Re(rho)<1` is the classical zero-free-line theorem.  In particular the positive-half-plane pole firewall of the original SHARP/Psi state has disappeared after passing to the squared-hinge bottom tail.

## 5. Why this separates two difficulties

The all-depth SHARP margin of `T-32302` has transform

\[
\frac{s+3/2}
{s(s-1/2)\zeta(s+1/2)},
\]

so an off-critical zero appears at positive real part `Re(rho)-1/2`.

By contrast, the bottom-tail state has transform (L-32313.8), with reciprocal zeta shifted by a full unit.  Therefore:

```text
bottom-tail positivity / lower bounds:
    shifted-zeta problem at Re(s+1)>1;

bottom tail beats the canonical local threshold at all depths:
    returns to the critical Psi / zeta(s+1/2) problem.
```

This explains the finite-band experiments.  The tail itself can remain robustly positive over enormous fixed ranges without constituting an RH proof; the genuinely critical information is in the shrinking comparison against the local threshold `vartheta_R` from `L-32312`.

## 6. A sign firewall for the bottom tail

Although (L-32313.8) is shifted away from RH, an **eventual one-sign theorem** for `C(x)` is still not declared elementary.

Suppose, for example, that `C(x)>=0` for all sufficiently large `x`.  Put `f(t)=C(e^t)`.  Its Laplace transform is (L-32313.8), up to an entire compact correction.  If the abscissa of convergence were zero, Landau's one-sign theorem would force a singularity at the real point `s=0`, but (L-32313.9) is regular there.  Hence the abscissa would have to be strictly negative.

Since every zeta zero `rho` produces a pole at `rho-1`, this would imply a **fixed zero-free strip**

\[
\boxed{
\operatorname{Re}\rho\le1-\delta
}
\tag{L-32313.10}
\]

for some absolute `delta>0`.

No such fixed strip is claimed here.  Thus even the apparently softer global tail sign should not be promoted from finite reconnaissance without proof.

## 7. Proof boundary

Closed exactly:

1. the squared-hinge Möbius representation of the continuum bottom tail;
2. continuity at every integer knot;
3. the derivative formula between knots;
4. the partial-summation representation through `B(x)`;
5. the Mellin transform `1/[s(s+1)(2s+1)zeta(s+1)]`;
6. the distinction between the shifted-zeta tail state and the critical SHARP/Psi state;
7. the conditional fixed-zero-free-strip consequence of eventual one-sidedness.

Open:

1. positivity or eventual one-sidedness of `C(x)`;
2. a quantitative all-depth comparison `C_R>vartheta_R`;
3. eventual one-sidedness of `Psi`;
4. full SHARP;
5. RH.
