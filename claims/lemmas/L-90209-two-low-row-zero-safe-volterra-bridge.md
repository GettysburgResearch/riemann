# L-90209 — The two-low-row SHARP and critical-log criteria are the same zero-safe source under one Volterra smoothing

Claim ID: `L-90209`  
Status: **PROPOSED COMPLETE EXACT TRANSFORM / CROSS-ROUTE LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: `L-33109`; `L-90208`; `T-32403`; elementary Mellin inversion  
Scope: exact low-row compression and route unification; no eventual-sign theorem and no RH conclusion

## 1. The critical-log uniform-Pascal rows

Let

\[
 w_X(q)=q^{-1/2}\log(X/q)\mathbf1_{q\le X}
\]

and let `c_X(n)` be its exact average-carry inverse coefficient under the uniform internal Pascal policy of `L-33109`.

The size-weighted Green occupation is

\[
 M_n(X)=\frac{n(n-1)}{n+1}c_X(n).
 \tag{L-90209.1}
\]

By `L-90208`, with `u=s+1/2`,

\[
 \widehat{M_n}(s)
 =\frac{\mathcal A_n(u)}{s^2\zeta(u)},
 \tag{L-90209.2}
\]

where

\[
 \mathcal A_n(u)
 =n^{1-u}+(2-n)(n+1)^{-u}
 +\frac2{n+1}\zeta(u,n+2).
 \tag{L-90209.3}
\]

For `n=2,3`,

\[
 \mathcal A_2(u)
 =2^{1-u}+\frac23\zeta(u,4),
 \tag{L-90209.4}
\]

\[
 \mathcal A_3(u)
 =3^{1-u}-4^{-u}+\frac12\zeta(u,5).
 \tag{L-90209.5}
\]

Define the two-low-row critical-log scalar

\[
 \boxed{
 \mathcal S(X)=5c_X(2)+3c_X(3).
 }
 \tag{L-90209.6}
\]

Using `c_X(2)=3M_2/2` and `c_X(3)=2M_3/3`,

\[
 \widehat{\mathcal S}(s)
 ={\frac{15}{2}\mathcal A_2(u)+2\mathcal A_3(u)
   \over s^2\zeta(u)}.
 \tag{L-90209.7}
\]

The Hurwitz tails collapse exactly:

\[
 \boxed{
 \frac{15}{2}\mathcal A_2(u)+2\mathcal A_3(u)
 =6\zeta(u)-3(1-2^{-u})(2-2^{-u}).
 }
 \tag{L-90209.8}
\]

Therefore

\[
 \boxed{
 \widehat{\mathcal S}(s)
 ={6\over s^2}
 -{3(1-2^{-u})(2-2^{-u})\over s^2\zeta(u)}.
 }
 \tag{L-90209.9}
\]

## 2. Exact zero-safe arithmetic source

Let

\[
 \omega=(\varepsilon-\delta_2)*(2\varepsilon-\delta_2)*\mu.
 \tag{L-90209.10}
\]

Then

\[
 \sum_{q\ge1}{\omega(q)\over q^u}
 ={(1-2^{-u})(2-2^{-u})\over\zeta(u)},
 \qquad \omega(1)=2.
 \tag{L-90209.11}
\]

Equation (L-90209.9) is exactly the Mellin transform of

\[
 \boxed{
 \mathcal S(X)
 =-3\sum_{2\le q\le X}\omega(q)
 q^{-1/2}\log{X\over q}.
 }
 \tag{L-90209.12}
\]

The apparently separate `6/s^2` term is precisely the correction for the omitted unit coefficient `omega(1)=2`.

The local polynomial

\[
 Q(u)=(1-2^{-u})(2-2^{-u})
 \tag{L-90209.13}
\]

has zeros only on `Re u=0` and `Re u=-1`. Hence no zeta zero with real part greater than one half is cancelled in (L-90209.9).

## 3. Exact bridge to the square-root-hinge low rows

Let `c_T^{\rm h}(n)` be the average-carry inverse of the square-root hinge

\[
 h_T(q)=q^{-1/2}-T^{-1/2}
 \qquad(q\le T),
\]

and put

\[
 \boxed{
 \mathcal H(T)=5c_T^{\rm h}(2)+3c_T^{\rm h}(3).
 }
 \tag{L-90209.14}
\]

`T-32403` proves

\[
 \boxed{
 \mathcal H(T)
 =-3\sum_{2\le q\le T}\omega(q)
 \left(q^{-1/2}-T^{-1/2}\right).
 }
 \tag{L-90209.15}
\]

For one arithmetic coefficient `q`,

\[
 \int_q^\infty q^{-1/2}\log(X/q)X^{-s-1}dX
 ={q^{-s-1/2}\over s^2},
\]

whereas

\[
 \int_q^\infty(q^{-1/2}-X^{-1/2})X^{-s-1}dX
 ={q^{-s-1/2}\over2s(s+1/2)}.
\]

Thus

\[
 \boxed{
 \widehat{\mathcal S}(s)
 ={2(s+1/2)\over s}\widehat{\mathcal H}(s).
 }
 \tag{L-90209.16}
\]

In logarithmic endpoint time `t=log X`, both functions vanish before the first active arithmetic coefficient, and Mellin inversion gives the exact Volterra relation

\[
 \boxed{
 \mathcal S(e^t)
 =2\mathcal H(e^t)
 +\int_0^t\mathcal H(e^u)\,du.
 }
 \tag{L-90209.17}
\]

Equivalently,

\[
 \boxed{
 2{d\over dt}\mathcal H(e^t)+\mathcal H(e^t)
 ={d\over dt}\mathcal S(e^t).
 }
 \tag{L-90209.18}
\]

The low-row SHARP route and the low-row critical-log route are therefore not independent conjectures. They are two Riesz smoothings of the same zero-safe arithmetic source.

## 4. Pole audit and conditional consumer

A hypothetical zeta zero `rho` with `Re rho>1/2` gives a genuine nonreal pole at

\[
 s=rho-1/2
\]

in both transforms, because `Q(rho)\ne0`. Neither transform has a positive-real singularity: zeta has no positive-real zero, and its pole at `u=1` makes `1/zeta(u)` vanish.

Consequently either eventual one-sign condition

\[
 \mathcal S(X)\ge0\quad(X\gg1)
 \tag{L-90209.19}
\]

or its reverse, and likewise either eventual sign of `mathcal H`, implies RH by the same Landau theorem used in `T-32403`.

No eventual sign is proved here. Relation (L-90209.17) does not allow an arbitrary one-sided implication in the reverse direction: a positive Volterra smoothing can hide local sign changes.

## 5. Route consequence

After `R-90201`, the frozen binary–ternary positivity/BTF route is refuted by deterministic policy resonances. The uniform Pascal policy has no deterministic resonance, and its two lowest rows already compress the entire RH-facing arithmetic into the zero-safe source `omega`.

The preferred elementary continuation is therefore one of:

1. prove a one-sided theorem for `mathcal H` or `mathcal S` while preserving the complete two-row cancellation;
2. construct a positive/ordered representation of the source `omega` in the resonance-free uniform Pascal coordinate;
3. prove a weaker signed low-row estimate sufficient for the same Landau consumer.

Full SHARP remains much stronger than required.

## 6. Proof boundary

Proved exactly:

- the low-row critical-log transform;
- its zero-safe finite Euler numerator;
- the physical arithmetic-source identity;
- the exact Volterra bridge between the SHARP hinge and critical-log low-row scalars;
- the common pole audit and conditional Landau consumer.

Open:

- eventual sign of either low-row scalar;
- SHARP;
- RH.
