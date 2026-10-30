# A fixed-order conjugate-exponent conductor sieve

**Status:** Source-dependent theorem and proof conditional on the cited large-sieve preprint. Computational, high_match and a separate line-by-line source replay have reviewed the rectangular sieve; their reviews are linked below. It extends the argument of De Faveri's cubic Proposition 8.1 to squarefree index ideals of any fixed order. It is a large-sieve estimate, not a zero-free region; no priority claim is made and the cited analytic inputs have not been independently established here.

Let n≥3 be fixed, let K be a fixed number field containing μ_n, and let S and the family `χ_q` be exactly those in [De Faveri, *Optimal large sieve for fixed order characters*](https://arxiv.org/abs/2610.04045v1), §§1–3. Use the original zero extensions. For A,B,Q≥1 write `a∼A` for `A≤Na<2A`, and set M=min(A,B), N=max(A,B). For every ε>0 and every complex λ supported on squarefree good ideals q∼Q,

    Σ_{a∼A} Σ_{b∼B} |Σ_{q∼Q, q squarefree} λ_q χ_q(a b^(n−1))|²
       ≪_{K,S,n,ε} (ABQ)^ε
          [AB + M^(1/n)N^(1−1/n)Q^(2/n)
              + M^(1−1/n)N^(1/n)Q] Σ_q |λ_q|².           (1)

The outer a,b sums range over all good ideals, without squarefree restrictions. Constants depend on the fixed character-family construction, not on λ or the scales. The result includes n=3 and recovers the published cubic proposition. It does not assert the same estimate for n-th-power-free but nonsquarefree q; the latter would require the additional root-number cross terms of the source's Lemma 3.3.

## Proof

The identity

    χ_q(a b^(n−1))=χ_q(a) overline(χ_q(b))               (2)

is exact, including zeros, because each χ_q has order dividing n. Swapping a,b conjugates the inner sum after conjugating λ, so the operator norm is symmetric in A,B. Assume A≤B and normalize `Σ|λ_q|²=1`.

We first record the general replacement for the source's cubic (8.3). If `𝓛₂(X,Y)` is the squared operator norm with unrestricted good row ideals of scale X and n-th-power-free column ideals of scale Y, De Faveri Lemma 6.1 and Theorem 1.1 give, for X,Y≥1,

    𝓛₂(X,Y) ≪_ε (XY)^ε [X+X^(1/n)Y
                          +X^(1−1/n)Y^(2/n)
                          +X^(2/n)Y^(1−1/n)].           (3)

Indeed Lemma 6.1 bounds 𝓛₂ by the maximum of `R·𝓛₁(X/R^n,Y)` for `1≤R≪X^(1/n)`. Reciprocity and the finite ray-class partition bound 𝓛₁ by the n-th-power-free Θ_n of Theorem 1.1. The four terms become at most the four displayed terms: the powers of R are respectively `1−n`, 1, `2−n`, and −1. This remains valid for squarefree columns, which are a subfamily. Fixed dyadic endpoint constants and `XY` powers are absorbed in ε.

Now repeat the argument of Proposition 8.1, whose analytic lemmas are stated for the fixed-order family, with (2) replacing its cubic identity. Insert a nonnegative smooth b-weight, expand the square, split the common factor `d=(q₁,q₂)`, and partition by the finitely many ray classes. The q_i are squarefree, so after writing `q_i=d q_i'`, the reduced q_i' are coprime and squarefree. The large-common-factor part `Nd≈Q` costs `≪(ABQ)^ε AB`. For the other ranges, the source's (3.5), Lemma 3.1 and Lemma 3.3 apply for arbitrary n: the reduced primitive character has conductor `q₁'q₂'`; its root number factors into one-variable phases when q₁',q₂' are squarefree. In Lemma 3.3 the `sharp` cross factors become fixed ray-class phases in this squarefree case. Fixed ramified and common-factor zero masks are retained by the source's divisor expansion; they cost divisor-bounded factors, not a new character identity.

Following the source's Mellin separation, GCD removal and Cauchy–Schwarz through the display immediately before (8.3), then inserting (3) and bounding its explicit monotone polynomial terms gives, for every localized dyadic range `d∼D`, `r∼R`, and e-scale E, a contribution bounded up to `(ABQ)^ε` by

    [BD/(QR)] · F_n(AE,Q/D) · Σ_{d∼D} Σ_{h∼Q/Nd}|λ_{hd}|², (4)

where F_n is the four-term bracket in (3). The source's intermediate kernel has column scale `Q/N(dg)`; the replacement by `Q/D` is made only after inserting (3), using monotonicity of F_n, not a monotonicity claim for its dyadic operator norm.

where `1≪R≪D≪Q` and

    1≤E ≪ (ABQ)^ε Q² R/(BD²).                           (5)

The source proves the preceding display with the same weights; (4) inserts the general-order 𝓛₂ estimate at the last step. The sum of the squared coefficients over d,h is divisor-bounded times the original norm. If the upper bound in (5) is below one, the localized range is empty. Summing dyadic ranges and fixed bad-prime classes costs an arbitrarily small additional power.

Put `X=AQ²R/(BD²)` and `Y=Q/D`. The prefactor `BD/(QR)` transforms the four terms of F_n into

    AQ/D,
    A^(1/n) B^(1−1/n) Q^(2/n) D^(−2/n) R^(1/n−1),
    A^(1−1/n) B^(1/n) Q D^(−1) R^(−1/n),
    A^(2/n) B^(1−2/n) Q^(3/n) D^(−3/n) R^(2/n−1).

All powers of D,R here are nonpositive for n≥3. Discard those powers; the resulting first term AQ is at most the resulting third term because A≤B. Let T₂, T₃, T₄ denote the resulting *global* versions of the second, third and fourth terms. Then:

    T₄/T₂=(AQ/B)^(1/n),
    T₄/T₃=(B/(AQ))^(1−3/n).

Thus T₄≤T₂ when `AQ≤B`, and T₄≤T₃ when `AQ≥B`; this includes equality for n=3. Add the diagonal AB term and undo the normalization to get (1). □

The proof imports the source's squarefree common-factor decomposition, primitive-character Poisson formula, and squarefree root-number splitting. It deliberately does not use a nonsquarefree q extension, a zero-density theorem, or a detector argument. Independent verification of the source lemmas and the above replay is still required before using the result.

## Conditional central second moment for the ±1-exponent subfamily

Assuming (1) and the source's standard approximate-functional-equation step, the cubic conductor-moment proof in De Faveri §8 also gives the following result for every fixed n≥3. Let ψ be a fixed unitary Hecke character of K. For A,B≥1 and ε>0,

    Σ_{Na≤A, Nb≤B} μ²(ab)
      |L(1/2, ψ χ_{a b^(n−1)})|² ≪_{K,S,n,ψ,ε} (AB)^(1+ε).  (6)

Here a,b are good integral ideals; μ²(ab) enforces squarefreeness and coprimality. This is the complete cube-free family when n=3. For n≥4 it covers only labels whose nonzero valuations are 1 or n−1; in particular it is **not** a conductor-ordered moment for all n-th-power-free characters.

For dyadic a∼A,b∼B, each χ_{a b^(n−1)} has conductor norm `≪_{K,S} N(ab)≪AB`, since the good primes dividing a or b appear with nonzero exponents modulo n and the bad conductor is fixed. Twisting by the fixed ψ changes this by a fixed factor. The approximate functional equation and Mellin separation used in [De Faveri, proof of Theorem 1.2, (8.4)](https://arxiv.org/html/2610.04045v1#S8.E4) reduce the moment, at a cost `(AB)^ε`, to squared ideal sums of length at most `(AB)^(1/2+ε)` with coefficients `ψ(j)χ_{a b^(n−1)}(j)/(Nj)^(1/2+η+it)`, with η>0 arbitrarily small and t in the source's truncated range. The finitely many principal or bounded-conductor exceptions are handled by the standard fixed-family bound, as in the cited proof.

Write each good index `j=q r²` with q squarefree, and split its fixed bad-prime part. Cauchy–Schwarz costs a convergent sum of `(Nr²)^(−1/2−η)`; the factor `χ_{a b^(n−1)}(r²)` has modulus at most one and can be dropped after taking absolute values. Reciprocity, with a finite partition of row and q ray classes, changes `χ_{a b^(n−1)}(q)` to a fixed class phase times `χ_q(a b^(n−1))`. The q-coefficients on each dyad have squared mass `≪1`. Thus (1) applies uniformly to each component. In the relevant range `Q≤(AB)^(1/2+ε)`, the two nontrivial terms in (1) are both `≪(AB)^(1+O(ε))`: after assuming A≤B, their ratios to AB are bounded respectively by `A^(2/n−1)` and `(A/B)^(1/2−1/n)`, apart from the harmless cutoff loss. The fixed bad-prime and r sums converge, yielding the dyadic moment. Summing dyads and renaming losses proves (6). □

The AFE step and uniformity in its auxiliary integrals are imported from the cited source proof; the preceding explanation identifies the only order-dependent steps. An independent review of this extension is still required. Formula (6) is a family moment, not an individual zero-free region and not a priority claim.

As a direct conductor-ordered corollary for this subfamily, the source conductor formula gives `N(ab)≤N cond(χ_{a b^(n−1)})`. Dyadically summing (6) over rectangles with `N(ab)≤X` yields

    Σ_{a,b good; μ²(ab)=1; N cond(χ_{a b^(n−1)})≤X}
       |L(1/2, ψ χ_{a b^(n−1)})|² ≪_{ψ,ε} X^(1+ε).   (7)

This again excludes middle valuation exponents when n≥4. In particular, for any fixed δ>0, at most `O(X^(1−δ))` such labels can have central value larger than `X^δ`, after choosing the moment loss below δ. The latter follows by Markov from (7); it is an almost-all central-value consequence, not a zero-free assertion.

**Independent review:** A second researcher checked the general-n replay, squarefree root-number splitting, two corrected localized exponents, the AFE q r² decomposition, conductor and ray classes, and the central-moment exponent arithmetic. The proof remains conditional on the cited preprint's analytic lemmas and AFE uniformity; the reviewer did not independently establish those inputs.

## Conditional zero density for the same subfamily

Assume (1), and assume the **fixed-field buffered zero detector** described below with its uniform height/profile losses. For every fixed σ with `3/4<σ<1` and ε>0 there exists τ>0 such that, for X≥2,

    Σ_{a,b good; μ²(ab)=1; N(ab)≤X}
      #{ρ: L(ρ,ψχ_{a b^(n−1)})=0,
            Re ρ≥σ, |Im ρ|≤X^τ}
       ≪_{K,S,n,ψ,σ,ε} X^(5/2−2σ+ε).                   (8)

Zeros are those of the primitive inducing character and are counted with multiplicity. The same bound holds when the indexing condition `N(ab)≤X` is replaced by `N cond(ψχ_{a b^(n−1)})≤X`: outside S and the fixed conductor of ψ every p|ab is tamely ramified, and the omitted fixed primes contribute only a fixed factor. The fixed unitary ψ may have any fixed archimedean type; any extra finite presentation twists must belong to one fixed finite set, with conductors and types fixed before X. The theorem is conditional on the source-dependent detector transfer spelled out below, as well as (1); no claim is made for arbitrary growing twists or for labels with middle local exponents.

To prove (8), first derive the only required moment. For a squarefree-index inverse polynomial of length Q, with a common fixed ray twist and normalized coefficient squared mass `≪X^ε`, dyadically partition a,b with `AB≪X` and apply (1). If M≤N and MN≪X, its off-diagonal terms obey

    M^(1−1/n)N^(1/n)Q ≤ X^(1/2)Q,
    M^(1/n)N^(1−1/n)Q^(2/n)
       ≤ X^(1−1/n)Q^(2/n) ≤ max{X,X^(1/2)Q}.

The last comparison splits at Q=X^(1/2). After summing `O(log²X)` dyads and the finite ray classes, every fixed inverse profile therefore satisfies

    Σ_{N(ab)≤X} |M_r|² ≪ X^{max(1,1/2+r)+ε},  Q=X^r,   (9)

with the fixed polynomial profile/frequency cost supplied by the source detector. Coefficients retain their Möbius signs, common ray twist and original ramified zero masks; (9) follows because the sieve is uniform in the coefficient vector. The fixed-ψ conductor can add finitely many primes to the mask without enlarging the bound.

The detector input is the [fixed-field saturated-detector replay](../2026-10-29-fixed-field-saturated-detector/README.md), based on the fixed-number-field analogue of [OpenAI Proposition 8.3 and Lemmas 8.1–8.2](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf), together with the fixed-type treatment in [Hu, Lemma 3.3 and proof of Proposition 6.3](https://hexagonmath.org/2610.00216v1). Concretely, for an arbitrarily small fixed detector/bin loss κ>0 chosen before X grows, bin each row's finite presentation family by a buffered zero maximum a, apply the detector at parameter t=1, and partition the boundedly many presentation and dyadic length choices. The input supplies

    r+m≥1−O(κ),   r≤1+O(κ),   m≤1/2+O(κ),
    |M_r|² ≥ X^{(2a−1)r−O(κ)}.                         (10)

The proof uses the primitive functional equation, polynomial vertical-strip bounds, a zero-free disk to the right of that row's buffered maximum, and bounded-degree gamma factors. These statements hold for the fixed field and fixed ψ type; nevertheless the complete transfer of the source detector to every listed family presentation, including deleted Euler factors, all profile derivatives and its one cumulative height allowance, is a **source-dependent bridge**, not independently proved in this note. The original row character and its primitive inducing function have the same zeros in Re(s)>0 because deleted Euler factors do not vanish there. Finitely many bounded-conductor/principal labels are absorbed.

From (10), `r≥1/2−O(κ)`. Chebyshev with (9) counts each witness fiber by

    X^{max(1,1/2+r)−(2a−1)r+ε}
       ≤ X^{3/2−(2a−1)+ε+O(κ)}
       = X^{5/2−2a+ε+O(κ)}.                         (11)

Indeed for r≥1/2 the exponent is `1/2+(1−(2a−1))r`, maximized at r=1; the small buffered excursions cost O(κ). A zero with real part at least σ puts its row in a bin with `a≥σ−O(κ)`. Sum the finite bins and logarithmically many dyadic choices. Choose κ sufficiently small relative to ε before X grows, and then choose τ sufficiently small after the detector's fixed polynomial height and profile orders are known; absorb their `X^{O(τ)}` cost, as well as the standard individual zero-count factor `O((X^τ+1)log X)`, into ε. This proves (8) under the detector input. □

For example, at σ=4/5 the exceptional count is `O(X^{9/10+ε})` for some sufficiently small positive τ. For fixed σ>3/4 choose ε<2σ−3/2. The exceptional number in (8) is then `o(X/log X)`. The family contains at least `≫X/log X` distinct primitive characters: good prime labels g=p have conductor supported at p and bounded fixed bad primes, so distinct p give distinct conductors; choose `Np≤X/C` for the fixed conductor constant C. Multiplying by fixed ψ preserves distinctness. Consequently a proportion tending to one of the distinct characters in this ±1-exponent family have **no zeros** in `Re s≥σ, |Im s|≤X^τ`. This is a density-one family rectangle, not a uniform zero-free region for every character or a zero-free assertion at unbounded heights. For n=3 the subfamily is the full cube-free family; for n≥4 labels carrying exponents other than 1 or n−1 remain outside the statement. No priority or comparison claim is made.

The independent computational review is [here](../../../reviews/2026-10-29-conjugate-conductor-sieve/README.md), and the detailed source-by-source replay is [here](audit-literature.md). These checks do not independently prove the imported analytic lemmas. Two independent internal checks verified the density exponent, dyadic moment algebra, global conductor scale and fixed-loss bookkeeping; they treat the general-field fixed-type detector and its differentiated-profile transfer as substantive imported hypotheses, not independently established theorems.
