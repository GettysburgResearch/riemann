import OAI.NumberTheory.DirichletL.Nonvanishing
-- Statement pinned against the root-namespace Mathlib definitions.
example : ∀ {s : ℂ}, (7:ℝ) / 8 < s.re → _root_.riemannZeta s ≠ 0 :=
  @OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re
example : ∀ {q : ℕ} [NeZero q] (χ : _root_.DirichletCharacter ℂ q) {s : ℂ},
    (7:ℝ) / 8 < s.re → ¬(χ = 1 ∧ s = 1) → _root_.DirichletCharacter.LFunction χ s ≠ 0 :=
  @OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re
open Lean in
#eval show CoreM Unit from do
  let env ← getEnv
  for n in [``riemannZeta, ``DirichletCharacter.LFunction] do
    let m := env.getModuleIdxFor? n
    let modName := m.map (fun i => env.header.moduleNames[i.toNat]!)
    IO.println s!"{n} defined in module {modName}"
