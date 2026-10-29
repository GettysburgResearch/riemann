# An exact long-prime obstruction to shortening a Möbius inverse

**Status:** An elementary structural obstruction, not a counterexample to a marked-moment theorem, a zero-free region, or a proof that every divisor decomposition fails. It identifies a coefficient class that any successful short-factor reduction must handle by an additional source estimate or genuine cancellation.

Fix a number field K and a finite bad-prime set S. Let W be a fixed nonzero nonnegative smooth annular profile, D→∞, and consider the centrally normalized inverse coefficient sequence

    a_D(n)=D^(−1/2) μ_K(n) W(Nn/D)     (n good).                 (1)

Fix 0<u<1. Suppose a finite sum of multiplicative convolutions is built entirely from factors supported on ideals of norm at most D^u; the factors may have arbitrary complex coefficients, arbitrary fixed bad-prime masks and arbitrary row-independent dyadic cutoffs. Every such convolution has coefficient zero at each prime ideal p with `Np>D^u`. Consequently it cannot equal (1) on an annulus where W is nonzero. This remains true no matter how many short factors are used: a nontrivial factor of a prime ideal is the prime itself.

The missed prime class is not power-negligible in coefficient ℓ². Choose a closed norm window inside the annulus where W≥c>0. The prime ideal theorem gives ≫D/log D good primes in that window, so

    Σ_{p good, Np>D^u} |a_D(p)|² ≫ 1/log D.                    (2)

In particular the residual after such a short-factor identity cannot have coefficient squared mass `O(D^(−η))` for any fixed η>0. On the trivial Kummer row, the prime-restricted response itself is `≍−sqrt(D)/log D`; this is a coefficient-level illustration only, since a physical detector may exclude that row. No comparable lower bound is asserted for the actual nonprincipal detector rows.

The obstruction persists beyond the one-prime term. If k≥2 is fixed and ku<1, choose k disjoint prime norm windows with `Np_i≈D^(1/k)>D^u` and product norm lying in an interval where W≥c. Unique ideal factorization and the prime ideal theorem give ≫`D/(log D)^k` distinct squarefree products `n=p₁⋯p_k`. Every nonunit divisor of such n has norm >D^u, so every convolution of solely D^u-supported factors again vanishes there; yet the normalized inverse coefficient squared mass on this class is `≫(log D)^(−k)`. Thus a reduction with a bounded number of explicitly handled long-prime slots must account for every feasible number of large prime factors; merely discarding their coefficient mass costs only logarithms, not a fixed power.

## What an exact finite identity actually produces

The obstruction is visible in a standard truncated reciprocal identity. Let

    M_U(s)=Σ_{Na≤U} μ_K(a)ψ(a)(Na)^(−s),
    L(s,ψ)=Σ_b ψ(b)(Nb)^(−s),

for a multiplicative zero-extended Hecke presentation ψ, initially on the absolute-convergence half-plane. Since `1−L(s,ψ)M_U(s)` has no Dirichlet coefficients of norms `1<Nn≤U`, its K-th power has no nonzero coefficient below the product scale U^K. Therefore, coefficientwise for `Nn≤U^K`,

    μ_K(n)ψ(n)
      = Σ_{j=1}^K (−1)^(j−1) binom(K,j)
          [(ψ·1)^{*(j−1)} * (ψ μ_K 1_{N·≤U})^{*j}](n).    (3)

Here `*` is ideal Dirichlet convolution, `(ψ·1)(n)=ψ(n)`, and the unit coefficient is included in each factor. Equation (3) is exact: it follows from `1/L = Σ_{j=1}^K (−1)^(j−1) binom(K,j)L^(j−1)M_U^j + (1−LM_U)^K/L` and the residual support. Choosing U≈D^(1/K) covers the original D-annulus.

However the `(j−1)` ordinary factors in (3) have no individual length bound U. If n=p is a prime of norm ≍D>U, all j short inverse factors must be units and one of the ordinary factors must carry p; the sum over j gives its required coefficient −ψ(p). In fact the combinatorial coefficient is exactly

    Σ_{j=2}^K (−1)^(j−1) binom(K,j)(j−1)=−1.

Thus (3) does not turn the prime part of the long inverse into a product of short inverse factors. A dyadic/Fourier separation may reorganize each right-hand term and a large inverse witness forces at least one of finitely many terms to be large, but the term still contains an unrestricted long ordinary factor or an explicitly long prime. A marked estimate whose permitted prime slots and ordinary lengths do not cover that factor cannot be invoked merely from the identity.

For numbers with all prime factors ≤D^u, there is a separate elementary balance lemma. Given an ideal n with norm ≍D, greedily multiply its prime factors until their product first exceeds a target T. The preceding product gives a divisor a with `T/D^u < Na≤T`, provided `D^u≤T<Nn`; hence both factors of n=a b can be made at most `O(sqrt(D·D^u))` by taking `T≈sqrt(D·D^u)`. This reduces the **support geometry** of smooth ideals to exponents `(1+u)/2<1`. It does not by itself factor the Möbius coefficient vector into a bounded sum of common row-independent products: the greedy choice, squarefree/coprime masks and smooth product profile must be separated, and a suitable **joint** moment for the two factors is still required. No such moment for the physical PR94-selected rows is supplied here.

The prime and k-prime obstructions are unconditional combinatorial facts. They do not rule out arithmetic cancellation in these classes, a marked theorem for a long prime, a well-controlled smooth/rough partition, or a new joint bilinear moment. Those are precisely the additional inputs needed before this route can be used to improve an individual ζ or L-function boundary.
