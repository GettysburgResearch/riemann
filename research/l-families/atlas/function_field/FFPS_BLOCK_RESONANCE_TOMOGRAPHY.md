# All-rank block-resonance tomography and the relative projector

Status: **exact finite Fourier/Kummer theorem on a connected monomial
stratum and exact all-rank coefficient ledger; no varying-place complex,
signed family estimate, RH, or GRH claim**

Exact bounded replay:
[`ffps_block_resonance_tomography.py`](ffps_block_resonance_tomography.py).

## 0. Outcome

The `C_2^r` block interferometer has an exact tomography theorem on every
connected monomial source stratum.  It distinguishes three quantities that
must not be conflated:

1. the ambient codimension of the stratum;
2. the codimension visible to the block-character row space;
3. the arithmetic coefficient of the geometrically constant modes.

Let `u_1,...,u_n` be physical ratio coordinates for a two-atom source, and
let the `r` quadratic block characters have exponent rows

\[
 B=(b_1,\ldots,b_r),\qquad b_i\in\mathbf F_2^n.
\tag{0.1}
\]

A selected character is indexed by `s in F_2^r` and pulls back to the
quadratic Kummer monomial with exponent

\[
 \beta(s)=sB\in\mathbf F_2^n.
\tag{0.2}
\]

Let `Z` be a connected monomial coset, and let `L_Z <= F_2^n` be the
mod-two reduction of its saturated monomial relation lattice.  Put

\[
 \rho=\operatorname{rank}B,
 \qquad
 c_Z=\dim\big(\operatorname{row}(B)\cap L_Z\big).
\tag{0.3}
\]

Then the geometrically invariant selected labels form the vector space

\[
 E_Z=\{s\in\mathbf F_2^r:\beta(s)\in L_Z\},
\]

of exact dimension

\[
 \boxed{d_Z=(r-\rho)+c_Z.}
\tag{0.4}
\]

Consequently

\[
 \boxed{
 \#\{0\ne s:\mathcal M_s|_Z\text{ is geometrically constant}\}
 =2^{d_Z}-1.}
\tag{0.5}
\]

This is the **block-resonance tomography theorem**.  A rank defect of `B`
already creates generic invariant modes.  If `B` has full row rank, only
block-visible relations contribute and `d_Z=c_Z`.

The arithmetic refinement is equally rigid.  The Frobenius signs of the
constant systems form a character

\[
 \alpha_Z:E_Z\longrightarrow\{\pm1\}.
\]

Writing `h=2^r`, the invariant coefficient of the normalized selected
average in the off-coset interferometer is

\[
 \boxed{
 A_Z={1\over h-1}\sum_{0\ne s\in E_Z}\alpha_Z(s)
 =
 \begin{cases}
 (2^{d_Z}-1)/(2^r-1),&\alpha_Z=1,\\[2mm]
 -1/(2^r-1),&\alpha_Z\ne1.
 \end{cases}}
\tag{0.6}
\]

Thus geometric multiplicity does not by itself determine a main-term
coefficient.  On an orientation-preserving fixed visible-codimension `c`
stratum with independent block rows,

\[
 A_Z={2^c-1\over2^r-1}=O_c(2^{-r}).
\tag{0.7}
\]

At the full orientation-preserving double collision, `c=d_Z=r` and

\[
 \boxed{A_Z=1.}
\tag{0.8}
\]

So fixed-codimension resonances are normalized away exponentially, but the
deepest collision is not.  This statement is coefficient tomography, not a
bound for the number or total mass of such strata.

There is an exact relative remedy.  Let `C` be the rotationally averaged
hard covariance and `S` its **unnormalized** nonprincipal selected energy.
In the Fourier group algebra,

\[
 \boxed{
 \mathsf C=\Pi_0+\sum_{s\ne0}\Pi_s,
 \qquad
 \mathsf S=\sum_{s\ne0}\Pi_s,
 \qquad
 \mathsf C-\mathsf S=\Pi_0.}
\tag{0.9}
\]

