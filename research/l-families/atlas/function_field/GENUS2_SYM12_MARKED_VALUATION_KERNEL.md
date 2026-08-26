# Genus-two `Sym^12`: the marked `(9,12)` valuation kernel

Status: exact finite invariant-theory calculation, with a source/action audit
still required before assigning the surviving directions to lift or stable
automorphic channels.

Scope: the `S_5`-invariant marked quotient at Siegel weight `(j,k)=(12,3)`.
No point counts, Frobenius interpolation, or Galois realization are used.

Companion replay:
[`genus2_sym12_marked_valuation_kernel.py`](genus2_sym12_marked_valuation_kernel.py).
Canonical output:
[`genus2_sym12_marked_valuation_kernel.json`](genus2_sym12_marked_valuation_kernel.json).

## 1. Result

Clery--van der Geer's regularity criterion turns the previously isolated
`66`-dimensional pre-holomorphic space into an exact finite boundary problem.
For the representative partition

\[
\pi=\{1,2,6\}\mid\{3,4,5\},
\]

the complete coefficientwise high-jet matrix has size `3481 x 66` after the
source's two-chart minimum is linearized.  Exact rational elimination gives

\[
\boxed{\operatorname{rank}_{\mathbb Q}J_\pi=51,
\qquad \dim\ker J_\pi=15.}
\tag{1}
\]

The same rank is obtained modulo `1000003` and `1000033`.  Since the standard
`S_5` fixing label `6` is transitive on the ten `3+3` partitions, one
representative imposes all ten boundary conditions on an `S_5`-fixed
covariant.

Thus the proposed zero-kernel shortcut does **not** close: the exact marked
covariant calculation leaves `15` holomorphic directions.

This is a useful obstruction, not a conclusion that the stable/general
Galois channel `G` is nonzero.  The `15` directions have not yet been split
into lift, endoscopic, character-twisted, and stable pieces.  Moreover, they
force a comparison between the natural root-permutation action used here and
the `S_6`/outer-automorphism convention used in the conditional low-weight
dimension rows.  Until that comparison is explicit, this packet does not
attach the `15` to any official isotypical row.

## 2. The primary-source criterion

