# CRIT23: architecture map. "At least 2/3 of zeta zeros are simple and on the critical line" (2026)

```text
Status: EXPLORATORY AUDIT (architecture map + spot checks). No new mathematical claim.
        Nothing here says RH is proved, or that it is closer to proved.
Scope: the asymptotic lower bounds  liminf N0s/N >= 2/3 (flat window) / >= 0.67250... (Montgomery–Taylor
        window) and liminf Nd/N >= 5/6 / >= 0.83625..., as proved in two independent sources, plus
        the refinement layer of Knausgard (0.67353..., 0.83900...). Results about zeta(s) only. Dirichlet-L,
        xi' and family-average extensions are noted but were not audited.
Exact sources or dependencies: see Section 0 (arXiv ids, versions, PDF SHA-256).
What was actually run: full reading of the three main sources; statement check of the imported
        BGSTB24 Lemma 5 against its original; hand re-derivation of the linear-algebra cores;
        numerical recomputation of every headline constant; randomised and optimised adversarial
        tests of the finite inequalities; a numerical check of the Poisson–Gabor identity
        (scripts in ./checks/, outputs quoted in Section 7). No Lean code was built or replayed, and
        no code from the authors' repositories was run.
Smallest remaining gap: (i) the error-term bookkeeping of the prime-side second moment (A-F §5)
        and of BGSTB24 Theorem 1 was read but not re-derived line by line; (ii) Knausgard's three
        branch-and-bound searches (Props 3.3, 5.3, 6.3) were not replayed.
```

## 0. Sources read

| Key | arXiv id (version read) | Pages | PDF SHA-256 | Role |
|---|---|---|---|---|
| **AF** | Alpöge–Furman, arXiv:2608.13637v2 (19 Aug 2026) | 21 | `6de3b156…4ef444` | First proof. Comment: argument "discovered and written by Claude"; Lean claimed. |
| **LZ** | Lamzouri, arXiv:2609.02882v2 (8 Sep 2026) | 17 | `305df7fc…1046b` | Independent human proof ("conceptually simpler"). Proves extra counts. |
| **KN** | Knausgård, arXiv:2610.08965v1 (6 Oct 2026) | 43 | `aedf2891…200f` | Refinement: 0.67353…, 0.83900… (computer-assisted, Lean with three run-axioms). |
| BGSTB24 | Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh, arXiv:2306.04799v1 = Acta Arith. 214 (2024) 357–376 | 13 | `133071c4…6ee9` | LZ imports its Lemma 5. Checked against the original. |
| PRZZ20 | arXiv:1802.10521v3 = Res. Math. Sci. 7 (2020) | 60 | `147187ac…90aa` | Prior record. Checked for the baseline constants. |
| Wu | arXiv:1206.3737v2 = Quart. J. Math. 66 (2015) | 9 | `d25092c0…47e6a5` | Prior distinct-zeros baseline. |

Full hashes are in the observatory fulltext cache (`fulltext/arxiv/<id>/sha256.txt`). PDFs are not redistributed.

## 1. Exact main theorems

Notation (shared): ρ = β + iγ is a nontrivial zero and m_ρ its multiplicity. N counts zeros with multiplicity, N_d counts distinct zeros, N_0^s counts simple zeros with β = 1/2, N_0 counts on-line zeros with multiplicity, N_s counts simple zeros, and N_{s∪0} counts, with multiplicity, zeros that are simple or on the line.

