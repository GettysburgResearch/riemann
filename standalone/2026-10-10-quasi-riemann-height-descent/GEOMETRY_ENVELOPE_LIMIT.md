# An exact limit of the existing geometric exponent certificate

**Status:** proved algebraic component, 10 October 2026. This is a limit of one specified sufficient exponent envelope, not a lower bound on the true zero-free constant and not a refutation of any stronger arithmetic estimate.

**Scope:** the September 30 balanced row-count function with the existing inverse/plain moment inputs, fixed plain parameter \(\kappa=3/4\), and the compensated geometry \(M+\ell=1\). The low-side formula considered here is the one valid for \(\ell\le1/5\), with the other length and contour conditions retained.

**Exact sources:** [the pinned manuscript](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex), labels "eq:target-cutoff", "eq:common-high-exponent", and "lem:balanced-endpoint"; the explicit geometric adapter in [GEOMETRY_PERTURBATION.md](GEOMETRY_PERTURBATION.md).

**What was run:** exact polynomial arithmetic in the quadratic field \(\mathbb Q(\sqrt{921})\), and rational enclosing intervals for the displayed decimal values, in "checks/check_research_algebra.py". A preliminary numerical search suggested the location; the proof below uses no grid, optimization output, or fitted inequality.

**Smallest missing gain for a larger improvement:** a better row-count bound at the actual simultaneous inverse/plain/prime-amplitude configuration, or a different physical probe. Varying the two geometric parameters while retaining the specified envelope cannot cross the bound below.

## 1. The envelope under consideration

Write

\[
l_x=\frac{1-\ell-b}{2},\qquad
l_y=\frac{1-\ell+b}{2},\qquad
h=\frac{1+3\ell+b}{2}.
\]

For the retained low estimate, the reference zero-free boundary is

\[
\beta_0=\frac{11}{12}-\frac{\ell}{4}.
\tag{1.1}
\]

Let \(0\le x\le1/2\), \(0\le\delta\le3/4\), and put

\[
D_x=3-\frac{17x}{9},\qquad
P_x=2-\frac{26x}{9}+\frac{8x^2}{9},
\]

\[
\mathcal J=(5/6-\delta)D_x+\delta P_x,\qquad
R_*=1-\delta+
\frac{(5/6-\delta)\delta P_x}{2\mathcal J}.
\tag{1.2}
\]

The high exponent relative to the reference low scale, at the outer moderate-row endpoint, is

\[
E_{\ell,b}(\delta,x)
=-\frac14+\frac{5\ell}{4}+\frac b6
+\delta\left(\frac12+\ell\right)+x\delta\ell
-\frac{1+3\ell+b}{2}(1-R_*).
\tag{1.3}
\]

An argument that closes by proving this specific envelope strictly negative on the whole rectangle must in particular make it negative at each point below. This is a statement about that uniform sufficient test; actual arithmetic rows need not realize every point of the rectangle.

## 2. A point where the geometric imbalance disappears

Set

\[
x_0=\frac12,\qquad
\delta_0=\frac{49-\sqrt{921}}{48}.
\tag{2.1}
\]

Since \(30<\sqrt{921}<31\), we have \(3/8<\delta_0<19/48<3/4\). This point is inside the required rectangle and strictly above the floor \(1/50\).

At \(x=1/2\),

\[
D_x=\frac{37}{18},\quad P_x=\frac79,\quad
\mathcal J=\frac{185-138\delta}{108}.
\]

Direct substitution shows

\[
R_*(\delta,1/2)-\frac23
=\frac{288\delta^2-588\delta+185}
       {3(185-138\delta)}.
\tag{2.2}
\]

The numerator vanishes exactly at \(\delta_0\). Its denominator is positive there. Therefore \(R_*(\delta_0,1/2)=2/3\).

Substituting this value in (1.3) cancels the coefficient of \(b\) identically:

\[
E_{\ell,b}(\delta_0,1/2)
=-\frac5{12}+\frac{\delta_0}{2}
+\ell\left(\frac34+\frac{3\delta_0}{2}\right).
\tag{2.3}
\]

The multiplier of \(\ell\) is positive. Hence strict negativity of the full envelope requires

\[
\ell<
\frac{5-6\delta_0}{9+18\delta_0}
=\frac{8\sqrt{921}+33}{1653}.
\tag{2.4}
\]

Combining (2.4) with (1.1) gives the necessary condition

\[
\boxed{\quad
\beta_0>
\frac{1507-2\sqrt{921}}{1653}
=0.874957067\ldots .
\quad}
\tag{2.5}
\]

This is the promised exact algebraic limit. It already holds before any additional Gram, slot-supply, or contour constraints are imposed. Adding those constraints cannot make this same sufficient envelope pass at a smaller boundary.

## 3. What this says about further research

The small rational perturbation in the companion proof lies safely above (2.5). It is a legitimate place to test the adapter and to make a modest derived improvement. There is no route to a substantially smaller constant simply by repeatedly refining these two geometric parameters while keeping (1.2)–(1.3).

The point exposing the limit is also informative. In the manuscript's notation \(q=x\delta\), so \(x_0=1/2\) is the upper prime-amplitude boundary. The row-count estimate permits that amplitude to coexist with the inverse/plain witness whose balanced count is \(R_*=2/3\). Separate marginal estimates retain this possibility. A bound for the actual simultaneous source might reduce its count, or show that the extreme amplitude cannot coexist with the relevant witness.

That is a specific reason to pursue a joint source estimate. It does not assume the needed incompatibility. The [native height note](NATIVE_HEIGHT.md) preserves the full divisor-product coefficient before estimating it; the [higher-moment note](UPSTREAM_HEIGHT_AND_MOMENTS.md) identifies the corresponding restricted convolution in the sextic family. Neither note supplies the missing improved count at this corner.

For scale, changing the low parameter all the way to \(\ell=1/5\) would target \(13/15\) before checking the high estimate. At (2.1), its uncompensated high exponent is exactly

\[
\left(\frac15-\frac{8\sqrt{921}+33}{1653}\right)
\left(\frac34+\frac{3\delta_0}{2}\right)>0.
\]

The current row bound would have to gain that quantity divided by \(h\) in its exponent merely to remove this one obstruction. Other points still need checking. The stronger conditional fourth-moment target \(17/24\) uses a different extraction route and is not subject to this particular geometry formula.
