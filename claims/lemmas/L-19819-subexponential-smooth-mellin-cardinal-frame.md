# L-19819 — Subexponential smooth Mellin-cardinal source frames

Claim ID: `L-19819`  
Title: Exact smooth source interpolation and a sub-square-root graph bound persist far beyond the quadratic-log cutoff  
Status: `PROPOSED — COMPLETE CARDINAL/MEASURE PROOF; STANDARD LOCAL MINIMUM-MODULUS INPUT DECLARED`  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: `L-15631`; Riemann--von Mangoldt; a standard local product/minimum-modulus estimate for zeta in a fixed strip  
Scope: complete finite CCM Fourier spaces on a diagonal dense enough for a global Weil-form limit

## 1. Purpose

`L-15631` constructs an exact smooth source right inverse on a Fourier cutoff
`N=O(L^2)`.  The quadratic-log cutoff is convenient for low-packet work, but it
is not forced by the source algebra.  For a whole-problem attack one wants the
finite Fourier spaces to approximate compact Gevrey test functions so strongly
that the rapidly growing support-side explicit-formula constants are harmless.

The present lemma permits a much larger cutoff while preserving the decisive
source graph rate

\[
 M_R=R^{1/4+o(1)},
 \qquad R=e^L.
\]

The permitted Fourier bandwidth is

\[
 H_L=\exp(o(\sqrt L)),
\]

so the dimension may be `R^(o(1))`.  This is more than enough for
superexponentially accurate approximation of compact Gevrey functions.

## 2. Smooth differential cardinals

Fix

\[
 \eta\in C_c^\infty((-a,a)),
 \qquad \int_{\mathbb R}\eta=1.
 \tag{L-19819.1}
\]

For a length `ell>2a`, put

\[
 b_\ell(t)=\ell^{-1}{\bf1}_{[-\ell/2,\ell/2]}(t),
 \qquad
 \chi_\ell=b_\ell*\eta.
 \tag{L-19819.2}
\]

Use

\[
 \widehat q(z)=\int_{\mathbb R}q(t)e^{-izt}\,dt,
 \qquad
 \omega_k={2\pi k\over\ell}.
 \tag{L-19819.3}
\]

Then

\[
 \widehat\chi_\ell(z)
 ={2\sin(\ell z/2)\over\ell z}\widehat\eta(z),
 \tag{L-19819.4}
\]

and the differential cardinal

\[
 q_{k,\ell}(t)
 ={(\partial_t+1/2)
   [\chi_\ell(t)e^{i\omega_kt}]
  \over i\omega_k+1/2}
 \tag{L-19819.5}
\]

satisfies exactly

\[
 \boxed{
 \widehat q_{k,\ell}(\omega_j)=\delta_{kj},
 \qquad
 \widehat q_{k,\ell}(i/2)=0.
 }
 \tag{L-19819.6}
\]

The associated even multiplicative source

\[
 f_{k,\ell}(e^t)=e^{-t/2}q_{k,\ell}(t)
 \tag{L-19819.7}
\]

is smooth, compactly supported away from zero, and satisfies both exact source
constraints

\[
 f_{k,\ell}(0)=0,
 \qquad
 \int_{\mathbb R}f_{k,\ell}(x)\,dx=0.
 \tag{L-19819.8}
\]

These statements are the exact algebra of `L-15631` and do not depend on the
number of columns.

## 3. Subexponential cutoff

Let `A->infinity`.  Choose a bandwidth `H_A>=2` satisfying

\[
 \boxed{
 \log H_A=o(\sqrt A).
 }
 \tag{L-19819.9}
\]

For a length `ell in [A,A+1]`, put

\[
 N_A=\left\lfloor{\ell H_A\over2\pi}\right\rfloor.
 \tag{L-19819.10}
\]

Thus

