# A quantitative covariance bound after exact support pruning

**Status:** proposed source-conditional component theorem. This note combines
two existing proved formulas in a new order: it deletes complete vanishing
divisor groups, then bounds the covariance of all remaining groups on the
specified good standard cusp face. It obtains a factor of order
`sqrt(B)` in one long-frequency term when `A` is at least `sqrt(B)`.
This selected-face theorem is not by itself a whole-object covariance
bound. The companion
[ALL_CUSP_COEFFICIENT_ADAPTER.md](ALL_CUSP_COEFFICIENT_ADAPTER.md),
Section 5, supplies the additional coefficient identities that extend
it to the full source completion and give a quantitative improvement
on short row ranges. Neither result enlarges the existing admissible
row range at the balanced `D^2` target, proves a new sector of the
original fourth moment, or proves a new zero-free region.

**Authorship:** scale_covariance_attack. An independent review, if supplied,
must bind the final contents separately.

**Exact dependencies.** The arithmetic and analytic conventions are those of
PR #915 at `9959364671f89b86f3992ec5ed5e19f804eb607b`,
`standalone/2026-10-10-sextic-critical-core/COUPLED_THETA_COMPLETION.md`,
Sections 1--6. Its Theorem 6.2 is used only on its stated good standard
infinity-cusp face. The exact support input is PR #920's mathematical
source commit `6aceafc1729ca0962eb12519b407b69c3b5a4d5f`,
`standalone/2026-10-10-theta-support-descent/RAMANUJAN_SUPPORT_PRUNING.md`,
Theorem 3.1, with its complete projected sum and its literal zero masks.
The source's opposite-derivative theta transformation and cusp expansion
remain analytic inputs; this note does not independently reprove them.
For the comparison in Section 4, the squarefree sextic large sieve is
used in exactly the form stated in PR #913,
`REFINED_ALL_ROW_SIEVE.md`, equation (1.1).

The signed-average discussion uses PR #919 at
`9b04a887e171b3104a66cf57296ce5b0b2920d78`,
`standalone/2026-10-10-averaged-conductor-frontier/SMALL_GCD_CONDUCTOR_REDUCTION.md`,
equations (2.6a) and (2.9). No statement from another changing branch is
silently substituted for these sources.

## 1. The exact completed face

Keep the Eisenstein field, chosen primary generators, fixed bad set `S`,
fixed finite ray data, and fixed compact smooth weights of the two
sources. Write `Na` for the ideal norm. The rows `k` below are squarefree,
outside `S`, and satisfy

\[
H\le Nk<2H,\qquad H\ge1.
\tag{1.1}
\]

All scales are bounded above by a fixed power of an auxiliary parameter
`D >= 2`. Constants may depend on that power, the fixed ray data and
smooth seminorms. Every positive exponent loss may be reassigned a
smaller preliminary value when logarithms are absorbed.

Let `J_{k,a,d}(B)` be exactly the complete double sum denoted
`I_{k,a,d}(B)` in the support source, equation (2.1). It includes the
whole squarefree theta index and the whole unrestricted cube index.
With `a = dg`, the selected first-reflection standard face is

\[
\mathcal F_{A,B}(k)=
\frac1{\sqrt A}
\sum_a^*\frac{\eta(a)\overline{\alpha(a)}^3\chi_k(a)^3}
                 {\sqrt{Na}}
 W_1(Na/A)
\sum_{dg=a}\mu_K(g)Nd\,J_{k,a,d}(B).
\tag{1.2}
\]

The fixed overall scalar from that source can be included; it changes
only the fixed constant in the inequalities below. Finite sums of the
permitted fixed standard-face ray branches are also allowed. Primes of
`a` and `k` that overlap produce the original zero and are retained as
such. No extra condition between `g` and the theta index is imposed.

For this paragraph alone, any row-independent factor `v(a)` can multiply
the outer coefficient in (1.2). The identity below is pointwise and
preserves it without a size restriction. For the quantitative bounds,
require the source's subpower bound

