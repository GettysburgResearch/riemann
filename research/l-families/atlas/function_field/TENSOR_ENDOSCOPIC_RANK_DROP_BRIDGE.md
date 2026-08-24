# Tensor rank drop and the integral `+q` split locus

## Status and scope

This packet proves an exact bridge between two previously independent atlas
calculations:

1. the trace-zero pullback of the transverse rank-drop line in the ambient
   product-tensor coefficient hypersurface; and
2. the arithmetic locus where the genus-two reciprocal polynomial factors
   into two integral elliptic-form quadratics having constant term `+q`.

The bridge is one-way in general: every tensor rank-drop product state is on
the integral split locus, but most integral split states are not tensor rank
drop.  Exact converses hold after specifying which trace-zero component one
is on.

The finite tables are deterministic convolutions of already locked trace and
coefficient histograms for `q=3,5,7`.  This packet enumerates no finite field,
curve, variety, or family member.  Its weights are ordered products of two
uniform-model laws, not a coarse moduli measure.

Direct dependencies are source- and payload-locked:

- `tensor_trace_zero_singular_strata.json`;
- `genus2_endoscopic_split_locus.json`;
- `genus1_cubic_family_laws.json`; and
- `balanced_control_family_scan.json`.

Their four producers are locked separately.  The generated JSON also locks
this producer, this note, and the focused test.

## 1. Normalizations

Write the elliptic factor as

\[
 P_E(T)=1+AT+qT^2.                                            \tag{1}
\]

The genus-one source stores the geometric trace `t_E` in
`1-t_E T+qT^2`, so

\[
                         \boxed{A=-t_E}.                       \tag{2}
\]

The genus-two polynomial is

\[
 P_C(T)=1+aT+bT^2+qaT^3+q^2T^4.                              \tag{3}
\]

Its integral `+q` split predicate is

\[
 P_C(T)=(1-rT+qT^2)(1-sT+qT^2),                              \tag{4}
\]

for integers `r,s`.  Equivalently,

\[
 r+s=-a,\qquad rs=b-2q,\qquad
 \Delta=a^2-4b+8q=(r-s)^2,                                   \tag{5}
\]

with the usual square and parity condition on `Delta`.

For the product-tensor normalized coefficients `(u,v,w,h)`, the transverse
rank detector on the singular plane is

\[
                         L=h+2v+2.                             \tag{6}
\]

Introduce the integral residual

\[
                         R=A^2+b-2q.                           \tag{7}
\]

## 2. The master sum-of-squares identity

The product parameter map in the tensor packet uses

\[
 x={A^2\over q},\qquad y={a^2\over q},\qquad z={b\over q}.
\]

Its exact pullback identity is

\[
 L=(x+z-2)^2+xy.
\]

After clearing `q^2`, this becomes

\[
 \boxed{q^2L=(A^2+b-2q)^2+A^2a^2=R^2+(Aa)^2.}                \tag{8}
\]

Consequently, on real or integer product parameters,

\[
 L=0\quad\Longleftrightarrow\quad R=0\text{ and }Aa=0.       \tag{9}
\]

Thus `L=0` alone is an exact detector of the reduced tensor rank-drop union
on the finite arithmetic product laws.  This sum-of-squares inference is not
valid over arbitrary complex points: there `R^2+(Aa)^2` can vanish by
cancellation.  The scheme-theoretic rank-line pullback must retain the
singular-plane equation separately.

Equation (9) gives the two reduced branches

\[
 \boxed{A=0, b=2q}
 \quad\text{or}\quad
 \boxed{a=0, b=2q-A^2}.                                     \tag{10}
\]

## 3. Reduced components versus scheme multiplicity

Work over `Q[A,a,R]`, with fixed nonzero `q` and the triangular coordinate
change (7).  The pullback of the reduced singular plane is

\[
 I_{\rm sing}=(Aa)=(A)\cap(a).                               \tag{11}
\]

This is a reduced union of the two trace-zero components.

The target rank line has equations `u=w=L=0`.  Since `w` is a multiple of
`u` on the product map, (8) gives

\[
 \begin{aligned}
 I_{\rm rank}
   &=(Aa,R^2+(Aa)^2)\\
   &=\boxed{(Aa,R^2)}.                                        \tag{12}
 \end{aligned}
\]

Exact monomial-ideal intersection gives the primary decomposition

\[
 \boxed{(Aa,R^2)=(A,R^2)\cap(a,R^2).}                        \tag{13}
\]

Both primary components are doubled in the transverse `R`-direction.  Their
radicals are

