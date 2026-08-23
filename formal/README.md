# Riemann formalization

This directory is an independent Lean 4/Lake project inside the Riemann research repository.
It formalizes the reviewed scientific release at repository commit
`852d8aa05c701ea7818ce8a50543e68987fef5cc` and research cutoff PR #707.

## Literal status

```text
Riemann Hypothesis:       UNPROVED
formal proof of RH:       NONE
reviewed-only path to RH: NONE
trusted custom axioms:    FORBIDDEN
```

The bootstrap establishes infrastructure and trusted statement plumbing. It does not claim that the 139 reviewed scientific claims have already been formalized.

## Build

```bash
cd formal
lake exe cache get
lake build
lake build Solution.RH
python3 scripts/validate_registry.py
python3 scripts/verify_source_locks.py
bash scripts/check_no_sorry.sh
bash scripts/check_axioms.sh
```

## Layers

- `RiemannFormal/Statement/`: canonical propositions, release metadata, and open-cut identifiers.
- `RiemannFormal/Upstream/`: Mathlib/Zeta23 bridges and source locks.
- `RiemannFormal/Analysis/`: analytic infrastructure owned by Formalization Reviewer A.
- `RiemannFormal/Arithmetic/` and `MellinLandau/`: arithmetic and fixed-detector work owned by Reviewer B.
- `RiemannFormal/Operator/` and `Refutations/`: operator algebra and formal firewalls owned by Reviewer C.
- `comparator/`: trusted Mathlib-only statements and sorry-free solution modules.
- `registry/`: the exact semantic-ID/formal-status map.
- `Experimental/`: incomplete work excluded from trusted default targets.

## Source policy

The scientific registry is `../canonical/2026-08-22/claims.tsv`. Formal status is tracked separately. A compiled theorem with an explicit open hypothesis is `PROVED_CONDITIONAL`, not `PROVED`.
