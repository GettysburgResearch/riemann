# Integrator patch proposed by gpt56-04-c

This file is an integration proposal only and does not directly modify root
registries.

## CLAIMS additions

| ID | Type | Status | Summary | Issue |
|---|---|---|---|---|
| L-2801 | Lemma | PROPOSED | Exact compact Toeplitz formulas for D-0801 archimedean and pole corrections | #28 |
| L-2802 | Lemma | PROPOSED | Universal rational high-carrier correction budget | #28 |
| O-2801 | Observation | PARTIAL | At the PR #44 target, all omitted exact corrections are below `1/750000` | #28 |
| X-2801 | Experiment/checker | PARTIAL | Exact rational correction checker and independent formula controls | #28 |

## OPEN_PROBLEMS update

For the optimized piecewise-carrier basin, replace “derive exact
archimedean/pole blocks” by:

1. independently review L-2801/L-2802;
2. certify the frozen-vector complete prime margin with directed phase balls;
3. separate that interval from zero by `1/750000`;
4. complete the admissibility and explicit-formula normalization audit.

## NEGATIVE_RESULTS addition

At `c=10^11`, `K=1024`, and `T=4709203636353.65`, the exact omitted
archimedean-plus-pole correction is universally bounded by approximately
`1.23703e-6`. PR #44's leading value remains empirical, so this is not a proof
of positivity. It does show that direct exact correction quadrature is not the
dominant unresolved error at that cell.

## Candidate registry

No addition. No negative complete interval exists.
