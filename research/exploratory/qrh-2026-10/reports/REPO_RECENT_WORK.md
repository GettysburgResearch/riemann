# Recent repository work relevant to the QRH wave (digest, 2026-10-10)

```text
Status: SURVEY (no new mathematics)
Scope: repository activity since the 2026-09-06 integration baseline
Exact sources or dependencies: origin/main f99d9e390 (last merge PR 824, 2026-09-08);
  PR 910 @670a76c1, PR 909 @7838b535, PR 908 @31c706bb, PR 907 @aa725eeb, PR 906 @ddc25eaf,
  PR 905 @0f82df3b, PR 904 @8c506696, PR 903 @72ad9bc0, PR 901, PR 888 @1ce38f1f, PR 891 @d5d55b79,
  PR 788 @a9c7b44f (descriptions); issue 902 (strategy review), issues 736/738 (latest comments);
  branches without PRs: claude/openai-math-riemann-analysis-w5copg @bd670c92d,
  claude/openai-math-riemann-analysis-lc2b3j @a3ec04b6f, claude/friendly-allen-cl0dew @409760c01;
  this wave's untracked files (CONDITIONAL_CONSEQUENCES.md, results/*.json, scripts/barrier_lp.py)
What was actually run: git fetch; git log/for-each-ref/diff --stat/show on the refs above;
  GitHub MCP list_pull_requests (open+closed, by update), pull_request_read, list_issues;
  gh api REST for PR bodies and issue comments. No checker was executed; nothing was reviewed for correctness.
Smallest remaining gap: n/a
```

RH remains unproved. Nothing below is integrated. Every research item since 2026-09-06 is an **open draft PR or a bare branch**. Main has received only documentation merges since then (PRs 806–824).

## 0. Bottom line for the wave

