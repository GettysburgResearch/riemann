# X-28005 — Binary–ternary pole-preserving prime annulus

Run

```bash
python experiments/X-28005-binary-ternary-prime-annulus/verify.py
```

The checker uses exact rational arithmetic and formal prime-logarithm vectors.

It verifies:

```text
inverse convolution identities          160
finite floor profiles                    161
average zero rows                        155
scaled source wavelets                 1,690
factor-18 vanishing rows                 221
generalized-prime identities             160
top-six annulus identities                94
continuum/discrete boundary identities    95
discrete carry-source identities          95
```

Retained digest, computed before inserting the digest field:

```text
5a2dd4bc22d4aa899f88fb59a1426f1cdfdf957c1bc233ed507530e8edf87bbd
```

## Assurance boundary

The replay proves finite source, carry, and commutator algebra. It does not
prove:

```text
BT-PAE;
the subexponential prime-annulus energy;
a strict independent-frequency transition recurrence;
the Riemann Hypothesis.
```
