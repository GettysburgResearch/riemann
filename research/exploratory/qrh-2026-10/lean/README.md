# Lean files of the qrh-2026-10 wave

```text
Status: EXPLORATORY formal corollaries of the imported 7/8 theorem. All three files build on top
  of the completed import build with no errors and no warnings of their own
  (../reviews/results/lean_corollary_build.log; lake also prints the 23 "has local changes"
  notices of the patched packages, filtered from that log). `#print axioms` shows only
  [propext, Classical.choice, Quot.sound] (../reviews/results/lean_corollary_axioms.log).
  Comparator (../reviews/LEAN_BUILD_ATTEMPT.md, Addendum C): SiegelFromSevenEighths ACCEPTED
  against the upstream SiegelZeros challenge; for the other files see the table there. No RH claim.
Scope: ZetaZeroStrip.lean (nontrivial zeros of Mathlib's riemannZeta lie in 1/8 <= Re s <= 7/8);
  DirichletZeroStrip.lean (the same strip for L(s, chi), chi primitive and nontrivial);
  SiegelFromSevenEighths.lean (both statements of the imported Siegel-zero comparator challenge,
  with c = log 3 / 8)
Exact sources or dependencies: pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6,
  standalone/2026-10-07-openai-quasi-riemann-import/upstream/lean (byte-exact import of
  openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a lean/); Lean v4.34.1; Mathlib d13f23b7;
  the imported theorems OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re and
  OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re; Mathlib's riemannZeta_one_sub
What was actually run: a clean lake build of the three modules (as OAI.QRHWave.*) in the scratch
  copy of the import; checks/CorollaryAxioms.lean. Comparator runs on comparator/*.json: see
  ../reviews/LEAN_BUILD_ATTEMPT.md, Addendum C (not run when this header was written)
Smallest remaining gap: ZetaZeroStrip rests on the zeta 7/8 theorem, which comparator accepted
  under the assumptions of LEAN_BUILD_ATTEMPT Addendum B. DirichletZeroStrip and
  SiegelFromSevenEighths rest on the Dirichlet 7/8 theorem, which comparator also accepted
  (Addendum C). The corollaries themselves have `#print axioms` evidence; their own comparator
  runs are in Addendum C. No part of the Lean development has had a human review
```

RH remains unsolved. None of the files says anything about the critical line beyond reflecting the
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

## DirichletZeroStrip.lean: the strip for primitive Dirichlet L-functions

`QRHWave.LFunction_quasi_critical_strip`: let `χ` be a primitive Dirichlet character with
`χ ≠ 1`. Then every zero `s` of Mathlib's `DirichletCharacter.LFunction χ` with
`gammaFactor χ s ≠ 0` has `1/8 ≤ Re s ≤ 7/8`.

The true Archimedean factor never vanishes. In Lean, `gammaFactor χ s = 0` holds exactly at its
poles, because Mathlib's `Gamma` is 0 at non-positive integers. So the hypothesis says that `s`
is not a pole of the Gamma factor, which for primitive `χ ≠ 1` is exactly the set of trivial
zeros.

`gammaFactor_eq_zero_iff` identifies the excluded points as the trivial zeros: `s = 0, −2, −4, …`
for even `χ`, and `s = −1, −3, …` for odd `χ`.

The lower edge applies Mathlib's functional equation to the primitive character `χ⁻¹`, whose
conductor equals that of `χ` by `conductor_inv`. Then `Λ(χ, s) = 0` forces `Λ(χ⁻¹, 1 − s) = 0`,
hence `L(χ⁻¹, 1 − s) = 0` with `Re(1 − s) > 7/8`. That contradicts the imported 7/8 theorem.
No non-vanishing of the root number is needed.

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

The constant is explicit. The helper theorem `gap_of_real_zero` states, with no `∃`:

    q ≥ 3,  χ any Dirichlet character mod q,  β < 1,  L(β, χ) = 0   ⟹   (log 3)/8 ≤ (1 − β) log q.

So this is an *effective* Landau–Siegel-type bound with constant `(log 3)/8 ≈ 0.137`. It is
conditional only on accepting the imported 7/8 Dirichlet theorem (comparator-accepted; Addendum
C). By contrast, the upstream Oct 1 proof states only `∃ c`, and its witness comes out of a chain
of lemmas (`SiegelZerosAwei.W50.uniform_exclusion_of_local_isolated_bezout`). Whether that `c` is
explicit was not checked here.

The file reuses the challenge's fully qualified names `OAI.SiegelZeros.WeightedTorusJets.*`,
because comparator matches by name. The upstream Siegel development uses the same names, so the
two modules cannot be imported together. "WeightedTorusJets" names the upstream method, which
this proof does not use.

This makes formal the remark in [../SIEGEL_DETERMINANT.md](../SIEGEL_DETERMINANT.md) that the
Siegel-zero statement is a weak corollary of the 7/8 claim. It also shows that the Oct 1 paper's
own proof is not needed for the challenge statement *if* the 7/8 development is accepted. It
says nothing about whether the Oct 1 argument itself is correct, or about its own constant
(`c ≈ 3·10⁻⁴` in SIEGEL_DETERMINANT.md).

## How to check

All three files must be compiled inside the imported Lean project (they import
`OAI.NumberTheory.DirichletL.Nonvanishing`):
1. Copy them to `OAI/QRHWave/` in that project, and run
   `lake build OAI.QRHWave.SiegelFromSevenEighths OAI.QRHWave.ZetaZeroStrip OAI.QRHWave.DirichletZeroStrip`.
2. Run `lake env lean <this dir>/checks/CorollaryAxioms.lean`.
3. For comparator, copy `comparator/QRHWaveStrip.lean` and the two JSON files into
   `ComparatorChallenges/`, then run `lake env comparator ComparatorChallenges/<name>.json`.

Note: `QRHWaveStrip.lean` is a challenge written in this wave, not an upstream one.