* **AF Theorem A** (p.1, §1.1). As T → ∞, N_0^s(T,2T) ≥ (2/3 − o(1)) N(T,2T) and N_d(T,2T) ≥ (5/6 − o(1)) N(T,2T). With the Montgomery–Taylor (MT) window ψ_MT(s) = cos(√2 s)·1_{[−1/2,1/2]}, the constants become 2 − c_MT^{-1} = 0.67250… and (3 − c_MT^{-1})/2 = 0.83625…, where c_MT^{-1} = 1/2 + (1/√2)cot(1/√2). The same bounds hold for (0,T] (p.2 and Remark 6.1, rate O(log log T / log T)). A fortiori N_0^*, N_0, N_s ≥ (2/3 − o(1))N.
  **AF Theorem B** (p.2). Theorem A holds for L(s,χ) with χ a fixed primitive character. The proof is a sketch on p.12 and was not audited.
  Lean statements (App. A, pp.15–16) include `thmB0_mult`, `thmC0_mult` and `montgomery_taylor_simple_on_critical_line_mult`, all on (T,2T] and cumulative.
* **LZ Theorem 1.1** (p.3), for (0,T]. The bounds are liminf N_0^s/N ≥ C_0 = 3/2 − (1/√2)cot(1/√2) = 0.67250…, liminf N_d/N ≥ C_1 = (C_0+1)/2 = 0.83625…, liminf N_{s∪0}/N ≥ C_2 = (1 + 2√2 + 2C_0)/(3 + 2√2) = 0.88762…, and liminf (N_s + N_0)/(2N) ≥ C_1.
  LZ does not state the flat-window 2/3 and 5/6 explicitly. They follow from the same proof with K = sinc, since C(1_{[−1/2,1/2]}) = 4/3.
* **KN Theorem 1.1** (p.2): liminf N_d/N ≥ 1645064/1960733 = 0.839004…. **Cor. 1.2**: liminf N_s/N ≥ 0.678009…. **Theorem 1.3** (p.3): liminf N_0^s/N ≥ 1669159/2478195 = 0.673538…. **Theorems 1.4–1.5**: (N_s + N_0)/(2N) ≥ 0.836769… and N_{s∪0}/N ≥ 0.889315….

## 2. Proof architecture and dependency structure

All three works use one object. Rescale the zeros to points z_ρ = i(ρ − 1/2)·(log T)/2π. A real point is exactly an on-line zero. The functional equation ρ ↔ 1 − ρ̄ makes the multiset invariant under complex conjugation. Attach to each point the vector f_z(u) = η(u)e^{−2πiuz} in L²(−1/2, 1/2), where η² = f is the window. Then form A = Σ_z m_z f_z⟨f_{z̄}, ·⟩. This operator satisfies:

* tr A = N.
* tr A² = Σ_{z,s} m_z m_s K(z − s)², with K = f̂. Its asymptotic is Montgomery's pair-correlation second moment, which is unconditional for Fourier support [−1, 1].
* On-line zeros contribute PSD rank-one pieces. An off-line pair contributes a block of signature (1,1) and trace 2m.

The two proofs differ only in how they realise A and how they extract the count.

### 2a. Alpöge–Furman (matrix / inertia route)

```
Weil explicit formula (2.1)-(2.2), supp F ⊂ [-log X, log X], X = T/2π
  └─ finite Gabor compression: d ~ N(T,2T) modulated copies φ̂(·-α_k), α_k = T + 2πk/L       §2.2-2.3
       ├─ Lemma 2.1 Poisson–Gabor identity (no aliasing at critical density; trace normalisation) p.5
       ├─ (Z) zero side: G̃ = P + Q; P ⪰ 0 (on-line), off-line pair ↦ 2m(aaᵀ − bbᵀ)            Prop 4.1, Lemma 3.1
       │      tr G̃ = N + o(N) (Prop 4.2); tail ‖Ẽ‖₁ ≪ T^{-1/2} needs the C² taper (Prop 4.3, Rem 4.4)
       ├─ (P) prime side: ‖G̃‖²_HS = (R(ψ)+o(1))N                                            Prop 5.2-5.5, Thm 5.7
       │      Montgomery–Vaughan bilinear Hilbert inequality (Lemma 2.2), Mertens sums (Lemma 5.1)
       │      R(ψ) = (∫ψ² + ∬|u−v|ψψ)/(∫ψ)²; R(ψ0)=4/3, R(ψ_MT)=c_MT^{-1}                     Lemma 5.6
       └─ (L) rank–trace inequality r ≥ 2trP + 4trQ − 4b − ‖P+Q‖²_HS  (von Neumann trace ineq.)  Lemma 3.2
            applied to (P1 = simple on-line part, Q' = rest, n+(Q') ≤ s2+p)                      §6 p.11
            ⇒ N0s ≥ rank P1 ≥ 4trG̃ − 2N − ‖G̃‖² = (2 − R(ψ) − o(1))N;  Nd ≥ ½(3 − R(ψ) − o(1))N
```

