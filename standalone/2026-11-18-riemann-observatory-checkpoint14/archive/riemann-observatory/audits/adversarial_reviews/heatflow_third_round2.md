# Independent heat-flow controls and Li100 review

Reviewer: li_advocate. Date:2026-11-17. Inspected `audits/heatflow_round2.md`, the complete directed-Decimal program and result, original deBruijnTheorem1 passage and the p.205 Theorem13 image. This review addresses the auxiliary atomic/smooth controls and finite coefficient certificate; it does not independently audit every antecedent in the full Newman classification.

## Analytic controls

For ρ_a=cosh(a)δ_0+(δ_1+δ_(−1))/2, multiplication by exp(τu²) gives exactly e^τcoshw+cosha. Solving coshw=−e^(−τ)cosha yields only imaginary zeros exactly when τ≥logcosha; at equality odd-π zeros are double. Below it there are simple off-axis zeros at±arcosh(e^(−τ)cosha)+(2k+1)iπ. The initial strip width is a. These are measure facts; the report correctly refrains from applying the function-only source theorem directly to atoms.

The differential comparison Δ'=−cothΔ gives d/dτ[a²−2τ−Δ²]=2(ΔcothΔ−1)≥0. **Its forward-strip conclusion Δ(τ)≤sqrt(max(a²−2τ,0)) is a τ≥0 statement from initial time0.** For negative τ the comparison reverses. Thus the report's informal phrase 'consistent with the exact model' must retain that forward-time range. All substantive sharpness and threshold arguments use positive τ and survive this clarification.

The original p.205 Theorem13 indeed assumes all initial zeros in a strip and uses multiplier exp(λ²u²/2), yielding width sqrt(max(Δ²−λ²,0)); hence direct τ gives2τ. Its all-zero assumption is important and is preserved by the proposed smoothing.

For h_ε∝exp(−(u/ε)^4), deBruijnTheorem1 applies to its potential: the derivative4u³/ε⁴ has only imaginary-axis zeros. Its Fourier zeros are real, equivalently the Laplace zeros are imaginary. The transform has order<2. Convolution with the three atoms produces the displayed positive even smooth density, still super-Gaussian after translations. At τ=0 its transform is exactly the atomic factor times M_ε. Off-axis zeros of the former cannot be canceled by the latter, whose zeros are imaginary. The initial strip is therefore exactly a.

The all-real-parameter heat integrals exist by quartic decay. The source theorem gives real-rootedness for τ≥a²/2. An off-axis initial zero persists on an open τ-neighborhood by Rouché, giving a strictly positive lower threshold. The real-rooted parameter set is upward closed, and local-uniform convergence plus the positive value at0 closes it at its endpoint. Hence0<Λ_(a,ε)≤a²/2 is correct for a>0.

After substituting v=εy, compact τ,w parameter sets have a uniform integrable majorant exp(−y⁴+C y²+C|y|+C). This proves the asserted local-uniform convergence to the atomic heat transform. A fixed simple off-axis zero before τ_a then persists, proving liminf_(ε→0)Λ_(a,ε)≥logcosha. No convergence of the global thresholds follows solely from this argument; the report correctly leaves it open.

For any c>2, choose small a with logcosha>a²/c. At τ=a²/c the atomic off-axis zero persists in a sufficiently narrow smooth approximation, contradicting the proposed universal c improvement. This proves sharpness of the coefficient2 even in the positive even C∞ super-Gaussian subclass. It does not require knowing the smooth threshold exactly.

## Smoothing and Li coefficients

An even entire transform of order<2 with only imaginary zeros and nonzero value at0 has a paired Hadamard product with no nonconstant exponential factor: the Hadamard polynomial has degree≤1 and evenness removes its linear term. The paired reciprocal squares converge. After shifting s−1/2, every pair gives a nonnegative Li contribution. Therefore adding logM_ε cannot reduce any Li coefficient. This justifies the smoothing lift of a finite positive atomic prefix; it does not assume a Gaussian exponential factor has disappeared without an order bound.

## Decimal interval audit and replay

I read and independently reran `experiments/code/heatflow_round2.py`. All100 lower endpoints were positive; the minimum was0.2449129068115194… . The threshold bracket was positive as recorded. Every acceptance decision uses directed Decimal Context operations, not default-context rounded arithmetic.

The hyperbolic inputs use exact Fraction positive Taylor sums through index80. The next term divided by1−r bounds the whole remaining tail because successive term ratios decrease and r is the first omitted ratio. The stated even/odd next degrees162/163 are correct. Conversion to Decimal uses outward division. Addition, multiplication, signed negation and reciprocal use the proper endpoints and ROUND_FLOOR/ROUND_CEILING, including negative coefficients.

If q(t)=∑q_nt^n and logq=const+∑c_nt^n, coefficient comparison in q'=q(logq)' gives exactly the implemented recurrence. The binomial conversion λ_n=n∑_(k=1)^n binom(n−1,k−1)c_k is correct. Only q coefficients through n are needed; no uncontrolled analytic tail of the logarithm is being dropped. The threshold bound (C−1)/C≤logC≤C−1 is valid for C≥1; interval dependency widens but does not invalidate its enclosure.

## A second independent arithmetic backend

I also wrote and ran `experiments/code/heatflow_li100_third.py`. It uses the previously audited standard-library scaled-integer interval backend at512 bits. Hyperbolic inputs are built from independently enclosed exp(±1/2),exp(±a), and coefficients are obtained through reciprocal-series inversion followed by q'/q convolution, rather than the author's direct log recurrence. All100 lower bounds again passed. Results are in `experiments/results/heatflow_li100_third.json`; the exact log threshold is enclosed through the independent elementary log algorithm. No external package or ordinary floating-point acceptance is used.

This verifies the finite100-coefficient statement at a=1/100 and, with the analytic nonnegative smoothing contribution, the claimed explicit smooth example at a=ε=1/100. It does not establish all-n positivity, the exact smoothed threshold, or any result about classical ξ.

Classification: independently checked controls and two arithmetic replays with no issue in the substantive statements. The forward-time qualifier in the atomic strip comparison should be made explicit. Whole-source bibliographic and normalization claims outside these inspected passages remain the responsibility of the primary-source track.
