# A common moving unitary twist in the FHL density bound

**Status.** This is a proposed source-qualified deduction from de Faveri's printed Θₙ sieve, the fixed-field Hecke analytic estimates and the buffered detector proof below. The recent source theorem and FHL local assertions are not independently proved here. It is a family zero-density bound, not an individual zero-free strip; no exhaustive priority claim is made.

Fix n≥4, a number field K containing μₙ, fixed FHL family data and a fixed admissible set S. Let χ_u be the original zero-extended FHL character at a good n-free label `Nu≤X`. Assume its primitive conductor and its good deleted radical are `≪Nu`, and that the good tame inertia character of χ_u at p is the `v_p(u)`-th power of a fixed local order-n character. Let ν=ν_X be **one common unitary Hecke character**, allowed to vary with X, whose finite conductor has norm `≤X^κ` and whose archimedean parameters lie in one fixed compact set. Use ν's primitive ideal presentation, extended by zero exactly at primes dividing its conductor; arbitrary additional deleted primes are not included unless their radical is separately bounded. No condition of coprimality between fν and u is imposed. The set S and all FHL choices stay fixed as X varies.

For fixed `1/2+1/n<σ<1`, put `δ=2σ−1`, `h=1−δ`. In the middle range `2/n<δ<1−1/n`, put

    t=3(n−3)/[n(3−δ)−7],
    R=2/n+(1−1/n−δ)t,   E(κ)=max{R,f(1+κ)}.                   (1)

In the high range `1−1/n<δ<1`, put

    t=10/(4+nh),   R=ht,   E(κ)=max{R,2h(1+κ)}.               (2)

Under the named source and standard fixed-field Hecke inputs, for every ε>0 there is τ>0 such that, **uniformly in every such common ν**,

    Σ_{u good, n-free; Nu≤X} N(σ,X^τ;(νχ_u)^*)
      ≪_{K,S,n,σ,κ,ε,arch-compact} X^(E(κ)+ε).                (3)

The star denotes the primitive inducing unitary Hecke character, and zeros are counted with multiplicity. Any fixed κ≥0 is permitted; the estimate is informative when E(κ)<1. The unchanged middle-range exponent R is obtained if κ≤t−1; the unchanged high-range exponent R is obtained if κ≤t/2−1. At the joining point δ=1−1/n, κ=0 and exponent 2/n follow by approaching from the middle range and absorbing a fixed small loss. No claim is made here for positive κ at that boundary.

For example, at n=4 and σ=4/5, `t=15/13`, `R=35/52`, and the middle range permits every fixed `κ<2/13`. The common twist can vary over all unitary Hecke characters satisfying the stated conductor and archimedean bounds, not merely powers of one fixed character.

## Uniform detector for the moving twist

The conductor of the primitive character inducing νχ_u divides the product of the two conductors, so its norm is `≪X^(1+κ)`. The original product presentation retains the χ_u zero mask and the ν conductor zeros. At a prime where those local characters cancel on inertia, the primitive inducing character may be unramified even though the original product still vanishes there. Thus its additional deleted Euler factors must be retained; their radical is supported on the union of the χ_u and ν presentation supports and has norm `≪X^(1+κ)`. These statements hold even when the two conductors share primes.

For fixed K and compact archimedean parameters, the standard Hecke functional equation and strip estimates are uniform in ν and u with these conductor bounds. Nested rightmost-zero rectangles, Euler-log anchoring, Borel–Carathéodory and three-circles therefore give the same `X^η` reciprocal bound to the right of the buffered zero, with constants uniform in the moving ν. The original deleted Euler product and its reciprocal cost `X^η` on each fixed positive-real-part half-plane. On the reflected line the functional equation instead costs

    X^[(1+κ)(a−1/2)+O(e+η)] (1+X^τ)^A.                       (4)

Here a is the buffered bin real part, e and η are fixed small preliminary losses and A depends only on K and the fixed archimedean compact set. Gamma-convolution with inverse length X^t, common Fourier separation, and fixed-order Sobolev reduction proceed exactly as in [the untwisted fixed-field proof](../2026-10-29-general-long-detector/README.md): t and κ are fixed and all polynomial growth orders are chosen before the sufficiently small height power τ.