### 2b. Lamzouri (Hilbert-space / Bessel route)

```
Prop 2.1 (pure algebra, any finite conjugation-invariant multiset Z, any even real η, supp ⊂ (−λ,λ)) p.6-12
   Σ_{z,s}K(z−s)² = ∬|F(u,v)|², F(u,v) = Σ_z f_z(u)f_z(v)                                   (2.12)
   off-line pair: f_z = g_z + i h_z, g_z ⊥ h_z, ‖g_z‖² − ‖h_z‖² = 1                         (2.11),(2.13)
   flag U ⊂ V ⊂ W (U = span{multiple reals, g_z}; V adds simple reals; W adds h_z)
   real Gram–Schmidt basis ψ_j; α_j = ⟨Aψ_j,ψ_j⟩ real; Bessel Σα_j² ≤ ∬|F|²                  (2.16)-(2.17)
   range bounds: Σ_U α ≥ 2 dim U; Σ_{V∖U} α ≤ n; α_j ≤ 0 on W∖V; Σα = |Z|                   (2.18)-(2.21)
   scalar steps a² ≥ 4a−4, a² ≥ 2a−1, a² ≥ 0 ≥ 2a  ⇒ (2.4) n ≥ 2|Z| − ΣK²; also (2.5)-(2.7)
Lemma 3.1 = BGSTB24 Lemma 5 (imported): Σ r̂(i(ρ−ρ')L/2π) w(ρ−ρ') = (T/2π)logT (r(0)+2∫₀¹αr) + O(1/√logT)  p.12
Lemma 3.2: remove w(u)=4/(4−u²) exactly via r = Q − Q''/(4 log²T), Q = f*f; δ→0 limit gives C_MT  p.13-15
Proof of Thm 1.1: Z_T = {i(ρ−½)logT/2π : 0<γ≤T}, real ⇔ β=½; plug (3.4) into (2.4)-(2.7)          p.15-16
```

### 2c. Knausgård (refinement layer, not an independent proof of 2/3)

KN reuses the LZ/AF operator. It imports BGSTB24 Lemma 5 in Prop 3.1, p.13, and builds on the AF Lean library (ref. [7]). It then adds the following:

* A threshold ("clipping") lemma, Lemma 2.1, p.9, imported from KN's earlier arXiv:2609.33043 and reproved. At c = 2 it contains AF Lemma 3.2.
* A Selberg/large-sieve majorant that bounds the Gram matrix on θ-separated sets (Lemma 2.3, p.10).
* A labelled Gram bound (Thm 2.6) built from pinching (Lemma 2.2), close-pair blocks (Lemma 2.4) and a telescoping "storage function" (Lemma 2.5).
* Computer-assisted 7- and 8-point local inequalities (Props 3.3, 5.3 and 6.3, verified by branch-and-bound).
* Certificate principles: Thm 3.2 gives liminf N_d/N ≥ (3 − C + x₂ − x₁ − b)/(2 − 2x₁ + x₂), and Thm 5.1 gives liminf N_0^s/N ≥ (2 − C − b)/(1 − x).

## 3. Imported results (exact citations; what was checked)

