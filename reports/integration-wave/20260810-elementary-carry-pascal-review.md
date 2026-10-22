# Integration-wave review: elementary carry, Pascal, SHARP, Cycle Debt, and endpoint routes

**Review cutoff:** 2026-08-10T22:01:31Z  
**Final live-head reconciliation:** 2026-08-10T22:21:22Z  
**Repository:** `gfreund123/riemann`  
**Frozen main/base SHA:** `d6409319b4041cd09bee85f55a344631508f2501`  
**Review branch:** `review/integration-wave-20260810-elementary`  
**Scope:** carry, fragmentation, Pascal, Cycle Debt, SHARP, WSTS, GFEP/BTF, prime endpoint, occupancy, annular, eta/Mersenne, and related elementary source-flow routes  
**Global conclusion:** **RH remains unproved.**

## 1. Executive verdict

The elementary graph contains a substantial exact infrastructure layer and several genuine unconditional theorems, but no unconditional closing sign or transport theorem.

The central durable spine is now clear:

```text
critical carry target
-> exact Möbius node divergence
-> balanced fragmentation / Markov occupation
-> policy-capacity Green debt or uniform-Pascal occupation
-> sharp prime-ramp or endpoint consumer
-> Landau pole exclusion
-> RH.
```

The exact finite algebra in this spine survives. What failed were several proposed ways to force positivity or small debt:

1. full coordinatewise GFEP for the frozen half-binary/half-ternary policy;
2. pointwise positivity and subpower weighted negative variation for that frozen producer;
3. any source-independent spectral gap for a stationary policy supported on finitely many fixed ratios;
4. automatic conversion of Hausdorff source mass into available edge capacity;
5. polylogarithmic terminal ordinary divisor-source atomic norm;
6. the claimed second Euler alternation after common-destination recombination;
7. exact critical-neutrality from a coordinatewise-positive uniform-Pascal reward;
8. eventual restricted Mersenne-collar saturation;
9. several fixed-order Abel and frozen finite-state closure mechanisms.

These failures do **not** refute signed Cycle Debt, state-dependent or nonstationary fragmentation, broad/continuum policies, uniform Pascal, SHARP, endpoint occupancy, or annular criteria. The strongest live mechanisms are:

- a policy-level signed Green-occupation bound;
- all-generation cycle-optimized boundary recurrence with actual capacity manifests;
- iterative square-root-hinge saturation after the proved top-half elimination step;
- the low-row/CN3 adjacent-dyadic Mertens-flux inequality;
- the factor-64 51-state Pascal payment;
- radix-four positive-detail packing with subquadratic signed score loss;
- the all-depth SHARP inner tail-vs-threshold theorem.

## 2. Frozen source ledger

The following SHAs are the exact heads used for this review. PR descriptions were used only as navigation; theorem, lemma, refutation, report, methodology, experiment-output, and handoff files were inspected at the stated refs.

