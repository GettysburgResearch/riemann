# Fourth moments in the theta cube tail

**Status.** A source-qualified restricted-dual estimate, independently checked internally but not a full inverse-moment bound or an individual zero-free theorem. It assumes Goldmakher–Louvel's quadratic sieve, de Faveri's Θ₆, the October 5 completed-theta `prop:R` and cube inversion, and the physical fixed-sector Poisson/mask/Fourier ledger cited in [the quadratic-prefix tail note](../2026-10-29-quadratic-sieve-theta-tail/README.md). No Hu zero-free hypothesis is used. The imported analytic sources and physical matching have not been externally verified here.

Use that note's notation: B actual b-rows, fixed k of norm ≈K, squarefree source label f of norm F, theta column scale D, and cube index c. The short cube-index mean is

    ||short||²_(ℓ²_b) ≪ (BKD F)^ε [BK+W C³],
    W=B²K²F/D.                                                  (1)

The prefix `A_b(x)` of the Möbius/angular/quadratic coefficient in the cube inversion satisfies

    Σ_(Nb≤B)|A_b(x)|⁴ ≪ (BKxF)^ε [B x²+B^(1/2)x⁴].             (2)

To see this, square the prefix, convolve its squarefree c-coefficients, split the resulting column as a squarefree part times a square, and split b in the same manner. The GL quadratic sieve applies to each pair of fixed square parts; all overlap zeros are row contractions or common column masks. Divisor bounds give squared column mass `≪x^(2+ε)/(Nv)²`, and Minkowski sums `Σ1/Nv≪log x`. The fixed χ_c(k)^3 and f masks remain common coefficients.

For the completed theta sum,

    Σ_(Nb≤B, b sixth-free)|T_{bk}(Z;f)|⁴
       ≪ (BKZF)^ε [B+Z²+B^(5/6)Z^(2/3)+B^(1/3)Z^(5/3)].      (3)

Indeed first fix one source theta cube index q. Its factor `χ_q(bk)^3` is a bounded b-row contraction and its exterior coefficient has modulus `1/Nq`. The remaining squarefree n-polynomial, when squared, has column valuations ≤2 and hence is Θ₆-admissible; its normalized coefficient mass is `≪Z^ε`. Apply de Faveri's printed Θ₆ to the **actual** sixth-free b rows, then use ℓ⁴ Minkowski and `Σ_(Nq≲Z^(1/3))1/Nq≪log Z`. The factors χ_n(k) and χ_n(f)^4 are common column multipliers and preserve every original zero. The same argument applies to `∂_(log Z)T`, using a fixed differentiated profile.

Apply Stieltjes partial summation in c and Hölder in the b-row sum, using (2) and (3) at `Z=D/(Nc)³`. If

    U=B^(1/2)C^(−1/2)+B^(3/8)log D
      +B^(1/4)D^(1/2)C^(−2)+B^(1/8)D^(1/2)C^(−3/2)
      +B^(11/24)D^(1/6)C^(−1)+B^(1/3)D^(1/6)C^(−1/2)
      +B^(1/3)D^(5/12)C^(−7/4)+B^(5/24)D^(5/12)C^(−5/4),

then `||tail||_(ℓ²_b)≪(BKDF)^ε U`. The first two terms are `≪sqrt B` up to logs. The other six come from the two faces of (2) against the four faces of (3); the only logarithmic integral is the second term displayed. All products with the row-dependent derivative are controlled by Hölder, not by moving that derivative outside the row sum.

Balance `W C³` in (1) with each of the six squared nontrivial tail terms. If at least one balance cutoff is ≥1, choose the largest cutoff; all are ≤D^(1/3) for B,K,F≥1. Up to small powers the resulting mean is bounded by BK plus the sum of the following six monomials (columns are powers of B,K,F,D):

    (19/14, 8/7,   4/7,  −1/7),
    (9/8,   1,     1/2,   0),
    (27/20, 4/5,   2/5,  −1/5),
    (1,     1/2,   1/4,   0),
    (18/13, 14/13, 7/13, −2/13),
    (25/22, 10/11, 5/11,  0).                                (4)

