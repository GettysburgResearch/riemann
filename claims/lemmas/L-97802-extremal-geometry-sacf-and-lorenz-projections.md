# L-97802 — Extremal geometry: future-prime tails, SACF projections and Lorenz dual rays

Claim ID: `L-97802`  
Status: **PROVED EXACT STRUCTURAL COMPARISON**  
Created: 2026-08-18  
Depends on: `L-97801`; PR #580; PR #589  
RH status: **unproved**

## 1. The extremal regime is genuinely cofinal

`L-97800` closes every truncated sieve through `z_*(X)=(1+o(1))log X`. Consequently a counterexample sequence to eventual two-row positivity must satisfy `Gamma_23(X)>1` along an unbounded sequence and must be carried by future-prime owners `p>z_*(X)`. No fixed finite active-prime set can be extremal.

This does not identify the extremal with `LAPBR67`. PR #589 proves that `LAPBR67` is false at moving least-prime states: its fixed adaptive depth loses to a seventh rough layer. `FPCB23` instead retains every future-prime depth in the exact least-owner sum (L-97801.5). The PR #589 moving state is a negative control for depth truncation, not the surviving theorem.

## 2. Exact SACF sign geometry after squaring

Take any finite dyadic/product block of (L-97801.5), and write it as

\[
 \mathcal B=\sum_m\mu(m)W_X(m).
\]

Its off-diagonal square is

\[
 |\mathcal B|^2-\sum_mW_X(m)^2
 =2\sum_{m<n}\mu(m)\mu(n)W_X(m)W_X(n).
\tag{L-97802.1}
\]

For squarefree `m,n`, put `d=(m,n)`, `m=da`, `n=db`. Then `a,b,d` are pairwise coprime and

\[
 \boxed{\mu(m)\mu(n)=\mu(a)\mu(b).}
\tag{L-97802.2}
\]

The common divisor is sign-free. On a fixed dyadic activation block the ratio `b/a` is bounded, and the remaining common-divisor interval is literal. Thus (L-97802.1) has exactly the separated coprime Type-II sign geometry isolated as `SACF` in PR #580, with additional least-prime order constraints inherited from `FPCB23`.

This is a structural projection, not an equivalence. SACF controls a square or energy. The future-prime gate is one-sided. Replacing every coefficient by its negative preserves the square and reverses the sign. Hence diagonal/PSD/SACF energy alone cannot certify `Gamma_23<=1` without a phase-sensitive arithmetic input.

## 3. Lorenz/Farkas comparison

At a fixed endpoint, the positive two-row cone is `R_+^2`. Its dual cone is also `R_+^2`, and (L-97801.8) shows that the sharp separating rays are exactly row two and row three. Thus a near-separator for `FPCB23` is a future-prime configuration that nearly exhausts one literal truncated row.

The completed-parity Lorenz dual of PR #589 is richer: its hinge parameter `lambda` simultaneously prices target and scalar coordinates, and its exact Bellman transition is `R^2`. Projecting that ledger onto either component row produces a valid diagnostic for `FPCB23`, but scalar Lorenz feasibility does not imply two nonnegative rows. The vector

\[
 (R_2,R_3)=(-1,2)
\]

has positive `5:3` scalar `5R_2+3R_3=1` while row two is negative.

```text
LAPBR67       fixed-depth large-prime sign; refuted by PR #589;
FPCB23        exact all-depth one-sided future-prime row correlation;
SACF          phase-blind squared Type-II projection of dyadic blocks;
Lorenz dual   target/scalar hinge projection; richer ledger, different cone.
```

The shared arithmetic object is the all-depth future-prime owner profile. The sharp conclusion-producing normalization for the two-row consumer is `Gamma_23`, not a fixed-depth current, square energy, or scalar-only hinge.
