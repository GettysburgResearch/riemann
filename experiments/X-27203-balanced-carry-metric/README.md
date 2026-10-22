# X-27203 — Exact balanced-carry metric regression

The standard-library checker verifies the finite algebra used by `L-27203`:

- `kappa(n,j)=D(n)-D(j)-D(n-j)`;
- high-column carries equal one on every balanced row;
- packet Tonelli identity `sum d*kappa=sum_q v(q)` for exact rational flows;
- the old upper-capacity inference is rejected by a typed logic mutation.

The analytic `O(sqrt(n))` divisor estimate and Stirling estimate are proved in
the claim file, not by this checker.
