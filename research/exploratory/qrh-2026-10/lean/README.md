# Lean files of the qrh-2026-10 wave

```text
Status: EXPLORATORY formal corollaries of the imported 7/8 theorem. Both files compile on top of the
  completed import build with no errors or warnings, and `#print axioms` shows only
  [propext, Classical.choice, Quot.sound]. Comparator results are in
  ../reviews/LEAN_BUILD_ATTEMPT.md, Addendum B. No RH claim.
Scope: ZetaZeroStrip.lean (nontrivial zeros of Mathlib's riemannZeta lie in 1/8 <= Re s <= 7/8);
  SiegelFromSevenEighths.lean (both statements of the imported Siegel-zero comparator challenge,
  with c = log 3 / 8)
Exact sources or dependencies: pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6,
  standalone/2026-10-07-openai-quasi-riemann-import/upstream/lean (byte-exact import of
  openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a lean/); Lean v4.34.1; Mathlib d13f23b7;
  the imported theorems OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re and
  OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re; Mathlib's riemannZeta_one_sub
What was actually run: lake build of both modules (as OAI.QRHWave.*) in the scratch copy of the
  import; checks/CorollaryAxioms.lean; comparator (Addendum B)
Smallest remaining gap: everything here inherits the trust status of the imported 7/8 Lean
  development (a kernel check under comparator's assumptions, not a human review)
```

RH remains unsolved. Neither file says anything about the critical line beyond reflecting the
imported half-plane.

## ZetaZeroStrip.lean: the quasi-critical strip

`QRHWave.quasi_critical_strip` has exactly the hypotheses of Mathlib's `RiemannHypothesis`:
`ζ s = 0`, `s` is not a trivial zero `-2(n+1)`, and `s ≠ 1`. Its conclusion is
`1/8 ≤ Re s ≤ 7/8`, where RH would need `Re s = 1/2`.

The proof:
* Upper edge: the imported 7/8 theorem.
* Lower edge: Mathlib's functional equation `riemannZeta_one_sub` at `1 − s`. If `Re s < 1/8`,
  then `ζ(1 − s) ≠ 0` (7/8 theorem), `Γ(1 − s) ≠ 0` and `(2π)^{−(1−s)} ≠ 0`, so
  `cos(π(1 − s)/2) = 0`. That forces `s = −2k` with an integer `k ≥ 1`, using `ζ(0) = −1/2` to
  exclude `k = 0`.

## SiegelFromSevenEighths.lean: the Siegel-zero challenge from 7/8

`ComparatorChallenges/SiegelZeros.lean` in the import is the formal target of the 1 October
Landau–Siegel paper. It asks for an absolute `c > 0` with

    c ≤ (1 − β) log q

for every real zero `β ∈ (0, 1)` of `L(s, χ)`, with `χ` real, primitive and non-principal of
modulus `q ≥ 3`.

The file proves both challenge statements with `c = (log 3)/8`:
* a real zero `β < 1` has `β ≤ 7/8`, by the imported 7/8 Dirichlet theorem;
* then multiply `1 − β ≥ 1/8` by `log q ≥ log 3`.

Primitivity, reality and non-principality of `χ` are not used.

This makes formal the remark in [../SIEGEL_DETERMINANT.md](../SIEGEL_DETERMINANT.md) that the
Siegel-zero statement is a weak corollary of the 7/8 claim. It also shows that the Oct 1 paper's
own proof is not needed for the challenge statement *if* the 7/8 development is accepted. It
says nothing about whether the Oct 1 argument itself is correct, or about its own constant
(`c ≈ 3·10⁻⁴` in SIEGEL_DETERMINANT.md).

## How to check

Both files must be compiled inside the imported Lean project (they import
`OAI.NumberTheory.DirichletL.Nonvanishing`):
1. Copy them to `OAI/QRHWave/` in that project, and run
   `lake build OAI.QRHWave.SiegelFromSevenEighths OAI.QRHWave.ZetaZeroStrip`.
2. Run `lake env lean <this dir>/checks/CorollaryAxioms.lean`.
3. For comparator, copy `comparator/QRHWaveStrip.lean` and the two JSON files into
   `ComparatorChallenges/`, then run `lake env comparator ComparatorChallenges/<name>.json`.

Note: `QRHWaveStrip.lean` is a challenge written in this wave, not an upstream one.
