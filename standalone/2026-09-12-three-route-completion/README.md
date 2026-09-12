# Progress on all three RH completion routes

**PROPOSED component mathematics and finite checks. RH remains unproved.**
This is one add-only research packet on main
`f99d9e3908dde4865377c75d9ca051c1f545bf4f`, pursuing the arithmetic,
ferromagnetic-realization and native-gamma routes together. The results below
are new proposed arguments; inherited theorems and numerical premises retain
their recorded status. Nothing here promotes a canonical or formal claim.

## 1. Arithmetic: a sharp exponent and a computable boundary channel

Let S_N and Lambda_N be DG26's positive odd-Legendre trace and finite operator
norm squared, and let Theta be the unknown supremum of nontrivial zeta-zero
real parts. [The proof](arithmetic/PROOF.md) sharpens the previous every-large-
degree witness to obtain the exact limits

    log(1+S_N)/log N -> 2Theta-1,
    log(1+Lambda_N)/log N -> 2Theta-1.

This includes Theta=1 and does not evaluate Theta. One unconditional
consequence is **subpower effective rank**, S_N/Lambda_N=N^o(1), improving
the generic dimension-N bound. It controls relative operator approximation;
it does not bound the largest mode or capture the whole trace in few modes.

An explicit finite adapter connects the ordinary Mobius energy
F_Y=sum_(k<=Y)(sum_(n<=k)mu(n)/n)^2 to this odd-source trace:

    S_N <= 26 F_(3 ceil((2N-1)^(3/2))) + 1296, N>=2.

The [retained-boundary construction](arithmetic/BOUNDARY_CHANNELS.md) improves
the finite arithmetic coverage: keeping one exact origin channel gives a
surrogate B_(N,M) with

    ||K P_N-B_(N,M)||_HS <=11(2N-1)^(7/2)/M^3.

It uses only mu through 3M and 8/pi^2, including every mixed term. Fixed r
retained channels reduce constant-error coverage to order
N^(1+1/(4r+2)). A complete N=4,M=32 directed replay verifies all output cells.

**Still missing:** a subpower upper bound for the actual magnitude, or the
native crossing covariance gain supplied as an open premise by latest #848.
The collision diagonal alone cannot be substituted for the whole energy.

## 2. Ferromagnets: certified motion toward the next moment

The [graft proof](ferromagnetic/PROOF.md) derives an exact merger of two
zero-field components that preserves both old Gibbs marginals, and a general
component-polynomial formula eliminating the lower-moment Jacobian from the
compensated next-cumulant derivative.

Applied to #863's degree-14 root box, two positive-edge directions strictly
decrease its actual sixteenth-moment excess while keeping all seven lower
even moments exact. One derivative lies between -.012 and -.011; the
correlated component grows from two spins to three. The native application
depends explicitly on #863's root-existence theorem; its theta integration
is not claimed newly replayed.

The new #867 star, which appeared during this pass, supplies an opposite-sign
degree-16 seed. Both endpoints belong to the general-star class. The
[additional search](star/ATTEMPT.md) varied structured couplings, released
weights and then all nineteen grouped weights/biases. No target crossing or
new exact degree-16 model was obtained. A convex mixture of the two endpoints
is not used as a ferromagnetic realization.

The [LP feasibility bridge](bridge/PROOF.md) adds a rigorous sixth-moment
integer-multiplicity constraint. An explicit positive six-atomic law passes
strict finite cumulant forms but violates this constraint on a fixed open
neighborhood. This makes finite positive quadrature's insufficient lifting
power concrete; it is not an obstruction to the native theta data.

**Still missing:** a positive-parameter path that reaches the next target,
and a target-containing extension at arbitrarily large orders.

## 3. Gamma: signed production from a known real-zero source

The [gamma proof](gamma/PROOF.md) constructs an exact positive convolution
path from Gamma(4,rate4), whose reciprocal transform has a Bessel/Sturm
real-zero proof, to each native Radau-compressed gamma source. A compensated
Levy generator and weighted Fisher/Poisson estimates justify its derivative
through the reciprocal square root and changing support.

Its regularized integrated Jensen balance equals the entire weighted
nonreal-zero defect, with complete radius error

    7/R^2 + [log(2R+4)+1]/(4R).

The balance includes births, collisions and crossings. Its initial defect
is zero independently of RH; no unknown Delta_xi is hidden as an initial
constant. The native modular Mellin tangent is also derived explicitly.
The inherited centered-N=5 disk implies total production >5e-8 there, so a
universally nonpositive finite-stage production rule would be false.

**Still missing:** decay of the actual signed production along the cofinal
native family. Bounds proving that the integral exists do not prove that it
tends to zero.

The [latest connection](gamma/LATEST_CONNECTION.md) incorporates #868, which
also appeared during this pass. It proves regularity through u=0 for its
native updates, using a Gamma(6,rate9) anchor for a stronger O(u) derivative
bound. At a common spectral radius, the complete signed step budgets telescope:
the endpoint-tail error stays T(R)/2, independent of the number of steps.
#868's local native annihilation remains its separately imported certificate.

## Checks, review and provenance

From this directory, with the Python standard library:

    python -S -B check_all.py --write validation.json

All eleven subprocess commands passed, covering normal/optimized arithmetic
reconstruction, finite algebra controls, and the specified mutation tests.
[validation.json](validation.json) records actual command outputs and file
hashes at execution. These finite checks do not machine-prove the infinite
paper arguments, replay all parent native integrals, or establish RH.

[REVIEW.md](REVIEW.md) records component cross-checks and repairs.
[SOURCE_LOCK.json](SOURCE_LOCK.json) pins the main research predecessors.
Per-route proof and validation files distinguish native derivations,
classical imports, inherited numerical premises and ordinary numerical
searches. The optional scouts require separate third-party libraries and
frozen Git objects; they are outside acceptance.
