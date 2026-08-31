# T-108104 — Source histories and same-cell group currents split into exact negative Hodge blocks

Status: **exact two-stage atom-to-source-group-to-residue-cell factorization,
exact orthogonal Hodge decomposition, exact invariance of the fixed-fibre
positive part under source-authorized history aggregation, exact negative
blocks for both within-history fluctuations and same-cell cross-group
zero-current directions, and exact recovery of the live factor-4225 ledger;
no complete live occupancy census, no signed cross-conductor estimate, no
relative trace theorem, no principal binding, and no proof of RH or GRH.**

Bounded replay:
[`source_grouped_positive_hodge_descent.py`](source_grouped_positive_hodge_descent.py).
Canonical output:
[`source_grouped_positive_hodge_descent.json`](source_grouped_positive_hodge_descent.json).

This packet combines three source-locked inputs:

1. [T-108100](SHARED_FIBRE_POSITIVE_QUOTIENT.md), which proves that the
   positive fixed-fibre Wick operator lives on the multiplicity-weighted
   residue quotient;
2. [T-108102](LIVE_SIGNED_HISTORY_POSITIVE_COMPRESSION.md), which binds that
   quotient to the live hundred-history collision;
3. the source-authorized history partition and exact signed recombination in
   [`FFPS_SIGNED_HISTORY_RECOMBINATION.md`](../l-families/atlas/function_field/FFPS_SIGNED_HISTORY_RECOMBINATION.md).

The new point is that these are not merely compatible statements.  Their
maps factor exactly, producing a second Hodge layer inside the already known
\(-d\) block.

## 0. Outcome

Fix one occupied shared-conductor fibre.  Let \(\Omega\) be its literal atom
set, \(\mathcal G\) the source-authorized history groups, and
\(\mathcal C\) the occupied physical residue cells.  Every group retains one
arithmetic tuple and all non-history labels, so all histories in one group
map to one cell.

Define the three aggregation maps

\[
 A:\mathbb C^\Omega\to\mathbb C^{\mathcal G},
 \qquad
 (Az)_g=Z_g:=\sum_{\omega\in H_g}z_\omega,
 \tag{0.1}
\]

\[
 C:\mathbb C^{\mathcal G}\to\mathbb C^{\mathcal C},
 \qquad
 (CZ)_a=\sum_{g\mapsto a}Z_g,
 \tag{0.2}
\]

and

\[
 R=CA,
 \qquad
 (Rz)_a=s_a:=\sum_{g\mapsto a}Z_g.
 \tag{0.3}
\]

Let

\[
 M=AA^*=\operatorname{diag}(m_g),
 \qquad m_g=|H_g|,
 \tag{0.4}
\]

and

\[
 D=RR^*=CMC^*=\operatorname{diag}(N_a),
 \qquad N_a=\sum_{g\mapsto a}m_g.
 \tag{0.5}
\]

The fixed-fibre Wick operator is

\[
 B_R=R^*SR-dI,
 \qquad d>0,
 \tag{0.6}
\]

and its occupied-cell quotient is

\[
 Q_R=D^{1/2}SD^{1/2}-dI.
 \tag{0.7}
\]

### Theorem T-108104

Put

\[
 V=A^*M^{-1/2},
 \qquad
 T=D^{-1/2}CM^{1/2},
 \qquad
 U=R^*D^{-1/2}.
 \tag{0.8}
\]

Then

\[
 V^*V=I_{\mathcal G},
 \qquad
 TT^*=I_{\mathcal C},
 \qquad
 \boxed{U=VT^*.}
 \tag{0.9}
\]

For every literal coefficient vector \(z\), define the normalized group and
cell currents

\[
 x=V^*z=M^{-1/2}Az,
 \qquad
 y=Tx=D^{-1/2}Rz.
 \tag{0.10}
\]

There is an exact orthogonal decomposition

