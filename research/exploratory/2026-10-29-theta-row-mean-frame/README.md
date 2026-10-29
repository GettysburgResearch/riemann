# A full-norm frame controlled by the angular theta row mean

**Status.** A source-qualified projection consequence of [rStation paper 5 v3, Theorem 5 and (9.4)](https://rstation.ai/problems/riemann_hypothesis/papers/5/v3), and the [full Gram estimate](../2026-10-29-theta-partial-frame/full-gram.md). The row-mean theorem imports the cited quasi-RH recursion and related analytic inputs; these are not independently verified here. This is not an inverse-moment bound or a zero-free region.

In the notation of the [theta-overlap note](../2026-10-29-cubic-theta-overlap-average/README.md), paper 5 defines `C_ℓ(n)=α(n)^ℓ γ₂(n)` for fixed nonzero integer ℓ. Its all-natural-row, unlabelled estimate (9.4), at ℓ=−1 and fixed finite ray twist ξ, gives

    Σ_(0<Nh≤H) |P_h(P)|² ≪_(ε,ξ,W) H(HP)^ε,                     (1)

where

    P_h(P)=P^(−1/2) Σ_(n good,sf) α(n)^(−1) γ₂(n) ξ(n)
                              χ_n(h) W(Nn/P).

The source permits one common smooth annular profile and fixed-polynomial dependence on its norm-twist height. The zero extensions are those of the source. The identity `μ(n)overline(γ₁(n))=α(n)^(−1)γ₂(n)` times a unit-modulus fixed-ray factor, followed by a finite ray-character expansion, identifies each overlap with a fixed finite combination of `P^(−1/2)P_h(P)`. Therefore

    Σ_(h good sixth-free, Nh≤H) |⟨m_P,v⁻_(P,h)⟩|²
       ≪_ε P^(−1)H(HP)^ε(1+|t|)^A.                            (2)

Restriction to sixth-free ideals, primary generators or any subset only decreases the positive sum in (1). The constants and height order A are fixed before the permitted height grows. This strengthens the earlier cube-split `H+H^(3/2)` overlap bound under paper 5's stronger source theorem.

For fixed δ>0 choose H=P^(1/2−δ). The full Gram estimate conditions all individually normalized v⁻_(P,h) with Nh≤H. Their column normalizations cost only H^ε, so their full-span projection obeys

    ||Proj_V m_P||² ≪_ε P^(−1)H(HP)^ε(1+|t|)^A.                 (3)

At P=Y^(6/5), the unrestricted-row sextic operator squared norm is `≪Y^(41/30+ε)`. Thus

    ||T_(Y,P) Proj_V m_P||² ≪Y^(23/30−6δ/5+ε)(1+|t|)^A.       (4)

This full-norm family includes every prime-power profile v_(p⁵) for Np≤H, but it does not include all sixth-free h of radical ≤H. The row mean also does not directly provide the same H-scale average for v_(p²): that orientation introduces the moving fourth-power label f=p, whereas (9.4) is the unlabelled f=1 statement. The separate [mixed-frame note](../2026-10-29-theta-mixed-radical-frame/README.md) records the weaker completed-theta estimate available for p². Neither projection estimate bounds `T_(Y,P)(1−Proj_V)m_P`, so no individual zero-free result follows.

Two source-qualified extensions reach beyond the range of uniform conditioning. The [almost-all frame](../2026-10-29-theta-almost-all-frame/README.md) retains `(1−o(1))` of the Gram eigen-directions up to full norm `H≤P^(128/231−δ)`. The [larger-cutoff partial frame](../2026-10-29-theta-row-mean-large-frame/README.md) reaches `H=P^(25/36−δ)` but guarantees only a power-sized fraction of the directions. Both control selected spectral subspaces, not the full profile span or the ambient complement.

**Independent source review:** Amplified_opt and Families checked paper 5 (9.4) at `C_{−1}`, finite-ray phase and sector decomposition, the `1/sqrt(Nn)` normalization, inverse orientation and h-prime zero masks. This is a review of source matching, not an independent proof of the imported theorem or the uncontrolled complement.
