# Survival-resolvent Bellman hardening of T-99020

Frozen parent:

```text
PR #620
493e12fcba3f9b98dda7c3595bff73b256e00ca4
```

New proof objects:

```text
L-99030 exact Hall residual root mass <16
L-99031 discounted survival-resolvent score theorem
R-99030 fixed-67 artificial-path scope firewall
T-99030 hardened full candidate
X-99030 exact replay
```

Replay:

```bash
python3 experiments/X-99030-survival-resolvent-bellman/verify.py \
  --output experiments/X-99030-survival-resolvent-bellman/results/verification.json
sha256sum -c T99030_CONTENT_SHA256SUMS
```

Expected:

```text
PASS_T99030_SURVIVAL_RESOLVENT_BELLMAN_HARDENING
9227646d2e9edead559d5169651bbe159644b5c2880470d5707c9cb8ff90fd91
```

Scientific status:

```text
new Bellman algebra                  exact
new root-mass calculation            directed exact
T-99020 score interface              materially strengthened
accepted proof of RH                 no
Riemann Hypothesis                   unproved pending review
```
