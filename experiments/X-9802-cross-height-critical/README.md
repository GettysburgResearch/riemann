# X-9802 — Rational cross-height critical-point certificates

`X-9802` implements `L-9802` without clearing large rational repairs into an
enormous product polynomial.

For

```text
phi(x) = sum_i beta_i log(((x-T_i)^2+u_i))
```

with one exact coefficient-sum-zero identity per height, it reconstructs

```text
P(x) = D(x) phi'(x),
D(x) = product_i ((x-T_i)^2+u_i) > 0.
```

The degree of `P` depends on the number of distinct height/node pairs, not on
the size or denominator of the `beta_i`.

The proof object supplies rational intervals isolating every real root of `P`.
The checker verifies the root count with exact Sturm arithmetic and proves the
response nonnegative on every root interval using self-contained rational
logarithm bounds. Since `phi` tends to zero at both infinities and is monotone
between critical points, this proves `phi>=0` globally.

It then contracts

```text
sum_i beta_i log |xi(1/2+sqrt(u_i)+iT_i)|^2
```

from exact positive squared-modulus intervals.

The checker uses no special function or floating point.

## Sharp PR #105 candidate

```text
center height T0:
  (-23, +46, -23)

upper height T0+5/16:
  (-750746, +1000000, -249254)

nodes:
  x = 2^-10, 2^-6, 2^-5
```

The derivative numerator has degree `9` and five real roots. Dyadic intervals of
width `3*2^-80` isolate all five. With 64 atanh terms, the integer-normalized
critical response lower bounds are approximately

```text
+2.28114181033643
+0.413720542806542
+105.043422397344
+5.61061546295551
+3817480.25682095
```

The p256 midpoint direct-`xi` portfolio is positive:

```text
integer normalization   +5.823585906012185...
normalized by 10^6      +5.823585906012185e-6
```

The response certificate is exact. The quoted direct-`xi` sign is empirical
until the adapter is run on the retained p192/p256 primitive files.

## Files

```text
verify.py
    Exact polynomial, Sturm, root-isolation, logarithm and finite-row checker.

build_from_pr105.py
    Binds the PR #105 center and upper-height direct-xi tables.

candidates/sharp-pr105-critical.json
    Exact response candidate, five root isolators and empirical direct margin.

certificates/synthetic-negative.json
    Same exact response certificate with a strict synthetic negative finite row.

tests/test_verify.py
    Eight adversarial tests.
```

## Local exact controls

```bash
python -m unittest discover -s tests -v
python verify.py certificates/synthetic-negative.json \
  --output results/synthetic.json
```

## Production replay

The workflow

```text
.github/workflows/pr105-cross-height-critical.yml
```

uses the retained PR #105 p192 and p256 primitive files. It requires:

1. identical derivative proof-object digests at both precisions;
2. p256 primitive squared-modulus intervals nested in p192 intervals;
3. the p256 final portfolio interval nested in the p192 interval;
4. a strict negative upper endpoint before any nomination.

## Search extension

The sharp candidate was obtained by rationalizing a continuous exchange/LP
search around the exact Jensen boundary row

```text
(-256,+341,-85).
```

The next search should:

1. optimize rational coefficients on asymmetric height triples;
2. add exact critical points whenever a grid solution violates global positivity;
3. freeze to dyadic coefficients;
4. run this checker before any direct-`xi` sign is discussed;
5. rank by normalized directed margin and response-certificate moat.
