# Frobenius extension towers: exact aliasing and divisor-grid fidelity

Status: **exact finite-extension permutation theorem, exact Möbius-polynomial
alias criterion, and exact finite-tower linear-fidelity obstruction; no
native FFPS source complex, categorical Adams compression, Betti lower
bound, trace estimate, CYSEL, RH, or GRH theorem**

Bounded exact replay:
[ffps_frobenius_extension_tower_aliasing.py](ffps_frobenius_extension_tower_aliasing.py).
Canonical summary:
[ffps_frobenius_extension_tower_aliasing.json](ffps_frobenius_extension_tower_aliasing.json).

Frozen dependencies:

| source | commit | git blob | role |
|---|---|---|---|
| FFPS_NATIVE_PARTIAL_FROBENIUS_VERDICT.md | e3903136912402a969abee7bfcf1ad5f9dfbd1a0 | 19939eb240ca6b2b6d5221954cec76fe0f5c4f9c | native partial-Frobenius obstruction |
| FFPS_CLOSED_POINT_ADAMS_COMPRESSION.md | 05da4d1705d994dd02d650f321196f8464034ba8 | c79e52ebf0099fe416bc2c79dcb041cc21e025fb | extension-field Adams alternative |
| L-106191 | 98af0db6e | 85c4ef92ead7d8b235f9c195c3c0acd16d16030f | centered graph-kernel normalization |

## 0. Verdict

Passing from geometric graph supports to their actions on one finite
extension does not preserve an unbounded Frobenius-degree coordinate.
It produces an exact cyclic quotient.

Let \(Q\) be a prime power, let \(N=Q^r\), and let \(P_r\) be the
permutation operator induced by

\[
 \sigma:x\longmapsto x^Q
 \qquad\hbox{on }\mathbf F_{Q^r}.
\]

With \(J\) the \(N\)-by-\(N\) all-ones matrix and
\(E=N^{-1}J\), define the correctly centered graph kernel

\[
 \boxed{H_n^{(r)}=P_r^n-E.}
\tag{0.1}
\]

There are three genuinely different observations:

| observation | value | information retained |
|---|---:|---|
| total number of graph points | \(Q^r\) | none about \(n\) |
| operator trace of \(H_n^{(r)}\) | \(Q^{\gcd(n,r)}-1\) | only \(\gcd(n,r)\) |
| complete pointwise kernel | \(H_n^{(r)}\) | exactly \(n\bmod r\) |

Thus neither total graph counts nor operator traces test whether a signed
support combination survives as a correspondence operator.

A finite tower \(T=\{r_1,\ldots,r_s\}\) remembers the exponent label modulo
\(\operatorname{lcm}(T)\).  Even injective labels do not guarantee linear
fidelity of a divisor grid.  The exact test is the rank of one small
residue-incidence matrix.  This distinction supplies both:

1. a viable bounded construction for any specified finite grid when the
   incidence matrix has full column rank; and
2. a quantitative no-go for realizing every coefficient of a growing
   Möbius divisor grid in literal point-function permutation models at
   bounded extension depth.

The no-go is deliberately not promoted to sheaf rank or Betti number.
A graph correspondence can have a compact geometric description even when
its point-function matrix has dimension \(Q^r\).

## 1. One extension level

### Theorem 1.1: Frobenius cycle ledger

For every \(d\mid r\), the number of cycles of exact length \(d\) in
\(\sigma\) is

\[
 c_d={1\over d}\sum_{e\mid d}\mu(d/e)Q^e.
\tag{1.1}
\]

Consequently

\[
 \sum_{d\mid r}dc_d=Q^r.
\]

**Proof.**
The fixed points of \(\sigma^d\) in an algebraic closure are
\(\mathbf F_{Q^d}\), of cardinality \(Q^d\).  Möbius inversion gives the
number of elements of exact degree \(d\); division by the orbit length
gives (1.1).  The exact-degree strata partition
\(\mathbf F_{Q^r}\).  \(\square\)

### Theorem 1.2: scalar collapse, trace collapse, and pointwise aliasing

For every \(m,n\geq0\):

\[
\begin{aligned}
 \sum_{x,y}(P_r^n)_{x,y}&=Q^r,\\
 \sum_{x,y}(H_n^{(r)})_{x,y}&=0,\\
 \operatorname{Tr}(P_r^n)&=Q^{\gcd(n,r)},\\
 \operatorname{Tr}(H_n^{(r)})&=Q^{\gcd(n,r)}-1,\\
 P_r^m=P_r^n
 \quad&\Longleftrightarrow\quad
 H_m^{(r)}=H_n^{(r)}
 \quad\Longleftrightarrow\quad
 m\equiv n\pmod r.
\end{aligned}
\tag{1.2}
\]

