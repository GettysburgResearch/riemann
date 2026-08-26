# Multiscale FFPS masks: one lawful square, no bandwise conductor escape

Status: **exact finite tensor/Fourier/source-order theorem and an exact
modewise conductor budget; no universal relative-complex no-go, signed
family estimate, principal individualization, RH, or GRH**

Exact bounded replay:
[`ffps_multiscale_single_square_gate.py`](ffps_multiscale_single_square_gate.py).

## 0. Outcome

Replacing one rank-`R` mask by bounded-rank masks in many degree bands does
not create a third assembly option at the quadratic source level.  There are
two relevant cases.

1. **All band restrictions occur before one common square.**  This is lawful
   in the rich-core source.  The gains multiply, but the construction is
   exactly the original rank-`R` joint quotient in a multiscale ordering.
   Every cross-band Fourier mode remains present and the selected place
   degrees add in its conductor budget.
2. **Each band is marginalized and squared as an independent scalar
   current.**  Multiplying the resulting inequalities produces a `2J`-th
   moment, where `J` is the number of bands.  Returning to quadratic scale
   takes a `J`-th root, changing the product leverage into its geometric
   mean.  It therefore does not accumulate the desired power saving for the
   native principal square.

More precisely, let band `j` contain `r_j>=1` binary checkerboard blocks and
put

\[
 R=\sum_{j=1}^Jr_j,\qquad h_j=2^{r_j},\qquad H=2^R=\prod_jh_j.
\]

If `L_j` is the sharp hard leverage of band `j`, coherent restriction before
the square gives

\[
 \boxed{L_{\rm joint}=\prod_{j=1}^JL_j.}
\tag{0.1}
\]

But its quotient is `K=C_2^R`, not a disjoint list of small quotients.  Of
its `H-1` nonprincipal characters, only

\[
 \sum_j(h_j-1)
\]

are supported in one band.  The remaining

\[
 \boxed{H-1-\sum_j(h_j-1)}
\tag{0.2}
\]

are cross-band modes.  For equal bounded rank `r_j=b`, their proportion is

\[
 1-{J(2^b-1)\over2^{bJ}-1}\longrightarrow1.
\tag{0.3}
\]

Thus almost all of the lawful joint selected spectrum is invisible to a
collection of separately squared band currents.

This closes the multiscale option left open in
`FUNCTION_FIELD_CLOSED_PLACE_SUPPLY_TAX.md` for every architecture that pays
modewise or common-open conductor.  Banding remains potentially useful only
inside a genuinely **relative joint complex** that cancels large-degree
constituents before any separate-mode conductor bound.  This packet does not
rule out such a cancellation.

The source construction imports exactly the four PR #751 locks already
audited for the rich-core tower:

| source claim | frozen blob | use here |
|---|---|---|
| `L-106080` | `346cc52420ec65457c2a5accc045d4a85635cc24` | squarefree original cores |
| `L-102884` | `179ae16058aa335c90f3b5a68350ff5a6929bab0` | common-core extraction |
| `L-106090` | `dadf3a4a65d2575983d692dafc0c94142c9a038d` | cross-coprimality and nonzero phases |
| `L-106120` | `a8d829dc10611adb7bfb4853902bdff0ab02a065` | one-current bilateral tensor template |

No new source identity is assumed.  The local tensor cost is the exact
coherent restriction theorem in `FFPS_COHERENT_TENSOR_COST_FRONTIER.md` and
the block version in `FFPS_BLOCK_CHECKERBOARD_COSET_INTERFEROMETER.md`.

## 1. The coherent pre-square identity

For band `j`, let `A_j` be the retained hard subgroup in its local phase
space.  The restrictions commute, so sequential pre-square filtering is
literally

\[
 \mathbf1_A=\prod_{j=1}^J\mathbf1_{A_j},
 \qquad A=\prod_jA_j.
\tag{1.1}
\]

The product Gram and the restricted constant vector also tensor.  Hence the
joint optimizer is the tensor product of the band optimizers and its sharp
dual cost is the product (0.1).  This is the same coherent-before-square
mechanism isolated in `FFPS_COHERENT_TENSOR_COST_FRONTIER.md`; a degree-band
label does not change the tensor algebra.

