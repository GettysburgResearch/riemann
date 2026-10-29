# A fourth-cycle target for the selected long-source norm

**Status:** A reduction to a concrete open correlation estimate, with a counterexample to an over-strong variant. It does not prove a selected operator estimate or any zero-free region. The numerical row-count exponent below is conditional on the applicable PR94 count source and its matching to the chosen physical rows.

Let F be a selected finite family of sixth-power-free Eisenstein rows, `M=#F`, with row norms at most Y. Let L≥Y and let S_L be **all** nonzero integral ideals of norm at most L. Form the row Gram matrix

    G(u,v)=Σ_{I∈S_L} χ_I(u) overline(χ_I(v)),
    E=G−diag(G).

The source kernel has |χ_I(u)|≤1, including all coprime zero masks. Fixed-field ideal counting gives `||diag(G)||≪L`. Every source subset S⊆S_L has selected squared operator norm at most the norm for S_L, by monotonicity in source columns. Since E is Hermitian,

    selectedNorm(F,S) ≤ C L + (Tr E⁴)^(1/4).                (1)

Suppose a source-compatible argument proves the **complete-source fourth-cycle estimate**

    Tr E⁴ ≪ Z^ε L² M³                                      (2)

uniformly with the physical selection, row masks and admissible parameter order. Then (1) implies

    selectedNorm(F,S) ≪ L + Z^(ε/4) L^(1/2) M^(3/4).      (3)

At the PR94 difficult bin, its C branch gives `M≪Z^ε Y^α` with `α=137478360780643/225606975000000≈0.60937106<2/3`, if that bound is applicable to this exact F. For every L≥Y, (3) becomes `≪Z^ε' L`; at L=Y the second term has the exponent `1/2+3α/4≈0.9570283`, saving about `0.04297` before the small losses. The [long-source amplification reduction](../2026-10-29-long-source-seed/README.md) explains what additional uniformity and transports are needed to use such a bound in an all-source detector. None of those analytic hypotheses is proved here.

Expanding the trace gives a closed four-row cycle,

    Tr E⁴ = Σ_{u₁,u₂,u₃,u₄∈F, uᵢ≠uᵢ₊₁}
              E(u₁,u₂) E(u₂,u₃) E(u₃,u₄) E(u₄,u₁),

with indices modulo four. Individual terms can be complex, though the total is nonnegative. Thus (2) needs cancellation in the signed cycle sum; an absolute-value estimate or isolated pair bounds are generally insufficient. The complete source and exact selected rows are important: no saturated weight on the entire unrestricted row family is introduced.

## The analogous statement for every source subset is false

In the broad arbitrary-ideal slot interface, fix `0<σ<1/2` and take Y large. Choose good prime elements π with norms comparable to Y^(1/3), and rows `u=π³`. They are sixth-power-free and number `M≫Y^(1/3)/log Y`. For any sufficiently short fixed slot width w>0, let P=Y^w and choose slot sources `J²` of norms at most P, with normalized constant coefficients. All J are coprime to the chosen π because w/2<1/3. On every row the sextic symbol is 1, and the slot has squared response `≫P^(1/2)`, so all rows are selected at slope σ.

