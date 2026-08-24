# Exact function-field detector pilot

Status: exact finite exploration for L-family programmes #737 and #741.

Scope: odd prime fields, elementary polynomial arithmetic, and a frozen exhaustive
family of the 100 monic squarefree cubic conductors over `F_5[T]`. Nothing here
implies RH or GRH over the integers.

## Files

- `pilot.py` implements dependency-free polynomial arithmetic, factorization,
  quadratic symbols, polynomial Moebius values, `L` coefficients, direct and
  formal reciprocal coefficients, and exact critical normalization in
  `Q(sqrt(q))`.
- `fixtures.json` is the compact frozen output for the cubic `F_5[T]` family.
- `REPORT.md` states the identities, finite theorem, counterexamples, and scope
  firewalls.
- `tests/test_function_field.py` independently exercises the arithmetic and
  replays the frozen fixture.

## Replay

From the repository root:

```text
python research/l-families/atlas/function_field/pilot.py \
  --check research/l-families/atlas/function_field/fixtures.json
python tests/test_function_field.py
```

The producer refuses any one monic-polynomial enumeration larger than 100,000
objects. The frozen run only uses degrees at most three.

## Scientific boundary

The fixture's signed statistic is the explicitly defined normalized product
`H_D(1) H_D(2)`. It is a deliberately minimal cross-degree probe. It is not the
repository's same-kernel `XD`, oriented `HCNC`, or physical-occupancy predicate.
Its mixed signs establish only that Frobenius root modulus by itself does not
force this toy signed cross-degree statistic memberwise.
