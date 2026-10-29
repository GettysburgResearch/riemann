# A conductor-ordered cubic detector from the rectangular sieve

**Status:** Proposed source-conditional zero-density derivation, not an individual zero-free theorem. It combines [De Faveri Proposition 8.1](https://arxiv.org/abs/2610.04045v1), its finite-ray reciprocity, and the fixed-field saturated-detector argument of [OpenAI Proposition 8.3](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf). The latter is stated in its source for the Eisenstein finite-order family, so the fixed-field and fixed-unitary-background transfer below is a substantive source-matching hypothesis. A proposed derivation and independent internal review of that transfer are [here](../2026-10-29-fixed-field-saturated-detector/README.md); they retain the fixed-field Hecke and differentiated-profile inputs explicitly. No priority claim is made. The source theorems are not independently proved here.

## Conditional statement

Fix K containing μ₃, fixed good-prime set S as in De Faveri, and a fixed unitary Hecke character ν whose finite conductor is supported on S. Let g vary over good cube-free ideals, and write χ_g for De Faveri's cubic family with its zero extensions. Suppose the fixed-field buffered saturated detector described below applies to the finite presentation set `νχ_g` and its conjugate, with the same uniformity in the original row masks, finite ray classes, fixed smooth-profile seminorms, and polynomial height factors. Then for each fixed 3/4<σ<1 and ε>0 there exists τ>0 such that

    Σ_{g good cube-free, N cond(νχ_g)≤X}
      N(σ,X^τ; νχ_g) ≪_{K,S,ν,σ,ε} X^{5/2−2σ+ε}.       (1)

Here N counts primitive L-zeros with multiplicity in `Re s≥σ`, `|Im s|≤X^τ`; a norm-character presentation's pole is not a zero. Constants and τ may depend on the fixed ν and σ, and no uniformity over an unbounded moving family of twists is claimed. The exponent is below one for σ>3/4, and as in the [conductor-density note](../2026-10-29-cubic-conductor-density/README.md), prime-ideal labels give ≫X/log X distinct characters, so (1) gives density-one zero-free rectangles. The family is ordered by conductor and the result is a density statement, not a zero-free region for each member.

## Inverse moment from De Faveri Proposition 8.1

Write g=a b² with a,b good squarefree and coprime. On dyads `Na≈A`, `Nb≈B`, set U=AB, order A≤B, and write A=U^γ with 0≤γ≤1/2. The primitive conductor of νχ_g lies between U and a fixed multiple of U: at every good p|ab, cubic ramification is nontrivial and ν is unramified, while fixed S-conductor exponents are uniformly bounded.

For a normalized inverse block of length D=U^r,

    M_g(D)=D^(−1/2) Σ_{q good} μ(q) ν(q)χ_g(q) W(Nq/D),

Proposition 8.1 yields, uniformly in the bounded real-length ranges,

    Σ_{a≈A,b≈B, μ²(ab)=1} |M_g(D)|²
       ≪ U^ε ( U + U^((1+γ)/3) D
                         + U^((2−γ)/3) D^(2/3) ).        (2)

The proof is direct. The squarefree Möbius support is exactly the q-support of Proposition 8.1 and the coefficient squared mass is O(1). Its source kernel is χ_q(ab²); source (2.5) changes this to χ_(ab²)(q) at a finite cost: partition the row parameter by its finite reciprocity ray class and absorb the resulting fixed class function of q into the coefficient vector. The original noncoprime zero masks agree. Positivity permits removing μ²(ab)=1 from the outer sum when applying the proposition. A fixed ν(q), a fixed profile, and a fixed norm-twist frequency remain row-independent coefficient factors. The separately reviewed [Sobolev reduction](../2026-10-29-cubic-detector-sobolev/README.md) controls the detector's rowwise real exponent and norm-twist height using only common differentiated coefficient vectors, with a factor O(1+T). It assumes the witness profile has the specific finite-dimensional source form described there; it does not cover arbitrary rowwise coefficients.

## Detector and count

Use the same nested zero-free bins as OpenAI §8. Each row with a zero of real part at least σ in the retained height interval has a bin left endpoint a≥σ−O(e), where e is an arbitrarily small fixed preliminary loss chosen before U tends to infinity. Put δ=2a−1. The `t=1` simultaneous saturated detector yields an inverse witness of a dyadic length U^r with

    1/2−O(ε_det)≤r≤1+O(1/log U),   |M_g(U^r)|²≥U^{δr−ε_det}.    (3)

For the fixed-field adaptation, choose the detector smoothing length Y*=U^B with a sufficiently large fixed B depending on the field and the fixed strip-growth estimate; do not assume the source’s Eisenstein choice B=20 works uniformly in K. The pre-saturation dyadic lengths are then bounded in [0,B+1+o(1)]; choose internal profile orders and τ after B. The lower length bound comes from the second, plain witness and its pointwise bound; it is not inferred from the inverse moment. Presentation, zero, twist frequency and smooth profile are grouped/handled using the fixed finite presentation set and the fixed-order Sobolev and common-height allowance. Exclude the possible pole-bearing presentation at g=1 before applying the detector, including a pure norm twist of the principal character; its ordinary zero count is separately negligible at the small heights used below.

Let

    E_γ(r)=max{1, r+(1+γ)/3, 2r/3+(2−γ)/3}.

From (2)–(3), Chebyshev bounds the row count for each fixed witness subdivision by U^{E_γ(r)−δr+O(ε_det)}. This exponent is convex in r, so its maximum on [1/2,1] is at an endpoint. At r=1/2 it is `1−δ/2`, while at r=1 it is `(4+γ)/3−δ`. Since γ≤1/2 and δ≤1, both are at most `3/2−δ`. Thus every retained dyadic box contributes at most

    U^{3/2−δ+ε} ≤ U^{5/2−2σ+O(e)+ε}

rows, up to the fixed polynomial height cost. This calculation uses the *actual* witness length; it does not assume r=1/2. The height cutoff is a sufficiently small U-power chosen after the detector losses and polynomial height orders. The individual Hecke zero count contributes at most a further small power of the height when passing from rows to zeros, which can be absorbed by shrinking the cutoff.

Finally partition the conductor range into dyadic A,B boxes, swapping names only in the bound of Proposition 8.1, not in the character presentation. There are O(log²X) boxes. For boxes U≥X^λ, take the global height X^τ below the local detector cutoff by choosing τ sufficiently small in terms of λ and the fixed detector order. The total of U^{5/2−2σ+ε} over these boxes is at most X^{5/2−2σ+ε}. Boxes U<X^λ contain O(X^{λ+ε}) labels and have at most O((X^τ+1)log(X(T+3)^d)) zeros per label; choose λ,τ>0 with λ+τ<5/2−2σ. Absorb dyadic logarithms and height powers into ε. This proves (1), provided the explicitly stated detector transfer and source bounds hold. □

## Scope and comparison

At σ=5/6, (1) gives exponent 5/6, compared with exponent 1 from the generic conductor reordering of De Faveri Corollary 1.5 and 9/10 from reordering [rStation paper 52 v5, Theorem 1](https://rstation.ai/problems/riemann_hypothesis/papers/52). At σ=17/20 it gives 4/5, versus 135/146 from generic reordering and 45/58 from that rStation theorem; the latter is stronger there but is restricted to the Eisenstein field and an unspecified sufficiently small power height. These comparisons import their respective recent source theorems; they are not priority or novelty claims.

There is also a stronger general-family comparator in part of this range. [Khale, O'Kuhn, Panidapu, Sun and Zhang, Lemma 3.3](https://arxiv.org/abs/2008.09677v3), in their fixed Galois-field setting, states a bound for **all** primitive finite-order ray characters of conductor norm at most R, summed also over bounded angular modes and zeros up to height M:

    ≪ (R² M^d)^{min(3/(2−σ), 2/σ)(1−σ)} (log RM)^B,
    d=[K:Q],  M>2.

At fixed or polylogarithmic height, this gives exponent `2 min(3/(2−σ),2/σ)(1−σ)` for our distinct cubic labels. In particular, at σ=4/5 its exponent is `1`, while (1) gives `9/10`. For `σ≥4/5` the comparator is `4(1−σ)/σ`; it improves on `5/2−2σ` precisely for `σ>(13−sqrt(41))/8=0.824609...`. At σ=17/20 the comparator is `12/17`, stronger than `4/5`. For `T=X^τ`, use the displayed `M^d` factor and a sufficiently small fixed τ before comparing; the crossover stated above is for fixed or polylogarithmic height. The 2021 source's proof cites standard Hecke large-sieve and zero-detection inputs and sketches their application; it has not been independently verified in this note.

The comparison applies to the cubic **label count**, not only after deduplication: at every good prime, the local cubic character records whether the prime occurs in `a`, in `b`, or in neither; hence distinct cube-free labels yield distinct primitive characters. Multiplication by one fixed unitary ν preserves distinctness. For a finite-order ν the comparator applies directly after enlarging the fixed bad set. For arbitrary fixed unitary ν, matching its angular type to one fixed mode of the 2021 source, separating a fixed finite-order character and norm twist, and bounding the resulting finite conductor by `O_{K,S,ν}(X)` require the exact character-basis identification in that source. Its Galois hypothesis is retained here. That source's introduction says the relevant later proof yields a prime-ideal result for non-Galois fields, but a separate verification of its density lemma in that generality is needed before asserting the comparison there.

Earlier cubic-specific density bounds need an ordering qualification. [Xia's 2006 thesis, Theorem 1.1](https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=osu1148497121&disposition=inline), and the [2007 journal article](https://doi.org/10.1016/j.jnt.2006.10.006), concern the Eisenstein family indexed by squarefree `c≡1 mod 9`, ordered by `Nc≤Q`; the thesis states `Q^{10(1−σ)+ε} T^{1+ε}` for `T≥2`. It is a smaller family than all cube-free presentations, with conductor comparable to index. [Blomer–Goldmakher–Louvel, Corollary 1.6 and footnote 3](https://arxiv.org/abs/1112.1650), explicitly question a step in Xia's published argument, noting that it would imply the Lindelöf hypothesis in the height aspect; the Xia assertion is therefore not taken as an independently validated comparator. Their own Corollary 1.6 treats **squarefree-index** Fisher–Friedberg characters over fixed fields containing μ₃, with index exponent `8(1−σ)/(7−6σ)` on `1/2<σ≤5/6` and an explicit height factor. As the conductor is comparable to the squarefree index, this gives exponent `8/11` at `σ=4/5` on that squarefree subfamily—stronger than (1) there, but it does not directly cover the general `a b²` family. De Faveri's later cube-free corollary changes the index family while remaining index-ordered; its comparison via conjugate reordering is recorded above.

**Remaining review:** Verify the fixed-field saturated-detector proof with the fixed unitary twist, in particular the primitive/nonprincipal exceptions, finite reciprocity and conductor masks, and uniform rowwise profiles. Confirm that the source Proposition 8.1 applies uniformly after those partitions and that no hidden κ/zero-free input is used. The result does not use a hypothetical marked moment and does not yield an individual zero-free half-plane.

## Limitation of the inverse-only choice of detector length

Within the displayed Prop. 8.1 majorant and the standard saturated-witness constraints, changing the detector parameter t from 1 to any value in [1,3/2] cannot improve the uniform inverse-only exponent. In the balanced row boxes A≈B≈U^(1/2), γ=1/2 and, for every `r≥1/2`, the sieve bound has exponent

    E_(1/2)(r)=1/2+r.

A saturated detector at length t only forces `t−1/2−O(ε_det)≤r≤t+o(1)`. For δ≤1, `E_(1/2)(r)−δr=1/2+(1−δ)r` is nondecreasing, and its worst allowed witness occurs at r=t, m=0. The resulting worst-case upper exponent is

    1/2+(1−δ)t,

which is minimized at t=1 (with equality for all t only at δ=1). The pair r=t,m=0 is compatible with the stated length constraints; this is a barrier for an optimization that uses only these witness inequalities and this inverse second-moment majorant, not a lower bound on actual counts. Improving it requires, for example, a stronger estimate exploiting the Möbius structure when the inverse length is about U, or an additional joint/plain moment and structural information excluding this worst witness.

## Fixed-field replay of the `t=1` detector

The following gives a proposed derivation of the remaining detector input from standard fixed-field Hecke analytic facts and the source's convolution argument. It is included to make the dependency reviewable, not to claim that the source theorem has already been independently established in this generality.

Fix a dyad U=AB and a finite family of presentations `νχ_g` and their conjugates. Their conductors and deleted radicals are O_{K,S,ν}(U), and only g=1 can induce a principal or pure norm-character presentation. Choose a detector loss e>0, a small height exponent τ>0 later, and T₁=U^τ. The finite-family nested-maxima construction of OpenAI Lemma 8.1 applies using ordinary Hecke continuation. It gives a bin `(i,a)` with a genuine zero ρ=σ_ρ+iγ when a>51/100, `a≤σ_ρ<a+e`, `|γ|≤3iT₁`, and a zero-free buffered rectangle for every presentation and conjugate. For a row with a zero at real part ≥σ and height below T₁, monotonicity gives a≥σ−e.

The fixed-type logarithmic-control proof in the [buffered detector note](../2026-10-29-fixed-type-buffered-detector.md) applies: it uses a fixed strip-growth polynomial, Euler convergence, Borel–Carathéodory and three circles. Together with the fixed-type functional equation and the O(U) deleted-radical bound, it gives the OpenAI Lemma 8.2 pointwise estimates, with δ=2a−1 and any prescribed small loss η,

    |M_r|² ≪ U^{δr+η},
    |S_m|² ≪ U^{δ min(m,1−m)+η},

for all fixed bounded lengths and all frequencies inside the single cumulative buffered-height allowance. For the reflected plain bound, use the conjugate presentation and include the polynomial gamma-height factor before choosing τ. Retained Mellin joins stay in the buffer; only the absolute-line tails are extended outside it.

For the saturation step set D=U and choose Y*=U^B with B a sufficiently large fixed constant depending on K, ν and a fixed global strip-growth bound. Let V_≤ be smooth, equal to one on [0,1] and zero on [2,∞), and define

    C_ψ(s)=Σ_l μ(l)ψ(l)V_≤(Nl/D)(Nl)^(−s),
    J=(2πi)^(−1) ∫_{(2)} Y*^z Γ(z)L_orig(ρ+z,ψ)C_ψ(ρ+z) dz.

Here ψ is the row presentation whose primitive inducing L-function vanishes at ρ. Deleted factors have no zeros in Re s>0, so L_orig(ρ,ψ)=0. Move the z-line to −1/4. The residue at z=0 vanishes, the nonprincipal L-function is entire, and fixed-field strip growth and the ideal count bound the new line by `U^{C−B/4}(1+T₁)^C` for a fixed C. Pick B first so this is o(1), then choose τ within the fixed height allowance. The Gamma factor controls the unbounded imaginary integration.

Expanding on the original line gives a smoothed convolution. For 1<Nn≤D its coefficient is `Σ_{l|n}μ(l)=0`, and the unit coefficient is 1+o(1). Thus the range Nl·Nk≫D has total magnitude ≫1. A terminal smooth cutoff at `Nl·Nk≤U^(B+1)` has negligible error, and fixed dyadic partitions give O((log U)²) possible length pairs D₁=U^r, D₂=U^m with r≤1+O(1/log U), r+m≥1−O(1/log U), and bounded r,m≤B+1+o(1). Logarithmic Fourier separation of the common product profile uses one common frequency for both polynomials; its rapidly decaying exterior tail is removed only after τ is fixed. For one retained pair and one common frequency, central normalization gives

    |M_r S_m|² ≫ U^{δ(r+m)−η}.

Comparing this with the two pointwise bounds forces m≤1/2+O(η), since δ≥2σ−1−O(e)>1/2 in the stated range. Dividing by the plain upper bound then gives `|M_r|²≥U^{δr−O(η)}` and r≥1/2−O(η). The zero's real part and the common height are the only remaining rowwise profile parameters after the dyadic labels are fixed. Sobolev in those parameters uses finitely many derivatives of y^(−σ_ρ−iγ) on a fixed annulus; the derivatives insert bounded log y powers, and the height interval costs a fixed polynomial in T₁. Applying the common-coefficient sieve to these differentiated profiles therefore supplies the uniformity required in (2). The cutoff exponent B, internal seminorm orders and arithmetic height degree are fixed before τ and the later external tail order.

A full line-by-line independent verification of this replay, including the original zero masks and the precise Hecke strip bound used on the shifted line, remains requested. It is the same finite-height issue as in the [fixed-type detector note](../2026-10-29-fixed-type-buffered-detector.md); no extrapolation of a global zero-free boundary is used.

For principal ν over the Eisenstein field, rStation paper 52 v5 also states a natural-row norm-ordered exponent `(8−7σ)/(3(2−σ))` for every 1/2<σ<1 at some small power height. The generic conjugate reordering gives conductor exponent `(8−7σ)/(2(2−σ))`, which is 1 at σ=4/5, versus 9/10 from (1). This compares only those displayed consequences; it does not exclude stronger direct conductor estimates elsewhere in the literature or establish a priority claim. The proof of (1) is conditional on its fixed-field detector replay and source sieve.

## Relative-zeta consequence for cyclic cubic extensions

Assume the conditional density theorem (1), and set ν=1. For every nontrivial family character χ_g, global class field theory attaches a cyclic cubic extension L_g/K. Its two nontrivial characters are χ_g and its conjugate, and Artin formalism gives the meromorphic identity

    ζ_(L_g)(s)/ζ_K(s) = L(s,χ_g) L(s,conjugate(χ_g)),

with the quotient understood by analytic continuation. Because the rectangle is symmetric in height, a zero of either factor there is equivalent to a zero of χ_g or its conjugate counted by (1). Therefore, for each fixed 3/4<σ<1 and ε>0, all but

    O_{K,S,σ,ε}(X^{5/2−2σ+ε})

fields in this family with cubic-character conductor norm at most X have a zero-free **relative quotient** in `Re(s)≥σ`, `|Im(s)|≤X^τ`, for a sufficiently small τ>0. The number of distinct fields in the family is ≫X/log X: good prime ideals p with Np≤X/C yield distinct conductor ideals and hence distinct cyclic cubic extensions. Thus the exceptional proportion tends to zero. The argument does not say that ζ_(L_g) itself is zero-free there: zeros of the fixed base ζ_K remain in its factorization.

Each cyclic cubic extension has only two nontrivial characters, which are inverses. For good cube-free g, its local character at a good ramified prime determines whether that prime has exponent one or two in g, so each primitive character has at most one such label. Hence the map from these labels to extensions is at most two-to-one; the upper bound on exceptional fields in fact already follows without that multiplicity observation. The conductor–discriminant formula gives

    |D_(L_g)| = |D_K|³ (N f_g)².

Equivalently, ordered by absolute discriminant at most D, the exceptional count is `O(D^{5/4−σ+ε})` and the zero-free quotient rectangle has height D^{τ/2}, after shrinking τ and adjusting ε and fixed constants. This is a density-one family statement conditional on the detector and rectangular sieve; it is not an individual uniform zero-free region or a claim about base-field zeta zeros. The class-field and discriminant identities are standard inputs, and no priority claim is made. An independent internal review checked the character-to-extension map, symmetric-height zero sets, prime-conductor lower bound, discriminant formula and height rescaling.
