# L-26204 — Boundary-jet reflected domination

Claim ID: `L-26204`  
Title: A complete finite quotient ledger reduces the carry sign to one source-specific Schur inequality on the exported half-pole boundary jets  
Status: **NEW FULL-PROPOSAL HINGE — FINITE IDENTITY AND LMI REQUIRE INDEPENDENT RECONSTRUCTION**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: `L-26201`–`L-26203`; the verified two-frequency physical reflected identity of PR #241  
Scope: finite endpoint `Y`; no bounded-rank or generic operator assertion

## 1. Complete finite source ledger

Fix `Y>=1`. Start from the oversupported dyadic source `widetilde eta_Y` of
`L-26203`, and partition its complete support by every point at which one of the
following changes:

1. the integer quotient `floor(Y/n)`;
2. the dyadic translate index;
3. a carry-kernel polynomial branch;
4. the physical unit-block support;
5. a first-crossing or endpoint convention.

Call the resulting finite cells `I in P_Y`. No cell is deleted. In particular,
the oversupport collar `(Y,2Y]` is part of the same source object.

For each cell let `nu_I` be the corresponding signed source column and export

\[
J_I=
\begin{pmatrix}
A_I\\B_I
\end{pmatrix}
=
\begin{pmatrix}
\int e^{x/2}d\nu_I(x)\\
\int xe^{x/2}d\nu_I(x)
\end{pmatrix}.
\tag{L-26204.1}
\]

Let `J_Y` be the direct sum of all these jet maps. Its scalar collar projection
must reproduce

\[
-\bigl[M(Y)-M(Y/2)\bigr]
\tag{L-26204.2}
\]

and, after the reviewed causal ratio adapter, the `2/3` first Farey cell.

## 2. Exact negative jet matrix

For the derivative order attached to one Green row, define

\[
N_r=2^{-r}
\begin{pmatrix}
7+3r&3/2\\
3/2&0
\end{pmatrix}.
\tag{L-26204.3}
\]

`L-26201` proves that this matrix contains the complete indefinite part of that
row. Let `N_Y` be the block-diagonal matrix formed from the actual rows of the
finite source ledger, with every multiplicity and orientation retained.

No positive-semidefinite claim is made for `N_Y`.

## 3. Positive B-spline reserve

Apply the exact Peano formula of `L-26202` on every cell. The positive interior
curvature gives a matrix `D_Y>=0` whose entries are finite integrals of the
triangular B-spline

\[
\mathcal B_{\alpha,\beta}(t,u)
\]

against `2e^(u/2)`. The endpoint traces are not included in `D_Y`; they remain
in `J_Y`.

At dyadic boundaries, finite Abel summation groups the endpoint traces before a
sign is taken. The resulting scalar coefficients are the exact binary digit
sums `s_2(ell)>=0`. This is a boundary reserve, not a Hankel theorem.

## 4. Source-specific reflected reserve

Use the independent-frequency reflected identity of PR #241, not a single
global vertical integral. Assemble the complete physical unit-block Gram for
the same source columns and the same support partition. After the complete-pair
bulk is eliminated, compress the remaining positive form to the boundary-jet
coordinates and take its exact Schur short. Denote the result by

\[
R_Y\succeq0.
\tag{L-26204.4}
\]

The production object must emit the underlying matrices `G_Y,C_Y,D_Y^ref` and
verify

\[
R_Y=G_Y-C_Y^*(D_Y^{ref})^{-1}C_Y.
\tag{L-26204.5}
\]

A scalar reflected identity or aggregate vertical positivity is not a substitute
for this source map.

## 5. Boundary-Jet Domination theorem

The proposed closing statement is the finite source-image inequality

\[
\boxed{
\left.
\bigl(D_Y+R_Y-N_Y\bigr)
\right|_{\operatorname{Ran}J_Y}
\succeq0
\qquad(Y\ge Y_0).}
\tag{L-26204.6}
\]

Equivalently, for every complete source coefficient vector `c`,

\[
\boxed{
\langle J_Yc,(D_Y+R_Y)J_Yc\rangle
\ge
\langle J_Yc,N_YJ_Yc\rangle.}
\tag{L-26204.7}
\]

This theorem is called **Boundary-Jet Domination (`BJD`)**.

It is source specific. The matrices may grow with `Y`; no absolute face rank,
contact count, or number of quotient cells is assumed.

## 6. Full sign assembly

The complete finite Green/carry form has the proposed exact decomposition

\[
\boxed{
\mathscr C(Y)
=
\mathscr P_Y
+
\langle J_Y,(D_Y+R_Y-N_Y)J_Y\rangle,}
\tag{L-26204.8}
\]

where `P_Y>=0` is the sum of:

- the exact complete-pair rank-one Grams of `L-26201`;
- the positive interior B-spline mixtures;
- all lower-scale source-complete squares produced by the physical reflected
  block.

Every transition and support collar is allocated either to `P_Y` or to `J_Y`.
There is no residual “small error” in (L-26204.8).

Subject to independent reconstruction of (L-26204.8), `BJD` gives

\[
\mathscr C(Y)\ge0.
\tag{L-26204.9}
\]

A weaker production version may permit a total negative endpoint debt
`O(log^A Y)`; combined with the finite Gamma-carry packing or Greedy Slack
consumer, that is still sufficient for the square-screw criterion.

## 7. Why this is not the rejected theorem

`BJD` does not assert that `phi''(x+y)` is conditionally positive. It accepts the
exact indefinite matrix `N_r` and asks the actual digital and reflected source
to dominate it after the complete quotient and collar assembly.

The determinant `-233/64` is a mandatory passing mutation: the unrestricted
kernel remains indefinite, while the completed source LMI may still be positive.

Likewise, a rank-`K` same-sign Möbius cube is retained in the source manifest. It
must either be half-pole paired, appear in the reflected reserve, or remain as a
visible negative jet. It cannot disappear by face counting.

## 8. Exact review hinge

The proposal is rejected by any one of:

1. a missing quotient or oversupport cell in (L-26204.8);
2. a wrong left/right endpoint trace;
3. failure of the half-pole-null pairing;
4. failure of the physical two-frequency source map;
5. a negative eigenvalue of `D_Y+R_Y-N_Y` on the actual source image;
6. loss of the dyadic or `2/3` Mertens scalar projection;
7. a same-sign Möbius cube not represented by the ledger.

## 9. Status boundary

Exact ingredients:

- the jet matrix `N_r`;
- half-pole-pair positivity;
- the B-spline Peano kernel;
- the dyadic boundary jets;
- the physical two-frequency reflected identity as an imported reviewed adapter.

New unverified theorem:

- the complete identity (L-26204.8) and the source-image LMI `BJD`.

RH is not claimed proved before that reconstruction.
