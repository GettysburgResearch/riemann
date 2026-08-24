# Genus-two tail geometry: exact bounded packet

## Purpose and scope

This note studies the exceptional negative tail of the existing genus-two toy
minor

\[
K=qa^2-b^2
\]

without enumerating another finite field or another family member.  The only
finite inputs are the frozen exact `q=3,5,7` support histograms in
`genus2_q_scan.json` and the aggregate affine-orbit certificate in
`genus2_affine_orbits.json`.  The auxiliary search is a sign-quotiented lattice
of at most 627 integer coefficient pairs in any one field.

There are two logically different layers throughout:

1. the polynomial identities below hold for every positive integer `q` and
   every integer-coefficient reciprocal quartic with admissible real pair
   traces;
2. every support, orbit, moment-share, absence, and isogeny-shape statement is
   an exact fact about `q=3,5,7` only.

Replay the packet with

```text
python research/l-families/atlas/function_field/genus2_tail_geometry.py --check research/l-families/atlas/function_field/genus2_tail_geometry.json
python -m unittest tests.test_genus2_tail_geometry -v
python -O -m unittest tests.test_genus2_tail_geometry -v
```

The script imports neither finite-field arithmetic nor the q-scan producer.

## Real Weil coordinates

Write the reciprocal Frobenius polynomial as

\[
P(T)=T^4+aT^3+bT^2+qaT+q^2.
\]

It has a degree-two real Weil polynomial

\[
R(X)=X^2+aX+(b-2q),\qquad
P(T)=T^2R(T+q/T).
\]

If `t_1,t_2` are the roots of `R`, then

\[
t_1+t_2=-a,qquad t_1t_2=b-2q,qquad
\Delta=(t_1-t_2)^2=a^2-4b+8q.
\]

Admissibility means `t_i` are real and lie in the Hasse interval
`[-2 sqrt(q),2 sqrt(q)]`.  For integer `(a,b)`, this is tested exactly by

\[
a^2\le16q,quad \Delta\ge0,quad b+2q\ge0,quad
\Gamma=(b+2q)^2-4qa^2\ge0.
\]

The last condition is not an arbitrary sieve:

\[
\Gamma=(4q-t_1^2)(4q-t_2^2).
\]

Thus `Delta` measures collision of the two real traces, while `Gamma` measures
their combined distance from the two Hasse endpoints.

## Three exact factorizations

### Square defect

Direct expansion gives

\[
P(T)=\left(T^2+\frac a2T+q\right)^2-\frac{\Delta}{4}T^2.
\]

Consequently `Delta=0` is exactly the repeated-angle locus.  Integrality then
forces `a=2r`, and

\[
b=2q+r^2,qquad
P(T)=(T^2+rT+q)^2,qquad
K=-4q^2-r^4.
\]

The collision wall therefore has a discrete quartic ladder, not a linear tail.

### Frobenius discriminant

An independent monic-quartic discriminant calculation factors as

\[
\operatorname{disc}(P)
=q^2\Delta^2\Gamma,
\qquad
\Gamma=(b+2q)^2-4qa^2=(6q-b)^2-4q\Delta.
\]

The two components of the nonregular locus are now explicit: collision of real
traces (`Delta=0`) and contact with a Hasse endpoint (`Gamma=0`).  The Haar
minimum sits at their intersection, not on the collision wall alone.

### Defect from the Haar edge

The lower `USp(4)` edge is `K=-20q^2`.  Its exact defect is

\[
E=20q^2+K
=q\Delta+(6q-b)(2q+b).
\]

Both summands are nonnegative for admissible pair traces.  Equality forces
`Delta=0`, `b=6q`, and `a^2=16q`, equivalently
`t_1=t_2=+/-2 sqrt(q)`.

There is also a useful localization lemma.  Put `x_i=t_i/sqrt(q)` and
`p=x_1x_2`.  Then

\[
K/q^2=(x_1-x_2)^2-4-p^2.
\]

If `p<=0`, writing `r=-p` gives

\[
(x_1-x_2)^2\ge4r,qquad
K/q^2\ge4r-4-r^2=-(r-2)^2\ge-4.
\]

Hence

\[
K<-4q^2\quad\Longrightarrow\quad b>2q.
\]

For such a far-negative point, the edge identity implies

