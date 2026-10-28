# Principal Euler correction at the residue point

**Status:** Elementary lemma derived from the cited local identity. Its scope is not new: Hu, [arXiv-equivalent preprint Lemma 6.1](https://hexagonmath.org/2610.00216v1), already states holomorphy and nonvanishing on Re(s)>2/3 for a broader unitary-family correction. The displayed local specialization was independently checked, but neither source was fully audited.
**Scope:** One scalar Euler-product ingredient, not a zero-free region.
**Source:** OpenAI, *The Quasi-Riemann Hypothesis*, 30 September 2026, Lemma 7.1, equations (7.11), (7.12), (7.17), and equation (10.1), [paper](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf) (PDF Git blob `8132b77eeb270a70b25df8d6609f008e83e65d91`). The proof below uses the paper's local identity as an input, not its asserted zero-free theorem.
**What was run:** Algebraic derivation from the displayed local formula and an elementary absolute-convergence estimate; no numerical computation or independent audit of the imported identity.
**Smallest remaining gap:** Independently check the specializations and whether this observation is already in the literature. Hu Lemma 6.1 already gives this domain. It does not extend the paper's multivariable contour bounds or improve its probe estimate.

## Claim

Use the notation of the source, including its fixed finite exceptional prime set S. For u=1 put

    H_eta(s) = H_{eta,1}(s,1,1/6).

For each fixed real σ0>2/3, the local factors in the paper define H_eta(s) by an absolutely and uniformly convergent Euler product on Re(s)≥σ0, after deleting the finitely many primes in S. On Re(s)>2/3 this product is holomorphic. Moreover, if S contains all prime ideals of norm at most P0, then uniformly in all complex s with Re(s)≥σ0 and all admissible target η,

    H_eta(s) = 1 + O_{σ0}(P0^{-c}),
    c = min(6σ0-4, σ0, 1) > 0.

Thus a sufficiently large P0, chosen in terms of σ0 before η, makes |H_eta(s)-1|≤1/2 on that half-plane. Additional finite deletions preserve the same bound. The source states this contraction on Re(s)>7/8; the point here is a larger domain for this *one residue-point product*.

## Proof

Fix a good prime p not in S, and write Q=Np. In the source's notation j=v_p(u)=0 and ρ=χ_p(1)=1. At w=1, z=1/6, its quantities are

    V = W = W_loc = Q^{-1},  D = η(p) Q^{-s},
    R = a_p^2 Q^{3-6s},  |a_p| ≤ 1.

Let E_p=P_p^*+D. Equation (7.11), specialized and simplified using (Q-1)V/(1-V)=1, gives the identity

    E_p = [R(1+1/Q-D) - D/Q] / (1-R).

For Re(s)≥σ0>2/3, |R|≤Q^{3-6σ0}≤2^{3-6σ0}<1, so the denominator is uniformly bounded away from zero. Since |D|≤Q^{-σ0}, this implies

    E_p = O_{σ0}(Q^{3-6σ0} + Q^{-1-σ0}).

Equation (7.17) is

    H_p - 1 = [D(V+W-VW) - VW + (1-V)(1-W)E_p]/(1-D).

Here |1-D|≥1-2^{-σ0}>0, and therefore

    H_p - 1 = O_{σ0}(Q^{3-6σ0} + Q^{-1-σ0} + Q^{-2})
            = O_{σ0}(Q^{-1-c}).

The count of integral ideals of norm at most x in the fixed quadratic field is O(x); partial summation bounds the sum over all prime ideals of norm exceeding P0 of Q^{-1-c} by O_c(P0^{-c}). Standard product estimates then give the stated uniform contraction and holomorphy. The implicit constants do not depend on η, S, or Im(s).

## Consequence and boundary

This calculation does **not** imply that the nonprincipal rows, the full tuple corrections, or the contour shifts are controlled for Re(s)>2/3. In particular, the source's compensated low bound (15.6) has exponent 3/16, while its signal exponent is C(s)=s-11/16. In Proposition 2.1 this low bound alone reaches its comparison threshold at 7/8: C(7/8)=3/16. Lowering that threshold requires a stronger low estimate or a modified probe, plus new high-side estimates; extending this scalar correction is insufficient.


## Prior-art qualification

Boyang Hu, [*A seven-eighths zero-free half-plane for unitary Weil L-functions*, version 1](https://hexagonmath.org/2610.00216v1), Section 6.3, Lemma 6.1, states holomorphy and nonvanishing for a principal correction in Re(s)>2/3, for his number-field and fixed-infinity-type construction. His explicit local factor (6.15) has the same algebraic shape as the residue-point factor above. His statement allows the finite excluded set as defined there and does not need the present quantitative tail-contraction formulation. The constructions are not identified term by term here; the preprint is an unaudited source claim. Thus the 2/3 domain is not a new mathematical target, even though the uniform proximity-to-one assertion above is a separate quantitative statement.