1. **The QRH manuscripts were already imported and analysed before this wave started**, in three stacked PRs and two Claude branches (Section 1). The wave's `INTAKE.md`, `ledger_check.py`, `threshold_calculus.py`/`barrier_lp.py` and `CONDITIONAL_CONSEQUENCES.md` substantially overlap with them. Read [PR 910](https://github.com/GettysburgResearch/riemann/pull/910) first.
2. [PR 910](https://github.com/GettysburgResearch/riemann/pull/910) already claims the conditional refinement `Re s > 139999/160000` (that is, `7/8 − 1/160000`). It also gives an **exact** limit for the unchanged envelope, `(1507−2√921)/1653 ≈ 0.874957067`. The wave's numerical optimum (`0.8749602`, `results/B_paper_bp7_8.json`) agrees with that limit. **Further tuning of the fixed geometry is exhausted.**
3. Three independent write-ups name the same missing structural input: a **joint (common-frequency) inverse/plain moment**, ratios-type or beyond Cauchy–Schwarz. These are [PR 908](https://github.com/GettysburgResearch/riemann/pull/908) RESEARCH_PLAN §7, [PR 910](https://github.com/GettysburgResearch/riemann/pull/910) UPSTREAM_HEIGHT §6.3, and branch w5copg §6. The proposed higher-moment route (fourth moment ⇒ `17/24`) is the second named lever.
4. No repository work assesses the Kintali `47/48` manuscript. That gap belongs to this wave alone.
5. Issue [902](https://github.com/GettysburgResearch/riemann/issues/902) is the owner-endorsed strategy. It rejects small numerical increments as flagship goals. It prefers source-specific estimates and decisive falsifications. A `1/160000` gain falls under the same critique.

## 1. QRH-specific work already on the repository

| Item | Date / status | Exact claim (one or two sentences) | Smallest named gap | Links (a–d) |
|---|---|---|---|---|
| [PR 908](https://github.com/GettysburgResearch/riemann/pull/908) `import/openai-quasi-rh-20261007` | 10-07, draft; IMPORTED + selective audit + CONDITIONAL | Imports openai/math@adc7f124 family 003 byte-exactly: 3,286 files, the 7/8 (Sep 30), 11/12 (Oct 5) and Landau–Siegel (Oct 1) papers, and the 3,232-module Lean closure. Conditionally on 7/8, it shows `F_X,E_X ≪ X^{3/4+ε}`. The full MHB32 map `κ ↦ (191+82κ)/273` sends 3/4 to `505/546`, which is worse, so there is **no bootstrap**. CAP36 then gives completion width `J ≪ Y^{7/8+ε}` and a difference bound `O(τ²Y^{5/4+ε})`. | Fresh Lean/Comparator build; native coarse covariance `S_Y ≤ C(log)^A(1+F_Y)^{2−δ}` | (a) Gauss/theta walkthrough, `lem:second-transfer` signed allocation `(1+1_{p∣k'})−1_{p∣k'}−1_{p∤k'}=1_{p∣k'}`; (b) Mertens/energy seeds; (c) 7/8 import |
| [PR 909](https://github.com/GettysburgResearch/riemann/pull/909) `import/openai-riemann-companions-20261009` | 10-09, ready (stacked on 908); IMPORTED + PROPOSED | Adds 22 companion manuscripts (families 007, 011, 012, 014, 021, 023, 026, 029, 142, 182). Proves the exact bridge `μ = β*χ_{−3}` with `β(n)=Σ_{N𝔞=n} μ_K(𝔞)`, completed Gram and NRC32 block means in ideal coordinates, and `F_X ≤ 𝒜_X ≤ 2F_X`. Family **029** claims Hecke zero-freeness in `Re s > 1−10⁻⁶` over cyclotomic fields ⊇ μ₁₂. | OAI-RP26-T1: `S_Y ≤ C(log 2Y)^A Y^a (1+F_Y)^p` with `a < ¾(2−p)`; a finite common-kernel transformation identity for the native `T_I` kernels | (a) family 023 cubic-character Gram `Σ_{p'≠p}|T_{p,p'}|² ≪ Z(P+(P³/Z)^{2/3})`; family 007 Liouville two-point; (c) family 029 |
| [PR 910](https://github.com/GettysburgResearch/riemann/pull/910) `research/quasi-rh-height-descent-20261010` | 10-10, draft; PROPOSED, with one AI-agent scoped review | (i) **Conditional on the listed imported inputs**: zero-free for `Re s > 139999/160000`. Uses `ℓ=1/6+1/40000`, a corrected row loss `f_ℓ(d)=−d+(5ℓ−1+d)_+/8 ≤ 0`, the margin `49/440640−1/16000=1073/22032000`, and an enlarged principal Euler domain `Re s ≥ 437/500`. (ii) Exact limit of the specified envelope at `0.874957067`. (iii) Diagonal-size `2k`-th moments of `A_u(D;W)` at `H=D^{1+θ}` would give `1/2+5(1+θ)/(12k)` (Prop. 7.2, exact prime-removal recursion). (iv) The fourth moment reduces to a squarefree balanced-divisor mean square (3.5). (v) Marginal Hölder interpolation of the inverse 2nd and plain 4th moments **cannot** beat `max(r,2m)` (§6.2, with an extremal example). | Audit of the geometric adapters; prove (3.5); a joint moment (6.6) `Σ_u |M_u S_u(t_u)|² ≪ U^{1+ε}` at rowwise heights; the native pointwise off-diagonal `𝒪_Y < 1/(12Ω)` | (a) sextic family moments, `H_η` factor `L_K^S(6s−3, ᾱ⁶η⁶)`, an angular Hecke character of infinite order; (b) native Möbius detector `R_Y=G_YB_Y−1`; (c) 139999/160000; (d) completed mean square with conductor cost `(1+|t|)⁴` (Prop. 4.4); tail supremum `B(T)` (Lemma 5.1); band target (8.1); shrinking-strip diagonal along `1/2+c·loglogY/logY`, c>2 |
| branch `claude/openai-math-riemann-analysis-w5copg` (no PR) | 10-07; IMPORTED + EMPIRICAL + PROPOSED | Leverage law: with a square-root mean square and principal-copy density `H^{−c}`, the family is zero-free for `Re s > (1+c)/2`, so sixth powers give 11/12. Exponent model: the boundary `σ₀ = 1 − h/6 + b/12` is set by the low side. The method's own optimum is ≈0.87497. Density-hypothesis counts give ≈`13/15`. Reaching `3/4` needs `h = 3/2` (ratios-type cross-row cancellation). Numerics: every `lem:arithmetic` identity holds for all 14,120 squarefree n with `N(n) ≤ 5·10⁴`. The mean square equals its diagonal within 4% for D ≤ 102,400. | Lean comparator run; a theorem-sized review of the 11/12 paper | (a) Gauss-identity replay, sextic mean square; (b) conditional `3/8` negative-mass exponent for fixed detectors |
| branch `claude/openai-math-riemann-analysis-lc2b3j` (no PR) | 10-07; EMPIRICAL | Lean source audit: no `sorry`/axiom/`native_decide` in the 3,232-file closure. The four challenge statements compile. The 7/8 closure (2,925 files) was **not built** (since built in this wave: reviews/LEAN_BUILD_ATTEMPT.md). | `lake build` plus four comparator runs | — |

The wave's own `CONDITIONAL_CONSEQUENCES.md` (μ(σ) interpolation, ψ and M(x) bounds) largely restates w5copg §5 and PR 908 `CONDITIONAL_BRIDGES.md`. Cite those rather than issuing new claim IDs for the same deductions.

## 2. Pre-QRH research (2026-09-09 → 09-25): native signed-energy programme

Issue [902](https://github.com/GettysburgResearch/riemann/issues/902) (09-19) makes the **balanced Newton energy** the primary attack. The reconstruction `μ − N(c) = μ*e*e` is exact below `(Y+1)²`. The target is `1+A_B ≤ C(1+A_Y)^p` with `p<2` ([PR 848](https://github.com/GettysburgResearch/riemann/pull/848)). The odd-source trace TC26 is a complementary diagnostic. The issue also withdraws priority from the 0.67 simple-zero increments ([PR 888](https://github.com/GettysburgResearch/riemann/pull/888) and siblings 887, 889, 890, 893–895).

| PR | Date / status | Claim | Smallest gap | Links |
|---|---|---|---|---|
| [904](https://github.com/GettysburgResearch/riemann/pull/904) MHB32 / ATC29 / NCL29 / MCB31 | 09-19→21, draft PROPOSED | Exact Mellin–Hankel adapter for the microscopic rational-angle band. Bounded future-activation tail with an extra power saving. Pure prime-power denominators controlled. | The high-composite full sum; the generic input exponent is still quadratic | (b), and the 505/546 map in PR 908 |
| [905](https://github.com/GettysburgResearch/riemann/pull/905) ACC29–NRC32 | 09-19→21, draft PROPOSED | Squarefree completion `J(c) ≤ 33F_Y` without future signs. The completed `c*c` is cubefree. NRC32 identity `F_{(Y+1)²−1} = F_Y + S_Y + D_Y`, `0 ≤ D_Y < 5/6`. | Upper bound for the coarse `S_Y` | This is the exact native target the QRH bridge aims at |
| [906](https://github.com/GettysburgResearch/riemann/pull/906) CQT32 | 09-21, draft | Energy is exactly quadratic in completion variables. A semiprime closed packet has energy `∼C_*Y²/(log Y)⁴` (not a counterexample). Rectangular bound `Σ|U_cd|² ≤ 2²¹H⁴E_cE_d`. | Complete native covariance | (b) |
| [907](https://github.com/GettysburgResearch/riemann/pull/907) RAB33…ADP37 | 09-25, draft | The anchored Fejér phase average `A_K ≤ 810 h_{16H}² (2h_L−1)` holds independently of `F_Y`. **Obstruction:** a non-native `|c| ≤ 1` source with the same kernel has principal energy `≥ 2⁻⁷²L²` and mean `O(log L)`. So generic mean-to-principal extraction is false. | A native concentration bound for `‖U₀‖²/D` | (a) principal-member extraction analogue; (d) phase/height τ up to `L²` |
| [903](https://github.com/GettysburgResearch/riemann/pull/903) SBC26/RSC26/DCN26 | 09-19→21, draft | Sylvester cutoff atoms. A native positive-sector obstruction. CM elliptic fixtures, including an exact `E_17` counterexample to a sign transfer (`a_7 = 5`). | Coarse family energy | (a) GL2/CM twist programme, issue 738 |
| [901](https://github.com/GettysburgResearch/riemann/pull/901) SRL | 09-18, draft | Vasyunin dual `d₆` gives a permanent `1/92` error floor for prime-power-only Nyman–Beurling approximants. Every squarefree denominator is indispensable. | Lower inverse-source bound | Failure control for any "drop composites" step |
| [891](https://github.com/GettysburgResearch/riemann/pull/891) SARG26 | 09-15, draft | Imported S(t) record brackets. Directed scalar replay passed; the primitive Z replay is pending; 310 of 844 brackets suffice. | Primitive Hardy-Z replay | (d) finite height only |
| [788](https://github.com/GettysburgResearch/riemann/pull/788) | 09-04, draft IMPORTED | Lamzouri arXiv:2609.02882 (> 2/3 simple critical zeros) plus the AxiomMath Lean development | Review | Input to the 888 series |
| branch `claude/friendly-allen-cl0dew` | 09-10, EMPIRICAL | Arb-certified sweeps of Pick/Loewner predicates, de Bruijn–Newman Laguerre and Weil forms. No violation found. | — | (d) finite-height detectors |

## 3. Overlap warnings (do not redo)

- **Exponent bookkeeping and barriers.** Already in w5copg `exponent_model/`, PR 910 `GEOMETRY_ENVELOPE_LIMIT.md` (exact, in `Q(√921)`) and `check_research_algebra.py` (148 predicates). One reconciliation is useful. The wave's DH-count optimum is `0.86984` (`results/F_DH_and_optimal.json`); w5copg reports `13/15 ≈ 0.86667`, and `barrier_lp.py` states `σ₀ ≥ 13/15` from the low side alone. These presumably use different count/energy models. State which.
- **Gauss-identity and mean-square numerics.** Done to `N ≤ 5·10⁴` and `D ≤ 1.02·10⁵` (w5copg).
- **The Lean audit** is done lexically. A real build needs a toolchain (lc2b3j, w5copg). If the wave has Lean available, the four comparator runs are the single highest-value verification step.
- **Height reformulations.** PR 910 `TAIL_AND_EULER.md` §5–7 already proves that a fixed-twist power bound is global, that `|t|^{−c}` gains only a constant, and that a translation-closed uniform band forces the line. It also shows Gaussian attenuation does not remove poles. Do not re-derive these.

## 4. Most promising pushes (a few agent-hours each)

**P1. Quantify, then probe, the joint inverse/plain moment.** This is the strongest single lever; three sources converge on it. Payoff step: add a `counts="joint"` model to `threshold_calculus.py`. It should use `#ℛ ≪ U^{1−δ(r+m)+ε}` (PR 910 eq. 6.7) in place of `max(r, 2m)`, under the PR 910 geometry with the detector constraints (6.2). Report the resulting `σ₀` exactly, which tells whether (6.6) is worth an analytic campaign. Empirical step: reuse w5copg `eisenstein.py`/`mean_square.py` to measure `Σ_u |M_u S_u(t_u)|²` with rowwise-maximised `t_u` against the product of marginals at `D ≤ 10⁴`, with the source masks. Deliverable: an exponent payoff table, plus EMPIRICAL scaling or an explicit row family violating (6.6).

**P2. Second independent replay of the PR 910 conditional deduction and of its uncovered Prop. 7.2.** The REVIEW states that `UPSTREAM_HEIGHT_AND_MOMENTS.md` §7, the source of the `1/2+5(1+θ)/(12k)` and `17/24` headline, was **not** independently reviewed. Extend `ledger_check.py` to the perturbed tuple: `ℓ = 1/6+1/40000`, `L₀ = 3/16 − 1/160000`, the `∂/∂ℓ ≤ 5/2` derivative bound, `1073/22032000`, and slack `19991/240000`. Then reconstruct Prop. 7.2's recursion `A₁(D) = B_p(D) − ν(p)B_p(D/Np)` and its induction. Deliverable: an exact-SHA review note at `670a76c1` naming the first uncertain step. This is verification, not progress, but it is cheap and needed before anything cites `17/24`.

**P3. Fourth-moment target (3.5): numerics plus structure.** Measure `Σ_{Nu≤H} |A_u(D)|⁴ / (D²H)` and the type split (sixth, cube, square, rest rows) with the w5copg code at `θ ∈ {0.05, 0.1}`. Separately, test the balanced-divisor column mean square (3.5) on the actual sextic symbols; PR 910's 90 panels used only ±1 surrogate phases. Deliverable: EMPIRICAL evidence for or against diagonal size, or a structured counterexample row class. Do not present a finite trend as the moment.

**P4. Bounded review of Kintali [K] (47/48).** No repository coverage exists. Identify [K]'s imported Hecke zero-density estimate (its Lemma 3.3). Check that its exponent supports the row count `R(a) = min(1, 5(1−a))` **uniformly in the conductor ranges of the Poisson rows** and at the needed heights. Check how much of [OAI] §§4, 6, 7 it inherits. Deliverable: the first uncertain step, or an adapter list. If it holds, [K] reduces the unverified surface to [OAI]'s probe, continuation and Poisson parts.

**P5. Quick falsification test of PR 910's native height route.** Its sufficient condition `𝒪_Y(σ;T) < 1/(12Ω)` for all large T, at `σ ≥ 1/2 + c·loglogY/logY`, forces `|G_Y B_Y − 1|` to be locally small everywhere on that curve. That is far beyond any known zero-free region. It is plausibly violated at large values of ζ even without zeros, since `|R_Y| ≥ 1/2` does not distinguish zeros from large values. Compute `ℰ_Y`, `𝒟_Y` and `𝒪_Y` at `Y = ⌈4(T+2)⌉` for T in `[10³, 10⁵]` along σ₀(Y). Check against Ω-results for `log|ζ|` in that strip. Deliverable: a decisive "the sufficient condition is false as stated" (in the spirit of issue 902), or EMPIRICAL margins. A positive finite run is not a band theorem.

**Longer horizon (outside this wave's hours):** the native common-kernel transfer for NRC32 `S_Y` (PR 909 OAI-RP26 acceptance tests; PR 908 §3). This is the bridge from QRH to the repository's own primary programme (issue 902). Its first deliverable is a finite coefficientwise identity with one common kernel, or an exact kernel-mismatch obstruction.

## 5. Scope reminders

- Every conditional item above carries QRH-IMPORT (unreviewed).
- `139999/160000` is conditional on the full imported analytic machinery, with one AI-agent scoped review and no Lean.
- PR 910's `17/24` and `1/2 + 5/(12k)` figures are conditional on moments that are **unproved**.
- No item here bounds `sup Re ρ` below `7/8` unconditionally, and none bears on the critical line.
