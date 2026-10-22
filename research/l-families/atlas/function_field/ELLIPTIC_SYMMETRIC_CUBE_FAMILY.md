# The elliptic symmetric-cube family

## Status and purpose

This packet studies a genuinely different functorial family obtained from the
two-dimensional genus-one Frobenius representation by `Sym^3`.  It is a
bounded exact calculation, not a new field census.  Its finite rows are
deterministic transforms of the source-locked model/stack trace histograms in
`genus1_cubic_family_laws.json` for `q=3,5,7,11,13`.

The main point is structural.  A degree-four weight-three reciprocal factor
may have ambient compact type `USp(4)`, but symmetric cubes occupy only the
rank-one image `Sym^3(SU(2))`. That thin image is visible both as an exact
plane curve in coefficient space and in low compact moments. This gives a
necessary compact-image signature for symmetric-cube origin which does not
require looking at zeros; arithmetic recognition needs additional tests.

All computations use integers, rational numbers, or exact Laurent
coefficients.  There are no floats, random samples, new curves, interpolation,
or external databases.

## 1. Conventions and the sign bridge

The requested base local factor is

\[
 P_E(T)=1+AT+qT^2=(1-\alpha T)(1-\beta T),
 \qquad \alpha+\beta=-A,\quad \alpha\beta=q.                 \tag{1}
\]

The locked genus-one source instead writes

\[
 L_E(T)=1-tT+qT^2,
 \qquad t=q+1-\#E(\mathbb F_q).                              \tag{2}
\]

Thus the conversion is load-bearing:

\[
 \boxed{A=-t.}                                                \tag{3}
\]

Every transformed atom stores both `source_geometric_trace_t` and
`converted_polynomial_coefficient_A`.  This prevents the same aggregate
twist symmetry which makes a sign error invisible in an even histogram from
silently changing the local factor.

The source fixture is locked by schema, canonical payload hash, LF-normalized
file hash, measure description, and the two normalization strings in (2).
The consumed measure is uniform monic squarefree cubic models, equivalently
the normalized elliptic moduli-stack measure.  It is not uniform coarse
elliptic isomorphism classes.

## 2. The degree-four weight-three factor

The four symmetric-cube roots are

\[
 \alpha^3,\qquad \alpha^2\beta=q\alpha,\qquad
 \alpha\beta^2=q\beta,\qquad \beta^3.                        \tag{4}
\]

Their first elementary symmetric function is

\[
 \begin{aligned}
 e_1
  &=\alpha^3+\beta^3+q(\alpha+\beta)\\
  &=(\alpha+\beta)^3-2q(\alpha+\beta)\\
  &=-A^3+2qA.                                                  \tag{5}
 \end{aligned}
\]

For the second one, direct pairwise expansion gives

\[
 \begin{aligned}
 e_2
 &=q(\alpha^4+\beta^4)+q^2(\alpha^2+\beta^2)+2q^3\\
 &=q(A^4-3qA^2+2q^2).                                         \tag{6}
 \end{aligned}
\]

The roots pair with product `q^3`, so `e_3=q^3e_1` and `e_4=q^6`.
Consequently

\[
 \boxed{
 \begin{aligned}
 P_{\operatorname{Sym}^3E}(T)
 ={}&1+(A^3-2qA)T
     +q(A^4-3qA^2+2q^2)T^2\\
   &+q^3(A^3-2qA)T^3+q^6T^4.
 \end{aligned}}                                               \tag{7}
\]

### Independent Newton route

The producer does not trust (7) alone.  Put

\[
 p_n=\alpha^n+\beta^n,\qquad
 p_0=2,\quad p_1=-A,\quad p_n=-Ap_{n-1}-qp_{n-2}.              \tag{8}
\]

The `k`-th power sum of the four roots (4) is

\[
 R_k=p_{3k}+q^kp_k.                                            \tag{9}
\]

Newton's identities applied to `R_1,...,R_4` independently
reconstruct all five coefficients in (7).  The two routes are compared at
every one of the 55 source trace atoms.

## 3. Normalization and the coefficient curve

Normalize the base geometric trace by

\[
 t_0={t\over\sqrt q}=-{A\over\sqrt q},\qquad -2\le t_0\le2.  \tag{10}
\]

Writing `Z=q^(3/2)T`, equation (7) becomes

\[
 1-xZ+yZ^2-xZ^3+Z^4,                                          \tag{11}
\]

where

