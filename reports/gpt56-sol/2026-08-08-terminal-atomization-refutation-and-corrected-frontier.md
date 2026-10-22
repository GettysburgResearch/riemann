# Terminal atomization refutation and corrected full-problem frontier

## Executive result

The terminal adjacent-commutator algebra of PR #304 is exact, but its
load-bearing norm estimate is false for the actual positive stopped-power
critical boundary.

For every `X>=192`, the complete initial ordinary divisor source satisfies

```text
||Sigma_X||_at >= X/750.
```

Therefore the implication

```text
finite Euler boundary
-> polylog ordinary atomic norm
-> polylog terminal commutator debt
```

cannot be used to prove Cycle Debt or RH.

## Why the error was plausible

The divided shifted fibers

```text
(2kq-1)^(-s)/(2k),
((2k+1)q)^(-s)/(2k+1)
```

have critical square-root capacity cost `q^(-1/2)k^(-1)` and hence a logarithmic
sum. The raw boundary exported by PR #286 instead contains

```text
(2kq-1)^(-s),
((2k+1)q)^(-s)
```

before an additional source identity is supplied. The missing divisors are
exactly the quantitative difference between logarithmic and macroscopic cost.

## Exact top-band obstruction

For one stopped endpoint `Y` and every

```text
Y/3 < m <= Y/2,
m >=64,
```

the unique strict-half ordinary source has

```text
sqrt(m) sigma_Y(m) < -1/5.
```

The positive endpoint layer cake retains the same sign on

```text
X/3 < m <=2X/5
```

and contributes at least `1/25` of atomic norm per source node. There are at
least `X/30` such nodes.

This is a source-level counterfamily. It is unaffected by Euler order, Peano
notation, or recombination of repeated labels.

## What survives

```text
adjacent central-tree commutator            exact
one divisor atom carry image                exact
24 sqrt(m) capacity upper bound              exact
paired divided-fiber logarithmic estimate   exact at that source type
```

The error is the identification of the complete raw boundary with a
polylogarithmic superposition of those divided fibers.

## Corrected full-problem frontier

The exact obstruction does not prove optimized Cycle Debt is large. It proves
that cancellation must occur **before ordinary divisor-source atomization**.
A serious continuation has three viable coordinates:

1. **relative source-to-existing-flow:** exhibit every incoming central capacity
   and perform the central/sibling switch without converting the residual to
   independent atoms;
2. **cycle-optimized raw boundary:** construct the complete boundary flow first,
   then minimize its negative capacity in the Pascal cycle quotient;
3. **reciprocal-eta compression:** apply the all-stage eta source before taking
   an absolute norm, retaining the exact Mersenne exceptional ledger.

The previous transition-band language is useful only if one of these maps is
actually emitted. Cone membership without coordinates is not a proof.

## Status

```text
PR #304 terminal atomic-norm proof       REJECTED
structured boundary Cycle Debt           OPEN / RH-BEARING
Riemann Hypothesis                       UNPROVED
```
