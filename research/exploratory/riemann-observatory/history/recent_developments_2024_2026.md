# Recent developments in RH-related research, 2024-01-01 to 2026-11-17

```text
Status: EXPLORATORY / IMPORTED (literature scan; no new RH claim; RH remains open)
Scope: stratum S7 (2024-01-01 .. 2026-11-17); works on zeta/L-function zeros, zero-free regions,
       zero density, Siegel zeros, Mobius/Liouville cancellation, Gauss-sum moments, criteria,
       spectral approaches, and the 2026 AI-generated claims
Exact sources or dependencies: corpus/recent_2024_2026_scan.jsonl (140 records); arXiv API;
       Crossref API; local read-only clone of the OpenAI math release (commit 4eaee8754);
       secondary web sources labelled as such
What was actually run: 71 arXiv API keyword/author/title queries (>= 3.5 s apart) plus id_list
       re-verification of all 102 arXiv ids (title and first-submission date matched);
       13 Crossref lookups (12 usable); reading of OpenAI CONTENTS.md, history.md, README files,
       lean/docs, formalization.yaml, Comparator statement, first pages / LaTeX of the
       relevant manuscripts; 10 web pages fetched. No code from the OpenAI release was run;
       no Lean project was compiled.
Smallest remaining gap: no record here exceeds evidence level L0/L0+ (index/abstract) except
       the OpenAI quasi-RH and Siegel manuscripts, whose statements and proof outlines were
       read (partial L1). No proof was checked.
```

## 1. What changed, in one paragraph

Three things changed between 2024 and November 2026. First, a refereed analytic advance: Guth and Maynard's large-value estimate for Dirichlet polynomials (arXiv:2405.20552; Annals 2026) gave the first improvement of Ingham's zero-density bound at σ = 3/4 in about 80 years, N(σ,T) ≤ T^{30(1−σ)/13+o(1)}, with primes in all intervals of length x^{17/30+o(1)}. Second, in August–October 2026 the unconditional proportion of zeta zeros that are simple and on the critical line rose from about 41% to 2/3 (0.6725). An AI system (Claude) found the first proof, and Lamzouri gave an independent human proof. Third, on 6 October 2026 OpenAI released AI-generated manuscripts. They claim a fixed zero-free half-plane Re s > 7/8 for every Dirichlet L-function, which is the quasi-Riemann hypothesis (QRH), with an 11/12 companion. A separate, short argument claims to exclude Landau–Siegel zeros. None of the 2026 claims is refereed. None of them bears directly on zeros at Re s = 1/2: the Riemann hypothesis remains open.

## 2. Refereed results (journal-published in or near the window)

| Work | Result | Venue |
|---|---|---|
| Guth–Maynard, arXiv:2405.20552 | N(σ,T) ≤ T^{30(1−σ)/13+o(1)}; PNT in short intervals x^{17/30+o(1)} | Ann. of Math. 203 (2026), doi:10.4007/annals.2026.203.2.6 |
| Dunn–Radziwiłł, arXiv:2109.07463 | Patterson's cubic Gauss-sum bias conjecture, **conditional on GRH** | Ann. of Math. 200 (2024), doi:10.4007/annals.2024.200.3.3 |
| Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh, arXiv:2306.04799 | Unconditional form of Montgomery's pair-correlation theorem | Acta Arith. 214 (2024) |
| Goldston–Lee–Schettler–Suriajaya, arXiv:2503.15449 | Pair-correlation conjecture alone (no RH) ⇒ 100% of zeros simple and critical | Mathematika (2026) |
| Matomäki–Radziwiłł–Shao–Tao–Teräväinen, arXiv:2411.05770 | Higher uniformity of Λ, μ, d_k in almost all short intervals | Invent. Math. (2026) |
| Pilatte, arXiv:2310.19357 | Σ λ(n)λ(n+1)/n ≪ (log x)^{1−c} | J. Amer. Math. Soc. (2026) |
| Gafni–Tao, arXiv:2505.24017 | Exceptional sets for PNT in short intervals from zero density | Ess. Number Th. 5 (2026) |
| Blomer–Thorner, arXiv:2410.17158 | Zero density near the critical line in GL(m) families | Trans. AMS (2026) |
| Arguin–Hamdan, arXiv:2405.06474 | Upper bound of the Fyodorov–Hiary–Keating conjecture on mesoscopic intervals | Ann. Probab. (2026) |
| Lu–Zaman–Zhao, arXiv:2602.03626 | No real zero ≥ 1 − 1/(5 log q) for quadratic characters, q ≤ 10^10 (computation) | Math. Comp., doi:10.1090/mcom/4268 |
| Maynard–Pratt; Thorner; Basak–Thorner–Zaharescu; Benli–Goel–Twiss–Zaman; Jaskari–Sachpazis; Dunn; Connes–Consani–Moscovici; Loeffler–Stoll; LeClair | Half-isolated zeros; exceptional zeros in higher rank; explicit Deuring–Heilbronn; Chowla under a Siegel zero; metaplectic large sieve; prolate operators; Mathlib zeta/L-functions with a formal RH statement; spectral-flow criterion | IMRN, IMRN, ANT, PAMS, MPCPS, ANT, AFA, AFM, ATMP |

