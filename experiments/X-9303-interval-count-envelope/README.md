# X-9303 — Overlapping exact interval-count envelopes

This experiment implements L-9304.

Exact total-zero counts in overlapping and asymmetric ordinate intervals are
partitioned into atomic cells. For each symmetric target radius, a finite linear
program asks for the least number of zeros forced inside that radius.

The certificate does not trust an LP solver. Every profile row contains:

- an integer feasible cell-count vector attaining the claimed count;
- an unrestricted rational dual vector proving that no feasible configuration
  can contain fewer zeros.

The verified breakpoint counts are converted into shell increments and used to
deflate direct completed-xi logarithmic-modulus Loewner rows.

## Exact synthetic control

The three exact counts

```text
(-3.1, +1.1): 21
(-1.1, +3.1): 21
(-3.1, +3.1): 22
```

force the atomic counts `(1,20,1)`. The inner dual is `(1,1,-1)`, proving twenty
zeros inside radius `1.1`.

For

```text
H(u)=(u-5)^2 (u+1)^20 (u+9)^2
rows=(3,6), columns=(4,7)
```

the exact checker gives:

```text
raw                         +0.8869072961098987757...
outer-only count deflation  +0.2049935136512567096...
optimal overlap profile     -1.7413309349973961437...
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
counts, mirror all endpoints around the target ordinate, nominate primal-dual
solutions at every breakpoint radius, and bind one directed completed-xi table.
A Riemann-xi negative remains pending independent count and xi reproduction plus
analytic review.
