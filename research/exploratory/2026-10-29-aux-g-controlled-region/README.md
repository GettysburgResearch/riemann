# Joint original-gcd, divisor and auxiliary-gcd control

**Status.** Historical/localized comparison of source-qualified bounds in [the growing-k theta aggregation](../2026-10-29-low-dual-theta-bound.md), [the auxiliary-g large-sieve calculation](../2026-10-29-sparse-dilation-theta-target.md), and [the dual-correlation generic bound](../2026-10-29-61-72-dual-correlation/README.md). A later [second-Poisson divisor aggregation](../2026-10-29-second-poisson-aggregate.md), conditional on its source replay and paper 5's inverse input (10.2), supersedes the all-g conclusion below and controls every feasible κ,g already for `d≥1/5`. This note's localized polytope compares weaker inputs and does not describe the strongest currently available source-qualified union. Their Poisson, fixed-sector/phase, common-profile and analytic source inputs remain imported. The new sparse estimate (A) is not assumed. No full inverse moment or individual zero-free region follows.

Set `P=Y^(6/5)` and localize `Nd≈Y^d`, `Nk≈Y^κ`, `Ng≈Y^g`. Ignore fixed-power margins and allow `Y^ε` losses. A nonempty top dual scale has

    0≤d≤6/5,  0≤κ≤d,  κ≥2d−7/5,  0≤g≤6/5−d.                   (1)

The inequalities come respectively from `Nd≤P`, `k|d`, `H₀=P²K/(Y D₀²)≥1`, and the nonempty residual column length `D=P/(D₀G)≥1`. The inequalities describe necessary scale constraints, not an assertion that every boundary dyad contains actual ideals.

There are three relevant O(Y^(1+ε)) criteria:

* **Full theta aggregation:** `d≥1/5+κ`, with the masks, source angular order and shared decomposition exactly as in the low-dual note. This holds for every g and uses paper 5's first averaged theta bound.
* **Unlocalized generic source:** for `11/35≤d≤12/35`, `κ≥11/5−6d`; for `12/35≤d≤7/10`, `κ≥7/25−2d/5`; for `d≥7/10`, every admissible κ. It holds for every g. No κ is controlled by this criterion below d=11/35.
* **g-localized sextic sieve:** `d≥1/5` and

      g ≥ max{0, 7/30−d/3−5κ/6,
                    11/10−3d−κ/2,
                    8/25−3d/5−4κ/5}.                         (2)

The third criterion is obtained by applying the unrestricted-row sextic large sieve to each g,k, then bounding every smaller frequency dyad by the top scale H₀. It retains the g localization and does not prove the open sparse incidence estimate.

## Exact union in the only remaining wedge

Combining the first two criteria already controls all admissible κ and g for `d≥12/35`. For `d<1/5` none of these displayed top-scale criteria proves a Y-sized bound. In the intermediate strip `1/5≤d<12/35`, the first two leave precisely

    d−1/5 < κ < min{d, 11/5−6d},                              (3)

with upper equality allowed when the upper endpoint is d and `d<11/35`, since generic control then does not apply. At `d=11/35`, the endpoint κ=d is already generically controlled. In this wedge the second nonzero lower bound in (2) dominates the other two. Indeed using `κ≥d−1/5`,

    (11/10−3d−κ/2) − (7/30−d/3−5κ/6)
       ≥ 4/5−7d/3 ≥0,
    (11/10−3d−κ/2) − (8/25−3d/5−4κ/5)
       ≥ 18/25−21d/10 ≥0.                                    (4)

The last inequalities hold exactly up to d=12/35. The active lower bound is positive in the open wedge: when its upper endpoint is d, positivity follows from d≤11/35; when the upper endpoint is `11/5−6d`, the bound vanishes exactly there. Thus the **complete controlled union of these three displayed criteria** in (3) is simply

    g ≥ 11/10−3d−κ/2.                                         (5)

This is a sufficient source-qualified bound and an exact description of the listed scalar criteria, not a lower bound on the actual arithmetic expression or an impossibility theorem for other arguments.

For any fixed auxiliary exponent `0≤g≤1/2`, (5), the full theta aggregation and the generic branch together control **every admissible κ** once

    d ≥ (12−10g)/35.                                          (6)

For `g≥1/2`, they control every admissible κ once `d≥1/5`. Equivalently, within (1) the threshold is `max{1/5,(12−10g)/35}`. It is sharp for this scalar union: below it and above 1/5, take κ just above d−1/5, still below the generic threshold, so (5) fails. At g=0 the all-κ threshold is the previous 12/35; at g=1/10 it improves to 11/35; at g=1/4 it improves to 19/70; at g=1/2 it reaches 1/5. Equality lines are understood with small parameter slack when source losses are present.