Publication status comes from the arXiv journal_ref/DOI or Crossref. A journal record is bibliographic evidence (L0), not an audit.

## 3. Unrefereed human preprints that matter

- **Moments and large values:** de Faveri–Pandey (2610.01035) give ∫|ζ|^6 ≪ T^{5/4−1/60+ε} and the first improvement since Hardy–Littlewood on large values ≥ T^{1/8}. Maynard–Pandey–Radziwiłł (2608.14777) improve Vinogradov's exponent N^{4/5} to N^{19/24} for minor-arc prime exponential sums. Tao–Trudgian–Yang (2501.16779) give a systematic exponent database.
- **Zero density, q-aspect and short intervals:** Chen–Gupta–Li (2507.08296) reach exponent 7/3 for Dirichlet L. Matomäki–Pandey–Pliego–Teräväinen–Wang (2610.09567) show μ cancels in all intervals [X, X+X^{19/35+ε}].
- **Zero-free regions:** Bellotti–Trudgian–Yang (2603.21490) give an explicit region 1 − 1/(4.896 log t). Fiori–Jaskari (2609.23222) give an explicit PNT error bound. Thorner (2608.12257) and Thorner–Zhao (2601.04189) treat Siegel-type regions and exceptional zeros in higher rank.
- **Critical-line follow-ups (human):** Lamzouri (2609.02882) gives an independent proof of the 2/3 bound. Lamzouri (2610.26841) shows at least 13/20 of zeros are isolated. Lamzouri (2611.14486) gives an unconditional small-gap constant 0.7892. Cobeli–Zaharescu (2610.23467) show more than 8/9 of zeros are simple or critical. B. Wang (2609.24167) shows the method is near its limit. Pearce-Crump (2609.15329) reaches 6.78% by Selberg's method alone. Conrey–Kwan–Lin–Turnage-Butterbaugh (2607.00282) show at least 1/9 of zeros are critical for twisted PGL(3).
- **Criteria and spectral work:** Connes's survey (2602.04022) and Andrews–Connes–La Gatta (2611.13129) study finite Weil-form ground states that reproduce zeros numerically. Suzuki (2610.32704, 2606.09096, 2610.41115) studies Weil-form operators, conditional on RH or in function fields. Ono (2610.38870) proves asymptotic Jensen–Pólya hyperbolicity for Dedekind zeta. Liu–Mao (2610.04972) prove infinite log-concavity of the ξ Taylor coefficients, an RH consequence proved unconditionally. Zhu (2608.24827) proves finite-window Weil positivity by certified computation. Kim–Nguyen (2502.21021) bound the first Mertens counterexample by about exp(1.96·10^19). None of these advances RH beyond finite or conditional statements.
- **de Bruijn–Newman:** Planat–Raymond (2611.06245) claim Λ < 0.156821 with a large unrefereed certificate. Freire et al. (2610.27343) give Λ_L ≤ 0.2978 for real characters of conductor ≤ 400. Both remain unverified here.

## 4. AI-generated or AI-discovered claims (unrefereed; kept separate)

### 4.1 OpenAI math release (local clone, commit 4eaee8754; 721 manuscripts, 373 families)

