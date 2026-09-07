# The elliptic-pair Rankin--Selberg / tensor SO(4) family

Status: **DRAFT exact local algebra, exact all-odd-prime-power low moments,
and source-locked finite pushforwards**

Scope: ordered pairs of independent marked genus-one cubic models over the
same odd finite field, the degree-four tensor local factor, its compact
coefficient image, its discriminant walls, and exact low moments.

Exact sources or dependencies: the only finite input is the complete trace
histogram in `genus1_cubic_family_laws.json` at `q=3,5,7,11,13`.  The all-`q`
formulas use only that packet's exact laws `W_2=q^2-1`,
`W_4=2q^3-3q-1`, and its marked-model/stack normalization.  Classical
global `GL(2) x GL(2)` theory is cited only as a literature boundary.

What was actually run: 645 ordered Cartesian products of the 55 locked
histogram atoms, two exact derivations of every resulting local factor, exact
rational coefficient transforms, and symbolic rational moment checks.  No
finite field or curve was constructed; the represented model-pair masses are
compressed histogram weights rather than individual loop iterations.

Smallest remaining gap: use geometrically linked, rather than independent,
elliptic pairs and decide which deviations from the product law detect an
isogeny, shared cover, global twist, or other correspondence.

## 1. Inputs, sign bridge, and measure

Write the two requested quadratic factors as

\[
 P_A(T)=1+AT+qT^2=(1-\alpha T)(1-\beta T),\qquad
 P_B(T)=1+BT+qT^2=(1-\gamma T)(1-\delta T),                 \tag{1}
\]

so that

\[
 \alpha+\beta=-A,\quad \gamma+\delta=-B,\quad
 \alpha\beta=\gamma\delta=q.                               \tag{2}
\]

The locked marked-cubic source instead uses

\[
 L_E(T)=1-tT+qT^2,\qquad t=q+1-\#E(\mathbb F_q).            \tag{3}
\]

The conversion is therefore

\[
 \boxed{A=-t_1,\qquad B=-t_2.}                              \tag{4}
\]

The finite law is the ordered product of two independent uniform
marked-model measures.  For trace observables, each marginal is equivalently
the normalized elliptic-stack measure.  It is not the uniform measure on
coarse elliptic isomorphism classes, and no coarse-pair interpretation is
inserted.

## 2. Exact degree-four tensor factor

The tensor eigenvalues are

\[
 \alpha\gamma,\quad \alpha\delta,\quad
 \beta\gamma,\quad \beta\delta.                            \tag{5}
\]

Their sum is `AB`.  Their second elementary symmetric function is

\[
 q\bigl(A^2+B^2-2q\bigr),                                   \tag{6}
\]

and reciprocal pairing gives the last two coefficients.  Hence

\[
 \boxed{
 P_{A\otimes B}(T)=
 1-ABT+q(A^2+B^2-2q)T^2-q^2ABT^3+q^4T^4.}                  \tag{7}
\]

The producer checks (7) by a second route.  If

\[
 p_n(A)=\alpha^n+\beta^n,\qquad
 p_0=2,\quad p_1=-A,\quad p_n=-Ap_{n-1}-qp_{n-2},           \tag{8}
\]

then the tensor power sum is

\[
 R_n=p_n(A)p_n(B).                                           \tag{9}
\]

Newton's identities applied to `R_1,...,R_4` reconstruct (7).  The closed
and Newton routes agree at every one of the 645 frozen atom pairs.  In
particular, the reciprocal constraints

\[
 c_3=q^2c_1,\qquad c_4=q^4                                 \tag{10}
\]

hold pointwise, not just after averaging.

## 3. The compact SO(4) coefficient image

Normalize

\[
 u={A\over\sqrt q},\qquad v={B\over\sqrt q},\qquad Z=qT.   \tag{11}
\]

Equation (7) becomes

\[
 P_{A\otimes B}(Z/q)=1-xZ+yZ^2-xZ^3+Z^4,                   \tag{12}
\]

with

\[
 \boxed{x=uv={AB\over q},\qquad
 y=u^2+v^2-2={A^2+B^2-2q\over q}.}                          \tag{13}
\]

At the representation level, the standard two-dimensional representations
of the two `SU(2)` factors have a four-dimensional orthogonal tensor product.
Its kernel is the diagonal center, giving

\[
 {SU(2)\times SU(2)\over\{(1,1),(-1,-1)\}}\simeq SO(4).    \tag{14}
\]

This is a rank-two compact image, unlike the rank-one symmetric-power slices.
It does not by itself prove that an arithmetic family has full `SO(4)`
monodromy.

Put `p=u^2` and `r=v^2`.  The Hasse bounds give `p,r in [0,4]`, and

