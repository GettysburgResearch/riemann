# L-90206 — The binary–ternary fragmentation characteristic has no spectral gap

Claim ID: `L-90206`  
Status: **PROPOSED COMPLETE EXACT ANALYTIC LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: characteristic function `Delta` of `L-90205`; elementary Diophantine approximation and Rouché's theorem  
Scope: deterministic renewal spectrum; no assertion that every characteristic zero survives in every boundary trace and no RH conclusion

## 1. Characteristic function

Retain

\[
 \boxed{
 \Delta(u)
 =1-\frac12\left[
 2^{1-u}+3^{-u}+(3/2)^{-u}
 \right].
 }
 \tag{L-90206.1}
\]

`L-90205` proves

\[
 \Delta(u)\ne0\qquad(\Re u>1),
 \tag{L-90206.2}
\]

while `Delta(1)=0` is the size-conservation root.

This lemma proves that the line `Re u=1` cannot be separated from the remaining characteristic spectrum by any fixed positive strip.

## 2. The conservation line has no other zero

Put

\[
 a=\log2,
 \qquad b=\log3.
\]

At `u=1+it`,

\[
 1-\Delta(1+it)
 =\frac12\left[
 e^{-ita}+\frac13e^{-itb}
 +\frac23e^{-it(b-a)}
 \right].
 \tag{L-90206.3}
\]

The three coefficients on the right have positive masses

\[
 1,\quad1/3,\quad2/3
\]

summing to two. If `Delta(1+it)=0`, their weighted sum equals the positive real number two. Equality in the triangle inequality forces all three phases to equal one. In particular,

\[
 ta\in2\pi\mathbb Z,
 \qquad
 tb\in2\pi\mathbb Z.
\]

But `a/b=log2/log3` is irrational: a rational relation would imply `2^r=3^s` for nonzero integers. Therefore

\[
 \boxed{
 \Delta(1+it)=0\Longrightarrow t=0.
 }
 \tag{L-90206.4}
\]

So every nonreal characteristic zero lies strictly to the left of the conservation line.

## 3. Almost periods on the conservation line

By Dirichlet's approximation theorem applied to the irrational number `b/a`, there exist integers

\[
 q_j\to\infty,
 \qquad p_j\in\mathbb Z
\]

such that

\[
 \left|q_j\frac ba-p_j\right|\longrightarrow0.
 \tag{L-90206.5}
\]

Set

\[
 t_j=\frac{2\pi q_j}{a}.
 \tag{L-90206.6}
\]

Then exactly

\[
 e^{-it_ja}=1,
\]

and (L-90206.5) gives

\[
 e^{-it_jb}\to1,
 \qquad
 e^{-it_j(b-a)}\to1.
\]

Consequently

\[
 \boxed{
 \Delta(1+it_j)\to0.
 }
 \tag{L-90206.7}
\]

Moreover differentiation of (L-90206.1) gives

\[
 \Delta'(1+it_j)\to\Delta'(1)>0.
 \tag{L-90206.8}
\]

The second derivative is uniformly bounded on every fixed-radius disk about the points `1+it_j`, because `Delta` is a finite exponential polynomial and the real parts remain in a fixed compact interval.

## 4. Nearby exact zeros

Let

\[
 z_j=1+it_j,
 \qquad
 \varepsilon_j=|\Delta(z_j)|\to0,
 \qquad
 d=\Delta'(1)>0.
\]

For large `j`,

\[
 |\Delta'(z_j)|\ge3d/4.
\]

Let `M` be a common bound for `|Delta''|` on the disks `|u-z_j|<=1`. Put

\[
 r_j=\frac{2\varepsilon_j}{|\Delta'(z_j)|}.
\]

Then `r_j->0`. On `|w|=r_j`, Taylor's theorem gives

\[
 \Delta(z_j+w)
 =\Delta(z_j)+\Delta'(z_j)w+E_j(w),
 \qquad
 |E_j(w)|\le\frac M2r_j^2.
\]

For all sufficiently large `j`,

\[
 |\Delta(z_j)+E_j(w)|
 <|\Delta'(z_j)w|.
\]

Rouché's theorem therefore shows that `Delta(z_j+w)` and the linear function `Delta'(z_j)w` have the same number of zeros in `|w|<r_j`, namely one. Thus there exists a characteristic zero `rho_j` with

\[
 \boxed{
 |\rho_j-(1+it_j)|\le r_j\longrightarrow0.
 }
 \tag{L-90206.9}
\]

By (L-90206.2) and (L-90206.4), for large `j` this nonreal zero satisfies

\[
 \Re\rho_j<1.
\]

Hence

\[
 \boxed{
 \Re\rho_j\longrightarrow1^{-},
 \qquad
 |\Im\rho_j|\longrightarrow\infty.
 }
 \tag{L-90206.10}
\]

This proves the no-spectral-gap theorem.

## 5. Consequence for deterministic fragmentation estimates

The increment renewal of `L-90205` has transfer denominator `Delta(u)`. Therefore no theorem based on a source-independent spectral gap of the frozen binary–ternary renewal can produce a uniform decay exponent

\[
 1-\Re u\ge\delta>0
\]

for all nonconservation modes: such a `delta` does not exist.

Equivalently, after the critical shift `s=u-1/2`, deterministic characteristic resonances occur with

\[
 \Re s\to1/2^{-}.
\]

This is an **information about the fragmentation geometry itself**, independent of Möbius signs or zeta zeros.

It explains two otherwise puzzling numerical features already present in the repository:

- pointwise first-entrance harmonic profiles are rough even at large scale;
- average renewal laws can be accurate while no fixed exponential rate controls the pointwise error.

## 6. Important scope boundary

A zero of `Delta` is only a **possible** pole of the continued fragmentation factor

\[
 \mathcal A(u)=N(u)/\Delta(u).
\]

A particular boundary trace may satisfy `N(rho_j)=0` and cancel a characteristic zero. This lemma does not assert that the zeros (L-90206.10) survive for every exit or for the sparse producer.

Accordingly, the theorem rules out a generic uniform spectral-contraction strategy but does not refute GFEP, producer positivity, or any source-specific cancellation theorem.

## 7. Proof boundary

Proved exactly:

- uniqueness of the characteristic zero on `Re u=1`;
- construction of arbitrarily accurate nonzero almost periods;
- nearby exact characteristic zeros by Rouché;
- characteristic zeros with real parts tending to one from below;
- absence of any source-independent fragmentation spectral gap.

Not proved:

- survival/noncancellation of those zeros for a particular boundary trace;
- any sign change of a GFEP or producer coordinate;
- RH or its negation.
