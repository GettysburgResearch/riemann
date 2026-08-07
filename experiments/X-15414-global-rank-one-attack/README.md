# X-15414 — Exact synthetic regression for the dyadic global attack

This standard-library `Fraction` checker verifies the finite algebra behind
`T-15412`:

\[
Q_\diamond(\log Y)=\frac{A(Y)-4A(Y/4)}{\sqrt Y}
=Y^{1/2}[C(Y)-C(Y/4)]
\]

and

\[
\int |Q_\diamond(x)|^2dx
=\int |C(Y)-C(Y/4)|^2dY.
\]

The certificate uses synthetic nonnegative rational atom weights. It is not a
prime-power or RH computation.

Replay:

```bash
python verify.py certificates/synthetic.json --output results/synthetic-verification.json
PYTHONPATH=. python -m unittest -v tests/test_verify.py
```

The checker also reconstructs the full stationary autocorrelation kernel of the
one-sided exponential window after multiplication by the prime weights:

\[
K(m,n)=
\begin{cases}
4/\max(m,n)-1/\min(m,n),&\max(m,n)\le4\min(m,n),\\
0,&\text{otherwise}.
\end{cases}
\]

For the retained synthetic nodes its exact LDL pivots are all positive.
