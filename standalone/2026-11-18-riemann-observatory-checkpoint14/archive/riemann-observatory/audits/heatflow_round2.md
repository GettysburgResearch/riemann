# Original heat-flow foundations, exact conventions, and positive-kernel controls

Campaign date/cutoff:2026-11-17. Original Newman1976 was read in full (seven printed pages); selected theorem/proof passages of deBruijn1950 were read. No classical RH gain or literature novelty is claimed. Independent review of the new control constructions is pending unless separately recorded.

## 1. Primary identities and a bibliographic correction

- N.G.deBruijn, *The roots of trigonometric integrals*, **Duke Mathematical Journal17(3)(1950),197–226**, DOI10.1215/S0012-7094-50-01720-0. The original is30pages;197–226 is verified in the primary scan and Newman's reference. The alternative297–314 is incorrect for this work. The received date16July1948 is not its publication year; a repository's1948 field must not replace the1950 journal identity.
- CharlesM.Newman, *Fourier transforms with only real zeros*, **Proceedings of the AMS61(2)(December1976),245–251**, DOI10.1090/S0002-9939-1976-0434982-5; JSTOR alternate DOI10.2307/2041319. Its printed copyright says1977, but the issue date and primary publication metadata are1976. Received5January1976, revised3May1976.

Private original scans, exact URLs and hashes are in `sources/heatflow_round2/source_manifest.jsonl`. No source PDFs or extracted full text are intended for default distribution.

## 2. What deBruijn's strip theorem assumes

Theorem10, printed p204, assumes a real-variable **function** f, integrable on R, with

    f(u)=conjugate(f(−u)),
    f(u)=O(exp(−|u|^β)) as |u|→∞, for some β>2.

Its Fourier integral H(z)=∫R f(u)exp(izu)du is real entire of order<2. The symmetry is Hermitian symmetry: f need not be real and even separately. Positivity and C∞ smoothness are **not** hypotheses of Theorem10. Identically zero transforms are excluded when discussing a finite containing zero strip.

Theorem13, p205, assumes in addition that **all** zeros of H lie in |Imz|≤Δ. For λ>0, the transform with multiplier exp(λ²u²/2) has all zeros in

    |Imz|≤sqrt(max(Δ²−λ²,0)).

With the direct heat parameter τ=λ²/2, this is sqrt(max(Δ²−2τ,0)). In particular real-rootedness is preserved for increasingτ, and initial finite stripΔ gives real-rootedness forτ≥Δ²/2.

The inspected proof replaces exp(λ²u²/2) by (cosh(λu/N))^(N²), applies Theorem12 repeatedly, and passes to a locally uniform Fourier-integral limit. The bound cosh y≤exp(y²/2), together with super-Gaussian decay and exp(|Imz||u|) on bounded z sets, supplies an integrable domination. Theorem7 is the required zero-exclusion/Hurwitz limit passage.

The **all-zeros** quantifier cannot be silently changed to “all but finitely many.” Immediately before Theorem13, deBruijn distinguishes two strong-universal-factor properties and explicitly says the corresponding asymptotic property for the Gaussian multiplier is not established there. This is a statement about the1950 source's scope, not a claim about the current status of that question.

Newman1976 Theorem1,p246 restates the strip result for real even integrable f with the same super-Gaussian exponent condition and the multiplier exp(δu²), δ>0. His stated strip is sqrt(max(Δ²−2δ,0)). Do not add positivity to this theorem merely because his Riemann kernel is positive.

## 3. Newman's classification and why a finite Riemann threshold needs it

Let ρ be an even nonnegative finite measure and

    Z_b(w)=∫R exp(wu−bu²)dρ(u),       b>0.

The Gaussian damping makes this entire in w without an assumption of all exponential moments onρ. Newman Theorem2, pp246–247, classifies the nonzeroρ for which **every b>0** gives only imaginary zeros. The possibilities are:

1. ρ=K(δ_t0+δ_(−t0)), K>0,t0≥0 (so a single atom at0 is included).
2. An absolutely continuous measure with density

       K u^(2m) exp(−αu⁴−βu²)
          ∏j [(1+u²/aj²) exp(−u²/aj²)],

   K>0,m∈{0,1,…},aj>0,Σjaj^(−4)<∞, and either α>0 with β real, or α=0 with β+Σjaj^(−2)>0. The last condition is automatically interpreted as satisfied if that sum is infinite. Empty, finite and infinite products are permitted.

The original page247 image was checked because OCR loses the canonical-product exponential, t0≥0, the fourth-power summability, and inequality endpoints.

