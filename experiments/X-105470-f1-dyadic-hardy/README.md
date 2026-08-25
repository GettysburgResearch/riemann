# X-105470 — F1 dyadic-cell and Hardy replay

Run

```bash
python experiments/X-105470-f1-dyadic-hardy/verify.py
python experiments/X-105470-f1-dyadic-hardy/tests/test_verify.py
```

The replay checks:

```text
exact Q(sqrt(2)) factorization of the dyadic filter;
exact cumulative-cell and one-Hardy-primitive algebra;
integer-cell affine localization of K_L;
right-endpoint and endpoint-jump identities;
closed logarithmic cell-mass formula;
uniform two-endpoint inequalities;
full-window continuous/discrete inequalities;
weighted l1 duality and finite Fubini;
Cauchy control used by the jump ledger;
one-interior-sample counterexamples.
```

The replay authenticates finite algebra, randomized high-precision evaluations,
and the stated firewalls.  It does not estimate `F1HARDY105470`, prove
`BCI102990`, or prove RH.