| Input | Used by | Exact citation | Check performed |
|---|---|---|---|
| Unconditional Montgomery form factor and pair sum | LZ (Lemma 3.1), KN (Prop 3.1) | BGSTB24 Lemma 5, eq. (3.4), resting on BGSTB24 Thm 1, eq. (1.4) | **Statement matches verbatim**: real even r ∈ L¹, supp ⊂ [−1,1], Lipschitz at 0, weight w(u) = 4/(4−u²), error O(1/√log T). The BGSTB24 Thm 1 proof uses Landau's explicit formula (Lemma 1), the Goldston–Montgomery asymptotic for R(x,T) (eq. 2.19, [GM87]) and **the Korobov–Vinogradov zero-free region** (eq. 2.18) for √T ≤ x ≤ T. |
| Prime-side second moment (own derivation) | AF §5 | Weil explicit formula [IK04 §5.5]; Montgomery–Vaughan [MV74 Thm 2]; Mertens/Chebyshev [MV07 §2.2] | Read. Main terms re-derived: M[µ,µ] + M[P,P] = (TL³/2π)(∫ψ² + 2∫₀¹w(ψ*ψ)). Error terms read, not re-derived line by line. AF state that no zero-free region, zero-density estimate or mollifier is used; this is consistent with what was read. |
| Montgomery–Taylor extremal window | AF Lemma 5.6, LZ Lemma 3.2 | [Mon75]; optimality [CCLM17, Cor. 14] | Constant recomputed (Section 7). Optimality is **not needed** for the lower bounds. |
| Von Neumann trace inequality; Sylvester inertia | AF Lemmas 3.1–3.2 | standard | Lemma 3.2 re-derived by hand and tested numerically. |
| Bessel inequality and real Gram–Schmidt | LZ Prop 2.1 | standard | Re-derived by hand and tested numerically. |
| Riemann–von Mangoldt; N(t,t+1) ≪ log t | all | [Tit86 Thm 9.2, 9.4] | standard |
| Threshold lemma | KN Lemma 2.1 | KN, arXiv:2609.33043, Lemma 4 | Proof re-read in KN and tested numerically (20k random instances, min slack > 0). |

## 4. The new mechanism relative to prior work

**Answer to "what jumps 5/12 to 2/3".** The 2/3 does not come from Levinson–Conrey mollification, zero-density estimates, derivatives of ζ, or pair-correlation information beyond Fourier support 1. It is Montgomery's 1973 pair-correlation second-moment argument, previously conditional on RH, made unconditional by a linear-algebra replacement for termwise positivity.

