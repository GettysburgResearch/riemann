# Integration-wave review: Brownian, operator, finite criteria, and Anthropic Zeta23 routes

**Review cutoff:** `2026-08-11T14:03:15Z`  
**Repository:** `gfreund123/riemann`  
**Frozen base (`main`):** `d6409319b4041cd09bee85f55a344631508f2501`  
**Review branch:** `review/integration-wave-20260811-independent-routes`  
**Scope:** Brownian/direct-xi, Weil/screw/carrier/operator, finite Robin/Nicolas/Li/Pick/Loewner, Anthropic Zeta23 import and local descendants. The elementary carry programme was reviewed only where an ostensibly independent route terminates at the same arithmetic floor.

## Executive verdict

No reviewed branch proves the Riemann Hypothesis.

The strongest genuinely independent live proposal is the **raw one-sided Brownian/Dirichlet-Hermite route**. Its finite gamma algebra, Dirichlet-average factorization, reciprocal Hermite interpolation, local-uniform convergence to xi, and exact half-plane stability for `N=2,3,4` survive review. It genuinely avoids the known symmetrized positive-Robin-mixture obstruction because its zero-bearing factor is the single Mellin transform `E[Q_N^z]`, not a positive combination of one-fiber determinants. The decisive all-`N`, or merely cofinal, half-plane nonvanishing theorem is open.

The **symmetrized Brownian/Robin route** retains exact one-fiber self-adjointness. Its two proposed easy closures do not survive: finite reflected-tail domination is impossible, and positive mixtures of the correct fibers do not preserve real-rootedness. The only surviving complete mechanism is an unconstructed aggregate canonical system/de Branges realization.

The **Weil/screw/carrier/operator corpus** contains substantial exact finite infrastructure, but its cofinal endpoint is not independent. Positive-complement elimination gives

`B - Z* C^{-1} Z <= B`,

so a Schur complement cannot repair a negative kernel direction. After complete capture, the vanishing corrected-kernel floor is an RH-equivalent criterion. The square-screw scalar is also the constant coordinate of the full matrix, so matrix enlargement does not bypass that scalar sign.

The **finite Robin/Nicolas/Li/Pick/Loewner programmes** provide authenticated finite barriers, finite semidecisions, and excluded feature spaces. No strict negative Riemann-data witness survives exact replay. In particular, the strongest declared Pick boxes are positive, and all 266 floating full-grid negative candidates in PR #80 replay positive.

The **Anthropic Zeta23 result** is a genuine upstream unconditional zero-proportion theorem and explicitly not an RH proof. The official paper and pinned Lean repository support the headline fixed-window Theorems A-E. Local short-window, growing-conductor, multirate, alias, prime-bank, Xi-cardinal, Fredholm/heat, and Q4 extensions are not covered by that upstream formalization.

Two urgent integration blockers were found:

1. `L-90301.8` on PR #357 is **FALSE as written**. For `K=-I_2`, its universal two-by-two formula returns `delta(K)=1`, while `tr(K_-)=2`. The adjacent trace/curvature transfer in `L-90301.6-.7` survives.
2. `claims/theorems/T-90502-pole-null-fredholm-heat-rh-equivalence.md` on PR #368 is binary-corrupted and not valid UTF-8 Markdown. Blob: `f5bbc2392327b965a278917076c470f7eb15f359`. The clean supporting lemmas remain reviewable, but this theorem artifact must be rewritten before integration.

## Freeze and live-repository handling

The initial cutoff was `2026-08-11T14:03:15Z`. `main` and the review branch were independently re-fetched at `d6409319b4041cd09bee85f55a344631508f2501`. One connector endpoint initially returned an impossible identifier while resolving a slash-containing branch ref; a direct commit fetch rejected it, so no conclusion uses that discarded response.

PR #364 moved while the review was in progress:

- first inspected: `219330bd0441a284fd16ff728dd843a7ee4503ee`;
- later observed and re-reviewed: `46caa771ad2ab7875c3ccd079d3ba327249fd9a4`.

The second freeze also discovered PRs #367 and #368 and added them to scope.

