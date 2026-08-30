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

The deposited detector takes exact local coefficient or trace data and
either reconstructs a candidate finite-rank local object with certificates,
or REFUSES, naming the FIRST failing axiom in the fixed battery

```text
A1 FINITE_RANK -> A2 EFFECTIVITY -> A3 INTEGRALITY -> A4 PURITY(q,w)
   -> A5 HELD_OUT   (+ A6 TENSOR pairwise)
```

with an exact witness for every refusal. By L-108001 the reconstruction is
unique and the held-out test is exact (never heuristic); the purity test is
exactly complete for degree <= 2 and exact-necessary above (labelled).

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
  and the virtual part is PURE of weight 2 (Tate-twisted). The detector
  therefore separates the two Mobius ontologies by the WEIGHT of their
  virtual parts: weight 0 (number field, per prime) vs weight 2 (function
  field, global affine). Believed new as an exact packaged observation;
  the underlying identities are classical;
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
```
