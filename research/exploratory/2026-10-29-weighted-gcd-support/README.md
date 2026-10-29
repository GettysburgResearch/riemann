# A weighted gcd-graph bound for sixth-order source operators

**Status:** A source-conditional operator estimate proved from standard fixed-field Kummer reciprocity and Hecke functional equations. It applies to structured families and arbitrary ordinary ideal sources. It does not prove a zero-free region, and no novelty or optimality claim is made. Its arithmetic normalization and estimates were independently reviewed; see [the detailed audit](../2026-10-29-complete-source-four-cycle/INDEPENDENT-ARITHMETIC-REVIEW.md) and the review note below.

Let `K=Q(sqrt(-3))`, and let χ_I(u) be the tracker’s zero-extended sextic residue character. Let F be a finite set of nonzero sixth-power-free element rows with `Nu≤Y`, and S any finite set of nonzero integral ideals with `NI≤L`, where Y,L≥2. A zero source ideal, if admitted, is a zero column and can be discarded. Define the squared operator norm

    N(F,S)=sup_{Σ_{I∈S}|b_I|²=1} Σ_{u∈F}|Σ_{I∈S}b_I χ_I(u)|².

Remove the two primes above 2 and 3 from each row ideal and factor its good part as

    (u)_good = a₁ a₂² a₃³ a₄⁴ a₅⁵,

with pairwise-coprime squarefree ideals a_j. Let 𝒜 be the distinct values of a₁, let `F_A={u∈F:a₁(u)=A}`, let `m_A=#F_A`, and set

    w_A=√m_A · (NA/Y)^(1/4),
    H(A,B)=1/N gcd(A,B),             D=diag(w_A).

Then for every ε>0,

    N(F,S) ≪_ε [L + Y ||D H D||_{2→2}] (LY)^ε.             (1)

The constant depends only on ε and the fixed Eisenstein field. The row and source sets may be selected by any conditions; (1) itself uses no amplitude or zero-location assumption.

## Proof

Choose a fixed nonnegative smooth W with W=1 on [0,1] and W=0 on [2,∞). The row Gram matrix for S is positive-semidefinite bounded by the complete weighted Gram matrix

    G_W(u,v)=Σ_{I≠0} W(NI/L) χ_I(u) overline(χ_I(v)).

Define `g(u)` by deleting the bad-prime powers from `(u)` and, for rows in different good-valuation blocks,

    Q(u,v)=∏_{p∤6 : v_p(u)≠v_p(v) mod 6} Np.

At a good p, the quotient Kummer character is tamely ramified exactly when the valuation difference is nonzero modulo 6, with conductor exponent 1. Its primitive conductor therefore has norm `≪Q(u,v)` and it is nonprincipal. A common p with equal positive valuations is absent from this conductor but remains a zero mask in the original source; retain it as an Euler-factor deletion. On the shifted line `Re s=−η`, all such deletions cost `(LY)^ε` after choosing η small. The source prime over 3 contributes zero; split off powers of the norm-4 prime over 2, retaining its actual bounded local factor. There are O(log(2L)) such pieces and each nonempty piece has rescaled length at least 1/2.

For each piece, the nonprincipal finite-order Hecke L-function has an entire completion and a Γ_C(s) factor, so L(0)=0 and cancels the simple pole at 0 of W’s Mellin transform. A shift to `Re s=−η` and the functional equation give

    |G_W(u,v)| ≪_ε sqrt(Q(u,v)) (LY)^ε                    (2)

between distinct good-valuation blocks. Within one such block, there are at most 216 rows (six units and six choices for each of the two bad-prime valuations); its entries are O(L) by ideal counting, so its operator norm is O(L).

For u∈F_A, let `T_u=a₂a₃a₄a₅`; then `NT_u≤sqrt(Y/NA)`. Put a=NA, b=NB, g=N gcd(A,B). If A≠B, their common primes have exponent 1 in both rows, so

    Q(u,v) ≤ (ab/g²) NT_u NT_v ≤ Y sqrt(ab)/g².

