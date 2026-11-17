# Actionable conjectures and propositions (Riemann Observatory)

```text
Status: EXPLORATORY / OBSERVATORY-PROPOSED list of precise, testable statements. None is claimed proved
        unless its status line says THEOREM with a source. RH is open. The quasi-Riemann hypothesis (OpenAI,
        2026) and the two-thirds theorem (Alpoge-Furman, AI-discovered and human-verified; Lamzouri) are
        UNREFEREED 2026 claims: the 11/12 paper was audited by the Observatory (AI agents) with no error
        found, imported inputs not re-proved; the 7/8 paper was not audited and its Lean formalization is
        claimed, not replayed. The Landau-Siegel exclusion is unrefereed (Observatory audit: no error found).
Scope: 28 statements: 8 opened by the 2026 developments (quasi-RH method limits and extensions, consequences,
        including discovery mechanisms M4 and M8), 5 on critical-line proportions and GL(2), 4 from campaign
        C1, 1 from C3, 2 from C4, 3 from C5, and 5 from other archive connections and campaigns. For each:
        statement, status, evidence, first test, how it could fail, sources.
Exact sources or dependencies: connections/connections.jsonl and connections_register.md (CON ids, corrected
        forms used for needs_correction items); audits/quasi_rh/DOSSIER.md; audits/claims_2026/CRIT23/
        DOSSIER.md and SIEGEL/DOSSIER.md; proposals/independent_campaigns/C1 and C3 FINAL.md, C2, C4, C5
        REPORT.md with SKEPTIC_REVIEW.md (downgraded statuses reported); frontiers/ledger.jsonl (LED ids);
        corpus/bibliography.jsonl (PAPER ids; works not in the corpus are cited by arXiv id).
What was actually run: reading of the sources above; one mpmath cross-check script (scratchpad
        synth/checks.py) recomputing c*_lambda, lambda*, C_MT, the predictions T^2/(4 delta^2) of AC-15 and
        the bound and example of AC-22. The short proof in AC-22 was written for this file and has not been
        reviewed. No other proof was checked here; no certified computation; no Lean build.
Smallest remaining gap: most statements in Sections 2.1-2.2 are conditional on unrefereed 2026 inputs
        whose verification is ranked first in proposals/ranked_research_directions.md (D-01 to D-03). The
        campaign conjectures (AC-14 to AC-23) rest on numerics that are either Rayleigh-Ritz upper bounds,
        floating point, or small finite ranges; a finite test can falsify them but never prove them.
```

## 0. Conventions

- **Status vocabulary.**
  - THEOREM, with its source and review level.
  - CONDITIONAL on a named hypothesis.
  - PROPOSITION-PROOF-SKETCH (PPS).
  - HEURISTIC.
  - CONJECTURE.
  - OBSERVATORY-PROPOSED: first formulated inside an Observatory campaign, connection or this file; not reviewed outside the Observatory.
  - UNREFEREED (human preprint) and AI-GENERATED UNREFEREED.
  - NUMERICAL-RIGOROUS (Arb or exact integers) versus NUMERICAL-NONRIGOROUS.
- **Tests.** A "first test" is the cheapest step that could falsify or sharpen the statement. Finite computations never prove infinite statements.
- **Disclosure.** The Observatory's audits, campaigns and connection verifiers are AI agents (Claude). Alpoge-Furman's proof was discovered by Claude.

## 1. Summary

| ID | Short name | Origin | Status | Cost of first test |
|---|---|---|---|---|
| AC-01 | Density shadow of Proposition 3.1 | quasi_rh DOSSIER §2.5 | HEURISTIC; theorem form proposed | low |
| AC-02 | Conjecture G (infinite-order Hecke, CM curves) | M8, CON-0037 | CONJECTURE | medium |
| AC-03 | Quartic row mean square J4 and the floor of Ji's architecture | M8, CON-0038 | CONDITIONAL implication plus computed floor | low to medium |
| AC-04 | Linnik exponent under a uniform half-plane | M4, CON-0016, CON-0001 | CONDITIONAL; known in substance | low |
| AC-05 | Piltz exponents under ζ ≠ 0 on Re s > 7/8 | M4, CON-0018 | CONDITIONAL; sound_and_useful | low |
| AC-06 | Gafni-Tao exponent under 7/8 | M4, CON-0019 | CONDITIONAL; sound_and_useful | low |
| AC-07 | Montgomery-Vaughan bound under quasi-GRH | M4, CON-0017 | CONDITIONAL; sketch | medium |
| AC-08 | Hooley-type thresholds for Artin | M4, CON-0020 | PROPOSITION; partly published | low |
| AC-09 | GL2-D: distinct zeros of one GL(2) L-function | M8, CON-0035 | CONDITIONAL | medium |
| AC-10 | GL2-F: family averages via Petersson | M8, CON-0036 | expected theorem, unwritten | medium |
| AC-11 | RH-free 19/27 under a sub-thin-box hypothesis | M2, CON-0006 | CONDITIONAL; PPS | medium |
| AC-12 | Third-moment ceiling at reduced bandwidth | research_programs CRIT §8 | CONJECTURE (pessimistic) | medium |
| AC-13 | ξ′ ceiling against Wu's 0.86957 | M3, CON-0015 | CONJECTURE | low |
| AC-14 | Li positivity horizon c·T² log T | C1 | OPEN TARGET | medium |
| AC-15 | Jensen-heat bridge on injected zeros | C1-J2 with C2-17 | HEURISTIC; consistency check | low |
| AC-16 | Nicolas implication horizon | C1-D3 | PPS | medium |
| AC-17 | Persistence (de Bruijn-Newman converse) | M2, CON-0008, C1-E1 | target lemma; sharp form HEURISTIC | medium |
| AC-18 | Rate 1/2 for de Branges failures | C3-ADJ-RATE | CONJECTURE | low |
| AC-19 | Interpolation-regime window detection | C4 | CONJECTURE | medium |
| AC-20 | Flat window law for almost all heights | C4 | CONJECTURE; upper half THEOREM under H1 | high |
| AC-21 | Function-field window criterion without RH | C5 skeptic | PPS | low |
| AC-22 | Function-field detection horizon | C5 open question; this file | PROPOSITION (elementary) plus open question | low |
| AC-23 | Realisability of fakes as quadratic-type Euler products | C5-E4 | CONJECTURE (weak) | low |
| AC-24 | Heat-open infinite log-concavity | M7, CON-0033 | CONJECTURE | medium |
| AC-25 | Pólya's approximant: Λ* ≤ −4 | M5, CON-0024 | CONJECTURE (empirical) | medium |
| AC-26 | Möbius Nyman-Beurling decay exponent −2(α − Θ) | M5, CON-0021 | PPS | low |
| AC-27 | Beurling [α,β]-systems with α ≥ 2/3, β < 1/2 | M7, CON-0032 | OPEN; T2 to verify | medium |
| AC-28 | Rectangular Epstein threshold (BST Conjecture 1.1 false) | C2 skeptic F7 | skeptic finding, not adjudicated | low |

