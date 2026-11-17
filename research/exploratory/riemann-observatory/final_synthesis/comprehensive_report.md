# Comprehensive report: answers to the ten synthesis questions

```text
Status: SYNTHESIS (exploration layer, Riemann Observatory). It answers the ten synthesis questions of the
        brief from the archive's adjudicated and verified records. It is not a review approval and not an
        integrated packet. It makes no claim about RH or its negation: RH is open. Every mathematical
        statement carries a status label and an archive reference.
        The 2026 claims are unrefereed:
        - OpenAI quasi-RH 11/12: human-edited. The Observatory's Level-2 audit found no error in the inspected
          portions (FND-0009); the imported inputs were not re-proved.
        - OpenAI quasi-RH 7/8: not audited by us. Lean is claimed and was not replayed.
        - Alpoge-Furman, at least 2/3 of zeros simple and on the critical line: one proof step was repaired
          (FND-0004); Lamzouri gave an independent proof; not refereed.
        - Landau-Siegel exclusion: OpenAI plus human re-proofs (FND-0010); not refereed.
        "THEOREM" below means one of the campaigns' small theorems, with a complete proof re-derived by an
        AI skeptic and an AI adjudicator. It does not mean a literature theorem, and no human has reviewed it.
Scope: the whole archive as of the search cutoff 2026-11-17: the corpus (1,000 works, 154 read at L1), the
        frontier ledger (232 records), the audits (FND-0001 to FND-0014), campaigns C1-C5, the discovery
        register (CON-0001 to CON-0039), the repository bridge (215 BRG items), and the history and quality
        files. Classical zeta unless stated otherwise.
Exact sources or dependencies, in order of precedence:
        (1) proposals/independent_campaigns/C1..C5/FINAL.md. These are authoritative over REPORT.md,
            SKEPTIC_REVIEW.md and every earlier synthesis.
        (2) audits/findings.jsonl, verified_findings.md, unresolved_findings.md, quasi_rh/DOSSIER.md,
            claims_2026/CRIT23/DOSSIER.md, claims_2026/SIEGEL/DOSSIER.md, L2_flag_audits/F1-F8.
        (3) frontiers/records_ledger.md and ledger.jsonl (verifier-corrected values);
            frontiers/research_programs.md.
        (4) connections/connections_register.md, connections.jsonl (verdicts), strongest_connections.md,
            repository_bridge.md, cross_field_opportunities.md.
        (5) frontiers/missing_lemmas.md, known_obstructions.md, unsolved_questions.md;
            proposals/ranked_research_directions.md and actionable_conjectures.md. These were written before
            the C2, C4 and C5 adjudications; where they conflict with a FINAL.md, the FINAL.md wins (Sec. 8.4).
        (6) history/*.md. (7) quality/*.md; corpus/bibliography.jsonl (PAPER ids); methodology.md.
What was actually run: reading of the files above, plus short python3 extractions from findings.jsonl,
        ledger.jsonl, connections.jsonl and bibliography.jsonl to tabulate ids, verdicts, corrected values
        and PAPER ids. No new mathematics, no recomputation, no Lean build, and no third-party code was run.
Smallest remaining gap: no human expert has reviewed any item of this archive. The verification gates
        UQ-A1 to UQ-A9 (Lean replays, a human check of the 11/12 imports, the 7/8 audit, the Siegel version of
        record, the residues of the 2/3 audit) bound the status of everything that cites the 2026 claims.
        The single statement whose failure would most change this report is Proposition 3.1 of the 11/12
        paper (QRH-D Sec. 2.5: "all the risk sits there"), whose proof rests on Prop. 6.2 plus Lemma 6.3 in the form used by Lemma 6.6, together with the imported Patterson-Kubota inputs
        (QRH-D Sec. 1.2). Among the archive's own results, the load-bearing inputs are:
        - Trudgian's S(t) bound, for C4-B and everything derived from it (read at L0+ only);
        - the Chowla-Selberg constant term, for C2-ADJ-2;
        - Broucke-Debruyne-Revesz Theorem 1.3, for CON-0032 T1.
```

## 0. Reading guide

**Abbreviations.**
- C1F to C5F: `proposals/independent_campaigns/<campaign>/FINAL.md`.
- QRH-D: `audits/quasi_rh/DOSSIER.md`.
- CRIT23-D and SIEGEL-D: `audits/claims_2026/CRIT23/DOSSIER.md` and `audits/claims_2026/SIEGEL/DOSSIER.md`.
- FND: `audits/findings.jsonl`, rendered in `verified_findings.md` and `unresolved_findings.md`.
- LED: `frontiers/ledger.jsonl`, using verifier-corrected values.
- CON: `connections/connections_register.md`. BRG: `connections/repository_bridge.md`.
- OB: `frontiers/known_obstructions.md`. UQ-x: an item of `frontiers/unsolved_questions.md`.
- D-xx and AC-xx: `proposals/ranked_research_directions.md` and `proposals/actionable_conjectures.md`.
- EVO, TL, ABN and RD: `history/evolution_of_methods.md`, `chronological_timeline.md`, `abandoned_approaches.md` and `recent_developments_2024_2026.md`.

**Status labels.**

| Label | Meaning |
|---|---|
| THEOREM | Observatory campaign theorem, adjudicated; complete proof in the FINAL file or its REPORT; AI-reviewed only |
| [T] | Published literature theorem (refereed or classical) |
| [T-U] | Unrefereed human preprint |
| [AI-U] | AI-generated or AI-discovered, unrefereed |
| IMPORTED | Literature statement used as an input, at the evidence level stated in the source record |
| [O] | Observatory-proposed (discovery register or dossier sketch), checked by one verifier, not adjudicated |
| CONDITIONAL | Proved under an explicit hypothesis |
| NUMERICAL-RIGOROUS | Arb ball arithmetic or exact integers, modulo FLINT/Arb correctness |
| NUMERICAL-NONRIGOROUS | Floating point or mpmath high precision |
| HEURISTIC, CONJECTURE, PPS | Heuristic; open statement; proposition with proof sketch |
| REFUTED, WITHDRAWN | Shown false with a witness; retracted by the adjudicator |

**The 2026 inputs at a glance.**

| Claim | Exact content | Status | References |
|---|---|---|---|
| QRH-11/12 | Every finite-order Hecke L over Q(sqrt(-3)), hence every Dirichlet L and zeta, is zero-free on Re s > 11/12 | [AI-U], human-edited. Level-2 audit by section: no error found in the inspected portions; the Patterson/Kubota (via Dunn-Radziwill) and Goldmakher-Louvel imports were not re-proved | PAPER-0161; LED-ZFR-2; FND-0009; QRH-D Sec. 1 |
| QRH-7/8 | The same with 7/8; 199 pp. | [AI-U]. Not audited by us. Lean claimed, not replayed | PAPER-0528; LED-ZFR-1; unresolved_findings |
| Below 7/8 | Best claimed exponent B_tw = 0.8740585... (Liu, hexagon:2610.00655v3) | [T-U]. Every such exponent imports the 7/8 paper's analytic inputs | LED-ZFR-3 (verifier correction); QRH-D Sec. 1.5 |
| Two thirds | liminf N_0^s/N >= 2/3; >= 0.6725007 with the Montgomery-Taylor window; distinct >= 5/6 | [AI-U] (discovered and written by Claude; verified by the human authors) plus an independent human proof [T-U]. One proof step repaired (FND-0004). Not refereed; Lean not replayed | PAPER-0486, PAPER-0533; LED-CRIT-1, -2; CRIT23-D |
| Knausgard | 0.67353820 (simple and critical), 0.83900460 (distinct) | [T-U]. Rests in addition on three unreplayed computer searches | PAPER-0166; LED-CRIT-3 |
| Siegel exclusion | There is an absolute c > 0 with (1 - beta) log q >= c for every real zero of a primitive real L(s, chi). Best claimed explicit all-q constant c = 1/64 (Guo, App. A) | [AI-U] plus three human-signed, AI-assisted re-proofs (Banks, Kerr, Guo) [T-U]; four proofs with three structurally independent cores. No issue found; Lean not replayed | PAPER-0529, -0160, -0164, -0165; LED-LFUN-6 (corrected); FND-0010; SIEGEL-D |
| Guth-Maynard | sup A(sigma) <= 30/13; primes in [x, x + x^(17/30+eps)] | [T], Ann. of Math. 2026 | PAPER-0054; LED-ZDE-1, -8 |

---

## 1. The most important conceptual transitions, 1859-2026

The archive's historical thesis (EVO Sec. 0) is that RH research is a sequence of **changes of representation**. Each representation made one obstacle tractable, and each produced a characteristic ceiling short of Re s = 1/2. Two diagnostics recur throughout:
- **the Davenport-Heilbronn test:** where is multiplicativity used in a way a functional-equation-only function cannot imitate?
- **locality:** finite or local zero information reaches no global statement without a further theorem.

The transitions below are ordered in time. Each states what changed, what it made possible, and the ceiling it produced.

**T1 (1859-1905). Primes as the zeros of an entire function.**
- Riemann's memoir (PAPER-0469) gave the continuation, the functional equation, the explicit formula, and RH as a side remark.
- Hadamard's factorisation (PAPER-0137) and von Mangoldt's explicit formula and zero count (PAPER-0077, PAPER-0136) made the zeros rigorous objects.
- The prime number theorem via zeta(1+it) != 0 (Hadamard and de la Vallee Poussin 1896, PAPER-0009, PAPER-0044) made *zero-free regions* the first currency of the subject [T].
- Ceiling: product formulas take the zeros as input. The campaign theorem C3-M1 (C3F Sec. 3.5) is an explicit instance (failure mode F11). The functional equation alone is compatible with off-line zeros.

**T2 (1900-1914). From zeros to error terms, and the fragility of sign conjectures.**
- von Koch (PAPER-0030) proved RH equivalent to pi(x) = Li(x) + O(sqrt(x) log x).
- Littlewood (1912, PAPER-0287) gave the M(x) criterion.
- Hardy (1914) proved infinitely many zeros on the line.
- Littlewood's Omega-theorem (1914) showed that sign and size conjectures at the sqrt(x) scale can fail at astronomical heights.
- The lesson, finite-to-infinite extrapolation, recurs for a century. Mertens was refuted (1985), Polya and Turan's T(x) were refuted (Haselgrove 1958), and Oliva's step (3) holds for every prime up to 1.39·10^17 but fails for some prime below e^727.95, and infinitely often (C3-ADJ-O2, THEOREM; C3F Sec. 3.4).

**T3 (1917-1942). Growth, mean values, density and proportion.**
- Hardy-Littlewood's mean values (PAPER-0120) and Lindelof's growth problem.
- Carlson's zero density (1921, PAPER-0444), extended by Ingham (PAPER-0441). "Few zeros far to the right" became a statement strictly weaker than RH.
- Selberg's positive proportion (1942, PAPER-0413) introduced mollification and "proportion" statements.
- Ingham (1942) showed that, under linear independence of the ordinates, M(x)/sqrt(x) is unbounded.
- Ceilings: the density hypothesis is the sharp target of density methods, and proportions are blind to o(N) off-line zeros (OB-15; CON-0030).

