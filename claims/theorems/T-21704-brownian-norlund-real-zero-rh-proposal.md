# T-21704 — Direct Brownian Green–Robin real-zero proposal for RH

Claim ID: `T-21704`  
Title: A real-zero theorem for explicit Brownian random-walk Green approximants would prove the Riemann Hypothesis by Rouché  
Status: **FULL GLOBAL PROPOSAL — ONE SOURCE-SPECIFIC REAL-ZERO THEOREM OPEN**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Corrected and strengthened: 2026-08-08  
Dependencies: `L-21705`--`L-21708`; Rouché's theorem  
RH status: **UNPROVED**

## 1. Canonical producer

Retain the finite Brownian gamma sums

\[
S_K=\sum_{j=1}^K\frac{\Gamma_{2,j}}{j^2},
\qquad
m_K(s)=\pi^{-s/2}\mathbb E[S_K^{s/2}].
\tag{T-21704.1}
\]

Put

\[
\omega_K=\left(\frac{\binom{2K}{K}}{4^K}\right)^2,
\qquad
Z_N=\sum_{K=1}^N\omega_K,
\qquad
\lambda_{N,K}=\frac{\omega_K}{Z_N}.
\tag{T-21704.2}
\]

Define

\[
\boxed{
 m_N^{\rm G}(s)=\sum_{K=1}^N\lambda_{N,K}m_K(s),
 \qquad
 \mathcal C_N(s)=m_N^{\rm G}(s)+m_N^{\rm G}(1-s).}
\tag{T-21704.3}
\]

The weights are normalized return probabilities of a planar simple random walk. They are not fitted from zeta zeros.

`L-21707` proves the elementary lower bound

\[
\omega_K\ge\frac1{4K},
\qquad
Z_N\ge\frac14H_N,
\]

and consequently

\[
\boxed{
|\mathcal C_N(s)-4\xi(s)|
\le
\frac{4\zeta(2)}{H_N}
\bigl(|s|+|1-s|\bigr),
\qquad0\le\operatorname{Re}s\le1.}
\tag{T-21704.4}
\]

Thus `mathcal C_N` converges locally uniformly to `4 xi` throughout the critical strip.

The logarithmic Nörlund approximants of `L-21706` remain a closely related producer with the slightly sharper factor `zeta(2)/H_N`. The central-binomial producer is now preferred because its complete coefficient array collapses to one exact random-walk Green profile.

## 2. Exact Green collapse

Define

\[
p_K(z)=
\frac{\Gamma(2K+1)}
{4^K\Gamma(K+1-z)\Gamma(K+1+z)}.
\tag{T-21704.5}
\]

At integer `n`,

\[
p_K(n)=\frac{\binom{2K}{K-n}}{4^K}
\]

is a one-dimensional simple-random-walk transition probability. The normalized Green profile is

\[
\boxed{
G_N(z)=\frac1{Z_N}\sum_{K=1}^Np_K(z)^2.}
\tag{T-21704.6}
\]

Writing

\[
m_N^{\rm G}(s)
=\pi^{-s/2}\Gamma(1+s/2)D_N^{\rm G}(s),
\]

`L-21707` proves exactly

