# Consolidated Literature Boundary Audit — Two-Programme Pass

Date: 2026-08-30
Scope: consolidation of 9 structured area audits covering planned claims C1–C6.
Areas audited: (A1) Ihara/graph zetas and graph RH; (A2) Epstein zetas / Eisenstein series zero behavior; (A3) Selberg-class rigidity and converse theorems; (A4) Davenport–Heilbronn functions and linear combinations of L-functions; (A5) coefficient/local-parameter transforms and defect factorizations; (A6) Beurling generalized primes; (A7) hypercomplex/algebra-valued zeta extensions; (A8) reconstruction of algebraic structure from trace data; (A9) cross-cutting comparative zeta taxonomy (surveys, databases, counterexample compendia).

---

## 1. Collision-risk table for claims C1–C6

Worst verdict per claim across all areas that audited it, with severity and detail. Verdicts used: COLLIDES (claim substantially published), PARTIAL_OVERLAP (content known, packaging/certification new), UNKNOWN (no auditor could certify either way).

| Claim | Worst verdict | Severity | Source of worst verdict | One-line summary |
|---|---|---|---|---|
| C1 — cross-world machine-readable survival matrix (L0–L9 ladder, mechanism axes, exact witness per cell) | COLLIDES (on the FE-solution-space/pencil framing sub-claim); PARTIAL_OVERLAP on the matrix artifact itself | High for framing, moderate for artifact | A4 (DH audit); A1, A2, A3, A5, A6, A9 concur partial_overlap | Every cell's mathematics is classical and the comparative-table idea exists (Terras "zeta dictionary" tables; Selberg-class surveys; LMFDB). The FE-solution-space framing of the DH row is standard converse-theorem territory and may not be claimed. New: the unified cross-ontology schema, survival ladder, per-cell certified witnesses, machine-readability of axiom FAILURE. |
| C2 — axiom-independence table with exact finite separating model per proper subset (non-Ramanujan witnesses + Sturm certificates) | PARTIAL_OVERLAP (unanimous), with a false-as-stated flag | High | A1, A3, A5, A6, A9 | Every individual separation is folklore-to-textbook (non-Ramanujan graphs: Ihara/Stark–Terras/Terras 2010; DH 1936; Beurling DMV 2006). "Exact finite model" is FALSE for Beurling rows (constructions are infinite/probabilistic). "Model-theoretic" reads as a formal-logic overclaim unless axioms are formalized over one signature. New: subset-lattice completeness, witnessed/empty-by-theorem/open trichotomy, machine-checkable Sturm certificates. |
| C3 — refusal-capable trace-to-object detector; Möbius local data as trace of nilpotent non-semisimple local system, purity the failing axiom | COLLIDES (reconstruction engine C3-i); Möbius claim untenable as literally stated | High (correctness risk, not just novelty risk) | A8 (trace audit); A2, A3, A5, A9 concur partial_overlap on the rest | Kronecker 1881 + Berlekamp–Massey + Ho–Kalman are the entire engine — classical. No finite matrix has tr(M^k) = mu(p^k) (power sums (−1,0,0,…) force all-zero eigenvalues, contradiction); Brauer–Nesbitt: trace data can NEVER certify non-semisimplicity. Function-field contrast (sum mu(f) T^{deg f} = (1−T)(1−qT), pure) shows EFFECTIVITY, not purity, is the convention-invariant failing axiom. New: assembled refusal pipeline with named-first-failure semantics. |
| C4 — transform-survival grammar with exact defect Euler products; iff-effectivity criterion | PARTIAL_OVERLAP, with a false-as-stated flag on the criterion | High (correctness + attribution risk) | A5 (transforms audit); A3, A9 concur | Defect extraction is classical practice (Rankin–Selberg/Shimura zeta(2s); Moreno–Shahidi; lambda-ring/plethysm formalism). The survival criterion at the meromorphy level is essentially Kurokawa's theorem (1978/1986, after Estermann 1928/Dahlquist 1952). As literally stated the iff is FALSE: virtual non-effective defects (e.g. zeta(s)/zeta(2s)) retain full meromorphic continuation — they lose entirety, not continuation. Newton–Thorne 2021 makes the effective direction a THEOREM for holomorphic GL(2) newforms. New: three-stratum trichotomy (entire / meromorphic-with-infinite-poles / natural boundary) as one criterion + mechanized defect tables. |
| C5 — certified zero-bifurcation atlas for Epstein zetas over lattice moduli | PARTIAL_OVERLAP — highest phenomenon-level collision of the pass | Very high | A2 (Epstein audit); A4, A5, A3, A9 concur | The core phenomenon is published: Arenstorf–Brewer 1993 tracked Epstein zero MOTION; Betermin–Samaj–Travenec (arXiv:2110.09368) and Travenec–Samaj (arXiv:1909.07112) already deliver critical-zero curves, MERGING at "edge zeros", off-critical branches connecting edge-zero pairs, and singular (phase-transition) expansions — for one-parameter rectangular/hypercubic families; McPhedran et al. track lattice-sum zero trajectories; boundary asymptotics known (Bateman–Grosswald, Stark, Chowla–Selberg + Bombieri–Hejhal at CM, Gonek–Lee/Lamzouri counts, Rezvyakova 2024/26). New and defensible: (a) two-parameter atlas over the full SL2(Z)\H fundamental domain, (b) argument-principle/interval CERTIFICATION, (c) k-indexed global stratification, (d) correlation with CM distance / shortest vector / cusp height. |
| C6 — collapse theorem for zeta over finite-dimensional commutative real algebras | PARTIAL_OVERLAP, borderline COLLIDES in substance | Moderate | A7 (hypercomplex audit); A2, A3, A5, A9 concur | The semisimple half is published: Rochon 2004 bicomplex zeta (idempotent split, bicomplex RH ⇔ classical RH — literally "nothing new is carried"); multicomplex zetas ditto. Nilpotent/jet half is classical (Clifford 1873 dual numbers; automatic differentiation). General collapse of function theory over such algebras is classical (Scheffers 1893 → Ketchum 1928 → Lorch 1943 → Plaksa–Shpakivskyi 2015). New: the assembled no-go theorem for zeta over ARBITRARY such algebras, A-valued completed zeta/FE with jet bookkeeping, real-residue-field subtleties, and the refined boundary (slice-regular quaternionic is ALSO rigid — novelty needs non-slice noncommutative theories or infinite dimension). |

### Per-claim detail