\[
 \sqrt{I_{\rm rank}}
 =(Aa,R)=(A,R)\cap(a,R),                                      \tag{14}
\]

which, in the original variables, are precisely the two branches in (10).

This distinction matters.  The integral split locus is a square-and-parity
predicate on integer coefficients, not a scheme defined in this packet.
Only the reduced integer support in (14) is proved to be split.  No
containment of the `R^2` nilpotent thickening in an “endoscopic scheme” is
asserted.

Indeed, substituting `b=2q-A^2+R` into (5) gives

\[
 \Delta=a^2+4A^2-4R.                                         \tag{15}
\]

On the reduction `(Aa,R)`,

\[
 \Delta=(a+2A)^2=(a-2A)^2,                                   \tag{16}
\]

because `Aa=0`.  On the nonreduced scheme, however,

\[
 \Delta-(a+2A)^2=-4(R+Aa),                                   \tag{17}
\]

and `R` survives as a nonzero square-zero direction.  Formula (17) is the
explicit multiplicity firewall.

## 4. Branch containment in the integral split locus

### 4.1 Elliptic trace-zero branch

On `A=0,b=2q`, direct multiplication gives

\[
 \boxed{
 P_C(T)=(1+qT^2)(1+aT+qT^2).}                                \tag{18}
\]

In the convention (4), the factor traces are `0` and `-a`.  Also

\[
 \Delta=a^2,                                                   \tag{19}
\]

so the square and parity requirements are automatic.

### 4.2 Genus-two trace-zero branch

On `a=0,b=2q-A^2`,

\[
 \boxed{
 P_C(T)=(1+AT+qT^2)(1-AT+qT^2).}                             \tag{20}
\]

The factor traces are `-A,A`, and

\[
 \Delta=4A^2.                                                  \tag{21}
\]

Again the split criterion holds identically.  The two branches meet at

\[
 A=a=0,\qquad b=2q,                                           \tag{22}
\]

where the factor is `(1+qT^2)^2`.  This is the only repeated-factor state on
the rank-drop union; every other rank-drop state is split-distinct.

Equations (18)--(21) prove

\[
 \boxed{\text{tensor rank drop}\Longrightarrow
        \text{integral `+q` split}.}                          \tag{23}
\]

This is a polynomial statement.  The phrase “endoscopic” remains an
operational label and imports no isogeny or polarization theorem.

## 5. Exact converse classification

Suppose first that `P_C` is split with factor traces `(r,s)` as in (4).

On the `A=0` singular component,

\[
 b=2q\quad\Longleftrightarrow\quad rs=0.                      \tag{24}
\]

Therefore

\[
 \boxed{A=0:\quad\text{rank drop iff one split factor trace is zero}.} \tag{25}
\]

On the `a=0` singular component, `r+s=0`, so the traces are `(-r,r)` and
`b=2q-r^2`.  Hence

\[
 \boxed{a=0:\quad\text{rank drop iff }r^2=A^2,}              \tag{26}
\]

or equivalently iff the unordered trace pair is `{-A,A}`.

Outside the singular preimage, `Aa!=0`, equation (8) makes rank drop
impossible over the integer model law even when `P_C` is split.  Thus the
failure of the global converse has three explicit sources:

- split states outside either trace-zero component;
- on `A=0`, split states whose two factor traces are both nonzero; and
- on `a=0`, split states whose anti-diagonal trace magnitude does not match
  `|A|`.

## 6. Complete frozen product-model incidence

Each source genus-one trace atom is paired with each source genus-two
coefficient atom.  Pair weights are products of the two member counts.

| `q` | all pairs | integral split | tensor singular | rank drop | split and singular | split-singular but not rank | split outside singular |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 2,916 | 486 | 1,068 | 66 | 150 | 84 | 336 |
| 5 | 250,000 | 70,500 | 82,480 | 5,000 | 21,700 | 16,700 | 48,800 |
| 7 | 4,235,364 | 1,049,580 | 1,155,420 | 72,324 | 287,532 | 215,208 | 762,048 |

The rank-drop share of the full integral split locus is respectively

\[
 {11\over81},\qquad {10\over141},\qquad {41\over595}.         \tag{27}
\]

Thus (23) is exact, but the converse misses most split product pairs in every
frozen field.

The split type within rank drop is:

| `q` | repeated rank pairs | distinct rank pairs |
|---:|---:|---:|
| 3 | 0 | 66 |
| 5 | 100 | 4,900 |
| 7 | 1,764 | 70,560 |

