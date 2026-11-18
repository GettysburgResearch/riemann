# Cross-field transplantation opportunities

```text
Status: SYNTHESIS of transplantation opportunities (exploration layer). Each is a proposal, not a result.
        RH is open.
Scope: tools from adjacent mathematics, family H and family F of methodology.md Sec. 2, and from the 2026
       machinery, each matched to a named RH obstacle.
Exact sources or dependencies: discovery items M3 (CON-0011..0015) and M5 (CON-0021..0024); the bridge's
       transplantable tools (BRG-*-T*: 49 analyst proposals, not individually graded; programme verifiers
       spot-checked some); campaigns C4 and C5 (REPORT with SKEPTIC_REVIEW); quasi-RH DOSSIER Sec. 4;
       CRIT23 DOSSIER Sec. 7-8; SIEGEL DOSSIER Sec. 7-8; research_programs.md.
What was actually run: reading and cross-matching only. No new computation.
Smallest remaining gap: no opportunity has been attempted beyond what its source record reports.
```

## 0. Conventions

- **Status labels and 2026 names** are as in strongest_connections.md Sec. 0.
- **Families** (methodology.md Sec. 2):
  - **H**, adjacent mathematics: the polynomial method, total positivity, Pick/Loewner theory, prolate functions, SDP, Fourier extremal problems, certified numerics, metaplectic forms;
  - **F**, dynamical and alternative: Jensen/Laguerre–Pólya, heat flows, Beurling primes, Euler-product truncations.
- **Tiers.**
  - Tier 1: the hypothesis matching has been checked by a verifier, and the first step produces a checkable output.
  - Tier 2: the matching is partial, or the output is diagnostic.
  - Tier 3: conceptual, high risk.

## 1. Summary

| # | Tier | Obstacle | Tool | IDs |
|---|---|---|---|---|
| O1 | 1 | individual GL(2) zeros | rank–trace certificate | CON-0035, CON-0011 |
| O2 | 1 | GL(2) family proportions | Petersson formula | CON-0036, CON-0012 |
| O3 | 1 | locality of Weil windows | finite-rank inertia (C5) and the detection criterion (C4) | C5 skeptic Sec. 3; C4-B, C4-C |
| O4 | 1 | lower certificates for windows | verified eigenvalue bounds | BRG-OPERATORS_HEAT-T1, T5 |
| O5 | 1 | RH-free discrete moments | off-line pair defect | CON-0006 |
| O6 | 1 | QRH frontier | Beurling perturbation | CON-0032 |
| O7 | 1 | graded criteria | Littlewood–Beurling exponent and Lagarias–Suzuki innerness | CON-0021, CON-0007 |
| O8 | 1 | ξ′ beyond Wu | Knausgård certificate principle | CON-0015 |
| O9 | 2 | metaplectic floor | quartic Kubota theta | CON-0038, CON-0014 |
| O10 | 2 | infinite-order Hecke characters | angular bookkeeping | CON-0037 |
| O11 | 2 | unbounded window families | ACL monotone slack and prolate conditioning | BRG-OPERATORS_HEAT-T2, T3 |
| O12 | 2 | de Bruijn–Newman converse | zero energy flow and universal factors | CON-0008, CON-0024 |
| O13 | 2 | coefficient routes | total positivity | CON-0033 |
| O14 | 2 | pointwise sign premises | lattice reduction | BRG-SHARP_NATIVE-T4, BRG-MELLIN_WAVELET-T3 |
| O15 | 2 | Pick hierarchy | height-to-order calibration | BRG-XI_PICK-T1–T4 |
| O16 | 2 | Siegel ceilings | polynomial method | SIEGEL Sec. 8 |
| O17 | 2 | causal Euler correction | smooth-number transforms | BRG-CAUSAL_EULER-T1, T2 |
| O18 | 2 | Robin certificates | CA interpolation | BRG-ROBIN-T1, T2 |
| O19 | 3 | comb envelope | linear forms in logarithms | research_programs POS (a) |
| O20 | 3 | bandwidth ceiling | SDP | CRIT23 Sec. 8 item 7 |
| O21 | 3 | principal member | Deligne, ILS, Kowalski–Michel | BRG-FAMILIES-T2–T4; C5-D1 |
| O22 | 3 | Weil-route effectivity | Riemann–Roch on the scaling site | C5 open targets ML-W0, ML-Den, ML-TP, ML-F1 |
| O23 | 3 | one-sided ψ bounds | integer Chebyshev polynomials | C5-ML-S; C5 skeptic Sec. 3.4 |
| O24 | 3 | SHARP Bellman block | Friedlander–Iwaniec Type II | BRG-SHARP_NATIVE-T7 |

