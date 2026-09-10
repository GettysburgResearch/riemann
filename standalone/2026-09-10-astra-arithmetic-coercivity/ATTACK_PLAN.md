# Attack plan: arithmetic no-concentration, not another kernel identity

**Research proposal. Q-AC26 remains OPEN.** The conditional proof route is in
PROOF.md and is not counted as an unconditional solution.

## 1. What changes

The preceding signed kernel admits finite spectral models built from any
selected zeros, including a hypothetical off-critical zero. Its exact
orthogonality is therefore not a zero-location selection mechanism.
Here the matrix B_X has only integer divisor data. Its forcing equation
B_X v=e_1 forces every coefficient of v to be the ACTUAL odd-Mobius sum.
The whole inverse is quantitatively equivalent, up to a logarithm, to that
same source energy. All-vector control is consequently a legitimate full-RH
target, not an unrelated positive surrogate or a stronger adapter left unproved.

The classical matrix/Dirichlet-inversion lineage is credited. What is being
proposed as a next mechanism is uniform shell compactness, not the invention
of arithmetic matrices or a proof by renaming the Mertens problem.

## 2. The direct global target

Prove that for A_j=3^(r_j),

    sup ||x_j||<infinity and ||B_(A_j)x_j|| -> 0
       imply ||L_(A_j)x_j|| -> 0.

This is equivalent to the uniform inequality Q-AC26, and would prove RH.
Every fixed coordinate of x_j already tends to zero, by triangular recursion.
A proof must control the moving tail; passing to a coordinatewise limit zero
and declaring norm convergence would be precisely the missing step.

The known source itself may generate approximate null vectors after
normalization, because its energy is unbounded. Their existence is not the
problem. The desired theorem says their extension into the next multiplicative
shell cannot carry a fixed positive fraction of their old normalized energy.

## 3. Where arithmetic could provide leverage

The new-shell inverse J_A is uniformly bounded. For old FORCING coordinates
d>=A/q, the transmitted matrix L_A V_A has Hilbert--Schmidt norm squared below
2q^2, for each fixed q. Thus a failure cannot be manufactured by a vanishing
forcing norm supported entirely in one fixed relative range of indices.
A proof must handle d/A -> 0, where many repeated divisibility scales interact.

One concrete investigation is to split the forcing into multiplicative bands
A/3^(j+1)<=d<A/3^j and derive a SIGNED or polarized cross-band estimate. A
triangle estimate grows with the number of bands and need not close. The
matrix entries and the true cross terms are explicitly available, so a
proposed estimate can be checked on the complete finite matrix before being
used analytically. No replacement by independent primes is justified.

A second investigation is an integer-matrix multiplier proof of
C_eta I+eta V_A^*V_A-(L_AV_A)^*(L_AV_A)>=0. This is the equivalent finite
certificate form, not a theorem that such a uniformly bounded C_eta exists.
Any proposed factorization must retain the exact floor/divisor boundary and
must be algebraically valid for arbitrary cutoff, not inferred from minors
at a finite list of cutoffs.

A third is a contradiction/compactness argument exploiting the full native
prime-shift relations. All finite prime shifts commute, but their norms in
the ordinary-index geometry and the growing prime boundary matter. Abstract
commutativity and positivity alone are insufficient: the exact countermodel
in Section 5 has those features and violates the desired conclusion.

## 4. A useful next bounded contribution

For fixed eta, compute exact rational bounds for

    c_eta(A)=max(0,lambda_max((L_AV_A)^*(L_AV_A)-eta V_A^*V_A)).

For any fixed A this is finite. The target requires sup_A c_eta(A)<infinity
for EVERY eta>0. The current eight certificates only show c_eta(A)<1 at
A=3,9,27,81 for eta=1/10,1/100. They are not an asymptotic forecast.

The most informative finite output would include a rational witness for a
failed proposed constant, its forcing decomposition across multiplicative
bands, and its exact divisor residual. That can falsify an overstrong
candidate mechanism without asserting an RH counterexample. A positive
certificate should cover all vectors by a complete Loewner test, not merely
check the source e_1 or sampled vectors.

## 5. Required safeguards and stopping rules

Do not use the positive diagonal or determinant as a singular-value bound.
Do not assert a fixed positive coercivity gap: the classical boundary-zero
argument proves it false. Do not reinterpret the positive native coefficients
of Z_X as positivity of an inverse or of a cross-scale form. Do not import
this countermodel's pole as an actual zeta zero. Do not discard small forcing
coordinates because each fixed-coordinate limit is zero.

A successful proof must provide either Q-AC26 with uniform C_eta, a weaker
uniform recurrence still giving subpower kappa, or a different source-faithful
global estimate. Another equivalent formulation without a new bound is not
completion. The supplied exact bridge and controlled sectors make the proposed
compactness problem operational, but do not solve it.
