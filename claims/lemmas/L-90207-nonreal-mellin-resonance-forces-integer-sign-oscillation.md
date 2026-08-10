# L-90207 — A nonreal Mellin resonance with vanishing interpolation error forces integer sign oscillation

Claim ID: `L-90207`  
Status: **PROPOSED COMPLETE ANALYTIC LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: the standard Landau theorem for eventually one-signed Mellin/Laplace sources already used in `T-90001`; elementary Mellin calculus  
Scope: a reusable real-to-integer sign-transfer theorem; no arithmetic input and no RH conclusion

## 1. Setup

Let `F:[1,infinity)->R` have polynomial growth and suppose its Mellin transform

\[
 \widehat F(s)=\int_1^\infty F(X)X^{-s-1}\,dX
 \tag{L-90207.1}
\]

is initially defined in a right half-plane. Assume it has a meromorphic continuation to

\[
 \Re s>0
 \tag{L-90207.2}
\]

which is holomorphic at every positive real point.

Suppose there is a nonreal point

\[
 s_0=\beta+i\gamma,
 \qquad \beta>0,\quad\gamma\ne0,
 \tag{L-90207.3}
\]

at which the continued transform is singular.

Finally suppose that for all sufficiently large real `X`, with `N=floor X`,

\[
 \boxed{
 |F(X)-F(N)|
 \le C\frac{1+\log X}{\sqrt X}.
 }
 \tag{L-90207.4}
\]

## 2. Theorem — integer eventual sign is impossible

Under these assumptions, neither integer sequence inequality

\[
 F(N)\ge0\quad(N\gg1)
 \tag{L-90207.5}
\]

nor

\[
 F(N)\le0\quad(N\gg1)
 \tag{L-90207.6}
\]

can hold. Consequently `F(N)` takes both positive and negative values for arbitrarily large integers `N`.

### Proof

Assume first (L-90207.5). Put

\[
 E(X)=C\frac{1+\log X}{\sqrt X}.
 \tag{L-90207.7}
\]

By (L-90207.4),

\[
 F(X)+E(X)\ge0
 \qquad(X\gg1).
 \tag{L-90207.8}
\]

The Mellin transform of the correction is explicit:

\[
 \boxed{
 \widehat E(s)
 =C\left[
 {1\over s+1/2}+{1\over(s+1/2)^2}
 \right],
 }
 \tag{L-90207.9}
\]

which is holomorphic throughout `Re s>0`, including at `s_0`. Therefore

\[
 \widehat{F+E}(s)=\widehat F(s)+\widehat E(s)
 \tag{L-90207.10}
\]

still has the nonreal singularity `s_0` and is still holomorphic at every positive real point.

Let `sigma_c` be the abscissa of convergence of the eventually nonnegative tail in (L-90207.8). Polynomial growth makes it finite. The singularity at `s_0` forces

\[
 \sigma_c\ge\beta>0;
 \tag{L-90207.11}
\]

otherwise the defining Mellin integral would be analytic in a half-plane containing `s_0`. Landau's theorem for eventually nonnegative Mellin sources then forces the positive real point `s=sigma_c` to be singular. This contradicts the assumed positive-real holomorphy.

The case (L-90207.6) is identical after replacing `F` by `-F`. Thus neither eventual integer sign is possible. ∎

## 3. Interpolation bound for transported fragmentation traces

Let `a(m)` be a real sequence satisfying

\[
 |a(m)|\le A_0,
 \tag{L-90207.12}
\]

and define the Möbius-transported critical trace

\[
 \boxed{
 F(X)=
 \sum_{\substack{m,k\ge1\\k\ {\rm squarefree}\\mk\le X}}
 a(m)\mu(k)(mk)^{-1/2}\log\frac X{mk}.
 }
 \tag{L-90207.13}
\]

For `N<=X<N+1`, no new positive-weight integer product activates. Terms with `mk=N` have zero weight at `X=N`, so exactly

\[
 F(X)-F(N)
 =\log\frac XN
 \sum_{mk\le N\atop k\ {\rm squarefree}}
 {a(m)\mu(k)\over\sqrt{mk}}.
 \tag{L-90207.14}
\]

Using

\[
 \sum_{k\le y}k^{-1/2}\le2\sqrt y,
 \qquad
 \sum_{m\le N}{1\over m}\le1+\log N,
\]

we obtain

\[
 \left|
 \sum_{mk\le N}{a(m)\mu(k)\over\sqrt{mk}}
 \right|
 \le2A_0\sqrt N(1+\log N).
 \tag{L-90207.15}
\]

Since `log(X/N)<=1/N` and `N>=X/2` for `X>=2`,

\[
 \boxed{
 |F(X)-F(N)|
 \le4A_0{1+\log X\over\sqrt X}.
 }
 \tag{L-90207.16}
\]

The same estimate, without subtracting adjacent endpoints, gives the polynomial bound

\[
 |F(X)|
 \le 2A_0\sqrt X(1+\log X)\log X
 =O(\sqrt X\log^2X),
 \tag{L-90207.17}
\]

so the finite-abscissa hypothesis used in the Landau argument is automatic.
Thus every bounded-increment fragmentation trace of `L-90205` satisfies all hypotheses of the integer-transfer theorem once its continued transform has the stated singularity structure.

## 4. Proof boundary

Proved exactly:

- a general nonreal-resonance obstruction to eventual sign on integer endpoints;
- preservation of the obstruction after the explicit decaying interpolation correction;
- the uniform interpolation estimate (L-90207.16) for every bounded transported fragmentation increment.

Not proved here:

- existence of a nonreal pole for a particular trace;
- any statement about GFEP or RH without a separately certified resonance.