**T4 (1933-1949). Geometry proves an RH, and the countermodel appears.**
- Hasse (PAPER-0139) and Weil (PAPER-0176, PAPER-0414) proved RH for curves over finite fields by intersection positivity on C x C. This became the template of what a proof should look like.
- In the same years, Davenport-Heilbronn (PAPER-0417) showed that a functional equation without an Euler product allows off-line zeros. That founded the Euler-product test.
- The archive sharpened the function-field side. Both of Weil's proofs feed one Gram matrix (C5-T1), and its 2g x 2g Toeplitz corner already decides RH (C5-T3, confluent form; C5F Sec. 3.2, 3.8). Both are THEOREMs.
- Ceiling: no number-field surface, no Frobenius, no Hodge index, and no real-coefficient Weil cohomology (C5F Sec. 4; OB-24; C5-OB4, IMPORTED from Deninger).

**T5 (1950-1956). RH as positivity and as spectrum.**
- Weil's explicit formula and positivity criterion (1952, PAPER-0473).
- de Bruijn's heat flow (1950, PAPER-0409).
- The Nyman-Beurling Hilbert-space closure (PAPER-0181, PAPER-0475).
- Selberg's trace formula (1956, PAPER-0353). It gives a spectral analogue in which the "RH" fails exactly when small eigenvalues exist (C2F SP-3).
- Turing (1953, PAPER-0474) made zero verification certifiable.
- Ceiling: an equivalent reformulation moves the difficulty into a positivity statement that has no independent reason to hold. "Spectral realization is cheap; positivity is the content" (OB-25; LED-OPS-3, corrected).

**T6 (1965-1976). Large sieve, mollifiers, statistics, Deligne.**
- Huxley's 12/5 (PAPER-0213).
- Levinson's 1/3.
- Montgomery's pair correlation (1973, PAPER-0091), with its RH-conditional "2/3 of zeros simple", and the random-matrix link (Dyson, PAPER-0494).
- Deligne's proof of the Weil conjectures (1974).
- Newman's conjecture Lambda >= 0 (1976, PAPER-0223).
- Zeros became a statistical ensemble.

**T7 (1980-2000). The modern three-sided shape (TL S4).**
- Random-matrix statistics and moments.
- A proliferation of equivalent criteria: Robin (PAPER-0206), Li (PAPER-0193), the Nyman-Beurling programme (strengthened by Baez-Duarte in 2003, PAPER-0004), Lagarias (2002, PAPER-0490).
- The Selberg class.
- Connes's noncommutative geometry. Its global number-field statement is unproved; see FND-0006.
- Two refutations: Mertens' conjecture (Odlyzko-te Riele 1985) and de Branges' positivity conditions (Conrey-Li 2000, PAPER-0779).

**T8 (2000-2023). Theorems about methods.**
- The decade's most distinctive output is a literature of *method limits* (EVO Sec. 12):
  - the mollifier error >= c/theta;
  - "theta = infinity implies RH" (Bettin-Gonek, PAPER-0064);
  - Lambda >= 0 (Rodgers-Tao, PAPER-0036; Dobner, PAPER-0333), which leaves heat flow no slack;
  - Farmer's critique of Jensen polynomials (PAPER-0686);
  - compatibility of the Alternative Hypothesis with all band-limited correlations (PAPER-0103; LED-SPACING-6);
  - Kakeya-hardness of the l^q large-values conjecture (LED-ZDE-18).
- Certified verification reached height 3.0·10^12 (PAPER-0001; LED-VERIF-1).
- Decoupling gave mu(1/2) <= 13/84 (LED-GROWTH-1).

**T9 (2024-2026). New mechanisms and a new verification regime.**
- Large values: Guth-Maynard [T].
- Pair correlation used as a *counting device*, through a rank-trace compression of Weil's Hermitian form (AF and LZ) [AI-U / T-U].
- Metaplectic theta functions plus a quadratic large sieve giving a fixed half-plane (QRH) [AI-U].
- Interpolation determinants excluding Siegel zeros [AI-U plus T-U].
- An epistemic shift (EVO Sec. 11.3):
  - old tools aimed at new targets;
  - formal verification proposed as primary evidence;
  - bulk release, crowd re-proofs, AI-agent audits and press coverage, all preceding refereeing.
- This archive is itself an instance. All its producers and verifiers are AI agents of related model families (quality/evidence_audit.md Sec. 1). CRIT23-D Sec. 2 discloses that the audit is not institutionally independent of the model family that discovered the 2/3 argument.

**What did not change.** Every method bounds something other than "zeros off the line" (EVO Sec. 12):
- zero-free regions bound the rightmost zero;
- density bounds counts far to the right;
- mollifiers and rank-trace bound a proportion;
- criteria test finite windows;
- computation verifies a finite height.

The passage from "few", "most" or "up to T" to "none" has never been made, and no 2026 result bears on Re s = 1/2.

---

## 2. Which strategies appear closest to meaningful new progress, and why

### 2.1 What "closest" means here

"Meaningful new progress" means a new infinite theorem that is genuinely weaker than RH, or a theorem about a method that redirects effort. The archive supplies three filters.

1. **Hitting-set test** (C2F Sec. 3.5 and Sec. 4, THEOREM-level logic; the "practical rule" is HEURISTIC). The step that decides the conclusion must use a property that every relevant RH-false relative lacks. The candidates are:
   - P4, the Selberg local condition;
   - P5, Lambda_F >= 0;
   - P8, degree 1 with conductor 1;
   - structure outside the predicate list, such as automorphy or special Gauss-sum identities.

   "Uses the Euler product" is not enough. C2-ADJ-1 (THEOREM) gives an RH-false Euler product with a self-dual degree-1 functional equation.
2. **Target genuinely weaker than RH.** Only zero density, and the density-currency targets (which can never give RH), are not RH-equivalent among the closing statements of the thirteen routes (missing_lemmas.md, cross-route remark 1).
3. **A named, checkable next lemma.**

### 2.2 The five strategies, ranked

**(1) The arithmetic-automorphic large sieve (the quasi-RH route).**
- *Status.* QRH-11/12 [AI-U; audited, no error found, FND-0009]; QRH-7/8 [AI-U; not audited]. Refinements below 7/8 are conditional on the 7/8 inputs.
- *Why it is closest.* It is the first claimed fixed zero-free half-plane for zeta. It uses exactly the inputs the countermodels lack (QRH-D Sec. 2.1):
  - Mobius multiplicativity;
  - the Gauss-Jacobi conversion mu = conj(alpha)·gamma_2^3, up to phases, with CRT-twisted multiplicativity;
  - the automorphy of Patterson's cubic theta function.

  It obtains a parity-sensitive bound with no sieve step (QRH-D Sec. 2.2; reading [O]).
- *Method limits.* These are dossier analyses: [O] where marked, otherwise checked in audit_S3.
  - The extraction lemma gives beta <= beta(n,h) = 1/2 + h(n-1)/(2n) from a full-row mean square over n-th power residue rows.
  - For sextic rows, h >= 1 is forced by the large-sieve diagonal. So 11/12 is the floor of that architecture (QRH-D Sec. 4.1; audit_S3 C4).
  - The 7/8 comparison system has B(l) = 11/12 - l/4 > 2/3 [O] (QRH-D Sec. 4.2).
  - Liu's "optimality" theorems are optima of a fixed inequality system, not bounds on the ideas.
  - Smaller n lacks an automorphic substitute: explicit Fourier coefficients of n-fold metaplectic theta functions are known only for n = 2 and 3.
  - Generic sextic sieves give only the trivial bound (QRH-D Sec. 4.3, (C4)).
  - Every input that reaches 1/2 is of GRH strength for a family (QRH-D Sec. 4.3, (C5)).
  - The proof is qualitative, so it gives no explicit zero-free region beyond the half-plane itself (QRH-D Sec. 2.6).
  - Proposition 3.1 is of density-hypothesis strength for the sextic family [O], so "all the risk sits there" (QRH-D Sec. 2.5).