The review inspected theorem/lemma files, dependencies, corrections, refutations, source locks, formalization source, retained certificates, manifests, and available output ledgers. PR descriptions were not treated as proofs.

## A. Brownian and direct-xi routes

### A1. Finite gamma/Norlund approximants

At PR #296, with `S_N=sum_{n<=N} Gamma_{2,n}/n^2`, the Laplace product

`E exp(-q S_N)=prod_{n<=N}(n^2/(n^2+q))^2`

and the Mellin factorization

`m_N(s)=pi^{-s/2} Gamma(1+s/2) D_N(s)`

are exact. The stated strip estimate yields local-uniform convergence to the chosen xi normalization; symmetrization doubles the limit. The cardinal derivative-sampling identities are exact finite algebra.

**Verdict:** `VERIFIED`, `UNCONDITIONAL THEOREM` for the finite identities and convergence. The Rouché implication remains conditional on a cofinal approximant zero-location theorem; local-uniform convergence alone does not supply it.

### A2. Correct Robin fiber

The corrected fiber is

`Phi_l(z)=cosh(l z/2)+2 z sinh(l z/2)`.

For `l>0` it is the characteristic determinant of a self-adjoint Neumann-Robin problem and has imaginary zeros in the branch convention used. For `l<0` there is one real pair. The frozen #296 theorem already uses the corrected even determinant; #318 is therefore a correction/provenance descendant, not a refutation of all #296 algebra.

**Verdict:** `VERIFIED WITH FIXES`, `UNCONDITIONAL THEOREM`.

### A3. Symmetrized shortcuts

PR #318 gives exact obstructions:

- finite reflected-tail domination is incompatible with the two tail asymptotics;
- positive mixtures of the correct one-fiber determinants need not be real-rooted; `Phi_0+0.1 Phi_8` violates the necessary Newton inequality.

**Verdicts:** reflected-tail shortcut `VERIFIED`, `REFUTATION`; positive-mixture closure `FALSE`, `REFUTATION`.

**Surviving scope:** only an aggregate positive canonical system/Hermite-Biehler construction for the full approximant. No such system is built.

### A4. Raw one-sided route

PR #343 obtains

`S_N=G_{2N} Q_N`,  `Q_N=sum_j W_j/j^2`,

with `W` Dirichlet of parameters `(2,...,2)`, and

`D_N(2z)=Gamma(2N+z)/(Gamma(2N)Gamma(1+z)) E[Q_N^z]`.

The branch also proves an explicit all-`N` exponential numerator, reciprocal double-knot Hermite interpolation, exact zero-freeness in the required half-plane for `N=2,3,4`, a squared-tail Euler-sine-product formula, a serial exponential recurrence with forced gamma zeros, the exact adverse-shift threshold `N>=4i^2`, and an explicit minimum/survival/Laplace normal form.

These are exact and materially stronger than the symmetrized route. They do **not** prove the needed minimum-phase theorem: increasing hazard/log-concavity of the underlying survival distribution does not automatically imply complex half-plane zero-freeness of its bilateral Laplace transform.

**First open theorem:** prove for all sufficiently large `N`, or a cofinal sequence,

`E[Q_N^z] != 0` for `Re z > 1/4`,

in the exact shifted convention required by the Rouché step.

**Route verdict:** `UNPROVEN / GAP`, `PROPOSED COMPLETE THEOREM`; genuinely independent of carry/Q4.

## B. Weil, screw, carrier, and operator routes

### B1. Exact finite infrastructure

