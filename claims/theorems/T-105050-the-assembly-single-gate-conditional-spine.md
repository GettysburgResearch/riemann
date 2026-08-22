# T-105050 — The assembly: the review-wave open core is a single-gate conditional spine, and each of seven gates alone implies RH

Claim ID: `T-105050`
Status: **PROVED GRAPH-ASSEMBLY THEOREM (conditional spine over independently reviewed edges) — RH ITSELF UNPROVED AND NOT CLAIMED**
Created: 2026-08-22
Agent: swarm lane A1 (assembly graph + fail-closed validator)
Replay: `experiments/X-105050-assembly/` (`assembly_graph.json`,
`build_graph.py`, `validator.py`, `verdict.json`, `recorded_checks.json`,
`REPORT.md`, `mutation_test/`, plus the link audit `LINK_AUDIT.md` /
`link_audit_verify.py` / `link_audit_results.json`). Contract: `M-105055`.
Companions in this deposit: `T-105051` (graded dial), `L-105052` (VK
envelope), `L-105053` (near-coprime core), `O-105054` (wall + mechanism).
RH status: **unproved — this file proves only conditional implications and
their machine-checked closure; the validator ASSERTS that no proved-only
path to RH exists.**

## 1. Statement

Let the 2026-08-21/22 review wave be frozen at:

- Reviewer A packet: `origin/review/2026-08-21/arithmetic-native-implication`
  @ `55fe0b6f23d9163e2b602608da84194ba243d7c4` (ledger
  `review/2026-08-21/arithmetic/CLAIMS.tsv`, routes
  `review/2026-08-21/arithmetic/ROUTE_EDGES.tsv`);
- Reviewer B cross-review: `origin/review/2026-08-22/reviewer-b-cross-review-a`
  @ `945a6eec3406cce8f6cd63eba6c69fb60676c41d`;
- Reviewer C coverage: `origin/review/2026-08-22/coverage-genealogy-delta`
  @ `a520556ac7f30290a11e1fcba7b6f6a24269153e`.

**(a) The gate lattice.** The open core of the reviewed transport program is
the following set of seven open gate hypotheses, each registered
`OPEN_SUFFICIENT_FOR_RH` (or the declared hypothesis string of a registered
route edge), together with one intermediate interface (`ROWS23`):

`HHFE102010`, `HCNC103100`, `CFBB102100`, `BPOE103300`, `FCHD67`,
`WX53POS` (five-three scalar positivity), `HNM67` (subpower negative mass),
and the intermediate `ROWS23` (rows 2,3 eventually nonnegative).

**(b) Single-gate sufficiency.** Through edges every one of which is
independently reviewer-registered (Section 3), **each gate alone implies
RH**: the minimal open cut of the assembly graph has cardinality **1**, and
every singleton `{gate}` is a solution (validator result (iii)).

**(c) The spine `RH <= HHFE102010`.** The distinguished gate is:

> **HHFE102010.** Let `eta` be the multiplicative function with
> `sum_{k>=0} eta(p^k) z^k = (1-z)^{-1/2}` (so `eta(p^k) = binom(2k,k)/4^k`,
> `eta * eta = 1` in Dirichlet convolution, and the Dirichlet series of
> `eta` is `zeta(z)^{1/2}`). Let `b_U(n) = mu(n) 1_{n>U}`,
> `h_U = b_U * eta`, `A_-(y) = 1` on `(1,2)`, `-sqrt(2)` on `(2,4)`, `0`
> else, `H_{U,-}(Y) = sum_n h_U(n) n^{-1/2} A_-(Y/n)`,
> `H_U(X) = int_U^{4X/U} |H_{U,-}(Y)|^2 dY/Y`, and `U_X = floor(X^{1/3})`.
> Then the gate asserts:
>
> `int_{2^L}^{2^{L+1}} H_{U_X}(X) dX/X = 2^{o(L)}` as `L -> infinity`.
>
> **If HHFE102010 holds, then RH holds** (sharp transfer
> `|B_U(X)| <= 3 H_U(X)`, T-102001.6, then the Type-I + Mellin–Landau
> consumer BVD100310).

