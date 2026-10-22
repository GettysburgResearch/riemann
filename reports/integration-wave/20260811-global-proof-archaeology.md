# Global proof archaeology and genealogy review

**Repository:** `gfreund123/riemann`  
**Role:** repository archaeologist and proof genealogist  
**Authoritative UTC cutoff marker:** `2026-08-10T22:28:10Z`  
**Frozen main:** `d6409319b4041cd09bee85f55a344631508f2501`  
**Review branch:** `review/integration-wave-20260811-archaeology`  
**Verdict:** **No accepted proof of the Riemann Hypothesis is present in the reviewed graph.**

The cutoff marker is the first GitHub-server-stamped review commit; the repository freeze occurred immediately before it. An earlier working note carried an incorrect future UTC label. The SHAs and mathematical conclusions were always frozen to the commits listed here and in the TSV.

This report reconstructs intellectual history rather than duplicating the parallel line-by-line mathematical reviews. It distinguishes a false theorem from a failed proof, a failed example from a closed mechanism class, finite evidence from a cofinal theorem, and an RH-equivalent criterion from an unconditional advance on its missing sign.

## 1. Live-repository finding and movement audit

At cutoff, `main` was exactly:

```text
d6409319b4041cd09bee85f55a344631508f2501
Replace setup placeholder with elementary consolidation status
```

This is an August 8 historical base, not the live scientific state. The live graph was distributed across stacked open PRs through #366. Conclusions were frozen to exact heads, not moving branch names.

Load-bearing inspected heads include:

| PR | Route | Frozen head |
|---:|---|---|
| #247 | Carry/Pascal BTF/MPR | `6c4dadc97db57a3cf352c9f72fab3bedce792382` |
| #292 | GFEP first entrance | `6011cde9ef7467729cc24360372a176b622a5655` |
| #297 | Carry-window Selberg/Kummer | `409e1764fc708f725aae8dcd3fad9b8ae480bea3` |
| #301 | Eta/Pascal closure | `80f25af026da9f967e95c2a1f0fe91c8e95801e7` |
| #302 | Reciprocal-eta/Mersenne | `477b527fb489397eb9e58ed6631be04f5eae00d1` |
| #304 | Terminal cutoff | `78b75fc17e27334a9950018528c1c6e083d74820` |
| #314 | MCF refutation | `f07f44263c3ff4b219918b05cac61a75e18ff773` |
| #315 | Cycle-optimized boundary | `33b312e32818adb78b5bdc78e4c64f1a870b532c` |
| #317 | Eta-core/CEV | `9b49c103ab3bd91724182c4c2fecfe2f0c9cb490` |
| #318 | Corrected Robin fiber | `277bfb19e2e5deed50b5bbc133453b7147046360` |
| #323 | Residue-character firewall | `7182b6162d4015bf732dce434784f990f32c0785` |
| #325 | Q4 reflected/Jordan | `8036edcd8b42f1fb3bbee605a6fae3b22985238d` |
| #329 | SHARP continuum | `219cab4496357867018f300936c877967ac0a81b` |
| #335 | Gamma/Pascal Green | `188bd0362c3a9f88adcbcf5298bf8eeade4016cf` |
| #343 | Raw Brownian/Hermite | `fed85f2969a5ab9f09890cd89bd6b57ff2115320` |
| #347 | Outer `255/256` SHARP | `f70bcda4d04200c96ddf5b74bc65ccb4aa8750ae` |
| #348 | WSTS/z-collapse | `89f0eb418a470d55e945b08daa3d0f0dc2fc7914` |
| #351 | Theta/GFEP bootstrap | `22a94f431d7f4cd87db5f3efdd97b086f8f60183` |
| #352 | Factor-64 endpoint | `906b5a477a1ed7c88a40db7569924f15f3d54b72` |
| #353 | Positive occupancy | `ed566f3198e236c54ba18049181016536f56d456` |
| #356 | GFEP/BTF and finite-policy refutation | `1a60df88aadac731ec32e48a87b74537662114dd` |
| #357 | Corrected Q4 inertia | `a2843d31649822014219a13ec29c70e4a30932cc` |
| #358 | Anthropic zeta-23 import | `6f675e6e49c5b1fee3b1c7fce92331d2bad16948` |
| #359 | Aggregate Q4 proposal | `9ffcb8d3dbc6affd859ea8567a061b71dd0d1e8b` |
| #362 | PIG firewall | `31c57c56c00c0a062a49a126d4e5a68ff28e9fe8` |
| #363 | Coherent Gabor spectrum | `01238699b9ea2844e674f56a965cde79559d770a` |
| #364 | Gaussian pair isolation | `219330bd0441a284fd16ff728dd843a7ee4503ee` |
| #365 | Xi-cardinal capture | `902a4cfeb36392c07878591e4a8381e3f4c7b2db` |
| #366 | Confluent jets | `3dd8184c4e34f3a7ecd2b64597c7737af2b59029` |