The resulting simultaneous inverse and ordinary witnesses obey, up to small fixed losses,

    r≤t,     m≤(1+κ)/2,     r+m≥t,                              (5)
    |M_r|²≳X^[(2a−1)r],  |S_m|²≳X^[(2a−1)m].

Indeed, the inverse bound remains `|M_r|²≪X^[(2a−1)r+loss]`, whereas the direct and reflected ordinary bounds give

    |S_m|²≪X^[(2a−1)min{m,1+κ−m}+loss].                         (6)

The usual Γ-convolution product lower bound forces the m restriction, and division by each opposite pointwise upper bound gives the individual witness lower bounds. The source's two character orientations can be grouped without changing labels: conjugate the common coefficient vector and ν at once. All derivatives in zero real part and frequency remain fixed-order and the height costs are uniform over the prescribed compact archimedean family.

If the inducing character is a pure norm character, its L-function has a shifted ζ_K pole and must be excluded from the Γ-contour argument. There is at most one such label u for a common ν: pure norm characters are unramified on every finite inertia group, so for each good p the local inertia of χ_u must be the inverse of that of ν. The assumed exact-order local character makes the exponent `v_p(u)∈{0,…,n−1}` uniquely determined. Thus all good valuations of u are determined. The one possible row contributes at most `O((X^τ+1)log X)` zeros in the fixed strip, by the standard uniform individual zero count, which is absorbed in (3). This argument does not enlarge S and does not assume that ν is finite-order.

## Source moments and scalar split

In every source polynomial, multiplication by ν(a) changes a fixed column coefficient vector to another **common** vector of no larger ℓ² norm. Source zeros at fν remain present, including primes also dividing u. De Faveri's Θₙ estimate therefore applies to the inverse squarefree columns and, after convolving powers and writing `a=a₁v²`, to the ordinary fourth and eighth moments by the same fixed-v contraction/Minkowski argument. No arithmetic large-sieve estimate uniform over row-dependent twists is asserted: ν is common to all rows in the moment.

Write the original threshold-divided four-face envelope as

    f(x)=max{1−δx, (1−δ)x, 1−1/n+(2/n−δ)x,
                         2/n+(1−1/n−δ)x}.                       (7)

In the middle range, put L=2t/3. The untwisted four-face calculation gives `f(x)≤R` throughout `[L,t]`. If r≥L use the inverse second moment. If r<L, (5) gives `L<2m≤1+κ`; the ordinary fourth moment and convexity of f give the upper bound `max{R,f(1+κ)}`. In the high range put L=4t/5. The eighth-moment calculation gives `f(x)≤R` throughout `[L,t]`. If r<L, then `L<4m≤2(1+κ)`; since `2(1+κ)≥2` and f(x)=hx for x≥2, convexity gives the upper bound `max{R,2h(1+κ)}`. Fixed κ, detector overflows and a,β bin losses are absorbed in ε before choosing the height power. See [the endpoint and fixed higher-power calculation](EXPANDED-KAPPA.md).

All bounds are uniform in ν because it occurs only through the displayed conductor bound, the compact archimedean parameters, and the unit-modulus/common-zero multiplier on the source vector. Neither a global zero-free hypothesis for the twist family nor any unrestricted row-dependent coefficient choice is used.

## Cubic and quadratic instances

The high-range proof also applies to n=3, since the two mixed Θ₃ faces coincide. For `5/6<σ<1`, set h=2(1−σ), `t=10/(4+3h)` and `R=10h/(4+3h)`; any fixed κ≥0 has exponent `E(κ)=max{R,2h(1+κ)}`, and κ≤`(1−3h)/(4+3h)` retains R. At the tracker value θ this threshold is `608041/11891959≈0.05113`. The same conductor, original-mask and pure-norm-row qualifications apply; this is a bound for a moving-twist cubic family, not a new full-zeta consequence.

A separate quadratic instance uses the squarefree-row/squarefree-column Goldmakher–Louvel sieve, not Θₙ for n≥3. Assume the quadratic source family satisfies its reciprocity and conductor hypotheses and the good squarefree labels' inertia identifies each label. For `1/2<σ<1`, put

    t=3/(2+h),   R=3h/(2+h),   E(κ)=max{R,h(1+κ)}.            (8)

