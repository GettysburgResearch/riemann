# L-93881 — The anchored Target-Lorenz compiler closes every physical row

Claim ID: `L-93881`  
Status: **PROPOSED COMPLETE DIRECTED/EXACT ANCHORED-SOURCE THEOREM**  
Inputs: exact stopping leaves; compact AVLT; directed tail AVLT; global `P_61` frontier-row theorem  
RH status: **unproved at this claim**

## 1. Terminal leaf

Let

\[
p\ge67,\qquad 1\le y<67,\qquad x=py.
\]

At a terminal stopped leaf write the positive even and odd source measures as
`E` and `O`. Let `T`, `S`, and `R_j` denote the exact causal target, declared
score, and component-row coordinates.

Order the even atoms by the Target-Lorenz target/score ratio. Let

\[
0\le u_e\le1,\qquad \sum_eu_eT(e)=T(O)
\tag{L-93881.1}
\]

be the leftmost cutoff vector. Put

\[
U=\sum_eu_eE_e,\qquad \nu=E-U.
\]

Then `\nu` is a positive source and every even occurrence has one owner.

## 2. Target and score

By construction,

\[
T(U)=T(O),
\]

so

\[
\boxed{T(\nu)=T(E)-T(O).}
\tag{L-93881.2}
\]

The bathtub principle gives the minimum score among all target-matching even
submeasures. The complete causal ordering therefore yields

\[
S(U)\le S(O).
\]

With

\[
\sigma=S(O)-S(U)\ge0,
\]

we have

\[
\boxed{S(\nu)=S(E)-S(O)+\sigma.}
\tag{L-93881.3}
\]

## 3. Inherited rows `2<=j<=66`

For each such row, define

\[
\Theta_j(p,y)
=
O_T E_R^{(j)}-E_T O_R^{(j)}.
\]

The compact directed calculation covers every real activation cell with

\[
py<166000,
\]

and the analytic/directed tail covers

\[
py\ge166000.
\]

The domains meet exactly. The directed primitives enclose every square root,
logarithm, `\zeta(1/2)`, and `\zeta'(1/2)` outward. The result is

\[
\boxed{\Theta_j(p,y)>0}
\tag{L-93881.4}
\]

for every `p>=67`, `1<=y<67`, and `2<=j<=66`.

The exact box-LP theorem then gives

\[
B_j:=R_j(U)-R_j(O)\ge0.
\tag{L-93881.5}
\]

Hence

\[
\boxed{R_j(E)-R_j(O)=R_j(\nu)+B_j\ge0.}
\tag{L-93881.6}
\]

## 4. Frontier rows `j>66`

The child endpoint is below `67`, so every child component row vanishes:

\[
R_j(\text{child})=0,\qquad j>66.
\]

For these rows the complete signed leaf row is the canonical finite-Euler
frontier row

\[
D_{P_{61},x}(j).
\]

The global finite-Euler theorem proves

\[
\boxed{D_{P_{61},x}(j)\ge0\quad(j>66).}
\tag{L-93881.7}
\]

To avoid silently extending the AVLT certificate, define the frontier physical
row directly by

\[
g_j=D_{P_{61},x}(j),
\]

as a current-only target-null row. No Target-Lorenz determinant is claimed
outside `2,...,66`.

## 5. Complete typed leaf

Define

\[
G_\omega=
\left(
\nu;\,
(B_2,\ldots,B_{66},g_{67},g_{68},\ldots);\,
\sigma
\right).
\]

Its source, target, score, and complete physical-row marginals are exactly those
of `E-O`. All row additions outside the source coordinate are current-only and
target-null.

Apply ordinary observations at `q` and `4q` to the complete row, sum all leaf
weights, and only then form

\[
\Xi(q)=\Gamma(q)-2\Gamma(4q).
\]

## 6. Stopping-line integration

The stopping-line and least-prime identities assign every anchored source
occurrence to one terminal leaf. Their positive path coefficients are finite at
fixed `X`. Therefore

\[
\boxed{
\Sigma_{X,\mathrm{anc}}
=
\sum_{\omega}\omega_X(\omega)G_\omega\ge0
}
\tag{L-93881.8}
\]

is a finite positive typed datum whose physical observation equals the exact
anchored Möbius row.

## 7. Reproducibility boundary

The packet physically imports:

```text
compact real-cell AVLT source and certificate;
directed analytic tail source and certificate;
directed zeta primitive;
typed-leaf compiler replay;
global P61 frontier-row theorem and replay.
```

A single failed interval or hash retracts this theorem.

## 8. Boundary

```text
target exactness                              EXACT
score superordination                        EXACT / DIRECTED ORDER
rows 2..66                                   DIRECTED COMPLETE AVLT
rows >66                                     GLOBAL FRONTIER THEOREM
one source owner per leaf                    EXACT
ordinary q/4q before detail                  EXACT
bulk source                                  SEPARATE / L-93880
Riemann Hypothesis                           UNPROVEN
```
