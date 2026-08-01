# L-15135 — Actual central-kernel jet coefficients and degree separation

Claim ID: `L-15135`  
Status: **PROVED FROM THE DISPLAYED CENTRAL KERNEL; NONLINEAR WARD MATCH OPEN**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: Shimizu v6/v8 central-kernel and common-counterterm definitions; `L-15134`  
Scope: identify the actual one-contour finite-jet coefficient at every order  
Related counterexample candidates: none

## 1. Displayed central kernel

The manuscript fixes

\[
 h_w(u)=\frac{e^{wu}-1}{u},
 \qquad h_w(0)=w.
 \tag{L-15135.1}
\]

Hence, as an entire power series in `w`,

\[
\boxed{
 h_w(u)=\sum_{n=1}^{\infty}
 \frac{w^n}{n!}u^{n-1}.}
 \tag{L-15135.2}
\]

Let `chi_M` denote the finite-window cutoff, independent of `w`, and write

\[
 h_{w,M}^{\rm fw}=\chi_M h_w.
\]

The common finite-jet counterterm is

\[
 C_M(h)
 =\iota_M^{\rm cen}P_M^{\rm cen}J_M^{\rm cen}(h).
 \tag{L-15135.3}
\]

All maps in (L-15135.3) are linear.

## 2. Coefficientwise counterterm formula

For `ell>=2`, the coefficient of `w^(ell-1)` in the counterterm is

\[
\boxed{
 [w^{\ell-1}]\,C_M(h_{w,M}^{\rm fw})
 =\frac{1}{(\ell-1)!}
 C_M\!\left(\chi_M(u)u^{\ell-2}\right).}
 \tag{L-15135.4}
\]

### Proof

Insert (L-15135.2), multiply by the fixed cutoff, and use linearity of every map
in (L-15135.3). QED.

Pairing with the manuscript's fixed finite-part probe gives the actual
one-contour counterterm coefficient

\[
\boxed{
 q_{\ell,M}
 =\frac{1}{(\ell-1)!}
 \mathcal Z_M\!\left(
  C_M(\chi_Mu^{\ell-2}),
  \eta_M^{\rm fp}
 \right).}
 \tag{L-15135.5}
\]

Any normalization factor belonging to the declared coefficient convention may
be placed on both sides; the one-leg linearity is unchanged.

## 3. Genuine order four

At the first nontrivial even order after cubic parity,

\[
\boxed{
 q_{4,M}
 =\frac16
 \mathcal Z_M\!\left(
  C_M(\chi_Mu^2),
  \eta_M^{\rm fp}
 \right).}
 \tag{L-15135.6}
\]

This is one finite contour pairing.  It is linear in the contour biform and in
the finite-jet counterterm vector.

By contrast, the contact correction required by `L-15134` is

\[
\begin{aligned}
 q_{4,M}^{\rm Ward}
 ={}&4\operatorname{Tr}(A^3D)
 -4\operatorname{Tr}(A^2D^2)\\
 &-2\operatorname{Tr}(ADAD)
 +4\operatorname{Tr}(AD^3)
 -\operatorname{Tr}D^4,
\end{aligned}
 \tag{L-15135.7}
\]

which is a connected nonlinear polynomial in the raw seam and counterterm seam
operators.

Thus the displayed central-kernel subtraction does not, by its form alone,
produce the quartic cyclic contact cumulant.

## 4. Scaling separation

Scale the finite contour biform by a scalar `t`, keeping its readout maps,
cutoff, and finite-jet maps fixed. Then

\[
 q_{\ell,M}(t)=tq_{\ell,M}(1),
 \tag{L-15135.8}
\]

whereas the raw and counterterm seam operators both scale by `t`, so

\[
 q_{\ell,M}^{\rm Ward}(t)
 =t^\ell q_{\ell,M}^{\rm Ward}(1).
 \tag{L-15135.9}
\]

Consequently, a natural identity valid on a scalar-stable class of contour
biforms can equate the two quantities for `ell>=2` only when both vanish
identically.  Indeed,

\[
 tq=t^\ell r
\]

for all `t` in an interval forces `q=r=0`.

This does not forbid an accidental equality at one fixed normalization. It
proves that such an equality is not a universal consequence of the linear
finite-part and finite-jet maps.

## 5. Two viable proof routes

The contact-free diagonal theorem can now be proved only through one of the
following mechanisms.

### Route A — seam-radical finite jets

Prove that the finite-jet range is annihilated by every realized seam leg and by
the fixed scalar probe. Then

\[
 D=0,
 \qquad q_{\ell,M}=0,
\]

and every contact word vanishes.

### Route B — nonlinear source Ward map

Construct an additional nonlinear map from the order-`ell` central source to
the connected cyclic tensor power and prove precisely

\[
 q_{\ell,M}=q_{\ell,M}^{\rm Ward}
\]

for the fixed Riemann contour data. This map is not present in
(L-15135.3)--(L-15135.5).

## 6. Proof boundary

The coefficient formula (L-15135.5) follows directly from the manuscript's
central kernel and common subtraction.  The theorem does not assert that the
actual value of (L-15135.6) is nonzero.  It proves that the requested nonlinear
contact cancellation is additional data, not a formal property of the displayed
finite-jet regularization.