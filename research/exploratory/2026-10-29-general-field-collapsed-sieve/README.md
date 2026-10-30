# A fixed-field marked moment from the sixth-order large sieve

**Status:** Proof conditional on De Faveri's preprint theorem; the Kummer-phase and mask arguments received an independent internal review. No zero-free region is claimed. This extends the [Eisenstein calculation](../2026-10-29-sextic-collapsed-moment/README.md) to a fixed number field containing the sixth roots of unity. The key extra point is a finite Kummer-phase lemma, proved below. The result does not by itself improve the saturated-witness count: that argument uses inverse length at least three-fifths of the row length.

**Prior art:** De Faveri §1.3.1 (1.10) already uses general n-th-power removal. Xu–Sang [Lemma 5.2 and its proof](https://arxiv.org/html/2610.17675v2) explicitly display the same four sixth-power-removal contributions in the Eisenstein setting. The results here are source consequences, with no novelty or priority claim.

**Input:** A. de Faveri, [*Optimal large sieve for fixed order characters*](https://arxiv.org/abs/2610.04045v1), Theorem 1.1 and §2.3.4. We use it for n=6, arbitrary coefficient vectors, and sixth-power-free **both** row and column ideals. Its proof is not independently verified here. Standard Kummer theory, class field theory, the S-unit theorem and ideal counting are also used. No priority claim is made for this consequence.

## Statement

Fix a number field K containing μ₆. Fix a finite set S of finite primes containing all primes above 6 and large enough that the ring O_{K,S} has class number one; enlarging any original fixed bad set to achieve this is permitted, provided all column ideals are restricted away from the enlarged S. Let Z≥2, m>0, U=Z^m, and let `𝒰` be a finite multiset of nonzero elements of K with integral principal ideals and norm `N(u)≤C U`, for one fixed C. Assume each principal ideal `(u)` occurs at most a fixed number M of times. This bounded-multiplicity hypothesis is essential: when the unit group is infinite, a norm bound alone contains infinitely many element rows.

Let r,z_i≥0, let z=Σ_i z_i, and take a fixed finite number of prime slots with pairwise disjoint underlying prime supports outside S. Let the inverse index n range over squarefree good ideals in a fixed annulus of scale Z^r. For each good ideal c define χ_c(u)=(u/c)₆ with the zero extension at (c,u)≠1. In all factors use one common orientation χ_c(u)^σ, σ∈{1,−1}; at zeros the negative orientation means the conjugate, i.e. zero. The multiplicative background ν(c) may be any fixed unitary Hecke character restricted to the good ideals, and the remaining prime coefficients are arbitrary row-independent values bounded in modulus by one. Smooth profiles have fixed annular supports and bounded sup norms; row-dependent coefficients and profile suprema are not included.

With the centrally normalized inverse and slot polynomials of OpenAI Lemma 17.1, if

    r+z ≤ m/2,

then, for every ε>0, uniformly over the prime lists and bounded coefficients,

    Σ_{u∈𝒰} |M_u(Z^r) ∏_i Q_{u,i}|² ≪_{K,S,C,M,ε,profiles,slot count} Z^{m+ε}.

The parameters m,r,z_i range over fixed bounded intervals. A fixed finite sum of whole products is allowed by Cauchy–Schwarz. The same assertion applies to any subset of a row family satisfying the multiplicity condition. This statement does not assert that every general-field physical slot system or Hu's unit-sector decomposition has been matched to these hypotheses.

## Finite Kummer-phase lemma

Let `I(S)` be the good integral ideals. For each good sixth-power-free ideal w, choose once a De Faveri decomposition

    w=(x_w) E_w g_w^6,   x_w≡1 (mod c_S),

where E_w belongs to the fixed finite set of ray-class representatives, and g_w is a good fractional ideal. Put t_w=x_w m_{E_w}∈K× as in De Faveri §2.3.4. At every good prime p,

    v_p(t_w) ≡ v_p(w)  (mod 6).                         (3)

Let `Ξ_w` be the primitive finite-order Kummer Hecke character for K(t_w^{1/6})/K, evaluated on good ideals coprime to w. It is unramified there because all good valuations outside w are multiples of six. De Faveri's χ_w and Ξ_w coincide at every good prime avoiding w and g_w: the frozen decomposition is then allowed in his definition. Both are finite-order Hecke characters, so equality outside a finite set implies equality at every good prime outside w, by Chebotarev. Thus for every good integral ideal c,

    χ_w(c)=1_{(c,w)=1} Ξ_w(c).                          (4)

This step deliberately freezes the decomposition before c varies. If t_w has a valuation divisible by six at a prime dividing g_w, Ξ_w there is its unramified local Artin value, not the zero-extended raw residue symbol.

Now let u∈K× satisfy, for a fixed good integral ideal v and a good sixth-power-free w,

    v_p(u)=v_p(w)+6v_p(v)   for every p outside S.

Then d=u/t_w has valuations divisible by six at every good prime. The group

    K(S,6)={d∈K× : v_p(d)≡0 (mod 6) for all p∉S}/K×⁶

is finite: the S-unit quotient O_{K,S}×/(O_{K,S}×)⁶ is finite, and the remaining obstruction maps to the finite 6-torsion of the S-ideal class group. Under our class-number-one choice of S, the S-unit quotient already accounts for all of K(S,6). For each class d choose its primitive Kummer Hecke character η_d, which is unramified outside S. For all good ideals c, keeping the natural zero masks,

    χ_c(u)=1_{(c,v)=1} η_d(c) χ_w(c).                  (5)

Indeed, outside the support of uv the equality follows from the Kummer-symbol identity u=d t_w; at a good p where v_p(u) is a positive multiple of six and p∤w, the left side is zero and the explicit v-mask supplies the zero. When p|w both sides vanish. Equation (4) supplies the other values even if the frozen generator t_w has a multiple-of-six valuation at p. Multiplicativity extends the identity to c with prime powers. The class d can vary with u and w, but it ranges over a fixed finite set and can be frozen by partitioning rows. In the conjugate orientation, conjugate every factor of (5).

## Sieve and summation

Write X=Z^r, P_i=Z^{z_i}, B=X∏P_i. Expand each product and collect the ideal `c=n∏p_i`. The inverse n is squarefree and disjoint slot supports prevent a prime from appearing in more than one slot, so every valuation of c is at most two; in particular c is sixth-power-free. The common multiplicative character, background and collision zeros give

    M_u ∏_i Q_{u,i}=Σ_{Nc≪B} b_c χ_c(u)^σ.

The coefficients b_c are row-independent. The number of tuples representing c is bounded by a fixed-order ideal divisor function; ideal counting then gives

    Σ_c |b_c|² ≪_ε Z^ε.

The estimate is uniform in prime lists and bounded coefficients; it needs only fixed slot count and fixed profile bounds.

For each row factor `(u)=s w v⁶` as ideals, with w good sixth-power-free, s supported on S with every exponent at most five, and v integral. The ideal v here is not required to be good: its S-part absorbs all remaining sixth powers at the bad primes, leaving finitely many possible s. Let v_good denote its part outside S; use v_good in (5). For good column ideals the masks for v and v_good coincide. Fix s, v and the finite Kummer class d from (5), and restrict to rows in this class. The slot coefficient becomes `b_c 1_{(c,v)=1}η_d(c)` (or its conjugate); its squared norm is no larger than that of b_c. Since each `(u)` has at most M labels, summing over this row subset costs at most M times the full sixth-power-free w-sum. De Faveri Theorem 1.1 gives for A≍U/(Nv)⁶ and any such coefficient vector

    ≪ (AB)^ε [A+B+A^(5/6)B^(1/3)+A^(1/3)B^(5/6)] Z^ε.

The finitely many s and d cost only fixed constants. Sum over ideals v with Nv≪U^(1/6): ideal counting and convergence of Σ(Nv)^(−k) for k>1 give

    ≪ (UB)^ε [U+B U^(1/6)+U^(5/6)B^(1/3)+U^(1/3)B^(5/6)].

If B≤U^(1/2), each displayed term is at most U. Constant annular factors and bounded powers of U,B are absorbed by reducing the auxiliary ε, proving the statement. □

The proof never sums over an infinite group of unit representatives. It fixes the actual finite row family first, partitions it by finite Kummer classes, and uses its bounded ideal multiplicity.

**Independent review:** A second researcher checked the frozen-presentation Artin comparison, including primes dividing g_w, finiteness of K(S,6), the w and v zero masks, and bounded ideal multiplicity. No substantive error was found. This review does not independently prove De Faveri’s cited theorem.

## Corollary: a full ideal-row sieve

The same argument gives a standalone sieve for natural ideal rows, without assuming they are principal. Let `χ_a(c)` be De Faveri's zero-extended sixth-order Hecke family for good ideals. For arbitrary complex coefficients b_c supported on good sixth-power-free ideals with Nc≤B, and any U,B≥1,

    Σ_{a good, Na≤U} |Σ_c b_c χ_a(c)|²
      ≪_{K,S,ε} (UB)^ε [U+B U^(1/6)+U^(5/6)B^(1/3)
                              +U^(1/3)B^(5/6)] Σ_c |b_c|².      (6)

No row multiplicity assumption is needed: the index here is the ideal a itself. To prove (6), write a=w v⁶ with w good and sixth-power-free. De Faveri §2.5.1 (2.4) gives the direct identity

    χ_a(c) = 1_{(c,v)=1} χ_w(c),

including the mask at repeated primes. For each fixed v, enlarge the nonnegative row sum to all sixth-power-free w of norm at most U/(Nv)⁶, and apply the cited De Faveri theorem to the masked coefficient vector. Summing v gives exactly (6). This proves the corollary subject to the same source theorem. In particular the sieve is O(U^{1+ε}) times coefficient mass when B≤U^{1/2}; it also records the dependence on larger B explicitly. An independent internal review checked the Kummer classes, masks and the ideal-row summation.

## Sharpness for the Eisenstein field, conditional on Xu–Sang

For K=Q(√−3), choose De Faveri's primary sextic family as in Xu–Sang [Remark 2.1](https://arxiv.org/html/2610.17675v2). The five-term upper bound in (6) is sharp up to `(UB)^ε`: for U,B≥2 the corresponding squared operator norm is at least

    ≫_ε (UB)^(−ε) [U+B+B U^(1/6)
                    +U^(5/6)B^(1/3)+U^(1/3)B^(5/6)].        (7)

This lower bound also imports Xu–Sang [Theorem 1.1](https://arxiv.org/html/2610.17675v2), whose squarefree row and column matrix is a submatrix of ours. That theorem supplies the four terms other than `B U^(1/6)`. If B≤U, the missing term is no larger than `U^(5/6)B^(1/3)`.

If B≥U, consider rows a=v⁶, with good ideals v of norm at most U^(1/6). Their number is ≫U^(1/6) for sufficiently large U by ideal counting with a fixed finite set of excluded primes. The exact sixth-power identity shows that each such row has character χ₁(c) on columns coprime to v; this is one fixed character η. Choose as columns all good prime ideals p with B/2≤Np≤B. For U sufficiently large, B≥U implies Np>U^(1/6), so no such p divides v. The prime ideal theorem gives N≫B/log B columns. Set b_p=conjugate(η(p))/√N. Every selected row then has inner sum √N, while the squared coefficient norm is one. The resulting squared operator norm is ≫U^(1/6)B/log B. Absorb the logarithm in `(UB)^ε`; bounded U are covered by the B term. Combining this with the squarefree lower bound proves (7). An independent internal review checked the sixth-power-row construction and comparison of exponents; the lower result, like the upper one, is conditional on its cited preprint.

## General n-th order ideal-row corollary

For any fixed integer n≥3 and fixed K containing μ_n, take De Faveri's exact n-th-order family, fixed S, and arbitrary coefficients supported on good n-th-power-free columns of norm at most B. The same n-th-power decomposition and source multiplicativity yield

    Σ_{a good, Na≤U} |Σ_{c good, Nc≤B} b_c χ_a(c)|²
      ≪_{K,S,n,ε} (UB)^ε [U+B U^(1/n)
                 +U^(1−1/n)B^(2/n)+U^(2/n)B^(1−1/n)] Σ_c|b_c|².

Indeed a=w v^n with w n-th-power-free gives the row mask 1_(c,v)=1. Apply De Faveri Theorem 1.1 at A=U/(Nv)^n and sum v. The corresponding v-exponents are n, 0, n−1 and 2; all nonzero ones exceed one, while the number of v is O(U^(1/n)). This is a direct corollary of the cited theorem and its n-th-power removal, without a priority claim. When B≤U^(1/2), the bracket is O_n(U). No matching lower bound in arbitrary fields or zero-free region is claimed. An independent internal review checked the n-th-power mask, all four summed exponents, and the endpoint B≤U^(1/2).
