# L-90422 — Ordinary-prime factor-16 normal form for the PIG mean

Claim ID: `L-90422`  
Title: The factor-four annularized compact-Q4 mean is, up to an explicit logarithmic four-adic term, a five-scale ordinary von-Mangoldt scalar supported on `[X/16,X]` with a zero-safe completely factored Mellin polynomial  
Status: **PROPOSED COMPLETE EXACT RH-EQUIVALENT REDUCTION — INDEPENDENT REVIEW REQUIRED; RH UNPROVED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: `L-90421`; exact compact coefficient formula of `L-90412`  
Scope: one ordinary-prime-power scalar; no unconditional critical-growth estimate

## 1. Ordinary triangular Chebyshev mean

Define

\[
 H(X)=\sum_{n\le X}\Lambda(n)
 \left(\frac{2n}{X}-1\right),
 \qquad X\ge1,
\tag{L-90422.1}
\]

and extend `H(X)=0` for `0<X<1`.

The compact-Q4 prefix coefficient is

\[
 c_\circ
 =\Lambda-D_4\Lambda+a_4,
\]

where

\[
 (D_4\Lambda)(m)=4\mathbf1_{4\mid m}\Lambda(m/4)
\]

and

\[
 a_4(m)=3(\log4)\sum_{r\ge1}\mathbf1_{m=4^r}.
\]

Let

\[
 A_4^{\rm at}(X)
 =\sum_{m\le X}a_4(m)
  \left(\frac{2m}{X}-1\right).
\]

Changing variables `m=4n` gives exactly

\[
 \boxed{
 M_\circ(X)=H(X)-4H(X/4)+A_4^{\rm at}(X).
 }
\tag{L-90422.2}

Moreover

\[
 \boxed{|A_4^{\rm at}(X)|\ll1+\log X.}
\tag{L-90422.3}

## 2. Five-scale ordinary prime scalar

Apply the factor-four annular operator of `L-90421`:

\[
 \mathcal A_4(X)
 =2M_\circ(X)-3M_\circ(X/2)+M_\circ(X/4).
\]

Substitution of (L-90422.2) gives

\[
 \boxed{
 \mathcal A_4(X)
 =\mathcal B_{16}(X)
  +\mathcal A_4^{\rm loc}(X),
 }
\tag{L-90422.4]

where the closing square bracket in the tag is typographical only,

\[
 \boxed{
 \begin{aligned}
 \mathcal B_{16}(X)
 ={}&2H(X)-3H(X/2)-7H(X/4)\\
 &+12H(X/8)-4H(X/16),
 \end{aligned}}
\tag{L-90422.5}

and

\[
 \mathcal A_4^{\rm loc}(X)
 =2A_4^{\rm at}(X)
 -3A_4^{\rm at}(X/2)
 +A_4^{\rm at}(X/4)
\]

satisfies

\[
 \boxed{\mathcal A_4^{\rm loc}(X)=O(1+\log X).}
\tag{L-90422.6}

Thus all RH-sensitive arithmetic in the annular PIG mean is carried by the ordinary von-Mangoldt scalar `B_16`.

## 3. Exact support on `[X/16,X]`

Put

\[
 Q(y)=2-3y-7y^2+12y^3-4y^4.
\tag{L-90422.7}

The two affine cancellation identities are

\[
 Q(1)=0,
 \qquad
 2-6-28+96-64=0.
\tag{L-90422.8}

Equivalently, when `m<=X/16`, the coefficient of `Lambda(m)` in (L-90422.5) is zero. Hence

\[
 \boxed{
 \mathcal B_{16}(X)
 \text{ is supported exactly on }
 X/16<m\le X.
 }
\tag{L-90422.9]

Its piecewise-linear kernel is

\[
 \boxed{
 \mathcal B_{16}(X)
 =\sum_{X/16<m\le X}\Lambda(m)K_{16}(m/X),
 }
\tag{L-90422.10}

where, away from the threshold conventions,

\[
 K_{16}(t)=
 \begin{cases}
 128t-4,&1/16<t\le1/8,\\
 8-64t,&1/8<t\le1/4,\\
 1-8t,&1/4<t\le1/2,\\
 4t-2,&1/2<t\le1.
 \end{cases}
\tag{L-90422.11}

At a dyadic threshold the term whose cutoff includes equality is retained; formula (L-90422.5) is the canonical exact convention.

## 4. Completely factored Mellin polynomial

The polynomial factors exactly as

\[
 \boxed{
 Q(y)
 =(1-y)(2-y)(1-2y)(1+2y).
 }
\tag{L-90422.12}

Since

\[
 \int_1^\infty H(X)X^{-z-1}dX
 =\frac{z-1}{z(z+1)}
  \left(-\frac{\zeta'}{\zeta}(z)\right),
\]

we obtain

\[
 \boxed{
 \begin{aligned}
 \int_1^\infty\mathcal B_{16}(X)X^{-z-1}dX
 ={}&Q(2^{-z})
 \frac{z-1}{z(z+1)}\\
 &\times\left(-\frac{\zeta'}{\zeta}(z)\right).
 \end{aligned}}
\tag{L-90422.13}

The four roots of `Q(2^-z)` lie on

\[
 \Re z\in\{-1,0,1\}.
\]

Therefore

\[
 \boxed{Q(2^{-\rho})\ne0}
\tag{L-90422.14}

for every nontrivial zeta zero with `0<Re rho<1`. Every open-strip zero survives.

The roots on `Re z=1` remove the deterministic pole/critical affine modes; they do not cancel a nontrivial zero.

## 5. Direct RH equivalence

Under RH, von Koch's estimate gives

\[
 \mathcal B_{16}(X)
 \ll\sqrt X\log^2(2X).
\tag{L-90422.15}

Conversely, if for every `epsilon>0`,

\[
 \mathcal B_{16}(X)
 =O_\epsilon(X^{1/2+\epsilon}),
\tag{L-90422.16}

then (L-90422.13)--(L-90422.14) exclude every zeta zero with real part above `1/2`. The functional equation gives RH. Hence

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathcal B_{16}(X)
 =O_\epsilon(X^{1/2+\epsilon})
 \text{ for every }\epsilon>0.
 }
\tag{L-90422.17}

## 6. Significance

The sole PIG mean obstruction now has a completely ordinary-prime-power presentation:

```text
five endpoint scales;
fixed annulus [X/16,X];
piecewise-linear kernel;
fully factored zero-safe Mellin polynomial;
only O(log X) difference from the compact-source annulus.
```

This is a cleaner target for the endpoint, annular, or explicit-formula programmes than the original generalized-prime source. It remains RH-equivalent and is not proved unconditionally here.

## 7. Proof boundary

Closed exactly:

1. compact mean = ordinary mean minus its quarter-scale copy plus local atoms;
2. five-scale coefficient vector `(2,-3,-7,12,-4)`;
3. support on `[X/16,X]`;
4. explicit four-band kernel;
5. complete factorization of the Mellin polynomial;
6. open-strip zero safety;
7. critical-growth equivalence to RH.

Open:

1. an unconditional critical-growth estimate for `B_16`;
2. RH.
