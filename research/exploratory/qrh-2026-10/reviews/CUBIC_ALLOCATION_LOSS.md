# Is a loss of order M hidden in the common-support allocations at n = 3? (risk item 10 of the cubic fourth-moment sketch)

```text
Status: REVIEW (bounded, one reader; external and unreviewed manuscript) + EXACT exponent ledgers
  and exact linear programs. Verdict (a): no hidden loss at n = 3. Every allocation inequality of
  the two common-support transforms, re-instantiated at n = 3, holds with minimum slack exactly 0.
  The minimum is attained at the same kind of zero-slack points as at n = 6, and no inequality is
  negative. The cubic route stays PROPOSED and CONDITIONAL on (H-A) and (H-B). No moment bound is
  proved. RH is not addressed.
Scope: risk item 10 of proposed/CUBIC_FOURTH_MOMENT/SKETCH.md, i.e. hypothesis steps A2 (first
  Poisson transform with complete common support, paper.tex l. 13114-13409) and A4 (second
  transform: diagonal, complete extraction, Moebius t-allocation, child normalisation,
  l. 13596-14310), in case 1 (z = 0) of Lemma 18.1, transferred from n = 6 to n = 3. Also covered
  are the places where A2/A4 outputs are consumed: the Gauss-row zero (l. 13572-13594) and the
  Theta-row ledger (l. 14312-14530). Not re-reviewed: the centred lattice step (item 9; see
  CUBIC_CENTRED_ATTACK, CUBIC_BOTH_RECTANGLES), the nested order (H-B), and Lemmas 4.5/4.7.
Exact sources or dependencies:
  repo HEAD aa323ea9e6f1efee14365b1d7db4d64fc902e6b3 (working branch).
  pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6:standalone/2026-10-07-openai-quasi-riemann-
    import/upstream/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex,
    sha256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 (re-extracted and
    re-hashed for this note; 16,677 lines; read as untrusted TeX). Read: l. 13110-13460,
    13560-14545. Grepped l. 13114-14540 for every order-dependent constant (Sec. 1.3).
  Read in full: reviews/LEMMA18_1_COMMON_SUPPORT.md, CUBIC_N3_GAPS.md,
    CUBIC_FOURTH_MOMENT_TRANSFER.md, reviews/CUBIC_CENTRED_ATTACK.md,
    proposed/CUBIC_FOURTH_MOMENT/{README,SKETCH}.md. Read in part: reviews/CUBIC_BOTH_RECTANGLES.md
    (header, Secs. 0-2), reviews/CUBIC_PROFILE_UNIFORMITY.md (as summarised in the README).
  Logic copied and parametrised by n (files unchanged): reviews/lemma18_support_checks.py
    (A1 bijection, A4 Moebius, A5 t-allocation, L1-L3), reviews/lemma18_ledger.py ((2.6), (2.12),
    (2.13), (2.15)-(2.16)).
  New: reviews/cubic_allocation_loss.py, sha256 d4c6359ffce97c90...6f381fca0817fd.
What was actually run (one process, nice -n 10, about 9 s):
  python3 -I reviews/cubic_allocation_loss.py -> 56/56 PASS, of which 11 are failing controls
    (all detected). Log sha256 b19e2fb9...debb83c32 (session scratchpad, alloc_run2.log).
  Run 1 gave 53/55. Its two FAIL lines were controls whose expected value I had hard-coded wrongly;
    Sec. 5.2 gives the details and every change between the runs.
  Arithmetic: EXACT (Python fractions, sympy, integer cyclotomic vectors). The linear programs are
    solved by an exact two-phase simplex in fractions. One scipy (float64) cross-check is printed
    and labelled FLOAT; no PASS criterion uses it.
Smallest remaining gap: the exact ledgers show that the displayed allocation steps lose nothing
  at n = 3. They cannot show that the displayed ledgers describe the analysis. The order-free
  allocation costs (divisor-bounded label counts, Rankin, O(log Z) dyads, the one Fourier measure
  that separates kernels and inverse roots) are inherited at n = 3 from the n = 6 line check
  without change. They were not re-read line by line here. The Fourier-measure L^1 bound
  (Lemma kernel-seminorms) remains imported.
```

RH is unsolved. This note does not prove or disprove RH, Lemma 18.1 or any moment bound. "No
hidden loss" means: every displayed allocation inequality, with 6 replaced by 3 where the order
enters, holds exactly. Its worst case over all allocations is computed exactly and is 0, not
negative. It does not mean the manuscript's analysis is correct.