## 2. Statements

### 2.1 Opened by the 2026 developments

#### AC-01 - The density shadow of Proposition 3.1 (a falsification handle for the 11/12 paper)

**Statement** (theorem form to be proved).

- Setting: K = Q(√−3), ν a fixed finite-order Hecke character, χ_𝔫(u) = (u/𝔫)₆, and A_u(D) = Σ_{(𝔫,S)=1} μ(𝔫)ν(𝔫)χ_𝔫(u)W(N𝔫/D).
- Assume paper2's Prop. 3.1: Σ_{N(u)≤D^{1+ϑ}} |A_u(D)|² ≪ D^{2+ϑ+ε}.
- Then for each σ ∈ (1/2, 1) and ε > 0, the number of sixth-power-free u₀ with U < N(u₀) ≤ 2U such that L(s, νχ_·(u₀)) has a zero ρ with Re ρ ≥ σ, visible to a fixed smooth detector at length D ≍ N(u₀), is ≪ U^{2−2σ+ε}.

**Status.** HEURISTIC [O] (DOSSIER §2.5); OBSERVATORY-PROPOSED as a theorem. The input is AI-generated and unrefereed; the Observatory audit found no error (FND-0009).

**Evidence.**

- Each such u₀ makes roughly (H/N(u₀))^{1/6} rows u₀a⁶ carry sums of size D^σ.
- GRH for the twists implies Prop. 3.1 (audit_S3 §4).
- The resulting count exceeds what generic large-sieve density gives (de Faveri, arXiv:2610.04045, Cor. 1.5: ≈ 0.73 at σ = 3/4 against 0.5). That is no contradiction, since the coefficients are special. It locates the risk.

**First test.**

1. Write the detector step: choose W and the meaning of "visible", and prove the implication.
2. Compute Σ_{N(u)≤H} |A_u(D)|²/(D^{1+ϑ}H) in exact Z[ω] arithmetic for D ∈ [500, 4000], H = D^{1.1}, with the archive harness (audits/quasi_rh/architecture_checks).

**How it could fail.**

- The heuristic step "zero implies large row sums" may lose a detector factor, weakening the exponent.
- Numerics at D ≤ 4000 cannot decide asymptotics; consistency there carries no weight.
- Clear power growth would flag Prop. 3.1 for expert review. It would not refute it.

**Sources.** DOSSIER §2.5, §5.5(d); audit_S3; PAPER-0161.

#### AC-02 - Conjecture G: zero-free half-planes for infinite-order Hecke characters of Q(√−3)

**Statement.** For every unitary Hecke character ψ of K = Q(√−3), of any infinity type l, L(s,ψ) ≠ 0 for Re s > 11/12.

**Corollaries if true.**

- For every E/Q with j(E) = 0, L(E,s) ≠ 0 for Re s > 17/12. This would be the first fixed zero-free half-plane for a holomorphic newform of weight ≥ 2.
- #{π primary : Nπ ≤ x, arg π ∈ I} = (|I|/2π)π_K(x) + O(x^{11/12+ε}), uniformly in arcs I.

**Status.** CONJECTURE (CON-0037, needs_correction, corrected form). It depends on the unrefereed paper2.

**Evidence.**

- From eq:convert2: μψγ₋₁ = χ_𝔫(−1)G^{−1}ν₀α^{l−1}γ₂.
- Only the frequency m = l − 1 = 0 shows a main term. Measured values: |S₀|/X^{5/6} ∈ [0.176, 0.220] for X ≤ 3200, while for m ∈ {−3, …, 3}∖{0} max |S_m| ≈ 0.42√X. These are 908-term finite numerics, reproduced by the verifier.
- Pass to ψ̄ for the frequency-0 case.

**First test.**

1. Derive the archimedean transform J_m(s) for m = −2 (the CM case via ψ̄_E), including the cusp-cocycle terms from ∂_{z̄}², and check that it is entire.
2. List every use of radial weights in paper2 Secs. 4-7 and App. A-B.
3. Extend the angular-bias numerics to X ≈ 2·10⁴ with CRT-multiplicative γ₂.

**How it could fail.**

- Second-derivative cocycle terms may reintroduce a constant mode.
- Some step may need a radial Mellin transform with growth in l.
- If Prop. 3.1 is false, everything fails.

**Sources.** CON-0037; DOSSIER §2.6; PAPER-0960 (Patterson bias).

#### AC-03 - Quartic row mean square J4, and the floor of Ji's architecture

**Statement.**

- **(A) Floor proposition.** Within the Observatory's transcription of Ji's inequalities (PAPER-0155), no zero-density input reaches 11/12. The floor is ≥ 0.9898 unconditionally and ≥ 25/26 under GRH for the quartic family; with the w-contour constraint θ ≥ 1/2 it is 0.996732. With de Faveri's density exponent the optimum is 0.998327, and Ji's own 599/600 is feasible.
- **(B) J4.** Over K = Q(i), with A_u(X) = Σ_{(𝔫,1+i)=1} μ_K(𝔫)(u/𝔫)₄ W(N𝔫/X): if Σ_{N(u)≤X^h} |A_u(X)|² ≪ X^{1+h+ε} for some fixed 1 ≤ h ≤ 10/9, then ζ(s) ≠ 0 for Re s > 1/2 + 3h/8.

**Status.** (A) is a computation inside a transcription (CON-0038, sound_and_useful). (B) is a CONDITIONAL implication [O] (DOSSIER item C2 with n = 4); J4 itself is a CONJECTURE.

**Evidence.**

- The verifier re-derived Ji's constraints C1-C6 and the analytic floors 0.996732, 89/90 and 23/24.
- Even without the contour constraint, C1 and C6 alone give ≥ 0.9898.
- The extraction in (B) follows the n = 6 case of paper2 §3.

**First test.**

1. Have an independent reader re-derive C6 and the H^{Λ(σ,θ)} factor, with Λ(σ,θ) = max(0, 1 − 3σ/2, 1 − σ − θ/3).
2. Compute Σ|A_u(X)|² for X ≈ 2000, H ≈ X^{1.05} over Z[i] and compare with X·H.

**How it could fail.**

- (A): the transcription may have missed a degree of freedom, such as a different grouping of characters.
- (B): J4 may be false because quartic Gauss-sum averages without an angular twist are biased (Dunn-Radziwill under GRH; de Faveri-Dunn-Hoffstein lower bounds).

