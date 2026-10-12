# Independent audit of the twice-integrated complete count

Verdict: **ACCEPT at the complete-source/imported-input scope.** Reviewed
all sections and B1--B14 in
[DOUBLE_COUNT_PICK.md](../heights/DOUBLE_COUNT_PICK.md) at SHA256
`23e67ff10510aa7b27b497cd58e7e8a6f1a874c1fe3a9099ba5b7651df7a74b0`,
and its checker at SHA256
`e6e9f89e6a8019f989a9ae9fc299df87cb27630b1489f46431b4a028aa21a170`.
Review time: 2026-10-10 15:05 UTC. The owner's exact normal/optimized
receipts are byte-identical at SHA256
`30ff247e3da1a532e8c8c15ce900795a71528d0d5bffb23f654d6d33f61e05b1`.
This independent review is analytical and code-based; it does not perform
another heavy computation or rerun any published theorem or census.

The periodic Bernoulli integrations were reconstructed independently.
The first converts the B2 integral to (2/3) times the B3 integral with no
boundary contribution. The second has the B4(0)=-1/30 contribution,
which gives exactly the required -1/(360*z^3) term and -1/4 times the B4
integral. The quartic Bernoulli absolute bound is 1/30. The complex norm
estimate for z=1/4+i*t/2 gives exactly the two cubic constants 1/45 and
pi/60; positive real part safely reduces the integral norm.

Taking the imaginary part of the same complete logarithm gives the
displayed log, arctangent and rational terms. Their leading coefficients
are 1/16+1/8-1/6=1/48. The lower cubic corrections 1/128+1/96=7/384
and upper correction 1/24 are in the proper directions. With the full
Bernoulli remainder, both cubic coefficients are below 1/8, which proves
0<epsilon(t)<1/(47*t) at every t>=32. The explicit cubic Gamma term
has not been omitted to obtain this cancellation.

The native count primitive bound uses the literal unconditional Turing
integral, the complete count convention, and epsilon/pi integrated to
log(t/T)/141. Dividing by log t and the uniform lower log T bound gives
the displayed conservative c_A. This supplies A_T=O(log t), not merely
a pointwise bound for Delta.

The continuous weighted rational derivative bounds use the same original
denominator and the exact D=t*partial_t formulas. One does not apply a
dimension-n theorem to a differentiated rational function with increased
pole multiplicities. Instead, D, D^2 and the bounded real multipliers act
on the original numerator, yielding exactly C1*q and C2*q^2. Weighted
Cauchy--Schwarz then gives the factor 2*(C2+C1^2) in the absolute f''
integral for f=|R|^2, for every complex numerator.

The first Stieltjes lower boundary vanishes by the right-continuous
Delta(T)=0, excluding every atom at T. The second, ordinary absolutely
continuous integration has lower boundary A_T(T)=0. At infinity proper
decay gives f=O(t^-2), f'=O(t^-3), while both discrepancy quantities are
O(log t), so both upper boundaries vanish. The sign of the resulting
2*integral A_T*f'' is positive, and its norm coefficient is exactly
J=4*c_A*(C2+C1^2). Every full integral converges absolutely.

The reference reserve and sampling upper bound apply to all D^jP with the
same denominator. The original proof therefore retains independently
varying source heights, the complete exponential and signed-pole
prefactor, every Taylor depth, and all multiplicities and reflected
members of the complete 2*dN_+ source. The new amplification bound at
q<=131/200 and strictly positive endpoint gap were checked against the
exact scalar code. The complete quadratic reserve decreases with q, so
the endpoint is its valid worst case.

The common selected cutoff lies inside the published critical-line census.
The below-or-at-cutoff source is therefore nonnegative, including an atom
at the selected point if present. The strict global 1400000 guard and
maximal even order 1401784 at H0 follow from the exact integer condition.
The accepted conclusion is finite global order and increasing order at
selectable cutoffs for changing tails. It supplies no all-order positivity
or RH proof.
