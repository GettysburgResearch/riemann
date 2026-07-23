# Integrator patch — Issue #45 witness-survival calculus

Agent: `gpt56-06-b`  
Issue: #45  
Date: 2026-07-23  
Branch: `agent/gpt56-06-b/45-witness-survival-calculus`

This patch is merge-order aware.  It does not modify the root registries because
most dependencies remain on concurrent draft branches.

## Proposed claim-registry additions

| ID | Kind | Title | Status | Owner | File |
|---|---|---|---|---|---|
| D-4501 | Definition | Uncertainty-closed finite-witness semantics | PROPOSED | `gpt56-06-b` | `claims/definitions/D-4501-uncertainty-closed-witness-semantics.md` |
| L-4501 | Lemma | Local inclusion contracts compose into global witness survival | PROPOSED | `gpt56-06-b` | `claims/lemmas/L-4501-compositional-enclosure-survival.md` |
| L-4502 | Lemma | Support-function and dual certificates for robust witness margins | PROPOSED | `gpt56-06-b` | `claims/lemmas/L-4502-support-function-robust-witness.md` |
| L-4503 | Lemma | Fixed-vector Pick contraction preserves uncertainty correlation | PROPOSED | `gpt56-06-b` | `claims/lemmas/L-4503-pick-fixed-vector-uncertainty-compression.md` |
| M-4501 | Method | Proof-carrying witness-survival assurance case | PROPOSED | `gpt56-06-b` | `claims/methodology/M-4501-proof-carrying-witness-survival.md` |
| X-4501 | Experiment | Exact checker for quantitative witness survival | exact algebraic synthetic controls | `gpt56-06-b` | `experiments/X-4501-witness-survival-checker/README.md` |

## Proposed open-problem entry

### Q-4501 — End-to-end uncertainty closure for the first genuine finalist

**Question.** Can one active route export a frozen exact finalist, a complete
logical-gate ledger, a sound quantitative evaluation DAG, and a small checker
whose root set has a strict moat inside the disproof region?

**Required distinction.** A numerical moat closes only the declared
quantitative uncertainty.  Equivalence, normalization, analytic-domain, source
completeness, and trusted-base obligations remain hard gates.

**Initial targets.** Issue #39 Pick-Rayleigh evaluation, the optimized carrier
basin in PR #44, and one exact arithmetic sign certificate.

## Proposed methodological registry addition

Add a repository-wide candidate-promotion requirement:

> Every `Z-####` candidate must include an uncertainty-closure ledger.  Every
> quantitative channel used by the decisive computation must be declared
> exactly once and enclosed by a sound proof object.  Every logical gate must
> have an evidence locator and no gate may remain blocking.  The final exact
> checker must prove a strict moat from the witness-failure boundary.

## Dependency and merge order

- D-4501, L-4501, L-4502, and M-4501 are route independent.
- L-4503 refers to D-3201/L-3202 on draft PR #38 and should be integrated after
  or together with those definitions.
- M-4501 treats L-3101/L-3102 on draft PR #33 and M-0901 on draft PR #44 as
  route-specific uncertainty-block producers; it does not promote them.
- X-4501 contains only synthetic exact arithmetic and may merge independently.

## Suggested README/process amendment after trial

After one real route completes the trial, add the following to candidate rules:

```text
A candidate is not quantitatively certified until an exact checker proves that
its decisive value/invariant remains inside the counterexample region for every
realization in a complete, explicitly declared uncertainty model.  Numerical
margin does not discharge theorem, normalization, domain, or completeness
gates.  Every residual trusted-base component must be named.
```

## Review order

1. `claims/definitions/D-4501-uncertainty-closed-witness-semantics.md`
2. `claims/lemmas/L-4501-compositional-enclosure-survival.md`
3. `claims/lemmas/L-4502-support-function-robust-witness.md`
4. `claims/lemmas/L-4503-pick-fixed-vector-uncertainty-compression.md`
5. `experiments/X-4501-witness-survival-checker/verify.py`
6. `experiments/X-4501-witness-survival-checker/tests/test_verify.py`
7. `claims/methodology/M-4501-proof-carrying-witness-survival.md`
8. `literature/witness-survival-source-ledger.md`
9. `reports/gpt56-06-b/2026-07-23-45-witness-survival-calculus.md`
