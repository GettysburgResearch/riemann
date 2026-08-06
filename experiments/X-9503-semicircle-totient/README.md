# X-9503 — Semicircle totient reconnaissance

This experiment evaluates the finite observable from `T-9501`,

\[
\mathcal V(X)=\frac2X\sum_{n<X}\frac{\varphi(n)}n
\sqrt{1-(n/X)^2},
\]

and records

\[
X^{3/2}\left(\mathcal V(X)-\frac3\pi\right).
\]

## Run

```bash
python scan.py --output results/reconnaissance.regenerated.json
```

The default exact totient sieve reaches `X=2,000,000`.

## Proof boundary

- `phi(n)` is produced by exact integer arithmetic.
- The square roots, `pi`, `math.fsum`, subtraction, and scaling are ordinary
  binary64 operations.
- No directed interval is produced.
- The finite rows do not prove the asymptotic bound in `T-9501`.
- Sign changes are expected and are not counterexamples.

The experiment is useful only for scale reconnaissance, implementation
calibration, and nomination of analytic inequalities.

## Initial observation

Across the committed grid, the unscaled error decreases from about `6.56e-4`
at `X=100` to about `8.77e-11` at `X=2,000,000`. The scaled quantity
`X^(3/2) E(X)` remains order one and changes sign repeatedly. This is consistent
with the critical-line pole exponent, but finite ordinary-floating consistency
is not evidence for RH.

## Next proof-producing step

Build a directed producer at selected exact integer cutoffs using:

1. exact `phi(n)`;
2. outward square-root intervals;
3. exact rational factors `phi(n)/n`;
4. pairwise or compensated interval summation;
5. an exact interval for `3/pi`.

The directed producer can validate individual levels and the zero-expansion
normalization. It cannot by itself certify the global `O_epsilon` theorem.