1. **Prior state.**
   * The unconditional records came from the mollifier method (Levinson 1974, Conrey 1989, then BCY11, Feng12 and PRZZ20). PRZZ20 gives κ > 0.417293 for zeros on the line and κ* ≥ 0.407511 for simple zeros on the line (arXiv:1802.10521v3, Section 1 text).
   * Under RH, Montgomery got 2/3 simple, and Montgomery–Taylor got 0.6725.
   * Unconditionally, Aryan (2022) and BGSTB24 showed that the *prime side* of Montgomery's second moment, including the sum over all complex zeros, is unconditional.
   * BGSTB25 and Goldston–Suriajaya (GS25, GS26) obtained 2/3 simple-and-critical only under a box hypothesis |β − 1/2| ≪ 1/log T. They identified the remaining obstacle: termwise positivity of K(γ − γ')² fails for off-line pairs.
2. **New step.** Do not read the zero side termwise. Treat the whole second moment as tr A² for the operator A, then use spectral inequalities. Each off-line pair gives a block of signature (1,1) with trace 2m (Sylvester inertia, Bombieri's observation). Eigenvalues are sorted into three sectors:
   * "simple on-line": scalar bound a² ≥ 2a − 1;
   * "positive part of the rest", whose dimension is at most the number of multiple on-line points plus off-line pairs, each carrying trace ≥ 2: scalar bound a² ≥ 4a − 4;
   * "negative part": a² ≥ 0 ≥ 2a.

   This is the matrix form of Montgomery's m² ≥ 2m − 1 together with the Conrey–Ghosh–Gonek refinement m² ≥ 3m − 2. AF package it as the rank–trace inequality (Lemma 3.2). LZ package it as diagonal entries in a flag-adapted real basis plus Bessel (Prop 2.1).
3. **Constants.** The bound is 2 − C(f) and (3 − C(f))/2, where C(f) = ∫f² + ∬|s − t| f(s)f(t) is the second-moment constant. The flat window gives 4/3, so 2/3 and 5/6. The MT window gives 1.32749…, so 0.67250… and 0.83625…. The 2/3 is the RH-conditional Montgomery number itself. It is not an incremental gain over 5/12, which came from a different machine.
4. **Method ceiling.** Using only bandwidth one, AF §7.2 report about 0.682 (Lean, with interval-arithmetic enclosures outside the kernel). KN Cor. 7.9 reports 0.68185, and KN Prop 7.3 reports 0.67383 for its eight-point scheme. Neither is a bound on the zeros.
5. **What it is not** (AF §1.4). It is a lower bound only and says nothing about the remaining third. It is insensitive to o(N) off-line zeros, and Davenport–Heilbronn-type counterexamples have only ≍ T = o(N) off-line zeros, so the result neither implies nor approaches RH.

**Unconditional inputs.** AF uses the Weil explicit formula, Riemann–von Mangoldt, N(t,t+1) ≪ log t, Stirling, Chebyshev–Mertens and Montgomery–Vaughan. LZ uses the same classical inputs through BGSTB24. That chain also contains the Landau explicit formula, the GM87 mean value and the Korobov–Vinogradov zero-free region. Everything is unconditional. No RH, GLH, pair-correlation conjecture or zero-density hypothesis is used in either route.

## 5. Load-bearing steps (numbered), with locations and status

| # | Step | AF location | LZ location | Status in this audit |
|---|---|---|---|---|
| S1 | Encoding plus conjugation symmetry. Zeros map to points or vectors; ρ ↔ 1 − ρ̄ gives the conjugate point or vector; real ⇔ β = 1/2. | §2.2–2.3: γ_ρ = (ρ − ½)/i, v_{1−ρ̄} = v̄_ρ | Thm 1.1 proof, p.15: Z_T | verified |
| S2 | Realise the second moment as a nonnegative quadratic object over the whole multiset. | (2.2), (2.11). Lemma 2.1 (Poisson–Gabor) gives exact trace normalisation Σ_k φ̂(z − α_k)² = aL² for **complex** z. | (2.9), (2.12): Σ K(z−s)² = ∬\|F\|² ≥ 0 | verified (AF Lemma 2.1 checked numerically to 1e−18; LZ (2.12) re-derived) |
| S3 | Block / inertia structure: on-line PSD rank-one with trace m; off-line pair has signature ≤ (1,1) and trace 2m. | Prop 4.1, Lemma 3.1, §6 (n₊(Q′) ≤ s₂ + p) | (2.11), (2.13): ‖g‖² − ‖h‖² = 1, g ⊥ h | verified |
| S4 | **Core inequality** (the new idea). | Lemma 3.2 (rank–trace, von Neumann) | Prop 2.1, (2.16)–(2.25) (flag + Bessel), and (2.5)–(2.7) | verified by hand; 20k random instances plus optimised adversarial search found no violation; equality cases reached |
| S5 | Trace equals N and localisation / tail. | Prop 4.2, Prop 4.3 (C² taper needed, Rem 4.4) | trivial: tr = \|Z_T\| (2.21), because BGSTB24 sums over exactly 0 < γ, γ′ ≤ T | verified (AF: see finding F7, harmless) |
| S6 | **Unconditional second moment**, Fourier support [−1,1], X ≤ T. | Props 5.2–5.5, Thm 5.7 (own proof via Montgomery–Vaughan) | Lemma 3.1 = BGSTB24 Lemma 5 (imported) | statement match verified; main terms re-derived; error terms read, not fully re-derived |
| S7 | Weight removal: w(ρ−ρ′) = 4/(4−(ρ−ρ′)²). | not needed (Weil form has no weight) | Lemma 3.2, (3.2)–(3.3): r̂ = (1 + π²z²/log²T)K² | verified (sign and normalisation checked) |
| S8 | Window optimisation: C(f) = ∫f² + ∬\|s−t\|ff. | Lemma 5.6 | Lemma 3.2, Rem 3.4 | recomputed to 30 digits (Section 7) |
| S9 | Counting bookkeeping. | §6: tr P₁ ≤ s₁, s₁ + 2s₂ + 2p ≤ N ⇒ (1.2); (ii): 2(s₁+s₂+p) ≥ (3−R)N | Thm 1.1 proof: N_0^s ≥ 2N − Σ, N_d ≥ (3N − Σ)/2, etc. | verified |
| S10 | (KN only) Clipping lemma; separated-set majorant; transfer; computer-assisted local inequality; certificate principle. | — | — | Lemma 2.1 tested; Λ, β, f ≤ g margins, C(f) and all final rationals recomputed. **Branch-and-bound searches not replayed** (Lean `native_decide` axioms, trusted compiler). |

The smallest statement whose failure would invalidate the result is S4 combined with S6. S4 is the inertia/Bessel inequality, which is elementary and checked here. S6 is the unconditional evaluation Σ K(i(ρ−ρ′)L/2π)² ~ C(f)·N over *all* zeros, which is imported from refereed BGSTB24 in LZ and proved independently in AF §5.

## 6. Step-by-step comparison of the two proofs; shared lemmas

| Step | AF | LZ | Shared? |
|---|---|---|---|
| Ambient space | finite d-dim Gabor compression (Weil form restricted to d ≈ N test functions) | L²(−1/2, 1/2); span W of ≤ N exponentials | Same operator; different coordinates. |
| Second-moment source | Weil explicit formula plus own prime-side evaluation (§5) | BGSTB24 Lemma 5 (Landau explicit formula, GM87, KV zero-free region) | **Independent derivations** of the same classical theorem. No common unverified lemma. |
| Weight w(u) | absent | removed exactly (Lemma 3.2) | — |
| Localisation | (T,2T] with √T margin, C² taper, tail ≪ T^{-1/2} | none needed (cumulative 0 < γ ≤ T) | — |
| Linear algebra | von Neumann trace inequality, Sylvester inertia | Gram–Schmidt in a real (J-fixed) structure, Bessel | **Independent proofs** of equivalent inequalities. |
| Optimisation | MT window, R(ψ) | MT window, C_δ → C_MT | classical constant (verified) |
| Formalisation | Lean: claims no hypotheses, three standard axioms (not replayed) | AxiomProver Lean: Prop 2.1 unconditional; Thm 1.1 **assumes** BGSTB24 Lemma 5 and Riemann–von Mangoldt as hypotheses (LZ App. A) | KN Lean builds on the AF library. |

**Verdict on shared unverified lemmas.** None were found. The two proofs share only classical, refereed inputs: the explicit formula, Riemann–von Mangoldt, the Montgomery–Vaughan / GM87 mean-value machinery and the MT constant. LZ's analytic input BGSTB24 (Acta Arith. 2024) predates AF and was refereed. LZ is an independent *verification* of the AF mechanism, written after reading AF, rather than an independent discovery.

KN is not independent of either. It imports BGSTB24 Lemma 5, as LZ does, and its formalisation extends the AF Lean library.

## 7. Numerical recomputations (scripts in `./checks/`, Python with mpmath, sympy, numpy and scipy)

| Quantity | Stated | Recomputed | Script |
|---|---|---|---|
| C_MT = 1/2 + cot(1/√2)/√2 | 1.3274992963205 (LZ 3.1) | 1.32749929632058835427 | constants.py |
| 2 − C_MT | 0.67250 | 0.67250070367941164573 | constants.py |
| (3 − C_MT)/2 | 0.83625 | 0.83625035183970582287 | constants.py |
| LZ C₂ (both stated forms) | 0.88762 | 0.88762000817335433987 | constants.py |
| BGSTB25 box value (2 + C₀)/3 (quoted by LZ) | 0.89083 | 0.89083356789313721524 | constants.py |
| AF Lean form c_MT = √2·tan(1/√2)/(1 + tan(1/√2)/√2) | 1/c_MT = C_MT | identical to 20 digits | constants.py |
| R(ψ₀) by quadrature | 4/3 | 1.333333333333333333333333 | rpsi.py |
| R(ψ_MT) by quadrature (AF 5.13) | c_MT^{-1} | equal to 2e−31 | rpsi.py |
| MT stationarity: G(u) = ψ + ∫\|u−v\|ψ constant | yes | 1.21960728200841 at u = 0, 0.2, 0.45 | constants.py |
| AF Rem 6.1: H(λ) = 2 − 1/λ − λ/3 | max on λ ≤ 1 at λ = 1, value 2/3 | H(1) = 2/3, H(0.9) = 0.589 | constants.py |
| AF §7.2(f): Christoffel Λ₂(0) for moments 1, 1, 4/3, 2, 13/4 | 5/36 ⇒ 13/18 | 5/36 ⇒ 13/18 (exact) | constants.py |
| KN C(f), windows 1, 2, 3 | 1.3327049582, 1.32794727, 1.33246363 | 1.33270495828, 1.32794727284, 1.33246363317 | knausgard.py |
| KN min K² on [0, 17/20], windows 1, 2, 3 | ≥ 0.06574, 0.05106, 0.06680 | 0.0657992, 0.0510858, 0.0668293 (grid) | knausgard.py |
| KN Λ = (2γ₀/θ)(1 + sinc θ) | 1.67105, 1.78942, 1.67931 | 1.6710515, 1.7894292, 1.6793104 | knausgard.py |
| KN f ≤ g margin, windows 1, 2, 3 | ≥ 1e−4 | 5.0e−4, 5.2e−2, 2.0e−3 (grid) | knausgard2.py |
| KN q, 2q − 1, s₀, (1 + s₀)/2, Thm 1.4b, Thm 1.5 | 1645064/1960733, … | all six rationals reproduced **exactly** from the stated certificates; μ, ν, r_h, r_k = 1.960733, 3.684917, 1.792984, 0.0688 | knausgard.py, knausgard2.py |
| AF Lemma 3.2 random (20k) | r − RHS ≥ 0 | min slack 0.0397; equality case slack 0 | linalg_tests.py |
| KN Lemma 2.1 random (20k) | ≥ 0 | min slack 5.6e−4 | linalg_tests.py |
| LZ (2.4)–(2.7), random conjugation-invariant multisets with multiplicities (4k, flat kernel) | ≥ 0 | min slack 0.0 (equality cases); Σ K² real (relative imaginary part ≤ 2e−16) and ≥ 0 | linalg_tests.py |
| LZ (2.4), (2.5), Nelder–Mead adversarial (MT and flat kernels) | ≥ 0 | min −1.8e−15 (rounding at equality) | adversarial.py |
| AF Lemma 2.1 Poisson–Gabor at complex z, z′ | exact identity | \|diff\| ≤ 1.5e−18 (lattice truncation) | gabor.py |

## 8. Findings

| ID | Class | Finding |
|---|---|---|
| F1 | typo_or_presentation (witness) | The AF abstract and §1.1 (p.2) give "5/12 for N_0^s/N [PRZZ20]" as the previous record. PRZZ20 (arXiv:1802.10521v3, Section 1, text lines 592–593 and the final optimisation) gives κ > 0.417293 for *critical* zeros and κ* ≥ 0.407511 for *simple* critical zeros. LZ (p.2) and KN (p.2) quote 0.4075 correctly. This is a comparison baseline only and is not load-bearing. |
| F2 | unresolved_ambiguity | Previous distinct-zeros record. AF cite 0.6603 [Wu15], which matches Wu arXiv:1206.3737 (66.036%). LZ (p.2) and KN (p.2) cite Ki–Lee, Funct. Approx. 47 (2012), Thm 5, as > 70%. Ki–Lee was not inspected. Not load-bearing. |
| F3 | typo_or_presentation | AF (2.1) is stated "for F ∈ C_c²(R) even", but (2.2) and (2.11) are applied to the non-even F̂(τ) = φ̂(τ − α_k)φ̂(τ − α_k′). This is harmless: the zero multiset is symmetric under γ_ρ ↦ −γ_ρ (ρ ↦ 1 − ρ) and ν_X is even, so both sides depend only on the even part of F. The extension is valid but not spelled out. |
| F4 | no_issue_found (input-set note) | "No … zero-free region is used" (AF p.2) is true of AF's own route. LZ's route imports BGSTB24, whose Thm 1 proof uses the Korobov–Vinogradov region (BGSTB24 eq. 2.18, needed for √T ≤ x ≤ T). Both routes are unconditional, but their input sets differ. |
| F5 | missing_hypothesis (formal scope) | LZ's Lean certificate (App. A) proves Theorem 1.1 *assuming* BGSTB24 Lemma 5 and Riemann–von Mangoldt, so the analytic input is not formalised there. AF claim a hypothesis-free Lean proof (three standard axioms). KN adds three `native_decide` run-axioms. **None was replayed here.** The AF paper cites `github.com/anthropics/zeta-23-lean` tag v1.0, while KN cites `github.com/anthropics/formal-math` commit fbdc36b. The relation between the two was not checked. |
| F6 | unresolved_ambiguity (out of CRIT23 scope) | AF Theorem B (Dirichlet L) is a one-paragraph sketch. AF Remark 7.2 (family average 0.811 / 0.905) has "details … omitted" and is not in Lean. AF Remark 7.1 (ξ′: 0.85838) was not recomputed. None of these is part of the CRIT23 claim. |
| F7 | typo_or_presentation (minor) | In the proof of AF Prop 4.2 the displayed bound "≪ L min(L³, D_ρ^{-3})" gives √X·L³ for the O(L) zeros with D_ρ < 1, not the stated √X·L². The stated bound follows from the sharper |φ̂(z)| ≪ e^{L\|Im z\|/2} min(L, \|z\|^{-1}, \|z\|^{-2}) of (2.8). Either way the term is o(N), so there is no effect on the theorem. |
| F8 | no_issue_found_in_inspected_portion | AF Lemma 3.2, Props 4.1 and 4.3, Lemma 5.6 and §6 chain; LZ Prop 2.1 (all of (2.4)–(2.7), including the t = 2 + √2 balancing), Lemma 3.2 and the Thm 1.1 proof; LZ Lemma 3.1 equals BGSTB24 Lemma 5 verbatim; KN Lemma 2.1, Thm 3.2, Thm 5.1 and Thm 6.2 arithmetic. No verified error was found in any of these. |

## 9. Not done / boundaries

* The full error analysis of AF §5 (Props 5.2–5.5) and of BGSTB24 Thm 1 (Lemmas 1–4) was not re-derived line by line.
* No Lean development (AF, LZ/AxiomProver, KN) was built or kernel-checked. KN's branch-and-bound searches (60.5M, 535M and 573M boxes) were not replayed.
* Unrefereed 2026 follow-ups named in KN (Freund, D'Souza, Chandru, Wang and others) were not inspected.
* The theorems are asymptotic lim inf lower bounds for proportions. They are not finite verifications and carry no information about the remaining ≤ 1/3 of zeros.