For a source atom set with quotient phase `Phi:Omega -> K`, write

\[
 P=\sum_{\omega}z_\omega,\qquad
 H_\chi=\sum_\omega\chi(\Phi(\omega))z_\omega.
\]

The one-square off-coset recombination is

\[
 \boxed{
 \mathcal I_{\rm joint}
 =|P|^2-{1\over H-1}\sum_{\chi\ne1}|H_\chi|^2.}
\tag{1.2}
\]

Applying the bands sequentially before this square changes neither (1.2)
nor its full character sum.  In particular it cannot replace that sum by
the band-pure characters alone.

### Native rich-core realization

The source order is lawful on the declared rich subsource.  Choose all `R`
cross-paired eligible place pairs canonically, group them by degree band,
and multiply their `2R` nonzero Ramanujan identities inside the same source
atom.  Then perform the complete Mellin transform, impose every band hard
restriction, and square once:

```text
one principal source atom
 -> all 2R nonzero place phases
 -> complete 2R-fold Mellin transform
 -> every band restriction
 -> one common square and Wick cleanup.
```

The product of the Ramanujan factors is still `(-1)^(2R)=1`.  Every block is
cross-paired, so every nonempty joint character remains nonprincipal on both
source sides.  This is exactly the all-rank source identity in
`FFPS_SCALABLE_RICH_CORE_BLOCK_TOWER.md`, now ordered into degree bands; it
does not require or license a tensor product of already-squared currents.

## 2. Exact separate-square no-go at quadratic scale

Suppose band `j` supplies a quadratic inequality

\[
 |P|^2\le L_jE_j.
\tag{2.1}
\]

Multiplying `J` such statements gives only

\[
 |P|^{2J}\le\left(\prod_jL_j\right)\left(\prod_jE_j\right).
\tag{2.2}
\]

The homogeneous return to the native quadratic scale is

\[
 |P|^2\le
 \left(\prod_jL_j\right)^{1/J}
 \left(\prod_jE_j\right)^{1/J}.
\tag{2.3}
\]

So separate squares retain only the geometric-mean leverage.  If every
band has the same fixed contraction `L<1`, (2.3) still has coefficient `L`,
whereas the lawful single square has `L^J`.  Keeping the product coefficient
from (2.2) would require a genuine `2J`-th-moment theorem, not a quadratic
principal amplifier.

This homogeneity obstruction is reinforced by an exact Fourier witness.
Choose a character `chi_*` nonprincipal in the first two bands and put, on
`K`,

\[
 z(a)={p+t\chi_*(a)\over H}.
\tag{2.4}
\]

Then

\[
 H_1=p,\qquad H_{\chi_*}=t,
\]

and every band-pure nonprincipal transform is zero.  Every separately
marginalized band interferometer therefore sees `|p|^2`, independently of
`t`, while

\[
 \mathcal I_{\rm joint}=|p|^2-{|t|^2\over H-1}.
\tag{2.5}
\]

Thus bandwise quadratic data do not determine the lawful joint quadratic
object.  The replay verifies (2.4)--(2.5) over exact rationals for quotients
through order `32`.

This is a no-go for direct separate-square assembly.  It is not a no-go for
a new higher-moment amplifier or an exact arithmetic relation that controls
the missing mixed modes.

A sequential operator-norm proof is not a counterexample to this statement
if it retains the unsummed phase vector in every unprocessed band.  Such a
proof still acts on the full tensor and is algebraically the coherent joint
case of Section 1.  The no-go applies when a band is marginalized to its
scalar principal current and that scalar is squared before the other band
coordinates are introduced.

## 3. Exact varying-place conductor budget

Let block `i` use one selected place from each source side and set

\[
 s_i=\deg\ell_i+\deg\rho_i,
 \qquad T=\sum_{i=1}^Rs_i.
\tag{3.1}
\]

For distinct tame branch places, a nonempty mode `S` has maximally extended
rank-one conductor model

\[
 b_S=\sum_{i\in S}s_i-2.
\tag{3.2}
\]

Every block occurs in exactly `2^(R-1)` of the `H-1` selected modes.  Hence