**C1.** Seven areas returned partial_overlap on the matrix; the DH audit returned COLLIDES on the framing sub-claim that DH lives in the 2-dimensional FE-solution space spanned by L(s,chi5), L(s,chi5-bar) with a self-dual pencil — this is exactly how Hamburger 1921 / Hecke 1936 / Bochner / Chandrasekharan–Narasimhan converse theory, Kaczorowski–Perelli's degree-1 classification (Acta Math. 1999), Bombieri–Hejhal 1995, and Bombieri–Ghosh 2011 already present it. The Terras-school "zeta dictionary" tables (Stark–Terras 1996–2007; Terras 2010 book) are the direct ancestor of the cross-world comparison and must be cited as such. LMFDB is the machine-readable prior artifact (genuine L-functions only, no axiom-failure schema — cite and contrast). Genre precedent for witness-per-cell matrices: Steen–Seebach / pi-Base, Complexity Zoo, House of Graphs (never instantiated for zeta axiomatics — citing them strengthens the claim). The Beurling FE cell must be recorded "no known witness; impossibility OPEN" (Hilberdink–Lapidus 2006 characterization; Lapidus dual-membrane conjecture) — recording "FE impossible" would be a false claim. "Wrong gamma completion" witnesses are instances of Kaczorowski–Perelli invariant theory + KP VII (no degree in (1,2)) and must credit that mechanism; import Knopp-style anti-rigidity so hypotheses are honest.

**C2.** Unanimous partial_overlap. Known separations that may not be claimed: EP+FE+trace formula without RH (any non-Ramanujan graph; the equivalence "graph RH iff Ramanujan" is standard from Ihara 1966 onward and stated with failing examples in Terras 2010 — even graph rationality can be added, strengthening the cell); FE without EP (DH 1936; Epstein h>1); EP without FE and dVP-optimality (Diamond–Montgomery–Vorhauer 2006); RH without integer regularity (Zhang 2007; Broucke–Debruyne–Vindas 2021); PNT without M(x)=o(x) (Debruyne–Diamond–Vindas); graph PNT without graph RH (Horton–Stark–Terras). Dependence theorems close cells and MUST be recorded as provably empty: Hamburger 1921; Conrey–Ghosh no degree in (0,1); KP degree-1 classification; KP VII no degree in (1,2); Weil converse theorems. Sturm-sequence certification is classical computational algebra (present as certification engineering). The census arXiv:1905.13485 (cubic Ramanujan graphs ≤ 20 vertices) partially collides with "exact small non-Ramanujan witnesses" — cross-check before claiming minimality; the session-verified 14-vertex bridged cubic witness and prism-family threshold (C_n x K_2 non-Ramanujan iff n ≥ 16, witness eigenvalue 1+sqrt(2+sqrt(2))) are clean matrix rows but minimality is NOT established. The table cannot separate the full axiom set from the critical-line conclusion — that is RH; say so.

**C3.** The engine COLLIDES (Kronecker 1881; Berlekamp–Massey 1968–69; Ho–Kalman 1966; gfun/Guess held-out validation practice); trace-to-char-poly on L-data is standard closing practice of point counting (Kedlaya–Sutherland 2008; Harvey). Refusal-per-named-criterion exists in three strands: Honda–Tate/DiPippo–Howe Weil-polynomial recognition; Farmer–Koutsoliotas–Lemurell FE-consistency refusal; Dold/Puri–Ward realizability congruences. The Möbius phrasing must be repaired: (i) no finite matrix realizes mu(p^k) as literal traces; (ii) Brauer–Nesbitt makes "non-semisimple" a property of the minimal Hankel REALIZATION, never of the object; (iii) in the det convention mu-data is a PURE weight-0 virtual (odd-parity) object — over F_q[t] literally (1−T)(1−qT) — so the invariant failure is EFFECTIVITY/parity, not purity; (iv) honest newforms already fail naive purity at Steinberg primes (Weil–Deligne monodromy), so purity failure alone cannot flag counterfeits. The pass's own code (core/reconstruct.py: A1 FINITE_RANK holds with (1−T)/1, A2 EFFECTIVITY fails) is the defensible phrasing — match the prose to the code. Adjacent conceptual ancestors: 1/zeta not in Selberg class; virtual/negative-multiplicity motive folklore (Kurokawa, Deninger, F1 literature); Sarnak Möbius randomness.

**C4.** Partial_overlap with correctness risk. Prior art by layer: (1) defect extraction — Rankin–Selberg/Shimura 1975, Moreno–Shahidi 1983, and the general lambda-ring/plethysm Schur-functor factorization (Knutson, Serre, Borger, Ramachandran); (2) survival dichotomy — Estermann 1928 / Dahlquist 1952 (constant local factors) and KUROKAWA 1978/1986 (Artin and automorphic type): non-cyclotomic-like (non-integer-virtual) defect implies natural boundary — the pass's criterion at the meromorphy level essentially IS Kurokawa's theorem, extended multivariably by Bhowmik–Essouabri–Lichtin and Delabarre; (3) effective direction — Langlands functoriality, proved for sym^n of holomorphic newforms (Gelbart–Jacquet; Kim–Shahidi; Kim; Newton–Thorne 2021), with Kim–Shahidi cuspidality criteria as exactly "survives as primitive iff defect trivial"; conceptual source: Langlands' Beyond Endoscopy (nonnegative pole multiplicities); (4) non-effective direction — open in general; Booker 2003 (Annals) is the model theorem (non-automorphic 2-dim Artin implies infinitely many poles); tied to Selberg orthogonality/zero-cancellation (Conrey–Ghosh); (5) fractional multiplicities — Selberg–Delange branch-point stratum. Restate the criterion as a trichotomy (effective ⇒ entire-up-to-finitely-many-poles [theorem where functoriality is known]; virtual non-effective ⇒ meromorphic with infinitely many poles [conjectural, reduces to zero-cancellation]; non-virtual ⇒ natural boundary [Kurokawa]) and present classical identities as regression tests, not findings. KP linear/nonlinear twist calculus is the existing Selberg-class transform theory — import, don't rederive.

**C5.** Highest phenomenon-level collision. Published: zero motion (Arenstorf–Brewer 1993; Hejhal ICM 1986 numerics); the full collision/edge-zero/off-critical-branch mechanism with singular expansions, one-parameter (Travenec–Samaj arXiv:1909.07112 / AMC 2021 hypercubic; Betermin–Samaj–Travenec arXiv:2110.09368 2D rectangular); lattice-sum trajectories (McPhedran et al. arXiv:1601.01724 series); pencil-homotopy zero tracking as an algorithm (Balanzario–Sánchez-Ortiz 2007); cusp asymptotics (Bateman–Grosswald 1964: real zero in (1/2,1) for y ≳ 7.0055; Stark 1967: on-line regularly spaced zeros, gap ~ pi/log y); CM fibers (Chowla–Selberg decomposition into Hecke L-functions; Hejhal 1986; Bombieri–Hejhal 1995 conditional almost-all-on-line); counts (Voronin; Gonek–Lee ~cT off-line; Lamzouri arXiv:1907.06387; Lee near-line cTlogT arXiv:2010.10490; Rezvyakova arXiv:2411.18492 positive proportion on-line, unconditional). Absent from the literature (the defensible core): (a) two-parameter bifurcation LOCI over the full fundamental domain (all prior work is one-parameter slices); (b) certification (all prior numerics are uncertified floating point); (c) k-indexed global stratification/topology of the off-line locus; (d) quantitative correlation with CM distance, systole/shortest vector, cusp height; (e) behavior along non-CM geodesics / generic transcendental z (no literature found). Retitle/reframe C5 around (a)–(e), crediting the mechanism to Samaj–Travenec(–Betermin) and the trajectory idea to Arenstorf–Brewer. EpsteinLib (arXiv:2412.16317) for evaluation.

