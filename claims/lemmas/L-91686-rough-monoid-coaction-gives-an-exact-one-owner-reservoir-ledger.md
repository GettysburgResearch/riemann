# L-91686 — The rough-monoid coaction gives an exact one-owner native/reservoir ledger

Claim ID: `L-91686`  
Status: **PROVED EXACT SOURCE-OWNERSHIP / NATURALITY THEOREM — POSITIVE NATIVE ENTRY SEPARATE**  
Created: 2026-08-14  
Depends on: unique factorization, `L-91377`, `L-91379`, same-index functor `L-91361/L-91658`  
RH status: **unproved**

## 1. Thresholded rough monoids

For a prime threshold `r>=67`, put
\[
 \mathcal R_{\ge r}
 =\{m\ge1:P^-(m)\ge r\},
\]
with `P^-(1)=infinity`.  For any typed endpoint family `F_X` whose coordinates are additive and obey same-index multiplicative scaling, define the labelled rough lift
\[
 \boxed{
 \mathfrak C_rF_X
 =\bigoplus_{m\in\mathcal R_{\ge r}}
 [m]\otimes m^{-1/2}U_mF_{X/m}.
 }
\tag{L-91686.1}
\]
The label `[m]` is retained until all ownership decisions have been made.

The unlabelled observation is
\[
 \operatorname{Obs}(\mathfrak C_rF_X)
 =\sum_{m\in\mathcal R_{\ge r}}
 m^{-1/2}U_mF_{X/m}.
\tag{L-91686.2}
\]

## 2. Unique least-prime recursion

Every nontrivial `m in R_(>=r)` has one unique decomposition
\[
 m=pu,
 \qquad p=P^-(m)\ge r,
 \qquad u\in\mathcal R_{\ge p}.
\]
Consequently
\[
 \boxed{
 \mathfrak C_rF_X
 =[1]\otimes F_X
 \oplus
 \bigoplus_{p\ge r}p^{-1/2}U_p\mathfrak C_pF_{X/p}.
 }
\tag{L-91686.3}
\]
This is a literal disjoint union of labelled source fibers. Repeating (L-91686.3) records the nondecreasing prime-factor sequence of `m`; no rough source atom has two paths.

Define the counit and reservoir projections by
\[
 \varepsilon([m])=\mathbf1_{m=1},
 \qquad
 \pi_{\rm res}=I-\varepsilon.
\]
Then
\[
 \boxed{
 \varepsilon\mathfrak C_rF_X=F_X,
 \qquad
 \pi_{\rm res}\mathfrak C_rF_X
 =\bigoplus_{m>1}[m]\otimes m^{-1/2}U_mF_{X/m}.
 }
\tag{L-91686.4}
\]

## 3. Naturality for positive source decompositions

Suppose, at every endpoint, a typed source-level identity has been proved:
\[
 F_X=B_X+Z_X,
 \qquad B_X,Z_X\ge0.
\tag{L-91686.5}
\]
Then linearity and same-index covariance give
\[
 \boxed{
 \mathfrak C_rF_X
 =\mathfrak C_rB_X+\mathfrak C_rZ_X
 }
\tag{L-91686.6}
\]
coefficientwise in source, row, ordinary response, radix-four response, score, entropy, and every child-owned port.

Every reservoir fiber inherits the owner it had in (L-91686.5). In particular, the rough lift cannot create a second owner for a source atom.

Conversely, selecting the identity fiber before observation gives the native identity exactly:
\[
 \boxed{F_X=B_X+Z_X.}
\tag{L-91686.7}
\]
The `m>1` reservoir cannot be used as extra native capacity unless it is explicitly assigned to a current or recursive owner.

## 4. Application to the finite-Euler row

For the native full Möbius row `c_X`, `L-91379` is exactly
\[
 \boxed{D_{P_{61},X}=\operatorname{Obs}(\mathfrak C_{67}c_X).}
\tag{L-91686.8}
\]
The identity fiber has
\[
 \Gamma(c_X)=w_X,
 \qquad
 \Xi(c_X)=\Omega_X,
 \qquad
 \mathcal H(c_X)=J_\Lambda(X),
\]
while the `m>1` fibers are the exact positive capacity/benchmark reservoir.

Thus the normalization firewall has a precise categorical meaning:

```text
native datum                    identity fiber m=1;
rough reservoir                 fibers m>1;
least-prime stopping tree       unique recursion (L-91686.3);
finite-Euler observation        forget labels and sum all fibers;
double spending                 observing reservoir as current and exporting it again.
```

## 5. What this proves and does not prove

The theorem closes the formal ownership half of `NRSLI`: once a positive native decomposition is known, its rough lift is source-disjoint and every reservoir atom has one inherited owner.

It does **not** construct the positive native decomposition (L-91686.5), prove the native ordinary/detail inequalities, or bound the `Y_4`-weighted native slack. Those remain the conclusion-producing half of `NRSLI/NRCT`.

```text
rough least-prime ownership                    EXACT
counit native/reservoir split                  EXACT
same-index naturality                          EXACT
finite-Euler = rough lift of native row        EXACT
formal reservoir double-spend firewall         EXACT
positive native entry and Y4 slack             OPEN / RH-BEARING
Riemann Hypothesis                             UNPROVEN
```
