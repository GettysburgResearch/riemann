# X-15612 — Exact soft-tail conditioning split

This is a finite rational regression for `L-15630`.

It verifies an exact core-preserving source right inverse, the unwhitened graph
bound

\[
K\preceq M^2G,
\]

the regularized complete-frame inequality

\[
K\preceq B^2(D+\tau G),
\qquad
\tau=\ell^{-2},
\qquad
B=M\ell,
\]

and the exact split into:

- a retained core;
- a soft profile sector \(D\preceq\tau G\);
- the complete remaining complement, where
  \[
  D\succeq\tau G,
  \qquad
  K\preceq B^2D.
  \]

The retained synthetic data are diagonal so every inequality is checked with
`fractions.Fraction`; no floating eigensolver is used.

Run:

```bash
python experiments/X-15612-soft-tail-conditioning/verify.py
```

Expected verdict:

```text
PASS_EXACT_L15630_CONDITIONING_SPLIT
```
