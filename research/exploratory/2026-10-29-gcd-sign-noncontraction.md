# Auxiliary gcd signs, their Euler series, and the unit branch

**Status.** These are exact elementary observations on the signed auxiliary-gcd expansion in the [mask-preserving second-Poisson note](2026-10-29-mask-preserving-second-poisson.md). They do not bound the full signed physical sum, prove an operator lower bound, or settle whether a more refined, coefficient-specific argument contracts.

Take distinct good squarefree n₁,n₂ in a fixed reciprocity sector, and define the cubic quotient character in its g-variable by

    ξ(g)=χ_{n₁}(g)^4 overline(χ_{n₂}(g)^4),

with the original nonunit zeros. After finite ray-sector expansion, each term is a Hecke character; at a good prime dividing exactly one of n₁,n₂, its local component is nontrivial of order three, so multiplying by a character of the fixed bad-prime ray group cannot make it principal. The primitive conductor is supported on the good radical of n₁n₂ and the fixed bad set, with norm ≪N(n₁n₂) times a fixed factor in the stated family.

For any fixed finite good mask B, the complete weighted series is, for Re s>1,

    Σ_{g good, (g,B)=1} μ(g) ξ(g)/(Ng)^s
      = L_S(s,ξ)^(−1) ∏_{p|B, p∉S} (1−ξ(p)/(Np)^s)^(−1).      (1)

The good-prime restrictions and any primes at which ξ already vanishes are retained in this formula. The Hecke nonvanishing theorem says L(1,ξ) is finite and nonzero for fixed nonprincipal ξ. Every finite Euler factor in (1) is nonzero at s=1. Thus the fixed-character cumulative series has a finite **nonzero** limiting value at s=1, justified by the fixed-character prime ideal theorem and partial summation. One cannot claim that this complete reciprocal-L sum cancels to zero. This statement does not apply to the artificial theta diagonal: its exact cancellation is the separate finite identity `Σ_{g|r}μ(g)=0` for r≠1, before auxiliary-g dyad localization.

Conversely, a single smooth annular g dyad is not the cumulative series (1). For any fixed ξ, a fixed smooth annular W satisfies

    Σ_g μ(g) ξ(g) W(Ng/G)/(Ng) = o(1)   (G→∞),             (2)

by the same fixed-character theorem; its implied rate is not uniform in a growing conductor. The physical kernels and masks depend on g,n₁,n₂,v,k and must be separated or kept explicitly before using (1) or (2). In particular (2) gives no useful power saving uniformly when `G≤Y^(1/5)` but the moving conductor can be as large as a fixed power of Y. Within the g=1 dyad there is only the unit term, so no cancellation occurs within that dyad; cancellation against other g dyads remains possible. The nonzero cumulative value in (1) likewise does not preclude joint cancellation among n₁,n₂,v,k or in the signed physical kernel.

A hypothetical estimate, for every fixed smooth W with uniform finite-seminorm control,

    Σ_g μ(g) ξ(g) W(Ng/G)/(Ng)
      ≪_{W,ε} Q_ξ^ε G^(−η+ε),                             (3)

uniformly in all such nonprincipal quotients and all G≥1, would have strong consequences: dyadic summation gives analytic continuation of `1/L_S(s,ξ)` to Re s>1−η for each fixed ξ, hence excludes all zeros of L_S there. For a putative zero ρ choose W≥0, smooth and supported in a sufficiently small fixed interval around 1, with positive integral. Continuity then makes its Mellin transform at ρ−1 nonzero, because the factor x^(ρ−1) is uniformly close to 1 on the support. This is an admissible annular test; no single arbitrary W is assumed nonvanishing at every zero. Thus (3) cannot be treated as a routine consequence of a fixed-character prime ideal theorem. A restricted `G≤Y^(1/5)`, `Q_ξ≲Y^C`, bound with only `Y^ε` losses implies the same fixed-character consequence if Y may grow and ε can be chosen arbitrarily small. These are implications, not counterexamples to (3).

## Why gcd bookkeeping alone gives no strict contraction

At the self-loop scales `D=Y^(6/5)`, choose N distinct good prime ideals nᵢ with norms in [D,2D], in one fixed ray class, and coefficients of absolute value N^(−1/2). For all i≠j their gcd is 1, so the signed gcd projector has only its unit-gcd term. Moreover every original row ideal u of norm ≤Y<D is coprime to every nᵢ, so the original source zero masks are identically one on these rows. The sum of absolute ordered-pair weights off the diagonal is N−1, versus N including the diagonal; its fraction tends to 1. Thus neither pairwise coprimality nor row-mask density gives an N-independent strict factor c<1 in the positive absolute/Cauchy ledger.

This is a countermodel only to a contraction based solely on those combinatorial losses. The actual oscillatory character Gram operator could exhibit cancellation or a spectral gap, and Möbius-specific structure could enable a different argument. Nor does the absolute-pair comparison show that the physical signed sum reaches its generic bound. At the unit gcd the reflected source scale is exactly the original inverse-moment scale, as detailed in [the self-loop note](2026-10-29-theta-inverse-self-loop.md).

**Independent review:** Families and High_match checked the nonprincipal quotient, masked Euler product, fixed-character convergence, annular decay and conditional Mellin implication. They also confirmed that the prime-pair argument addresses only combinatorial contraction and does not exclude cross-dyad or signed-operator cancellation.
