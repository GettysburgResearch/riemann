# X-23701 — Carry Green exact replay and floating phase-frame reconnaissance

## Exact checker

Run:

```bash
python verify.py
```

Arithmetic class: `EXACT_RATIONAL_AND_INTEGER`.

It checks:

- the carry-floor identity;
- the affine Möbius Green kernel;
- the cumulative carry derivative;
- Green-tail inversion on independent rational targets;
- the formal logarithmic-binomial increment;
- a rational interval certificate for the outer derivative gate;
- deliberate mutations.

It does **not** test positive phase renewal, asymptotics, a prime estimate, the
square-screw normalization, Landau's theorem, or RH.

## Floating reconnaissance

Run, for example:

```bash
python recon.py 1000 64
```

This requires NumPy and SciPy/HiGHS. It constructs the exact finite outer-band
dictionary in ordinary double precision and solves the finite minorant LP.

Arithmetic class: `FLOATING_RECONNAISSANCE`.

A successful solver return is not a certificate. Reported ratios compare the LP
objective with the exact finite von-Mangoldt ramp evaluated in floating point;
they do not prove the asymptotic lower bound.