**Sources.** CON-0038; DOSSIER §4.1, §4.3; PAPER-0155.

#### AC-04 - Linnik exponent under a uniform half-plane (corrected)

**Statement.** Suppose every Dirichlet L-function is zero-free in Re s > θ, for a fixed θ < 1. Then, effectively:

- P(a,q) ≪_{θ,ε} q^{12/5+ε} with refereed density inputs (Montgomery's fixed-modulus estimate with Huxley's 12/5);
- q^{7/3+ε} with Chen-Gupta-Li Cor. 1.4 (PAPER-0745, unrefereed);
- ψ(x;q,a) = (x/φ(q))(1 + O(x^{−δ})) for φ(q) ≤ x^{5/12−ε}.

**Status.** CONDITIONAL; known in substance (CON-0016 and CON-0001, sound_but_known). It corrects DOSSIER §3, which gave 8/3 and the range x^{1−Θ}.

**Evidence.** sup_{1/2≤σ≤θ} min(3/(2−σ), 3/(3σ−1)) = 12/5, attained at σ = 3/4. With CGL's 7/3 cap, the sup equals 7/3 on [5/7, 16/21].

**First test.**

1. Write a one-page lemma with an explicit δ.
2. Check the uniformity in σ of the o(1) in CGL Thm 1.2 (§§5-7).

**How it could fail.** Only if the density estimates fail uniformly at small height. If QRH is false the statement is vacuous.

**Sources.** CON-0016; CON-0001; Thorner-Zaman (PAPER-0961, PAPER-0962); LED-LFUN-10.

#### AC-05 - Piltz divisor exponents under ζ ≠ 0 on Re s > 7/8

**Statement.** If ζ(s) ≠ 0 for Re s > 7/8, then α_k ≤ 7/8 − 49/(24k) for every k ≥ 9. This beats the tabulated records for k = 14, …, 21: 0.72917 against 0.73190 (Li) at k = 14, and 0.77292 against 0.79137 at k = 20. Under 11/12, α_k ≤ 11/12 − 17/(7k) for k ≥ 12.

**Status.** CONDITIONAL on the zeta half-plane, i.e. the Lean-claimed OpenAI statement. CON-0018, sound_and_useful (the verifier re-ran piltz.py).

**Evidence.**

- Titchmarsh §14.2 method: μ(σ) = 0 for σ > θ.
- Gabriel / Hardy-Ingham-Pólya convexity interpolates from the anchor (35/54, 9).
- ANTEDB Lemma 16.9.

**First test.**

1. Check the exact hypotheses of Ivić Lemma 8.3 at the limiting endpoint B = ∞.
2. Rerun with the anchors behind Li's and Trudgian-Yang's tables; an anchor (0.638889, 9) would raise C(7/8) to ≈ 2.125.

**How it could fail.** Through an artifact: for k ≥ 22 the comparison is against Ivić's older formulas, not tabulated records.

**Sources.** CON-0018; LED-GROWTH (μ(σ) context).

#### AC-06 - Gafni-Tao exceptional-set exponent under 7/8

**Statement.** If ζ ≠ 0 on Re s > 7/8, the Gafni-Tao Thm 1.2 exponent satisfies

μ(θ) ≤ max(U_{<7/8}(θ), min((3/14)(1 − θ) + 3/4, (3/5)(1 − θ) + 1/2)),

where U_{<7/8} is the GT supremum restricted to σ < 7/8.

- This strictly improves the bound exactly for θ ∈ (≈0.2445, 5/12), with maximal gain ≈ 0.0108 at θ ≈ 0.2725.
- Under 11/12 the gain is at most ≈ 0.0026, at θ ≈ 0.25.
- The thresholds 17/30 and 2/15 are unchanged.

**Status.** CONDITIONAL; CON-0019, sound_and_useful. CON-0028 adds that it is a record only if it survives GT Thm 1.3 (the A* data).

**Evidence.** A(7/8) = 12/7 and A*(7/8) = 24/5 from the tables. The endpoint 5/12 is exact, since A(7/8)(1 − θ) = 1.

**First test.** Recompute with GT Thm 1.3 (A*) and with exact rational arithmetic at the breakpoints.

**How it could fail.** The gain may disappear under Thm 1.3. The endpoint 0.2445 is a statement about this method's bound, not about the true μ.

**Sources.** CON-0019; CON-0028; LED-ZDE-8, -9.

#### AC-07 - Montgomery-Vaughan character-sum bound under quasi-GRH

**Statement.** Suppose L(s, χψ) ≠ 0 for Re s > θ for every ψ of modulus ≤ (log q)^C, with θ < 1 fixed. Then max_x |Σ_{n≤x} χ(n)| ≪ (1 − θ)^{−1} √q log log q for every primitive χ mod q.

**Status.** CONDITIONAL; the verifier's sketch in CON-0017 (needs_correction; this is the corrected form). MV §§8-9 were not re-read.

**Evidence.**

- On minor arcs, the unconditional MV Corollary 1.
- On major arcs, a QRH version of MV Lemma 2 with error x·y^{θ−1}(log kx)²/(1 − θ)², with y = (log q)^{C/(1−θ)}.
- The θ < 2/3 threshold of the Granville-Soundararajan route is an artifact of that route.

**First test.**

1. Write the QRH version of Lemma 2 and the MV §9 bookkeeping.
2. Check that θ = 1/2 recovers MV.

**How it could fail.** MV's proof might use GRH somewhere besides Lemma 2 (CON-0029 notes Littlewood's bound). The part checked by the verifier, √q(log q)^{6/7}, would then be the best available.

**Sources.** CON-0017; CON-0029; PAPER-0082.

#### AC-08 - Hooley-type thresholds for Artin's conjecture

**Statement.** Let a be admissible, and suppose ζ_{Q(ζ_k, a^{1/k})} is zero-free in Re s > θ for all squarefree k. Then liminf N_a(x)/π(x) ≥ A(a) − log(1/(2(1 − θ))), which is positive for θ < 1 − e^{−A(a)}/2 ≈ 0.656 for generic a.

Known thresholds: Nongkynrih (2001) gives a positive proportion for a = 2 when θ < 1 − e^{−12A/5}/2 ≈ 0.796; Hooley's remark gives infinitude when θ < 1 − 1/(2e) ≈ 0.816. Consequently 7/8 and 1 − 10⁻⁶ give nothing by these routes.

**Status.** PROPOSITION: elementary Bombieri-Vinogradov bookkeeping, plus published results (CON-0020, corrected).

**Evidence.** Bombieri-Vinogradov for prime q ≤ √x/(log x)^B, with Brun-Titchmarsh for the tail.

