# L-20811 — Gibbs entropy and the prime/power chain rule

Claim ID: `L-20811`  
Title: The full prime-prefix sign is exactly a relative-entropy budget, with a canonical split between prime placement and higher-power truncation  
Status: `PROPOSED — COMPLETE FINITE ENTROPY IDENTITIES AND RÉNYI HIERARCHY`  
Authoring agent: `gpt56-03-v`  
Created: 2026-08-07  
Dependencies: `T-20802`; the log-sum inequality  
Scope: entropy attack on the cofinal prime-prefix theorem  
Related counterexample candidates: none

## 1. Two canonical probability laws on a prefix

For a nonempty prime-power prefix, put

\[
 \psi_j=\sum_{r\le j}\Lambda(q_r)
       =\sum_{p^k\le q_j}\log p.
 \tag{L-20811.1}
\]

This is the ordinary Chebyshev function evaluated at the endpoint prime power.
Define two probability distributions on the same finite set of prime-power
rows:

\[
 \boxed{
 \pi_r={\Lambda(q_r)q_r^{-1/2}\over P_j}
       ={w_r\over P_j},}
 \tag{L-20811.2}
\]

and

\[
 \boxed{
 \rho_r={\Lambda(q_r)\over\psi_j}.}
 \tag{L-20811.3}
\]

Thus `pi` is the critical exponential tilt of the unweighted von Mangoldt law
`rho`:

\[
 {\pi_r\over\rho_r}
 ={\psi_j\over P_j}e^{-\tau_r/2}.
 \tag{L-20811.4}
\]

## 2. Exact Shannon identity

Let

\[
 D_j=D_{\rm KL}(\pi\|\rho)
 =\sum_{r\le j}\pi_r\log{\pi_r\over\rho_r}.
 \tag{L-20811.5}
\]

Using (L-20811.4),

\[
 \boxed{
 D_j=\log{\psi_j\over P_j}-{Q_j\over2P_j}.}
 \tag{L-20811.6}
\]

Define the explicit entropy budget

\[
 \boxed{
 \mathcal K_j
 =\log{\psi_j\over P_j}
  -{A_+^*(P_j)\over2P_j}.}
 \tag{L-20811.7}
\]

Then the Fenchel reserve is exactly

\[
 \boxed{
 M_j=2P_j(\mathcal K_j-D_j).}
 \tag{L-20811.8}
\]

Consequently

\[
 \boxed{
 M_j\ge0
 \iff
 D_{\rm KL}(\pi\|\rho)\le\mathcal K_j.}
 \tag{L-20811.9}
\]

The RH-facing sign is therefore not an unspecified cancellation between two
large prime moments. It is the assertion that the information cost of the
critical Gibbs tilt fits inside one explicit archimedean entropy budget.

## 3. Exact chain rule over base primes

For a base prime `p`, let

\[
 K_p=\max\{k:p^k\le q_j\},
 \quad
 S_{p,K}=\sum_{k=1}^Kp^{-k/2},
 \quad
 T_{p,K}=\sum_{k=1}^Kk p^{-k/2}.
 \tag{L-20811.10}
\]

The prime marginals of `pi` and `rho` are

\[
 \boxed{
 \Pi_p={\log p\,S_{p,K_p}\over P_j},
 \qquad
 R_p={K_p\log p\over\psi_j}.}
 \tag{L-20811.11}
\]

Conditioned on the base prime, the power laws are

\[
 \boxed{
 g_{p,k}={p^{-k/2}\over S_{p,K_p}},
 \qquad
 u_{p,k}={1\over K_p}.}
 \tag{L-20811.12}
\]

The relative-entropy chain rule gives the exact orthogonal split

\[
 \boxed{
 D_j
 =D_{\rm KL}(\Pi\|R)
  +\sum_{p\le q_j}\Pi_p
    D_{\rm KL}(g_p\|u_p).}
 \tag{L-20811.13}
\]

The conditional power cost is elementary:

\[
 \boxed{
 D_{\rm KL}(g_p\|u_p)
 =\log{K_p\over S_{p,K_p}}
  -{\log p\over2}{T_{p,K_p}\over S_{p,K_p}}.}
 \tag{L-20811.14}
\]

It vanishes exactly when `K_p=1`. Hence (L-20811.13) separates:

