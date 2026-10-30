# First-stage target for fixed nonzero infinity type

**Status:** Proposed research target and conditional exponent calculation. No improved zero-free region is proved. None of the source papers has been fully audited here.

**Sources:** Hu, [*A seven-eighths zero-free half-plane for unitary Weil L-functions*](https://hexagonmath.org/2610.00216v1), Sections 4 and 6; Liu, [*Zero-free half-planes for Hecke L-functions over number fields*](https://arxiv.org/abs/2610.26835v1), Sections 13–14 and Appendix B; and Xu–Sang, [*Amplified moments and a refinement of the quasi-Riemann hypothesis*](https://arxiv.org/abs/2610.15291v2), Sections 3, 6–8 and Appendix D. These are recent preprints; their claims, and their precise correspondence of notation, require independent review.

## Why a first-stage improvement may be approachable

Fix a number field F, put K = F(zeta_12), and fix a unitary Hecke target of K with a prescribed infinity type. Hu's proposed method compensates the physical probe so that, despite the infinite-order target, its prime slots are finite-order residue characters (equation (6.10)) and its Poisson row numerator is the finite-order factor L_K(w,chi_u) (equation (6.12)); the target remains in the denominator. Thus Liu's Proposition 14.3, which bounds the amplified average of the finite-order numerators over K containing the twelfth roots of unity, is a candidate input without first proving an approximate functional equation for an infinite-type numerator. This is not yet an application: the row sets, possible inverse orientation, finite ray factors, slot coefficients, original masks, and all profile and height uniformity must match Liu's hypotheses exactly.

Hu's paired fourth moment, Theorem 4.2, allows kappa >= 3/4. A first stage with kappa = 3/4 can use the source's claimed 7/8 ceiling; Liu's finite-order result over every K also supplies the finite-character zero-free premise for this kappa. Xu–Sang's first-stage numerical parameters are

    kappa = 3/4,  b = 173/2000,  ell = 10027/60000,
    B0 = 69991/80000 = 0.8748875.

Their admissibility and endpoint margins are certified in their Proposition 7.1 and Appendix D. These *scalar* inequalities do not verify that Hu's infinite-type probe satisfies the inputs on which they are applied.

## Low-side calculation and its missing analytic premise

The balanced lengths and continuation exponent associated to those parameters are

    lx = (1-b-ell)/2 = 44783/120000,
    ly = (1+b-ell)/2 = 55163/120000,
    h  = (1+b+3ell)/2 = 31757/40000,
    C_b(s) = s - (4+b)/6,
    C_b(B0) = lx/2 + b/12 = 46513/240000.

For a rescaled subset of the prime slots of total length d in [0,ell], the Xu–Sang/Liu finite-type argument bounds the completed row norm with the extra exponent

    L_ell(d) = max(0, 5ell + d - 1)/4.

The general-variable counterpart of this estimate for Hu's actual fixed-infinity-type marked row is an analytic premise that has **not** been derived here. Hu proves its relevant special-geometry low estimate in Proposition 6.2, using his general marked energy Lemma 4.8 and additive Gram Proposition 3.8. One must retain the same completed row, all masks, fixed-type phases, row-unit quotient, common profile, and both branches of his reflected energy, and establish the stated L_ell(d) bound uniformly for every subset.

If that premise holds with the same accompanying Gram and summation estimates, the contribution of one subset is bounded by

    Z^(lx/2 + b/12 - d + L_ell(d)/2 + epsilon).

The extra -d is the sum of tuple counting, compensation, and the X' square-root factor; it must be recomputed for the actual probe rather than assumed for a modified one. Because 5ell<1, one has L_ell(d) <= d/4, so the subset loss is at most -7d/8. A fixed finite number of subsets gives the desired low exponent C_b(B0), up to epsilon; the logarithmic normalizer costs Z^epsilon. The exact Gram-scale margin is ly-ell-11b/6 = 16079/120000 > 0.

## Independent gates before a theorem

1. Prove the variable-geometry infinite-type low estimate above with Hu's actual row energy and Gram inputs; prove a compatible principal signal with C_b(s), not the fixed C(s)=s-11/16 from his Section 6.
2. Match Liu's averaged numerator bound to Hu's finite residue-character row, including every bad-prime and zero-extension mask; preserve all target phases and polynomial height factors in the nonprincipal contour argument.
3. Rebuild Hu's count and high-side contour comparison at the first-stage parameters, including the full target family, principal correction, small and large row ranges, and a saving uniform in the later finite twists. Verify the assumptions of the Xu–Sang scalar certificate apply to these physical expressions.
4. Establish a common-probe continuation and the family descent for infinite-order unitary characters, treating shifted poles of unitary norm characters. The same low and high estimates must refer to the same normalized probe.

The second stage would additionally require care with the moment parameter: its kappa = 29991/40000 = 0.749775 is strictly below the stated range of Hu's Theorem 4.2. Liu's finite-order moment with this parameter does not automatically furnish the corresponding paired moment for an infinite-type background. At the still lower Liu fixed point, 2B_flat-1 is about 0.749773294. Neither this gap nor the first-stage physical gates above is resolved by plugging numbers into a scalar certificate.

**What was run:** Direct comparison of Hu (6.10), (6.12), Theorem 4.2 and Proposition 6.2 with Liu Proposition 14.3 and Xu–Sang Proposition 7.1; exact rational arithmetic for the displayed exponents and Gram margin. No theta, local-factor, contour, moment, or finite-type-to-infinite-type proof was replayed.
