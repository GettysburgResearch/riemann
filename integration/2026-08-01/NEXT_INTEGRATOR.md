# Handoff to the next integrator

## Authoritative state

Use this directory as the cutoff authority:

- cutoff: `2026-08-01T21:35:52Z`;
- base `main`: `d7fe83f463a2416faa4279cfb406f7283aa34b2c`;
- exact source review heads: `PR_LEDGER.md` / `pr-ledger.json`;
- canonical packet candidates: `../../canonical/registry.yaml`;
- collision records: `../../canonical/aliases.yaml`.

Do not use commit timestamps to replace an exact review-recorded SHA.

## First merge/extraction order

The following is a recommended order, not an automatic merge command.

### 1. Reviews, corrections, and refutations

Process #140, #141, #173, and review-only #212 before the claims they correct. Their value is repository-wide: they block local-to-global overreach, wrong Hermite inertia, inconsistent targeted-Li coefficients, hard-window artifact promotion, and false gap-parity statements.

### 2. Independent finite arithmetic foundations

Extract #24 and #40. Preserve Robin's source-qualified imported equivalence and the finite endpoint of every computation.

### 3. Shared finite ξ algebra

Extract #48 and #52, followed by finite positive controls #68 and #71. Apply the listed normalization and provenance fixes before integrating dependent branches.

### 4. Finite production artifacts

Extract #65 as one exact finite positive carrier certificate and #105 as a finite direct-ξ/zero-deflation production packet. Do not use either as evidence for RH.

### 5. Finite operator-algebra spine

Process #150, #168, #169, #192, #199, #204, and #206 in dependency order. The finite algebra is reusable. Preserve the corrected-kernel cofinal sign as open.

### 6. Canonical positive-anchor theorem

Use #134 as the preferred one-node one-scalar form. Extract the genuinely additional multi-anchor adapter from #132 and the distinct segment-budget contribution from #133 after collision aliases are allocated.

## Repairs that should precede broad carrier or localized-Weil integration

1. **D-0001 / PR #4:** primary-source dictionary, admissibility, sign, normalization, and artifact/source correspondence.
2. **PR #91:** closed-form/form-core repair.
3. **PR #144:** genuine dense-refinement/form-density hypothesis.
4. **PR #177:** endpoint-domain repair.
5. **PR #181:** complete zero-shell enforcement and source authentication.
6. **PR #200:** new outward-serialized interval artifact; the retained interval is invalid.
7. **PR #211:** recover the missing archive segment and replay the complete bundle.
8. **PRs #152/#158/#163/#164:** namespace, source-domain, and cofinal-scope extraction rather than whole-branch merge.

## Known directly refreshed post-review deltas

These present heads were directly observed and differ from the review-recorded frozen heads. The old verdict does not extend to the delta.

| PR | Reviewed head | Directly refreshed present head | Initial delta interpretation |
|---:|---|---|---|
| #158 | `e2b67e5ecfe3c6742086558a792fb61766a4ce4c` | `0965166d9b12bec576d7728793d9c2542364f2c1` | Later audit/review material and branch additions; classify separately. |
| #164 | `e2e8a23f860184ce66d24ea75b04ca8a57a4b6a3` | `a46b6bb9269b46caa205aebe50a7f19ccc9d86da` | Contains the review batch report and later changes. |
| #165 | `3a4c4f77271596fef6af4aa7262503c7cde28cc0` | `c3c6c98a580277e22a04790222989bf3816f2ef2` | Contains the later review report; do not extend theorem verdict automatically. |
| #191 | `be7118ea650ccbed82f036d23e5b329d5957a8b3` | `27bb5dcd7a0a1739eeaa26ad97f12eb0a14bc19b` | Later review-report and finite-ladder changes. |
| #200 | `ceb4378a166680db73d840e1aeba6f216db6b6a9` | `7162c2a221fd87e6e7baf4e7245d6f42b5e04de3` | Review report added after the invalid serialized interval. |
| #202 | `f675940e8f493b5cfc1166af0398577078be2d61` | `d29dd935958d88560d73b1865185972ec06f1011` | Later review-report commit; mathematical delta needs classification. |
| #208 | `f3b5a9cad45f352c79236b9966aa3f7c117de33b` | `43b1c54187dd0abdc4cbc34fa1a692b25fbe92cf` | Later review report and branch changes. |
| #211 | `54c884c3dccb8618b706ae3d7bdd6edf47c59bc9` | `d1cf0320fb80dbe4d39e0e36d1c8af69bdcf3ff6` | Later review report; missing archive segment remains a blocker. |
| #212 | `88617ac916d3df6e61ec5b4726e866743b8fc4a3` | same | Review-only PR. |

The next pass must directly refresh every other present head before making a complete frozen/current table. A blank present-head entry in this snapshot is intentional uncertainty, not an assertion of equality.

## Post-cutoff PRs and commits

PR #213 is post-cutoff and contains this integration snapshot. Agents may have pushed additional commits after the cutoff. Classify each delta by:

- editorial;
- review-only;
- proposed connection;
- new mathematics;
- artifact change;
- repair;
- unknown.

A review-only commit may be integrated as review evidence without extending the source theorem verdict. New mathematics always requires a new exact-SHA review.

## What remains incomplete in this pass

- present head SHAs were not individually refreshed for every cutoff PR;
- source theorem bodies were not cherry-picked or mechanically extracted;
- large artifacts were not downloaded or independently replayed;
- no expensive special-function, zero, prime, spectral, or interval computation was rerun;
- canonical packet entries are metadata-level candidates, not final merged theorem files;
- unresolved claim-ID collisions have been recorded but not all assigned final canonical IDs;
- external primary-source audits remain where the review reports say they remain.

These are explicit boundaries, not hidden work.

## Updating the snapshot efficiently

1. Copy `pr-ledger.json` into a new timestamped integration directory.
2. Directly query the open PR list and present head SHA for every row.
3. Compare present head with the review-recorded SHA.
4. Fetch only changed files for delta classification.
5. Reuse the exact old review when the source SHA is unchanged.
6. Review only new mathematical/artifact deltas.
7. Append aliases and registry records; never rewrite old identities.
8. Update root README only if stable navigation or process has changed.
9. Leave a new handoff rather than editing this one as though the cutoff moved.

## Normal lightweight checks

Run:

```bash
python scripts/integration/validate_integration.py
```

Then check:

- JSON and schema parsing;
- exactly 127 cutoff rows and 126 review verdicts;
- aggregate `29 / 55 / 39 / 3`;
- unique PR numbers and canonical IDs;
- full 40-hex reviewed SHAs;
- no PR #213 inside the cutoff population;
- append-only alias identities;
- valid internal paths;
- no claim status broadened beyond its review;
- no artifact called immutable merely because its hash is known or its Actions retention has not expired.

## Suggested first research-facing questions after integration

1. Can D-0001 be reconstructed independently from the primary finite Guinand–Weil source and released code?
2. Can one repaired pole-free prime cell be replayed end-to-end with outward intervals and complete zero-shell coverage?
3. Can the complete-kernel programme prove an actual zeta-specific weighted trace or joint corrected-residual bound?
4. Which direct-ξ primitive enlargement escapes the exact feasible-anchor closure of the current table?
5. Can the #53 Robin terminal stream be independently regenerated and replayed?

Answering any one of these would materially improve the next integration pass without repeating the full review wave.
