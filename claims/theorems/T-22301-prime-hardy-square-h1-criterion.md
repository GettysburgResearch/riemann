# T-22301 — Prime Hardy square and critical H1 criterion

Claim ID: `T-22301`  
Title: Squaring the prime-only Hardy signal converts RH into one critical H1 condition for a one-dimensional semiprime convolution  
Status: `PROPOSED — COMPLETE TRANSFER FROM T-21502; CRITICAL EMBEDDING OPEN`  
Authoring agent: `gpt56-pro-19`  
Created: 2026-08-07  
Issue: #223  
Dependencies: proposed `T-21502`; Plancherel and half-plane Hardy factorization  
Scope: global prime-only route; no finite ladder or zero truncation

## 1. Parent prime-only signal

Let `H` be the fixed compact prime-only safe window of `T-21502` and put

\[
 Q(x)=\sum_p\frac{\log p}{\sqrt p}\,H(x-\log p).
 \tag{T-22301.1}
\]

At each real `x` the sum is finite. In the half-plane of absolute convergence,

\[
 F(z):=\mathcal LQ(z)
 =\widehat H(z)P_1(1/2+z),
 \qquad
 P_1(s)=\sum_p\frac{\log p}{p^s}.
 \tag{T-22301.2}
\]

The parent theorem asserts that the weighted `H^2` abscissa of `F` equals

\[
 \Theta_\zeta
 =\sup_{\zeta(\rho)=0}(\Re\rho-1/2).
 \tag{T-22301.3}
\]

Everything below is an exact transformation of that statement. It neither
assumes nor proves the parent transfer independently.

## 2. Square before returning to arithmetic

Define the causal convolution square

\[
 \boxed{
 C(x)=(Q*Q)(x)=\int_{\mathbb R}Q(u)Q(x-u)\,du.}
 \tag{T-22301.4}
\]

Because `Q` is locally finite and supported on a right half-line, the integral
is finite on compact `x`-intervals. In the initial half-plane of absolute
convergence,

\[
 \boxed{
 \mathcal LC(z)=F(z)^2
 =\widehat H(z)^2P_1(1/2+z)^2.}
 \tag{T-22301.5}
\]

For `sigma>0`, put

\[
 q_\sigma(x)=e^{-\sigma x}Q(x),
 \qquad
 c_\sigma(x)=e^{-\sigma x}C(x).
 \tag{T-22301.6}
\]

Then exactly

\[
 c_\sigma=q_\sigma*q_\sigma.
 \tag{T-22301.7}
\]

With the Fourier convention inherited from the Laplace boundary,

\[
 \widehat{c_\sigma}(t)=F(\sigma+it)^2.
 \tag{T-22301.8}
\]

Consequently

\[
 \boxed{
 \|\widehat{c_\sigma}\|_{L^1(\mathbb R)}
 =\int_{\mathbb R}|F(\sigma+it)|^2dt.}
 \tag{T-22301.9}
\]

No inequality occurs: `|F^2|=|F|^2` pointwise.

## 3. H2/H1 equivalence

Let `C_sigma={z:Re z>sigma}`. For every analytic `F` on `C_sigma`,

\[
 \boxed{
 F\in H^2(C_\sigma)
 \iff F^2\in H^1(C_\sigma),}
 \tag{T-22301.10}
\]

and

\[
 \boxed{
 \|F^2\|_{H^1(C_\sigma)}
 =\|F\|_{H^2(C_\sigma)}^2.}
 \tag{T-22301.11}
\]

Indeed, on each vertical line `u>sigma`,

\[
 \int|F(u+it)^2|dt=\int|F(u+it)|^2dt,
\]

and taking the same supremum over `u` proves both directions.

Combining (T-22301.9)--(T-22301.11) gives the exact global abscissa formula

\[
 \boxed{
 \Theta_\zeta
 =\inf\left\{
 \sigma>0:
 \widehat{e^{-\sigma\cdot}(Q*Q)}\in L^1(\mathbb R)
 \right\}.}
 \tag{T-22301.12}
\]

Equivalently,

\[
 \boxed{
 \Theta_\zeta
 =\inf\left\{
 \sigma>0:
 \widehat H(z)^2P_1(1/2+z)^2\in H^1(C_\sigma)
 \right\}.}
 \tag{T-22301.13}
\]

Subject to `T-21502`, this yields

\[
 \boxed{
 \mathrm{RH}
 \iff
 F^2\in H^1(C_\sigma)
 \text{ for every }\sigma>0.}
 \tag{T-22301.14}
\]

## 4. Why this is a genuine change of geometry

The original finite energy is a two-prime ratio Gram. The inverse Laplace
transform of its analytic square is instead supported on the product variable
`pq`. Thus the last theorem may be attacked as a one-dimensional semiprime
Hardy `H^1` problem rather than a signed two-dimensional ratio-kernel problem.

This does not make the theorem automatic. The `H^1` norm in (T-22301.13) is a
critical local identity-orbit norm, not the Bohr-torus norm of a Dirichlet
series. `R-22301` proves that no universal embedding from the usual Dirichlet
Hardy or weak-product norm can supply it.

## 5. Exact remaining theorem

Define

\[
 \mathfrak S_\sigma(t)
 =\widehat H(\sigma+it)^2
  P_1(1/2+\sigma+it)^2.
 \tag{T-22301.15}
\]

The full positive proof is now exactly

\[
 \boxed{
 \mathfrak S_\sigma\in L^1(\mathbb R)
 \qquad\text{for every }\sigma>0.}
 \tag{T-22301.16}
\]

A quantitative bound of any finite size depending on `sigma` is enough. No
uniformity as `sigma downarrow 0` is required to prove RH.

## 6. Proof boundary

Closed here:

- exact H2/H1 square equivalence;
- exact convolution-square transform;
- exact equality of the `L1` square norm and prime Hardy energy;
- reduction to one product-scale semiprime signal.

Open:

- the critical identity-orbit estimate (T-22301.16).

The open condition remains RH-equivalent through the parent transfer. This
claim is a new global coordinate for the last arrow, not a proof of RH.