| PR | reviewed head SHA | role in this review |
|---:|---|---|
| #240 | `0ce602acba9a882573f719beb8f479c1a23446a9` | original WSTS / theta-bridge lineage |
| #244 | `0ce602acba9a882573f719beb8f479c1a23446a9` | atomwise shell-tail and radical/chord criteria |
| #247 | `6c4dadc97db57a3cf352c9f72fab3bedce792382` | carry/Pascal identities, fragmentation, Farkas, BTF/MPR, `4 log 2` packing |
| #248 | `4130a474ebd349bf54b6ef00325d33eaaf00901` | terminal ordinary atomic-norm obstruction |
| #265 | `821d4dd5b10eb4b258c9951fb184059a9fe4532c` | endpoint-scale atoms and positive triangular packing |
| #272 | `fa7877dd2ffedd095284e956427e35642d1f2634` | Cycle Debt consumer and boundary transference lineage |
| #276 | `784c0fac42bca41b822b3ccdbe7362637c3501f1` | central/dyadic carry cascade continuation |
| #280 | `0b46acee0c749201de365546b63ff3e043b747075` | weighted boundary-transference obstruction |
| #285 | `eed349f7a65eb8c78e34469fc0deda8865ae5c0` | eta/source-filter continuation |
| #292 | `5386b82e29c6e75b70934aff6ad13f42b8e8b5a` | fixed-order Abel no-go |
| #294 | `5914360d85134c21fd36d5e148a3668e18d1d9d` | average-carry inverse / SHARP precursor |
| #295 | `7617a0c0a2c7f65f3061a7ffd4e4303329ff6d2f` | finite-state Markov occupation prototype |
| #301 | `5ec75ba3fb53bb4280b27d024b5747e498e5daf1` | interval/Perron and source-flow proposal lineage |
| #303 | `4367007d658c78a42024a9c94c3c6b078cac2568` | exact source-flow capacity audit and SFC repair |
| #309 | `18e25ec92583e9110a57cf037b691491c278fe39` | complete-boundary atomic lower bound |
| #310 | `8998daed5a900a787530e8b5a16c27ee383bfa10` | terminal source norm audit |
| #311 | `e4639719f88b80a459a31d205369554dfa7ecaf4` | arithmetic-fiber dilation / adjacent-tree commutator audit |
| #312 | `75db5030dd5defe655f85d195508aae45694ed55` | recombination and lost Euler alternation |
| #313 | `cfb4dc9e043d10b9e251028e5c33d82aa307bfc3` | boundary atomization refutation |
| #314 | `f07f44263c3ff4b219918b05cac61a75e18ff773` | Mersenne saturation refutation and surviving localization |
| #315 | `33b312e32818adb78b5bdc78e4c64f1a870b532c` | atomic-linear boundary but positive outer-band carry flow |
| #316 | `c387a48cd6ff07433aafb08b312c0473efef9192` | first activated boundary with logarithmic central-flow debt |
| #317 | `9b49c103ab3bd91724182c4c2fecfe2f0c9cb490` | eta core, cutoff obstruction, pure-central firewall |
| #322 | `c5cf36c4aa24e632963554fc270ef26bd29d0c61` | five-adic finite-state scope correction |
| #324 | `501af0adf6302a9d15e1badaa7054de9d593db48` | critical-neutral principal mode and dyadic dipole source |
| #332 | `c4d44dd9119795920bbbfae8acc841d28a20883c` | square-root-hinge top-half elimination and CHS frontier |
| #333 | `14731af78ebb0226aa418fd66203c5772b4411c6` | critical-Haar source and cap-boundary scalar |
| #335 | `188bd0362c3a9f88adcbcf5298bf8eeade4016cf` | Gamma/carry convex order, Markov occupation, Pascal Green kernel |
| #347 | `f70bcda4d04200c96ddf5b74bc65ccb4aa8750ae` | outer `255/256` SHARP and shifted-zeta bottom tail |
| #348 | `89f0eb418a470d55e945b08daa3d0f0dc2fc7914` | resident WSTS⇔RH proof, z-collapse, Haar annularization |
| #351 | `22a94f431d7f4cd87db5f3efdd97b086f8f60183` | GFEP/WSTS consolidation and multiplicative-search lineage |
| #352 | `906b5a477a1ed7c88a40db7569924f15f3d54b72` | endpoint symbol, prime-power moat, annular hierarchy, radix-four detail packing |
| #353 | `ed566f3198e236c54ba18049181016536f56d456` | positive occupancy, mean-age, complete-prime-power gap |
| #355 | `2107c85370369372361bb6b82b79ebf0676eb283` | positive first-entrance kernels and genuine nonnegative-flow dual |
| #356 | `1a60df88aadac731ec32e48a87b74537662114dd` | frozen GFEP/BTF refutation, policy dichotomy, Pascal/annular/CN3 continuation |

### Head-reconciliation note

During discovery, the connector returned stale, non-resolving heads for #247 (`4b2805ca13c430cc4717b759223f888752ac8b1e`) and #303 (`e18fc20183e9a84be0a87c68fc0a4bd2ac78b00`). Those refs returned 404 when theorem files were fetched. I therefore recorded the discrepancy and reviewed the live, resolving heads `6c4dadc...` and `4367007...`; I did not silently substitute one claim state for another. The final live recheck found the principal reviewed heads stable.

## 3. Unified elementary route map

### 3.1 Exact finite arithmetic layer

For the critical target

\[
w_X(q)=q^{-1/2}\log(X/q)\mathbf 1_{q\le X},
\]

Möbius inversion produces a node divergence `R_X`. A split flow `d` has carry load

