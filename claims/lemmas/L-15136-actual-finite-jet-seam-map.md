# L-15136 — Actual central finite-jet seam map and failure of the seam-radical shortcut

Claim ID: `L-15136`  
Status: **PROVED FROM THE DISPLAYED CONTOUR/SEAM MAPS; CLEAN RADICAL ROUTE DOES NOT FOLLOW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: Shimizu v6/v8 finite-window contour coordinate, common central finite-jet subtraction, seam transpose realization, pairing-preserving seam lift, and singular-boundary comparison map  
Scope: decide the proposed route `D=0`, `q_ell=0` using the actual manuscript maps rather than an abstract finite model  
Related counterexample candidates: none

## 1. Actual maps

For a centered finite window `M`, write

\[
 C_M
 =\iota_M^{\rm cen}P_M^{\rm cen}J_M^{\rm cen}
 \tag{L-15136.1}
\]

for the common linear finite-jet map. The regularized source is

\[
 \Psi_{w,M}^{\rm fw}
 =\widetilde\Psi_{w,M}^{\rm fw}
  -C_M(h_{w,M}^{\rm fw}),
 \qquad
 h_w(u)=\frac{e^{wu}-1}{u}.
 \tag{L-15136.2}
\]

The finite contour coordinate of a logarithmic representative `psi` is

\[
 \epsilon_M^{\rm fp}(\psi)
 \in(\mathfrak S_M^{\rm cfw})',
 \qquad
 \langle\epsilon_M^{\rm fp}(\psi),\eta\rangle
 =\mathcal Z_M(\psi,\eta).
 \tag{L-15136.3}
\]

Let

\[
 \mathcal R_{\partial,R,M}^{\rm fp}
 :(\mathfrak S_M^{\rm cfw})'\to\mathcal D_R'
 \tag{L-15136.4}
\]

be the manuscript's seam-transpose realization, and let

\[
 \mathcal U_{\rm seam}:
 \mathfrak S_M^{\rm cfw}\to\mathcal D_R^\Gamma
 \tag{L-15136.5}
\]

be its fixed readout lift. The pairing theorem gives

\[
 \boxed{
 \left\langle
  \mathcal R_{\partial,R,M}^{\rm fp}(b),
  \mathcal U_{\rm seam}\eta
 \right\rangle_{\partial,R}
 =\langle b,\eta\rangle_{\partial,\rm fp}.}
 \tag{L-15136.6}
\]

Consequently the seam realization is injective on finite coordinates:

\[
 \boxed{
 \mathcal R_{\partial,R,M}^{\rm fp}(b)=0
 \Longrightarrow b=0.}
 \tag{L-15136.7}
\]

Indeed, pair the left side with every lifted readout and use finite-dimensional dual separation.

Finally let

\[
 \mathfrak J_R
 =\Pi_R\,LCI_R\,Tr_{\partial,R}^{\rm cmp}
 \tag{L-15136.8}
\]

be the actual comparison/LCI/projection chain into `mathcal K_R`.

## 2. Raw and jet comparison maps

Fix one finite readout coordinate space `E_(M,N)` with a single logarithmic lift `Lambda_(M,N)`. Define

\[
 \widetilde R_{M,N}e_a
 =\mathfrak J_R
   \mathcal R_{\partial,R,M}^{\rm fp}
   \epsilon_M^{\rm fp}(\widetilde\Lambda_{M,N}e_a),
 \tag{L-15136.9}
\]

and the actual finite-jet comparison map

\[
 C_{M,N}e_a
 =\mathfrak J_R
   \mathcal R_{\partial,R,M}^{\rm fp}
   \epsilon_M^{\rm fp}
   (C_M\Lambda_{M,N}e_a).
 \tag{L-15136.10}
\]

The renormalized comparison map is

\[
 R_{M,N}=\widetilde R_{M,N}-C_{M,N}.
 \tag{L-15136.11}
\]

Let `S_R=S_R*` be the centered seam involution on `mathcal K_R`. In orthonormalized finite readout coordinates put

\[
 A_{M,N}=\widetilde R_{M,N}^*S_R\widetilde R_{M,N},
 \qquad
 K_{M,N}=R_{M,N}^*S_RR_{M,N}.
 \tag{L-15136.12}
\]

