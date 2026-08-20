# L-100160 — Exact critical quadratic prefix/future-tail decomposition

Claim ID: `L-100160`  
Status: **PROVED EXACT FINITE/ABSOLUTELY-CONVERGENT IDENTITY**  
Created: 2026-08-20  
RH status: **not assumed**

Let

\[
\beta(n)=\mu(n)-\mathbf 1_{67\mid n}\mu(n/67),
\]

and let `C_2` be the critical quadratic remainder of `L-100001`:

\[
C_2(x)=16\mathcal B(3/2)x-H_2^U(x).
\]

Write

\[
A_\beta(x)=\sum_{n\le x}{\beta(n)\over n},\qquad
B_\beta(x)=\sum_{n\le x}{\beta(n)\over\sqrt n},
\]

and

\[
T_{3/2}(x)=\sum_{n>x}{\beta(n)\over n^{3/2}}.
\]

Using the exact Peano kernel

\[
\kappa_{2,1}(t)=\begin{cases}2t-t^2,&0<t\le1,\\1,&t\ge1,\end{cases}
\]

one obtains, by splitting at `n=x`,

\[
\boxed{
{C_2(x)\over16}
=2\sqrt x\,A_\beta(x)-B_\beta(x)+xT_{3/2}(x).
}
\tag{L-100160.1}
\]

Indeed the term with `n<=x` is

\[
16x{\beta(n)\over n^{3/2}}
\left(2\sqrt{n/x}-{n\over x}\right)
=32\sqrt x{\beta(n)\over n}-16{\beta(n)\over\sqrt n},
\]

while `n>x` contributes `16x beta(n)n^{-3/2}`.

## Activation cancellation

At an integer activation `x=N`, the prefix part

\[
2\sqrt x A_\beta(x)-B_\beta(x)
\]

jumps by

\[
2\sqrt N{\beta(N)\over N}-{\beta(N)\over\sqrt N}
={\beta(N)\over\sqrt N},
\]

whereas `x T_(3/2)(x)` jumps by exactly

\[
-N{\beta(N)\over N^{3/2}}
=-{\beta(N)\over\sqrt N}.
\]

Hence `C_2` is continuous across every activation.

Let `D=x d/dx`. Between activations the three prefix/tail functions are constant, so

\[
\boxed{
D\left({C_2\over16}\right)
=\sqrt x\,A_\beta(x)+xT_{3/2}(x).
}
\tag{L-100160.2}
\]

The activation jumps again cancel distributionally. Therefore (L-100160.2) holds globally in the absolutely-continuous/distributional sense.

Differentiating once more on cells gives the dual identities

\[
\boxed{
(D-\tfrac12)D\left({C_2\over16}\right)
={1\over2}xT_{3/2}(x),
}
\tag{L-100160.3}
\]

and

\[
\boxed{
(D-1)D\left({C_2\over16}\right)
=-{1\over2}\sqrt x\,A_\beta(x).
}
\tag{L-100160.4}
\]

Thus the critical positive quadratic envelope couples the live reciprocal prefix to an absolutely convergent future tail in one exact activation-free equation.

## Scope

This theorem does not sign either `A_beta` or `T_(3/2)`. It identifies a new exact interface: any critical closure may trade negative prefix excursions against the supercritical future tail without introducing an activation ledger. A source-blind PSD/self-reciprocal argument is insufficient and is recorded separately as a firewall.