| Manuscript (date) | Claim | Lean (per release) |
|---|---|---|
| Quasi-RH 7/8 (2026-09-30) | Every finite-order Hecke L over Q(√−3) and every Dirichlet L, ζ included, has no zero in Re s > 7/8. Method: two-stage comparison of reflected and Poisson-summed completed cubic-theta sums with 1/L. | **Yes.** The Comparator statement is `riemannZeta s ≠ 0` for 7/8 < Re s, with standard axioms only. We did not compile it. |
| Quasi-RH 11/12 (2026-10-05) | The same families are zero-free in Re s > 11/12. Stated corollaries: effective PNT in arithmetic progressions with error x^{11/12} log x, Vinogradov's least-nonresidue conjecture, an effective class-number bound, and Euler's idoneal list. Human-edited. | No |
| Uniform exclusion of Landau–Siegel zeros (2026-10-01) | (1−β) log q ≥ c (absolute c) for real zeros of real primitive L(s,χ). Interpolation determinants in Q(√d,√2), independent of QRH. | Yes (no explicit c) |
| Primitive roots, all admissible bases (2026-10-04) | Uniform zero-free strip Re s > 1−10^{−6} for all finite-order Hecke L over cyclotomic F ⊇ μ12; infinitude in Artin's conjecture for every admissible base | No |
| Dependants | Deterministic polynomial factorization over F_p uses the cyclotomic strip as a black box. Power saving for polynomial differences at primes uses 7/8. Simultaneous primitive roots is explicitly conditional. | No |
| Related number theory | Ordinary two-point Chowla / binary corrected Elliott (Lean). Unconditional Patterson first moment for cubic Gauss sums (Lean). μ(p−1)=1 infinitely often. Poisson–Dirichlet law for p−1. Joint Dickman law (Lean). Ostmann (Lean). Large prime gaps (Lean). Jacobsthal (Lean). Totients (Lean). Gaussian moat (Lean). Squarefree quartics (Lean). Catalan's constant irrational (Lean). Goldfeld density and mean rank. Function-field generic Ramanujan. Ramanujan graphs. GOE universality for regular graphs. | as marked |

`history.md` records no withdrawal or revision of any number-theory manuscript. The October 2026 withdrawals concern Hodge-type papers only. The release README calls the collection "raw research data" and says that "some of the unformalized results could have issues". In family 182, only the square-difference paper is formalized, not the prime-argument paper that depends on 7/8.

### 4.2 Anthropic / Claude: two thirds of zeros simple and critical

Alpöge–Furman (arXiv:2608.13637; comment: "Proof discovered autonomously by Claude (Anthropic); verified and communicated by the listed authors"; Lean formalization claimed) prove the following unconditionally: ≥ 2/3 of zeros are simple and on the critical line, and ≥ 5/6 are distinct. With the Montgomery–Taylor window the constants are 0.6725 and 0.8362. The mechanism is a rank–trace inequality on a finite compression of Weil's Hermitian form, which replaces RH in Montgomery's 1973 argument. Verification within the producing company is not independent. Independent support comes from Lamzouri's human proof (2609.02882), Arias de Reyna's exposition (2610.24612), and refinements by Knausgård (2610.08965: 0.67353 and 0.83900; Lean with three axioms recording search-program outputs; self-described AI-assisted).

### 4.3 Other AI-assisted items

These include Ben Green's Siegel-zero variant (hexagonmath.org 2610.00311v2: "arguments all due to ChatGPT", human-written text), Kimura's unconditional class-number ≤ 2000 table (2610.21511, AI contributions disclosed, Lean), and Ono's AxiomProver-autoformalized theorem.

## 5. Human follow-ups to the OpenAI claims (all unrefereed)

