# Registry and blueprint audit

## Publication inventory

The final target head contains both files that were absent from the earlier observed head:

- `formal/registry/deltas/B.tsv`;
- `formal/blueprint/src/content-B.tex`.

`B.tsv` contains 15 data rows. `content-B.tex` contains seven theorem nodes. They are resident, so neither is classified as missing publication.

## Registry findings

The conservative rows for the unfinished wavelet and half-divisor packets are appropriate: the generic finite algebra does not promote the full canonical claims. The rows for fixed rows 2/3 and the 5:3 numerator match the reviewed finite algebra, subject to independent compilation.

Three statuses are too strong:

1. `ARITH.SHARP.SEQUENTIAL_FIRST_OWNER = PROVED` maps a generic list identity to the much richer L-99601 source theorem.
2. `ARITH.SOURCE.TYPING_FIREWALLS = PROVED` maps role tags and toy witnesses to the complete physical source ledger and hostile fixtures.
3. `API.MELLIN.SUBPOWER_NEGATIVE_MASS = PROVED_CONDITIONAL` maps a tautological `consumes` field to the exact Mellin-Landau API.

The dependency `ARITH.XD.SAME_K1_TRANSLATION -> ARITH.XD.OLD_K0_K1_EDGE` should not be interpreted as a proof premise: the latter is a false historical edge that the former supersedes.

No independent run of `generate_registry.py` or `validate_registry.py` was possible. The source rows appear schema-shaped and use canonical semantic IDs, but runtime validation remains an integration gate.

## Blueprint findings

The file is present, but two nodes should be marked `\notready` and narrowed:

- the sequential first-owner node;
- the source-typing firewall node.

The fixed-native consumer declares `\uses{thm:B-five-three-exact}`, although the Lean proof does not use the 5:3 theorem and does not use `data.sourceIdentity`. The dependency graph is therefore inaccurate.

The half-divisor and wavelet nodes correctly use `\notready` for the missing canonical layers.

## Source-lock and report findings

No B-owned declaration-to-source ledger or versioned formal-status report is published. The joined canonical registry can recover one source object per semantic ID, but that is insufficient when a local helper is weaker than the canonical claim to which it is mapped. This is a `SOURCE_LOCK_DEFECT` and an `INCOMPLETE_PUBLICATION` finding.
