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

## The stronger all-Dirichlet theorem

Joseph Bebel's tracker submission independently formalizes the strict zero-free boundary \(B_*=0.8733458561067185768\ldots\) for every Dirichlet character of positive modulus, with the principal pole excluded. Taking the principal character of modulus one gives the ordinary zeta statement. The declaration uses the unique real root in \((13/15,7/8)\) of the degree-nine polynomial in Liu's Theorem 7.2. The companion declarations prove root isolation and an explicit rational upper comparison. The source commit is `c74d855c3bdfceeee059501aea76c8b1627b9abd`, and the submitted source subtree is `44932d56db449a81c8663b944c14c33e3756a6c2`. [Lean statements](https://github.com/GTimG/QuasiRiemannTracker/blob/c74d855c3bdfceeee059501aea76c8b1627b9abd/submissions/2026-11-13-continuum-exact-contact/src/Candidate/Main.lean) · [Liu's analytic comparison](https://hexagonmath.org/2611.00421v1)

We extracted the complete verification report from the tracker's admission archive and hashed its unmodified JSON string. The resulting SHA-256, `9397e8075defc71c0ff6d05d38f474c91aa6027c0171ed1409ae2b634f9c2168`, matches the separately published certificate. The report records `PASS` for the three canonical declarations `QRH.canonical_bound`, `QRH.canonical_bound_le`, and `QRH.canonical_bound_isolated`, with permitted axioms `Classical.choice`, `Quot.sound`, and `propext`. The default Lean kernel, NanoDa and con-ron accepted the export, with judge exit code 0 at 22:34:40 UTC on 15 November 2026. The hash of the solution export in that report is `576741b24c20992fc37643baf1e309eec95e01eed66fdede5685b31a7c583152`. Our local check covers the published report, source statement, date, and matching rational and algebraic bounds. The 127-digit numerator and 128-digit denominator recorded in the report appear literally in the pinned source and give the ratio \(0.87334585610671857680118479606507235677044\ldots\). Liu's extension at the same number to general number fields and unitary Hecke characters is a separate analytic result. [Archived report](https://github.com/GTimG/QuasiRiemannTracker/blob/8802b512b5d117dadefa41a0d00ad028f29450fe/records/143/c74d855c3bdfceeee059501aea76c8b1627b9abd/continuum-exact-contact/43761452075-1.json) · [Certificate](https://gtimg.github.io/QuasiRiemannTracker/certificates/continuum-exact-contact.json) · [Successful verification job](https://github.com/GTimG/QuasiRiemannTracker/actions/runs/43761452075/job/132957199949)

## Local replay checkpoint

The local scratch checkout matched the frozen OpenAI commit and Lean subtree above. The first build was interrupted after job 4,357 of 7,061. We resumed it with the same Lean 4.34.1 toolchain and stopped it during the final research window at 14:57 UTC. Its last completed job was 4,457 of 7,061, and 320 OAI module objects were present in the local build cache. The final resumed-build log had SHA-256 `4b3aee0e41a9349e531e8349096fc51f3338e82f7ed30922717b8bcad8cbe59d`. The local run did not reach the final nonvanishing module or the final axiom query. The complete 7,061-job build and three-axiom output reported above are from the separately hash-verified external receipt.

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