- **Re-proofs of Siegel-zero exclusion:** Banks (2610.15483) gives explicit constants, (1−β) log q ≥ 3.0·10^{−3} for q ≥ 10^{10}, and all q ≥ 3 via Lu–Zaman–Zhao. Kerr (2610.21099) gives a simpler proof. Guo (2610.30476) gives an elementary proof with c = 1/100. Banks (2610.31402) works over a base field and derives an effective Brauer–Siegel theorem.
- **Numerical refinements of 7/8, conditional on OpenAI inputs:** Liu (2610.12234) reaches 0.874957, with Lean claimed. Xu–Sang (2610.15291) reach 0.8748867. Liu (2610.26835) reaches 0.874887 for every number field. Chang–Wang (2611.00924) reach 0.874462. Ji (2611.16665) reaches 599/600 via quartic Gauss sums over Q(i).
- **Consumers of QRH:** Goldbach exceptional sets (Pintz–Althöfer 2610.15559; Li–Liu 2610.26756); class groups and Chebotarev (Frei–Sofos–Widmer 2610.18491); Euclidean rings (Grobner 2610.24900); 3-sphere recognition in coNP (Baldwin–Sivek 2611.06705); the Gauss sphere problem (Bellotti–Kerr 2610.29636); de Bruijn–Newman Λ ≤ 0.13963 assuming 7/8 (2610.12803); primes in (x, x+x^{7/8}) (Visser 2610.20058).
- **Unlocated dependency:** several papers (2611.09031, 2611.02280, 2610.37179, 2610.18491) cite a quasi-RH for Dedekind zeta functions "announced by Cureton and Thorner". No arXiv record was found in this scan, and it is not in the JSONL.

## 6. Expert reception (secondary sources; quotations as reported, not independently confirmed)

- **Quanta, 2026-10-19.** Experts "largely agree" that the 11/12 proof is correct. Write-ups of 7–13 pages are circulating privately, and the 199-page 7/8 paper "has been set aside". Radziwiłł calls the implications "staggering" but the papers "horribly written". Sarnak will not regard it as "a Theorem" until humans check all details. Sawin expects RH to remain as far off as before.
- **Tao, 2026-10-19.** "The Siegel zero problem has been solved in a number of ways". The analytic QRH arguments are "still in the process of being fully digested". He sketches Green's formulation.
- **Quanta, 2026-11-05.** Reports the race to simplify the Siegel-zero proof (Green, Kerr, Barreto, Pescador–Barreto–van Dijk) and quotes Granville: "It's all moot now".
- **Community infrastructure.** A guest post on Tao's blog (2026-10-24) announces `oai-math-revised` for rewriting the OpenAI write-ups. The organizers of an 11-15 January Hausdorff Center (Bonn) retreat, announced 2026-10-30, refer to "the recently established proof of the quasi Riemann Hypothesis". This is evidence of adoption, not of refereeing.
- **Two thirds result.** A guest post by Turnage-Butterbaugh on Tao's blog (2026-10-22) presents the 2/3 bound (Claude/Alpöge–Furman; Lamzouri) and stresses that even 100% would not prove RH. Anthropic's own page (2026-08-10) gives the provenance; it is a company source.

## 7. What did not change (boundaries for this archive)

- RH and GRH are open. QRH, a half-plane Re s > θ with θ < 1, says nothing about zeros near Re s = 1/2. Experts quoted above do not expect the metaplectic method to reach 1/2.
- Proportion results, even at 100%, do not imply RH. 2/3 is a lower density statement.
- Finite computations do not prove infinite statements. Examples are Weil positivity on bounded windows, Lu–Zaman–Zhao up to 10^10, de Bruijn–Newman certificates, and numerical Weil ground states.
- Lean claims attest that a formal statement was checked against Mathlib definitions by the producer. The Observatory compiled nothing. Where a claim states extra axioms (Knausgård), the kernel does not check those inputs.
- Yitang Zhang's 2022 Landau–Siegel preprint (arXiv:2211.02515) lies outside this window and was not re-assessed.

## 8. Limitations of this scan

- **Index coverage.** The arXiv keyword search is incomplete, and items without the queried phrases may be missed. zbMATH, OpenAlex, Semantic Scholar and MathSciNet were not used for this stratum.
- **Unopened sources.** Scientific American coverage was seen only through search snippets and is not cited. The `oai-math-revised` repository was not accessible from this session.
- **Evidence level.** Records are at evidence level L0/L0+. Claims are paraphrased from abstracts or first pages and must not be read as audits.
- **Selection.** The family-G sample is deliberately minimal: one unrefereed disproof claim and one self-withdrawn proof. Many 2024–2026 arXiv "proofs" of RH were seen in the `ti:"Riemann hypothesis"` listing and were not catalogued.
