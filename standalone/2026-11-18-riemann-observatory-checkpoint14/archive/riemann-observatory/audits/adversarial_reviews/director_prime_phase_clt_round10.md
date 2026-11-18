# Director adjudication: an arithmetic prime-phase central limit theorem

18 November 2026. I independently checked the full proof analytic64_euler_tilt_concentration.md, the exact uniform HLZ input already adjudicated, and the complete independent uniform64_euler_phase_clt_skeptic.md. The exact finite-word checks corroborate the algebra but are not the proof of the limit. The Euler-product antecedent is matched to Najnudel–Wei; product-measure facts are also proved directly. Publication priority is unassessed.

Assume RH. Draw one ordinate from |gamma|>Y with probability proportional to |zeta'(1/2+i gamma)|²/(1/4+gamma²), both signs included. For fixed D>0 put P=(logY)^D and

    H_P=sum_(p<=P)1/p,
    V_P=(1/2)sum_(p<=P)(1/p−1/p²),
    W_P(gamma)=sum_(p<=P)cos(gamma log p)/sqrt p.

Then

    P_Y(|W_P/H_P−1|>epsilon) <<_(D,epsilon) 1/H_P,
    (W_P−H_P)/sqrt(V_P) converges in law to N(0,1),

and every fixed normalized moment converges to the Gaussian moment. The same real statistic has exactly the same law after restriction to positive ordinates by reflection. Multiple zeros carry zero weight. This is not an unweighted zero theorem, a spacing theorem, or total-variation convergence of a growing torus distribution. The analytic onset remains ineffective.

The exact refined character estimate is indispensable. For every fixed range exponent D' and saving B, its error at m/n is bounded by a constant times (gcd(m,n)/sqrt(mn))log(mn/gcd²)/logY plus log^(-B)Y/sqrt(mn). Expand each raw W_P^j into rational characters before centering. All coefficients are nonnegative and all indices are at most P^j. The relative error therefore sums against the model raw moment, O_j(H_P^j), instead of the much larger absolute coefficient norm. The remaining coefficient norm is at most(2sqrt P)^j and is absorbed by choosing B after fixed D,j. Binomial centering and division by V_P^(j/2) then leave an error tending to zero at every fixed order. Gaussian determinacy completes the method of moments. A covariance operator bound by itself would not establish this stronger theorem.

The comparison model has independent Poisson-circle coordinates with radii p^(-1/2). Their centered bounded increments have variance V_P. Lindeberg proves weak convergence; a uniform subgaussian exponential bound supplies convergence and uniform integrability of all fixed moments. The full proof treats those as separate steps.

This model is a boundary Euler-product tilt. At every fixed sigma>1/2, its radii p^(-sigma) give the Haar-equivalent density |randomEulerProduct_sigma|²/zeta(2sigma). The normalized finite products form an L2-bounded martingale, and the limiting Euler product is nonzero almost surely. At sigma=1/2 the product is singular to Haar: W_P/H_P tends almost surely to1 under the critical product and to0 under Haar. The separating event follows by a variance-summable martingale and Kronecker, without assuming Kakutani's theorem. Thus the conditional arithmetic CLT detects a genuine prime-phase tilt at the singular boundary, not independent uniform phases. Its observed bias cannot be imported as a proof of the RH assumption used to derive it.
