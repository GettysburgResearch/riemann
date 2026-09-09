# T-108002 — A refusal-capable exact structure detector for local trace data

```text
Claim ID: T-108002
Status:   PROVED (the instrument's exactness and refusal semantics, resting
          on L-108001) + EXACT_WITNESS battery results; nothing here is a
          statement about any global L-function
Created:  2026-08-30
Programme: #763 (Riemann Structures), research modes B (computational
          structure induction) and experiment 2 (trace-to-object
          reconstruction) + 8 (counterfeit ontology suite)
Depends on: L-108001 (uniqueness of minimal rational forms); Kronecker
          rationality criterion (classical)
Instrument: research/exploratory/2026-08-30-two-programme-pass/core/reconstruct.py
Replay:   experiments/X-108002-structure-detector/  (EXACT_RATIONAL)
RH status: RH and GRH are unproved; this claim does not address them.
```

## Statement

The deposited detector takes exact local coefficient or trace data
(improper numerators supported — trace generating series `-T Q'/Q` have
numerator degree equal to `deg Q`) and either reconstructs a candidate
finite-rank local object with certificates, or REFUSES, naming the FIRST
failing axiom in the fixed battery

```text
A1 FINITE_RANK -> A2 EFFECTIVITY -> A3 INTEGRALITY -> A4 PURITY(q,w)
   -> A5 HELD_OUT   (+ A6 TENSOR pairwise)
```

with an exact witness for every refusal. A1 certifies the PREFIX of the
window only, so A5's prediction of the withheld tail is substantive by
construction. By L-108001 the reconstruction is unique (properness
hypotheses as corrected there; improper forms certified by full-window
re-expansion). The degree-2 purity test is exactly complete:
`(product = q^w AND disc <= 0) OR (trace = 0 AND product = -q^w)`
— the second branch was MISSING in the first deposit and was found by the
adversarial wave with the counterexample `1 - 4T^2` at `(2,2)` (pure,
wrongly refused); above degree 2 the test is exact-necessary (labelled),
with the Ext^2 divisibility branch operative (its length guard originally
made it dead code for every degree >= 3; also found by the wave). A2
verdicts are statements about the reduced, class-level form: effectivity
of a particular virtual PRESENTATION is not trace-detectable, symmetric to
the Brauer-Nesbitt caution on non-semisimplicity.

## Battery results (all EXACT_RATIONAL; X-108002, 10 checks green)

- genuine degree-2 elliptic-type local data: full pass (A1-A5 hold);
- **number-field Mobius local data** `mu(p^k)`: finite rank HOLDS,
  refusal at **A2 EFFECTIVITY** with exact witness numerator `(1 - T)` —
  the Mobius local object is the VIRTUAL NEGATIVE of the trivial weight-0
  object. Phrased with the Brauer-Nesbitt caution from the boundary audit:
  trace data can never certify non-semisimplicity, and no matrix has
  `tr(M^k) = mu(p^k)`; the convention-invariant exact statement is
  precisely "A1 holds, A2 fails with witness (1-T)";
- **function-field Mobius contrast** (exhaustive exact computation over
  monic polynomials, q = 2, 3): the affine `F_q[x]` Mobius series is
  `1 - qT` — finite rank, VIRTUAL (A2 fails) with witness `(1 - qT)`,
  and the witness's single inverse root is `q`, with `q^2 = q^w` at
  `w = 2` (machine-recorded in the battery): the two Mobius ontologies are
  separated by the exact numerator witnesses `(1-T)` vs `(1-qT)`, read by
  inspection of the linear witness as virtual weight 0 vs virtual weight 2
  (Tate-twisted). Believed new as an exact packaged observation; the
  underlying identities are classical;
- structureless data refuses at A1; non-integral local factors at A3;
  integral weight-violating factors at A4; a corrupted tail is caught
  (A1 or A5 — silent acceptance is the tested-against failure mode);
  tensor compatibility holds on true products and fails with an indexed
  witness on perturbed ones.

## Novelty position (boundary-audit gated)

The engine is classical (Kronecker; Berlekamp-Massey; Ho-Kalman
realization). Audit verdict COLLIDES on the engine, clear on the
instrument: what is deposited as new is the assembled refusal pipeline
with named-first-failure semantics and exact witnesses, its battery
grounding, and its use on repository-native observables (O-108004,
separate). No claim of new mathematics in the linear algebra.

## Failure ledger

- F-108002-1: the pass's original phrasing of the Mobius finding
  ("nilpotent non-semisimple local system failing purity") was WRONG and
  was corrected by the machine output itself plus the boundary audit: the
  failing axiom is EFFECTIVITY, and non-semisimplicity is not a
  trace-certifiable property. The corrected phrasing above is the claim.
- F-108002-2 (FATAL, found by the adversarial wave, FIXED): the first
  deposit's degree-2 purity test omitted the trace-zero branch
  `(trace = 0 AND product = -q^w)` and wrongly refused the pure factor
  `1 - 4T^2` at `(2,2)`; the completeness clause was false as deposited.
  Fixed in core/reconstruct.py; the counterexample and its impure sibling
  are now battery rows B10.
- F-108002-3 (major, FIXED): traces mode was inoperative for all nonzero
  genuine data (improper numerators truncated); fixed in
  core/exact.minimal_rational_form with full-window re-expansion
  certification; battery rows B11 added.
- F-108002-4 (major, FIXED): with A1 on the full window, A5 was provably
  redundant given L-108001 and could never fire; redesigned so A1
  certifies the prefix and A5 predicts the withheld tail.
- F-108002-5 (major, FIXED): the Ext^2 purity branch above degree 2 was
  dead code (length guard); now operative.
- F-108002-6 (instructive, FIXED): the original "structureless" battery
  row was eventually periodic, i.e. genuinely finite-rank; the improved
  detector correctly certified its structure. Replaced by the primes;
  the mislabel is recorded as a lesson about what "structureless" means.
- F-108002-7 (robustness, FIXED): A6 crashed instead of refusing on
  high-degree inputs (power-sum window too short); lengths corrected.
```