**First test.** Read Hooley §§5-6 to confirm the ranges; check whether the Murty-Murty BV variant covers part of [x^{1−θ}, x^{1/2}].

**How it could fail.** It could not fail as an implication. Improvement needs a non-abelian large sieve over q ∈ [x^{1/8}, x^{1/2}].

**Sources.** CON-0020.

### 2.2 Critical-line proportions and GL(2)

#### AC-09 - GL2-D: a positive proportion of distinct zeros for every primitive GL(2) L-function

**Statement.** Let f be a primitive holomorphic or Maass newform. Assume Lemma GL2-PC (D-11 in the ranked directions): the unconditional all-zeros pair-sum asymptotic for Fourier support in [−1/2 + ε, 1/2 − ε] in GUE units. Then liminf N_d(f;T,2T)/N(f;T,2T) ≥ c*_{1/2} = 0.461688…, where c*_λ = √2 tan(λ/√2)/(1 + (λ/√2) tan(λ/√2)).

Barrier (THEOREM for the window class): the simple-on-line certificate is positive only for λ > λ* = 0.5501939647, so bandwidth 1/2 alone yields no simple critical zeros.

**Status.** CONDITIONAL on Lemma GL2-PC (plausible, unwritten). CON-0035 and CON-0011, needs_correction; the corrected values are used.

**Evidence.**

- rank(G̃) ≥ (tr G̃)²/‖G̃‖²_HS (AF Rem. 3.3).
- R*_{1/2} = 2.1659639, recomputed by quadrature and by an n = 400 quadratic programme.
- A doubled-lattice configuration with 0% simple and 50% distinct zeros is consistent with bandwidth-1/2 data, so the simple-zero barrier is genuine.

**First test.** Take LMFDB zeros of L(s,Δ) (level 1, weight 12) or of 11a up to height ≈ 10⁴. Compute the window-weighted ΣK²/N at bandwidth 1/2 and compare with 13/6 (flat window) and 2.1660 (cos(u/√2) window). This tests the normalisation, not the theorem.

**How it could fail.**

- The GL(2) prime-side diagonal at X ≈ T^{1/2} may need a zero-free input stronger than the classical region.
- The Montgomery-Vaughan edge may force λ slightly below 1/2.

**Sources.** CON-0035; CON-0011; LED-CRIT-19; CRIT23 DOSSIER §7.

#### AC-10 - GL2-F: simple critical zeros on average over H_k(N)

**Statement.** Fix k ≥ 2; let N be prime → ∞ and T polylogarithmic in N. Assume the diagonal lemma: Σ_f ω_f |Σ_{p≤X} a_p λ_f(p)|² = (1 + O((X/N)^{k−1}N^ε)) Σ|a_p|² for X ≤ N^{1−ε}. Assume also a family zero-density estimate, an averaged counting estimate and an exterior-tail bound. Then:

- Σ_f ω_f N₀ˢ(f;T,2T)/Σ_f ω_f N(f;T,2T) ≥ 0.6725 − o(1);
- the distinct-zero analogue is ≥ 0.8363 − o(1);
- with the Weil bound only (k = 2, bandwidth 3/4), the bounds are 0.4191 and 0.7095.

**Status.** Expected theorem; proof not written (CON-0036 and CON-0012, corrected).

**Evidence.**

- The rank-trace certificate is linear in (tr A, tr A²), so averaging with nonnegative weights is legitimate.
- The mechanism mirrors Hua-Yang's Dirichlet-family theorem (arXiv:2608.16034, not in corpus).

**First test.**

1. Prove the diagonal lemma by opening the Kloosterman sums and applying the additive large sieve; check the relative error (X/N)^{k−1} numerically for N ≈ 10³-10⁴.
2. The prediction for the window statistic at bandwidth 0.9 is R*(0.9) = 1.406898.

**How it could fail.**

- Forms with small L(1, sym² f) dominate the harmonic weights. This is harmless for the weighted statement.
- If T grows like a power of N, the bandwidth drops and simple zeros are lost.

**Sources.** CON-0036; CON-0012; LED-CRIT-18.

#### AC-11 - RH-free 19/27 under a sub-thin-box hypothesis

**Statement.**

- (a) Unconditionally, N*(T) ≥ |S₁|²/(S₂ + D/2), with D the off-line pair defect.
- (c) Suppose that for all large T every zero with T < γ ≤ 2T has |β − 1/2| ≤ η(T)/(log T)^{3/2} with η(T) → 0. Then liminf N*(T)/N(T) ≥ 19/27, counting simple zeros anywhere.

**Status.** CONDITIONAL theorem; PROPOSITION-PROOF-SKETCH (CON-0006, needs_correction, corrected form). The verifier: "the rest stands: inequality (*) and theorem (c)".

**Evidence.** Subharmonicity of |a′|² on discs of radius 1/L; the local count N(t+1) − N(t) ≪ log t; unconditional mollified mean values for |σ − 1/2| ≤ 3/L. Together these give D ≪ η²TL³ = o(S₂).

**First test.**

1. Write the note.
2. Quantify the largest explicit η such that inequality (*) beats Knausgard's simple-anywhere 0.67800919: D ≤ ηTL³ with η < 0.01074.

**How it could fail.** BHB's error terms O(TL^{2+ε}) might interact with the defect. Note also that the hypothesis is stronger than BGST's fixed thin box.

**Sources.** CON-0006; PAPER-0070; PAPER-0453; PAPER-0049.

#### AC-12 - Third-moment ceiling at reduced bandwidth (a pessimistic conjecture)

**Statement.** Let 𝒞 be the class of certificates for liminf N₀ˢ/N that use only:

- tr A = N;
- the second trace moment with Fourier support [−1, 1];
- a third trace moment with support in the Rudnick-Sarnak range (X = T^{2/3−ε});
- the on-line/off-line inertia structure.

Then no certificate in 𝒞 certifies more than 0.6819.

**Status.** CONJECTURE (OBSERVATORY-PROPOSED in this file). It is designed as a decision test for research_programs CRIT §8.

**Evidence.**

- The bandwidth-one two-moment ceiling is 0.6818287 (AF §7.2; author-stated, not audited).
- AF §7.2(e) state informally that higher moments add nothing unconditionally at X ≍ T.
- AF Rem. 6.1: reducing the bandwidth strictly lowers the second-moment constant.
- The ledger verifier for CRIT expects that a third moment at reduced bandwidth may not raise the Chebyshev-Markov-Stieltjes lower bound on the rank.

**First test.** An interval-enclosed LP/SDP over periodic configurations with the on/off partition plus the third-moment constraint. Abandon the direction if the ceiling exceeds 0.6818 by less than 10⁻³ (research_programs CRIT §8).

