# Lean files of the qrh-2026-10 wave

```text
Status: EXPLORATORY formal corollary (kernel-checked in a scratch build; see below). No RH claim.
Scope: one file, SiegelFromSevenEighths.lean: the two statements of the imported Siegel-zero
  comparator challenge, derived from the imported 7/8 Dirichlet theorem
Exact sources or dependencies: pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6,
  standalone/2026-10-07-openai-quasi-riemann-import/upstream/lean (byte-exact import of
  openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a lean/); Lean v4.34.1; Mathlib d13f23b7;
  the imported theorem OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re
What was actually run: see ../reviews/LEAN_BUILD_ATTEMPT.md, Addendum B
Smallest remaining gap: the correctness of the imported 7/8 Lean development is a kernel check
  under comparator's stated trust assumptions, not a human review
```

## What the file shows

`ComparatorChallenges/SiegelZeros.lean` in the import is the formal target of the 1 October
Landau–Siegel paper. It asks for an absolute `c > 0` with

    c ≤ (1 − β) log q

for every real zero `β ∈ (0, 1)` of `L(s, χ)`, `χ` real, primitive and non-principal of modulus
`q ≥ 3`.

`SiegelFromSevenEighths.lean` proves both challenge statements with `c = (log 3)/8`.
* It uses only the imported 7/8 Dirichlet theorem: a real zero `β < 1` has `β ≤ 7/8`.
* It then multiplies `1 − β ≥ 1/8` by `log q ≥ log 3`.
* Primitivity, reality and non-principality of `χ` are not used.

This makes [../SIEGEL_DETERMINANT.md](../SIEGEL_DETERMINANT.md)'s remark formal: the
Siegel-zero statement is a weak corollary of the 7/8 claim. It also shows that the Oct 1
paper's own proof is not needed for the challenge statement *if* the 7/8 development is accepted.
Conversely, it says nothing about whether the Oct 1 argument is correct, or about its constant
(`c ≈ 3·10⁻⁴` in SIEGEL_DETERMINANT.md).

## How to check it

The file must be compiled inside the imported Lean project (it imports
`OAI.NumberTheory.DirichletL.Nonvanishing`). Copy it to `OAI/QRHWave/SiegelFromSevenEighths.lean`
in that project and run comparator with the challenge module `ComparatorChallenges.SiegelZeros` and
solution module `OAI.QRHWave.SiegelFromSevenEighths` (the theorem names and permitted axioms are
as in `ComparatorChallenges/SiegelZeros.json`). The commands and the outcome are in
[../reviews/LEAN_BUILD_ATTEMPT.md](../reviews/LEAN_BUILD_ATTEMPT.md), Addendum B.