The end-of-review recheck found no head-SHA movement in `main`, #356, #362, #365, or #366. PR #365's metadata timestamp changed, but its reviewed head did not.

The full 41-row ledger is `audits/integration-wave/20260811-proposal-genealogy.tsv`.

## 2. Historical integration baselines

### First integration snapshot

`integration/2026-08-01/` froze PRs #1–#127 at final integration commit `d7fe83f56b7784eb3045092b88635e55014b909f`. Its durable conclusions remain sound:

- finite completed-xi identities and determinant/Gram/inertia algebra;
- finite Robin/resolvent/operator computations;
- explicit negative results and scope firewalls;
- exact-SHA and artifact-ledger discipline.

Its unresolved boundaries also remain correct: source normalization, cofinality, Brownian source mismatch, Möbius transfer, and decisive artifact provenance.

### Historical front door PR #214

PR #214, head `99e0c656c7d370ac6fdb7d1944bf6c2becea93d0`, built a durable packetized front door and claimed no RH proof. It is now historical: later open research branches vastly outgrew its 18-family index. Preserve it unchanged; do not rewrite it as though it represented PRs #247–#366.

### PR #44–#63 audit

The pre-public audit identified four recurring failure patterns that later reappear under new notation:

1. verified finite algebra with missing or mistyped production provenance;
2. metadata corrections that propagate bad provenance;
3. duplicate/superseded reviews counted as independent evidence;
4. RH-equivalent front doors treated as closure.

## 3. Chronological project map

### A. Finite xi, Cayley, Robin, and operator packets

The earliest wave produced real finite mathematics: determinant factorizations, Gram inertia, local Cayley signs, finite Robin bounds, resolvent identities, and Schur algebra. PRs #44–#52 require artifact quarantine, not mathematical erasure. PR #54 survives as a compact boundary-current criterion but reaches an RH-equivalence firewall. PR #55 was corrected by #63 and decisively by #318.

### B. Carry/Pascal producer architecture

Exact atomized carry rows, Pascal cycles, Möbius divergence, balanced fragmentation, and Farkas duality accumulated into PR #247's full conditional spine. Bounded-order Abel positivity then failed, motivating PR #292's all-generation first-entrance recombination. PR #301 attempted eta/Pascal/Hausdorff closure; #302 and #304 pursued Mersenne and terminal-cutoff variants.

The central genealogical lesson is salvage after failure:

- fixed-order positivity failed, but Green/entrance identities survived;
- pair-first source typing failed, but the actual-coordinate decoder survived;
- atomic boundary norm was linear, but optimized carry-column mass was polylogarithmic;
- Mersenne-collar saturation failed, but eta resolvents and sparse telescopes survived.

### C. SHARP, Green occupation, and policy selection

PRs #326/#329/#335/#347 identify SHARP, uniform-Pascal Green occupation, the square-root hinge inverse, and a local-versus-tail Möbius inequality as the same canonical object. PR #347 proves a large finite outer band. PR #356 then proves:

- frozen binary–ternary GFEP, producer positivity, and BTF oscillate cofinally;
- every finite stationary fixed-ratio policy lacks a source-independent spectral gap;
- uniform continuum/Pascal policies remove deterministic policy resonances.

Thus finite stationary atomic spectral-gap closure is dead; fragmentation, signed debt, and adaptive/continuum policies are not.

### D. Q4 reflected/Jordan/Hermitian programme

The Q4 family develops compact zero-safe sources, all-pass frames, paired reserves, exact placement, vector Jordan curvature, parity jets, two-state ledgers, and inertia-tolerant aggregation. Its key corrections are:

- scalar diagonal reserve does not imply source-matrix reserve;
- scalar Schur curvature does not control mixed/vector curvature;
- bare charges and currents depend on convolution order;
- trace positivity or small negative inertia does not control a large positive current.

PR #359 proposed a full composition; PR #362 identifies the positive innovation gate as RH-equivalent in the corrected assembly.

