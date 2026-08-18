# X-97700 — future-prime hinge Bellman replay

This is an exact-rational regression for `L-97700` and `L-97701`.

It checks:

- the exact squared inequality behind the uniform one-prime gap at `p=67`;
- additivity of the oriented Lorenz hinge deficits under disjoint source union;
- parity-swap covariance `D^+(S A)=D^-(A)`;
- positive source scaling;
- the one-step coupled Bellman equations;
- the two-step elimination `D^+=g^+ + R^2 D^+` on synthetic finite trees.

Run:

```bash
python3 experiments/X-97700-future-prime-hinge-bellman/verify.py
```

Expected:

```text
PASS_X_97700_FUTURE_PRIME_HINGE_BELLMAN
safe_edge_square_gap= 2524
```

The replay verifies finite algebra only.  The asymptotic refutation `R-97700`
uses classical prime-harmonic asymptotics and the retained annular base theorem;
the replay does not replace that analytic proof.  It also does not construct the
open explicit Bellman barrier or prove RH.