- PR #65: finite carrier/fixed-vector positive certificate. `FINITE SEMIDECISION`, not cofinal positivity.
- PR #98: exact screw-convexity/minimization algebra; large scan remains `EMPIRICAL ONLY`.
- PR #144: localized ground-state/bottom monotonicity. Completeness converts the route into an `RH-EQUIVALENT CRITERION`.
- PR #168: exact finite packet repair. Capture of the omitted complement remains open.
- PR #192: complement augmentation is exact; positivity of the added complement does not imply positivity of the full form.
- PR #199: exact Schur classifier `S=B-Z* C^{-1}Z <= B`; after capture, the corrected-kernel floor is the RH-bearing endpoint.
- PR #204: local Mobius/kernel synthesis is exact; complete tails are open.
- PR #206: fixed two-frame radical-tail closure is insufficient; this is a route no-go result.
- PR #208: the square-screw statistic is the constant coordinate of the full matrix; a matrix bound must prove that scalar sign too.
- PR #218: Haar/r-adic finite algebra is exact; no cofinal positivity theorem.
- PR #337: Suzuki admissible shift-to-zero is equivalent to unshifted Weil positivity; a finite shifted real-zero theorem is not enough.

### B2. Guardrails and refutations

PR #140 correctly blocks the invalid inference from a locally zero-free slab or finite real-zero theorem to global Weil/Pick/screw positivity. PR #337 supplies a finite-dimensional shifted/unshifted countermodel. Ground-state subtraction, shift conventions, and finite spectral reality must not be conflated with the unshifted global Weil criterion.

### B3. Exact current endpoint

The operator programme should be integrated as layered route infrastructure, not as a completed proof. Its first open theorem is a cofinal capture statement together with

`B_ker,j - Z_ker,j^* C_j^{-1} Z_ker,j >= -epsilon_j G_ker,j`,  `epsilon_j -> 0`.

At complete capture this is an `RH-EQUIVALENT CRITERION`, not an independent analytic estimate that may be assumed.

## C. Finite Robin, Nicolas, Li, Pick, and Loewner programmes

### C1. Robin/Nicolas

- PR #24 supplies an exact finite Robin barrier, including the finite crossing data. `VERIFIED`, `FINITE SEMIDECISION`.
- PR #34 reports a much larger finite range but the raw complete stream is not retained; keep a provenance caveat.
- PR #53's terminal `10^100` stream is omitted; its global finite-range claim remains `UNPROVEN / GAP` until the stream is supplied.
- `L-3107` on PR #33 is sound additive-margin/checkpoint infrastructure for Nicolas, not a cofinal theorem and not a negative witness.

No finite Robin or Nicolas violation is authenticated.

### C2. Li/Hermite

- PR #22 is numerical reconnaissance only; no negative Li coefficient.
- PR #33 proves an exact negative-window statement for the contribution of one hypothetical off-line quartet, but it does not control the total Li coefficient.
- PR #141 gives exact Hermite/inertia algebra and correctly refutes the complex-center shortcut.

No authenticated negative total Li coefficient exists.

### C3. Pick/Loewner/CvS

- PR #67 closes a declared 520-feature value-only table positively.
- PRs #68 and #71 prove complete positivity of their declared eight-point matrix boxes.
- PR #80 replays all 266 floating full-grid negative candidates as positive and certifies the strongest fixed direction positive.
- PR #125 contains strict negative synthetic controls only; they are checker tests, not Riemann-data witnesses.
- PR #173 supplies Connes-van Suijlekom normalization/coordinate corrections.

**Verdict:** exact finite exclusions and finite semidecisions survive; no strict negative Riemann-data witness and no cofinal feature-completeness theorem.

## D. Anthropic Zeta23 upstream and local descendants

### D1. Upstream theorem and formalization

Primary upstream pins:

- official paper SHA-256: `6792988e6cd0e17690621ce898abd5d534f98407741bc7cb14bbe7d07c77d72f`;
- official concise note SHA-256: `45e0330ad37965e5531fa1f4f11e5bebcae147a5237a3e5b3d029efa7ddf759d`;
- Lean repository `anthropics/zeta-23-lean`: `3635e74826a4c1fcece7d1cd2b6fa75e43a00510`;
- Mathlib: `51e6992efd06126df61a496bebf8f49482a4e129`;
- Lean toolchain: `4.33.0-rc2`.

For each fixed `0<lambda<=1`, the paper proves effective sufficiently-large-`T` results in the fixed dyadic/cumulative window setting. Headline proportions are at least `2/3` on the line, `2/3` simple and on the line, and `5/6` distinct, with optimized variants approximately `0.67250`, `0.67250`, and `0.83625`. The package also treats each fixed primitive Dirichlet `L`-function.