**C6.** Borderline collides in substance. Rochon 2004 (Tokyo J. Math., confirmed via Project Euclid) IS the collapse statement for the bicomplex algebra: idempotent decomposition, bicomplex Euler product, bicomplex RH equivalent to classical RH. Multicomplex versions exist (~2013 paper; arXiv:1601.04785). Bicomplex Hurwitz/gamma/Dirichlet strand exists (low-confidence attributions). General mechanism classical: Scheffers 1893, Ketchum 1928, Lorch 1943, Price 1991, Plaksa–Shpakivskyi arXiv:1503.07134. Slice-regular quaternionic theory (Gentili–Struppa; Colombo–Gentili–Sabadini–Struppa arXiv:0905.1861) shows the quaternionic slice route is ALSO rigid (sphere-zeros through conjugate pairs) — so "noncommutativity" alone is not the right boundary: honest boundary is "non-slice noncommutative theories (Fueter/monogenic — cite Krausshar's Clifford-valued Eisenstein/Epstein series as existing content there) or infinite dimension" and cite Connes' noncommutative program as the live boundary case. What is apparently unrecorded: the general theorem for arbitrary finite-dimensional commutative real A with FE/jet bookkeeping (differentiated FE mixing zeta, zeta', Gamma'/Gamma), real-residue-field factors (hyperbolic numbers, R[eps]), zero-divisor/continuation subtleties, and the debunking corollary against "hypercomplex RH proofs" (e.g. the non-credible 2025 MDPI Symmetry quaternionic paper). Frame as folklore-assembling no-go proposition; do not oversell.

---

## 2. Per-area known-results map

Confidence levels are the auditors' own (high/medium/low). Attributions marked "approximate" or "unverified" by auditors are flagged.

### A1 — Ihara/graph zetas and graph RH (audited C1, C2)
- Ihara determinant formula for (q+1)-regular graphs — Ihara 1966; graph reinterpretation Serre/Sunada mid-1980s. [high]
- Bass's theorem (three-term determinant formula, arbitrary graphs); alt. proofs Stark–Terras 1996, Foata–Zeilberger ~1999, Kotani–Sunada 2000. [high]
- Hashimoto non-backtracking edge matrix formulation; non-normality of B is where purity/unitarity fails. — Hashimoto ~1989. [high]
- Graph RH ⇔ Ramanujan; full "zeta dictionary" tables in Stark–Terras trilogy (1996/2000/2007) and Terras 2010 book. [high]
- Folklore separation: regular graph zetas have Euler product, FE, Selberg-type trace formula (Ahumada ~1987; Terras–Wallace ~2003; Horton–Newland–Terras), and Weil-style RATIONALITY, yet RH fails exactly for non-Ramanujan graphs; stated in prose, never as a formal independence table. [high]
- Graph PNT holds for ALL finite connected graphs regardless of graph RH (known PNT-without-RH separation); irregular graphs generically fail naive RH (Kotani–Sunada 2000; Horton–Stark–Terras 2006; Horton thesis ~2006). [medium]
- Explicit Ramanujan families: LPS/Margulis 1988; Chiu 1992 (cubic); Morgenstern 1994; MSS 2015 bipartite all degrees. [high]
- Density: Friedman 2008 (Alon conjecture); Bordenave ~2020; Huang–McKenzie–Yau arXiv:2412.20263 — random d-regular graph exactly Ramanujan with probability → ~69% (Tracy–Widom mass). [high]
- Census of cubic Ramanujan graphs ≤ 20 vertices exists (arXiv:1905.13485; authors unverified); minimal non-Ramanujan cubic order not confirmed. [low]
- Session-verified: 14-vertex bridged cubic graph non-Ramanujan (exact integer charpoly, lambda_2 in (2.85,2.9) > 2sqrt2); 10- and 12-vertex analogues Ramanujan; prism C_n x K_2 non-Ramanujan iff n ≥ 16, algebraic witness 1+sqrt(2+sqrt(2)) ≈ 2.8478. Minimality NOT established. [high, session-computed]
- DH 1936 + Balanzario–Sánchez-Ortiz ~2007 computed off-line zeros; Selberg-class axiom analyses (Conrey–Ghosh 1993; KP ~1999–2011; Perelli surveys). [high]
- Beurling engineered counterexample tradition (Diamond–Montgomery–Vorhauer ~2006; Broucke–Debruyne–Vindas). [medium]
- LMFDB machine-readable cross-object data (no graph zetas, no counterfeits, no axiom-survival framing); Farmer–Pitale–Ryan–Schmidt axiomatization ~2019 (venue/year medium confidence). [medium]

### A2 — Epstein zetas / Eisenstein series zero behavior (audited C5 primarily; all claims)
- Potter–Titchmarsh ~1935: infinitely many on-line zeros; early off-line zeros for h > 1. [high]
- Davenport–Heilbronn 1936: zeros with Re(s) > 1 for h(d) > 1 forms and for Hurwitz zeta (rational a ≠ 1/2,1; transcendental a). [high]
- Bateman–Grosswald 1964: real zero in (1/2,1) for y ≳ 7.0055; asymptotics of real zeros as y → ∞. [high]
- Stark ~1967: for large y all zeros in a growing region are on-line except real ones, regularly spaced gap ~ pi/log y. [medium]
- Selberg–Chowla ~1967: CM decomposition into Hecke L-functions via class-group characters; Chowla–Selberg formula. [high]
- Hejhal ICM 1986: large-scale numerics/heuristics, zeros close to but off the line, close pairs. [high]
- Bombieri–Hejhal 1995: conditionally, almost all zeros of linear combinations of independent Euler products on-line and simple ("carrier wave" mechanism). [high]
- Voronin ~1976–80: >> T on-line zeros unconditionally. [medium]
- Gonek–Lee ~2015–17: ~cT off-line zeros for h > 1; Lamzouri ~2019 improvement (arXiv:1907.06387). [medium]
- Rezvyakova arXiv:2411.18492 / Izv. Math. 90:2 (2026): positive proportion of zeros on-line, unconditional. [high]
- Lee / Ki density-near-line results (arXiv:1811.01613 etc.); statements/venues not verified. [low]
- DIRECT PRIOR ART: Arenstorf–Brewer 1993 (motion of zeros of m^2 + y^2 n^2 as y varies; attribution via search, article paywalled). [medium]
- DIRECT PRIOR ART: Betermin–Samaj–Travenec arXiv:2110.09368 and Travenec–Samaj arXiv:1909.07112 / AMC — edge zeros, merging, off-critical branch generation, singular expansions; hypercubic analogue. [high]
- McPhedran et al. "Zeros of lattice sums" series (~2016, arXiv:1601.01724). [medium]
- Sarnak–Strömbergsson ~2006: extremal lattices for Epstein zeta (hexagonal, D4, E8, Leech) — geometric moduli literature (extrema, not zeros). [high]
- Random Epstein zetas zero-free half-plane (arXiv:1305.1333, Södergren school; authors unverified). [low]
- Lagarias–Suzuki ~2005–06: truncated Eisenstein integrals with all zeros on-line; nodal-line literature (Ghosh–Reznikov–Sarnak school). [medium]
- Imports: graph-zeta facts [high]; Beurling engineered systems [medium]; Kronecker/Berlekamp–Massey + 1/zeta Selberg-class folklore [high]; Rochon bicomplex zeta ~2004 [medium].