Proof architecture, reconstructed from the full source: Gaussian convolutionρ_b→ρ weakly produces densities expressible through Z_(b/2)(bu), hence canonical products with only imaginary zeros. If the source's shape parameters Ab,Bb remain bounded, normal-family estimates give a canonical density of the displayed form. If they diverge, monotonicity of the logarithmic derivative forces support to concentrate at a symmetric pair, including0. Lemmas1–4, pp248–251, implement this dichotomy. Sufficiency follows by polynomial/canonical-product approximation and the real-zero-preserving polynomial operations cited by Newman. Those antecedent polynomial theorems were not independently audited here.

### The original Riemann parameter runs in the opposite direction

Newman defines, p245 equations1.1–1.4,

    Ξ_b(x)=∫R exp(ixu−bu²) F(u)du,
    Ξ_0(x)=ξ(1/2+ix).

His positive even Riemann kernel is

    F(u)=Σn≥1 [4π²n⁴ exp(9u/2)−6πn² exp(5u/2)]
                 exp(−πn² exp(2u)),

and satisfies the even super-exponential bound in his1.3. Increasingb is forward Fourier heat: ∂bΞ_b=∂x²Ξ_b. In this convention real-rootedness persists for **decreasing b**.

Theorem3,p247 states exactly: there is a finite real b0 with

    −1/8≤b0<∞,
    Ξ_b has only real zeros iff b≤b0.

The endpoint is included, and multiple real zeros are allowed. This is not the statement that b0 is negative, nor that every super-Gaussian kernel has a finite threshold.

Here is the source's substantive lower-finiteness argument. Every canonical density in Theorem2 has a lower bound of quartic type, obtained from

    (1+x²) exp(−x²) ≥ exp(−x⁴/2).

The inequality follows by differentiating log(1+y)−y+y²/2 fory≥0. Its derivative is y²/(1+y)≥0. The finite sumΣaj^(−4) makes the resulting quartic coefficient finite. The Riemann kernel decays faster than every quartic lower bound, so it is not in the classified class. Thus some dampingb produces nonreal zeros; the downward real-rooted set is not allR. The strip theorem supplies a nonempty part (b≤−1/8). Local uniform convergence inb plus Hurwitz, with Ξ_b(0)>0, closes the set at its finite endpoint.

### Exact conversion to the inspected Rodgers–Tao convention

Rodgers–Tao, PAPER-S004, equations1–4,p2 of the inspectedv5, use

    H_t(z)=∫0∞ exp(tu²) Φ(u) cos(zu)du,
    H_0(z)=ξ(1/2+iz/2)/8.

Comparing their explicitΦ with Newman's1.2 gives **F(2u)=2Φ(u)**. Therefore direct substitution yields

    Ξ_b(x)=8 H_(−4b)(2x),
    Λ_standard=−4b0.

In particular b0≥−1/8 becomes Λ_standard≤1/2. RH is b0≥0, equivalently Λ_standard≤0. Newman's complementary conjecture b0≤0 becomes Λ_standard≥0. Missing either the Fourier-variable dilation2 or the sign would corrupt the constants. This conversion uses the actual two displayed primary kernels, not recollection of a secondary convention.

## 4. Finite, infinite and undefined threshold cases

The existence of a finite cutoff is not automatic for arbitrary positive measures.

- For the Riemann kernel, the preceding source argument gives a finite threshold.
- The positive smooth super-Gaussian kernel exp(−u⁴) has real Fourier zeros after multiplication by exp(τu²) for **every realτ** (Pólya's quartic family; also compatible with Newman's canonical class). Its upward heat threshold is−∞.
- A symmetric two-atom measure also has only imaginary Laplace zeros for every heat parameter: its transform is a scalar multiple of cosh(t0w). This is a measure example, not a function satisfying deBruijnTheorem10.
- A merely finite measure can fail to admit positive heat tilts at all: for a Gaussian density, exp(τu²) becomes nonintegrable beyond its Gaussian exponent. One cannot define an all-real-parameter heat family from finiteness alone.

Thus one must separately verify existence of the family, nonempty real-rooted set, upward closure, closure at the endpoint, and failure of real-rootedness at some parameter. Our controls below verify those facts explicitly.

## 5. Exact three-atom positive-kernel model

For a≥0 let

    ρ_a=cosh(a)δ0+(δ1+δ_(−1))/2,
    F_a(w)=∫exp(wu)dρ_a(u)=cosh w+cosh a.

This is an even nonnegative finite measure, so it lies in the **ambient measure class** of NewmanTheorem2. It is not a Lebesgue-integrable kernel function and is not directly an input to deBruijnTheorem13.