\[
L_q(d)=\sum_m (\partial d)_m\lfloor m/q\rfloor.
\]

Therefore exact carry saturation is equivalent to the finite node equation

\[
\partial d=R_X.
\]

This is the principal finite normal form. Farkas duality identifies the obstruction cone as balanced-superadditive potentials. Size weighting converts the same equation into a descending Markov Green equation

\[
M-MP=s,\qquad s_n=nR_X(n).
\]

No RH input is present in these identities.

### 3.2 Unconditional positive progress

The central first-difference packing is feasible and has entropy

\[
4\log 2\,\sqrt X+O(\log^2X).
\]

This is genuine unconditional progress, but the critical sharp constant is `4`, not `4 log 2`; the missing gain is reuse of residual carry capacity.

For decreasing discretely convex targets, the exact top-half inverse is nonnegative and does not overfill any lower column. Applied to the square-root hinge, it saturates the top half and exports a nonnegative strict-half residual. This is a global, all-parameter theorem, not a finite scan. It does not show that the residual stays in an indefinitely iterable cone.

The Gamma/carry comparison proves a strict margin for the pure square-root state mode. It closes the continuum/state mode, not the arithmetic Möbius occupation.

### 3.3 Signed transport layer

For a fixed policy, every Cycle-Debt dual factors through the policy capacity drift. If `M=s(I-P)^{-1}` is the signed Green occupation and `d_G` the exact capacity drift, the optimized debt is bounded by

\[
\sum_n(-M_n)_+d_G(n).
\]

This identifies the strongest clean policy-level open theorem: construct one explicit cofinal policy for which this weighted negative occupation is subpower.

The boundary version of the same problem must preserve actual edge capacity, keep common destinations recombined, separate fresh from propagated boundary, and delay absolute values until after Pascal-cycle optimization. Current names include SFC, COBT, CBVR, and CNCR. They are best treated as interfaces to one signed capacity-debt problem, not as four independent proof routes.

### 3.4 Consumers

There are several compact consumers:

- signed Cycle Debt or positive near-saturation gives the sharp complete-prime-power ramp and hence RH;
- WSTS is equivalent to RH;
- eventual negativity of the minimal prime endpoint is equivalent to RH;
- the complete-prime-power gap `o(log^2 X)` is equivalent to RH;
- eventual sign of the zero-safe factor-64 annular scalar is equivalent to RH;
- CN3 implies RH and its reverse follows from standard RH bounds in the associated normal form.

These are criteria or conditional consumers, not unconditional sign mechanisms.

## 4. GFEP, BTF, producer positivity, and fragmentation: exact verdicts

| object | verdict | exact scope |
|---|---|---|
| Full coordinatewise GFEP | **FALSE** | For the frozen half-binary/half-ternary first-entrance policy, the fixed exit `(n,p)=(2,2)` changes sign at arbitrarily large integer endpoints. |
| Frozen binary–ternary GFEP | **FALSE** | The certified characteristic pole has shifted real part `>0.4965737487`; both positive and negative excursions exceed every `O(X^delta)` below that exponent. |
| Positive first-entrance packet kernels | **VERIFIED** | Abel/Stieltjes summation makes each kernel coefficient nonnegative for every nonnegative exit trace. This does not make the Möbius-weighted aggregate positive. |
| Sparse producer pointwise positivity | **FALSE for the frozen policy** | The actual sparse producer trace at node two has the same surviving resonance and changes sign cofinally. |
| Generic pointwise producer positivity | **UNPROVEN / GAP** | Other policies, state-dependent policies, and nonstationary policies are not covered by the frozen counterexample. |
| Frozen weighted negative BTF | **FALSE** | The fixed producer coefficient has negative excursions not `O(X^delta)` for every `delta<0.4965737487`; hence its weighted negative ledger cannot be `X^{o(1)}`. |
| Frozen absolute BTF | **FALSE** | The same fixed coefficient forces `sum sqrt(n)|A_X(n)|` to have near-square-root excursions. |
| Signed Cycle Debt | **UNPROVEN / GAP; still live** | A signed pairing or optimized negative-capacity theorem can cancel coordinates before absolute values and is not contradicted by one oscillatory producer coefficient. |
| Finite stationary fixed-ratio spectral gap | **FALSE as a generic mechanism** | Every finite atomic characteristic has nonreal zeros arbitrarily close to the conservation line; there is no source-independent gap. |
| Source-specific signed cancellation | **not ruled out** | The no-gap theorem says nothing about numerator cancellation, selected arithmetic sources, or signed multichannel recombination. |
| State-dependent fragmentation | **live** | An explicit ordered quarter-balanced policy has an exact triangular recurrence and a continuum nonlattice gap; its arithmetic occupation sign is open. |
| Nonstationary/adaptive fragmentation | **live** | No general refutation was found. |
| Continuum/broad policies | **live** | The uniform continuum characteristic has only the conservation root; broad nonlattice policies escape the finite-atomic resonance mechanism. |