\[
|v(a)|\ll_\delta D^\delta
\quad\text{for every }\delta>0
\tag{1.3}
\]

on the polynomially bounded support. This is the bounded coefficient
extension justified in PR #915, not a claim that an arbitrary outer
coefficient preserves a new Euler product.

The support source supplies a fixed constant `C_S` such that

\[
Ng>C_S\sqrt B
\quad\Longrightarrow\quad J_{k,a,d}(B)=0.
\tag{1.4}
\]

This zero holds before the `e,f` subdivision of `d`, before theta norm
dyads, and before any absolute-value estimate. Therefore (1.2) is
unchanged by inserting `1_{Ng <= C_S sqrt(B)}`. In particular, in the
sesquilinear expansion of its row norm every term with a complete
vanishing group on either side is zero. This assertion includes cross
terms between different `a,d,g` labels; it does not need orthogonality
of their nonzero values.

It would be false to infer that each summand of a prematurely expanded
`e,f` or theta-dyad decomposition separately vanishes. The deletion in
(1.4) is performed on the exact complete group, and only its remaining
part is subsequently decomposed.

## 2. A bound for the entire surviving standard face

Put

\[
G_* = \min(A,\sqrt B).
\tag{2.1}
\]

Replacing either argument in this minimum by a fixed positive multiple
only changes the constant below, because the outer support has
`Na` comparable to `A`. Every bounded nonempty scale may be placed in
a fixed unit annulus.

### Theorem 2.1

For the exact object (1.2), including any multiplier satisfying (1.3),

\[
\boxed{
\sum_{k\sim H}^{*}|\mathcal F_{A,B}(k)|^2
\ll_\epsilon D^\epsilon
\left[
HA+\frac{H^2 A G_*}{B}
 +\left(\frac{H^2A^2}{B}\right)^{2/3}
\right].
}
\tag{2.2}
\]

The sum contains all interference between the surviving divisor
allocations on this selected face. It is not a sum of the energies of
individual allocations with their cross terms omitted.

### Proof

First apply the pointwise identity (1.4). Next expand, for each surviving
`d`, the exact divisor projection

\[
\mathbf1_{d\mid nb}
=\sum_{ef=d}\mathbf1_{e\mid n}\mathbf1_{f\mid b}
                         \mathbf1_{(f,n)=1}.
\tag{2.3}
\]

This restores precisely the original `a = efg` allocation and its zero
masks. The remaining ideals are squarefree and pairwise coprime. In
particular, the negative label `g` is not required to be coprime to the
reindexed squarefree or cube theta index.

Partition `Ne`, `Nf`, `Ng` into dyadic annuli `E`, `F`, `G`.
On every nonempty block,

\[
EFG\asymp A,\qquad G\ll G_*,\qquad E,F,G\gg1.
\tag{2.4}
\]

A block meeting the exact cutoff may have a partial restriction on its
`g` values. This causes no new regularity assumption: Theorem 6.2 of
the source freezes `f,g` before its quadratic--cubic composition.
Restricting the set of those frozen labels leaves its bound valid.
Likewise, after `f,g` are fixed, `v(efg)` is a permitted bounded
coefficient on its `e` axis, after rescaling by (1.3). No derivative of
this coefficient is used.

For this block that theorem gives

\[
\sum_{k\sim H}^*
 |\mathcal F_{E,F,G}(k)|^2
\ll D^{\epsilon_0}
\left[HE+Y+(EY)^{2/3}\right],
\qquad
Y=\frac{H^2EG^2}{BF}.
\tag{2.5}
\]

It already includes the full cube and squarefree-index sums after
their legitimate norm localization, including smooth tails. Substitute
`E` comparable to `A/(FG)`. The three terms are bounded respectively by

\[
HE\ll HA,
\qquad
Y\ll\frac{H^2AG}{BF^2}
\ll\frac{H^2AG_*}{B},
\tag{2.6}
\]

and

\[
(EY)^{2/3}
\ll\left(\frac{H^2A^2}{BF^3}\right)^{2/3}
\ll\left(\frac{H^2A^2}{B}\right)^{2/3}.
\tag{2.7}
\]

