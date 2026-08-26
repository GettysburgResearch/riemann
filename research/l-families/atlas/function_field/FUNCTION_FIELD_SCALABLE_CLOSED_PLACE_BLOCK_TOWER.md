# Function-field scalable closed-place block tower

Status: **exact closed-place orientation and conditional clean-pair algebra,
plus a squarefree factor-count asymptotic from Euler-product singularity
analysis; no universal FFPS source adapter or complex, signed trace estimate,
RH, or GRH**

Bounded replay:
[`function_field_scalable_closed_place_block_tower.py`](function_field_scalable_closed_place_block_tower.py).

## 0. Outcome

The scalable rich-core architecture has a natural one-characteristic
function-field port.  It is stronger than a collection of fixed-fibre
examples: the permissible block rank can grow logarithmically with conductor
degree on a density-one set of squarefree polynomial cores.

Let `q` be odd and let `C,D in F_q[T]` be squarefree coprime cores of degree
`n`.  For the source-algebra statement, additionally assume a clean pair

\[
 N=P G^2C^2,\qquad M=QG^2D^2,
 \qquad (C,Q)=(D,P)=1,
\tag{0.0}
\]

with all displayed factors pairwise coprime as required by the two
orientations.  This is the direct function-field analogue of the clean pair
delivered by the number-field FFPS renewals; it is an assumption here, not a
constructed function-field Boolean/owner adapter.

A closed place `v` of degree `d` supports the quadratic orientation of the
sign-pair quotient exactly when

\[
 4\mid q^d-1.
\tag{0.1}
\]

Therefore the eligible degree density is

\[
 \delta_q=
 \begin{cases}
 1,&q\equiv1\pmod4,\\
 1/2,&q\equiv3\pmod4,
 \end{cases}
\tag{0.2}
\]

where in the second case precisely the even-degree places are eligible.

If

\[
 r=\lfloor\alpha\log n\rfloor,
 \qquad0<\alpha<\delta_q,
\tag{0.3}
\]

then a uniformly chosen monic squarefree degree-`n` polynomial has fewer
than `r` eligible irreducible factors with probability at most

\[
 \boxed{
 n^{-c_{\delta_q}(\alpha)+o(1)},\qquad
 c_\delta(\alpha)=
 \delta-\alpha+\alpha\log(\alpha/\delta)>0.}
\tag{0.4}
\]

Choose the first `r` eligible factors of each core and cross-pair them.  For
every clean pair (0.0), the `2r` nonzero closed-place Ramanujan identities can
be multiplied before any square is taken, and every nontrivial mode of the
resulting `C_2^r` quotient is nonprincipal on both sides.  This is a
coefficientwise clean-pair identity; calling it a decomposition of the full
FFPS current would require the missing adapter.  Each block has residue
cardinalities `Q_1,Q_2>=5` and

\[
 L_{Q_1,Q_2}<4/5.
\]

Consequently

\[
 \boxed{
 L_r<(4/5)^r
 =n^{-\alpha\log(5/4)+o(1)}.}
\tag{0.5}
\]

This produces, inside one characteristic, a power-of-conductor-degree formal
leverage gain on a density-one squarefree-core family.  It is a concrete
global target for the varying-closed-place sheaf programme.  It does not yet
construct the Boolean/owner incidence complex or estimate its relative
Frobenius trace.

## 1. Closed-place orientation

For a place of degree `d`, the residue field is `F_(q^d)`.  The sign-pair
group

\[
 F_{q^d}^{\times}/\{\pm1\}
\]

has a nontrivial quadratic character exactly when its order `(q^d-1)/2` is
even, proving (0.1).

If `q=1 mod 4`, every `q^d` is one modulo four.  If `q=3 mod 4`, this happens
exactly for even `d`.  The prime-polynomial theorem

\[
 I_q(d)={q^d\over d}+O(q^{d/2}/d)
\]

shows that the logarithmic density of even degrees in the closed-place Euler
product is one half.  This proves (0.2).

Under (0.0), at each eligible factor `L|C`, the source difference is nonzero
modulo `L`, while at each eligible `R|D` the opposite orientation holds.  The
residue-field additive identities are

\[
 \sum_{h\in k_L^\times}\psi_L(h(N-M))=-1,
 \qquad
 \sum_{k\in k_R^\times}\psi_R(k(N-M))=-1.
\tag{1.1}
\]

Their product over `r` factors on both sides equals `(-1)^(2r)=1` before one
common square.  Mellin transformation of this clean pair supplies the
physical squareclasses at those `2r` places.  Cross-pairing one place from
each core ensures every nonempty block subset remains bilateral.

This is the function-field analogue of the clean-pair source algebra in
`FFPS_SCALABLE_RICH_CORE_BLOCK_TOWER.md`.  A universal Boolean/owner source
adapter and a moduli-space complex realizing all varying places are still
missing.  In particular, (1.1) alone does not prove that all clean pairs occur
with the required FFPS coefficients or that their sum commutes with the
subsequent hard restriction.

## 2. Squarefree generating function

Let `omega_E(F)` count eligible irreducible factors of a squarefree monic
polynomial.  For `0<t<=1`, its bivariate Euler product is

\[
 \mathcal F_t(u)
 =\prod_{P\in E}(1+t u^{\deg P})
  \prod_{P\notin E}(1+u^{\deg P}).
\tag{2.1}
\]

The linear term in `log F_t` is

\[
 t\sum_{P\in E}u^{\deg P}
 +\sum_{P\notin E}u^{\deg P}.
\]

The prime-polynomial theorem and (0.2) give the singular expansion at
`u=1/q`

