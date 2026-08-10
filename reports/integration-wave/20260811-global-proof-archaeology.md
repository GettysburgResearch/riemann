# Global proof archaeology and genealogy review

**Repository:** `gfreund123/riemann`  
**Role:** repository archaeology and proof genealogy, not independent reconstruction of every live proof  
**Review cutoff:** `2026-08-11T05:37:06Z`  
**Frozen main:** `d6409319b4041cd09bee85f55a344631508f2501`  
**Review branch:** `review/integration-wave-20260811-archaeology`  
**Verdict:** **No accepted proof of the Riemann Hypothesis is present in the reviewed graph.**

This report reconstructs intellectual lineages. It distinguishes a false theorem from a failed proof, a failed example from a closed mechanism class, finite evidence from a cofinal theorem, and an RH-equivalent criterion from an unconditional advance on its remaining sign.

## 1. Freeze and live-repository finding

At the cutoff, the default branch `main` was exactly commit

```text
d6409319b4041cd09bee85f55a344631508f2501
Replace setup placeholder with elementary consolidation status
```

That commit is dated 2026-08-08 and contains an elementary consolidation status, not the later research wave. The scientifically live state was distributed across open stacked PR branches through PR #366. Consequently:

1. `main` is a historical integration base, not the current scientific state.
2. conclusions in this report are frozen to exact PR heads, never to a moving branch name alone;
3. historical front doors are preserved as historical records and are not silently reinterpreted as current;
4. a missing file on `main` is not evidence that a live branch theorem disappeared.

Important inspected live heads include:

| Family | PR | Branch | Frozen head |
|---|---:|---|---|
| Carry/Pascal full conditional architecture | #247 | `agent/gpt56-pro-09-u/238-gamma-carry-factorization` | `6c4dadc97db57a3cf352c9f72fab3bedce792382` |
| GFEP first-entrance proposal | #292 | `research/gpt56-sol-280-global-fragmentation-spine` | `6011cde9ef7467729cc24360372a176b622a5655` |
| Carry-window Selberg/Kummer | #297 | `agent/gpt56-pro-09-r/281-carry-window-selberg-kummer` | `409e1764fc708f725aae8dcd3fad9b8ae480bea3` |
| Eta/Pascal repair frontier | #301 | `agent/gpt56-pro-global/296-triangular-eta-pascal-closure` | `80f25af026da9f967e95c2a1f0fe91c8e95801e7` |
| Reciprocal-eta/Mersenne | #302 | `agent/gpt56-pro-09-v/280-central-cascade-global-attack` | `477b527fb489397eb9e58ed6631be04f5eae00d1` |
| Terminal cutoff proposal | #304 | `research/gpt56-sol/303-descendant-capacity-commutator` | `78b75fc17e27334a9950018528c1c6e083d74820` |
| MCF exact refutation | #314 | `review/gpt56-pro-306-mcf-eta-dual-refutation` | `f07f44263c3ff4b219918b05cac61a75e18ff773` |
| Cycle-optimized boundary repair | #315 | `agent/gpt56-pro-22/307-boundary-atomic-refutation-cycle-debt` | `33b312e32818adb78b5bdc78e4c64f1a870b532c` |
| Eta core/central firewall | #317 | `research/gpt56-sol/304-cutoff-cancellation-critical-jet` | `9b49c103ab3bd91724182c4c2fecfe2f0c9cb490` |
| Corrected Brownian Robin fiber | #318 | `research/gpt56-sol/296-correct-robin-cardinal-fiber` | `277bfb19e2e5deed50b5bbc133453b7147046360` |
| Radix-character firewall | #323 | `research/gpt56-sol/322-residue-character-firewall` | `7182b6162d4015bf732dce434784f990f32c0785` |
| Q4 reflected/Jordan family | #325 | `research/gpt56-sol/324-two-contact-brownian-normal-form` | `8036edcd8b42f1fb3bbee605a6fae3b22985238d` |
| SHARP continuum/Green state | #329 | `agent/gpt56-sol/323-halfpower-dual-superposition` | `219cab4496357867018f300936c877967ac0a81b` |
| Gamma/Pascal Markov occupation | #335 | `agent/gpt56-sol/331-gamma-carry-convex-order` | `188bd0362c3a9f88adcbcf5298bf8eeade4016cf` |
| Raw Brownian/Hermite | #343 | `agent/gpt56-sol/340-raw-brownian-dirichlet-stability` | `fed85f2969a5ab9f09890cd89bd6b57ff2115320` |
| Outer 255/256 SHARP | #347 | `research/gpt56-sol/347-outer-127-128-sharp` | `f70bcda4d04200c96ddf5b74bc65ccb4aa8750ae` |
| WSTS audit/z-collapse | #348 | `agent/gpt56-sol/90005-zcollapse-proof` | `89f0eb418a470d55e945b08daa3d0f0dc2fc7914` |
| Theta/GFEP bootstrap | #351 | `claude/riemann-proof-review-8nz34i` | `22a94f431d7f4cd87db5f3efdd97b086f8f60183` |
| Factor-64 endpoint criterion | #352 | `agent/gpt56-pro/90006-endpoint-negative-drift` | `906b5a477a1ed7c88a40db7569924f15f3d54b72` |
| Positive occupancy state | #353 | `research/gpt56-pro/353-positive-occupancy-source` | `ed566f3198e236c54ba18049181016536f56d456` |
| Finite-atomic/GFEP refutation | #356 | `research/gpt56-pro/90102-liouville-bernstein-extremality` | `1a60df88aadac731ec32e48a87b74537662114dd` |
| Corrected Q4 inertia state | #357 | `research/gpt56-sol/90300-claude-inertia-q4` | `a2843d31649822014219a13ec29c70e4a30932cc` |
| Anthropic zeta-23 import | #358 | `research/gpt56-pro/90301-claude-signature-moment` | `6f675e6e49c5b1fee3b1c7fce92331d2bad16948` |
| Aggregate Q4 full proposal | #359 | `agent/gpt56-pro-09-w/90304-aggregate-inertia-q4` | `9ffcb8d3dbc6affd859ea8567a061b71dd0d1e8b` |
| PIG equivalence firewall | #362 | `research/gpt56-pro/90402-pig-rh-equivalence` | `31c57c56c00c0a062a49a126d4e5a68ff28e9fe8` |
| Gabor/Xi pair spectrum | #363 | exact PR head | `01238699b9ea2844e674f56a965cde79559d770a` |
| Gaussian terminal-pair isolation | #364 | exact PR head | `219330bd0441a284fd16ff728dd843a7ee4503ee` |
| Xi-cardinal Gram capture | #365 | `research/gpt56-pro/364-xi-cardinal-gram-capture` | `902a4cfeb36392c07878591e4a8381e3f4c7b2db` |
| Confluent cluster renormalization | #366 | `research/gpt56-pro/365-confluent-cluster-renormalization` | `3dd8184c4e34f3a7ecd2b64597c7737af2b59029` |

