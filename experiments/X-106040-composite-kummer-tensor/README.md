# X-106040 — Composite Kummer tensor-frame replay

Standard-library exact replay for `R-106040`, `L-106040`, and `T-106040`.

It checks:

```text
one-prime sign-pair frame p I-J;
sharp local factor (p-1)/(p+1);
two- and three-prime tensor frames;
2^omega(q) quadratic-class sector count;
reciprocity of sector contraction and principal-root-fibre weight;
source-blind sector recombination cost;
coefficientwise principal completion for squarefree conductors;
failure of the unpublished scalar 1-phi(q)/q formula.
```

Run:

```bash
python3 verify.py --output /tmp/x106040.json
cmp /tmp/x106040.json results/verification.json
```

The replay checks exact finite integer and rational algebra. It does not prove
the coherent composite owner-conductor moment, `HBCQDSP102888`, or RH.