\[
\Delta\le E/q,qquad 6q-b\le E/(4q).
\]

So genuine approach to `-20` simultaneously forces trace collision and a large
positive product `t_1t_2` near `4q`.

## The three frozen minima have three different shapes

The q-scan support minimum determines a unique admissible pair `(abs(a),b)` in
each field.  Combining it with the aggregate affine certificate gives one
minimum orbit in every case.

| `q` | chosen `(a,b)` | `K` | `Delta` | `Gamma` | orbit / stabilizer | exact Frobenius shape |
|---:|---:|---:|---:|---:|---:|---|
| 3 | `(-2,6)` | `-24` | 4 | 96 | `6 / 1` | `(T^2+3)(T^2-2T+3)` |
| 5 | `(-4,14)` | `-116` | 0 | 256 | `10 / 2` | `(T^2-2T+5)^2` |
| 7 | `(-7,25)` | `-282` | 5 | 149 | `42 / 1` | irreducible over `Q` |

The orbit proof does not need the omitted per-orbit table.  At `q=5`, the
frozen order-two stabilizer witness is itself the ten-member minimum atom.  At
`q=3,7`, every nonfree frozen orbit has stabilizer order two.  A nonidentity
affine involution in odd characteristic has multiplier `-1`; since `-1` is a
nonsquare in both fields, it flips nonzero `a`.  The unique minimum pairs have
nonzero `a`, so their stabilizers are trivial.  Their atom counts equal the
full affine group orders `6` and `42`.

This yields an exact isogeny-shape trichotomy:

- `q=3` is split nonisotypic, with elliptic traces `0` and `2`;
- `q=5` is split isotypic, with elliptic trace `2` twice;
- `q=7` is `F_7`-simple.  Here `R=X^2-7X+11` has real trace field
  `Q(sqrt(5))`, and modulo two the quartic is
  `T^4+T^3+T^2+T+1=Phi_5`.  It has no linear factor, while division by the sole
  irreducible quadratic `T^2+T+1` leaves `T+1`, proving irreducibility.

The corresponding quartic discriminants are `13824`, `0`, and `182525`.

The important corrective is that the extreme tail is **not** uniformly a
repeated-angle or automorphism phenomenon.  The minimum atoms that dominate
high moments already occur in three different Frobenius geometries.

## Repeated-angle ladder versus the actual support

The complete integral collision ladders and their intersections with the
frozen `K` supports are:

```text
q=3: r=0..3, K=-36,-37,-52,-117;                  no support intersection
q=5: r=0..4, K=-100,-101,-116,-181,-356;          r=0,2 intersect
q=7: r=0..5, K=-196,-197,-212,-277,-452,-821;     r=0,2 intersect
```

At the positive rung `r=2`, the admissible coefficient pair is unique.  Thus
all ten `q=5` members at `K=-116` and all 42 `q=7` members at `K=-212` are
repeated-angle members.  Yet their twelfth absolute-moment shares are radically
different:

```text
q=5, K=-116: 371001690114457905135616 / 598826630780182957326013
              = 0.619547747286...
q=7, K=-212: 515122296789900884328841216 / 21534399981678900177112291767
              = 0.023920903170...
```

At `q=7`, the simple off-diagonal minimum supplies `0.734068421457...` of the
same moment.  Isolating the collision wall is therefore necessary for regular
semisimple arguments, but it is not a sufficient model for the high tail.

## A realization gap, not an integrality gap

The tiny exact coefficient-lattice scan finds much deeper admissible integer
quartics than the marked quintic family realizes:

| `q` | admissible `(abs(a),b)` pairs | lattice minimum `(abs(a),b;K)` | actual minimum `K` | actual/lattice edge-defect ratio |
|---:|---:|---:|---:|---:|
| 3 | 38 | `(6,15;-117)` | `-24` | `52/21` |
| 5 | 75 | `(8,26;-356)` | `-116` | `8/3` |
| 7 | 118 | `(10,39;-821)` | `-282` | `698/159` |

Every lattice minimum is the largest integral repeated rung available:
`r=3,4,5` respectively.  None of its `K` values appears in the exact family
support.  Thus small-field tail scarcity is not explained by coefficient
integrality or by the `USp(4)` trace region.  The missing ingredient is
realization by this Jacobian family with its marked rational Weierstrass point.

