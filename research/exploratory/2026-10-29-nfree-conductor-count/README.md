# Counting full n-free character and prime-degree field families

**Status.** This is a classical Euler-product and Tauberian count, combined with the standard tame conductor and finite-bad-place properties of the fixed FHL character family. It sharpens the denominator in the source-dependent family-density results; it is not a zero-free theorem or a novelty claim. The primes and fields K,n,S, and the unitary twist ν are fixed throughout.

Let `n≥3`, let K contain μ_n, and let the n-free good ideals be `g=∏_{j=1}^{n−1} a_j^j` with the a_j pairwise-coprime squarefree good ideals. Then, for a positive constant C,

    #{g : N rad(g)≤X} ∼ C X(log X)^{n−2}.                         (1)

Indeed for a fixed squarefree radical a there are `(n−1)^ω(a)` exponent assignments. Put k=n−1 and write

    F(s)=∑_{a good, sf} k^ω(a)/(Na)^s
        =∏_{p∉S}(1+k(Np)^(−s))
        =ζ_{K,S}(s)^k H(s),
    H(s)=∏_{p∉S}(1+k(Np)^(−s))(1−(Np)^(−s))^k.                 (2)

The Euler product for H converges locally uniformly in `Re s>1/2`, and `H(1)>0`. The deleted zeta function has a simple pole with positive residue. A standard positive-coefficient Tauberian theorem for a pole of order k therefore gives (1), with

    C = H(1) [Res_{s=1} ζ_{K,S}(s)]^k / Γ(k) > 0.

At each good prime dividing g, the local Kummer character has conductor exponent 1 and its tame inertia exponent is exactly the valuation of g modulo n. The fixed twist ν is unramified there. The finitely many possible local n-torsion classes at the bad primes and the fixed ν give a constant C₀ with

    N rad(g) ≤ N cond(νχ_g) ≤ C₀ N rad(g).                       (3)

The label-to-character map is injective, even after the fixed twist ν: if `νχ_g=νχ_h`, source multiplicativity makes the primitive character induced by `χ_{g h^{n−1}}=χ_g χ_h^{n−1}` principal. If a good valuation of g and h differed, the valuation in `g h^{n−1}` would be nonzero modulo n, forcing that prime into its conductor, a contradiction. This uses de Faveri §2.5.1, equation (2.4), and its good-conductor formula; it does not depend on choosing an orientation for the tame local exponent. Taking radical cutoff X/C₀ in (1) gives

    #{νχ_g primitive-inducing : N cond(νχ_g)≤X}
       ≫_{K,S,n,ν} X(log X)^{n−2}.                              (4)

For ν=1 and n=4, the labels with no odd valuation have the form a² and contribute O(X); all other labels have local order four somewhere. Hence (4) still holds with exact order four. If n=p is prime, all nonunit labels have exact order p, and each corresponding cyclic degree-p extension has exactly p−1 nontrivial characters. By injectivity, its label fiber has at most p−1 elements, so (4) gives ≫X(log X)^{p−2} distinct fields with conductor cutoff X.

Every nontrivial power of an order-p character has exactly the same local kernels and conductor. The conductor–discriminant formula `|D_L|=|D_K|^p(Nfχ)^{p−1}` then gives the field lower bound

    #{L in this constructed family : |D_L|≤Y}
       ≫ Y^{1/(p−1)}(log Y)^{p−2}.                              (5)

The logarithmic denominator improvement is compatible with, but not needed for, the power-saving exceptional counts in the [quartic/quintic summary](../2026-10-29-quartic-quintic-conductor-summary/README.md) and the [cyclic-prime quotient application](../2026-10-29-cyclic-prime-degree-density/README.md). No claim is made that the constructed fields exhaust all cyclic degree-p extensions.

**Independent review.** High_match checked the Euler product and Tauberian constant, bounded fixed bad conductors, character injectivity, exact-order exclusions, field fibers and discriminant exponents.
