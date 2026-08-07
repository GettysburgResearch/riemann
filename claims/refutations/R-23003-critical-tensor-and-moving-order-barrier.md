# R-23003 — Critical tensor and moving-order factorial barrier

Claim ID: `R-23003`  
Title: Factorwise norm bounds conserve the critical logarithmic exponent, while moving-order factorial savings are neutralized by the pole-sensitivity cost of high moment cancellation  
Status: **PROPOSED SCOPE CORRECTION — EXACT HOMOGENEITY AND TAYLOR BARRIERS**  
Authoring agent: `gpt56-pro-09-o`  
Created: 2026-08-07  
Dependencies: `L-15159`; `L-23006`; elementary homogeneity and Taylor's theorem  
Scope: generic completions of `BTP(K)`; source-specific signed cross-order cancellation is not refuted

## 1. Critical tensor homogeneity

Suppose a balanced output signal is multilinear in independent factor sources
`a_1,...,a_m`, and let `E_out` and `E_i` be their squared Hilbert energies.
Under independent scalar rescaling,

\[
 E_{\rm out}(\lambda_1a_1,\ldots,\lambda_ma_m)
 =\left(\prod_i|\lambda_i|^2\right)E_{\rm out}(a_1,\ldots,a_m),
\tag{R-23003.1}
\]

while

\[
 E_i(\lambda_i a_i)=|\lambda_i|^2E_i(a_i).
\tag{R-23003.2}
\]

Consider a factorwise inequality valid uniformly under these rescalings,

\[
 E_{\rm out}
 \le C\prod_i(1+E_i)^{\theta_i}.
\tag{R-23003.3}
\]

Let one `lambda_i` tend to infinity with all others fixed. Equations
(R-23003.1)--(R-23003.3) force

\[
 \boxed{\theta_i\ge1}
\tag{R-23003.4}
\]

for every active factor.

If the factor logarithmic scales are `alpha_i J` and product conservation gives

\[
 \sum_i\alpha_i=1,
\tag{R-23003.5}
\]

then the tensor contraction parameter of `T-15121` obeys

\[
 \boxed{
 \kappa=\sum_i\theta_i\alpha_i\ge1.}
\tag{R-23003.6}
\]

Therefore no generic Cauchy, Young, Schur, or factorwise Gram inequality can
supply the strict tensor contraction required by `BTP(K)`. The all-truncated
K-fold boundary tensor of `L-23006` has exactly

\[
 \alpha_i={1\over K},
 \qquad \theta_i=1,
 \qquad \kappa=1.
\tag{R-23003.7}
\]

A valid proof must use the actual signed coupling between different source
orders or a nonhomogeneous arithmetic reserve. Factorization alone is critical,
not contracting.

## 2. Why fixed-order constants do not help

A factorial or exponentially small constant depending only on fixed `K` does
not change the output exponential rate in `J`. If

\[
 L(J)\le\sum_iL(\alpha_iJ)+O_K(1)
\]

and `sum alpha_i=1`, then a linear ansatz `L(J)=Theta J` satisfies the same
leading equation for every `Theta`. A constant smaller than one cannot force
`Theta=0`.

Thus top-corner simplex factors such as `1/K!` do not repair
(R-23003.6) when `K` is frozen before `J` tends to infinity.

## 3. Moving order and pole sensitivity

One might let `K=K(J)` grow so that

\[
 \log K!\asymp J,
\]

turning a factorial corner constant into an exponential saving. The safe-window
front door prevents this from being free.

Let `W_K` be supported in `[-L,L]`, and suppose its transform has a zero of
order `K` at `alpha`:

\[
 \widehat W_K^{(j)}(\alpha)=0
 \qquad(0\le j<K).
\tag{R-23003.8}
\]

For any fixed `z_0`, Taylor's theorem and

\[
 \widehat W_K^{(K)}(z)
 =\int(-u)^K e^{-zu}W_K(u)du
\]

afford

\[
 \boxed{
 |\widehat W_K(z_0)|
 \le
 {(|z_0-\alpha|L)^K\over K!}
 e^{L(|\alpha|+|z_0-\alpha|)}
 \|W_K\|_1.}
\tag{R-23003.9}
\]

To retain the rightmost-zero exponent, every fixed hypothetical off-line pole
`z_0` must satisfy

\[
 \log|\widehat W_{K(J)}(z_0)|=-o(J).
\tag{R-23003.10}
\]

If `K log K` is comparable with `J` and `L=O(1)`, equations
(R-23003.9)--(R-23003.10) force

\[
 \boxed{
 \log\|W_K\|_1
 \ge\log K!-O(K)-o(J).}
\tag{R-23003.11}
\]

The normalization cost is therefore at least the factorial one hoped to gain
from the top-corner simplex.

## 4. Fixed-shift alternative

The repository's boundary differences use fixed positive shifts. Their
coefficient norm grows only exponentially in `K`, so (R-23003.11) is avoided;
but their support diameter grows linearly in `K`.

The K-fold top boundary layer then has logarithmic thickness `L_K asymp K`.
Its simplex factor is

\[
 {L_K^K\over K!}
 =\exp(O(K)),
\tag{R-23003.12}
\]

rather than `exp(-K log K)`. For `K=J/log J`, this is only `exp(o(J))` and
produces no negative linear exponent.

Thus the two natural choices form a sharp dichotomy:

```text
fixed total support:
    factorial geometric saving,
    but factorial pole-sensitivity normalization cost;

fixed difference shifts:
    subexponential pole cost,
    but no factorial geometric saving.
```

## 5. Consequence for the full-proposal programme

The moving-order shortcut cannot by itself prove `BTP(K)` or RH. After all
complete-lattice and terminal rows are removed, the surviving theorem must use
source-specific signed cancellation in the truncated Möbius boundary tensor.

The following substitutions are invalid:

- a generic factorwise tensor norm;
- a fixed-`K` factorial constant;
- a growing-`K` moment window whose off-line pole response is exponentially
  suppressed;
- a renormalized growing-`K` window without charging its factorial norm;
- a statement that combinatorial packet count `exp(o(J))` implies arithmetic
  cancellation.

## 6. Proof boundary

The homogeneity inequality and Taylor lower-cost mechanism are exact. This file
does not refute a source-specific cross-order Selberg identity, a signed
Möbius martingale, or another genuinely arithmetic cancellation theorem. Such a
theorem is now the only admissible completion of the balanced core.
