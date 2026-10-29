# Riemann zeta as the growth exponent of a quadratic full-inverse moment

**Status:** A source-qualified analytic identity, not a new zero-free region. It imports the standard functional equation and zero theory of ζ, quadratic reciprocity, one-dimensional Poisson summation, the primitive quadratic Gauss-sum identity, and Heath-Brown's quadratic large sieve. The moment bound appearing in the resulting RH criterion is not proved here. Independent review of the precise uniform character-sum and contour inputs is requested.

Let V≥0 be a fixed smooth function supported in a compact interval of `(0,∞)`, with `∫V>0`. Let W≥0 be a fixed smooth compact-annular function whose Mellin transform

    Ŵ(s)=∫₀∞ W(x)x^(s−1)dx

has no zeros in `Re s>0`. One construction is recorded in [the cubic mean note](../2026-10-29-cubic-full-inverse-mean/README.md): take the smooth compactly supported density w of `Σ_{j≥1} U_j`, where `U_j` are independent uniform variables on `[-2^(−j),2^(−j)]`, and set W(x)=w(log x). Its transform is `∏_{j≥1} sinh(2^(−j)s)/(2^(−j)s)`, which has zeros only on the imaginary axis.

For odd positive squarefree integers d≡1 (mod 4), let χ_d be the primitive quadratic Dirichlet character of fundamental discriminant d. Delete the factor at 2 and define

    M_d(D)=D^(−1/2) Σ_{n odd} c_d(n)W(n/D),
    c_d(n)=Σ_{ab=n} μ(a)μ(b)χ_d(b).                            (2)

Thus `Σ_{n odd}c_d(n)n^(−s)=1/[ζ_odd(s)L_odd(s,χ_d)]` for Re s>1, where ζ_odd(s)=(1−2^(−s))ζ(s). The zero extension of χ_d at primes dividing d is retained. Define

    Θ_ζ=sup{Re ρ: ζ(ρ)=0, 0<Re ρ<1}.

For every fixed `0<r<1/2`, the following identity follows from the standard inputs stated below:

    limsup_{X→∞} log[X^(−1) Σ_{d>0, d squarefree, d≡1 (4)}
                    V(d/X)|M_d(X^r)|²]/log X
       = r(2Θ_ζ−1).                                              (3)

Interpret log 0 as −∞. Hardy's theorem supplies critical-line zeros, so Θ_ζ≥1/2. Consequently the moment bound `Σ_d V(d/X)|M_d(X^r)|²≪_ε X^(1+ε)` for every ε>0, with this one W and one r, is equivalent to RH. This is an equivalence, not a proof of the moment estimate or RH.

## Squarefree row-character estimates

The weighted number of rows is

    Σ_{d squarefree, d≡1 (4)} V(d/X)=C_V X+O_ε(X^(1/2+ε)),    (4)

where C_V>0. To see this, write the mod-4 indicator on odd d as `(1+χ₄(d))/2`. The principal generating series is `ζ_odd(s)/ζ_odd(2s)`, with a positive residue at s=1; the χ₄ term has `L(s,χ₄)/ζ_odd(2s)` and is holomorphic at 1. Mellin shifting to `Re s=1/2+ε` proves (4), with the standard fixed-character vertical-growth bounds.

For q>1 an odd squarefree integer and h any odd positive integer, quadratic reciprocity gives χ_d(q)=(d/q) for d≡1 mod4. With the mask `(d,h)=1`,

    Σ_{d squarefree, d≡1 (4), (d,h)=1} V(d/X) χ_d(q)
       ≪_{V,ε} X^(1/2+ε) q^(1/2+ε) h^ε.                     (5)

For a ratio of two squarefree q-indices, q in (5) is its nontrivial squarefree exponent-difference kernel; equal exponents supply additional coprimality masks absorbed into h. The estimate remains valid after the fixed mod-4 projection.

For completeness, expand squarefreeness by `μ²(d)=Σ_{k²|d}μ(k)` and write d=k²m. The original mask `(d,h)=1` is exactly `(k,h)=1` and `(m,h)=1`; retain the former, and only then expand the latter as `Σ_{e|(m,h)}μ(e)` and put m=e v. All variables are odd. The cubic-style zero issue is explicit here: `χ_q(k²)=1_((k,q)=1)`, and any e sharing a prime with q contributes zero through χ_q(e). The remaining congruence is `v≡e (mod 4)`, because odd k²≡1 (mod 4) and e is invertible mod4. Project it using the two mod-4 characters. The nonprincipal quadratic character in v is the primitive Jacobi character modulo q or its product with χ₄, of conductor q or 4q; the principal mod-4 component only imposes oddness and can be written as the difference between a complete sum and its even sub-sum. Common-prime masks therefore either vanish or are retained by the e-divisor sum; no primitive-conductor reduction silently discards them.