The forward Laplace heat flow is exactly

    F_(a,τ)(w)=exp(τ∂w²)F_a(w)=exp(τ)cosh w+cosh a.

All zeros are imaginary iff

    τ≥τ_a:=log cosh a.

Indeed the equation is cosh w=−r with r=exp(−τ)cosh a. If r>1, its zeros are ±arcosh(r)+(2m+1)iπ, so they are off the imaginary axis. If0<r<1, all solutions are imaginary; at r=1 the zeros(2m+1)iπ are double. Thusτ_a>0 fora>0. In original damping variablesb=−τ this gives the cutoff b_a=−log cosh a.

In the Fourier variable w=ix, the initial zeros have |Imx|=a. The exact strip half-width is

    Δ_a(τ)=arcosh(exp(−τ)cosh a)       ifτ<τ_a,
    Δ_a(τ)=0                         ifτ≥τ_a.

The universal expression sqrt(max(a²−2τ,0)) is consistent with this exact model, but its applicability to atoms is not inferred from the function theorem. Independently, Δ_a′=−cothΔ_a while Δ_a>0, so d/dτ[a²−2τ−Δ_a(τ)²]=2(Δ_a cothΔ_a−1)≥0. Also logcosh a≤a²/2. These elementary calculations explain the constant comparison without changing source hypotheses.

## 6. A rigorous positive smooth approximation that does fit the source

Let hε(u)=cε exp(−(u/ε)⁴), normalized to have mass1, ε>0. This is even, strictly positive, C∞, and super-Gaussian. Its Laplace transform Mε(w) has only imaginary zeros: deBruijnTheorem1,p198 applies to the potentialf(u)=(u/ε)⁴, whose derivative4u³/ε⁴ is a polynomial with only imaginary-axis zeros. Its transform has order<2 by Theorem10.

Define the ordinary density

    f_(a,ε)=ρ_a*hε.

Explicitly it is cε[cosh(a)exp(−(u/ε)⁴)+(1/2)exp(−((u−1)/ε)⁴)+(1/2)exp(−((u+1)/ε)⁴)]. It is strictly positive, even, C∞ and integrable. Translation of the quartic tails still gives O(exp(−|u|³)) for large|u|, so it satisfies Theorem10 with an exponent>2. Its Laplace transform at heat0 is exactly

    F_(a,ε,0)(w)=F_a(w)Mε(w).

All initial zeros therefore lie in |Rew|≤a; the off-axis zeros±a+iπ remain, and the other zeros are imaginary. In particular the initial strip is exactly a.

The heat transforms

    F_(a,ε,τ)(w)=∫exp(τu²+wu) f_(a,ε)(u)du

exist for every realτ and are locally uniform inτ,w. The source strip theorem gives only imaginary zeros forτ≥a²/2. Atτ=0 there are off-axis zeros, and one persists forτ in a neighborhood of0 by Rouché on a small off-axis circle. Upward closure and Hurwitz endpoint closure apply. Consequently this **source-class smooth density** has a finite threshold

    0<Λ_(a,ε)≤a²/2       (a>0).

No claim that its exact threshold equals logcosh a is made.

Asε→0 the heat transforms converge locally uniformly to the atomic transform at every fixed realτ. To justify this, write each translated convolution integral with v=εy; forτ,w in compact sets, exp(τ(c+εy)²+w(c+εy)) exp(−y⁴) has an integrable bound independent ofε≤1. Dominated convergence is uniform on those compact parameter sets. Every simple off-axis atomic zero atτ<τ_a persists for sufficiently smallε. Hence the rigorous implication is

    liminf_(ε→0) Λ_(a,ε) ≥ logcosh a.

Local uniform convergence alone does **not** prove convergence of the global thresholds; that stronger assertion is left open here.

### Sharpness of the universal constant even for positive smooth kernels

For any c>2 choosea>0 so small that logcosh a>a²/c, using logcosh a/a²→1/2. Atτ=a²/c the atomic transform has a simple off-axis zero. The locally uniform approximation makes that zero persist for some sufficiently smallε. The smooth initial transform still has its zeros in the exact strip|Imx|≤a.

Thus no universal improvement replacing2 by c>2 in sqrt(max(a²−2τ,0)) can hold even in this strictly positive, even, C∞ super-Gaussian subclass. This is a source-grounded sharpness reconstruction with novelty unassessed.

## 7. Why finite Li-type positivity still does not certify a nonpositive threshold

