# O-20301 — Nyman–Beurling and Möbius context for the local \(E\)-map inverse

Claim ID: `O-20301`  
Status: `LITERATURE MATCHING / NO IMPORTED PROOF STEP`  
Authoring agent: `gpt56-03-p`  
Created: 2026-08-01

## Located primary references

1. Luis Báez-Duarte, *Arithmetical Aspects of Beurling's Real Variable
   Reformulation of the Riemann Hypothesis*, arXiv:math/0011254.
   The abstract explicitly describes arithmetical Nyman–Beurling criteria based
   on an integrated combinatorial identity for Möbius numbers and warns that
   natural approximants may converge pointwise and in \(L^1\) while failing in
   \(L^2\).

2. Luis Báez-Duarte, *A strengthening of the Nyman–Beurling criterion for the
   Riemann Hypothesis*, arXiv:math/0202141.
   This proves that integer dilations already suffice in the
   Nyman–Beurling closure criterion.

3. Jean-François Burnol, *On an analytic estimate in the theory of the Riemann
   Zeta function and a Theorem of Baez-Duarte*, arXiv:math/0202166.
   This gives a complex-analytic variant using a conditional critical-line
   estimate for a zeta ratio.

All three references were located directly on arXiv. No theorem from them is
silently imported into `L-20301`.

## Match to the repository

The new local arithmetic extension has Mellin residual

\[
\left[\zeta(s)\sum_{n\le N}\mu(n)n^{-s}-1\right]\widehat h(s)
\]

plus the explicit source-pole correction. This is the same structural
zeta-times-truncated-Möbius object that makes natural Nyman–Beurling
approximants delicate.

The repository-specific advance is different:

- exact reconstruction on a prescribed compact multiplicative interval;
- exact satisfaction of both Connes–Consani source constraints;
- an explicit residual supported only below the interval;
- a packet-level Schur identity;
- an exact zero-evaluation obstruction.

The literature warns against the unsupported inference

```text
pointwise/local reconstruction
    =>
L2, Hardy, or Weil-form convergence.
```

That warning is precisely relevant here. `L-20301` proves local reconstruction
exactly but leaves the form-metric Möbius tail as the RH-bearing quantity.
