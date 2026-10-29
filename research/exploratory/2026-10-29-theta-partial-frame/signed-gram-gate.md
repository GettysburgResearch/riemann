# The signed Gram estimate needed beyond Gershgorin

**Status.** This is the original source audit and an explicit sufficient estimate, not a zero-free region. The subsequently developed [small-square / large-square proof](full-gram.md) establishes the stated conditioning for the full-norm family under the additional source inputs recorded there; the stronger explicit H/√P expression below remains only a possible target. It refers to [de Faveri's Theorem 1.1](https://arxiv.org/abs/2610.04045), [the inverse-oriented theta overlaps](../2026-10-29-cubic-theta-overlap-average/README.md), and [the partial-frame result](README.md).

Let h,k run through the distinct good sixth-free ideals of norm ≤H and choose their primary generators. Put

    w_P(s)=1_(s good,sf,in fixed sector) |V(Ns/P)|² (Ns/P)^(−1),
    D_h=P^(−1) Σ_s w_P(s) 1_((s,h)=1),
    G_hk=(P√(D_h D_k))^(−1) Σ_s w_P(s) χ_s(k) overline(χ_s(h)).

The diagonal is **exactly** G_hh=1, including every zero mask. The weights D_h satisfy H^(−ε)≪D_h≪1 in the scale ranges at issue. This is the Gram matrix of the individually normalized inverse-oriented profiles, with its orientation possibly transposed; transposition does not change its spectrum.

A sufficient signed-off-diagonal statement for full conditioning up to H≤P^(1/2−δ) is: for each fixed δ>0 there is κ(δ)>0 such that, uniformly in all coefficient vectors c,

    |Σ_(h≠k) c_h overline(c_k) G_hk|
       ≪_δ P^(−κ(δ)) Σ_h |c_h|².                                (A)

Then `||G−I||≤P^(−κ)` and the full profile span is uniformly conditioned. A more explicit possible target is `(PH)^ε H/√P` on the right of (A), with preliminary ε chosen below δ; no such estimate is asserted here. The fixed ray sector, original masks and normalizations above are part of the target. It is stronger than an averaged scalar overlap and stronger than bounding only selected high-Gram directions.

## What the printed large-sieve proof supplies

Theorem 1.1 gives a nonnegative quadratic-form **upper bound** of order `(PH)^ε Θ₆(H,P)` with an unspecified constant. For H≤P^(1/2), this yields `||G||≪P^ε` after normalizing the columns, but it does not show `||G−I||=o(1)` or any uniform lower eigenvalue bound. The trace does imply the large high-Gram subspace in the companion note; the remaining eigenvalues may still be small.

The proof does not print the stronger asymptotic (A). The later [small-square / large-square argument](full-gram.md) derives a power-saving version of (A), conditional on its reciprocity, functional-equation and unrestricted-row sieve inputs; it does not derive the displayed possible H/√P rate. In §1.3.1 its first step completes a positive outer sum, opens the square and applies Poisson. The n-th-power removal (1.10) takes a trivial positive sum in the power index. In §4, Lemma 4.3 enlarges the row set by positivity, and Lemma 4.4 takes absolute values after gcd sorting and replaces the signed expression by maxima and nonnegative sieve norms. In §5, Lemma 5.1 applies Cauchy–Schwarz to decouple the root-number interactions; §7 iterates resulting upper inequalities. The resulting bounds are valuable uniform operator upper bounds, but those positivity, absolute-value and maximum steps do not preserve a diagonal main term with a power-small signed remainder. In particular an `O(P)` diagonal-scale term with an unspecified constant cannot be subtracted from the final upper inequality to recover (A).

Pairwise Hecke subconvexity alone proves the weaker Gershgorin range H≤P^(128/359−δ) for all profiles. The later proof extends to H≤P^(1/2−δ) using small-square Hecke shifts and the positive large-square sieve tail, which goes beyond summing the earlier pairwise absolute bounds. No claim is made that de Faveri's techniques cannot be sharpened to do this; the cited theorem and its displayed recursion alone do not supply it.
