# Riemann formalization

This nested Lean project contains the formalization track for the Riemann
Agentic Polymath repository.

**Current release: formal-v0.1. The Riemann Hypothesis remains unproved.**

Start here:

1. [`FORMAL_V0_1.md`](FORMAL_V0_1.md) — release scope, provenance and exact status;
2. [`RESULTS.md`](RESULTS.md) — strongest unconditional and conditional results;
3. [`OPEN_GATES.md`](OPEN_GATES.md) — missing analytic, arithmetic and operator inputs;
4. [`TRUST.md`](TRUST.md) — Challenge/Solution, no-sorry and axiom boundaries;
5. [`registry/FORMAL_V0_1_MANIFEST.json`](registry/FORMAL_V0_1_MANIFEST.json) — machine-readable locks;
6. generated `registry/FORMALIZATION_MAP.tsv` — all 139 canonical semantic claims.

## Exact build

From the repository root:

```bash
cd formal
lake exe cache get
cd ..
bash formal/scripts/run_formal_v0_1_release.sh
```

The release runner performs:

- the trusted Lean build;
- all seven Challenge/ChallengeDeps/Solution comparator builds;
- exact Challenge/Solution theorem-type comparison;
- canonical registry, source-lock and blueprint validation;
- the trusted no-sorry/custom-axiom boundary;
- the complete fail-closed axiom audit;
- the formal-v0.1 manifest and release-front-door checks.

It does not run distributed mathematics or any historical heavy numerical
campaign.

## Scientific boundary

The formal library contains genuine unconditional finite algebra and genuine
conditional implications. A conditional theorem concluding RH is not an
unconditional proof: the tail-Mellin Landau, negative-mass holomorphy and
fixed arithmetic producer estimates remain explicit inputs.

The actual-Xi order-three theorem likewise remains conditional and concludes
positive semidefiniteness through order three only.

Research after PR #707 is excluded from formal-v0.1. It may enter a later
release only after scientific review and canonical integration.