By (2), the Hilbert–Schmidt norm of the A,B block of G_W is at most `Y w_A w_B/g · (LY)^ε`. This remains true when a prime in A\B also occurs in the other row's T: the right-hand side merely counts it more than once. Within an A block, separate the bounded good-valuation subblocks: the off-block terms have `sqrt(Q)≤sqrt(Y/a)`, giving norm `≪L + m_A sqrt(Y/a)(LY)^ε = L + Y w_A²/a·(LY)^ε`.

For a vector x, write `x_A` for its restriction to F_A. Bounding each block quadratic form by its operator norm and applying the scalar Rayleigh quotient to the vector `(||x_A||)_A` gives (1). □

## A polynomial-size, large-radical example

Let Y tend to infinity. Pick good prime ideals D and R of norms comparable respectively to `Y^(1/5)` and `Y^(1/4)`, and distinct good primes p_j, all coprime to DR, of norm comparable to `Y^(3/10)`. Choose norm intervals with upper endpoints `Y^(1/5)`, `Y^(1/4)` and `Y^(3/10)` so that the sixth-power-free rows `u_j=D p_j R²` have norm at most Y and at least a fixed multiple of Y. In the Eisenstein PID choose one generator per row. Prime-ideal counting supplies `M≈Y^(3/10)/log Y` rows.

Their exponent-one supports are `A_j=D p_j`, so `NA_j≈Y^(1/2)`, each `m_{A_j}=1`, and `w_{A_j}²≈Y^(−1/4)`. For i≠j, `gcd(A_i,A_j)=D`, giving

    ||D H D|| ≪ M·Y^(−1/4)/ND
                 ≪ Y^(−3/20)/log Y.

Thus for L≥Y, (1) gives `N(F,S)≪_ε L(LY)^ε`, even though M is a fixed positive power of Y and `N(rad(u_j))≈Y^(3/4)>sqrt(Y)`. The unweighted support graph alone has norm ≫M/ND≈Y^(1/10)/log Y, so the actual per-block weights are material. Any selected subfamily also satisfies the bound by row monotonicity.

## What is still missing for physical detector rows

The actual row-count input around the difficult PR94 point is only `M≤Y^(α+ε)`, with `α≈0.609371`. Cardinality alone does not bound the weighted graph norm. For distinct prime rows of norm comparable to Y, each m_A=1, w_A≈1, and distinct supports are coprime; hence `||D H D||≈M`. The accompanying [four-cycle note](../2026-10-29-complete-source-four-cycle/README.md) explicitly constructs a **tailored arbitrary prime-slot vector** selecting a polynomial number of such prime rows at any fixed σ<1, showing that broad amplitude selection alone cannot force this graph to be small. This is a limitation of the positive majorant, not a counterexample to the true selected operator. The construction does not meet the fixed smooth physical-slot or detector-zero conditions automatically.

A concrete sufficient distribution condition is the weighted degree bound

    max_A w_A Σ_B w_B/N gcd(A,B) ≪ (LY)^ε.                 (3)

It implies `||D H D||≪(LY)^ε` by Schur's test and gives the desired long-source size when L≥Y. A sufficient alternative is the stronger weighted gcd-energy bound

    Σ_{A,B} w_A²w_B² / N gcd(A,B)² ≪ (LY)^(2ε),            (4)

by the Frobenius norm. Neither condition is proved for the actual detector rows. Establishing one would require new information about how the fixed prime spike and zero-location constraints distribute their exponent-one supports; if those supports can be nearly coprime, a proof must exploit signed character cancellation beyond (1).

**Independent review:** Families checked the Kummer conductor masks, cross-overlap primes, weighted Hilbert–Schmidt exponents, bounded 216-row local blocks and PSD/block-Rayleigh argument. High_match separately checked the unweighted gcd graph and its source normalization; the weighted refinement is explicitly the subject of the first review. The fixed-field Kummer/Hecke facts are analytic inputs, not a Lean proof of this theorem.
