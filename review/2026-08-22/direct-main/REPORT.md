# Direct-to-main scientific delta audit

**Repository:** `gfreund123/riemann`  
**Audit range:** `a88bed9711b1b2057fb258354924056c5ad8696b..677203992eb0168920365ee45ae9db76bfa97dcf` with the base excluded and the head included  
**Commits classified:** **85**  
**Review date:** 2026-08-22  
**Scientific status:** **RH remains unproved.**

## Executive verdict

The 85 direct-to-main commits form eleven contiguous packets:

- eight scientific/research packets;
- one reviewed-state synchronization packet;
- one duplicate/publication-probe packet;
- one README-only branding packet.

No packet changes the present status of the Riemann Hypothesis.

The strongest direct-main mathematics not already visible from a PR-number chronology is:

1. the exact Cauchy/Jordan source, scattering, rational-storage, Hardy-factor and safe-line compound-Poisson identities in `L-91014`--`L-91029`;
2. the exact nonduplicating causal-packet identity and total child coefficient `<1/8` in `L-91355`;
3. the direct fixed-row reciprocal-zeta Mellin transform and large-row noncancellation in `L-96000/L-96001`;
4. the activation-zero supercritical positivity and Euler--Taylor positive-remainder ladder in `L-99930/L-99931`.

Each conclusion-facing route nevertheless stops at an explicit unsupported or RH-equivalent statement:

```text
Cauchy/Jordan:
  completed first-chaos source-to-boundary domination / CJHI;

P79/factor-54:
  source-labelled row provenance, true causal packet typing,
  noninherited rows and one-use physical ledger;

T-96000:
  simultaneous global positivity of the prime-sieved native rows;

T-99930:
  critical envelope or subpower negative mass of the last scalar.
```

## Commit coverage

`COMMIT_PACKETS.tsv` partitions the range by contiguous commit indices. GitHub compare checks give cumulative packet endpoints

```text
7, 16, 26, 27, 32, 48, 53, 64, 66, 67, 85.
```

The packet sizes are

```text
7 + 9 + 10 + 1 + 5 + 16 + 5 + 11 + 2 + 1 + 18 = 85.
```

Thus every commit is classified exactly once as a reviewed theorem packet, a packet controlled by later review/refutation, metadata/documentation, or duplicate/recovery. No commit is left `TARGETED_REVIEW_REQUIRED`.

## Packet dispositions

### DM-001 — Brownian reviewed-state synchronization

**Commits:** `de605b718682b588dfad6736235347923f194dab` through `b812a249d463772dc66e94d252449ed1529c5923`  
**Count:** 7  
**Verdict:** `METADATA_ONLY`

These commits update the August 11 integration front door after the Brownian review. They modify only integration status, claim-resolution and handoff files. They introduce no new Brownian theorem and should not be counted as an additional scientific wave.

### DM-002A — Cauchy/Jordan source and scattering foundation

**Commits:** `4996719fc2d804f3ae2416930f25045880c60557` through `5350f8a81702e4cd6ff9f7b0cd59c6a523dfcffe`  
**Count:** 9  
**Claims:** `L-91014`--`L-91020`  
**Verdict:** `VERIFIED_WITH_FIXES`

The exact local mathematics substantially survives:

- `L-91014`: positive generalized-Jordan divisor isometry, coherent tensor factorization and logarithmic coproduct;
- `L-91015`: pole-subtracted affine recurrence and positive tail/Hankel forcing under its displayed sign convention;
- `L-91016`: fixed-axis all-pass diagonalization, off-line hyperbolic signature and depth projector;
- `L-91017`: tensor commutation and critical main-state algebra;
- `L-91018`: positive two-port Cauchy-detail Gram;
- `L-91019`: exact second-jet ANOVA decomposition;
- `L-91020`: safe-line random-unitary/CP correlation channel and forward negative-mass contraction.

These are operator/source identities, not a completed RH route. `L-91020` is one-way. The inverse implication needed by the scale recurrence is absent.

PR #400 controls this family. It preserves amplitude-level and first-chaos structures while refuting the scalar form-core shortcut, the inference from amplitude unitarity to radial-curvature sign, and the scalar-commutator replacement for the full delayed Gram.

### DM-002B — normalized Cauchy recurrence, heat band and prime semigroup

