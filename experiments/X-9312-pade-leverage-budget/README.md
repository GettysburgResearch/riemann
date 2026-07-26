# X-9312 — Exact Padé line-mass leverage budget

L-9314 identifies each distance from a one-node Padé boundary as an exact
positive Christoffel-type integral.  Therefore every proof-grade critical-line
zero bin consumes a nonnegative, rigorously lower-bounded portion of the total
Padé gap.

X-9312 verifies the finite contradiction

```text
upper(total directed Padé gap)
<
sum certified multiplicity * lower(bin leverage).
```

Such an inequality is impossible under RH.

## Inputs

A certificate contains:

- `side`: `lower` or `upper`;
- exact old nodes `u_j`;
- the exact added node `w`;
- optional certified support edge `A`;
- a rational endpoint polynomial `q` with `q(-w)=1`;
- a directed interval for the corresponding total Padé gap;
- pairwise-disjoint proof-gated zero bins in the squared-distance variable.

The lower-bound kernel is

```text
q(y)^2 / ((y+w) product_j (y+u_j)).
```

The support-upper kernel is

```text
(y-A) q(y)^2 /
((w+A)(y+w) product_j (y+u_j)).
```

## Exact trust boundary

The checker uses only Python integers and `fractions.Fraction`:

1. exact verification of `q(-w)=1`;
2. strict pairwise-disjointness of the zero bins;
3. interval Horner evaluation of `q`;
4. exact interval squaring and rational-function division;
5. exact multiplicity-weighted summation;
6. strict final comparison.

No optimizer, floating logarithm, eigenvalue routine, or special-function call
enters the checker.

## Verdicts

```text
CERTIFIED_NEGATIVE_PADE_LINE_MASS_BUDGET
CERTIFIED_CONSISTENT_PADE_LINE_MASS_BUDGET
UNRESOLVED_PADE_LINE_MASS_BUDGET
```

The output also ranks bins by multiplicity-weighted leverage uncertainty.  That
ranking tells the saturated sign-chain route which zero bins are most valuable
to refine for the active witness.

## Synthetic controls

The controls use no old nodes, `w=1`, and `q(y)=1`.

For a unit atom at `y=1`, the lower leverage is exactly `1/2`.

- total gap `3/4`: consistent;
- fake total gap `2/5`: strict contradiction.

For the upper kernel with `A=0`, a unit atom at `y=3` contributes `3/4`.
A fake total upper gap `7/10` gives a strict contradiction.

These are algebraic controls only, not Riemann-ξ candidates.

## Reproduction

```bash
cd experiments/X-9312-pade-leverage-budget
python -m unittest discover -s tests -v
python verify_leverage_budget.py certificates/synthetic-consistent.json
python verify_leverage_budget.py certificates/synthetic-lower-negative.json
python verify_leverage_budget.py certificates/synthetic-upper-negative.json
```

A Riemann-ξ nomination requires a source-bound directed Padé gap, a source-bound
rational endpoint polynomial, proof-grade nonoverlapping zero bins, and
independent analytic/numerical reproduction.
