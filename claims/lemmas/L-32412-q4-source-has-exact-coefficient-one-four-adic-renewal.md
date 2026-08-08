# L-32412 — The Q=4 source has an exact four-adic renewal, and its compact innovation remains RH-bearing

Claim ID: `L-32412`  
Status: **PROPOSED COMPLETE EXACT RENEWAL / SCOPE FIREWALL — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `L-32404`, corrected `L-32407`; elementary Dirichlet algebra

## 1. Exact source renewal

Let `delta_4` denote the Dirichlet atom at `4`. The local source comb of `L-32404` is

\[
 e_4=\varepsilon-3\delta_4-3\delta_{16}-3\delta_{64}-\cdots.
\]

Its local generating function is

\[
 \frac{1-4x}{1-x}.
\]

Therefore coefficientwise

\[
 \boxed{
 e_4=(\varepsilon-4\delta_4)+\delta_4*e_4.
 }
 \tag{L-32412.1}
\]

Let

\[
 c_4=e_4*\Lambda_4
\]

be the correctly typed physical interval coefficient of `L-32407`. Then

\[
 \boxed{
 c_4=h_4+\delta_4*c_4,
 \qquad
 h_4=(\varepsilon-4\delta_4)*\Lambda_4.
 }
 \tag{L-32412.2}
\]

## 2. Prefix and physical-field recurrence

Put

\[
 G_4(X)=\sum_{m\le X}c_4(m),
 \qquad
 \Psi_4(X)=\sum_{m\le X}\Lambda_4(m).
\]

Summing (L-32412.2) gives, for every real `X>=1`,

\[
 \boxed{
 G_4(X)=G_4(X/4)+\Psi_4(X)-4\Psi_4(X/4).
 }
 \tag{L-32412.3}
\]

Let

\[
 \mathcal Q_4(X,\theta)
 =G_4(X)-G_4(\theta X)-G_4((1-\theta)X)
\]

be the unnormalized physical Jensen field, and define the compact innovation

\[
 \mathcal I_4(X,\theta)
 =H_4(X)-H_4(\theta X)-H_4((1-\theta)X),
\]

where

\[
 H_4(X)=\Psi_4(X)-4\Psi_4(X/4).
\]

Then exactly

\[
 \boxed{
 \mathcal Q_4(X,\theta)
 =\mathcal Q_4(X/4,\theta)+\mathcal I_4(X,\theta).
 }
 \tag{L-32412.4}
\]

At critical square-root normalization,

\[
 \mathfrak P_4(X,\theta)=X^{-1/2}\mathcal Q_4(X,\theta),
 \qquad
 \mathfrak I_4(X,\theta)=X^{-1/2}\mathcal I_4(X,\theta),
\]

so

\[
 \boxed{
 \mathfrak P_4(X,\theta)
 =\frac12\mathfrak P_4(X/4,\theta)
 +\mathfrak I_4(X,\theta).
 }
 \tag{L-32412.5}
\]

This is an exact four-adic renewal, not an estimated recurrence.

## 3. Closed formula for the generalized-prime prefix

If `R=floor(log_4 X)`, the local correction in `Lambda_4` gives

\[
 \Psi_4(X)
 =\psi(X)+(\log4)
  \left[
   \frac{4^{R+1}-4}{3}-R
  \right].
 \tag{L-32412.6}
\]

Consequently

\[
 \boxed{
 H_4(X)
 =\psi(X)-4\psi(X/4)+3R\log4.
 }
 \tag{L-32412.7}
\]

The deterministic linear density cancels exactly. The innovation is a compact quarter-scale Chebyshev discrepancy plus one explicit logarithmic staircase.

## 4. The compact innovation is not an elementary remainder

In Dirichlet variables the innovation coefficient is

\[
 h_4=(\varepsilon-4\delta_4)*\Lambda_4.
\]

Hence its interval-field multiplier is

\[
 \boxed{
 (1-4^{1-s})L_4(s)N_\theta(s).
 }
 \tag{L-32412.8}
\]

Every zero of `1-4^(1-s)` lies on `Re(s)=1`. Every nontrivial zeta zero lies in `0<Re(s)<1`. Therefore the factor `1-4^(1-s)` cannot cancel a nontrivial zeta zero.

At a zero `rho` of multiplicity `m_rho`, the residue of (L-32412.8) is

\[
 \boxed{
 -m_\rho(1-4^{1-\rho})N_\theta(\rho)\ne0
 }
 \tag{L-32412.9}
\]

as a carry-position vector.

Thus a subexponential bound for the compact innovation by itself is still an RH-strength theorem. Equation (L-32412.5) is useful as an exact state transition, but it does not turn the innovation into a soft error term.

## 5. Relation to the all-pass state

The renewal (L-32412.5) and the unitary scattering realization of `L-32406` are two compatible descriptions of the same local Euler factor:

```text
coefficient/source coordinate:
    one strict 1/2 delayed copy + compact innovation;

critical-frequency coordinate:
    one unit-modulus all-pass transform + deterministic gauge.
```

The apparent strict `1/2` in the first description does not contradict critical neutrality because the compact innovation carries the complementary zeta-zero residue. A valid proof must dissipate that innovation through the source-bound reflected/Selberg ledger; it cannot simply declare it polylogarithmic.

## 6. Proof boundary

Closed exactly:

1. source-comb renewal;
2. prefix renewal;
3. physical-field renewal;
4. critical-normalized coefficient `1/2` delay;
5. closed Chebyshev formula for the compact innovation;
6. proof that the innovation remains RH-bearing.

Open:

1. a dissipative reflected estimate for the innovation;
2. combination with the all-pass terminal state into a coefficient-one block recurrence;
3. RH.
