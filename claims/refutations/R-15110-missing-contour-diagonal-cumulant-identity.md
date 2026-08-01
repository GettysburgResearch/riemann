# R-15110 — The missing source theorem is a one-contour/product-contour diagonal cumulant identity

Claim ID: `R-15110`  
Status: **PROVED TYPE-SEPARATION AND NECESSARY-AND-SUFFICIENT DEFECT FORMULA**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: Shimizu v6/v8 finite-window contour definitions; `L-15133`  
Scope: isolate the sole remaining source-level equality after constructing the nonlinear contour-cyclic coefficient  
Related counterexample candidates: none

## 1. Two actual coefficient types

The manuscript's displayed finite classical scalar is obtained from one central logarithmic representative and one fixed Guinand--Weil contour probe:

\[
\mathcal L_M(\psi)
=\mathcal Z_M(\psi,\eta_M^{\rm fp}).
\tag{R-15110.1}
\]

For the central finite-window family

\[
\Psi_{w,M}^{\rm fw}
=\sum_{q\ge0}w^q\psi_{q,M},
\]

define the displayed one-contour coefficient

\[
\boxed{
A^{\rm GW,scalar}_{\ell,M}
=[w^{\ell-1}]
\mathcal Z_M
(\Psi_{w,M}^{\rm fw},\eta_M^{\rm fp})
=\mathcal Z_M(\psi_{\ell-1,M},\eta_M^{\rm fp}).}
\tag{R-15110.2}
\]

By contrast, `L-15133` constructs the connected product-contour coefficient

\[
\boxed{
A^{\rm GW,cyc}_{\ell,M,N}
=
\left[
 \mathcal Z_M^{\otimes\ell}
 \circ(\Lambda_{M,N}\otimes\iota_{M,N})^{\otimes\ell}
\right]
(\operatorname{coev}^{\rm cyc}_{G^\dagger,\ell}).}
\tag{R-15110.3}
\]

These objects have different source types:

\[
A^{\rm GW,scalar}_{\ell,M}
:\mathcal T_{\log,M}\to\mathbb C,
\]

whereas

\[
A^{\rm GW,cyc}_{\ell,M,N}
:(\mathcal T_{\log,M}\otimes E_M)^{\otimes\ell}	o\mathbb C
\]

after cyclic gluing.

The latest manuscript itself says that scalar central tests and cyclic tensor tests are not elements of the same space and must be compared after pullback from a universal coefficient object. The present file identifies the exact pullback still required.

## 2. The cyclic diagonal map

A proof of

\[
A^{\rm GW,scalar}_{\ell,M}
=A^{\rm GW,cyc}_{\ell,M,N}
\tag{R-15110.4}
\]

requires a nonlinear map

\[
\boxed{
\Delta^{\rm CL}_{\ell,M,N}:
\psi_{\ell-1,M}
\longmapsto
\operatorname{coev}^{\rm cyc}_{G^\dagger,\ell}
\text{ decorated by }
(\Lambda_{M,N},\iota_{M,N})^{\otimes\ell}.}
\tag{R-15110.5}
\]

More invariantly, it requires the finite identity

\[
\boxed{
\begin{aligned}
&\mathsf{FP}^{\rm ct}_M
 [\mathcal M_{\rm fw}(\psi_{\ell-1,M},\eta_M^{\rm fp})]\\
&\quad=
(\mathsf{FP}^{\rm ct}_M)^{\otimes\ell}
\left[
 \mathcal M_{\rm fw}^{\otimes\ell}
 \left(
  (\Lambda\otimes\iota)^{\otimes\ell}
  \operatorname{coev}^{\rm cyc}_{G^\dagger,\ell}
 \right)
\right].
\end{aligned}}
\tag{R-15110.6}
\]

The left side is a one-contour finite part. The right side is a product-contour finite part followed by a connected cyclic contraction. Equation (R-15110.6) is the exact scalar/cyclic pullback theorem.

## 3. Genuine order-four defect

Cubic parity makes the final order-three values vanish once the grading is transported. The first nontrivial even defect is

\[
\boxed{
\begin{aligned}
\Delta^{\rm CL}_{4,M,N}
={}&
[w^3]\,
\mathcal Z_M
 (\Psi_{w,M}^{\rm fw},\eta_M^{\rm fp})\\
&-
B_{a_1b_1}(G^\dagger)_{b_1a_2}
B_{a_2b_2}(G^\dagger)_{b_2a_3}\\
&\qquad\cdot
B_{a_3b_3}(G^\dagger)_{b_3a_4}
B_{a_4b_4}(G^\dagger)_{b_4a_1}.
\end{aligned}}
\tag{R-15110.7}
\]