The complete reviewed-head ledger is in `audits/integration-wave/20260811-proposal-genealogy.tsv`.

## 2. Historical integration baselines

### 2.1 First exact-SHA integration snapshot

The frozen `integration/2026-08-01/` snapshot reviewed PRs #1–#127 at final integration commit `d7fe83f56b7784eb3045092b88635e55014b909f`. Its durable achievements were organizational and packet-level:

- finite completed-xi identities and finite determinant/Gram/inertia algebra;
- finite Robin/resolvent and operator computations;
- explicit negative results and scope firewalls;
- exact-SHA and artifact-ledger discipline.

Its durable open boundaries were also correct: source normalization, cofinality, Brownian source mismatch, Möbius transfer, and production-artifact provenance.

### 2.2 Historical front door PR #214

PR #214, head `99e0c656c7d370ac6fdb7d1944bf6c2becea93d0`, built the durable README/AGENTS/results-index structure, imported four resident packets, preserved canonical blob identities, and recorded a safe operator/Weil import order. It claimed no RH proof and reran no heavy science.

That front door remains a good historical baseline. It is no longer a complete map of the live graph. The correct integration action is to retain it unchanged in history and create a new current index rather than rewriting its old verdicts as though they had anticipated PRs #247–#366.

### 2.3 Pre-public audit of PRs #44–#63

The audit at `reports/gpt56-global-01/2026-08-01-pre-public-review-pr44-pr63.md` remains foundational. It established four recurring repository failure modes:

1. finite algebra verified while the production source is missing or misidentified;
2. metadata corrections that propagate, rather than repair, bad provenance;
3. duplicate or superseded reviews presented as independent evidence;
4. compact RH-equivalent criteria mistakenly treated as closure.

Those same patterns recur later under more sophisticated mathematics.

## 3. Chronological project map

### Phase A — finite xi, Cayley, Robin, and operator packets

The earliest wave produced real finite mathematics: determinant factorizations, Gram inertia, local Cayley signs, finite Robin bounds, resolvent identities, and operator Schur algebra. The failures were mainly provenance and finite-to-cofinal scope. PRs #44–#52 require artifact quarantine, not mathematical erasure. PR #54 survives as a compact boundary-current criterion but hits an RH-equivalence firewall. PR #55 was corrected first by PR #63 and decisively by PR #318.

### Phase B — finite reservoir and producer no-go results

