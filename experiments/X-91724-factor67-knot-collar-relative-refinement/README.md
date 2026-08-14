# X-91724 — Factor-67 activation-knot collar and relative-refinement replay

Run:

```bash
python3 verify.py
python3 -m py_compile verify.py
sha256sum -c SHA256SUMS
```

Expected:

```text
PASS_FACTOR67_KNOT_COLLAR_RELATIVE_REFINEMENT
```

The checker uses exact `Fraction` arithmetic.  It verifies:

```text
the raw Lipschitz/native-relative counterexample;
the endpoint knot-collar mass bound from density <183/50;
the positive barycentric interpolation error L_eta h/(2m_eta);
the 10152||C|| reserve-payment schedule;
vanishing score-collar schedules;
one-use endpoint ownership;
three hostile mutations.
```

It deliberately does not replay the imported factor-67 density, finite
activation geometry, Hall amplification, correction-map norm, all-column
reserve, direct-integral contraction, terminal, common-port or endpoint
consumer theorems.
