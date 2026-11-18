# Round 12 — a finite-moment barrier and a process limit

18 November 2026 UTC. This report updates the preceding Round 11 snapshot. The current corpus contains 999 selected works, 125 complete substantive readings, and five whole-work Level 3 audits. Selection, source access, complete reading and proof verification remain distinct. The 1,000-work substantive-reading and deep-audit program remains unfinished. No proof or disproof of RH, publication novelty, or new zero-density exponent is claimed.

## What the new calculations establish

The main advance is a precise distinction between three regimes of the derivative-weighted prime phases. Cumulative sums can have Gaussian limits. Fixed positive polynomial bands have non-Gaussian features and persistent cross-band dependence. Shrinking exponent bands have a Brownian process limit, with a proof that controls every scale of prime-subset mass. A complete comparison law has been constructed inside the corresponding random matrix model, while its arithmetic identification remains open.

The arithmetic probability throughout this report samples strict two-sided zero ordinates |γ|>Y with masses proportional to |ζ′(1/2+iγ)|²/(1/4+γ²), assuming RH. Multiple zeros have zero weight. The matrix model uses a global joint Haar-matrix/root-label derivative-square tilt, including one deterministic selected root after rotation. Changing either probability convention changes the question.

## A tempting all-order moment formula cannot be a probability law

Fix 0<a<b and let W_Y be the sum of cos(γ log p)/√p over Y^a<p≤Y^b. For each fixed integer r satisfying rb<1/2, the limiting raw moment is r! times the coefficient of z^r in

```text
M_form(z)=exp(H z+H z²/4) [(1−d z)^4+q z(1−d z)],
H=log(b/a), d=b−a, q=(2/3)(b³−a³).
```

The formula comes from the actual shifted quadratic theorem applied to aggregate Dirichlet polynomials. Its distinct-prime kernel has total degree four; the new four-prime interaction has coefficient 24. Only opposite-sign repeated-prime pairs survive, giving the Gaussian pairing factor. The remainder is estimated on the full aggregate before its main term is expanded.

This formula supplies finitely many moments at a fixed positive b. Extending it unchanged to every order is impossible: M_form(1/d)=0, but a positive probability's finite exponential moment is strictly positive. The proof of this obstruction checks the missing analytic point. The formal coefficients have an explicit signed Gaussian-polynomial inverse; its absolute even moments dominate any hypothetical positive same-moment law. Monotone convergence of cosh therefore gives every finite exponential moment, forcing that law's MGF to equal M_form.

There is also a finite certificate. On [a,b]=[1/20,1/10], a degree-70 Hermite polynomial has normalized formal squared expectation

```text
−0.0011820826117612421070700877… < −0.00118.
```

Two exact coefficient methods and independent 160-, 192- and 256-bit interval calculations verify its sign. It uses formal moments through order 140. The source window for that band supplies only orders 0–4; all tests inside the legitimate window remain positive. Thus this is an obstruction to extrapolation, not a contradiction of the source or of a possible true law with different higher moments. It specifies why additional frequency-chamber terms or another characteristic-function estimate are mathematically necessary. [Full adjudication](../audits/adversarial_reviews/director_band_laws_round12.md) · [Independent finite certificate](../experiments/results/director_round12_formal_gram.json)

Classical mock-Gaussian moment theorems and polynomial-normal transform results are relevant antecedents. The source search did not establish priority for the particular formula or obstruction. The archive preserves the exact prior-art passages and the limits of that search.

## Zero covariance misses polynomial-band dependence

For bounded real Riemann-integrable weights supported in a common [a,b]⊂(0,1/6), let C_f and S_g be the cosine and sine prime sums with those weights. Their mixed third cumulant satisfies

```text
lim κ(C_f,S_g,S_h)
 =12 [∫ f(x)(x²−2)dx] [∫ g(y)y dy] [∫ h(z)z dz].
```

The signed primary-source calculation and an independent derivative-rooted CUE projection calculation give the same kernel. All odd-sine entries vanish by reflection, so this completes the centered third tensor. For an unweighted common band, Δ_j=b^j−a^j, the new entry is (Δ₃−6Δ₁)Δ₂². On [1/20,1/10] it is exactly −21537/1280000000.

Cosine and sine have exact zero covariance. Nevertheless, for nonnegative weights with positive integrals, the mixed cubic is negative, even if the cosine and sine supports are disjoint. Uniform fourth moments pass this cubic to every weak subsequential limit. Such a limit cannot have independent cosine and sine components. Pointwise nonzero weights supported only on null sets do not imply strict negativity; an independent review caught and corrected that quantifier. The result does not decide the sine marginal or the existence of a full arithmetic vector limit. [Signed tensor and dependence proof](../audits/adversarial_reviews/director_joint_process_round12.md)

## A Brownian limit on shrinking exponent bands

Fix 0<r₀<1 and let b=b(Y)→0 while b logY→∞. Define

```text
X_Y(r)=Σ_(Y^(r₀b)<p≤Y^(rb)) [cos(γlogp)/√p−1/p], r₀≤r≤1.
```