The requested order-four theorem is exactly

\[
\boxed{\Delta^{\rm CL}_{4,M,N}=0.}
\tag{R-15110.8}
\]

At all orders, put

\[
\boxed{
\Delta^{\rm CL}_{\ell,M,N}
=A^{\rm GW,scalar}_{\ell,M}
-A^{\rm GW,cyc}_{\ell,M,N}.}
\tag{R-15110.9}
\]

Then the complete source theorem is

\[
\boxed{
\Delta^{\rm CL}_{\ell,M,N}=0
\quad\text{for every }\ell\ge2,M,N.}
\tag{R-15110.10}
\]

## 4. Why the actual definitions do not yet force the diagonal identity

The contour biform `Z_M`, its fixed probe, and the finite readout Gram determine the product-contour cyclic object of `L-15133`. They do not determine the Taylor vectors `psi_(q,M)` of the separately introduced central source family.

This independence is visible in the smallest exact model. Take one-dimensional spaces with

\[
G=1,
\qquad
\mathcal Z(\psi,\eta)=\psi\eta,
\qquad
B=1,
\qquad
\eta^{\rm fp}=1.
\]

The connected order-four contour cycle is fixed:

\[
A^{\rm GW,cyc}_4=1.
\]

But the two even central families

\[
\Psi_w^{(c)}=c w^3
\]

have the same contour biform, seam tensor, Gram, readout maps, and all coefficients below order four, while

\[
A^{\rm GW,scalar}_4=c.
\]

Choosing `c=1` gives compatibility and choosing `c=0` does not. Thus the one-leg contour data and the lower-order parity data do not logically imply (R-15110.8). One must prove a relation between the central source family and the connected cyclic tensorization.

This is not the earlier homogeneity objection. It is a nonuniqueness theorem for the missing **diagonal lift** while every one-copy contour and readout object is held fixed.

## 5. Counterterms and diagonal contact terms

Tensorizing the finite-part rule gives a well-defined product-contour distribution. Pulling a product distribution back to a diagonal is a separate operation. In general, diagonal pullback can create contact terms supported where contour singularities collide.

Therefore a valid proof of (R-15110.6) must establish all of the following:

1. existence of the cyclic diagonal pullback for the regularized finite-window contour kernels;
2. compatibility of the common finite-jet subtraction with `ell`-fold tensorization;
3. absence, or exact cancellation, of every diagonal contact/counterterm contribution;
4. naturality under window refinement and Moore--Penrose readout reconstruction;
5. connected-cumulant normalization, excluding disconnected cycle partitions.

None of these follows merely from linearity of `FP_M^ct`.

## 6. Necessary and sufficient source theorem

The actual manuscript coefficient equals the sewn coefficient if and only if its central family satisfies the cyclic diagonal identity (R-15110.6). Indeed, the right side is exactly `A^(GW,cyc)=A^sew` by `L-15133`, while the left side is exactly the displayed classical coefficient.

Thus the sole remaining source theorem may be stated without operator language:

```text
For every ell,M,N, the one-contour central coefficient is the connected
cyclic diagonal pullback of ell copies of the finite Guinand--Weil contour
biform, with one Moore--Penrose coevaluation at each gluing and no residual
contact term.
```

## 7. Majorant after compatibility

If (R-15110.10) is proved and

\[
\sup_{M,N}\|K_{M,N}\|_2\le C,
\]

then the existing majorant transfers immediately to the actual classical coefficients:

\[
|A^{\rm GW,scalar}_{\ell,M}|
\le C^\ell,
\]

\[
\sum_{\ell\ge2}
|A^{\rm GW,scalar}_{\ell,M}|r^{\ell-1}
\le\frac{C^2r}{1-Cr}
\qquad(r<1/C).
\]

No second limit theorem is needed. The finite diagonal identity is the only missing input.

## 8. Verdict

The nonlinear universal coefficient object requested by the manuscript now exists explicitly as `L-15133`. Its cyclic pullback equals the sewn trace at every order. The remaining equality with the separately displayed Guinand--Weil scalar coefficient is **not derivable from the published contour definitions without the cyclic diagonal/cumulant identity** (R-15110.6).

That identity is the smallest exact obstruction left at the classical source interface.
