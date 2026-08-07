# X-26201 — Exact Green–dipole Skorokhod interfaces

This experiment has two deliberately separate layers.

## Exact consumer

`verify.py` uses only the Python standard library, integers, and
`fractions.Fraction`.

For the supplied rational synthetic packet it reconstructs:

- the endpoint-projected prime-power incidence profiles;
- the exact Green Gram and exact linear solve;
- the exact equality state;
- the all-integer Möbius–Poisson charge;
- the negative-excursion layer cake;
- the signed endpoint-dipole recombination;
- clipped lower and upper formal-log certificates;
- prefix and suffix Skorokhod contact debts.

Run:

```bash
python experiments/X-26201-green-dipole-skorokhod/verify.py \
  experiments/X-26201-green-dipole-skorokhod/certificates/synthetic.json
```

The formal logarithms are represented by exact coefficient vectors on
`log p`, one coordinate per prime. No floating logarithm is trusted.

## Tests

```bash
python -m unittest discover \
  -s experiments/X-26201-green-dipole-skorokhod/tests -v
```

Nine tests cover the valid packet and mutations of the endpoint, source,
prime-power manifest, target, expected contact debt, seed sign, fraction
syntax, and schema.

## Reconnaissance

`recon.py` uses NumPy binary64 to nominate the actual parabolic theorem:

```bash
python experiments/X-26201-green-dipole-skorokhod/recon.py \
  --output experiments/X-26201-green-dipole-skorokhod/results/reconnaissance.json
```

That output is explicitly discovery-only. It is not an interval certificate.

## Boundary

The exact consumer verifies finite algebra. It does not prove the
Green–Dipole Sharpness theorem, a cofinal contact bound, the prime-ramp
asymptotic, or RH.
