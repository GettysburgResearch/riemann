# L-90009 — The prime-power moat removes every original zeta-zero pole

Claim ID: `L-90009` (provisional range; allocate before integration)  
Title: The prime-only endpoint is the classical full prime-power Riesz deficit plus an unconditionally negative zero-insensitive quadratic-log moat  
Status: **PROPOSED COMPLETE EXACT TRANSFORM / UNCONDITIONAL ASYMPTOTIC LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-09  
Depends on: `L-90004`; the classical zero-free line and Vinogradov--Korobov contour for zeta  
Scope: exact decomposition and deterministic moat; no unconditional sign theorem for the RH-sensitive endpoint

## 1. Two endpoint deficits

Retain the prime-only endpoint scalar of `L-90004`,

\[
 A(X)=J_{\mathbb P}(X)-P_{\mathbb P}(X),
\tag{L-90009.1}
\]

where

\[
 P_{\mathbb P}(X)
 =\sum_{p\le X}\frac{\log p}{\sqrt p}\log\frac Xp.
\]

Put

\[
 P_\Lambda(X)
 =\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}\log\frac Xn
\tag{L-90009.2}
\]

and define the complete prime-power Riesz deficit

\[
 \boxed{\Delta_\Lambda(X)=4\sqrt X-P_\Lambda(X).}
\tag{L-90009.3}
\]

The new object is the difference

\[
 \boxed{\mathfrak M(X)=A(X)-\Delta_\Lambda(X).}
\tag{L-90009.4}
\]

At finite level this is

\[
\boxed{
\mathfrak M(X)
=J_{\mathbb P}(X)
 +\sum_{\substack{p^k\le X\\k\ge2}}
  \frac{\log p}{p^{k/2}}\log\frac X{p^k}
 -4\sqrt X.
}
\tag{L-90009.5}
\]

Thus

\[
\boxed{A(X)=\Delta_\Lambda(X)+\mathfrak M(X)}
\tag{L-90009.6}
\]

is an exact identity, with no asymptotic or zero hypothesis.

The first summand contains the ordinary nontrivial-zero obstruction.  The point
of this lemma is that the second summand does not.

## 2. Exact transform

Use the notation of `L-90004`:

\[
 s=z+\frac12,\qquad
 \mathcal P_1(s)=\sum_p\frac{\log p}{p^s},
\]

\[
 \mathcal D(w)
 =\sum_p(\log p)\sum_{k\ge1}
   \bigl((kp)^{-w}-(kp+1)^{-w}\bigr),
\]

and

\[
 \widehat A(z)
 =\frac1{z^2}
  \left[\frac{\mathcal D(s-1)}s-\mathcal P_1(s)\right].
\tag{L-90009.7}
\]

For \(\Re s>1\),