**How it could fail.** The third moment at bandwidth 2/3 might exclude the configurations with one third of the zeros off the line, as the Montgomery-Taylor window excludes the flat-window extremals. The ceiling would then rise, and an RH-free triple-correlation lemma becomes the target.

**Sources.** CRIT23 DOSSIER §7; LED-CRIT-10; research_programs CRIT §3, §8.

#### AC-13 - Zeros of ξ′: no bandwidth-one certificate beats Wu

**Statement.** No certificate built from the two bandwidth-one trace moments (Farmer-Gonek form factor) and the on/off partition certifies a proportion of zeros of ξ′ that are simple and on the line exceeding 0.86957, Wu's unconditional proportion on the line (without simplicity).

**Status.** CONJECTURE (OBSERVATORY-PROPOSED). The window part is CON-0015, sound_and_useful, NUMERICAL-NONRIGOROUS.

**Evidence.** The supremum over admissible windows is 0.868641 ± 2·10⁻⁶ for simple-on-line, and 0.934321 for distinct. AF Rem. 7.1: 0.85838 (flat window) and 0.86864 (quartic window).

**First test.** Run the periodic-configuration ceiling LP of AF §7.2 with the Farmer-Gonek form factor. Report an interval-enclosed ceiling, and abandon if it is below 0.86957 + 10⁻⁴.

**How it could fail.** The ceiling LP may exceed 0.8696. Then a Knausgard-type 7-8-point certificate (his Thm 5.1 with C(f) = R*(ψ) = 1.13136) becomes the instrument.

**Sources.** CON-0015; PAPER-0486 (Rem. 7.1).

### 2.3 From campaign C1 (detection horizons)

#### AC-14 - Li positivity beyond T²

**Statement.** There is an explicit c > 0 such that, for T ≥ T₁, RH(T) implies λ_n > 0 for all 1 ≤ n ≤ cT² log T.

**Status.** OPEN TARGET (C1 FINAL §8.1). The known part is a THEOREM (C1-L2; statement due to Oesterlé via Voros; complete independent proof in C1 FINAL): RH(T) with T ≥ 100 implies λ_n > 0 for n ≤ T².

**Evidence.**

- C1-L4 (PPS): exponent 2 is optimal for arguments using only RH(T) plus N(t) bounds.
- The single-defect barrier is n ≈ c(T)T² log T, with c(T) = 5.84, 5.44, 4.53, 4.10 at T = 100, 10³, T₀, 10¹⁰⁰, so c(T) → 4.
- Against adversarial phases the heuristic ceiling is c = 2.

**First test.** Redo Regime I of the C1-L2 proof keeping the oscillation of cos(nφ) instead of bounding by −(na)². Compute the largest c for which the explicit tails (Rosser) still close at T = 100.

**How it could fail.** A configuration of several defects with adversarial phases could make any c > 0 false for arguments of this type. The skeptic's stress model fails 10-18% earlier than the single defect.

**Sources.** C1 FINAL §3.1, §1 (item 4), §8.1; LED-POS-2.

#### AC-15 - Jensen-heat bridge on injected zeros

**Statement.** Let ξ̃ = ξ·P, where P has an injected quadruple at 1/2 ± δ ± iT, in the isolated regime (T small relative to the first zeta zero, or more generally T/δ large with no real zeros nearby). Then the first degree d with J^{d,0}(ξ̃) not hyperbolic satisfies d* = (T²/(4δ²))(1 + o(1)).

**Status.** HEURISTIC (C1-J2, with "possibly new" kept only as a search-limited label). The cross-check is OBSERVATORY-PROPOSED in this file.

**Evidence.**

| Quadruple at | Predicted T²/(4δ²) | Observed |
|---|---|---|
| 0.9 + 5i | 39.06 | first failure at d = 40 (C2-17; C2 skeptic: exactly 40; NUMERICAL-NONRIGOROUS) |
| 0.6 + 5i | 625 | hyperbolic to d = 240 |
| 0.75 + 10i | 400 | hyperbolic to d = 240 |
| 0.9 + 14i | 306 | hyperbolic to d = 240 |

On Farmer's toy functions X_j the bridge is within 2.6% of the certified thresholds (X₁₀: 119.63 against 120; X₄₀: 1891.89 against 1898; X₆₀: 4245.1 against 4243).

**First test.** Use Arb-certified root counting for J^{d,0}(ξ̃) at the predicted d ± 2. By C1-ADJ-MONO, one certified pair fixes the threshold for all d. Run (0.9, 5), (0.8, 5) (predicted 69.4), (0.9, 8) (predicted 100) and (0.75, 10).

**How it could fail.**

- The isolated-pair approximation t_c ≈ 2δ² breaks down when real zeros are near (dense regime, t_c ≈ 4δ/log(T/2π)).
- The C2 numerics used rounded coefficients; 60-digit rounding produced spurious non-real roots, so certification is essential.
- The normalisation of C1's even Jensen polynomials against C2's must be matched first.

**Sources.** C1 FINAL §2 (C1-J2, C1-J3), §3.3; C2 REPORT C2-17; C2 SKEPTIC_REVIEW (C2-17 replay).

#### AC-16 - Nicolas implication horizon

**Statement.** There is an explicit X(T), with X(T) ≥ c·T²/(log T)² for T ≥ T₁, such that RH(T) implies Nicolas' criterion c(x) > 0 for all 2 ≤ x ≤ X(T). Here c(x) = log Π_{p≤x}(1 − 1/p)^{−1} − γ − log log θ(x). In particular X(T₀) ≥ 3.0·10¹³, which would make Morrill-Platt's Robin range a corollary of RH(T₀).

**Status.** PROPOSITION-PROOF-SKETCH (C1-D3, leading order only).

**Evidence.**

- The leading explicit formula is √x log x·c(x) = 2 + Σ_ρ x^{ρ−1/2}/(ρ(1 − ρ)) + o(1), whose zero sum lies in [−β, β] under RH, with β = 0.0461914.
- The leading-order horizon at T₀ is 4.36·10²³, and the ψ/π analogue is a theorem (Johnston).

**First test.** Write the truncated explicit formula with all O(1/log x) terms and explicit constants. Evaluate X(T₀) and compare it with 3.0·10¹³.

**How it could fail.** The lower-order and S(t) terms could force a much smaller X(T). Any value above 3.0·10¹³ still suffices for the corollary.

**Sources.** C1 FINAL §2 (C1-D3), §3.4, §8.3; LED-ARITH-1, -6, -17.

#### AC-17 - Persistence: an off-line zero forces Λ > 0 quantitatively

**Statement.**

