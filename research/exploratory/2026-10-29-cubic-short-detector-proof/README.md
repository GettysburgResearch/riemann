# A fixed-field short detector for cubic conductor families

**Status and inputs.** This packet gives a source-qualified proof of the short saturated-witness lemma for the actual cubic family used in the [density calculation](../2026-10-29-short-cubic-conductor-detector/README.md), rather than assuming that lemma as an opaque input. It follows [OpenAI Lemmas 4.9–4.10 and 8.1–8.3](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf), with a fixed-field strip, a floor arbitrarily close to 1/2, and inverse cutoff t<1. The standard primitive Hecke analytic continuation, Euler product, functional equation and fixed-type strip bounds, and the cubic family and sieve assertions named below are imported. The proof does not establish those preprint assertions independently, nor an individual zero-free region. An adversarial review is requested before treating the source matching as closed.

## The precise witness statement

Fix K containing μ₃, the finite good-prime set S and cubic family of [de Faveri](https://arxiv.org/abs/2610.04045v1), and a fixed unitary Hecke character ν whose finite conductor is supported on S. Let g range over good cube-free ideals `g=A B²` with A,B squarefree and coprime, and suppose `N cond(νχ_g)≤X`. Use original zero-extended presentations: on good ideals χ_g vanishes whenever the ideal meets g, and on S-good ideals νχ_g is extended with the same mask. Let `1/2<σ₀<1`, `1/2<t≤3/2` and ε>0 be fixed.

For all sufficiently large X, each row with a primitive zero `Re ρ≥σ₀`, `|Im ρ|≤X^τ` has, except for the single possible norm-character row g=1, a finite bin `(i,a)` and simultaneous centrally normalized annular inverse and ordinary witnesses

    r≤t+O(1/log X),       r+m≥t−O(1/log X),
    0≤m≤1/2+ε,            r≥t−1/2−ε,
    |M_r|² ≫ X^{(2a−1)r−ε},     |S_m|² ≫ X^{(2a−1)m−ε},             (1)

with `a≥σ₀−e>1/2`, where e>0 and then τ>0 depend on the fixed data and ε. The same row presentation is used in both witnesses. Both use one zero and one common Fourier frequency. The profiles have fixed annular supports, bounded untwisted seminorms and only the real part of that zero and the common frequency as row-dependent real parameters. The bin, presentation and dyadic length choices lie in fixed or logarithmic-size sets. Replacing X by CX for fixed C changes only constants and negligible logarithmic endpoint terms.

A pure norm character, including the principal character, has a shifted Dedekind zeta function and is not entire. It is excluded from the contour proof. At every good p|g the cubic character is tamely ramified and ν is unramified, so `νχ_g` cannot be a pure norm character unless g=1. That one presentation has at most `O((X^τ+1)log(X+3))` zeros in the relevant bounded real strip; it is treated separately in a density count. The conjugate family is included in every buffer below.

## Source matching and global strip

The cubic source's conductor formula gives the primitive conductor of χ_g as a fixed-S-supported factor times `rad(g)`, with the S-local conductor exponents uniformly bounded. Hence `N rad(g)≤N cond(νχ_g)≤X`, while the primitive conductors of νχ_g and its conjugate and the radical of every deleted Euler product are `O_{K,S,ν}(X)`. The good ramification also proves the norm exception above. This paragraph uses the source conductor/zero-extension identity and the standard tame local character calculation; it is not an assertion for an arbitrary imprimitive presentation.

For the primitive inducing character ξ, write Q=Nf(ξ). All such characters have the fixed infinity type of ν, or its conjugate. The ordinary Hecke functional equation and the absolutely convergent Euler product imply a standard fixed-strip bound: for each fixed compact real interval J there are fixed C,A such that

    |L(s,ξ)| ≤ C [Q(3+|Im s|)^[K:Q]]^A,     Re s∈J.               (2)

The constants depend on K, J and the fixed infinity type, not on g. One obtains (2) by Euler convergence to the right of 1, the functional equation and Stirling on a line left of J, and Phragmén–Lindelöf on finitely many strips. Fixed archimedean shifts are retained in C,A. This is a standard fixed-type Hecke theorem, not a claim that the source's field-specific exponent U² persists over arbitrary K.

If `R` is the deleted radical and `D_R(s)=∏_(p|R)(1−ξ(p)Np^(−s))`, then for any fixed b>0 and ε₁>0,

    |D_R(s)|+|D_R(s)|^(−1) ≪_(b,ε₁,K) (NR)^ε₁,   Re s≥b,          (3)
    |D_R(s)| ≪_(ε₁,K) (NR)^[max(0,−Re s)+ε₁]       on fixed strips. (4)

For (3), split the finitely many small primes from primes for which `Np^(−b)≤ε₁ log(Np)/C`, and use log(1±z) bounds. For (4), factor out `Np^[max(0,−Re s)]` and absorb `2^ω(R)` into `(NR)^ε₁`. In positive real part D_R has no zero. This is OpenAI Lemma 4.10 with all masks retained.

## One buffered zero-free rectangle per row

Pick a fixed floor `1/2<σ_f<σ₀`, a small fixed e<σ₀−σ_f, and `T₁=X^τ`. For j=1,…,I, `I=ceil(1/e)+2`, take the maximum of σ_f and real parts of all zeros with real part at least σ_f and height at most `3jT₁`, over the row's primitive presentation and its conjugate. Euler convergence bounds these maxima by 1. One consecutive increment is at most e; rounding its lower maximum down to a grid of mesh e produces `(i,a)` with

    a≥σ₀−e>σ_f,    M_i<a+e,    M_(i+1)<a+2e.                       (5)

The maximum M_i is attained by a zero ρ=β+iγ of one presentation, `a≤β<a+e`, `|γ|≤3iT₁`. This is the finite nested-maxima argument of OpenAI Lemma 8.1, with the fixed floor σ_f in place of 51/100. No family-wide rightmost zero or unbounded height supremum is used.

For any `|v|≤(3i+2)T₁`, the disk around 2+iv of radius `R₂=2−a−2e` lies in `Re s>a+2e` and inside the next height interval for large X. It is zero-free for both primitive presentations. Let g(s)=log L(s,ξ) there, normalized by the absolutely convergent Euler log at the center. On the inner disk of radius 49/100, |g| is bounded absolutely. The strip bound (2) controls `Re g` by `O(log C_X)` on radius `R₃=2−a−3e`, where `C_X` is a fixed power of `X(3+T₁)`. Borel–Carathéodory gives `|g|≪_e log C_X` at radius `R₄=2−a−4e`. Hadamard three-circles between radii 49/100 and R₄ gives `|g|≪_e (log C_X)^κ` on radius `R₆=2−a−6e`, with one κ<1 uniform for `a∈[σ_f,1]` once e is fixed. For every prescribed η>0, (3) then yields

    |L_orig(s)|+|L_orig(s)|^(−1) ≪ X^η,
    Re s≥a+6e,   |Im s|≤(3i+2)T₁.                                  (6)

Farther right use absolute Euler convergence. The finite number of presentation choices is included in the same maximum. This is the fixed-type version of OpenAI Lemma 4.9; the exponent κ approaches 1 as e shrinks but e is fixed before X grows.

The primitive functional equation, the conjugate version of (6), and (4) give on `Re s=1−a−6e` in the same height range

    |L_orig(s)| ≪ X^{a−1/2+12e+η}(1+T₁)^C.                        (7)

Here one factor `X^{a−1/2+6e}` comes from the conductor, and at most `X^{6e+η}` comes from the deleted radical. The gamma quotient contributes the displayed fixed polynomial in T₁. For a fixed number of separated frequencies, assign all of them fractions of a single T₁/2 displacement budget; the budget is not renewed after a shift.

## Annular pointwise bounds with partial contour shifts

Write `δ=2a−1`. Let D=X^r and N=X^m in a fixed bounded range, and let h be any real frequency with `|h|≤(3i+1)T₁`. For a fixed smooth annular profile W define

    M_r = D^(−1/2) Σ_(q good) μ_K(q) ψ(q) W(Nq/D)(Nq/D)^(−β−ih),
    S_m = N^(−1/2) Σ_(q good) ψ(q) W(Nq/N)(Nq/N)^(−β−ih),

where ψ is the selected original presentation and β=Re ρ. Mellin inversion puts the norm twist in the L-argument. On the central frequency range, shift the inverse line to `Re(s+β)=a+6e` and use (6). For the plain sum, use either that line or `Re(s+β)=1−a−6e` and (7). The remaining frequency tails stay on absolute lines, while finite horizontal joins lie inside the buffer for the reciprocal. The Mellin transform of the untwisted fixed annular profile decays faster than any fixed power. After all fixed length and height orders are chosen, first choose τ and then the external decay order large enough that the omitted tails are negligible. Thus, for arbitrarily small prescribed η,

    |M_r|² ≪ X^{δr+η},
    |S_m|² ≪ X^{δ min(m,1−m)+η}.                                  (8)

The real zero part β≥a affects only the contour location; it does not replace a by β in these upper exponents. The estimate remains valid for bounded r,m beyond one; the reflected estimate then may have a negative exponent and the tail order is increased accordingly. This reproduces OpenAI Lemma 8.2 with the cumulative-height and fixed-field allowances explicit.

## Gamma convolution and saturation for short t

Set `D*=X^t`, choose a smooth V≤ equal to one on [0,1] and zero on [2,∞), and choose `Y*=X^B` for B large enough below. Put

    Cψ(s)=Σ_l μ_K(l)ψ(l)V≤(Nl/D*)(Nl)^(−s),
    J=(1/2πi)∫_(2) Y*^z Γ(z)L_orig(ρ+z,ψ)Cψ(ρ+z) dz.

The selected primitive function is entire and its original presentation vanishes at ρ by (3), so shifting to `Re z=−1/4` crosses only the zero residue at z=0. On that line `Re(ρ+z)>1/4`; (2)–(3), the ideal count and the finite inverse give a bound of the form

    |J| ≪ X^{C−B/4} (D*)^[5/4−β+o(1)](1+T₁)^C.

Fix B sufficiently large for the bounded t interval, then choose τ sufficiently small; J=o(1). This is the contour step in OpenAI Proposition 8.3, with no use of its printed lower restriction t≥1. The cutoff t>1/2 is imposed here only to obtain a positive inverse length from saturation.

On Re z=2 expand and invert Γ. For `1<N(lk)≤D*`, the inner Möbius coefficient is zero, while the unit contributes `e^(−1/Y*)=1+o(1)`. Insert the product cutoff `1−V≤(2N(lk)/D*)`, and a terminal smooth cutoff supported at `N(lk)≪X^(B+1)`; the latter costs o(1) by exponential decay and ideal counting. Dyadically partition l,k. The pairs have D≪D*, DN≫D*, DN≪X^(B+1), so r≤t+O(1/log X), r+m≥t−O(1/log X), with r,m bounded. There are O(log²X) pairs.

On a pair write `x=Nl/D`, `y=Nk/N`. Its common product profile has the form `W₁(x)V≤(Dx/D*) W₂(y) H(DN;xy)` with a compact annular H whose logarithmic derivatives are uniform. Fourier inversion in log(xy) gives one frequency v and an L¹ Fourier norm bounded uniformly. Its outside-`cT₁` tail is negligible by a sufficiently high **external** derivative order selected after τ. Some pair and `|v|≤cT₁` therefore give a product lower bound. The two central-normalized annular factors use the common height h=γ−v, and

    |M_r S_m|² ≫ X^{δ(r+m)−η}.                                    (9)

All logarithmic losses are absorbed in η. Compare (9) with (8): since `δ≥2σ_f−1>0`, this forces `m≤1/2+O_{σ_f}(η)`; divide (9) by each opposite upper bound to get the two individual lower bounds in (1). Shrinking the preliminary η yields the requested ε. This is the complete short-t modification of the source argument, subject to its standard analytic inputs.

## Quantitative common-coefficient Sobolev and the remaining arithmetic input

For each fixed bin, dyadic pair and finite reciprocity class, the two profiles in the preceding construction are of the form

    W₁(x)V≤(Dx/D*) x^(−β−ih),       W₂(y)y^(−β−ih),

where the dyadic ratio D/D* is common to the class, β lies in a fixed compact interval and `|h|≪_e T₁`. Cover the β interval by O(1) unit intervals and the h interval by O(1+T₁) unit intervals. Sobolev on each rectangle gives the sum over rows of rowwise suprema bounded by integrals of the four mixed derivatives with orders 0 or 1 in each parameter. Derivatives insert only bounded powers of log x or log y on the annulus. The profile V≤(Dx/D*) has uniform seminorms, including when its transition moves through the annulus. Thus every differentiated inverse coefficient vector is row-independent after fixing parameters and has squared norm O(1).

The arithmetic step is de Faveri Proposition 8.1 and its finite-ray reciprocity identity, applied to those **common** squarefree inverse coefficient vectors with the original noncoprime masks. This gives the displayed rectangular inverse moments. For ordinary S_m, write each good column uniquely as qv² with q squarefree. The factor ψ_g(v²) has modulus at most one and sits outside the q-sum. At fixed v and parameters the q-coefficient squared mass is O(1/(Nv)²), and the same bound holds for the Sobolev derivatives; the argument `(Nq)(Nv)²/N` stays in a fixed annulus. Minkowski and `Σ_{Nv≪√N}(Nv)^(−1)≪log(2N)` give the plain moment. Multiplying by at most O(1+T₁) for the parameter cover, and by the fixed polynomial height costs in (7), is absorbed by choosing τ small after the moment loss is fixed. A mere pointwise moment without derivatives would not justify these rowwise choices.

For cubic labels, the squarefree-column rectangular sieve and reciprocity are source results, not derived from the detector. For general n restricted labels, the [general-n sieve replay](../2026-10-29-conjugate-conductor-sieve/README.md) is an additional, separately unproved source extension. Subject to those source assertions and the explicitly listed standard Hecke facts, no extra marked moment or uniform all-height zero-free hypothesis enters this packet. The field-specific strip growth, finite S-conductor bound, primitive/original masks and the uniformity of all source versions remain exact review targets.

**Independent review:** [INDEPENDENT-REVIEW.md](INDEPENDENT-REVIEW.md) checks the six steps, explicit profile reduction and source hypotheses, conditional on the cited standard Hecke facts and de Faveri assertions. The [separate Sobolev proof](../2026-10-29-detector-profile-sobolev/README.md) supplies the finite-dimensional common-coefficient reduction rather than assuming an abstract rowwise-profile moment.