\[
 \boxed{
 z=
 \underbrace{(I-VV^*)z}_{\text{within-history fluctuation}}
 +
 \underbrace{V(I-T^*T)x}_{\text{same-cell group-current fluctuation}}
 +
 \underbrace{Uy}_{\text{physical cell current}}.}
 \tag{0.11}
\]

The first two summands lie in \(\ker R\).  Consequently

\[
 \boxed{
 B_Rz
 =-d(I-VV^*)z
 -dV(I-T^*T)x
 +UQ_Ry.}
 \tag{0.12}
\]

Functional calculus gives the complete positive and negative actions:

\[
 \boxed{(B_R)_+z=U(Q_R)_+y,}
 \tag{0.13}
\]

\[
 \boxed{
 (B_R)_-z
 =d(I-VV^*)z+dV(I-T^*T)x+U(Q_R)_-y.}
 \tag{0.14}
\]

Thus the positive part depends only on the final signed cell currents
\(s_a\), not on the distribution of coefficients among histories or among
source groups in one cell.

In particular,

\[
 Az=Az'\Longrightarrow (B_R)_+z=(B_R)_+z',
 \tag{0.15}
\]

and the stronger implication

\[
 CAz=0\Longrightarrow (B_R)_+z=0
 \tag{0.16}
\]

allows nonzero group currents to cancel inside one residue cell.  Equation
(0.16) strictly enlarges the previously exhibited class \(Az=0\).

## 1. Exact two-stage energy ledger

Write

\[
 E_g=\sum_{\omega\in H_g}|z_\omega|^2.
 \tag{1.1}
\]

The three orthogonal norms in (0.11) are

\[
 \boxed{
 V_{\rm hist}(z)
 :=\|(I-VV^*)z\|^2
 =\sum_g\left(E_g-\frac{|Z_g|^2}{m_g}\right),}
 \tag{1.2}
\]

\[
 \boxed{
 V_{\rm group}(z)
 :=\|V(I-T^*T)x\|^2
 =\sum_g\frac{|Z_g|^2}{m_g}
  -\sum_a\frac{|s_a|^2}{N_a},}
 \tag{1.3}
\]

and

\[
 \boxed{
 \|y\|^2=\sum_a\frac{|s_a|^2}{N_a}.}
 \tag{1.4}
\]

The second variance has the cellwise form

\[
 \boxed{
 V_{\rm group}(z)
 =\sum_a\sum_{g\mapsto a}
 m_g\left|\frac{Z_g}{m_g}-\frac{s_a}{N_a}\right|^2.}
 \tag{1.5}
\]

Therefore

\[
 \boxed{
 \|z\|^2
 =V_{\rm hist}(z)+V_{\rm group}(z)
  +\sum_a\frac{|s_a|^2}{N_a}.}
 \tag{1.6}
\]

Both variances are nonnegative and are paid at the exact eigenvalue \(-d\).
The full scalar decomposition is

\[
 \boxed{
 \langle z,B_Rz\rangle
 =\langle y,Q_Ry\rangle
 -dV_{\rm hist}(z)-dV_{\rm group}(z).}
 \tag{1.7}
\]

The positive and negative quadratic ledgers are

\[
 \boxed{
 \langle z,(B_R)_+z\rangle
 =\langle y,(Q_R)_+y\rangle,}
 \tag{1.8}
\]

\[
 \boxed{
 \langle z,(B_R)_-z\rangle
 =\langle y,(Q_R)_-y\rangle
 +dV_{\rm hist}(z)+dV_{\rm group}(z).}
 \tag{1.9}
\]

This is a source-labelled refinement of the T-108100 decomposition.  It
identifies exactly which part of \(\ker R\) comes from history fluctuations
and which part comes from cancellation among different retained arithmetic
or source groups in one physical cell.

## 2. Proof of the factorization

Because the history groups partition \(\Omega\),

\[
 AA^*=M.
\]

Hence \(V^*V=M^{-1/2}AA^*M^{-1/2}=I\).  Similarly,

