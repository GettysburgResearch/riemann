# X-15114 — Exact classical source sewing and fixed-probe obstruction

This experiment uses only Python integers, `fractions.Fraction`, JSON, and
SHA-256.

It verifies on one redundant finite readout:

1. the Gram matrix and its Moore--Penrose inverse;
2. all four Penrose identities;
3. quotient compatibility of the seam form;
4. the pseudoinverse cyclic identity through order eight;
5. a direct eight-index order-four contraction;
6. invariance under a nonorthogonal redundant coordinate change;
7. the exact linear-versus-quartic scaling obstruction;
8. one all-orders Hilbert--Schmidt geometric majorant.

Retained values:

```text
trace moments 2..8  7, 10, 31, 61, 154, 337, 799
order-four sewn      31
linear value at 2B   62
sewn value at 2B     496
homogeneity gap      434
series majorant      3 on |w|<=1/6 with C=3
```

Reproduce:

```bash
python3 verify.py certificates/redundant-readout-order4.json
python3 -m unittest discover -s tests -v
```

This is a finite algebraic control. It neither evaluates `xi` nor proves the
classical Guinand--Weil pullback or RH.
