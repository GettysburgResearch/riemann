# L-24903 — Paid-coordinate exponent bound

Claim ID: `L-24903`  
Title: Every truncated coordinate paid outside a positive reflected Gram costs exactly one `1/K` unit in the energy exponent  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #249  
Dependencies: normalized inverse-zeta tuple weights and fixed-order divisor bounds  
Scope: boundary-charge rows satisfying `D-24901.3`--`D-24901.4`

## 1. One normalized truncated coordinate

Let `V=e^{J/K+O_K(1)}`. A truncated Möbius coordinate occurs with square-root
normalization `a^{-1/2}` and a coefficient of divisor order at fixed `K`.
Therefore

\[
\sum_{a\le V}{d_{r_K}(a)(1+\log a)^{s_K}\over\sqrt a}
\le V^{1/2+o_K(1)}.
\tag{L-24903.1}
\]

This is the only estimate used for a paid coordinate; no cancellation is
claimed after payment.

Thus one paid coordinate costs

\[
V^{1/2+o_K(1)}
\]

in amplitude and

\[
\boxed{V^{1+o_K(1)}
=\exp\left[\left({1\over K}+o_K(1)\right)J\right]}
\tag{L-24903.2}
\]

in energy.

## 2. Several simultaneous charges

Suppose a boundary row pays `q` truncated coordinates and all remaining
coordinates stay inside either:

1. a positive reflected Gram; or
2. a declared lower-scale auxiliary source.

Iterating (L-24903.1) gives amplitude mass

\[
V^{q/2+o_K(J)}
\]

and hence

\[
\boxed{
\|b_\gamma\|^2
\le
\exp\left[
\left({q\over K}+o_K(1)\right)J
\right]
\left[1+M_K((1-\delta)J+C_K)\right].}
\tag{L-24903.3}
\]

The number of boundary rows and their fixed-order binomial coefficients may
depend arbitrarily on `K`; for fixed `K` they contribute only `e^{o_K(J)}`.

## 3. Maximum charge, not total face count

If there are `N_K` codimension-one faces, each paying one coordinate, then

\[
\sum_{r=1}^{N_K}\|b_r\|^2
\le
N_K\exp\left[\left({1\over K}+o_K(1)\right)J\right]
[1+M_K(\cdots)].
\]

Since `N_K` is independent of `J`, the exponent is still `1/K`. It is incorrect
to charge `N_K/K` merely because there are `N_K` faces.

Conversely, one face which simultaneously pays `q=Omega(K)` coordinates has
an order-one exponent and is fatal. The certificate must therefore track the
maximum simultaneous charge.

## 4. Consequence for an absolute charge bound

If `RBC(K)` proves

\[
q_K\le C_{\rm ref}
\]

with `C_ref` absolute, then

\[
\boxed{
\sum_\gamma\|b_\gamma\|^2
\le
\exp\left[
\left({C_{\rm ref}\over K}+o_K(1)\right)J
\right]
\left[1+M_K((1-\delta)J+C_K)\right].}
\tag{L-24903.4}
\]

## 5. Proof boundary

Closed exactly:

- the normalized `V^(1/2)` amplitude cost of one paid coordinate;
- the `q/K` energy exponent;
- the irrelevance of the number of fixed-order face families.

Not closed:

- the actual charge map;
- the reflected reserve;
- an absolute bound on `q_K` for the top Möbius corner.
