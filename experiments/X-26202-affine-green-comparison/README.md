# X-26202 — Exact affine Green / Skorokhod comparison replay

This standard-library checker authenticates the finite algebra of `L-26204` on
one rational control.

Run:

```bash
python experiments/X-26202-affine-green-comparison/verify.py
```

It verifies:

- a signed equality state and its prime-power response;
- the prime oversupport affine lift;
- preservation of every old prime-power row;
- the single new boundary charge;
- formal von-Mangoldt/objective identities using prime-exponent vectors;
- prefix Skorokhod nonnegativity;
- the exact prefix residual and contact-debt formulas;
- the inequalities `max negative excursion <= boundary charge` and
  `prefix contact mass <= boundary charge`;
- four fail-closed mutations.

Retained result:

```text
classification                 EXACT_AFFINE_GREEN_SKOROKHOD_COMPARISON
X                              12
oversupport prime              13
boundary charge                2
maximum negative excursion     5/8
prefix contact mass            5/8
old prime-power rows preserved 8
mutation tests                 4/4 PASS
proof SHA-256
92df3a4acca946b1ccb0e4ac3b036a7e2fb8a5ed3618074a5b90338a053f1048
```

Arithmetic class:

```text
integers + fractions.Fraction + formal prime-log coefficient vectors
```

The replay proves no cofinal affine-charge estimate, prime-ramp asymptotic, or
Riemann Hypothesis conclusion.
