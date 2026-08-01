# X-15113 — Exact same-matrix cyclic and grading checker

Experiment ID: `X-15113`  
Associated claims: `L-15129`, `L-15130`, `L-15131`, `R-15108`  
Author: `gpt56-04-f`  
Date: 2026-08-01

## Purpose

This Fraction-only checker verifies three exact finite statements.

1. **Graded same-matrix pass.** One positive Gram `G`, one Hermitian seam form `B`, and one `G`-self-adjoint grading `J` satisfy

   ```text
   J^2=I,
   J*G=GJ,
   J*BJ=-B.
   ```

   The checker reconstructs `T=G^-1B`, verifies the six-index order-three contraction, verifies every supplied trace moment, forces odd moments to zero, and repeats the calculation after a nonorthogonal basis change.

2. **Inverse-Gram obstruction.** In dimension one, `G=(4), B=(4)` gives

   ```text
   Tr((G^-1 B)^3)=1,
   Tr(B^3)=64.
   ```

3. **Compression obstruction.** A perfectly graded `2 x 2` operator is compressed to a line not invariant under the grading. The compressed cubic trace is exactly `64/125`, with the grading-square and anticommutator defects retained explicitly.

## Retained graded control

The exact moments through order eight are

```text
Tr(T^2) = 205/72
Tr(T^3) = 0
Tr(T^4) = 40225/10368
Tr(T^5) = 0
Tr(T^6) = 8061625/1492992
Tr(T^7) = 0
Tr(T^8) = 1616430625/214990848
```

A triangular nonorthogonal basis change produces dense Gram, seam, and grading matrices but preserves every cyclic coefficient exactly.

## Reproduction

```bash
python3 verify.py certificates/graded-cyclic-pass.json
python3 verify.py certificates/gram-omission-obstruction.json
python3 verify.py certificates/compression-leakage-obstruction.json
python3 -m unittest discover -s tests -v
```

## Trust boundary

The verifier uses only Python integers, `fractions.Fraction`, JSON, and SHA-256. It constructs no classical explicit-formula coefficient and evaluates no zeta or xi function. Passing proves only the finite operator-side same-matrix and grading identities.
