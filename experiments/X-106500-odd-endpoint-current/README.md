# X-106500 — Odd-endpoint current hierarchy replay

Run:

```bash
python -B experiments/X-106500-odd-endpoint-current/verify.py
```

Expected classification:

```text
PASS_T106500_ODD_ENDPOINT_CURRENT_HIERARCHY
```

The replay checks exactly:

- `(v-u)(v^K-u^K)>=0` for odd `K` on a signed integer grid;
- the complete sum/difference binomial decomposition through `K=15`;
- positivity of the first eight formal mixed-current chaoses;
- the `K=5` coefficient vector `(5,10,1)/16`;
- the fixed conclusion allowance `997/1000-9/10=97/1000`.

It does not evaluate Xi, control the variable endpoint all-pass phase, prove
`FIFTHPHASE106500`, establish ninety percent, density one, or RH.  The script
writes its result and proof-object digest to `results/verification.json`.
