# L-15137 — Actual relative-det2 Ward pullback for the central finite jet

Claim ID: `L-15137`  
Status: **PROVED CONSTRUCTIVE FINITE SOURCE THEOREM**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: `L-15136`; finite Carleman--Fredholm determinant calculus; cyclic trace expansion  
Scope: construct the missing nonlinear Ward pullback from the manuscript's actual raw and finite-jet comparison maps  
Related counterexample candidates: none

## 1. Actual finite operators

Use the actual maps of `L-15136` and put, at one finite window/readout level,

\[
 A=A_{M,N}
 =\widetilde R_{M,N}^*S_R\widetilde R_{M,N},
 \tag{L-15137.1}
\]

\[
 K=K_{M,N}
 =R_{M,N}^*S_RR_{M,N},
 \qquad
 R_{M,N}=\widetilde R_{M,N}-C_{M,N},
 \tag{L-15137.2}
\]

and

\[
 D=A-K.
 \tag{L-15137.3}
\]

All three are finite self-adjoint operators in the same orthonormalized readout space. Equation `L-15136.13` expresses `D` entirely in terms of the actual raw map, actual finite-jet map, and actual seam involution.

## 2. Relative determinant Ward functional

Define the nonlinear finite-jet Ward pullback by the relative regularized determinant

\[
 \boxed{
 \mathscr W_{M,N}(w)
 =\frac d{dw}
  \log\frac{\det{}_2(I+iwA)}
                 {\det{}_2(I+iwK)}.}
 \tag{L-15137.4}
\]

This is constructed from the actual finite maps. It is invariant under finite readout coordinate changes and contains no chosen zeta zeros or target determinant identity.

For `|w|` below both inverse operator norms,

\[
 \boxed{
 \mathscr W_{M,N}(w)
 =\sum_{\ell=2}^{\infty}
  (-i)^{\ell-2}
  q_{\ell,M,N}^{\rm rel}
  w^{\ell-1},}
 \tag{L-15137.5}
\]

where

\[
 \boxed{
 q_{\ell,M,N}^{\rm rel}
 =\operatorname{Tr}(A^\ell)
  -\operatorname{Tr}(K^\ell).}
 \tag{L-15137.6}
\]

Since `K=A-D`, the all-orders contact polynomial of `L-15134` satisfies

\[
 \boxed{
 q_{\ell,M,N}^{\rm rel}
 =-\mathcal P_\ell(A,D).}
 \tag{L-15137.7}
\]

Thus the relative determinant is exactly the connected nonlinear counterterm required to remove every mixed finite-jet contact loop.

## 3. Genuine order four

At the first nontrivial even order,

\[
 \boxed{
 \begin{aligned}
 q_{4,M,N}^{\rm rel}
 ={}&4\operatorname{Tr}(A^3D)
 -4\operatorname{Tr}(A^2D^2)\\
 &-2\operatorname{Tr}(ADAD)
 +4\operatorname{Tr}(AD^3)
 -\operatorname{Tr}(D^4).
 \end{aligned}}
 \tag{L-15137.8}
\]

### Proof

Subtract the exact cyclic expansion of `Tr(A-D)^4` from `Tr A^4`. No commutativity assumption is used. QED.

This is the nonlinear quartic source pullback missing from the displayed linear central-jet subtraction.

## 4. Raw diagonal defect and complete Ward counterterm

Let

\[
 \widetilde a_{\ell,M,N}^{\rm scalar}
 \tag{L-15137.9}
\]

be the actual raw one-contour coefficient before finite-jet subtraction. The raw connected contour cycle of the same finite readout is `Tr A^ell`. Define the measured raw diagonal defect

\[
 \boxed{
 \delta_{\ell,M,N}^{\rm raw}
 =\widetilde a_{\ell,M,N}^{\rm scalar}
  -\operatorname{Tr}(A^\ell).}
 \tag{L-15137.10}
\]

Every quantity in (L-15137.10) is determined by the actual finite contour and actual finite readout data.

Define the **complete nonlinear Ward pullback**

\[
 \boxed{
 q_{\ell,M,N}^{\rm Ward}
 =\delta_{\ell,M,N}^{\rm raw}
  +q_{\ell,M,N}^{\rm rel}.}
 \tag{L-15137.11}
\]