For a nonprincipal primitive character of conductor Q, one-dimensional Poisson summation and the Gauss sum give `Σ_m χ(m)V(m/Y)≪_V Q^(1/2) log(2Q)` uniformly in Y>0. Here Y=X/(k²e); the fixed subtraction for even v changes Y by a factor two. Because V is compactly supported away from zero, the inner sum is empty unless `k≪sqrt(X/e)`. Summing first over k and then over e|h costs at most `sqrt(X) Σ_{e|h} e^(−1/2)`, and `Σ_{e|h} e^(−1/2)≤τ(h)≪_ε h^ε`. This proves (5). The factor at 2 is handled by the fixed mod-4 projection, not by treating 2 as an unramified good prime.

## Full inverse mean and lower growth

Only b=1 is principal among odd squarefree b. Indeed `(d/b)` is a nonprincipal primitive quadratic character of d modulo every b>1, and multiplying by a fixed mod-4 character cannot cancel its odd ramification. Expanding (2), applying (4) to b=1 and (5) to b>1, and using `#{(a,b):ab≪D}≪D^(1+ε)` gives

    [Σ_d V(d/X)M_d(D)]/[Σ_d V(d/X)]
       = D^(−1/2) Σ_{a odd} μ(a)W(a/D)
           + O_ε(X^(−1/2+ε)D^(1+ε)).                          (6)

The Mellin transform of the unnormalized main term is `Ŵ(s)/ζ_odd(s)` on Re s>1. Every nontrivial ζ-zero ρ with Re ρ>0 gives a pole of its meromorphic continuation: Ŵ(ρ)≠0 and `1−2^(−ρ)≠0`. If β=Re ρ, the normalized main term is `Ω(D^(β−1/2−η))` along an unbounded sequence for each η>0. Otherwise its Mellin integral would analytically continue across the pole. At D=X^r with r<1/2, the error in (6) is smaller than that Ω-bound for sufficiently small η and ε. Weighted Cauchy–Schwarz and (4) then give a lower exponent arbitrarily close to `r(2β−1)`.

Taking β arbitrarily close to Θ_ζ proves the lower side of (3) when Θ_ζ>1/2. If Θ_ζ=1/2, Hardy's existence of a critical-line zero and the same nonvanishing Mellin transform give a normalized mean `Ω(D^(−η))`, hence limsup at least 0. This endpoint is separate from the cubic case: here the diagonal mean has no ζ(2s) pole at 1/2.

## Second-moment upper growth

Suppose ζ has no zeros in `Re s>θ`, where `1/2≤θ<1`. For any η>0, standard reciprocal-zeta bounds in a zero-free half-plane and Mellin inversion imply

    Σ_{a odd} μ(a)W(a/Y) ≪_{W,θ,η} Y^(θ+η)                 (7)

uniformly for Y>0. The finite omitted factor `1−2^(−s)` has no zero for Re s>0. Small Y gives an empty or bounded sum; on the line `Re s=θ+η` the rapidly decaying Ŵ absorbs polynomial vertical growth.

Group (2) by b and put

    C_b(D)=D^(−1/2) μ(b) Σ_{a odd}μ(a)W(ab/D),
    M_d(D)=Σ_{b odd squarefree} C_b(D)χ_d(b).

Only b≪D occur and (7) gives

    |C_b(D)|≪D^(θ−1/2+η)b^(−θ−η),
    Σ_b |C_b(D)|≪D^(1/2+ε),                                  (8)

