# X-14312 — Exact certified-zero S-lemma floor

This directory verifies the finite rational implication in `L-14319`.
It performs no zeta evaluation and does not construct a localized Weil form.
After JSON parsing it uses only Python integers and `fractions.Fraction`.

## Certified inequality

The upstream packet supplies relative Loewner enclosures

```text
A0-eps_A G <= A <= A0+eps_A G,
J0-eps_J G <= J <= J0+eps_J G.
```

For `alpha>=0`, the checker proves

```text
A0-alpha(J0-delta^2 G)
 -(eps_A+alpha eps_J)G
 -F G >= 0.
```

It also proves a robust Slater margin using `J0-eps_J G`. Therefore every
exact visible vector satisfying

```text
x^T J x >= delta^2 x^T G x
```

has Rayleigh quotient at least `F`.

## Synthetic separation

```text
A = diag(2,-1)
J = diag(1,0)
delta^2 = 3/4
alpha = 3
```

The unrestricted form is negative on the second coordinate, but

```text
A-3(J-3I/4)=5I/4.
```

Thus the visible-cone floor is exactly `5/4`.

## Reproduction

```bash
python experiments/X-14312-certified-zero-slemma/verify.py \
  experiments/X-14312-certified-zero-slemma/certificates/synthetic.json \
  --output /tmp/x14312-result.json

python -m unittest discover \
  -s experiments/X-14312-certified-zero-slemma/tests -v
```

Expected result: eight tests passing.

## Production boundary

A production packet is rejected unless it binds a
`CERTIFIED_RELATIVE_LOEWNER_AND_ZERO_FRAME` gate. That gate must cover:

- actual certified critical-line zeros and multiplicities;
- exact Fourier--Mellin normalization;
- directed zero-representer Gram enclosures;
- the finite Weil-form enclosure;
- the metric and all relative Loewner radii.

The checker proves the finite S-lemma implication only. It does not prove the
cofinal residual floor or RH.
