# Independent internal review of the infinitely divisible padding obstruction

Reviewed `../theta/INFINITE_DIVISIBILITY_OBSTRUCTION.md`, actual
file-byte SHA256
`e8aaf8f5d469c213ee3aa0967f3c1570f030e7d7c37795daa66a539b2d63733e`.
No blocking error found at the displayed scope. This review reconstructs
the deductions from the explicitly imported classical Levy--Khintchine
representation; it does not independently reprove that structural
probability theorem or validate its whole historical source. This is
internal component review, not external acceptance or an RH result.

Independence and positivity imply that finite two-sided exponential
moments of X=U+V force the same moments for both factors. Jensen then
gives the needed subquadratic upper bound for the cumulant of U, with
only a linear change from the mean of V. In Levy--Khintchine form all
small-jump remainders are nonnegative, while large jumps outside a
selected interval cost at most their finite total mass. A nonzero
Gaussian part therefore forces quadratic growth. A nonzero Levy
measure has positive finite mass on some interval bounded away from
zero, and forces exponential growth in the corresponding sign of t.
Both contradict the two-sided subquadratic upper bound. The only
remaining infinitely divisible factor is a deterministic drift.

The actual theta MGF has logarithm `(1/2)|t|log|t|+O(|t|)` on both
sides, so it satisfies the hypotheses. A countable positive mixture
of infinitely divisible laws would give each component the same
subquadratic upper bound (up to its fixed mixing constant), hence make
each component deterministic. Such a mixture is countably atomic and
cannot equal the positive continuous theta density. The explicit
exception for an uncountable mixture of point masses is necessary and
correct.

For the separate vanishing-leaf-weight star corollary, conditional
independence, fair-hub symmetry, bounded second moments and largest
weight tending to zero give bounded conditional mean m_N and variance
v_N. Taylor expansion of each centered leaf has remainder bounded by
`C_z*w*Var`, and the logarithmic correction obeys the same summable
bound. Thus every selected convergent parameter subsequence has limit
`exp(-v*z^2/2)cos(m*z)`. Positive v supplies a forbidden Gaussian
factor; zero v gives at most two atoms. The conclusion is restricted
to the stated conditional-independent star architecture and hypotheses,
not arbitrary correlated graph observables or arbitrary weak limits
without the uniform second-moment assumption.