The actual finite-jet operator correction is therefore

\[
 \boxed{
 \begin{aligned}
 D_{M,N}:={}&A_{M,N}-K_{M,N}\\
 ={}&\widetilde R_{M,N}^*S_RC_{M,N}
    +C_{M,N}^*S_R\widetilde R_{M,N}
    -C_{M,N}^*S_RC_{M,N}.
 \end{aligned}}
 \tag{L-15136.13}
\]

This formula is the map-level version of the contact operator. It includes the two raw/jet cross channels; it is not merely the self-pairing of the jet range.

## 3. Exact seam-radical criterion

The clean route `D_(M,N)=0` follows from the strong two-sided radical conditions

\[
 \widetilde R_{M,N}^*S_RC_{M,N}=0,
 \qquad
 C_{M,N}^*S_R\widetilde R_{M,N}=0,
 \qquad
 C_{M,N}^*S_RC_{M,N}=0.
 \tag{L-15136.14}
\]

Invariantly, the realized jet range must be `S_R`-orthogonal to both the raw range and itself.

The actual manuscript proves a different statement: the **regular area-type** boundary form vanishes on the regular-trace-vanishing space, while the singular boundary trace supported on the zero-area seam remains nontrivial and is precisely the datum transported into the comparison map. The finite-window weights are carried by

\[
 T_{\partial,R}^{\rm fw}(\phi)
 =\mathcal N_{\rm seam}
   (\mathfrak b_{\rm fp,\partial}^{\rm fw}(\phi)),
 \tag{L-15136.15}
\]

not by the regular area form.

Therefore the manuscript's boundary-cancellation theorem does **not** imply any of the three identities in (L-15136.14). It removes the regular trace while deliberately retaining the singular seam coordinate.

Moreover, by (L-15136.7), the realized finite-jet seam distribution can vanish only if its full contour coordinate vanishes:

\[
 \boxed{
 \mathcal R_{\partial,R,M}^{\rm fp}
 \epsilon_M^{\rm fp}(C_Mh)=0
 \Longrightarrow
 \epsilon_M^{\rm fp}(C_Mh)=0.}
 \tag{L-15136.16}
\]

No such coordinate-annihilation theorem is supplied for the central jets.

## 4. Scalar-probe invisibility

The coefficientwise expansion of the actual central kernel gives

\[
 [w^{\ell-1}]C_M(h_{w,M}^{\rm fw})
 =\frac1{(\ell-1)!}C_M(\chi_Mu^{\ell-2}).
 \tag{L-15136.17}
\]

Hence the displayed linear one-contour jet subtraction is

\[
 \boxed{
 q_{\ell,M}^{\rm lin}
 =\frac1{(\ell-1)!}
 \left\langle
  \epsilon_M^{\rm fp}
  (C_M(\chi_Mu^{\ell-2})),
  \eta_M^{\rm fp}
 \right\rangle.}
 \tag{L-15136.18}
\]

Scalar invisibility would require the fixed probe to annihilate every one of these coordinates. The seam pairing theorem does not imply that one-dimensional orthogonality, and the common use of the subtraction in three ledgers does not imply it either.

## 5. Verdict on route A

The cleaner route would require two new actual identities:

\[
 \epsilon_M^{\rm fp}\circ C_M=0
 \quad\text{after the complete comparison map,}
 \tag{L-15136.19}
\]

and

\[
 \eta_M^{\rm fp}
 \perp\epsilon_M^{\rm fp}(C_M\operatorname{span}\{\chi_Mu^q:q\ge0\}).
 \tag{L-15136.20}
\]

They are not consequences of the contour definitions. The Section 4 construction explicitly preserves nonzero singular boundary traces after regular-trace cancellation. Thus the proposed proof `D=0`, `q_ell=0` fails at the actual map interface, not merely in an abstract model.

This does not assert that a special finite Riemann matrix can never satisfy `D=0` accidentally. It establishes that the displayed central finite-jet range is not proved to be a two-sided seam radical, and that the manuscript's stated cancellation theorem is of the wrong boundary type for that conclusion.

The correct constructive replacement is the nonlinear relative-determinant Ward pullback of `L-15137`.