\[
 x^2=pr,\qquad y=p+r-2.                                     \tag{15}
\]

Therefore

\[
 \boxed{D=(y+2)^2-4x^2=(p-r)^2\ge0.}                        \tag{16}
\]

Here `D` is specifically the discriminant of the reconstruction equation

\[
 \lambda^2-(y+2)\lambda+x^2=0,                              \tag{16a}
\]

whose unordered roots are `p,r`.  Thus `D=0` is the fold of the coefficient
map that forgets the ordering of the two squared base traces.  It is also one
factor of the reciprocal quartic's root discriminant, but it is **not** that
full discriminant; Section 4 exhibits the missing Hasse-endpoint factor.

Conversely, a real point `(x,y)` belongs to the compact coefficient image
exactly when `D>=0` and

\[
 p={y+2+\sqrt D\over2},\qquad
 r={y+2-\sqrt D\over2}                                      \tag{17}
\]

both lie in `[0,4]`.  Choose real `u,v` with squares `p,r` and signs whose
product is `x`.  This proves sufficiency; the inequalities are not merely a
necessary numerical screen.

Every frozen arithmetic atom carries an exact rational forward certificate

\[
 p={A^2\over q},\quad r={B^2\over q},\quad
 D={(A^2-B^2)^2\over q^2},                                  \tag{18}
\]

so no square roots or floating point enter the replay.

## 4. Fold walls and the full reciprocal-quartic discriminant

The coefficient-map fold `D=0` occurs exactly when `A^2=B^2`.  Its two sign
branches have different repeated factors.

If `A=B`, then the second quadratic factor has the same two roots as the
first, and

\[
 \boxed{P_{A\otimes A}(T)=
 (1-qT)^2\bigl(1-(A^2-2q)T+q^2T^2\bigr).}                  \tag{19}
\]

If `B=-A`, its roots are the negatives of the first pair, and

\[
 \boxed{P_{A\otimes(-A)}(T)=
 (1+qT)^2\bigl(1+(A^2-2q)T+q^2T^2\bigr).}                  \tag{20}
\]

These are local polynomial identities.  Equality or opposition of two
traces at one finite field does **not** prove that the curves are isomorphic,
quadratic twists, isogenous, linked by a correspondence, or associated with
the same global automorphic representation.  The frozen fold-wall masses record
local coincidences only.

### 4.1 The additional Hasse-endpoint component

For the full root discriminant, write the normalized reciprocal quartic as

\[
 Q(Z)=Z^4-xZ^3+yZ^2-xZ+1
     =(Z^2-sZ+1)(Z^2-tZ+1),                                \tag{20a}
\]

where `s+t=x` and `st=y-2`.  The product formula for polynomial
discriminants gives

\[
 \operatorname{Disc}_Z(Q)
 =(s^2-4)(t^2-4)(s-t)^4.                                   \tag{20b}
\]

Both factors eliminate exactly:

\[
\begin{aligned}
 D&=(y+2)^2-4x^2
    =(s^2-4)(t^2-4)=(p-r)^2,\\
 E&=x^2-4(y-2)
    =(s-t)^2=(p-4)(r-4).
\end{aligned}                                               \tag{20c}
\]

Consequently the exhaustive normalized quartic root discriminant is

\[
 \boxed{\operatorname{Disc}_Z(Q)
 =D\,E^2
 =(p-r)^2(p-4)^2(r-4)^2.}                                  \tag{20d}
\]

The fold component `D=0` is the union `A=B` or `A=-B` recorded in
(19)--(20).  The additional component `E=0` is the Hasse-endpoint union
`p=4` or `r=4`, equivalently `A^2=4q` or `B^2=4q`.  At `D=E=0` one has
`p=r=4` and the multiplicity increases.

The producer certifies (20c)--(20d) symbolically in two independent
coordinate systems, `(s,t)` and `(p,r)`: all six bivariate residual
polynomials are identically zero.  It separately constructs the `7 x 7`
Sylvester matrix of `Q,Q'` and checks its exact rational resultant against
`D E^2` on every one of the 645 frozen atom pairs.  Thus the normalization
and exponent on `E` are not inferred from a fitted factorization.

None of the five frozen `q` values reaches the endpoint component, because
they are nonsquare primes and an integral trace cannot satisfy `A^2=4q`.
That makes the frozen endpoint mass zero; it does not remove `E=0` from the
all-prime-power theorem.

## 5. Compact Haar trace moments

Under Haar measure on `Spin(4)=SU(2)xSU(2)`, the normalized tensor trace is
the product `uv` of two independent standard `SU(2)` traces.  Since

