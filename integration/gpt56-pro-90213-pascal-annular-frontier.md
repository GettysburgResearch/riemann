# Integration handoff — global Pascal reward and annular filter frontier

Branch: `research/gpt56-pro/90102-liouville-bernstein-extremality`  
PR: #356  
Status: exact theorem packet; finite replay; RH unproved

## Import order

1. `claims/lemmas/L-90213-pascal-boundary-reward-extremality.md`
2. `claims/lemmas/L-90214-global-uniform-pascal-reward-extremality.md`
3. `claims/lemmas/L-90215-two-low-row-scalar-has-an-exact-positive-divisor-renewal.md`
4. `claims/lemmas/L-90216-uniform-pascal-dyadic-filter-cone.md`
5. `claims/lemmas/L-90218-positive-pascal-filter-cannot-have-a-double-neutral-root.md`
6. `claims/lemmas/L-90219-double-neutral-filters-have-unavoidable-pascal-debt.md`
7. `claims/lemmas/L-90217-factor64-compact-signed-pascal-reward.md`
8. `experiments/X-90206-pascal-boundary-reward-extremality/`
9. `experiments/X-90207-uniform-pascal-dyadic-filter-cone/`
10. `reports/gpt56-pro/2026-08-10-pascal-annular-all-out-attack.md`

## Exact status changes

```text
canonical 15:4 reward                         local identity -> global extremizer
higher positive Pascal boundary states        cannot improve 15:4
ordered balanced constant-tail reward         sharp interval [0,2]
low-row scalar geometry                       positive forcing + one Mobius inversion
finite positive Pascal dyadic filters         complete linear cone
positive Pascal double-neutral annulus         impossible for every degree
signed double-neutral Pascal reward            unavoidable quantitative debt
improved factor-64 Pascal negativity           exactly states 13..63
factor-64/Pascal repair                        one 51-state payment theorem
RH                                             UNPROVED
```

## Cross-PR imports

- PR #329 / #335: uniform Pascal kernel, hitting law, SHARP occupation coordinates.
- PR #352: improved factor-64 polynomial and annular RH criterion.
- PR #356 earlier files: frozen GFEP/BTF refutation and resonance-free Pascal pivot.

The factor-64 criterion remains valid at its claimed conditional/equivalent scope. This packet proves only that coordinatewise-positive uniform-Pascal reward cannot realize a double-neutral annular filter, and localizes the signed failure.

## Validation

```text
python experiments/X-90206-pascal-boundary-reward-extremality/verify.py
PASS_X_90206_PASCAL_BOUNDARY_REWARD_EXTREMALITY

python experiments/X-90207-uniform-pascal-dyadic-filter-cone/verify.py
PASS_X_90207_UNIFORM_PASCAL_DYADIC_FILTER_CONE
```

GitHub Actions are not configured on this stack. Independent mathematical review remains required.

## Preferred next theorem

For the critical uniform-Pascal occupation `M`, prove

\[
\sum_{m=13}^{63}[-d_{64}(m)]M(m)
\le
\sum_{m=2}^{12}d_{64}(m)M(m)
+39(\sqrt2-1)
\sum_{m\ge64}\frac{M(m)}{m(m-1)}.
\]

This is the exact factor-64/Pascal bridge. A generic PSD, spectral-gap, or filter-search substitute is not sufficient.
