# A fixed prime slot detects the Riemann-zeta inverse boundary

**Status.** A proposed fixed-profile marked growth identity using the [quadratic full-inverse identity](../2026-10-29-riemann-quadratic-inverse-growth/README.md), elementary squarefree inversion, the classical Burgess r=2 character-sum bound and the prime number theorem. It does not prove the moment bound or a new zero-free region. The converse upper growth uses the classical quadratic large sieve as in the cited identity; the zero-boundary implication needs only its lower-mean direction. No priority claim is made.

Let d range over positive squarefree integers d≡1 mod 4, let V≥0 be fixed smooth compactly supported on `(0,∞)` with positive integral, and use the fixed nonnegative compact-annular W with Mellin transform nonzero in Re s>0 from the cited note. Define

    M_d(D)=D^(−1/2) ∑_{a,b odd} μ(a)μ(b)χ_d(b)W(ab/D),
    Q_d(P;t)=P^(−1/2) ∑_{p odd prime} χ_d(p)U(p/P)(p/P)^(it),

where U is a fixed nonzero smooth compact-annular profile and all quadratic symbols retain zero values. Let `D=Y^r`, `P=Y^z`, with fixed

    0<r<z,       r+z<4/11.                                    (1)

The restriction r<z makes all inverse indices b smaller than all slot primes for large Y, including the fixed profile support constants. For any t=t(Y), the marked energy satisfies

    ∑_d V(d/Y)|M_d(D)Q_d(P;t)|²
      = ∑_d V(d/Y)|M_d(D)|² [P^−1∑_p |U(p/P)|² 1_{p∤d}]
          + O_ε(Y^{1/2+ε} (PD)^{11/8}).                       (2)

The error constant is uniform in t, since its proof takes absolute values of the prime phases. The diagonal factor is uniformly ≍1/log P for every d in the row support: only O_z(1) of the ≫P/log P slot primes can divide d. Under (1) the error is `O(Y^{1−δ})` for some δ>0 after choosing ε small.

Let `Θ_ζ` be the supremum of real parts of the nontrivial ζ zeros. For every fixed r,z satisfying (1),

    limsup_{Y→∞} log[Y^−1 ∑_d V(d/Y)|M_d(Y^r)Q_d(Y^z;t(Y))|²]/log Y
       = r(2Θ_ζ−1),                                             (3)

uniformly for arbitrary choices of the single real frequency t(Y). In particular, a bound for **one prescribed frequency**,

    ∑_d V(d/Y)|M_d(Y^r)Q_d(Y^z;t(Y))|² ≪_ε Y^{1+κ+ε}
    for every ε>0,                                              (4)

is equivalent to `Θ_ζ≤1/2+κ/(2r)`; for κ=0 it is equivalent to RH. The direction from (4) to the zero boundary uses the lower-mean Ω argument only; the reverse direction uses the quadratic large-sieve upper estimate from the cited growth identity. The Burgess input here is the incomplete-character-sum bound, not merely a central-value subconvexity estimate. This criterion applies to this full ζ-product inverse and fixed annular prime profile, not automatically to a different relative inverse, detector fiber, or prime-slot normalization.

## Proof of the off-diagonal bound

Write

    M_d(D)=∑_{b odd, sf} C_b(D)χ_d(b),
    ∑_b |C_b(D)| ≪_ε D^(1/2+ε),

as in the cited quadratic note; only b≪D occur. For distinct slot primes p,q, the condition P≫D ensures p and q divide neither b₁ nor b₂. The character in the row sum is the nonprincipal quadratic symbol with squarefree kernel

    m=pq·(b₁△b₂) ≤ pq b₁b₂ ≪ P²D²,

where △ denotes symmetric difference of prime factors. Primes in `gcd(b₁,b₂)` contribute original coprimality masks. The mod-4 projection, finite masks and squarefree inversion yield uniformly

    ∑_{d sf, d≡1(4), (d,h)=1} V(d/Y) (d/m)
       ≪_ε Y^(1/2+ε) m^(3/16+ε) h^ε                 (5)

for odd squarefree m>1 and odd h. For completeness, write d=k²n and expand `(n,h)=1` by divisors e|h, retaining `(k,h)=1`. The nonprincipal inner character is a primitive Jacobi character of conductor m or its product with χ₄ of conductor 4m; oddness may be imposed by subtracting an even sub-sum. Burgess's r=2 estimate, extended to a fixed smooth profile by partial summation, is uniform for these primitive conductors and gives

    ∑_{k²e≪Y} (Y/(e k²))^(1/2)m^(3/16+ε)
       ≪ Y^(1/2)e^(−1/2)m^(3/16+ε) log(2Y),