### E. Endpoint/WSTS/annular/occupancy programme

WSTS, the endpoint scalar, factor-64 annular filters, positive occupancy, Gamma/Pascal deconvolution, and the complete prime-power gap are transforms or consumers of one prime–radical flux. The durable pieces are exact Mellin symbols, the negative prime-power moat, factor-64 minimality in the phase-blind integer-filter class, the occupancy identity, and the signed packing-score objective. Eventual sign or subquadratic loss remains open and RH-facing.

### F. Anthropic zeta-23, Gabor, and complete-kernel synthesis

The imported theorem is an unconditional zero-proportion result, not RH. Native no-gain theorems close finite co-lattice, coherent same-lattice, and finite no-alias window banks inside the same two-trace architecture. PRs #364–#366 pivot to off-line-pair isolation, Xi-cardinal cofinal capture, and confluent jet renormalization. Finite packet conditioning escapes are largely removed; the arithmetic corrected-kernel floor remains RH-equivalent.

## 4. Proposal/correction/refutation/salvage DAGs

```text
Brownian:
#55 original fiber -> #63 sign/order fix -> #318 corrected fiber
  -> finite reflected-tail domination FALSE
  -> positive-fiber cone closure FALSE
  -> one-fiber theorem survives -> aggregate BACS open
  -> #343 raw Dirichlet/Hermite route open

Carry/GFEP:
#247 BTF/MPR -> fixed Abel mutations FALSE -> #292 GFEP
  -> #351 consolidation -> #356 cofinal frozen-policy refutation
  -> finite-stationary no-gap theorem
  -> adaptive/nonstationary/continuum escape survives

Eta/cutoff:
#301 eta-Pascal -> #303/#312 source corrections -> decoder survives
  -> #304 atomic cutoff -> #305/#308 linear obstruction
  -> #315 optimized outer-band flow -> #317 eta core/CEV open

Mersenne:
#302 reciprocal eta -> exact MCF support menu -> #314 cofinal refutation
  -> unrestricted cycle-optimized flow not refuted

Q4:
#297 finite frame -> #325 Q4 source/state -> #339-#350 placement/source fixes
  -> #357 inertia correction -> #359 full composition
  -> #362 PIG RH-equivalence firewall

Endpoint:
#348 WSTS -> #351 bootstrap -> #352 annular endpoint
  -> #353 positive occupancy/Gamma/complete-gap state

Kernel/Gabor:
#199 corrected-kernel classifier -> #358/#361 zeta-23 import
  -> #360/#363 finite-window no-gain -> #364 pair isolation
  -> #365 Xi-cardinal capture -> #366 confluent jets
  -> arithmetic corrected floor open/RH-equivalent
```

## 5. Salvage dossiers

### Dossier 1 — early finite xi/Gram production

**Proposal:** certified finite zero/Gram/inertia production.  
**PR and reviewed SHA:** #44 `ea290a5363bea44854f8fc57433c45311d5ddaca`, descendants #48/#52.  
**Claimed proof spine:** certified zeros → finite Gram/inertia witness → operator conclusion.  
**First broken or open arrow:** the production source and manifest do not certify the advertised zero data.  
**Failure type:** ARTIFACT OR PROVENANCE FAILURE.  
**Exact refutation or gap:** cited source/table mismatch and no independent resident certification.  
**Surviving independent results:** finite determinant, adjugate, inertia, and rational replay algebra.  
**Later corrections:** #49–#52.  
**Later descendants:** PR #214 operator packets.  
**Possible resurrection:** FINITE REPAIR.  
**Current recommendation:** retain algebra; quarantine production claims.

### Dossier 2 — original Brownian Robin fiber

**Proposal:** Brownian approximants are positive mixtures of good Robin fibers.  
**PR and reviewed SHA:** #55 `a60adc8a6405becdce4e41e7b04731402d0d451e`.  
**Claimed proof spine:** Brownian moments → centered fibers → real spectra → RH.  
**First broken or open arrow:** wrong odd term and ordering sign.  
**Failure type:** SIGN OR NORMALIZATION ERROR.  
**Exact refutation or gap:** #318 derives `cosh(ell z/2)+2z sinh(ell z/2)` and exact aggregate counterexamples.  
**Surviving independent results:** finite approximation and corrected one-fiber Robin theorem.  
**Later corrections:** #63/#318.  
**Later descendants:** #343 raw route.  
**Possible resurrection:** MATRIX / INERTIA REPAIR.  
**Current recommendation:** supersede the original formula; integrate corrected fiber and aggregate question separately.

