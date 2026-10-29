# Uniform detector and fourth-moment interface for the direct n-free family

**Scope.** This supplies the analytic interface used in [the direct density calculation](README.md), rather than assuming an abstract saturated detector or rowwise-profile moment. It follows the gamma-convolution and buffering argument in [OpenAI, Lemmas 4.9–4.10 and 8.1–8.3](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf), but spells out the fixed-field and all-n-free quantifiers. The inputs are (i) the classical analytic continuation, Euler product, functional equation and uniform fixed-field vertical-strip estimates for finite-order Hecke characters, (ii) the FHL multiplicativity, good local conductor and zero-extension identities, and (iii) [de Faveri Theorem 1.1](https://arxiv.org/abs/2610.04045v1), with n-free indices on both sides. Those source assertions are not independently proved here. The argument uses only cutoff t>1, so no short-cutoff replay is needed. It remains a source-qualified proof, not an individual zero-free theorem.

## Setup and uniform classical estimates

Fix n≥4, K containing μ_n, the FHL good set S, and σ₀>1/2. Let u range over good n-free ideals Nu≤X, with original zero-extended finite-order FHL character ψ_u. Its primitive inducing character ξ_u has fixed infinity type and conductor norm `Q_u≪_{K,S,n} Nrad(u)≪X`; the radical of the finite Euler factors deleted in the original presentation is also `≪X`. These are the source local-conductor/mask inputs. Good primes dividing a nonunit n-free u have nonzero exponent modulo n and supply nontrivial tame local ramification, so u=1 is the only possible principal presentation. In a density sum it contributes at most `O((X^τ+1)log(X+3))` zeros in the fixed strip and height range, and is treated separately.

For any fixed compact real strip J, the classical Hecke functional equation, absolute Euler convergence and Phragmén–Lindelöf give, uniformly over the primitive characters and their conjugates,

    |L(s,ξ_u)| ≪_J [X(3+|Im s|)^[K:Q]]^A     (Re s∈J),      (1)

for a fixed A depending on K,J,n,S. The fixed infinity type is essential; no field-degree-two exponent is transplanted. If `D_u(s)` is the finite deleted Euler product, for every fixed c>0 and η>0,

    |D_u(s)|+|D_u(s)|^−1 ≪ X^η   (Re s≥c),
    |D_u(s)| ≪ X^[max(0,−Re s)+η]  on fixed strips.             (2)

These follow by bounding the product over its radical and absorbing divisor factors into X^η. In particular deleted factors have no zeros in Re s>0. All characters, original masks and their conjugates are included in these estimates.

## Rowwise zero buffer

Fix a floor `1/2<σ_f<σ₀` and a sufficiently small fixed e>0. Put T₁=X^τ. For j=1,…,I, where `I=ceil(1/e)+2`, let M_j be the maximum of σ_f and the real parts of zeros of either ξ_u or its conjugate with real part at least σ_f and height at most `3jT₁`. If the original row has a zero with Re≥σ₀ and height ≤T₁, every M_j is at least σ₀. Euler convergence bounds the M_j by 1, so one consecutive increase is ≤e. Round its lower maximum down to the e-grid: for some fixed finite bin index i and a,

    a≥σ₀−e>σ_f,    M_i<a+e,    M_(i+1)<a+2e.                  (3)

Select a zero ρ=β+iγ realizing M_i, from either the original or conjugate presentation. Then `a≤β<a+e`, `|γ|≤3iT₁`. The two presentations are retained in the buffer. Their choice will be partitioned into two cases in the moment step; it does not require replacing the label u by a conjugate label of a different norm.

For `|v|≤(3i+2)T₁`, the disk centered at 2+iv of radius `2−a−2e` is zero-free for both primitive presentations and lies inside the next height rectangle once X is large. Normalize the logarithm by its absolutely convergent Euler series at the center. It is bounded on a fixed inner disk, while (1) bounds its real part by `O(log C_X)` on the disk of radius `2−a−3e`, where C_X is a fixed power of `X(3+T₁)`. Borel–Carathéodory on the radius `2−a−4e`, followed by the three-circles theorem between the fixed inner disk and that radius, gives `|log L|≪_e(log C_X)^κ` on the radius `2−a−6e`, for one κ<1 uniform in the finitely many a bins. Choose e small enough that the fixed inner disk is strictly inside all these disks. Together with (2), for every prescribed η>0, after choosing τ sufficiently small,

    |L^S(s,ψ_u)|+|L^S(s,ψ_u)|^−1 ≪ X^η
       (Re s≥a+6e, |Im s|≤(3i+2)T₁),                          (4)

and likewise for the conjugate. For Re s≥2 the Euler product supplies the bound directly. Here L^S denotes the actual zero-extended presentation on S-good ideals. The primitive functional equation, (4) for the conjugate and (2) imply on `Re s=1−a−6e` in the same height range

    |L^S(s,ψ_u)| ≪ X^(a−1/2+12e+η)(1+T₁)^A.                   (5)

The two 6e contributions are respectively the conductor factor and a possible left-strip deleted-radical factor. All profile and Fourier shifts must share the same T₁/2 height budget; it is not renewed for each shift.

## Annular bounds and simultaneous saturation

Fix `1<t<3/2` and an arbitrarily small final loss λ>0. In a bounded dyadic range put D=X^r, N=X^m, and define

    M(D;β,h)=D^−1/2 Σ_l μ_K(l)ψ_u(l) W₁(Nl/D)(Nl/D)^(−β−ih),
    S(N;β,h)=N^−1/2 Σ_k ψ_u(k) W₂(Nk/N)(Nk/N)^(−β−ih),      (6)

with fixed smooth annular W_j, allowing a common cutoff `V_≤(Nl/X^t)` in M. The unit-scale endpoint is included by a fixed compact annular convention. Let δ_a=2a−1. Mellin inversion shifts the inverse block to `Re(s+β)=a+6e`, and the ordinary block either there or to `Re(s+β)=1−a−6e`. The central contour portions use (4)–(5); absolute-line tails have arbitrarily high fixed decay order. Since β∈[a,a+e], choosing e and τ after the bounded length range and before the external tail order gives uniformly

    |M|² ≪ X^(δ_a r+λ),
    |S|² ≪ X^[δ_a min(m,1−m)+λ].                               (7)

The second line remains valid when m>1; its exponent can be negative. These are pointwise estimates for the same selected original or conjugate row presentation.

To force witnesses, choose `D*=X^t`, a smooth `V_≤=1` on [0,1] and 0 on [2,∞), and `Y*=X^B`, with B sufficiently large depending only on the fixed field, t range and strip-growth order. Define the finite inverse

    C_u(s)=Σ_l μ_K(l)ψ_u(l)V_≤(Nl/D*)(Nl)^−s

and integrate `Γ(z)Y*^z L^S(ρ+z,ψ_u) C_u(ρ+z)` on Re z=2. Shift to Re z=−1/4. The selected nonprincipal L-function is entire, and at z=0 the Γ residue vanishes because ρ is its zero; there are no other crossed Γ poles. The fixed-strip bound and the finite polynomial C_u give the shifted integral `≪X^(C−B/4)(1+T₁)^A`, with fixed C,A. Choose B first and τ afterwards so this is o(1).

Expanding on Re z=2, the unit term is `1+o(1)`. For every good ideal a with `1<Na≤D*`, the convolution coefficient vanishes exactly: `Σ_(l|a) μ_K(l)=0`, and multiplicativity of ψ_u holds including its zeros. Insert a smooth product cutoff that vanishes below a fixed fraction of D* and is 1 above D*, then a terminal cutoff at `N(lk)≪X^(B+1)` with negligible exponential tail. An O(log²X) dyadic partition gives a pair D,N with

    r≤t+O(1/log X),     r+m≥t−O(1/log X),                      (8)

and a nonnegligible convolution block. The remaining two-variable weight is smooth on a fixed product annulus; Fourier inversion in `log((Nl/D)(Nk/N))` separates it into the two profiles in (6), with one common real frequency v and a uniformly bounded Fourier L¹ norm. All ratios D/D*, DN/D* and DN/Y* occur in uniformly smooth cutoffs; derivatives of the exponential are uniformly bounded on their effective ranges. Choose an external decay order after τ so the frequencies outside a fixed fraction of T₁ are negligible. One pair and one such v satisfy, with h=γ−v,

    |M S|² ≫ X^[δ_a(r+m)−λ].                                  (9)

Comparing (9) with both estimates (7) yields

    δ_a[m−min(m,1−m)] ≤ 3λ+o(1),
    m≤1/2+O_(σ_f)(λ),
    |M|² ≫ X^(δ_a r−2λ),    |S|² ≫ X^(δ_a m−2λ).             (10)

Use a smaller preliminary λ to achieve any requested final loss. This is simultaneous saturation: the inequalities concern the same row, zero, dyadic pair and common frequency.

## Common profiles and the fourth moment

There are finitely many bins and two character orientations, and O(log²X) dyadic length pairs. In one group, D,N, the cutoff profile and t are common; the only row-dependent real parameters in (6) are β in a fixed compact interval and h in a fixed multiple of `[-T₁,T₁]`. Apply the two-variable first-order Sobolev inequality to M, S, or **S²** on that rectangle and sum over rows. It bounds rowwise suprema by integrals of the four mixed derivatives with orders at most one in each parameter. The h-interval costs `O(1+T₁)` and the β interval has fixed length. Derivatives add only bounded annular log factors, apart from harmless common `log X` factors if a global phase is retained. Thus, after fixing β,h, each differentiated polynomial has one coefficient vector common to every row in the group.

For a squarefree-column inverse vector, de Faveri Theorem 1.1 directly gives, uniformly in that common vector,

    Σ_(u n-free, Nu≤X) |Σ_a c_a ψ_u(a)|²
       ≪ (XD)^η [X+D+X^(1−1/n)D^(2/n)
                               +X^(2/n)D^(1−1/n)] Σ_a |c_a|². (11)

For conjugate selected presentations, conjugate the whole coefficient vector and apply exactly the same operator norm. No conjugate-label relabeling or norm comparison is needed. Restriction to any detector bin or row subset only decreases the nonnegative moment. Fixed finite reciprocity sectors can be partitioned before applying the source.

For an ordinary block, and for S² after convolving its two common coefficient vectors, write each good column uniquely as `a=a₁v²` with a₁ squarefree. For each fixed v, `ψ_u(v²)` is a row-dependent contraction of modulus ≤1 and sits **outside** the common a₁-sum; this remains true when a₁ and v share primes and preserves every zero mask. A normalized block of column length Q has, after this split, squared a₁-coefficient mass `≪X^η/(Nv)²`, including its fixed β,h derivatives; divisor bounds cover the convolution. Minkowski in the row ℓ² norm followed by `Σ_(Nv≪√Q)1/Nv≪log X` gives (11) with D=Q for the second or fourth moment, up to X^η. Taking Q=N² for S² proves the required ordinary fourth moment. All profile/parameter differentiation happens before fixing v or is justified by the same finite product rule.

Choose all bin, contour and moment losses first, then a common τ>0 small relative to the finitely many fixed height exponents, and finally the Fourier/Schwartz decay orders. The factor O(T₁), all fixed polynomial `(1+T₁)^A` factors, and the individual zero-count factor `O((X^τ+1)log(X+3))` are then absorbed in X^ε. A witness counted at a bin a≥σ₀−e can be estimated using δ₀=2σ₀−1, with only O(e) loss, since r,m are bounded. This proves the detector and common-profile input used in the direct calculation, subject to (1)–(2), the FHL conductor/mask facts and printed source sieve (11).

## Remaining source qualifications

The proof does not independently verify de Faveri's large-sieve theorem or its FHL construction. In particular, its unit/ray-class normalizations must be matched to the original good-ideal family with their zeros; the theorem is used in precisely its n-free-row/n-free-column scope. The ordinary Hecke analytic continuation, functional equation, fixed-strip growth, the standard finite-ideal counting/divisor estimates, and the elementary complex-analysis tools invoked above are classical inputs. The finite-family buffering and gamma-convolution arguments are given here, but a formal or line-by-line independent check of the Mellin/Fourier contour estimates and their uniform constants is still appropriate. No separate moving-b twist, arbitrary rowwise coefficient vector, all-height zero-free input, or short-t detector is assumed.

**Independent review.** Families checked the fixed-field buffer, Gamma convolution, uniform dyadic/Fourier cutoffs, selected conjugate orientation, and Sobolev applied to S² with the fixed-v original masks. No concrete gap was found under the stated Hecke, FHL and printed-sieve inputs; this review does not independently establish those external inputs.