\[
 \boxed{
 {1\over H-1}\sum_{S\ne\varnothing}b_S
 ={H\over2(H-1)}T-2.}
\tag{3.3}
\]

This is the optimistic modewise-maximal-extension average.  On the common
open deleting all selected branch places, every nonconstant line instead
pays `T-2`.  Filling inactive punctures separately is exactly the
maximal-extension operation that still needs a source-compatible boundary
identity.

In particular, if `D_max` is the largest selected place degree, then

\[
 \overline b_1\ge{D_{\max}\over2}-2.
\tag{3.4}
\]

The order-statistic theorem in
`FUNCTION_FIELD_CLOSED_PLACE_SUPPLY_TAX.md` says that for

\[
 R=\lfloor\alpha\log n\rfloor
\]

a density-one squarefree degree-`n` core selection has

\[
 D_{\max}\ge n^{\alpha/\delta-o(1)}.
\tag{3.5}

Partitioning those `R` places into bands cannot alter their maximum or their
sum.  Combining (3.3)--(3.5) with

\[
 L_{\rm joint}<(4/5)^R
 =n^{-\alpha\log(5/4)+o(1)}
\]

reproduces exactly the previous conductor threshold.  If a normalized trace
bound loses `D_max^theta`, a net formal gain still requires

\[
 \boxed{\theta<\delta\log(5/4).}
\tag{3.6}

Bounded rank per band has not improved this exponent.

There is also a simple scale explanation.  A degree shell `(D_{j-1},D_j]`
contains about `delta log(D_j/D_{j-1})` eligible factors of a random
squarefree core.  Supplying `b` factors in each of `J` shells therefore
needs total logarithmic degree span about `bJ/delta`.  Since `R=bJ`, the last
shell again lies at degree `exp(R/delta)`, namely `n^(alpha/delta)` when
`R=alpha log n`.

## 4. What remains genuinely open

The multiscale proposal is not useless; it identifies the necessary shape
of the next geometric theorem.  A successful construction must keep all
bands in one relative class and cancel common large-degree constituents
*before* either:

- decomposing into the `H-1` character modes;
- passing to modewise maximal extensions; or
- paying the common-open conductor `T-2`.

Proving estimates separately on bounded-rank band complexes cannot recover
the joint gain because it loses (0.2).  The relevant target is therefore a
cross-band relative pushforward or filtration whose associated graded
retains the mixed modes while cancelling their repeated boundary classes.
That possibility is not excluded by this packet and is now the sole
multiscale escape hatch at quadratic scale.

## 5. Proof ledger

Proved exactly:

- coherent sequential pre-square restriction equals one joint restriction;
- joint hard leverage is the product of band leverages;
- the band-pure and cross-band mode census (0.2);
- the separate-square homogeneity gate (2.2)--(2.3);
- the exact invisible mixed-character witness (2.4)--(2.5);
- the varying-degree selected-mode average (3.3);
- persistence of the supply-tax exponent under any band partition.

Imported with their stated scopes:

- the native all-rank rich-core source identity;
- the squarefree closed-place order-statistic theorem;
- the formal block leverage and rank-one tame open-curve formulas.

Not proved:

- a relative complex cancelling the large-degree branch constituents;
- transfer of the random-core supply law to the full weighted FFPS source;
- the signed varying-conductor estimate, principal individualization, RH,
  or GRH.

## 6. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_multiscale_single_square_gate.py --check
python -B -O research/l-families/atlas/function_field/ffps_multiscale_single_square_gate.py --check
python -B -m unittest tests.test_ffps_multiscale_single_square_gate
python -B -O -m unittest tests.test_ffps_multiscale_single_square_gate
```

The replay uses exact rational arithmetic, at most eight blocks, four bands,
and `256` quotient points.  It enumerates no source atom, polynomial,
closed place, curve, `L`-function, or zero.

## 7. Novelty boundary

Tensor restriction, Walsh orthogonality, and the binomial conductor average
are elementary.  The project contribution is the source-ordered trichotomy:
product gain with one square and all mixed modes; geometric-mean gain after
separate squares; or an as-yet-unbuilt relative joint complex.  No external
novelty or priority claim is made.
