# Independent check of the Vinogradov–Korobov sharpening of the zero-buffer tail

Reviewer: search_skeptic. Date: 2026-11-17. This extends `AF_zero_buffer_skeptic_round2.md`; it does not replace that note's explicit window hypotheses or independently establish the prime-side matrix moment.

**Scoped conclusion:** the classical Vinogradov–Korobov zero-free region, as stated in the inspected BGSTB and Guth–Maynard sources, improves the zero-buffer nuclear error to

||E₀||₁ ≪ √T exp[−c₁ L^(1/3)/(log L)^(1/3)] + O(T^−3/2),

where L=log(T/(2π)) and c₁>0 is fixed. Thus for every fixed A>0,

||E₀||₁=O_A(√T L^−A).

Consequently this truncation layer, even with zero buffer, preserves the prime-side O(N log L/L) relative rate if that full-matrix estimate and its window hypotheses have separately been established. There is no newly improved limiting zero-proportion constant or asserted literature priority here.

## Primary-source location of the external input

Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh, *An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta function*, arXiv2306.04799v1, 7 June 2023:

* §2, equations (2.9)–(2.11), p4, defines Θ(t) as the largest real part of any nontrivial zero up to absolute ordinate t, and a decreasing zero-free majorant Θ(t)≤1−η(t).
* §2, p6, first paragraph explicitly states the Korobov–Vinogradov choice η(t)=c/[(log t)^(2/3)(log log t)^(1/3)] for a positive constant c, and immediately uses its exponential saving.

Cached PDF: `sources/analytic/2306.04799.pdf`, SHA-256 `133071c4d85c875fe9b1a7d4001f22d7174270ab8f1fa8e6cee6178d20276ee9`.

An independent source statement is Guth–Maynard, arXiv2405.20552v2, §13.1, end of p50 before p51: N(σ,T)=0 when σ≥1−c(log T)^−2/3(log log T)^−1/3, referring to [M3, Corollary 11.4]. Cached PDF SHA-256 `915392cf7d0ecd108479814a9a1481e23423ef63415776471cec3975ae482cae`.

I inspected these source passages. The original Korobov/Vinogradov proofs and the cited monograph corollary were not read in this scoped check. The zero-free theorem is therefore an explicitly named external established input, rather than an original result independently proved here. Shrinking c if necessary resolves any strict/non-strict boundary convention.

## Uniform two-sided zero strip on the relevant heights

Set δ=η(3T). For all sufficiently large T and all zero ordinates t∈[T/2,3T], the zero-free input gives β≤1−δ. The functional equation sends β+it to 1−β+it, so it also gives β≥δ. Hence in the γ-coordinate z=(ρ−1/2)/i=t+i(1/2−β),

|Im z|≤1/2−δ.                         (1)

This is the exact hypothesis needed for the improvement; a one-sided real-part bound without functional-equation reflection would not suffice. The constant δ is uniform over this whole interval, by the decreasing zero-free majorant. Since δ→0, we may and do take T sufficiently large that 0<δ≤1/4.

## Local Parseval mass: the denominator is uniformly harmless

Use the notation and window assumptions of the zero-buffer note, in particular |φ|≤M and a≥a₀>0. For a zero satisfying (1), Parseval gives

Σ_{k∈Z}|φ̂(z−α_k)|²=L∫φ(u)² exp(2 Im(z)u)du.

Writing b=1−2δ∈[1/2,1),

∫φ(u)² exp(2 Im(z)u)du

≤2M²∫₀^{L/2}cosh(bu)du

=2M² sinh(bL/2)/b

≤2M² exp[(1/2−δ)L].

The explicit lower bound b≥1/2 is why the factor 1/b is uniformly bounded. There is no implicit division by the individual |Im z|; zeros on the critical line are included.

For the normalized retained mass q(z)=(aL²)^−1||v_z||²₂, this proves

q(z)≤C (√X/L) exp(−δL).               (2)

For an excluded zero satisfying (1) at distance D≥1 from I, the same two integrations by parts used in the zero-buffer note give

|φ̂(r+iη)|²≤C exp(L|η|)|r|^−4

≤C √X exp(−δL)|r|^−4.

The retained-grid comparison therefore gives

q(z)≤C (√X/L) exp(−δL) D^−3.         (3)

All constants remain independent of T because the window and cutoff are fixed. A varying family of windows requires uniform M,a₀ and transform-decay constants; this conclusion is not stated for an arbitrary such family.

## Near-height and far-height zero sums

First consider excluded zeros with t∈[T/2,3T]. The two D<1 endpoint strips have multiplicity O(L); (2) bounds their total q-mass by O(√X exp(−δL)). For D≥1, the global unit-count argument of the preceding note gives Σm_zD^−3=O(L). Equation (3) gives the same total bound. This is the only place where the improved zero-free strip is used.

For t outside [T/2,3T], no improved strip is assumed. Such zeros have D=dist(t,I)≥T/2. The unsharpened estimate is q(z)≤C(√X/L)D^−3. Partitioning the exterior into unit distance shells gives

Σ_{t outside[T/2,3T]}m_zD^−3

≤C Σ_{j≥T/2−1}j^−3 log(2T+j+4)

=O(L/T²).

For example this follows by the integral substitution j=Tu and the convergence of ∫_(1/3)^∞u^−3[1+log(1+u)]du. The estimate includes every negative ordinate and arbitrarily large positive ordinates. Thus their total q-mass is O(√X/T²)=O(T^−3/2).

Finally ||v_zv_zᵀ||₁=||v_z||²₂, so summing these positive bounds proves absolute nuclear convergence and

||E₀||₁≪√X exp(−δL)+√X/T².           (4)

There is no need for a density hypothesis, zero spacing, or RH. Only the classical unit-interval zero count and zero-free region enter.

## The saving and the transferred rate

Since log(3T)=L+O(1),

δL ≥ c₁ L^(1/3)/(log L)^(1/3)

for some c₁>0 and all sufficiently large T. For every fixed A>0,

[L^(1/3)/(log L)^(1/3)] / log L = L^(1/3)/(log L)^(4/3) →∞,

so the exponential in (4) is O_A(L^−A). The unspecified constants and starting height may depend on A and on the external zero-free constant; no effective numerical range is asserted.

If N∼TL/(2π), ||F||_HS=O(√N), and ||F||²_HS=κN+O(N log L/L) have separately been established, then

| ||G₀||²_HS−||F||²_HS |

≤2||F||_HS||E₀||₁+||E₀||₁²

=O_A(N L^(−A−1/2)+N L^(−2A−1)).

Taking, for example, A=1 makes this o(N/L). Thus the zero-buffer truncation does not worsen the stated full-matrix O(N log L/L) error. The trace error O(√T), already independently repaired, is also o(N/L). The exact finite block and rank–trace argument is unchanged from the preceding note.

## Scope and audit classification

No constant/window/gamma-coordinate or zero-count obstruction was found in this sharpening. The only extra analytic input beyond the zero-buffer note is the named classical zero-free theorem, used uniformly on a comparable-height interval and reflected by the functional equation. A de la Vallée Poussin strip of width c/log T alone would supply only a bounded exponential factor; the stronger Vinogradov–Korobov width is what gives arbitrarily large powers of log T here.

Classification: independently checked scoped argument with an explicitly cited external theorem; final archive adjudication pending. It repairs/simplifies the truncation layer and its rate. It does not establish the §5 full-matrix moment, validate every window estimate there, or certify the complete source theorem.
