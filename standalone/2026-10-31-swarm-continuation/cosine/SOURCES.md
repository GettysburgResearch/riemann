# Sources, overlap, and scope

Inspected during the October 30, 2026 follow-up.

1. **Bhaskar Bagchi, _On Nyman, Beurling and Báez-Duarte's Hilbert space reformulation of the Riemann hypothesis_ (2006).** [Full primary preprint](https://arxiv.org/pdf/math/0607733). Theorem 1 is the native weighted step-space criterion used here. The paper explicitly treats the weight `1/[k(k+1)]`, the fractional-part generators, and the equivalent totality statement. Those are classical inputs, not new claims of this pass.

2. **Luis Báez-Duarte, _A general strong Nyman–Beurling criterion for the Riemann hypothesis_ (2005).** [Full primary preprint](https://arxiv.org/pdf/math/0505453). Sections 1–3 discuss replacing a target kernel and its Müntz source together, with support and regularity conditions. The general idea of changing source kernels while preserving a closure problem is therefore established prior art. This note instead keeps the literal discrete Bagchi generators and gives their explicit cosine images and finite remainder bounds.

3. **Jean-François Burnol, _On Fourier and Zeta(s)_ (final version 2003).** [Full primary preprint](https://arxiv.org/pdf/math/0112254). The retrieved paper was searched and its relevant discussion of the scale-invariant unitary `F I`, gamma multipliers, Báez-Duarte's unitary operator, and co-Poisson/ Sonine spaces was read, particularly Sections 2, 5, and 6. The use of Fourier/cosine followed by inversion as a lossless gamma-phase operator is explicitly classical. We do not claim discovery of that transform or of the Fourier–Mellin approach to RH. The full 50-page paper was not independently audited.

4. **NIST DLMF.** The [Hankel transform and inversion](https://dlmf.nist.gov/10.22.v), [Bessel Mellin integral](https://dlmf.nist.gov/10.22.E43), [gamma reflection and duplication](https://dlmf.nist.gov/5.5), and [gamma asymptotics](https://dlmf.nist.gov/5.11) supply standard special-function identities. For the order minus one half used here the Hankel kernel is the ordinary cosine kernel, and all specific normalizations are derived in the note.

5. **Nicol Leong, _On some effective results involving zeros of the Riemann zeta function_ (2025).** [Author's research summary in the Bulletin of the Australian Mathematical Society](https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/on-some-effective-results-involving-zeros-of-the-riemann-zeta-function/8D885EAF542CEA62250CDF37719DC7B0). Its final section records the standard unconditional Mertens bound of the form `M(x)=O(x exp(-c sqrt(log x)))`, as well as stronger estimates, and identifies Lee–Leong [arXiv:2208.06141](https://arxiv.org/abs/2208.06141) as a detailed source. Only the classical decay needed to justify convergence of two Möbius endpoint series is imported here; no claimed recent numerical boundary is used.

## Repository overlap

The prior packet is [PR #1026](https://github.com/GettysburgResearch/riemann/pull/1026), head `11b4f6612275955a1fddb5c53f67dc21124783f8`. Its arithmetic note identifies the signed Levy obstruction and a log-gamma-noise completion. The current pass supplies a different deterministic transformation; it does not retract the earlier classification within the stated positive convolution family.

[PR #1025's synthesis](https://github.com/GettysburgResearch/riemann/blob/21ad73effe5e1afb94a912776e2a0242931ea5ef/standalone/2026-10-30-research-swarm/SYNTHESIS.md) was read at its exact head. Its arithmetic compensator removes a character-family divisor-switching main term with cutoff Q. The `y log(n)/n` term in this note is a separate harmonic-cutoff compensation in the exact cosine image of one native fractional-part generator.

The source-specific factorization, complete native sine formulas, Sobolev estimates, and complete-frequency tail argument are derived in this pass. The targeted search did not establish that every such formula is previously unpublished. They should be described as proved components developed here, with the classical transforms and criterion attributed above, rather than as a worldwide novelty or priority claim.
