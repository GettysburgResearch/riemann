# Classical inputs, attribution and reading scope

No external result below is treated as a new project discovery. The particular
norm-transfer and all-cutoff exponent statements are proposed research
syntheses; external novelty has not been established.

**Euler arithmetic and zeta completion.** The Euler product and its absolutely
convergent logarithmic derivative on Re s>1, continuation of zeta with its
single pole, critical-strip localization and reflection are standard inputs.
NIST DLMF 27.4 and 25.10 provide the conventions:
https://dlmf.nist.gov/27.4
https://dlmf.nist.gov/25.10
No zero census or numerical zero ordinate is imported. Classical existence of
a critical-line zero is used only for the optional subcritical-b observation.

**Hardy analysis.** Paley-Wiener with norm (1/(2pi))integral |F(iy)|^2,
inner-outer factorization, and Poisson-Schwarz representation of an outer log
are imported classical theorems. All source-specific hypotheses, signs and
weighted estimates are checked in PROOF.md. Laguerre orthogonality is used
only at finite order and follows directly by Rodrigues integration by parts.
Kunik, "Logarithmic Fourier integrals for the Riemann Zeta Function",
arXiv:0804.4829v2, is a relevant primary-source lineage for the half-plane
Poisson-Schwarz and Blaschke formulation:
https://arxiv.org/abs/0804.4829
The abstract/metadata were consulted for attribution; no full-paper or PDF
review is claimed. No Kunik formula is imported as an unproved OEC26 identity.

**Logarithmic and approximation criteria.** Bui-Lester-Milinovich,
"On Balazard, Saias, and Yor's equivalence to the Riemann Hypothesis",
arXiv:1306.0856, and Burnol, "A lower bound in an approximation problem
involving the zeros of the Riemann zeta function", arXiv:math/0103058,
are primary-source context. Their abstracts were consulted, not a fresh
line-by-line audit. No numerical constant from them is needed here:
https://arxiv.org/abs/1306.0856
https://arxiv.org/abs/math/0103058

**Conditional input, used ONLY in the converse.** RH implies
|theta(x)-x|=O(sqrt(x)log^2(2x)). Lee-Nosal, "Sharper bounds for the error in
the prime number theorem assuming the Riemann Hypothesis", arXiv:2312.05628v4,
Theorem 1.2, gives stronger explicit forms. The theorem/introductory statements
in the HTML were checked. OEC26 needs only an unspecified absolute constant,
not their numerical thresholds or a replay of their calculations:
https://arxiv.org/html/2312.05628v4

**Failed unconditional bound.** The ordinary zero-free-region PNT estimate
|theta(x)-x|<=Cx exp(-c sqrt(log x)) is a classical imported estimate, also
used in the frozen OE26 packet. Constants are not numerically certified.
Its exact use and failure to reach the new endpoint are stated in
ABEL_AND_ATTEMPT.md. None of these inputs asserts the requested subpower cost.