- There are absolute c, γ₀ > 0 such that ζ(1/2 + δ + iγ) = 0 with 0 < δ < 1/2 and γ ≥ γ₀ implies Λ ≥ cδ²/(log γ)².
- Sharp form: Λ ≥ c·min(δ², δ/log γ).

**Status.** The first form is a target lemma with a proof outline (CON-0008, sound_and_useful). The sharp form is HEURISTIC (C1-E1).

**Evidence.**

- C1-E1 collision-time model: t_c ≈ 2δ² for an isolated pair and ≈ 4δ/log(T/2π) when dense. Three implementations agree; at T₀, t_c = 1.99·10⁻⁴, 0.0153, 0.0516 and 0.1013 for δ = 0.01, 0.1, 0.25 and δ_max.
- Window-energy argument in CON-0008.

**First test.** Write the energy proof rigorously (ODE between collisions; Polymath Prop. 3.1(ii)), and compare the explicit constant with the C1 gap-lattice ODE (exp_dbn_jensen.py).

**How it could fail.** The far-field velocity bound needs an H_t′/H_t estimate at distance about 1 from the zeros, beyond Polymath Thm 1.5(iv). Clusters of real zeros could slow the collision.

**Sources.** CON-0008; C1 FINAL §2 (C1-E1), §3.5, §8.5; LED-DBN-4, -10.

### 2.4 From campaign C3 (failure anatomy)

#### AC-18 - The de Branges zero condition fails at half of all zeros

**Statement.** With P_n = −Re{ξ′(ρ_n)ξ(1 + ρ_n)}, #{n ≤ N : P_n < 0}/N → 1/2 as N → ∞. A weaker target: P_n < 0 for infinitely many n, or for a positive proportion of n.

**Status.** CONJECTURE C3-ADJ-RATE (adjudicated as a conjecture with heuristic support). The reformulation is a THEOREM (C3-ADJ-S): P_n < 0 iff S(γ_n) − δ(γ_n) ∈ (3/4, 7/4) mod 2, under RH up to γ_n with simple zeros.

**Evidence.**

- Arb verdicts with 0 undetermined in every block. Failures per 1000 zeros: 80, 131, 167, 193, 194, 209, 227, 224 at n₀ = 1, 10⁴, 10⁵, 10⁶, 10⁷, 10⁸, 10⁹, 10¹⁰.
- A wrapped Gaussian with the empirical Var(S − δ) matches every block within about one standard error.
- Var(S − δ) grows at about 0.055 per unit of log log T, close to Selberg's 1/(2π²) = 0.0507.

**First test.** Compute 1000-zero blocks at n = 10¹¹ and 10¹² with acb.zeta_zeros. The prediction is ≈ 0.23 and ≈ 0.24. Extrapolation (HEURISTIC): 25% near T ≈ 10¹⁴, 40% near T ≈ 10⁵⁴³.

**How it could fail.** Equidistribution of S(γ_n) − δ_n mod 2 at unit scale is not implied by a CLT at scale √(log log T). The positive correlation between S(γ_n) and arg ζ(3/2 + iγ_n) (0.67-0.89) could persist and bias the limit.

**Sources.** C3 FINAL §3.2-§3.3, §9 (items 1-2); FND-0013; PAPER-0779.

### 2.5 From campaign C4 (Weil-window locality)

#### AC-19 - Interpolation-regime detection by Weil windows

**Statement.** Fix δ ∈ (0, 1/2). Assume H1 at height T: one off-line quadruple at 1/2 ± δ ± iT, and all other zeros on the line. Then λ_min(L) < 0 for every L ≥ (1/2) log(T/2π) + C, with C absolute (independent of T and δ).

**Status.** CONJECTURE (OBSERVATORY-PROPOSED; a C4 open question).

**Evidence.**

- In the additive single-defect model, the Galerkin thresholds are Rayleigh-Ritz upper bounds on L*, so they point in the direction of the conjecture. They give L* − L_N ∈ [0.02, 0.63] for T₀ = 27.7 to 7·10⁴.
- The thresholds decrease under basis refinement: at T₀ = 100, δ = 0.01 they go 0.327, 0.220, 0.186, 0.177 (investigator), then 0.170 at N = 192 (skeptic).
- In the lattice model (C4-LAT, THEOREM), L > π/s, i.e. the Nyquist window, detects every δ > 0.
- For κ = δ log(T/2π) > κ_c = 2.1773, detection already happens at L_flat ≪ L_N (C4-B, rigorous under H1).

**First test.**

1. A full-saturation (Landau-Widom-type) test-function construction. Zhu's half-saturation canonical product would give only L ≥ log(T/2π), twice the Nyquist window.
2. Larger-N Galerkin runs at T₀ = 10⁴ and δ = 0.01.

**How it could fail.** C may have to depend weakly on δ, as C(δ) ≈ b log(1/δ) with fitted b = 0.015-0.06. Prime-comb alignment at special heights could also shift the threshold by O(1).

**Sources.** C4 REPORT (C4-LAT, C4-B, C4-D1, C4-D2, open questions); C4 SKEPTIC_REVIEW (C4-D2, C4-R).

#### AC-20 - The flat window law holds for almost all heights

**Statement.** Fix δ ∈ (0, 1/2) and assume H1. Let L_flat(T,δ) solve sinh(2δL)/(2δ) − L = (1/2) log(T/2π). Then L*(T,δ)/L_flat(T,δ) → 1 as T → ∞ along a set of heights of full logarithmic density.

**Status.** CONJECTURE (OBSERVATORY-PROPOSED). The upper half, limsup ≤ 1, follows from the THEOREM C4-B under H1, since L_B/L_flat → 1. The content is the lower half, a blindness statement. It is conditional at best (C4-BL needs hypothesis R, which the skeptic notes is essentially the needed matrix inequality).

**Evidence.**

- Numerics: |L* − L_flat| ≤ 0.08 at T = 10²⁰-10⁵⁰ for δ = 0.49 (upper bounds).
- Ψ_eff/log(T/2π) = 0.60-0.92 at 10⁶-10¹⁰.

**First test.** The lower half cannot be tested by Rayleigh-Ritz numerics, which certify detection, not blindness. The first test is theoretical: prove hypothesis R on average over T in the sampling regime T ≥ (1 + c)2πe^{2L}. A numerical companion is to search, by Kronecker-type alignment of T log p for p ≤ e^{2L}, for heights where Ψ_eff ≪ log T, and to measure L_sinh there.

**How it could fail.** Worst-case prime-comb alignment can be of size ≈ 4σ²e^L, comparable to log T at L ≈ L_flat. So the statement must exclude a sparse set of heights. Whether that set has logarithmic density zero is the question.

