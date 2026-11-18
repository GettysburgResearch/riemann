# Director adjudication: a computable remainder and an unconditional logarithmic tail

17 November 2026. I independently checked the full proofs prime64_finite_remainder.md and prime64_explicit_log4_tail.md, the prior effective decomposition, the two complete skeptic reports uniform64_finite_remainder_skeptic.md and uniform64_hardy_log4_skeptic.md, and both check programs. I reran the height-100 Arb certificate and all arithmetic checks. This adjudication distinguishes the unconditional critical-line derivative series from its RH-conditional interpretation as a length-limit constant. Publication novelty has not been assessed.

## An explicit finite-length comparison

For k=2, let E_N be the full squared anchored error, L=log N, and C_F the derivative coefficient sum over a complete certified finite list |gamma|<=Y. Use the quantities B(Y), A(Y), q, alpha, eta, delta and D_rho defined explicitly in prime64_finite_remainder.md. Every one is computed from elementary constants, a certified finite list, disjoint ordinate intervals and local zeta disk/derivative bounds. Under RH,

    |sqrt(L E_N)−sqrt(C_F)|
      <= alpha + q sqrt(c_+)/(1+sqrt(1−q)),
    |L E_N−C_2| <= 2 sqrt(c_++A(Y)) eta + eta².

The proof first separates the scaled residual into the near zero sum and a background norm at most sqrt(2·10^26/L). Weighted Cauchy–Schwarz handles every off-diagonal term in the far-height near sum, including arbitrarily close zeros. It gives squared tail B(Y)=6·10^22(1+floor Y)^(-1/16). Finite kernels are then cut to mutually disjoint delta windows; their common lost mass is at most q=min(1,4/(pi L delta)). Cauchy on radius2delta gives the displayed local coefficient Lipschitz constants D_rho, including at multiple zeros. Their remaining replacement errors add as squares only because these inner windows are disjoint.

The truncated finite model has norm exactly sqrt((1−Q)C_F), Q<=q. Reverse triangle inequality supplies the finite debit above. No extra tail term is needed in this direct comparison beyond the tail already in alpha. Passing to C_2 adds the independently bounded coefficient tail. The formulas remain valid for q=1 and an empty finite list. Completeness at the cutoff, including multiplicity and possible equality, is an explicit premise. A purported finite list omitting a close inner zero would invalidate this argument. The two-kernel overlap fixture demonstrates why untruncated individual masses cannot simply be added.

With the later coefficient tail below, A(Y) can be decreased to the minimum of the old value and the explicit logarithmic bound when Y>=16. This substitution is ONLY for the derivative coefficient tail, not for the near-function tail B(Y) inside alpha. Keeping the latter distinction is necessary for a valid finite-N remainder. The constants are computable but too coarse to yield a practical small length threshold from the present small-N examples.

## An unconditional derivative-series tail

For every T>=16,

    sum_(0<gamma<=T, critical line) |zeta'(1/2+i gamma)|²
      <= 260000 T log^4(4T).

Distinct zeros are enough; counting multiplicity makes no change at a multiple zero since the derivative is zero. This is unconditional. The proof does not assert that all zeros are on this line. It uses the exact real even Hardy Z function, whose derivative at zero vanishes. For each positive real zero a preceding stationary point exists, either at zero or by Rolle in the preceding gap. The disjoint intervals give sum |Z'(gamma)|²<=2 integral_0^T|Z'Z''|. Cauchy bounds this by continuous derivative mean squares.

Those continuous bounds are independently explicit. On |sigma−1/2|<=1/log(4T), the integral over |t|<=T+1 of |zeta|² is at most3000 T log(4T). Euler summation at M=ceil(2(T+1)), an absolutely summable integrated Bernoulli Fourier remainder and a Gaussian Gram bound prove it. The off-diagonal Gaussian row sum is below12; the pole and remainder are bounded separately, including low t. The holomorphic Hardy phase on the strip has squared modulus at most21. Cauchy on the actual complex disks gives integral |Z^(j)|²<=65000(j!)² T log^(2j+1)(4T), j=1,2. No zero separation or asymptotic moment constant is used.

For Y>=16 the two-sided k=2 derivative series therefore has tail at most

    (6.24·10^6/Y)[H^4+4H³+12H²+24H+24]
      <= 2.1·10^7 H^4/Y,   H=log(4Y).

Reflection, |sqrt2 exp(−i gamma log2)−1|²<6 and partial summation give the first bound. Dropping the nonpositive strict-tail endpoint only enlarges it. The log-fourth-power order agrees with the separately derived RH asymptotic; its coarse numerical constant was obtained independently and is effective. This bound and the series exist unconditionally. The prescribed-array identification with C_2 requires RH.

## A real evaluated certificate and its limits

The director rerun used python-flint0.9.0/FLINT3.6.0 at128bits. The exact all-zero count at100+2^(-10) is29. All29 distinct positive Hardy-zero balls lie strictly below100 and have nonzero derivative balls; they exhaust the count, including multiplicity. Negative ordinates follow by reflection; eta excludes the real critical zero. The finite coefficient sum lies in

    [0.25253801685456458, 0.25253801685456460].

The independent192bit replay and actual count/jet API contracts are documented in the skeptic report. The effective logarithmic tail at100 is below1.715·10^8, so the full critical-line series is unconditionally in

    [0.25253801685456458, 1.716·10^8].

Under RH this encloses the prime-array limit C_2. The upper endpoint remains very wide. A sufficient 1% certificate from this particular tail bound would need a complete finite sum through6·10^15 with width below0.00017; no such large list was computed. The checked tail there is less than0.00235. This scale is an explicit diagnosis of the bound's limitations, not a proposal to run an enormous unbudgeted zero computation.