\[
 \boxed{x=t_0^3-2t_0},\qquad
 \boxed{y=t_0^4-3t_0^2+2}.                                   \tag{12}
\]

Here `x` is the normalized symmetric-cube trace and `y` the normalized
second elementary coefficient.  In `SU(2)` character notation,

\[
 x=\chi_3(t_0),\qquad y=1+\chi_4(t_0).                        \tag{13}
\]

Eliminating `t_0` from (12) gives

\[
 \boxed{F(x,y)=-x^4+x^2y+x^2+y^3-2y^2=0.}                    \tag{14}
\]

One short elimination uses `z=t_0^2`:

\[
 y=z^2-3z+2,\qquad x^2=z(z-2)^2,\qquad
 x^2=z(y-1)-y+2.                                               \tag{15}
\]

Substitution yields (14).  Away from the exceptional denominators, the
normalization parameter can be recovered rationally:

\[
 \boxed{t_0={x(y-1)\over x^2-y}.}                              \tag{16}
\]

Thus (14) is a rational coefficient curve, rather than merely an equation
which accidentally vanishes on the image.

For an exact finite-field check without adjoining `sqrt(q)`, let

\[
 S=t^3-2qt,\qquad D=t^4-3qt^2+2q^2.                           \tag{17}
\]

The raw coefficient of `T^2` is `qD`, while
`x=S/q^(3/2)` and `y=D/q^2`.  Clearing denominators in (14) gives the
integer identity

\[
 \boxed{-S^4+qS^2D+q^3S^2+D^3-2q^2D^2=0.}                    \tag{18}
\]

Every frozen source atom is checked against (18).

## 4. Nodes, branches, and the absence of cusps

The polynomial curve (14) has singular locus

\[
 (-1,1),\qquad (0,0),\qquad (1,1).                            \tag{19}
\]

For completeness, its two partial derivatives are

\[
 F_x=-2x(2x^2-y-1),\qquad F_y=x^2+3y^2-4y.                   \tag{19a}
\]

If `x=0`, imposing `F=F_y=0` leaves only `y=0`.  In the other
case put `r=x^2` and `y=2r-1`.  Then

\[
 F=(r-1)^2(8r-3),\qquad F_y=(r-1)(12r-7),                    \tag{19b}
\]

whose only common root is `r=1`.  This proves that the list (19) is
complete, rather than the output of a bounded singular-point search.

Their normalization preimages are respectively

\[
 t_0^2+t_0-1=0,\qquad t_0^2-2=0,\qquad t_0^2-t_0-1=0.         \tag{20}
\]

All six roots are real and lie in `[-2,2]`.  The compact coefficient path
therefore crosses itself at all three algebraic singularities.  With local
coordinates `(X,Y)`, the quadratic tangent cones are

\[
 \begin{array}{c|c}
 (-1,1)&-4X^2-2XY+Y^2\\
 (0,0)&X^2-2Y^2\\
 (1,1)&-4X^2+2XY+Y^2.
 \end{array}                                                   \tag{21}
\]

Each is nondegenerate and splits into two distinct real tangent lines.
Hence the three singularities are ordinary real nodes.

There are no cusps.  Indeed

\[
 {dx\over dt_0}=3t_0^2-2,\qquad
 {dy\over dt_0}=2t_0(2t_0^2-3),                               \tag{22}
\]

and the two derivatives have no common zero.  At `t_0^2=2/3`, where the
first derivative vanishes, the second is nonzero.

The projection to the `x`-axis branches at

\[
 x=\pm{4\sqrt6\over9},\qquad x^2={32\over27};                 \tag{23}
\]

the projection to the `y`-axis branches at `y=2` and `y=-1/4`.
The real compact arc begins at `(-4,6)`, ends at `(4,6)`, and passes through
the three nodes according to the parameter order in (12).

This geometry is a coefficient-map phenomenon.  It does not say that an
elliptic curve, a symmetric-cube motive, or a moduli space is singular.

### 4.1 The arithmetic restriction remains injective across the real folds

There is a sharper arithmetic fact which is invisible in the real picture.
Let

\[
 S_q(t)=t^3-2qt                                                   \tag{24a}
\]

be the integral symmetric-cube trace.  For two integers `t_1,t_2`,

\[
 S_q(t_1)-S_q(t_2)
 =(t_1-t_2)(t_1^2+t_1t_2+t_2^2-2q).                             \tag{24b}
\]