Every selected invariant channel therefore cancels coefficient by
coefficient in the relative hard-minus-selected object.  What remains is
exactly the principal channel with coefficient one.  This does not estimate
that channel; it identifies the RH-bearing remainder.

Equation (0.9) is not the atom-free off-coset interferometer.  The latter is

\[
 \mathsf I=\Pi_0-{1\over h-1}\sum_{s\ne0}\Pi_s.
\tag{0.10}
\]

It erases every same-quotient pair, including the full collision, but it does
not cancel a partial invariant ledger as a relative projector.  The two
normalizations solve different problems.

## 1. Geometric model and exact invariant criterion

Work over a finite field of odd characteristic after the fixed orientation
cover needed to make the physical quadratic characters honest Kummer
systems.  Let

\[
 T=(\mathbf G_m)^n
\]

be the physical pair-ratio torus.  The block row `b_i` defines a quadratic
Kummer line

\[
 \mathcal F_i=\mathcal L_\kappa(u^{b_i}).
\]

For `s=(s_1,...,s_r)`, put

\[
 \mathcal M_s=\bigotimes_i\mathcal F_i^{\otimes s_i}
 =\mathcal L_\kappa(u^{sB}).
\tag{1.1}
\]

Let `Z` be a geometrically connected monomial coset.  Its integral relation
lattice `Lambda_Z <= Z^n` is saturated; equivalently the quotient character
lattice is torsion-free.  Constants are squares over the algebraic closure,
so reduction modulo two gives an exact criterion:

\[
 \boxed{
 \mathcal M_s|_Z\text{ is geometrically constant}
 \iff sB\in L_Z,
 \qquad L_Z=(\Lambda_Z+2\mathbf Z^n)/2\mathbf Z^n.}
\tag{1.2}
\]

The connectedness/saturation hypothesis is load-bearing.  On a disconnected
monomial scheme, component characters can create additional constants not
recorded by one row space.

The restriction of `beta` maps `E_Z` onto
`row(B) intersect L_Z`; its kernel is `ker(beta)`.  Hence there is an exact
sequence

\[
 0\longrightarrow\ker\beta
 \longrightarrow E_Z
 \longrightarrow\operatorname{row}(B)\cap L_Z
 \longrightarrow0.
\tag{1.3}
\]

Since `dim ker beta=r-rho`, (0.4)--(0.5) follow.

This is the monomial analogue of graph-mask transversality.  There the
invariant count is controlled by the intersection with a cycle space.  Here
it is controlled by the preimage of the source-stratum relation space.

## 2. Arithmetic coefficient dichotomy

For `s in E_Z`, choose the geometrically trivial realization of
`M_s|_Z`.  Its arithmetic Frobenius acts by a sign `alpha_Z(s)`.  Tensor
multiplication gives

\[
 \alpha_Z(s+t)=\alpha_Z(s)\alpha_Z(t),
\]

so `alpha_Z` is a character of the finite vector space `E_Z`.
Orthogonality gives

\[
 \sum_{s\in E_Z}\alpha_Z(s)
 =\begin{cases}
 2^{d_Z},&\alpha_Z=1,\\
 0,&\alpha_Z\ne1.
 \end{cases}
\tag{2.1}
\]

Removing the zero label proves (0.6).  The two ledgers are therefore:

| arithmetic type on `E_Z` | selected invariant coefficient | normalized coefficient |
|---|---:|---:|
| orientation-preserving/trivial | `2^d-1` | `(2^d-1)/(2^r-1)` |
| nontrivial fixed coset | `-1` | `-1/(2^r-1)` |

The second row is not a contradiction to positivity of the complete
selected energy.  It is the Frobenius coefficient of one geometrically
constant source stratum after the source has been decomposed into signed
ledgers.

## 3. Bilateral block collision atlas

For the scalable bilateral candidate, use `2r` ratio coordinates

\[
 x_1,y_1,\ldots,x_r,y_r
\]

