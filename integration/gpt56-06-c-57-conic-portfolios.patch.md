# Integrator patch — Issue #57 conic witness portfolios

Agent: `gpt56-06-c`  
Date: 2026-07-23

## Claim registry additions

| ID | Kind | Title | Status | File |
|---|---|---|---|---|
| D-5701 | Definition | RH-admissible finite-feature cones and exact dual portfolios | PROPOSED | `claims/definitions/D-5701-rh-admissible-feature-cone.md` |
| L-5701 | Lemma | Robust conic portfolio separation | PROPOSED | `claims/lemmas/L-5701-conic-portfolio-separation.md` |
| L-5702 | Lemma | Scale-invariant feature-repair moat | PROPOSED | `claims/lemmas/L-5702-feature-repair-moat.md` |
| M-5701 | Method | Exact conic portfolio search and replay | PROPOSED | `claims/methodology/M-5701-exact-conic-portfolio-search.md` |
| X-5701 | Experiment | Exact conic portfolio checker and synthetic controls | exact algebraic synthetic controls | `experiments/X-5701-conic-portfolio/README.md` |

## Current-state insertion

Issue #57 adds a dual-cone closure above individual finite witnesses. Several
RH-valid scalar or PSD conditions may be combined with exact nonnegative weights
or exact Gram multipliers. A portfolio advances only when its robust worst case
over one shared primitive-feature uncertainty set is strictly negative.

This does not add a counterexample candidate and does not promote any imported
xi, Weil, Loewner, Stieltjes, or arithmetic criterion.

## Dependencies

- stacked on PR #50: D-4501 and support-function witness-survival machinery;
- intended consumers: Issues #39, #41, #42, #47, #55;
- all route-specific logical gates remain at their existing statuses.
