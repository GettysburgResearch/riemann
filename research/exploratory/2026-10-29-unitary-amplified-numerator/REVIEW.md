# Independent internal review

Reviewed the fixed-field amplified numerator note against Hu (6.10), (6.12), Theorem 4.2 and Proposition 4.14, Xu–Sang Proposition 5.1, and the companion approximate-functional-equation calculation. This is a review of the stated source-dependent deduction, not a proof of Hu's moment theorem, theta identities, or the full zero-free argument.

Two issues in the original assumptions were identified and corrected in the current note:

1. A separate lower-bound loss U^(−ε₀) for each slot accumulates as Nε₀, so it is incompatible with a binning loss chosen independently of a later slot count. The corrected relative-width loss U^(−ε₀ℓᵢ) has total loss at most ε₀ L. It is necessary to fix a bounded total-length range or choose ε₀ after the geometry's L is fixed.
2. A zero-amplitude slot may actually vanish. The corrected statement imposes a lower bound only for gᵢ>0, bounds gᵢ uniformly to control the fractional discarded slot, and uses all positive slots if their lengths are exhausted before the requested capacity.

For the physical main slots, Hu (6.10) gives

    Q_i(u;z)=−Σ_p W_i(Np/P_i)(Np)^(z−1) overline(χ_u(p)).

The windows W_i are real. Conjugating the whole slot and dividing by the explicit scale P_i^(conjugate(z)−1/2) produces a centrally normalized sum with character χ_u and profile W_i(y)y^(conjugate(z)−1). Hu's Theorem 4.2 therefore admits the direct specialization ω₀=1, ξ_u=χ_u, a_i=1. Finite fixed ray restrictions expand into permitted Θ-character combinations. The good-prime zero extension and common masks must remain present. The identification of χ_u with its primitive inducing character at the good primes, including zero values at ramified row primes, is an explicit Hu/Kummer source input in the statement. Bounded exceptional inducing characters are excluded as stated. The two factors after differentiating the row-conductor profile are distinct permitted plain profiles; the selected slot product is unchanged. Hu's moment is stated for these paired profiles, and Proposition 4.14 makes its mesh independent of the subsequent fixed slot count.

At κ=3/4, the moment premise is precisely finite-order zero-freeness for Re s>7/8. It is a source input, and no extension of Hu's theorem to κ<3/4 is used. The physical profile's frequency and every other retained Fourier variable must obey the same cumulative height budget; the abstract numerator statement explicitly assumes the physical match and finite height orders.

The two Hölder exponents, short-block identity, full-capacity threshold and endpoint algebra in the current note check. The AFE's conductor-dyad Sobolev step is conditional on Hu's source moment and its common-profile/mask uniformity. The review does not settle the remaining full dynamic contour, principal residues, or low-side physical source matching.
