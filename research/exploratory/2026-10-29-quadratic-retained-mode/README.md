# Removing quadratic coefficient modes preserves the zeta growth exponent

**Status:** A classical-input extension of the [direct quadratic full-inverse identity](../2026-10-29-riemann-quadratic-inverse-growth/README.md). It does not prove a moment bound, RH, or a new zero-free region. The standard Dirichlet character-sum, ζ analytic and Heath-Brown quadratic-sieve inputs are those stated in that note; no priority claim is made.

Keep its fixed nonnegative annular profiles V,W, with `∫V>0` and Ŵ nonzero in `Re s>0`. For odd positive squarefree b put

    C_b(D)=D^(−1/2) μ(b) Σ_{a odd} μ(a) W(ab/D).

The original inverse block has the character expansion `M_d(D)=Σ_b C_b(D)χ_d(b)`, with d positive squarefree and d≡1 mod4. Let F be any fixed finite set of odd squarefree b, and remove precisely these **character modes**:

    M_d^F(D)=Σ_{b∉F, b odd squarefree} C_b(D)χ_d(b).             (1)

For `Θ_ζ=sup Re ρ` over nontrivial ζ-zeros and any fixed `0<r<1/2`,

    limsup_{X→∞} log[X^(−1)Σ_d V(d/X)|M_d^F(X^r)|²]/log X
        =r(2Θ_ζ−1).                                             (2)

This holds more generally for an arbitrary family of row-independent deletion sets F_X, provided that one fixed odd squarefree `b₀` belongs to none of them for all sufficiently large X. Thus F_X may itself grow or vary with X; the retained b₀ must be fixed in advance. Conversely, no assertion is made when every fixed character mode is eventually removed, or when the deletion depends on the individual row d.

## Correlating one retained mode

Choose a fixed odd squarefree `b₀∉F`, or the common retained b₀ in the varying-set version. The weighted diagonal row mass is

    Σ_d V(d/X)χ_d(b₀)²
       = C_V X h(b₀)+O_{b₀,V,ε}(X^(1/2+ε)),
    h(b₀)=∏_{p|b₀}p/(p+1)>0,   C_V=(2/π²)∫V.                 (3)

This is the squarefree mod-4 row count with the exact zero mask `(d,b₀)=1`. For b≠b₀, the product χ_d(b)χ_d(b₀) is the nonprincipal character of the odd squarefree exponent-difference kernel, times the mask at gcd(b,b₀). Its conductor is `≪_{b₀}b`; the fixed common-prime mask and mod-4 class are retained. The uniform smooth squarefree character bound from the parent note gives

    Σ_d V(d/X)χ_d(b)χ_d(b₀)
       ≪_{b₀,V,ε} X^(1/2+ε)b^(1/2+ε).                        (4)

Unconditionally, annular support and ideal-free divisor counting give `|C_b(D)|≪sqrt(D)/b` for b≪D and C_b=0 outside a fixed multiple of D. Thus summing (4) over any row-independent subset gives

    [Σ_d V(d/X) M_d^F(D)χ_d(b₀)]/[Σ_d V(d/X)]
       =h(b₀) C_{b₀}(D)+O_{b₀,V,W,ε}(X^(−1/2+ε)D^(1+ε)).   (5)

The implicit constants do not depend on F or F_X. The denominator is `C_V X+O(X^(1/2+ε))`; its correction is absorbed in the displayed error. Weighted Cauchy–Schwarz, with (3), gives

    Σ_d V(d/X)|M_d^F(D)|²
      ≥ |Σ_d V(d/X)M_d^F(D)χ_d(b₀)|² /
        Σ_d V(d/X)χ_d(b₀)².                                     (6)

The test χ_d(b₀) must be retained in this denominator; treating it as a constant one would ignore its ramified zero mask.

Let `P(Y)=Y^(−1/2)Σ_{a odd}μ(a)W(a/Y)`. Since μ(b₀)≠0,

    C_{b₀}(D)=μ(b₀)b₀^(−1/2) P(D/b₀).                         (7)

