# L-32312 — The continuum SHARP scalar has an exact positive renewal and Abel--Green identities

Claim ID: `L-32312`  
Title: The all-depth SHARP margin is the hyperbola inverse of the positive kernel `4 sqrt(x)-3`, with exact Abel representations, jump law, and interval ODE  
Status: **PROPOSED COMPLETE EXACT ANALYTIC/FINITE-SUM THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `T-32302` only for the definition of `Psi`; elementary partial summation and Möbius inversion  
Scope: exact structure of the continuum scalar; no sign theorem or RH conclusion

## 1. The scalar

Retain

\[
 A(x)=\sum_{n\le x}{\mu(n)\over\sqrt n},
 \qquad
 B(x)=\sum_{n\le x}{\mu(n)\over n},
\]

and

\[
\boxed{
 \Psi(x)=4\sqrt x\,B(x)-3A(x),
 \qquad x\ge1.
}
\tag{L-32312.1}
\]

`T-32302` proves that eventual one-sidedness of `Psi` implies RH and that fixed-ratio SHARP coefficients converge to a positive multiple of this scalar. The present lemma derives additional exact structure without assuming any sign.

## 2. Green-kernel representation

For `n<=x`, put

\[
 k(x/n)=4\sqrt{x/n}-3.
\]

Then directly

\[
\boxed{
 \Psi(x)
 =\sum_{n\le x}{\mu(n)\over\sqrt n}
   \left(4\sqrt{x/n}-3\right).
}
\tag{L-32312.2}
\]

In logarithmic variables `x=e^t`, the causal kernel is

\[
\boxed{k(t)=4e^{t/2}-3,\qquad t\ge0.}
\tag{L-32312.3}
\]

Its Laplace transform is

\[
\int_0^\infty k(t)e^{-zt}dt
={z+3/2\over z(z-1/2)},
\]

so (L-32312.2) reproduces exactly the Mellin transform of `T-32302` after multiplication by `1/zeta(z+1/2)`.

The kernel itself is strictly positive and increasing on `t>=0`. All sign difficulty is therefore in the Möbius source, not in the Green response.

## 3. Exact positive renewal identity

Let

\[
 (\mathcal P f)(x)
 :=\sum_{d\le x}{1\over\sqrt d}f(x/d).
\tag{L-32312.4}
\]

Then

\[
\begin{aligned}
\mathcal P\Psi(x)
&=\sum_{d\le x}{1\over\sqrt d}
  \sum_{n\le x/d}{\mu(n)\over\sqrt n}
   \left(4\sqrt{x/(dn)}-3\right)\\
&=\sum_{m\le x}{1\over\sqrt m}
  \left(\sum_{n\mid m}\mu(n)\right)
   \left(4\sqrt{x/m}-3\right).
\end{aligned}
\]

Since

\[
\sum_{n\mid m}\mu(n)=\mathbf1_{m=1},
\]

all composite hyperbola fibers cancel and one obtains

\[
\boxed{
 \sum_{d\le x}{1\over\sqrt d}\Psi(x/d)
 =4\sqrt x-3.
}
\tag{L-32312.5}
\]

Equivalently,

\[
\boxed{
 \Psi(x)
 =4\sqrt x-3
  -\sum_{2\le d\le x}{1\over\sqrt d}\Psi(x/d).
}
\tag{L-32312.6}
\]

The forcing is strictly positive for every `x>=1`, and every delayed argument `x/d` is at most `x/2`. Thus `Psi` is the exact causal hyperbola inverse of one positive forcing under one positive renewal operator.

This identity is not a positivity theorem: the total delayed coefficient mass is not a contraction, and taking absolute values would destroy the Möbius cancellation that produced (L-32312.5).

## 4. First Abel identity

Partial summation of

\[
 B(x)=\sum_{n\le x}{1\over\sqrt n}\,{\mu(n)\over\sqrt n}
\]

against the prefix `A` gives

\[
\boxed{
 B(x)
 ={A(x)\over\sqrt x}
 +{1\over2}\int_1^x A(t)t^{-3/2}\,dt.
}
\tag{L-32312.7}
\]

