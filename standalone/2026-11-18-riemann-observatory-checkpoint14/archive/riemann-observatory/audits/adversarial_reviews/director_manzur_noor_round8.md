# Director adjudication: the exact jump transport and its anchor boundary

Date: 2026-11-17. I read Manzur–Noor arXiv2610.03568v1 in full, including (B)–(D), (11)–(14), (20)–(25), references and its assistance disclosure. Source SHA ba5c1ab46edf1dbef9741dd1e999ec492c0be59bc65d82cc7ac7dfab8520c076. I read both independent reconstructions audits/manzur_noor_anchor_prefix_skeptic62.md and audits/adversarial_reviews/witness62_manzur_noor_step_bridge.md, independently checked the unitary basis, exact Mellin factor, sharp norm, evaluation and zero propagation. This is a scoped source theorem/interface reconstruction, not a whole-paper Level2/3 or novelty claim. The source's zeta criterion is credited to its authors.

Let S be the unit-interval step subspace of L²([1,∞),dx/x²), with cell values b_n and squared norm Σ|b_n|²/[n(n+1)]. The map B from disk Hardy coefficients a_j is

    (Ba)_n=Σ_(j<n)a_j−n a_n,   n≥1.

It is exactly unitary. B e0 is the constant1; B ej equals −j on cell j and1 on all cells after j. Each has norm1, and distinct inner products vanish by telescoping. Orthogonality to all these vectors forces all tail sums, and hence all cell values, to vanish. This proves completeness, not merely a bounded embedding. For the source h_k, Bh_k=k[floor(x/k)−floor(x)/k].

If Jτ=B Tτ B^(-1), then its jump at n is n^(iτ) times the old jump. For M f(s)=∫_1^∞ f(x)x^(−s−1)dx,

    M(Jτf)(s)=(s−iτ) M f(s−iτ)/s,   Re s>1/2.

The rational factor is essential: Jτ fixes1, while bare vertical translation would not. The exact norm is

    ||Tτ||=||Jτ||=sqrt(1+τ²)+|τ|.

The upper follows from the boundary supremum of |(s−iτ)/s| on the ambient Hardy space and unitary vertical translation. For sharpness within S, approximate an ambient smooth compact test after the integer dilation U_m f(x)=sqrt(m) f(x/m) by its unit-step samples. The norm error is O_f(1/m), and Jτ U_m=m^(iτ)U_m Jτ. Thus S attains the same supremum in the limiting norm ratios. This improves the source's sufficient estimate1+2|τ|; priority is not assessed.

For any fixed nonprincipal χ put F=L(.,χ), Sχ(x)=Σ_(n≤x)χ(n), gχ,k(x)=Sχ(x/k)−Sχ(x)/k and Wχ=closed span{gχ,k:k≥2} inside S. Each has evaluation M gχ,k(1)=0. Since M f(1)=<f,1> has norm1,

    dist_S(Jτ gχ,k,Wχ) ≥ |F(1−iτ)| |k^(iτ)−1|/k.

This is unconditional and follows from the exact Mellin factor. Nonvanishing on Re s=1 makes it positive off resonance. No nonzero τ can leave all of Wχ invariant: simultaneous resonance for k=2,3 is impossible. This is independent of GRH.

If the unrestricted ordinary span approximates1 (in particular under the separately reconstructed fixed-character GRH theorem), integer dilations of1 show its closure is all S. Subtracting a small multiple of Sχ, whose evaluation is F(1)≠0, then gives Wχ=ker M(.,1) inside S. The displayed distance is consequently exact under that hypothesis. This is not a closure assertion in the entire ambient Hardy space.

Fix k≥2 and nonzero τ with k^(iτ)=1. Then

    Jτ gχ,k∈Wχ  ⇔  GRH for this fixed χ.

The forward GRH implication is the preceding kernel description. Conversely, membership forces F(ρ−iτ)=0 at every right-half-strip zero ρ of F: the annihilating evaluation at ρ leaves the factor k^(−ρ+iτ)−k^(-1), whose modulus cannot vanish for 1/2<Reρ<1. Iteration gives an arithmetic vertical progression of zeros. The primary fixed-modulus density bound quoted in Jutila1972 §1.1(1.1), independently inspected by both reviewers, bounds the whole character product, both ordinate signs, by exponent min(3/(2−α),2/α)(1−α)<1 for fixed α>1/2. It contradicts the resulting linear count. Euler-factor zeros of an imprimitive character are on Re0 and irrelevant; the functional equation transfers any left off-line nontrivial zero to the right for the same χ. The membership converse itself would hold without resonance, but there the unconditional evaluation already rules membership out.

The source criterion and this resonant variant do not control length. For τ≠0 the unique formal floor coefficients of Jτρ_k at primes p∤k are −(p^(iτ)−1)/k. At most one prime can be resonant, so infinitely many are nonzero. Thus even this one transported vector belongs to no finite ordinary length span. An independent ℓ² model in the proponent note has exact density, a norm1 group, perfect unconstrained approximation and fixed-prefix cost b/(1−b). It rigorously refutes inferring the subreciprocal prefix endpoint bound from bounded transport/density alone. The next precise arithmetic step still needs actual length-N polynomials satisfying every prescribed prefix coefficient.