The phrase “GFEP is false” should not be used without the frozen policy, exit, and quantifiers. The exact refutation is powerful but narrow: it closes the full coordinatewise and frozen producer-positivity program, not every first-entrance or fragmentation architecture.

## 5. Cycle Debt and boundary lineage

### 5.1 Durable exact identities

The carry/Pascal four-cycle identities, Möbius divergence, balanced-fragmentation/Farkas equivalence, adjacent-tree divisor commutators, and finite capacity LP are durable route infrastructure.

The corrected source-flow coordinate is also exact: a divisor source entry is represented through adjacent complete trees, and a paired eta source has a signed central/sibling identity. What fails is treating that identity as an automatically nonnegative standalone flow.

### 5.2 Exact failures

1. **Source mass is not edge capacity.** A decreasing source `c_n` places `c_n-c_{n+1}` on the canonical root edge. For `c_n=1/n`, the proposed eta switch needs `B_k` but the canonical source flow supplies only `A_k-B_k`, a factor `2k` smaller.
2. **Ordinary terminal atomic norm is macroscopic.** Several independent audits find a complete critical boundary with ordinary divisor-source atomic norm `Omega(X)` (or the relevant macroscopic scaling), contradicting proposed polylogarithmic terminal atomization.
3. **Arithmetic fibers dilate.** A quotient-only or source-blind lift misses full floor/fiber ancestry; naive central recursion can amplify lower-band weighted variation.
4. **The second Euler alternation disappears after recombination.** Common destinations must be summed before absolute values; the recombined tail is ordinary, not the claimed alternating tail.
5. **A submitted weighted boundary schedule fails.** The lower bound refutes that schedule, not every optimized schedule.
6. **Literal divisor max-flow for the critical-neutral annulus is impossible.** Active `3/5/7` divisibility edges preserve the combined Möbius/kernel color, leaving negative components behind a zero-capacity cut.

### 5.3 Surviving repair

The same boundary can have ordinary atomic norm `Omega(X)` yet coherent carry-column mass `O(log^2 X)`. The complete outer band has a zero-negative-debt central realization, and the first activated boundary has an explicit paired representation with logarithmic central-flow debt plus a strict half-scale residual. Thus ordinary atomic-norm failure does not refute optimized Cycle Debt.

The strongest present formulation is:

> Preserve the complete boundary in native Pascal/carry coordinates; bind every source use to actual incoming capacity; recombine common destinations before variation; and prove an all-generation coefficient-one recurrence whose cumulative weighted negative capacity is `X^{o(1)}` or polylogarithmic.

At policy level this is the negative Green-occupation theorem. At boundary level it appears as SFC/CBVR/CNCR. The first genuinely open theorem is the all-generation propagation estimate, not the first-boundary decomposition.

## 6. Pascal, Gamma, SHARP, and the low-row collapse

### 6.1 Uniform Pascal and Green occupation

The exact selected-child kernel is

\[
P_m(k)=\frac{2k}{m(m-1)},\qquad 1\le k<m.
\]

The entrance probability from any `m>n` is `2/(n+1)`, giving the explicit Green occupation

\[
M_n=s_n+\frac{2}{n+1}\sum_{m>n}s_m.
\]

The average-carry inverse is a scalar multiple of this occupation. Hence average-carry inversion, uniform Pascal, and Markov fragmentation are the same object in three coordinate systems.

Full uniform-Pascal positivity is still open. The policy has no deterministic nonreal resonance; all remaining poles arise from the arithmetic reciprocal-zeta factor or source numerator.

### 6.2 Reward rigidity and no-go theorems