## 2. Tier 1

### O1. Rank–trace certificate (2026) → individual GL(2) zeros
- **Obstacle.** For an individual GL(2) L-function no positive proportion of simple zeros is known, and only 6.96% of zeros are known to be critical (LED-CRIT-19).
- **Tool.** The AF/LZ certificate [AI-generated / unrefereed].
- **Matching.**
  - The bandwidth 1/2 equals the Murty–Perelli range.
  - Simple zeros fail: λ* = 0.5502.
  - Distinct zeros work: 1/R*(1/2) = 0.4617.
- **First step.** Prove the GL(2) second-moment lemma.
- **Risk.** Medium. Simple zeros are out of reach within the window class.

### O2. Petersson formula → GL(2) family averages
- **Obstacle.** No proportion of simple or distinct GL(2) zeros is known on family average.
- **Tool.** Hua–Yang [unrefereed] and ILS PAPER-0019.
- **Matching.** Needs an explicit diagonal lemma, a zero-density deletion, and a Gevrey tail. The Weil-bound fallback gives 0.4191 / 0.7095 at k = 2.
- **First step.** Prove the diagonal lemma using the additive large sieve.
- **Risk.** A family average is not a statement about members.

### O3. Finite-rank inertia (C5) and the detection criterion (C4) → window locality for abstract zero multisets
- **Obstacle.**
  - Over Q no mechanism makes the Weil form on a single window decide anything about zeros.
  - The window margin collapses like exp(−c e^{2L}).
  - The Nyquist heuristic of the C4 brief was refuted.
- **Tool.**
  - (i) [theorem; C5 skeptic Sec. 3.1] Inertia(T_N) = (r−m, m, N−r). Hence RH holds iff T_{2g} ⪰ 0, without assuming P is squarefree.
  - (ii) [proposition, proof sketch] RH(C) holds iff W ≥ 0 for any one a > (g − 1/2) log q.
  - (iii) Bombieri 2000 (PAPER-0090), Thm 8 [theorem].
  - (iv) C4-C [theorem].
  - (v) C4-B [theorem, conditional on H1]: L* ≤ (1/(2δ))(log log T + ...).
- **Matching.**
  - Finite rank is exactly what fails for ζ.
  - 'No finite window suffices over Q' is not a theorem; the coherent target is model-theoretic.
- **First step.** Prove a blindness lemma for abstract zero multisets, via hypothesis R, with interval arithmetic. Separately, remove the factor (1 + 1.41L) from C4-B.
- **Risk.** High for blindness: the collision model detects defects 0.42–0.85 below Nyquist. Low for the C4-B improvement.

### O4. Certified eigenvalue enclosures → lower certificates for Weil windows
- **Obstacle.**
  - Zhu reports λ*(0.8) ≥ 8.9·10⁻¹⁸ [unrefereed; high precision with an error budget, not directed rounding].
  - No independent replay exists.
  - The host's single-window certificate at L = 1 is open.
- **Tools.**
  - Zhu's one-stroke reduction [unrefereed].
  - Temple–Kato, Lehmann–Goerisch and Plum lower bounds [theorem-level methods].
  - Arb ball arithmetic.
- **Matching.** Zhu's λ* is taken over even f. The C4-P values are upper bounds only.
- **First step.** A directed-rounding replay at L = 0.8, then the host's form at L = 1.
- **Risk.** The precision needed grows like e^{2L}. A finite window is never evidence for RH.

### O5. Off-line pair defect → RH-free discrete moments
- **Obstacle.** CRIT bottleneck (c).
- **Tool.** CON-0006: inequality (*) and theorem (b).
- **First step.** Find the largest η admissible from Conrey's '99.9% within 8/L'.
- **Risk.** The hypothesis δ = o(L^{−3/2}) goes far beyond known density results.