### Dossier 3 — fixed-order Abel positivity

**Proposal:** bounded smoothing order yields global producer positivity.  
**PR and reviewed SHA:** mutation lineage culminating in #299 `cd45a45b480c35e46317a29e07d73c379af0df27`.  
**First broken or open arrow:** exact negative witnesses at successive low orders.  
**Failure type:** EXACT COUNTEREXAMPLE.  
**Surviving independent results:** exact Abel identities and signed residual decomposition.  
**Later descendants:** #292 all-generation recombination.  
**Possible resurrection:** RECOMBINE BEFORE ABSOLUTE VALUES.  
**Current recommendation:** close bounded-order positivity; retain mutation tests.

### Dossier 4 — frozen GFEP/BTF producer

**Proposal:** frozen half-binary/half-ternary first-entrance source or producer has eventual nonnegative/subpower behavior.  
**PR and reviewed SHA:** #292 `6011cde9ef7467729cc24360372a176b622a5655`; #351 `22a94f431d7f4cd87db5f3efdd97b086f8f60183`.  
**First broken or open arrow:** a near-conservation characteristic pole survives in the actual traces.  
**Failure type:** GENERIC MECHANISM NO-GO.  
**Exact refutation or gap:** #356 proves both signs cofinally and refutes frozen BTF.  
**Surviving independent results:** Green/entrance algebra, top-fifth sign, positive Stieltjes packets, lambda rigidity.  
**Later descendants:** uniform Pascal and adaptive/signed debt.  
**Possible resurrection:** STATE-DEPENDENT POLICY.  
**Current recommendation:** mark frozen targets FALSE; preserve infrastructure.

### Dossier 5 — eta/Pascal/Hausdorff closure

**Proposal:** positive triangular eta/Pascal matching with polylog debt.  
**PR and reviewed SHA:** #301 `80f25af026da9f967e95c2a1f0fe91c8e95801e7`.  
**First broken or open arrow:** scalar jets lose node labels; noncoprime tensorization is false.  
**Failure type:** SOURCE-TYPING ERROR.  
**Exact refutation or gap:** wrong-series, reverse-flow, non-Hausdorff, and tensorization witnesses.  
**Surviving independent results:** modal decomposition and exact actual-coordinate Möbius decoder.  
**Later corrections:** #303/#312.  
**Later descendants:** #304/#315/#317.  
**Possible resurrection:** CHANGE OF SOURCE.  
**Current recommendation:** promote the decoder; archive the positivity composition.

### Dossier 6 — terminal cutoff atomic lift

**Proposal:** polylogarithmic divisor-source atomic norm closes the cutoff.  
**PR and reviewed SHA:** #304 `78b75fc17e27334a9950018528c1c6e083d74820`.  
**First broken or open arrow:** a macroscopic quotient band forces linear weighted norm.  
**Failure type:** EXACT COUNTEREXAMPLE.  
**Surviving independent results:** adjacent commutator, exact shift terminalization, positive outer-band flow, polylog column mass.  
**Later corrections:** #305/#308/#315/#317.  
**Possible resurrection:** CHANGE OF NORM.  
**Current recommendation:** forbid atomwise norms before destination recombination.

### Dossier 7 — Mersenne-collar fragmentation

**Proposal:** eventual exact saturation by a fixed MCF support menu.  
**PR and reviewed SHA:** source #302; refutation #314 `f07f44263c3ff4b219918b05cac61a75e18ff773`.  
**First broken or open arrow:** nonreal eta poles force sign changes.  
**Failure type:** GENERIC MECHANISM NO-GO.  
**Surviving independent results:** eta inverse, Mersenne localization, finite isolated feasibility.  
**Possible resurrection:** NONE for the stated support menu.  
**Current recommendation:** close exact MCF; do not generalize to adaptive support.

### Dossier 8 — radix-five/eta contraction

**Proposal:** finite residue or strict eta contraction closes the principal Möbius state.  
**PR and reviewed SHA:** #323 `7182b6162d4015bf732dce434784f990f32c0785`.  
**First broken or open arrow:** nonprincipal Dirichlet-L channels are present; eta is neutral at zeta-zero modes.  
**Failure type:** SOURCE-TYPING ERROR.  
**Surviving independent results:** character decomposition, low-frequency contraction, dyadic uniqueness.  
**Possible resurrection:** CHANGE OF SOURCE.  
**Current recommendation:** make the character firewall mandatory.