**Commits:** `a7db1ffcd74211aa949606b22ca77d9fe4e0a42b` through `3fed211942d51d2c01a19bf89aa502ed10a4b811`  
**Count:** 10  
**Claims:** `L-91021`--`L-91029`, `T-91005`  
**Verdict:** local theorems `VERIFIED` or `VERIFIED_WITH_FIXES`; `T-91005` is `OPEN_RH_EQUIVALENT`

The strongest exact results are:

- the factor-16 rational storage identity and exact three-square residual in `L-91022`;
- the fixed completed-xi scattering factorization and delay identity in `L-91023`;
- the per-atom positive heat-band/Laplace representation in `L-91024`;
- the exact one-plus-three cubic source-port decomposition in `L-91025`;
- the scalar rational Hardy spectral factor in `L-91026`;
- the exact two-section xi scattering cocycle in `L-91027`;
- the safe-line compound-Poisson prime semigroup and carré du champ in `L-91029`.

`L-91021` and `L-91028` give unconditional sufficiently-large-scale terminal positivity. They are plausible and structurally sound, but canonical extraction should state the exact uniform differentiated-Stirling estimate and its effective constants rather than leave them in `O(1)` form.

`L-91024` must be typed carefully. Complete monotonicity of one real critical-line atom is unconditional. Complete monotonicity of the full zeta gate is proved **under RH** and is not an unconditional heat theorem.

`T-91005` is an exact criterion: the coefficient-one normalized recurrence for all carriers and scales is RH-equivalent. It should be registered as an equivalence, not advertised as independent progress.

A local convention repair is required between `L-91026` and `T-91006`: the two files choose conjugate Hardy factors and attach opposite causal-pole labels. Their moduli agree, but one canonical Fourier/Hardy convention must be selected before output orientation is used.

### DM-002C — T-91006 proposal wrapper

**Commit:** `b837c12199dd407116f604ce6c938039d1a76da4`  
**Verdict:** `OPEN_RH_EQUIVALENT`

`T-91006` is not a proof theorem. It defines CJHI as the exact remaining theorem:

```text
safe positive Jordan first chaos
  + completed gamma/pole channel
  -> lossless boundary Hardy Gram
  + positive complement,
```

with coefficient-one return and every carrier cross term preserved.

PR #400 supersedes the wrapper's preferred wording. The controlling open statement is completed source first-chaos curvature dominating the model-space tangent leakage on the corrected delayed form core. This is RH-equivalent and remains open.

### DM-003A — original P79 finite Hall and target-flow wrapper

**Commits:** `1aa5878d42cedf8a7bda0a8200582595bd51ee90` through `af2bec38df64bc18086de0c93d256149c07d86ac`  
**Count:** 5  
**Claims:** `L-91347`, `L-91348`, `T-91303`  
**Verdict:** `SUPERSEDED`

`R-91308` later shows that the original `L-91347` checker used a global convex minimum outside the active cell. `R-91309` shows that target-exact Hall residual coefficients do not automatically reproduce the arithmetic component row.

The scalar target-flow/debt algebra of `L-91348` may be retained conditionally once true causal Hall capacities exist. `T-91303` must be archived as a failed full-proof wrapper.

### DM-003B — corrected-cell and direct-Euler proposal

**Commits:** `a1c243935e18b78af5959ed7e714b06764fdc9d5` through `d688cc7cb73eea9e50f10352a50516ab2c4f4625`  
**Count:** 16  
**Claims:** `R-91308`, `L-91350`, `R-91309`, `L-91351`, `T-91304`, `O-91311`  
**Verdict:** `GAP_BLOCKED`, with two exact false subclaims

PR #431 is the controlling direct reconstruction.

Its exact findings are binding:

1. `L-91350.2` is false. At `t=79`, `p=83`, `y=1`, sources `85`, `86` and `87` occur in the formal prefix but exceed `py=83`, so their actual causal contribution is zero.
2. `X-91127` uses the same false formula, omits parent activation cells, does not match its retained JSON schema, and is not hash-locked.
3. A hidden hazard child has target `2r` and score `r^2`; an `r`-scaled canonical child has target `2r` and score `r`.
4. Pointwise source fractions are not automatically scalar weights for a signed endpoint-loss functional.
5. Rows `j>y` are not covered by the inherited-row positivity theorem.

PR #436 adds another exact correction:

```text
A_P(83) < 0,
```