Equivalent form after the proved subpower diagonal (`L-103101`,
`L-103102`): `HHFE102010 <=> HCNC103100`, where
`HCNC103100`: `int_{2^L}^{2^{L+1}} [O_{U_X,N_X}]_+ dX/X = 2^{o(L)}` with
`O_{U,N} = sum_{U<m,n<=N, m != n, 1/4<m/n<4} h_U(m) h_U(n) (mn)^{-1/2}
R(log(m/n))`, `R` the explicit even piecewise-linear ratio-four
autocorrelation of `A_-` (L-103100.2), `N_X = floor(X/U_X)`. By
Mellin–Plancherel (L-103102.1) the gate energy equals
`(1/2pi) int_R |hat A_-(i gamma)|^2 |P_{U,N}(1/2 + i gamma)|^2 d gamma`,
`P_{U,N}(z) = sum_{U<n<=N} h_U(n) n^{-z}` — a compactly weighted finite
fractional Nyman–Beurling error (`zeta^{-1/2}` vs `M_U zeta^{1/2}`).

**(d) Gate partial order (proved implications among gates).** Through
reviewer-backed edges only:
`BPOE103300 => HHFE102010 <=> HCNC103100`, and `FCHD67 => ROWS23`.
Adding the deposit-only composition `T-102110` (no ledger row — see
Section 4): `HCNC103100 => CFBB102100` (zero matrix), completing
`BPOE -> HHFE <-> HCNC -> CFBB`. `WX53POS`, `HNM67` and (reviewer-backed)
`CFBB102100` are incomparable islands; every gate `=> RH`.

**(e) Verified closure.** Every non-gate edge input is a claim verified in
Reviewer A's `CLAIMS.tsv` (status `VERIFIED` or `VERIFIED_WITH_FIXES`, the
latter with its required fix carried verbatim in the graph), or a proved
exact conditional theorem whose only open input is the gate on the same
edge. The fail-closed validator checks structure and provenance (40-hex
SHAs, path-at-commit existence via `git cat-file`) BEFORE reachability and
asserts: **proved-only reachability does not reach RH** (Reviewer B's
sanity result reproduced), every gate alone reaches RH, and the minimal
open cut is a single gate.

## 2. The graph (nodes)

41 nodes: 32 claims, 8 hypotheses, 1 terminal (`RH`). Full four-coordinate
inventory in `assembly_graph.json`; the load-bearing claim rows:

| node | status | source (claim_id, path, branch, sha) |
|---|---|---|
| L-99601 | VERIFIED | `L-99601`, `claims/lemmas/L-99601-sequential-first-owner-euler-hazard.md`, `origin/review/gpt56-pro/99600-three-interface-hostile-audit`, `24ab64551225f2dba9aa53a533eb9b0285c6e363` |
| R-99600 | REFUTED (firewall) | `R-99600`, `claims/refutations/R-99600-alpha-child-hazard-is-not-the-native-euler-source.md`, same branch, `24ab6455...c363` |
| L-99602 | VERIFIED_WITH_FIXES | `L-99602`, `claims/lemmas/L-99602-exact-two-row-mellin-landau-consumer.md`, same branch, `24ab6455...c363` |
| L-99261 | VERIFIED | `L-99261`, `claims/lemmas/L-99261-five-three-row-zero-free-mellin-witness.md`, `origin/research/gpt56-pro/99260-three-vulnerability-hardening`, `433fd3662f7b2e4ba384ce64f196380e88624090` |
| L-99270 | VERIFIED_WITH_FIXES | `L-99270`, `claims/lemmas/L-99270-zero-free-smoothing-and-negative-mass.md`, `origin/review/gpt56-pro/99270-three-vulnerability-hardening`, `e928fd615d753882706bb88c51b717bd8d4a86ba` |
| L-99272 | VERIFIED_WITH_FIXES | `L-99272`, `claims/lemmas/L-99272-specialized-landau-and-scalar-firewall.md`, same branch, `e928fd61...86ba` |
| L-99282 | VERIFIED_WITH_FIXES | `L-99282`, `claims/lemmas/L-99282-holomorphic-perturbation-landau-transfer.md`, `origin/review/gpt56-pro/99280-triad-hardening`, `3f9e80f09fe1f595927ea7dce6fb49ac68c5c21b` |
| L-99281 | DEPOSITED_UNREVIEWED | `L-99281`, `claims/lemmas/L-99281-subpower-defect-resolvent.md`, same branch, `3f9e80f0...c21b` |
| L-102001 / L-102009 / L-102010 / T-102001 | V / V / VWF / COND_EXACT | PR 696, `origin/research/gpt56-sol/102000-parabolic-bessel-vaughan-correction`, `f4016db548afceb31b150547cb6cd48b4cddb77d` |
| L-103100 / L-103101 / L-103102 | V / V / COND_EXACT | PR 702, `origin/research/gpt56-pro/103100-fractional-hankel-near-collision`, `89f995450977c3590aada0c1447a7e6af7fcd9ac` |
| L-102100 / L-102103 / L-102105 / T-102100 / T-102110 | V / V / VWF / COND_EXACT / DEPOSITED_UNREVIEWED | PR 703, `origin/research/gpt56-pro/102100-carrier-free-staircase-matrix`, `0a46dba5c74e573945e3612937606f6ca735a1d3` |
| L-103300 / L-103303 / L-103304 / T-103300 | V / V / V / COND_EXACT | PR 707, `origin/research/gpt56-pro/103300-balanced-phase-gram`, `7bf3308d40ac8ed1ba50e404ff6e9c47526d89e4` |
| L-100310 / L-100311 / L-100312 | DEPOSITED_UNREVIEWED | PR 685, `origin/research/gpt56-pro/100300-two-route-endgame`, `4f69b7656f42dcb5ff250d13adc9f88e8d18f315` |
| T-105000 / O-105010 / L-105031 / L-105032 / T-105040 | DEPOSITED_UNREVIEWED (context only) | `claude/riemann-proof-review-8nz34i`, `e81eaca5c93e833fd465dd3917f9dce03e57fc04` |

Gate hypothesis nodes carry the path of the file that defines them:
`HHFE102010` @ `claims/lemmas/L-102010-half-divisor-symmetric-one-field-reduction.md`
(PR 696 @ `f4016db5...db77d`); `HCNC103100` @
`claims/lemmas/L-103102-fractional-nyman-and-near-collision-equivalence.md`
(PR 702 @ `89f99545...af9ac`, CLAIMS.tsv row 46); `CFBB102100` @
`claims/theorems/T-102100-carrier-free-staircase-perron-frontier.md`
(PR 703 @ `0a46dba5...35a1d3`, row 62); `BPOE103300` @
`claims/theorems/T-103300-balanced-phase-amplitude-and-physical-occupancy-frontier.md`
(PR 707 @ `7bf3308d...d89e4`, row 66); `FCHD67` @
`claims/lemmas/L-99601-sequential-first-owner-euler-hazard.md`
(PR 652 @ `24ab6455...c363`, row 17); `WX53POS` @
`claims/lemmas/L-99261-five-three-row-zero-free-mellin-witness.md`
(PR 649 @ `433fd366...4090`); `HNM67` @
`claims/lemmas/L-99270-zero-free-smoothing-and-negative-mass.md`
(PR 653 @ `e928fd61...86ba`); `ROWS23` @
`claims/lemmas/L-99602-exact-two-row-mellin-landau-consumer.md`
(PR 652 @ `24ab6455...c363`).

## 3. Proof by graph (every edge, four coordinates)

All `ROUTE_EDGES` citations are
(`review/2026-08-21/arithmetic/ROUTE_EDGES.tsv`,
`origin/review/2026-08-21/arithmetic-native-implication`,
`55fe0b6f23d9163e2b602608da84194ba243d7c4`) at the stated line.

