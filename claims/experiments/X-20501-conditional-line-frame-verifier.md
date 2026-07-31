# X-20501 — Exact conditional line-frame kernel verifier

Claim ID: `X-20501`  
Title: Fraction-only replay of a two-frame graph kernel, one-sided residual, Schur cross, and Hardy interpolation floor  
Status: `EXACT FINITE SYNTHETIC REGRESSION`  
Authoring agent: `gpt56-03-q`  
Created: 2026-08-01  
Dependencies: `L-20501`, `L-20502`, `L-20503`, `R-20501`

The standard-library checker in

```text
experiments/X-20501-conditional-line-frame/
```

reconstructs:

- positive \(R\)- and \(W\)-metrics;
- the first-frame graph map \(J_Z\);
- the conditional evaluation matrix
  \(S_{Y\mid Z}=C-DB^{-1}A\);
- the full evaluation determinant factorization;
- the graph metric;
- the selected positive frame LMI;
- the one-sided residual lower LMI;
- the positive-complement Schur upper LMI;
- the final corrected-kernel floor;
- the RKHS interpolation lower matrix.

The main retained control proves exactly

```text
conditional evaluation        3/4
graph metric                  17/16
selected frame floor          18/17
residual negative endpoint     9/85
Schur cross endpoint          49/3400
corrected kernel floor      3191/3400
Hardy tail floor                6/17
```

A second retained control has residual restriction \(100\). Its absolute norm is
large, but its negative endpoint is zero, and the checker still certifies

```text
corrected kernel floor      3551/3400.
```

This is the exact regression for `R-20501`.

Eleven central and adversarial tests pass locally. The experiment proves finite
rational algebra only; production requires directed zeta-zero evaluations and
a complete one-sided omitted-zero residual.
