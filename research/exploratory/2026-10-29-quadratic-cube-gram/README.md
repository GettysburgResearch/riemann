# Conditioning a cube-labelled Gauss frame via the quadratic Weyl bound

**Status.** A source-qualified elementary consequence of [Nelson's Theorem 1.1](https://arxiv.org/abs/1911.06310v3), conditional on the usual FHL reciprocity and conductor/mask identities. This 3/8 Gershgorin range is superseded by the squarefree-power frame, which conditions all R³ labels up to P^(1/2−δ) using the quadratic large sieve, and that frame also has a stronger P^(−1)H overlap mean. The useful Nelson consequence beyond square root is the independently checked [almost-full quadratic frame](../2026-10-29-quadratic-weyl-frame/README.md), which reaches P^(3/5−δ) in Hilbert–Schmidt average. No complement bound or zero-free region follows.

Work over K=Q(ω), with fixed good set S and a fixed finite source ray sector as in the [full Gram note](../2026-10-29-theta-partial-frame/full-gram.md). Let s range over good squarefree source ideals with Ns≈P under a fixed nonnegative smooth annular weight. Index inverse-oriented Gauss profiles by `h=a³`, for good squarefree a of `Na≤T`, using the same phase, common profile and normalizations as in that note. Since every character is zero on nonunits,

    χ_s(a³)=χ_s(a)³

is the zero-extended quadratic residue character. For each fixed δ>0 and `T≤P^(3/8−δ)`, the individually normalized Gram matrix satisfies

    ||Gram−I|| = o_(P→∞)(1),                                (1)

with an explicit small power after fixing all auxiliary losses. The full norms of the labels a³ may reach `T³=P^(9/8−3δ)`, beyond the general all-label `P^(1/2−δ)` full-norm range. But the stronger [squarefree-power frame](../2026-10-29-theta-squarefree-power-frame/README.md) already conditions this slice up to `T=P^(1/2−δ)` by the quadratic large sieve, so (1) is only a simpler alternative proof in a smaller range. This statement does not cover general sixth-free labels of that size.

For distinct a,b, reciprocity and a finite ray-character expansion turn the s-variable in `χ_s(a³)overline(χ_s(b³))` into a nonprincipal quadratic Hecke character χ_{a,b} times one of finitely many fixed unitary ray characters ξ, with its original deleted Euler factors. A good prime in the symmetric difference of a,b makes the quadratic character nonprincipal even after any fixed S-supported twist. Its finite conductor norm is `≪_S Na·Nb≤T²`. The squarefree s-Dirichlet series is

    L_K(z, ξχ_{a,b})/L_K(2z,(ξχ_{a,b})²)

up to exact finite Euler deletion factors. On `Re z=1/2+η`, the reciprocal denominator converges absolutely and the deletions cost `(Na Nb)^ε`. The fixed-ray numerator can be bounded by the consequence of Nelson explained in [the hybrid-gap note](../2026-10-29-nelson-hecke-hybrid-gap.md): for arbitrary quadratic χ and fixed unitary ξ,

    L_K(1/2+it,ξχ) ≪_(K,ξ,ε) Q_χ^(1/6+ε)(1+|t|)^A. (2)

It follows from Nelson's quadratic-twist theorem by taking the unitary Eisenstein representation `ξ|·|^{it} ⊞ ξ^(−1)|·|^(−it)`. The conductor of ξχ is comparable to that of χ up to factors depending only on ξ, and no cube-free restriction is needed. Interpolation and a Mellin shift of the common profile yield the normalized off-diagonal bound

    |Gram_ab| ≪ P^(−1/2+ε) T^(1/3+ε).                      (3)

The normalizing diagonal density is ≫T^(−ε), by squarefree ideal counting with the original mask `(s,a)=1`; the fixed-sector principal main term is positive and its standard shifted-line error is smaller in this range. There are O(T^(1+ε)) labels, so the off-diagonal row sum is

    ≪ P^(−1/2+ε) T^(4/3+ε)=o(1)

when T≤P^(3/8−δ). Gershgorin proves (1), absorbing the diagonal normalization into the losses. A fixed finite family of independent norm profiles is handled by the corresponding fixed-dimensional diagonal Gram blocks.

A weaker overlap follows from the already available moving-twist individual bound: it gives `|⟨m_P,v_(a³)⟩|≪P^(−1/2+ε)(Na)^(1/2+ε)` and therefore, by (1),

    ||Proj_(cube frame) m_P||² ≪ P^(−1+ε) T^(2+ε).          (4)

At P=Y^(6/5), inserting the unrestricted-row source operator bound `||T_(Y,P)||²≪Y^(41/30+ε)` makes the projected energy `≪Y^(1−(12/5)δ+ε)` for `T=P^(25/72−δ)`. The stronger paper 5 Theorem 6 average gives `≪P^(−1+ε)T` for this slice, as already used in the squarefree-power frame; hence (4) and the energy cutoff just derived are superseded. Neither argument controls cross terms involving the orthogonal complement.
