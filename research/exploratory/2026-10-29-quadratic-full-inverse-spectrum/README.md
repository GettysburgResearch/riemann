# A quadratic-family inverse moment equivalent to the zeta zero boundary

**Status:** Proposed exact implication using classical quadratic reciprocity, smooth character sums and Mellin inversion; independent audit requested. This is a reformulation of the Riemann zeta zero boundary, not a proof of RH or a new zero-free region. No priority claim is made.

Fix nonnegative C∞ annular functions V,W, with `∫V>0`, and choose W once using the [infinite-convolution construction](../2026-10-29-cubic-full-inverse-mean/README.md): its Mellin transform is nonzero on Re s>0. Let d range over positive squarefree integers with d≡1 (mod 4), so d is a positive fundamental discriminant and χ_d is the primitive quadratic character modulo d. Let superscript (2) mean that the Euler factor at 2 is deleted. For n odd define

    [ζ^(2)(s)L^(2)(s,χ_d)]^(−1) = Σ_{n odd} c_d(n)n^(−s),
    c_d(n)=Σ_{ab=n} μ(a)μ(b)χ_d(b),
    M_d(D)=D^(−1/2) Σ_{n odd} c_d(n) W(n/D).          (1)

For d>1 the product inverted in (1) is the 2-deleted Dedekind zeta of Q(√d). All zero masks at primes dividing d are retained. Put

    Θ_ζ=sup{Re ρ: ζ(ρ)=0, 0<Re ρ<1}.

For every fixed `0<r<1/2`, the following identity follows from the classical inputs described below, including Heath-Brown’s quadratic large sieve. The elementary proof first establishes the range r<1/4; the final section extends it:

    limsup_{X→∞} log[X^(−1) Σ_{d sf, d≡1(4)} V(d/X)|M_d(X^r)|²]
                   / log X = r(2Θ_ζ−1).                (2)

Interpret log 0 as −∞ if necessary. In particular, for any one such r and the single fixed W above,

    RH for ζ  ⇔  Σ_d V(d/X)|M_d(X^r)|² ≪_ε X^(1+ε)
                  for every ε>0.                       (3)

This is a moment criterion for RH, not a derivation of its right-hand side. The proof does not import the cubic conductor sieve or the tracker zero-free theorem. It does use the classical existence and functional equation of nontrivial ζ zeros, standard smooth Dirichlet-character estimates, and the stated squarefree averaging.

## Uniform first and second character averages

The weighted family size is

    N_V(X)=Σ_{d sf, d≡1(4)} V(d/X)=c_V X+O_V(X^(1/2+ε)), c_V>0.  (4)

For odd squarefree b>1, uniformly in b,

    Σ_{d sf, d≡1(4)} V(d/X)χ_d(b)
       ≪_ε X^(1/2+ε)b^(1/2+ε).                         (5)

