# Verification report

The integration was built from frozen main `677203992eb0168920365ee45ae9db76bfa97dcf` and Reviewer D `06c8ea18ffe20c7efa01b0fdacb8ebea0a2b5b22`.

## Local checks

```text
Mellin-Landau consumer:     PASS_MELLIN_LANDAU_CONSUMER
Scientific integration:    PASS_FINAL_SCIENTIFIC_INTEGRATION
RH status:                  UNPROVED
Proven-only path to RH:     false
Targeted review rows:       0
Unresolved conflicts:       0
Heavy campaigns rerun:      false
Family packets:             22
Canonical mirror tables:    9
```

The validators check:

- exact frozen heads and research cutoff;
- required front-door and registry files;
- claim, edge, alias, family, refutation, computation, PR-disposition, conflict, and extraction counts;
- unique semantic identifiers;
- 40-hex source SHAs;
- referentially closed JSON hyperedges;
- explicit open premises on every live edge to RH;
- absence of a reviewed/proven-only path to RH;
- exact PR coverage from #375 through #707;
- zero targeted-review rows;
- zero unresolved review conflicts;
- no heavy campaign marked as rerun;
- byte-identical integration/canonical tables;
- exact family-packet claim coverage;
- fixed Mellin consumer graph typing;
- literal front-door status language.

## Commands

```bash
python3 canonical/consumers/mellin-landau/validate_consumer.py
python3 integration/2026-08-22/validate_integration.py
python3 verification/2026-08-22/run_all.py
```

No heavy computation is invoked by these commands.
