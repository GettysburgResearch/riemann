# X-105430 — Critical-sign rigidity finite replay

Run:

```bash
python -B experiments/X-105430-critical-sign-rigidity/verify.py \
  experiments/X-105430-critical-sign-rigidity/results/verification.json
```

Expected:

```text
PASS_X_105430_CRITICAL_SIGN_RIGIDITY
7f4cc784c8647c1bfd2e6e1fc6fce8a08cf92214f41f4e6a7aae10df7fc334f8
checks=30
RH_UNPROVEN
```

The replay authenticates:

- the exact positive-residue quartic separator `z^4-z^2+1`;
- a real-rooted quartic with the exact affine-plus-critical Herglotz split;
- the critical atom weight and location in that fixture;
- the exact three-height localizer partial fraction and scale symbol;
- the exact minimal two-height partial fraction;
- two-height residue recovery and affine cancellation;
- positivity of both microscope Fourier polynomials;
- the unit-interval bounds for both scale-flow symbols;
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

The analytic proof obligations remain in `L-105430--L-105439`, `T-105430`,
`T-105440--T-105441`, and their hostile review contracts.
