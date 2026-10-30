# Fixed twisted Gauss modes do not exhaust the natural-row operator

**Status.** The proposition below is a deduction from Xu–Sang, [arXiv:2610.17675v2](https://arxiv.org/abs/2610.17675v2), Proposition 3.1 and the proof of Lemma 4.2. Those inputs are a 2026 preprint, and its Gram formula imports other source results; this note does not independently establish those inputs. It concerns **all natural rows** with a smooth row weight and squarefree columns. It gives no lower bound for the squarefree-row or selected-row operator. It is a restriction on finite-mode projections, not a complete spectral decomposition.

Let K=Q(ω), and adopt the exact conventions and fixed ray fiber σ of Xu–Sang §2.1. Enlarge the finite exceptional set S by a fixed prime cutoff, as permitted there and in Corollary 4.3, so that the constant C₀ in Lemma 4.2 satisfies C₀−1<1/4. Let w be the nonnegative fixed radial row weight in §3.1 and define the weighted natural-row operator

    (T_Y b)(m) = w(m/√Y)^{1/2} Σ_s b(s) overline(χ_s(−m)),

where (m,S)=1, s ranges over squarefree primary good elements of the fixed ray fiber with Y/2 < Ns < Y, and characters retain their zero extensions. Each row and column set has O_S(Y) elements. In particular ||T_Y|| ≤ ||T_Y||_HS ≪_S Y. The exact choice of the harmless row phase and replacing conjugate characters by their conjugates does not change the norm statement below.

Fix finitely many sixth-power-free good elements h_j and smooth profiles U_j supported in (1/2,1). Consider the columns

    b_{h_j,U_j}(s) = Y^{-1/2} U_j(Ns/Y)(Ns/Y)^{-1/2}
                       G(s,1) J₆(h_j,s).

The source's convention J₆(h,s)=χ_s(h) includes its zero mask. Let V_Y be their span, and P_Y the orthogonal projection onto V_Y. The h_j and profiles are fixed independently of Y.

**Source-conditional proposition.** For a good prime p outside S and all supports of the h_j, chosen after S is fixed, there is a fixed U≥0, U≠0, such that

    ||T_Y (I−P_Y)||² ≫_{p,S,w,U,h_j,U_j} Y^{7/6}.

In particular, removing any fixed finite list of such radial, fixed-twist Gauss columns does not leave an O(Y^{1+ε}) squared operator norm. This does not rule out a projection whose dimension or twisting conductors grow with Y, and it does not show a failure for the Möbius vector specifically.

**Proof from the source inputs.** Put b_p=b_{p,U} with U∈C_c^∞((1/2,1)) nonnegative and nonzero. Since s is squarefree and coprime to S, its sextic character is primitive in the relevant sense, and the normalized Gauss transformation gives

    G(s,−m) = overline(χ_s(−m)) G(s,1),     |G(s,1)| = 1,

including the zero at (m,s)>1. Hence, exactly using source (3.1),

    ||T_Y b_p||² = Y ||F^{sf}_{p,1;U}(·;Y)||²_Y.

The exclusion (s,p)=1 in (3.1) is already enforced by the zero-extended J₆(p,s). Proposition 3.1 at q=L=Y, d=p, e_p=1 gives the all-column main term

    ||F_{p,1;U}||²_Y = C_{S,w} I(U)² Y^{1/6} Ω(p,1) + O_{p,ε}(Y^{1/12+ε}),
    I(U)=∫₀^∞ U(t)t^{-5/6}dt > 0,
    Ω(p,1)=(Np)^{-5/6}(1+(Np)^{-1})^{-2} > 0.

The proof of Lemma 4.2 separates the unit powerful component from the nonunit components. Its displayed estimate (4.4) and following summation bound the latter by (C₀−1) times the square root of the same main term, plus O_{p,ε}(Y^{1/24+ε}). This argument explicitly retains Ω(d,e), so it applies to fixed d=p as well as d=1; compare the triangle-inequality use in Corollary 4.3. Therefore, after taking ε sufficiently small,

    ||T_Y b_p||² ≫_{p,S,w,U} Y^{7/6}.

Also ||b_p||² ≍_{p,S,U} 1 by squarefree ideal counting in finitely many fixed ray classes, with the fixed prime p excluded.

For every j, the product J₆(p,s) overline(J₆(h_j,s)) is, on the relevant coprime ideals, a finite-order Hecke character up to a fixed ray phase. It is ramified and nontrivial at p, because p∤h_jS; multiplying by any character of the fixed S-supported ray group cannot make it principal. The additional zero masks at finitely many primes divide Euler factors and do not change this conclusion. Thus squarefree Möbius inversion, or a Mellin shift of the fixed-conductor Dirichlet series L_K(z,ξ)/L_K(2z,ξ²) with its finite local factors, implies

    ⟨b_p,b_{h_j,U_j}⟩ ≪_{p,h_j,S,U,U_j,ε} Y^{-1/2+ε}.

The Mellin argument starts with Re z>1 and shifts to Re z=1/2+ε; L_K(z,ξ) is entire because ξ is nonprincipal, the denominator has Re(2z)>1, and the smooth Mellin transform has rapid decay. Finite S-ray restrictions are expanded into a fixed finite sum of ray characters.

The Gram matrices of the fixed columns have limits given by squarefree ray-density constants and integrals of the fixed radial profiles. After deleting exact linear dependencies, these limiting Gram matrices are positive definite: the underlying finitely many local residue patterns all have positive density, so a zero limiting quadratic form forces the corresponding fixed profile combination to vanish for every allowed residue pattern. Consequently the orthogonal projection coefficients are uniformly controlled, giving

    ||P_Y b_p|| ≪ Y^{-1/2+ε}.

The Hilbert–Schmidt bound then yields ||T_Y P_Y b_p|| ≪ Y^{1/2+ε}=o(Y^{7/12}) for ε<1/12. Triangle inequality with the preceding source lower bound implies ||T_Y(I−P_Y)b_p|| ≫ Y^{7/12}. Since ||(I−P_Y)b_p||≤||b_p||≪1, the proposition follows.

**Scope and interpretation.** The new test b_p is a fixed-prime twist of a Gauss vector. Its orthogonality to any specified finite list follows because p may be chosen outside their support. The result only obstructs a finite list fixed independently of Y; in particular it says nothing against a growing family of twisted theta modes and gives no estimate for its orthogonal complement. The lower bound uses the source's all-natural-row moment, not its more delicate separate transport to squarefree rows. It also does not address whether a fixed smooth prime/Möbius vector has small projections onto every *growing* twist. Finally, the theorem is as conditional as the cited preprint inputs and does not prove a new zero-free region.

## Comparison with spectral and dispersion literature

No source located in this search proves an O(A+B), up to subpowers, squared operator remainder after a complete theta/residual projection in the full cubic or sextic residue-character matrix, uniformly in arbitrary growing twists and levels. This is a finding of the search, not a mathematical nonexistence assertion. The following distinctions matter:

* Dunn–Radziwiłł, [*Bias in cubic Gauss sums*](https://arxiv.org/abs/2109.07463v3), §1.4 and Propositions 9.1–9.2, subtract an explicit cubic polar correction in a structured dispersion estimate. Their coefficient hypotheses include rough squarefree support and cancellation against nonprincipal cubic symbols; the cited argument uses the generalized Riemann hypothesis for Hecke L-functions. Their congruence-extension proposition records explicit losses in moving factors. It is not a complementary arbitrary-coefficient operator norm.
* Dunn, [*Metaplectic cusp forms and the large sieve*](https://doi.org/10.2140/ANT.2025.19.1823), Theorem 1.5, gives bilinear estimates for Fourier coefficients of a fixed cubic metaplectic cusp form, with a polynomial dependence on a ray modulus. It is not a square-root norm bound for the character matrix after all residual modes are removed.
* De Faveri–Dunn–Hoffstein, [*Non-orthogonality of the cubic and quartic large sieves via Rankin–Selberg*](https://arxiv.org/abs/2607.07911v2), prove lower obstructions and discuss the difficulties of squarefree and level-uniform metaplectic correlations; their result is not a complementary norm upper bound.
* [rStation paper 10](https://rstation.ai/problems/riemann_hypothesis/papers/10) claims a volume-size continuous-remainder mean square for particular adjoint Gauss images. Section 8 conditionally compares a specified growing-dimensional row correction with a theta-residue matrix under a Gram hypothesis. Its error has explicit growing-label losses, and the paper expressly leaves the full complementary operator and its action on the Möbius/plain vector uncontrolled. This is a non-peer-reviewed source whose claims have not been independently checked here.
* [rStation paper 54](https://rstation.ai/problems/riemann_hypothesis/papers/54/v2) constructs and bounds a projection onto a specified family of moving cubic output modes. It explicitly does not establish completeness or control of the complementary output. Its bounds depend on source inputs and are not an independent verification of those inputs.
