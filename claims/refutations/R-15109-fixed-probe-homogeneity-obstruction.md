# R-15109 — A fixed linear contour probe cannot supply the fourth cyclic trace

Claim ID: `R-15109`  
Status: **PROVED TYPE/HOMOGENEITY OBSTRUCTION**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: the displayed finite-part coordinate definitions in Shimizu v6/v8; `L-15132`  
Scope: smallest exact obstruction at the classical source interface  
Related counterexample candidates: none

## 1. The manuscript's displayed scalar interface

The manuscript defines a finite-window contour-coordinate bilinear form

\[
 \mathcal Z_{\mathrm{fp},\partial}^{\mathrm{fw}}(\psi,\eta)
 =\mathsf{FP}^{\mathrm{ct}}_M[\mathcal M_{\mathrm{fw}}(\psi,\eta)]
 \tag{R-15109.1}
\]

and hence a finite-part coordinate functional

\[
 \epsilon_M^{\mathrm{fp}}(\psi)\in E_M'
 \tag{R-15109.2}
\]

by

\[
 \langle\epsilon_M^{\mathrm{fp}}(\psi),\eta\rangle
 =\mathcal Z_{\mathrm{fp},\partial}^{\mathrm{fw}}(\psi,\eta).
 \tag{R-15109.3}
\]

The latest abstract states separately that the classical scalar probe is fixed
by the geometric Guinand--Weil contour normal form, while the operator side is
obtained through finite-window scalar coefficients and cyclic tensor
contractions.

Thus the displayed one-probe scalar interface is a **linear fixed-probe pairing**:

\[
 \mathcal L_M(\psi)
 =\langle\epsilon_M^{\mathrm{fp}}(\psi),\eta_M^{\mathrm{fp}}\rangle.
 \tag{R-15109.4}
\]

If

\[
 \Psi_{w,M}^{\mathrm{fw}}
 =\sum_{q\ge0}w^q\psi_{q,M}
\]

is the regularized central family (the finite-jet subtraction is linear), then
the coefficient actually supplied by this displayed scalar map is

\[
 \boxed{
 [w^q]\,\mathcal L_M(\Psi_{w,M}^{\mathrm{fw}})
 =\langle\epsilon_M^{\mathrm{fp}}(\psi_{q,M}),
          \eta_M^{\mathrm{fp}}\rangle.}
 \tag{R-15109.5}
\]

No inverse-Gram cyclic gluing appears in the displayed definitions
(R-15109.1)--(R-15109.5). Version 8 says that scalar and cyclic tests are instead
obtained by pullback from a further universal Cauchy--Laplace coefficient
object. The missing source theorem is therefore the explicit construction of
that tensor object and the proof that its scalar pullback equals the sewn loop.

## 2. What linear realization alone cannot prove at order four

Let `B` denote a finite seam form and let `G` be its readout Gram. Suppose one
tries to identify the displayed one-probe functional with the fourth trace using
only the linear seam-transpose realization from finite-part coordinates. Under
scaling of that realized seam datum, any such one-probe scalar has degree one:

\[
 \mathcal L_M(tB)=t\mathcal L_M(B).
 \tag{R-15109.6}
\]

The first nontrivial even determinant coefficient is

\[
 \mathcal C_4(G,B)=\operatorname{Tr}((G^\dagger B)^4),
 \tag{R-15109.7}
\]

which satisfies

\[
 \mathcal C_4(G,tB)=t^4\mathcal C_4(G,B).
 \tag{R-15109.8}
\]

Therefore no natural identity

\[
 \mathcal L_M(B)=\mathcal C_4(G,B)
 \tag{R-15109.9}
\]

can be deduced from the linear realization maps alone on a source class closed
under scalar multiplication. If the common value is nonzero at one datum,
scaling by any `t` with `t^3!=1` gives a contradiction.

This is not a counterexample to a separately defined nonlinear universal
coefficient object, and it does not rule out equality at the manuscript's one
fixed datum. It proves that the missing universal pullback must contain an
additional fourth-order tensor/sewing operation; the displayed one-probe
coordinate by itself is not that operation.

## 3. Exact redundant-readout control

Take

\[
 U=\begin{pmatrix}1&0&1\\0&1&1\end{pmatrix},
 \qquad
 S=\begin{pmatrix}2&1\\1&-1\end{pmatrix}.
\]

Then

\[
 G=U^TU=
 \begin{pmatrix}1&0&1\\0&1&1\\1&1&2\end{pmatrix},
\]

\[
 G^\dagger=
 \frac19\begin{pmatrix}5&-4&1\\-4&5&1\\1&1&2\end{pmatrix},
\]

and

\[
 B=U^TSU=
 \begin{pmatrix}2&1&3\\1&-1&0\\3&0&3\end{pmatrix}.
\]

The source sewing theorem gives

\[
 \mathcal C_4(G,B)=\operatorname{Tr}(S^4)=31.
\]

Choose a fixed linear probe normalized so that `L(B)=31`. At scale `t=2`,

\[
 \boxed{\mathcal L(2B)=62,}
\]

whereas

\[
 \boxed{\mathcal C_4(G,2B)=2^4\cdot31=496.}
\]

The exact gap is

\[
 \boxed{496-62=434.}
\]

The same sewn moments are invariant under a dense nonorthogonal coordinate
change, while the Moore--Penrose readout remains redundant. `X-15114` verifies
all identities with `fractions.Fraction`.

## 4. What a valid repair must contain

A source-level order-four coefficient that is claimed to equal this matrix trace must be a tensor contraction of the form

\[
 B_{a_1b_1}(G^\dagger)_{b_1a_2}
 B_{a_2b_2}(G^\dagger)_{b_2a_3}
 B_{a_3b_3}(G^\dagger)_{b_3a_4}
 B_{a_4b_4}(G^\dagger)_{b_4a_1}.
 \tag{R-15109.10}
\]

For order `ell`, it must have `ell` seam factors and `ell` inverse-Gram
gluings. This object is nonlinear in the finite-part coordinate and lives on a
cyclic tensor power, not in the original one-probe dual space.

Hence the phrase “scalar and cyclic tests are pullbacks of one universal
coefficient object” becomes a proof only after the universal object and both
pullbacks are displayed and (R-15109.10) is derived.

## 5. Majorant does not repair the type mismatch

`L-15132` supplies a uniform majorant

\[
 \frac{C^2r}{1-Cr}
\]

for the correctly sewn coefficients. This justifies every limit once the
finite coefficient identity is known. Dominated convergence cannot turn a
linear fixed-probe coefficient into a quartic cycle; the mismatch exists before
any limit is taken.

## 6. Verdict

The manuscript's displayed one-probe scalar definitions and its finite cyclic
trace assertions are **not yet connected in the accessible text by an explicit
source tensor identity**. The smallest nontrivial obstruction occurs at order four:

\[
 \boxed{
 \text{linear fixed-probe coefficient}
 \not\equiv
 \text{quartic Moore--Penrose sewn loop}.}
\]

The correct amendment is `L-15132`. Proving that the classical explicit-formula
coefficient is the amended sewn loop remains open and RH-bearing.
