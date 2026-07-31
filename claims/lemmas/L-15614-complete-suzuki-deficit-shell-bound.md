# L-15614 — Complete Suzuki-deficit shell bound

Claim ID: `L-15614`  
Title: The complete arithmetic weighted deficit is reduced to a global large-deviation integral for one finite von-Mangoldt Dirichlet polynomial  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Created: 2026-07-31  
Dependencies: Suzuki equations (4.5)–(4.6); `L-14311`; the Montgomery–Vaughan mean-value theorem for Dirichlet polynomials; elementary digamma and Fourier-remainder bounds  
Scope: proof-grade upper envelopes for `Tr D_(a,G)` in `L-15608/L-15612`  
Related counterexample candidates: none

## Exact arithmetic symbol

Use the scaled Suzuki form on `[-1,1]` and the modified lower symbol of
`L-14311`.  Put

\[
 X=e^{2a},
 \qquad
 c_n=\frac{\Lambda(n)}{\sqrt n},
 \qquad
 S_a(t)=\sum_{n\le X}c_n n^{-it}.
 \tag{L-15614.1}
\]

At scaled frequency `xi=at`, the prime translation polynomial is exactly

\[
 2\sum_{n\le X}c_n\cos(t\log n)
 =2\Re S_a(t).
 \tag{L-15614.2}
\]

Let

\[
 k_a(x)=a\,r''(ax)1_{[-2,2]}(x),
 \qquad
 R_a=\|k_a\|_1
 =\int_{-2a}^{2a}|r''(u)|du.
 \tag{L-15614.3}
\]

For `a|t|>=1`, the exact cancellation of `-log a` against
`log_+|at|` in `L-14311` gives

\[
 s_a^+(at)
 \ge
 \log|t|+C_*
 -2\Re S_a(t)-R_a,
 \tag{L-15614.4}
\]

where

\[
 C_*=C_0-(2A_\zeta+1)
 \tag{L-15614.5}
\]

in the declared Suzuki normalization.  The universal negative-logarithm charge
`-2/pi` is kept outside this modified symbol exactly as in `L-14311`.

For a scalar level `G`, define

\[
 C_{a,G}=G-C_*+R_a.
 \tag{L-15614.6}
\]

Then

\[
 \boxed{
 (G-s_a^+(at))_+
 \le
 \left(C_{a,G}-\log|t|+2\Re S_a(t)\right)_+.}
 \tag{L-15614.7}
\]

Thus the complete arithmetic trace problem is an explicit positive-part
large-deviation problem for the finite polynomial `S_a`.

## Two elementary coefficient budgets

Put

\[
 A_1(a)=\sum_{n\le X}c_n,
 \qquad
 A_2(a)=\sum_{n\le X}c_n^2.
 \tag{L-15614.8}
\]

Without using the prime number theorem,

\[
 \boxed{A_1(a)\le4ae^a+2a,}
 \tag{L-15614.9}
\]

and

\[
 \boxed{
 A_2(a)
 \le1+4a^2+\frac83a^3.}
 \tag{L-15614.10}
\]

Indeed, `Lambda(n)<=log n`, and comparison with the corresponding decreasing or
integrable elementary functions gives

\[
 \sum_{n\le X}\frac{\log n}{\sqrt n}
 \le2\sqrt X\log X+\log X,
\]

and

\[
 \sum_{n\le X}\frac{(\log n)^2}{n}
 \le1+(\log X)^2+\frac13(\log X)^3.
\]

Sharper Chebyshev/PNT bounds may replace these budgets without changing the
argument.

## Rigorous dyadic-shell estimate

Let `T>=1` and suppose

\[
 L_T:=\log T-C_{a,G}>0.
 \tag{L-15614.11}
\]

For `T<=|t|<=2T`, (L-15614.7) and

\[
 (2x-L)_+\le\frac{x^2}{L}
 \qquad(x\ge0,L>0)
 \tag{L-15614.12}
\]

give

\[
 \int_{T\le|t|\le2T}
 (G-s_a^+(at))_+dt
 \le
 \frac1{L_T}
 \int_{T\le|t|\le2T}|S_a(t)|^2dt.
 \tag{L-15614.13}
\]

The Montgomery–Vaughan mean-value theorem yields a universal explicit constant
`C_MV` such that

\[
 \boxed{
 \int_{T\le|t|\le2T}
 (G-s_a^+(at))_+dt
 \le
 \frac{(4T+C_{MV}X)A_2(a)}
      {\log T-C_{a,G}}.}
 \tag{L-15614.14}
\]

This is a proof-grade shell envelope.  It uses every prime power through `X`
and no sampled phase.

