# T-108106 — Positive shared-fibre debt is bounded by one doubly-centered signed current

Status: **exact full-grid projection majorant for the positive fixed-fibre
Wick operator, exact row/column ANOVA formula, exact retention of all history,
source-group, and cross-cell terms before squaring, exact zero-positive-debt
criterion for currents annihilated by double centering, and a census-free full-fibre upper
bound for the declared live one-cell vector; no complete live current census,
no signed cross-conductor estimate, no relative trace theorem, no principal
binding, and no proof of RH or GRH.**

Bounded replay:
[`live_quotient_centered_current_majorant.py`](live_quotient_centered_current_majorant.py).
Canonical output:
[`live_quotient_centered_current_majorant.json`](live_quotient_centered_current_majorant.json).

This packet continues
[T-108104](SOURCE_GROUPED_POSITIVE_HODGE_DESCENT.md).  T-108104 proved that
all literal histories and all same-cell source-group fluctuations descend to
the signed normalized cell current

\[
 y_a=N_a^{-1/2}s_a,
 \qquad
 s_a=\sum_{g\mapsto a}Z_g,
\]

before the occupied-cell positive quotient is evaluated.  The remaining
bound still appeared to involve the unknown operator \((Q_R)_+\).  The new
point is that this norm can be removed from an unconditional upper bound.

## 0. Full-grid setup

Let

\[
 H_q=I_q-{1\over q}\mathbf1\mathbf1^*,
 \qquad
 P=H_\ell\otimes H_\rho.
\tag{0.1}
\]

The operator \(P\) is the orthogonal projection onto arrays with both row and
column means zero.  Let \(E\) extend an occupied-cell vector by zero to the
full \(\ell\times\rho\) residue grid, and let

\[
 S=E^*PE
\tag{0.2}
\]

be the occupied principal compression.  With the original atom-to-cell map
\(R\), put

\[
 M_R=R^*SR,
 \qquad
 d=\left(1-{1\over\ell}\right)
   \left(1-{1\over\rho}\right),
 \qquad
 B_R=M_R-dI.
\tag{0.3}
\]

For a literal vector \(z\), write

\[
 s=Rz,
 \qquad
 \widetilde s=Es.
\tag{0.4}
\]

After the T-108104 history grouping,

\[
 s_a=\sum_{g\mapsto a}Z_g.
\tag{0.5}
\]

## 1. Theorem T-108106

Because

\[
 M_R=(PER)^*(PER)\succeq0,
\]

scalar functional calculus gives

\[
 0\preceq(M_R-dI)_+\preceq M_R.
\tag{1.1}
\]

Therefore every literal or source-grouped coefficient vector satisfies

\[
 \boxed{
 0\le\langle z,(B_R)_+z\rangle
 \le\langle z,M_Rz\rangle
 =\|P\widetilde s\|_2^2.}
\tag{1.2}
\]

This bound contains neither \(\|(Q_R)_+\|\) nor the multiplicities \(N_a\).
It depends only on the **complete signed cell current**, assembled before the
projection and before the square.

Write the zero-extended current as \(s_{xy}\), and define

\[
 r_x=\sum_y s_{xy},
 \qquad
 c_y=\sum_xs_{xy},
 \qquad
 T=\sum_{x,y}s_{xy}.
\tag{1.3}
\]

Then

\[
 (P\widetilde s)_{xy}
 =s_{xy}-{r_x\over\rho}-{c_y\over\ell}+{T\over\ell\rho},
\tag{1.4}
\]

and the upper bound has the exact ANOVA form

\[
 \boxed{
 \begin{aligned}
 \|P\widetilde s\|_2^2
 &=\sum_{x,y}|s_{xy}|^2
 -{1\over\rho}\sum_x|r_x|^2
 -{1\over\ell}\sum_y|c_y|^2
 +{1\over\ell\rho}|T|^2.
 \end{aligned}}
\tag{1.5}
\]

All four terms in (1.5) are evaluated after the literal history and source
currents have been summed.  Thus every same-cell, same-row, same-column, and
cross-conductor cross term is retained.

## 2. Proof and relation to the occupied quotient

T-108100 gives the exact equality

\[
 \langle z,(B_R)_+z\rangle
 =\langle y,(Q_R)_+y\rangle,
 \qquad y=D^{-1/2}Rz.
\tag{2.1}
\]

The new estimate does not replace this equality.  It supplies a second,
operator-free control.  Since \(M_R\succeq0\), the scalar inequality

\[
 (\lambda-d)_+\le\lambda
 \qquad(\lambda\ge0)
\]

proves (1.1).  Moreover,

\[
 \langle z,M_Rz\rangle
 =\langle Es,PEs\rangle
 =\|PEs\|_2^2
\]

