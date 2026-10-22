# X-30201 — Source-flow eta–Pascal exact regression

This proof object separates three statements which had previously been grouped
together:

1. the central/sibling carry **difference** is exact;
2. the corresponding edge replacement is exact **relative to an incoming
   central edge**;
3. the replacement is **not** a standalone realization of the formal paired
   divisor source.

Run:

```bash
python experiments/X-30201-source-flow-manifest/verify.py
```

The standard-library checker verifies:

```text
sibling carry identity                       28,920 cases
standalone source/edge mismatch                 120 general witnesses
relative replacement identity                28,920 cases
adjacent-tree divisor commutators              3,320 cases
paired source and Pascal-cycle identities      4,880 cases
shifted residual Hausdorff differences        36,936 cases
finite cutoff start-parity ledger             45,149 cases
```

The first eta pair is retained as the minimal review witness:

```text
formal source columns q=2,3,4       1/2, -1/3, 0
constructed nonnegative edge load   1/3,  1/6, 1/2
```

The checker uses only integers and `fractions.Fraction`. The Hausdorff scan is
finite regression supporting the positive-measure proof in `L-30202`; it is not
the proof of that all-order theorem.

## Scope firewall

This experiment does **not** prove:

```text
SFC;
an all-generation source-to-flow manifest;
DCD contraction;
Cycle Debt;
RH.
```

Its purpose is to reject a wrong source/edge type conversion while preserving
the valid relative Pascal algebra.