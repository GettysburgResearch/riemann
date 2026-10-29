# Independent source audit: general-order conjugate rectangle

This audit checks the proposed squarefree-column replay against [de Faveri v1](https://arxiv.org/abs/2610.04045v1), particularly §§2.5, 3, 6 and 8. It takes the source statements as inputs and does not independently establish them. In particular, the printed Proposition 8.1 is cubic; the general-order rectangle is a derived, source-dependent proposition, not a verbatim citation. It does not establish the separate detector or Sobolev-profile transfer used by downstream density applications.

**Finding.** I found no cubic-only identity needed by the squarefree-column replay once the kernel is explicitly χ_q(a b^(n−1)) and the general-order L₂ estimate is substituted. The following checks identify precisely where the unprinted argument uses the source and why it cannot automatically be extended to nonsquarefree q.

1. Source §2.5.1 gives multiplicativity including the original zero extension on good ideals, and χ_q has order dividing n. Thus χ_q(a b^(n−1))=χ_q(a) overline(χ_q(b)) even at primes dividing q. Exchanging A and B conjugates the sum and coefficient vector. After expanding the squared norm and setting d=(q₁,q₂), squarefree qᵢ make the residual qᵢ′ squarefree, mutually coprime and coprime to d. The common d-character supplies the exact (a,d) and (b,d) zero masks; the b-mask is removed by the source's divisor expansion r|cd in (8.2), not by replacing it with 1.

2. After fixing a ray sector, source Lemma 2.4 gives conductor q₁′q₂′ for the primitive quotient; its good local characters are primitive and the fixed bad parts cancel by (3.5). In the non-diagonal range D<Q/2, the residual pair cannot both be the unit ideal, so this quotient is nonprincipal. Lemma 3.1 applies at its actual conductor; Poisson reverses the conjugate b-quotient and aligns it with the a-quotient. The zero dual ideal vanishes by nonprincipality. The d≈Q diagonal is handled separately by the source's trivial AB estimate.

3. In Lemma 3.3, for squarefree qᵢ′ the extra-power ideals qᵢ′^flat equal 1 and qᵢ′^sharp=qᵢ′. Therefore the two cross-symbols disappear. The remaining η depends on finitely many ray classes and is fixed in the sector; β_{q₁′} and conjugate β_{q₂′} are one-column phases. This is valid for general fixed n in the source lemma. When qᵢ′ are nonsquarefree the extra-power symbols need not split, so this audit gives no such extension.

4. The source §8 decomposition of a nonzero dual ideal as se, with s supported on the fixed bad primes and e good, separates the s-dependence into one-column factors. The dual cutoff in (3.2) makes the s-sum and discarded tail subpower-cost for fixed field and smooth weight. Mellin separation supplies a single common frequency. Removing (q₁′,q₂′)=1 by Möbius inversion produces a common factor g and new columns fᵢ. The factor χ_g(ae) overline(χ_g(ae)) is precisely 1_{(g,ae)=1}; only after the remaining sum is a nonnegative square can that row condition be dropped. The resulting coefficients depend on f,g,d,r,s and the common frequency, but not on a or e. The ideal factorization count for u=ae and the repetition of λ_{dfg} are divisor-bounded.

5. Source Lemma 6.1 and Theorem 1.1 give, up to ε powers, L₂(X,Y) bounded by

    X + X^(1/n)Y + X^(1−1/n)Y^(2/n) + X^(2/n)Y^(1−1/n).

The powers of the Lemma 6.1 parameter R in these four terms are 1−n, 1, 2−n and −1. Finite reciprocity sectors preserve the operator orientation. At the harmless edge X/R^n<1, enlarge the bounded dyadic interval to scale 1. The source (8.3) is the cubic collapse of this general bound; it is not valid unchanged when n>3.

6. In the source's final localized display before (8.3), r|cd implies Nr≪D and the dual dyadic scale satisfies E≪(ABQ)^ε Q²R/(BD²). Only after replacing L₂ by the displayed positive four-term polynomial may Q/N(dg) be enlarged to O(Q/D). With prefactor BD/(QR), the four terms become

    AQ/D,
    A^(1/n) B^(1−1/n) Q^(2/n) D^(−2/n) R^(1/n−1),
    A^(1−1/n) B^(1/n) Q D^(−1) R^(−1/n),
    A^(2/n) B^(1−2/n) Q^(3/n) D^(−3/n) R^(2/n−1).

All displayed powers of D,R are nonpositive for n≥3. After discarding them, the first term is bounded by the third when A≤B; the fourth is bounded by the second if AQ≤B and by the third if AQ≥B. The dyadic and divisor sums cost ε powers. The dyadic localized inequality in the proposed note is therefore a replay of the source display with this substituted bound, not itself a printed source theorem.

All implicit constants may depend on n,K,S and on fixed smooth weights. No uniformity in growing n, changed field, arbitrary moving profile, or polynomial-height derivatives is supplied by this check. Root-number and conductor assertions remain dependent on the cited preprint, and the independent verification of that preprint is outside this audit.
