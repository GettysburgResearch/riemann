# Independent replay of the claimed quasi-RH Lean formalization — NOT EXECUTED

```text
Status: PLANNED / BLOCKED (requires explicit permission to build and run third-party code)
Scope: verification of a machine-checked proof claim; no mathematics is asserted here
Exact sources or dependencies: github.com/openai/math @ 4eaee87548250b2682affda7d05d947c05554bae, lean/ (toolchain leanprover/lean4:v4.34.1, Mathlib d13f23b723b8a846827a245b89c10fc7d3f11612)
What was actually run: static inspection only (file reading, import-closure computation, text scan)
Smallest remaining gap: compile the solution module and check axioms / exact statement independently
```

## What OpenAI claims

`lean/ComparatorChallenges/QuasiRiemannHypothesis.{lean,json}` states, against **Mathlib's own** `riemannZeta`:

```lean
theorem riemannZeta_ne_zero_of_seven_eighths_lt_re
    {s : ℂ} (hs : (7 / 8 : ℝ) < s.re) : riemannZeta s ≠ 0
```

with solution module `OAI.NumberTheory.DirichletL.Nonvanishing` and permitted axioms `propext, Quot.sound, Classical.choice` (`enable_nanoda: false`). Parallel challenges: `DirichletSevenEighths`, `HeckeSevenEighths`, `SiegelZeros`. Scope description: `lean/docs/003.md`.

## What the Observatory checked (static only)

* The challenge statement uses Mathlib's `riemannZeta` and a strict half-plane `7/8 < Re s`; it is a faithful formal rendering of "ζ has no zeros in Re s > 7/8" (Mathlib's `riemannZeta 1` is a junk value that is nonzero, so the point s = 1 does not trivialize the statement).
* Import closure of the solution module inside the OAI library: **2,924 modules, ≈486,000 lines**, plus Mathlib, `PrimeNumberTheoremAnd` (2 imports) and `RellichKondrachov` (1 import).
* A text scan of the 2,924 modules found **no** occurrences of the tokens `sorry`, `admit` (as a tactic), `axiom`, `native_decide`, `implemented_by`, `@[extern`, `unsafe`, `opaque` or `debug.skipKernelTC`. A text scan is not a proof check: it cannot see code introduced by macros or by dependencies, and it says nothing about whether the files compile.

## Replay procedure (proposed; blocked in this session)

Building a Lean project executes its lakefile and tactic code, i.e. untrusted third-party code. The session's safety policy blocked doing so without the user's explicit request. With permission, the procedure is:

1. Install `elan` and toolchain `leanprover/lean4:v4.34.1`.
2. In `lean/`: `lake update` (the project lakefile applies its own dependency patches from `lean/patches/`), confirm the manifest revisions are unchanged, then `lake exe cache get`.
3. `lake build OAI.NumberTheory.DirichletL.Nonvanishing` (estimate: several hours on 4 cores; the README warns about `vm.max_map_count` and suggests `GLIBC_TUNABLES=glibc.malloc.mmap_max=0:glibc.malloc.arena_max=1`).
4. In a fresh file: `import OAI.NumberTheory.DirichletL.Nonvanishing`, restate the exact theorem and close it with the library lemma, then `#print axioms` for both.
5. Preferably also run the Lean FRO `comparator` with `lean4export` (and an independent kernel such as `nanoda`), as OpenAI's own instructions describe, since `#print axioms` alone does not protect against environment manipulation by metaprograms.

Until this is done, the Observatory records the 7/8 theorem as **announced with a claimed formalization, formalization not independently replayed**.
