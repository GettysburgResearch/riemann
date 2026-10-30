# Common-coefficient control for rowwise cubic inverse witnesses

**Status:** An elementary Sobolev reduction from the stated rectangular cubic sieve, proposed for independent review. It does not prove the saturated zero detector or the cited arithmetic sieve. The purpose is to remove a specific uniformity ambiguity in [the conductor-density derivation](../2026-10-29-cubic-conductor-detector/README.md).

Fix K containing μ₃, De Faveri's good set S, a fixed unitary character ν, and a dyadic box `Na≈A`, `Nb≈B`. Put U=AB, M=min(A,B), N=max(A,B). Assume [De Faveri Proposition 8.1](https://arxiv.org/abs/2610.04045v1), its finite-ray reciprocity law and original zero masks. Fix a common inverse dyad D, with D and U in prescribed polynomial ranges, and a smooth W supported in a fixed compact annulus. Let V be a fixed smooth inverse cutoff. For each row g=a b² put

    F_g(v,t)=D^(−1/2) Σ_(q good) μ_K(q) ν(q)χ_g(q)
               W(Nq/D) V(Nq/U) (Nq/D)^(−v−it),

where `v` lies in a fixed compact real interval and `|t|≤T`, T≥1. Then, for every ε>0,

    Σ_(a≈A,b≈B, μ²(ab)=1) sup_(v,|t|≤T) |F_g(v,t)|²
       ≪_(K,S,ν,W,V,ε) (1+T) (U D)^ε
          [U + M^(2/3)N^(1/3)D + M^(1/3)N^(2/3)D^(2/3)].  (1)

The same conclusion holds for conjugate presentations, fixed row subsets and a fixed finite collection of annular windows. Constants are uniform in the rows and the continuous choices v,t. A fixed finite number of additional bounded real profile parameters is allowed at the cost of finitely many derivatives and a fixed polynomial factor in their interval sizes. In particular, with T=U^τ the additional factor can be absorbed into an arbitrarily small U-power by choosing τ afterward.

## Proof

Fix the finite reciprocity ray class of g and split q into its finitely many ray classes. Source reciprocity makes χ_g(q) a fixed class-dependent unit scalar times χ_q(g) when (g,q)=1; when (g,q)≠1 both original symbols vanish. Absorb the scalar, μ_K(q), ν(q), the fixed class cutoff and the displayed profile into a row-independent vector λ_q. The Möbius factor makes q squarefree, as required by Proposition 8.1. Conjugating a whole presentation conjugates the coefficient vector and the kernel and does not change its absolute square. The restriction μ²(ab)=1 can be dropped from the positive row sum when applying the proposition.

For fixed v,t, and for every mixed derivative ∂_v^i∂_t^j with i,j∈{0,1}, differentiation only multiplies the coefficient by a bounded power of `log(Nq/D)` on the fixed annulus. Thus

    Σ_q |∂_v^i∂_t^j λ_q|² ≪ D^(−1) #{q: Nq≪D} ≪_K 1,

uniformly in v,t and the dyadic scales. The derivatives of the fixed cutoffs are likewise uniformly bounded. Proposition 8.1 therefore bounds the row sum of each differentiated |F_g|² by the bracket in (1), up to `(UD)^ε`; the finite class partition costs a fixed constant.

Cover the v interval by a fixed number of unit intervals and the t interval by O(1+T) unit intervals. On each unit rectangle, one-dimensional Sobolev in v and then in t gives

    sup_rectangle |F_g|² ≪ Σ_(i,j∈{0,1}) ∫_rectangle |∂_v^i∂_t^j F_g|² dv dt.

Sum over rows and rectangles, then use the uniform fixed-parameter sieve bounds. This yields (1). The inequality is applied to the sum of rowwise suprema; it is not an inference from a pointwise moment bound without derivatives. A fixed factor of `D/U` in the cutoff is common within the dyadic box. If that ratio is allowed to vary in a compact interval, the same argument adds one parameter and its bounded derivative. □

## Boundary

The witness construction still has to show that its inverse profile is exactly a member of this finite-dimensional family, up to a fixed finite sum, and that its twist frequency lies in the shared detector allowance. The [fixed-field detector note](../2026-10-29-fixed-field-saturated-detector/README.md) identifies those profile parameters but remains source-dependent. The proof here does not cover arbitrary row-dependent coefficients or a varying unitary twist ν.