The quadratic norm `r^2+rs+s^2` takes only the residue classes
`0,1,3 mod 4`; it is never `2 mod 4`.  If `q` is odd, however,
`2q=2 mod 4`.  Therefore the second factor in (24b) cannot vanish, and

\[
 \boxed{q\text{ odd}\quad\Longrightarrow\quad
        S_q:\mathbb Z\longrightarrow\mathbb Z\text{ is injective}.}     \tag{24c}
\]

No Hasse bound is needed.  In particular, the symmetric-cube trace by itself
recovers the base integral Frobenius trace, even though the normalized real
map `t_0 -> t_0^3-2t_0` is not injective on `[-2,2]`. No real trace fiber
contains two arithmetic Frobenius-lattice points, so the folds create no
collision between integral traces. The lattice can still meet such a real
fiber on one branch: `t=0`, for example, shares its trace value with the
nonarithmetic parameters `t_0=+-sqrt(2)`.

Oddness is essential: for `q=2`, the traces `t=0` and `t=2` both give
`S_q(t)=0`.  Thus this is an arithmetic parity lemma, not a general property
of the symmetric-cube character.

## 5. Why the curve detects a thin compact image

On a maximal torus of `SU(2)`, the standard eigenvalues are `z,z^-1`.
The symmetric cube has eigenvalues

\[
 z^3,z,z^{-1},z^{-3}.                                         \tag{24}
\]

Because the highest weight is odd, this irreducible four-dimensional
representation is symplectic, and `Sym^3(SU(2))` lies in `USp(4)`.  It is a
faithful rank-one image: the central element `-I` maps to `-I`, not to the
identity.

By contrast, a generic `USp(4)` torus has two independent parameters and
eigenvalues

\[
 z_1,z_1^{-1},z_2,z_2^{-1}.                                   \tag{25}
\]

It is not constrained by (14).  For example the valid `USp(4)` torus point
with eigenvalues `1,1,-1,-1` has `(x,y)=(0,-2)`, and

\[
 F(0,-2)=-16.                                                  \tag{26}
\]

Thus failure of (14) is a pointwise obstruction to `Sym^3` origin. Since its
zero locus is Haar-null in the rank-two generic `USp(4)` coefficient region,
the compact-image distinction is stronger than a small bias in one moment.

## 6. Exact compact moment fingerprints

Two independent methods evaluate moments on the thin image:

1. the `SU(2)` Weyl constant term with positive root `2e`;
2. triangular decomposition in the characters
   `chi_n=U_n(t_0/2)`.

For generic `USp(4)`, the producer uses the rank-two Weyl constant term with
positive `C_2` roots

\[
 2e_1,\quad2e_2,\quad e_1-e_2,\quad e_1+e_2.                  \tag{27}
\]

The exact trace moments are:

| degree | 0 | 2 | 4 | 6 | 8 | 10 | 12 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| `Sym^3(SU2)` | 1 | 1 | 4 | 34 | 364 | 4269 | 52844 |
| generic `USp4` | 1 | 1 | 3 | 14 | 84 | 594 | 4719 |

All odd trace moments vanish in both rows.  The first separation is already

\[
 \boxed{\mathbb E_{\operatorname{Sym}^3(SU2)}x^4=4,\qquad
        \mathbb E_{USp4}x^4=3.}                               \tag{28}
\]

For the second coefficient:

| degree | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| `Sym^3(SU2)` | 1 | 1 | 2 | 5 | 16 | 62 | 272 |
| generic `USp4` | 1 | 1 | 2 | 4 | 10 | 27 | 82 |

The first two moments agree; the third separates the images.  A mixed
separation occurs at the same small scale:

\[
 \boxed{\mathbb E_{\operatorname{Sym}^3(SU2)}x^2y^2=7,\qquad
        \mathbb E_{USp4}x^2y^2=5.}                            \tag{29}
\]

The fixture retains further mixed rows, because different arithmetic
families may approach their limiting compact laws at noticeably different
rates even when (28) already separates the two declared comparator laws.

## 7. Exact finite-family laws for every odd `q`

The source genus-one packet proves, with its stated level-one
Eichler--Shimura input, that under the uniform-model/normalized-stack measure

\[
 \mathbb E\,\chi_0(t_0)=1,                                    \tag{30a}
\]

and, for every `j>=1`,

\[
 \mathbb E\,\chi_{2j}(t_0)
 =-{1+\Theta_{2j+2}(q)\over q^{j+1}},                         \tag{30b}
\]