\[
 \mathbb E_{SU(2)}[u^{2n}]=C_n,\qquad
 \mathbb E_{SU(2)}[u^{2n+1}]=0,                            \tag{21}
\]

we have

\[
 \boxed{\mathbb E_{SO(4)}[x^{2n}]=C_n^2,\qquad
 \mathbb E_{SO(4)}[x^{2n+1}]=0.}                           \tag{22}
\]

Through order 12 this is

```text
[1, 0, 1, 0, 4, 0, 25, 0, 196, 0, 1764, 0, 17424].
```

This is a compact representation baseline.  It is not an equidistribution
claim about five finite fields or a number-field family.

### 5.1 A useful three-way compact discriminator

The first seven standard-trace moments for three degree-four compact images
are

| image | moments in orders `0,...,6` |
|---|---|
| `SO(4)` standard | `[1,0,1,0,4,0,25]` |
| `Sym^3(SU(2))` | `[1,0,1,0,4,0,34]` |
| generic `USp(4)` standard | `[1,0,1,0,3,0,14]` |

Thus `SO(4)` and `Sym^3(SU(2))` alias through trace-moment order 4 and
first separate at order 6.  Generic `USp(4)` separates from both already at
order 4.

The producer does not import the existing symmetric-cube fixture for this
comparison.  It independently obtains the symmetric-cube sequence by the
`SU(2)` Clebsch--Gordan recursion for the multiplicity of `V_0` in
`V_3^(tensor n)`.  For generic `USp(4)`, the three symplectic pair
contractions survive in degree 4, while the 15 degree-six contractions have
the unique rank-four Pfaffian relation, leaving 14.  These exact derivations
are tiny and contain no sampling.

Coefficient support supplies a second discriminator.  The `SO(4)` image
fills the two-dimensional semialgebraic region (16)--(17), while the
symmetric-cube image lies on the one-dimensional nodal curve

\[
 -x^4+x^2y+x^2+y^3-2y^2=0,                               \tag{22a}
\]

as follows independently from `x=t^3-2t`, `y=t^4-3t^2+2`.  The curve lies
inside the same reciprocal degree-four compact coefficient region, but its
Haar pushforward differs.  This is compact-image discrimination, not a claim
that any finite family has converged to one of these laws or that its actual
monodromy has been proved.

Indeed, with `z=t^2`, one has

\[
 x^2=z(z-2)^2,\qquad y=z^2-3z+2.                            \tag{22b}
\]

Direct substitution into (22a) gives zero identically, while the `SO(4)`
region discriminant restricts to

\[
 (y+2)^2-4x^2=(z-1)^2(z-4)^2\ge0\quad(0\le z\le4).          \tag{22c}
\]

Thus both the curve containment and the dimension contrast are exact, rather
than inferred from the displayed moments.

## 6. Exact all-odd-prime-power low moments

Let `u=t/sqrt(q)` for one locked marked-cubic draw.  From
`W_2=q^2-1`, `W_4=2q^3-3q-1`, and
`E_model[t^(2n)]=W_(2n)/q`, one obtains, for every odd prime power `q`,

\[
 m_2=\mathbb E[u^2]=1-q^{-2},\qquad
 m_4=\mathbb E[u^4]=2-3q^{-2}-q^{-3}.                       \tag{23}
\]

Take independent copies `u,v`, and use `x=uv`, `y=u^2+v^2-2`.  Direct
expansion gives

\[
\begin{aligned}
 \mathbb E[x^2]
   &=(1-q^{-2})^2,\\
 \mathbb E[x^4]
   &=(2-3q^{-2}-q^{-3})^2,\\
 \mathbb E[y]
   &=-2q^{-2},\\
 \mathbb E[y^2]
   &=2-2q^{-2}-2q^{-3}+2q^{-4},\\
 \mathbb E[x^2y]
   &=2-6q^{-2}-2q^{-3}+4q^{-4}+2q^{-5},\\
 \mathbb E[D]
   &=2-2q^{-2}-2q^{-3}-2q^{-4}.
\end{aligned}                                               \tag{24}
\]

Here `D=(u^2-v^2)^2`.  The producer checks (24) in two symbolic routes:
first as expressions in `m_2,m_4`, and then as separately expanded rational
functions of `q`.  It also checks each formula against all five complete
Cartesian histogram laws.  No polynomial was fitted to those rows.

## 7. Frozen finite pushforwards and resource boundary

The locked source has the following compressed sizes.

| `q` | source trace atoms | marked models | ordered atom pairs | represented ordered model pairs |
|---:|---:|---:|---:|---:|
| 3 | 7 | 18 | 49 | 324 |
| 5 | 9 | 100 | 81 | 10,000 |
| 7 | 11 | 294 | 121 | 86,436 |
| 11 | 13 | 1,210 | 169 | 1,464,100 |
| 13 | 15 | 2,028 | 225 | 4,112,784 |