The Mellin transform of the unnormalized sum in P is `Ŵ(s)/ζ_odd(s)`, so a ζ-zero ρ of real part β gives `P(Y)=Ω(Y^(β−1/2−η))` for each η>0. For D=X^r, the error in (5) is smaller whenever `r(3/2−β+η)<1/2`, after shrinking its ε. For every r<1/2 this is true for all β≥1/2 and sufficiently small η. By (6) this supplies the lower side of (2), using zeros β arbitrarily close to Θ_ζ; at Θ_ζ=1/2 use any critical-line zero from Hardy's theorem.

## Upper side and the θ-strip criterion

If ζ is zero-free in `Re s>θ` with `1/2≤θ<1`, the reciprocal-zeta Mellin shift gives `|C_b(D)|≪D^(θ−1/2+η)b^(−θ−η)` for fixed η>0. Removing any subset of coefficients cannot increase their ℓ² mass, so

    Σ_{b∉F_X}|C_b(D)|² ≪ D^(2θ−1+2η).                           (8)

Heath-Brown's quadratic large sieve applies to odd squarefree b,d and Jacobi symbols `(b/d)`, which equal χ_d(b) on d≡1 mod4. Original gcd zeros agree. Removing the mod-4 restriction and the bounded nonnegative V only enlarges the row sum. Thus for D≤X,

    Σ_d V(d/X)|M_d^{F_X}(D)|²
       ≪_ε (XD)^ε (X+D)D^(2θ−1+2η).                            (9)

Let θ↓Θ_ζ to get the upper side of (2) if Θ_ζ<1. If Θ_ζ=1, the unconditional divisor bound gives `|M_d^{F_X}(D)|≪D^(1/2+ε)`, hence upper exponent r; zeros approaching 1 give the matching lower exponent. This proves (2).

More generally, for fixed `1/2≤θ<1` and `0<r<1/(3−2θ)`, the same proof shows the equivalence

    ζ has no zeros in Re s>θ
      ⇔  Σ_d V(d/X)|M_d^{F_X}(X^r)|²
             ≪_ε X^{1+r(2θ−1)+ε} for every ε>0,                (10)

provided one fixed b₀ is retained for all sufficiently large X. The forward direction uses (9) and r<1. For the reverse direction, a zero β>θ makes the error in (5) negligible because `r(3/2−β+η)<1/2` for sufficiently small η, and (6) contradicts the proposed exponent. In the same way the exact limsup (2) extends to `r<1/(3−2Θ_ζ)`.

Removing character modes in (1) is not the same operation as deleting finitely many n from the original inverse Dirichlet polynomial; it removes all convolution terms with that b index. Correlation with an arbitrary fixed retained b₀, rather than the original mean b₀=1, is what preserves the common ζ-pole detection.

## A growing low-mode deletion: a one-way zero-free implication

Fix `1/2≤θ<1`, `0<κ<1−θ`, and `0<r<1/(3+κ−2θ)`. Define the row-independent tail

    M_d^{>κ}(D)=Σ_{b odd squarefree, b>D^κ} C_b(D)χ_d(b).

If, for the fixed W and every ε>0,

    Σ_d V(d/X)|M_d^{>κ}(X^r)|²
        ≪_ε X^{1+r(2θ−1)+ε},                                  (11)

then ζ has no zero with `Re s>θ/(1−κ)`. The restriction κ<1−θ makes this conclusion nonvacuous. This is a one-way implication, not the fixed-mode equivalence (10).

Suppose a zero ρ has real part `β>θ/(1−κ)`. By the Mellin pole argument, for each sufficiently small η>0 there is an unbounded sequence Y_j with

    |A(Y_j)|≥Y_j^(β−η),    A(Y)=Σ_{a odd}μ(a)W(a/Y).

Choose an odd prime

    2Y_j^{κ/(1−κ)}≤p_j≤4Y_j^{κ/(1−κ)}

