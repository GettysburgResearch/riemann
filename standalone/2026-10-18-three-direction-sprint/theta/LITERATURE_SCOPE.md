# Classical overlap and the scope of the transfer obstructions

The primary source is Charles M. Newman, *Fourier transforms with only
real zeros*, Proceedings of the AMS61(2),245--251 (1976),
[complete original paper](https://www.math.northwestern.edu/~auffing/papers/Newman.pdf),
DOI10.1090/S0002-9939-1976-0434982-5. The full statement and proof of
Theorem2 and the theta application in Theorem3 were read during this
sprint.

Theorem2 classifies even finite measures whose Gaussian-damped Fourier
transforms have real zeros for every positive damping. Its proof studies
weak limits of Gaussian densities times products with pure imaginary
zeros and obtains a quartic canonical density form. Theorem3 excludes
the actual theta kernel using its faster tail decay.

Consequently the zero-field results in RANK_ONE_HIERARCHY_OBSTRUCTION.md
and GAUSSIAN_MEDIATOR_OBSTRUCTION.md are native reconstructions and
applications of a classical obstruction. They are not presented as a
new classification or a newly discovered barrier to theta completion.

STRIP_MEDIATOR_OBSTRUCTION.md separately proves the bounded-strip
quartet variant under its exact hypotheses. ENTIRE_ONSITE_OBSTRUCTION.md
and POSITIVE_ONSITE_COROLLARY.md prove their stated entire-density
closure components, with arbitrary quadratic renormalization and the
specified onsite positivity. No exhaustive priority claim is made for
these extensions. The native modular-cusp argument is in the root
BESSEL_COMPLETION_ATTEMPT.md; it does not depend on treating a classical
theorem as new.

All of these are architecture obstructions or conditional consumers.
They do not construct the required cofinal theta law, improve a zeta
zero-free region or prove RH. Their hypotheses do not cover every
correlated spin or transfer representation.