\[
 -\frac{\zeta'}{\zeta}(s)
 =\sum_{m\ge1}\mathcal P_1(ms).
\tag{L-90009.8}
\]

The complete deficit has transform

\[
\boxed{
 \widehat{\Delta_\Lambda}(z)
 =\frac4{z-\frac12}
  +\frac1{z^2}\frac{\zeta'}{\zeta}(s).
}
\tag{L-90009.9}
\]

Subtracting (L-90009.9) from (L-90009.7), and using (L-90009.8), gives

\[
\boxed{
\widehat{\mathfrak M}(z)
=
\frac1{z^2}
\left[
 \frac{\mathcal D(s-1)}s
 +\sum_{m\ge2}\mathcal P_1(ms)
\right]
-\frac4{z-\frac12}.
}
\tag{L-90009.10}
\]

This is initially an absolutely convergent identity in a right half-plane and
then a meromorphic-continuation identity.

## 3. Every original nontrivial-zero pole cancels

Let \(\rho\) be a nontrivial zero with \(\Re\rho\ge1/2\), and put
\(z_\rho=\rho-1/2\).

`L-90004` proves

\[
 \operatorname*{Res}_{z=z_\rho}\widehat A(z)
 =\frac{m_\rho}{z_\rho^2}.
\tag{L-90009.11}
\]

The same residue occurs in (L-90009.9), because
\(\zeta'/\zeta\) has residue \(m_\rho\) at \(\rho\).  Hence

\[
\boxed{
 \operatorname*{Res}_{z=z_\rho}
 \widehat{\mathfrak M}(z)=0.
}
\tag{L-90009.12}
\]

The cancellation can also be read directly from (L-90009.10).  In the
\(r=1\) term of the shifted-difference expansion,

\[
 \mathcal D(s-1)
 =(s-1)\zeta(s)\mathcal P_1(s)+\mathcal H(s-1),
\]

the product \(\zeta(s)\mathcal P_1(s)\) is regular at every zero of zeta,
including multiple zeros.  The remaining prime-zeta terms have arguments
\(ms\), \(m\ge2\); when \(\Re s\ge1/2\), those arguments lie on or to the
right of the classical zero-free line \(\Re(ms)=1\), and no original zero pole
is reintroduced.

Thus \(\widehat{\mathfrak M}\) is holomorphic on the open right half-plane
apart from the removable main-pole bookkeeping already displayed, and it has
no nonzero singularity on the imaginary axis.  All movable zero singularities
which remain are scaled copies

\[
 z=\frac{\rho}{m}-\frac12,\qquad m\ge2,
\tag{L-90009.13}
\]

and lie strictly to the left of that axis.

## 4. The origin pole and its sign

The complete deficit transform (L-90009.9) has at most an order-two pole at
\(z=0\), because \(\zeta(1/2)\ne0\).  Therefore the order-three pole found in
`L-90004` survives unchanged in the moat:

\[
\boxed{
 \widehat{\mathfrak M}(z)
 =
 \frac{1+\zeta(1/2)}{2z^3}
 +\frac{\mu_1}{z^2}
 +\frac{\mu_0}{z}
 +O(1).
}
\tag{L-90009.14}
\]

The leading physical term is

\[
\boxed{
 c_2\log^2X,\qquad
 c_2=\frac{1+\zeta(1/2)}4
 =-0.1150886272023967032223747881\ldots<0.
}
\tag{L-90009.15}
\]

This is the same prime-square pole isolated in `L-90004`, now separated from
every original zeta-zero pole.

## 5. Unconditional moat asymptotic

After subtracting the three origin principal parts in (L-90009.14), shift the
Mellin contour along the standard Vinogradov--Korobov zero-free contour.

The only movable singularities near the new contour are the \(m=2\) copies

\[
 z=\frac{\rho-1}{2},
\]

so their distance from the imaginary axis is one half of the classical
zero-free distance from \(\Re s=1\).  The \(m\ge3\) main-pole copies begin at
\(z=-1/6\), and every remaining term in the normally convergent
prime-zeta/shifted-difference expansions is farther left.  The factor \(z^{-2}\)
supplies the required Riesz decay on horizontal segments.

On this contour, the standard bounds

```text
zeta'/zeta = O(log^2(|t|+3)),
P_1(ms) normally convergent for m>=3,
zeta(s)P_1(s)=-zeta'(s)+a normally convergent tail
```

supply polynomial vertical growth after the principal parts have been removed.
The usual height optimization in the truncated Mellin integral therefore gives
real constants \(\mu_1,\mu_0\) and positive constants \(c,C\) such that

\[
\boxed{
\begin{aligned}
 \mathfrak M(X)
 ={}&c_2\log^2X+\mu_1\log X+\mu_0\\
 &+O\!\left(
 (1+\log X)^C
 \exp\!\left[
 -c(\log X)^{3/5}(\log\log(3X))^{-1/5}
 \right]\right).
\end{aligned}
}
\tag{L-90009.16}
\]

No RH input occurs.  In particular,

\[
\boxed{
 \mathfrak M(X)
 =\frac{1+\zeta(1/2)}4\log^2X+O(\log X)<0
}
\tag{L-90009.17}
\]

for all sufficiently large \(X\).

This is an unconditional negative **prime-power moat**.  The RH-sensitive
quantity \(A\) is obtained by placing the complete prime-power deficit
\(\Delta_\Lambda\) inside that moat.

## 6. Logarithmic derivative

Let

\[
 \mathcal D_X=X\frac{d}{dX}
\]

at noninteger endpoints.  Multiplying (L-90009.10) by \(z\), or
differentiating the same contour expansion, gives

\[
\boxed{
 \mathcal D_X\mathfrak M(X)
 =
 \frac{1+\zeta(1/2)}2\log X+\mu_1+o(1).
}
\tag{L-90009.18}
\]

Hence the moat is itself strictly decreasing eventually, unconditionally.

There is also an exact finite identity.  Since

\[
 \mathcal D_X\Delta_\Lambda(X)
 =2\sqrt X-\psi_{1/2}(X),
\qquad
 \psi_{1/2}(X)=\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n},
\]

equation (L-90009.6) gives

\[
\boxed{
 \mathcal D_X\mathfrak M(X)
 =
 \mathcal D_X A(X)
 +\psi_{1/2}(X)-2\sqrt X.
}
\tag{L-90009.19}
\]

Equivalently,

\[
\boxed{
 \mathcal D_X A(X)
 =
 \mathcal D_X\mathfrak M(X)
 -\bigl(\psi_{1/2}(X)-2\sqrt X\bigr).
}
\tag{L-90009.20}
\]

All original zero sensitivity of the endpoint derivative is therefore confined
to the familiar weighted Chebyshev fluctuation.

## 7. Deterministic upper wall for the classical deficit

Put

\[
 \mathcal Q(X)=-\mathfrak M(X).
\]

Cofinally, \(\mathcal Q(X)>0\), and

\[
\boxed{
 \mathcal Q(X)
 =
 -\frac{1+\zeta(1/2)}4\log^2X+O(\log X).
}
\tag{L-90009.21}
\]

The exact decomposition becomes

\[
\boxed{
 A(X)<0
 \iff
 \Delta_\Lambda(X)<\mathcal Q(X).
}
\tag{L-90009.22}
\]

Thus `T-90008` can be read as an RH-equivalent **upper-wall theorem** for the
classical full prime-power Riesz deficit.  The wall itself is deterministic,
unconditionally positive, and free of every original zeta-zero pole.

In the terminology of Suzuki's weighted-Chebyshev criterion, RH also gives the
opposite eventual inequality \(\Delta_\Lambda(X)\ge0\).  Hence, under RH, the
complete deficit eventually lies in the explicit corridor

\[
\boxed{
 0\le\Delta_\Lambda(X)<\mathcal Q(X).
}
\tag{L-90009.23}
\]

The upper wall alone is already RH-equivalent by (L-90009.22) and `T-90008`;
the lower wall is the classical weighted-Chebyshev sign criterion.

## 8. Proof boundary

Closed here, subject to independent review:

1. the exact finite decomposition \(A=\Delta_\Lambda+\mathfrak M\);
2. the exact moat transform;
3. cancellation of every original nontrivial-zero pole;
4. isolation of all remaining singularities in the open left half-plane;
5. the negative quadratic-log Laurent coefficient;
6. the unconditional zero-free-contour asymptotic;
7. eventual unconditional negativity and decrease of the moat;
8. the exact weighted-Chebyshev derivative identity;
9. the deterministic upper-wall formulation.

Still open:

1. the upper-wall inequality
   \(\Delta_\Lambda<\mathcal Q\) unconditionally;
2. eventual negativity or monotonicity of \(A\);
3. RH.
