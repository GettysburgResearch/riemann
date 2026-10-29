# The base-zeta obstruction survives centering and finite-mode deletion

**Status:** Proposed consequence of the standard row correlation and quadratic large sieve used in [the quadratic growth note](2026-10-29-riemann-quadratic-inverse-growth/README.md). The source estimates are imported there; this is not a new zero-free region, and independent review is requested. It identifies what a sharper coefficient-specific moment would need to prove.

Keep the same fixed smooth compact-annular W with Mellin transform nonzero on Re s>0, fixed nonnegative compact row weight V of positive mass, squarefree positive `d≡1 mod 4`, `D=X^r`, and `0<r<1/2`. Set

    A(Y)=Σ_(a odd) μ(a) W(a/Y),
    C_b(D)=μ(b)D^(−1/2) A(D/b),
    P_d(D)=Σ_(b odd squarefree) C_b(D)χ_d(b).

Thus P_d is the complete odd-prime-deleted inverse polynomial of ζ(s)L(s,χ_d). Only `b≪D` contribute. Let F be **any fixed finite set** of positive odd squarefree integers, and let `P^F_d` be the same sum omitting b∈F. In particular F={1} subtracts its principal b-mode. We claim that, under the already stated standard inputs,

    limsup_(X→∞) log[X^(−1)Σ_d V(d/X)|P^F_d(X^r)|²]/log X
      = r(2Θ_ζ−1).                                               (1)

This implies, for each fixed `1/2≤θ<1`, that the bound

    Σ_d V(d/X)|P^F_d(X^r)|² ≪_ε X^(1+r(2θ−1)+ε)  for every ε>0  (2)

is equivalent to `ζ(s)≠0` for Re s>θ, apart from its pole at 1. It suffices that (2) hold for all sufficiently large X. In particular, deleting finitely many characters cannot turn an inverse-moment proof of a better fixed strip into a routine consequence of the same large sieve. A deletion depending on D, or a different choice of family/weights, is outside this statement.

## Why deleting the mean does not remove the base zero

Choose an odd squarefree `b₀>1` outside F, once and for all, and define the normalized row expectation using V. For every squarefree b, the product χ_d(b₀)χ_d(b) equals a quadratic character for the squarefree symmetric-difference kernel together with a mask for common primes. If b=b₀, the product is `1_((d,b₀)=1)`; its row mean is

    h(b₀)=∏_(p|b₀) p/(p+1)>0

up to `O(X^(−1/2+ε))`. If b≠b₀, the symmetric-difference kernel is odd, squarefree and greater than one; the fixed modulo-4 projection cannot cancel its odd conductor. The row bound (5) of the companion gives

    E_X[χ_d(b₀)P^F_d(D)]
       = h(b₀) C_(b₀)(D) + O_(b₀,ε)(X^(−1/2+ε)D^(1+ε)).   (3)

Here the masks are retained, and the error follows from the trivial bound

    |C_b(D)| ≪ D^(1/2)/b,
    Σ_(b≪D)|C_b(D)| sqrt(b) ≪ D.

The fixed factor b₀, divisor losses and a harmless finite F are absorbed into the constants and ε. For example F={1}, b₀=3 gives `h(3)=3/4` and `C_3(D)=−D^(−1/2)A(D/3)`. The first unweighted row mean has lost its base term, but this bounded nonprincipal correlation recovers a scaled copy of that same term.

The Mellin transform of A(Y) is Ŵ(s)/ζ_odd(s), with ζ_odd(s)=(1−2^(−s))ζ(s). A zero `ρ=β+iγ` of ζ in Re s>0 makes a pole because Ŵ(ρ) and `1−2^(−ρ)` are nonzero. Thus for any η>0, `A(Y)=Ω(Y^(β−η))` along an unbounded sequence. Scaling by fixed b₀ preserves that Ω statement. For r<1/2 the error in (3) is smaller after choosing η,ε sufficiently small, including the endpoint β=1/2. Weighted Cauchy–Schwarz and `E_X|χ_d(b₀)|²≤1` then supply the lower growth exponent `r(2β−1−2η)`. Zeros with β arbitrarily close to Θ_ζ, and a critical-line zero when Θ_ζ=1/2, give the lower side of (1).

## Matching upper bound and coefficient-level equivalence

If ζ has no zeros for Re s>θ≥1/2, the ordinary reciprocal-zeta contour shift in the companion gives `A(Y)≪_η Y^(θ+η)`. Therefore

    Σ_(b odd squarefree, b∉F)|C_b(D)|²
       ≪_(θ,η) D^(2θ−1+2η) Σ_b b^(−2θ−2η)
       ≪ D^(2θ−1+2η).

Heath–Brown's quadratic large sieve bounds the numerator in (1) by `(XD)^ε(X+D)` times this coefficient square sum, after enlarging the rows to all positive odd squarefree d and using quadratic reciprocity with the original zero masks. As r<1/2, `D≪X`. Taking θ down to Θ_ζ proves the upper side of (1) when Θ_ζ<1; if Θ_ζ=1, use the trivial coefficient bound above to get `Σ|C_b|²≪D`, while zeros approach 1 to give the matching lower exponent.