### O6. Beurling perturbations (F) → the QRH frontier
- **Obstacle.** Can integer regularity β < 1/2 force QRH-type regions?
- **Tool.** The BDR construction.
- **First step.** Extend it to α ≥ 2/3; define the function A(β).
- **Risk.** The Hilberdink–BDR conjecture may fail.

### O7. Hardy-space rates and Lagarias–Suzuki innerness → graded criteria
- **Obstacle.** Converting rates or positivity at level ω into half-planes. Host nodes: the MELLIN graded premise and L-91035.
- **Tools.**
  - CON-0021 [Observatory-proposed].
  - Dimitrov–Oliveira.
  - Suzuki Thm 11.1.
  - Lagarias–Suzuki [theorem]: ζ ≠ 0 on Re s > 1/2 + ω₀ iff Θ_ω is meromorphic inner for every ω > ω₀.
- **Matching.** All of these are two-sided equivalences. Under QRH-7/8, the range of L-91035 extends to a > 3/8 [conditional].
- **First step.** Write the proof of CON-0021.
- **Risk.** These are converters only.

### O8. Knausgård certificate principle (H) → zeros of ξ′
- **Obstacle.** Beating Wu's 0.86957.
- **Tool.** Knausgård Thm 5.1 [unrefereed].
- **First step.** An ξ′ ceiling LP.
- **Risk.** The local statistics of ξ′ zeros are not GUE.

## 3. Tier 2

### O9. Quartic metaplectic theta → an independent 7/8
- **Obstacle.** The order-6 floor of 11/12, and the floor of 2/3 for the 7/8 system.
- **Tool.** Kubota theta series. Explicit coefficients are known only for n = 2, 3.
- **Matching.** Needs the quartic mean square (C2)/J4. No μ-removal identity is known for n = 4.
- **First step.** Numerics at X ≈ 2000, H ≈ X^{1.05}; a test of μ-removal.
- **Risk.** High, from Patterson-type bias.

### O10. Angular bookkeeping → infinite-order Hecke characters
- **Obstacle.** Scope (DOSSIER Sec. 2.6).
- **Tool.** The paper2 machinery.
- **First step.** Derive J_m for m = −2.
- **Risk.** A main term at m = 0. Entirely conditional on unrefereed inputs.

### O11. Monotone slack and prolate conditioning (ACL) → unbounded families of windows
- **Obstacle.** The coercive codimension K grows doubly exponentially in L.
- **Tools.** ACL Prop. 8.17 and Thm 8.14 [unrefereed].
- **Matching.** Needs a monotone Rayleigh quotient. ACL's hypothesis (H2′) is open.
- **First step.** Verify monotonicity for the host's form.
- **Risk.** The reformulation is RH-equivalent.

### O12. Zero energy flow and universal factors (F) → the de Bruijn–Newman converse
- **Tools.** The Polymath zero ODE; de Bruijn Thm 8.
- **First step.** CON-0008 (energy proof); CON-0024 (strip width).
- **Risk.** Informative only below γ ≈ 10^4.

### O13. Total positivity → closing coefficient-inequality routes
- **Tools.** McNamara–Sagan; Liu–Mao.
- **First step.** Liu–Mao Sec. 3 at t = −t₀.
- **Risk.** The output is a no-go theorem.

### O14. Lattice reduction → refuting sign premises
- **Obstacle.** Eventual sign of H^{[1]}, whose bias is 1.80332.
- **Tools.** Haselgrove PAPER-0489; Hurst PAPER-0585; Ingham PAPER-0071.
- **First step.** Certified coefficients plus an LLL search.
- **Risk.** Feasibility is borderline. The premise refuted is one the host does not claim.

### O15. Height-to-order calibration → the host's Pick hierarchy
- **Tools.** Audenaert [theorem]; Heinavaara [theorem]; Sra [unrefereed].
- **First step.** Compute N(b) for the X9 model, b = 2^k up to 2^{12}.
- **Risk.** Diagnostic only.

### O16. Polynomial method → Siegel constants
- **Obstacle.** The floor κ ≥ 1/2, and the ceiling 3 − 2√2 = 0.1716.
- **Tool.** OAI PAPER-0529; Guo [unrefereed].
- **First step.** Insert the Pólya–Vinogradov bound into Guo Prop. 4.1; extend to Hecke characters.
- **Risk.** Payoff in constants only. The method does not see complex zeros.