Under nonnegative uniform-Pascal reward, eventual affine tail, and removal of the independent 3-channel, the Green reward budget forces `r<=5/2`. Equality uniquely gives the two-low-row reward ratio `15:4` and source polynomial

\[
(1-t)(1-t/2).
\]

This is a global extremum even if infinitely many higher boundary states are allowed.

More strongly, every nonzero nonnegative uniform-Pascal reward has a strictly positive square-root critical defect. Therefore coordinatewise-positive reward and exact critical neutrality are incompatible. No higher-degree positive dyadic filter can repair this.

Allowing signed reward yields the unique minimax critical-neutral adapter

\[
Q_\star(t)=(1-t)(1-\sqrt2\,t).
\]

Its reciprocal-square negative tail sums exactly, collapsing the infinite problem to CN3, a three-source inequality. CN3 is also an odd-annulus scalar and an adjacent-dyadic Mertens-flux bound. The natural divisor graph cannot prove it because of the color-preserving cut.

### 6.3 SHARP

The strongest cofinal finite-depth theorem is:

\[
c_T(j)>0\qquad(j>T/256).
\]

It combines fixed quotient-cell inequalities, an analytic tail, and 261,888 directed endpoint gates. It proves only the outer `255/256`; the inner `1/256` remains open.

The fixed-depth bottom tail is the shifted-zeta squared-hinge state

\[
\mathcal C_R=\sum_{n\le R}\mu(n)(n^{-1/2}-R^{-1/2})^2,
\]

with Mellin transform

\[
\frac{1}{s(s+1)(2s+1)\zeta(s+1)}.
\]

This is distinct from the RH-bearing all-depth SHARP scalar with `zeta(s+1/2)`. Large finite or outer-region positivity must not be promoted to full SHARP.

The two-low-row critical-log scalar and the square-root-hinge scalar are related by a positive Volterra transform. Full SHARP is therefore much stronger than the actual low-row RH consumer.

## 7. WSTS and shell-tail criteria

The repaired resident theorem establishes

\[
\mathrm{WSTS}\Longleftrightarrow\mathrm{RH}.
\]

Load-bearing corrections include analytic extension through the top cell and replacement of a false monotonicity claim for `|g'|` by a valid decreasing majorant. Under RH, a conservative `O(log^4 X)` shell-tail bound is resident. In the other direction, WSTS telescopes to a one-sided prime ramp whose Mellin transform retains every hypothetical off-critical zero; Landau excludes such poles.

An exact one-crossing theorem collapses the even-endpoint shell maximum to one bottom scalar up to a tiny deterministic error. This removes geometric complexity but does not estimate the surviving scalar.

Verdict: WSTS is a compact **RH-equivalent criterion**, not unconditional progress toward RH.

## 8. Prime endpoint, occupancy, complete prime powers, and annular filters

### 8.1 Minimal prime endpoint

The minimal endpoint scalar `A(X)` has an exact Mellin symbol. Eventual negativity of `A(X)` is equivalent to RH. The complete-prime-power decomposition separates a zero-sensitive coordinate from a deterministic moat; the moat is globally negative and decreasing.

### 8.2 Positive occupancy normal form

Every carry column has a positive moving occupancy deficit source. This does not imply pointwise negativity of the endpoint response: each fixed column is eventually positive, so the moving boundary is essential.

For prime weights, endpoint sign is exactly a positive-source backward mean-age inequality. Prime squares supply the entire negative quadratic drift, with source constant `-1-zeta(1/2)>0` after critical normalization.

The complete-prime-power front door is

\[
F_\Lambda(X)=o(\log^2X),
\]

which is equivalent to RH. No eventual sign of the complete gap is required.

### 8.3 Correct finite packing objective

For a feasible packing, the conclusion-producing quantity is signed seed/entropy score loss, not unweighted slack and not pointwise blocker loss. Weights above one may contribute favorably. This supersedes stronger ESGS/ESBT-style unsigned objectives.

Applying the radix-four critical detail to both the target and endpoint atoms gives:

- a strictly positive transformed target;
- a strictly positive triangular endpoint matrix;
- exact telescoping back to ordinary carry feasibility;
- a canonical positive detail greedy.

The remaining theorem is **R4DSL**: prove subquadratic signed score loss. Local matrix positivity is no longer the issue.

