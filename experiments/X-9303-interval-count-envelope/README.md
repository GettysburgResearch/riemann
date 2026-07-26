# X-9303 — Overlapping exact interval-count envelopes

This experiment implements the declared-constraint relaxation in L-9304.

Exact total-zero counts in overlapping and asymmetric ordinate intervals are
partitioned into atomic cells. For each symmetric target radius, a finite linear
program asks for the least number of zeros forced inside that radius.

The resulting profile is optimal relative to the supplied interval equations,
not necessarily relative to every structural fact about zeta zeros. Production
adapters should add independently justified symmetry constraints explicitly.

The certificate does not trust an LP solver. Every profile row contains:

- an integer feasible cell-count vector attaining the claimed count;
- an unrestricted rational dual vector proving that no feasible configuration
  can contain fewer zeros.

The verified breakpoint counts are converted into shell increments and used to
deflate direct completed-xi logarithmic-modulus Loewner rows.

## Exact synthetic control

The three exact counts

```text
(-3.1, +1.1): 23
(-1.1, +3.1): 23
(-3.1, +3.1): 24
```

force the atomic counts `(1,22,1)`. The inner dual is `(1,1,-1)`, proving
twenty-two total zeros inside radius `1.1`. This count includes the two zeros
modeled by the off-line factor; omitting them would not be an honest total-zero
synthetic control.

For

```text
H(u)=(u-5)^2 (u+1)^20 (u+9)^2
rows=(3,6), columns=(4,7)
```

the exact checker gives:

```text
raw                         +0.8869072961098987757...
outer-only count deflation  +0.1438052723804491154...
optimal overlap profile     -1.9733926014112437401...
```

Thus arbitrary overlapping counts expose a hidden off-line synthetic factor that
both the raw row and the best single outer-window count leave positive.

## Files

- `verify_interval_count_deflation.py` — integer/Fraction primal-dual and
  direct-xi row checker;
- `certificates/synthetic-overlap-profile.json` — exact control;
- `results/synthetic-summary.json` — compact retained result;
- `tests/test_verify.py` — adversarial mutations.

## Reproduction

```bash
python -m unittest discover -s tests -v
python verify_interval_count_deflation.py \
  certificates/synthetic-overlap-profile.json \
  --output /tmp/x9303-result.json
```

The second command intentionally returns status `1`, because the synthetic
certificate contains a strict negative optimal-profile row.

## Production use

A production adapter should consume exact Turing/argument-principle interval
counts, require proof-grade zero-free evidence for every original and mirrored
endpoint (or use an explicit boundary-atom convention), nominate primal-dual
solutions at every breakpoint radius, and bind one directed completed-xi table.
The current checker verifies arithmetic replay, not external provenance. A
Riemann-xi negative remains pending source-artifact binding, independent count
and xi reproduction, and analytic review.