Here \(\gcd(0,r)=r\).

**Proof.**
Every graph of a map on an \(N\)-point set contains \(N\) points.
Both row and column sums of \(P_r^n\) are one, whereas \(E\) has the same
property, proving the first two lines.  The trace is the number of fixed
points of \(x\mapsto x^{Q^n}\), namely
\(\#\mathbf F_{Q^{\gcd(n,r)}}\).  Finally \(\sigma\) has exact order \(r\):
there are elements of exact degree \(r\), on which it has an \(r\)-cycle.
Subtracting the same \(E\) does not change equality.  \(\square\)

This proves a useful blindness example.  For \(Q=2,r=3\),

\[
 P_3^5-P_3
\]

has total entry sum zero and operator trace zero, but it is a nonzero
operator of rank four.  Scalar and trace cancellation therefore do not
imply support cancellation.

### Theorem 1.3: centered cyclic algebra

On the full \(Q^r\)-dimensional point-function space,

\[
 \operatorname{rank}H_n^{(r)}=Q^r-1
\tag{1.3}
\]

for every \(n\), and

\[
 H_m^{(r)}H_n^{(r)}=H_{m+n}^{(r)}
\tag{1.4}
\]

with indices read modulo \(r\).  In particular

\[
 \mathscr A_r=
 \operatorname{span}_{\mathbf Q}
 \{H_0^{(r)},\ldots,H_{r-1}^{(r)}\}
 \cong\mathbf Q[C_r]
\tag{1.5}
\]

is \(r\)-dimensional and has unit \(H_0^{(r)}=I-E\).

The exact minimal polynomials on the full point-function space are

\[
\begin{aligned}
 m_{P_r}(t)&=t^r-1,\\
 m_{H_1^{(r)}}(t)&=t(t^r-1),\\
 m_{H_n^{(r)}}(t)&=
 t\bigl(t^{r/\gcd(n,r)}-1\bigr).
\end{aligned}
\tag{1.6}
\]

**Proof.**
Split the point-function space into constants and the mean-zero subspace
\(W\).  The operator \(H_n^{(r)}\) is zero on constants and equals the
invertible \(P_r^n\) on \(W\), proving (1.3).  Since \(P_rE=EP_r=E\) and
\(E^2=E\), direct multiplication proves (1.4).

A full \(r\)-cycle supplies every \(r\)-th root in the spectrum of \(P_r\).
The eigenvalue one remains on \(W\), because the \(Q\) rational fixed
points supply nonconstant fixed vectors.  Hence all \(r\)-th roots still
occur on \(W\), which proves linear independence in (1.5) and all three
minimal polynomials in (1.6).  \(\square\)

The important compression is exact but limited: the literal matrices are
\(Q^r\)-dimensional, while the algebra generated by all shifted centered
graphs is only \(r\)-dimensional.

## 2. Möbius divisor polynomials

Use the closed-point orientation

\[
 M_a(t)=\sum_{e\mid a}\mu(e)t^{a/e}.
\tag{2.1}
\]

At extension level \(r\),

\[
 M_a(P_r)=
 \sum_{j=0}^{r-1}
 \left(
   \sum_{\substack{e\mid a\\a/e\equiv j\pmod r}}\mu(e)
 \right)P_r^j.
\tag{2.2}
\]

Because \(I,P_r,\ldots,P_r^{r-1}\) are linearly independent,

\[
 \boxed{
 M_a(P_r)=0
 \Longleftrightarrow
 \sum_{\substack{e\mid a\\a/e\equiv j\pmod r}}\mu(e)=0
 \quad\hbox{for every }j\bmod r.}
\tag{2.3}
\]

For \(a>1\), \(\sum_{e\mid a}\mu(e)=0\), so replacing every \(P_r^{a/e}\)
by \(H_{a/e}^{(r)}\) leaves exactly the same operator.

The general rank is a finite cyclotomic calculation.  If \(m_r(\zeta)\)
denotes the multiplicity of an \(r\)-th root \(\zeta\) as an eigenvalue of
\(P_r\), then

\[
 \operatorname{rank}M_a(P_r)=
 \sum_{\substack{\zeta^r=1\\M_a(\zeta)\ne0}}m_r(\zeta).
\tag{2.4}
\]

The multiplicities are determined by (1.1): a cycle of length \(d\)
contributes once to each \(d\)-th root.

For a prime \(p\),

\[
 M_p(P_r)=P_r^p-P_r=P_r(P_r^{p-1}-I)
\]

and therefore

\[
 \boxed{
 \operatorname{rank}M_p(P_r)
 =
 Q^r-\sum_{d\mid r}c_d\gcd(d,p-1).}
\tag{2.5}
\]

In particular \(M_p(P_r)=0\) exactly when \(r\mid p-1\).
The replay checks, among other rows,

| \(Q\) | \(a\) | \(r\) | result |
|---:|---:|---:|---|
| 2 | 5 | 3 | nonzero, rank 4, trace 0 |
| 2 | 7 | 3 | zero by \(7\equiv1\pmod3\) |
| 2 | 7 | 4 | nonzero, rank 6, trace 0 |
| 2 | 11 | 5 | zero by \(11\equiv1\pmod5\) |

Thus exact extension-field realizations can annihilate a nontrivial
Möbius recombination merely through modular aliasing.

## 3. A finite extension tower

Let \(T=\{r_1,\ldots,r_s\}\) and put

\[
 L_T=\operatorname{lcm}(r_1,\ldots,r_s).
\]

The tuple of complete pointwise kernels associated to exponent \(n\) is

\[
 \mathbf H_T(n)=
 (H_n^{(r_1)},\ldots,H_n^{(r_s)}).
\]

### Theorem 3.1: label period and cyclic-algebra capacity

\[
 \mathbf H_T(m)=\mathbf H_T(n)
 \Longleftrightarrow
 m\equiv n\pmod {L_T}.
\tag{3.1}
\]

The joint centered span, with internal unit
\((H_0^{(r)})_{r\in T}\), is a cyclic algebra of dimension

\[
\boxed{
 D_T=
 \deg\operatorname{lcm}_{r\in T}(t^r-1)
 =
 \sum_{\substack{d\ge1\\d\mid r\ {\rm for\ some}\ r\in T}}\varphi(d).}
\tag{3.2}
\]

**Proof.**
Equation (3.1) follows level by level from (1.2).  Polynomial evaluation
in the tuple of cyclic generators has kernel

\[
 \bigcap_{r\in T}(t^r-1)
 =
 \left(
   \operatorname{lcm}_{r\in T}(t^r-1)
 \right)
\]

in the principal ideal domain \(\mathbf Q[t]\), where the constant
polynomial acts as the centered unit rather than the ambient identity.
Factoring
\(t^r-1\) into cyclotomic polynomials proves (3.2).  \(\square\)

If one instead takes the conventionally unital subalgebra of the full
endomorphism algebra, the ambient identity adds the independent tuple of
constant projectors.  Its dimension is \(D_T+1\), and the minimal
polynomial of the generator tuple is

\[
 t\operatorname{lcm}_{r\in T}(t^r-1).
\]

### Theorem 3.2: exact divisor-grid fidelity test

Let \(S=\{n_1,\ldots,n_k\}\) be the exponent support to be retained.
Form the stacked residue-incidence matrix

\[
 B_{(r,j),n}=\mathbf 1_{n\equiv j\pmod r},
\qquad
r\in T,\quad0\le j<r,\quad n\in S.
\tag{3.3}
\]

Then the map

\[
 (c_n)_{n\in S}
 \longmapsto
 \sum_{n\in S}c_n\mathbf H_T(n)
\tag{3.4}
\]

is injective if and only if \(B\) has column rank \(k\).

**Proof.**
At level \(r\), the coefficients of the independent basis
\(\{H_0^{(r)},\ldots,H_{r-1}^{(r)}\}\) are precisely the residue-class sums
recorded by the rows of \(B\).  Taking the direct sum over the levels gives
(3.4).  \(\square\)

This is stronger than label injectivity.  The replay gives:

| divisor grid | tower | labels distinct? | \(D_T\) | grid rank | faithful? |
|---|---|---:|---:|---:|---:|
| nonzero-\(\mu\) divisors of 30 | \(2,3,5\) | yes | 8 | 7 | no |
| nonzero-\(\mu\) divisors of 210 | \(2,3,5,7\) | yes | 14 | 13 | no |
| nonzero-\(\mu\) divisors of 210 | \(2,3,5,7,11\) | yes | 24 | 16 | yes |

The first row is especially diagnostic: CRT labels distinguish all eight
columns and the ambient cyclic algebra also has dimension eight, but the
particular divisor columns still satisfy one linear relation.

For a single specified Möbius coefficient vector, full grid fidelity is
unnecessary.  It is enough that its image is nonzero.  All three replay
towers retain that particular signed vector even in the two nonfaithful
rows.  The theorem therefore separates three questions:

1. are the exponents differently labelled;
2. does one chosen signed sum survive;
3. can every coefficient on the grid be recovered?

They are not equivalent.

## 4. Literal matrix cost

Suppose \(a\) has \(\omega(a)=w\) distinct prime factors.  Its nonzero
Möbius divisor grid has

\[
 k=2^w
\tag{4.1}
\]

columns.

For one extension level, linear fidelity requires \(r\ge k\), so the
literal point-function permutation matrix has dimension at least

\[
 Q^k=Q^{2^w}.
\tag{4.2}
\]

For an arbitrary tower whose largest level is \(R\), (3.2) gives the
necessary bound

\[
 k\le D_T
 \le\sum_{d\le R}\varphi(d)
 \le {R(R+1)\over2}.
\tag{4.3}
\]

Hence

\[
 R\ge
 \left\lceil{\sqrt{8k+1}-1\over2}\right\rceil,
\qquad
 \max_{r\in T}Q^r
 \ge
 Q^{\left\lceil(\sqrt{8k+1}-1)/2\right\rceil}.
\tag{4.4}
\]

Even the weak universal tower bound therefore leaves a literal matrix
dimension exponential in \(2^{w/2}\).  It is much smaller than the
single-level cost, but still unbounded and doubly exponential in \(w\)
for fixed \(Q>1\).

Equations (4.2)--(4.4) are necessary costs only for linear fidelity of
every coefficient on the complete nonzero-Möbius grid.  They do not apply
to one fixed signed vector, which can remain visible far below those
thresholds.

## 5. What this says about the support-shift escape

The extension-field idea has a real exact use:

~~~text
replace an unbounded graph-degree label by a finite cyclic operator
  -> retain a chosen finite divisor grid through a rank-certified tower
  -> make every modular alias explicit
  -> keep signed Möbius recombination before taking norms
~~~

It also has a precise limitation.  A tower of bounded maximum depth cannot
faithfully carry coefficient grids of unbounded dimension.  Growing the
tower restores algebraic capacity, but a literal point-function
realization pays the exponential dimensions in Section 4.

This conclusion does not settle the categorical closed-point route.
The point-function matrix rank \(Q^r-1\) is an external separation rank of
the numerical kernel.  A graph correspondence may encode the same action
without being presented as \(Q^r-1\) external tensor summands.  Therefore
this packet proves none of:

* a lower bound for constructible-sheaf rank;
* a lower bound for compactly supported Betti numbers;
* failure of a correspondence-level or Grothendieck-group compression;
* construction of the native owner/Boolean/Artin--Schreier source complex;
* commuting partial Frobenius for that native source;
* a uniform Adams-transformed conductor or Betti estimate;
* CYSEL, WCADD106140, WCKUM106140, principal individualization, RH, or GRH.

The next categorical question is now narrower: can the signed native
source be retained as a compact correspondence or Grothendieck class
without externalizing its pointwise kernel into \(Q^r-1\) rank-one
summands?  The finite-extension calculation neither supplies nor rules out
that escape.

## 6. Proof ledger

| statement | grade |
|---|---|
| cycle formula (1.1) | **PROVED EXACT** |
| total-count and centered-mass collapse | **PROVED EXACT** |
| trace formula and \(\gcd(n,r)\) blindness | **PROVED EXACT** |
| pointwise aliasing exactly modulo \(r\) | **PROVED EXACT** |
| centered rank, multiplication, algebra dimension, and minimal polynomials | **PROVED EXACT** |
| Möbius residue criterion (2.3) | **PROVED EXACT** |
| general cyclotomic rank rule and prime formula (2.5) | **PROVED EXACT** |
| finite-tower period and joint-algebra dimension | **PROVED EXACT** |
| residue-incidence fidelity criterion | **PROVED EXACT** |
| single-level and arbitrary-tower literal matrix lower bounds | **PROVED EXACT FOR FULL GRID FIDELITY** |
| survival of the complete native signed FFPS complex | **NOT TESTED** |
| sheaf-rank or Betti lower bound | **NOT CLAIMED** |
| categorical Adams compression of the native source | **NOT CONSTRUCTED** |
| analytic trace estimate, CYSEL, RH, or GRH | **NOT PROVED** |

## 7. Bounded replay

The replay constructs no finite field elements.  It builds an abstract
permutation with the exact Frobenius cycle inventory (1.1), which is
permutation-isomorphic to Frobenius on \(\mathbf F_{Q^r}\).  It uses only
\(Q=2\) and \(1\le r\le5\); the largest exact rational matrix is
\(32\)-by-\(32\).

It verifies:

* every formula in (1.2)--(1.6) on the bounded panel;
* exact Möbius actions and the prime rank formula;
* modular zero and nonzero examples invisible to scalar traces;
* joint algebra dimensions and residue-incidence ranks for the three
  finite towers above;
* the literal-matrix cost ledger through \(w=6\);
* frozen source blobs and the canonical JSON fixture.

Run:

~~~text
python -B research/l-families/atlas/function_field/ffps_frobenius_extension_tower_aliasing.py --check
python -m unittest tests.test_ffps_frobenius_extension_tower_aliasing
~~~
