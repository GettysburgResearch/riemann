# T-98000 integration handoff

## Publication

```text
branch: research/gpt56-pro/98000-zero-marginal-lorenz-collapse
base:   PR #596 @ 40bfd7e70521f4205e95d3960812a6cef6073c05
status: successor research packet; RH unproved
```

## Controlling result

For every sufficiently large real endpoint,

\[
CPSL67
\Longleftrightarrow
GTC67\wedge GPC67.
\]

The proof has three new inputs:

1. `Q_*(Y)/T(Y)` is strictly increasing from zero to six;
2. Lorenz atoms are therefore ordered by increasing source index;
3. the zero-scalar squarefree shell forces the odd target beyond all
   positive-scalar even capacity by a positive `sqrt(X)` main term.

## Review order

```text
claims/lemmas/L-98000-unsieved-scalar-target-ratio-is-ordered.md
claims/lemmas/L-98001-canonical-index-order-and-one-switch-lorenz-envelope.md
claims/lemmas/L-98002-zero-marginal-squarefree-shell-asymptotic.md
claims/lemmas/L-98003-native-target-mellin-landau-criterion.md
claims/theorems/T-98000-eventual-lorenz-collapse-to-two-zero-hinges.md
claims/methodology/M-98000-zero-marginal-closure-protocol.md
experiments/X-98000-zero-marginal-lorenz/
reports/gpt56-pro/2026-08-18-zero-marginal-lorenz-collapse.md
```

## First hostile checks

- Re-derive the derivative numerator and its concavity on every activation cell.
- Verify the integral bounds producing constants `c,d,C,K` and the tail start
  at `Y=8`.
- Check that source coefficients are absorbed into both target and scalar
  coordinates identically.
- Confirm `Q_*(Y)>0` exactly for `Y>2`, so the scalar-active cutoff is `k<X/2`.
- Re-derive the parity-indicator shell identity and the coefficient
  `(3/pi^2)(4log2+3sqrt2-6)`.
- Check real-endpoint boundary conventions at `k=X/2` contribute only a harmless
  single zero-scalar atom.
- Do not infer either `GTC67` or `GPC67` from the collapse theorem.

## Next mathematical target

Attack `GPC67` directly through the exact largest-prime identity of PR #590 and
the minimal root budget of PR #594. The Lorenz all-threshold cone is no longer
the minimal theorem required for RH.