### A3 — Selberg class rigidity and converse theorems (audited C1–C6 from the FE side)
- Selberg axioms, class S and S# — Selberg 1989/1992. [high]
- Degree 0: F = 1 in S (Conrey–Ghosh); S# degree-0 Dirichlet polynomials classified (KP 1999). [high]
- No degrees in (0,1) (Conrey–Ghosh, precursors Richert/Bochner); no degrees in (1,2) — KP VII, Annals 173 (2011), verified. Degree 2 unclassified. [high]
- Degree-1 classification: zeta and shifted Dirichlet L-functions (KP I, Acta Math. 1999). [high]
- Hamburger 1921–22 uniqueness; fragile — Knopp ~1990s: without growth hypotheses the FE solution space is infinite-dimensional. [high/medium]
- Hecke 1936 correspondence; solution spaces of fixed FE are linear, finite-dimensional for lambda ≤ 2, infinite-dimensional for lambda > 2; Bochner 1951/58, Chandrasekharan–Narasimhan ~1961. [high]
- Weil 1967 converse theorem (twists force modularity); Booker-school degree-2 converse theorems with Selberg-type gamma factors (arXiv:2110.00311; Venkatesh extension, Forum Math. Sigma ~2022). [high]
- Gamma-data non-uniqueness and KP invariants (degree, conductor, xi, root number, H-invariants); forbidden conductors (arXiv 2024). [medium]
- DH 1936; Epstein off-line zeros; zero-trajectory prior art (CAMWA 1993; McPhedran; Travenec–Samaj) — surfaced by search. [high/medium]
- Ihara/Bass/Stark–Terras/Terras graph-zeta facts. [high]
- Beurling systems (Beurling 1937; DMV ~2006; Zhang; Broucke–Debruyne–Vindas). [medium]
- Defect factorizations: Rankin–Selberg; Shimura 1975; Kim–Shahidi 2002 / Kim 2003 cuspidality criteria; Newton–Thorne 2021. [high]
- Langlands Beyond Endoscopy (~2004; Venkatesh, Herman, Altug, Arthur) — closest existing formulation of an effectivity criterion. [high]
- KP twist theory (nonlinear twists detect degree/conductor) — existing Selberg-class transform calculus. [high]
- Rochon 2004 bicomplex zeta; multicomplex successors. [high]
- Berlekamp–Massey/Hankel standard in point counting; Farmer–Koutsoliotas–Lemurell numerical FE-fitting. [medium]
- Unique factorization into primitives (Conrey–Ghosh); Selberg orthonormality. [high]

### A4 — Davenport–Heilbronn and linear combinations (audited C1 DH row, FE framing, pencil motion)
- Exact DH construction (combination of conjugate mod-5 L-functions; period-5 coefficients; conductor 5, self-dual FE, no Euler product) — DH 1936; Titchmarsh §10.25; Bombieri–Ghosh 2011. [high]
- Infinitely many zeros with Re(s) > 1, count ~ cT; Hurwitz zeta cases; Cassels ~1961 algebraic irrational a. [high]
- >> T zeros in any off-line substrip (joint universality; Karatsuba–Voronin 1992; Laurinčikas). [medium]
- Critical-line lower bounds: Karatsuba ~1990–91 N_0(T) >> T(log T)^{1/2−eps}; improved 2017 (Steklov; author unverified). [medium]
- Bombieri–Hejhal 1995: conditional 100%-on-line for combinations; carrier-wave mechanism. [high]
- Bombieri–Ghosh 2011: real parts of zeros in Re(s) > 1, sigma*, density conjecture. [high]
- Righetti 2017 (ANT 11): disproved general Bombieri–Ghosh density conjecture; general >> T off-line existence/density for combinations. [high]
- Booker–Thorne ~2014: combinations of cuspidal automorphic L-functions have zeros in Re(s) > 1 unless essentially genuine. [medium]
- Saias–Weingartner ~2009: periodic-coefficient dichotomy. [medium]
- Computed off-line DH zeros: Spira ~1994; Balanzario–Sánchez-Ortiz Math. Comp. 76 (2007) — computed BY deformation/homotopy along a pencil (pencil zero-tracking is their published algorithm). [high]
- Epstein: Potter–Titchmarsh; Bateman–Grosswald; Stark; Y. Lee arXiv:1204.6297 (~cT off-line, real parts dense). [medium]
- Zero motion: Arenstorf–Brewer ~1993; Hejhal ~1986. [medium]
- Travenec–Samaj edge-zero mechanism (1909.07112; 2110.09368) — exactly C5's collision-and-departure mechanism, one-parameter, uncertified. [high]
- McPhedran series ~2016. [medium]
- FE solution spaces classical: Hamburger 1921; Hecke 1936; Bochner; Chandrasekharan–Narasimhan; KP 1999/2011. [high]
- RMT analogue: Barhoumi–Hughes–Najnudel–Nikeghbali arXiv:1301.5144. [medium]
- Near-line counts for combinations: Lee et al. arXiv:2010.10490 (J. Anal. Math. ~2023), arXiv:2311.10285, arXiv:2501.00551. [medium]
- Synthesis caution: DH row must NOT read "no Euler product ⇒ zeros escape in bulk" — off-line zeros are density zero; conditionally 100% on-line. [high]

### A5 — Coefficient/local-parameter transforms; defect factorizations (audited C4 primarily; all claims)
- Rankin–Selberg: sum a_f(n)^2 n^{−s} = zeta(s) L(s, sym^2 f)/zeta(2s); sum a_f(n^2) n^{−s} = L(s, sym^2 f)/zeta(2s) — Rankin 1939, Selberg 1940, Shimura 1975. [high]
- Moreno–Shahidi ~1983: fourth moment of tau via symmetric-power L-functions with explicit correction Euler product. [high]
- Estermann 1928 dichotomy (cyclotomic or natural boundary); Dahlquist 1952 analytic extension. [high]
- KUROKAWA (~1978 announcement; ~1986 Proc. LMS I & II): meromorphy-vs-natural-boundary dichotomy for Artin-type and automorphic-type Euler products — closest existing theorem to C4's criterion. [high]
- Multivariable extensions: Bhowmik–Essouabri–Lichtin ~2007–10; Delabarre; du Sautoy–Woodward ghost polynomials. [medium]
- Lambda-ring/plethysm: any multiplicativity-preserving polynomial transform factors into Schur-functor L-functions — Knutson 1973; Serre; Borger 2009; Ramachandran ~2014–15. [high]
- Selberg–Delange: non-integer powers, branch points, continuation only to zero-free region — Selberg 1954; Delange 1961/71; Tenenbaum. [high]
- Functoriality anchors: Gelbart–Jacquet ~1978; Kim–Shahidi ~2002; Kim ~2003; Newton–Thorne ~2021 (ALL sym^n, holomorphic newforms). [high]
- Non-effective direction: Booker ~2003 (Annals) — non-automorphic 2-dim Artin L has infinitely many poles; Aramata–Brauer; zeta(s)/zeta(2s) keeps continuation with infinitely many poles (virtual non-effective ≠ loss of continuation). [medium]
- Selberg-class structure: unique factorization (conditional); degree classification d < 2; Rankin–Selberg closure OPEN; no classification of coefficient maps preserving membership. [high]
- Counterexample worlds (DH; Potter–Titchmarsh; Beurling/DMV; Weil 1948; non-Ramanujan Ihara zetas). [high]
- Epstein zero-trajectory literature (McPhedran ~2016; Travenec–Samaj ~2019–21; Bombieri–Hejhal; Stark; Sarnak–Strömbergsson). [medium]
- Rochon ~2004 bicomplex zeta; multicomplex. [high]
- Fité–Kedlaya–Rotger–Sutherland ~2012: Sato–Tate moment tables as structure detectors. [high]
- Farmer–Koutsoliotas–Lemurell ~2013–19; Booker numerical verification. [medium]

