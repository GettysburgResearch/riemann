# WITHDRAWN — false Q4 aligned innovation bound

The first version of this note confused two different transforms:

```text
carry(Lambda) = log binomial;
additive prefix defect of psi != log binomial.
```

The correct aligned innovation contains

\[
\psi(4n)-\psi(4j)-\psi(4k)
-4[\psi(n)-\psi(j)-\psi(k)],
\]

plus the explicit dyadic terms. It is not proved `O(log n)`.

See corrected `L-32305`. PR #345's innovation-square domination remains open and RH-bearing.
