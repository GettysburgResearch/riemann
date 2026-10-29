# A quadratic Weyl-bound frame past the square-root cutoff

**Status.** A source-qualified partial spectral result using [Nelson, Theorem 1.1](https://arxiv.org/abs/1911.06310v3), paper 5 v3 Theorem 6 and the cited sixth-order source operator bound. It gives an almost-full spectral subspace of a particular quadratic Gauss-profile family, not a bound on its ambient complement or a new zero-free region. Independent review requested.

Use the coefficient vector, Gauss profiles, fixed ray-sector source rows, normalizations and bad-prime zero masks of the [squarefree-power frame](../2026-10-29-theta-squarefree-power-frame/README.md). Let `A` have as columns the normalized original profiles `v_(P,R³)` for good squarefree ideals R with `NR≤H`, one primary generator per ideal. Write N≈H for their number and G=A*A.

For distinct R,T, the moving quotient is a nonprincipal quadratic Hecke character χ of conductor `Q≪NR NT` up to a fixed bad-prime factor. At a good prime where the squarefree labels differ it is ramified. The fixed source-sector and reciprocity expansions can multiply it by any of finitely many fixed unitary finite-ray characters ξ; these need not themselves be quadratic. Nelson's Theorem 1.1 nevertheless gives the required hybrid Weyl bound uniformly for such ξ: choose the unitary Eisenstein representation

    σ = ξ|.|^(it) ⊞ ξ^(−1)|.|^(−it).

Since χ is quadratic, `L(σ⊗χ,1/2)=|L(1/2+it,ξχ)|²`. The theorem's `C(χ)^(1/3+ε)` bound and its polynomial dependence on `C(σ)` imply

    L(1/2+it,ξχ) ≪_(ξ,ε) Q^(1/6+ε)(1+|t|)^A.              (1)

This uses the **quadratic** theorem with arbitrary full conductor, not Nelson's separate cube-free nonquadratic theorem. Finite S factors, old source zeros and variable deletions cost `(NR NT)^ε`; interpolation to `Re s=1/2+η` and the squarefree Dirichlet-series identity then give

    |G_(R,T)| ≪ P^(−1/2+ε)(NR NT)^(1/6+ε)
               ≪ P^(−1/2+ε) H^(1/3+ε).                    (2)

The denominators `L(2s,(ξχ)²)` are bounded by absolute Euler products on this line. The fixed ray sectors, source profiles and unit choices are handled exactly as in the earlier Gram proof; individual column normalizations cost H^ε.

Consequently

    ||G−I||_HS² ≪ P^(−1+ε) H^(8/3+ε),
    #{λ(G)∉[1/2,3/2]}/N ≪ P^(−1+ε) H^(5/3+ε).             (3)

For any fixed δ>0, taking `H=P^(3/5−δ)` and choosing losses below the margin retains `(1−o(1))N` Gram eigenvalues in `[1/2,3/2]`. Their image V_mid under A has the same dimension. These directions are spectral combinations, not a claim that every named `R³` profile is well conditioned.

Paper 5 Theorem 6 (12.2), with the squarefree core and angular order −1, supplies the overlap mean

    ||A*m_P||² ≪ P^(−1+ε)H(1+|t₀|)^B,                       (4)

where t₀ is the source norm-twist height and its fixed polynomial cost is separate from the Mellin variable t in (1). Thus

    ||Proj_(V_mid)m_P||² ≪ P^(−1+ε)H(1+|t₀|)^B.             (5)

At `P=Y^(6/5)`, the full-row sixth-order source operator satisfies `||T_(Y,P)||²≪Y^(41/30+ε)`, giving

    ||T_(Y,P)Proj_(V_mid)m_P||²
       ≪ Y^(133/150−6δ/5+ε)(1+|t₀|)^B.                     (6)

When `δ<1/10`, the earlier full-norm and squarefree-power mixed span, whose dimension is `O(P^(1/2+ε))`, can be intersected away: `V_mid∩V_old^⊥` still has `(1−o(1))N` dimensions and obeys the same projection and energy bounds. The ambient source complement and its mixed term remain uncontrolled. All fixed-profile choices, smooth norms, source positivity and the height budget are as in the cited notes.

**Independent reviews.** Literature checked the Nelson unitary-Eisenstein specialization with fixed nonquadratic ray twists and polynomial height dependence. Families checked the quadratic quotient, sector and deletion masks, Euler denominator, Hilbert–Schmidt calculation, spectral projection and energy exponents. Both reviews retain the source theta and operator estimates as imported inputs.

High_match independently checked the same Nelson specialization, nonquadratic fixed sector twists, good-prime nonprincipality, deletion masks, Hilbert–Schmidt threshold and energy exponent.