Likewise, for distinct odd squarefree b,b',

    Σ_{d sf, d≡1(4)} V(d/X)χ_d(b)χ_d(b')
       ≪_ε X^(1/2+ε)(bb')^(1/2+ε).                    (6)

For odd b, χ_d(b)=(d/b), the Jacobi symbol. In (6) the product character is nonprincipal: after removing common prime factors its primitive odd conductor is the nonempty squarefree symmetric difference of b and b'. The mod-4 projection `1_(d≡1 mod4)` is a fixed combination of principal and χ₄ characters; it cannot cancel ramification at any odd prime. Extra zeros from common factors are restored by divisor inclusion–exclusion. Expand μ²(d)=Σ_{k²|d}μ(k). For each of O(X^(1/2)) possible k, the remaining smooth sum of a nonprincipal Dirichlet character of conductor q is `≪_ε q^(1/2+ε)`, uniformly in its length, by one-dimensional Poisson summation and the primitive Gauss identity; imprimitive masks cost q^ε. This gives (5)–(6). Equation (4) follows by the same squarefree expansion and elementary smooth counting in fixed residue classes. Its constant is `c_V=(2/π²)∫₀^∞V(t)dt`.

## Mean, lower bound, and converse

Averaging (1) with (4)–(5) yields

    [Σ_d V(d/X) M_d(D)]/N_V(X)
       = D^(−1/2) Σ_{a odd} μ(a) W(a/D)
           + O_ε(X^(−1/2+ε)D^(1+ε)).                    (7)

Indeed b=1 gives the main term; for b>1, (5), the divisor bound and `ab≪D` give the error. The unnormalized main sum has Mellin transform

    Ŵ(s)/ζ^(2)(s).                                        (8)

If ζ has a zero ρ=β+iγ with β>1/2, Ŵ(ρ) and `1−2^(−ρ)` are nonzero, so (8) has a pole. The usual Mellin-analytic-continuation argument implies that for every η>0 its normalized sum is Ω(D^{β−1/2−η}). At β=1/2 the same argument applies to any nontrivial critical-line zero, which exists in the case Θ_ζ=1/2 by the classical existence and functional equation of nontrivial ζ zeros. For fixed r<1/2 choose η and the preliminary error loss small enough that the error in (7) is negligible along the Ω sequence. Weighted Cauchy–Schwarz and (4) yield the lower half of (2), including the case where the supremum Θ_ζ is not attained.

Conversely, assume ζ is zero-free in Re s>θ for a fixed `1/2≤θ<1`. Mellin inversion and standard reciprocal-zeta polynomial growth on `Re s≥θ+η` give for the inner μ-sum

    Σ_{a odd} μ(a) W(ab/D) ≪_{W,η} (D/b)^(θ+η).        (9)

The reciprocal has a zero, not a pole, at s=1. Thus write

    M_d(D)=Σ_{b odd, sf} c_b χ_d(b),
    |c_b| ≪ D^(θ−1/2+η)b^(−θ−η).                       (10)

Only b≪D contribute. The original unsummed double convolution gives `Σ_b |c_b|≪D^(1/2+ε)`. Expanding the weighted second moment, the diagonal b=b' is bounded by

    ≪ X D^(2θ−1+2η) Σ_b b^(−2θ−2η)
      ≪ X D^(2θ−1+2η),                                  (11)

which also works at θ=1/2 because η>0. For b≠b', (6) and the ℓ¹ mass bound give

    ≪ X^(1/2+ε)D^(2+ε).                                 (12)

If `D=X^r` and `r<1/[2(3−2θ)]`, this is absorbed by `X^(1+ε)D^(2θ−1)`. Hence an assumed θ-strip gives

    Σ_d V(d/X)|M_d(X^r)|² ≪ X^(1+ε) X^{r(2θ−1)}.      (13)

For Θ_ζ<1, apply (13) for θ>Θ_ζ and let θ decrease to Θ_ζ; the condition on r holds for every θ≥1/2 when r<1/4. If Θ_ζ=1, the divisor bound gives the trivial upper exponent r. Together with the lower bound this proves (2), without assuming that the supremum is attained. Statement (3) is its Θ_ζ=1/2 specialization. □

The result gives a concrete full-zeta moment whose improvement to `X^{1+ε}` is exactly as strong as RH; it does not claim the moment estimate has been proved. The only excluded local factor is 2, whose Euler correction is nonzero in Re s>0. Primitive and imprimitive normalizations, the Gauss-sum estimates and the mod-4 sector must be independently checked before treating this note as settled.

## Classical quadratic large-sieve extension to every r<1/2

The restriction r<1/4 in the elementary covariance proof is not necessary if one imports [Heath-Brown's quadratic large sieve, Theorem 1](https://matwbn.icm.edu.pl/ksiazki/aa/aa72/aa7234.pdf). For complex coefficients λ_b supported on positive odd squarefree b≤B, it states

    Σ_{d≤Y, d odd squarefree} |Σ_{b≤B} λ_b (b/d)|²
       ≪_ε (YB)^ε (Y+B) Σ_b|λ_b|².                  (14)

Because d≡1 mod 4 and b is odd, quadratic reciprocity gives `(d/b)=(b/d)` with the original zero value when gcd(d,b)>1. The family in this note is a subset of the rows in (14), and V is bounded and compactly supported. The coefficients c_b in (10) are supported on odd squarefree b≪D. The reciprocal-zeta estimate (9) gives

    Σ_b |c_b|² ≪_{θ,η,W} D^(2θ−1+2η)
       Σ_b b^(−2θ−2η) ≪ D^(2θ−1+2η),                 (15)

including θ=1/2 because η>0. With D≤X, (14) gives

    Σ_d V(d/X)|M_d(D)|² ≪ X^(1+ε)D^(2θ−1+ε).       (16)

Thus the zero-free-to-moment implication holds for every fixed r<1 (indeed for D≤X), conditional on the classical quadratic large sieve and ζ's θ-strip. The average (7) detects a putative zero with a negligible error for every fixed r<1/2. Combining these, both (2) and (3) extend from `0<r<1/4` to **every fixed `0<r<1/2`**. At Θ_ζ=1/2 use any known nontrivial zero on the critical line and choose η small enough to dominate the mean error; at Θ_ζ=1 use the same trivial upper bound as above. No unproved cubic sieve or high-order character-family estimate is involved.

The large sieve controls only the zero-free-to-moment direction; it does not supply the reciprocal-zeta estimate (9) without the corresponding zero-free hypothesis. Therefore this extension does not prove RH. It is an exact conditional reformulation using the classical quadratic large sieve, and its possible prior appearance in the literature has not been exhaustively checked.

For the staged Dirichlet candidate `θ=4369351/5000000`, its asserted nonvanishing for the principal character away from its pole would give ζ's θ-strip, subject to the candidate's conventional-L-function interpretation and independent analytic-review qualifications; its imported constants passed `leanchecker --fresh` in the same Lean kernel. The classical quadratic-sieve converse would then give, for every fixed `0<r<1/2`,

    Σ_d V(d/X)|M_d(X^r;W)|² ≪_ε X^(1+0.7477404 r+ε).

The power 0.7477404 equals `2θ−1`; this is a source-dependent moment consequence, not an independent improvement of the zero-free boundary.

## A fixed-boundary criterion beyond r=1/2

Fix `1/2≤θ<1` and `0<r<1/(3−2θ)`. Then the same fixed W and V give the exact equivalence

    ζ(s)≠0 for Re s>θ
       ⇔  Σ_d V(d/X)|M_d(X^r)|² ≪_ε X^{1+r(2θ−1)+ε}
           for every ε>0.                                           (17)

For the forward direction, `r<1`, so the quadratic large sieve gives (16). For the reverse direction, a zero ρ with real part β>θ makes the normalized main term in (7) Ω of `D^{β−1/2−η}`. Its error is smaller if `r(3/2−β+η)<1/2`. The strict bound on r guarantees this after choosing η and the preliminary error loss small enough. Cauchy–Schwarz then contradicts the right side of (17), taking ε sufficiently small compared with `r(β−θ)`. At θ=1/2 the permitted range reduces to r<1/2, recovering the RH criterion above.

The exact limsup identity also extends to every `0<r<1/(3−2Θ_ζ)`: approach Θ_ζ by zero ordinates' real parts from below and apply the same error comparison, then use (16) for the upper bound. The cases Θ_ζ=1/2 and Θ_ζ=1 are treated as above. This is a parameter-dependent range because Θ_ζ is unknown. It characterizes zero-freeness through an independent-looking family moment but does not prove the moment estimate.
