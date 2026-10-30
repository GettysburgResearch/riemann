# A proposed rectangular sieve for conjugate-power rows

**Status:** Proposed extension of De Faveri's cubic Proposition 8.1, conditional on his general-order large sieve and the stated source transform/reciprocity identities. The displayed exponent algebra is exact; the full source-to-general-n proof, especially root-number separation, masks and dyadic summation, is under independent review. This note does not claim a zero-free region or priority.

Fix n≥3, a number field K containing μ_n and the fixed good set S and character family of [De Faveri, arXiv:2610.04045v1](https://arxiv.org/abs/2610.04045v1), §§2–3. Let A,B,Q≥1 and set M=min(A,B), N=max(A,B). For arbitrary squarefree good-ideal coefficients λ_q, the proposed bound is

    Σ_(a≈A,b≈B) |Σ_(q≈Q, q squarefree) λ_q χ_q(a b^(n−1))|²
       ≪_(K,S,n,ε) (ABQ)^ε [AB
          + M^(1/n) N^(1−1/n) Q^(2/n)
          + M^(1−1/n) N^(1/n) Q] Σ_q |λ_q|².            (1)

The outer sum allows arbitrary good ideals a,b; a fixed restriction such as μ²(ab)=1 may be imposed by positivity. The original noncoprime zero extensions are retained. At n=3 (1) is exactly the cubic Proposition 8.1, after ordering A≤B. The new proposed range n>3 is **not** asserted in that proposition.

## Source-based derivation and point to audit

The identity

    χ_q(a b^(n−1)) = χ_q(a) conjugate(χ_q(b))

holds also at zeros, since each source character takes values in μ_n∪{0}. The norm in (1) is symmetric in A,B after conjugating λ, so assume A≤B. In De Faveri's proof of Proposition 8.1, expand the b sum, separate the common divisor of the two squarefree column ideals, split the fixed reciprocity ray classes, and apply his general Poisson formula and Lemma 3.3. The squarefree residual columns make the cross root-number factors in Lemma 3.3 trivial, so the remaining two column weights separate. These steps use the conjugate-product identity above, and the cited Lemmas 3.1 and 3.3 are stated for general n; the explicit general-n replay and all mask conventions are still a review gate here. The diagonal gives AB.

For the remaining localized dyadic source variables D,R with 1≤R≤D≤Q, the last stage of the source argument reduces to a prefactor `BD/(QR)` times an unrestricted-row character operator `L_n(X,Y)` at

    X=A Q² R/(B D²),       Y=Q/D,                          (2)

up to a subpower factor and a coefficient mass summable by the source's divisor bound. General-n Theorem 1.1 and n-th-power removal give, with squarefree columns,

    L_n(X,Y) ≪ (XY)^ε [X + X^(1/n)Y
                   + X^(1−1/n)Y^(2/n) + X^(2/n)Y^(1−1/n)]. (3)

The row is unrestricted in (3); fixing each n-th-power part and summing it gives these four terms. The last three n-th-power summations respectively use exponents 0, n−1 and 2, and are convergent except for the explicitly counted X^(1/n) factor.

Substituting (2) into (3) and multiplying by BD/(QR), the four nonnegative terms are

    A Q / D,
    A^(1/n)B^(1−1/n) Q^(2/n) D^(−2/n) R^(1/n−1),
    A^(1−1/n)B^(1/n) Q D^(−1) R^(−1/n),
    A^(2/n)B^(1−2/n) Q^(3/n) D^(−3/n) R^(2/n−1).

All D and R powers are nonpositive for n≥3. Since A≤B, the first is bounded by the third with D,R dropped. Call the remaining second, third and fourth terms T₂,T₃,T₄ after D,R are dropped. The exact ratios are

    T₄/T₂ = (A Q/B)^(1/n),
    T₄/T₃ = (B/(A Q))^(1−3/n).

If Q≤B/A, then T₄≤T₂; if Q≥B/A, then T₄≤T₃. Hence the source's fixed-number dyadic sums and divisor losses give (1), provided its post-reflection reduction is indeed valid with the general-n kernel and phases. For n=3 the two ratios make T₄=T₃ identically, as in the printed proof. □

## Possible density consequence

Restrict to coprime squarefree a,b and the family `χ_(a b^(n−1))`, possibly multiplied by a fixed unitary Hecke twist whose conductor primes are in S. Its primitive good conductor is exactly rad(ab)=ab, with a fixed S-supported factor, and its original zero masks remain. Finite-ray reciprocity converts the inverse Möbius block of `χ_(a b^(n−1))` to the squarefree q kernel in (1). The Sobolev grouping in [the cubic note](../2026-10-29-cubic-detector-sobolev/README.md) uses only arbitrary q coefficients and is formally independent of n.

If (1) and the fixed-field saturated detector apply with these source conventions, then on a row box AB≈U and a normalized inverse block D=U^r, (1) gives exponent

    E_γ(r)=max{1, 1−1/n−γ(1−2/n)+(2/n)r,
                    1/n+γ(1−2/n)+r},
    γ=log_U M ∈ [0,1/2].

The detector with t=1 supplies `r∈[1/2,1]` up to arbitrarily small fixed losses and a squared inverse spike U^(δr), δ≥2σ−1−O(e). For σ>3/4, hence δ>1/2 after losses, the first nontrivial term minus δr is at most `1−δ/2` (use γ≥0 and 2/n≤2/3); the second is at most `3/2−δ` (use γ≤1/2 and r≤1). More directly for n=3, its positive slope on part of the range is handled at r=1 and remains below `3/2−δ`. Thus the uniform exponent is at most `3/2−δ=5/2−2σ`, with the usual arbitrarily small loss. The dyadic/conductor and small-height argument in the cubic note would then give an exceptional-count bound X^(5/2−2σ+ε) at some sufficiently small power height, for this **conjugate-power subfamily**, not all n-th-power-free characters.

No part of this possible consequence should be quoted until the general-n rectangular sieve, detector matching and prior literature have been independently checked. The user-requested zeta/Dirichlet region is not affected by this conditional density calculation.
