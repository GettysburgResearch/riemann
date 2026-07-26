# X-9312 — Exact Padé residual-mass leverage budget

L-9314 identifies each distance from a one-node Padé boundary as an exact
positive Christoffel-type integral. Therefore every proof-grade positive piece
of the residual RH measure consumes a rigorously lower-bounded portion of the
total Padé gap.

X-9312 verifies the finite contradiction

```text
upper(total directed Padé gap)
<
lower(certified residual-submeasure contribution).
```

Such an inequality is impossible under RH.

## Inputs

A certificate contains:

- `side`: `lower` or `upper`;
- exact old nodes `u_j`;
- the exact added node `w`;
- an optional certified support edge `A`;
- a rational endpoint polynomial `q` with `q(-w)=1`;
- a directed interval for the corresponding total Padé gap;
- proof-gated residual-mass records.

Two residual record kinds are supported.

### Atomic zero bin

```json
{
  "kind": "atom",
  "y": {"lower": "L", "upper": "U"},
  "multiplicity": 1,
  "gate": {"status": "CERTIFIED_CRITICAL_LINE_ZERO_LOWER_BOUND"}
}
```

Atomic bins must be pairwise disjoint. They may only describe line zeros not
already removed from the residual table.

### Far-endpoint residual segment

If a zero with squared distance `y in [L,U]` was safely deflated at `B>=U`, the
remaining factor contains common positive Lebesgue measure on `[U,B]`.

```json
{
  "kind": "segment",
  "y": {"lower": "U", "upper": "B"},
  "multiplicity": 1,
  "gate": {"status": "CERTIFIED_FAR_ENDPOINT_RESIDUAL_SEGMENT"}
}
```

The checker lower-bounds this contribution by

```text
multiplicity * (B-U) * inf_{s in [U,B]} leverage(s).
```

Segment records may overlap when they correspond to distinct proof-bound source
factors; their positive measures add by multiplicity.

## Kernels

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
2. proof-gate and anti-double-counting checks;
3. interval Horner evaluation of `q`;
4. exact interval squaring and rational-function division;
5. exact atomic or length-weighted segment summation;
6. strict final comparison.

No optimizer, floating logarithm, eigenvalue routine, or special-function call
enters the checker.

## Verdicts

```text
CERTIFIED_NEGATIVE_PADE_LINE_MASS_BUDGET
CERTIFIED_CONSISTENT_PADE_LINE_MASS_BUDGET
UNRESOLVED_PADE_LINE_MASS_BUDGET
```

The historical verdict names are retained for schema compatibility, but the
proof object now covers generic certified residual mass, not only atoms.

The output ranks items by contribution uncertainty. That ranking tells the
saturated sign-chain or factor-removal route which records are most valuable to
refine for the active witness.

## Synthetic controls

The controls use no old nodes, `w=1`, and `q(y)=1`.

For a unit atom at `y=1`, the lower leverage is exactly `1/2`.

- total gap `3/4`: consistent;
- fake total gap `2/5`: strict contradiction.

For the upper kernel with `A=0`, a unit atom at `y=3` contributes `3/4`; a fake
total upper gap `7/10` gives a strict contradiction.

A segment `[1,3]` has length 2 and leverage at least `1/4`, so its certified
contribution is at least `1/2`; the same fake gap `2/5` is contradictory.

These are algebraic controls only, not Riemann-ξ candidates.

## Reproduction

```bash
cd experiments/X-9312-pade-leverage-budget
python -m unittest discover -s tests -v
python verify_leverage_budget.py certificates/synthetic-consistent.json
python verify_leverage_budget.py certificates/synthetic-lower-negative.json
python verify_leverage_budget.py certificates/synthetic-upper-negative.json
```

A Riemann-ξ nomination requires a source-bound directed Padé gap and endpoint
polynomial, a globally compatible proof-gated residual submeasure, and
independent analytic/numerical reproduction.