1. **E-NATIVE-FCHD** `[L-99601, FCHD67] -> ROWS23`
   (CONDITIONAL_IMPLICATION). Source: ROUTE_EDGES line 6
   (`EDGE.NATIVE.FCHD`, PROVED_CONDITIONAL, verdict CONDITIONAL_EXACT,
   first_missing_input `ARITH.FCHD67`) + `L-99601` §4 @
   `claims/lemmas/L-99601-sequential-first-owner-euler-hazard.md`,
   PR 652 @ `24ab64551225f2dba9aa53a533eb9b0285c6e363`.
2. **E-MELLIN-ROWS23** `[L-99602, ROWS23] -> RH`. Source: ROUTE_EDGES
   line 2 (`EDGE.MELLIN.ROWS23`, CONDITIONAL_EXACT) + `L-99602.1–.6`
   (numerator elimination `P_2, P_3` common-zero-free in `Re z > 0`),
   same PR/SHA. Landau backbone `L-99272` (PR 653 @ `e928fd61...86ba`).
3. **E-MELLIN-FIVE-THREE** `[L-99261, WX53POS] -> RH`. Source:
   ROUTE_EDGES line 3 + `L-99261.4` (numerator
   `-3(2^{-z}-1)(2^{-z}-2)` zero-free in the strip), PR 649 @
   `433fd3662f7b2e4ba384ce64f196380e88624090`.
4. **E-MELLIN-NEGMASS** `[L-99270, HNM67] -> RH`. Source: ROUTE_EDGES
   line 4 + `L-99270.10–.13`, PR 653 @ `e928fd61...86ba` (exact reviewed
   arity 2 preserved; `L-99272` recorded as backbone).
5. **E-VAUGHAN-HALF-FIELD** `[L-102001, L-102009, L-102010] ->
   HHFE102010` (PROVED_REDUCTION — reduction INTO the open interface,
   never establishing it). Source: ROUTE_EDGES line 14, PR 696 @
   `f4016db548afceb31b150547cb6cd48b4cddb77d`.
6. **E-NC-TO-HHFE** `[L-103100, L-103101, HCNC103100] -> HHFE102010`
   and **E-HHFE-TO-NC** `[L-103100, L-103101, L-103102, HHFE102010] ->
   HCNC103100` (EQUIVALENCE_AFTER_DIAGONAL, the two directions of
   ROUTE_EDGES line 15; mechanism `O_+ <= H` and `H <= D + O_+` with
   `D = N^{o(1)}`, `L-103101`/`L-103102`), PR 702 @
   `89f995450977c3590aada0c1447a7e6af7fcd9ac`.
7. **E-HHFE-RH** `[HHFE102010] -> RH`. Source: ROUTE_EDGES line 16
   (`EDGE.HHFE.RH`, OPEN_SUFFICIENT_FOR_RH) + mechanism T-102001.6
   (`|B_U(X)| <= 3 H_U(X)`) @
   `claims/theorems/T-102001-ratiofour-two-field-and-gate.md`, PR 696 @
   `f4016db5...db77d`, + BVD100310 consumer `L-100310..L-100312` @
   `claims/lemmas/L-10031{0,1,2}-*.md`, PR 685 @
   `4f69b7656f42dcb5ff250d13adc9f88e8d18f315` (see Section 4 caveat 3).
8. **E-STAIRCASE-CFBB** `[L-102100, L-102103, L-102105, CFBB102100] ->
   RH` (HYPEREDGE). Source: ROUTE_EDGES line 22 + T-102100.2, PR 703 @
   `0a46dba5c74e573945e3612937606f6ca735a1d3`. (Source premise typo
   `SURVIVAL_COBBOUNDARY` repaired to `L-102100`; defect recorded.)
9. **E-BPOE-HHFE** `[L-103300, L-103303, L-103304, BPOE103300] ->
   HHFE102010` (HYPEREDGE) and **E-BPOE-RH** `[BPOE103300] -> RH`.
   Source: ROUTE_EDGES lines 23–24 + T-103300.4, PR 707 @
   `7bf3308d40ac8ed1ba50e404ff6e9c47526d89e4`.