### 8.4 Annular criteria

The hierarchy runs through factors 729, 125, 81, and 64. The preferred factor-64 polynomial is zero-safe and has a rigorous RH-side margin. Its eventual one-sign theorem is RH-equivalent and open.

Factor 64 is minimal only under the declared finite integer-radix, phase-blind absolute critical-zero-norm method. It is not a universal lower bound on every annular or source-specific construction.

On uniform-Pascal rewards, every double-neutral finite annular filter has unavoidable signed debt. For the improved factor-64 filter, the reward is negative exactly on states `13..63`, positive on `2..12` and `>=64`, with an explicit positive reciprocal-square tail. This reduces the Pascal/annular bridge to one 51-state payment inequality.

## 9. Eta, Mersenne, critical Haar, and source filters

Exact eta/Mersenne localization, odd-Möbius identities, paired Hausdorff residual structure, and critical-Haar source identities survive.

The following do not survive:

- eventual restricted Mersenne-collar saturation;
- treating a paired eta source as a standalone nonnegative edge flow;
- treating source coefficient mass as available central capacity;
- a source-free five-state/five-residue closure;
- strict source-blind contraction of the complete critical eta mode;
- pure-central eta-resolvent recombination as a new positive producer.

At zeta-zero modes the critical eta multiplier is neutral, not strictly contracting. The correct target is a coefficient-one delayed recurrence. Critical-Haar factors and logarithmic commutators are useful because they preserve off-line poles while canceling neutral or pole-blind modes. They supply compact normal forms and bottom-coordinate telescopes, but their final scalar signs remain open.

When an old Mersenne or eta proof fails, the independent localization, Hausdorff typing, finite shift identity, weighted-jet contraction, and exact source formulas should be retained rather than discarded with the failed closure.

## 10. Elementary-route Rosetta stone

| coordinate/name | same underlying object |
|---|---|
| carry target `w_X` | Möbius node divergence `R_X`; size-weighted source `s_n=nR_X(n)` |
| balanced fragmentation | descending Markov occupation `M-MP=s` |
| average-carry inverse | uniform-Pascal Green occupation, up to the explicit scalar normalization |
| SHARP | nonnegativity of the uniform-Pascal occupation / local-vs-tail inequality |
| Cycle-Debt dual | policy supermartingale drift bounded by the exact capacity drift |
| signed Cycle Debt | weighted negative Green occupation after recombination |
| two-low-row SHARP | critical-log scalar under a positive Volterra transform |
| critical-neutral low-row scalar | CN3 = three source coordinates = odd annulus = adjacent-dyadic Mertens flux |
| prime endpoint `A(X)` | positive occupancy mean-age state plus deterministic prime-power moat |
| complete-prime-power criterion | subquadratic endpoint gap / signed packing-score loss |
| factor-64 annulus | finite signed Pascal reward with debt localized to states `13..63` |
| endpoint atom | carry law plus an elementary exponential delay; Gamma equality weight is formal deconvolution |
| WSTS shell-tail | z-collapsed endpoint scalar and one-sided prime-ramp consumer |
| SFC / COBT / CBVR / CNCR | capacity-faithful all-generation versions of the same signed boundary-debt problem |

## 11. Live, dead, and superseded route table