The carry programme developed exact atomized carry rows, Pascal four-cycles, Möbius divergence, balanced fragmentation, and duality. The N-UNI lineage (PRs #164–#183) proved a genuine mechanism theorem: a fixed finite update family with a bounded trajectory cannot support the proposed deterministic uniform `C/m` reservoir recurrence. This closed that mechanism class but not source-dependent or adaptive producers.

### Phase C — full carry/Pascal proposals

PR #247 assembled the first modern full conditional spine. PR #292 replaced failed fixed-order Abel positivity with all-generation first-entrance recombination. PR #301 attempted eta/Pascal/Hausdorff closure. PRs #302 and #304 pursued reciprocal-eta/Mersenne and terminal cutoff variants. Each failure generated durable mathematics:

- fixed-order smoothing failed, but first-entrance and Green identities survived;
- pair-first positivity was mistyped, but an actual-coordinate boundary decoder survived;
- atomic boundary norm was linear, but optimized carry-column mass was polylogarithmic;
- Mersenne-collar saturation was refuted, but the eta resolvent and sparse telescope survived.

### Phase D — SHARP, Green occupation, and policy selection

PRs #326, #329, #335, and #347 showed that SHARP, the uniform Pascal Green kernel, the square-root hinge inverse, and a local-vs-tail Möbius inequality are the same canonical object in different coordinates. PR #347 pushed exact finite positivity to the outer `255/256`. PR #356 then supplied the decisive policy genealogy:

- the frozen binary–ternary GFEP, producer positivity, and BTF oscillate cofinally;
- every finite stationary fixed-ratio policy lacks a source-independent spectral gap;
- the uniform continuum and uniform Pascal policies remove deterministic policy resonances.

Thus the dead class is finite stationary atomic spectral-gap closure, not fragmentation itself.

### Phase E — Q4 reflected/Jordan/Hermitian programme

The Q4 lineage begins from carry-window Selberg/Kummer structure and develops compact radix-four sources, all-pass frames, paired reserves, exact physical placement, vector Jordan curvature, parity jets, two-state reflected ledgers, and inertia-tolerant aggregation. Its corrections are genealogically important:

- diagonal scalar reserve does not imply source-matrix reserve;
- a scalar Schur shortcut fails when a diagonal Hessian entry vanishes but the mixed derivative does not;
- bare charges and currents depend on convolution order;
- trace positivity and small negative inertia do not control a large positive current.

PR #359 proposed a complete composition, but PR #362 identified its positive innovation gate as RH-equivalent within the corrected assembly. The Q4 route therefore has many salvageable sub-RH packets and one explicit RH-equivalent consumer.

### Phase F — WSTS, endpoint, annular, and occupancy programmes

PRs #348, #351, #352, and #353 should not be indexed as four unrelated routes. They share one prime–radical flux:

- WSTS and the prime ramp are equivalent front doors;
- the factor-64 scalar is a zero-safe annular filter of the endpoint state;
- positive occupancy is the Green source of the endpoint scalar;
- the Gamma/Pascal state is an elementary delay/deconvolution of the same source;
- the complete prime-power gap removes the deterministic prime-square moat.

The strongest durable endpoint statements are the exact Mellin symbols, the globally negative prime-power moat, factor-64 minimality within the phase-blind integer-filter class, the positive occupancy identity, and the signed packing-score objective. The eventual sign or subquadratic loss remains open and RH-bearing or RH-equivalent.

### Phase G — Anthropic zeta-23, Gabor, and complete-kernel synthesis

PRs #358 and #361 correctly import the external theorem as an unconditional zero-proportion theorem, not an RH proof. The native repository then proves useful architecture no-gos:

- co-lattice multiwindow profiles collapse to one scalar profile;
- finite no-alias multirate banks do not improve the two-trace architecture;
- coherent same-lattice banks preserve the complete nonzero spectrum.

The route then pivots from improving a two-trace constant to isolating a hypothetical off-line pair. PRs #364–#366 construct Gaussian/Xi-cardinal isolation, cofinal finite-packet capture, and confluent jet renormalization. The zero-side and conditioning-side escape routes are substantially reduced. The arithmetic corrected-kernel floor remains the RH-equivalent hinge identified already by PR #199.

## 4. Proposal → correction → refutation → salvage DAGs

### 4.1 Brownian/Robin DAG

```text
PR55 original Brownian/Robin fiber
  -> PR63 ordering/sign correction
  -> PR296 finite Brownian/Norlund approximants
  -> PR318 exact centered-fiber correction
       -> finite reflected-tail domination FALSE
       -> positive good-fiber cone closure FALSE
       -> corrected one-fiber Robin theorem SURVIVES
       -> aggregate BACS question OPEN
  -> PR343 raw one-sided Dirichlet/Hermite route
       -> N=2 zero-free VERIFIED
       -> cofinal all-N stability OPEN
```

### 4.2 Carry/GFEP DAG

```text
PR247 BTF/MPR architecture
  -> fixed-order Abel mutations (PR279/299) FALSE
  -> PR292 GFEP first-entrance recombination
  -> PR351 WSTS/GFEP consolidation
  -> PR355 positivity/source variants
  -> PR356 certified frozen-policy oscillation
       -> frozen GFEP FALSE
       -> frozen producer positivity FALSE
       -> frozen BTF FALSE
       -> finite stationary atomic no-gap theorem
       -> uniform Pascal/continuum escape SURVIVES
```

### 4.3 Eta/Pascal/cutoff DAG

```text
PR301 eta-Pascal/Hausdorff closure
  -> PR303/312 source-typing corrections
  -> actual-coordinate boundary decoder SURVIVES
  -> PR304 terminal cutoff atomic closure
       -> PR305/308 exact linear atomic obstruction
       -> PR315 positive outer-band optimized flow
       -> PR317 eta core and recombination identity
            -> pure-central positivity FALSE
            -> COBT/CEV adaptive cycle debt OPEN
```

### 4.4 Mersenne DAG

```text
PR302 reciprocal-eta/Mersenne cascade
  -> all-order continuum monotonicity FALSE at overlap 6
  -> sparse Mersenne telescope SURVIVES
  -> exact MCF support menu
       -> PR314 cofinal Mellin/Landau refutation
  -> unrestricted/nonstationary Cycle Debt NOT REFUTED
```

### 4.5 Q4 DAG

```text
PR297 finite pole frame + endpoint reserve
  -> PR325 Q4 all-pass/pair/current frame
  -> PR339/341/342 placement and two-state ledgers
  -> PR345 scalar Schur shortcut FALSE; vector curvature
  -> PR346 parity source
       -> PR349 first source-order correction
       -> PR350 second source-order correction
  -> PR357 inertia-tolerant state; current-from-inertia shortcut FALSE
  -> PR359 aggregate-inertia full composition
  -> PR362 PIG is RH-equivalent
```

### 4.6 Endpoint DAG

```text
PR348 WSTS <=> RH and z-collapse
  -> PR351 elementary bootstrap and lambda-extremality
  -> PR352 endpoint Mellin symbol, moat, annular hierarchy, factor 64
  -> PR353 positive occupancy, Gamma bridge, complete gap, packing objective
  -> PR356 low-row Volterra alias and finite-policy firewall
```

### 4.7 Operator/Gabor DAG

```text
PR199 corrected-kernel classifier
  -> PR358/361 zeta-23 import and two-trace extensions
  -> PR360 finite multirate no-gain
  -> PR363 coherent same-lattice spectral collapse
  -> PR364 Gaussian off-line pair isolation
  -> PR365 Xi-cardinal cofinal capture
  -> PR366 confluent jet renormalization
  -> arithmetic corrected-kernel floor OPEN / RH-EQUIVALENT
```

## 5. Salvage dossiers

### 5.1 Early finite xi/Gram production packet

**Proposal:** certified finite zero/Gram/inertia production packet  
**PR and reviewed SHA:** #44 `ea290a5363bea44854f8fc57433c45311d5ddaca`, with #48/#52 provenance descendants  
**Claimed proof spine:** certified zero data → finite Gram/inertia witness → operator sign conclusion  
**First broken or open arrow:** source files and manifests do not certify the advertised zero dataset  
**Failure type:** ARTIFACT OR PROVENANCE FAILURE  
**Exact refutation or gap:** cited tables and repository artifacts do not match the claimed production source  
**Surviving independent results:** finite determinant, adjugate, inertia, and rational replay algebra  
**Later corrections:** PRs #49–#52; historical integration packets  
**Later descendants:** finite Pick/operator packet in PR #214  
**Possible resurrection:** FINITE REPAIR  
**Current recommendation:** retain finite theorem statements; quarantine every production claim until independently sourced and hashed.

### 5.2 Original Brownian Robin fiber

**Proposal:** Brownian/Nörlund approximants decompose into good Robin fibers  
**PR and reviewed SHA:** #55 `a60adc8a6405becdce4e41e7b04731402d0d451e`  
**Claimed proof spine:** Brownian moment approximation → centered cardinal fibers → self-adjoint Robin spectra → real zeros → RH  
**First broken or open arrow:** the displayed centered fiber is not even and has the wrong linear term  
**Failure type:** SIGN OR NORMALIZATION ERROR  
**Exact refutation or gap:** PR #318 derives `cosh(ell z/2)+2z sinh(ell z/2)` and supplies counterexamples to aggregate closure  
**Surviving independent results:** finite gamma/Nörlund approximation, corrected one-fiber Robin classification  
**Later corrections:** #63 and #318  
**Later descendants:** raw Dirichlet/Hermite route #343  
**Possible resurrection:** MATRIX / INERTIA REPAIR  
**Current recommendation:** archive the original formula; integrate corrected one-fiber and raw routes separately.

### 5.3 Fixed-order Abel positivity

**Proposal:** a bounded smoothing order makes the carry source positive  
**PR and reviewed SHA:** mutation lineage through #299 `cd45a45b480c35e46317a29e07d73c379af0df27`  
**Claimed proof spine:** iterate a positive-looking kernel → eliminate local sign debt → positive producer  
**First broken or open arrow:** exact negative witnesses occur at successive low orders  
**Failure type:** EXACT COUNTEREXAMPLE  
**Exact refutation or gap:** orders one through at least four/five fail on explicit finite rows  
**Surviving independent results:** exact Abel identities and residual decompositions  
**Later corrections:** #292 first-entrance recombination  
**Later descendants:** GFEP and signed all-generation routes  
**Possible resurrection:** RECOMBINE BEFORE ABSOLUTE VALUES  
**Current recommendation:** classify bounded-order positivity as dead; preserve the mutations as mandatory tests.

### 5.4 Frozen GFEP/BTF producer

**Proposal:** the half-binary/half-ternary first-entrance source or producer is nonnegative/subpower  
**PR and reviewed SHA:** #292 `6011cde9ef7467729cc24360372a176b622a5655`; consolidated #351 `22a94f431d7f4cd87db5f3efdd97b086f8f60183`  
**Claimed proof spine:** exact stochastic fragmentation → first-entrance positivity → sharp prime ramp → RH  
**First broken or open arrow:** one fixed bottom exit and the actual producer possess a nonreal characteristic pole near the conservation line  
**Failure type:** GENERIC MECHANISM NO-GO  
**Exact refutation or gap:** PR #356 proves cofinal sign oscillation and failure of BTF for the frozen producer  
**Surviving independent results:** Green/entrance algebra, top-fifth sign, positive Stieltjes packets, lambda-rigidity and positive convolution cone  
**Later corrections:** #356  
**Later descendants:** uniform Pascal, adaptive policy, signed Cycle Debt  
**Possible resurrection:** STATE-DEPENDENT POLICY  
**Current recommendation:** mark frozen targets FALSE; preserve the algebra and route future work away from finite stationary atomic policies.

### 5.5 Eta/Pascal/Hausdorff closure

**Proposal:** interleaved eta source admits positive Hausdorff/Pascal matching with polylog debt  
**PR and reviewed SHA:** #301 `80f25af026da9f967e95c2a1f0fe91c8e95801e7`  
**Claimed proof spine:** scalar Euler jets → nodewise positive matching → tensorized carry map → Cycle Debt  
**First broken or open arrow:** scalar jets do not bind node labels; noncoprime tensorization is false  
**Failure type:** SOURCE-TYPING ERROR  
**Exact refutation or gap:** exact wrong-series, reverse-flow, non-Hausdorff, and noncoprime witnesses are resident  
**Surviving independent results:** modal source decomposition and exact actual-coordinate Möbius boundary decoder  
**Later corrections:** #303 and #312  
**Later descendants:** #304, #315, #317  
**Possible resurrection:** CHANGE OF SOURCE  
**Current recommendation:** promote the decoder as an independent theorem; archive the positivity composition.

### 5.6 Terminal cutoff atomic lift

**Proposal:** terminate every half-scale boundary with polylogarithmic divisor-source atomic norm  
**PR and reviewed SHA:** #304 `78b75fc17e27334a9950018528c1c6e083d74820`  
**Claimed proof spine:** finite Euler expansion → atomic boundary source → adjacent commutator → polylog debt  
**First broken or open arrow:** a macroscopic quotient band forces the source coordinates and has linear weighted norm  
**Failure type:** EXACT COUNTEREXAMPLE  
**Exact refutation or gap:** #305/#308/#315/#317 prove linear lower bounds  
**Surviving independent results:** adjacent commutator, exact shift terminalization, positive outer-band carry flow, polylog column-capacity mass  
**Later corrections:** #315 and #317  
**Later descendants:** COBT/CEV  
**Possible resurrection:** CHANGE OF NORM  
**Current recommendation:** prohibit atomwise norms before destination recombination; retain optimized carry-coordinate question.

### 5.7 Mersenne-collar fragmentation

**Proposal:** eventual exact saturation by a fixed Mersenne-collar support menu  
**PR and reviewed SHA:** source #302 `477b527fb489397eb9e58ed6631be04f5eae00d1`; refutation #314 `f07f44263c3ff4b219918b05cac61a75e18ff773`  
**Claimed proof spine:** reciprocal-eta sparse telescope → fixed support flow → exact saturation → RH  
**First broken or open arrow:** the exact dual scalar has nonreal eta poles and changes sign cofinally  
**Failure type:** GENERIC MECHANISM NO-GO  
**Exact refutation or gap:** Landau contradiction at integer endpoints with controlled interpolation  
**Surviving independent results:** eta inverse identity, Mersenne sign localization, finite isolated feasibility  
**Later corrections:** #314  
**Later descendants:** unrestricted cycle-optimized flow  
**Possible resurrection:** NONE for the stated support menu  
**Current recommendation:** close exact MCF; do not overstate the theorem against adaptive supports.

### 5.8 Radix-five and eta contraction

**Proposal:** finite residue automaton or strict eta transfer contraction closes the Möbius state  
**PR and reviewed SHA:** #323 `7182b6162d4015bf732dce434784f990f32c0785`  
**Claimed proof spine:** finite residue state → source-free contraction → principal zeta control  
**First broken or open arrow:** nonprincipal Dirichlet-L channels are present, and the eta multiplier equals one at zeta-zero frequencies  
**Failure type:** SOURCE-TYPING ERROR  
**Exact refutation or gap:** exact character Fourier decomposition and zero-mode identity  
**Surviving independent results:** character decomposition, low-frequency weighted-jet contraction, radix-two uniqueness  
**Later corrections:** dyadic PMSD and Q4 programmes  
**Later descendants:** #330 and Q4 source-complete states  
**Possible resurrection:** CHANGE OF SOURCE  
**Current recommendation:** make the character firewall mandatory; do not call nonprincipal modes finite boundary noise.

### 5.9 Q4 scalar Schur and source-order shortcuts

**Proposal:** local scalar reserve/Schur curvature controls the compact Q4 current  
**PR and reviewed SHA:** #345 `36e0b71f27798835e622a0646474ff24064ca62a`, with source formulas #346  
**Claimed proof spine:** positive scalar curvature → Schur bound → current recurrence  
**First broken or open arrow:** diagonal Hessian information and trace positivity do not control mixed/vector curvature; source formulas depend on convolution order  
**Failure type:** SCALAR / MATRIX SCOPE ERROR  
**Exact refutation or gap:** exact scalar countermodel and source-order witnesses in #345/#349/#350  
**Surviving independent results:** compact zero-bare source, vector Jordan curvature, parity frame, corrected balanced moat  
**Later corrections:** #349/#350/#357  
**Later descendants:** #359/#362  
**Possible resurrection:** MATRIX / INERTIA REPAIR  
**Current recommendation:** retain only corrected vector/Hermitian packets and their exact source order.

### 5.10 Aggregate Q4 inertia full composition

**Proposal:** aggregate negative-inertia control eliminates the unknown current and closes RH  
**PR and reviewed SHA:** #359 `9ffcb8d3dbc6affd859ea8567a061b71dd0d1e8b`  
**Claimed proof spine:** compact Q4 source → current-free determinant inequality → coefficient-one recurrence → pole exclusion  
**First broken or open arrow:** a bound on negative spectral mass does not bound positive innovation energy  
**Failure type:** MISSING LOAD-BEARING THEOREM  
**Exact refutation or gap:** #357 gives the scope counterexample; #362 proves the remaining PIG is RH-equivalent  
**Surviving independent results:** exact aggregate determinant/current elimination and cofinal negative-inertia estimates  
**Later corrections:** #362  
**Later descendants:** future multi-statistic or altered-observable approaches  
**Possible resurrection:** DIFFERENT CONSUMER  
**Current recommendation:** reject the full composition, preserve the inertia theorem, and display the PIG firewall prominently.

### 5.11 Endpoint factor-64 criterion

**Proposal:** a minimal phase-blind annular endpoint filter supplies an unconditional eventual negative sign  
**PR and reviewed SHA:** #352 `906b5a477a1ed7c88a40db7569924f15f3d54b72`  
**Claimed proof spine:** endpoint Mellin symbol → negative prime-power moat → factor-64 annulus → eventual sign → RH  
**First broken or open arrow:** the unconditional sign is not proved and is RH-equivalent  
**Failure type:** RH-EQUIVALENCE FIREWALL  
**Exact refutation or gap:** no contradiction to the criterion; the gap is exactly its eventual sign  
**Surviving independent results:** zero-safe filter, minimality in the declared class, exact Bernstein certificates, negative moat  
**Later corrections:** #353 positive occupancy state  
**Later descendants:** source-specific signed packing  
**Possible resurrection:** DIFFERENT CONSUMER  
**Current recommendation:** retain as a compact front door; never count it as closure progress by itself.

### 5.12 Finite stationary fragmentation policy class

**Proposal:** choose a finite stationary fixed-ratio policy with a uniform source-independent spectral gap  
**PR and reviewed SHA:** theorem #356 `1a60df88aadac731ec32e48a87b74537662114dd`  
**Claimed proof spine:** fixed renewal characteristic → uniform gap → subpower producer  
**First broken or open arrow:** simultaneous phase recurrence creates characteristic zeros arbitrarily close to the conservation line  
**Failure type:** GENERIC MECHANISM NO-GO  
**Exact refutation or gap:** theorem `L-90208` covers every finite atomic stationary fixed-ratio policy  
**Surviving independent results:** policy characteristic calculus and exact uniform Pascal Green kernel  
**Later corrections:** continuum/nonstationary policy pivot  
**Later descendants:** adaptive Green occupation  
**Possible resurrection:** CONTINUUM RATHER THAN FINITE-ATOMIC POLICY  
**Current recommendation:** mark the class dead and route policy research to the explicit escape categories.

### 5.13 Same-lattice and finite multirate Gabor gains

**Proposal:** add finitely many coherent/co-lattice windows or no-alias multirate channels to improve the zeta-23 two-trace constant  
**PR and reviewed SHA:** #358 `6f675e6e49c5b1fee3b1c7fce92331d2bad16948`, #360 `df53319d9b8d465b01678986f86261a8d6d16965`, #363 `01238699b9ea2844e674f56a965cde79559d770a`  
**Claimed proof spine:** vector window bank → richer Gram spectrum → better rank/inertia lower bound  
**First broken or open arrow:** the bank collapses to one aggregate profile or a coisometric copy of the same spectrum  
**Failure type:** GENERIC MECHANISM NO-GO  
**Exact refutation or gap:** exact kernel/spectrum identities close the finite same-lattice/no-alias class  
**Surviving independent results:** alias variables, pair spectrum, growing resonant-bank frontier  
**Later corrections:** #364–#366 isolation route  
**Later descendants:** Xi-cardinal capture  
**Possible resurrection:** NONSTATIONARY POLICY  
**Current recommendation:** close finite bank variants; retain growing irregular/prime-resonant and different-moment consumers.

### 5.14 Corrected-kernel completion

**Proposal:** finite zero isolation plus Schur correction proves a nonnegative kernel floor  
**PR and reviewed SHA:** #199 `4158e0d3e7f91829a6c545308605ea8177023aa3`, descendants #364–#366  
**Claimed proof spine:** isolate off-line pair → control Gram/collisions → arithmetic corrected floor → RH  
**First broken or open arrow:** the arithmetic floor is exactly the remaining RH-equivalent sign theorem  
**Failure type:** RH-EQUIVALENCE FIREWALL  
**Exact refutation or gap:** #199 proves a fixed Xi-cardinal negative moat under false RH; #365/#366 eliminate finite packet conditioning escapes  
**Surviving independent results:** Xi-cardinal source, finite Gabor capture, confluent jet positivity, exact Schur classifier  
**Later corrections:** #365/#366  
**Later descendants:** high-order moment-Gram and source-complete arithmetic floor  
**Possible resurrection:** DIFFERENT CONSUMER  
**Current recommendation:** integrate zero-side capture and arithmetic-side floor as separate packets, with the firewall between them.

## 6. Ten most valuable salvage packets

1. **Finite completed-xi determinant/Gram/inertia algebra.** Independent of failed production provenance and reusable by operator, Pick, and Gabor routes.
2. **Corrected one-fiber Brownian Robin theorem.** The old formula is false, but the corrected spectral classification is exact and sharply separates positive and negative lengths.
3. **Actual-coordinate Möbius boundary decoder.** It survives the eta/Pascal positivity failure and preserves noncoprime destinations exactly.
4. **Atomic-versus-optimized boundary contrast.** Linear divisor-source norm coexists with positive outer-band carry flow and polylogarithmic column mass; this is a reusable warning against early absolute values.
5. **Markov occupation and policy-drift duality.** Balanced fragmentation, Green occupation, and Cycle Debt are one object, reducing architectural duplication.
6. **Finite-stationary no-gap theorem and uniform-Pascal escape.** This closes a broad dead class while identifying a concrete live replacement.
7. **Q4 source/frame/Hermitian packet.** Compact zero-bare source, all-pass frame, paired reserve, vector curvature, and corrected physical placement survive the failed scalar/current shortcuts.
8. **Endpoint positive occupancy and prime-square moat.** WSTS, annular criteria, Gamma/Pascal, and complete prime-power gap acquire a common positive-source state.
9. **Xi-cardinal finite-packet capture.** Super-Gaussian cardinal division, `O(1/L)` Gabor capture, and a linear Schur moat remove finite Gram-collapse escape routes.
10. **Confluent jet renormalization.** Finite collisions are coordinate artifacts after Newton divided differences; only growing active order/tails remain.

Additional high-value packets include lambda-rigidity/positive convolution cones, finite outer `255/256` SHARP, exact Mersenne/eta telescopes, and co-lattice/multirate no-gain theorems.

## 7. Genuinely dead mechanism classes

A class is listed here only when the reviewed graph contains a theorem or exact class-wide identity.

1. **Finite stationary fixed-ratio fragmentation with a source-independent spectral gap.** Closed by PR #356 `L-90208`; characteristic zeros approach the conservation line for every finite atomic policy.
2. **The frozen half-binary/half-ternary GFEP, pointwise producer positivity, and BTF.** Closed for that policy by PR #356 `R-90201`; both signs occur arbitrarily far out.
3. **Eventual exact Mersenne-collar saturation with the declared support menu.** Closed by PR #314 through an explicit eta dual and Landau contradiction.
4. **Deterministic uniform `C/m` reservoir recurrence for the declared finite update family when a bounded trajectory exists.** Closed by the N-UNI theorem in the PR #174–#183 lineage.
5. **Finite reflected-tail domination in the corrected Brownian/Nörlund Robin mixture.** Closed for every finite N by PR #318.
6. **Closure of individually good positive-length Robin fibers under arbitrary positive superposition.** Closed by PR #318's exact Newton-inequality counterexample.
7. **Strict translation-invariant complete eta contraction in a norm containing zeta-zero modes.** Closed by PR #323 because the multiplier equals one on those modes.
8. **Zeta-only source-free radix-five contraction.** Closed as a zeta-only mechanism by PR #323: the state contains nonprincipal mod-five L-functions. The stronger GRH-valued problem is not closed.
9. **Scalar Schur control of the compact Q4 current from the diagonal row curvature alone.** Closed by the exact mixed-Hessian countermodel in PR #345.
10. **Inference from small negative inertia to bounded positive Q4 current.** Closed by the exact family in PR #357.
11. **Finite co-lattice coherent multiwindow gain within the same two-trace architecture.** Closed by PRs #358/#363: only an aggregate profile or the same nonzero spectrum remains.
12. **Finite no-alias multirate improvement in that architecture.** Closed by PR #360; growing prime-resonant aliases are outside the theorem.

Not dead: signed Cycle Debt, state-dependent policies, nonstationary policies, continuum policies, aggregate canonical systems, raw Brownian stability, matrix/inertia repairs, growing resonant Gabor banks, or the arithmetic corrected-kernel floor.

## 8. Route aliases and shared canonical objects

The detailed Rosetta stone is in `integration/integration-wave-route-rosetta-stone.md`. The most important aliases are:

- SHARP positivity = uniform Pascal Green occupation positivity = a local-versus-tail Möbius inequality.
- Critical-log low-row scalar = a positive Volterra smoothing of the same zero-safe SHARP source.
- BTF/GFEP/frozen producer = different observables of one finite stationary binary–ternary Green chain.
- Balanced fragmentation flow = size-biased Markov occupation; Cycle-Debt duals = bounded policy-capacity drifts.
- WSTS, endpoint `A(X)`, factor-64 annular scalar, positive occupancy, and complete prime-power gap = filters or consumers of one prime–radical flux.
- Q2/Q4 all-pass, root-Haar complement, parity frame, and two-state critical-Haar ledger = one radix-four source/state system after source-order correction.
- Xi-cardinal isolation, Gaussian terminal-pair threat, Gabor capture, and corrected-kernel floor = zero-side coordinates of one complete-kernel classifier.

## 9. Urgent contradictions for the integrator

1. **Main versus live graph:** `main` at `d6409319...` is stale; a current front door cannot be generated by merely editing the old results index.
2. **PR #214 status:** retain it as historical integration; do not overwrite its 18-family snapshot with post-cutoff claims.
3. **GFEP/BTF:** PRs #292/#351 must carry an explicit supersession edge to PR #356.
4. **Q4 full composition:** PR #359 must carry edges to PR #357's current/inertia counterexample and PR #362's PIG equivalence firewall.
5. **Brownian fiber:** every citation of the PR #55/PR #296 cardinal formula must be superseded by PR #318.
6. **Terminal cutoff:** PR #304 must point to #305/#308/#315/#317; its atomic norm claim is false while its commutator survives.
7. **Eta/Pascal:** PR #301 must separate the false positive matching from the surviving actual-coordinate decoder.
8. **Q4 source order:** PR #346 formulas must not be imported without #349/#350 corrections.
9. **Artifact provenance:** PRs #44–#52 cannot be promoted as certified production without independent source and hash closure.
10. **Policy no-go scope:** PR #356 closes finite stationary atomic spectral-gap closure, not adaptive, signed, nonstationary, or continuum policies.
11. **Scalar/matrix scope:** trace, determinant, diagonal curvature, and negative inertia cannot be silently promoted to matrix PSD or current control.
12. **External zeta-23 import:** upstream sources and Lean commit are pinned, but this review did not rebuild the full formal dependency closure; native extensions need independent status.

## 10. Computation and artifact policy

No heavy experiment was rerun. The review inspected reports, theorem files, manifests, retained result files, hashes, and declared scopes. In particular it did not rerun:

- historical zero tables, prime scans, interval arithmetic, spectral, Robin, or matrix-production workloads;
- the factor-64 endpoint scans through five million;
- the outer-`255/256` SHARP 261,888 tail gates;
- the multiplicative fiber-WHT searches with enormous class sizes;
- PR #356's exact recurrence through 20,000, 70-digit complex interval/Rouché certificate, or 39,998 trace checks;
- Anthropic's full Lean build or dependency closure;
- finite Gabor/Xi-cardinal and confluent-cluster verification suites.

No new numerical experiment was needed for the genealogical conclusions.

## 11. Overall verdict

The repository contains a large amount of valuable exact mathematics, but its historical narrative repeatedly overcounted coordinate changes as independent routes and repeatedly placed the final RH-equivalent sign behind a new acronym. The strongest integrable advances are not full proofs; they are:

- exact finite packets;
- exact source-typing and convolution-order corrections;
- broad mechanism no-go theorems;
- compact RH-equivalent front doors;
- explicit policy, matrix, and consumer escape categories;
- increasingly sharp isolation of the remaining arithmetic sign.

The correct lifecycle verdict is therefore:

```text
Riemann Hypothesis:                 UNPROVEN / GAP
accepted full proposal:             NONE
historical full proposals:          SUPERSEDED or REFUTED AS STATED
finite theorem infrastructure:      substantial VERIFIED / VERIFIED WITH FIXES
RH-equivalent criteria:             numerous and useful, but not closure
adaptive/continuum/matrix routes:    DORMANT BUT LIVE or LIVE
```

This is archaeology and review. It is not an RH proof, disproof, or integration commit.