## 0. Verdict

**(a) No hidden loss at n = 3.** The minimum slack over the allocation polytope is **exactly 0**
for every allocation inequality. This was checked by exhaustive local enumeration and by exact LPs
over the full cone of mixed local types. No inequality that is tight at n = 6 becomes negative at
n = 3. The losses that do occur are terminal, of size `O(σ + ξ)`, and do not grow with `L` or `M`
([D4]). Compared with the tolerance: allocation loss `0 < c*(δ)·M` for every `δ < 11/147`.

The finding is sharper than "a loss below tolerance". The allocations have **zero slack and zero
loss**. They contribute no margin either: all of the route's margin `μ*(δ)` comes from the closing
optimisation (SKETCH §3.5), none from the allocations. The zero-slack points at n = 3 are:

* first-transform primes of type `(1,1)` and `(2,1)` (budget (2.6));
* `F_1 = 5c/6` on the whole region `3c ≥ 4d + 2R`;
* second-transform nonunit `i = 1, 2` and equal `i = 3`;
* the Gauss-row zero with the manuscript's crude count, which has slack identically 0 at n = 3.

**A correction to the register's tolerance model.** The register attaches the tolerance `c*(δ)` to
item 10. That tolerance (denominator 432) applies only to an additive loss confined to the
**centred** Theta-row deficit. Allocation losses are of two other kinds (Sec. 4):

* **Losses in the order-free ledgers.** These are the first-transform closure, the diagonal, the
  child allowance, and the t-volume. All stages use them, including the application point
  `A = M`, `q = 0`. Each has minimum slack 0, so **any** loss `cM` with `c > 0` there is fatal, at
  n = 3 exactly as at n = 6.
* **Losses in `F_1`/`F_2`.** These scale with the extracted length `v`. Two stages tolerate them
  iff the effective coefficient stays at or above `κ_crit(δ)`:
  * `κ_crit(0) = 3 − √5 ≈ 0.7639`, i.e. a loss of up to `≈ 0.069` per unit of `v`;
  * `κ_crit(1/100) ≈ 0.7740`, i.e. up to `≈ 0.059` per unit of `v`.

**Register update line** (proposed; SKETCH.md is not edited by this note):

| # | step | status | evidence | most likely failure mode |
|---|---|---|---|---|
| 10 | A2, A4: common-support transforms and extraction | **imported; re-instantiated at n = 3, no loss** (min slack exactly 0; bounded review) | COMMON_SUPPORT 24/24 (n = 6); CUBIC_ALLOCATION_LOSS 56/56 (exact LPs, 11 controls) | an undisplayed allocation cost that is not `Z^{o(1)}`: in an order-free ledger it is fatal for any `c > 0`; in `F_1`/`F_2` it is fatal once the coefficient of `v` drops below `κ_crit(δ)` (`3 − √5` at `δ = 0`) |

## 1. The two allocations, restated

Units: `log Z`. `A = n_1 + n_2`, `M = m + q`, `θ = 1/n`. Case 1: `z = 0`, so `w = w_o = ℓ = 0` and
`g = J_+ + σ`.

### 1.1 First transform (A2; l. 13192-13409)

**What is allocated.** The two full index products are written `Ca`, `Db`. Here `C, D` carry the
complete common support (`rad C = rad D`), and `(a,b) = 1`, `(ab, CD) = 1`.

* Each common prime with multiplicities `(i, j)` has its valuation fixed in each plain and slot.
* The prime then punctures every residual factor.
* The **conductor split** is:
  * `𝔯` = the primes with `n ∤ i − j`;
  * the Möbius mask `𝔢 | 𝔠/𝔯`;
  * logs `R ≤ p` and `E ≤ p − R`.
* The Möbius label `s` removes `(a,b) = 1`.
* One Fourier measure, fixed before the live labels, separates the kernel and inverse roots. It
  gives **one norm power `q_a^{it}` per whole column**.

