# X-91125 — P61 row splice forty-one-divisor core

This exact standard-library replay supports `L-91346`.

It certifies:

- the global lower bounds used to prove that
  \(q_j(Y)=Q_Y(j)/\sqrt Y\) is increasing for every `2 <= j <= 66`;
- all `262,144` squarefree divisor-prefix states of `P_61`;
- the exact uniform post-adjunction floor
  \[
  \delta_{61}
  =\frac{336338530534578047569}
         {224523472888007630167974}>0;
  \]
- the complete list of the forty-one divisors of `P_61` below `67`;
- the Abel-core coefficient dictionary and its total coefficient `delta_61`.

It deliberately does **not** certify the remaining inequality

\[
\mathcal C_j(X)\ge0,
\qquad 2\le j\le66,
\quad X\ge67j,
\]

and it does not prove the Riemann Hypothesis.

## Replay

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```

The script uses `Fraction`, integer square-root enclosures at denominator
`10^70`, and directed atanh-series logarithm intervals. No third-party package
or floating-point sign decision is used.