| route | status | first open theorem or terminal verdict |
|---|---|---|
| exact carry/Pascal divergence and Farkas | **LIVE infrastructure** | construct a source-specific positive or subpower-debt solution |
| central one-pass packing | **VERIFIED but quantitatively insufficient** | improve `4 log 2` to the sharp constant through residual-capacity reuse |
| frozen half-binary/half-ternary GFEP | **DEAD / FALSE** | exact cofinal sign oscillation |
| frozen producer positivity | **DEAD / FALSE** | exact cofinal sign oscillation |
| frozen BTF | **DEAD / FALSE** | fixed coefficient has near-square-root negative excursions |
| finite atomic stationary spectral-gap strategy | **DEAD as a generic mechanism** | no source-independent gap for any finite fixed-ratio policy |
| signed Cycle Debt | **LIVE** | subpower policy Green debt or all-generation capacity recurrence |
| state-dependent broad fragmentation | **LIVE** | finite arithmetic occupation control and finite-to-continuum stability |
| square-root hinge saturation | **LIVE** | prove exported strict-half residual is indefinitely recyclable |
| terminal ordinary atomic-norm closure | **DEAD / FALSE** | macroscopic lower bound |
| cycle-optimized boundary transport | **LIVE** | CBVR/CNCR/SFC all-generation recurrence |
| uniform Pascal / full SHARP | **LIVE** | inner-region/all-depth occupation sign |
| outer SHARP | **VERIFIED partial theorem** | inner `1/256` remains |
| positive uniform-Pascal critical-neutral filter | **DEAD / IMPOSSIBLE** | every positive reward has positive critical defect |
| low-row `15:4` scalar | **LIVE** | sign after corrected positive forcing and Möbius inversion |
| CN3 | **LIVE compact RH-bearing criterion** | adjacent-dyadic Mertens-flux lower bound |
| WSTS | **RH-EQUIVALENT, not a mechanism** | unconditional WSTS is exactly the open RH content |
| prime endpoint eventual sign | **RH-EQUIVALENT** | unconditional sign open |
| positive occupancy / complete gap | **LIVE mechanism/criterion** | subquadratic signed packing-score loss |
| factor-64 annular scalar | **RH-EQUIVALENT** | unconditional sign open |
| factor-64 Pascal bridge | **LIVE** | explicit 51-state payment theorem |
| radix-four detail packing | **LIVE** | R4DSL signed score-loss estimate |
| restricted Mersenne saturation | **DEAD / FALSE** | localization survives, eventual saturation does not |
| pure-central eta positivity | **DEAD / FALSE** | requires noncentral cycles or signed debt |
| fixed-order Abel closure | **DEAD for the proved finite orders** | dynamic, weighted, or scale-dependent variants remain possible |

## 12. First open theorem for each distinct live route

1. **Policy Green Debt:** exhibit an explicit cofinal policy with `sum(-M_n)_+d_G(n)=X^{o(1)}`.
2. **Capacity-faithful boundary recurrence:** prove SFC/CBVR/CNCR after common-destination recombination, with actual incoming capacity and finite collars.
3. **Critical Hinge Saturation:** show the nonnegative strict-half residual from top-half elimination can be iterated to exact saturation.
4. **Uniform Pascal / SHARP:** prove the inner-region occupation sign, or a sufficient low-row combination.
5. **CN3:** prove `3s_2+2s_3>=3sqrt(2)s_1`, equivalently the adjacent-dyadic Mertens-flux bound.
6. **Factor-64 Pascal payment:** pay the exact negative reward block on states `13..63` from low-row reserve and positive tail.
7. **R4DSL:** construct positive detail-feasible endpoint weights with signed entropy-score loss `o(log^2X)`.
8. **Endpoint occupancy transport:** realize the continuum Gamma/carry coupling in the finite arithmetic matrix with subquadratic signed score loss.
9. **All-depth SHARP tail:** prove the shrinking bottom-tail threshold comparison uniformly as depth tends to infinity.
10. **Adaptive fragmentation:** construct a nonstationary or state-dependent policy whose source-specific numerator and Green occupation avoid the finite-atomic resonance obstruction.

## 13. Ten high-value dormant questions worth reviving

1. Can the ordered quarter-balanced policy’s exact sliding-band recurrence be combined with a discrete nonlattice renewal theorem strong enough to control the Möbius source?
2. Is there a finite-to-continuum stability theorem that preserves weighted negative Green occupation, not merely spectral location?
3. Can first-generation logarithmic boundary debt be propagated with coefficient one after separating fresh and inherited boundary?
4. Does the strict-half residual produced by convex top-half elimination admit a canonical positive hinge decomposition at the next scale?
5. Can CN3 be proved by a parity-breaking transport between incomparable odd squarefree components rather than divisibility edges?
6. Can the factor-64 51-state debt be paid by a monotone comparison theorem for the explicit Pascal occupation?
7. Can the radix-four detail greedy be analyzed directly in signed entropy score instead of unsigned slack?
8. Can the endpoint atom-to-Gamma martingale be discretized state-dependently without requiring positivity of the reciprocal-zeta deconvolution factor?
9. Is there a nonstationary policy whose local laws approximate the broad continuum kernel while retaining exact finite carry identities?
10. Can the inner SHARP region be compressed to finitely many low-row scalars without introducing a filter zero that cancels an off-line zeta pole?