Use the auxiliary functional-equation family

    X_a(s)=F_a(s−1/2),
    λ_n[X]=(1/(n−1)!) (d^n/ds^n)[s^(n−1)logX(s)] at s=1.

The logarithm is analytic near1 because X_a is positive on the real axis. These are Li-type coefficients of this explicit model, not coefficients of the Riemann xi function.

At a=0, X_0(s)=2cosh²((s−1/2)/2). Its zeros are the double critical-line pairs ρ=1/2±i(2m+1)π. A paired zero factor contributes

    2−u^n−u^(−n)=2−2cos(nθ)≥0,
    u=(ρ−1)/ρ,       |u|=1.

The paired series converges, since its terms are O(n²/|ρ|²). For every fixedn some sufficiently high pair has0<|nθ|<2π, so λ_n[X_0]>0 strictly. Each λ_n[X_a] depends continuously ona. Therefore for each finiteN there existsa_N>0 such that

    0<a<min(a_N,1/2) ⇒ λ_1[X_a],…,λ_N[X_a]>0,

while X_a has zeros with real parts1/2±a and heat thresholdlogcosh a>0.

The smooth approximation preserves this control. Since Mε is even entire of order<2 with only imaginary zeros and Mε(0)>0, its Hadamard product pairs as a constant times∏j(1+w²/yj²), withΣyj^(−2)<∞ and no nonconstant exponential factor. Shifting by1/2 gives critical-line paired factors, hence nonnegative Li-type coefficients. Logarithmic additivity gives

    λ_n[F_a(s−1/2)Mε(s−1/2)]
       =λ_n[X_a]+λ_n[Mε(s−1/2)] ≥λ_n[X_a].

Thus the same finite positive prefix persists in a strictly positive smooth super-Gaussian kernel with positive finite heat threshold. This does not refute an infinite positivity criterion or establish anything about classicalξ. It identifies the missing global/all-n control when a proof attempt uses only a finite prefix.

### A concrete finite-prefix interval enclosure

At the exact rational parameter a=1/100, `experiments/code/heatflow_round2.py` encloses the first100 Li-type coefficients by directed Decimal interval arithmetic. Every lower endpoint is positive; the smallest is greater than0.2449129068. Transcendental inputs cosh(1/2),sinh(1/2),cosh(1/100) are bounded by exact positive rational Taylor sums plus geometric remainder bounds. The logarithmic Taylor recurrence is

    q0=cosh(1/2)+cosh(a),
    qn=(cosh(1/2) if n even else sinh(1/2))/n!,
    cn=qn/q0−Σ1≤k<n k ck q_(n−k)/(n q0),
    λn=n Σ1≤k≤n binom(n−1,k−1) ck.

All basic operations round outward at180decimaldigits. The threshold is rigorously positive using(C−1)/C≤logC≤C−1 with C=cosh(1/100), giving a bracket approximately[4.999791675×10⁻⁵,5.000041667×10⁻⁵]. Full endpoints and tail evidence are saved in `experiments/results/heatflow_round2.json`. This is an analytic finite-coefficient enclosure, not an all-n theorem. Its interval algorithm and recurrence remain pending separate adversarial review; the general existence argument above does not depend on this computation. Combining the enclosure with the nonnegative smoothing contribution gives an explicit source-class example at a=ε=1/100: its first100 Li-type coefficients are positive, it still has zeros w=±1/100+iπ, and its finite heat threshold lies strictly between0 and1/20000 inclusive at the upper endpoint. The exact threshold is not calculated.

## 8. Scope of verification and continuation

Primary source statements/images checked: deBruijnTheorem10,p204;Theorem13 and proof,p205;Theorem1,p198; selected§7; NewmanTheorems1–3 and all seven-page proof; Newmanp245 and Rodgers–Taop2 explicit kernels. Image checks were essential: OCR corrupts b0's range, endpoint inclusion, product conditions, and the Fourier-variable factor2.

Independently reconstructed portions: the threshold endpoint/Hurwitz argument, canonical-density quartic lower bound, exact atomic model, quartic smoothing's source-class membership, local-uniform witness persistence, finite-prefix argument and universal-constant sharpness. These need separate adversarial review before any claim beyond auxiliary reconstruction. No full30-page deBruijn audit or independent proof of all Newman's polynomial/entire-function antecedents is claimed.

Next concrete tasks: review the smoothing/Li Hadamard-product quantifiers; formalize the elementary log inequality and atomic threshold; investigate whether global threshold convergence can actually be proved rather than inferred from local uniform convergence; retain the exact normalization table in every future heat-flow experiment. No new classical-RH claim follows.