Now choose the **subset** `S={J²:NJ≤Y^(1/2), (J,∏π)=1}`. Excluding the row primes loses only O(1/log Y) proportion by the union bound, since `M/Y^(1/3)≪1/log Y`. Ideal counting then gives `#S≫Y^(1/2)`. Every matrix entry is 1. Thus `G=(#S)11*`, `E=(#S)(11*−Id)`, and

    Tr E⁴ ≥ ((M−1)#S)⁴ ≫ Y^(10/3−o(1)),
    Y² M³ = Y^(3+o(1)).

The uniform version of (2) for all subsets S therefore fails. The selected operator itself has squared norm `M#S≈Y^(5/6−o(1))`, which remains below Y; this example does not contradict the target long-source bound. It uses arbitrary square-ideal slots, not fixed smooth prime slots.

The complete-source hypothesis in (2) is consequential, because the nonsquare sources can cancel the square-source contribution. For the same π³ family and distinct rows, the complete off-diagonal sum is a nonprincipal quadratic Hecke-character sum with conductor norm `≪N(π₁π₂)≪Y^(2/3)`, up to fixed bad factors. However, one must not import the rational Dirichlet Pólya–Vinogradov bound `O(sqrt(Nq))` for a sharp **ideal-norm** cutoff without justification: the classical number-field bound reported for degree two has the form `O((Nq)^(1/3)Y^(1/3) log^C)`, here only `Y^(5/9) log^C`. This does not verify (2) for the family. A previous draft incorrectly claimed the stronger bound; that claim is withdrawn. Generic physical rows may have product conductor as large as Y², and their complete-source four-cycle remains unproved.

## Strength test: two selected rows already demand square-root cancellation

The complete-source estimate (2) has a serious arithmetic consequence in the broad row-independent prime-coefficient class. Fix any two good sixth-power-free rows u,v of norms at most Y, and take a slot length P=Y^w for a fixed w>0. For good prime ideals p with norms in [P,2P], set

    a_p = (overline(χ_p(u)) + e^(iφ) overline(χ_p(v))) / (2√P),

where φ is a single constant chosen so that `Re(e^(iφ) Σ_p χ_p(u) overline(χ_p(v)))≥0`. The coefficients are fixed across the row sum, satisfy `|a_p|≤P^(−1/2)`, and have squared mass O(1/log P). Each row has at most 1/w divisors among the slot primes. Therefore, by prime-ideal counting, both slot responses have modulus `≫√P/log P`. Both rows are selected at every fixed slope σ<1 for all sufficiently large Y; any fixed common ray-class restriction may be imposed when choosing the two rows.

For `F={u,v}`, the off-diagonal matrix is

    E = [[0,C],[overline(C),0]],
    C = Σ_{NI≤L} χ_I(u) overline(χ_I(v)),
    Tr E⁴ = 2|C|⁴.

If (2) is asserted uniformly for every two-row set satisfying this broad amplitude selection, then (2), with L=Y, would imply

    |Σ_{NI≤Y} χ_I(u) overline(χ_I(v))| ≪ Y^(1/2+ε)

uniformly over all such pairs, after adjusting the arbitrary loss. The underlying pair-character conductor can have norm as large as a constant multiple of Y², so this asks for square-root cancellation in a long incomplete sextic-character sum at approximately square-root conductor. Standard Pólya–Vinogradov or Burgess bounds do not by themselves supply this strength. This does not disprove (2), nor does it transfer to fixed smooth physical coefficients: the slot above was tailored to the chosen pair. It also does not imply that the pair meets additional detector-zero or witness conditions. It shows that proving (2) uniformly over the broad arbitrary-prime coefficient interface would require a major new input, even though the selected operator itself remains allowed to have size O(Y) for two rows.

## A weaker cycle target that permits exceptional modes

The pair obstruction does not apply if (2) is replaced by the weaker sufficient estimate

    Tr E⁴ ≪ Z^ε (L⁴ + L² M³).                              (4)

Indeed the fourth-root bound becomes `||E||≪Z^(ε/4)(L+L^(1/2)M^(3/4))`, and the same `α<2/3`, L≥Y argument yields the selected long-source bound. The L⁴ term allows one or a bounded number of exceptional eigenvalues of size comparable with L; in particular, it does not imply square-root cancellation for M=2 and is not contradicted by the square-source construction above. An approach might isolate a bounded exceptional spectral contribution and prove a random-size fourth-cycle estimate for the rest. This is a concrete research target, not an established bound. It is still stronger than the desired operator norm because the trace controls the number of large eigenvalues as well as their maximum.

**Independent review:** A second researcher checked the complete-source reduction, the square-source counterexample, the tailored two-row selection with its zero masks and phase. The unsupported low-conductor Pólya–Vinogradov step was subsequently withdrawn. The softened estimate (4) remains open.

## Exact arithmetic form of the remaining cycle

For a complete ideal cutoff S_L and any u,v∈F, including u=v, direct expansion gives

    (E²)(u,v) = Σ_{I,J∈S_L} χ_I(u) overline(χ_J(v))
                   · Σ_{w∈F\{u,v}} overline(χ_I(w)) χ_J(w),
    Tr E⁴ = Σ_{u,v∈F} |(E²)(u,v)|².                        (5)

The two exclusions arise from deleting G's diagonal and are essential when u=v. For I,J coprime to the fixed bad primes, the inner factor is exactly `χ_{I⁵J}(w)`, including every zero when w shares a factor with I or J. On the sixth-power skeleton diagonal this factor is a coprimality mask; off it, it is a nonprincipal sextic correlation. Equation (5) presents the problem as a bilinear estimate in two complete ideal cutoffs coupled to the *same selected row set*, with source masks retained. It also shows where a simple application of an unrestricted large sieve loses the selection: it forgets the correlation between the selected set and the pair I,J. Neither (4) nor a sufficient off-skeleton estimate is proved here.

## Smooth majorization and a proved low-conductor test case

There is a useful way to avoid the sharp ideal cutoff entirely. Fix `W≥0`, smooth on `[0,∞)`, with W=1 on `[0,1]` and W=0 on `[2,∞)`, and define

    G_W(u,v)=Σ_I W(NI/L) χ_I(u) overline(χ_I(v)),
    E_W=G_W−diag(G_W).

For every S⊆S_L, the row Gram matrix for S is bounded above by G_W in the positive-semidefinite order: their difference is a sum of nonnegative multiples of rank-one source-column matrices. Consequently `selectedNorm(F,S)≤||G_W||`. Ideal counting gives `||diag(G_W)||≪_W L`, so either fourth-cycle target (2) or its weaker form (4), stated for E_W, is sufficient. No claim is made that a bound for E_W implies the same trace bound for the *sharp* E.

For the particular low-conductor π³ family above, the smooth majorant gives an actual O(L) norm bound, conditional only on standard finite-order Hecke character and functional-equation facts. Choose one good primary generator per prime ideal π with `Nπ≤Y^(1/3)`, and put `F={π³}`. For distinct π,ρ, the off-diagonal character `I↦χ_I(π³) overline(χ_I(ρ³))` is nonprincipal quadratic, with primitive conductor norm `Q≪N(πρ)≪Y^(2/3)`, after the fixed bad primes are accounted for. The original zero extensions agree with that primitive character up to fixed Euler-factor deletions; the primes π and ρ themselves are ramified in the quadratic Kummer character.

The original source treats the fixed primes over 2 and 3 specially, so one should not silently identify its complete Euler product with the primitive quadratic L-function. The prime over 3 contributes zero. Split the source ideals by the exponent j of the fixed norm-4 prime over 2; at most `O(log(2L))` exponents contribute. On the remaining good ideals, the original pair character agrees with the primitive quadratic Hecke character after deletion of finitely many fixed Euler factors. The variable primes π and ρ are ramified and belong to the conductor, so their original zero masks do not introduce additional missing Euler factors.

For each rescaled good-ideal sum, with `X=L/4^j≥1/2`, Mellin inversion and the Hecke functional equation give, for every ε>0,

    Σ_{I good} W(NI/X) χ(I) ≪_{W,ε} Q^(1/2+ε).              (6)

The Mellin transform of W has only a simple pole at s=0. The completed nonprincipal finite-order Hecke L-function over this imaginary quadratic field is entire and has a Γ_C(s) factor, so L(0,χ)=0; fixed Euler-factor deletions preserve this zero. Shift to `Re s=−ε` and use the functional equation and absolute convergence at `1+ε`; rapid vertical decay of W's Mellin transform absorbs the polynomial growth in the imaginary part. Since X≥1/2, the resulting X^(−ε) factor is bounded. Summing the O(log(2L)) fixed-prime pieces gives

    |E_W(π³,ρ³)| ≪_{W,ε} Y^(1/3+ε) log(2L).

Because `#F≪Y^(1/3)`, the row-sum bound yields `||E_W||≪Y^(2/3+ε) log(2L)`, which is O(L) uniformly for L≥Y after choosing ε sufficiently small. The diagonal is O(L), so `selectedNorm(F,S)≪L` for every source subset of ideals of norm ≤L in this special family. Also `Tr(E_W⁴)≤M||E_W||⁴≪Y^(4/3+ε)M⁵ log(2L)^4≪L^(2+ε')M³`, so the stronger weighted target (2) holds for this family up to a power loss.

This calculation does not assert sharp-cutoff character cancellation or the unweighted fourth-cycle bound. The earlier draft's arbitrary rapid-decay claim is withdrawn because the norm-4 Euler factor can differ from that of the primitive Hecke character; the fixed-prime decomposition above avoids that issue. The argument does not extend to generic physical pairs, whose conductor can be ≍Y² and for which L≥Y is too short to gain from (6).
## Small-radical families

The same smooth argument suggests the following more general consequence of standard sextic Kummer and Hecke-character inputs. It has not yet been independently audited. Let F consist of sixth-power-free Eisenstein element rows u with nonzero radical ideals of norm at most R≥2. Let S be any finite set of nonzero ideals of norm at most L≥1. Then, with the source's sextic character and zero masks,

    selectedNorm(F,S) ≪_ε (L+R²)(LR)^ε.                     (7)

In particular, for rows of norm at most Y with `N(rad(u))≤Y^(1/2)` and L≥Y, this gives `selectedNorm(F,S)≪L(LY)^ε`, without an amplitude or zero-location selection. For a physical class that can be decomposed into small- and large-radical rows, monotonicity and the sum-of-row-blocks operator inequality reduce the missing long-source estimate to the large-radical block; the proof does not establish that missing block or a zero-free region.

For (7), group together rows whose ideal valuations agree at every prime outside 6. Each group has at most `6·6²=216` rows: there are six units and two primes above 6, each with valuation in {0,…,5}. Rows from different groups have a nonzero valuation difference at a good prime and hence a nonprincipal pair character. By ideal counting and `5^ω(a)≪_ε (Na)^ε`, the number of rows is `M≪_ε R^(1+ε)`: choose their squarefree radical ideal of norm at most R, choose one of the five nonzero valuations at each prime, and choose a unit.

For rows u,v in distinct good-valuation groups, the pair-character on good source ideals is a nonprincipal finite-order Hecke character whose primitive conductor has norm `Q≪N(rad(uv))≪R²`. This is the standard tame Kummer conductor bound: every prime outside the fixed bad set with a nonzero valuation difference modulo six has conductor exponent one, and primes over 6 have bounded conductor exponents. If a prime divides both rows and the valuation difference cancels modulo six, the primitive character may be unramified there while the original source still vanishes there. Retain this mask by deleting that prime's Euler factor. On `Re s=−η`, the product of all such factors is `≪_η R^(O(η))`; the number of prime factors contributes another arbitrarily small power. The fixed primes above 2 and 3 are handled by splitting their source exponents as in the preceding section. The smooth sum of each rescaled good ideal component is therefore `≪_ε R^(1+ε)`; after summing fixed-prime exponents,

    |E_W(u,v)| ≪_ε R^(1+ε) log(2L)

uniformly for rows in distinct good-valuation groups. This uses the pole cancellation at s=0 and the functional equation as above, with a smaller preliminary loss to absorb the variable deletion factors. Each within-group Gram block has size at most 216 and entries O(L), hence operator norm O(L); the off-block part has norm `≪M R^(1+ε)log(2L)`. PSD domination transfers the resulting bound to every S of norm at most L. Absorbing logarithms and smaller losses proves (7), subject to the stated standard arithmetic inputs. □

**Independent review:** A second researcher checked the nonprincipal Kummer argument, tame conductor bound, shared-prime deletion factors, the zero at s=0, the `X≥1/2` fixed-prime split, ideal counting, and PSD/Gershgorin steps. The result remains conditional on the standard Kummer/Hecke identifications and functional-equation inputs stated above; no priority claim is made.

## Pairwise conductor refinement

For a more sensitive criterion, assume also `Nu≤Y` for all u∈F. Let `g(u)` be the ideal obtained from `(u)` by deleting its powers of the two primes above 6, and define for each pair

    Q(u,v) = ∏_{p∤6 : v_p((u)) ≠ v_p((v)) (mod 6)} Np.

The proposed sharper bound, conditional on the same standard Kummer/Hecke input, is

    selectedNorm(F,S) ≪_ε (L + max_{u∈F} Σ_{v∈F, g(v)≠g(u)} Q(u,v)^(1/2))
                         · (LY)^ε.                          (8)

It retains the actual pairwise ramification rather than replacing it by a uniform radical bound. Rows in the same good-valuation block are excluded from the sum: at most 216 rows share g(u), since there are six units and two bad-prime valuations in {0,…,5}. Every block entry has magnitude O(L), and each block has operator norm O(L). The F=∅ case is trivial.

For p∤6 the local Kummer character is tame. Because raising to the sixth power is an isomorphism on principal local units, a unit Kummer class can only contribute an unramified local character. Therefore the pair-character ramifies at p exactly when the valuation difference is nonzero modulo six, and its conductor exponent there is one; its primitive conductor has norm `≪Q(u,v)`, with an absolute fixed factor at primes over 6. Unit phases may change unramified values and the bounded wild factor, but do not change this tame conductor criterion. For different good-valuation blocks, some tame prime ramifies, so the pair-character is nonprincipal. This also handles all subtleties arising from unit phases and differences supported only at bad primes inside the bounded blocks.

As before, the source kernel also vanishes when a good prime divides both u and v and their valuations agree modulo six. Such a prime is unramified in the primitive pair-character but remains deleted from the source sum. At `Re s=−η` its Euler deletion costs at most `1+Np^η`; the product over all such primes is `(LY)^ε` after choosing η and the auxiliary divisor loss sufficiently small, since `N(rad(uv))≤Y²`. Splitting the fixed bad-prime powers, applying the smooth Hecke bound to each component and absorbing `log(2L)` yields

    |G_W(u,v)| ≪_ε Q(u,v)^(1/2) (LY)^ε

for `g(u)≠g(v)`. Hermitian row-sum control of the off-block matrix, the O(L) bound for its good-valuation diagonal blocks, and PSD source domination give (8). These calculations are a proof under the indicated arithmetic identifications, not a new zero-free region.

If `M=#F` and every `N(rad(u))≤R`, then `Q(u,v)≤N(rad(uv))≤R²`; retaining the radical bound throughout the Euler-deletion estimates, the same proof gives the sharper cardinality-dependent estimate

    selectedNorm(F,S) ≪_ε (L + M R) (LR)^ε.                (9)

The elementary bound `M≪_ε R^(1+ε)` recovers (7), after changing the arbitrarily small loss. Compared with (7), (9) can be materially stronger for a sparse selected class. The bound (8) may be stronger still when many pairs share the same prime exponents, even if their radicals are individually large.

As an illustration beyond small radicals, take a fixed sixth-power-free element A, distinct good prime elements `π_j∤A` with `Nπ_j≤P`, and one fixed `1≤r≤5`. For rows `u_j=A π_j^r` of norm ≤Y, the prime valuations of A cancel pairwise and `Q(u_i,u_j)≤P²`. If M is the number of rows, (8) gives

    selectedNorm({u_j},S) ≪_ε (L+MP)(LY)^ε.

The radical of A may be large. Its source zero mask is retained as variable Euler deletions and absorbed only at the displayed small power loss. In particular, MP≤L gives the long-source-size bound for this family, independent of prime-slot selection. This is a structural special case, not a bound for an arbitrary union of such blocks: the number of blocks and cross-block conductor sums must still be controlled.

**Independent review of (8):** A second researcher checked the tame Kummer ramification criterion, nonprincipal condition across distinct good-valuation blocks, variable zero-mask deletions, fixed bad-prime decomposition, Mellin cancellation, bounded good-valuation blocks and Gershgorin estimate, conditional on the stated source-to-Hecke identification.

More generally, suppose every row has the same positive valuation at each prime dividing a fixed squarefree good ideal D, and `N(rad(u))≤R`. The primes of D are absent from Q(u,v), and each occurs in both radicals, so `Q(u,v)≤R²/(ND)²`. The pairwise estimate yields

    selectedNorm(F,S) ≪_ε (L + M R/ND) (LY)^ε.

This controls a high-radical cluster whenever `MR≤L·ND`, with the common-prime source deletions retained. It does not automatically control cross-correlations between different clusters.

The row-sum estimate in (8) can itself be sharpened. Let C be the real symmetric nonnegative matrix with `C(u,v)=sqrt(Q(u,v))` when `g(u)≠g(v)` and zero otherwise. Entrywise control of the off-block matrix and its Rayleigh quotient imply

    selectedNorm(F,S) ≪_ε (L + ||C||_{2→2}) (LY)^ε.        (10)

Indeed `|x*E_W x|≤(LY)^ε |x|ᵀ C |x|`. For any positive weights t_u, the weighted Schur bound gives

    ||C||_{2→2} ≤ max_u t_u^(−1) Σ_v C(u,v)t_v.

This can use unequal cluster sizes or pairwise conductor geometry; the uniform row sum is the special case t_u=1. Establishing such a conductor-graph bound for the actual large-radical physical selected rows remains open.

**Tracker normalization audit:** A third researcher traced `localRowValue` in `CompactEnergyFamilies.lean` to `canonicalSextic` in `Arithmetic/EisensteinEmbedding.lean:461`, using one fixed embedding of the Eisenstein ring in C. In `GaussSum/FiniteFourier.lean:801`, `sexticChar=cubicChar²·quadraticCharO`, and `cubicChar_reduce` at line 578 gives the cubic exponent `(Np−1)/3`. At every p∤6 the resulting residue exponent is `2(Np−1)/3+(Np−1)/2=7(Np−1)/6`, congruent to `(Np−1)/6` modulo `Np−1`. Reduction is injective on μ₆ at such p. Thus the source's good-prime symbol agrees with the standard sixth-power residue symbol under a coherent fixed embedding, up to a single global inversion if the opposite Artin convention is used. The latter leaves conductors and all norm estimates unchanged. The analytic Hecke functional equation, tame Kummer conductor facts and Mellin argument remain paper-level inputs, not Lean-checked here.

## All same-exponent-one row blocks are controlled

For any sixth-power-free row u, uniquely factor its good part into pairwise-coprime squarefree ideals

    (u)_good = a₁ a₂² a₃³ a₄⁴ a₅⁵,

and call a₁ its exponent-one support. Fix a squarefree good ideal A with norm a, and consider any set F_A of rows with `a₁=A`, `Nu≤Y`. The product `T=a₂a₃a₄a₅` has norm at most `(Y/a)^(1/2)`, and each of its prime factors has at most four choices of exponent. Including units and the bounded bad-prime valuations gives

    #F_A ≪_ε (Y/a)^(1/2+ε).

For two such rows, all primes of A have equal valuation 1 and disappear from Q(u,v); every remaining good prime with differing valuation divides `T_u T_v`. Thus `sqrt(Q(u,v))≤(Y/a)^(1/2)`. The pairwise criterion (8) gives, for any source set S of ideals of norm ≤L,

    selectedNorm(F_A,S) ≪_ε (L + Y/a)(LY)^ε.                (11)

Now let F be an arbitrary finite family of sixth-power-free rows of norm ≤Y, and G_S its row Gram matrix for S. Keep exactly the entries joining rows with the same exponent-one support; call the resulting block-diagonal matrix `G_same`. Each block is positive semidefinite, so its operator norm is bounded by (11), and therefore

    ||G_same|| ≪_ε (L+Y)(LY)^ε.                            (12)

For L≥Y, all equal-a₁ interactions are controlled at the desired long-source size, without any amplitude, density or zero-location hypothesis. This includes the a₁=1 low-radical family and arbitrary fixed high-radical A. The complementary matrix `G_S−G_same` is Hermitian and need not be positive. It remains sufficient, but unproved, to control its one-sided quadratic form by `O(L Z^ε)` on the actual selected rows. Thus (12) isolates cross-a₁ interactions; it does not establish a complete long-source bound or a zero-free region.

**Independent review of (11)–(12):** A second researcher checked the squarefree-factor count, cancellation of the common a₁ from Q, treatment of the bounded wild/unit blocks, the PSD majorization, and the operator norm of the direct sum. The result controls only same-a₁ row pairs; it does not supply the remaining cross-block bound.