\[
\boxed{
D_N^{\rm G}(s)
=2\sum_{n=1}^N
\left[(s-1)G_N(n)-nG_N'(n)\right]n^{-s}.}
\tag{T-21704.7}
\]

No triangular coefficient forest remains: the whole finite arithmetic object is one sampled Green function and its derivative.

## 3. Exact positive truncation defect

The same lemma proves

\[
\boxed{
D_N^{\rm G}(s)
=2(s-1)\zeta(s)
-2\pi\sin\frac{\pi s}{2}
\int_0^\infty A_N(y)y^{1-s}dy,}
\tag{T-21704.8}
\]

for `-4<Re(s)<2`, where

\[
A_N(y)=\frac{G_N(iy)-1}{\sinh^2\pi y}\ge0.
\tag{T-21704.9}
\]

Moreover, with the truncations coupled to the full Brownian sum

\[
S_\infty=\sum_{j\ge1}\frac{\Gamma_{2,j}}{j^2},
\]

one has

\[
\boxed{
\pi^2A_N(\sqrt q)
=\int_0^\infty e^{-qx}b_N(x)dx,}
\tag{T-21704.10}
\]

where

\[
\boxed{
 b_N(x)=
 \sum_{K=1}^N\lambda_{N,K}
 \mathbb P(S_K\le x<S_\infty)\ge0.}
\tag{T-21704.11}
\]

Equivalently,

\[
\boxed{
2\xi(s)-m_N^{\rm G}(s)
=\frac{s}{2}\pi^{-s/2}
\int_0^\infty b_N(x)x^{s/2-1}dx.}
\tag{T-21704.12}
\]

The finite-to-infinite error is the actual positive occupation time between the truncated and complete gamma sums. It is not an opaque analytic remainder.

## 4. Exact Robin-fiber geometry

Let `T_N(x)=P(S>x)` be the tail of the central-binomial cutoff mixture. Put

\[
W_N(a)=e^{a/2}T_N(\pi e^{2a})
\]

and

\[
H_a(z)=\cosh(az)+2z\sinh(az).
\]

`L-21708` proves

\[
\boxed{
\mathcal C_N\left(\frac12+z\right)
=\int_{-\infty}^{\infty}W_N(a)H_a(z)da.}
\tag{T-21704.13}
\]

For every `a>0`, `H_a` is the characteristic determinant of the nonnegative self-adjoint Robin problem

\[
-u''=\lambda u,
\quad u'(0)=0,
\quad u'(a)+\tfrac12u(a)=0,
\]

and all its zeros lie on the imaginary `z` axis. For `a<0`, `H_a` has exactly one reflected real pair, determined by

\[
2z\tanh(|a|z)=1.
\]

Thus the entire finite zero problem is concentrated in one explicit operation:

```text
negative logarithmic-length Robin fibers
+ positive logarithmic-length Robin fibers
-> one global no-double-spend self-adjoint assembly.
```

Every favorable fiber is already solved. The source of every possible off-line pair is visible.

## 5. Sole load-bearing theorem — BGRRZ

> **Brownian Green–Robin Real-Zero theorem (`BGRRZ`).** There is an unbounded sequence `N_j`—more strongly, every `N`—such that every zero of
> \[
> \mathcal C_{N_j}(s)
> \]
> in
> \[
> 0<\operatorname{Re}s<1
> \]
> lies on `Re(s)=1/2`.

A production proof must use the exact Green or Robin source, for example by constructing:

1. a canonical system for the complete mixture (T-21704.13);
2. a positive Schur complement transporting the negative-length Robin sector into the positive sector;
3. an all-order Lee--Yang Wronskian certificate for the even kernel of `L-21708`;
4. a common-interlacing theorem for the transported fiber family.

The theorem may not be replaced by a finite contour count, positivity of the occupation defect, or fiberwise spending without a global capacity ledger.

## 6. BGRRZ implies RH

Assume BGRRZ and suppose `rho` is an off-line zero of `xi` in the open critical strip. Choose a closed disk `D` centered at `rho`, contained in that strip and disjoint from the critical line, with zero-free boundary.

By (T-21704.4),

\[
\mathcal C_{N_j}\longrightarrow4\xi
\]

uniformly on `D`. Rouché's theorem gives the same positive number of zeros of `mathcal C_(N_j)` and `xi` in `D` for all sufficiently large `j`, contradicting BGRRZ. Therefore

\[
\boxed{\mathrm{BGRRZ}\Longrightarrow\mathrm{RH}.}
\tag{T-21704.14}
\]

The limiting zeta function enters only after the finite real-zero theorem is proved.

## 7. Reconnaissance and exact replay

The exact checker `X-21704` verifies the Green coefficient collapse, normalization, finite-product order, Wallis bound, and mutations using rational arithmetic:

```text
coefficient rows             408
normalization rows            48
finite-product order rows    680
Wallis rows                  512
mutations                    4/4

PASS_EXACT_BROWNIAN_GREEN_DEFECT_ALGEBRA
proof-object SHA-256
65442b5fb1ff09e06c7f237102cc289bb9c28f6d33f1b12cea7f54d0670277d7
```

It does not certify the contour theorem, BGRRZ, or RH.

Binary64 reconnaissance for the central-binomial producer gives matching strip and critical-line counts at the retained controls:

```text
N=100,  height=300     138 / 138
N=500,  height=300     138 / 138
N=1000, height=500     269 / 269
N=1000, height=2000   1517 / 1517
```

These are discovery records only.

## 8. Automatic rejection tests

Reject a claimed completion if it:

1. also proves the known-failing raw cutoff without identifying a false hypothesis;
2. uses only `A_N>=0` or complete monotonicity of the truncation defect;
3. drops the actual `a<0` Robin sector;
4. spends one favorable fiber independently on multiple unfavorable fibers;
5. invokes generic log-concavity or `TP_2` in place of an all-order theorem;
6. changes the square spectrum `1^2,2^2,...` or the central-binomial weights silently;
7. uses a property of `xi` or its zeros inside the finite proof;
8. promotes finite winding counts to an all-height result.

## 9. Review order and status

Review:

1. `L-21705` finite gamma algebra;
2. `L-21707` Green/occupation identity;
3. `X-21704` exact replay;
4. `L-21708` Robin-fiber decomposition;
5. `L-21706` and the original Nörlund mutation;
6. this theorem;
7. a future BGRRZ production certificate.

Exact boundary:

```text
finite Brownian/gamma construction       PROPOSED COMPLETE
Green coefficient collapse               PROPOSED COMPLETE + exact replay
positive occupation defect               PROPOSED COMPLETE
Robin-fiber localization                  PROPOSED COMPLETE
critical-strip convergence                PROPOSED COMPLETE
BGRRZ                                     OPEN / RH-BEARING
BGRRZ -> RH                               COMPLETE CONDITIONAL
Riemann Hypothesis                        UNPROVED
```
