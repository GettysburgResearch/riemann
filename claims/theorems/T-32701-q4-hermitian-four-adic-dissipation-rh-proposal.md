# T-32701 — Q=4 Hermitian four-adic dissipation proposal for RH

Claim ID: `T-32701`  
Title: Finite-deformation product routing into fresh four-adic reserve yields a coefficient-one delayed pole-energy recurrence and the Riemann Hypothesis  
Status: **FULL CONDITIONAL PROPOSAL — ONE SOURCE-COMPLETE HERMITIAN ROUTING THEOREM OPEN; RH UNPROVED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: PR #325 `L-32404--L-32412`; PR #337 `L-32708--L-32719`; atomized pole criterion of PR #297/PR #302  
Scope: exact final theorem and complete conditional deduction; no reviewer is asked to invent the missing routing

## 1. Principal pole energy

Let `U(t,theta)` be the ordinary atomized reciprocal-zeta logarithmic current and let

\[
 E(J)=\int_J^{J+\log4}
       \int_{1/4}^{3/4}|U(t,\theta)|^2d\theta dt.
 \tag{T-32701.1}
\]

The existing vector-valued pole criterion gives

\[
 \boxed{E(J)=e^{o(J)}\Longrightarrow\mathrm{RH}.}
 \tag{T-32701.2}
\]

The Q=4 all-pass factor has an exact unitary state realization. Writing the Q=4 pole current as `V`,

\[
 V=\phi_4U+g_4,
 \tag{T-32701.3}
\]

where `g_4` is a uniformly bounded deterministic gauge. On consecutive `log4` slabs,

\[
 \boxed{
 \|U_k\|^2+\|x_k\|^2
 =\|\phi_4U_k\|^2+\|x_{k+1}\|^2.
 }
 \tag{T-32701.4]
\]

(The closing bracket in the tag is typographical only.)

## 2. Complete current-scale ledger already closed

On every sufficiently large quarter-balanced physical row, `L-32715` places simultaneously inside one Q=4 Kummer square:

1. the complete Selberg forcing;
2. the product-source term;
3. both individual source-convolved terms;
4. the true pole-current square.

At least a fixed positive fraction of the reserve remains unused. The finite low-parent, real-X, and adverse unweighted-source rows are explicit polynomial collars.

Thus no current-scale arithmetic estimate remains.

## 3. Finite deformation and exact source typing

For real `tau>=0`,

\[
 J_\tau(s)=A_4(s-\tau)/A_4(s)
\]

has nonnegative coefficients (`L-32712`). After source convolution, the finite reflected difference is a literal Hermitian square. Its imaginary-shift second variation gives the correctly polarized augmented reserve.

The parity pair of `L-32714` forces every product destination into

\[
 4^rq,
 \qquad q\text{ odd},
\]

and gives the exact normal form

\[
 \text{strict descendant at scale }4^{-r}
 +\text{one current-row divisor boundary}.
 \tag{T-32701.5}
\]

The deterministic Q=4 reserve has asymptotic sixteenfold storage on a four-adic lift (`L-32713`), and the exact reserve increment pays the deterministic generalized-prime innovation (`L-32716`).

The true pole innovation is instead

\[
 I_e=\mathcal L_{4e}((\mu*h_4)),
 \tag{T-32701.6}
\]

not the Kummer innovation. `R-32707` makes this source distinction mandatory. `L-32718` proves that its cost is nevertheless a vanishing fraction of the fresh top-scale reserve.

## 4. Sole closing theorem — Q4HFD

The **Q=4 Hermitian Four-adic Dissipation theorem** (`Q4HFD`) is the following finite-deformation statement.

For every sufficiently large logarithmic slab, perform the following operations in this order:

1. form the complete two-frequency finite-`tau` Q=4 Jordan product square;
2. retain both source legs and all independent-frequency cross terms;
3. apply the exact parity decomposition before any norm;
4. route each `4^r q` destination by the product-carry identity of `L-32714`;
5. charge every current-row divisor boundary to the same-row cross energy;
6. charge every strict descendant to the **fresh reserve increment at its destination scale**, never to inherited reserve;
7. take the imaginary-shift second variation at `tau=0` only after this finite positive routing;
8. insert the true-current innovation payment of `L-32718`;
9. leave the Q=4 all-pass terminal state as the sole coefficient-one return.

The resulting physical block inequality must be

\[
 \boxed{
 \begin{aligned}
 &\|\phi_4U_k\|^2
 +\mathcal D_k
 +\mathcal C_k\\
 &\qquad\le
 C(1+k)^A
 +\|x_k\|^2,
 \end{aligned}}
 \tag{Q4HFD}
\]

where

\[
 \mathcal D_k\ge0
\]

is the sum of disjoint fresh four-adic reserve increments and

\[
 \mathcal C_k\ge0
\]

is the remaining current-scale Q=4 reserve/collar form. No copy of principal pole energy occurs on the right except through the single incoming scattering state `x_k`.

Equivalently, after using (T-32701.4) and absorbing the deterministic gauge,

\[
 \boxed{
 E(J)\le C(1+J)^A+E(J-\log4).
 }
 \tag{T-32701.7}
\]

## 5. Conditional completion

Iterating (T-32701.7) through `O(J)` fixed-size slabs gives

\[
 E(J)=O((1+J)^{A+1})=e^{o(J)}.
 \tag{T-32701.8}
\]

The pole criterion (T-32701.2) then yields

\[
 \boxed{Q4HFD\Longrightarrow\mathrm{RH}.}
 \tag{T-32701.9}
\]

No strict contraction of the critical principal mode is requested. Critical-line modes return with coefficient one; an off-line mode would expand under scale and violate the polynomial recurrence.

## 6. Automatic rejection tests

Reject an asserted proof of `Q4HFD` if it does any of the following:

1. replaces the true innovation `mu*h_4` by the deterministic Kummer innovation `h_4`;
2. differentiates the finite deformation before the source/product routing;
3. infers matrix positivity from scalar diagonal positivity;
4. uses the Q=4 all-pass factor to transport the Kummer reserve through `1/zeta`;
5. drops either individual reflected source term;
6. turns the bare-source polylog field into a stand-alone principal estimate;
7. spends `R_4(4e)` once on the current-scale row and again on a descendant;
8. routes a destination with odd two-adic valuation after the parity sum;
9. replaces the exact independent-frequency physical orientation by an arbitrary row Gram;
10. promotes finite computation or PNT-scale `o(n)` cancellation to the required subpower recurrence.

## 7. Exact status

```text
Q4 positive inverse / generalized primes         PROPOSED COMPLETE
Q4 balanced Selberg-Kummer reserve                PROPOSED COMPLETE
true physical current typing                      PROPOSED COMPLETE
bare-source field and adverse collar              PROPOSED COMPLETE
finite Jordan deformation positivity              PROPOSED COMPLETE
correct Hermitian second variation                PROPOSED COMPLETE
four-adic destination normal form                 PROPOSED COMPLETE
asymptotic reserve storage                        PROPOSED COMPLETE
complete current-scale reflected row budget       PROPOSED COMPLETE
true innovation fresh-reserve cost                PROPOSED COMPLETE
Q4HFD finite-deformation descendant routing       OPEN / RH-BEARING
Q4HFD -> coefficient-one recurrence -> RH         COMPLETE CONDITIONAL
Riemann Hypothesis                                UNPROVED
```