For example, the first row denotes `B^(19/14)K^(8/7)F^(4/7)D^(−1/7)`. We do **not** assert a global small-C fallback for (4). In the physical residual core and b-ranges below, at least the first balancing cutoff is ≥1 even after the source's mask-divisor expansion; this is checked explicitly next.

## Physical core and mask-divisor guard

Write `Nd₀≈Y^d`, `Nk≈Y^κ`, `Ng≈Y^g`, sixth-free dual core `Nb≈Y^b`, and `P=Y^(6/5)`. The physical ledger has `D≈P/(D₀G)`, dual norm `H≲P²K/(Y D₀²)`, and norm-prefactor `Y^(1/30)D₀^(2/3)K^(−5/6)B^(−1/6)`. Open the combined a,d′ mask over `e|rad(a d′)` as in the quadratic-tail note. The source label is `f=gke`, while the residual scale is `D′=D/Ne`. Taking square roots for Minkowski and including the exterior `(Ne)^(−1/2)`, the six rows of (4) have e powers

    −1/7, −1/4, −1/5, −3/8, −2/13, −3/11.                      (5)

All divisor sums are therefore subpower. The first balance cutoff is ≥1 when `D′²≥B^(3/2)K²Nf`. Since `Na≲(H/B)^(1/6)` and `Nd′≈D₀/K`, for every e in the mask expansion its logarithmic margin is at least

    17/10 − 4d − 3g − κ/2 − b.                                (6)

In either residual core `d+g+6κ/5≤C₀`, `0≤κ≤d`, with `C₀≤7/50`, (6) is ≥`17/10−4C₀−b`. It is strictly positive for all b in the ranges claimed below, so every mask term has a valid cutoff ≥1. This check is essential; a base-scale guard alone would not control a moving e.

After the physical prefactor, the six monomials of (4) have core-uniform exponents at most

    −29/210 + (17/21)C₀ + (25/21)b,
       1/30 +  (2/3)C₀ + (23/24)b,
    −31/150 + (13/15)C₀ + (71/60)b,
       1/30 +  (2/3)C₀ +  (5/6)b,
    −59/390 + (32/39)C₀ + (95/78)b,
       1/30 +  (2/3)C₀ + (32/33)b.                            (7)

Each maximum occurs at d=C₀, κ=g=0; the BK face is no larger than the fourth displayed bound. This follows by linear optimization over `0≤κ≤d`, `d+g+6κ/5≤C₀`. For `C₀=7/50` the fifth face is the limiting one at exponent 21/20, giving

    b≤223/250=0.892.                                           (8)

For the staged θ threshold `E*=19949123/18750000` and `C₀=1925877/15625000`, the same face is limiting, and a fixed strict margin gives

    b<1357811867/1484375000≈0.91473642.                          (9)

The full square and artificial diagonal are bounded separately in every g-dyad as in the source ledger; no local diagonal cancellation is asserted. Summing dyads costs only X^ε. This controls the specified small-divisor/core part of those dual frequencies and leaves the complementary sixth-free core open. Neither the imported theta/Poisson identities nor the resulting full inverse target are proved here.

**Independent internal reviews.** High_match and Other_families checked the prefix and completed-theta fourth moments, eight Abel terms, six balance faces, moving-e divisor losses and cutoff guard, vertex maxima, and both exact thresholds. Their reviews assume the stated external source and physical-calibration inputs.

**Independent review.** High_match checked the A₄/T₄ reductions, actual row masks and fixed profiles; Other_families checked the Abel terms, six balances and moving-e guard. [check_exact.py](check_exact.py) independently verifies the physical monomials, e powers and residual-core maximizers. None of these reviews establishes the imported analytic identities or the remaining large-core complement.
