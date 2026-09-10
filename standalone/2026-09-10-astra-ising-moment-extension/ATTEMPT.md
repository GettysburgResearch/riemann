# Attempt, design change, and exact remaining theorem

## What was actually attempted

The requested next operation was to extend the old four-even-moment seed using
positive interactions without sacrificing its lower moments. We differentiated
that constrained problem before treating a small numerical fit as progress.
The result was unfavorable: every allowed edge direction at the original
28-spin independent point lowers its already deficient tenth moment. The
certificate checks all seven edge classes. This does not rule out a nonlinear
path, splitting equal groups, adding vertices, or changing the graph.

A different direction, adding Gaussian variance and readjusting the positive
weights, has a rigorously positive derivative for the first unmatched moment.
This is the general local identity in PROOF Section 2. Replacing that reservoir
by many small signs suggested the six-group 270-spin candidate. Its exact root
is defined and certified independently of those exploratory numerics. The
actual matched orders are 2 through 12, not every order. Its moment 14 error
is strictly positive, rather than hidden by a stopping tolerance.

We also tested a Curie--Weiss interaction within the 256-spin group while
retaining the six lower moments, and several single interacting pairs. The
floating continuation attempts did NOT find a certified moment-14 solution.
One Curie--Weiss fit approached a collision of two weight groups. This is a
search outcome, not a theorem that this ansatz cannot succeed. No finite fit
failure has been promoted to a mathematical obstruction.

## Why the next graph must really use interactions

Merely adding more independent weight groups can match more low moments, but
cannot finish this particular problem. The exact product-of-cosines structure
forces zeros to replicate under tripling. The ACTUAL theta transform has a
certified real zero whose triple is not a zero. Our quantitative version
already excludes the original moment tolerance at order m=256; it makes no
claim that 256 is the first failure.

There is no contradiction with the Lee--Yang theorem. Real zero geometry does
not require zero tripling. A two-spin ferromagnet with J=(log2)/2 already has
chi(t)=0 and chi(3t)=1 at an appropriate real t. Thus it supplies an exact
interaction mechanism which the independent and Gaussian-reservoir models lack.
The new lower bound on total coupling and the parent's upper restriction on a
removable rank-one reserve concern DIFFERENT graph quantities. Neither forces
all edges to tend to zero, and neither rules out sparse interacting limits.

A useful exact representation for the next attack is the random-cluster
expansion of a finite Ising graph. For J_e>=0 expand

    exp(J_e sigma_u sigma_v)
       =exp(-J_e)[1+(exp(2J_e)-1)1_(sigma_u=sigma_v)].

Summing spins gives a positive weight proportional to
2^(number of clusters) product_(open e)(exp(2J_e)-1) on edge subsets.
Conditional on that subset, the cluster signs are independent. If A_C is the
sum of observable weights within a cluster, the characteristic function is
EXACTLY the corresponding weighted average of product_C cos(t A_C).
The interaction can therefore cancel products at one frequency without
cancelling every conditional product there. This is the classical
random-cluster expansion, derived here only to specify the mechanism.

The cluster weights are NOT free mixture weights. They must come from ONE
finite graph with nonnegative edge factors. Treating arbitrary mixtures of
real-zero functions as ferromagnets would lose the Lee--Yang hypothesis.
The next genuinely useful construction must exploit that constrained cluster
law, rather than simply assign quadrature weights to theta moments.

## The complete sufficient ending

Produce, for every m, a finite graph, positive/nonnegative weights a_i and
couplings J_ij>=0 such that

    |E X_m^(2r)-mu_(2r)|<=2^-m, 1<=r<=m,
    X_m=sum_i a_i sigma_i,

where mu_(2r) are the UNCHANGED full theta moments. Lee--Yang plus the variance
bound pays the entire complex Taylor tail; locally uniform entire convergence
and Hurwitz then imply RH. PROOF Section 7 includes this consumer.

The missing assertion is existence of the graph at arbitrary order. It is
NOT proved by local nonsingularity, by the new exact six-equation solution,
by a large number of spin parameters, or by the positivity of a moment matrix.
The Gaussian-replacement IFT is local and cannot be blindly iterated: the
independent obstruction proves that some such iteration must cease to meet the
actual targets. The connected positive-J models through order 12 do not
supply a graph-enlargement induction or a uniform continuation radius.

This packet therefore requests review of a precise constructive extension,
a general local lift, and source-specific restrictions on the eventual
construction. It does not submit a completed RH proof with a central estimate
left for reviewers to invent.