### Dossier 9 — Q4 scalar Schur/source-order shortcuts

**Proposal:** scalar reserve/Schur curvature controls compact Q4 current.  
**PR and reviewed SHA:** #345 `36e0b71f27798835e622a0646474ff24064ca62a`; source formulas #346.  
**First broken or open arrow:** diagonal/trace data do not control mixed vector curvature; convolution order was wrong.  
**Failure type:** SCALAR / MATRIX SCOPE ERROR.  
**Exact refutation or gap:** #345/#349/#350 exact countermodels and corrections.  
**Surviving independent results:** zero-bare source, vector Jordan curvature, parity frame, corrected moat.  
**Possible resurrection:** MATRIX / INERTIA REPAIR.  
**Current recommendation:** retain corrected vector packets only.

### Dossier 10 — aggregate Q4 inertia composition

**Proposal:** aggregate negative-inertia control removes the current and closes RH.  
**PR and reviewed SHA:** #359 `9ffcb8d3dbc6affd859ea8567a061b71dd0d1e8b`.  
**First broken or open arrow:** negative spectral mass does not bound positive innovation.  
**Failure type:** MISSING LOAD-BEARING THEOREM.  
**Exact refutation or gap:** #357 supplies a scope counterexample; #362 proves PIG RH-equivalent.  
**Surviving independent results:** aggregate determinant/current elimination and negative-inertia estimates.  
**Possible resurrection:** DIFFERENT CONSUMER.  
**Current recommendation:** reject the composition; preserve the inertia theorem and firewall.

### Dossier 11 — factor-64 endpoint criterion

**Proposal:** a minimal phase-blind annular filter has unconditional eventual negative sign.  
**PR and reviewed SHA:** #352 `906b5a477a1ed7c88a40db7569924f15f3d54b72`.  
**First broken or open arrow:** the sign is not proved and is RH-equivalent.  
**Failure type:** RH-EQUIVALENCE FIREWALL.  
**Surviving independent results:** zero-safe filter, declared-class minimality, Bernstein certificates, negative moat.  
**Later descendant:** #353 occupancy state.  
**Possible resurrection:** DIFFERENT CONSUMER.  
**Current recommendation:** retain as compact front door, not closure.

### Dossier 12 — finite stationary fragmentation class

**Proposal:** a finite stationary fixed-ratio policy has a source-independent spectral gap.  
**PR and reviewed SHA:** #356 `1a60df88aadac731ec32e48a87b74537662114dd`.  
**First broken or open arrow:** simultaneous phase recurrence produces zeros arbitrarily close to conservation.  
**Failure type:** GENERIC MECHANISM NO-GO.  
**Surviving independent results:** policy characteristic calculus and uniform-Pascal escape.  
**Possible resurrection:** CONTINUUM RATHER THAN FINITE-ATOMIC POLICY.  
**Current recommendation:** register the dead class and explicit escape categories.

### Dossier 13 — finite window-bank gain

**Proposal:** finitely many coherent/co-lattice/no-alias windows improve the zeta-23 two-trace constant.  
**PR and reviewed SHA:** #358/#360/#363.  
**First broken or open arrow:** the bank collapses to one aggregate profile or the same nonzero spectrum.  
**Failure type:** GENERIC MECHANISM NO-GO.  
**Surviving independent results:** alias variables, pair spectrum, growing-bank frontier.  
**Later descendants:** #364–#366.  
**Possible resurrection:** NONSTATIONARY POLICY.  
**Current recommendation:** close finite variants; retain growing irregular/prime-resonant consumers.

### Dossier 14 — corrected-kernel completion

**Proposal:** finite pair isolation plus Schur correction supplies a nonnegative arithmetic floor.  
**PR and reviewed SHA:** #199 `4158e0d3e7f91829a6c545308605ea8177023aa3`; descendants #364–#366.  
**First broken or open arrow:** the arithmetic floor is the remaining RH-equivalent sign.  
**Failure type:** RH-EQUIVALENCE FIREWALL.  
**Surviving independent results:** Xi-cardinal source, finite Gabor capture, confluent jet positivity, exact classifier.  
**Possible resurrection:** DIFFERENT CONSUMER.  
**Current recommendation:** separate zero-side capture from arithmetic-side floor.

## 6. Ten most valuable salvage packets

