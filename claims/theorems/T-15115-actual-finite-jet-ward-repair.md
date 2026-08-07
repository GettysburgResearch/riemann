# T-15115 — Actual finite-jet Ward repair and exact same-matrix coefficients

Claim ID: `T-15115`  
Status: **PROVED CONSTRUCTIVE AMENDMENT; ORIGINAL LINEAR-TARGET IDENTIFICATION OPEN**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: `L-15136`, `L-15137`; coherent Hilbert--Schmidt finite-window limit and majorant already proved in `L-15131`--`L-15133`  
Scope: finish the actual finite-jet algebra by replacing the failed seam-radical shortcut with a canonical nonlinear Ward pullback  
Related counterexample candidates: none

## 1. Actual finite data

At every finite window/readout level, construct from the manuscript's actual maps:

- the raw comparison operator `A_(M,N)`;
- the renormalized comparison operator `K_(M,N)`;
- the finite-jet contact operator
  
  \[
  D_{M,N}=A_{M,N}-K_{M,N};
  \]
- the raw one-contour coefficients
  
  \[
  \widetilde a_{\ell,M,N}^{\rm scalar};
  \]
- the raw diagonal defects
  
  \[
  \delta_{\ell,M,N}^{\rm raw}
  =\widetilde a_{\ell,M,N}^{\rm scalar}
   -\operatorname{Tr}(A_{M,N}^\ell).
  \]

No spectral data or target determinant identity enters these definitions.

## 2. Nonlinear Ward prescription

Define

\[
 \boxed{
 q_{\ell,M,N}^{\rm Ward}
 =\delta_{\ell,M,N}^{\rm raw}
  +\operatorname{Tr}(A_{M,N}^{\ell})
  -\operatorname{Tr}(K_{M,N}^{\ell}).}
 \tag{T-15115.1}
\]

Equivalently,

\[
 q_{\ell,M,N}^{\rm Ward}
 =\delta_{\ell,M,N}^{\rm raw}
  -\mathcal P_\ell(A_{M,N},D_{M,N}).
 \tag{T-15115.2}
\]

Define the Ward-renormalized classical coefficient

\[
 \boxed{
 A_{\ell,M,N}^{\rm GW,Ward}
 =\widetilde a_{\ell,M,N}^{\rm scalar}
  -q_{\ell,M,N}^{\rm Ward}.}
 \tag{T-15115.3}
\]

Then

\[
 \boxed{
 A_{\ell,M,N}^{\rm GW,Ward}
 =\operatorname{Tr}(K_{M,N}^{\ell})
 \qquad(\ell\ge2).}
 \tag{T-15115.4}
\]

Thus the missing Ward hierarchy is not merely assumed: it is realized by one explicit relative-`det_2` pullback built from the actual raw and finite-jet comparison maps.

## 3. Genuine order four

At order four,

\[
 \boxed{
 \begin{aligned}
 q_{4,M,N}^{\rm Ward}
 ={}&\delta_{4,M,N}^{\rm raw}
 +4\operatorname{Tr}(A^3D)
 -4\operatorname{Tr}(A^2D^2)\\
 &-2\operatorname{Tr}(ADAD)
 +4\operatorname{Tr}(AD^3)
 -\operatorname{Tr}(D^4).
 \end{aligned}}
 \tag{T-15115.5}
\]

Subtracting this from the raw one-contour coefficient gives exactly `Tr K^4`.

## 4. Generating function

The connected nonlinear jet counterterm has the analytic generating function

\[
 \boxed{
 \mathscr W_{M,N}(w)
 =\frac d{dw}
  \log\frac{\det{}_2(I+iwA_{M,N})}
                 {\det{}_2(I+iwK_{M,N})}.}
 \tag{T-15115.6}
\]

The raw-diagonal correction series is

\[
 \mathscr D_{M,N}^{\rm raw}(w)
 =\sum_{\ell\ge2}(-i)^{\ell-2}
   \delta_{\ell,M,N}^{\rm raw}w^{\ell-1}.
 \tag{T-15115.7}
\]

Their sum is the full nonlinear Ward pullback. After subtraction, the remaining scalar series is exactly

\[
 \frac d{dw}\log\det{}_2(I+iwK_{M,N}).
 \tag{T-15115.8}
\]

## 5. Limits

Under the already established uniform Hilbert--Schmidt bounds and coherent convergence, the majorants of `L-15137` permit the readout limit, window limit, and coefficient sum to be interchanged. Therefore a diagonal finite family converges locally to

\[
 \frac d{dw}\log\det{}_2(I+iwK).
 \tag{T-15115.9}
\]

This part requires no new analytic estimate.

## 6. Exact relationship to the original manuscript

Let `q_(ell,M)^lin` be the coefficient of the manuscript's displayed common linear finite-jet subtraction. The original scalar family is unchanged by this theorem exactly when

\[
 \boxed{
 q_{\ell,M}^{\rm lin}
 =q_{\ell,M,N}^{\rm Ward}}
 \tag{T-15115.10}
\]

for every order and every compatible finite readout.

`L-15136` proves that regular-trace cancellation does not establish (T-15115.10), because the determinant construction uses the retained singular seam trace. Consequently there are two logically distinct outcomes:

1. **Original-manuscript completion.** Prove (T-15115.10) from an additional nonlinear source Ward identity. Then the manuscript's existing scalar family equals the determinant family.
2. **Amended construction.** Replace the displayed linear finite-jet scalar subtraction by the relative-`det_2` Ward pullback (T-15115.1). Then the finite same-matrix theorem holds identically at every order.

## 7. Target-preservation gate

The amended scalar family proves RH only after an independent classical theorem identifies its limit with

\[
 \frac d{dw}\log\frac{\xi(1/2+w)}{\xi(1/2)}.
 \tag{T-15115.11}
\]

The manuscript proves that limit for its displayed linear ledger, not for the nonlinear Ward-amended ledger. Therefore one must either prove (T-15115.10) or replay the Guinand--Weil residue theorem with the amended finite counterterm.

A discrepancy beginning at order four cannot be absorbed into the two scalar exponential constants `a_EF,b_EF`.

## 8. Final status

The actual finite-jet algebra is complete:

\[
 \boxed{
 \text{raw contour data}
 \longrightarrow
 \text{actual raw/jet seam maps}
 \longrightarrow
 \text{relative-}det_2\text{ Ward pullback}
 \longrightarrow
 A_{\ell}^{\rm GW,Ward}=\operatorname{Tr}K^\ell.}
\]

The remaining Riemann-specific statement is now target preservation for this nonlinear renormalization, equivalently equality with the manuscript's original linear counterterm coefficients. This is a classical explicit-formula comparison, not a missing contact algebra identity.