### A6 — Beurling generalized primes (audited C1/C2 Beurling rows, FE cell)
- Beurling 1937: PNT if N(x) = Ax + O(x log^{−gamma} x), gamma > 3/2; sharp (Diamond ~1970). [high]
- Kahane ~1997: PNT under L2 condition (Bateman–Diamond conjecture); refinements Debruyne–Vindas, arXiv:2012.06220. [high]
- Diamond–Montgomery–Vorhauer 2006 (Math. Annalen 334): dVP zero-free region and PNT error OPTIMAL under Beurling axioms; RH fails badly. [high]
- Zhang ~2007; Broucke–Debruyne–Vindas arXiv:2004.11501: RH-analogue without integer regularity (RH does not imply von Koch in Beurling world). [high]
- Hilberdink ~2005: max(alpha, beta) ≥ 1/2 conservation law. [medium]
- Broucke–Vindas arXiv:2309.01567: well-behaved systems realizing admissible exponent pairs; no FE. [medium]
- PNT-equivalence decoupling: PNT does not imply M(x) = o(x) unconditionally — Debruyne–Diamond–Vindas arXiv:1609.03504; Debruyne–Vindas arXiv:1606.03579; arXiv:2406.00736. [high]
- Chebyshev decoupling: Hall ~1970s; Diamond's L1 conjecture FALSE (Kahane-attributed counterexample); Diamond–Zhang Acta Arith. 160 (2013). [medium]
- Diamond–Zhang monograph, AMS Surveys 213 (2016) — the prose predecessor of any Beurling axiom/conclusion matrix. [high]
- FE STATUS: no non-classical Beurling system with genuine self-dual Riemann-type FE known; no impossibility theorem either. Hilberdink–Lapidus 2006 (arXiv:math/0410270) characterize generalized FEs (theta/modular dual expansion, generically pairing DISTINCT dual systems); Lapidus 2008 fractal-membrane FE conjectural; approximate FEs generally unavailable (Révész series arXiv:2012.09045, 2110.11463, 2207.00665, 2409.10051; Broucke). [medium]
- Selberg-class degree-gap and Hecke–Bochner rigidity as context (does not settle the Beurling case). [medium]
- Complementary witnesses: DH 1936; non-Ramanujan Ihara witnesses. [high]
- Active adjacent field: Bohr's theorem for Beurling systems (Broucke–Kouroupis–Perfekt ~2024); Halász-type (arXiv:1902.03870); functional independence (Axioms ~2025–26). [medium]

### A7 — Hypercomplex / algebra-valued zeta (audited C6 primarily)
- Rochon 2004, Tokyo J. Math. 27, 357–369 (confirmed, Project Euclid): bicomplex zeta via idempotents, bicomplex Euler product, bicomplex RH ⇔ classical RH. [high]
- Price 1991 multicomplex function theory; Segre 1892; Cockle 1848; Luna-Elizarrarás–Shapiro–Struppa–Vajiac ~2015. [high]
- Multicomplex zetas: ~2013 paper (authors unverified); arXiv:1601.04785 multicomplex Dedekind-like zeta = Gaussian-rational components (authors unverified). [medium]
- Bicomplex Hurwitz/gamma/Dirichlet strand (Indian school; authorship unverified). [low]
- General commutative-algebra function theory collapse: Scheffers 1893; Ketchum 1928; Lorch 1943; Plaksa–Shpakivskyi arXiv:1503.07134; Cook A-calculus; dual numbers Clifford 1873 / autodiff. [high]
- Quaternionic: slice-regular theory (Gentili–Struppa ~2006–07; CGSS arXiv:0905.1861) — unique slice-regular extension; zero set = real zeros + 2-spheres through conjugate pairs; a "quaternionic zeta" exists trivially and carries nothing new; slice Dirichlet series possibly Alpay–Colombo–Sabadini (low confidence). [high]
- Genuinely noncommutative content exists: Krausshar ~2000–04, Clifford-valued (monogenic) Eisenstein/Epstein series — prior art on the noncommutative side of C6's boundary. [medium]
- 2025 MDPI Symmetry 17(7):1134 quaternionic "RH proof" — exists, not credible; C6 undercuts the genre. [medium]
- The GENERAL C6 statement (arbitrary finite-dimensional commutative real algebra, zeta + jets, no-go boundary) appears unrecorded; absence claim from 4 searches + training. [medium]

### A8 — Reconstructing structure from trace data (audited C3 primarily)
- Kronecker 1881: finite Hankel rank iff rational; rank = minimal realization dimension. [high]
- Berlekamp ~1968 / Massey 1969; Dornstetter ~1987 Euclid equivalence. [high]
- Ho–Kalman ~1966: minimal realization; finitely supported impulse responses have NILPOTENT minimal state matrices (classical, not a phenomenon). [medium]
- Brauer–Nesbitt ~1937: trace data determines only semisimplification — no trace-only detector can certify non-semisimplicity. [high]
- Weil–Deligne pairs (rho, N), nilpotent monodromy invisible in L-factors; Steinberg primes give naive-purity failure INSIDE the automorphic world — Deligne 1973 Antwerp; Tate Corvallis 1979. [high]
- Honda–Tate + DiPippo–Howe 1998: exact Weil-polynomial membership/refusal test; Kedlaya–Sutherland enumeration. [high]
- Trace-to-char-poly with Weil-bound early termination = standard point-counting closing step (Schoof tradition; Kedlaya–Sutherland ANTS 2008; Harvey ~2014). [high]
- FKRS 2012 (+ arXiv:2106.13759; CRAS 2019): Sato–Tate group recognition from moment statistics with held-out checks. [high]
- Larsen–Pink ~1990: representations from invariant dimensions. [medium]
- FKL arXiv:1502.00850: existence/refusal of L-functions from FE consistency; Selberg-class degree-range refusals. [high]
- Dold ~1983; Puri–Ward ~2001; Byszewski–Graff–Ward ~2021: realizability congruences (exact named-axiom refusal criterion). [medium]
- 1/zeta not in Selberg class; Sarnak Möbius randomness ~2010–11; Müllner ~2017. [medium]
- Function-field Möbius: sum mu(f) T^{deg f} = (1−T)(1−qT) = Z(T)^{−1} — finite rank, PURE, VIRTUAL: effectivity, not purity, is the invariant failing axiom. Rosen 2002 folklore. [medium]
- Deligne interpolation categories Rep(S_t) (2007); Comes–Ostrik ~2011; complex rank invisible to Hankel rank. [high]
- Deninger regularized-determinant program ~1991–94; F1 literature (Soulé, Deitmar, Connes–Consani, Kurokawa, Manin) — no record of the mu(p^k) Hankel observation there. [medium]
- Murmurations (He–Lee–Oliver–Pozdnyakov ~2022): instrument-first precedent on a_p data. [high]
- gfun (Salvy–Zimmermann ~1994); Guess (Kauers ~2009); non-holonomicity refusals (Flajolet–Gerhold–Salvy ~2005). [medium]

