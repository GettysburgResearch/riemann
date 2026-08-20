# T99810 — Canonical fail-closed RH proof spine after the native-source audits

The original packet froze PR #656 at
`db404ec00cf022f003ee2bbee66e0cf62ac45003`.  This collision-safe publication
stacks on PR #659 at `83c17b32a99ac9e1aa5aec3168535550eb286636`,
which has since committed the separate GPMOC route advertised only in the
earlier PR #656 prose.  The present packet contributes the complementary
Euler–Hausdorff and phase-owner formulation.

**The Riemann Hypothesis remains unproved.**  The purpose of this packet is to
publish the strongest proof spine actually supported by the repository, remove
superseded full-proof claims from the normative graph, and add two exact
structural results:

1. an Euler–Hausdorff representation of the scalar SHARP obstruction;
2. a real-pole firewall for every coefficientwise-positive inverse-renewal
   completion.

It also proves that phase twisting removes the pointwise degeneracy of the
owner martingale in global Abelian average.  What remains is a source-specific
localization/Carleson theorem across distinct squarefree cores.

## Canonical scalar

Put `p=67`,

\[
 \beta(n)=\mu(n)-\mathbf1_{p\mid n}\mu(n/p),
 \qquad
 T(y)=(4\sqrt y-3)\mathbf1_{y\ge1},
\]

and

\[
 h(x)=\sum_{n\le x}\frac{\beta(n)}{\sqrt n}T(x/n).
\]

The exact Mellin transform is

\[
 \int_1^\infty h(x)x^{-s-1}dx
 =\frac{(1-p^{-(s+1/2)})(s+3/2)}
 {s(s-1/2)\zeta(s+1/2)}.
\]

The live repository proves that

\[
 RH\iff \int_1^X h_-(t)\frac{dt}{t}=X^{o(1)}
 \iff \int_X^{67X}|h(t)|^2\frac{dt}{t}=X^{o(1)}.
\]

T99810 gives a third exact formulation through the positive Euler discrepancy.

## Replay

```bash
python3 experiments/X-99810-canonical-spine/verify.py \
  --output experiments/X-99810-canonical-spine/results/verification.json
sha256sum -c T99810_CONTENT_SHA256SUMS
```

Expected:

```text
PASS_T99810_CANONICAL_PROOF_SPINE
```

## Binding boundary

```text
historical paired stopping-line proof        rejected by native-source audit
contracted alpha-child native promotion      false
canonical scalar/Mellin consumer              exact
Euler–Hausdorff bridge                        exact
positive-completion real-pole firewall        exact
phase-owner Abelian spectral gap              exact
PR #656 body-only claims at frozen head        excluded historically
PR #659 GPMOC successor                        committed / separate open gate
cross-core localization/Carleson theorem      open / RH-equivalent
Riemann Hypothesis                            unproved
```