using the prime number theorem, and define `D_j=p_jY_j`, `X_j=D_j^(1/r)`. Then `p_j≈D_j^κ` and, with a fixed strict margin, `p_j>D_j^κ` because `p_j^(1−κ)>Y_j^κ`. Thus the p_j-mode is actually in the tail, while

    |C_{p_j}(D_j)|=D_j^(−1/2)|A(Y_j)|
       ≫ D_j^{β(1−κ)−1/2−η(1−κ)}.                         (12)

Correlate the tail with χ_d(p_j). The diagonal has row density `h(p_j)=p_j/(p_j+1)≥2/3`. For each b≠p_j the nonprincipal quadratic correlation has conductor `≪bp_j`, with the common-prime masks included. The same squarefree-d estimate and the trivial bound `|C_b(D)|≪sqrt(D)/b` yield, uniformly for p≈D^κ,

    [Σ_d V(d/X)M_d^{>κ}(D)χ_d(p)]/[Σ_d V(d/X)]
       =h(p)C_p(D)+O_ε(X^(−1/2+ε)D^(1+κ/2+ε)).             (13)

The diagonal row-count and denominator errors are smaller and included. Along X_j the error in (13) is smaller than (12) if

    r[3/2−β+κ(1/2+β)+η(1−κ)]<1/2.                            (14)

Since `β(1−κ)>θ`, the bracket is strictly below `3/2+κ/2−θ` after sufficiently small η; the assumed r bound gives (14). Weighted Cauchy–Schwarz then forces a moment lower exponent arbitrarily close to `1+r[2β(1−κ)−1]`, strictly above the exponent in (11), a contradiction.

A zero-free half-plane `Re s>θ/(1−κ)` does not by the elementary large-sieve coefficient argument imply (11). Its direct tail coefficient ℓ² bound carries exponent `(1−κ)(2θ/(1−κ)−1)=2θ−1+κ`, an extra κ. Additional cancellation would be needed to close that gap, and no such cancellation is asserted.

## A positive baseline for the growing tail

Every nonzero nonnegative smooth compact-annular W has a nonvanishing elementary tail diagonal. Let `B=sup supp W`; by the definition of support and continuity, W is bounded below by a positive constant on some closed interval J contained in `(B/2,B)`. This applies in particular to the infinite-convolution profile.

For b/D∈J and b odd, the support of W forces a=1 in the inner sum for C_b: every other odd a is at least 3, and `ab/D>B`. Consequently

    C_b(D)=μ(b)D^(−1/2)W(b/D)    when b/D∈J.                 (15)

Every such b exceeds D^κ for sufficiently large D whenever κ<1. The multiplicative weight h has positive average on odd squarefree integers: for Re s>1,

    Σ_{b odd sf} h(b)b^(−s)
      =ζ_odd(s) ∏_{p odd}(1−p^(−s))(1+[p/(p+1)]p^(−s)).    (16)

The product is holomorphic and nonzero near s=1, with positive value there, since each local factor is nonzero and differs from 1 by `O(p^(−1−Re s)+p^(−2Re s))`. A nonnegative smooth minorant supported in J and Mellin inversion therefore give

    Σ_{b odd sf, b/D∈J} h(b) ≫ D.

Equations (15)–(16) imply that the tail's diagonal energy satisfies `Σ_{b>D^κ}h(b)|C_b(D)|²≫1`. The covariance asymptotic of the parent note holds for this row-independent cutoff with the same error `O_ε(X^(−1/2+ε)D^(2+ε))`. Therefore, for every fixed r<1/4,

    Σ_d V(d/X)|M_d^{>κ}(X^r)|² ≫ X.                           (17)

In this range any proposed upper bound with a strictly negative D-power relative to X is false, independent of ζ's zeros. For example, a bound at scale `X D^{−κ+ε}` with small ε cannot hold. The one-way implication above remains logically valid, but such an impossible bound would not be a useful target. Equation (17) does not resolve tail moments whose proposed exponent is at least 1 or extend the elementary covariance estimate beyond r<1/4.
