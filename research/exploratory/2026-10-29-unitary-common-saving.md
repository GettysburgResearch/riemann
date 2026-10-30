# Common saving and late target-dependent heights

This note isolates the quantifier step in the [unitary closure](2026-10-29-unitary-family-closure.md). It is an elementary conditional lemma, not a proof of the needed physical estimates or a new zero-free region.

Let β range over a fixed compact interval [B₀,B₁], let C(β) be continuous, and let targets ψ range over an arbitrary set. Suppose finitely many real margins c₁,…,c_J>0 and a slot system have been fixed independently of ψ. Assume that, for every fixed ψ, every ε>0, every positive integer N, every Z≥2 and every T≥1, the actual error Eψ(Z) satisfies

    |Eψ(Z)| ≤ Aψ,ε,N [ Σ_j Z^(C(β)−c_j+ε)(1+T)^(aψ,ε)
                         + Z^(bψ,ε) T^(−N) ].              (1)

Here aψ,ε,bψ,ε are finite and independent of N; Aψ,ε,N may depend on ψ, ε, N. The same β, slot system, original arithmetic masks and physical expression must be used in every term. Then there is ρ>0 depending only on the finitely many margins and the β interval, not on ψ, such that

    Eψ(Z) ≪ψ Z^(C(β)−ρ).                                   (2)

Proof. Put c=min_j c_j and ρ=c/4, ε=c/4. For each ψ choose τψ>0 with aψ,ε τψ≤c/4, and then choose Nψ so large that bψ,ε−Nψτψ≤min_{β∈[B₀,B₁]} C(β)−ρ. Set T=Z^τψ. The first sum has exponent at most C(β)−c/2; the tail has exponent at most C(β)−ρ. The target-dependent constants and threshold are harmless. □

Thus target-dependent height degrees alone do not destroy a family-wide saving: the height cutoff and the external decay order may be chosen after the target, provided the power margins and the physical slot system were fixed first and bψ,ε,aψ,ε do not grow with the requested tail order N. The latter is exactly the independent-order conclusion supplied in the abstract trace-tail setup, and it must be checked for each extra separated variable rather than inferred from a weighted L¹ norm.

For the proposed first-stage geometry one needs (1) for Eψ=Jψ−fψ, with c_j covering the principal approximation and contour remainders, the floor and moderate detector bins, and the two outer row ranges. Existing notes derive their exponents under source-facing hypotheses; they do not prove that Hu's variable-scale physical local identities, finite unit-sector recombination, retained-domain trace bounds, common-profile/height controls, and buffered detector estimates simultaneously establish (1) for exactly the same probe. In particular Hu Proposition 6.3 states the required integrated high-side conclusion only in its fixed (ℓ,b)=(1/6,1/8) geometry and under B>7/8. The abstract lemma above therefore removes no substantive analytic assumption and must not be used as a substitute for that source-to-physical bridge.