### A9 — Cross-cutting comparative taxonomy (audited C1, C2 primarily)
- Selberg axioms + S# as named axiom-subset class; role of each axiom discussed in prose (Selberg ~1992; KP survey ~1999; Perelli ~2004–05; Kaczorowski lecture notes). [high]
- DH 1936 as THE canonical Euler-product-necessity witness (Titchmarsh §10.25; all surveys). [high]
- Epstein h > 1 off-line zeros (Potter–Titchmarsh; DH second paper; Stark; Voronin; Bombieri–Hejhal). [medium]
- Beurling: EP without FE settles that cell (Beurling 1937; DMV ~2006; Zhang; BDV). [high]
- Dependence theorems close cells: Hamburger ~1921; Conrey–Ghosh ~1993; KP 1999–2011; Weil ~1967. An independence table ignoring these is wrong, not incomplete. [high]
- Graph RH iff Ramanujan with named failing examples in print (Stark–Terras I–III; Terras 2010 names specific graphs, e.g. K3 x C10 minus edges). [high]
- Ramanujan existence/density literature (LPS; Margulis; Friedman; MSS; Hoory–Linial–Wigderson survey; Murty survey). [high]
- Deligne mechanism anatomy (EP from point counts, FE from duality, RH from purity/positivity via tensor-power squaring) — standard exposition (Katz 1976; Freitag–Kiehl; Mazur). C1's mechanism axes codify this known anatomy. [high]
- Prose comparative surveys: Conrey Notices ~2003; Bombieri Clay 2000; Sarnak Clay 2004; Gelbart–Miller BAMS 2004; Katz–Sarnak BAMS 1999; Iwaniec–Kowalski Ch. 5. None a matrix; none machine-readable. [high]
- LMFDB (arXiv:1511.04289): closest machine-readable artifact; Selberg-class-scoped; NO axiom-survival schema. [high]
- Genre precedent elsewhere: Steen–Seebach / pi-Base; Complexity Zoo; House of Graphs; "Convexity Zoo" (2026 hit); Watkins's online zeta directory (prose catalogue prior art). Never instantiated for zeta axiomatics. [medium]
- Estermann/Dahlquist/Kurokawa natural-boundary backbone for C4; proved functorial-survival cases. [medium]
- Kronecker/BM for C3 core. [high]
- Scheffers/Ketchum/Price/Rochon for C6. [medium]
- Sarnak–Strömbergsson for C5 moduli side; no published certified bifurcation atlas found. [medium]
- Absence claim: no systematic witness-per-cell axiom matrix, machine-readable or otherwise, known — a genuine but curatorial/infrastructural gap. [medium]

---

## 3. Results to import as matrix rows / anchors