## 14. Heavy computations inspected but not rerun

No large scan, exhaustive multiplicative-class search, large Walsh-Hadamard transform, large interval/Rouché computation, producer scan, or expensive LP sweep was launched in this review.

I inspected retained code, manifests, hashes, mutation tests, and outputs for, among others:

- #356 `X-90204`: exact Fraction recurrences through 20,000, 70-digit complex interval arithmetic, a radius-`1e-18` Rouché disk, and 39,998 trace checks;
- #347 `X-32307`: 261,888 directed endpoint tail gates and quotient cells through 255;
- #352 annular artifacts: endpoint scans through five million and 1,024 rational Bernstein subinterval certificates;
- #351 multiplicative/Walsh-Hadamard searches with classes reported up to `2^669`;
- #247 reconnaissance through `10^8`;
- #332 multi-million-row reserve checks and the symbolic all-parameter floor-prefix certificate;
- #315 complete boundary and outer-band checks;
- #353 26,059 exact source and cell identities;
- #303 tens of thousands of exact source-flow, commutator, parity, and capacity identities;
- #301 truncated interval/Perron certificates.

Only the retained proof objects and their claimed scopes were reviewed; these heavy experiments were not independently reproduced.

## 15. Urgent contradictions for the integrator

1. Do not integrate any statement of full coordinatewise GFEP or frozen binary–ternary producer positivity as open; both are exactly false.
2. Do not retain frozen BTF as a live hinge; its weighted negative and absolute forms fail cofinally.
3. Do not infer edge capacity from Hausdorff source mass; the canonical capacity is a first difference and may be smaller by factor `2k`.
4. Do not use a polylog terminal ordinary divisor-source atomic norm; the complete critical boundary has a macroscopic lower bound.
5. Do not take absolute values before recombining common destinations; the claimed second Euler alternation is then false.
6. Do not claim a source-independent gap for any stationary finite fixed-ratio fragmentation policy.
7. Do not claim exact critical neutrality from a coordinatewise-positive uniform-Pascal reward; a global no-go theorem forbids it.
8. Do not call factor 64 universally minimal; the theorem is relative to the declared phase-blind integer-radix method.
9. Do not promote outer `255/256` SHARP or finite endpoint scans to full/cofinal SHARP.
10. Do not retain eventual restricted Mersenne saturation or pure-central eta positivity; preserve only their independent localization and exact identities.
11. Do not treat WSTS, CN3, endpoint negativity, complete-gap decay, or annular sign as unconditional progress; they are RH-bearing criteria.
12. Do not advertise any elementary chain as a proof of RH. Every current route still contains an explicit RH-bearing sign, debt, recurrence, or score-loss theorem.

## 16. Integration recommendations

1. Canonicalize the exact finite spine around carry divergence, Markov occupation, and the policy-capacity dual.
2. Mark #356’s frozen GFEP/BTF refutation as the terminal lifecycle event for those antecedents while preserving #355’s positive packet kernels and #247’s divergence/Farkas infrastructure.
3. Treat SFC, COBT, CBVR, and CNCR as related interfaces to one signed boundary-capacity problem; avoid four parallel “last theorem” narratives.
4. Promote the uniform-Pascal Green formula as the Rosetta coordinate linking average-carry inversion, SHARP, and fragmentation.
5. Keep partial SHARP results in a fixed-depth section and explicitly isolate the inner/all-depth scalar.
6. Separate endpoint criteria from mechanisms: endpoint symbol, moat, and factor-64 equivalence are criteria; occupancy and radix-four positive details are mechanism infrastructure; R4DSL is the open estimate.
7. Preserve all exact refutations beside the repaired surviving statements, especially the norm distinction `ordinary atomic Omega(X)` versus `carry-column O(log^2 X)`.
8. Use the status TSV accompanying this report as the claim-level import checklist.

## 17. Final proof boundary

The repository now has a strong elementary map, exact finite normal forms, several unconditional positive theorems, sharp mechanism-class no-go results, and compact RH-equivalent criteria. It does **not** contain a verified unconditional proof of any remaining RH-bearing sign, debt, recurrence, or score-loss theorem.

**Riemann Hypothesis: UNPROVED.**