The coefficient estimate itself has the same obstruction. With any fixed finite F and fixed `b₀∉F`, a bound `Σ_(b∉F)|C_b(D)|²≪_ε D^(2θ−1+ε)` bounds the single term C_(b₀), hence `A(Y)≪_ε Y^(θ+ε)` for all Y by the fixed dilation `D=b₀Y`. The Mellin transform then rules out every ζ zero to the right of θ. Conversely the zero-free half-plane gives the coefficient estimate by the displayed argument. Thus no coefficient-only square-sum improvement of this shape can avoid establishing the corresponding ζ zero-free region.

## Moving tail: a weaker but still explicit obstruction

Let `0<κ<1` and keep only modes `b>D^κ`. Given `1/2≤θ<1`, suppose a uniform all-ε bound of the stronger shape

    Σ_d V(d/X) |Σ_(b>D^κ) C_b(D)χ_d(b)|²
        ≪_ε X^(1+r[2θ(1−κ)−1]+ε),     D=X^r,                  (4)

holds for all large X. If

    0<r<1/[3+κ−2θ(1−κ)],                                        (5)

then the same imported row estimates imply ζ has no zeros Re s>θ. This is a **necessary** limitation on bounds of the specific scale (4), not a claim that every estimate for a growing tail implies a fixed strip. The exponent in (4) may be less than 1, which is allowed.

Indeed, suppose ζ(β+iγ)=0 with β>θ and choose an Ω-sequence for A(Y). By Bertrand's postulate choose a prime `b₀` between `2Y^(κ/(1−κ))` and `4Y^(κ/(1−κ))`; set `D=b₀Y` and `X=D^(1/r)`. Then `b₀>D^κ`, `b₀≍D^κ` and the signal in the b₀ correlation is at least `D^(β(1−κ)−1/2−η)` after adjusting η. The diagonal density is `b₀/(b₀+1)≥2/3`. The squarefree-kernel row bound and `Σ_b |C_b|sqrt(b)≪D` give the uniform moving-test error

    O_ε(X^(−1/2+ε) D^(1+κ/2+ε)).

By (5) this error is smaller than the signal for β>θ with small enough losses, while Cauchy and (4) bound the correlation by `D^(θ(1−κ)−1/2+ε)`. These inequalities contradict each other on the Ω-sequence. The argument uses the estimates' uniformity in the now-moving b₀; this is an explicit source condition and the extension awaits independent review.

## Nearby methods and source qualifications

[Gao–Zhao](https://doi.org/10.1016/j.jnt.2022.12.007) and [Toma](https://arxiv.org/abs/2405.18778) prove or conditionally study quadratic averages of Möbius coefficients attached to one reciprocal Dirichlet L-function, as summarized in [the prior-art note](2026-10-29-quadratic-inverse-prior-art.md). They do not estimate the full inverse coefficient C_b above; their isolated-factor moments cannot be substituted for a full-Dedekind inverse moment. General density theorems for varying quadratic characters control how many relative factors have zeros, but the base ζ factor is common to every row and a density estimate alone need not exclude one base zero.

As a source-qualified comparison that does not assume a fixed zero-free strip, the classical Korobov–Vinogradov method gives `M(x)≪x exp(−c(log x)^(3/5)(log log x)^(−1/5))` for some c>0; see [Nicol Leong's 2025 thesis abstract](https://doi.org/10.1017/S0004972725000188), which records an effective form. Restricting to odd a by dyadic decomposition, then applying partial summation to W, yields the same shape for A(Y), with a smaller constant. Split the b-square sum at `b=√D`: small b use the A(D/b) bound, and large b use the trivial bound. Hence

    Σ_b |C_b(D)|² ≪ D exp(−c' (log D)^(3/5)(log log D)^(−1/5)).

In the elementary diagonal/off-diagonal calculation of the companion, the row-correlation error is `O(X^(1/2+ε)D^(2+ε))`. For D=X^r and fixed r<1/2, this error is smaller than the displayed subpower-saving diagonal bound, after reducing c' and choosing ε sufficiently small. Therefore the complete, centered, or finitely deleted family moment has the unconditional upper bound

    Σ_d V(d/X)|P^F_d(X^r)|²
      ≪ X D exp(−c'' (log D)^(3/5)(log log D)^(−1/5)).

This is a subpower saving relative to the trivial XD scale, and gives no fixed zero-free boundary to the left of 1. It is asymptotically weaker than any fixed-strip input such as the candidate below. These deductions use the companion's stated elementary quadratic row estimate and have not been independently checked beyond the algebra shown.

The exact target `θ=0.8738702` is a locally built candidate dependent on the pinned tracker/OpenAI analytic development; it is not an independently established source-free premise. [Tracker PR 94](https://github.com/GTimG/QuasiRiemannTracker/pull/94) states the nearby bound 0.87387234 for all Dirichlet L-functions, likewise sharing those upstream dependencies. [Baiying Liu, Theorem 17.1](https://arxiv.org/html/2610.26835v1), claims the broader result `Re s>0.874886647039964…` for finite-order Hecke L-functions over every number field, including all Dedekind zeta functions, using substantial imported theta inputs; its numerical boundary is weaker than the tracker bound for quadratic Dedekind zetas (which factor into two Dirichlet L-functions), although its Hecke-family scope is much wider. These source claims and their dependency chains have not been independently verified here.