| quantity | value | n-dependent? |
|---|---|---|
| outside factor (Poisson, `|τ(ξ_𝔯)| = q_𝔯^{1/2}`) | `m − A − R/2 − E` | only through which primes are in `𝔯` |
| label count | `p + s_0 + ε_1` | no |
| moving support, frequency scale | `q̃ = q + R + E`, `K_0 = 2A − c − d + R + E − m` | through `R` |
| norm target (2.5) | `N_C ≪ Z^{A − c + q̃ + B_c − s_0}` | through `B_c` |
| closure (ledger, l. 13384) | `M + ½(B_c + B_d − (c + d − 2p − R))` | no ([A1], sympy) |
| budget (2.6) | `B_c + B_d ≤ c + d − 2p − R` | yes: `r = 1_{n∤i−j}`, and `B_c` |
| allowance | n = 6: `((3c − 5d − R)/6)_+`; n = 3: `((3c − 4d − 2R)/6)_+` | yes |
| zero frequency | exponents `≡ 0 (mod n)` ⇒ powerful product; exponent `m − M = −q ≤ 0` | no ([A9]) |
| Gauss-row zero (via `s`) | `G(u,0) = 0` unless `u` is an n-th power; count `Y^{1/n}`; `s_0 ≤ (a_0 + θ_N)/n` | yes ([G1]-[G3]) |

### 1.2 Second transform (A4; l. 13596-14310)

**What is allocated.**

* `u = D_2 a`, `v = E_2 b` with complete common support. The aggregate parameters are
  `c_2, d_2, b_2 = (c_2 + d_2)/2`, `p_2`, `g_2 = log q_{(D_2,E_2)}`, `t_2` (unit primes),
  `V` (nonunit primes) and `f`.
* The **t-allocation**: a squarefree Möbius `𝔱` removes `(a,b) = 1`. Each `p | 𝔱` is allocated by
  inclusion-exclusion to a plain, which divides both rectangles' scales by `q_p`.
* **Child normalisation**: `e_j, ω_j, r̃_j, t_-`.

| quantity | value | n-dependent? |
|---|---|---|
| local absolute table | `|F| ≤ P^{g_2 − t_2}`, with `n | i` and `n | j_0` cases | yes ([S1]; brute force in CUBIC_N3_GAPS [F1], [T1]) |
| moving support | `q' = q̃ + w_o + t_2 + V`, active primes `e_p = v_p(G_cV_id) mod n ≠ 0` | yes ([S2]) |
| width (2.13) | `M' = M + J − g − g_2 + t_2 ≤ M − σ` | no ([S3]) |
| diagonal (2.12) | excess `≤ A − M + σ + δ_fr,1`; uses only `B_c ≥ 0` | no ([S5]) |
| child allowance (2.14) | `M' + Δ_child`, `Δ_child = b_2 − p_2 + B_c ≥ 0` | no ([S4]) |
| t-allocation, (2.18h), clipped shell | `t_- − r̃_1 − r̃_2 − (r − r̃_1)_+ ≤ ω_2 − r`; total `≤ 2θ_N` | no ([S6]-[S8]) |
| exceptional count | `Z^{(m' − f)/n}`; nonunit `i = 1` forced valuation `−2 mod n` (4 for n = 6, 1 for n = 3) | yes: `f = 2v_1` (n = 6), `f = v_1` (n = 3) ([S11]) |
| Theta-row identity | `A − (1−θ)M − F_1 − F_2` with `F_1, F_2` at `θ = 1/n` | yes (CUBIC_N3_GAPS [L1]) |

### 1.3 Every order-dependent constant in l. 13114-14540 (fresh grep)

* l. 13182: zero frequency "modulo six".
* l. 13212: the `𝔯`-rule "nonzero modulo six".
* l. 13379-13406: `B_c`, `B_d` and the proof of (2.6).
* l. 13576-13582: the Gauss-row zero (sixth powers, `Y^{1/6}`, `q_s^6`).
* l. 13706-13749 and 13768-13780: local rules and table, `e_p mod 6`.
* l. 14341-14379: fixed-ray valuations mod six, the residue `4 mod 6`, `𝔥_0𝔳^6`, the count.
* l. 14437-14523: (2.15)-(2.17).
* l. 13457-13552 and 14196-14271 (`p^6` amplifier, `6κ − 1`, `ℓ_p ≥ σ/6`): positive slots only,
  not used when `z = 0`.

This agrees with the catalogue in CUBIC_N3_GAPS §3.1. There are no others. In particular:

* the Poisson normalisation, the Rankin and divisor counts, the Fourier separation and the
  t-allocation contain no n;
* the Gauss-sum modulus `|τ| = q^{1/2}` for a primitive character holds for every order.

## 2. The n = 3 instance: worst-case slack over the allocation polytope

Method:

* An allocation is a nonnegative mixture of local prime types.
* First transform: per unit log-norm, a type `(i, j)` contributes `(c, d, p, R) = (i, j, 1, 1_{n∤i−j})`.
* Second transform, per unit log-norm:
  * equal `i`, unit;
  * equal `i`, nonunit (with the forced `f`);
  * equal `n | i`;
  * unequal `i > j_0`, `n | j_0`, in both orientations.