and `∑_{e|h} e^(−1/2)≪h^ε`. Factors where k or e meet m vanish; retaining them cannot enlarge the bound. This proves (5), with small powers absorbing fixed factors and logarithms.

Applying (5) to m≤P²D² and summing over b₁,b₂ with the ℓ¹ bound gives, for each ordered p≠q, a row correlation `≪Y^(1/2+ε)P^(3/8)D^(11/8)`. There are O(P²) ordered pairs, and the prime-slot normalization is 1/P, yielding the error in (2). All original p,q,b zero masks are retained. Without Burgess, the elementary Pólya–Vinogradov/trivial-length minimum yields the weaker m^(1/4+ε) exponent and the sufficient range r+z<1/3.

For the lower side of (3), the first moment of M_d is governed by `Ŵ(s)/[(1−2^(−s))ζ(s)]`. Every nontrivial ζ zero β+iγ gives, along a sequence, unmarked energy at least `Y^{1+2r(β−1/2−η)}`; its averaging error is negligible because r<1/2. The diagonal in (2) carries this bound with only a logarithmic loss, and the O(Y^{1−δ}) off-diagonal is negligible. Let β approach Θ_ζ, treating Θ_ζ=1/2 using a critical-line zero. For the upper side, the cited quadratic large-sieve identity bounds the unmarked energy by `Y^{1+r(2Θ_ζ−1)+ε}`, including Θ_ζ=1 via its trivial endpoint. The diagonal and `O(Y^{1−δ})` error then give the matching limsup. □

**Independent review.** The squarefree inversion, Burgess r=2 and Pólya–Vinogradov estimates, nonprincipal kernel and masks for distinct slot primes, ℓ¹ coefficient bound, off-diagonal exponent, uniformity in the prescribed frequency, and limsup inference were checked independently. The growth identity still depends on the cited quadratic inverse result and its analytic inputs; it gives no unconditional marked-moment bound.

## Weyl-subconvexity extension

The fixed-frequency identity and equivalence also hold in the larger range

    0<r<z,       r+z<3/8,                                      (6)

subject to [Nelson's quadratic Hecke subconvexity theorem](https://arxiv.org/abs/1911.06310v3), Theorem 1.1 and its stated polynomial dependence on the Eisenstein representation's analytic conductor. Specifically, (2)'s error improves to

    O_ε(Y^(1/2+ε)(PD)^(4/3)),                                 (7)

uniformly in the slot frequency. The previously proved Burgess `4/11` range remains an independent alternative.

For the squarefree row covariance in (5), write its exact Dirichlet series after the mod-4 projection. Each term is a nonprincipal primitive quadratic Dirichlet L-function times a reciprocal `L(2s,ψ²)`, fixed 2-factors and the original finite deletion factors at primes of h. For `Re s>1/2`, the denominator reciprocal is uniformly bounded, while the deleted factors cost `h^ε`. Nelson's theorem applied to the unitary Eisenstein representation `|.|^(it)⊞|.|^(−it)` gives

    L(1/2+it,ψ) ≪_ε Q_ψ^(1/6+ε)(1+|t|)^A.

The conductor `Q_ψ` is `≪m`, including the fixed mod-4 twist; the theorem permits arbitrary quadratic conductor, so no cube-free qualification is needed. Interpolating to `Re s=1/2+η` and shifting the Mellin contour of V gives, with fixed profile constants,

    Σ_(d sf, d≡1(4), (d,h)=1) V(d/Y) (d/m)
       ≪_ε Y^(1/2+ε)m^(1/6+ε)h^ε.                         (8)

For distinct p,q, the already established `r<z` condition ensures the squarefree kernel m is nontrivial and `m≪(PD)²`. The ℓ¹ coefficient masses contribute D and the ordered prime pair count with slot normalization contributes P, giving (7). If r+z<3/8, (7) is `O(Y^(1−δ))` for some δ>0. The unchanged positive diagonal and the cited unmarked inverse limsup then prove (3)–(4) for the larger range (6). The input theorem is stronger than the elementary Burgess character-sum bound and is a separate imported analytic result; this remains an equivalence, not a proof of RH or of the marked moment.

**Independent review of the Weyl extension.** Families checked the mod-4 characters, their nonprincipality, fixed 2-factors and moving deletion masks, the Nelson/Mellin bound, the exponent `4/3` and the enlarged range. The result remains conditional on the cited analytic input and does not establish the marked moment or RH.

High_match independently checked the Weyl extension's quadratic characters, finite masks and `4/3` and `3/8` exponents.
