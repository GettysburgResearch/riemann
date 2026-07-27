# X-12103 — Certified line-mass budgets for positive-anchor responses

## Purpose

A near-null PA-3 or PA-7 quadratic need not become negative to contradict RH.
Under the inherited critical-line response representation, it must be at least
the sum of the contributions from every proof-grade line-zero bin that remains
in the same source measure.

For a frozen polynomial `q`, old nodes `u_i`, and positive anchors `w_j`, the two
response channels are

```text
R0(y) = q(y)^2 /
        [product_i(y+u_i) product_j(y+w_j)]

R1(y) = y q(y)^2 /
        [product_i(y+u_i) product_j(y+w_j)].
```

If a disjoint certified bin contains at least `m` critical-line zeros and exact
interval arithmetic proves `R(y)>=lambda` over that bin, then the complete
response is at least `m*lambda` under RH.

A strict directed comparison

```text
upper(total response) < sum_bin m_bin lambda_bin
```

is a finite contradiction even when the total response remains positive.

## Exact checker

`verify.py` uses only integers and `fractions.Fraction`. It reconstructs:

- exact squared-distance intervals from ordinate bins;
- exact interval Horner evaluation of the frozen witness polynomial;
- fail-closed square lower bounds;
- the positive denominator upper bound;
- square and `y`-times-square leverage;
- multiplicity-weighted leverage sums;
- strict final comparison and deterministic digest.

It requires every bin to carry

```text
gate = CERTIFIED_DISJOINT_CRITICAL_LINE_ZERO_BIN
survives_source_measure = true.
```

The bins must be strictly disjoint. This prevents using a zero after the same
factor was already removed by atomized or selected-factor deflation.

## Synthetic strict contradiction

Use

```text
T=0
old node 1
anchor 2
q(y)=1
one line zero at gamma=1
multiplicity 1.
```

Then `y=1` and

```text
R0(1)=1/[(1+1)(1+2)]=1/6.
```

The supplied total upper bound is `1/10`, so the exact checker returns

```text
CERTIFIED_LINE_MASS_BUDGET_CONTRADICTION.
```

Verification SHA-256:

```text
19a9978824d8bdfb9f6dc6287439e097fe6c7529ab7e39e5ed37cb607d543f60
```

The consistent control changes the total upper bound to `1/4` and returns no
strict contradiction. Its verification SHA-256 is

```text
366218ce7d65eb825d7d69e3a3f52ca17ab987f853ddd040d5239b8dbdc531d0.
```

These are finite synthetic controls, not Riemann-xi results.

## Reproduction

```bash
python experiments/X-12103-anchor-line-mass-budget/verify.py \
  experiments/X-12103-anchor-line-mass-budget/certificates/synthetic-contradiction.json

python experiments/X-12103-anchor-line-mass-budget/verify.py \
  experiments/X-12103-anchor-line-mass-budget/certificates/synthetic-consistent.json

python -m unittest discover \
  -s experiments/X-12103-anchor-line-mass-budget/tests -v
```

The contradiction process exits one, a consistent result exits zero, and a
malformed certificate exits two.

## No-double-counting architectures

Exactly one of the following must be declared:

```text
RAW_UNREMOVED_RESPONSE
SELECTED_FACTOR_RESIDUAL
DIRECTED_ADD_BACK_RESPONSE.
```

- With a raw response, any proof-grade disjoint line-zero bin may be used.
- With selected-factor residuals, only surviving zeros may enter the budget.
- With add-back, every removed contribution is restored before comparison.

A global zero count without localization is insufficient for bin leverage.

## Candidate application

After directed PA-3 or PA-7 data exist:

1. freeze the minimum midpoint H0 and H1 directions to rational vectors;
2. contract the complete total quadratic interval;
3. use proof-grade zero bins not removed from the response;
4. compute every exact leverage lower bound;
5. refine only bins whose polynomial interval crosses zero;
6. rank by `leverage_lower-total_upper`, not midpoint eigenvalue.

This composes with recent saturated-bin, selected-factor, and Padé leverage work,
but no concurrent claim is promoted by this checker.

## Current classification

- `L-12103`: `PROPOSED`.
- X-12103 checker and controls: exact finite rational arithmetic.
- Riemann-data line-mass artifact: none.
- Counterexample status: none.
