# A proposed conditional first-stage region for unitary Weil L-functions

**Status:** Conditional research theorem and proof reduction. The listed analytic inputs are taken from recent preprints and their field/type interfaces, not independently proved or fully replayed here. The source-to-probe matching is part of the hypotheses. Consequently this note does **not** claim an unconditional new zero-free region or a reviewed proof. It records precisely what the completed scalar and contour calculations would yield if those inputs apply simultaneously.

Let `B₀=69991/80000=0.8748875`. Assume the following statements with the indicated source quantifiers, for every fixed number field K containing μ₁₂ and every fixed infinity-type orbit in Hu's construction.

1. Hu's claimed 7/8 zero-free theorem holds for the full fixed-type buffered family and for the finite-order Hecke family needed by its fourth moment. The primitive Hecke functional equation, fixed-type strip estimates, unit-sector decomposition and conductor/deleted-radical estimates hold as used in Hu §§3–4 and §7.1. In particular, the global-line reciprocal and deleted factors satisfy the quantitative U^ε(1+|t|)^A bound in [the outer-row note](../2026-10-29-unitary-outer-rows/README.md), including principal denominator presentations, and the nonprincipal numerator satisfies its U^(3/5+ε) central-line bound.
2. Hu's general-scale physical identity (6.5), marked identity, finite compensation (6.9), full unramified and ramified local tables and sector recombination hold for one common test system and bad set. Its physical prime slots, numerator and denominator have exactly the character orientations, fixed-ray coefficients and zero masks required by Hu Theorems 4.1–4.2. Hu's nonprincipal/principal row identification holds after recombining sectors.
3. Hu's marked reflected-energy Lemma 4.8, fixed-type theta reflection and additive Gram Proposition 3.8 apply to every rescaling and mark subset of that physical system, with their stated retained-dyad tail, common-profile and finite-seminorm controls. The active nonresidual radical and its N₀ subproduct have the support identified in [the low-side audit](../2026-10-28-hu-variable-low/audit.md). The common Gaussian separation, finite unit sectors and normalizing prime-window asymptotics are valid as in that note.
4. Hu's inverse and paired fourth moments, unmarked inverse moment, finite-type zero-free premise and Proposition 4.14's loss/mesh order apply to every fixed buffered presentation and common-profile derivative used in the detector and finite-order numerator. The fixed-field primitive finite-order numerator admits the AFE, conductor-dyad Sobolev reduction and uniform smooth profiles in [the AFE note](../2026-10-29-fixed-field-afe/README.md), with the physical primitive/imprimitive coefficients and original masks. The fixed-type nested zero detector, simultaneous witnesses, amplitude upper/lower bins and cumulative Fourier-height allowance apply at any β>B₀, including β≤7/8, with the quantitative reciprocal and deleted-factor bounds in [the detector note](../2026-10-29-fixed-type-buffered-detector.md).
5. The above local identities and all-height/seminorm bounds match OpenAI Lemma 10.2's integrated and trace-tail hypotheses for the **same** variable-geometry expression, after the target-independent real choices and before the target-dependent height/tail choices. Every separating frequency used as an external trace coordinate has the requisite rapid pointwise density bound; internal measures known only in weighted L¹ remain integrated within their fixed arithmetic estimate. One cumulative height allowance is allocated across the Mellin, detector, AFE and selected-slot frequencies before truncation. The physical common presentation and masks are unchanged through every contour move and moment application.

These assumptions include nontrivial source-to-physical interfaces, not merely the printed fixed-geometry conclusions of Hu Proposition 6.2 or 6.3. In particular Hu's Proposition 6.3 is stated with a `B>7/8` hypothesis, so its conclusion is not imported wholesale for this new boundary.

**Conditional conclusion.** Under these inputs, every continuous unitary Hecke character of every number field has no zero in `Re(s)>B₀`; its only possible singularities there are the standard norm-character poles. The same region and the norm-character pole-order formula hold for every finite-dimensional continuous unitary global Weil representation. Fixed finite Euler factors can be deleted without introducing zeros in this region.

## Proof from the stated inputs

