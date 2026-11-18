# Director adjudication: a precise tail deficit criterion

Date: 2026-11-17. Two independent reconstructions: effective_cluster62_suzuki_finite_certificates.md §§1–3 and prefix_skeptic62_suzuki_landau.md. I checked the primary Suzuki Aspects paper's transform and zero sum, and independently reconstructed the compensation, Landau argument and residues. The argument is an ordinary application of classical nonnegative Laplace-transform theory. Priority unassessed; Suzuki already uses Landau for positivity and treats modified shifted functions in §11.

Use the unshifted real function Ψ(t)=−g(t), normalized by

    Ψ(t)=Σ_(ξ(1/2−iγ)=0) mγ(1−e^(iγt))/γ²,
    Laplace Ψ(u)=ξ'(1/2+u)/[u² ξ(1/2+u)]   (Re u>1/2).

The zero sum is locally normally convergent; no central zero occurs and Σmγ/|γ|²<∞. For every fixed real ω≥0 the following are equivalent:

    ∃C,T≥0 ∀t≥T: Ψ(t)≥−C e^(ωt);
    ξ has no zero in Re s>1/2+ω.

The boundary is allowed. If the second assertion holds, symmetry bounds |Imγ|≤ω; absolute summation gives |Ψ(t)|≤S(1+e^(ωt)). Under RH the cosine-paired sum is nonnegative.

For the reverse let f=1_[T,∞)(Ψ+C e^(ωt))≥0. Its Laplace transform, initially far right, continues meromorphically as

    ξ'/[u²ξ](1/2+u)+C/(u−ω)
       −∫_0^T [Ψ(t)+C e^(ωt)]e^(−ut)dt.

The finite integral is entire. If the convergence abscissa a were finite and >ω, this expression would be regular near real a: ξ has no real zero for real argument>1/2, including its nonzero removable value at1. Nonnegative Laplace Landau theory forbids such regularity at a finite abscissa. A self-contained proof uses the Taylor series at a nearby real point b>a, its nonnegative moment coefficients, and Tonelli to force convergence at a real x<a. Thus a≤ω (or a=−∞). The transform is analytic on Re u>ω. Each zero ρ past the stated line would produce a genuine pole with nonzero residue mρ/(ρ−1/2)², which neither the compensator nor finite integral can cancel. This proves the claim, including ω=0. For ω≥1/2 the standard zero strip already supplies the condition.

A polynomial factor t^K in the permitted deficit yields the same open half-plane by allowing every ω+ε and then exhausting ε↓0. If a zero lies strictly past the line, negating the quantified eventual bound gives liminf e^(−ωt)Ψ(t)=−∞. This result supplies no such lower bound for the actual zeta Ψ at ω<1/2.

For the correctly normalized merged screw line, the tail estimate D(t)=||S_t||²/(2π)−Ψ(t)≤C e^(ωt) is sufficient, since its norm is nonnegative. A finite norm certificate or a finite Gram check proves no all-tail estimate. The proponent's bounded-time spectral countermodels are retained as model evidence, not as actual zeta counterexamples and not as a completed independent audit. The next precise step would be a certified unconditional tail comparison at a nontrivial ω, which is mathematically comparable in strength to the corresponding zero-free assertion. Recasting the missing tail as a positive norm does not resolve it.
