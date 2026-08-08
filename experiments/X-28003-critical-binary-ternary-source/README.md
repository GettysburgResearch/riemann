# X-28003 — Critical binary–ternary source exact replay

Run

```bash
python experiments/X-28003-critical-binary-ternary-source/verify.py
```

The checker works in the exact coefficient ring

```text
Q(sqrt(2),sqrt(3))
```

using four rational coordinates and no external library.

It verifies:

```text
finite floor support                 {1,2,3,4,6,9,12,18,36}
inverse convolution identities       200
floor-profile identities              201
scaled carry-wavelet identities       780
factor-108 vanishing instances         22
generalized-prime formal identities   150
```

Retained digest, computed before inserting the digest field:

```text
69bdd744471b399457febfe9e8929af6cc577f3c5b0e0050809d2937cc794530
```

## Assurance boundary

The replay verifies exact algebra for `L-28004`. It does not prove:

```text
the subexponential compact-source energy;
the independent-frequency physical source map;
a strict physical transition reserve;
the Riemann Hypothesis.
```
