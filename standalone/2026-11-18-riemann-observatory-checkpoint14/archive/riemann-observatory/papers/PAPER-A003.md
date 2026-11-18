# PAPER-A003 — Lamzouri: finite multisets and unconditional critical zeros

Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, [arXiv:2609.02882v2](https://arxiv.org/abs/2609.02882v2), first 2 September 2026, revised 8 September 2026. Preprint; no journal publication verified. Accessed 17 November 2026. Complete mathematical text and appendix read (L1); finite inequality and derivative weight removal reconstructed, not whole-paper L2. Upstream original BGSTB Lemma5 inspected, not all of its proof inputs.

## Exact core

For λ>0, η real, even in L²(R), suppη⊂(−λ,λ), ∫η²=1, write K(z)=Fourier(η²)(z), Fourier convention exp(−2πiuz). For a finite nonempty **conjugation-invariant multiset** Z, Proposition2.1 pp6–12 gives

number of simple real elements ≥ 2|Z| − Σ_{z,s∈Z}K(z−s)².

Sums count multiplicity; the square is the analytic square, not the pointwise absolute square. Although individual off-line terms need not be positive, the total is real and equals a tensor Hilbert-space norm. There are also bounds for distinct elements, simple-or-real elements, and combined simple plus real counts. Conjugation symmetry is indispensable: Z={i} violates the displayed conclusion since K(0)=1 would give 0≥1.

Theorem1.1, p3: with C0=3/2−cot(1/√2)/√2=0.6725007…, C1=(1+C0)/2 and C2=(1+2√2+2C0)/(3+2√2), the lower limits are N0s/N≥C0; Nd/N≥C1; Ns∪0/N≥C2; (Ns+N0)/(2N)≥C1. N0 counts critical zeros with multiplicity, N0s counts simple critical zeros, Ns counts simple zeros anywhere, Nd distinct zeros anywhere. These are classical ζ statements; the theorem does not establish RH or simplicity of all zeros.

## Architecture and specific checks

Conjugation-invariant finite Z → f_z(u)=η(u)e^(−2πiuz) → split conjugate pairs into g_z,h_z → nested subspaces U⊂V⊂W → real Gram–Schmidt coefficients → Bessel inequality in the tensor square → scalar quadratic inequalities with different charges for simple-real, multiple-real and nonreal pairs → finite counting inequality. Linear independence follows from exponential-polynomial uniqueness on the positive-measure set where η≠0. Degenerate empty subranges contribute zero; distinct/nonreal versus multiplicity counts must not be interchanged.

Apply to Z_T={i(ρ−1/2)logT/(2π):0<Imρ≤T}, invariant under conjugation by ρ↦1−conjugate(ρ). The upstream unconditional pair correlation is weighted by w(ρ−ρ')=4/(4−(ρ−ρ')²). Lemma3.2 removes w using **two fixed tests**, Q=f*f and Q'', f=η²: define r_T=Q−Q''/(4log²T). Since Fourier(Q'')=−4π²z² Fourier(Q), at z=i(ρ−ρ')logT/(2π), Fourier(r_T)(z)w(ρ−ρ')=K(z)². Apply upstream theorem separately to Q and Q''; a direct invocation for a changing test r_T would require uniformity not supplied by a fixed-test statement. Smoothing parameter δ is fixed first, T→∞ second, δ→0 last. The limiting cosine window is positive on [−1/2,1/2], so ηδ is a valid smooth square root and support stays strictly inside the bandwidth.

## Limitations and reuse

AppendixA says formal certificates cover Proposition2.1 and Theorem1.1 **assuming** upstream Lemma5 and standard zero counting. No local build of the Lean repository was performed; formal status is source-reported. Remark3.4 identifies the Montgomery–Taylor extremal constant as optimal for this single-window argument. Larger critical-line claims exist by October/November 2026 and require separate certificate audits; this paper is not called the final record.

The reusable ingredient is positivity of the **whole tensor sum**, replacing impossible termwise positivity of an entire kernel at arbitrary complex differences. Next: derive explicit finite-T constants for a fixed smooth η by unpacking upstream O_f terms; then certify finite-T lower bounds. Another direction is proving richer pair-interaction lower bounds, but a numerical optimum alone is insufficient.
