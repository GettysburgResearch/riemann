# Targeted prime-sieve falsification scope

A separate high-precision diagnostic checked the stronger initial-prime statement on:

```text
initial-prime prefixes: r=0,...,6;
component rows:         j=2,...,40;
endpoints:              every integer j<=Y<=400;
activation sides:       Y=(d*m)^- and Y=(d*m)^+
                        for active squarefree d and the first 35 row knots.
```

No negative value was found. A second scan checked every integer full native row for `3<=X<=400` and every `2<=j<X`, again without a negative value.

These are falsification diagnostics only. They do not replace the universal `FRONTIER-CHAIN` proof in `L-94200` and are not promoted to evidence that RH is established.
