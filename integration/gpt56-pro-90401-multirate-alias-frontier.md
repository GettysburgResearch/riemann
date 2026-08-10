# Integration handoff — multirate alias frontier after Claude zeta-23

Branch target: `research/gpt56-pro/90401-multirate-alias-signature`  
Base: PR #358 branch `research/gpt56-pro/90301-claude-signature-moment`  
Status: proposed mathematics; independent review required; RH unproved

## Load-bearing files

```text
claims/lemmas/L-90401-multirate-no-alias-gabor-collapse.md
claims/lemmas/L-90402-exact-alias-polyphase-decomposition.md
claims/lemmas/L-90403-subpolynomial-prime-resonant-alias-diagonal-is-lower-order.md
claims/observations/O-90401-prime-resonant-alias-frontier-after-claude.md
experiments/X-90401-multirate-alias/
reports/gpt56-pro/2026-08-10-multirate-alias-attack-after-claude.md
```

## Exact contribution

- Extends the co-lattice collapse to arbitrary finite no-alias rates, offsets, and incommensurable lattices.
- Derives the exact alias/polyphase kernel when the dual period is shorter than the support.
- Identifies prime-power phase locking as the only new stationary arithmetic degree of freedom.
- Proves exact resonant diagonals from fixed or subpolynomial prime banks are lower order.

## Review gate

Before promotion, a reviewer must check:

1. Fourier/Poisson normalizations and conjugations;
2. the no-alias boundary case `P=L`;
3. trace collapse for the union Gram matrix, including cross-window terms;
4. period-average formulas;
5. the Chebyshev–Mertens comparison in `L-90403`;
6. every scope statement distinguishing resonant diagonal from unbounded cross terms.

## Honest next burden

The first surviving extension is a growing prime-resonant alias bank with `Y=X^theta`, or a nonstationary/multi-statistic certificate. Neither is solved here. The separate full-RH Q4 route remains blocked at QIDR’s coefficient-one source/state recurrence, not at local negative-mass control.
