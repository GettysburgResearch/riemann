# Independent review: powering the source character family

This reviews the compatible-choice bridge in [the full-order note](README.md) against de Faveri, [§§2.2–2.3](https://arxiv.org/abs/2610.04045v1), and the quadratic endpoint against Goldmakher–Louvel, [Definition 1, Remark 3, Theorem 1.1 and Corollary 1.2](https://arxiv.org/abs/1112.1642). It is a written source audit, not a Lean formalization. The general-order conjugate-pair sieve needed later is still a source-proof replay, not a theorem independently established by this review.

Fix n=dm, j=dk, gcd(k,m)=1. De Faveri chooses S, c, `R_n=H_c⊗Z/n`, a basis of `R_n≅(Z/n)^r`, and good ideal and S-integer representatives E_i,m_i with `E_i O_S=m_i O_S`. The same S,c also meet the order-m local-power condition. The natural quotient `H_c/nH_c→H_c/mH_c` is surjective; the chosen n-basis maps to a generating r-tuple in `R_m≅(Z/m)^r`, hence a basis. The same E_i,m_i are therefore permitted order-m choices, and their representatives use exponents reduced modulo m.

For coprime good ideals q,b, take the source decomposition `q=(x)E_t G^n` with `x≡1 (mod c)` and `(G,b)=1`. Write t=t₀+mℓ coordinatewise and define `G'=G^d ∏E_i^ℓ_i`. Then

    q=(x)E_t₀(G')^m,
    x m_Et = x m_Et₀ (∏m_i^ℓ_i)^m.                              (1)

The second display uses the source's multiplicative definition of m_E. The m-family decomposition additionally requires its power ideal to be coprime to b. Since b is good and c is S-supported, weak approximation supplies `z∈K×` with `z≡1 (mod c)` and prescribed valuations `v_p(z)=−v_p(G')` for p|b. Replace G' by `(z)G'` and x by `x z^(−m)`. This preserves the ideal identity and the congruence, and makes the adjusted power ideal coprime to b. Both symbol numerators are b-units: their good valuations match the corresponding E ideals because `E O_S=m_E O_S`, and q and the respective power ideal are coprime to b. Their ratio is `(z∏m_i^ℓ_i)^m`; because the ratio is a b-unit, so is the displayed root.

The order-n and order-m residue symbols use the same field embedding and satisfy `(α/p)_n^d=(α/p)_m` at every good prime p; extend multiplicatively over b. Therefore

    χ_q^(n)(b)^j = χ_q^(m)(b)^k                               (2)

for these compatible choices whenever (q,b)=1. Both sides retain the source's zero when (q,b)≠1. The k-th power is an automorphism of μ_m; an embedding of the cyclotomic subfield with this action extends to a complex embedding of K. This matches the source's allowed fixed embedding change. The family choices are fixed once for all q,b, even though the auxiliary decomposition and z may depend on the pair; source well-definedness makes (2) independent of that choice.

## Quadratic singleton

For even n, no separate reconstruction of a quadratic family is necessary for the large-sieve inequality. Goldmakher–Louvel Definition 1 explicitly treats the Fisher–Friedberg/Friedberg–Hoffstein–Lieman primitive Hecke families, §2 constructs them with the same S,c,E data, and Remark 3 states that their n/2-th powers form a quadratic family. Their Corollary 1.2 directly bounds the matrix `χ_b(a)^(n/2)` on squarefree good a,b by `(MN)^ε(M+N)∑|λ_b|²`. At good primes dividing squarefree b the original local character has exact order n, so its n/2-th power is ramified of order 2 and has the same good-prime zero mask. On ideals coprime to c the primitive inducing character agrees with the original zero-extended source presentation; the fixed c-supported factors do not create missing good-prime terms. De Faveri's §2.3 gives the same FHL construction, so the compatible data give the required matrix orientation directly.

The audit does not establish de Faveri's analytic theorem independently, the separately derived rectangular conjugate-pair generalization, the detector/profile replay, or an exhaustive literature-priority comparison. Those remain inputs and qualifications of the full-order density claim; no individual zero-free region follows from this matching.

For precise source navigation, Goldmakher–Louvel §2, pp. 3–4, constructs the FHL symbols from S,c,E,m_E and derives `f_a=c_a a*`; the first paragraph on p. 5 explicitly reuses χ_a for the primitive inducing character and checks the Hecke-family axioms. Corollary 1.2 on p. 2 then applies directly to its n/2-th powers. The comparison with de Faveri's §2.3 is at the level of these fixed choices, not merely of matching local conductors.