For a **fixed** (d,κ) in the wedge, the old sufficient condition `K G²≥Y` requires `g≥(1−κ)/2`; the exact stronger threshold (5) saves

    (1−κ)/2 − (11/10−3d−κ/2) = 3(d−1/5).                  (7)

The gain is strict for d>1/5, independent of κ. For example `(d,κ)=(1/4,1/10)` needs g≥3/10 instead of g≥9/20. The bound `G≥D`, from the other elementary sparse-sieve regime, is weaker than (5) throughout this wedge.

## Are small auxiliary gcds excluded?

No lower bound on g follows from the scale constraints (1). In particular the divisor g=(1) occurs in the auxiliary Möbius projector, and g=0 is compatible with every interior admissible pair (d,κ) for which the other source ranges are nonempty. A large-g estimate cannot be promoted to the entire g-sum without independently controlling its small-g complement. The criterion (5) really is a limitation of the present proof when it demands positive g; it does not say the underlying signed sum is large. Summing O(log Y) g-dyads costs only Y^ε after every dyad is controlled.

The physical low-dual source calculation is restricted to the long residual-column range d≤7/10; for d≥7/10 the separate generic source criterion controls all κ and g. Fixed S factors and the excluded principal pair require the same separate handling as in the linked notes.

## Second-Poisson localized refinement

The source-qualified [second-Poisson calculation](../2026-10-29-second-poisson-g-bound.md) supplies a fourth criterion, retaining the common multiplicative χ_n(k)^5 coefficient, its zero masks, source phase/fibre replay and common-profile hypotheses. In the wedge (3), it suffices that

    g ≥ max{0, 11/30−d−κ/6, 7/10−d−5κ/2,
                 2/5−d−2κ/5}.                                  (8)

Combining it with (5), the two localized criteria control exactly their scalar union

    g ≥ min{11/10−3d−κ/2,
             max{0, 11/30−d−κ/6, 7/10−d−5κ/2,
                        2/5−d−2κ/5}}.                           (9)

This strictly enlarges the controlled interior for some feasible points: at `(d,κ)=(1/4,1/10)`, (5) requires g≥3/10 whereas (8) requires only g≥1/5. The scales permit this example: `0≤κ≤d`, `g≤6/5−d`, and the top dual exponent is positive. This is an improvement to a localized sufficient region, not a claim that a given dyad contains rows or that a zero-free region follows.

In fact, throughout the wedge the old threshold (5) is at least each affine term in (8): the three differences are nonnegative at the wedge closure's four vertices `(1/5,0)`, `(1/5,1/5)`, `(11/35,11/35)`, and `(12/35,1/7)`, and each difference is affine. The new terms all meet at κ=1/7, independently of d. Thus (9) simplifies to the following **complete scalar union**, conditional on the second-Poisson replay:

    g ≥ max{0, 7/10−d−5κ/2}      when κ≤1/7,
    g ≥ max{0, 11/30−d−κ/6}      when κ≥1/7.                (10)

At κ=1/7 both displayed values coincide with the third term of (8). In replaying the second Poisson step for a fixed original k, its growing-conductor factor `χ_n(k)^5` must remain inside the arbitrary common column coefficients. The new Poisson frequency is then summed at scale R₀; it would be incorrect to enlarge that frequency scale by K and retain the exponents of (8).

The fixed-g **all-κ threshold** (6) is unchanged by this refinement. Both the old threshold in (5) and each of the three affine thresholds in (8) are nonincreasing in κ. At the boundary κ=d−1/5, the middle threshold in (8) equals the old threshold:

    7/10−d−(5/2)(d−1/5) = 6/5−7d/2
                             = 11/10−3d−(d−1/5)/2.

Thus their minimum, maximized over the residual κ wedge, reaches `6/5−7d/2` as κ↓d−1/5, exactly the old worst value. After including the always-required d≥1/5, this reproduces `max{1/5,(12−10g)/35}` for **this restricted collection of bounds**. The unit auxiliary ideal g=1 remains admissible, so that restricted union has all-g, all-κ threshold d=12/35. The later second-Poisson aggregation named in the status improves that source-qualified threshold to d=1/5 by using paper 5 (10.2); it does not follow from the scalar bounds optimized here. These are exact statements about the specified sufficient inequalities under the scale relaxation; the second-Poisson source replay is conditional and no arithmetic lower bound is claimed.

[check_polytope.py](check_polytope.py) verifies the affine identities, wedge-vertex domination and threshold arithmetic exactly. An independent review reproduced the second-Poisson exponent simplification and the fixed-k coefficient requirement. It does not establish the imported analytic identities or the full inverse moment.
