# Height-averaged marks: an exact transfer and the short-time barrier

**Status:** Elementary conditional reductions and an explicit finite-dimensional counterexample. No inverse moment, zero-free region, or RH is proved here. Fixed-row weights are required; detector-selected sets depending on t are outside the transfer.

Let F_Y be any finite row family with nonnegative weights v_u independent of t, supported on rows of norm ≪Y. Let M_u be any fixed inverse polynomial, and suppose its prime symbols have unit modulus when the prime is coprime to u and vanish otherwise. Fix `P=Y^z`, z>0, a nonnegative smooth prime profile U positive on a fixed subannulus, and define

    Q_u(t)=P^(−1/2) Σ_(p good) U(Np/P) χ_p(u) (Np/P)^(it).

In the rational quadratic case, distinct prime ideals have distinct norms. The Montgomery–Vaughan mean-value theorem gives, uniformly over all rows with `|u|≪Y`,

    (1/T)∫_0^T |Q_u(t)|²dt ≍ 1/log P,   T=C P,              (1)

for sufficiently large fixed C: the diagonal has ≍P/log P primes and each row is divisible by only O_z(1) of them. The upper and lower constants are independent of u and Y. Consequently

    (1/T)∫_0^T Σ_u v_u |M_u|² |Q_u(t)|²dt
       ≍ [1/log P] Σ_u v_u |M_u|².                            (2)

This is an equivalence with no polynomial height loss. Taking the quadratic full-relative inverse and squarefree row family of the [growth identity](../2026-10-29-riemann-quadratic-inverse-growth/README.md), its exact logarithmic limsup is therefore

    1 + r(2Θ_ζ−1),          0<r<1/2,                          (3)

up to the standard inputs of that note. An averaged upper bound `≪Y^(1+κ+ε)` for every ε>0 forces `Θ_ζ≤1/2+κ/(2r)`; κ=0 implies RH. This is an equivalence of the two moments at the specified averaging length, not a proof of either bound.

Over the Eisenstein field, group prime ideals by integer norm. Every norm fiber contains at most two prime ideals, so the diagonal is uniformly ≪1/log P. The two-twist parallelogram and `ξ³` row transport in the [Eisenstein frequency note](../2026-10-29-eisenstein-frequency-transfer/README.md) give the corresponding lower bound for `|Q_0(g,t)|²+|Q_0(ξ³g,t)|²`, with the fixed ξ-deleted inverse and the stated row-family restrictions. Thus the same comparison (2) holds for this sum of two marks. The lower half of the cubic full-inverse mean implies RH for ζ_E if its height-averaged marked moment were `≪Y^(1+ε)` for one r<1/2. An exact limsup identity for the cubic upper side also requires the additional source-qualified input specified in the cubic note.

## Why elementary short-time diagonalization cannot work uniformly

Fix any `0≤α<1`, set `T=P^α`, and fix any finite set of bounded twists `η_1,...,η_J` on the prime support. For arbitrarily large P there are coefficients `a_p`, with `|a_p|≤1` and

    P^(−1) Σ_p |a_p U(p/P)|² ≫ 1/log P,                         (4)

such that **all** the J twisted sums

    Q_j(t)=P^(−1/2) Σ_p a_p U(p/P) η_j(p) χ_p(u) p^(−it)

are smaller than a fixed negative power of P uniformly for `0≤t≤P^α`. Thus their average squares cannot have the diagonal lower bound ≫1/log P. The coefficients may be chosen after fixing one row u, absorbing its unit-modulus χ_p(u), and are then fixed independently of the remaining rows. This shows a limitation of a uniform rowwise argument with arbitrary coefficients, not a counterexample for the fixed physical choice `a_p=1` or an average over detector-selected rows.

To construct them, choose a compact subannulus of U's support on which U≥c>0. The prime number theorem gives N≈P/log P primes there. O_z(1) primes dividing the chosen row and any fixed bad primes may be discarded. Let k be a fixed positive integer and divide the ordered primes into consecutive blocks of size `Jk+1`. The sum of the spans of all disjoint blocks is O(P); hence, for a sufficiently large fixed B, at least a positive fraction of the blocks have span ≤B log P. This gives ≫P/log P good blocks.

On each good block choose x₀ equal to the log of its first prime and choose a nonzero vector c with `max_i |c_i|=1` solving the `Jk` homogeneous linear equations

    Σ_i c_i η_j(p_i) (log p_i−x₀)^h = 0,
        1≤j≤J,  0≤h<k.

There is a nonzero solution because the block has `Jk+1` coordinates. Set `a_(p_i)=c₀ c_i/[U(p_i/P)χ_(p_i)(u)]`, where c₀>0 is fixed small enough that `|a_(p_i)|≤1`, and set all other coefficients to zero. Since every good block has at least one coefficient of magnitude 1 before the fixed rescaling, (4) holds.

Taylor expansion of `exp(−it(log p_i−x₀))` cancels the first k terms for every j. Since each log-span is O(log P/P), each block contributes `O_{J,k}((T log P/P)^k)`. Summing at most O(P/log P) blocks and applying the P^(−1/2) normalization gives

    sup_(0≤t≤T) |Q_j(t)|
       ≪_(J,k) [sqrt(P)/log P] · [T log P/P]^k.             (5)

Choose any fixed `k>1/[2(1−α)]`. The right side then decays by a positive power of P. The same construction works for any fixed finite J; allowing J or k to grow with P changes the problem and is not covered. It does not establish that actual quadratic characters on physical rows can realize these tailored coefficient vectors.

**Independent review:** Families checked the short-time block count, nullspace construction, Taylor remainder, row/prime masks, coefficient mass and all exponents. The long-time equivalence follows from the separately reviewed frequency transfers.
