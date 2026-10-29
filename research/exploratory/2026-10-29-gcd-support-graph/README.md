# A cross-support gcd graph bound

**Status:** A structured-family operator estimate conditional on the standard Kummer character identification and finite-order Hecke functional equation in the [pairwise conductor note](../2026-10-29-complete-source-four-cycle/README.md). It controls some unions of exponent-one support blocks, including examples that satisfy the broad amplitude-selection test. It does not prove the long-source estimate for all detector-selected rows, nor an individual zero-free region.

Let F consist of sixth-power-free Eisenstein element rows of norm at most Y, with fixed bounded row-label multiplicity per ideal. As in the source note, source ideals lie in S_L={I:NI≤L} and retain the original local masks. Write the good part of each row uniquely as

    (u)_good = A_u a₂(u)² a₃(u)³ a₄(u)⁴ a₅(u)⁵,
    T_u = a₂(u)a₃(u)a₄(u)a₅(u),

with all displayed squarefree ideals pairwise coprime. Let 𝒜 be the distinct A_u and set

    H_{A,B}=1/N(gcd(A,B)),     A,B∈𝒜.

Then for every ε>0, and every subset S⊆S_L,

    selectedNorm(F,S) ≪_ε (L+Y||H||_{2→2})(LY)^ε.             (1)

Here `selectedNorm` is the squared source-to-row operator norm, not its square root. Since H is a symmetric nonnegative matrix, its spectral norm can be estimated by Schur weights or by any valid graph bound.

## Proof and cross-support primes

Write `a=NA`, `b=NB`, `d=N gcd(A,B)`. The row-size constraint implies `NT_u≤(Y/a)^(1/2)` and `NT_v≤(Y/b)^(1/2)`. The tame pair conductor Q(u,v) is the product of good primes whose row valuations differ modulo six. Every common prime of A and B has valuation 1 in both rows and is excluded from Q. Every other contributing prime divides `A B T_u T_v`. Hence

    Q(u,v) ≤ [ab/d²] NT_u NT_v,
    sqrt(Q(u,v)) ≤ sqrt(Y)(ab)^(1/4)/d.                         (2)

The cross terms require care: a prime in A\B may divide T_v, and a prime in B\A may divide T_u. Its exponents are then different, so it can contribute to Q; the right side of (2) counts it twice and remains an upper bound. Likewise equal higher exponents only make the bound looser. No cancellation is asserted at these primes.

For each A the elementary factorization count, including units and bounded bad-prime exponents, yields

    M_A=#F_A ≪_ε (Y/a)^(1/2)(LY)^ε.                            (3)

For A≠B, different good valuation vectors give a nonprincipal pair character. The smooth Gram majorant and Hecke functional equation in the source note bound each off-block entry by `sqrt(Q(u,v))(LY)^ε`, retaining all deleted Euler factors. Equations (2)–(3), and the matrix estimate `||C||≤max|C_uv| sqrt(M_A M_B)`, yield

    ||G_W[F_A,F_B]|| ≪_ε (Y/d)(LY)^ε.                           (4)

For A=B, use the previously established same-support bound instead: the whole positive semidefinite diagonal block has norm `≪(L+Y/a)(LY)^ε`. This includes equal-good-valuation groups that may have a principal pair character; one must not apply the nonprincipal off-block estimate to such pairs.

For an arbitrary row vector x, let `z_A=||x|_{F_A}||₂`. The diagonal and cross-block bounds give

    x*G_W x ≪_ε (LY)^ε [L Σ_A z_A² + Y zᵀ H z]
             ≤ (LY)^ε [L+Y||H||] ||x||₂².

The smooth weighted Gram majorizes the Gram for every subset S in positive semidefinite order. This proves (1), subject to the same standard arithmetic inputs as the source note. No claim is made that the signed off-diagonal Gram is itself positive.

## A common-support regime

If every exponent-one support A contains the same good squarefree ideal D and K=#𝒜, then `H_{A,B}≤1/ND`, so

    selectedNorm(F,S) ≪_ε [L+YK/(ND)](LY)^ε.                 (5)

In particular, if L≥Y and `K≤ND·(LY)^ε` up to an arbitrarily small loss, (5) is a long-source-size bound. It permits polynomially many support blocks and is useful even when `ND<sqrt(Y)`, a range where the earlier crude common-divisor cardinality bound `L+(Y/ND)²` need not be O(L). It can also be markedly stronger than the vertical-stacking bound K·L.

For a concrete nonempty regime, take a good prime ideal D with norm ≍Y^(1/3), another fixed good prime R with norm ≍Y^(5/24), and K≈Y^(1/4)/log Y distinct good primes P_i with norms ≍Y^(1/4). Choose fixed interval constants so `N(D P_i R²)≤Y`, and take one generator of each ideal `D P_i R²` in the Eisenstein ring. All are sixth-power-free, with A_i=D P_i and row norm ≍Y. Here K/ND≈Y^(−1/12)/log Y, so (5) gives the target `O(L(LY)^ε)` for L≥Y. The previous `L+(Y/ND)²` bound gives only `L+Y^(4/3)`, and vertical stacking gives O(KL). This establishes a structured family, not that an arbitrary physical detector output lies in it.

The example can also meet the broad single-slot amplitude selection from the source note. Restrict to a positive-proportion finite ray class of the rows, take a prime slot P=Y^0.98, and choose the same row-independent coefficients by the source note's torus maximization. The slot primes are coprime to all row factors. With M=K≈Y^(1/4)/log Y, every row has squared response `≫P/(M² log²P)=Y^(0.48−o(1))`, exceeding P^0.446=Y^0.43708 for large Y. These are coefficients tailored to the family, so this does not assert the same selection for fixed smooth physical slots or a detector-zero condition.

## Limitations

If all supports are pairwise coprime, then every off-diagonal H entry is 1, so `||H||≥K−1` and (1) reduces to a loss of order YK. In particular the prime-row torus example in the source note still shows that broad amplitude selection does not force the gcd graph to be small. More generally, (1) takes absolute values of row correlations and cannot exploit cancellations between distinct A-blocks. Establishing an O(L) bound for arbitrary selected families would require additional structural information about their support graph or a signed cross-block estimate; neither is supplied here.