\[
 |\omega_k|\leq H_A,
 \qquad
 d_A:=2N_A+1
 =\exp(o(A))=R^{o(1)},
 \qquad R=e^A.
 \tag{L-19819.11}
\]

## 4. Cofinal simultaneous zero avoidance

Let `Z(H_A)` denote the multiset of ordinates of every nontrivial zeta zero with
absolute ordinate at most `2H_A+2`; no critical-line hypothesis is imposed.
Set

\[
 \delta_A=
 {1\over[A H_A\log(2H_A)]^2}.
 \tag{L-19819.12}
\]

Delete from `[A,A+1]` every length for which

\[
 \left|{2\pi k\over\ell}-\gamma\right|<\delta_A
 \tag{L-19819.13}
\]

for some `|k|<=N_A` and some `gamma in Z(H_A)`.

For one fixed ordinate `gamma>=1`, the possible integers `k` number
`O(1+gamma)`.  On the relevant set,

\[
 \left|{d\over d\ell}{2\pi k\over\ell}\right|
 \asymp {\gamma\over A},
\]

so the total deleted length associated with that ordinate is

\[
 O(\delta_A A).
 \tag{L-19819.14}
\]

The Riemann--von Mangoldt bound gives

\[
 \#Z(H_A)=O(H_A\log(2H_A)).
 \tag{L-19819.15}
\]

Hence the total deleted length is

\[
 O(\delta_A A H_A\log(2H_A))
 =O\!\left({1\over A H_A\log(2H_A)}\right)
 =o(1).
 \tag{L-19819.16}
\]

The bounded-height ordinates are treated by the same calculation or by a finite
compactness deletion.  Therefore there exists

\[
 \boxed{
 \ell_A\in[A,A+1]
 }
 \tag{L-19819.17}
\]

such that every selected grid point is at vertical distance at least `delta_A`
from the ordinate of every zero in the required height range.  The chosen
length may simultaneously avoid any prescribed countable set.

## 5. Local minimum-modulus bound

The standard local factorization in a fixed strip gives the following
unconditional estimate.  For `|t|<=H`, if the point `1/2+it` has distance at
least `delta` from the ordinate of every zero with `|gamma-t|<=2`, then

\[
 \boxed{
 |\zeta(1/2+it)|^{-1}
 +\left|{d\over dt}\zeta(1/2+it)^{-1}\right|
 \leq
 \exp\{C\log(2H)[\log(2H)+\log(1/\delta)]\}.
 }
 \tag{L-19819.18}
\]

A proof uses the local product

\[
 \zeta(s)=e^{O(\log H)}
 \prod_{|\gamma-t|\leq2}(s-\rho)
 \tag{L-19819.19}
\]

in `-1<=Re s<=2`, with the pole and gamma factors removed in the usual way.
There are `O(log H)` local zeros with multiplicity.  The lower distance bound
controls the product; logarithmic differentiation gives the derivative bound.
The constants are absolute after the bounded-height range is separated.

For the lengths (L-19819.17), equations (L-19819.12) and (L-19819.18) give

\[
 \boxed{
 Z_A:=
 \max_{|k|\leq N_A}
 \left(
 |\zeta(1/2+i\omega_k)|^{-1}
 +|\partial_\ell\zeta(1/2+i\omega_k)^{-1}|
 \right)
 =\exp(o(A))=R^{o(1)}.
 }
 \tag{L-19819.20}
\]

Indeed

\[
 \log(1/\delta_A)=O(\log A+\log H_A),
\]

and (L-19819.9) makes

\[
 \log H_A(\log A+\log H_A)=o(A).
\]

The derivative in `ell` also contains
`partial_ell omega_k=O(H_A/A)`; this is `exp(o(A))` and is absorbed.

## 6. Exact finite source inverse

For

\[
 y(t)=\sum_{|k|\leq N_A}y_ke^{i\omega_kt},
\]

define

