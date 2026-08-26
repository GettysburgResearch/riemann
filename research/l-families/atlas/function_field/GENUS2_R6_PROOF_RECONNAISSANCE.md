# Genus-two `R6` proof reconnaissance

**Status:** exact pointwise reduction and exact low-moment no-go.  No formula
for the squarefree-family mean of `R6` is claimed.

**Scope:** every normalized `USp(4)` conjugacy class for the pointwise and
Haar statements; every real `q>=19` for the probability-law no-go, hence in
particular every odd prime power in that range.  No finite field or family
member is enumerated, and none of the frozen `q=3,5,7` values of `mean(R6)`
is consumed.

**Exact sources or dependencies:** the `C2` character normalization and
`R6` decomposition in `BALANCED_CONTROL_FAMILY_SCAN.md`; the proved five
all-`q` low character means recorded in
`GENUS2_DETECTOR_BOUNDARY_QUOTIENT.md`; and the exact capped character engine
`usp_coefficient_minor_rank_scan.py`.  The JSON artifact hashes these and the
other requested reconnaissance inputs.

**What was actually run:** exact Laurent-polynomial reconstruction, exact
Weyl constant terms, integer dimensions, and rational inequalities.  No
primitive family source record is read.  Under the conservative accounting
that counts every bounding-box character-weight candidate as a source atom,
the replay uses 1,035 atoms, below the hard cap 4,096.

**Smallest remaining gap:** evaluate either `mean(R6)` directly in the
squarefree quintic family or, after independently evaluating
`mean(chi_(0,3))`, evaluate the single rank-two combination
`3 mean(B_1 B_2)+2 mean(B_3)`.  Evaluating its two terms separately is one
possible route, not a logical requirement.  The no-go below proves that the
five existing all-`q` low means cannot supply this missing arithmetic.

## 1. A rank-two echo reduction

For a normalized conjugacy class with eigenvalues

\[
 \{x,x^{-1},y,y^{-1}\},
\]

put

\[
 X_r(z)=z^{2r}+z^{-2r},
 \qquad B_r=-X_r(x)X_r(y).
\]

Thus `B_1` is the balanced control `B`.  The elementary Chebyshev product

\[
 X_1(z)X_2(z)=X_3(z)+X_1(z)
\tag{1}
\]

gives

\[
 B_1B_2=(X_3(x)+X_1(x))(X_3(y)+X_1(y)).
\tag{2}
\]

It also gives the already implicit echo identity

\[
 B_1^3=6B_1-3B_1B_2-2B_3.
\tag{3}
\]

Indeed, `X_1^3=X_3+3X_1`; expanding in the two torus coordinates and using
(1) proves (3) directly.  Combining (3) with the exact pointwise identity

\[
 R_6=B_1^3-6B_1+2\chi_{0,3}
\]

yields

\[
 \boxed{R_6-2\chi_{0,3}=-3B_1B_2-2B_3.}
\tag{4}
\]

The replay independently reconstructs the two character decompositions

\[
 B_3=\chi_{0,3}-\chi_{2,3}+\chi_{2,4}-\chi_{0,6},
\tag{5}
\]

\[
 B_1B_2=-\chi_{6,0}+\chi_{4,2}-\chi_{2,4}+\chi_{0,6},
\tag{6}
\]

so (4) reproduces every coefficient in

\[
 R_6=2\chi_{2,3}+3\chi_{6,0}-3\chi_{4,2}
     +\chi_{2,4}-\chi_{0,6}.
\]

Consequently the mean target has the exact alternative form

\[
 \boxed{
 \langle R_6\rangle_q
 =2\langle\chi_{0,3}\rangle_q
 -3\langle B_1B_2\rangle_q-2\langle B_3\rangle_q.}
\tag{7}
\]

This is a genuine source-burden reduction at the torus level.  Direct `R6`
has 37 Laurent support atoms.  After the separately isolated
`2 chi_(0,3)` channel is removed, the residual has exactly 16 atoms and uses
only frequencies one and three.

The reduction is also sharp among separated products in these coordinates.
In the ordered basis `(X_1,X_3)` on each torus coordinate, the coefficient
matrix of `R6-2 chi_(0,3)` is

\[
 \begin{pmatrix}-3&-3\\-3&-1\end{pmatrix},
 \qquad \det=-6.
\tag{8}
\]

It therefore has tensor rank exactly two over `Q` (and over `R`).  In
particular it cannot be replaced by one separated product of an `x`-trace
and a `y`-trace.  Equations (4) and (7) attain the minimal two-product rank.
This does not prove that the two family averages are easy; it identifies the
minimal separated-product rank exposed by the echo coordinates; it does not
exclude a different arithmetic reduction of the combined average.

