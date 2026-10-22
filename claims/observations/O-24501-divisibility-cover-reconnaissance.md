# O-24501 — Divisibility-cover reconnaissance, now superseded

Claim ID: `O-24501`  
Status: `SUPERSEDED / ASYMPTOTIC INTERPRETATION REFUTED BY R-24501`  
Scope: historical floating reconnaissance only  
Issue: #245

The first continuation tested the monotone cover from the original `L-24502`: find nonnegative atoms `alpha_m` satisfying

\[
\sum_{kq\le X}\alpha_{kq}\ge e_X(q),
\qquad
\sum_{t=m}^X\alpha_t\le b_X^{(0)}(m),
\]

while minimizing

\[
\sum_m\alpha_m\log m.
\]

Ordinary floating LP runs returned approximate costs

```text
X=100      0.2621
X=200      0.9062
X=500      2.5954
X=800      3.9606
X=1000     4.7683
X=1500     6.5142
```

and were feasible with the tested tail-capacity constraints. These values were always labeled reconnaissance.

## Exact later disposition

`R-24501` proves that this apparent trend is pre-asymptotic. For all sufficiently large `X`, every nonnegative cover satisfying the prime-power constraints has weighted cost

\[
\gg\sqrt X,
\]

because a fixed band of large primes has positive seed excess and pairwise disjoint multiple sets below `X`.

Therefore:

```text
polylogarithmic Divisibility Cover    REJECTED
floating small-X trend                SUPERSEDED
exact identities L-24502.8/.9         RETAINED
signed adjacent transport             NOT REFUTED
```

The old numbers are retained only as a warning: a finite LP ladder can strongly suggest the wrong asymptotic regime.