so the uniform positive score-surplus claim in `L-91351.11` is false.

What survives from direct main is narrower:

- the exact one-prime divisor-row identity;
- exact companion target and score identities;
- inherited residual-row positivity at its stated scope;
- the exact score-minus-target formula before the false sign estimate;
- the source-type refutations `R-91308/R-91309`.

PR #436 later supplies a true causal Hall replacement and literal residual-row entropy results. Those later heavy certificates were not rerun here. Their remaining conclusion-facing theorem is LRPT/SFFEP, the source-labelled common-flow and finite-frontier provenance theorem.

`T-91304` does not establish RH.

### DM-003C — causal nonduplicating packet budget

**Commits:** `4e203a42ec4dae6590d15f8c92a56d28c0ae2a5a` through `9c7538559d7f56c2914b39aed5a1fb3fbf7ce131`  
**Count:** 5  
**Claim:** `L-91355`  
**Verdict:** `VERIFIED_WITH_FIXES`

The exact identities survive:

```text
s_k + sum_j lambda_j = 1,

P_X
 = s_k P_X
 + sum_j lambda_j [P_X-r_j A_(p_j)P_(X/p_j)]
 + sum_j alpha_j A_(p_j)P_(X/p_j),

sum_j alpha_j < 1/8.
```

This is a useful standalone source-ledger theorem. It prevents parallel-parent duplication and closes child-mass accounting.

It does **not** prove that the survival and causal residual terms are positive native physical packets. That packet-typing theorem remains open. PR #439 controls this distinction.

### DM-004 — T-96000 fixed-row Mellin packet

**Commits:** `29e093940e9fdc7b96c103da40a729b23aa7e549` through `994bd4bedcc8b61cebabaf005cc69225fc3fe459`  
**Count:** 11  
**Claims:** `R-96000`, `L-96000`, `L-96001`, `T-96000`  
**Verdict:** analytic layer `CONDITIONAL_EXACT`; proof wrapper `GAP_BLOCKED`

The transform

```text
C_j(s)
 = C_j/s^2
 + P_j(s+1/2)/(s^2 zeta(s+1/2))
```

is exact on its initial convergence half-plane and supplies the stated meromorphic continuation. `L-96001` gives a valid large-row noncancellation asymptotic.

The conclusion is conditional on simultaneous global nonnegativity of the prime-sieved rows. PR #544 preserves the fixed-row consumer but rejects the `FRONTIER-CHAIN` producer: grouping by product leaves one knot, whereas the claimed transport uses multiple knots without a global one-use cross-product allocation.

The row-selection issue should be stated precisely. A proof by contradiction may choose `j` after a hypothetical zero **if** one fixed countable family has already been produced and all of its rows are globally nonnegative. It is not valid if the producer itself changes the detector after seeing the zero or horizon. The later fixed rows `2,3`, and especially the fixed 5:3 scalar, remove this ambiguity and are preferable canonical consumers.

Canonical integration should retain `L-96000/L-96001` as analytic predecessors and exclude `T-96000` as a proof claim.

### DM-005 — publication probes

**Commits:** `203e7cd3d35ff41556ccc37e5544355b057dd1b2` through `f789265569013ebff254b082c2e0428970bdaf57`  
**Count:** 2  
**Verdict:** `DUPLICATE_RECOVERY`

These are one-line remote publication tests. They contain no theorem.

### DM-006 — README branding

**Commit:** `bac504b2d227669d9d5310d96e6cf805f6376ff2`  
**Verdict:** `DOCUMENTATION_ONLY`

The commit links the repository to the Agentic Polymath Project. It has no scientific effect.

### DM-007 — T-99930 critical Taylor packet

**Commits:** `7472f585892e2aebf11e9749131f2e490e55743b` through `677203992eb0168920365ee45ae9db76bfa97dcf`  
**Count:** 18  
**Claims:** `L-99930`, `L-99931`, `L-99932`, `R-99930`, `T-99930`  
**Verdict:** unconditional local results survive; terminal estimate is `OPEN_RH_EQUIVALENT`

The strongest previously under-indexed result is `L-99931`:

> every Euler--Taylor remainder whose effective prime exponent is at least `3/2` is positive.

Together with `L-99930`, this supplies:

- global activation-zero positivity for every real `m>=2`;
- certified alternating orientation of every absolutely convergent Euler layer through exponent `3/2`;
- an exact identification of the first prime-harmonic layer where the simple contraction fails.

`L-99932` then constructs one fixed critical scalar with an explicit positive kernel and a reciprocal-zeta Mellin transform that is holomorphic at positive real points and retains every hypothetical off-line pole.

The positive kernel is not the positive arithmetic output. The native Möbius projection remains signed.

`R-99930` is a valuable no-go theorem: supercritical positivity gives a nonnegative primitive of the critical density, not its sign; positive smoothing cannot cancel the last real carrier.

PR #663 strengthens the supercritical theorem in the ordinary SHARP setting and identifies the critical prime-harmonic wall. PR #668 proves exact distributional descent and classifies the critical weighted downward-variation estimate as RH-equivalent.

`T-99930` is therefore a valid synthesis and fixed-detector criterion, not an RH proof.

## Computation policy and dispositions

No heavy computation was rerun.

The review used only:

- exact source and SHA/path inspection;
- small rational identities;
- representative packet-weight fixtures;
- standard-library validation;
- method and retained-artifact inspection.

The direct-main P79 certificate `X-91127` is rejected as a complete proof object for exact mathematical reasons independent of rerunning its 383,472 gates.

The later replacement campaigns in PR #436 are recorded as:

```text
RETAINED ARTIFACT / METHOD AUDITED / HEAVY CAMPAIGN NOT RE-RUN.
```

## Strongest results safe to canonicalize

Subject to the local fixes in `CLAIMS.tsv`:

1. `L-91014`: positive generalized-Jordan divisor isometry and coproduct.
2. `L-91019/L-91025`: exact positive finite-jet orthogonal decompositions.
3. `L-91022`: exact factor-16 storage and three-square residual.
4. `L-91023/L-91027`: completed xi scattering factorization and cocycle.
5. `L-91026`: scalar rational Hardy spectral factor, after convention repair.
6. `L-91029`: safe-line compound-Poisson prime semigroup and carré du champ.
7. Exact `L-91351` one-prime row/target/score split identities, with false sign and typing conclusions removed.
8. `L-91355`: nonduplicating causal packet budget and `<1/8` child mass.
9. `L-96000/L-96001`: fixed-row Mellin transform and analytic noncancellation.
10. `L-99930/L-99931`: supercritical activation-zero positivity and positive Taylor-remainder ladder.
11. `L-99932`: fixed zero-safe critical scalar and conditional Mellin--Landau consumer.
12. The direct and later mechanism refutations listed in `REFUTATIONS.tsv`.

## Packets requiring exclusion from canonical proof status

Exclude or archive as historical wrappers:

- `T-91006` as a purported completed route;
- `T-91303`;
- `L-91350/X-91127`;
- `L-91351.11` and the positive typed-splice conclusion;
- `T-91304`;
- `T-96000`;
- any reading of `T-99930` that treats the critical estimate as proved.

## Exact additions Reviewer D must make

1. Add `COMMIT_PACKETS.tsv` or an equivalent range registry to the reconciliation freeze.
2. Add direct-main provenance rows for every surviving claim in `CLAIMS.tsv`.
3. Record PR #400 as controlling the Cauchy/Jordan conclusion-facing interface.
4. Record PR #431 and PR #436 as controlling the P79 direct-main corrections.
5. Record PR #439 as controlling the scope of `L-91355`.
6. Record PR #544 as controlling the T-96000 producer gap.
7. Record PR #663 and PR #668 as controlling the T-99930 supercritical/critical boundary.
8. Canonicalize the fixed Mellin consumer using rows `2,3` or the fixed 5:3 scalar while retaining `L-96000/L-96001` as historical analytic predecessors.
9. Add the T-99930 Taylor ladder to the standalone-results index.
10. Add the causal Hardy-factor orientation discrepancy to the normalization fixes.
11. Mark all heavy replacement artifacts retained but not rerun.
12. Preserve the final generated statement:

```text
DIRECT_MAIN_PACKET_CHANGES_RH_STATUS: false
```

## Final conclusion

No direct-main packet proves RH, and no direct-main packet creates a reviewed-only path to RH.

The range contains valuable standalone mathematics and several exact no-go results. Its main integration value is to recover those results from direct-main history while preventing four historical full-proof wrappers from being mistaken for canonical proof status.
