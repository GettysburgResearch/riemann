# NGR26 execution and assurance boundary

The mathematical assertions are proposed paper proofs. No independent referee
acceptance, RH proof, Lindelof proof or new critical prime-error bound is claimed.

## Bounded reconstructions

`check.py` is standard-library Python, using integers and Fraction. It includes:

- 12 gamma mass/mean/variance cases, shapes/rates 1 through 12.
- 312 rational transform evaluations and 78 pairs of complete stable-kernel
  majorants. These are checks of finite formulas, not a grid proof of an analytic
  inequality on a half-plane.
- 12 exact norms of the gamma-smoothed exponential TARGETS, not actual feedback
  energies. At D=1 the exact norm squared is 2/3.
- Three balance/centering/prefix checks of the parent's native bank with its
  logarithmic seed correction retained as a FORMAL variable. Its true logarithmic
  value and old error below 0.02 are not numerically evaluated here.
- 384 floor-increment comparisons and 34 complete truncated Dirichlet-feedback
  panels through index 128, degrees 1 through 4. Independent divisor summation
  checks the convolution; source telescoping and all pre-horizon zeros are kept.
  Nothing after that coefficient cutoff is counted as numerically reconstructed.
- 12 complete polynomial-tail antiderivative identities, with the factor exp(-T)
  symbolic; these authenticate the factorial tail formula, not actual tail sizes.
- Eight explicitly SYNTHETIC, rank-deficient three-feature ridge problems and
  their complete-square identities. No actual G_m or optimized b_m is evaluated.

Ordinary and optimized isolated Python reconstruct byte-identical mathematical
output. `--emit` is producer mode, not authenticated acceptance. The accepting
`--check` validates the exact inventory/hashes, rejects duplicate JSON keys,
float/nonfinite numbers and Boolean aliases, and reconstructs every retained
mathematical result. Acceptance does not use assert.

`test_rejections.py` executes one pristine copied acceptance and eight actual
refusals per mode. Cases are: altered target norm, false RH status, Boolean alias,
float alias, duplicate JSON, a resealed primitive kernel shift changed from 1/2
to 1/3, unsealed proof mutation, and an extra file. The primitive mutation fails
an independent rational transform identity, not merely a file hash.

Commands:

```bash
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
python -I -S -B test_rejections.py
python -I -S -B -O test_rejections.py
```

## File delivery

The flat packet has ten regular files including SHA256SUMS, with nine manifest
entries. A clean archive extraction and an add-only temporary Git patch roundtrip
are tested with both checker modes and preserve an unrelated sentinel. They are
not complete Riemann repository builds. Remote publication is checked separately
against the same local Git blob and subtree identities; the external handoff
receipt records the final commit without circularly changing this packet.

The parent 16,739-byte manuscript was read from the mounted handoff and fetched
through the connector; its local Git blob and SHA256 match SOURCES.json. No parent
executable, million-cell certificate, high-degree zeta integral, actual zero,
external numerical campaign, Lean/Comparator, Windows run or remote CI is claimed.
The latest other-agent PR descriptions supplied orientation only. Primary DLMF
sections and an abstract-level prior-art check are separately recorded. The full
analytic proofs are not consequences of the finite test counts.