The same uniform detector applies and the quadratic inverse second/ordinary fourth count envelope is `f(x)=max{1−δx,hx}`. It is ≤R on `[2t/3,t]`. If r is below 2t/3, then `2t/3<2m≤1+κ`, so convexity gives the exponent E(κ). The original R remains valid for κ≤t−1=(1−h)/(2+h). The quadratic source's transposed operator norm and common ν coefficient transport are as in [the quadratic density note](../2026-10-29-quadratic-fourth-density/README.md). The corresponding uniform bound is (3) with the n-free sum replaced by good squarefree labels and E(κ) from (8). As above, any pure-norm inducing row is separately counted and is unique under the stated inertia-injectivity condition. The Corrigan–Zhao rational comparison cited there is for untwisted quadratic Dirichlet characters; it does not automatically establish this moving-common-twist assertion.

**Independent review.** High_match checked the fixed-S, common-vector setup, the conductor and deletion bounds under local cancellation, uniform fixed-field Hecke estimates for compact archimedean type, the pure-norm row count, and the middle/high κ margins. The cited sieve and FHL source results remain inputs.

## Simultaneous avoidance for all finite-order twists in a conductor ball

For fixed K, the number of finite-order Hecke characters ν with `Nfν≤Q` is `≪_{K,ε}Q^(2+ε)`. Indeed, for every modulus f the number of characters of the narrow ray class group is its order, `≪_K Nf` by the ray-class exact sequence and the bounded archimedean sign factor. The number of integral ideals with norm at most Q is `O_K(Q)`, so summing over conductor ideals gives `O_K(Q²)` up to harmless small powers. Finite-order archimedean components lie in a fixed finite set. Count primitive characters by their conductors, and use their primitive conductor-zero presentations as above.

Consequently, whenever `E(κ)+2κ<1`, (3) and a union bound imply that all but

    O(X^(E(κ)+2κ+ε))                                             (9)

of the good n-free labels `Nu≤X` have the following **simultaneous** property: for every finite-order Hecke character ν with `Nfν≤X^κ`, the primitive L-function `L(s,(νχ_u)^*)` has no zero in `Re s≥σ`, `|Im s|≤X^τ`. The same conclusion holds for the squarefree quadratic instance under its stated assumptions. The uniformity in (3) is required: one first chooses a single τ and constant valid for the whole conductor ball, then sums over its characters. The possible pure-norm pole-bearing row for each ν is already included in (3); its total contribution is bounded by the same union argument. This statement counts exceptional **rows**, not pairs, and gives no individual all-height strip.

For n=4 and σ=4/5, choose `κ=1/10<2/13`. Then R=35/52 and (9) has exponent

    35/52 + 2/10 = 227/260 < 1.                                 (10)

Thus all but `O(X^(227/260+ε))` good fourth-free labels in this specified family avoid zeros in the common rectangle for every finite-order twist with conductor norm ≤`X^(1/10)`, subject to the same source inputs. The simultaneous set includes twists ramified at primes dividing u and twists that may produce a pure norm character; no coprimality assumption or uniformity over infinitely many conductors is imposed.

For the squarefree quadratic instance at σ=4/5, h=2/5 and (8) permits `κ=1/5<1/4`. Here R=1/2, so all but `O(X^(9/10+ε))` labels simultaneously avoid the rectangle for every finite-order ν with `Nfν≤X^(1/5)`, under the stated fixed-field GL-family and detector inputs. Corrigan–Zhao already give the untwisted rational-family exponent R=1/2 with explicit height dependence; that prior theorem is not, without a separate argument, this simultaneous moving-twist assertion.

For the n=3 high-range instance at θ, `κ=1/20<608041/11891959` is allowed and `R+2κ=74957259/118919590≈0.630319<1`. This gives the analogous simultaneous statement for that specified cubic natural-label family under the same source hypotheses; it does not claim a priority improvement over specialized cubic literature.

**Simultaneous-bound review.** High_match checked the fixed-K narrow ray class count, compact finite-order infinity types, uniform τ and constant, the union bound including possible pure-norm rows, and the n=4 example.
