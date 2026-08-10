# L-32403 — A main-pole-killing positive-inverse dyadic source

Claim ID: `L-32403`  
Title: The local-Euler value `lambda=2` removes the zeta pole and every artificial eta-line pole from the physical field while preserving all nontrivial zeta zeros and nonnegative inverse/generalized-prime data  
Status: **PROPOSED COMPLETE EXACT ANALYTIC/FINITE LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: algebra of `L-32402`; classical zero-freeness of zeta on `Re(s)=1`  
Scope: exact source purification and pole ledger; no subexponential bound or RH claim

## 1. The distinguished parameter

Put

\[
 \boxed{
 E_*(s)=1-2^{1-s},
 \qquad
 B_*(s)={E_*(s)\over\zeta(s)},
 \qquad
 A_*(s)={\zeta(s)\over E_*(s)}.
 }
\tag{L-32403.1}
\]

This is the local-Euler family of `L-32402` at `lambda=2`.

The inverse/source coefficients are

\[
 \boxed{
 b_*=(\varepsilon-2\delta_2)*\mu,
 }
\tag{L-32403.2}
\]

and

\[
 \boxed{
 a_*(n)=\sum_{r=0}^{v_2(n)}2^r
 =2^{v_2(n)+1}-1>0.
 }
\tag{L-32403.3}
\]

Thus the inverse Dirichlet series remains coefficientwise positive even though
the parameter lies beyond the pole-moat segment `[-1,1]` of `L-32402`.

The generalized-prime coefficients are

\[
 \boxed{
 \Lambda_*(n)
 =\Lambda(n)+(\log2)\sum_{r\ge1}2^r\mathbf1_{n=2^r}
 \ge0.
 }
\tag{L-32403.4}
\]

At `n=2^r` the coefficient is `(1+2^r)log2`.

## 2. Exact physical source

The source-convolved carry atom is

\[
 \boxed{
 Y^*_{X,m}(\theta)
 =J_{m/X}(\theta)-2J_{2m/X}(\theta).
 }
\tag{L-32403.5}
\]

Collecting on the common centered-interval basis gives

\[
 \boxed{
 \sqrt X\,\mathfrak P_{*,\theta}(\log X)
 =\sum_{n\le X}c_*(n)J_{n/X}(\theta),
 }
\tag{L-32403.6}
\]

where

\[
 \boxed{
 c_*(n)=
 \begin{cases}
 3\log2,&n=2,\\
 -\log2,&n=2^r,\ r\ge2,\\
 \log p,&n=p^a,\ p\text{ odd},\\
 -2\log p,&n=2p^a,\ p\text{ odd},\\
 0,&\text{otherwise}.
 \end{cases}}
\tag{L-32403.7}
\]

The corresponding generalized-Chebyshev state is, for `x>=2`,

\[
 \boxed{
 C_*(x)
 =\psi(x)-2\psi(x/2)+2\log2.
 }
\tag{L-32403.8}
\]

Unlike the `lambda=1` state, its continuous density cancels **before** a Jensen
or parabolic projection:

\[
 x-2(x/2)=0.
\tag{L-32403.9}
\]

Thus `C_*` is already a pure dyadic prime-density fluctuation.

## 3. Physical transform

Let

\[
 N_\theta(s)={1-\theta^s-(1-\theta)^s\over s}
\]

as before, and let

\[
 L_*=-{A_*'\over A_*}
 =-{\zeta'\over\zeta}+{E_*'\over E_*}.
\]

Then

\[
 \boxed{
 \widehat{\mathfrak P_{*,\theta}}(z)
 =N_\theta(s)
  \left[
   -E_*(s){\zeta'(s)\over\zeta(s)}+E_*'(s)
  \right],
 \qquad s=z+\frac12.
 }
\tag{L-32403.10}
\]

The bracket is simply `E_* L_*`.

## 4. The pole at one is removed exactly

Near `s=1`,

\[
 E_*(s)=1-e^{-(s-1)\log2}
       =(s-1)\log2+O((s-1)^2),
\]

while

\[
 -{\zeta'\over\zeta}(s)
 ={1\over s-1}+O(1),
\qquad
 {E_*'\over E_*}(s)
 ={1\over s-1}+O(1).
\]

Therefore

\[
 \boxed{
 E_*(s)L_*(s)=2\log2+O(s-1),
 }
\tag{L-32403.11}
\]

so the zeta pole is removable in the physical detector.

This is the coefficient-side reason for the exact zero-density identity
(L-32403.9).

## 5. The artificial eta-line poles are also removed

The zeros of `E_*` are

\[
 s_k=1+{2\pi i k\over\log2},
 \qquad k\in\mathbb Z.
\]

For `k!=0`, classical zero-freeness of zeta on `Re(s)=1` gives
`zeta(s_k)!=0`. Although `L_*` has the local-Euler pole `E_*'/E_*` there, the
physical combination is

\[
 E_*L_*
 =-E_*{\zeta'\over\zeta}+E_*',
\]

which is analytic at every `s_k`.

Thus the physical field does **not** inherit the nonreal eta-line poles which
obstruct the eventual one-sign Mersenne-collar construction reviewed on PR
#314.

## 6. Every nontrivial zeta zero remains

If `rho` is a nontrivial zeta zero, then `0<Re(rho)<1`. Hence

\[
 E_*(\rho)=1-2^{1-\rho}\ne0,
\]

because a zero of `E_*` has real part exactly one. If the multiplicity of `rho`
is `m_rho`, then

\[
 \boxed{
 \operatorname*{Res}_{s=\rho}
 [E_*(s)L_*(s)]
 =-m_\rho E_*(\rho)\ne0.
 }
\tag{L-32403.12}
\]

The atomized vector factor `N_theta(rho)` is not identically zero on any
balanced theta interval, exactly as in `L-32402`. Therefore the source is a
zero-safe detector of every nontrivial off-line zero.

## 7. Why this source is qualitatively different

The `lambda=2` source simultaneously has:

```text
positive inverse coefficients;
nonnegative generalized-prime coefficients;
a two-tap dyadic source;
zero continuous prime density;
no zeta-pole forcing at s=1;
no surviving artificial eta-line pole;
all nontrivial zeta-zero poles retained.
```

It may therefore be used with the reflected Selberg identity without a separate
main-pole safe window. This removes one boundary channel from the production
problem.

The price is that the atom `J_r-2J_(2r)` is no longer one-signed in every
factor-five cell, so the `lambda=1` pointwise transition-reserve theorem does not
transfer automatically.

## 8. New research target — MPKS

A **Main-Pole-Killed Selberg certificate** would apply the general reflected
identity of `L-28013` to `A_*`, keep the complete centered-interval physical
Gram, and prove a coefficient-one lower-scale recurrence with no separate pole
boundary.

This is a candidate replacement for `NTBR`, not a theorem proved here. The first
required check is whether the stronger dyadic generalized-prime reserve in
(L-32403.4) controls the sign-changing `J_r-2J_(2r)` transition matrix after all
cross terms are retained.

## 9. Proof boundary

Closed exactly, subject to review:

- positive inverse/generalized-prime source data;
- exact physical coefficient classification;
- exact cancellation of the continuous density;
- removal of the pole at one;
- removal of all artificial eta-line poles in the physical detector;
- retention of every nontrivial zeta-zero pole.

Open:

- the source-complete reflected Selberg recurrence for this source;
- a subexponential energy estimate;
- RH.