where the second bound follows directly from the divisor count before cancellation in a. For the full r<1/2 range, use [Heath-Brown's quadratic large sieve](https://doi.org/10.4064/aa-72-3-235-275): for arbitrary coefficients on odd squarefree b≤B,

    Σ_{d≤T, d odd squarefree} |Σ_{b≤B, b odd squarefree} λ_b (b/d)|²
       ≪_ε (TB)^ε (T+B) Σ_b|λ_b|².                            (9)

The Jacobi symbol includes zero when gcd(d,b)>1. For d≡1 mod4, quadratic reciprocity gives `χ_d(b)=(d/b)=(b/d)`; the nonnegative weighted sector sum is bounded by the unrestricted d-sum up to a fixed factor. Applying (9) with T≪X, B≪D and λ_b=C_b(D), and using the square of the first bound in (8), gives

    Σ_d V(d/X)|M_d(D)|² ≪_ε (XD)^ε(X+D)D^(2θ−1+2η).        (10)

For D=X^r with r<1/2, X+D≪X. Letting θ↓Θ_ζ and the losses tend to zero gives the upper side of (3) when Θ_ζ<1. If Θ_ζ=1, use the elementary pointwise bound `|M_d(D)|≪D^(1/2+ε)` and O(X) rows, giving limsup ≤r. This equals the lower bound obtained from zeros with real parts arbitrarily close to 1.

There is also an elementary, weaker-range route that does not import (9). On expanding the weighted second moment, b=c are the only principal character ratios: for distinct odd squarefree b,c, the symmetric-difference kernel is a nontrivial odd squarefree q and shared prime factors contribute only zero masks. The diagonal terms are at most

    X Σ_b |C_b|² ≪ X D^(2θ−1+2η),

because `Σ_b b^(−2θ−2η)` converges. For b≠c, (5) gives an absolute row correlation `≪X^(1/2+ε)D^(1+ε)` since q≤bc≪D² and shared-factor masks cost D^ε. The total off-diagonal is therefore

    ≪ X^(1/2+ε)D^(1+ε) (Σ_b |C_b|)²
    ≪ X^(1/2+ε)D^(2+ε).                                      (11)

For D=X^r, the off-diagonal in (11) is smaller than `X D^(2θ−1)` whenever `r<1/[2(3−2θ)]`; this holds for all θ≥1/2 if r<1/4. Thus the elementary covariance argument proves (3) in that shorter range independently of Heath-Brown's sieve.

This proof applies to the full zeta product `ζ_odd(s)L_odd(s,χ_d)` for a quadratic extension with the prime 2 deleted, and to the stated fixed real quadratic discriminant subfamily. It does not use a relative-family zero-density estimate and does not establish the moment bound that would prove RH.

## A sharper fixed-boundary criterion

Fix `1/2≤θ<1` and `0<r<1/(3−2θ)`. The same single-test moment satisfies the exact equivalence

    ζ(s) has no zeros in Re s>θ
      ⇔  Σ_d V(d/X)|M_d(X^r)|²
             ≪_ε X^{1+r(2θ−1)+ε} for every ε>0.               (12)

For the forward implication, (10) applies because `r<1/(3−2θ)<1`, so D<X; take the reciprocal-zeta line at θ+η and absorb η into ε. For the reverse implication, a zero ρ=β+iγ with β>θ gives the mean Ω of size `D^(β−1/2−η)`. It dominates the error in (6) when

    r(3/2−β+η)<1/2,

which follows, after choosing η and the preliminary error loss small enough, from the strict inequality `r<1/(3−2θ)` and β>θ. Weighted Cauchy–Schwarz then forces moment growth larger than the right side of (12) for small ε. The endpoint θ=1/2 gives the previous r<1/2 RH criterion.

A corresponding parameter-dependent extension of (3) is valid for every fixed `0<r<1/(3−2Θ_ζ)`. If Θ_ζ>1/2, choose zeros β arbitrarily close to Θ_ζ so the above mean-error inequality holds and let β↑Θ_ζ; the large-sieve upper estimate holds for all r<1. If Θ_ζ=1/2 the permitted range is r<1/2 and the Hardy-zero argument applies. If Θ_ζ=1 the permitted range is r<1, and the divisor-bound upper estimate and zeros with β↑1 give equality. These are conditional identities about a moment, not new zero-free regions.

## An explicit diagonal asymptotic and deterministic energy

Define

    h(b)=∏_{p|b} p/(p+1),
    E(D)=Σ_{b odd squarefree} h(b)|C_b(D)|²,

where C_b(D) is defined above. Unconditionally, under the same standard smooth character-sum inputs, for X,D≥2,

    X^(−1) Σ_d V(d/X)|M_d(D)|²
       = C_V E(D)+O_ε(X^(−1/2+ε)D^(2+ε)).                  (13)

Here `C_V=(2/π²)∫₀∞V(t)dt`. To prove (13), the diagonal row average is

    Σ_{d sf, d≡1 (4), (d,b)=1} V(d/X)
      = C_V X h(b)+O_ε(X^(1/2+ε)b^ε).                       (14)

The principal mod-4 component has Dirichlet series `ζ_odd(s)/ζ_odd(2s) ∏_{p|b}(1+p^(−s))^(−1)`, whose residue gives h(b); the nonprincipal mod-4 component is regular at 1. Mellin shifting to 1/2+ε and bounding the finite factors gives the error. Multiplying (14) by `|C_b|²` and summing costs `≪X^(1/2+ε)D^(1+ε)` using the unconditional ℓ¹ bound in (8). Unequal b,c have the nonprincipal symmetric-difference quadratic character and the common-prime masks; (5) gives the total `≪X^(1/2+ε)D^(2+ε)` exactly as in (11). Dividing by X gives (13). In particular the error is o(1) for D=X^r and fixed r<1/4, after choosing losses small.

The deterministic energy itself records the zeta boundary:

    limsup_{D→∞} log E(D)/log D = 2Θ_ζ−1.                    (15)

For the upper bound use `h(b)≤1` and the coefficient bound from a zero-free line θ>Θ_ζ as above; if Θ_ζ=1 use the trivial divisor bound. For the lower bound retain the b=1 term, whose Mellin transform has a pole at every nontrivial ζ-zero because Ŵ is nonzero in Re s>0. Zeros with real parts arbitrarily close to Θ_ζ give the result; when Θ_ζ=1/2 a critical-line zero is supplied by Hardy's theorem. The energy identity needs no quadratic large sieve and makes no claim that ζ has a particular zero-free region.
