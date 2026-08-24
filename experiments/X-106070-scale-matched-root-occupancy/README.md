# X-106070 — Scale-matched root-residue occupancy replay

This replay authenticates the finite algebra used by
`L-106070--L-106073` and `T-106070`.

Run from the repository root:

```bash
python experiments/X-106070-scale-matched-root-occupancy/verify.py \
  --output experiments/X-106070-scale-matched-root-occupancy/results/verification.json
```

Expected verdict:

```text
PASS_X_106070_SCALE_MATCHED_ROOT_OCCUPANCY
checks=166834
sha256=67e946c4710d492cae450d7a2581f72e81ab7d8b72c11f5871ad24121212748b
```

## Checked exactly

The standard-library replay checks:

- four deterministic Bertrand-interval prime candidates and retention of three
  primes different from `67`;
- the linear owner-pattern partition and existence of one colour-safe modulus;
- coefficientwise unramifiedness of every fixture `P*c^2` in its block;
- injectivity and two-sided uniqueness of scale-matched collision lines;
- disjointness of the plus and minus quadratic-root lines;
- representation aggregation by finite-dimensional Cauchy;
- the product-energy bound for root-residue occupancy;
- the exact inequality `ell/B^2 <= 256/B` in the owner budget;
- harmonic control of distinct owner products;
- Cauchy across a finite linear source partition;
- the compact-support implication `X/512 < P*B^2 <= X`.

## Not checked

The replay does **not** prove:

- Bertrand's postulate;
- the divisor-square estimate for stopped-Vaughan coefficients;
- the uniform `X^(o(1))` representation bound;
- any analytic Dirichlet-`L` or zeta estimate;
- the fixed Mellin consumer;
- the Riemann Hypothesis.

Those are mathematical inputs or consequences cited in the proof packet.  The
replay is an exact finite mutation detector, not an independent proof of the
extraordinary conclusion.