The pinned Lean source proves headline Theorems A-E without user hypotheses, against Mathlib's analytic foundations. The source and audit were inspected; the major build was not rerun. A separate bandwidth-one ceiling theorem carries an additional interval-enclosure premise and must not be described as having the same hypothesis-free status as A-E.

**Verdict:** `IMPORTED / UPSTREAM VERIFIED`, `UNCONDITIONAL THEOREM`. Explicitly not RH.

### D2. Preferred local import boundary

PR #361 at `c13b8836f6c7f4e36f17ab1c4ebe41e4cf072f2e` correctly separates upstream source locks/audit from local extensions. Use it as the provenance front door.

### D3. Local extensions

- PR #358: completed-lattice co-lattice identity is locally exact, but the short-window/growing-conductor theorem lacks uniform Riemann-von-Mangoldt/trace/end-effect/omitted-factor/pole/taper closure. `UNPROVEN / GAP`.
- PR #360: no-alias and alias/polyphase decompositions are exact. The prime-bank estimate is only for fixed or restricted subpolynomial banks; growing banks and cross-alias terms remain open.
- PR #363: coherent same-lattice compression and the off-line-pair spectrum are exact local identities, not an upstream theorem transfer.
- PR #364: finite and terminal Gaussian isolation of a hypothetical off-line pair survives review at moved head `46caa771...`; the threat-chain argument uses `O(sqrt N log N)=o(N)`. No RH theorem follows without the terminal sign.
- PR #365: Xi-cardinal RKHS competitors and critical-lattice capture are strong route infrastructure; the corrected arithmetic floor remains open.
- PR #366: confluent cluster/jet renormalization is valid at fixed order; uniform growing order, tails, and the floor are open.
- PR #367: reduces the corrected floor to a terminal Gaussian-Chebyshev scalar. This is an `RH-EQUIVALENT CRITERION`; its sign is not proved.
- PR #368: trace-class pole-null completion, index shift, Levy-prime structure, and relative heat criterion are usable with wording/domain fixes. The universal heat-sign theorem is open, and the headline theorem file is corrupted.

None of these local claims is covered automatically by the upstream Lean repository.

### D4. Q4 transfer only

PR #357's `L-90301.6-.7` accurately imports the abstract idea that adverse spectral mass controls trace/determinant curvature. This is a local algebraic transfer, not upstream formalization and not a review of the Q4 composition. `L-90301.8` is false universally and must be repaired piecewise:

- if `lambda_+<=0`, `delta(K)=-tr K`;
- if `lambda_-<0<lambda_+`, use the radical expression;
- if `lambda_->=0`, `delta(K)=0`.

## Route-independence table

| Route | Independence from carry/Q4 | Terminal statement | Verdict |
|---|---|---|---|
| Raw Brownian/Dirichlet-Hermite | High | all-`N` minimum-phase/nonvanishing | live independent proposal; `UNPROVEN / GAP` |
| Symmetrized Brownian/Robin | High in conception | aggregate canonical system/Hermite-Biehler | one-fiber verified; easy closures refuted |
| Anthropic Zeta23 A-E | Yes | unconditional zero proportions below RH | `IMPORTED / UPSTREAM VERIFIED` |
| Xi-cardinal/Gaussian | High analytically | corrected Gaussian/prime arithmetic floor | infrastructure; endpoint RH-equivalent |
| Pole-null Fredholm/heat | High analytically | heat-trace nonpositivity for all positive parameters | criterion verified with fixes; sign open |
| Screw/carrier/localized operator | Partial | cofinal capture plus square-screw/current floor | finite infrastructure; endpoint RH-equivalent |
| Finite Robin/Nicolas/Li | Yes as searches | finite violation or cofinal inequality | finite semidecision only |
| Pick/Loewner/CvS | Mostly criterion/reformulation | cofinal completeness or strict negative matrix | finite exclusions; no witness |
| Multirate/alias/prime banks | Yes, but not presently an RH route | uniform growing-bank asymptotic | local exact identities; theorem open |
| Q4 inertia transfer | No | Q4 innovation/current gate | local transfer; adjacent formula false |