The corresponding compressed coefficient supports and coefficient-map fold
masses are

| `q` | `(x,y)` support | `A=B` mass | `A=-B` mass | intersection | wall union |
|---:|---:|---:|---:|---:|---:|
| 3 | 16 | 54 | 54 | 16 | 92 |
| 5 | 25 | 1,300 | 1,300 | 400 | 2,200 |
| 7 | 36 | 9,408 | 9,408 | 1,764 | 17,052 |
| 11 | 49 | 139,150 | 139,150 | 48,400 | 229,900 |
| 13 | 64 | 346,788 | 346,788 | 24,336 | 669,240 |

The equality of the two signed fold-wall masses here is a consequence of the
locked twist-symmetric marginal trace histograms.  It is a statement about
this measure, not an assertion that the two wall loci are geometrically the
same.

For clarity, the separately typed exhaustive repeated-root table is

| `q` | fold `D=0` | endpoint `E=0` | intersection | full `Disc(Q)=0` union |
|---:|---:|---:|---:|---:|
| 3 | 92 | 0 | 0 | 92 |
| 5 | 2,200 | 0 | 0 | 2,200 |
| 7 | 17,052 | 0 | 0 | 17,052 |
| 11 | 229,900 | 0 | 0 | 229,900 |
| 13 | 669,240 | 0 | 0 | 669,240 |

The numerical equality of the first and last columns is special to these
five source rows.  The `A=+/-B` table is never relabeled as an exhaustive
repeated-root table.

Thus the replay visits exactly 645 ordered histogram atom pairs, not the
5,673,644 represented model pairs.  The declared atom-pair cap is `55^2=3025`,
and a separate conservative accounted-work cap is checked before completion.
The JSON freezes, for every `q`,

- the exact input trace histogram and its canonical hash;
- the normalized tensor-trace histogram;
- the complete `(x,y)` coefficient histogram;
- the complete integral local-factor histogram;
- exact coefficient-map fold masses on `A=B`, `A=-B`, their intersection,
  and their union;
- separately typed endpoint and exhaustive full-quartic repeated-root masses;
- all six rational moments in (24).

The source fixture, source producer, this producer, this note, and the tests
are LF-normalized SHA-256 locked.  The payload has its own canonical hash.

## 8. Classical literature and novelty boundary

The `GL(2) x GL(2)` automorphic tensor-product setting is classical.  A
primary boundary reference is Dinakar Ramakrishnan,
*Modularity of the Rankin--Selberg L-series, and multiplicity one for
SL(2)*, Annals of Mathematics 152 (2000),
[arXiv:math/0007203](https://arxiv.org/abs/math/0007203).

This packet neither reproves that theorem nor invokes it to broaden any
hypothesis.  The local tensor factor (7), the `Spin(4)` description, and
classical Rankin--Selberg theory are not claimed as new.  The exact
semialgebraic packaging, locked marked-cubic Cartesian laws, and explicit
finite-`q` defect formulas are a project-specific record, but no literature
priority is claimed for that packaging without a dedicated search.

## 9. Scope firewalls

This packet does not establish:

- full arithmetic or geometric `SO(4)` monodromy for a supplied family;
- a new automorphy, analytic continuation, or functional-equation theorem;
- a global curve relation from `A=+/-B` at one finite field;
- a uniform coarse-isomorphism-class pair law;
- an asymptotic rate or number-field equidistribution theorem from five rows;
- a global recognition theorem from the coefficient region alone;
- identification of the fold discriminant `D` with the exhaustive quartic
  root discriminant (the latter is `D E^2` and includes `p=4` or `r=4`);
- a zero-free region, RH, or GRH.

For global recognition, the compact coefficient inequalities would have to
be combined with integrality, determinants, ramification, compatible
cross-prime behavior, and monodromy data.  A local polynomial can lie in the
same coefficient region for reasons unrelated to an elliptic-pair tensor
origin.

## 10. Replay

From the repository root:

```text
python -B research/l-families/atlas/function_field/elliptic_pair_rankin_so4_family.py --check
python -B -O research/l-families/atlas/function_field/elliptic_pair_rankin_so4_family.py --check
python -B -m unittest tests.test_elliptic_pair_rankin_so4_family
python -B -O -m unittest tests.test_elliptic_pair_rankin_so4_family
```

To regenerate after a deliberate audited change, replace `--check` by
`--write`.  A source-lock failure must be investigated, not bypassed by
silently accepting a new upstream histogram or normalization.
