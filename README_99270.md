# T-99270 — Three-vulnerability hardening of the scalar SHARP route

This add-only successor to PR #647 audits the three weakest points of its
closure chain and repairs or bypasses each one.

## Main advances

1. **Pointwise tail weakened.** RH follows from either eventual positivity of
   one zero-free multiplicative box average or subpower logarithmic negative
   mass.
2. **Composition removed.** The scalar conclusion no longer depends on the
   SHARP row kernel, Hall, random-key ownership, Volterra calibration, or the
   PR #648 coboundary route.
3. **Consumer and finite theorem authenticated.** Landau is proved from
   first principles, and an independent global-Möbius scanner rechecks every
   real cell through `10^8`.

## New arithmetic mechanism

The factor-67 defect has the exact positive inverse renewal

```text
T(x) = sum_(d<=x) (v_67(d)+1)/sqrt(d) * h(x/d)
```

and an exact logarithmic prime-power owner. The new live target is a
source-owned Carleson estimate proving subpower negative mass.

## Replay

```bash
cd experiments/X-99270-three-vulnerability-hardening
python3 verify.py --output results/verification.json
python3 -m unittest discover -s tests -v

# optional complete independent 10^8 replay
./replay.sh --full
```

Expected fast verdict:

```text
PASS_T99270_THREE_VULNERABILITY_HARDENING
2c73659aecec49a110a9dd9ce060d1b9699add76a114e362781b8890aebde0d5
```

## Boundary

```text
pointwise global tail       unproved
smoothed global tail        unproved
subpower negative mass      unproved
Riemann Hypothesis          unproved
```