while every odd character has mean zero.  Through character index `12`, only
`chi_10` sees a cuspidal correction: `Theta_12(q)`.  The weight-14 cusp space
attached to `chi_12` is zero.

The needed decompositions are

\[
\begin{aligned}
 x^2={}&\chi_0+\chi_2+\chi_4+\chi_6,\\
 y={}&\chi_0+\chi_4,\\
 y^2={}&2\chi_0+\chi_2+3\chi_4+\chi_6+\chi_8,\\
 x^2y={}&2\chi_0+4\chi_2+5\chi_4+4\chi_6+2\chi_8+\chi_{10},\\
 x^4={}&4\chi_0+9\chi_2+11\chi_4+10\chi_6+6\chi_8
          +3\chi_{10}+\chi_{12},\\
 y^3={}&5\chi_0+6\chi_2+11\chi_4+7\chi_6+6\chi_8
          +2\chi_{10}+\chi_{12}.
                                                               \tag{31}
\end{aligned}
\]

Substitution in (30a)--(30b) gives the exact all-odd-`q` laws

\[
\begin{aligned}
 \mathbb E[x]&=0,\\
 \mathbb E[y]&=1-q^{-3},\\
 \mathbb E[x^2]&=1-q^{-2}-q^{-3}-q^{-4},\\
 \mathbb E[y^2]&=2-q^{-2}-3q^{-3}-q^{-4}-q^{-5},\\
 \mathbb E[x^2y]&=2-4q^{-2}-5q^{-3}-4q^{-4}-2q^{-5}
                    -q^{-6}-\Theta_{12}(q)q^{-6},\\
 \mathbb E[x^4]&=4-9q^{-2}-11q^{-3}-10q^{-4}-6q^{-5}
                  -3q^{-6}-q^{-7}-3\Theta_{12}(q)q^{-6},\\
 \mathbb E[y^3]&=5-6q^{-2}-11q^{-3}-7q^{-4}-6q^{-5}
                  -2q^{-6}-q^{-7}-2\Theta_{12}(q)q^{-6}.
                                                               \tag{32}
\end{aligned}
\]

There are again two independent derivations in the producer.  One expands
each observable into the locked base trace moments through degree `12`; the
other uses (31) and (30a)--(30b).  For the five frozen fields, a third route directly
transforms the source trace histogram.  All three agree exactly.

Several features are worth retaining for later work:

- the mean second coefficient differs from its compact value `1` first at
  order `q^-3`, with no `q^-1` or `q^-2` term;
- the trace variance sees the full nontrivial ladder
  `chi_2+chi_4+chi_6`, hence corrections at `q^-2,q^-3,q^-4`;
- the first modular-form correction in these selected observables appears in
  `E[x^2y]`, `E[x^4]`, and `E[y^3]`, with multiplicities `1,3,2` inherited
  from `chi_10` in (31);
- their leading constants are exactly the thin compact moments `2,4,5`, not
  the generic `USp(4)` values.

This is a clean example of a family retaining its functorial compact image in
the leading term while arithmetic cohomology enters only in lower-order
corrections.

## 8. Frozen transforms, not a new census

For each of `q=3,5,7,11,13`, the producer reads the locked source histogram
of `t`, converts `A=-t`, and stores:

- the symmetric-cube trace `S=t^3-2qt`;
- all five integral polynomial coefficients from (7);
- the reduced second coefficient `D` from (17);
- the exact rational values `x^2=S^2/q^3` and `y=D/q^2`;
- transformed trace and `(T^1,T^2)` factor histograms;
- the seven finite-family averages in (32).

There are 55 source histogram atoms representing 3,650 upstream family
members.  This packet performs zero curve or field enumeration.  On these
five frozen supports both the symmetric-cube trace map and the full factor
map are injective.  Unlike a mere finite observation, trace injectivity is an
exact all-odd-`q` theorem by (24c). The real parameter curve still has the
three double points in (19); the integral restriction simply never places two
arithmetic traces in the same real trace fiber.

The producer refuses fields absent from the source lock and stops above a
100-atom cap.  The Weyl calculation has a separate exact Laurent
product-pair cap.  Actual counts and peak Laurent support are recorded in the
fixture.

## 9. Literature and priority boundary

The symmetric-cube lift is classical and is not a novelty claim of this
packet.  Two primary references fix that boundary:

- Henry H. Kim and Freydoon Shahidi,
  [*Symmetric cube L-functions for GL_2 are entire*](https://arxiv.org/abs/math/9909198),
  proves the holomorphy result for third symmetric-power `L`-functions of
  nonmonomial `GL_2` cusp forms over arbitrary number fields.
- Henry H. Kim and Freydoon Shahidi, with an appendix by Colin J. Bushnell and
  Guy Henniart,
  [*Functorial products for GL_2 x GL_3 and the symmetric cube for GL_2*](https://arxiv.org/abs/math/0409607),
  proves the functorial symmetric-cube map for `GL_2` cusp forms.

Accordingly, this packet claims no originality for the `Sym^3`
representation, the root transform (4), the reciprocal factor (7), or the
global automorphic lift.  The project-specific work is narrower:

- the exact pushforward of the already locked genus-one model/stack family;
- elimination and normalization of its coefficient image, including the
  three-node real geometry;
- the odd-`q` integral-trace injectivity lemma and resulting absence of
  arithmetic collisions across the real folds;
- exact finite-`q` coefficient and mixed-moment defects through source base
  degree `12`, with the first `Theta_12` multiplicities exposed.

Even those items are only project-specific calculations, not certified
literature firsts.  A dedicated priority search would be required before
calling any of them novel.

## 10. What is exact, what is imported, and what remains doubtful

Exact within this packet:

- both derivations of the reciprocal polynomial (7);
- the normalization (11)--(13), implicit curve (14), rational inverse (16),
  singular locus, node classification, and branch values;
- the all-odd-`q` integral trace-injectivity lemma (24c);
- the integer cleared identity (18) on every source atom;
- the `SU(2)` and `USp(4)` Haar constant terms and the independent `SU(2)`
  character audit;
- the transformations of the locked histograms and their agreement with the
  formulas (32).

Imported, with an explicit dependency:

- the genus-one stack character theorem (30a)--(30b), including the definition of
  `Theta_12(q)`;
- the five tiny source trace histograms and their measure interpretation.

Not established here:

- a new automorphy theorem for global symmetric-cube `L`-functions;
- a global recognition or descent theorem for an arbitrary degree-four local
  factor merely because its coefficients satisfy (14);
- realization of every such arbitrary factor as the `H^i` of a new smooth
  projective variety;
- equidistribution of any number-field family;
- a zero-free region, RH, or GRH;
- a literature-priority claim for the coefficient equation or moment
  packaging.

The representation theory behind `Sym^3(SU(2))` is classical.  The explicit
coefficient curve, its nodal normalization, and the three-route finite-`q`
moment synthesis are candidate-useful propositions for this atlas, but they
must undergo a literature search before anyone calls them novel.

For an actual elliptic curve, `Sym^3 H^1_et(E)` is a genuine l-adic
representation; it is not merely a formal polynomial.  The firewall concerns
the converse direction: equation (14) alone cannot recognize a compatible
global system or prove descent for arbitrary supplied local factors.  The
classical automorphic lift cited above is neither reproved nor needed for the
finite-field calculations in this packet.

One conceptual doubt deserves emphasis. A local factor satisfying (14) is not
ruled out at the compact representation-image level, but the equation is not
sufficient even for local arithmetic symmetric-cube origin. The point
`(x,y)=(0,0)` lies on (14), with normalization preimages
`t_0=+-sqrt(2)`. Over odd `F_q`, an elliptic source would therefore need an
integer trace `t` with `t^2=2q`, impossible because `v_2(2q)=1`. Thus the node
is an explicit arithmetic false positive. A fortiori, the equation alone is
not a global descent theorem: unrelated local systems could land on the same
coefficient curve, and isolated primes could satisfy it accidentally. A
genuine global recognition theorem would require the integral trace lattice,
compatible behavior across primes, ramification, determinant, and monodromy
data. The packet provides a sharp compact obstruction and exact family
statistics, not that recognition theorem.

## 11. Replay contract

From the repository root, run

```text
python research/l-families/atlas/function_field/elliptic_symmetric_cube_family.py --check
python -O research/l-families/atlas/function_field/elliptic_symmetric_cube_family.py --check
python -m unittest tests.test_elliptic_symmetric_cube_family
python -O -m unittest tests.test_elliptic_symmetric_cube_family
```

An explicit path remains accepted, for example
`--check research/l-families/atlas/function_field/elliptic_symmetric_cube_family.json`;
bare `--check` and `--write` use the adjacent default fixture.

The JSON also locks the producer, this note, and the test file.  A deliberate
change requires regenerating the fixture with `--write`; an upstream source
change first requires an explicit audit and source-lock update.
