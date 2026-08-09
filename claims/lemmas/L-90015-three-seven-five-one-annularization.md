# L-90015 — The 3–7–5–1 filter annularizes the prime endpoint exactly

Claim ID: `L-90015` (provisional range; branch-qualified)  
Title: A four-scale radix-nine filter kills both interior seed modes and the ramp modes, leaving a fixed factor-729 annulus and one explicit negative prime-power moat  
Status: **PROPOSED COMPLETE EXACT FINITE/TRANSFORM LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-10  
Depends on: `L-90004`, `L-90009`  
Scope: exact annularization and pole bookkeeping; no unconditional sign of the filtered endpoint

## 1. The filtered endpoint

Retain the prime endpoint scalar

\[
 A(X)=J_{\mathbb P}(X)-P_{\mathbb P}(X)
\]

of `L-90004`. Define

\[
\boxed{
 \mathcal U_9(X)
 =3A(X)-7A(X/9)+5A(X/81)-A(X/729).
}
\tag{L-90015.1}
\]

The coefficient polynomial is

\[
\boxed{
 Q(y)=3-7y+5y^2-y^3=(1-y)^2(3-y).
}
\tag{L-90015.2}
\]

Its three cancellation moments are

\[
 3-7+5-1=0,
\tag{L-90015.3}
\]

\[
 -7+2\cdot5-3=0,
\tag{L-90015.4}
\]

and

\[
 3-7\cdot3+5\cdot9-27=0.
\tag{L-90015.5}
\]

They respectively kill the constant/logarithmic scale mode, its first logarithmic moment, and the critical `X^{-1/2}` seed mode.

## 2. Exact factor-729 annular support

Put

\[
 X_j=X/9^j,
 \qquad
 (a_0,a_1,a_2,a_3)=(3,-7,5,-1).
\]

For every integer `m<=X/729`, all four zero-extended seed terms are active and

\[
 b_{X_j}(m)
 =2\sqrt m\left(\log{X\over m}-j\log9-2\right)
 +{4m\,3^j\over\sqrt X}.
\tag{L-90015.6}
\]

Consequently (L-90015.3)--(L-90015.5) give

\[
\boxed{
 \sum_{j=0}^3a_j b_{X_j}(m)=0
 \qquad(m\le X/729).
}
\tag{L-90015.7}
\]

Likewise, for every prime `p<=X/729`,

\[
 w_{X_j}(p)=p^{-1/2}\left(\log{X\over p}-j\log9\right),
\]

so (L-90015.3)--(L-90015.4) give

\[
\boxed{
 \sum_{j=0}^3a_j w_{X_j}(p)=0
 \qquad(p\le X/729).
}
\tag{L-90015.8}
\]

Use the radical switching of `L-90004`,

\[
 d(m)=\log\operatorname{rad}(m)-\log\operatorname{rad}(m-1).
\]

Define

\[
 \beta_{9,X}(m)=\sum_{j=0}^3a_jb_{X_j}(m),
 \qquad
 \omega_{9,X}(p)=\sum_{j=0}^3a_jw_{X_j}(p).
\]

Then exactly

\[
\boxed{
\begin{aligned}
 \mathcal U_9(X)
 ={}&\sum_{X/729<m\le X}\beta_{9,X}(m)d(m)\\
 &-\sum_{X/729<p\le X}(\log p)\omega_{9,X}(p).
\end{aligned}}
\tag{L-90015.9}
\]

Thus the criterion uses a fixed multiplicative annulus in the radical-switching coordinate. Small primes may still occur as factors of annular integers; no claim of large-prime-only support is made.

At endpoints `X=729N`, every scale is integral and (L-90015.9) is a completely finite identity on `[N,729N]`:

\[
\boxed{
 \mathcal U_9(729N)=3A_{729N}-7A_{81N}+5A_{9N}-A_N.
}
\tag{L-90015.10}
\]

## 3. Exact Mellin multiplier

