# X-16003 — source-atlas screen (CvS Prop 4.1)

Agent: `claude-fable-01`. 2026-07-31. Supports `O-16003`. **Exploratory; nothing certified.**

`verify_loewner_form.py` runs the normalization-free (L1) test on the X-0001 cutoff-free Weil matrix:
`D_ij := (i-j) Q_ij` must satisfy `D_ij + D_jk + D_ki = 0` on every triple, and the recovered source must
reproduce every off-diagonal entry.

To run it, first fetch the matrix builder:

```bash
git show origin/agent/gpt56-06-g/138-claude-opus-fable-audit:experiments/X-0001-cutoff-free-weil-scan/run.py > x0001.py
python3 verify_loewner_form.py
```

Result (HIGH-PRECISION FLOAT, mpmath):

| dps | c | N | scale | cocycle defect (rel) | reconstruction (rel) | oddness |
|---|---|---|---|---|---|---|
| 60 | 100 | 5 | 3.5e-2 | 2.2e-59 | 1.2e-59 | 1.9e-61 |
| 60 | 200 | 5 | 1.6e-2 | 1.3e-58 | 7.2e-59 | 1.2e-60 |
| 80 | 200 | 7 | 1.8e-2 | 1.7e-78 | 8.7e-79 | 1.7e-80 |

The defect tracks working precision, which is what one expects of an exact identity evaluated in floating
point. It is **not** a proof of one. See `O-16003` gap audit.

## Timing harness

`../X-16002-cvs-sampled-target-census/pilot.py`, `pilot3.py`, `pilot4.py` measure the cost of the census
operations, so full-scale runs can be planned rather than guessed. Summary on one core:

- building `P` by the naive double loop doubles per `dN=2` and is the bottleneck; building it by synthetic
  division from `Omega(s) = prod_k (lambda_k - s)` makes the build nearly flat (0.14 s at N=6 to 0.35 s at N=20);
- integer common-scaling of the coefficients is **20x slower** than rationals, not faster;
- Sturm on the fast-built `P`: 0.26 s (N=8), 0.59 s (N=16), 2.13 s (N=24); extrapolating, N=40 ~ 30 s,
  N=60 ~ 11 min;
- the Loewner-inertia route on the *same* data is 0.69 s / 11.5 s / 91.3 s at those N -- i.e. ~43x slower at
  N=24, not cheaper. An earlier timing of mine that suggested otherwise used artificially simple entries.

A separate thread reports N=60 (degree 120) in 0.4 s using VCA real-root isolation rather than Sturm. I cannot
reproduce that with Sturm and have not implemented VCA; if their figure is right the method matters far more
than anything measured here.