Fix K, an infinity-type orbit and its common family 𝔽ω, with supremum β of zero real parts. The first input gives β≤7/8. Suppose β>B₀. Choose Xu–Sang's first-stage geometry and a fixed even, sufficiently fine disjoint slot system:

    κ=3/4,  b=173/2000,  ℓ=10027/60000,
    lₓ=44783/120000,  lᵧ=55163/120000,
    h=31757/40000,  C_b(s)=s−(4+b)/6.

The fields, type orbit, losses, mesh and slots are chosen before the later finite-order target twist; target-specific finite sets S, height degrees, thresholds and constants may be chosen later. For each fixed target, the same final S is used in the physical probe, both contour calculations and the principal signal. By the third input and the low-side calculation, every oriented target's normalized probe satisfies

    |Jψ(Z)| ≪ψ,ε Z^(C_b(B₀)+ε).                              (1)

For the same probe, the full local table and source estimates give the exact physical high identity. The [D1 majorant](../2026-10-29-unitary-first-euler-region/README.md), [D2 identity](../2026-10-29-hu-d2-identity.md), [fixed-type detector](../2026-10-29-fixed-type-buffered-detector.md) and [dynamic contour](../2026-10-29-unitary-dynamic-contour/README.md) implement the contour moves under the listed hypotheses. Hu's moments and Xu–Sang's abstract witness comparison give the fixed-type row count in [the witness note](../2026-10-29-hu-witness-count/README.md). The finite-order AFE and paired fourth moment give [the amplified numerator](../2026-10-29-unitary-amplified-numerator/README.md); the whole-tuple conductor ledger gives [the raised-line error bound](../2026-10-29-raised-line-error/README.md).

Insert these bounds into the original finite main/error expansion. Xu–Sang's first-stage exact rational certificate, independently reconstructed by `../2026-10-29-unitary-high-contour/check_endpoint.py`, gives a positive saving for the whole intermediate-row rectangle; the [moderate-row calculation](../2026-10-29-unitary-high-contour/README.md) includes the floor and supplies the full exponent. The [outer-row calculation](../2026-10-29-unitary-outer-rows/README.md) handles the small, bounded and distant nonprincipal rows. The [principal contour](../2026-10-29-hu-principal-contour/README.md) gives the same signal

    fψ(Z)=(2πi)^(−1) ∫_(Re s=2) Z^C_b(s) exp((s−5/6)^2)
                           Hψ^S(s)/L_K^S(s,ψ) ds,

where Hψ^S is holomorphic and nonzero to the right of B₀. Each real saving is fixed before the finite target twist. After all finite height orders are known, choose the target-specific height exponent and then the external tail order. Thus for some ρ>0 common to all later finite twists in the fixed type orbit,

    |Jψ(Z)−fψ(Z)| ≪ψ Z^(C_b(β)−ρ).                           (2)

The [family closure](../2026-10-29-unitary-family-closure.md) applies Mellin inversion to (1) and (2): its transform is holomorphic on `Re s>max(B₀,β−ρ)`, while its identified value has a nonzero numerator. It excludes all zeros there, contradicting the definition of β. Therefore β≤B₀. Conjugation and vertical translation restore the target removed by the source orientation.

For an arbitrary base field F, pass to K=F(μ₁₂) and use Hu's abelian descent, treating norm-character poles separately. Finally Hu's unitary Brauer induction and Frobenius reciprocity transfer the rank-one result and pole multiplicities to all finite-dimensional continuous unitary representations of the global Weil group. This completes the conditional implication. □

## Review boundary

Independent internal checks cover the elementary endpoint polynomial, Gaussian scale algebra, D1/D2 local exponents, amplified numerator algebra, dynamic contour under its inputs and outer powers. They do not independently prove Hu's full ramified Gauss table, theta/sector construction, moment inductions, source-to-physical mask matching or the global 7/8 theorem. An end-to-end adversarial integration review is still required before the conditional source list or the conclusion can be treated as a fully checked research result. The numerical gain over 7/8 is 9/80000 = 0.0001125, so even successful validation would be modest.
