# T-108501 — Finite-dimensional commutative (and one-variable associative) zeta extensions carry only jets

```text
Claim ID: T-108501
Status:   PROVED (complete elementary proof in the standalone file)
Created:  2026-08-30
Programme: #764 (Generalized L-Objects), axis L (higher-dimensional parents
          and shadow geometry), central question 13, hypercomplex collapse
          test (issue experiment 18)
Depends on: structure theory of Artinian commutative algebras (standard);
          locally uniform convergence of Dirichlet series (standard)
Proof:    standalone/2026-08-30-commutative-collapse/PROOF.md
Replay:   experiments/X-108501-commutative-collapse/  (EXACT_RATIONAL
          pillars + one labelled FLOATING_RECONNAISSANCE corroboration)
RH status: RH and GRH are unproved; this claim does not address them.
```

## Statement (summary)

For any finite-dimensional commutative unital R-algebra `A` and `s` in the
complexification with `Re > 1` on the spectrum, the algebra-valued series
`sum_n exp(-s log n)` equals, componentwise over the Artinian decomposition
into local factors `C·1 ⊕ N_i`, the finite jet package

```text
( sum_{j < m_i} zeta^{(j)}(lambda_i) n_i^j / j! )_i .
```

Consequences: the extension is determined by finitely many derivatives of
`zeta` on the spectrum; it is invertible iff `zeta` is nonzero on the
spectrum (NO new zero geometry); every structural identity (Euler product,
completed functional equation, continuation) decomposes componentwise and
jet-wise. **Corollary:** the same holds for a single algebra variable in ANY
finite-dimensional associative algebra (the argument runs inside the
commutative subalgebra `C[s]`); in particular the naive quaternionic zeta
collapses slice-wise — the collapse half of #764's named theorem target on
quaternionic/multicomplex extensions, for all series/functional-calculus
definitions.

## Novelty position (boundary-audit gated)

PARTIAL_OVERLAP, borderline collides in substance: the bicomplex instance
is published (Rochon 2004 — bicomplex RH equivalent to RH — precisely a
collapse instance; mechanism classical since Scheffers-era hypercomplex
analysis; cf. Plaksa-Shpakivskyi), and per the audit slice-regular
quaternionic theory is also rigid. Claimed here: only the uniform
general statement with jet/functional-equation bookkeeping, the
no-new-zero-geometry corollary, and its use as a reusable #764 firewall.
Escaping the collapse within finite dimensions provably requires more than
one-variable functional calculus (several noncommuting variables, free
calculi, or non-power-series function theories) — recorded as the open
boundary.
```