## Strongest non-carry results

1. Upstream Zeta23 A-E and pinned Lean formalization.
2. Raw Brownian all-`N` Dirichlet-average/Hermite structure and exact `N=2,3,4` half-plane stability.
3. Exact Brownian refutations of reflected-tail and positive-mixture closure.
4. Xi-cardinal/Gaussian finite competitors and terminal off-line-pair isolation.
5. Exact Schur classifier identifying the genuine corrected-kernel endpoint.
6. Pole-null trace-class completion, exact index-one pole shift, and heat criterion.
7. Exact finite Pick closures and replay of every floating negative candidate as positive.
8. Localized/Suzuki guardrails separating shifted real-zero results from unshifted Weil positivity.

## First open theorem for each live route

- **Raw Brownian:** cofinal/all-`N` half-plane nonvanishing of `E[Q_N^z]`.
- **Symmetrized Brownian:** construct the aggregate positive canonical system/Hermite-Biehler object.
- **Carrier/screw:** cofinal normalized capture with complete tails and all-scale sign.
- **Localized Schur:** complete capture plus the fully corrected kernel floor `epsilon_j->0`.
- **Xi-cardinal/Gaussian:** corrected arithmetic lower floor for the complete hierarchy.
- **Terminal Gaussian scalar:** unconditional nonnegativity of the Chebyshev-error/Gaussian liminf.
- **Pole-null heat:** `Theta_{a,c}(beta)<=0` for every `beta>0` without assuming RH.
- **Confluent clusters:** uniform growing cluster order with tails/floor closed.
- **Robin/Nicolas/Li:** a cofinal theorem or authenticated strict finite violation.
- **Pick/Loewner:** cofinal feature completeness or a strict certified Riemann-data negative matrix.
- **Short-window/growing-conductor Zeta23:** complete uniform trace/RvM/end-effect/conductor bookkeeping.
- **Multirate banks:** growing-bank theorem including non-diagonal alias terms.
- **Upstream beyond bandwidth one:** new unconditional off-diagonal prime-pair input.
- **Q4 transfer:** repair `L-90301.8`, then prove the Q4-specific innovation/current gate.

## Computation not rerun

No large Brownian zero scan, Nyström/Fredholm sweep, carrier replay, Lean build, interval campaign, Pick/Loewner search, or large prime-bank/matrix search was rerun. Retained source, exact proofs, manifests, hashes, certificates, and audit files were inspected. Small exact checks were used only where decisive.

## Integration recommendations

1. Import exact Brownian finite algebra/convergence and raw Dirichlet-Hermite results; mark the all-`N` theorem open.
2. Import the two Brownian refutations prominently; remove positive-mixture and reflected-tail closure language from live mechanisms.
3. Preserve exact Schur sign and label the corrected floor `RH-EQUIVALENT CRITERION`.
4. Preserve every finite certificate with its manifest and declared feature space; never promote finite positivity to global RH.
5. Use PR #361 as the Anthropic provenance front door and keep upstream/local namespaces separate.
6. Mark #358, #360, and #363-#368 local and unformalized except for independently reviewed finite identities.
7. Block corrupted `T-90502` until rewritten as clean UTF-8.
8. Block or patch `L-90301.8` before any Q4 reuse.
9. Do not transfer Zeta23 Lean status to short windows, growing conductors, aliasing, prime banks, Xi-cardinal capture, Fredholm/heat, or Q4.
10. Keep the explicit front-door statement: **RH remains unresolved at every reviewed SHA.**

## Frozen repository SHAs

### Brownian/direct-xi

- #296 `4a68887f9f713aea7f63444030379fb864766a2d`
- #318 `277bfb19e2e5deed50b5bbc133453b7147046360`
- #343 `fed85f2969a5ab9f09890cd89bd6b57ff2115320`

### Finite criteria

