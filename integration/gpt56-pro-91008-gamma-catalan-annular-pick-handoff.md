# Integration handoff — Gamma–Catalan safe-disc law and annular Pick sign

## Source lock

```text
repository:      gfreund123/riemann
parent PR:       #394
parent branch:   research/gpt56-pro/91004-radial-curvature-depth-projector
parent SHA:      82ee32348b05512514462966bfeb4e2de4ae5ecf
continuation:    research/gpt56-pro/394-gamma-pick-annular-asymptotic
RH status:       UNPROVED
```

The continuation is additions-only relative to the frozen parent, apart from no parent-file edits.

## Review order

1. `claims/lemmas/L-91008-high-carrier-safe-disc-is-catalan-stieltjes.md`
2. `claims/theorems/T-91003-safe-disc-positivity-and-growing-catalan-jet.md`
3. `claims/refutations/R-91003-subcritical-safe-disc-tests-are-high-carrier-blind.md`
4. `claims/lemmas/L-91009-log-derivative-control-transfers-to-annular-pick-positivity.md`
5. `claims/theorems/T-91004-vinogradov-korobov-penetrates-the-pick-sign-annulus.md`
6. `experiments/X-91008-gamma-catalan-safe-disc/`
7. `experiments/X-91009-vk-annular-pick-ray/`
8. `reports/gpt56-pro/2026-08-11-gamma-catalan-annular-pick.md`
9. parent PR #394, then PR #393

## Claim classification

| Claim | Intended classification | Notes |
|---|---|---|
| high-carrier `A_x/log|x| -> Phi` on fixed safe discs | proposed complete asymptotic theorem | uses only Stirling and absolute Euler convergence |
| `Phi` Catalan coefficient law | exact algebra | independent of zeta |
| `Phi` beta-`(3/2,3/2)` Stieltjes measure | exact integral identity | yields strict fixed Pick geometry |
| real-ray positivity to `3/4-C/log|x|` | proposed unconditional theorem | inside direct-Euler disc |
| growing safe-line coefficient/Hausdorff positivity | proposed unconditional theorem | leading order `(1/log(4/3)) log log|x|` |
| off-line pair coefficient/pole law | exact, imported algebra | from PR #393/#394 pole formula |
| subcritical safe-disc blindness | proposed complete asymptotic firewall | no RH conclusion |
| general sublog log-derivative transfer | proposed complete conditional theorem | exact declared input |
| VK annular positivity | proposed unconditional transfer | depends on standard classical log-derivative theorem |
| full annular Pick/radial-curvature sign | open / RH-equivalent | not claimed |

## Integration cautions

1. Do not transfer upstream Anthropic Lean status to any file in this continuation.
2. Do not describe the Catalan limit as evidence for RH; it is universal high-carrier gamma background.
3. Do not infer global Pick positivity from convergence of fixed finite Pick matrices.
4. The Vinogradov–Korobov theorem is an external classical input and the continuation does not improve its zero-free-region constant.
5. The positive real-ray statement is weaker than full Pick positivity and much weaker than pointwise radial curvature positivity.
6. The constant `1/log(4/3)` is a sharp asymptotic detection boundary for the deepest possible off-line pair, not a proof that such a pair exists.
7. All analytic theorem packets require independent review before canonical integration.

## Replays

```bash
cd experiments/X-91008-gamma-catalan-safe-disc
python3 verify.py --json /tmp/x91008.json
cmp /tmp/x91008.json results/verification.json
sha256sum -c SHA256SUMS

cd ../X-91009-vk-annular-pick-ray
python3 verify.py --json /tmp/x91009.json
cmp /tmp/x91009.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected:

```text
PASS_GAMMA_CATALAN_SAFE_DISC
PASS_VK_ANNULAR_PICK_RAY
```

The replays certify finite identities and scale laws only.

## Exact frontier after this branch

```text
safe-disc asymptotic object                     explicit Catalan Stieltjes law
pointwise safe-ray sign                         closed to 3/4-C/log|x|
classical zero-free sign penetration            closed at VK-width past 3/4
fixed safe-disc Pick/Hankel packets              asymptotically positive and RH-blind
critical growing order                          begins at loglog|x|/log(4/3)
fixed annular radius                            open
cofinal radius one / radial curvature sign      RH-equivalent and open
Riemann Hypothesis                              unproved
```
