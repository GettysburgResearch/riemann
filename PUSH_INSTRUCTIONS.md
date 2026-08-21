# Independent push instructions

Frozen intended base:

```text
PR #701
research/gpt56-pro/100720-cubic-hinge-rough-prefix-audited
b8fa864f257cce623b020ff94b09c5afcbcabdee
```

Suggested successor:

```text
research/gpt56-pro/103300-balanced-phase-gram
```

From a checkout of `gfreund123/riemann`:

```bash
git switch research/gpt56-pro/100720-cubic-hinge-rough-prefix-audited
git pull --ff-only
git switch -c research/gpt56-pro/103300-balanced-phase-gram

# Copy the packet contents into the repository root, excluding this outer
# directory name. Stage only the listed T103300 paths.
git add -- \
  README_103300.md PR_BODY_103300.md PUSH_INSTRUCTIONS.md \
  claims/lemmas/L-103300-critical-carrier-normalized-balanced-homotopy.md \
  claims/lemmas/L-103301-nonzero-phase-monotonicity-and-finite-euler-gain.md \
  claims/lemmas/L-103302-positive-unsieved-cubic-transition-defect.md \
  claims/lemmas/L-103303-centered-cubic-bspline-autocorrelation.md \
  claims/lemmas/L-103304-half-divisor-field-is-source-square-root.md \
  claims/refutations/R-103300-local-transition-cone-is-not-native-invariant.md \
  claims/theorems/T-103300-balanced-phase-amplitude-and-physical-occupancy-frontier.md \
  experiments/X-103300-balanced-phase-gram \
  integration/2026-08-21/t103300-source-lock.json \
  integration/2026-08-21/t103300-namespace-migration.json \
  reports/gpt56-pro/2026-08-21-balanced-phase-gram-assault.md \
  standalone/2026-08-21-balanced-phase-gram/PROOF_PACKET.md \
  T103300_CONTENT_SHA256SUMS MANIFEST.json

python3 experiments/X-103300-balanced-phase-gram/verify.py \
  --output experiments/X-103300-balanced-phase-gram/results/verification.json
sha256sum -c T103300_CONTENT_SHA256SUMS

git commit -m 'research: balanced phase and cubic Gram assault (T103300)'
git push -u origin research/gpt56-pro/103300-balanced-phase-gram
```

Open a draft PR titled
`research: balanced phase and cubic Gram assault (T103300)`, using
`PR_BODY_103300.md`, against
`research/gpt56-pro/100720-cubic-hinge-rough-prefix-audited`.