and disjoint block rows

\[
 b_i=e_{x_i}+e_{y_i}.
\tag{3.1}
\]

These rows have rank `r`.  The theorem gives the exact orientation-preserving
table:

| source stratum | block-visible dimension `c_Z` | invariant selected modes | normalized coefficient |
|---|---:|---:|---:|
| generic pair torus | `0` | `0` | `0` |
| `x_i=1` only, generically | `0` | `0` | `0` |
| `y_i=1` only, generically | `0` | `0` | `0` |
| `x_i y_i=1` for `i` in a `c`-set | `c` | `2^c-1` | `(2^c-1)/(2^r-1)` |
| `x_i=y_i=1` for `i` in a `c`-set | `c` | `2^c-1` | `(2^c-1)/(2^r-1)` |
| all `r` double collisions | `r` | `2^r-1` | `1` |

A one-sided physical collision is not enough: `e_(x_i)` alone does not lie
in the block row space.  A compensating block resonance `x_i y_i=1` is
already enough.  Cross-block relations are also visible: for example

\[
 \prod_{i\in S}x_i y_i=1
\]

contributes the row `sum_(i in S)b_i` even if no individual physical
coordinate collides.  Formula (0.4), rather than a visual collision list, is
the complete classifier.

For a fixed `c` and growing `r`, (0.7) is exponentially small.  This does
not imply that the union of all `c`-strata is negligible: its number,
degrees, incidence multiplicities, and source weights can grow with `r`.

## 4. Exact relative projector

Let `K=C_2^r`, `h=|K|`, and write its characters as `chi_s`,
`s in F_2^r`.  For source amplitudes `z_omega`, put

\[
 H_s=\sum_\omega\chi_s(\Phi(\omega))z_\omega,
 \qquad H_0=P.
\]

The sharp coset observations are

\[
 O_a=\sum_s\chi_s(a)H_s.
\]

Only after averaging all `h` rotations does orthogonality diagonalize the
hard covariance:

\[
 C={1\over h}\sum_{a\in K}|O_a|^2
 =|P|^2+\sum_{s\ne0}|H_s|^2.
\tag{4.1}
\]

Put

\[
 S=\sum_{s\ne0}|H_s|^2.
\]

Then

\[
 \boxed{C-S=|P|^2.}
\tag{4.2}
\]

At pair quotient `g in K`, the three kernels are

\[
 K_C(g)=\sum_s\chi_s(g)
 =\begin{cases}h,&g=0,\\0,&g\ne0,\end{cases}
\]

\[
 K_S(g)=\sum_{s\ne0}\chi_s(g)
 =\begin{cases}h-1,&g=0,\\-1,&g\ne0,\end{cases}
\]

and

\[
 \boxed{K_C(g)-K_S(g)=1.}
\tag{4.3}
\]

On a stratum with invariant space `E_Z`, the invariant-channel trace ledger
is

\[
 C_{\rm inv}=1+\sum_{0\ne s\in E_Z}\alpha_Z(s),
 \qquad
 S_{\rm inv}=\sum_{0\ne s\in E_Z}\alpha_Z(s).
\tag{4.4}
\]

Thus

| arithmetic type | `C_inv` | `S_inv` | `C_inv-S_inv` |
|---|---:|---:|---:|
| `alpha_Z=1` | `2^d` | `2^d-1` | `1` |
| `alpha_Z!=1` | `0` | `-1` | `1` |

Every common selected invariant cancels.  The surviving `1` is the
principal channel, not an error term.  Bounding it is exactly the
individualization/RH-bearing problem.

The atom-free interferometer instead is

\[
 I=|P|^2-{1\over h-1}S.
\tag{4.5}
\]

Its invariant coefficient on `Z` is `1-A_Z`.  Hence it is zero on the full
orientation-preserving collision, but equals

