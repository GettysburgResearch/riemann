# X-105430 — Critical-sign rigidity finite replay

Run:

```bash
python -B experiments/X-105430-critical-sign-rigidity/verify.py \
  experiments/X-105430-critical-sign-rigidity/results/verification.json
```

Expected:

```text
PASS_X_105430_CRITICAL_SIGN_RIGIDITY
b2924d153ad3b49690f7329228d2445893bbfb7437e7cd77bc320e6ac9b69cb4
checks=17
RH_UNPROVEN
```

The replay authenticates:

- the exact positive-residue quartic separator `z^4-z^2+1`;
- a real-rooted quartic with the exact affine-plus-critical Herglotz split;
- the critical atom weight and location in that fixture;
- numerical sanity checks for exponential vertical-side harmonic-measure decay;
- numerical sanity checks that `exp(C log X loglog X)` is beaten by the strip side harmonic measure.

It does **not** replay:

- the completed-zeta safe-half-plane asymptotic;
- the Jensen good-side theorem;
- the finite-strip Lindelof passage for Xi;
- the complete Xi critical sign;
- the moving saddle;
- RH.

The analytic proof obligations remain in `L-105430--L-105434` and their hostile review contract.