Substitution into (L-32312.1) yields

\[
\boxed{
 \Psi(x)
 =A(x)
  +2\sqrt x\int_1^x A(t)t^{-3/2}\,dt.
}
\tag{L-32312.8}
\]

Thus the all-depth scalar is one boundary value of the half-weighted Mertens sum plus a positive Green average of its entire history.

## 5. Second Abel identity

Conversely, treat

\[
 A(x)=\sum_{n\le x}\sqrt n\,{\mu(n)\over n}
\]

by partial summation against `B`. One obtains

\[
\boxed{
 A(x)
 =\sqrt x\,B(x)
 -{1\over2}\int_1^x B(t)t^{-1/2}\,dt.
}
\tag{L-32312.9}
\]

Hence

\[
\boxed{
 \Psi(x)
 =\sqrt x\,B(x)
  +{3\over2}\int_1^x B(t)t^{-1/2}\,dt.
}
\tag{L-32312.10}
\]

Equations (L-32312.8) and (L-32312.10) are exact Stieltjes/Abel identities with the standard right-continuous prefix convention.

## 6. Jump and interval differential laws

On an open interval

\[
 N<x<N+1,
\]

both `A(x)=A_N` and `B(x)=B_N` are constant. Thus

\[
\boxed{
 \Psi(x)=4B_N\sqrt x-3A_N
}
\tag{L-32312.11}
\]

and

\[
\boxed{
 \Psi'(x)={2B_N\over\sqrt x}.
}
\tag{L-32312.12}
\]

Consequently every smooth interval obeys the universal ODE

\[
\boxed{
 2x\Psi''(x)+\Psi'(x)=0.
}
\tag{L-32312.13}
\]

At an integer `N`, the right-continuous jump is

\[
\begin{aligned}
\Delta\Psi(N)
&=4\sqrt N\,{\mu(N)\over N}
 -3{\mu(N)\over\sqrt N}\\
&=\boxed{{\mu(N)\over\sqrt N}.}
\end{aligned}
\tag{L-32312.14}
\]

The slope coordinate has the jump

\[
\boxed{
 \Delta\bigl(\sqrt x\,\Psi'(x)\bigr)\big|_{x=N}
 ={2\mu(N)\over N}.
}
\tag{L-32312.15}
\]

Thus the entire continuum scalar is a piecewise square-root Green trajectory driven by explicit decreasing Möbius impulses.

## 7. Reconstruction of the two weighted Möbius prefixes

Away from integers, equations (L-32312.11)--(L-32312.12) can be inverted:

\[
\boxed{
 B(x)={\sqrt x\over2}\Psi'(x),
}
\tag{L-32312.16}
\]

and

\[
\boxed{
 A(x)={2x\Psi'(x)-\Psi(x)\over3}.
}
\tag{L-32312.17}
\]

Hence no information has been discarded by passing from `(A,B)` to `Psi`: the continuum margin is a complete scalar state for these two weighted Möbius prefixes between source impulses.

## 8. Consequence for the proof search

The all-depth SHARP frontier can now be attacked in either of two exact forms:

```text
positive-renewal form:
    P Psi = 4 sqrt(x)-3;

impulse/Green form:
    2x Psi''+Psi'=0 between integers,
    Delta Psi(N)=mu(N)/sqrt(N),
    Delta(sqrt(x)Psi')=2mu(N)/N.
```

A successful sign proof must exploit the special coupled sizes of these two Möbius impulses or a monotone Lyapunov functional for the positive renewal. A generic renewal-contraction argument is impossible because the positive delay mass is larger than one; a componentwise Stieltjes proof is already refuted by `R-32403`.

This replaces arbitrary-depth quotient-cell bookkeeping by one explicit causal dynamical system. It does not prove its one-sidedness.

## 9. Proof boundary

Closed exactly here:

1. positive Green-kernel representation;
2. exact positive renewal identity and recurrence;
3. both Abel representations;
4. interval ODE;
5. exact Möbius jump and slope-jump laws;
6. reconstruction of `A,B` from `Psi` between jumps.

Still open:

1. eventual one-sidedness of `Psi`;
2. full SHARP;
3. RH.