### O17. Smooth-number transforms → the host's causal Euler correction
- **Tools.** Hildebrand–Tenenbaum Lemma 3.4 [theorem], with region 1 − (log y)^{−2/5−ε} ≤ σ; Gorodetsky.
- **First step.** A moving-region version of DC5.
- **Risk.** No leverage on RH.

### O18. CA interpolation → the host's Robin certificates
- **Tools.** Robin; Briggs; Akbary–Friggstad.
- **First step.** CA enumeration in directed arithmetic.
- **Risk.** A finite range only.

## 4. Tier 3

### O19. Linear forms in logarithms → the comb envelope
- **Obstacle.** Zhu's resolution requirement T₁ = 2πe^{A_L}.
- **Tool.** Baker–Wüstholz. Not checked by any Observatory agent.
- **Matching.** Kronecker's theorem limits the possible gain.
- **First step.** Quantify the height at which near-alignment is possible.
- **Risk.** High.

### O20. SDP → beyond the bandwidth ceiling
- **Tools.** Chirre–Gonçalves–de Laat PAPER-0073 [conditional on RH]; BGSTB24 PAPER-0053.
- **Matching.** The sign goes the wrong way. The rank bound needs only a Hermitian matrix.
- **First step.** An inertia-compatible LP.
- **Risk.** High.

### O21. Deligne, ILS and Kowalski–Michel → extracting the principal member
- **Tools.** Weil I PAPER-0496 [theorem]; ILS; Kowalski–Michel.
- **Matching.** Fails at the known points. C5-D1: the tensor-power trick is equivalent to RH.
- **First step.** The open slot of T4.
- **Risk.** A no-go result is likely.

### O22. Riemann–Roch on the scaling site → Weil-route effectivity
- **Targets.** C5 targets ML-W0, ML-Den, ML-TP and ML-F1.
- **Risk.** Very high: there is no intersection theory yet.

### O23. Integer Chebyshev polynomials → one-sided bounds on ψ
- **Tools.** Gelfond–Schnirelman; Pritsker. The integer Chebyshev constant satisfies t_Z ∈ [0.4222286, 0.4226847], which is > 1/e.
- **First step.** Search for weight sequences w_n with B(w_n) → 1.
- **Risk.** Very high.

### O24. Friedlander–Iwaniec Type II → the SHARP Bellman block
- **Tool.** Friedlander–Iwaniec, Ann. Math. 148 (1998).
- **First step.** State a native version of hypothesis (B).
- **Risk.** It gives only log-power savings.

## 5. Transplants already shown not to work

- Generic sextic large sieves (DOSSIER C4).
- Mollified moments plus extraction (CON-0031); mollifier length θ = 1 gives only 0.6107 (LED-CRIT-8).
- Higher traces at X ≍ T (CRIT23 Sec. 7.4).
- Jensen polynomials and universality (PAPER-0686; BRG-XI_PICK-O3; FND-0002).
- The Landau–Pintz method (BRG-MELLIN_WAVELET-O6).
- Pretentious methods (BRG-SHARP_NATIVE-O5).
- Sieve axioms alone (parity).
- Positive-weight systems: Beurling primes PAPER-0581 and PAPER-0619; Davenport–Heilbronn PAPER-0417.
- De Branges's positivity conditions (PAPER-0779; FND-0013).
- Fixed-P producers (BRG-OPERATORS_HEAT-T8).
- Deligne's positivity engine gives Ramanujan, not RH (C5-OB7).
- The formal zeta axioms over F_q: 12,801 fakes (C5-E1).
- Weil windows via pointwise envelopes.
- The Siegel polynomial method for complex zeros (SIEGEL Sec. 7.4).
- Finite verification as global evidence.

## 6. Dependence on unrefereed 2026 inputs

| Opportunity | Unrefereed 2026 input needed |
|---|---|
| O1, O2, O8 | CRIT-2/3 (and Hua–Yang for O2; Knausgård for O8) |
| O3, O4, O11, O19 | Zhu and ACL (for calibration only) |
| O5, O6, O12–O15, O17, O18, O21–O24 | none for the first step |
| O7 | QRH-7/8, for the ω = 3/8 corollaries only |
| O9, O10 | the paper2 machinery |
| O16 | SIEGEL |
| O20 | none |

