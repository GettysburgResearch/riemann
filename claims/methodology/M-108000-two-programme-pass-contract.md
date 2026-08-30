# M-108000 — Contract for the 2026-08-30 two-programme discovery pass

```text
Claim ID: M-108000
Status:   METHODOLOGY (governs claims T/L/R/O-1080xx and T/L/R/O-1085xx)
Created:  2026-08-30
Depends on: issues #763 (Riemann Structures), #764 (Generalized L-Objects)
RH status: RH and GRH are unproved; nothing in this pass claims otherwise.
```

## Scope and identity

First Gate-0 research pass jointly covering programme #763 (upstream
structures and mechanisms) and programme #764 (deformations, moduli,
rigidity of generalized L-objects). Claim bands: **1080xx = #763**,
**1085xx = #764** (bands through 107xxx are in use by other lanes; verified
free at pass start). One branch, one PR; per-programme reports under
`reports/claude/`; shared substrate under
`research/exploratory/2026-08-30-two-programme-pass/`.

## Rigor vocabulary (as used in every cell and claim of this pass)

- `PROVED_HERE` — complete proof in this deposit; every finite computation
  backing it is exact (`fractions.Fraction` or exact symbolic algebra) and
  replayable.
- `IMPORTED_THEOREM` — a known theorem used as input, with attribution;
  if the exact attribution is uncertain the citation slot reads
  `CITATION-NEEDED: <description>` and the claim's validity must not depend
  on the attribution's precision.
- `EXACT_WITNESS` / `REFUTED_BY_WITNESS` — a finite exact object deciding a
  cell (the witness is embedded or path-referenced).
- `NON_DIRECTED_HIGH_PRECISION` / `FLOATING_RECONNAISSANCE` — numerics with
  stated precision; conjecture-generating evidence ONLY; never decides a
  HOLDS/FAILS cell and never yields a zero theorem.
- `SYNTHETIC_CONTROL` — an engineered object whose role is calibration or
  counterfeit testing.
- `OPEN` — believed-relevant but undecided; in particular, nonexistence
  claims that are hard (e.g. "no functional equation exists") stay OPEN
  unless a proof is deposited.

## Firewalls instantiated for this pass

1. No relabeling: an RH-equivalent estimate is not "structure"; nothing in
   this pass shortens the distance to RH and no claim may suggest it does.
2. No zero theorems from plots or finite precision (issue #764 firewall);
   every Epstein-lab statement is a located-numerically statement with
   stated dps.
3. No fabricated attributions: uncertain attributions are CITATION-NEEDED
   and are gated by the boundary audit
   (`research/exploratory/2026-08-30-two-programme-pass/BOUNDARY_AUDIT_CONSOLIDATED.md`);
   known results are imported as known, never advertised as new.
4. Novelty discipline: each claim carries a "novelty position" paragraph
   stating what is classical, what is repackaged, and what is believed new,
   with the boundary-audit verdict referenced.
5. Sibling independence (both issues): #763 material may not assume #764's
   desired conclusions and vice versa; shared artifacts (the worlds corpus)
   carry per-cell provenance so each programme consumes only labeled facts.
6. A finite computation is never promoted to an unbounded conclusion; a
   family/moduli scan is never called a classification.
7. Every JSON artifact of this pass embeds `"rh_established": false`.

## Promotion standard (target, from the issues)

An object or mechanism claim is promotion-grade when an independently
defined object explains at least two genuinely different phenomena and
survives at least one held-out prediction or counterfeit test. Cells and
claims below that bar are exploratory and labeled so.