\[
 CMC^*=RR^*=D,
\]

so \(TT^*=I\).  Finally,

\[
 VT^*
 =A^*M^{-1/2}M^{1/2}C^*D^{-1/2}
 =R^*D^{-1/2}=U,
\]

proving (0.9).

The atom projection onto vectors constant within each source group is
\(VV^*=A^*M^{-1}A\).  Decompose first at that projection and then decompose
the normalized group current at the coisometry \(T\):

\[
 z=(I-VV^*)z+Vx,
 \qquad
 x=(I-T^*T)x+T^*y.
\]

This is (0.11).  The first term lies in \(\ker A\subseteq\ker R\).  For the
second,

\[
 D^{-1/2}RV(I-T^*T)x
 =T(I-T^*T)x=0.
\]

Thus both terms are in \(\ker R\), while the last is \(VT^*y=Uy\).
T-108100 gives

\[
 B_R=UQ_RU^*\oplus(-dI_{\ker R}),
\]

which immediately proves (0.12)--(0.14).

For (1.2), the minimum-energy vector with fixed group sums \(Z_g\) is
constant on each group and has energy \(|Z_g|^2/m_g\).  Formula (1.3)
follows from the orthogonal decomposition of \(x\) under \(T\).  Expanding
the weighted cell means proves (1.5).  Equations (1.6)--(1.9) follow.

## 3. Source-authorized history recombination

The frozen signed-history packet partitions atoms by a label retaining the
arithmetic tuple and every non-history source label.  Its aggregated
coefficient is exactly \(Z_g\).  Every history in the group has the same
physical residues, so this partition is precisely an admissible map \(A\)
in (0.1), and the original residue aggregation factors as \(R=CA\).

Therefore history recombination has two distinct exact consequences.

1. For the complete principal moment, the inherited packet supplies its paid
   diagonal conversion ledger.
2. For the fixed-fibre positive Wick operator, no conversion error occurs at
   all: equations (0.13) and (0.15) show that the original positive action is
   exactly determined by the grouped currents.

The operator and multiplicities are not silently changed.  One evaluates the
**original** \((B_R)_+\), with the original atom multiplicities \(m_g\) and
cell multiplicities \(N_a\), from the grouped current vector.  Replacing each
group by a new multiplicity-one atom would define a different operator and
is not authorized by this theorem.

After history grouping, the only source information still visible to the
positive part is

\[
 \boxed{
 y_a=\frac{1}{\sqrt{N_a}}
 \sum_{g\mapsto a}Z_g.}
 \tag{3.1}
\]

All same-group history oscillation is in \(V_{\rm hist}\), and all
same-cell cancellation among distinct groups is in \(V_{\rm group}\).
Both are exact negative Hodge payments.

## 4. The live hundred-history block

For the source-locked control,

\[
 m_1=N_a=100,
 \qquad
 Z_1=4w,
 \qquad
 E_1=676|w|^2.
\]

There is only one source group in the declared subpacket, so

\[
 V_{\rm group}=0.
\]

Equations (1.2)--(1.4) give

\[
 \boxed{
 V_{\rm hist}
 =\left(676-\frac{16}{100}\right)|w|^2
 =\frac{16896}{25}|w|^2,}
 \tag{4.1}
\]

and

\[
 \boxed{
 \|y\|^2=\frac{16}{100}|w|^2=\frac4{25}|w|^2.}
 \tag{4.2}
\]

Thus T-108102's factor \(4225\) is recovered as the one-group specialization
of the full two-stage theorem:

\[
 \frac{676}{4/25}=4225.
\]

The new theorem adds the next exact possibility.  Distinct grouped
arithmetic pairs may carry nonzero \(Z_g\) but satisfy

\[
 \sum_{g\mapsto a}Z_g=0.
\]

Then their complete group-mean energy is paid by \(V_{\rm group}\), and the
positive quotient sees zero.  This is genuine cross-group cancellation at
the cell-current level, not selection of a zero-sum subset inside one
history group.