The calculation uses Section 7 of Clery--van der Geer,
[*Tautological modular forms of level two and degree two*](https://arxiv.org/abs/2605.13300),
v1, especially Definition 7.1, Proposition 7.3, and Criterion 7.4.

Write a covariant of bidegree `(d,b)` as

\[
C_{d,b}=\sum_{j=0}^{b}P_jx_1^{b-j}x_2^j.
\]

For a `3+3` partition `pi`, choose one block and make the two substitutions

\[
\begin{aligned}
\varphi_\pi:
  (l_{i,1},l_{i,2})&\longmapsto(l_{i,1}+t,1),\\
\varphi'_\pi:
  (l_{i,1},l_{i,2})&\longmapsto(1,l_{i,2}+t)
\end{aligned}
\qquad (i\text{ in the chosen block}).
\]

Their definition is

\[
v_\pi(P_j)
=2d-\min\left\{
\deg_t\varphi_\pi(P_j),
\deg_t\varphi'_\pi(P_j)
\right\}.
\tag{2}
\]

Proposition 7.3 identifies this with order along the boundary divisor, and
Criterion 7.4 says that the associated meromorphic modular form is
holomorphic exactly when the boundary valuations are nonnegative.  Their
worked `(d,b)=(2,6)` example applies the condition to every coefficient; this
packet follows that coefficientwise convention.

At `(d,b)=(9,12)`, (2) says that, for every `j`, at least one of the two chart
polynomials has `t`-degree at most `18`.  It is essential that the source uses
a **minimum**.  Killing the degree-`>18` part in both charts would impose an
incorrectly strong condition.

## 3. Authenticated `66`-dimensional source

Put `R=Sym^9(V)`.  Permuting the first five roots and distinguishing the
sixth gives the natural root-symmetric module

\[
W=\operatorname{Sym}^{5}(R)\otimes R.
\]

The order-`12` covariants are

\[
H=\operatorname{Hom}_{\mathrm{SL}_2}
\left(\operatorname{Sym}^{12}(V),W\right).
\tag{3}
\]

In the monomial basis `e_a=u^(9-a)v^a`, a weight-`12` state is a pair

\[
(a_1\leq\cdots\leq a_5;c),
\qquad
a_1+\cdots+a_5+c=21.
\]

There are `752` such states.  Weight `14` has `686` states.  With

\[
E e_a=a e_{a-1},
\]

the exact sparse raising map

\[
E:W_{12}\longrightarrow W_{14}
\]

has rational rank `686`, independently certified modulo `1000003`.  Hence

\[
\dim H=752-686=66.
\tag{4}
\]

The replay constructs a primitive integral basis of this kernel.  Its
canonical digest is

```text
6f09eb35f716efab67f717cf55adcde1dab3e9fc11ef73747d41668f95d95c1e
```

This realizes, rather than merely recounts, the `66`-dimensional space from
the preceding defect audit.

## 4. Exact representative boundary map

For `pi={1,2,6}|{3,4,5}`, split the five symmetric labels as `2+3`.  In the
symmetric-polynomial basis the exact coproduct is

\[
\Delta_{2,3}(y^n)
=\sum_{\substack{m\leq n\\|m|=2}}
\left(\prod_a\binom{n_a}{m_a}\right)
x^m z^{n-m}.
\tag{5}
\]

The selected factor is

\[
\operatorname{Sym}^2(R)\otimes R_6,
\]

and the unselected factor is `Sym^3(R)`.  The replay uses twice the canonical
symmetrization of `Sym^2(R)` into labels `1,2`, solely to keep every matrix
entry integral.  This is one common nonzero scalar and does not change a
kernel.

Starting with a highest-weight vector `h in H`, its coefficient `P_j` is a
nonzero scalar multiple of `F^j h`; the coefficientwise scalar is irrelevant
to every degree and kernel calculation.  Applying (5), the two substitutions
in Section 2, and retaining the terms of `t`-degree `19,...,27` gives two
exact linear maps

\[
A_j:H\to T_j^\varphi,
\qquad
B_j:H\to T_j^{\varphi'}.
\]

For a vector `h`, the source condition is initially the union

\[
h\in\ker A_j\ \cup\ \ker B_j.
\tag{6}
\]

The key technical point is that (6) really does linearize on `H`.  Exact
rational ranks are:

| `j` | `rank A_j` | `rank B_j` | rank stacked | deduction |
|---:|---:|---:|---:|---|
| 0 | 66 | 5 | 66 | `ker A_0 subset ker B_0` |
| 1 | 66 | 9 | 66 | `ker A_1 subset ker B_1` |
| 2 | 66 | 16 | 66 | `ker A_2 subset ker B_2` |
| 3 | 64 | 22 | 64 | `ker A_3 subset ker B_3` |
| 4 | 63 | 32 | 63 | `ker A_4 subset ker B_4` |
| 5 | 58 | 41 | 58 | `ker A_5 subset ker B_5` |
| 6 | 51 | 51 | 51 | `ker A_6 = ker B_6` |

Therefore (6) equals `ker B_j` for `j=0,...,6`.  The Weyl involution swaps
`j` with `12-j` and swaps the two charts, so for `j=7,...,12` it equals
`ker A_j`.

The genuine Criterion 7.4 matrix on the `66` columns is consequently

\[
J_\pi=
\begin{pmatrix}
B_0\\ \vdots\\ B_6\\ A_7\\ \vdots\\ A_{12}
\end{pmatrix}.
\tag{7}
\]

Its coefficient ranks, in order `j=0,...,12`, are

\[
5,9,16,22,32,41,51,41,32,22,16,9,5.
\]

The combined rank is only `51`; the later coefficient blocks add no rank
beyond the middle block.  A primitive basis for the `15`-dimensional kernel
has digest

```text
1326459cad19fcf373b6d4364acfc5597acb9799d5fbb87ca4c8e905fd8ce95d
```

## 5. What is proved

The following are exact statements in the natural split-root convention:

1. The `S_5`-fixed pre-holomorphic source (3) has dimension `66`.
2. The two-chart minimum in Criterion 7.4 linearizes coefficient by
   coefficient through the kernel containments in the table above.
3. The representative `3+3` regularity matrix (7) has rational rank `51`.
4. Its kernel has dimension `15`.
5. Standard `S_5` transitivity carries the representative condition to all
   ten `3+3` boundary divisors.

The computation is independently checked in three characteristics: over
`Q`, modulo `1000003`, and modulo `1000033`.  All three ranks are `51`.

## 6. What is not proved

This packet does **not** prove any of the following:

- that one of the `15` directions is stable/general rather than a lift,
  endoscopic form, or character-twisted channel;
- that the stable cohomological term `G` is nonzero;
- the all-`q` formula for `Hhat_12`;
- an unconditional Galois realization of Shmakov's displayed nonregular
  Eisenstein associated-graded expression;
- `epsilon_Eis=L`, or any change to the corrected conditional status of that
  identity;
- RH or GRH.

In particular, the earlier formal identity

\[
\widehat H_{12}=-\mathbb L f_-+\varepsilon_{\mathrm{Eis}}-G
\]

retains exactly its prior proof grade.  This packet is independent finite
algebra; it does not promote a source-caveated Euler expression to a Galois
or Frobenius theorem.

## 7. The new reconciliation problem

The conditional `(12,3)` official-data reading used in the preceding audit
contains no row that was assigned a standard `S_5` fixed vector.  Equation
(1) says that the natural marked covariant calculation does not vanish.
These statements should not be forced together without checking conventions.

There are at least two live explanations:

1. **Low-weight continuation.**  The implemented `k=3` row is based on the
   same nonregular continuation already marked conditional in
   Bergstrom--Clery, Remark 5.4.
2. **Action convention.**  Clery--van der Geer explicitly warn that the
   natural permutation action on six Weierstrass points and the action used
   in parts of the level-two literature differ by the outer automorphism of
   `S_6`.  Odd multidegree and character normalizations must also be traced
   through `nu` before branching an official row to the marked subgroup.

The smallest next theorem-grade task is therefore not another point count.
It is an equivariance diagram:

\[
\begin{CD}
\text{root-symmetric covariants} @>{\nu}>>
\text{level-two modular forms}\\
@V{S_5\text{ fixing root }6}VV @VV{\text{official }S_5\text{ convention}}V\\
\text{marked covariants} @>>> \text{marked modular forms}.
\end{CD}
\]

One must compute the possible outer automorphism and character twist on this
diagram, then place the `15`-dimensional kernel into lift/general channels.
Only the projection of that kernel to the stable/general summand can bear on
`G`.

## 8. Resource and replay audit

The replay is deliberately bounded:

- zero point counts;
- one representative partition;
- `752` states in the largest source weight space;
- `66` source columns;
- exact sparse arithmetic over `Q` plus two finite-field rank checks;
- a designed wall-clock cap of `60` seconds on the project machine (the
  recorded development run completed in about `36` seconds).

Run:

```text
python research/l-families/atlas/function_field/genus2_sym12_marked_valuation_kernel.py --check
pytest -q tests/test_genus2_sym12_marked_valuation_kernel.py
```

The tests separately verify the `752 -> 686` highest-weight map, the
twice-canonical chart symmetrization, the first coefficient's two-chart
containment, the committed full-rank certificate, and the resource firewall.

## 9. Novelty boundary and sources

Primary inputs:

- Clery--van der Geer,
  [*Tautological modular forms of level two and degree two*](https://arxiv.org/abs/2605.13300):
  the split-root covariant construction, natural `S_6` warning, Definition
  7.1, Proposition 7.3, and Criterion 7.4.
- Bergstrom--Clery,
  [*Dimension formulas for spaces of vector-valued Siegel modular forms of
  degree two and level two*](https://arxiv.org/abs/2309.04388): the
  low-weight dimension framework and its nonregular caveat.
- Shmakov,
  [*Cohomology of Local Systems on Siegel Threefolds with Square-Free
  Parahoric Level*](https://openscholar.uga.edu/nanna/record/1979/files/dissertation.pdf?registerDownload=1&version=1&withMetadata=0&withWatermark=0):
  the separately caveated nonregular cohomological formulas discussed in the
  preceding defect audit.

Clery--van der Geer provide the general valuation criterion; they do not, in
the cited version, print the `(d,b)=(9,12)` marked `66 x 3481` calculation or
the rank `51`/nullity `15` result.  This packet establishes that result inside
the project.  No claim of external novelty or publication priority is made
without a dedicated literature and author-convention check.
