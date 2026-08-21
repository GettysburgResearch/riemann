# X-91129 — Direct Euler splice composition regression

This small exact replay checks the algebra used by `L-91351/T-91304`:

```text
parent row = p^(-1/2) child row + arithmetic residual row;
parent target and score have the same split;
residual score minus target has coefficient 58/2075;
substochastic branch homogeneity charges bounded debt once.
```

It does not replace the analytic/directed inherited-row certificate
`L-91346/X-91125`.

Replay:

```bash
python3 verify.py
```

Expected verdict:

```text
PASS_DIRECT_EULER_SPLICE_COMPOSITION
```