- #22 `749ecfd0d2af53fa6eb8fdb786b7ad0c218cd462`
- #24 `ae477857d036fc182adb8db4e34e846fde7931b3`
- #33 `eed9b53ec995dfca119048eae060aab630f6065b`
- #34 `eda7ba6e378851ebe7ec1441b6503ba365eb0e35`
- #38 `5c360c9202244051b27e2fc2a2b39bebe002e6d5`
- #48 `ac4e8e7b36a95dd0bb325bcaf69ab79a10e68b12`
- #52 `b19d2982d5cdc3c13eaa72a9064f7c994e0c6313`
- #53 `5ee7df986e6191e57df33b7e0f32a0e22e10497e`
- #67 `8f3cce40048c84f1bfd19e815491790a13e4247b`
- #68 `7b0942a83eede8b57d4f28b14a78d80edc295f2a`
- #71 `82934cf24ed575e9e554ba4e6c912a447aa1dd4e`
- #80 `724ba6621bcf864ffbf2f25680074198be618ea5`
- #125 `016ed393cd267bef8bbb4a4bf281179d95e8d7cb`
- #141 `e15c50341187b7c0e672594654ad9416b55c9ce7`
- #173 `7085396b3c7e033d50ac4c031c5acdbe9b7814a6`

### Weil/screw/carrier/operator

- #65 `7296bf55449a4b510e4823028744deb793516e14`
- #98 `2f012ebd4bd782f0ba93a6ecc4f98f62b262be20`
- #140 `5f4df90f890615bde7762278951a8adab7f0083d`
- #144 `dd42bda400982e395c4102a8f66d25e2bb940e26`
- #168 `2a3667399b4a16311e1875932f9361c6aa6c8d0d`
- #192 `6c1a3a73de6b020aabaf1dff6cda9b8c7129af3f`
- #199 `4158e0d3e7f91829a6c545308605ea8177023aa3`
- #204 `4b770cf245ca2253efb0db2b807f4eab37775333`
- #206 `ff659984de0ab0c397ebefad393bc585c9007bc2`
- #208 `8a573d0245411313326223d8afb792e95eeef073`
- #218 `5fade63daa279fe6003b66f3763ca3bf05fd912d`
- #337 `46a4a25ccefbd480d533b03ee5e41d9980f25248`

### Anthropic import and descendants

- #357 `a2843d31649822014219a13ec29c70e4a30932cc`
- #358 `6f675e6e49c5b1fee3b1c7fce92331d2bad16948`
- #359 `9ffcb8d3dbc6affd859ea8567a061b71dd0d1e8b`
- #360 `df53319d9b8d465b01678986f86261a8d6d16965`
- #361 `c13b8836f6c7f4e36f17ab1c4ebe41e4cf072f2e`
- #363 `01238699b9ea2844e674f56a965cde79559d770a`
- #364 `46caa771ad2ab7875c3ccd079d3ba327249fd9a4` (first reviewed `219330bd0441a284fd16ff728dd843a7ee4503ee`)
- #365 `902a4cfeb36392c07878591e4a8381e3f4c7b2db`
- #366 `3dd8184c4e34f3a7ecd2b64597c7737af2b59029`
- #367 `2a725fb71794dfca11e76c1af2a49e6b3ea8bc9c`
- #368 `0de8f97f37617c050534c242ee3761af15b87a97`

## External pins

- Anthropic paper SHA-256 `6792988e6cd0e17690621ce898abd5d534f98407741bc7cb14bbe7d07c77d72f`
- concise note SHA-256 `45e0330ad37965e5531fa1f4f11e5bebcae147a5237a3e5b3d029efa7ddf759d`
- Lean `3635e74826a4c1fcece7d1cd2b6fa75e43a00510`
- Mathlib `51e6992efd06126df61a496bebf8f49482a4e129`

## Explicit RH status

**No reviewed branch establishes RH or its negation.** The strongest complete theorem in scope is the imported Zeta23 zero-proportion theorem, which intentionally remains below RH. Every local complete-proof proposal ends at an open all-`N`, cofinal-capture, corrected-floor, terminal-scalar, or heat-sign theorem that is RH-bearing or RH-equivalent.