The repeated counts equal the branch intersection in (22), as predicted.

### 6.1 Inclusive component converses

The following component rows include their common intersection.

| `q` | `A=0` split | `A=0` rank/zero-factor | `A=0` split non-rank | `a=0` split | `a=0` rank/trace-match | `a=0` split mismatch | rank intersection |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 108 | 48 | 60 | 54 | 18 | 36 | 0 |
| 5 | 14,100 | 2,900 | 11,200 | 9,500 | 2,200 | 7,300 | 100 |
| 7 | 149,940 | 37,044 | 112,896 | 160,524 | 37,044 | 123,480 | 1,764 |

These numbers quantify exactly the two converse failures in (25)--(26).

The JSON retains every rank-drop histogram atom, including `A,a,b`, both
source multiplicities, branch labels, factor traces, discriminant, and split
type.  A canonical digest binds the complete 2,471-row classification ledger
without bloating the fixture with every complement row.

## 7. What the detectors recognize

On the integer product law, `L=0` is exactly rank drop by (8)--(9).  Its
contingency with the integral split predicate is:

| `q` | split and `L=0` | split and `L>0` | non-split and `L=0` | non-split and `L>0` |
|---:|---:|---:|---:|---:|
| 3 | 66 | 420 | 0 | 2,430 |
| 5 | 5,000 | 65,500 | 0 | 179,500 |
| 7 | 72,324 | 977,256 | 0 | 3,185,784 |

So `L=0` has perfect precision for the split predicate but low recall: it
recognizes the special trace-matched rank-drop sublocus, not endoscopy in
general.

The locked endoscopic packet already proves that the genus-two-only controls
`B`, `F`, and even the complete balanced Frobenius echo fail to recognize the
full split locus.  The bridge records those source facts unchanged:

| `q` | `B`: fibers / mixed / members mixed | `F`: fibers / mixed / members mixed | complete echo: fibers / mixed / members mixed |
|---:|:---:|:---:|:---:|
| 3 | `14 / 1 / 12` | `12 / 1 / 24` | `17 / 1 / 12` |
| 5 | `33 / 3 / 246` | `24 / 6 / 700` | `39 / 1 / 6` |
| 7 | `55 / 5 / 2,898` | `53 / 5 / 2,856` | `67 / 2 / 924` |

There is no contradiction: `L` consumes the additional elliptic coefficient
`A` and detects only the much smaller matched pullback locus, whereas the
other controls are functions of the genus-two polynomial alone.

## 8. Resource and replay contract

The complete finite transform visits

\[
 7\cdot32+9\cdot81+11\cdot138=2{,}471                       \tag{28}
\]

source histogram atom pairs, below the strict exclusive cap `5,000`.  It uses
only integers, `Fraction`, and sparse monomial-ideal arithmetic.  There are no
floats, random samples, interpolation steps, or new field/member scans.

Replay with

```text
python research/l-families/atlas/function_field/tensor_endoscopic_rank_drop_bridge.py --check
python -m unittest tests.test_tensor_endoscopic_rank_drop_bridge -v
python -O -m unittest tests.test_tensor_endoscopic_rank_drop_bridge -v
```

Bare `--check` and `--write` use the adjacent default fixture; an explicit
path is also accepted.

## 9. Geometry and interpretation firewall

What is exact here:

- the sum-of-squares identity (8);
- the reduced and nonreduced pullback ideals (11)--(14);
- both branch factorizations and the converse classification;
- the complete locked product-histogram incidence tables; and
- the detector contingencies and source locks.

What is not implied:

- The ambient coefficient hypersurface or its transverse cone being singular
  does not make `E`, `C`, `E x C`, or a Jacobian a singular variety.
- The polynomial factors in (18) or (20) do not, within this packet, import
  Honda--Tate/Tate theory, prove a product isogeny, identify the canonical
  principal polarization, split a smooth genus-two curve, or produce
  elliptic quotient maps.
- The nilpotent scheme in (12)--(13) is not asserted to lie in a scheme of
  endoscopic objects; only its reduced integer support passes the arithmetic
  split predicate.
- Trace zero or rank drop is not by itself evidence of extra endomorphisms,
  a special correspondence, or a family monodromy component.
- The three frozen product-model laws imply no all-`q` frequency,
  equidistribution theorem, number-field transfer, RH statement, or GRH
  statement.

The strongest honest interpretation is therefore a precise coefficient-level
incidence theorem: tensor rank drop singles out two trace-matched branches
inside the larger integral quadratic-factor locus.