**Sources.** C4 REPORT (C4-B, C4-BL, C4-D3, C4-H); C4 SKEPTIC_REVIEW (C4-H downgraded, C4-BL).

### 2.6 From campaign C5 (function-field transfer)

#### AC-21 - Function-field Weil criterion on one finite window, without assuming RH

**Statement.** Let C have genus g over F_q, and let W(u) = Σ_ρ m_ρ û(γ_ρ) conj(û(γ̄_ρ)) be the zero side of the explicit formula for u ∗ ũ. Then RH(C) holds iff W ≥ 0 on C_c^∞(−a, a) for any single a > (g − 1/2) log q. The bound is sharp for the formal class of fake zeta functions.

**Status.** PROPOSITION-PROOF-SKETCH (C5 skeptic §3.2). It rests on the confluent inertia theorem (C5 skeptic §3.1, THEOREM, exact checks) and on Suzuki's fibre decomposition (arXiv:2610.41115 Prop. 4.3; not in corpus), redone without RH.

**Evidence.**

- inertia(T_N) = (r − m, m, N − r) for N ≥ r, checked exactly on 3,300 squarefree, 249 non-squarefree and 93 synthetic cases.
- A fake with T₅ ≻ 0 and T₆ indefinite (q = 3, g = 3, h = x³ − 10x − 7) shows sharpness.

**First test.** Write the fibre decomposition with off-circle ζ_j line by line (polarised Parseval on residue classes γ_j + 2πZ/log q). Check it numerically on the census by evaluating W on explicit test functions.

**How it could fail.** The polarised Parseval step for non-real γ requires û to be evaluated off the real axis; the growth of û there must be controlled.

**Sources.** C5 REPORT (C5-T3, C5-E3); C5 SKEPTIC_REVIEW §3.1-§3.2.

#### AC-22 - A function-field detection horizon

**Proposition** (OBSERVATORY-PROPOSED in this file; elementary; not reviewed). Let P satisfy the curve functional equation with real coefficients. Suppose exactly two of its 2g normalised reciprocal roots lie off the unit circle, and that they are real, β and 1/β with |β| > 1. Then the first k with |N_k − q^k − 1| > 2g·q^{k/2} satisfies

k* ≤ ⌊arccosh(2g − 1)/log|β|⌋ + 1.

*Proof.*

1. t_k = β^k + β^{−k} + Σ_j e^{ikθ_j}, where the sum runs over the 2g − 2 unimodular roots.
2. Since β and 1/β have the same sign, |β^k + β^{−k}| = 2cosh(k log|β|).
3. Hence |t_k| ≥ 2cosh(k log|β|) − (2g − 2), which exceeds 2g once 2cosh(k log|β|) > 4g − 2. ∎

**Check.** For the hidden fake q = 3, g = 3, h = x³ − 10x − 7: |β| = 1.04071 and the bound is 57.4, so k* ≤ 58. The census reports k* = 28. All g = 1 fakes have k* = 1, consistent with the bound.

**Open question** (C5).

- What is the distribution of k*·log|β_max| over the census?
- There is no general lower bound: phases can align at k = 1.
- This is the function-field picture of C1's dispersal. The Toeplitz test detects every fake at size N ≤ 2g (C5-T3), while pointwise point counts can need k* up to ≈ arccosh(2g − 1)/log|β|.

**First test.** Tabulate k* and |β_max| per case from experiments/results/C5-function-field-transfer/fake_census.json.

**How it could fail.** The proposition is elementary and covers only real off-circle pairs. A complex off-circle quadruple needs a separate bound, because the phase of β^k matters.

**Sources.** C5 REPORT (C5-E1 example (b), open questions); C5 SKEPTIC_REVIEW §4.

#### AC-23 - Most fakes are quadratic-type Euler products as q grows

**Statement.** For g = 2 and odd q → ∞, the fraction of RH-false admissible P (C5-E1) that are realisable as Euler products over the places of P¹/F_q, with a_v ∈ {±1} off a set S of total degree 2g + 2 (C5-E4), tends to a positive limit.

**Status.** CONJECTURE (OBSERVATORY-PROPOSED; weak, 4 data points). The interpretation is HEURISTIC.

**Evidence.** Realisable over RH-false: 8/17, 133/199, 482/675 and 1122/1534 at q = 3, 5, 7, 9, i.e. 0.47, 0.67, 0.71, 0.73. For g = 1 it is 64/64. Both the investigator's and the skeptic's algorithms reproduce these counts.

**First test.** Run q = 11 and q = 13 for g = 2 with the mod-2 criterion C5-L2 and the exact recursion.

**How it could fail.** The fraction may depend on q modulo small integers through the mod-2 condition P(T)(1 − T)(1 − qT) ≡ Π_{v∈S}(1 − T^{deg v}), and so may not converge.

**Caveat.** Nothing here transfers to Q, where individual primes are visible and the degree-1 Selberg class is rigid (Kaczorowski-Perelli).

**Sources.** C5 REPORT (C5-L2, C5-E4); C5 SKEPTIC_REVIEW §4.

### 2.7 Other archive connections and campaigns

#### AC-24 - Infinite log-concavity is heat-open, so it cannot imply RH

**Statement.** Write F_t(x) = Σ λ_n(t)x^n for the Taylor expansion attached to H_t, with kernel e^{tu²}Φ (for t = 0, F₀(x) = ξ(1/2 + √x)). Then there is t₀ > 0 such that (λ_n(t)) is strictly infinitely log-concave for every t ∈ (−t₀, 0]. Consequently strict infinite log-concavity of (λ_n), and its truncations (r-log-concavity), cannot imply RH, because H_t is RH-false for every t < 0 (Rodgers-Tao).

**Status.** CONJECTURE (CON-0033, needs_correction; restricted per the correction to the log-concavity hierarchy).

**Evidence.**

- At t = 0 this is Liu-Mao (arXiv:2610.04972, not in corpus; unrefereed).
- Numerics (mpmath at 300 digits; NUMERICAL-NONRIGOROUS): L^jλ_n(t) > 0 for 1 ≤ j ≤ 10 and n ≤ 120 − j at t ∈ {−0.01, −0.1, −1, −10, −100, −1000, −10⁴}, and for ξ̃ with quadruples at 0.6 + 5i, 0.6 + 14i, 0.9 + 5i, 0.99 + 2i.
- Degree 2: (1, b, c) is infinitely log-concave iff b²/c ≥ φ² = (3 + √5)/2 (credited to McNamara-Sagan).

**First test.** Redo Liu-Mao §3 with kernel e^{tu²}Φ for |t| ≤ t₀, then run interval arithmetic for n ≤ 12000 and m ≤ 14 at t = −t₀.