10. **E-HCNC-CFBB** `[T-102110, HCNC103100] -> CFBB102100`
    (CONDITIONAL_IMPLICATION, trust_mode=deposited). Source: `T-102110`
    (via `L-102106`: `|B_A^dag| + |B_Q^dag| <= C H_U`) @
    `claims/theorems/T-102110-near-collision-incoming-edge-to-the-joint-matrix.md`,
    PR 703 @ `0a46dba5...35a1d3`. NOT reviewer-registered; excluded from
    all strict-mode results.

Reachability closure (validator, both modes): proved-only fixpoint
= the 21 reviewed claims; RH and every hypothesis unreachable. Assuming
any single gate: RH reachable through edges 1–9 alone. QED (as a graph
theorem over the cited edges; nothing more).

## 4. Honest scope (carried verbatim; nothing promoted)

1. **RH is unproved.** Reviewer A REPORT.md @ `55fe0b6f`: "RH remains
   unproved"; "Proven-only path to RH: none". Reviewer B @ `945a6eec`:
   "The strict cross-review parser finds no proved-only path to RH. That
   is a sanity result, not validation of every scientific edge." This
   assembly proves conditional implications only.
2. **VERIFIED_WITH_FIXES caveats (verbatim required fixes):** L-99602
   "Separate convergence from continuation"; L-99270 "State local
   integrability and finite abscissa"; L-99272 "Keep the finite-abscissa
   step explicit"; L-99282 "Defect must stay fixed and signed"; L-102010
   "Keep support truncation before full-line Hardy"; L-102105 "Use
   identical cutoff/source in both coordinates". Per
   CANONICAL_EXTRACTION_PLAN.md: "VERIFIED WITH FIXES material must be
   extracted into a corrected standalone packet rather than imported
   through an unsafe ancestor."
