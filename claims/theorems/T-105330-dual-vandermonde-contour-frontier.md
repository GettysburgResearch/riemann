# T-105330 — Dual Vandermonde contour hierarchies for the two sharp Xi last-defect gates

Claim ID: `T-105330`  
Status: **MAJOR EXACT COORDINATE REDUCTION; BOTH XI SIGN HIERARCHIES OPEN**  
Created: 2026-08-23  
Depends on: `L-105214--L-105218`, `L-105300`, `L-105320--L-105329`, parent `T-105220`  
RH status: **unproved**

## 1. Purpose

The parent programme identifies two exact and complementary last defects:

```text
PRES105220  a positive real critical residue;
BRP105220   a negative square of the boundary Cauchy-Loewner remainder.
```

The present theorem converts both into explicit scalar determinant hierarchies
on the same contour coordinate. It does not replace the sharp gates by a
variance average or a bounded packet test.

## 2. Critical hierarchy

For a regular window containing `M` simple noncommon critical points of `F`,
put

\[
a_\ell
=-{1\over2\pi i}\int_{\partial\Omega}
 {F(z)\over F'(z)}z^\ell\,dz
\]

and

\[
D_k^{\rm crit}
=\det[a_{r+s}]_{r,s=0}^{k-1},
\qquad1\le k\le M.
\]

Then `L-105328` proves

\[
\boxed{
D_k^{\rm crit}
={(-1)^k\over k!(2\pi i)^k}
\int_{(\partial\Omega)^k}
\Delta(z)^2
\prod_a{F(z_a)\over F'(z_a)}\,dz_a.
}
\tag{T-105330.1}
\]

Moreover,

\[
\boxed{
D_k^{\rm crit}>0\quad(1\le k\le M)
\Longleftrightarrow
\begin{cases}
\text{all critical points in the window are real},\\
F(c)/F''(c)<0\text{ at every one of them}.
\end{cases}
}
\tag{T-105330.2}
\]

Define `CRVH105330` to be this complete strict hierarchy in every regular
window of the exact exhaustion, with common-zero and multiplicity events kept
in their separate confluent ledger.

## 3. Boundary hierarchy

For every finite real noncritical packet `X=(x_1,...,x_k)`, let

\[
D_X^{\rm bdry}
=\det[\mathscr R_{F,\Omega}(x_i,x_j)]_{i,j=1}^{k}.
\]

`L-105329` proves

\[
\boxed{
\begin{aligned}
D_X^{\rm bdry}
={\left(\prod_iF'(x_i)^2\right)\Delta(X)^2
 \over k!(2\pi i)^k}
\int_{(\partial\Omega)^k}
 {\Delta(\zeta)^2
  \prod_aF(\zeta_a)/F'(\zeta_a)
 \over\prod_{i,a}(\zeta_a-x_i)^2}
\prod_a d\zeta_a.
\end{aligned}
}
\tag{T-105330.3}
\]

Define `BCVH105330` by

\[
D_X^{\rm bdry}\ge0
\]

for every finite real packet and every window of the exact exhaustion. Because
subpackets are included, this is equivalent window-by-window to all-packet
positive semidefiniteness of the boundary Loewner kernel.

## 4. Exact conclusion graph

On the simple noncommon stratum,

\[
\boxed{
\mathrm{CRVH105330}
\Longleftrightarrow
\mathrm{PRES105220}
+\text{absence of the nonreal critical correction}.
}
\tag{T-105330.4}
\]

Also,

\[
\boxed{
\mathrm{BCVH105330}
\Longleftrightarrow
\text{the all-packet boundary-PSD component of }\mathrm{BRP105220}.
}
\tag{T-105330.5}
\]

Under `CRVH105330`, the nonreal-critical clause of `BRP105220` is already
supplied. Therefore the parent Bezoutian Schur complement and derivative telescope give

\[
\boxed{
\mathrm{CRVH105330}
\wedge
\mathrm{BCVH105330}
\Longrightarrow
\mathrm{PRES105220}
\wedge
\mathrm{BRP105220}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-105330.6}
\]

Neither antecedent hierarchy is proved for the last defective Xi derivative.

## 5. Fixed-order Xi-double-prime specialization

Take

\[
F=\Xi''.
\]

At a real zero `c` of `Xi'''`,

\[
-\rho_c
=-{\Xi''(c)\over\Xi''''(c)}
={\Xi'''(c)^2-\Xi''(c)\Xi''''(c)
 \over\Xi''''(c)^2}.
\tag{T-105330.7}
\]

Thus the critical matrix is the exact moment matrix of the fixed-order
Laguerre orientation values at the `Xi'''` critical nodes. The modular scalar and adaptive cofinal routes on PR #720 can therefore be
retyped as attempts to prove the **real-critical weight component** of
`CRVH105330` for this fixed derivative level, rather than merely a mean sign.
A complete `CRVH105330` proof must additionally exclude nonreal critical pairs
and retain the common-zero/multiplicity ledger.

The first two determinant channels are insufficient by `R-105328`; all
critical orders up to the complete count, or a source theorem forcing their
joint positivity, are required.

## 6. Interaction with the compression and temperature coordinates

The exact root-compression operator and conserved residue temperature on this
PR remain useful producer coordinates:

- the pencil `det(mathsf P+t mathsf G)` is the quotient-algebra residue
  characteristic polynomial;
- high-tail saddle control, if hostilely verified, places the terminal
  critical pencil in the positive cone;
- centered weighted winding controls low moments of the same boundary current.

But the conclusion-facing objects are now explicit:

```text
complete critical Vandermonde determinants;
complete boundary Cauchy-Vandermonde determinants.
```

Small variance or one centered scalar flux cannot substitute for them.

## 7. Immediate analytic work packages

```text
CRIT-MODULAR-105330:
  derive a complete-source formula for the critical multiple-contour
  determinants, preserving all mixed theta-orbit terms before signs;

BDRY-TERMINAL-105330:
  find one terminal Xi window with nonnegative boundary packet determinants;

ANNULAR-TRANSPORT-105330:
  use L-105217 to descend that positivity across annuli once CRVH is known;

CONFLUENT-105330:
  splice the existing common-zero/multiplicity jet ledger into the determinant
  hierarchy without silently deleting singular levels.
```

## 8. Exact boundary

```text
critical Vandermonde factorization/pencil       PROVED EXACT
quotient-resultant identification                PROVED EXACT
critical multiple-contour determinants           PROVED EXACT
critical hierarchy <-> sharp residue signs       PROVED EXACT / FINITE WINDOW
boundary contour-square quadratic forms          PROVED EXACT
boundary Cauchy-Vandermonde determinants          PROVED EXACT
boundary hierarchy <-> all-packet PSD component   PROVED EXACT / FINITE WINDOW
CRVH105330 for fixed low Xi                       OPEN / SHARP RH-BEARING
BCVH105330 for fixed low Xi                       OPEN / SHARP RH-BEARING
moving complex saddle                            PROPOSED / REVIEW REQUIRED
Riemann Hypothesis                               UNPROVEN
```