Under RH, X_Y converges in D([r₀,1]) with J₁ topology to standard Brownian motion at time (1/2)log(r/r₀). The scalar consequence is a finite-variance Gaussian limit for any shrinking band with a/b→r∈(0,1) and a logY→∞. All fixed scalar moments converge.

The important proof ingredient is a fourth-moment bound for every prime subset of reciprocal mass h. The shifted aggregate theorem gives h²+L^−M, where L=logY. This alone does not give tightness: a singleton can have h² smaller than every fixed logarithmic saving. A separate analytic sampling argument supplies L²h². It applies disk orthogonality to ζ(s)D_I(s)² at the zeros and combines the classical continuous fourth moment of ζ with an elementary eighth moment of the prime polynomial. Multiplicity-counting disk overlaps cost only a logarithm.

The minimum of those bounds is O(h^(3/2)), uniformly at every scale. Interpolation at exact reciprocal-prime times then gives an all-time modulus. The clock approaches (1/2)log(r/r₀), jumps vanish, and the fixed-dimensional Gaussian projections identify the path limit. A full-range O(h²) bound remains unproved and is unnecessary here. Effective cutoff moduli and the audited effective aggregate input give an in-principle conditional onset; no numerical onset was calculated. [Complete proof and independent audit](../audits/adversarial_reviews/director_joint_process_round12.md)

This method is reusable: combine a sharp asymptotic with a size-independent remainder and a coarser estimate with exact local mass, then change bounds at the scale where their errors balance. A failed demand for an unnecessarily strong fourth bound has therefore become useful negative knowledge.

## The complete random matrix candidate law

For every fixed 0<a<b<∞, the globally derivative-square tilted rooted CUE Fourier band has a full limiting law and convergence of every fixed moment. Its free-point projection is the unit-density sine projection with the two Fourier modes corresponding to 1 and s−1/2 on [0,1] removed. One deterministic root is reinserted in the statistic.

The test function is f(u)=−∫_a^b cos(2πxu)dx/x. The centered statistic is defined by an L² limit of centered finite windows. Its absolute point sum diverges almost surely, so its summation convention matters. The characteristic function is a Hilbert–Schmidt regularized determinant with an explicit, absolutely convergent second-order trace correction. Local kernel convergence and uniform O(1/R) squared tail bounds prove the noncompact limit. Projection exponential bounds give convergence of all fixed moments. The finite-N calculation through N=2000 and dense exact small cases checks the implementation; it is not an arithmetic experiment or a certified convergence rate. [Law, determinant and source lineage](../audits/adversarial_reviews/director_band_laws_round12.md)

The arithmetic low moments now match this candidate through the full third tensor in their proved ranges. That is an explicit mathematical interface, but not a full law transfer. The next task is an estimate for the arithmetic characteristic function or a genuinely higher-support formula, with constants and hypotheses that reach beyond a finite moment window.

## Source fidelity and whole-work progress

Li's complete nine-page 1997 journal-typeset manifestation is now the fifth whole-work Level 3 audit. Both main positivity criteria survive reconstruction. A nonvanishing-symbol slip and a missing positive complex-place normalization factor have exact witnesses and local repairs. The Q(i) Jacobi-theta example gives true coefficient 4 versus the printed 2/π. The source came from a public mirror; current publisher-byte identity remains unverified. An initially suspected coefficient-sign error was withdrawn after checking the different Taylor centers. [Complete adjudication](../audits/adversarial_reviews/director_li_whole_round12.md)

Báez-Duarte's original strengthening and the complete HLZ article have newly recorded Level 1 readings. Their deeper source findings remain pending whole-work adjudication; this does not undo the separately verified scoped theorems. The original German Riemann pages and von Mangoldt's 1905 source have also been recovered and independently read at their stated scopes. Riemann's whole-work promotion remains pending. Earlier historical and translation qualifications are preserved without attributing translation-only defects to the original author.

The newly selected Hughes–Rudnick source has a complete Level 1 reading and a separately investigated averaging-weight tail question. The archive retains the two reviews and proposed repair as pending director adjudication. It is not counted as a verified source-error group. Primary antecedents for the CUE/Palm law and the 1905 zero-count improvement were added after exact source-hash and duplicate checks. The eight new dependencies are useful inputs, rather than additions made to force an exact round corpus count.

## What a new team should attempt next

The Round 11 report's historical transitions, operator obstructions, unconditional Hardy enclosure 0.61649875288731141829<C₂<1.075561, and broader frontier questions remain in force. This update adds the explicit full-model law, finite-moment obstruction, signed tensor and two-scale tightness method. None supplies the missing arithmetic positivity, trace realization, or quantitative approximation tail needed for RH.

A team should first replay the independent signed kernel and Hermite certificates, then reconstruct the two-scale subset bound. It should next derive the first arithmetic frequency-chamber correction beyond the finite window, or prove a bounded-test comparison with the explicit compensated DPP law. In parallel, it should complete the pending whole-work source adjudications and expand complete readings beyond the present 125. The durable ledgers and continuation commands specify exactly which work has been completed and which has not.
