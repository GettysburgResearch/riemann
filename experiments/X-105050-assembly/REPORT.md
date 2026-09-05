# Assembly-graph validator report (Lane A1)

Verdict: **PASS** (all structural, provenance and reachability checks green — fail-closed `req` checks, immune to `python3 -O`; online git verification mode)

RH status: **UNPROVED**. Proved-only reachability (open/conditional/equivalent/refuted/unreviewed material excluded) does NOT reach RH in either trust mode — matching Reviewer B's strict cross-review parser sanity result (@ 945a6eec).

## Counts
- nodes: 41 (claims 32, hypotheses 8, terminal 1)
- edges: 12
- aliases: 34
- (sha,path) coordinates verified: 34

## (i) Proved-only reachable set (strict)
L-102001, L-102009, L-102010, L-102100, L-102103, L-102105, L-103100, L-103101, L-103102, L-103300, L-103303, L-103304, L-99261, L-99270, L-99272, L-99282, L-99601, L-99602, T-102001, T-102100, T-103300


## (ii) Conditional reachability — gate alone => RH?

| gate | strict (reviewer-backed) | deposited |
|---|---|---|
| HYP.BPOE103300 | True | True |
| HYP.CFBB102100 | True | True |
| HYP.FCHD67 | True | True |
| HYP.HCNC103100 | True | True |
| HYP.HHFE102010 | True | True |
| HYP.HNM67 | True | True |
| HYP.ROWS23 | True | True |
| HYP.WX53POS | True | True |

Every declared gate suffices ALONE, already in strict mode.

## (iii) Minimal open cut
Cardinality **1**. Singleton solutions: HYP.BPOE103300, HYP.CFBB102100, HYP.FCHD67, HYP.HCNC103100, HYP.HHFE102010, HYP.HNM67, HYP.ROWS23, HYP.WX53POS

## (iv) Gate partial order (proved implications between gates)

### strict mode
Equivalence classes: [['HYP.BPOE103300'], ['HYP.CFBB102100'], ['HYP.FCHD67'], ['HYP.HCNC103100', 'HYP.HHFE102010'], ['HYP.HNM67'], ['HYP.ROWS23'], ['HYP.WX53POS']]
Cover relations: [['HYP.BPOE103300', 'HYP.HCNC103100'], ['HYP.FCHD67', 'HYP.ROWS23']]

### deposited mode
Equivalence classes: [['HYP.BPOE103300'], ['HYP.CFBB102100'], ['HYP.FCHD67'], ['HYP.HCNC103100', 'HYP.HHFE102010'], ['HYP.HNM67'], ['HYP.ROWS23'], ['HYP.WX53POS']]
Cover relations: [['HYP.BPOE103300', 'HYP.HCNC103100'], ['HYP.FCHD67', 'HYP.ROWS23'], ['HYP.HCNC103100', 'HYP.CFBB102100']]

Reading: BPOE103300 => HHFE102010 <=> HCNC103100 (strict); HCNC103100 => CFBB102100 only via the unrowed T-102110 (deposited mode); FCHD67 => ROWS23; WX53POS, HNM67, CFBB102100 otherwise incomparable islands; every gate => RH.

## Recorded provenance defects (reported, never silently normalized)

- **PROV.A.MISSING_LEADING_E** — review/2026-08-21/arithmetic/CLAIMS.tsv row CONSUMER.MELLIN.ZERO_SAFE_BOX @ 55fe0b6f23d9163e2b602608da84194ba243d7c4 | observed: 39-character SHA 928fd615d753882706bb88c51b717bd8d4a86ba | disposition: Repaired in this canonical registry only; source review branch untouched (Reviewer C PROVENANCE_DEFECTS.tsv disposition).
- **G-DANGLE.STAIRCASE_TYPO** — review/2026-08-21/arithmetic/ROUTE_EDGES.tsv line 22 @ 55fe0b6f23d9163e2b602608da84194ba243d7c4 | observed: premise name ARITH.STAIRCASE.SURVIVAL_COBBOUNDARY (double B) does not match CLAIMS.tsv semantic id ARITH.STAIRCASE.SURVIVAL_COBOUNDARY | disposition: Repaired to L-102100 in edge E-STAIRCASE-CFBB; defect recorded (Reviewer B G-DANGLE-001 class).
- **LEDGER.MISSING_ROWS.BVD100310** — review/2026-08-21/arithmetic/CLAIMS.tsv @ 55fe0b6f23d9163e2b602608da84194ba243d7c4 | observed: L-100310, L-100311, L-100312 (PR 685 @ 4f69b7656f42dcb5ff250d13adc9f88e8d18f315) have no ledger rows although EDGE.HHFE.RH routes through them | disposition: Nodes carried as DEPOSITED_UNREVIEWED; flagged as an integration obligation.
- **LEDGER.MISSING_ROW.T-102110** — review/2026-08-21/arithmetic/CLAIMS.tsv @ 55fe0b6f23d9163e2b602608da84194ba243d7c4 | observed: T-102110 (HCNC => CFBB composition) has no ledger row | disposition: Edge E-HCNC-CFBB carried at trust_mode=deposited only.
- **LEDGER.MISSING_ROW.L-99281** — review/2026-08-21/arithmetic/CLAIMS.tsv @ 55fe0b6f23d9163e2b602608da84194ba243d7c4 | observed: L-99281 (subpower defect resolvent) not separately rowed; verified only inside the PR 650 triad | disposition: Node carried as DEPOSITED_UNREVIEWED.
