# A universal lower bound for the positive support graph

**Status:** An unconditional combinatorial bound for the positive weighted gcd graph used to majorize a sextic character Gram matrix. It does not lower-bound the signed character operator or establish the existence of any large detector-selected family. No priority claim is made.

Let F be a finite set of distinct sixth-power-free Eisenstein elements u with `Nu≤Y`, counted with their actual unit and bad-prime choices, and let `M=#F`. Define the exponent-one support `A(u)` using primes away from 6, put `m_A=#{u∈F:A(u)=A}`, and define

    K_AB = sqrt(m_A m_B) (NA·NB/Y²)^(1/4) / N gcd(A,B).

For every ε>0,

    ||K|| ≫_ε M² / Y^(1+ε).                                   (1)

Thus `M≥Y^(1/2+η)` forces `||K||≫Y^(2η−ε)`, regardless of the support distribution or how F was selected. This is a limitation of the nonnegative majorant, not of the underlying character operator. PR94's bound `M≪Y^(.609371+ε)` is an **upper** count and does not show that any selected set has more than `sqrt(Y)` rows.

## Proof

Write the good part of a row ideal as

    (u)_good = A a₂²a₃³a₄⁴a₅⁵.

For fixed A, `N(a₂a₃a₄a₅)≤sqrt(Y/NA)`, and each prime in that radical has at most four nonunit exponent choices. Ideal counting and divisor bounds therefore imply, for every small fixed e>0,

    m_A ≪_e Y^e sqrt(Y/NA).                                  (2)

The choices at the two fixed bad primes and the six units cost a bounded factor.

Partition the supports into O(log(2Y)) dyadic intervals. Choose a bin `[U/2,U]` containing `m≫M/log(2Y)` rows, and let `F_U` be those rows. By (2), each support B in this bin has multiplicity `≪_e Y^e sqrt(Y/U)`.

Fix a row u∈F_U and a threshold T≥1. If `N gcd(A(u),B)≥T`, then some divisor D of A(u), of norm at least T, divides B. For `ND≤U`, ideal counting gives `#{B: NB≤U, D|B}≪U/ND`. Summing over the `≪_e Y^e` divisors of A(u) and multiplying by the bin multiplicity bound gives

    #{v∈F_U : N gcd(A(u),A(v))≥T}
       ≪_e Y^(2e) sqrt(YU)/T.                                (3)

Choose `T=C_e Y^(2e) sqrt(YU)/m`, with C_e large enough that at most `m/2` partners are excluded for each u. This T is at least 1 after enlarging C_e: (2) and ideal counting show `m≪_e Y^e sqrt(YU)`. Hence at least `m²/2` ordered pairs in F_U have gcd norm <T. On all of these pairs,

    (NA(u) NA(v)/Y²)^(1/4) / N gcd(A(u),A(v))
       ≫ sqrt(U/Y)/T.

Test K against `x_A=sqrt(m_A)` on the bin and zero elsewhere. Its squared norm is m, and its Rayleigh numerator is the sum of the left side over all ordered row pairs in F_U. Consequently

    ||K|| ≫ m sqrt(U/Y)/T ≫_e m² / Y^(1+2e).

The O(log Y) bin loss and `Y^(2e)` are absorbed into `Y^ε` by choosing e sufficiently small. □

This universal result strengthens the previous `M³/Y^(2+ε)` bound and does not require a coprime-pair hypothesis. It uses the particular nonnegative majorant and actual support multiplicities. A much smaller norm for the true signed character Gram matrix remains possible through cancellation.

The threshold `M≈sqrt(Y)` is attained at the power scale. Take every squarefree good Eisenstein ideal `a` of norm at most `sqrt(Y)` and select one generator of the principal ideal `a²` as a row. All rows are sixth-free, have the single exponent-one support A=1, and standard squarefree ideal counting gives `M≈sqrt(Y)`. The graph is the one-by-one matrix with entry `M/sqrt(Y)≈1`, while the lower bound `M²/Y` is also of constant order.

The power of M in (1) is also sharp throughout the intermediate range. Fix `1/2<α<1` and put `U=Y^(2α−1)` and `X=sqrt(Y/U)=Y^(1−α)`. Let the exponent-one supports A run through good prime ideals with `U/2≤NA≤U`. For each A take all good squarefree ideals R of norm at most X that are coprime to A, and select one generator of each row ideal `A R²`. The rows are sixth-free and have norm ≤Y. Prime-ideal and squarefree-ideal counts give `K≈U/log U` supports, `m_A≈X`, and `M≈UX/log U≈Y^α/log Y`. The graph has diagonal `w_A²/NA≪1/U` and off-diagonal `w_Aw_B≈1`, so its norm is `≈K≈Y^(2α−1)/log Y`. The lower bound `M²/Y` has the same power of Y, differing only by a logarithm. Constants can depend on the fixed α; no detector selection is claimed for these rows.

The same obstruction applies to the short-source target. In the graph upper estimate `L+Y||K||`, the second term is at least `M²/Y^ε` by (1). Thus showing this displayed upper bound is `≪[L+Y^(1−σ)L^σ]Y^ε` requires

    M ≪ [L+Y^(1−σ)L^σ]^(1/2) Y^ε.

For `L=Y^t` with `0≤t≤1` and `0≤σ≤1`, the right side has power `Y^((1−σ+σt)/2+ε)`. This is a necessary condition for **this positive-graph proof strategy**, not for the actual character norm: the graph itself only supplies an upper bound on that norm.

## Extension to n-free ideal families

The same proof holds over any fixed number field K for n-free ideals with fixed integer `n≥2`: define A using the good prime ideals of valuation exactly one, and delete any fixed finite set of bad primes. Permit at most H row labels per ideal, for fixed H. The constants may depend on K, n, the bad set, H and ε. Indeed the valuations at each bad prime have only n choices, the product of all good primes of valuation at least two has squared norm ≤`Y/NA`, and assigning each such prime an exponent in `{2,...,n−1}` costs only `Y^ε`. Standard ideal-counting and divisor bounds give (2) and (3) verbatim. No Kummer identification, roots of unity, or analytic hypothesis is needed. In fields with infinitely many units, the bounded-label condition prevents counting infinitely many generators of one ideal; the statement is naturally about ideals or a bounded choice of representatives.

**Independent review:** Families checked the per-support multiplicity, the dyadic-bin large-gcd count, the choice of T, the ordered-pair Rayleigh inequality, and the extension to n-free ideals with bounded labels. This is a mathematical review, not a formal proof in Lean.

**Second independent review:** High_match checked the bin and divisor counts, the Rayleigh bound, both sharpness examples and the fixed-number-field n-free extension.
