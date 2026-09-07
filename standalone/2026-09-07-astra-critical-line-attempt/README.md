# Near-linear quadratic bound: direct critical-line attempt

**The requested bound and RH are not proved.** This packet records a direct
attempt to prove the actual bound from the preceding balanced-hyperbola
packet, rather than asserting that another RH-equivalent condition is solved.
It is author-submitted component mathematics requiring independent review.

Read [PROOF.md](PROOF.md), especially sections 2--4 and the stopping point in
section 6. The frozen parent is PR #805 at
`ccd0a80dbd9844d06ccd6331a15b085b9c9afa41`.

The proved component statements are:

- An absolutely convergent critical-line integral for the complete actual
  quadratic form. The contour shift is unconditional because the balanced
  Dirichlet polynomial removes the pole at 1. It does not bound that integral.
- A uniform O(Y) bound for its entire frequency tail beyond Y^(4/3). The
  remaining signed integral is unestimated at the required scale.
- An actual-source upper bound of classical Mertens strength,
  O(Y^2 exp(-c (log Y)^(3/5) (log log Y)^(-1/5))). This is explicitly an
  application of imported established theory, not a new fixed-power saving.
- Either one-sided near-linear inequality on the predetermined grid would
  suffice, by a proved Landau-Mellin argument. Neither sign bound is supplied.

The contour contains a square, not a modulus square. Absolute-value estimates
introduce an unproved weighted moment; generic diagonal control fails on the
parent's balanced counterexamples. Those examples are not the Mobius vector.

## Bounded replay

Python 3.10 or newer, standard library only, from this directory:

```bash
python3 check.py
python3 -O check.py
python3 check.py --self-test
python3 -O check.py --self-test
```

The parent proof must be present at the unchanged sibling path recorded in
SOURCE_LOCK.json. The checker authenticates it by Git blob, byte length and
SHA-256, but executes no parent code. It reconstructs finite integer/Fraction
fixtures and rejects corrupted inventories and results. `--emit FILE` is
explicitly a generation mode, not a manifest-validated acceptance command.

The checker DOES NOT establish any analytic integral estimate, replay external
zero data, validate the imported Mertens theorem, or prove RH. See
[VALIDATION.md](VALIDATION.md) for exact execution scope and unperformed checks.