* Global variables: `q`, `E ≤ p − R`, `D_k = K_0 − K ≥ −δ_fr,1`.
* The positive parts `B_c` and `(L − v)_+` are handled by epigraph variables. The branch
  `J ≥ 0` / `J < 0` is handled by two LPs.
* Every LP was solved exactly.

| inequality (where) | n = 3 worst slack | attained at | n = 6 | check |
|---|---|---|---|---|
| (2.6) budget, per unit `c + d` | **0** | local `(1,1)`, `(2,1)`, `(1,2)` | 0, same types | [A2] all `i,j ≤ 120`; [A3] exact LP over mixtures |
| `F_1 ≥ κ_1 c` | `κ_1 = 5/6` (exact global min) | any allocation with `3c ≥ 4d + 2R`, e.g. `(2,1)` or `(12,9)` | `2/3` | [A4], [A4b]: `F_1 − 5c/6 = (2d/3 + R/3 − c/2)_+` identically |
| `F_2 ≥ κ_2 b_2` | `κ_2 = 1` | nonunit `i = 1, 2`; equal `i = 3` | `2/3` at nonunit `i = 1` | [S9]; [S10] LP: `min[F_2 − min(c_2,d_2)] = 0` |
| centred deficit `A − 2M/3 − F_1 − F_2 − (L−v)_+ ≤ A − 2M/3 − (5/6)L` | **0**, for `L = 1/4, 43/102, 1/2` | `v = L`, first-transform `(2,1)` primes only | 0 at `κ = 2/3`, `L = M/4` (paper (2.19)) | [D1], [D2]; [D3]: target `5/6 + 1/100` gives `−L/100` (no hidden spare) |
| same, with `σ = 1/100`, `δ_fr,1 = 1/200` | `−(2/3)(σ + δ_fr,1) = −1/100` for every `L` | | | [D4]: terminal, independent of `L` and `M` |
| Gauss-row zero (crude count) | slack `(1 − 3/n)(a_0 + θ_N)` = **0 identically** | every `a_0` | `(a_0 + θ_N)/2 ≥ 0` | [G1], [G2] |
| Gauss-row zero (refined count `Y^{1/3}/q_s`) | `a_0/3 + s_0 + θ_N/3 ≥ 0` | | | [G3] |
| outside factor `−R/2` | exact: `|τ(χ^e)|² = P` for `e = 1, 2` | | | [A5] at `P = 7, 13`, exact in `Z[ζ_{3P}]` |
| zero frequency, diagonal, (2.13), (2.14) | slack ≥ 0, min 0; no n | | identical | [A9], [S3]-[S5] |

**No constraint that held with equality at n = 6 fails at n = 3.** Here is what happens to each
n = 6 equality case:

* **(2.6) at `(1,1)` and `(2,1)`.** Still exactly 0 at n = 3 with the cubic allowance.
* **`F_1 = 2c/3` (n = 6).** Replaced by `F_1 = 5c/6`. This is not a loss against n = 6: it is the
  coefficient the cubic closing condition (C) already assumes. Against the `κ = 1` that the
  single-window cubic transfer would need, it is a known shortfall, already priced into (C).
* **`F_2 = 2b_2/3` at nonunit `i = 1` (n = 6).** Becomes `F_2 = b_2`, now at three local types.
  The sextic spare `f/6` (COMMON_SUPPORT §3) is gone, because the forced valuation is 1 rather
  than 4 ([S11]).
* **(2.19) at `v = L`.** It becomes the cubic (C) at `v = L`, with value 0.
* **The Gauss-row zero.** It has slack `(a_0 + θ_N)/2` at n = 6 and slack identically 0 at n = 3.
  That is still not negative. n = 3 is exactly the boundary order for the manuscript's crude
  count; n = 2 would fail ([G1-CTRL]). The refined count restores positive slack.

## 3. The extraction steps (A4)

* **Möbius extension (`s` and `𝔱`).** These are exact identities ([A8], [S6], copied from the
  n = 6 checks). The `s`-label nets to zero in the first ledger ([A6]). It is realised later as
  `p_2 − s_0` radicals, `Y/q_s` diagonal moduli, and `s³ | u` in the Gauss-row zero, which at n = 3
  replaces `s⁶ | u` ([G3]).