## 2. Orthogonality no-go for the proved low moments

Let

\[
 \mathcal L_{\mathrm{low}}=
 \operatorname{span}\{1,\chi_{0,1},\chi_{2,0},\chi_{0,2},
                         \chi_{2,1},\chi_{4,0}\}.
\]

The five nonconstant characters here are exactly the channels whose means
are proved for every odd prime power by the existing moment packet.  The
five constituents of `R6` are distinct from them and from `chi_(0,3)`.
Exact Weyl constant terms give the diagonal Gram matrix

\[
 \operatorname{diag}(1,1,1,1,1,1,1,24)
\tag{9}
\]

in the ordered basis

\[
 (1,\chi_{0,1},\chi_{2,0},\chi_{0,2},\chi_{2,1},\chi_{4,0},
   \chi_{0,3},R_6).
\]

Thus `R6` is orthogonal to the entire proved low space (and also to
`chi_(0,3)`), while

\[
 \|R_6\|_{\mathrm{Haar}}^2=2^2+3^2+(-3)^2+1^2+(-1)^2=24.
\tag{10}
\]

In particular there is no pointwise linear identity expressing `R6` through
the known low characters.  The following construction makes the stronger
mean-level underdetermination explicit while matching the actual proved
low means.

Write those means as `m_lambda(q)`.  Their character dimensions, in the same
order, are

\[
 5,\ 10,\ 14,\ 35,\ 35.
\]

For `q>=3`, their signs are fixed, and direct substitution of the proved
formulas gives

\[
 S(q):=\sum_\lambda \dim(\lambda)|m_\lambda(q)|
 ={19\over q}-{5\over q^2}+{80\over q^3}
  -{40\over q^4}+{49\over q^5}.
\tag{11}
\]

Set `delta(q)=1-S(q)`.  Its numerator is positive for every real `q>=19`,
because with `t=q-19>=0`,

\[
\begin{aligned}
 q^5\delta(q)
 &=q^5-19q^4+5q^3-80q^2+40q-49\\
 &=t^5+76t^4+2171t^3+27641t^2+132736t+6126>0.
\end{aligned}
\tag{12}
\]

For a unitary representation character, `|chi_lambda(U)|<=dim(lambda)`.
The same triangle inequality gives the explicit bound

\[
 |R_6(U)|\le
 2(154)+3(84)+3(220)+260+140=1620.
\tag{13}
\]

Define two central densities relative to Haar measure by

\[
 f_{q,\pm}(U)=1+\sum_\lambda m_\lambda(q)\chi_\lambda(U)
 \mathbin{\pm}{\delta(q)\over2\cdot1620}R_6(U).
\tag{14}
\]

Equations (11)--(13) imply

\[
 f_{q,\pm}(U)\ge1-S(q)-{\delta(q)\over2}
 ={\delta(q)\over2}>0.
\]

Every nontrivial character has Haar mean zero, so both densities have total
mass one.  Orthogonality (9) then gives, exactly,

\[
 \int\chi_\lambda f_{q,+}\,dU
 =\int\chi_\lambda f_{q,-}\,dU=m_\lambda(q)
\tag{15}
\]

for all five proved low channels, whereas

\[
 \boxed{
 \int R_6 f_{q,\pm}\,dU
 =\mathbin{\pm}{\delta(q)\over135}.}
\tag{16}
\]

At `q=19`, for example,

\[
 \delta(19)={6126\over2476099},\qquad
 {\delta(19)\over135}={2042\over111424455}.
\]

Therefore the exact five all-`q` low means, character algebra, and positivity
of a compact-group probability law do **not** determine `mean(R6)`.  Any
proof of the squarefree-family value must use new arithmetic information;
it cannot be a formal consequence of the locked low moments.

## 3. Boundary and replay

The probability laws in Section 2 are comparison laws on the compact group,
not assertions that they arise from squarefree quintics.  Their role is an
exact logical no-go: they rule out determination from the stated moment data
alone.  They do not rule out a direct arithmetic evaluation of (7).

The three frozen `mean(R6)` values are neither read nor fitted.  No additional
field, extension tower, family member, database, random sample, floating-point
number, or asymptotic inference occurs.  Run:

```text
python -B research/l-families/atlas/function_field/genus2_r6_proof_reconnaissance.py --check
python -B -O research/l-families/atlas/function_field/genus2_r6_proof_reconnaissance.py --check
python -B -m unittest tests.test_genus2_r6_proof_reconnaissance
python -B -O -m unittest tests.test_genus2_r6_proof_reconnaissance
```
