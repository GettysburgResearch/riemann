# A marked inverse moment from the sextic large sieve

**Status:** Proof conditional on the cited preprint theorem. The character-family conventions, sixth-power masks and exponent arithmetic have been independently reviewed. This does not by itself prove a zero-free region.  
**Scope:** The Eisenstein field, all element rows, a fixed finite number of disjoint prime slots with arbitrary bounded row-independent coefficients, one common finite ray twist and character orientation, and one fixed smooth annular inverse profile.  
**Inputs:** De Faveri's preprint, [Optimal large sieve for fixed order characters, Theorem 1.1 and §2.3.4](https://arxiv.org/abs/2610.04045v1); the sixth-power-free upper bound is also quoted in [Xu–Sang, equations (1.2) and (2.3) and Remark 2.1](https://arxiv.org/html/2610.17675v2). Unique factorization in Z[ω], ideal divisor bounds, and fixed-field ideal counting. No OpenAI inverse or plain moment is used.  
**Novelty:** No priority claim. This is a direct large-sieve consequence; its exact marked-moment range and usefulness should be compared with previous literature.  
**Remaining question:** Determine whether any useful detector uses the new range; the source detector does not use it directly. The result depends on a recent preprint, and no claim is made that the theorem has completed external peer review.

Let F=Q(√−3), and let S be a fixed finite set of prime ideals containing those above 6. Use the primary generators, zero-extended sextic characters χ_n(u), Möbius coefficients μ, fixed finite-order ray character ν, disjoint prime supports, and normalizations of [OpenAI Lemma 17.1](https://wcook04.github.io/plectis-atlas/papers/The-Quasi-Riemann-Hypothesis-September-30-2026.html). Fix m>0, nonnegative r,z_i, and finitely many slots; put z=Σ_i z_i and assume

    r+z ≤ m/2.                                           (1)

For bounded parameters, arbitrary row-independent slot coefficients with modulus ≤1 and fixed smooth annular profiles,

    Σ_{u∈O, 0<Nu≪Z^m} |M_u(Z^r;W) Q_u|² ≪_ε Z^{m+ε}.   (2)

The implied constant can depend on S, the fixed ray character, the bound on the slot count, support ratios and finitely many profile seminorms; it is uniform in the choices of prime subsets and bounded coefficients. Either common character orientation is allowed. A fixed finite sum of whole products follows by Cauchy–Schwarz. For fixed norm-twist heights, differentiating the profiles gives the usual fixed-polynomial height cost; no row-dependent choice of profile is asserted without an additional Sobolev argument.

The result crosses the second face `2r+8z<3m` of the source lemma when `0≤r<m/6`: for example r=m/20, z=43m/100 satisfies (1) strictly and `r+2z<m`, but `2r+8z=3.54m>3m`. The region is not a global enlargement of the source region: when r is larger, (1) can be more restrictive. The source lemma's simultaneous-witness detector uses r≥3m/5 on its amplified inverse branch, so this extension does not automatically improve that row count or any zero-free boundary.

## Proof

Let U=Z^m, X=Z^r and P_i=Z^{z_i}, and write B=X∏_i P_i. By the fixed annular support bounds, every product `c=n∏p_i` has norm ≪B. The inverse n is squarefree; the slot primes are pairwise distinct because the supports are disjoint. Thus the valuation of c at any prime is at most two, even if a slot prime divides n: c is sixth-power-free.

Expand the product and collect equal ideals c. Multiplicativity of the common character, with the source's zero extension, gives

    M_u Q_u = Σ_{c sixth-power-free, Nc≪B} b_c χ_c(u)^σ,  σ=±1,    (3)

where b_c contains the common ν(c), the Möbius factor, the tests, and normalization B^(−1/2). This equality retains collisions rather than discarding them. The coefficients are row-independent. For each c the number of representations as `n∏p_i` is at most a fixed-order divisor function. With the slot count fixed, Cauchy–Schwarz, the ideal divisor bound and ideal counting imply

    Σ_c |b_c|² ≪_ε Z^ε.                                  (4)

Indeed the total number of tuples in the prescribed annuli is O(B), and each tuple has weight O(B^(−1/2)); taking the maximum divisor multiplicity costs Z^ε. All indices avoid S, so fixed ray masks and ν are absorbed into b_c. Uniformly bounded slot coefficients and fixed profile suprema suffice for this step.

We import the following sixth-power-free sextic large-sieve estimate from De Faveri’s preprint: for arbitrary coefficients c_b supported on sixth-power-free good ideals of norm ≤B,

    Σ_{a sixth-power-free, Na≤A} |Σ_b c_b χ_b(a)|²
      ≪_ε (AB)^ε [A+B+A^(5/6)B^(1/3)+A^(1/3)B^(5/6)] Σ_b |c_b|².  (5)

The symbol has the source orientation χ_b(a)=(a/b)₆, zero when the indices are not coprime. In De Faveri §2.3.4, the family is indexed by the numerator, so the matrix entry χ_a(b) in that notation equals (a/b)₆ for primary choices; no transposition is needed. Xu–Sang Remark 2.1 identifies their primary sextic-symbol family with the same large-sieve family. Any fixed finite ray/unit representatives produce finitely many row classes and column phases, and hence affect only the implied constant. Restricting either index away from S only deletes rows or columns.

For an element row u, factor its ideal uniquely as `(u)=s w v^6`, where w is sixth-power-free and prime to S, s is supported on S with valuations in {0,…,5}, and v is an integral ideal. There are finitely many choices for s and the unit of u. For each such choice, the corresponding factor χ_c(unit·s) is a column-dependent phase (or a fixed bounded column mask) and is absorbed into b_c. The good part of v has a primary generator; its S-supported part can be included in the same factorization, and since c is coprime to S it changes neither the mask nor its bound. For each fixed v, the sixth power contributes precisely the column mask `1_{(c,v)=1}`; it does not change character values on coprime columns. Discarding the extra coprimality or norm restrictions on w only enlarges the nonnegative row sum. With `Nv^6≪U`, apply (5) to the resulting w-sum with A≪U/(Nv)^6 and coefficient vector `b_c 1_{(c,v)=1}`. Its squared norm is no larger than (4). Summing over all v and the finite unit/bad-prime classes yields

    (UB)^ε [ U + B U^(1/6) + U^(5/6)B^(1/3)
                    + U^(1/3)B^(5/6) ].                         (6)

Here `Σ_v (Nv)^(−6)`, `Σ_v (Nv)^(−5)` and `Σ_v (Nv)^(−2)` converge, while the number of v with `Nv≪U^(1/6)` is O(U^(1/6)). Since B≤U^(1/2), every term in (6) is O(U), up to the displayed arbitrarily small power. Fixed finite support constants are absorbed in that power. This proves (2). □

Independent review checked the sixth-power-free row and column hypotheses, the orientation via De Faveri §2.3.4, the fixed bad-prime masks, the ℓ² estimate and the exponent arithmetic. This review does not replace verification of the cited preprint itself.
