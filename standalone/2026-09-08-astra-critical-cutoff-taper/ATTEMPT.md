# The attempted unconditional completion: exact stopping point

Status: the requested full RH proof was not obtained. This note accompanies
component proofs and an RH-conditional convergence theorem, not a completed
RH argument. No independent acceptance or external novelty is claimed.

## 1. What the new calculation settles

The hard-cutoff norm contains R(X)^2/(2X^2). Even a proof that the uncut state
v lies in L2 does not, by itself, make point evaluation at log X small.
The fixed logarithmic taper removes this artificial endpoint difficulty while
preserving the source before log X. The unconditional estimate (9) pays the
full infinite future of the averaged state. It does not merely remove it.

On RH, the classical mean-square theorem supplies the stronger fact J<infinity,
not just subpower growth. The new taper then gives a concrete boundary
construction with rate O(1/sqrt(log X)) for the complete complex logarithm.
In particular the tapered entropy converges to a finite target value; it need
not be described only by the earlier conditional growing polylogarithmic bound.

These are useful analytic completion and normalization statements. They do
not prove the arithmetic hypothesis. They are not evidence that the remaining
unconditional step has become a technical lemma.

## 2. The attempted import of Cramer's estimate

The candidate closing chain would be

    integral_Y^(2Y) |psi(x)-x|^2 dx <= K Y^2
        -> integrable weighted theta discrepancy
        -> J<infinity
        -> analytic logarithm in Re s>1/2
        -> RH.

Every arrow is supplied in PROOF.md. The first assertion has NOT been proved
unconditionally. The external paper explicitly assumes RH for its upper
estimate. Its unconditional lower estimate goes in the wrong direction.
Reusing the first assertion as an available input would be circular.

Squaring the usual RH pointwise bound also loses logarithms and does not
reproduce CM. This distinction is already emphasized in the external paper.
No numerical verification of a finite prefix establishes CM for arbitrary Y.

## 3. Direct arithmetic attack on the first assertion

For the source actually needed here, partial summation is exact:

    R(x)=sqrt x/log x [theta(x)-x]+2sqrt2/log2
                         -integral_2^x [theta(u)-u]d(sqrt u/log u).

Applying the classical unconditional PNT remainder
|theta(x)-x|<=C x exp(-c sqrt(log x)) gives, after splitting the integral at
sqrt x and decreasing c if necessary,

    |R(x)|<=C' x^(3/2)exp(-c' sqrt(log x)),
    integral_2^X R(x)^2/x^3 dx
                         <=C'' X exp(-c'' sqrt(log X)).

The exact cutoff norm has a bound of the same scale, and its tapered version
inherits an upper bound of order X^(1/2)exp(-c'''sqrt(log X)) in norm.
This remains a positive power of X. It gives neither finite J nor the weaker
subpower bound in the parent. Constants are not numerically certified here.

Expanding the square of R does not repair this: it produces prime-prime,
prime-continuum, and continuum-continuum terms. Their cancellation IS the
remaining quantity; retaining only the prime diagonal would change the source.
The current proof offers no new unconditional estimate for those full terms.

## 4. Why finite target entropy is not a bound for the approximants

The boundary function log^+|(s-1)zeta(s)/s^2| at s=1/2+iy has an integrable
positive part from standard polynomial zeta growth. That by itself cannot
bound Ebar(X). Identification of a boundary target does not justify passage
to it in the norm used by the proof.

A simple exact analytic control shows the missing uniformity. For Re z>0 set

    F_n(z)=(z+1)^(-1)
                exp[-sum_(k=1)^n (3/2)^k/(k(z+1)^k)].

For each finite n it is bounded, H2, zero-free and outer, extending
nonvanishingly through the imaginary axis. It has the correct 1/z behavior
at positive real infinity. On every compact subset of Re z>1/2 it converges to

    F(z)=(z-1/2)/(z+1)^2.

That target has a zero in the full right half-plane. Its positive logarithmic
boundary integral is finite. Also log F_n(1)=-log2-sum_(k=1)^n(3/4)^k/k
is uniformly bounded. Nevertheless the positive logarithmic boundary costs
cannot have a bounded subsequence: the Poisson--Schwarz/Montel argument would
then extend the safe limit zero-freely to Re z>0, contradicting that zero.

This is a synthetic analytic control, NOT ordinary primes, a zeta function,
or a counterexample to RH. It rejects only that general interchange of limits.
Its behavior is not used as a premise in any arithmetic statement.

## 5. Scope of the proposed review

Review T1's endpoint accounting, the signed Volterra identity (19), the CM
hypothesis flag, the all-frequency higher-power tail, and the identification
of the logarithmic Hardy trace after dividing by z+1. The finite source
weights and the geometric versus arithmetic averaging are essential.

The paper does not claim strong L2 convergence of the EXPONENTIAL Abar_X,
unconditional bounded entropy, an unconditional Cramer estimate, a new
zero-free region, or closure of the original source domain. It supplies an
RH-conditional boundary construction and a complete conditional route to RH.
The proof of the first arithmetic upper bound remains missing.
