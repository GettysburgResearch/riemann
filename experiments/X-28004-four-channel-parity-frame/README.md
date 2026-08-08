# X-28004 — Four-channel binary–ternary parity frame

Run

```bash
python experiments/X-28004-four-channel-parity-frame/verify.py
```

The checker works exactly in

```text
Q(sqrt(2),sqrt(3))[z,w]
```

using only `fractions.Fraction` and a four-coordinate algebraic-number class.

It verifies:

```text
one-variable Bézout identities    2
tensor Bézout identity            exact constant polynomial
Hadamard norm identities          100 synthetic vector systems
forcing twist-sum identities      500 integer valuation patterns
```

Retained digest, computed before inserting the digest field:

```text
b339810189bb94626524b9da21ef8e787cd05d38df517f81a86a51866ea6a617
```

## Assurance boundary

The replay proves finite polynomial, parity, and norm algebra. It does not prove:

```text
the four-channel physical upper estimate;
preservation of a strict reserve after collars;
BTEBC;
the Riemann Hypothesis.
```
