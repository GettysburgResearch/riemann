# X-103130 — QPTI semiprime-main regression

This replay supports `L-103121`, `R-103121`, and `T-103130`.

It checks, without network access:

- the exact finite-prime Euler coefficient of the live core `omega(c)>=2`;
- an elementary absolute tail certificate proving that the infinite live-core
  coefficient is positive;
- the exact closed form and negative sign of `Khat_L(1/2)`;
- a literal finite physical current at `X=1,000,000`, using exactly two
  exponent-one owner primes and at least two exponent-two core primes;
- the negative normalized current predicted by the semiprime asymptotic.

The infinite asymptotic uses the classical squarefree-semiprime theorem and
bounded-variation partial summation.  The replay is a deterministic algebraic
and finite-regression companion; it does not replace that proof.

Run:

```text
python -B experiments/X-103130-qpti-semiprime-main/verify.py
python -B -O experiments/X-103130-qpti-semiprime-main/verify.py
```

Expected verdict:

```text
PASS_T103130_QPTI_SEMIPRIME_MAIN_REFUTATION
```

The output explicitly records that RH is not established.