\[
 {2^r-2^c\over2^r-1}
\tag{4.6}

on a trivial-arithmetic visible-codimension `c` stratum.  It removes the
same-quotient collision kernel; it is not a projector that removes every
partial geometrically constant mode.

This creates an exact three-way boundary:

| object | atom-free | cancels every selected Fourier channel | retains principal |
|---|---:|---:|---:|
| selected energy `S` | no | no | no |
| relative projector `C-S` | no | yes | yes |
| off-coset interferometer `I` | yes | no (except full same quotient) | yes |

No quadratic normalization in this packet gets all three advantages for
free.

## 5. Connection to the scalable rich-core tower

`FFPS_SCALABLE_RICH_CORE_BLOCK_TOWER.md` proves, inside one declared native
rich subsource, that `r` bilateral phase blocks occur before one common
square and that their formal hard leverage is less than `(4/5)^r`.  It also
proves that every nonzero selected quotient mode is bilateral.

For any **fixed** choice of its phase places and any actual connected
monomial pair stratum, the present theorem applies once the associated
quadratic exponent matrix `B` has been constructed.  It gives two immediate
acceptance tests:

1. `rank(B)=r` is necessary to avoid a generic invariant selected mode;
2. every collision ledger must be graded by `c_Z=dim(row(B) intersect L_Z)`,
   not by ambient codimension alone.

If the disjoint bilateral rows (3.1) are legally realized, then fixed
block-visible codimension has the small normalized coefficient (0.7), the
full collision has coefficient one, and the relative object cancels every
common selected invariant before estimation.

What is **not** proved is just as important.  The scalable source identity
does not itself construct:

- one pair stack over varying closed places;
- one saturated relation lattice valid through all Boolean cleanups;
- a common derived hard-current and selected complex realizing (0.9);
- compatible maximal extension and boundary corrections;
- a bound for the number or total source mass of each `c_Z` stratum;
- a signed varying-conductor estimate or principal individualization.

In particular, this packet does not promote the fixed-place exponent matrix
to a varying-place complex.  It supplies the exact tomography that such a
construction would have to pass.

## 6. Proof ledger

Proved exactly:

- the invariant criterion (1.2) for a connected saturated monomial coset;
- the row-space/intersection dimension formula (0.4);
- the invariant selected-mode count (0.5);
- the arithmetic coefficient dichotomy (0.6);
- the bilateral collision table;
- the all-`r` relative projector (0.9), (4.2)--(4.4);
- the distinction from the normalized atom-free interferometer (4.5)--(4.6).

Imported with explicit scope:

- the fixed-fibre rank-one quadratic Kummer interpretation;
- the `C_2^r` block quotient and coset observations;
- the scalable rich-core source identity and formal leverage theorem.

Not proved:

- geometric independence for the native varying-place rich-core tower;
- a common source stack or derived complex;
- collision-stratum mass bounds, boundary-extension legality, or Betti
  control after all cleanups;
- any varying-conductor estimate, principal theorem, RH, or GRH.

## 7. Bounded replay

Run:

```text
python -B research/l-families/atlas/function_field/ffps_block_resonance_tomography.py --check
python -B -O research/l-families/atlas/function_field/ffps_block_resonance_tomography.py --check
python -B -m unittest tests.test_ffps_block_resonance_tomography
python -B -O -m unittest tests.test_ffps_block_resonance_tomography
```

The replay uses bit-packed row reduction on at most ten block labels.  It
checks generic, one-sided, aligned, fixed-codimension, full-double-collision,
arithmetic-twist, and rank-defect panels, plus the complete quotient kernel
for at most five blocks.  It enumerates no monomial strata, finite-field
points, closed places, conductors, curves, or `L`-function zeros.

## 8. Novelty boundary

The binary rank formula, finite-character orthogonality, and Fourier
projector are elementary.  The project contribution is the source-typed
coupling: it turns the scalable block mask's collision problem into one
row-space intersection invariant, separates geometric multiplicity from
arithmetic coefficient, and identifies exactly which relative object
cancels the shared invariant channels.  No external novelty or priority
claim is made.
