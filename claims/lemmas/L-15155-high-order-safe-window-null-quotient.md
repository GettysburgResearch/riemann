# L-15155 — High-order safe windows and the rowwise null-mode quotient

Claim ID: `L-15155`  
Title: Boundary-safe finite differences annihilate every prescribed polynomial pole model, so exact decomposition rows may be centered independently before the adjoint Gram estimate  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Dependencies: `L-15153`; PR #216 `L-21501/T-21502`  
Scope: exact rowwise-centering repair for finite Vaughan/Heath--Brown packets

## 1. Two boundary difference operators

Let `H` be the compact prime-only safe window of `T-21502`. Its transform has
simple zeros at

\[
 z=0
 \quad\text{and}\quad
 z={1\over2},
 \tag{L-15155.1}
\]

and no zero in

\[
 0<\operatorname{Re}z<{1\over2}.
 \tag{L-15155.2}
\]

Define the finite translation differences

\[
 (\Delta_0f)(u)=f(u)-f(u-1),
 \tag{L-15155.3}
\]

and

\[
 (\Delta_{1/2}f)(u)=f(u)-2f(u-\log4).
 \tag{L-15155.4}
\]

Their bilateral Laplace multipliers are respectively

\[
 1-e^{-z}
 \quad\text{and}\quad
 1-2\,4^{-z}.
 \tag{L-15155.5}
\]

For an integer `m>=1`, put

\[
 \boxed{
 H^{[m]}
 =\Delta_0^{m-1}\Delta_{1/2}^{m-1}H.}
 \tag{L-15155.6}
\]

Then `H^[m]` is still compactly supported and piecewise linear, and

\[
 \boxed{
 \widehat H^{[m]}(z)
 =\widehat H(z)
  (1-e^{-z})^{m-1}
  (1-2\,4^{-z})^{m-1}.}
 \tag{L-15155.7}
\]

Consequently:

1. `widehat H^[m]` has a zero of order at least `m` at `z=0`;
2. it has a zero of order at least `m` at `z=1/2`;
3. it has no zero in the open counterexample strip;
4. it retains the vertical `O((1+|t|)^-2)` decay of `H` on every fixed strip.

Thus every `H^[m]` is independently safe for the rightmost-pole transfer.

## 2. Polynomial moment annihilation

For `alpha in {0,1/2}` and `0<=r<m`, the order-`m` zero gives

\[
 \boxed{
 \int_{\mathbb R}u^r e^{-\alpha u}H^{[m]}(u)du=0.}
 \tag{L-15155.8}
\]

Indeed the integral is `(-1)^r` times the `r`-th derivative of the transform at
`alpha`.

For a logarithmic block `J`, define

\[
 K_{J,m}(u,v)
 =\int_J^{J+1}
 H^{[m]}(x-u)H^{[m]}(x-v)dx.
 \tag{L-15155.9}
\]

Let

\[
 d\rho_{\alpha,r}(v)=v^r e^{\alpha v}dv.
 \tag{L-15155.10}
\]

For fixed `x`, substitution `t=x-v` gives

\[
\begin{aligned}
 \int H^{[m]}(x-v)v^r e^{\alpha v}dv
 ={}&e^{\alpha x}
 \sum_{q=0}^r
 {r\choose q}x^{r-q}(-1)^q\\
 &\times
 \int t^q e^{-\alpha t}H^{[m]}(t)dt
 =0.
\end{aligned}
 \tag{L-15155.11}
\]

Therefore the block kernel annihilates every such mode in either leg:

\[
 \boxed{
 \int K_{J,m}(u,v)d\rho_{\alpha,r}(v)=0,}
 \tag{L-15155.12}
\]

and symmetrically in `u`.

Put

\[
 \mathcal N_m
 =\operatorname{span}
 \left\{
 u^rdu,\ u^re^{u/2}du:
 0\le r<m
 \right\}.
 \tag{L-15155.13}
\]

The finite Gram form descends exactly to the quotient of signed source measures
by `mathcal N_m`.

## 3. Independent rowwise centering

For finite signed measures `nu,tau`, write

\[
 \mathfrak B_{J,m}(\nu,\tau)
 =\iint K_{J,m}(u,v)d\nu(u)d\tau(v).
 \tag{L-15155.14}
\]

Let an exact finite arithmetic decomposition be

\[
 \nu=\sum_{a=1}^R\nu_a.
 \tag{L-15155.15}
\]

For each row choose an arbitrary polynomial pole companion

\[
 \rho_a\in\mathcal N_m.
 \tag{L-15155.16}
\]

No compatibility condition such as `sum rho_a=0` is required. Equations
(L-15155.12)--(L-15155.14) give the exact identity

\[
 \boxed{
 \mathfrak B_{J,m}(\nu,\nu)
 =\sum_{a,b=1}^R
 \mathfrak B_{J,m}(\nu_a-\rho_a,
                    \nu_b-\rho_b).}
 \tag{L-15155.17}
\]

Thus the concern that continuous main terms cancel only after all Vaughan or
Heath--Brown rows are recombined is removed at the kernel level: each row may
be centered by its own Laurent-polynomial companion, provided the window order
exceeds the companion degree.

This is a quotient identity, not an asymptotic approximation.

## 4. Positive row closure

The kernel is positive semidefinite because it is a Gram of translated windows.
Define the row energies

\[
 E_a(J)=\mathfrak B_{J,m}(\nu_a-\rho_a,
                         \nu_a-\rho_a)\ge0.
 \tag{L-15155.18}
\]

Cauchy--Schwarz in the Gram Hilbert space gives

\[
 |\mathfrak B_{J,m}(\nu_a-\rho_a,
                    \nu_b-\rho_b)|
 \le\sqrt{E_a(J)E_b(J)}.
 \tag{L-15155.19}
\]

Hence

\[
 \boxed{
 \mathfrak B_{J,m}(\nu,\nu)
 \le
 \left(\sum_{a=1}^R\sqrt{E_a(J)}\right)^2
 \le R\sum_{a=1}^RE_a(J).}
 \tag{L-15155.20}
\]

Every cross row is therefore controlled by a finite vector of nonnegative
self-energies. The decomposition does not have to identify each auxiliary row
with the original prime block.

## 5. Application to fixed-order Heath--Brown rows

For a fixed identity order `K`, a row of the standard finite Heath--Brown
identity has Dirichlet series

\[
 M_V(s)^j[-\zeta'(s)]\zeta(s)^{j-1},
 \qquad1\le j\le K,
 \tag{L-15155.21}
\]

where `M_V` is a finite Möbius polynomial. Its pole at `s=1` has order at most
`j+1<=K+1`. The inverse pole model is therefore

\[
 e^{u/2}\times
 \text{a polynomial in }u\text{ of degree at most }K.
 \tag{L-15155.22}
\]

Choosing

\[
 m=K+1
 \tag{L-15155.23}
\]

places every row pole model in `mathcal N_m`. Consequently all rows can be
centered independently before Type-I/Type-II estimates are applied.

This closes the rowwise-centering gate identified in the latest review. It does
not supply the Type-II estimates themselves.

## 6. Proof boundary

Closed here:

- explicit high-order compact safe windows;
- their complete boundary zero geometry;
- annihilation of every prescribed finite polynomial pole model;
- exact independent row centering;
- reduction of all cross terms to a finite vector of positive row energies.

Not closed:

- subexponential bounds for the centered row energies;
- closure of the auxiliary vector under a scale decomposition;
- RH.