There are at most a fixed power of `log(2D)` many `E,F,G` blocks.
Minkowski in the row Hilbert space bounds the norm of their actual sum
by the sum of their norms. Equivalently, Cauchy bounds its squared norm
by the number of blocks times the sum of block squared norms. This
retains and controls all cross terms, at only a fixed logarithmic
cost. Choose `epsilon_0` small enough to absorb that cost and the
coefficient rescaling into `D^epsilon`. Equations (2.6)--(2.7) prove
(2.2). The finitely many permitted fixed-ray branches are handled by
the same Hilbert-space inequality. \(\square\)

### A window refinement

Suppose a portion of the surviving sum is restricted to
`G_0 <= Ng <= G_1`, with `1 <= G_0 <= G_1` and
`G_1 <= C G_*`. The same proof gives

\[
\boxed{
\sum_{k\sim H}^{*}|\mathcal F_{[G_0,G_1]}(k)|^2
\ll D^\epsilon
\left[
\frac{HA}{G_0}+\frac{H^2AG_1}{B}
 +\left(\frac{H^2A^2}{B}\right)^{2/3}
\right].
}
\tag{2.8}
\]

Here the window acts on complete groups before decomposition. More
generally an arbitrary bounded multiplier on their `g` label is
permitted. The stronger first term follows from
`E << A/(F G_0)`; the other terms are unchanged.

For two such windows, their actual covariance in the same row Hilbert
space is at most the geometric mean of the two right sides of (2.8).
This is Cauchy--Schwarz with the literal row weights and phases. It
asserts a bound on that covariance, not orthogonality of the windows.

## 3. Balanced scales and the precise gain

At `A = B = D`, equation (2.2) becomes

\[
\boxed{
\sum_{k\sim H}^{*}|\mathcal F_{D,D}(k)|^2
\ll D^\epsilon
\left[HD+H^2D^{1/2}+H^{4/3}D^{2/3}\right].
}
\tag{3.1}
\]

In particular the entire specified reflected face is bounded by
`D^(2+epsilon)` for `1 <= H <= D^(3/4)`.
Using the same source block theorem without the exact support pruning
only bounds `G` by `A`; its resulting complete-face envelope is

\[
D^\epsilon
\left[HD+H^2D+H^{4/3}D^{2/3}\right],
\tag{3.2}
\]

which reaches `D^(2+epsilon)` only through `H <= D^(1/2)`.
Thus the new result improves a complete projected-face bound, not just
the estimate for the already vanishing all-negative component.

On a fixed dyadic scale interval, the corresponding averaged estimate
follows immediately by integrating (3.1). For example, if
`H(D) = D^r` with fixed `r >= 0`, then

\[
\int_X^{2X}
\sum_{k\sim D^r}^{*}|\mathcal F_{D,D}(k)|^2\frac{dD}{D}
\ll X^\epsilon
\left[X^{r+1}+X^{2r+1/2}+X^{4r/3+2/3}\right].
\tag{3.3}
\]

The variation in the row annulus creates no problem because the
pointwise estimate holds at each scale. The measure of the dyadic
interval is `log(2)`. This corollary supplies no further saving from
scale integration.

At the actual difficult fourth-moment dual range
`H = D^(3-theta)`, the term `H^2 D^(1/2)` has exponent
`13/2 - 2 theta`. Its decrease by `1/2` from (3.2) is real,
but its size is still far beyond the needed covariance estimate.

## 4. Compare the correct whole-object bound before interpreting the gain

The physical balanced completion, before restricting to a reflected
cusp face, already satisfies a stronger classical estimate in a short
row range:

\[
\sum_{k\sim H}^{*}|\mathcal C_{A,B}(k)|^2
\ll D^\epsilon
\left[H+AB+(HAB)^{2/3}\right].
\tag{4.1}
\]

For completeness, expand its physical cube index `b`. For fixed `b`,
the remaining normalized squarefree product polynomial has physical
length `L_b` comparable to `AB/(Nb)^3`, coefficient squared mass
`O(D^epsilon L_b)`, and an exact exterior coefficient of modulus at
most `1/Nb`. Every moving coprimality condition remains in its
row-independent column coefficients. The squarefree sextic sieve
bounds that normalized polynomial by