Scaling in the Mellin integral gives

\[
\boxed{
 \widehat{\mathcal U_9}(z)
 =Q(9^{-z})\widehat A(z)
 =(1-9^{-z})^2(3-9^{-z})\widehat A(z).
}
\tag{L-90015.11}
\]

At a hypothetical off-line zero

\[
 z_\rho=\rho-\frac12,
 \qquad \Re z_\rho>0,
\]

one has `|9^{-z_rho}|<1`. The only roots of `Q(y)` are `y=1` and `y=3`, so

\[
\boxed{Q(9^{-z_\rho})\ne0.}
\tag{L-90015.12}
\]

Hence every off-line zero survives with residue

\[
\boxed{
 \operatorname*{Res}_{z=z_\rho}
 \widehat{\mathcal U_9}(z)
 =
 {m_\rho Q(9^{-z_\rho})\over z_\rho^2}\ne0.
}
\tag{L-90015.13}
\]

The filter also has no positive-real pole of its own. Therefore it preserves the Landau converse while removing the entire deep interior of the finite arithmetic sum.

## 4. The filtered prime-power moat

Use the exact decomposition of `L-90009`,

\[
 A(X)=\Delta_\Lambda(X)+\mathfrak M(X),
\]

where

\[
 \mathfrak M(X)
 ={1+\zeta(1/2)\over4}\log^2X
 +\mu_1\log X+\mu_0
 +O_\eta(X^{-\eta}\log^B(2X))
\]

for every fixed `0<eta<1/6`.

Put

\[
 \mathcal M_9(X)
 =3\mathfrak M(X)-7\mathfrak M(X/9)
 +5\mathfrak M(X/81)-\mathfrak M(X/729).
\]

The double root `Q(1)=Q'(1)=0` kills the linear and constant terms. Since

\[
 \sum_{j=0}^3j^2a_j=4,
\]

the quadratic term gives

\[
\boxed{
 \mathcal M_9(X)
 =(1+\zeta(1/2))(\log9)^2
 +O_\eta(X^{-\eta}\log^B(2X)).
}
\tag{L-90015.14}
\]

The limiting moat is the explicit negative constant

\[
\boxed{
 C_9=(1+\zeta(1/2))(\log9)^2
 =-2.22249758405246967649\ldots .
}
\tag{L-90015.15}
\]

Thus

\[
\boxed{
 \mathcal U_9(X)
 =\mathcal C_9(X)+\mathcal M_9(X),
}
\tag{L-90015.16}
\]

where

\[
 \mathcal C_9(X)
 =3\Delta_\Lambda(X)-7\Delta_\Lambda(X/9)
 +5\Delta_\Lambda(X/81)-\Delta_\Lambda(X/729)
\]

contains the surviving original zero response, while `M_9` is zero-insensitive and converges unconditionally to `C_9<0`.

## 5. Why this is a genuine new coordinate

The previous minimal criterion `A(X)<0` is global in the radical coordinate and has a growing negative `log^2 X` moat. The present filter exchanges growth for localization:

```text
unfiltered endpoint:
    global arithmetic support;
    negative moat of order log^2 X;

3-7-5-1 endpoint:
    exact factor-729 annular support;
    fixed negative moat C_9;
    every off-line zero retained.
```

This is not a proof of the annular sign. It supplies a compact, scale-stationary target whose deterministic margin and zero response are both explicit.

## 6. Proof boundary

Closed exactly, subject to review:

1. the polynomial factorization and three moments;
2. cancellation of every seed and ramp term below `X/729`;
3. the finite radical-annular identity;
4. the Mellin multiplier;
5. noncancellation of every off-line zero;
6. the filtered prime-power-moat asymptotic and constant.

Still open:

1. unconditional eventual sign of `U_9`;
2. an arithmetic proof that the annular zero-sensitive coordinate fits inside the fixed moat;
3. RH.

Replay: `experiments/X-90015-annular-endpoint/verify.py`.
