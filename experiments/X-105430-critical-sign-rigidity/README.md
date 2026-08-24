# X-105430 — Critical-sign rigidity finite replay

Run:

```bash
python -B experiments/X-105430-critical-sign-rigidity/verify.py \
  experiments/X-105430-critical-sign-rigidity/results/verification.json
```

Expected:

```text
PASS_X_105430_CRITICAL_SIGN_RIGIDITY
7a806d3972d352cc7287436ebf2d82b85314bebf6bfc3fea1c44a24d035c1e2a
checks=23
RH_UNPROVEN
```

The replay authenticates:

- the exact positive-residue quartic separator `z^4-z^2+1`;
- a real-rooted quartic with the exact affine-plus-critical Herglotz split;
- the critical atom weight and location in that fixture;
- the exact three-height localizer partial fraction;
- the fine-scale residue-recovery coefficient;
- positivity of the microscope Fourier polynomial;
- the unit-interval bound for the scale-flow symbol;
- numerical sanity checks for exponential vertical-side harmonic-measure decay;
- numerical sanity checks that `exp(C log X loglog X)` is beaten by the strip side harmonic measure.

It does **not** replay:

- the completed-zeta safe-half-plane asymptotic;
- the Jensen good-side theorem;
- the finite-strip Lindelof passage for Xi;
- coarse-scale Xi microscope negativity;
- backward microscope scale descent;
- the complete Xi critical sign;
- the moving saddle;
- RH.

The analytic proof obligations remain in `L-105430--L-105437`, `T-105430`,
`T-105440`, and their hostile review contracts.