\[
 \boxed{
 {\cal C}_{\ell_A}y
 =\sum_{|k|\leq N_A}
 {y_k\over\zeta(1/2+i\omega_k)}f_{k,\ell_A}.
 }
 \tag{L-19819.21}
\]

In the periodized Mellin normalization of `L-16211/L-15631`, the arithmetic
multiplier and (L-19819.6) give

\[
 \boxed{
 P_{N_A}\Sigma E({\cal C}_{\ell_A}y)=y.
 }
 \tag{L-19819.22}
\]

Thus the complete `d_A`-dimensional Fourier space has an exact smooth source
frame at every selected length.

## 7. Graph and support-derivative estimates

For every fixed integer `p>=0`, Leibniz and (L-19819.5) give

\[
 \|q_{k,\ell}\|_{W^{p,1}}
 \leq C_{p,\eta}(1+|\omega_k|)^p.
 \tag{L-19819.23}
\]

Consequently

\[
 \left\|\sum_{|k|\leq N_A}c_kq_{k,\ell}\right\|_{W^{p,1}}
 \leq
 C_{p,\eta}\sqrt{d_A}(1+H_A)^p\|c\|_2.
 \tag{L-19819.24}
\]

Differentiating in `ell` introduces only factors polynomial in `A`, `H_A`, and
`d_A`, together with the zeta inverse and its derivative.  Therefore

\[
 \boxed{
 \|Q_{\ell_A}\|_{\ell^2\to W^{p,1}}
 +\|\partial_\ell Q_{\ell_A}\|_{\ell^2\to W^{p,1}}
 =\exp(o(A)).
 }
 \tag{L-19819.25}
\]

The exact two-end decomposition remains

\[
 \widehat q_{k,\ell}(z)
 =e^{i\ell z/2}a_{k,+}(z,\ell)
  +e^{-i\ell z/2}a_{k,-}(z,\ell),
 \tag{L-19819.26}
\]

with smooth rapidly decreasing amplitudes, exactly as in `L-15631`.

Transport to the symmetric multiplicative profile costs at most

\[
 e^{A/4+O(1)}=R^{1/4+o(1)}.
\]

Combining with (L-19819.20) and (L-19819.25) yields the complete unwhitened
source graph bound

\[
 \boxed{
 M_R=R^{1/4+o(1)}.
 }
 \tag{L-19819.27}
\]

In particular,

\[
 \boxed{
 {M_R\log R\over\sqrt R}\longrightarrow0.
 }
 \tag{L-19819.28}
\]

The dimension satisfies `d_R=R^(o(1))`, so it may be inserted into the
rank-one Bessel large sieve `L-19818` without changing any power of `R`.

## 8. A useful explicit schedule

For any fixed

\[
 0<\theta<1/2,
\]

one may take

\[
 \boxed{
 H_A=\exp(A^\theta),
 \qquad
 N_A\asymp A\exp(A^\theta).
 }
 \tag{L-19819.29}
\]

Then

\[
 d_A=\exp(A^\theta+O(\log A))=R^{o(1)},
\]

while the source and support-derivative graph remains `R^(1/4+o(1))`.

This cutoff is far larger than `O(A^2)` but still lies safely below every
power of the radial scale `R=e^A`.

## 9. What is and is not proved

The lemma proves:

1. exact smooth source constraints;
2. exact finite interpolation;
3. existence of cofinal lengths avoiding every relevant zero ordinate;
4. a source dimension `R^(o(1))`;
5. a complete graph and support-derivative bound `R^(1/4+o(1))`;
6. an exact finite two-end support-phase ledger.

The exact right inverse is for the declared periodized arithmetic map.  Its use
in a localized Weil matrix requires the same periodization/restriction adapter
and explicit-formula normalization used by the production CCM construction.
The local minimum-modulus estimate (L-19819.18) is standard but should be
independently audited in the repository's exact completed-zeta convention.

This lemma does not by itself prove a line-centered local-Weyl LMI or RH.
