# X-30901 — First activated-boundary pairing replay

This standard-library checker supports `L-30901`.

Run:

```bash
python3 verify.py
```

The checker treats `log(X)`, `log(2q-1)`, and `log(n)` as formal basis symbols. It verifies term by term that

```text
log(X/(2q-1)) C p(q)-C_X w_X(q)
```

is exactly the paired series

```text
sum_k [
  (2kq-1)^(-1/2) log(min(2kq-1,X)/(2q-1))
 -( (2k+1)q)^(-1/2) log(min((2k+1)q,X)/(2q-1))
].
```

It also checks that the pair intervals are disjoint and that at most one pair crosses the cutoff for each output coordinate.

Retained result:

```text
classification
PASS_EXACT_FIRST_BOUNDARY_PAIRED_LOG_IDENTITY

formal coefficient comparisons  98,740
cutoff-crossing pairs               620
proof digest
0f9cde1c40b3ace7919f8115cacfdd0bc5802215d9bbf12d8f79ff22259ee524
```

The analytic derivative and variation estimates are proved in `L-30901`; this finite replay does not prove `CBVR`, Cycle Debt, or RH.