Witness rows (mathematics is prior art; import with citation, attach certificates as the pass's contribution):

1. **DH row** — FE + continuation + self-duality, no Euler product; off-line zeros (even sigma > 1). Witness: Davenport–Heilbronn 1936; computed zeros Spira ~1994, Balanzario–Sánchez-Ortiz 2007 (e.g. near 0.808 + 85.699i). Phrase carefully: off-line zeros are density zero; >> T(log T)^{1/2+...} on-line (Karatsuba); conditionally 100% on-line (Bombieri–Hejhal). Pass contribution: first certificate-grade off-line DH zero.
2. **Non-Ramanujan graph row** — Euler product + FE + trace formula + Weil-style RATIONALITY, graph RH fails. Witness family: any non-Ramanujan regular graph; session-verified 14-vertex bridged cubic (exact integer charpoly given in A1 audit) and prism family C_n x K_2, threshold n = 16, algebraic witness eigenvalue 1 + sqrt(2 + sqrt(2)). Cite Ihara/Bass/Stark–Terras/Terras; cross-check minimality vs arXiv:1905.13485. Pass contribution: Sturm certificates, rationality-strengthened cell, certified minimal order (after enumeration).
3. **Graph PNT-without-RH row** — Horton–Stark–Terras / Kotani–Sunada; certified witness pairing prime-cycle counts with pole locations of a certified non-Ramanujan graph.
4. **Density-of-RH-truth anchor** — Huang–McKenzie–Yau arXiv:2412.20263: random d-regular graph exactly Ramanujan with probability → ~69%. Unique "probability RH holds in a family is a proven constant" row; no number-field analogue.
5. **Beurling rows** — DMV 2006 (dVP optimality; EP + regular integers do not force RH); Zhang 2007 / BDV 2021 (RH without regularity); Debruyne–Diamond–Vindas (PNT without M(x) = o(x)); Hall / Diamond–Zhang (Chebyshev decoupling); Hilberdink max(alpha,beta) ≥ 1/2 as a cross-world conservation row. NOTE: witnesses are infinite/probabilistic constructions — use a two-tier witness taxonomy (finite/exact vs constructive-infinite/citation or certified truncation). FE cell: OPEN, anchored on Hilberdink–Lapidus 2006.
6. **Epstein rows** — h > 1 off-line zeros (Potter–Titchmarsh, DH); cusp asymptotics (Bateman–Grosswald threshold y ≈ 7.0055; Stark spacing ~ pi/log y) as atlas boundary conditions; CM fibers via Chowla–Selberg decomposition + Bombieri–Hejhal model; counts (Gonek–Lee/Lamzouri ~cT off; Rezvyakova positive proportion on, unconditional 2024/26).
7. **Empty cells (dependence theorems)** — Hamburger 1921 (degree-1 zeta FE forces zeta); Conrey–Ghosh (no degree in (0,1)); KP I (degree-1 classification); KP VII (no degree in (1,2)); Weil converse (twists force automorphy); Hecke solution-space dimensions (finite for lambda ≤ 2, infinite for lambda > 2; Knopp anti-rigidity without growth hypotheses). Record trichotomy: witnessed / empty-by-theorem / open.
8. **C4 strata anchors** — Estermann–Dahlquist–Kurokawa dichotomy (natural boundary); zeta(s)/zeta(2s) = sum mu(n)^2 n^{−s} (virtual non-effective, still meromorphic everywhere — the middle stratum's canonical witness); Booker 2003 (non-effective ⇒ infinitely many poles, 2-dim Artin case); Newton–Thorne 2021 (effective direction a theorem for holomorphic GL(2) — an unconditional proved COLUMN of the grammar); Selberg–Delange (fractional stratum); Shimura zeta(2s) defect; Kim–Shahidi cuspidality criteria; Langlands Beyond Endoscopy as conceptual source.
9. **C3 axiom battery anchors** — Kronecker/BM/Ho–Kalman (engine); Brauer–Nesbitt as an explicit NO-GO ROW (trace-only detectors see semisimplifications); Weil-bound early termination (Kedlaya–Sutherland); Honda–Tate/DiPippo–Howe (membership/refusal prototype); FKRS moments (neighboring instrument); FKL FE-consistency (neighboring instrument); Dold/Puri–Ward realizability as a NEW axiom row (A-REALIZABILITY); Steinberg bad-prime witness from an honest newform (e.g. 11a at p = 11, local factor 1 − T) separating monodromy-type purity failure from Möbius-type effectivity failure; function-field Möbius contrast row (1−T)(1−qT).
10. **C6 anchors** — Rochon 2004 (bicomplex RH ⇔ RH = the collapse instance); multicomplex zetas; Scheffers→Plaksa–Shpakivskyi collapse mechanism; Clifford 1873 dual-number jets; slice-regular rigidity (CGSS arXiv:0905.1861); Krausshar monogenic Eisenstein series (the noncommutative boundary has content); Connes' program as the live boundary case.
11. **C5 prior-art anchors to credit** — Arenstorf–Brewer 1993 (trajectory idea); Travenec–Samaj arXiv:1909.07112 + Betermin–Samaj–Travenec arXiv:2110.09368 (edge-zero collision/departure mechanism, singular expansions); McPhedran arXiv:1601.01724 series; Balanzario–Sánchez-Ortiz (pencil-homotopy tracking algorithm); Hejhal ICM 1986; EpsteinLib arXiv:2412.16317 (evaluation); Sarnak–Strömbergsson (moduli geometry).
12. **Schema/genre anchors** — LMFDB (cite and contrast: machine-readable, axiom-failure-blind); Terras zeta-dictionary tables (direct ancestor of cross-world comparison); pi-Base/Steen–Seebach, Complexity Zoo, House of Graphs (genre precedent); Iwaniec–Kowalski Ch. 5 axioms; Katz–Sarnak family axis; Deligne mechanism anatomy (Katz 1976; Freitag–Kiehl) for the mechanism axes.

---

## 4. Recommended citations (deduplicated, by cluster)

Graph zetas / Ramanujan:
- Ihara, J. Math. Soc. Japan 18 (1966). Sunada (~1986). Hashimoto, Adv. Stud. Pure Math. 15 (~1989). Bass, Internat. J. Math. 3 (1992). Kotani–Sunada, J. Math. Sci. Univ. Tokyo 7 (2000). Foata–Zeilberger (~1999).
- Stark–Terras, Advances in Math. I (1996), II (2000), III (2007). Horton–Stark–Terras, Contemp. Math. 415 (2006). Terras, "Zeta Functions of Graphs: A Stroll through the Garden", CUP (2010/2011) — the zeta-dictionary tables C1 must cite as direct ancestor. Ahumada (~1987); Terras–Wallace (~2003).
- Lubotzky–Phillips–Sarnak, Combinatorica 8 (1988); Margulis (1988); Chiu, Combinatorica 12 (1992); Morgenstern (1994); Marcus–Spielman–Srivastava, Annals (2015); Friedman, Memoirs AMS (2008); Bordenave (~2020); Huang–McKenzie–Yau, arXiv:2412.20263; Miller–Novikoff–Sabelli, arXiv:math/0611649; Hoory–Linial–Wigderson, BAMS (2006); Murty survey (2003); arXiv:1905.13485 (census, authors unverified); arXiv:1905.04297.

Selberg class / converse theorems:
- Selberg, Amalfi proceedings (1992). Conrey–Ghosh, Duke (1993). Kaczorowski–Perelli: Acta Math. 182 (1999); Annals 173 (2011) [no 1 < d < 2]; "The Selberg class: a survey" (1999); Perelli surveys I–II (2004–05); invariants papers; forbidden conductors (arXiv 2024); nonlinear-twist calculus (Milan J. Math. ~2010; arXiv:1304.4734; arXiv:1507.07177); converse-theorem survey, Boll. UMI (2016).
- Hamburger (1921–22); Knopp (~1990s); Hecke, Math. Ann. (1936); Bochner (1951/~1958); Chandrasekharan–Narasimhan (~1961); Weil, Math. Ann. (1967); Booker et al. arXiv:2110.00311; Venkatesh-extension converse theorem, Forum Math. Sigma (arXiv:2207.00451).

Davenport–Heilbronn / combinations:
- Davenport–Heilbronn I–II, J. London Math. Soc. (1936). Titchmarsh, 2nd ed., §10.25. Cassels (~1961). Bombieri–Hejhal, Duke 80 (1995). Bombieri–Ghosh, Russian Math. Surveys 66 (2011). Righetti, ANT 11 (2017) (arXiv:1506.05716) + thesis. Booker–Thorne (~2014). Saias–Weingartner (~2009). Spira (~1994). Balanzario–Sánchez-Ortiz, Math. Comp. 76 (2007). Karatsuba (~1990–91; Steklov 2017). Barhoumi–Hughes–Najnudel–Nikeghbali arXiv:1301.5144. Lee et al. arXiv:2010.10490, 2311.10285, 2501.00551. Ferry et al. arXiv:1602.06328.

Epstein / Eisenstein:
- Potter–Titchmarsh (~1935). Bateman–Grosswald (1964). Stark, Mathematika (~1967). Selberg–Chowla (~1967). Hejhal, ICM Berkeley (1986/87). Voronin (~1976–80). Gonek–Lee (~2015–17); Lamzouri arXiv:1907.06387; arXiv:1204.6297 (Y. Lee); arXiv:1811.01613; Rezvyakova arXiv:2411.18492 / Izv. Math. 90:2 (2026).
- PRIMARY C5 COLLISIONS: Arenstorf–Brewer, Comput. Math. Appl. 26(5) (1993); Travenec–Samaj arXiv:1909.07112 / Appl. Math. Comput. (2021–22); Betermin–Samaj–Travenec arXiv:2110.09368; McPhedran et al. arXiv:1601.01724 (+ sequels).
- Sarnak–Strömbergsson, Invent. Math. (~2006). arXiv:1305.1333 (random Epstein, authors unverified). Lagarias–Suzuki arXiv:math/0412039; IMRN sign-changes (~2019). EpsteinLib arXiv:2412.16317. Steuding (~2007, venue unverified).

Beurling:
- Beurling, Acta Math. (1937). Diamond (~1970). Kahane (~1997). Diamond–Montgomery–Vorhauer, Math. Annalen 334 (2006). Zhang (~2007). Broucke–Debruyne–Vindas arXiv:2004.11501. Hilberdink, J. Number Theory (~2005). Hilberdink–Lapidus, Acta Appl. Math. 94 (2006), arXiv:math/0410270. Lapidus, "In Search of the Riemann Zeros" (~2008). Broucke–Vindas arXiv:2309.01567. Debruyne–Diamond–Vindas arXiv:1609.03504; Debruyne–Vindas arXiv:1606.03579; arXiv:2406.00736. Diamond–Zhang, Acta Arith. 160 (2013) + monograph AMS Surveys 213 (2016). Révész (± Broucke) arXiv:2012.09045, 2110.11463, 2207.00665, 2409.10051. Broucke–Kouroupis–Perfekt, Math. Annalen (~2024).

Transforms / defects / functoriality:
- Estermann (~1928); Dahlquist, Ark. Mat. (~1952); Kurokawa, Proc. Japan Acad. (~1978) + Proc. LMS I & II (~1986) + Astérisque 94 (1982) exposition; Bhowmik–Essouabri–Lichtin (~2007–10); Delabarre (arXiv:1001.3838, 1004.0360); du Sautoy–Woodward (~2008).
- Rankin (1939); Selberg (1940); Shimura (1975); Moreno–Shahidi (~1983); Selberg (~1954) + Delange (~1961/71) [Selberg–Delange]; Knutson (1973); Serre N_X(p) (~2012); Borger (~2009); Ramachandran (~2014–15).
- Gelbart–Jacquet (~1978); Kim–Shahidi (2002); Kim (2003); Newton–Thorne, Publ. IHES (2021); Booker, Annals (~2003); Aramata (~1930s)/Brauer (~1947); Langlands, "Beyond Endoscopy" (~2004); Venkatesh (~2004); Herman arXiv:1208.5783; Altug (~2015–20); "Local and global questions beyond endoscopy" arXiv:2310.02438.

Trace reconstruction / detectors:
- Kronecker (1881); Berlekamp (~1968)/Massey (1969); Dornstetter (~1987); Ho–Kalman (~1966); Brauer–Nesbitt (~1937); Deligne, Antwerp II (1973); Tate, Corvallis (1979); Tate (1966)/Honda (1968); DiPippo–Howe (1998); Kedlaya–Sutherland, ANTS VIII (2008); Harvey (~2014); Fité–Kedlaya–Rotger–Sutherland, Compositio (2012) + arXiv:2106.13759 + CRAS (2019); Larsen–Pink (~1990); Farmer–Koutsoliotas–Lemurell arXiv:1502.00850; Dold (~1983); Puri–Ward (~2001); Byszewski–Graff–Ward (~2021); Deligne Rep(S_t) (2007); Comes–Ostrik (~2011); Deninger (~1992; ICM 1994); Soulé (2004); Connes–Consani (~2009–16); Kurokawa absolute zetas (~2005); Sarnak Möbius randomness (~2010–11); Müllner (~2017); Rosen, "Number Theory in Function Fields" (2002); He–Lee–Oliver–Pozdnyakov (~2022); Salvy–Zimmermann gfun (~1994); Kauers Guess (~2009); Flajolet–Gerhold–Salvy (~2005).

Hypercomplex / algebra-valued:
- Rochon, Tokyo J. Math. 27 (2004) — PRIMARY C6 anchor. Price (1991). "A Multicomplex Riemann Zeta Function" (~2013, verify authors). arXiv:1601.04785 (verify authors). Bicomplex Hurwitz strand (verify authors). Scheffers (1893); Ketchum, Trans. AMS (~1928); Lorch, Trans. AMS (~1943); Plaksa–Shpakivskyi arXiv:1503.07134; Clifford (1873). Gentili–Struppa (~2006–07); Colombo–Gentili–Sabadini–Struppa arXiv:0905.1861. Krausshar, Birkhäuser (~2004). MDPI Symmetry 17(7):1134 (2025) — cautionary example only, not a mathematical source.

Cross-cutting / mechanism anatomy / databases:
- Deligne, Weil I (1974), Weil II (1980); Katz, PSPM 28 (1976); Freitag–Kiehl (1988); Mazur (~1970s); Weil (1948).
- Iwaniec–Kowalski, AMS Colloquium 53 (2004), Ch. 5. Katz–Sarnak, BAMS (1999). Conrey, Notices AMS (2003). Bombieri, Clay (2000). Sarnak, Clay (2004). Gelbart–Miller, BAMS (2004).
- LMFDB Collaboration, arXiv:1511.04289; lmfdb.org. Farmer–Pitale–Ryan–Schmidt, Bulletin AMS (~2019, venue unverified).
- Steen–Seebach, "Counterexamples in Topology" (~1978); pi-Base (topology.pi-base.org); Watkins's online zeta directory (~2000s).

---

## 5. Honesty note: web access and reliance on training knowledge

All nine area audits report `web_access: true`. None relied solely on training knowledge; however, web verification was partial and uneven, and the following caveats apply:

- **Verified against live sources during auditing** (high confidence in bibliographic data): Kaczorowski–Perelli VII, Annals 173 (2011) (verified via annals.math.princeton.edu); Rochon 2004 (verified via Project Euclid); the Travenec–Samaj / Betermin–Samaj–Travenec arXiv items; Rezvyakova arXiv:2411.18492 / Izv. Math. 90:2 (2026); Huang–McKenzie–Yau arXiv:2412.20263; most arXiv-numbered items listed with URLs.
- **Surfaced by search but not fully verified**: Arenstorf–Brewer 1993 attribution (article paywalled; authorship via search hit); arXiv:1905.13485 census (authors unverified); arXiv:1601.04785 and the ~2013 multicomplex zeta paper (authorship unverified); arXiv:1305.1333 (authors unverified); the bicomplex Hurwitz strand (authorship from training memory).
- **From training knowledge with approximate years/venues (marked "~" throughout)**: Balanzario–Sánchez-Ortiz (~2007); Foata–Zeilberger (~1999); Ahumada (~1987); Farmer–Pitale–Ryan–Schmidt (~2019, venue unverified); Knopp (~1990s); Hall (~1970s, venue unknown); Voronin's exact references; Ki/Lee exact titles and venues; Steuding (~2007); Karatsuba's 2017 Steklov improvement (author of the improvement unverified); Watkins directory attribution; many "circa" dates in clusters A3, A5, A8, A9. Verify all "~"-dated and "unverified" items before citing in any manuscript.
- **Absence claims** (e.g. "no published axiom-survival matrix", "the general C6 statement is unrecorded", "no CM-distance correlation study exists") rest on a small number of web searches (typically ~4 per auditor) plus training knowledge with cutoff January 2026. Folklore is inherently hard to search; treat every absence claim as medium confidence at best, and re-run targeted searches before submitting novelty claims — especially for C5's correlation layer and C6's general statement.
- **Session-computed results** (A1: 14-vertex non-Ramanujan bridged cubic charpoly; prism threshold n = 16) are verifiable from the stated exact integer polynomials but were produced in-session, not drawn from literature; minimality claims were explicitly NOT established.