## 5. Exact replay fixtures

The bounded producer uses exact rational arithmetic only.

### Two-stage fixture

Four history groups of sizes

\[
 (2,3,1,4)
\]

occupy two cells with total multiplicities \((5,5)\).  Two different
literal vectors have the same group sums and therefore the same cell
currents, but different literal energies.  Their positive quotient debts
are exactly equal, while their negative history payments differ.

For the quotient control

\[
 Q=\begin{pmatrix}1&2\\2&1\end{pmatrix},
\]

the positive and negative quotient eigenvalues are \(3\) and \(-1\).
The producer verifies (1.7)--(1.9), including the original full Wick scalar,
with fractions only.

### Cross-group zero-current fixture

Two groups of size two in one cell carry group sums \(2\) and \(-2\).  Each
group is internally constant, so

\[
 V_{\rm hist}=0.
\]

Their cell current is zero and

\[
 \boxed{V_{\rm group}=4,
 \qquad \|y\|^2=0.}
\]

This gives an exact vector in \(\ker R\setminus\ker A\).  Its positive debt
is zero and its whole energy lies in the \(-d\) block.

## 6. Strategic consequence

The fixed-fibre positive route no longer needs to carry literal history
vectors after the source-authorized sums \(Z_g\) have been formed.  The exact
pipeline is

```text
literal histories z_(g,h)
  -> grouped signed currents Z_g
  -> cell currents s_a = sum_(g->a) Z_g
  -> normalized quotient current y_a=s_a/sqrt(N_a)
  -> (Q_R)_+.
```

The first arrow loses no positive information.  The second arrow converts
same-cell cross-group cancellation into an exact negative Hodge block.  The
remaining positive obstruction is therefore entirely

\[
 \boxed{
 \langle y,(Q_R)_+y\rangle,}
\]

with the **complete** grouped current, multiplicity census, and conductor
labels still attached.

This does not supply those complete currents.  The live collision files
certify subblocks, not a full fibre.  The next gate is consequently

```text
LIVEQUOTIENTCURRENT108106

For each source-locked live owner panel, enumerate or symbolically assemble
all retained source-group currents Z_g, their cell map, and the original
multiplicities m_g and N_a.  Form

  y_a = N_a^(-1/2) sum_(g->a) Z_g

before every absolute value.  Then prove a signed estimate after conductor
recombination, or realize the resulting currents in a compatible relative
partial-Frobenius trace object.
```

## 7. Scope ledger

| statement | status |
|---|---|
| exact factorization \(R=CA\) | **PROVED** |
| isometry/coisometry factorization \(U=VT^*\) | **PROVED** |
| orthogonal three-block decomposition (0.11) | **PROVED** |
| within-history block has eigenvalue \(-d\) | **PROVED** |
| same-cell cross-group zero-current block has eigenvalue \(-d\) | **PROVED** |
| positive part invariant under authorized history aggregation | **PROVED** |
| live factor-4225 ledger | **RECOVERED EXACTLY** |
| complete live grouped-current and multiplicity census | **OPEN** |
| signed cross-conductor quotient estimate | **OPEN** |
| global partial Frobenius / RELTRACE | **OPEN** |
| principal binding | **OPEN** |
| RH / GRH | **UNPROVED** |

## 8. Replay boundary

```text
python -B research/riemann-structures/source_grouped_positive_hodge_descent.py --check
python -B -O research/riemann-structures/source_grouped_positive_hodge_descent.py --check
python -B -m unittest tests.test_source_grouped_positive_hodge_descent
python -B -O -m unittest tests.test_source_grouped_positive_hodge_descent
```

The replay authenticates six exact predecessor blobs and uses exact integer
and rational arithmetic.  It does not enumerate a complete fibre, a
conductor family, a curve, a sheaf, a zero set, or an admissible global
coefficient family.