- *Consequences if correct* (QRH-D Sec. 3; CON-0016, CON-0001):
  - effective primes in progressions for q up to about x^(1/12);
  - effective class-number and least-nonresidue bounds;
  - Lindelof to the right of Theta;
  - a Linnik exponent q^(12/5+eps) from refereed density inputs (sound_but_known, which corrects the dossier's 8/3).
- *Not implied:* RH or GRH, the density hypothesis below Theta, Lindelof on the line, and better short-interval exponents. The last fails because the binding point is sigma = 7/10 (CON-0028).

**(2) Rank-trace / pair-correlation counting.**
- *Status.* 2/3 (0.6725 with the Montgomery-Taylor window) simple and critical [AI-U plus T-U; FND-0004 repaired]. Knausgard's 0.67354 [T-U, self-described AI-assisted; rests on unreplayed computer searches].
- *Why it is close.* The 2/3 bound replaces RH in Montgomery's 1973 argument by an inertia and rank-trace inequality on a finite compression of Weil's form (CRIT23-D Sec. 0). If correct, it moves the unconditional record for simple critical zeros from the refereed 0.407511 (PRZZ) to 2/3 in one step; the claim is unrefereed. The refereed record for zeros on the line counted with multiplicity was 0.417293962 (PRZZ, with Wu as co-record; LED-CRIT-4 corrected). Its analytic input, the unconditional Montgomery theorem BGSTB24 (PAPER-0053), is refereed. Two proofs exist that share no unverified lemma (CRIT23-D Sec. 0); LZ was written after AF and shares the Montgomery-Taylor extremal problem, so it is a second proof rather than fully independent corroboration (LED-CRIT-2, verifier correction).
- *Limits.*
  - The bandwidth-one ceiling is about 0.6818 (LED-CRIT-10). It is author-stated and interval-certified inside unrefereed preprints, and was not audited by us.
  - The argument holds verbatim for Davenport-Heilbronn and Epstein.
  - It is insensitive to o(N) off-line zeros, so even 100% would not be RH (CRIT23-D Sec. 0; CON-0030).
- *Why progress is still plausible.* CON-0006 locates exactly where RH enters the 19/27 simple-zero machinery: only S_2 uses it. It gives an RH-free conditional route (Sec. 4).

**(3) Large values and zero density.**
- *Status* [T], refereed:
  - sup A <= 30/13;
  - the density hypothesis for sigma >= 25/32;
  - primes in all intervals of length x^(17/30+eps) (LED-ZDE-1, -4, -6, -8).
- *Why it is close.* It is refereed, it moves steadily, its target (the density hypothesis) is genuinely weaker than RH, and it has direct prime consequences.
- *Limits.*
  - The density hypothesis is the sharp target, so density never gives RH.
  - The bottleneck is a tangency at sigma = 7/10.
  - The l^q large-values conjecture implies Kakeya (LED-ZDE-18).
  - No 2026 half-plane improves short-interval exponents (CON-0028, sound_but_known).

**(4) Semilocal Weil positivity and finite windows.**
- *Status.*
  - Pos((log 2)/2) [T] (Yoshida; Connes-Consani 2021, PAPER-0099; LED-POS-6).
  - Pos(0.8) [T-U], an unrefereed computation (high precision with an error budget, not directed rounding, per CON-0010), not independently replayed (Zhu; LED-POS-7).
  - The S-local trace formula [T] (LED-OPS-2).
  - A reality theorem for a simple even ground state [T] (LED-OPS-7).
- *Why it is close.* The problem is well posed, only finitely many places enter, and it is auditable.
- *Adjudicated limits.*
  - C5-ADJ-MODEL (THEOREM): zero-side window positivity plus zeta-like counting cannot force RH. Any effective finite reduction must therefore use prime-side structure.
  - C5-ADJ-LOG (THEOREM, trivial): a threshold L_0 with Pos(L) implying RH for L >= L_0 exists non-constructively. So "over Q no finite window suffices" is false as stated.
  - Certifying Pos(L) costs about 5.2 to 5.5·e^(2L) digits (C5F, row 6, correcting OB9).
  - C4-ADJ-BLIND (THEOREM): every bounded family of windows is blind, uniformly in height, to a neighbourhood of the line. The radius collapses doubly exponentially.
  - C4-B (THEOREM under the single-defect hypothesis H1): no window is height-local for large-delta defects.

**(5) Interpolation-determinant Siegel exclusion.**
- *Status.* [AI-U plus three T-U re-proofs (Banks, Kerr, Guo)]. The four proofs have three structurally independent cores: OAI/Banks, Kerr, Guo (SIEGEL-D Sec. 2 and header), so the claim does not rest on any single one.
- *Limits* (SIEGEL-D Sec. 7):
  - the arithmetic fraction obeys kappa >= 1/2;
  - the zero couples to the primes with a loss of order delta (log X)^2;
  - c is of order 10^-2, and the present comparison shape is capped near 3 - 2·sqrt(2) = 0.1716 (UQ-H8);
  - it says nothing about complex zeros, zero-free strips or Chowla-type positivity;
  - Linnik's L = 5 is unchanged (CON-0027).
- This route is closest to *finished*, not closest to RH.

### 2.3 What is not close (adjudicated)

- **Large criterion computations: Li, Jensen, psi/pi, Robin, Nyman-Beurling, Mertens, Lambda.**
  - Every family with a finite implication horizon has one of size about T^2, except the local PF/Laguerre criteria, whose horizons are linear in the height (C1F Sec. 3.6, HEURISTIC structural summary; C1-ADJ-LOCAL).
  - "RH(T) with T >= 100 implies lambda_n > 0 for n <= T^2" is a THEOREM (C1-L2; the statement is Oesterle's).
  - No published large criterion computation is informative beyond T_0 = 3,000,175,332,800, except trivially for isolated pi(x) above 1.1·10^26 (C1F Sec. 5).
  - A proved Lambda <= 0.2 adds nothing beyond RH(T_0) plus unconditional theory (C1F, row 8).
- **Heat-flow arguments "with room to spare".** Rodgers-Tao: any valid argument must fail for every t < 0 (OB-11). The Turan inequalities hold for every H_t (C2-14, THEOREM).
- **Formal transfer of function-field proofs.** The census contains 12,787 RH-false "fake" curve zeta functions satisfying the formal axioms (C5-E1).
- **Hilbert-Polya realizations without positivity** (OB-25; LED-OPS-20).

---

## 3. Historically neglected ideas that deserve reconsideration

The archive has no dedicated file on this question. The evidence comes from the "old tools, new targets" pattern of 2026 (EVO Sec. 11.3) and from the campaign and discovery results that revived old statements. "Neglected" here means *under-exploited for RH-type targets*: several of these ideas are famous in their own fields.

1. **Metaplectic theta functions** (Kubota; Patterson 1977; Heath-Brown-Patterson 1979; Dunn-Radziwill 2024, PAPER-0960).
   - The 11/12 argument turns on the automorphy of the cubic theta function and on its explicit coefficients (QRH-D Sec. 2.2, Sec. 4.1).
   - The press reports experts as saying metaplectic forms were used where "nobody expected" them (QRH-D Sec. 1.4, secondary [S]).
   - What to reconsider: explicit quartic and higher coefficient structure. It is the single missing input for an OpenAI-independent route (CON-0038; UQ-B2).
2. **Transcendence-style auxiliary constructions:** interpolation determinants, Siegel's lemma, Masser's 1981 zero estimate, Stepanov-type injectivity (SIEGEL-D Sec. 0, Sec. 2).
   - Their claimed success on Siegel zeros (unrefereed; FND-0010) makes two classical problems worth revisiting:
     - over Q, a Stepanov-type route needs only *one* one-sided bound psi(x) <= x + O(x^(1/2+eps)) (C5-S1, THEOREM, classical Landau), whereas over F_q only the lower one-sided bound forces RH (C5-SK-ASYM, THEOREM);
     - Pritsker's weighted integer-Chebyshev problem (C5-ML-S, CONJECTURE). The current bracket for t_Z([0,1]) is [0.4222286, 0.4226847], which is above 1/e (unrefereed).
3. **Montgomery's 1973 argument used as a counting device.** The RH-conditional 2/3 stood for 53 years. An unconditional Montgomery theorem (BGSTB24) and a rank-trace inequality unlocked it (CRIT23-D Sec. 0).
   - The general lesson: audit exactly where RH is used in classical conditional results.
   - CON-0006 does this for Conrey-Ghosh-Gonek / Bui-Heath-Brown (Sec. 4.2).
4. **Gram's law and S(t) at special points** (Trudgian 2011; Selberg's central limit theorem).
   - C3-ADJ-S (THEOREM) shows that de Branges' necessary zero condition is exactly a condition on S(gamma_n) mod 2.
   - The positive-proportion methods for failures of Gram's law are therefore the natural tool for de Branges failures (UQ-E1).
5. **Littlewood 1912 and Beurling 1955 in Hardy-space form.** CON-0021 [O; sound_and_useful] gives an exact dictionary between Nyman-Beurling approximation rates and the abscissa Theta of the zeros.
6. **Beurling generalized primes as obstruction maps** (Diamond-Montgomery-Vorhauer, PAPER-0581; Broucke-Debruyne-Revesz; Hilberdink). CON-0032 turns an RH-conditional construction into an unconditional refutation by a case split (Sec. 4.2).
7. **Classical real-entire-function theory.** Three old results gave clean negative or control results:
   - Csordas-Varga 1988 (log-concavity) gives C2-14: every Turan inequality holds for every H_t, including t < 0 where H_t has non-real zeros;
   - Craven-Csordas-Smith 1987 gives C2-ADJ-6: unconditional uniform large-shift Jensen hyperbolicity for an off-line perturbation of H_0.2;
   - Polya's 1926 approximant xi* is proposed as an arithmetic-free control for Lambda (CON-0024, empirical only).
8. **Small-support Weil positivity and the semilocal trace formula** (Yoshida 1992; Connes 1999 Thm 4; Connes-Consani 2021).
   - Over F_q, the finite-rank Toeplitz mechanism decides RH on one window, with the sharp threshold (g - 1/2) log q (C5-ADJ-W, C5-ADJ-SHARP).
   - The number-field mechanism is the target of ML-C1 (Connes-Consani Conjecture 4.1 at q = 3).
9. **Oesterle's unpublished 2000 typescript and Brown 2005** (PAPER-0600). The forward semi-local Li theorem is now a THEOREM with a complete proof (C1-L2). The converse, a two-way finite zero detector, is open (UQ-F1).
10. **Chowla-Selberg and Bateman-Grosswald 1964.** The exact constant term gives C2-ADJ-2 (Sec. 7). Bateman-Grosswald may already contain the threshold equation; it was not accessed.
11. **Lattice reduction from cryptanalysis**, for Ingham-kernel searches on Mertens and Skewes (research_programs.md ARITH Sec. 6 and Sec. 8; Kim-Nguyen 2025).
12. **Deninger's quaternionic positivity** (C5-ML-Den, CONJECTURE) and **Speiser 1934** (CON-0023, sound_but_known).

**A cautionary case.** Siegel's 1932 auxiliary function R(s) from Riemann's Nachlass was tested against the 2026 theorem and judged **vocabulary_only** (CON-0022). Without an open attribution lemma, no constraint follows.

---

## 4. The strongest genuinely new connections found by this program (verified only)

Three tiers are kept apart below:
- adjudicated campaign connections (FINAL files);
- discovery-register items judged sound_and_useful, or needs_correction used only in corrected form, all of them *Observatory proposals* checked by one verifier;
- bridge mappings to the host repository, which are proposals for the host's own review.

The register's verdicts: 9 sound_and_useful, 10 sound_but_known, 19 needs_correction, 1 vocabulary_only, and 0 false (connections_register.md legend; strongest_connections.md header).

### 4.1 Adjudicated campaign connections

- **One Gram matrix behind both of Weil's proofs, and its finite corner** (C5-T1, C5-T3, C5-ADJ-W, C5-ADJ-SHARP; all THEOREM).
  - Over F_q, Hodge index and Rosati positivity give the same positive semidefinite matrix.
  - Its inertia is (d - m, m, N - d) for N >= d, so RH(C) holds iff T_(2g) >= 0.
  - Positivity of Weil's form on C_c^inf(-a, a) holds iff T_(ceil(2a/h)) >= 0. The window threshold (g - 1/2) log q is attained in the formal class for 20 of the 24 tested (q, g).
  - Set against C5-ADJ-MODEL over Q, this makes "infinite genus" exact for the window route: over F_q the zero set has finite rank d <= 2g modulo 2·pi/h, and over Q no zero-side argument can supply a substitute.
- **De Branges positivity is a Gram-type statement** (C3-ADJ-S, THEOREM). The condition -Re(xi'(rho_n)·xi(1 + rho_n)) >= 0 holds iff S(gamma_n) - delta(gamma_n) lies outside (3/4, 7/4) mod 2. It links the de Branges programme to Gram's law and Selberg's central limit theorem.
- **Two kinds of horizon** (C1F and C4F, cross-campaign HEURISTIC; README Sec. 3).
  - Index criteria disperse information: Li needs n of order T^2/delta, and Jensen needs d of order T^2/(2·t_c).
  - A Weil window sees a large-delta defect already at L ~ (1/(2·delta)) log log T (C4-B under H1, THEOREM).
  - Both are single-defect statements.
- **Completing the square on both sides** (C4-C and C4-ADJ-PAIR, THEOREM). The detection criterion is the zero-side counterpart of the host repository's S_L. This is a structural analogy, not a result (C4F Sec. 3.6).
- **The Jensen-heat bridge against the countermodel zoo** (C1-J2 and C2-17).
  - The isolated-pair prediction d* ~ T^2/(4·delta^2) gives 39.06 for the injected quadruple at 0.9 + 5i.
  - C2 observed the first non-hyperbolic Jensen polynomial at d = 40 (NUMERICAL-NONRIGOROUS).
  - This is a consistency check of a HEURISTIC, not a validation. AC-15 is the certified test.

### 4.2 Discovery-register items (Observatory-proposed; one verifier each)

1. **CON-0032 (sound_and_useful): the Beurling frontier.**
   - T1, an [O] theorem, non-constructive, with the verifier's re-derivation: for every beta > 2/5 there is a discrete Beurling system with N_P(x) = ax + O(x^(beta+eps)) for which psi_P(x) = x + O(x^(1/2+eps)) fails.
   - Proof by case split. If RH fails for zeta, the rational system is a witness. If RH holds, Broucke-Debruyne-Revesz Theorem 1.3 supplies one.
   - This answers, non-constructively, a question C2 left open. T1 rests on BDR Theorem 1.3, an arXiv preprint whose journal status was not verified.
   - T4 maps the open region: beta < 1/2 and Theta >= 2/3, which contains 7/8 and 11/12, has no known countermodel.
2. **CON-0021 (sound_and_useful): the Nyman-Beurling decay exponent.**
   - [O] proposition, both directions re-derived at proof-sketch level: for alpha in (Theta, 1), limsup log s_n(alpha)/log n = -2(alpha - Theta).
   - Hence RH holds iff s_n(alpha) << n^(1 - 2·alpha + eps) for one, equivalently every, alpha in (1/2, 1).
   - It removes the n^(-delta/3) loss of Balazard-Saias.
3. **CON-0006 (corrected): the off-line pair defect.**
   - (a) [O] unconditional inequality: N*(T) >= |S_1|^2/(S_2 + D/2), where D is the off-line pair defect.
   - (b) [O] conditional theorem: if every zero in (T, 2T] satisfies |beta - 1/2| <= eta(T)/(log T)^(3/2) with eta -> 0, then liminf N*/N >= 19/27.
   - This is the first exact accounting of where RH enters the CGG/BHB discrete moments.
4. **CON-0025 (sound_and_useful).** The imaginary quadratic fields whose class group has exponent at most 2 are exactly the 65 known ones, and Euler's idoneal list is complete, *without* quasi-RH.
   - It is conditional on Kimura's Theorem 1 with Proposition 9 (unrefereed; Lean reported, not replayed) and on Elsenhans-Klunners-Nicolae Theorem 1 (refereed).
   - Computed exactly: two independent scans of every fundamental discriminant up to 3.2981·10^16 with omega >= 12, 0 survivors.
5. **CON-0038 (sound_and_useful).**
   - Ji's OpenAI-independent route over Q(i) (599/600) has a floor near 0.99 for every zero-density input. Every variant examined has a floor of at least 23/24 > 11/12.
   - So an independent 11/12 needs a quartic row mean square (conjecture J4).
   - This is a statement about Ji's inequality system, not about zeta.
6. **CON-0030 (corrected): density currency.** [O] formalisation of folklore: inputs of density type (Riemann-von Mangoldt, n-level correlations with o(TL) error, Levinson-Conrey output inequalities, bandwidth-limited trace moments) are stable when o(T) zeros are moved. No argument using only these inputs can exclude a single off-line quadruple.
7. **CON-0035, CON-0011, CON-0036, CON-0012 (corrected): GL(2) transfer of the rank-trace device.**
   - For an individual GL(2) L-function, bandwidth 1/2 gives no simple zeros (lambda* = 0.5502). A distinct-zero target 1/R*(1/2) = 0.4617 is conditional on an unported pair-sum asymptotic.
   - Family averages of at least 0.6725 (simple critical) are a plan conditional on a Petersson diagonal lemma.
8. **Smaller items.**
   - CON-0008: the persistence lemma, an off-line zero forces Lambda >= c·delta^2/(log gamma)^2. A sketch with two gaps.
   - CON-0018 and CON-0019: exponent dictionaries conditional on QRH-7/8. Piltz alpha_k <= 7/8 - 49/(24k) beats the records for k = 14 to 21; the Gafni-Tao mu(theta) is lowered only on (0.2445, 5/12).
   - CON-0015: the xi' window class saturates at 0.868642, below Wu's 0.86957 (floating-point optimum).
   - CON-0024: Polya's xi* as a control, with empirical Lambda* <= -4 (non-rigorous).

### 4.3 Repository bridge (proposals for the host's review)

Of 166 prior-art and obstruction items (215 in all):
- 79 confirmed;
- 74 confirmed with correction;
- 12 relation_overstated (evidence_audit Sec. 1).

Identity-level prior art includes:
- the host's C_X(s) correction factor and Gorodetsky's smooth-number ratio (BRG-CAUSAL_EULER-P1, identical);
- the host's Robin reductions and CLMS 2007 (BRG-ROBIN-P1, P2);
- the host's Sec. 10 scalar and Knausgard's Theorem 5.1 (BRG-OPERATORS_HEAT-P15, P16).

None of this changes any integrated status (strongest_connections.md Sec. 4).

---

## 5. Assumptions and obstacles that recur across unrelated approaches

| # | Obstacle (exact form) | Approaches it binds | Evidence |
|---|---|---|---|
| 1 | **Countermodel / hitting set.** Any step whose zeta inputs are shared by an RH-false relative cannot decide RH. Witnesses: Davenport-Heilbronn (5 certified off-line zeros with t <= 300, a complete list); Epstein x^2 + 5y^2 (35 with t <= 200, complete; zeros with sigma > 1, e.g. at t about 1193.9); zeta_19; the synthetic xi~; the F_c family M10; Selberg and Ihara zetas; 12,787 function-field fakes | Functional-equation-only arguments; Jensen tails; Turan inequalities; Euler product without P4/P5/P8; formal function-field axioms; rank-trace counting | C2F Sec. 3.1, 3.5, 4 (SP-1 to SP-8); C5-E1; OB-1 to OB-7 |
| 2 | **No source of positivity.** Every RH-equivalent route ends in a positivity statement with no independent reason to hold: Weil, Li, Connes' global trace formula, unitarity of Meyer's representation, de Branges | Weil/Li/Bombieri; operators; Connes; de Branges; function-field transfer | C5F Sec. 6; OB-25; LED-OPS-3 (corrected); FND-0006, FND-0013 |
| 3 | **Locality and finite-to-infinite.** Implication horizons of about T^2; single-defect detection scales; one finite window cannot be decided from the zero side; first failures at Skewes scale | Criterion computations; Weil windows; arithmetic sign conjectures | C1F Sec. 3-5; C5-ADJ-MODEL; C3-ADJ-O2; C3F tag F5 |
| 4 | **Density currency and proportion blindness.** Proportions, even 100%, ignore o(N) off-line zeros. Mollifier error >= c/theta; bandwidth-one cap about 0.6818; band-limited data are compatible with the Alternative Hypothesis | Mollifiers; pair correlation; rank-trace; zero statistics | CON-0030; OB-14 to OB-16; LED-CRIT-9, -10; LED-SPACING-6 |
| 5 | **Heat-flow openness.** Any valid argument must fail for every t < 0 | Turan, Jensen, log-concavity, de Bruijn-Newman | OB-11; C2-14; CON-0033 (corrected) |
| 6 | **Diagonal / large-sieve barrier and parity.** Positivity plus duality returns D^2 below the diagonal; sieve axioms cannot see parity; generic large sieves carry extra (AB)^(2/3)-type terms | Quasi-RH extraction; sieve methods; zero density | QRH-D Sec. 2.2-2.3, 4.1; OB-12, OB-19; LED-ZDE-18 |
| 7 | **Archimedean place and infinite genus.** No finite rank; window margins collapse like exp(-c·e^(2L)) | Weil windows; semilocal operators; function-field transfer | C5F Sec. 3.5, 4 (W6, OB2, OB3, OB9 corrected); OB-18 |
| 8 | **One defect versus configurations.** Model statements assume a single off-line quadruple; adversarial multi-defect configurations could fail earlier | Every detection-horizon statement; C4-B (hypothesis H1) | C1F gap (c); C4F gap (b) |
| 9 | **Fragility of explicit constants.** Erratum chains propagate silently | Explicit zero-free regions, PNT, Robin | C3F D13; FND-0003, FND-0012; LED-ARITH-19 |
| 10 | **Fidelity and independence of verification.** A Lean check is only as good as the fidelity of its definitions and its axioms; agents are correlated | Every 2026 claim; this archive | QRH-D Sec. 1.3 (custom Hecke LFunction); CRIT23-D F5 (run-axioms); quality/limitations.md |

Obstacles 1, 2 and 3 are the deepest: they bind routes with no common technique. Obstacle 1 tells a proof what it must use. Obstacle 2 says that no number-field object yet carries a pairing whose positivity has a reason independent of RH (C5F, smallest remaining gap). Obstacle 3 says that finite information never substitutes for a theorem.

---

## 6. Published arguments with credible technical issues (adjudicated findings, scoped wording)

The rules are methodology Sec. 6. An error requires an explicit witness reproduced independently. Corrections in print are reported as such. Unverified items stay unresolved. Every finding below is scoped to the named claim; none is a verdict on a whole paper.

### 6.1 Verified errors (public characterization allowed, in this scope only)

- **FND-0001, Yakaboylu, J. Phys. A 57 (2024), arXiv:2309.00405 v6.**
  - Scoped wording (F1 audit): the paper's Stage-II argument (Sec. II, Eqs. 13-18) does not establish a self-adjoint similarity transform with real spectrum.
  - Witnesses: the proposed weight (18) is indefinite, with an explicit vector giving <U|U> = -0.0231. The boundary condition (17) admits eigenfunctions with non-real eigenvalues, for example s about 0.8811 + 63.4528i, where zeta != 0. The identical argument would place an off-line Davenport-Heilbronn zero on the line.
  - The paper does not claim a proof of RH. It must not be described as having claimed one.
- **FND-0002, Farmer, Adv. Math. 411 (2022).**
  - Table 4.1 contains two minor numerical slips. The j = 10 threshold is 119 rather than 118: J^(119,0) of X_10 is certified real-rooted, and degrees from 120 on have non-real zeros. The j = 20 entries correspond to moving the zeros 9·pi/2 and 11·pi/2 rather than the two closest to 20, for which the threshold is 477.
  - The paper's conclusions are unaffected.
  - Three independent Arb certifications (C1-J4; C1-ADJ-X10).
- **FND-0003, Bellotti-Trudgian-Yang, arXiv:2603.21490v1** [T-U].
  - The Table 1 entry m_5 = 0.00735709 is not a lower bound for the stated rational polynomial. The certified minimum lies in (0.0073564918, 0.0073564919).
  - With the corrected value, the sum of (log p)·m_p is 0.2354513 > 0.23545, so Lemma 10, Theorem 1 and the constant 4.896 are unaffected. The Observatory independently reproduced the 4.896 chain.
  - This must never be described as an error in Theorem 1 or in 4.896.
- **FND-0004, Alpoge-Furman, arXiv:2608.13637v2** [AI-U].
  - Permitted wording: "a local error in the proof of AF Prop. 4.2, with a short repair; the Proposition and all results are unaffected."
  - Witness: zero #10085 at T = 10^4. Repair: tr G~ = N(I') + O(sqrt(T) log T).
  - An independent second review of the repair is still open (UQ-A5).
  - Separately, Arias de Reyna's exposition (arXiv:2610.24612) judged one boundary step of v2 wrong as written and repairable (EVO Sec. 5). The archive does not establish that this is the same step.
- **FND-0012, Cheng-Graham, Lemma 2** (already corrected in print by Hiary-Patel-Yang 2022). The bound 1/(pi·theta) + 1 is false as stated. C3-CG1 adds an explicit smooth certified instance: theta = 0.02, |S| = 31.598... > 16.9155.
- **FND-0014: claims already withdrawn or not accepted** (Atiyah 2018; Micheas arXiv:2607.04338 v1; Queme arXiv:2004.00460; Oliva arXiv:1807.06447). The exact failing steps are reconstructed in C3-A1, C3-M1, C3-Q1, C3-O1 and C3-ADJ-O2. All these claims were already withdrawn, self-flagged or publicly critiqued.
- **Campaign-adjudicated refutations not yet entered as FND records** (C2F, authoritative):
  - **Liu-Wu, arXiv:2503.24275 (and 2010.03521).**
    - The claim "non-trivial zeros of the Davenport-Heilbronn function can only lie on the critical line" is false (C2-07).
    - Witnesses: certified off-line zeros, by two independent methods and evaluation routes, and the classical theorem that the function has infinitely many zeros in sigma > 1.
    - Failing step as identified: a strict ratio inequality evaluated at a common zero of f(s) and f(1 - s), i.e. 0/0.
    - C2F Sec. 7, item 8, asks for a further L2 check of that step against the full text before any external citation.
  - **Betermin-Samaj-Travenec, arXiv:2110.09368v2, Conjecture 1.1.**
    - The conjecture is false (C2-ADJ-2, THEOREM; it needs no numerics).
    - The paper's reported agreement "by at least 22 decimal digits" is inconsistent with the exact formula: the two numbers agree to 19 decimal places.
    - The finding concerns a conjecture, not a theorem of the paper.

### 6.2 Valid with stronger consequences

- **FND-0013, Conrey-Li (IMRN 2000).** De Branges' necessary zero condition fails frequently, not only at their witness:
  - 195/2000 and 2724/20000 failures by three independent Arb implementations, and 15,567/100,000 by the adjudicator's implementation, cross-checked against a second formula for n <= 20000 (C3F header and Sec. 3.2);
  - block rates rising from 8% to about 22% up to n = 10^10;
  - an exact S(t) reformulation (C3-ADJ-S).

### 6.3 Correct but misinterpreted

- **FND-0006, Connes 1999 (Selecta).**
  - Theorem 5, global trace formula equivalent to RH, is proved for global fields of positive characteristic.
  - For number fields the paper reduces RH to an unproved trace-formula/positivity statement. Its literal subspace B_Lambda is {0} for any field with an archimedean place.
  - Citations attributing a proved number-field result misread the paper. Instances are in the F5 audit, Sec. 4.
- **FND-0007, Andrade-Keating (J. Number Theory 2014).** Theorem 1 and Sec. 5.3 rest on Conjecture 5; later citations should carry the conditionality.
- **FND-0008, Ng-Shen-Wong (JEMS 2026).**
  - The issue was a misreading by the Observatory's own Level-1 reader: a pdftotext artefact turned 1/2 into "12".
  - A minor citation-range mismatch (the paper quotes k >= 1/2 where the companion proves k >= 1) is immaterial at k = 4.
  - Theorem 1.1 is conditional on RH and a quaternary additive-divisor conjecture.
- **Recurring misreadings of correct work, flagged across the archive:**
  - Zhu's exp(-L·e^L) is an RH-conditional *upper* bound, not a decay law. The C5 investigator misquoted it (C5F, row 6).
  - Liu's "optimality" is the optimum of a fixed inequality system (QRH-D Sec. 4.2).
  - Proportion theorems are not progress toward "all zeros" (C3F D9).
  - Lambda <= 0.2 adds nothing beyond RH(T_0) (C1F, row 8).

### 6.4 No issue found in the inspected portion

- **FND-0009, QRH-11/12.**
  - Seven section auditors and about one hundred identity checks in Z[omega].
  - The sign of the Kubota multiplier was settled numerically: theta(gamma w) = (c/a)_3 theta(w) to 2e-13.
  - Appendix A: 515,936 cases, 0 failures.
  - Imports checked against their statements, not re-proved.
- **FND-0010, Siegel exclusion.**
  - Nine load-bearing steps re-derived in each of four proofs; 130 PASS / 0 FAIL.
  - Toy replays show that the hypotheses p > H, Frob_p in {sigma, sigma·tau}, and Q-independence of the kernel coordinates are each necessary.
  - Two harmless missing-hypothesis items in Kerr (SIEGEL-D Sec. 0).

### 6.5 Not characterized (open questions only)

- **FND-0005** (Yang's Littlewood-type constant across versions): a suspected gap, with no public characterization allowed.
- **FND-0011** (Planat-Raymond, Lambda < 0.156821): no issue found in the inspected portion; the large certificate was not replayed.

### 6.6 Corrections already in print, and documentation-level ambiguities (not Observatory findings)

- Turing's errors were corrected by Lehman.
- Ford 2002: 8.463 became 8.464.
- Feng 2012's gap was repaired by Pratt-Robles (theta = 6/11).
- Pearce-Crump: 7% became 6.78%.
- Hiary's 0.63·t^(1/6) log t became 0.77, then 0.618 (C3F D13).
- BGST v3 corrects the proof of BGSTB24 Theorem 1 and states that Lemmas 5 and 7 are unaffected (LED-CRIT-13).
- The Ramare 2016 to Dusart 2018 erratum chain: BFKNW (unrefereed) state that Dusart's Mertens-product corollaries were invalid as proved and recover them (LED-ARITH-19).
- Polymath15's Table 1, row 2: the canopy step underlying Platt-Trudgian's Lambda <= 0.2 is described as one they "expect to be able to verify". This is a documentation-level ambiguity in a refereed input (LED-DBN-9, corrected; F8).

---

## 7. New mathematical claims independently established by the program

**Scale and modesty.** Every item below is small. None bears on whether RH holds. Every proof was produced and checked by AI agents (investigator, skeptic, adjudicator); no human has refereed any of them. Prior-art searches were limited to the arXiv API, zbMATH, Crossref and occasional web search. Where novelty is stated, it is search-limited. Arb certificates are conditional on FLINT/Arb.

### 7.1 Campaign theorems (adjudicated)

| ID | Statement (short) | Status and evidence | Novelty |
|---|---|---|---|
| C1-L1 | Li quadruple identity: lambda_n = sum over on-line zeros of 2(1 - cos n·phi) + sum over quadruples of 4[1 - cosh(na) cos(n·phi)] | THEOREM | Elementary |
| C1-L2 | If T >= 100 and RH(T) holds, then lambda_n > 0 for 1 <= n <= T^2. So RH(T_0) gives n <= 9.00105·10^24, and RH(317) gives n <= 100489: Johansson's rigorous lambda_1, ..., lambda_100000 carry no information beyond height 317 | THEOREM; complete independent proof, Rosser tails written out (C1F Sec. 3.1) | **The statement is Oesterle's** (2000, unpublished, via Voros); "possibly new" withdrawn |
| C1-N1, N2 | Nyman-Beurling floor: an off-line pair forces norm(chi - f)^2 >= F = (4·delta/T^2)(1 + O(1/T^2)) for every f in B_lambda | THEOREM; second-order coefficient NUMERICAL-NONRIGOROUS | Not discussed in C1F; search-limited |
| C1-ADJ-MONO | Real-rootedness of Jensen polynomials is monotone in the degree | THEOREM | Classical |
| C2-01 | Complex Krawczyk test | THEOREM | Standard |
| C2-15, C2-24 | The synthetic xi~ = xi·P_Q; the meta-lemma (an RH-false member with predicates P_1, ..., P_k shows those predicates do not imply RH) | THEOREM | Elementary |
| C2-21 | A continuous Beurling system with zeros exactly {0, rho, conj(rho)} and N(x) = Ax + O(x^sigma) for every sigma > beta | THEOREM | Search-limited |
| C2-05, C2-11 | Right edges: Davenport-Heilbronn != 0 for Re s >= 1.13514; Epstein x^2 + 5y^2 != 0 for Re s >= 1.17816 | THEOREM (computer-assisted) | Bombieri-Ghosh may contain the sharp form (IMPORTED, L0+) |
| C2-14 | All Turan inequalities b_m(t)^2 > ((2m-1)/(2m+1))·b_(m-1)(t)·b_(m+1)(t) hold for **every** real t, including t < 0 where H_t has non-real zeros | THEOREM, given Csordas-Varga 1988 (IMPORTED, L0+); moment lemma proved (C2-ADJ-3) | The t = 0 case is CNV 1986; the t < 0 corollary is "probably known, not located" |
| C2-ADJ-1 | F_c(s) = zeta(s)(1 + c·2^(-s) + 2·4^(-s)), c > 2·sqrt(2): an ordinary Dirichlet series, multiplicative coefficients, an Euler product over the rational primes, a self-dual degree-1 functional equation of conductor 4, and zeros on Re s = log_2 a != 1/2. It violates only P4, P5 and P8 | THEOREM | **Folklore** (Perelli's remark); no paper with this exact family located |
| C2-ADJ-2 | Z_k(1/2) = 2·gamma + 2 log(k/(4·pi)) + 8·sum over N of d(N)·K_0(2·pi·N·k). Unique threshold k* = 7.0555079554...; a real zero in (1/2, 1) for every k > k*; **BST Conjecture 1.1 is false** | THEOREM, plus two independent numerical codes | The formula may be in Bateman-Grosswald 1964 (not accessed); no published refutation of the conjecture found |
| C2-ADJ-6 | For an off-line perturbation of H_0.2: J^(d,n) hyperbolic for all d once n >= n_0, although some J^(d,0) is not | THEOREM, given Craven-Csordas-Smith (L0+) and Platt-Trudgian Cor. 2 | Repair of C2-17 |
| C3-A1, Q1, M1 | Exact failure mechanisms in Atiyah (2.6 forces T constant), Queme (termwise limit at the boundary of convergence), Micheas (Theorem 1 false) | THEOREM | Explains already-withdrawn claims |
| C3-O1, C3-ADJ-O2 | Oliva's step (3) holds for every prime 5 <= p <= 1.39·10^17, fails for some prime p < e^727.951332668, and fails infinitely often | THEOREM, modulo IMPORTED Platt-Trudgian 2016 and Littlewood 1914 | Sharpening of a withdrawn preprint's step |
| C3-CG1 | An explicit smooth counterexample to Cheng-Graham Lemma 2 | THEOREM (computer-assisted) | The error was already corrected by HPY and Ford; adds an instance to Landau's 1928 examples |
| C3-ADJ-S | sign P_n = sign sin(pi·S(gamma_n) + pi/4 - a(gamma_n) - c(gamma_n)). The de Branges zero condition fails iff S(gamma_n) - delta_n lies in (3/4, 7/4) mod 2 | THEOREM plus NUMERICAL-RIGOROUS | **New as stated**, as far as the search found (arXiv API, AIM page, Gram's-law literature); elementary |
| C4-C, C4-ADJ-PAIR | Exact detection criterion (Schur-Sylvester), and the pair identity W = P + 2m·abs(<g,u>)^2 - 2m·delta^2·abs(<g,w>)^2 | THEOREM | C4-C is standard and not new |
| C4-LAT | Lattice/flat model: inf W < 0 iff L > pi/s or sinh(2·delta·L)/(2·delta) - L > Psi_0/2; crossover kappa_c = 2.1773189849653, the root of sinh k = 2k | THEOREM (model). The mirror-pair aside was refuted and repaired | Model statement |
| C4-B | Under H1 (one off-line quadruple, all other zeros on the line, T >= 100), windows of length L_B = (1/(2·delta))(log log T + log log log T + O_delta(1)) detect the defect | THEOREM (conditional on H1; vacuous if RH holds). Asymptotic display corrected to (0.5 + 0.704L) log T | "Possibly new", search-limited; Danesh 2026 uses the same e^(delta·x) mechanism without a window law |
| C4-ADJ-C | Under H1, lambda_min(L) < 0 for every L >= (1/2) log(T/2·pi) + C(delta), with certified C(delta) from 4.40 (delta = 0.49) to 313.17 (delta = 0.01), i.e. of order (2.1 to 3.1)/delta | THEOREM (finiteness; certified constants on finite T-ranges); tail PPS | Search-limited |
| C4-ADJ-BLIND | If P >= a·norm(g)^2 on window L, then W >= (a - 2m[sigma^2(delta,L) + 2·sinh^2(delta·L)/T])·norm(g)^2 at every height T | THEOREM | Search-limited |
| C4-ADJ-INV | Window positivity excludes single defects under H1 in explicit ranges. Beyond T_PT, the first informative window at delta = 0.49 is L = 6.49 | THEOREM plus NUMERICAL-RIGOROUS | Contrapositive of C4-B |
| C5-L0, L1, L2, T1, T2 | Parametrisation of curve-type polynomials; place-count bounds; mod-2 criterion; one Gram matrix; RH iff T_N >= 0 for all N | THEOREM (C5-T1 modulo IMPORTED intersection theory) | Largely classical in spirit |
| C5-T3 (confluent) | inertia(T_N) = (d - m, m, N - d) for N >= d, with no squarefree hypothesis; RH iff T_(2g) >= 0 | THEOREM (skeptic's confluent proof, re-derived) | Rank statement as in Suzuki Prop. 4.3 under RH |
| C5-ADJ-W | Over F_q, with no RH and no Euler product assumed: Weil positivity on C_c^inf(-a, a) holds iff T_(ceil(2a/h)) >= 0. RH holds iff positivity holds for one (every) a > (d-1)h/2, in particular a > (g - 1/2) log q | THEOREM | Suzuki's fibre identity with RH removed; novelty not asserted |
| C5-ADJ-SHARP | The threshold (g - 1/2) log q is attained in the formal class for 20 of 24 tested (q, g). Example: q = 3, P = 1 - T^2 - 7T^3 - 3T^4 + 27T^6, with inertia (5,0,0) at N = 5, (5,1,0) at N = 6, and first Hasse-Weil violation at k = 28 | THEOREM (computer-assisted, exact) | Search-limited |
| C5-ADJ-LOG | There is L_0 with Pos(L) implying RH for every L >= L_0 | THEOREM (trivial, non-constructive) | Trivial |
| C5-ADJ-MODEL | For any real multiset R_0 with square-summable transforms on window L, adjoining the lattice (pi/L)Z and an off-line quadruple with delta <= 1/(4L) keeps W >= 0.35·L·norm(u)^2 on L^2(-L, L) | THEOREM (counting error O(T)); the O(1) refinement is PPS | **Not claimed new** (uncertainty principle; cf. Bombieri 2000 Thms 10-11) |
| C5-SK-ASYM, C5-S1, C5-D1 | Over F_q a lower one-sided bound forces RH and the upper does not; over Q either one-sided bound suffices (Landau); the uniform tensor-power strip is equivalent to RH | THEOREM | Likely folklore / classical / trivial |

### 7.2 Rigorous computations

All are NUMERICAL-RIGOROUS unless marked.
- **EXP-0001:** 100,000 Arb-certified zeta zeros, maximum radius 1.7·10^-24 (evidence_audit Sec. 1).
- **Davenport-Heilbronn:** exactly 5 off-line zeros with |t| <= 300, the lowest at 0.80851718245663738555 + 85.69934848537759217193i (C2-03, C2-04).
- **Epstein x^2 + 5y^2:** exactly 35 off-line zeros with |t| <= 200, the lowest at height 15.6682495.... Zeros with sigma > 1 at t about 1193.946 and 4108.108, each certified twice independently. That 1193.95 is the *lowest* is NUMERICAL-NONRIGOROUS (screen for t <= 4200).
- **Other zeros:** zeta_19 has a zero with Re = 1.0010955... at t about 600884.2. H_t has certified non-real zeros at t = -20 and t = -50.
- **Farmer's X_10:** real-rooted Jensen polynomials for d <= 119 and non-real zeros from d = 120 on, by three implementations.
- **De Branges failures:** 15,567 among the first 10^5 zeros, with 1000-zero blocks up to n_0 = 10^10.
- **Mertens values:** M(7766842813) = 50286 and M(10^10) = -33722.
- **Function-field census:** 16,354 admissible and 12,787 fakes over 24 pairs (q, g); with the degenerate Z = 1 included, 16,368 and 12,801. Exact inertia checks on 3,300 cases.
- **C4 witnesses:** eight Arb-certified test functions on which the injection-model form is negative; seven of them detect below the Nyquist window, in both models (C4-ADJ-WIT; model statements). The eighth (add_T1e3_d0.01, L - L_N = +0.465) validates a Nyquist-regime float detection.

### 7.3 Audit results (Sec. 6)

- FND-0009: no error found in the inspected portions of the 11/12 paper.
- FND-0004: one proof-step error, repaired.
- FND-0010: no issue found in four Siegel proofs.
- FND-0003: independent reproduction of the 4.896 chain, plus one corrected table entry.
- FND-0001, -0002, -0012, -0013, -0014 as in Sec. 6.
- CRIT23-D: Arb enclosures of every AF/LZ constant, and the exact KN rationals.

### 7.4 Observatory-proposed results with one verifier (not adjudicated)

- CON-0032 T1, an unconditional non-constructive refutation of "Beurling plus integer regularity implies RH" for beta > 2/5.
- CON-0021, the Nyman-Beurling decay law.
- CON-0006 (a)-(b).
- CON-0025, an exact scan.
- CON-0038 (A).

These are proposals. Before any of them is cited outside the Observatory, it needs adjudication or human review.

---

## 8. Conjectures and connections that failed testing, and why

### 8.1 The refuted Nyquist heuristic (C4)

- **The brief's heuristic.** A Weil window of half-width L detects an off-line quadruple at height T only if T <~ 2·pi·e^(2L), up to O(log(1/delta)) in L. Equivalently, L must reach about L_N(T) = (1/2) log(T/2·pi).
- **Verdict.** REFUTED for every fixed delta in (0, 1/2) (C4F Sec. 2a, C4-R).
- **Why.**
  - Under the single-defect hypothesis H1, detection occurs at L ~ (1/(2·delta)) log log T = o(L_N(T)) (C4-B, THEOREM).
  - Under H1, uniformly, every L >= L_N(T) + C(delta) detects, with explicit finite C(delta) (C4-ADJ-C).
  - In the lattice model the exact law is L* = min(L_N^+, L_flat) (C4-LAT).
  - For fixed L, the C4-B condition holds up to doubly exponential heights, so no window is height-local for large-delta defects.
- **What survives.** Blindness is proved only in an astronomically thin neighbourhood of the line; between that radius and the C4-B detection range there is no theorem (C4F Sec. 3.6, item 4; gap (a)). With Zhu's unrefereed a = 8.9·10^-18 at L = 0.8 (claimed certified on the geometric side; high precision with an error budget, not directed rounding, per CON-0010), the additive model is blind on every window L <= 0.8 to injected quadruples with delta <= 3.5·10^-9 and T >= 100 (C4-ADJ-BLIND).
- **Rigorous scope.** At T_PT = 3.0002·10^12 the rigorous C4-B window beats Nyquist only for delta > delta* = 0.2354455 (Arb: margin positive at 0.2355, negative at 0.2354; C4F Sec. 1 row 6).
- **Also refuted.**
  - The investigator's "corrected statement", Nyquist locality for near-line defects (kappa < kappa_c), fails as a universal law. Certified collision-model witnesses detect defects with kappa = 0.22, 0.74 and 1.47 at 0.016, 0.386 and 0.486 below L_N, and the additive model detects kappa = 1.86 at 0.159 below L_N (C4-ADJ-WIT).
  - The C4-LAT mirror-pair aside ("take a higher sinc power") is refuted; the mirror term grows with the power.
- **Withdrawn or downgraded.**
  - The C4-H normalised conjecture is a corollary of C4-B.
  - The claims "0 <= c(T)" and "supported by C4-D4" are withdrawn.
  - C4-REL point (2) is withdrawn as guidance for host window families.
  - The C4-P profile values are Rayleigh-Ritz upper bounds 0.3-6% above the infimum, so at most 2 digits are meaningful.

### 8.2 Other refuted, withdrawn or downgraded campaign sentences

- **C1.**
  - "De Bruijn-Newman has no finite RH-implication" is REFUTED: Platt-Trudgian Cor. 2 derives Lambda <= 0.2 from RH up to 2.51·10^12.
  - "Possibly new" for C1-L2 is withdrawn (Oesterle).
  - "Below 0.3% agreement in 24 cases" for the Jensen-heat bridge becomes at most 1.03% over 20 comparable rows. It is an internal consistency check, not a validation.
  - The headline 4·10^23 for Nyman-Beurling becomes 2.1·10^23.
  - "|M(x)| <= m·sqrt(x) is not a consequence of RH" becomes "not known to follow".
- **C2.**
  - The blind-spot sentence ("no RH-false function with an ordinary Dirichlet series, an Euler product and a self-dual functional equation is known") is REFUTED by M10.
  - "A valid proof must use the Euler product" is REFUTED as a necessity claim and is not sufficient either. The valid form is the hitting-set statement.
  - The uniform-in-d Jensen statement for xi~ is downgraded to CONDITIONAL on zeta having finitely many off-line zeros (C2-17a, C2-28a); C2-ADJ-6 repairs it.
  - The investigator's Li thresholds (20857, 7395, 112929, 41098) are withdrawn in favour of 20855, 7477, 112538 and 40908. At n = 7395 the true value is +1.87.
  - "Epstein zeros with sigma > 1 first appear near 3.6·10^6" is withdrawn.
- **C3.**
  - The mechanism sentence "phase-locking with no arithmetic reason" is withdrawn and replaced by C3-ADJ-S.
  - "Strictly stronger than RH" becomes "sufficient and unconditionally false".
  - The first "ceiling" item is withdrawn: it is a record, not a theorem.
  - Version counts are removed from failure mode F15.
- **C5.**
  - "Over Q no finite window can suffice" (in C5-T3, OB2(c), ML-E1 and the assessment) is REFUTED as literally stated. It is a logical error, by C5-ADJ-LOG.
  - The OB9 decay law exp(-L·e^L) is REFUTED. The data give -ln lambda_min ~ c·e^(2L) with c about 12.
  - "Cannot even give the PNT" overstated Pritsker.
  - The 41 "undecided" census cases are non-admissible.

### 8.3 Connections that failed or were corrected

- **CON-0022 (vocabulary_only).** Siegel's 1932 R(s) is not constrained by the 2026 theorem without an open attribution lemma, and the tests are vacuous below gamma about 1.6·10^5.
- **Refuted sub-claims inside 19 corrected proposals** (strongest_connections.md Sec. 5.2). For example:
  - the Artin threshold 0.5466 (CON-0020);
  - "degree 3 gives nothing" and the target 0.4170 (CON-0011, CON-0035);
  - "exactly circular" (CON-0014);
  - the "law" (CON-0031);
  - the Robin cap at 2.169·10^25 (CON-0003);
  - Zhu "certified" (CON-0010). The verifier labels Pos(0.8) high-precision computation with an error budget, not directed rounding.
- **Bridge.** 12 items are relation_overstated (strongest_connections.md Sec. 5.3).
- **Transplants shown not to work** (cross_field_opportunities.md Sec. 5):
  - generic sextic sieves;
  - mollified moments plus extraction (proven mollifier lengths 4/7 and 17/33 against the 4/3 needed for 7/8; CON-0031);
  - higher traces at X ~ T;
  - Jensen polynomials;
  - the Landau-Pintz method;
  - pretentious methods;
  - Deligne's positivity engine, which yields Ramanujan, not RH;
  - Weil windows via pointwise envelopes;
  - the Siegel polynomial method for complex zeros.

### 8.4 Earlier archive texts superseded by the FINAL adjudications

- The campaign index (proposals/independent_campaigns/README.md) describes C2, C4 and C5 as unadjudicated. All five now have a FINAL.md.
- AC-21 (function-field Weil criterion on one window without RH) is now THEOREM C5-ADJ-W. AC-28 (the rectangular Epstein threshold) is now THEOREM C2-ADJ-2. D-23's "window corollary is a PPS" is superseded.
- UQ-I2 (does a small off-line displacement survive positivity on every fixed window in abstract zero classes?) is answered affirmatively by C5-ADJ-MODEL: with counting error O(T) as a THEOREM, and with error O(1) as a PPS.
- UQ-D5 (blindness below L_N) is answered in part.
  - Height-uniform blindness is proved only for astronomically small delta (C4-ADJ-BLIND).
  - Certified detection below L_N occurs in both injection models (C4-ADJ-WIT).
  - A general blindness theorem remains open.
- C2-14 is upgraded from CONDITIONAL to THEOREM. The completeness of the Davenport-Heilbronn and Epstein zero lists is upgraded to NUMERICAL-RIGOROUS.
- known_obstructions.md OB-18(d) and ranked_research_directions.md Sec. 3 call the Nyquist-locality replacement "not established". C4F makes it **REFUTED as a universal law**.

### 8.5 Literature conjectures that failed, for context

| Conjecture | Status | Source |
|---|---|---|
| Mertens' |M(x)| < sqrt(x) | Refuted (1985); first counterexample below exp(1.96·10^19) | LED-ARITH-9 |
| Polya's L(x) <= 0 and Turan's T(x) >= 0 | Refuted (Haselgrove 1958) | C3F D7 |
| Turan's partial-sum hypothesis | Refuted; zeta_N zero-free in sigma > 1 iff N <= 18 or N = 20, 21, 28 | C3F D5 |
| de Branges' positivity conditions | False | C3F D1; FND-0013 |
| Cramer's model as a law | Contradicted (Maier) | C3F D8 |
| Stieltjes' M(x) = O(sqrt(x)) | **Open**: believed false, not refuted | C3F D6 |

---

## 9. The 25 most promising actionable research problems

The companion file `final_synthesis/top_25_research_opportunities.md` is written by another agent from the same sources. The list below uses the archive's stable identifiers (D-, AC-, UQ-, CON- and campaign ids) so the two lists can be matched item by item. Where wording or order differs, the identifiers' source records govern, and the campaign FINAL files govern over everything else. Each item gives: **statement** (exact, with its status), **why** it matters, and **next step**.

### A. Verification gates (they bound the status of everything citing 2026 claims)

1. **Kernel replay of the formal 2026 statements** (D-01; UQ-A1, A2, A4, A14).
   - *Statement:* replay `QuasiRiemannHypothesis` (zeta(s) != 0 for 7/8 < Re s), `DirichletSevenEighths`, `HeckeSevenEighths` and `SiegelZeros` at github.com/openai/math@4eaee875. Use comparator, an independent kernel and `#print axioms`.
   - *Why:* a pass certifies the zeta and Dirichlet 7/8 statements, hence 11/12 a fortiori, independently of the exposition (QRH-D Sec. 1.3).
   - *Next step:* obtain explicit permission to build third-party code. Prove that the custom Hecke `LFunction` equals its Dirichlet series on Re s > 1. Audit the 199-page 7/8 manuscript to the depth of FND-0009.
2. **A human-checkable proof of 11/12** (D-02; UQ-A3, B7).
   - *Statement:* verify the imports of paper2's Proposition 3.1 and its load-bearing step, Prop. 6.2 plus Lemma 6.3 as used in Lemma 6.6 (QRH-D smallest remaining gap and Sec. 1.2), including:
     - Dunn-Radziwill's transcription of Patterson's Theorem 8.1 and of the Kubota multiplier (c/a)_3, against Patterson 1977 itself;
     - Goldmakher-Louvel Theorem 1.1 for the family used;
     - the multiplier case analysis and Lemma 6.3;
     - the Lemma B.2 constants.
   - *Next step:* write the half-page proof that Radziwill reports [S] and list its minimal imports.
3. **A falsification handle for Proposition 3.1** (D-04; AC-01; UQ-B6).
   - *Statement:* as a separate theorem, #{u_0 ~ U : L(s, nu·chi_.(u_0)) has a detectable zero with beta >= sigma} is at most U^(2 - 2·sigma + eps).
   - *Why:* this is the density-hypothesis-strength shadow of Prop. 3.1 [O]. A numerical violation would falsify it.
   - *Next step:* prove the implication, then test it on small sextic families.
4. **One Siegel-exclusion core to version-of-record standard** (D-03; UQ-A9, A10).
   - *Statement:* a human-refereed proof of one core: OAI/Banks Lemma 3 with Lemma 7, Kerr Lemma 5 with Masser's Theorem 1 (mu >= 4/3), or Guo Proposition 3.1.
   - *Next step:* replay the `SiegelZeros` Lean and Kimura's checks, and replay the Lu-Zaman-Zhao run behind Banks' all-q constant.
5. **Close the residues of the two-thirds audit** (D-09; UQ-A5 to A8).
   - *Statement:*
     - a second review of the P1-F1 repair, tr G~ = N(I) + O(X^(1/2) L);
     - an independent directed-rounding replay of Knausgard's three branch-and-bound inequalities, the only gap between 0.6735382 and the audited 0.6725007;
     - a line-by-line write-up of the BGSTB24 error terms on the LZ route;
     - a replay of zeta-23-lean v1.0.

### B. Quasi-RH: extensions and limits

6. **Architecture floors as theorems** (D-10; UQ-B4, B10).
   - *Statement:* prove that in the extraction architecture h >= 1 is forced for sextic rows, so beta >= 11/12. Prove that the 7/8 comparison system cannot go below 2/3 without changing the direct estimate. Or exhibit an architecture reaching a half-plane left of 3/4.
   - *Status:* both are currently [O] sketches (QRH-D Sec. 4).
7. **The quartic row mean square J4** (D-19; AC-03; UQ-B2, A15).
   - *Statement:* for K = Q(i) and A_u(X) = sum over (n, 1+i) = 1 of mu_K(n)·(u/n)_4·W(N(n)/X), show that the sum over 0 < N(u) <= X^h of |A_u(X)|^2 is at most X^(1+h+eps) for some 1 <= h <= 10/9. This gives zeta != 0 on Re s > 1/2 + 3h/8 (CON-0038).
   - *Next step:* test whether the angular-weight-1 quartic Kubota coefficients satisfy a mu-removal identity analogous to paper2's (eq:gj). Have an independent reader re-derive the transcription of Ji's six inequalities.
8. **The order-3 route** (D-13; UQ-B3).
   - *Statement:* square-root cancellation for Mobius-weighted cubic Gauss sums with a suitable angular twist over Q(sqrt(-3)). This is a Patterson-type statement for mu·g~, and it would give 5/6 by the short route (QRH-D Sec. 4.3, (C2)).
   - *Next step:* small-scale numerics of the twisted sums, and a search for the angular factor that kills the Patterson bias.
9. **Conjecture G** (D-20; AC-02; UQ-B8; CON-0037 corrected).
   - *Statement* (CONJECTURE, [O]): every unitary Hecke character of Q(sqrt(-3)), of any infinity type, has L(s, psi) != 0 on Re s > 11/12. This includes L(E, s) for the curves y^2 = x^3 + D.
   - *Next step:* verify Proposition 3.1 at angular frequency m = l - 1.
10. **The Beurling frontier** (D-26; AC-27; UQ-B11, B12; CON-0032).
    - *Statement:* construct an [alpha, beta]-system with alpha >= 2/3 and beta < 1/2, or prove that none exists. Determine A(beta) = sup{alpha : an [alpha, beta]-system exists} for beta < 1/2. Write T2 as a lemma under QRH(Theta).
    - *Why:* this is the only region in which integer regularity could still matter for 7/8 and 11/12.

### C. Critical-line counting

11. **Beyond the bandwidth-one ceiling** (D-07; UQ-C1 to C4).
    - *Statement:* prove unconditionally that liminf N_0^s(T)/N(T) > 0.6819.
    - *Why:* any proof needs an input beyond bandwidth one. Candidates are unconditional upper information on F(alpha) for some alpha > 1, third-trace information at X ~ T, or an inertia-compatible use of F >= 0 off [-1, 1].
12. **An RH-free 19/27** (D-14; AC-11; UQ-C5, C6; CON-0006).
    - *Statement (ML-CGG):* the sum over T < gamma <= 2T with beta != 1/2 of |B·zeta'(rho) - B·zeta'(1 - conj(rho))|^2 is o(T (log T)^3), for the BHB mollifier with theta -> 1/2. This gives liminf N*/N >= 19/27 without RH.
    - *Next step:* find the largest explicit eta for which |beta - 1/2| <= eta/(log T)^(3/2), combined with Conrey's "99.9% within 8/L", beats 0.6818.
13. **Transfer to GL(2)** (D-11, D-12; AC-09, AC-10; UQ-C9, C10).
    - *Statement:* (a) for one fixed newform, the all-zeros pair-sum asymptotic for Fourier support < 1/2, which gives liminf N_d/N >= 0.4617; (b) the explicit Petersson diagonal lemma for X <= N^(1-eps), which gives harmonic averages >= 0.6725 (simple critical) and >= 0.8363 (distinct).

### D. Weil positivity and windows

14. **Weil positivity on a window containing the prime 2** (D-16; UQ-A11, D1).
    - *Statement:* (a) an independent directed-rounding replay of Zhu's lambda*(0.8) >= 8.9·10^-18; (b) a proof, without computer certification of the continuum infimum, of Pos(L_1) for some L_1 > (log 2)/2.
    - *Why:* it would be the first extension of proved Weil positivity beyond Yoshida's window by a mechanism.
15. **Semilocal positivity at lambda^2 = 3 (ML-C1)** (D-28; UQ-D2; C5F Sec. 5).
    - *Statement:* with S = {infinity, 2}, the semilocal operator framework proves Weil's inequality for h = h_1 * h_2, with h_1 supported in (3^(-1/2), 3^(1/2)) and both half-moments zero (Connes-Consani Conjecture 4.1 at q = 3).
    - *Next step:* identify ker u(F)_22 with the semilocal Sonin space, explicitly with prolate functions.
16. **Two-sided Weil-window detection** (D-33; AC-19, AC-20; UQ-D5 to D7; C4F Sec. 6).
    - *Statement:* (a) the blindness half: bound the local resolvent D(T, delta, L) = lambda_max(E_w*(P + 2·E_u·E_u*)^(-1)·E_w) above for T >= (1 + c)·2·pi·e^(2L). (b) The detection half: replace C(delta) ~ 2.5/delta by O(log(1/delta)) under H1, using an interpolating Paley-Wiener function at full saturation. (c) Remove H1 for far defects.
    - *Next step:* certify one positive lower bound for an injection-model form just below a float threshold.
17. **An effective finite reduction over Q** (C5F Sec. 5 EFR and Sec. 9.3).
    - *Statement:* find an explicit L_0 and a proof, not assuming RH, that Pos(L_0) implies RH. By C5-ADJ-MODEL this must use prime-side structure.
    - *Model question:* in the class of symmetric zero multisets with N(T) = theta(T)/pi + O(log T), determine the detection horizon L*(delta, T). Is it O(1/delta + log T)?
    - *Over F_q (quick projects):* prove "g = 1 is admissible iff -q <= a <= q + 1" for all q, and measure the share of fakes that need the full window.

### E. Criteria and horizons

18. **A Nicolas/Robin implication theorem** (D-15; AC-16; UQ-G5).
    - *Statement:* RH(T) implies Nicolas' inequality for x <= X(T), with X(T) ~ c·T^2/log^2 T and all truncation terms explicit.
    - *Why:* any X(T_0) >= 3.0·10^13 makes the Morrill-Platt Robin range a corollary of Platt-Trudgian (C1F Sec. 8.3).
19. **Semi-local Li in both directions** (UQ-F1, F2; D-34; AC-14).
    - *Statement:* (a) the converse: lambda_1, ..., lambda_N >= 0 implies there is no zero with beta != 1/2 and |gamma| <= c·sqrt(N), up to logarithms, repairing Brown's Theorem 2. (b) RH(T) implies lambda_n > 0 for n <= c·T^2 log T with explicit c > 0. At T_0, even c = 1 lifts the horizon from 9.0·10^24 to about 2.6·10^26.
20. **The Jensen-heat bridge with error control** (D-29; AC-15; UQ-F3).
    - *Statement:* J^(d,0) of xi is hyperbolic near X = T^2 iff H_t is real-rooted near 2T at t = T^2/(2d), up to O(T^3/d^2).
    - *First test:* Arb-certify the smallest non-hyperbolic degree for xi~ (non-rigorous value d = 40 for the quadruple at (0.9, 5)), reusing C1's certified pipeline and monotonicity lemma (C2F Sec. 7.1; C1-ADJ-MONO).
21. **De Bruijn-Newman: explicit scaling and persistence** (D-17, D-25; AC-17; UQ-F8, F9, A12, A13).
    - *Statement:* (a) if all zeros with 0 < gamma <= T lie on the line, then Lambda <= A/log T for T >= T_0, with explicit A about 5. (b) zeta(1/2 + delta + i·gamma) = 0 implies Lambda >= c·delta^2/(log gamma)^2 (CON-0008). (c) Complete the Polymath15 row-2 canopy verification, and replay one 2026 bound below 0.2.

### F. Other routes and infrastructure

22. **Failures of the de Branges zero condition** (D-32; AC-18; UQ-E1, E2).
    - *Statement:* S(gamma_n) - delta_n lies in (3/4, 7/4) mod 2 for infinitely many n, or for a positive proportion of n (C3-ADJ-S). Also conjecture C3-ADJ-RATE, that the failure proportion tends to 1/2.
    - *Next step:* adapt Trudgian's positive-proportion proof for failures of Gram's law to zeros. The cheap test is the blocks near n = 10^11 and 10^12, predicted at about 0.23 and 0.24.
23. **Zero density at the Guth-Maynard bottleneck** (D-36; UQ-H1).
    - *Statement:* for 1-bounded Dirichlet polynomials, LV(sigma, tau) < tau + 1 - 2·sigma near (7/10, 13/10), i.e. |W| <= N^(9/10 - delta) at sigma = 7/10 and T = N^(13/10). This gives sup A < 30/13 and the PNT in intervals of length x^(17/30 - delta'').
24. **A mechanized countermodel pre-review filter** (D-08; C2F Sec. 4, Sec. 7.5; C3F Sec. 6, Sec. 9.8).
    - *Statement:* a tool that tags each step of a proposed argument with the predicates P1-P11 it uses. It runs the step on Davenport-Heilbronn, Epstein, zeta_19, xi~ and M10 with their certified zeros, and flags any step whose predicate set is satisfied by an RH-false member.
    - *Companion mathematics:* classify the elements of S#_1 with an Euler product and Lambda_F >= 0. Either an RH-false example exists, or the class reduces to Dirichlet L-functions.
25. **Effective consequences of Siegel exclusion, and the limits of the method** (D-06, D-24; CON-0025; UQ-H7, H8).
    - *Statement:* (a) a third replay of the exponent-2 class-group scan, and a check of Kimura's Lean statement of Proposition 9. (b) Can an interpolation-determinant method uniformly exclude exceptional zeros for GL(2) or Rankin-Selberg families? (c) Can any comparison of Guo-Lemma-5.1 type certify c >= 1/5, or is 3 - 2·sqrt(2) the ceiling of the present shape?

**Next tier, not listed above:**
- D-18 and D-21: conditional consequences of a half-plane, written as lemmas.
- D-22, D-27, D-30 and D-31: host-programme items.
- D-35: Riemann-Roch on the square of the scaling site. Its significance is high and its tractability very low (ML-W0).
- UQ-A17: independent replication of RH(3·10^12) and an extension to height 10^13.
- UQ-G4: Robin for 22-free n.
- UQ-G6: a certified limsup M(x)/sqrt(x) >= 2.

---

## 10. What a team of very capable mathematicians and AI agents should work on first, and why

**First, the verification gates** (problems 1 to 5). They are cheap relative to their value, and every downstream item depends on them.
- The frontier changed in 2026, and the changes rest on unrefereed claims. The archive's own audits are AI audits, and the producers and checkers come from correlated model families (quality/limitations.md, "Verification limits" 4).
- A team should pair one human expert with independent agents on each claim:
  - Lean replays with an independent kernel and statement-fidelity checks (problem 1);
  - a human check of the Patterson-Kubota imports behind 11/12 (problem 2);
  - one Siegel core taken to version of record (problem 4);
  - the residues of the 2/3 audit (problem 5).
- Until these pass, no document should cite 11/12, 7/8, 2/3 or Siegel exclusion as a theorem (UQ, priority digest).
- The same discipline applies to the Observatory's own campaign results that bear on published work: C2-ADJ-2 (the BST conjecture), the Liu-Wu failing step, and C3-ADJ-S should receive human review before any external citation (C2F Sec. 7.8).

**Second, turn method limits into theorems** (problems 6, 10 and 11, and the floors in Sec. 2.2).
- The decade's most distinctive output is the method-limit literature (EVO Sec. 12). The 2026 methods arrived with their own floors:
  - 11/12 for sextic extraction;
  - above 2/3 for the 7/8 system;
  - about 0.6818 for bandwidth-one counting;
  - c of order 10^-2 for Siegel.
- These are currently author-stated or [O] sketches. Proving them as theorems tells a team where *not* to spend effort, and exactly which new input each route needs.
- CON-0032 and CON-0038 show the pattern: precise obstruction maps that name the single missing ingredient.

**Third, the most leveraged genuinely weaker infinite statements.** Each uses arithmetic structure that passes the hitting-set test, and each has a named next lemma:
- the quartic mu-removal identity and J4 (problem 7), the only route to an OpenAI-independent half-plane;
- a counting input beyond bandwidth one (problem 11), or the RH-free 19/27 (problem 12);
- the Guth-Maynard bottleneck at sigma = 7/10 (problem 23), the refereed frontier;
- a mechanism for positivity on a window containing the prime 2 (problems 14 and 15), the first step past Yoshida's window.

The second and third items are where human ideas are scarcest. AI agents are already effective at the exponent bookkeeping and certified numerics around them: CON-0038's floor computation, C4's Arb witnesses, C5's exact census.

**Fourth, infrastructure that protects all routes:**
- the countermodel pre-review filter (problem 24);
- certified-computation conventions: label every number as a ball, an exact integer or floating point, and check that winding contours close exactly (C2F A1);
- a machine-readable dependency graph of explicit constants, which would catch erratum chains such as Ramare to Dusart (LED-ARITH-19).

**What to avoid, on the archive's adjudicated evidence:**
- larger criterion computations as tests of RH beyond T_0 (C1F Sec. 4-5);
- "Nyquist locality" as a design rule for window families (C4F, REFUTED);
- heat-flow arguments with room to spare (Rodgers-Tao);
- formal transfer of function-field proofs (C5-E1);
- Hilbert-Polya realizations without a positivity source (OB-25);
- reading proportion theorems as progress toward "all zeros" (CON-0030).

**Why this order.** Every RH-equivalent route ends in a positivity statement for which no number-field source exists (Sec. 5, obstacle 2; C5F Sec. 6). The archive offers no route to RH. The realistic gains are of four kinds:
- (i) certainty about the 2026 claims;
- (ii) theorems that locate the next missing input;
- (iii) weaker infinite theorems built on arithmetic structure that countermodels lack;
- (iv) one mechanism-level positivity result past the prime-free window.

The long conceptual bet, a Riemann-Roch or effectivity source of positivity on Spec Z (ML-W0), should be staffed, but as a minority effort. Its smallest model case would re-derive a positivity that is already known (C5F, smallest remaining gap).

---

## 11. What this archive does NOT establish

- **Nothing about RH.** RH is open. No item proves or disproves it, and nothing here is evidence for or against it beyond the cited finite or conditional content (README; quality/limitations.md).
- **No 2026 claim is a theorem.**
  - "No error found" (FND-0009, FND-0010) means no error was found by AI agents in the inspected portions. It is not a referee report.
  - The 7/8 manuscript was not audited.
  - No Lean development was built or replayed: the session's safety policy blocked building third-party code (audits/lean_replay/README.md).
  - The imported metaplectic and large-sieve inputs were not re-proved.
- **No campaign theorem has had human review.** "THEOREM" means a complete proof re-derived by AI skeptics and adjudicators. Several such theorems rest on imported inputs read only at L0 or L0+:
  - Trudgian's S(t) bound for C4-B;
  - Csordas-Varga for C2-14;
  - Craven-Csordas-Smith for C2-ADJ-6.
- **Novelty is search-limited.** MathSciNet, OpenAlex and Semantic Scholar were not used. Bateman-Grosswald 1964, Oesterle's typescript and several classical primary texts were not accessed.
- **Detection and blindness statements are model statements.** C4-B and C4-ADJ-C assume a single off-line quadruple (H1). The injection models are synthetic. No lower bound (non-detection) on any threshold is certified, except the astronomically thin C4-ADJ-BLIND radius.
- **The finite computations imply nothing global.** This covers 100,000 certified zeros, certified countermodel zeros, de Branges failure counts and window witnesses.
- **The corpus is not complete.**
  - 846 of the 1,000 works have index-level records only.
  - 78 of 232 Level-1 targets had no legitimate open full text.
  - Russian, Japanese and Chinese literature is under-covered.
  - Family G (failed claims) is capped by design.
- **The bridge licenses no change to the host repository.** Its mappings are proposals for the host's own review:
  - a Galerkin upper section is not a lower certificate;
  - a family identity is not extraction of the principal member;
  - fixed-P61 control is not growing-prime control (strongest_connections.md Sec. 4.4).
- **The unresolved items are not errors.** FND-0005 and FND-0011 are open questions for expert review only.

