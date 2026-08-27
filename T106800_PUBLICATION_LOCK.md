# T-106800 publication lock

Created: 2026-08-27  
Repository: `gfreund123/riemann`  
Branch: `research/gpt56-pro/106800-beta-spectral-abscissa`  
Pull request: `#762`

## Frozen base and scientific checkpoint

```text
original audited PR #758 parent:
fad8ce2c4ce8633c5bb67356e6765800eac3d440

final synchronized PR #758 base:
fc7ee1304746d3c5b50d02592ccb0d8cdf329c4f

scientific commit:
2c3d4a651da8c30764f0c603492d932f3a4e9fe0

scientific tree:
ebb6615edaa08d173aede8dd05e19d6d9006188b
```

The eleven parent commits between the original audit head and the synchronized
base add disjoint function-field, beta-renormalization, Tate-notch, and
spectral-nonalignment packets. None changes a T-106800 path. The final parent
also supplies a zero-independent beta-kernel repair; T-106800 is compatible
with it but does not require a zero-dependent kernel choice.

## Conclusion-facing Git blobs

```text
claims/lemmas/L-106800-half-weighted-zero-abscissa-transport.md
779b7e5b8f1d5ea79e15ed56122386e60b29c9e7

claims/lemmas/L-106801-critical-beta-maximal-energy-and-vk-transfer.md
e1b5fa7763fca07286d30239c35c30fc647393b6

claims/theorems/T-106800-single-harmonic-spectral-abscissa-and-vk-energy.md
23b37a5afd2d2bb17cebab55639bd690073a8610

claims/refutations/R-106800-endpoint-only-and-source-blind-shortcuts.md
dce460cacd537b0e52398b592ec89f3a76364ab0

experiments/X-106800-beta-spectral-abscissa/verify.py
9e6a7c497b108f290f80722ec8a32a7b0949d78d

experiments/X-106800-beta-spectral-abscissa/results/verification.json
919556e8d4084450dbff6abd9a68306ca68e3978

integration/2026-08-27/t106800-source-lock.json
e21e32fc7eb0cb723d3983dc0643bf7fd3f51698
```

## Replay

```text
PASS_T106800_BETA_SPECTRAL_ABSCISSA_AND_VK_ENERGY

exact checks:
155561

proof object:
439a4c6f55c11c2af331eafb711f2e72e4ec4712deb714fad0a12ac21f7ec403
```

## Scientific status

```text
single fixed beta harmonic exponent:             2*Theta-1 PROVED
maximal compact beta energy exponent:            2*Theta-1 PROVED
zero-free half-plane growth dictionary:          PROVED
Vinogradov-Korobov beta-energy saving:            PROVED FROM CLASSICAL INPUT
fixed power saving:                               NOT PROVED
new zero-free half-plane:                         NOT PROVED
Riemann Hypothesis:                               UNPROVED
Generalized Riemann Hypothesis:                   UNPROVED
```

The replay authenticates exact finite transformations and constants. It does
not reprove the classical Mertens zero-abscissa theorem or the external
Vinogradov-Korobov Mertens estimate.