1. Finite completed-xi determinant/Gram/inertia algebra.
2. Corrected one-fiber Brownian Robin classification.
3. Exact actual-coordinate Möbius boundary decoder.
4. Linear atomic obstruction together with optimized carry-column salvage.
5. Markov occupation and policy-drift duality.
6. Finite-stationary no-gap theorem plus uniform-Pascal escape.
7. Corrected Q4 source/frame/vector-curvature packet.
8. Endpoint positive occupancy, Gamma bridge, and prime-square moat.
9. Xi-cardinal cofinal finite-packet capture.
10. Confluent finite-cluster jet renormalization.

Additional valuable packets include lambda rigidity, outer `255/256` SHARP, exact eta/Mersenne telescopes, negative-notch finite-block firewalls, and window-bank no-gain theorems.

## 7. Genuinely dead mechanism classes

Only theorem-level or exact class-wide closures are listed:

1. finite stationary fixed-ratio fragmentation with source-independent spectral gap (#356);
2. frozen binary–ternary GFEP/producer/BTF (#356);
3. exact eventual MCF support menu (#314);
4. declared finite-update uniform `C/m` reservoir mechanism;
5. finite corrected-Robin reflected-tail domination (#318);
6. arbitrary positive superposition closure of good Robin fibers (#318);
7. strict complete eta contraction in a norm containing zeta-zero modes (#323);
8. zeta-only source-free radix-five closure (#323);
9. scalar compact-Q4 Schur shortcut (#345);
10. inference from small negative inertia to bounded positive current (#357);
11. finite co-lattice coherent multiwindow gain (#358/#363);
12. finite no-alias multirate gain (#360).

Not dead: signed Cycle Debt, state-dependent/nonstationary/continuum policies, aggregate canonical systems, raw Brownian stability, matrix repairs, growing aliases, or different consumers.

## 8. Route aliases

The detailed map is `integration/integration-wave-route-rosetta-stone.md`. The essential aliases are:

- SHARP = uniform-Pascal Green positivity = a local-versus-tail Möbius inequality.
- Critical-log low-row scalar = positive Volterra smoothing of the same zero-safe SHARP source.
- BTF/GFEP/frozen producer = observables of one finite stationary binary–ternary chain.
- Balanced fragmentation = size-biased Markov occupation; Cycle-Debt duals = bounded policy-capacity drifts.
- WSTS, endpoint `A(X)`, factor-64 annulus, positive occupancy, and complete gap = filters/consumers of one prime–radical flux.
- Q2/Q4 all-pass, root-Haar, parity frame, and two-state ledger = one corrected radix-four source/state system.
- Xi-cardinal isolation, Gaussian pair threat, Gabor capture, and corrected floor = interfaces of one complete-kernel classifier.

## 9. Urgent contradictions for the integrator

1. `main` is stale; do not build the current index by incrementally editing its old front door.
2. Preserve PR #214 as historical, not current.
3. Add explicit supersession from #292/#351 to #356.
4. Add #359 → #357/#362 correction/firewall edges.
5. Supersede every old Brownian cardinal formula by #318.
6. Add #304 → #305/#308/#315/#317 while retaining the commutator.
7. Separate #301's false positive matching from its exact decoder.
8. Import #346 only through #349/#350 source-order corrections.
9. Quarantine #44–#52 production claims pending independent provenance.
10. Do not generalize #356 beyond finite stationary atomic policies.
11. Do not promote trace, determinant, diagonal curvature, or inertia to matrix/current control.
12. Keep upstream zeta-23, repository extensions, diagnostics, and formal-build status separate.

## 10. Computation policy

No heavy experiment was rerun. Inspected but not regenerated:

- historical zero, prime, interval, spectral, Robin, and matrix production;
- factor-64 endpoint scans;
- outer-SHARP tail gates;
- enormous fiber-WHT searches;
- #356 exact recurrence/Rouché/interval package;
- Anthropic's full Lean build;
- Gabor/Xi-cardinal and confluent-cluster suites.

No new numerical experiment was required for the genealogical conclusions.

## 11. Final verdict

```text
Riemann Hypothesis:                 UNPROVEN / GAP
accepted full proposal:             NONE
historical full proposals:          SUPERSEDED or REFUTED AS STATED
finite theorem infrastructure:      substantial VERIFIED / VERIFIED WITH FIXES
RH-equivalent criteria:             numerous useful front doors, not closure
adaptive/continuum/matrix routes:    LIVE or DORMANT BUT LIVE
```

This is archaeology and review. It is not an RH proof, disproof, or integration commit.