3. **L-100310..L-100312 (BVD100310, PR 685 @ `4f69b765...f315`) have NO
   rows in Reviewer A's CLAIMS.tsv** (`git grep "100310"
   review/2026-08-21/arithmetic/CLAIMS.tsv` @ `55fe0b6f` = 0 matches).
   The implication edge `EDGE.HHFE.RH` IS registered (ROUTE_EDGES line
   16) and REPORT.md lists `HHFE102010` among "valid sufficient open
   conditions", but the three mechanism lemmas are deposit-only; they are
   carried as DEPOSITED_UNREVIEWED and flagged as an integration
   obligation.
4. **L-99281 is not separately rowed** in CLAIMS.tsv; it is verified only
   as an internal step of the PR 650 triad and enters solely via
   L-99282's `H_0` hypothesis. If a producer ever arrives in the
   "nonnegative + holomorphic defect" form, this step needs its own row.
5. **T-102110 unrowed:** the gate-order arrow `HCNC => CFBB` is
   deposit-backed only (trust_mode=deposited); reviewer-backed order is
   `BPOE => HHFE <=> HCNC` and `FCHD67 => ROWS23` only.
6. **T-102001 has no separate ledger row**; the sharp constant 3 is
   endorsed inside ARITH.VAUGHAN.HALF_DIVISOR (row 43: "the two fields
   reduce to one with Hardy norm 3") and Reviewer B VERDICT_DELTA line 24
   ("Hardy norm 3 survives"). The L-102010 file text carries constant 5.
7. **105xxx context nodes** (T-105000, O-105010, L-105031, L-105032,
   T-105040 @ `claude/riemann-proof-review-8nz34i` tip
   `e81eaca5c93e833fd465dd3917f9dce03e57fc04`) are deposited-unreviewed,
   carry zero edges, and are premises of NO RH edge: O-105010's
   architecture selection and T-105040's smooth-half closure are context
   for the gate, not steps toward it.
8. **Firewalls binding any gate proof:** R-99600 (alpha-child promotion
   FALSE — dead edge not reproduced); R-103300 (no invariant-cone or
   regional-absolute substitute for BPOE); "Do not replace by absolute
   correlation" (HCNC, row 46); "No local cone substitute" (CFBB, row
   62); R-102000 (positive spline does not inherit Type-I zero moment);
   Reviewer B: the two-row consumer needs SIMULTANEOUS native fixed-row
   production — "a hypothetical zero may determine which member detects
   it, but may not determine or change the family."
9. **Finite certificates are not global edges** (Reviewer C lifecycle
   rule): L-99252 (10^8 H_67 positivity) and T-99000 remain
   RETAINED_HEAVY_CERTIFICATE, cited nowhere as premises.
10. **Recorded provenance defects** (reported, never silently
    normalized): 39-char SHA in CLAIMS.tsv row CONSUMER.MELLIN.
    ZERO_SAFE_BOX (PROV.A.MISSING_LEADING_E); ROUTE_EDGES line 22 premise
    typo `SURVIVAL_COBBOUNDARY`; missing ledger rows for L-100310..312,
    T-102110, L-99281 (full list in `assembly_graph.json`
    `provenance_defects`).
11. **Statement-precision repair to the gate object (audit finding,
    this deposit — `T-105051` and the link audit).** The literal
    T-102001.5 / L-102010.13 inequality `|B_U(X)| <= 3 H_U(X)` with the
    UNTRUNCATED energy `H_U` has an unjustified step: on the annulus
    `(X/U, 4X/U]` the truncated field of the Hardy argument and the
    untruncated field of L-102010.12 differ, with no pointwise
    domination. The rigorous chain (proved in `T-105051` Step 0, exactly
    implementing the reviewer fix "keep support truncation before
    full-line Hardy") is `|B_U(X)| <= 3 Ht_U(X)` with the
    truncated-field energy
    `Ht_U(X) = int_U^{4X/U} |sum_{U<n<=X/U} h_U(n) n^{-1/2} A_-(Y/n)|^2 dY/Y`.
    The spine's gate is therefore read with `Ht` (GATE in `T-105051`'s
    notation); the untruncated statement stands as deposited but its RH
    edge routes through the repaired object. Numerically the two
    energies track closely and `|B| <= 3 min(H, Ht)` at all samples
    (statement-precision repair, not an observed failure).
12. **Both the truncated and untruncated energies are measured
    essentially FLAT** over `L = 8..26` (fitted block exponents
    0.021/0.042 vs the trivial 2/3 — `T-105051` scope, `O-105054.4`);
    LABELED HEURISTIC evidence the gate is true-shaped; certifies
    nothing.

## 5. Falsifiers

- Any (sha, path) coordinate in `assembly_graph.json` failing
  `git cat-file -e sha:path` falsifies the record (validator fails closed
  before reachability).
- A proved-only path to RH appearing in this graph would falsify the
  assembly's central sanity assert — and would mean either a graph bug or
  an unregistered proof; the validator hard-fails either way.
- A refutation of any cited VERIFIED/VERIFIED_WITH_FIXES row at its
  frozen SHA (per FREEZE.json identity keys) removes the corresponding
  edge; single-gate sufficiency must then be recomputed — in particular a
  refutation of L-103101 (subpower diagonal) severs the
  HHFE <=> HCNC equivalence, and a refutation of T-102001.6/BVD100310
  severs E-HHFE-RH, demoting HHFE from the spine.
- A proof that some gate is FALSE (e.g. `liminf` of the dyadic-block
  energy grows like a power of `2^L`) kills that gate's edges but no
  other gate: the validator's per-gate conditional sets are independent.

## 6. Replay

```
cd experiments/X-105050-assembly
python3 build_graph.py          # regenerates assembly_graph.json
python3 validator.py            # online: verifies all 34 (sha,path) pairs via git, then reachability
python3 validator.py --offline  # fail-closed fallback to recorded_checks.json
# PASS criteria: exit 0; verdict.json .verdict == "PASS";
#   proved_only does not contain RH (either trust mode);
#   conditional_rh true for all 8 hypotheses in strict mode;
#   minimal_open_cut.cardinality == 1 with all 8 singletons;
#   hasse.strict covers == [[BPOE,HCNC-class],[FCHD67,ROWS23]];
#   hasse.deposited adds [HCNC-class, CFBB].
```

Environment: python3 stdlib only; git repo at `/home/user/riemann`
(override with `RIEMANN_REPO`). Deterministic: no timestamps, no
randomness; byte-identical `verdict.json` on repeated runs.