\[
D^\epsilon\left[H+L_b+(HL_b)^{2/3}\right].
\tag{4.2}
\]

Apply Minkowski in the row norm. The three resulting cube sums are
bounded respectively by

\[
\sqrt H\sum_{Nb\ll B^{1/3}}\frac1{Nb},\qquad
\sqrt{AB}\sum_b(Nb)^{-5/2},\qquad
(HAB)^{1/3}\sum_b(Nb)^{-2}.
\tag{4.3}
\]

The first is logarithmic and the other two converge. Squaring proves
(4.1), with bounded nonempty scales included using the fixed supports.
This is the squarefree-row version of the existing physical expansion
used in PR #918, `INTERFACE_COMPARISON.md`, Corollary 3.3. No reflected
analytic estimate is needed for it.

For `A = B = D`, (4.1) gives `D^(2+epsilon)` throughout
`H <= D`. It is a bound for a different, complete object whose reflected
faces can interfere. Consequently (3.1) must not be advertised as an
extension of the full physical object's admissible row range. It is
useful information about one specified reflected part and the signs
that must be preserved to control it. The sharper physical envelope
and the new component estimate can coexist without either component
being nonnegative in the full reflected decomposition.

The full original moment additionally requires all row valuations,
the moving auxiliary and exclusion families of the A2 projection,
and the exact centered covariance after removing cube completion.
None of those interfaces is removed by Theorem 2.1.

## 5. The signed scale average cannot erase an unbounded positive norm

The pinned PR #919 remainder `S_h(D)` is real and satisfies

\[
\mathcal N(D)=S_h(D)+E(D)\ge0,
\qquad |E(D)|\ll_\epsilon D^{h+2+\epsilon},
\tag{5.1}
\]

where `N(D)` is the exact smooth norm of its small-gcd residual
polynomial. In particular,

\[
S_h(D)\ge -C_\epsilon D^{h+2+\epsilon}.
\tag{5.2}
\]

For any real `x >= -b`, with `b >= 0`, one has
`|x| <= x + 2b`. Thus a bound of target size for the signed dyadic
integral is, at the exponent level, equivalent to the same bound for
its absolute-value integral:

\[
\int_X^{2X}|S_h(D)|\frac{dD}{D}
\le\int_X^{2X}S_h(D)\frac{dD}{D}
 +O_\epsilon(X^{h+2+\epsilon}).
\tag{5.3}
\]

The reverse inequality with the absolute value is immediate. If a
nonnegative excess `e` is allowed, the same statement holds with
`X^(h+2+e+epsilon)`, since the error in (5.3) is smaller.
This is a consequence already implicit in the source's lower bound;
it is recorded here to constrain the attempted combination.

The scale-averaged criterion is still weaker than a pointwise one:
it permits concentration on narrow intervals of `D`. But in its
actual signed remainder, large positive mass cannot be cancelled by
negative mass of an equally unbounded power. A new estimate must
control the residual norm itself, or its integral, through genuine
coefficient cancellation inside that norm. Neither the finite number
of bad-ray characters nor the bounded logarithmic length of the scale
interval produces such an estimate by orthogonality alone.

## 6. Scope of the completed attack

The new proved consequence is (2.2), with the window refinement (2.8):
complete support zeros remove high `g` groups before norms, and this
shrinks the long-frequency contribution of the entire surviving good
standard face. All covariance among those surviving groups is bounded
using the original large-sieve theorem and logarithmic block summation.

The attempted combination does not yield the signed small-gcd,
large-conductor average required by PR #919. It does not identify the
possible `v = 1` residue in PR #920 with a favorable moment diagonal,
and it does not replace the post-reflection sextic row by a quadratic
one. Those would be additional mathematical claims requiring their
own identities and estimates. No full fourth moment, cofinal moment
hierarchy, `17/24` boundary, or RH result is asserted here.
