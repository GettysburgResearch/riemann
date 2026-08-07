# T-15122 — Vanishing-rate high-order Type-II systems imply RH

Claim ID: `T-15122`  
Title: A family of high-order safe-window packet systems with scale contraction dominating its coefficient-growth rate forces the common rightmost-zero exponent to vanish  
Status: **PROPOSED EXACT COMPOSITION THEOREM PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Updated: 2026-08-07 with the fixed-reserve partition of `L-15157`  
Dependencies: `L-15151`, `L-15154`--`L-15157`, `T-15121`  
Scope: quantitative composition theorem for increasing Heath--Brown order

## 1. Quantitative packet recurrence

For every integer `K>=2`, let

\[
 \mathbf E_K(J)
 =(E_{K,1}(J),\ldots,E_{K,r_K}(J))
 \tag{T-15122.1}
\]

be a finite nonnegative auxiliary-energy system containing the full-von-Mangoldt
safe block for `H^[K+1]`.

Suppose there are numbers

\[
 0<\delta_K<1,
 \qquad
 \varepsilon_K\ge0,
 \tag{T-15122.2}
\]

such that, uniformly over the finite packet dictionary,

\[
 \boxed{
 E_{K,i}(J)
 \le
 \exp\{(\varepsilon_K+o_K(1))J\}
 \left[
 1+\max_{h}
  \max_{k\le(1-\delta_K)J+O_K(1)}
  E_{K,h}(k)
 \right].}
 \tag{T-15122.3}
\]

Here `o_K(1)` tends to zero as `J->infinity` for each fixed `K`.

## 2. Quantitative exponent bound

Put

\[
 M_K(X)=1+\max_{i,J\le X}E_{K,i}(J).
\]

Equation (T-15122.3) gives

\[
 \log M_K(X)
 \le
 (\varepsilon_K+o_K(1))X
 +\log M_K((1-\delta_K)X+O_K(1)).
 \tag{T-15122.4}
\]

Iterating the contracted scale yields

\[
 \boxed{
 \limsup_{X\to\infty}{\log M_K(X)\over X}
 \le{\varepsilon_K\over\delta_K}.}
 \tag{T-15122.5}
\]

The fixed support shifts contribute only `o(X)` over the logarithmic number of
iterations.

## 3. Common rightmost-zero exponent

Every high-order window `H^[K+1]` is compact, has sufficient vertical decay,
and has no transform zero in the open counterexample strip. By `L-15151`, its
full-von-Mangoldt and ordinary-prime cumulative energies have the same
rightmost-zero exponent

\[
 \Theta_\zeta.
 \tag{T-15122.6}
\]

The block energy is bounded by the finite auxiliary packet vector in `L-15156`.
Therefore (T-15122.5) implies

\[
 \boxed{
 2\Theta_\zeta
 \le{\varepsilon_K\over\delta_K}.}
 \tag{T-15122.7}
\]

for every `K` for which the complete packet recurrence is proved.

Consequently, if

\[
 \boxed{
 {\varepsilon_K\over\delta_K}\longrightarrow0,}
 \tag{T-15122.8}
\]

then

\[
 \Theta_\zeta=0
\]

and hence

\[
 \boxed{\mathrm{RH}.}
 \tag{T-15122.9}
\]

## 4. Fixed-reserve corollary

`L-15157` proves that the first-crossing partition may use any fixed

\[
 0<\delta<{1\over2}
\]

for every identity order. Type-II packets then have both factor scales at most
`(1-delta)J+O_K(1)`, and every failure is declared Type I with a small factor
at scale `delta J+O_K(1)`.

Thus one may take

\[
 \delta_K=\delta
 \tag{T-15122.10}
\]

uniformly. In the linear packet system, the high-order sufficient condition
simplifies to

\[
 \boxed{\varepsilon_K\longrightarrow0.}
 \tag{T-15122.11}
\]

No artificial `1/K` contraction loss is present.

## 5. Tensor-packet version

Suppose a packet is bounded by a finite product of lower-scale auxiliary
energies. If

\[
 E_{K,i}(J)
 \le
 \exp\{(\varepsilon_K+o_K(1))J\}
 \prod_s
 \left[1+M_K(\alpha_{K,s}J)
 \right]^{\theta_{K,s}},
 \tag{T-15122.12}
\]

and

\[
 \kappa_K=\sum_s\theta_{K,s}\alpha_{K,s}<1,
 \tag{T-15122.13}
\]

then

\[
 \limsup_{X\to\infty}{\log M_K(X)\over X}
 \le{\varepsilon_K\over1-\kappa_K}.
 \tag{T-15122.14}
\]

Thus the sufficient high-order condition is

\[
 {\varepsilon_K\over1-\kappa_K}\to0.
 \tag{T-15122.15}
\]

This is the quantitative closure appropriate to genuinely tensorized Type-II
packets.

## 6. Why varying the window is legitimate

The window changes with `K`, but the spectral exponent does not. For every
finite `K`, the transform of `H^[K+1]`:

1. cancels only boundary pole models;
2. remains nonzero in the open critical counterexample strip;
3. therefore detects exactly the same value `Theta_zeta`.

It is enough to derive a sequence of upper bounds on the same invariant and let
`K` increase. No limiting window or uniform convergence of windows is used.

## 7. Exact review hinge

A full proof through this route requires the complete `CP(K)` estimate of
`M-15112`, including:

- signed packet recombination;
- certified companions and transition residuals;
- terminal Type-I estimates;
- a closed auxiliary system;
- a coefficient rate satisfying (T-15122.11) or (T-15122.15).

The theorem rejects three invalid substitutes:

- a fixed positive exponential rate independent of `K`;
- a decomposition estimate that loses the signed binomial packet by rowwise
  total variation;
- a tensor scale factor tending to one faster than the coefficient rate tends
  to zero.

## 8. Proof boundary

The quantitative composition is complete. The high-order centered packet
estimate producing `epsilon_K` remains the arithmetic hinge of `M-15112`.
