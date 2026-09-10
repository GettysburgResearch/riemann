# Sources and exact boundaries

Repository: GettysburgResearch/riemann; author branch PR #805.
Frozen parent: 7919f443c0c2c2a87f95d3237d4fe77fb87f9a74.
Original main base: 051808c1f8367b4320c52f94b40908eb2173d622.

The current PR metadata was read independently. It confirms both the
intervening growth-transfer packet at cbed8fe5cc3b29a334aa4807d328484d01dceb6a
and the subsequently uploaded balanced-lift packet. The original branch is
not overwritten with the earlier local baseline.

## Repository dependencies

- standalone/2026-09-06-astra-balanced-lift/PROOF.md: source coefficients,
  their rational constrained optimum, primitive and Mellin identities.
  Git blob 5fb7798a5d3ade45ec761e24744593cbc056a369, 19,030 bytes;
  SHA-256 b3f4ec2c4b85fa64e13370176dac3a3529ce315411752c553411623c7fff2a39.
  The exact-head directory listing and full proof were inspected.
- Its verification.json, 7,137 bytes, SHA-256
  350ee09fce4f639a6ee06b327f6423c3ae8c6e79e02fbe4dbb260b496bc15f98,
  supplies an independently produced numerical comparison, not input weights
  or new energy values. The remote content was read and the unchanged local
  predecessor replay was separately repeated in each interpreter mode.
- standalone/2026-09-06-astra-growth-transfer/PROOF.md was read at the same
  frozen head. Its bounded harmonic-Mobius convolution motivated GE26.4.
  That argument is reconstructed here, including the k-dependent weight.
  Its analytic zero-free-half-plane imports and norm-growth claims are NOT
  assumptions of GE26.1-GE26.6. No sibling code is executed by this checker.

## Classical primary references consulted

1. Luis Baez-Duarte, A strengthening of the Nyman--Beurling criterion for the
   Riemann Hypothesis, arXiv:math/0202141.
   https://arxiv.org/abs/math/0202141
   The integer approximation programme is classical. The one-way implication
   used here is also proved directly by bounded Mellin evaluation in GE26.7;
   the reverse approximation theorem is not needed for the new norm formula.

2. Werner Ehm, On certain Gram matrices and their associated series,
   arXiv:2405.06349v2.
   https://arxiv.org/html/2405.06349v2
   Consulted for the existing Gram-kernel/reciprocity landscape and for the
   boundary on conditionally optimal Mobius mollifiers. The new finite Green
   formula is derived directly. No unproved asymptotic claim from this source
   is imported. General Nyman--Beurling Gram evaluation is not new here.

3. Sandro Bettin and Sary Drappeau, Partial sums of the cotangent function,
   arXiv:1905.01954 (2019).
   https://arxiv.org/abs/1905.01954
   The abstract describes reciprocity and alternation for piecewise-smooth
   weighted cotangent sums, with continued-fraction bounds. No theorem in
   that paper has been verified to provide the full coupled endpoint bound
   GE26.OPEN. No such import or claimed range extension is made.

4. NIST DLMF, sections 5.9 and 5.5, integral and reflection formulas for psi.
   https://dlmf.nist.gov/5.9
   https://dlmf.nist.gov/5.5
   The standard difference integral plus reflection yields the cotangent
   integral used in GE26.6. The finite sum, change of variable and remainder
   inequality are proved explicitly. No computed special-function value is
   used by the checker.

The weighted norm pairing, elementary Fourier sine identity, min-kernel
factorization and tridiagonal inverse are standard Hilbert/Green algebra.
All of their needed specializations are proved. Cotangent sums in the
Nyman--Beurling problem have an extensive literature; no first-discovery or
priority claim is made for the finite Green representation or synthesis.
Only repository source bytes and the stated primary-source boundaries are
being asserted, not a comprehensive novelty audit.

## Unproved and unperformed

GE26.OPEN, the original full-source block gain, and RH are unproved.
No all-scale numerical campaign, new zero data, Lean/kernel build, external
interval certificate, remote CI PASS, or independent mathematical acceptance
is claimed. Owner settings, main, canonical registries and formal code are
outside the write scope.