* **Common extraction.**
  * The decomposition is a bijection, independent of the order ([A7]). At n = 3 there are fewer
    `𝔯`-primes and more `𝔢`-mask primes (172,872 against 216,090 incidences on the test lattice).
    This costs nothing, because `E` enters every ledger favourably.
  * The local table `|F| ≤ P^{g_2 − t_2}` with `g_2 − t_2 ≤ min(c_2, d_2)` holds for all
    `i, j_0 ≤ 30` ([S1]).
  * Every active moving prime is in the unit set or the nonunit set ([S2]). So `q'` is unchanged
    in form.
* **Child polynomials.**
  * The width identity and `M' ≤ M − σ` hold ([S3]); so does the child allowance
    `Δ_child ≥ 0` ([S4]).
  * The exact LP over child normalisations gives `max(e_1 + e_2 + t_- − r̃_1 − r̃_2) = 2θ_N`
    exactly ([S7]). This is the exceptional volume bound `a_0 − b_2 + 2θ_N`.
  * The t-count never exceeds `ω_2 − r` ([S8]), so the lattice saving `r = (L − v)_+` survives
    the allocation.
  * None of these contains n.

## 4. Tolerances, recomputed (SKETCH §3.5)

Take `M = 1`. The two-stage closing constraints are (C) `κL ≥ A − 2/3 + c_C + μ`,
(R) `1 − A + 2L ≤ b_{j−1} − μ`, and the caps `L ≤ A/2`, `L ≤ A − 1/2 − μ`. Here `lo(A)` is a
maximum of affine maps and `hi(A)` a minimum of affine maps. So each stage's ceiling is an exact
crossing point, and the endpoint tests are exact.

| loss model | applies to | tolerance, `δ = 0` | `δ = 1/100` | check |
|---|---|---|---|---|
| margin `μ` in every constraint | uniform demand | `μ* = 11/612 ≈ 0.01797` | `953/61200 ≈ 0.01557` | [P1] |
| additive loss in the **centred** deficit only | the register's `c*` | `11/432 ≈ 0.02546` | `953/43200 ≈ 0.02206` | [P2] |
| additive loss in the Theta-row deficit, uncentred stage included (U ceiling `2/3 − c`) | | `11/507 ≈ 0.02170` | `953/50700 ≈ 0.01880` | [P3] |
| loss proportional to `v`: `F_1 + F_2 ≥ κv` | **an allocation loss in `F_1`/`F_2`** | `κ ≥ 3 − √5 ≈ 0.7639`, i.e. `5/6 − κ ≤ 0.0694` | `κ ≥ (306 − 160√2)/103 ≈ 0.7740`, i.e. `≤ 0.0593` | [P4] |
| any nested version | | `κ > 2/3`; (C)-only additive `< 1/12` | | [P5] |
| loss in an order-free ledger ((2.6) closure, diagonal, (2.14), t-volume) | used by every stage, including `A = M`, `q = 0` | **0** | **0** | Sec. 2: min slack 0 |

`c*(δ) = (11 − 147δ)/432` is reproduced exactly from SKETCH §3.5, as is
`μ*(δ) = (11 − 147δ)/612`. The `/432` form applies when the loss sits only in (C). The binding
point at `v = L` uses no lattice saving (CUBIC_CENTRED_ATTACK §0). There the whole deficit
reduces to `F_1 + F_2 ≥ (5/6)v`, which is an allocation output. So an allocation loss would act
through `κ` and not as an additive `c_C`. That is why the `κ` row is the relevant tolerance for
item 10.

## 5. Failing controls

### 5.1 The eleven controls (all detected in run 2)