## Finite support of the deficit

Since

\[
 |S_a(t)|\le A_1(a),
\]

(L-15614.7) vanishes whenever

\[
 \log|t|>C_{a,G}+2A_1(a).
\]

Therefore the modified deficit is supported inside

\[
 \boxed{
 |t|\le T_{\max}(a,G)
 :=\exp\bigl(C_{a,G}+2A_1(a)\bigr).}
 \tag{L-15614.15}
\]

Let

\[
 T_0=\max\{1,\exp(C_{a,G}+1)\}
\]

and choose the least integer `K` with `2^K T_0>=T_max`.  Combining a direct
central-interval bound with (L-15614.14) gives the complete explicit estimate

\[
\begin{aligned}
 \int_{\mathbb R}(G-s_a^+(at))_+dt
 \le{}&2T_0\bigl(C_{a,G}+2A_1(a)+|\log T_0|\bigr)\\
 &+\sum_{k=0}^{K}
 \frac{(4\,2^kT_0+C_{MV}X)A_2(a)}
      {\log(2^kT_0)-C_{a,G}}.
\end{aligned}
 \tag{L-15614.16}
\]

After the change of variables `xi=at`, the weighted localization trace on the
scaled interval of length two obeys

\[
 \boxed{
 \operatorname{Tr}D_{a,G}
 =\frac1\pi\int_{\mathbb R}(G-s_a^+(\xi))_+d\xi
 \le\frac a\pi\,[\text{right side of (L-15614.16)}].}
 \tag{L-15614.17}
\]

Any separately charged `-2/pi` scalar or directed assembly radius must be
inserted into `G` in the safe direction.

## What this proves asymptotically

The elementary budgets imply only

\[
 T_{\max}(a,G)
 \le
 \exp\bigl(O_G(1)+O(ae^a)\bigr),
 \tag{L-15614.18}
\]

and hence a complete but very coarse bound of the form

\[
 \boxed{
 \operatorname{Tr}D_{a,G}
 \le\exp\bigl(O_G(ae^a)\bigr).}
 \tag{L-15614.19}
\]

This is far larger than the natural one-dimensional source phase-space scale
`e^(2a)`.  Consequently, the standard mean-square theorem, the prime number
theorem, and the newest plunge-region localization estimates do **not** by
themselves establish

\[
 \operatorname{Tr}D_{a,G}
 -d_a(G-\alpha_a)
 \le G-\Gamma_a.
 \tag{L-15614.20}
\]

The localization theorems control eigenvalue tails **after** a frequency weight
has been supplied; they do not provide the missing global large-deviation bound
for `S_a(t)` over all frequencies.

## Exact arithmetic theorem still required

A sufficient proof-grade improvement is any envelope `M_a(T)` satisfying

\[
 \int_{T\le|t|\le2T}
 \left(C_{a,G}-\log|t|+2\Re S_a(t)\right)_+dt
 \le M_a(T)
 \tag{L-15614.21}
\]

for every dyadic shell and

\[
 \boxed{
 \frac a\pi\sum_T M_a(T)
 \le d_a(G-\alpha_a)+G-\Gamma_a.}
 \tag{L-15614.22}
\]

Equation (L-15614.22), together with `L-15612`, is the desired scalar cofinal
condition.  It is a global large-values theorem for the finite von-Mangoldt
polynomial with a moving logarithmic barrier.

High moments may improve (L-15614.14) on distant shells, while the explicit
formula may replace `S_a` by zero terms on selected ranges.  Neither replacement
may omit its complete error or assume RH.

## Distinction from the numerical spectral-strength law

The recently observed numerical law

\[
 S(a)\sim(2a)^3/6
\]

sums strengths of delayed prime channels in a finite numerical basis.  It is not
an identity for

\[
 \operatorname{Tr}P_I\mathcal F^{-1}(G-s_a)_+\mathcal FP_I,
\]

which contains the positive part of the complete oscillatory symbol over the
entire frequency line.  The cubic observation therefore cannot be substituted
for (L-15614.22).

## Proof boundary

- Equations (L-15614.7), (L-15614.15), and the coefficient budgets are
  elementary once the exact Suzuki normalization is fixed.
- Equation (L-15614.14) imports a standard proof-grade Dirichlet-polynomial
  mean-value theorem; a production certificate must instantiate its explicit
  constant and endpoint convention.
- The complete bound (L-15614.16) is sufficient but deliberately crude.
- No current result proves the cofinal shell sum (L-15614.22).
- This lemma does not prove RH; it identifies the exact arithmetic asymptotic
  that remains after automatic weighted-deficit capture.