because \(P=P^*=P^2\).  Expanding

\[
 H_\ell\otimes H_\rho
 =I-\Pi_\ell\otimes I-I\otimes\Pi_\rho
  +\Pi_\ell\otimes\Pi_\rho
\]

automatically yields (1.4)--(1.5).

Combining T-108104 and T-108106 gives the exact pipeline

```text
literal atoms z_(g,h)
  -> source-group currents Z_g
  -> complete signed cell current s_a=sum_(g->a) Z_g
  -> zero extension to the full residue grid
  -> double centering H_ell tensor H_rho
  -> one squared norm.
```

No triangle inequality is required at any arrow.

## 3. Exact zero-positive-debt directions

If

\[
 P\widetilde s=0,
\tag{3.1}
\]

then (1.2) forces

\[
 \boxed{(B_R)_+z=0.}
\tag{3.2}
\]

In fact \(M_R^{1/2}z=0\), so

\[
 M_Rz=0,
 \qquad
 B_Rz=-dz.
\tag{3.3}
\]

Thus every complete current lying in the row-plus-column additive subspace is
an exact \(-d\) direction.  This criterion is stronger than cellwise zero
current: nonzero currents may survive in individual cells while cancelling
after double centering.

The retained replay includes a full-grid field

\[
 s_{xy}=a_x+b_y
\]

with nonzero entries but \(P\widetilde s=0\), hence zero positive debt.

## 4. The live one-cell vector

For the source-locked live panel

\[
 \ell=1031,
 \qquad
 \rho=521,
 \qquad
 d={535600\over537151},
\]

the declared hundred-history subpacket has signed cell current

\[
 s=4w
\]

and literal energy

\[
 E=676|w|^2.
\]

For a one-cell current, (1.5) gives

\[
 \boxed{
 \|P\widetilde s\|_2^2
 =d|s|^2
 =16d|w|^2.}
\tag{4.1}
\]

Therefore the positive debt of that zero-extended vector in the **full
fibre**, irrespective of all other occupied cells, satisfies

\[
 \boxed{
 \langle z,(B_R)_+z\rangle
 \le16d|w|^2
 ={4d\over169}E
 <{4\over169}E.}
\tag{4.2}
\]

This is an unconditional factor greater than \(42.25\) from literal energy
to positive debt and does not use the unknown quotient norm or cell
multiplicity.

For comparison, the previously certified isolated one-cell principal block
has the exact diagnostic

\[
 {396\over25}d|w|^2.
\tag{4.3}
\]

The gap between the full-grid majorant (4.1) and that isolated principal-block
diagnostic is

\[
 {4\over25}d|w|^2.
\tag{4.4}
\]

Equations (4.1)--(4.4) do **not** assert that the hundred histories constitute
a complete native source.  They bound the declared zero-extended vector.  A
bound for the complete source still requires the complete signed current to
be assembled first.

## 5. Strategic consequence

The remaining fixed-fibre positive problem is now smaller than the previous
quotient formulation suggested.  It is enough to control

\[
 \boxed{
 \left\|(H_\ell\otimes H_\rho)
 \widetilde{\left(\sum_g Z_g\right)}\right\|_2^2,}
\tag{5.1}
\]

with all source and conductor labels retained until after the sum.  Neither a
full spectral diagonalization of \(Q_R\) nor an a priori bound for
\(\|(Q_R)_+\|\) is necessary for this upper-bound route.

The next named gate is

```text
RELATIVECURRENTTRACE108108

Assemble the complete source-labelled cell current in every live fibre,
double-center it on the full residue grid before squaring, and prove the
required signed cross-conductor estimate.  In parallel, realize the same
double-centered current as a compatible relative partial-Frobenius trace.
```

The complete live census, the signed global estimate, and the relative trace
remain open.

## 6. Replay ledger

The bounded producer uses exact rational arithmetic.  It verifies:

1. the ANOVA formula against direct full-grid projection;
2. a two-cell occupied quotient with positive debt \(2/3\) and centered
   majorant \(7/3\);
3. a nonzero additive current with exactly zero centered energy;
4. the live density, factor, isolated one-cell diagnostic, and exact gap.

```text
PASS_T108106_LIVE_QUOTIENT_CENTERED_CURRENT_MAJORANT

full-grid projection majorant                    PROVED
double-centered ANOVA identity                   PROVED
unknown quotient norm removed from upper bound   PROVED
all current cross terms retained before square   PROVED
zero-centered current has zero positive debt     PROVED
live declared-vector census-free majorant        PROVED
complete live grouped-current census             OPEN
signed cross-conductor estimate                  OPEN
global partial Frobenius / RELTRACE               OPEN
principal binding                                OPEN
RH / GRH                                         UNPROVED
```
