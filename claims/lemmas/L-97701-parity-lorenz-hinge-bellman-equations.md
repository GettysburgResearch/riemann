# L-97701 — Completed-parity Lorenz feasibility is an exact two-channel hinge Bellman equation

Claim ID: `L-97701`  
Status: **PROVED EXACT FINITE-DIMENSIONAL REDUCTION**  
Created: 2026-08-18  
Depends on: `L-97601` owner ledger and `L-97603/L-97611` scalar Lorenz primal-dual  
RH status: **unproved**

## 1. Hinge form of the Lorenz dual

At one fully expanded finite owner ledger, let the even atoms be indexed by `E`
and the odd atoms by `O`.  Write an atom as

\[
(a_i,t_i,r_i),\qquad a_i\ge0,\quad t_i>0,
\]

where `a_i` is capacity and `(t_i,r_i)` are its target and scalar coordinates.
Put

\[
T_E=\sum_{i\in E}a_it_i,
\quad R_E=\sum_{i\in E}a_ir_i,
\]

and analogously `T_O,R_O`.

Define the oriented hinge deficits

\[
\boxed{
D^+(\lambda)
=\lambda T_O+
\sum_{i\in E}a_i(r_i-\lambda t_i)_+-R_O,
}
\tag{L-97701.1}
\]

and

\[
\boxed{
D^-(\lambda)
=\lambda T_E+
\sum_{i\in O}a_i(r_i-\lambda t_i)_+-R_E.
}
\tag{L-97701.2}
\]

The finite Lorenz theorem implies

\[
\boxed{
\text{even source can meet the complete odd target/scalar demand}
\iff
D^+(\lambda)\ge0\quad\text{for every }\lambda\in\mathbb R.
}
\tag{L-97701.3}
\]

No separate target-capacity clause is needed in the all-`lambda` formulation.
Indeed, if `T_O>T_E`, then as `lambda -> -infinity`, every hinge is active and

\[
D^+(\lambda)
=(R_E-R_O)+\lambda(T_O-T_E)\to-\infty.
\]

When `T_O<=T_E`, minimizing (L-97701.1) is exactly the fractional-knapsack
Lorenz dual of `L-97603`.

For a fixed ledger, `D^+` is continuous piecewise affine.  Its only finite
breakpoints are the even ratios

\[
\theta_i=r_i/t_i.
\]

Thus a finite endpoint can be checked exactly by the finitely many hinge
breakpoints together with the two affine tails.

## 2. Additivity, scaling and parity swap

The deficits have three exact functorial properties.

### Disjoint source union

If ledgers `A,B` have disjoint atom ownership, then

\[
D^\pm_{A\oplus B}(\lambda)
=D^\pm_A(\lambda)+D^\pm_B(\lambda).
\tag{L-97701.4}
\]

### Positive source scaling

If every capacity in a ledger is multiplied by `rho>=0`, then

\[
D^\pm_{\rho A}(\lambda)=\rho D^\pm_A(\lambda).
\tag{L-97701.5}
\]

### Parity swap

If `S` exchanges even and odd ownership, then

\[
D^+_{SA}=D^-_A,
\qquad
D^-_{SA}=D^+_A.
\tag{L-97701.6}
\]

These statements are immediate from (L-97701.1)--(L-97701.2), but they are
load-bearing because the rough owner recursion is exactly a disjoint union of
positively scaled parity-swapped children.

## 3. Exact future-prime Bellman system

Use the unique least-prime rough recursion of `L-97601/L-96502`.  At a state `v`
with endpoint `X_v` and least allowed rough prime, write `b_v` for its local
no-further-rough-prime base ledger and `v_p` for the child obtained by assigning
first ownership to rough prime `p`.  The owner identity is

\[
P_v=b_v\oplus
\bigoplus_{p\in\mathcal P(v)}p^{-1/2}S P_{v_p}.
\tag{L-97701.7}
\]

Applying (L-97701.4)--(L-97701.6) gives the exact coupled equations

\[
\boxed{
D_v^+(\lambda)
=d_v^+(\lambda)+
\sum_{p\in\mathcal P(v)}p^{-1/2}D_{v_p}^-(\lambda),
}
\tag{L-97701.8}
\]

\[
\boxed{
D_v^-(\lambda)
=d_v^-(\lambda)+
\sum_{p\in\mathcal P(v)}p^{-1/2}D_{v_p}^+(\lambda),
}
\tag{L-97701.9}
\]

where `d_v^\pm` are the two oriented deficits of the local base ledger `b_v`.
Every sum is finite because the endpoint strictly decreases and the completed
rough history has finite nilpotence depth.

Let `R` denote the literal positive least-prime child operator.  Then

\[
D^+=d^+ + R D^-,
\qquad
D^-=d^- + R D^+.
\tag{L-97701.10}
\]

Eliminating the opposite parity gives

\[
\boxed{
(I-R^2)D^+=g^+,
\qquad
g^+=d^+ + R d^-.
}
\tag{L-97701.11}
\]

Likewise `(I-R^2)D^-=d^-+Rd^+`.
Since `R` is nilpotent,

\[
\boxed{
D^+=(I-R^2)^{-1}g^+
=\sum_{k\ge0}R^{2k}g^+,
}
\tag{L-97701.12}
\]

with a finite positive sum.

Equation (L-97701.12) is the exact Lorenz-dual analogue of the parity resolvent.
It keeps the native source, all future primes, cumulative parity, and the exact
hinge parameter `lambda` in one state equation.

## 4. Exact Bellman barrier criterion

For every state and hinge parameter, let `B_v(lambda)` be any explicit function
such that

\[
B_v(\lambda)\ge0
\tag{L-97701.13}
\]

and

\[
\boxed{
B_v(\lambda)
\le
g_v^+(\lambda)+(R^2B)_v(\lambda).
}
\tag{L-97701.14}
\]

At terminal states `R^2B=0`, so the same inequality applies.
Backward induction on the finite rough rank and (L-97701.11) give

\[
D_v^+(\lambda)\ge B_v(\lambda)\ge0.
\tag{L-97701.15}
\]

Hence a barrier satisfying (L-97701.13)--(L-97701.14) for every real `lambda`
proves scalar completed-parity feasibility at every state.

Conversely, if scalar feasibility holds, `B=D^+` is itself a nonnegative barrier
with equality.  Therefore existence of a nonnegative future-prime Bellman
barrier is **equivalent**, not merely sufficient, to the completed-parity scalar
Lorenz theorem.

The research problem is now constructive: exhibit a lower-dimensional explicit
`B` from source data without using the unknown `D^+` itself.

## 5. Why this formulation is useful

The equation explains simultaneously why the previous local approaches failed:

- a one-channel local current discards the `D^-` channel;
- a disjoint reserve does not enter the same hinge deficit;
- fixed even-depth truncation approximates the positive resolvent by a current
  whose local Bellman source can have the wrong sign;
- a future-prime quotient profile is natural because `R^2` is the exact Markov
  transition in the parity-restored Bellman equation.

It also gives an exact fail-closed separator.  If no barrier exists at a finite
endpoint, the original Lorenz LP supplies an optimizing `lambda`, and that same
hinge is a concrete negative `D^+` witness.
