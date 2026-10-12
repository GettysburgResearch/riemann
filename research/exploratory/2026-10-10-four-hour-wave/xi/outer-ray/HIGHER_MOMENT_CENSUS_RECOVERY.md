# Higher complete moments give count-free census exclusion predicates

Status: proposed conditional analytic continuation of the count-free theorem.
Scope: a complete even source product in a known strip, an authenticated
positive Fourier source, finitely many actual sign changes, and a native
complete logarithmic moment. No new native jet above degree six or new
finite height is certified here.
Exact dependencies: [THEOREM.md](THEOREM.md) and the zero-free-disk and
one-occurrence selection proofs (CF1)--(CF8) in
[COUNT_FREE_CENSUS_RECOVERY.md](COUNT_FREE_CENSUS_RECOVERY.md).
What was actually run: no new higher-degree primitive computation. The
already separate degree-six packet provides the case `k=3`; the other cases
below are analytic predicates for future directed calculations.
Smallest remaining gap: authenticate sufficiently narrow sign intervals and
a higher-degree native logarithmic coefficient, then pass the displayed
strict exclusion inequality. The formulas do not supply that computation.

## 1. General source theorem

Let `F(0)>0` be an even real entire function of order strictly less than two,
with its complete constant-times-genus-zero-in-`z^2` zero product. Assume
every zero lies in `|Im rho|<=A`, where `A>=0`, and assume the exact positive
Fourier representation

\[
 F(z)=\int_0^\infty\cos(zu)\,d\mu(u),\qquad d\mu\ge0,
\tag{HM1}
\]

with all exponential moments finite. Choose `B>A` such that
`F(-iB)<2F(0)`. The cosine expansion from (CF2) proves `F` zero-free on
`|z|<=B`. Consequently every zero satisfies
`|Re rho|>sqrt(B^2-A^2)`. Choose a real `R0>0` with

\[
 R_0\le\sqrt{B^2-A^2},\qquad
 2k\arctan(A/R_0)<\pi/2,
 \qquad c_k=\cos(2k\arctan(A/R_0))>0,
\tag{HM2}
\]

for a fixed positive integer `k`.

From disjoint positive real intervals with actual strict opposite `F`
endpoint signs, choose exactly one zero occurrence `gamma_j` in each.
For actual Xi, authenticated Hardy-Z sign changes supply these intervals.
Their original multiplicity or completeness is not assumed. Remove the
selected reflected negative occurrences too, and retain every other source
zero with its remaining nonnegative integer multiplicity. Define

\[
 T_k=-k[z^{2k}]\log\frac{F(z)}{F(0)}-\sum_j\gamma_j^{-2k}.
\tag{HM3}
\]

The complete product and its normally convergent logarithmic power series
near zero give

\[
 T_k=\sum_{\text{remaining}\operatorname{Re}\rho>0}
       m_\rho\rho^{-2k}
 \ge c_k\sum_{\text{remaining}\operatorname{Re}\rho>0}
       m_\rho|\rho|^{-2k}\ge0.
\tag{HM4}
\]

The inequality is an inequality of real quantities: complete conjugate
pairs make the complex sum real, and each individual summand has real part
at least `c_k |rho|^(-2k)` by the acute-angle condition in (HM2).
Absolute convergence allows passage from finite complete blocks. Removing
one real occurrence leaves all extra multiplicities nonnegative. Neither
an unknown conjugate pair nor an unselected real occurrence can cancel
another source contribution in (HM4).

Let a valid directed enclosure give `T_k<=U_k`. If a proposed finite height
`H>0` satisfies

\[
 U_k(H^2+A^2)^k<c_k,
\tag{HM5}
\]

there is no remaining source zero with `|Re rho|<=H`: its positive-half-plane
occurrence would alone contribute at least `c_k/(H^2+A^2)^k` to (HM4).
Thus all source zeros there are selected and real, and all selected zeros
there are simple. As in (CF9), keeping every selected interval away from
the boundary gives a literal complete simple finite list. This reasoning
does not use a zero-count routine or its historical contracts.

## 2. Eight acute actual-Xi moment orders from the same source disk

For actual Xi, (CF1)--(CF5) provide `B=11/2`, `A=1/2`, and zero-free disk
radius `11/2` from the native seed `Xi(0)>99/200`. Take `R0=27/5<sqrt(30)`.
For each integer `1<=k<=8`, the elementary bound `atan x<x` gives

\[
 2k\arctan(5/54)<\frac{40}{27}<\frac32<\frac\pi2.
\tag{HM6}
\]

Here `pi>3` is the elementary inscribed-hexagon bound. Therefore (HM2)--(HM5)
are valid for all eight moment orders. For rational `R0,A`, the projection
constants are exact rational numbers:

\[
 c_k=\frac{\displaystyle\sum_{j=0}^k(-1)^j
       {2k\choose2j}R_0^{2k-2j}A^{2j}}
       {(R_0^2+A^2)^k}.
\tag{HM7}
\]

This is the real part of `(R0-iA)^(2k)/(R0^2+A^2)^k`. The strict angle
bound, rather than a bare positive numerical cosine, justifies the
monotone projection needed in (HM4). No positivity for arbitrarily high
moment orders is asserted. In particular a complete strip alone does not
keep all powers of an unknown nonreal zero in an acute sector.

For any newly authenticated Xi height satisfying (HM5), the existing
finite-census column theorem gives its full closed lower companion column,
with all `lambda>0`, integer `r` such that `H-(r+2)/2>0`, and horizontal
range `|T|<H-(r+2)/2`. This is an application to the recovered census,
not a claim that any uncomputed higher moment has passed (HM5).

## 3. Root-width and native-coefficient budgets remain explicit

Suppose a directed native coefficient encloses
`C_k=-k[z^(2k)]log(F/F(0))` by `[Clo,Chi]`, and each chosen source zero lies
in an authenticated positive interval `[l_j,u_j]`. Monotonicity supplies
the full selected-root enclosure

\[
 T_k\in\left[
 C_{\rm lo}-\sum_j l_j^{-2k},\quad
 C_{\rm hi}-\sum_j u_j^{-2k}\right].
\tag{HM8}
\]

Its width is the native coefficient width plus the complete finite interval
width

\[
 D_k=\sum_j(l_j^{-2k}-u_j^{-2k})
 \le2k\sum_j(u_j-l_j)l_j^{-(2k+1)}.
\tag{HM9}
\]

The final inequality follows by integrating the decreasing positive
derivative magnitude `2k x^(-2k-1)` across each interval. Directed arithmetic
must preserve the displayed endpoints when it evaluates (HM8); ordinary
root midpoints do not authenticate this enclosure. Formula (HM9) gives an
explicit way to decide which low intervals need refinement and how narrow
their widths must be before spending effort on a higher-degree native jet.
Producer candidates still require actual strict sign replay. A small fitted
moment or an enclosure that ignores any interval width cannot pass (HM5).

The finite predicate only needs a valid upper bound in (HM5); mathematical
positivity comes from (HM4). No Gaussian artificial-pair parameter family or
companion sector sampling is part of this count-free census mechanism.
