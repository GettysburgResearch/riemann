# Validation, review scope and reproducibility

This packet contains proposed source-conditional research. The mathematical arguments were checked by separate AI agents at the scopes below. Those reviews and the finite diagnostics do not independently establish the imported theta machinery, the angular reciprocal theorem, the native moment premises, or the external fixed-order large sieve. They are not human peer review or proof-assistant formalization.

## 1. Analytic and source premises

The mixed completed estimate and full A2 transfer use the pinned OpenAI theta framework and the stated classical row sieve. The improved scalar notation `beta=11/12` additionally uses the canonical angular reciprocal input on a fixed line strictly to its right, with a final epsilon loss; the `beta=1` alternative uses counting in that scalar step. The latter alternative still retains the theta foundation.

The signed inverse-Möbius sector estimates use the native second moment uniformly in every shortened scale and polynomial moving mask at the same physical height `H=D^h`, with `h>1` fixed. Their stronger `b<1` version also requires the explicitly uniform pointwise premise. A fixed-character bound with unspecified conductor dependence does not satisfy that premise.

The `4/7` spectral extension separately imports Alexandre de Faveri's Theorem 1.1 at arXiv:2610.04045v1. The primary statement and fixed-family conventions were inspected by the root and the spectral reviewer. The theorem is credited as an external input, not reproved. It is not needed for the `31/19` full A2 estimate or the preserved `5/8` spectral baseline.

The proof that the full positive A2 correction sum closes does not control the centered signed two-column first-Poisson remainder or the adverse initial dual-height regime. The full fourth inverse moment, `17/24`, a cofinal moment hierarchy and a new zeta zero-free boundary remain open.

## 2. Scoped independent reviews

Every report names exact target SHA-256 hashes. The manifest binds the reports to those same bytes.

| Report | Checked scope |
|---|---|
| [Root mixed and spectral review](reviews/ROOT_MIXED_AND_SPECTRAL_REVIEW.md) | New mixed-label local costs, overlap/zero conventions and masked inverse; baseline all-row spectral mean; optimal-sieve application and its limits |
| [Stratified inverse interface review](reviews/STRATIFIED_INVERSE_INTERFACE_REVIEW.md) | Composition with the mixed estimate, exact inverse masks/phases, capped empty tail and disjoint row strata |
| [Stratified inverse proof review](reviews/SIXTH_POWER_STRATIFIED_INVERSE_REVIEW.md) | Sixth-power-free sieve specialization, exponent sums, cutoff optimization, scale conventions and scope |
| [Full A2 transfer review](reviews/ANISOTROPIC_A2_NORM_TRANSFER_REVIEW.md) | Exact #914/#918 coefficient projection, all label overlaps, arbitrary positive cutoffs, all six independently derived norm exponents and complete correction sum |
| [Signed graph and matching review](reviews/CROSS_GCD_GRAPH_AND_MATCHING_SECTORS_REVIEW.md) | Native covariance lemma, one-sided selectors, fixed all-order matchings, all 15 fourth-moment intersections and hard-complement scope |
| [Independent arithmetic review](reviews/MIXED_STRATIFIED_ARITHMETIC_REVIEW.md) | Finite character identities, local valuation exponents, repeated cube factors, cutoff support, rational optimization and A2 bookkeeping |
| [Optimal-sieve spectral review](reviews/OPTIMAL_SIEVE_SPECTRAL_EXTENSION_REVIEW.md) | Fixed-family comparison, literal shared-prime zeros, all-row multiplicity, three crossovers and exact squarefree-row cusp corollary |
| [Packet scope review](reviews/PACKET_SCOPE_REVIEW.md) | Headline normalization, parameter uniformity, distinct arithmetic/spectral regimes, source conditions and unproved interfaces in the README |

The root authored the stratified inverse and helped derive the A2 cutoff. Its own review is not counted as independent validation of those arguments; separate agents supplied those reviews. Each review explicitly identifies the inherited analytic inputs it accepts without reproving.

## 3. Executed exact arithmetic diagnostics

The root read the checking code and independently ran all three programs. Their generated JSON results are included with the packet. Arithmetic is exact: integer pairs for `Z[zeta_6]` and rational fractions for exponents. Acceptance gates raise `RuntimeError` explicitly and do not depend on removable Python assertions.

### Mixed labels, inverse and A2 scales

`checks/check_mixed_stratified.py` passed:

- 2,401 effective-row relabel identities and 2,401 cubed identities, including every zero/sixth-root assignment in the four-variable q/f-overlap model.
- 14,406 physical cube-mask identities.
- 175 one-prime and 8,281 two-prime sixth-power character identities, including 5,145 cases with a prime shared by the sixth-power part and its remainder.
- 216 exact residue-progression checks and the three local energy-cost exponents for each moving-label type.
- 3,136 full inverse identities and 25,088 truncated inverse identities, with all q/f/outer-mask combinations in the two-prime model.
- Live repeated `h/b`, inner `n/d`, and outer-mask `r/h` overlap terms; 3,136 below-one empty-short cases and 3,136 exactly empty capped tails.
- Exact optimization on the vertices of the feasible logarithmic parameter tetrahedron, split at `R1=R2`, for `beta=1` and `beta=11/12`.
- The A2 normalization and overlap removal, all six norm-exponent triples, and the harmonic counts `(0,1,0,2,0,0)`.

This finite convolution model uses exact sampled physical data with the original support and incidence rules. It does not construct actual Gauss coefficients or numerically evaluate theta transforms. Its purpose is to expose illegal mask deletion, extra coprimality, repeated-factor loss and exponent errors.

### Signed graph and matching identities

`checks/check_cross_gcd_graph.py` passed:

- 784 bounded-gcd-selector covariance identities.
- 3,920 fourth-moment and 5,880 sixth-moment matching identities, with ordinary and signed one-sided shared-incidence selectors and all 49 row phase/zero assignments at two primes.
- 2,621,440 endpoint-selector checks over a four-prime model, including 2,370 cases where the residual endpoint gcd in the cycle is material.
- Exact classification of all 15 nonempty cross-edge intersections as 4 single edges, 2 matchings, 4 stars, 4 paths and 1 cycle.
- Rational verification of the union range and selected fixed-order exponent identities.

The checker evaluates finite signed identities, not the native second moment or the infinite higher-order inequalities. The all-order theorem is proved symbolically in the manuscript; the finite model exercises orders four and six.

### Spectral exponents

`checks/check_spectral_exponents.py` passed the exact crossover calculations for the old and new block envelopes, recovered the thresholds `5/8` and `4/7`, and checked the limiting scalar change `13/16 - 11/14 = 3/112`. It also rejects the tempting false improvement obtained by deleting the mixed term `H^(5/6) X^(1/3)`: at `a=9/16`, the resulting actual norm exponent would still be `65/128 > 1/2`.

This is exponent bookkeeping and an explicit negative control. It does not numerically certify analytic continuation, the theta estimate or the external large sieve.

## 4. Reproduce the packet checks

From the repository root:

```bash
python standalone/2026-10-10-sextic-moving-labels/checks/check_mixed_stratified.py
python standalone/2026-10-10-sextic-moving-labels/checks/check_cross_gcd_graph.py
python standalone/2026-10-10-sextic-moving-labels/checks/check_spectral_exponents.py --output standalone/2026-10-10-sextic-moving-labels/checks/spectral_exponents.json
python standalone/2026-10-10-sextic-moving-labels/checks/verify_packet.py
git diff --check 1a1152008706f7e24fa1efe4990588f8f99c5d8d HEAD -- README.md standalone/2026-10-10-sextic-moving-labels ':!standalone/2026-10-10-sextic-moving-labels/sources/**'
```

The first three commands regenerate the committed diagnostic reports deterministically. The integrity verifier checks the entire file inventory except the manifest itself, byte counts, SHA-256 hashes, source Git blob identities, the actual pinned `commit:path` lookups, and the exact review-target hashes. The pinned Git objects must be available locally; when one is missing the verifier explicitly names the commit that must be fetched. A local source copy with only a matching declared string is not sufficient.

The final command checks the authored changes after committing; the local prepublication gate uses the same path scope with `--cached`. Exact source snapshots are excluded from this whitespace-only check because `sources/pr921/ARBITRARY_ROW_MOMENTS.md` deliberately retains its pinned upstream extra newline at EOF. Its bytes are checked by the source verifier. The new spectral review's extra EOF newline was removed without changing its content or its target hashes; the manifest records the resulting review bytes. No mathematical manuscript was changed after its review.

[SOURCE_LOCK.json](SOURCE_LOCK.json) includes 33 pinned repository source objects and separately identifies the external primary references. Nine newly needed adjacent source files are preserved byte-for-byte; earlier retained sources and snapshots are referenced in place. The additional external paper is linked by exact version and has not been copied in full.

`MANIFEST.json` intentionally excludes its own bytes to avoid a circular hash. Git fixes the manifest bytes in the eventual commit. The manifest does include the verifier and all review reports. Source integrity, finite arithmetic checks and mathematical review are distinct claims, with the limits above.