This is a question nomination, not a nonexistence theorem for genus-two
Jacobians in general.  An admissible reciprocal quartic may fail to be a Weil
polynomial, may represent an abelian isogeny class containing no principal
polarization or Jacobian, or may be realized only by curves outside the marked
quintic presentation.

## High moments detect one atom by order ten

For an atom `k`, its exact share of the absolute moment of order `m` is

\[
\frac{n_k|k|^m}{\sum_j n_j|j|^m}.
\]

The minimum atom is below one half at order eight and above one half at order
ten in all three fields:

| `q` | order 8 | order 10 | order 12 |
|---:|---:|---:|---:|
| 3 | `0.489148036275` | `0.538377894777` | `0.583992741334` |
| 5 | `0.395815186937` | `0.517080057799` | `0.619547747286` |
| 7 | `0.494136681249` | `0.629807910214` | `0.734068421457` |

The earlier twelfth-moment observation can therefore be sharpened: the single
minimum orbit already becomes the majority contribution at the tenth even
moment in every frozen field.

The natural uniform-member measure is the orbit measure weighted by affine
orbit size, equivalently by inverse marked stabilizer order up to the common
group factor.  For the minimum atom its mass, the coarse one-representative
mass, and their ratio are

```text
q=3: 1/27  versus 1/29,   coarse/member = 27/29
q=5: 1/250 versus 1/132,  coarse/member = 125/66
q=7: 1/343 versus 1/349,  coarse/member = 343/349.
```

The extra `q=5` stabilizer makes coarse orbit averaging overcount precisely the
repeated minimum stratum by almost a factor of two.  Full coarse-orbit means of
`K` or the high character packet `H` are **not identifiable** from the frozen
aggregate fixture, because it intentionally omits the invariant attached to
each orbit.  This packet records that failure instead of rerunning the field
enumeration.

## The q=5 minimum has hidden non-affine geometry

The exact minimum witness is

\[
C:y^2=x^5+x^3+x\quad\text{over }\mathbf F_5.
\]

Oddness gives the affine symmetry

\[
(x,y)\longmapsto(-x,2y).
\]

It has order four on the curve and squares to the hyperelliptic involution;
the affine conductor action sees only its order-two shadow.

The conductor is also reciprocal:

\[
x^6D(1/x)=D(x).
\]

Hence there is a non-affine involution

\[
\tau:(x,y)\longmapsto(1/x,y/x^3).
\]

The two exact quotient maps are visible without point counting.  With
`u=x+1/x`,

\[
v=\frac{y(x+1)}{x^2}
\quad\Longrightarrow\quad
v^2=(u^2-1)(u+2),
\]

and for the hyperelliptic involution composed with `tau`,

\[
w=\frac{y(x-1)}{x^2}
\quad\Longrightarrow\quad
w^2=(u^2-1)(u-2).
\]

The script verifies both as zero Laurent-polynomial residuals.  These quotient
maps make the elliptic splitting geometric, while
`P=(T^2-2T+5)^2` shows that both factors lie in the same ordinary trace-two
isogeny class.

This also sharpens the measure warning.  `AGL(1,F_q)` preserves the chosen
branch point at infinity.  The inversion `tau` exchanges it with another
branch point, so the affine stabilizer is not the full automorphism group of
the unmarked curve.  “Stack-weighted” claims based on these orbit sizes must be
read as weights for marked affine presentations.

## What this packet leaves open

- Three fields do not support an asymptotic frequency or rate claim.
- The `q=7` real trace field `Q(sqrt(5))` is exact, but no new endomorphism-ring
  or real-multiplication theorem is asserted here.
- The absent coefficient-lattice minima are not proved absent from every
  genus-two Jacobian family.
- Per-orbit `K` and `H` values cannot be recovered from the aggregate affine
  fixture, so no full uniform-orbit mean is reported.
- The toy coefficient minor remains distinct from an analytic Pick/Loewner,
  XD, or HCNC detector, and nothing here transfers to number fields.

The most concrete next problem is a realization theorem: classify which
integral real Weil polynomials near the codimension-two corner
`Delta=Gamma=0` occur in the rational-Weierstrass genus-two family, separately
for split nonisotypic, split isotypic, and simple real-quadratic strata.  Any
effective high-moment theorem must handle all three rather than declaring the
collision wall to be the whole tail.
