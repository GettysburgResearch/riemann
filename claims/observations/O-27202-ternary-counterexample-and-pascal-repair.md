# O-27202 — What the ternary counterexample says about the surviving MFT cone

Claim ID: `O-27202`  
Status: **RESEARCH SYNTHESIS AFTER EXACT COUNTEREXAMPLE**

The pure ternary producer fails first, in the directed `X=10^7` computation, at

```text
n=63   A_X(n) < -0.00157404973202414
n=71   A_X(n) < -0.0009646886...
n=95   A_X(n) < -0.0009217101...
n=319  A_X(n) < -0.0000256818...
```

Only the first value is currently retained as a proof-grade MPFR certificate.
The pattern is informative:

1. the failure occurs deep inside the previously open inner fifth;
2. it is not an endpoint-rounding fluctuation;
3. one fixed split rule is too rigid, even though it survives to very large
   finite endpoints;
4. the complete MFT LP can still be feasible because Pascal four-cycles permit
   redistribution among split rows without changing any carry column or the
   binomial objective.

The preferred continuation is therefore not another stationary split rule. It
is a **localized Pascal repair** of the exact signed ternary flow:

```text
signed ternary equality flow
-> identify negative parent coefficients
-> add zero-divergence Pascal four-cycles
-> preserve every carry column and entropy exactly
-> obtain a nonnegative balanced flow with controlled support.
```

The exact counterexample becomes a mandatory mutation for any proposed repair.
A schema that cannot make the `X=10^7, n=63` coefficient nonnegative without
altering the target columns is rejected immediately.
