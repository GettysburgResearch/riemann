# X-106070 — Scale-matched palette, core-matching, and quartic-payment replay

This replay authenticates the finite algebra retained from
`L-106070--L-106072`.  The first `L-106073/T-106070` closure proposal has been
retracted by `R-106071`; this replay never checked the failed
quartic-to-quadratic adapter.

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

- four deterministic Bertrand-interval prime candidates and retention of three
  primes different from `67`;
- the linear owner-pattern partition and existence of one colour-safe modulus;
- coefficientwise unramifiedness of every fixture `P*c^2` in its block;
- injectivity and two-sided uniqueness of fixed-owner collision lines;
- disjointness of the plus and minus quadratic-root lines;
- representation aggregation by finite-dimensional Cauchy;
- the **quartic** matched-pair product-energy bound;
- the inequality `ell/B^2 <= 256/B` for that quartic owner-pair budget;
- harmonic owner bookkeeping;
- Cauchy across a finite linear source partition;
- the compact-support implication `X/512 < P*B^2 <= X`.

## Binding correction

The replay field historically named

```text
root_residue_occupancy_has_product_energy_bound
```

means only

\[
\sum_{P,Q,d}\|Z_{P,c(d)}\|^2\|Z_{Q,d}\|^2,
\]

a quartic Hilbert--Schmidt shadow.  It does not mean the quadratic character
occupancy

\[
\sum_r\left\|\sum_{Pc^2\equiv r}Z_{P,c}\right\|^2.
\]

`X-106071` is the exact rejection certificate for confusing these objects.

## Not checked

The replay does **not** prove:

- the quadratic owner-residue estimate `HQORO106071`;
- `BPOE103300`;
- the divisor-square estimate or its uniform source composition;
- any analytic Dirichlet-`L` or zeta estimate;
- the fixed Mellin consumer;
- the Riemann Hypothesis.

It remains a valid finite mutation detector for the palette, matching and
quartic-payment mathematics that survived the audit.