1. the placement of the base primes; and
2. the complete, explicit entropy debit caused by retaining only finitely many
   powers of each base prime.

This is the entropy counterpart of the finite Euler-factor defect in
`L-20812`.

## 4. Rényi hierarchy

For `alpha>1`, define

\[
 R_{\alpha,j}
 =\sum_{r\le j}\Lambda(q_r)q_r^{-\alpha/2}.
 \tag{L-20811.15}
\]

The order-`alpha` Rényi divergence is exactly

\[
 \boxed{
 D_\alpha(\pi\|\rho)
 ={1\over\alpha-1}
 \log\left(
 {\psi_j^{\alpha-1}R_{\alpha,j}\over P_j^\alpha}
 \right).}
 \tag{L-20811.16}
\]

Since `D_KL<=D_alpha`, one obtains the finite lower bound

\[
 \boxed{
 Q_j\ge
 {2P_j\over\alpha-1}
 \log{P_j\over R_{\alpha,j}}.}
 \tag{L-20811.17}
\]

Therefore the directed finite inequality

\[
 \boxed{
 {2P_j\over\alpha-1}
 \log{P_j\over R_{\alpha,j}}
 \ge A_+^*(P_j)}
 \tag{L-20811.18}
\]

is a sufficient certificate for the prefix reserve `M_j>=0`. It involves only
three positive finite prime moments and one explicit archimedean barrier.

As `alpha` decreases to one, (L-20811.16) converges to the exact Shannon
identity and (L-20811.17) converges to equality.

## 5. Shrinking-strip interpretation

Write

\[
 \alpha=1+2\omega.
 \tag{L-20811.19}
\]

Then

\[
 R_{1+2\omega,j}
 =\sum_{q\le q_j}{\Lambda(q)\over q^{1/2+\omega}},
 \tag{L-20811.20}
\]

so the Rényi lower bound becomes

\[
 \boxed{
 Q_j\ge{P_j\over\omega}
 \log{P_j\over R_{1+2\omega,j}}.}
 \tag{L-20811.21}
\]

This is the finite positive shifted-line statistic used in `T-20803`. The
critical Shannon theorem is approached from the right of `Re s=1/2`, without
analytic continuation and without assigning any zero ordinate.

## 6. Why a fixed Rényi order cannot close the RH scale

Fix `1<alpha<2`. Partial summation and the prime number theorem give, with
`X=q_j`,

\[
 P_j\sim2\sqrt X,
 \qquad
 Q_j\sim2\sqrt X(\log X-2),
 \tag{L-20811.22}
\]

and

\[
 R_{\alpha,j}
 \sim {X^{1-\alpha/2}\over1-\alpha/2}.
 \tag{L-20811.23}
\]

Hence the generic Rényi loss satisfies

\[
 \boxed{
 Q_j-
 {2P_j\over\alpha-1}
 \log{P_j\over R_{\alpha,j}}
 \sim c_\alpha P_j,}
 \tag{L-20811.24}
\]

where

\[
 \boxed{
 c_\alpha
 =-2-{2\over\alpha-1}\log(2-\alpha)>0.}
 \tag{L-20811.25}
\]

For `alpha=1+epsilon`,

\[
 c_\alpha=\epsilon+O(\epsilon^2).
 \tag{L-20811.26}
\]

Thus a fixed order loses a quantity of order `P_j`, while the RH reserve is of
constant or smaller scale. To make the universal Rényi loss `O(1)`, one must
enter the shrinking regime

\[
 \alpha_j-1=O(P_j^{-1}),
 \tag{L-20811.27}
\]

and to make it `o(1)` one needs `o(P_j^-1)`. This is why `T-20803` uses the
much thinner offset `omega_j=P_j^-2`.

The conclusion is a scope correction: fixed-line Euler-product or Rényi bounds
cannot finish the theorem merely by improving constants. The proof must resolve
a strip whose width shrinks with the prefix.

## 7. Proof boundary

- The Shannon, chain-rule, and Rényi identities are exact finite algebra.
- The PNT asymptotics only classify the loss of a fixed Rényi order; they do not
  prove the Shannon budget.
- The prime marginal entropy in (L-20811.13) remains the load-bearing arithmetic
  term.
- `T-20803` converts the limiting Shannon problem into one explicit shrinking-
  strip inequality with a vanishing deterministic tolerance.
- No RH proof is claimed.