# T-15112 — Sewn classical source coefficients and one uniform majorant give the determinant limit

Claim ID: `T-15112`  
Status: **PROVED CONDITIONAL COMPOSITION THEOREM; CLASSICAL TENSOR IDENTIFICATION OPEN**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: `L-15129`--`L-15132`; regularized determinant continuity  
Scope: exact repaired source interface for the finite-window determinant programme  
Related counterexample candidates: none

## 1. Finite source data

For every finite window/readout pair `(M,N)`, let

\[
 U_{M,N}:E_{M,N}\to H_M,
 \qquad
 G_{M,N}=U_{M,N}^*U_{M,N},
\]

and let `S_M=S_M*`. Put

\[
 B_{M,N}=U_{M,N}^*S_MU_{M,N}.
\]

Define the **sewn finite coefficient** by the Moore--Penrose closed loop

\[
\boxed{
 A_{\ell,M,N}^{\rm sew}
 =\operatorname{Sew}_\ell(U_{M,N},S_M).}
 \tag{T-15112.1}
\]

Then `L-15132` gives

\[
\boxed{
 A_{\ell,M,N}^{\rm sew}
 =\operatorname{Tr}(K_{M,N}^\ell),}
 \tag{T-15112.2}
\]

where

\[
 K_{M,N}=P_{U_{M,N}}S_MP_{U_{M,N}}|_{\operatorname{Ran}U_{M,N}}.
\]

## 2. One all-orders majorant

Assume

\[
 \sup_{M,N}\|K_{M,N}\|_2\le C.
 \tag{T-15112.3}
\]

Then for `|w|<1/C`,

\[
 \sum_{\ell\ge2}
 |A_{\ell,M,N}^{\rm sew}|\,|w|^{\ell-1}
 \le\frac{C^2|w|}{1-C|w|}.
 \tag{T-15112.4}
\]

Thus the readout limit, window limit, and series sum may be interchanged by one
geometric majorant.

## 3. Coherent Hilbert--Schmidt limit

Suppose a diagonal sequence satisfies

\[
 K_{M_j,N_j}\to K
 \quad\text{in }\mathfrak S_2,
 \tag{T-15112.5}
\]

with `K=K*`. Then

\[
\boxed{
 \lim_j
 \sum_{\ell\ge2}(-i)^{\ell-2}
 A_{\ell,M_j,N_j}^{\rm sew}w^{\ell-1}
 =
 w\operatorname{Tr}\bigl(K^2(I+iwK)^{-1}\bigr)}
 \tag{T-15112.6}
\]

locally uniformly on `|w|<1/C`. The right side is

\[
 \frac d{dw}\log\det{}_2(I+iwK).
\]

## 4. Exact classical pullback gate

Let `A_(ell,M,N)^GW` be the coefficient independently obtained from the
manuscript's Guinand--Weil/Cauchy--Laplace contour ledger. A valid source
interface must prove

\[
\boxed{
 A_{\ell,M,N}^{\rm GW}
 =A_{\ell,M,N}^{\rm sew}}
 \tag{T-15112.7}
\]

for every `ell,M,N` from the actual contour definitions.

The displayed one-probe finite-part coordinate does not imply (T-15112.7), by
`R-15109`. The missing theorem must exhibit the cyclic tensor lift and one
Moore--Penrose coevaluation at every gluing.

If (T-15112.7) is proved, and the independent classical limit is

\[
 \sum_{\ell\ge2}(-i)^{\ell-2}
 A_{\ell,M_j,N_j}^{\rm GW}w^{\ell-1}
 \longrightarrow
 \frac d{dw}\log\frac{\xi(1/2+w)}{\xi(1/2)},
 \tag{T-15112.8}
\]

then the determinant identity and RH follow by `T-15111`.

## 5. Exact status

The source-sewing formula, coordinate invariance, and common majorant are now
proved. The source-specific equality (T-15112.7) is not proved by the accessible
manuscript text. Since its complete even hierarchy is equivalent to the target
determinant identity, this is the exact RH-bearing interface.