\[
 \boxed{
 \mathcal F_t(u)
 =(1-qu)^{-\{1+\delta_q(t-1)\}}G_{q,t}(u),}
\tag{2.2}
\]

where `G_(q,t)` is analytic and nonzero in a fixed neighbourhood slit at the
dominant singularity, uniformly for `t` in compact subsets of `(0,1]`.
All quadratic and higher Euler-log terms converge there.

When `q=3 mod 4`, the parity split also produces a secondary factor
`(1+qu)^((1-t)/2)` at `u=-1/q`.  Its coefficient contribution is one full
power of `n` smaller than the positive `u=1/q` term for `0<t<1`; it does not
change (2.3).  Recording this secondary branch is necessary—calling the
remainder analytic on the whole dominant circle would be false.

Standard coefficient transfer gives

\[
 \sum_{\substack{F\text{ monic squarefree}\\\deg F=n}}
 t^{\omega_E(F)}
 \asymp_{q,t}
 q^n n^{\delta_q(t-1)}.
\tag{2.3}
\]

The number of monic squarefree degree-`n` polynomials is
`q^n-q^(n-1)`.  Hence

\[
 \mathbb E[t^{\omega_E(F)}]
 \ll_{q,t}n^{\delta_q(t-1)}.
\tag{2.4}
\]

If `omega_E(F)<r`, then

\[
 1\le t^{-(r-1)}t^{\omega_E(F)}.
\]

Take `r` from (0.3) and optimize at `t=alpha/delta_q`.  Equations
(2.3)--(2.4) yield (0.4).  Requiring richness for both coprime cores changes
only the union bound at this exponent; the coprimality Euler factors are
analytic and nonzero at the same dominant singularity.

## 3. Formal leverage frontier

For an eligible cross-pair with norms `Q_1,Q_2`, the exact hard block factor
is

\[
 {4(Q_1-1)(Q_2-1)\over
   5Q_1Q_2+Q_1+Q_2+1}<{4\over5}.
\tag{3.1}
\]

Disjoint block leverage multiplies, proving (0.5).

The two competing degree exponents are

\[
 c_\delta(\alpha)
 =\delta-\alpha+\alpha\log(\alpha/\delta),
 \qquad
 \lambda(\alpha)=\alpha\log(5/4).
\tag{3.2}
\]

Their balanced diagnostic points are

\[
\begin{array}{c|c|c}
\delta&\alpha_*&c_\delta(\alpha_*)=\lambda(\alpha_*)\\ \hline
1/2&0.274064461784&0.061155717291\\
1&0.548128923568&0.122311434583.
\end{array}
\tag{3.3}

The second row is exactly twice the first because both exponents scale
linearly under `alpha=delta beta`.

This frontier ignores the degrees of the selected places in the eventual
Betti number, irreducible-place projectors, collision strata, and the signed
hard-minus-selected trace.  It is not an optimized RH theorem.

## 4. What the closed-place theorem changes

The fixed-fibre ternary sheaf packet left six universal operations open:
varying places, irreducibility selection, owners, Boolean incidence,
collision cleanup, and signed conductor recombination.  The present result
settles one preliminary concern:

\[
 \boxed{
 \text{eligible closed-place supply is abundant enough for growing block
 rank.}}
\]

It also quantifies the target.  A relative trace-complex theorem is useful if
its normalized loss grows more slowly than
`n^(alpha log(5/4))`, while its excluded poor-core contribution stays below
`n^(-c_delta(alpha))` at the relevant source normalization.

The remaining geometric questions are sharper:

1. Can the varying irreducible-place projector be built with Betti cost
   polynomial in `r` and the selected degrees?
2. Do the common invariant constituents cancel in the relative
   hard-minus-selected Grothendieck class before the place pushforward?
3. Can factor-degree profiles be chosen so total ramification grows only
   linearly in `r`, rather than with conductor degree `n`?
4. Does the Boolean/owner source weight preserve the squarefree factor-count
   large deviation (0.4)?

## 5. Proof ledger

Proved from exact clean-pair algebra plus standard prime-polynomial
singularity analysis:

- the closed-place orientation criterion and density (0.1)--(0.2);
- the conditional `2r`-phase pre-square identity for every clean pair (0.0);
- bilateral support of every selected quotient mode;
- the squarefree factor-count bound (0.4);
- the power-degree leverage bound (0.5);
- the diagnostic frontier (3.3).

Not proved:

- a universal varying-place sheaf or Boolean/owner source adapter (and hence
  an identity for the fully summed FFPS current);
- uniform Betti/conductor control in the selected place degrees;
- the signed relative trace estimate or source-weighted poor-core bound;
- principal individualization, RH, or GRH.

External calibration: Das--Elma--Kuo--Liu et al.,
[*On the number of irreducible factors with a given multiplicity in function
fields*](https://arxiv.org/abs/2409.08559), prove in particular that the
number of distinct multiplicity-one factors has normal order `log(deg F)`
and satisfies an Erdos--Kac theorem.  That is consistent with the
`delta log n` supply used here; the residue-degree-restricted Chernoff
exponent (0.4) is derived directly from (2.1), not imported from their result.

## 6. Bounded replay

```text
python -B research/l-families/atlas/function_field/function_field_scalable_closed_place_block_tower.py --check
python -B -O research/l-families/atlas/function_field/function_field_scalable_closed_place_block_tower.py --check
python -B -m unittest tests.test_function_field_scalable_closed_place_block_tower
python -B -O -m unittest tests.test_function_field_scalable_closed_place_block_tower
```

The replay checks five base cardinalities and closed-place degrees through
eight, plus scalar frontier equations.  It enumerates no polynomial, closed
place, curve, or point.