**How it could fail.** Liu-Mao's large-n asymptotics may depend on t = 0 features; the numerics cover only low indices in the Gaussian regime.

**Sources.** CON-0033; PAPER-0036; C2-29.

#### AC-25 - Pólya's approximant has strictly negative de Bruijn-Newman constant

**Statement.** For Φ*(u) = 4π² cosh(9u) exp(−2π cosh 4u), the symmetrised n = 1 term of Φ, the constant Λ* = Λ_DN(Φ*) satisfies Λ* ≤ −4 (Polymath normalisation).

**Status.** CONJECTURE (empirical; CON-0024, sound_and_useful). Λ* ≤ 0 is a THEOREM (Pólya), and Λ* is finite (Newman, since Φ* decays faster than exp(−Ct⁴)).

**Evidence.**

- No Fourier critical points were found for λ ∈ {−0.05, −0.2, −0.5, −1, −2} on [0, 200], or for λ ∈ {−4, −128, −512, −2048} on [0, 600].
- Argument-principle counts equal the real sign-change counts at λ = −4 and −128.
- Quadrature error is uncontrolled.
- Zeros at λ = 0: 17.9856, 38.1308, 48.9495, 57.9499 (corrected list).

**First test.** Use the verifier's reduction via de Bruijn's cosh shrink: Λ* ≤ inf{λ : all zeros of the Fourier transform of e^{λu²} exp(−2π cosh 4u) lie in |Im z| ≤ 9/√2}, with rigorous quadrature.

**How it could fail.** A collision at moderate λ ∈ (−4, 0) between grid points. Λ* = 0 is not excluded by anything proved.

**Sources.** CON-0024; LED-DBN-1, -7.

#### AC-26 - Möbius Nyman-Beurling decay exponent equals −2(α − Θ)

**Statement.** Let Θ = sup Re ρ. Following Manzur-Quintero (arXiv:2611.03924, not in corpus), set E = 1/s, G_k = (k^{−s} − k^{−1})ζ(s)/s, S_n = Σ_{k≤n} μ(k)G_k and s_n(α) = ‖S_n − E‖²_{H²(C_α)}. Then:

- for α ∈ (Θ, 1), limsup_n log s_n(α)/log n = −2(α − Θ);
- for α ≥ 1, the limsup is −2(1 − Θ);
- RH holds iff s_n(α) ≪ n^{1−2α+ε} for one, equivalently every, α ∈ (1/2, 1).

**Status.** PROPOSITION-PROOF-SKETCH (CON-0021, sound_and_useful with minor corrections at α = 1). It is an RH-equivalent reformulation, not progress.

**Evidence.**

- Upper bound: Perron for M_n(s) shifted to Re = β₀ + ε.
- Lower bound: M_1(x) = Ω(x^{Θ−1−ε}) via the continuation of 1/ζ.
- MQ Table 1: the decade slopes for n ≤ 10⁶ are within 0.08 of 1 − 2α (an illustration only).

**First test.** Write the 3-4 page proof, handling α = 1 through (M_n(s) − M_n(1))ζ(s). Check Balazard-Saias 2004 for an existing weighted-norm rate.

**How it could fail.** Uniformity as α ↓ Θ; the Ω-statement holds only along a subsequence.

**Sources.** CON-0021; PAPER-0004; PAPER-0606.

#### AC-27 - Beurling systems with α ≥ 2/3 and β < 1/2 exist

**Statement.**

- (i) There exists a Beurling generalized prime system with ψ_P(x) = x + O(x^{α+ε}) (sharp) and N_P(x) = ax + O(x^{β+ε}), with α ≥ 2/3 and β < 1/2.
- (ii) T2 of CON-0032: for Θ ∈ [1/2, 2/3) and β > 2Θ/(Θ + 2), "Beurling + N_P = ax + O(x^{β+ε}) implies QRH(Θ)" is false unconditionally.

**Status.** (i) is OPEN; it is an instance of the existence conjecture recorded in CON-0032 as Hilberdink-BDR (all [α,β] with max(α,β) ≥ 1/2). (ii) is OBSERVATORY-PROPOSED and to be verified line by line. CON-0032's T1 (β > 2/5 for RH) is a THEOREM given BDR 1.3, by case split.

**Evidence.** BDR Thm 1.1 (any α ∈ [0,1) with β ∈ [1/2, 1)); BDR Thm 1.3, assuming RH (1/2 < α < 2/3 with β ≥ 2α/(α + 2)); BDR Remark 5.3(2) (improvements possible).

**First test.**

1. Audit BDR §5 for every use of RH and write T2 under QRH(Θ).
2. Try the double-prime variant (Remark 5.3, α < 4/5) with convolution estimates sharper than the hyperbola method.

**How it could fail.** A hidden Ingham-type inequality linking α and β below 1/2. That would itself be a positive theorem: integer regularity would then carry quasi-RH information.

**Sources.** CON-0032; C2-19, C2-20, C2-26; PAPER-0581; PAPER-0601.

#### AC-28 - Rectangular Epstein threshold: the real off-line zero appears exactly when an exponentially small sum is positive

**Statement.** By Chowla-Selberg at s = 1/2, Z_{x²+k²y²}(1/2) = 2γ + 2 log(k/(4π)) + 8 Σ_{N≥1} d(N)K₀(2πNk), exactly. Hence:

- the unique solution of ζ₂(1/2, Δ) = 0 on (0, 1), with Δ = 1/k, is Δ*_c = 0.141733239663887191395…;
- it is not e^γ/(4π) = 0.141733239663887191389…, so Betermin-Samaj-Travenec Conjecture 1.1 is false by a relative 4.2·10⁻²⁰;
- real off-line zeros exist for every rectangular form with k > 4πe^{−γ}.

**Status.** A finding of the C2 skeptic (F7), not adjudicated. The "every k > 4πe^{−γ}" part is stated by the skeptic as a THEOREM via the formula and monotonicity in k ≥ 1. This is a side result: Epstein functions matter here only as countermodels.

**Evidence.** At k = 4πe^{−γ} the sum gives 8Σd(N)K₀(…) = 8.3917·10⁻²⁰ > 0. Two independent evaluations agree (the closed form and Riemann's theta integral).

**First test.** An independent ball-arithmetic evaluation of the K₀ sum at k = 4πe^{−γ} and of the root Δ*_c. Locate Bateman-Grosswald (1964), which probably contains the exact threshold equation.

**How it could fail.** A normalisation mismatch between BST's Δ and 1/k. The monotonicity in k must also be checked on the whole range used.

**Sources.** C2 SKEPTIC_REVIEW (F7, C2-12); C2 REPORT (C2-12); PAPER-0826 (Chowla-Selberg).