| control | what was plugged in | effect | verdict it would give |
|---|---|---|---|
| [A2-CTRL] | allowance `((3c − 3d − 2R)/6)_+`, which would buy `κ_1 = 1` | (2.6) fails at `(2,1)` by `1/6 · log q_p`: a ledger excess of `c/24`, a positive multiple of `M` in an order-free ledger | (c) |
| [A4-CTRL] | the **sextic** allowance at n = 3 | `min F_1/c = 11/15 < 5/6` (mixture `(1,1) + (12,6)`, or a single `(15,9)`, with `3c = 5d`, `R = 0`) | — |
| [A5-CTRL] ×2 | the sextic `𝔯`-rule at a cubic `(4,1)` prime (`6 ∤ 3` but `3 | 3`) | `ξ_𝔯 = χ³` is trivial; normalised `|G|² = (P−1)²/P` (36/7, 144/13) `> 1`, so `|G_ξ| ≤ 1` fails by about `P^{1/2}` and the outside factor loses `R'/2` | (c) |
| [G1-CTRL] | n = 2 in the crude Gauss-row count | slack `−(a_0 + θ_N)/2` | (c) for n = 2 |
| [G4-CTRL] | the sextic count `Y^{1/6}` for cube moduli | exact counts: 61 cubes against 10 at `Y = 10⁶`; 6,049 against 100 at `10¹²`; 604,593 against 1,000 at `10¹⁸`. This illustrates the known `cY^{1/3}`; it is not a trend fit | false claim detected |
| [S9-CTRL] | no nonunit forcing (`f = 0`) | `min F_2/b_2 = 2/3` | (c), see [D6] |
| [S11-CTRL] | the sextic `f = 2v_1` at n = 3 | the forced valuation at nonunit `i = 1` is 1 (mod 3), not 4 (mod 6); `f = v_1` only | over-claim detected |
| [D5-CTRL] | the sextic allowance at n = 3, in the joint LP | min slack `−L/10`, a loss of `0.0422M` at `L = 43/102`; `κ = 11/15 < κ_crit`, and two stages fail | (c) |
| [D6-CTRL] | `f = 0`, in the joint LP | min slack `−L/6`, i.e. `0.0703M`; `κ = 2/3`, and no nested version closes | (c) |
| [D7-CTRL] | sextic `θ = 1/6` data against the cubic target `5/6` | min slack `−L/6` | (c) |

### 5.2 Run 1 versus run 2, and a finding about the sextic-allowance control

**What run 1 asserted.**

* Run 1 gave 53/55. Its two FAIL lines were [A4-CTRL] and [D5-CTRL].
* Both controls detected the wrong input. But I had asserted the exact values `19/24` and `−L/24`.
* I took `19/24` from the per-prime figure in CUBIC_N3_GAPS [A3-CTRL]: "the sextic allowance gives
  `F_1/c = 19/24` at a cubic `(4,1)` prime". That statement is correct for a single `(4,1)` prime.

**Why the global value is lower.** `B_c` is the positive part of a **global** sum. The exact LP
finds a mixture with `3c = 5d` and `R = 0`, where `B_c = 0` and `F_1 = c/3 + 2c/5 = 11c/15`.
[A4c] confirms this exactly at the single types `(15,9)` and `(30,18)`.

**What changed for run 2.** Two control criteria became "detected" (`< 5/6` and `< 0`), and the
exact values are now printed. Two edits do not touch any PASS criterion:

* In [S7], a redundant lower bound `e + w ≥ −1` was mis-signed (`≤ 1`). It is inert for the
  maximum, and the value 2 is unchanged.
* The label of the float cross-check was corrected.

No PASS criterion of a non-control check was changed.

**What the finding means.**

* For the route: none. The cubic allowance's `κ_1 = 5/6` is a global identity, `F_1 − 5c/6 =
  (2d/3 + R/3 − c/2)_+` ([A4b]), and the LP over mixtures confirms it ([A4]).
* For the control: with the sextic allowance, the cubic route would be **broken** (`κ = 11/15 <
  3 − √5`). It would not merely lose `L/24` below tolerance, as the per-prime figure suggests.
* For the method: per-prime minima of `F_1` are not global minima, because `B_c` does not
  separate over primes. `F_2` and the (2.6) slack do separate. `F_2` is additive, and the slack is
  concave, so its minimum is at a single type ([A3]).

## 6. What this does not show

* That the displayed ledgers describe the analysis. This note checks the displayed allocation
  inequalities, not the estimates behind them.
* The size of the separating Fourier measure (Lemma kernel-seminorms). It is imported, and it is
  order-free.
* The cubic finite lemmas 4.B-4.D and 4.G beyond small moduli. [S1] uses their closed forms; the
  brute-force evidence is CUBIC_N3_GAPS [F1], [T1], [C1], [E].
* Items 8, 9, 11 and 12 of the register. Lemma 18.1 itself (item 12) has had no human check.

## 7. Files

* `reviews/cubic_allocation_loss.py` (new). Sections [P], [A], [G], [S], [D]: 56 checks, 11 of
  them failing controls. EXACT arithmetic. Run with
  `nice -n 10 python3 -I reviews/cubic_allocation_loss.py` (about 9 s).
* The run logs (`alloc_run1.log`, `alloc_run2.log`) are kept in the session scratchpad. The script
  is the reproducible artifact.
