# L-15155 — High-order safe windows and the null-mode quotient

Claim ID: `L-15155`  
Title: Boundary-safe finite differences annihilate every certified polynomial pole model and provide an exact packet-centering quotient  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Updated: 2026-08-07 after finite-cutoff companion audit  
Dependencies: `L-15153`; PR #216 `L-21501/T-21502`  
Scope: exact null-space mechanism for finite Vaughan/Heath--Brown packets; no estimate for cutoff or transition residuals

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

Define

\[
 (\Delta_0f)(u)=f(u)-f(u-1),
 \tag{L-15155.3}
\]

and

\[
 (\Delta_{1/2}f)(u)=f(u)-2f(u-\log4).
 \tag{L-15155.4}
\]

Their bilateral Laplace multipliers are

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

Then `H^[m]` is compactly supported and piecewise linear, and

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

For `alpha in {0,1/2}` and `0<=r<m`,

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

## 3. Exact independent subtraction rule

For signed measures `nu,tau`, write

\[
 \mathfrak B_{J,m}(\nu,\tau)
 =\iint K_{J,m}(u,v)d\nu(u)d\tau(v).
 \tag{L-15155.14}
\]

Let

\[
 \nu=\sum_{a=1}^R\nu_a
 \tag{L-15155.15}
\]

be any finite exact decomposition. For each packet choose a source-bound
companion

\[
 \rho_a\in\mathcal N_m.
 \tag{L-15155.16}
\]

No compatibility condition such as `sum rho_a=0` is required. Equations
(L-15155.12)--(L-15155.14) give

\[
 \boxed{
 \mathfrak B_{J,m}(\nu,\nu)
 =\sum_{a,b=1}^R
 \mathfrak B_{J,m}(\nu_a-\rho_a,
                    \nu_b-\rho_b).}
 \tag{L-15155.17}
\]

This is an exact quotient identity. It says that a companion **already proved
to lie in `N_m`** may be removed independently. It does not say that a proposed
finite-cutoff main term lies in `N_m`.

## 4. Positive auxiliary-vector reduction

Define

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

Thus, after signed packet grouping and certified companion subtraction, all
cross terms reduce to a finite vector of nonnegative self-energies.

## 5. Heath--Brown Laurent principal parts

For fixed order `K`, the unpartitioned `j`-th Heath--Brown summand has Dirichlet
series

\[
 M_V(s)^j[-\zeta'(s)]\zeta(s)^{j-1},
 \qquad1\le j\le K.
 \tag{L-15155.21}
\]

Its Laurent principal part at `s=1` has order at most `j+1<=K+1`. The inverse
principal-part density is, beyond the fixed initial half-line endpoint,

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

places that **global Laurent principal part** in `N_m`.

However, a first-crossing partition of the finite summand introduces truncated
factor ranges, shifted step boundaries, and compact transition sources. Those
pieces are not automatically global polynomial densities. They must either:

1. remain in the packet source;
2. be separated and estimated explicitly; or
3. be removed only after a separate certificate proves membership in `N_m`.

Consequently this lemma closes the null-space mechanism, not the analytic
rowwise-centering estimate. The companion and transition ledger belongs to
`CP(K)` in `L-15156/M-15112`.

## 6. Proof boundary

Closed here:

- explicit high-order compact safe windows;
- their complete boundary zero geometry;
- annihilation of every certified finite polynomial pole model;
- exact independent subtraction in the null quotient;
- reduction of all cross packets to a finite vector of positive self-energies.

Not closed:

- construction of useful companions for finite cutoff packets;
- estimates of shifted-boundary and transition residuals;
- subexponential bounds for the packet energies;
- RH.