Equivalently,

\[
 \boxed{
 q_{\ell,M,N}^{\rm Ward}
 =\delta_{\ell,M,N}^{\rm raw}
  -\mathcal P_\ell(A,D).}
 \tag{L-15137.12}
\]

This is precisely the Ward identity requested in `T-15114`, now promoted from a condition to an explicit construction using the actual raw scalar, raw comparison operator, and renormalized comparison operator.

## 5. Exact corrected scalar identity

Define the Ward-renormalized one-contour coefficient by

\[
 \boxed{
 A_{\ell,M,N}^{\rm GW,Ward}
 =\widetilde a_{\ell,M,N}^{\rm scalar}
  -q_{\ell,M,N}^{\rm Ward}.}
 \tag{L-15137.13}
\]

Then, identically at every finite level and every order,

\[
 \boxed{
 A_{\ell,M,N}^{\rm GW,Ward}
 =\operatorname{Tr}(K_{M,N}^\ell).}
 \tag{L-15137.14}
\]

### Proof

Using (L-15137.10)--(L-15137.11),

\[
\begin{aligned}
 A_{\ell}^{\rm GW,Ward}
 &=\widetilde a_\ell
  -\delta_\ell^{\rm raw}
  -\operatorname{Tr}A^\ell
  +\operatorname{Tr}K^\ell\\
 &=\operatorname{Tr}K^\ell.
\end{aligned}
\]

QED.

At order four,

\[
 \boxed{
 q_{4}^{\rm Ward}
 =\delta_4^{\rm raw}
 +4\operatorname{Tr}(A^3D)
 -4\operatorname{Tr}(A^2D^2)
 -2\operatorname{Tr}(ADAD)
 +4\operatorname{Tr}(AD^3)
 -\operatorname{Tr}D^4.}
 \tag{L-15137.15}
\]

## 6. One majorant

Assume

\[
 \|A_{M,N}\|_2\le C,
 \qquad
 \|K_{M,N}\|_2\le C
 \tag{L-15137.16}
\]

uniformly. Then

\[
 |q_{\ell,M,N}^{\rm rel}|
 \le2C^\ell,
 \tag{L-15137.17}
\]

and, for `r<1/C`,

\[
 \boxed{
 \sum_{\ell=2}^{\infty}
 |q_{\ell,M,N}^{\rm rel}|r^{\ell-1}
 \le\frac{2C^2r}{1-Cr}.}
 \tag{L-15137.18}
\]

If the raw scalar and raw cyclic ledgers each obey the already declared bound `C^ell`, then

\[
 |\delta_{\ell,M,N}^{\rm raw}|\le2C^\ell,
\]

and the complete Ward counterterm satisfies

\[
 \boxed{
 \sum_{\ell=2}^{\infty}
 |q_{\ell,M,N}^{\rm Ward}|r^{\ell-1}
 \le\frac{4C^2r}{1-Cr}.}
 \tag{L-15137.19}
\]

Thus the nonlinear amendment has one geometric majorant and is compatible with the existing readout, window, and Hilbert--Schmidt limits.

## 7. Relation to the manuscript's displayed linear subtraction

The manuscript currently supplies the linear coefficient `q_(ell,M)^lin` of `L-15136.18`. The nonlinear Ward theorem proves the original finite scalar identity exactly if and only if

\[
 \boxed{
 q_{\ell,M}^{\rm lin}
 =q_{\ell,M,N}^{\rm Ward}}
 \tag{L-15137.20}
\]

for every retained finite readout. When (L-15137.20) is not proved, (L-15137.13) is a mathematically complete **amended renormalization prescription**, not a proof that the manuscript's original linear prescription already has the same coefficients.

The amendment is not arbitrary: it is the unique connected relative-`det_2` counterterm normalized to vanish when the finite-jet comparison map vanishes and to enforce the same-matrix cyclic identity at every order.

## 8. Proof boundary

This lemma completes route B constructively for the actual finite maps. It does not show that the Ward-renormalized classical ledger retains the manuscript's independently claimed limit to `xi'/xi`. To preserve that target without amendment, one must prove (L-15137.20), or prove that the difference tends to zero in the classical limit. Since a quartic difference cannot be absorbed into the two central exponential constants, this remains a substantive source comparison.
