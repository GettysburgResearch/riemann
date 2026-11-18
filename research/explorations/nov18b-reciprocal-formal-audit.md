# The external seven-eighths theorem and its kernel receipt

The source frozen at OpenAI/math commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` proves the Riemann zeta function is zero-free in the strict half-plane \(\Re s>7/8\), with the usual analytic pole at 1. Its Lean declaration is

```lean
theorem riemannZeta_ne_zero_of_seven_eighths_lt_re
    {s : ℂ} (hs : (7 / 8 : ℝ) < s.re) : riemannZeta s ≠ 0
```

The declaration is in the namespace `OAI`. The nonzero value of Mathlib's totalized function at 1 concerns the library convention at the pole. On the punctured half-plane the theorem has the usual analytic meaning. The module also proves the corresponding result for each Dirichlet character, excluding its principal pole. The Comparator challenge contains a placeholder for the submitted proof. The solution module imports the unconditional detector assembly. [Solution](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Nonvanishing.lean) · [Final assembly](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Detector/FinalAssemblyUnconditional.lean) · [Mathlib zeta definition](https://github.com/leanprover-community/mathlib4/blob/d13f23b723b8a846827a245b89c10fc7d3f11612/Mathlib/NumberTheory/LSeries/RiemannZeta.lean)

## Published independent replay

The fork grwtsk/openai-math ran Lean's primary kernel at the frozen revision. Its audit commit was `c32d905c72fec3f487634fc26cd4c177ee834465`. The original and audit Lean subtree hashes both equal `b67b84636537041bf8da1e7263a827a5ab7ffba4`. The artifact records an empty diff of the Lean sources and separate dependency identities, including upstream compatibility patches. The toolchain was Lean 4.34.1, with Mathlib revision `d13f23b723b8a846827a245b89c10fc7d3f11612`. [Workflow run](https://github.com/grwtsk/openai-math/actions/runs/37923366946)

We downloaded artifact `11618648102` and independently hashed the archive. Its SHA-256 was `5dce19c94e806540c155c41d52b3f2517a8ec76b2d717be72758b5f4802d4012`. The included module build log ends with successful completion of 7,061 jobs. We extracted and hashed the actual axiom probe log, obtaining `504d167f9b5814b54a35e4d15ed480302ff0ff1b428b32899b81859f9d1e70b0`. Its elaborated declaration and transitive kernel axiom query report

```text
'OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re' depends on axioms:
[propext, Classical.choice, Quot.sound]
```

The Dirichlet declaration has the same three axioms. This receipt records a conventional Lean-kernel replay against the pinned dependencies. The audit's alternative-kernel switch `enable_nanoda` was false. [Build artifact](https://github.com/grwtsk/openai-math/actions/runs/37923366946/artifacts/11618648102)

## Reproduction

From the pinned solution's `lean` directory, with its pinned toolchain installed, run

```sh
lake update
lake exe cache get
lake build OAI.NumberTheory.DirichletL.Nonvanishing
lake env lean Probe.lean
```

The contents of `Probe.lean` are

```lean
import OAI.NumberTheory.DirichletL.Nonvanishing

#check OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re
#print axioms OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re
#check OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re
#print axioms OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re
```
