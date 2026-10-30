# Annotated literature catalogue

Search cutoff: **30 October 2026**. Entries distinguish new work, revisions, known imports, and leads with incomplete access. “Primary theorem inspected” means the statement and named parts were read; it is not a completed independent proof review. “Formal admission inspected” identifies an upstream receipt, not a fresh local replay. Proposed uses are this pass's assessment.

## Priority map

| Read first | Why |
|---|---|
| L01 | New external Dirichlet benchmark, admitted and merged today |
| L02–L03 | Yesterday's revisions with directly relevant moment/positivity material |
| L04–L06 | New analytic inputs or optimization mechanisms to test |
| L08–L09 | Relevant techniques with indispensable RH assumptions |
| L10–L12, L17 | Real-zero and effective arithmetic developments |
| L13–L16 | Positivity, formalization, Robin and Gram-method alternatives |
| L18–L22 | Follow-ups and exact maintenance of already known sources |
| L23–L24 | Unverified architecture leads; do not use as theorem inputs |
| L25–L28 | Access-limited leads and background/version corrections |

Each record below has a machine-readable counterpart in [SOURCES.json](SOURCES.json). Exact repository overlaps and follow-up acceptance conditions appear in [REPO_MAP.md](REPO_MAP.md).

## L01 — Dirichlet nonvanishing at 0.87341198 with a selected-norm leaf

**ArviFoxy.** GitHub: GTimG/QuasiRiemannTracker#97; 62b12e08066b0269a01f34696ace896e3cb5eb32. Date for this record: **2026-10-30**.  
**Status:** upstream protected formal admission inspected; not replayed here.  
**Primary sources:** [record](https://github.com/GTimG/QuasiRiemannTracker/pull/97) · [text/source](https://github.com/GTimG/QuasiRiemannTracker/blob/62b12e08066b0269a01f34696ace896e3cb5eb32/submissions/2026-10-30-arvi-selected-leaf/src/Candidate/Main.lean).  
**Inspection:** Live PR API; archived protected receipt; final theorem; frozen canonical target and pinned standard definitions.

The upstream all-moduli theorem excludes zeros for $\Re s>43670599/50000000$, with the principal pole excluded. The contribution combines selected sextic norms with reflected radial estimates and a retuned return. It was merged on 30 October at 07:47:37 UTC.

**Evidence:** the protected admission records PASS for the canonical target with Lean, NanoDa and con-ron; the final export uses the ordinary Dirichlet L-function. Exact hashes and evidence limits are in [TRACKER_EVIDENCE.json](TRACKER_EVIDENCE.json). No kernel run or complete dependency audit was performed here.

**Use:** reconstruct the selected-row estimate before adapting it to #1020/#1023. This replaces the older scalar optimization benchmark for Dirichlet functions; it does not automatically extend the same number to arbitrary Hecke families.

## L02 — Zero-free half-planes for Hecke L-functions over number fields and Quasi-Riemann Hypothesis

**Baiying Liu.** arXiv: 2610.26835; v2. Date for this record: **2026-10-29**.  
**Status:** primary preprint statements and revision sections inspected.  
**Primary sources:** [record](https://arxiv.org/abs/2610.26835v2) · [text/source](https://arxiv.org/html/2610.26835v2).  
**Inspection:** Version history; Theorem 17.1; sections 5.1 and 13; Appendix C; comparison with v1.

Theorem 17.1 retains $B_\flat=0.874886647039964\ldots$ for every finite-order Hecke character over every number field, with principal poles allowed and no boundary-line assertion.

The revision expands theta normalization and weighted transformed moments. Appendix C makes the two-transform recurrence and arithmetic-data loss control explicit.

**Use:** refresh the exact analytic interfaces underlying #1009 and later moment packets. Inspect measures, profile dependencies and induction direction before importing the additional detail. This is a source revision rather than a newly lowered all-field boundary; its analytic dependencies were not independently reproved.

## L03 — On some positivity properties of the Riemann Xi function

**Suvrit Sra.** author-site: riem-xi; v2 (author-site). Date for this record: **2026-10-29**.  
**Status:** primary PDF theorem statements inspected.  
**Primary sources:** [record](https://suvrit.github.io/papers/riem-xi/) · [text/source](https://suvrit.github.io/papers/riem-xi/riem-xi-v2.pdf).  
**Inspection:** Version table; Theorems 1.1–1.3; source normalization; prior-work discussion.

The 29 October author-site revision proves strict log-concavity for reciprocal-transform densities $\Theta,\Lambda$, and $\Lambda\in PF_{256}$ using published verification through $3\cdot10^{12}$. Its generalized Laguerre inequalities hold on a domain determined by the verified height.

**Use:** compare finite determinant inequalities with the project's actual xi objects. These are reciprocal densities, not the usual theta/Fourier kernel whose transform is $\Xi$; #1023's qualitative log-concavity countermodel concerns a different object.

The paper does not establish unconditional $PF_\infty$, RH, or a higher verified zero height; it discusses RH-equivalent $PF_\infty$ formulations. Site v2 is not “arXiv v2”; the earlier Hexagon record is 2610.00584v1.

## L04 — Zero-density estimates from an improved large-values bound

**Mark Lewko.** Palomar/GitHub: PALOMAR-2026-10-11-000010; registry v1; source ee2a8a32be49a4f73c7386e9dffdea24d7e3d8c0. Date for this record: **2026-10-11**.  
**Status:** formal source endpoints inspected; registry verification reported.  
**Primary sources:** [record](https://palomar-registry.org/entry?id=PALOMAR-2026-10-11-000010&version=1) · [text/source](https://github.com/mrklwk/zeta-density-39-over-17-lean/blob/ee2a8a32be49a4f73c7386e9dffdea24d7e3d8c0/lean/Solution.lean).  
**Inspection:** Challenge, Solution, actual-zero/multiplicity definitions, MiddleLargeValues and historical verification file; no dependency replay.

The source targets actual Mathlib zeta zeros and gives the uniform density exponent $39(1-\sigma)/17+\varepsilon$ for $1/2\le\sigma\le1$ and $T\ge2$. Its useful bounded-coefficient interface is
$$
|W|\ll_\varepsilon N^\varepsilon\left(N^2/V^2+
N^{18/7}T^{6/7}/V^4\right),\qquad N^{6/5}\le T\le N^{5/3},
$$
for a 1-separated large-value set $W$ in a translated interval of length $T$, with $N\ge2$, $V>0$, coefficients $|a_n|\le1$ on $N<n\le2N$, and $|D(t)|\ge V$ for $t\in W$.

**Use:** replay this interface, then test it in L05's optimization framework. A character/conductor analogue is an additional problem.

No conventional PDF was located. The registry reports multiple-kernel verification; this pass inspected the formal statements, not its full proof closure. The pinned README predates registry admission and must not be confused with a later receipt. Density permits exceptional zeros.

## L05 — Higher order uniformity of the primes and cancellation of the Möbius function in shorter intervals

**Kaisa Matomäki; Mayank Pandey; Javier Pliego; Joni Teräväinen; Mengdi Wang.** arXiv: 2610.09567; v1. Date for this record: **2026-10-07**.  
**Status:** primary theorem statements and method inspected.  
**Primary sources:** [record](https://arxiv.org/abs/2610.09567v1) · [text/source](https://arxiv.org/html/2610.09567v1).  
**Inspection:** Theorems 1.1–1.4 and section 3 reduction.

The paper gives Gowers uniformity of the von Mangoldt function relative to its Cramér model on all intervals of length $X^{3/5+\varepsilon}$, and Möbius cancellation on all intervals of length $X^{19/35+\varepsilon}$, with the stated logarithmic savings.

**Use:** Section 3 reduces product mean values of Dirichlet polynomials to a piecewise-linear positivity test. That is a concrete interface for introducing genuinely stronger large-value estimates into this repository's exponent work. Testing L04 inside it is a proposed experiment, not a result of this pass.

The interval-length exponent $19/35$ is not a zero-free boundary. Fixed-order and coefficient-complexity restrictions must remain attached.

## L06 — Large value estimates for Dirichlet polynomials and trilinear sums over short intervals

**Runbo Li.** arXiv: 2610.18923; v1. Date for this record: **2026-10-12**.  
**Status:** primary theorem statement inspected.  
**Primary sources:** [record](https://arxiv.org/abs/2610.18923v1) · [text/source](https://arxiv.org/html/2610.18923v1).  
**Inspection:** Theorem 1, setup and named large-value inputs; not all casewise proofs.

Theorem 1 refines a trilinear range for $1/2<\theta<4/7$. The polynomials have divisor-bounded coefficients and product length comparable to $x$; one factor is prime-factored, and the lengths satisfy explicit balance and piecewise constraints.

**Use:** this is a worked application of the L05 framework and a useful test of whether new bounds cover the actual obstructing factor lengths. The prime-factored hypothesis cannot be removed. The result is neither an arbitrary-coefficient trilinear estimate in every range nor an individual zero-free strip.

## L07 — Large Value Estimates for Dirichlet Polynomials with Characters and Zero Density of Dirichlet L-Functions

**Bin Chen; Vishal Gupta; Yung Chi Li.** arXiv: 2507.08296; v2. Date for this record: **2026-07-27**.  
**Status:** background dependency; primary theorem statements inspected.  
**Primary sources:** [record](https://arxiv.org/abs/2507.08296v2) · [text/source](https://arxiv.org/html/2507.08296v2).  
**Inspection:** Theorems 1.1–1.2 and proof outline.

The fixed-modulus family density bound has exponent $(7/3)(1-\sigma)+\varepsilon$ in $qT$. The large-values theorem requires $N\ge(qT)^{2/3}$, bounded coefficients, primitive characters and separated ordinates for each character; a divisor $q_1\mid q$ is retained in finer bounds.

**Use:** examine the divisor parameter and affine/GCD-twist machinery when matching natural-label families to conductor-ordered statements. Replacing $qT$ by $T$, or a density bound by zero exclusion, is unjustified. This July revision is included as an explicit dependency, not advertised as new October work.

## L08 — Small values of the Riemann zeta-function near the critical line

**Hung M. Bui; Alexandra Florea; André Heycock.** arXiv: 2610.27591; initial indexed record; full text unavailable. Date for this record: **2026-10-20**.  
**Status:** RH-conditional; primary indexed abstract only.  
**Primary sources:** [record](https://arxiv.org/abs/2610.27591) · [text/source](https://arxiv.org/abs/2610.27591).  
**Inspection:** Primary indexed abstract and author seminar abstract; direct abs/HTML/PDF retrieval failed.

The abstract assumes RH for bounds on normalized negative $2k$-moments near $1/2+\alpha$, $0<k<1/2$, and for the improved Möbius summatory estimate obtained at $k=1/2$.

**Use:** a quantitative target and a source of techniques for inverse-zeta work. First identify which truncated-polynomial components survive without RH. Importing the final estimate into an RH proof would be circular.

Full theorem text was inaccessible in this pass. The [author's seminar abstract](https://www.math.ucdavis.edu/research/seminars?talk_id=7733) confirms the RH assumption; its 5 November seminar date is not the paper's submission date.

## L09 — Half-sized gaps between zeros of the Riemann zeta function

**Andriy Bondarenko; Winston Heap.** arXiv: 2610.26038; v1. Date for this record: **2026-10-19**.  
**Status:** RH-conditional; primary theorem and key lemmas inspected.  
**Primary sources:** [record](https://arxiv.org/abs/2610.26038v1) · [text/source](https://arxiv.org/html/2610.26038v1).  
**Inspection:** Theorem 1, Lemmas 1–2, quotient identities and discussion of contour hypotheses.

Assuming RH, the lower limiting normalized gap is at most $1/2$. A symmetric Möbius resonator is coupled to a quotient of shifted zeta functions.

**Use:** extract the coefficient identity and the mixed-mean architecture for signed coupling. The authors separate these identities from RH-dependent holomorphy and contour shifts; the latter cannot be imported into an unconditional RH argument.

The fraction $1/2$ describes gap size, not the real part of zeros. This is not a new zero-free region.

## L10 — Landau-Siegel zeros over a base field and effective Brauer-Siegel

**William D. Banks.** arXiv: 2610.31402; v2. Date for this record: **2026-10-26**.  
**Status:** primary theorem scope inspected; v2 mathematics unchanged.  
**Primary sources:** [record](https://arxiv.org/abs/2610.31402v2) · [text/source](https://arxiv.org/html/2610.31402v2).  
**Inspection:** Version history, introduction/main results, section 7.1 and dependencies.

For fixed $k$ and quadratic $F/k$, Corollary 1.2 gives an effective $c(k)>0$ such that every real zero $\beta\in(0,1)$ of $L(s,\chi_{F/k})=\zeta_F(s)/\zeta_k(s)$ satisfies $(1-\beta)\log d_F\ge c(k)$. It derives effective Brauer–Siegel consequences and a weighted Frobenius estimate whose subset must contain the identity.

**Use:** compare the small-generator/Masser argument and its field dependence with existing determinant/descent routes. This is not a stronger fixed complex-zero half-plane. V2 corrects references and attribution, explicitly leaving the mathematics unchanged. The proof was not reconstructed here.

## L11 — Exceptional zeros of Hecke L-functions

**Christopher Frei; Wataru Kai.** Hexagon: 2610.00466; v2. Date for this record: **2026-10-29**.  
**Status:** primary PDF theorem statements inspected.  
**Primary sources:** [record](https://hexagonmath.org/2610.00466v2) · [text/source](https://hexagonmath.org/pdf/2610.00466v2).  
**Inspection:** Version history; Theorem 1.1; Proposition 1.2; Lemma 4.2.

For real-valued Hecke characters over a fixed number field, Theorem 1.1 gives an effective-in-principle separation for real zeros $\beta\in(0,1)$ in terms of the conductor norm, excluding the unit conductor in that logarithmic normalization. A small integral generator with controlled order index enables the number-field extension of Kerr's argument.

**Use:** compare conductor and lattice dependencies with L10 and the repository's algebraic transfer notes. Constants are not made explicit. V2 adds the concurrent Banks reference; use the history's 29 October date, not the landing header's original 22 October date.

This is Hexagon, not arXiv. It supplies no newly smaller all-height complex-zero boundary.

## L12 — Zeros of quadratic Dirichlet L-functions

**Dave Platt; Tim Trudgian.** arXiv: 2610.29018; v1. Date for this record: **2026-10-21**.  
**Status:** primary computational theorem inspected; computation not replayed.  
**Primary sources:** [record](https://arxiv.org/abs/2610.29018v1) · [text/source](https://arxiv.org/html/2610.29018v1).  
**Inspection:** Theorem 1 and rigorous computation description.

The result excludes positive real zeros for real primitive characters through conductor $10^9$, and through $10^{10}$ for odd characters. The computation uses rigorous ball arithmetic, with class-number input in the odd case.

**Use:** explicit low-conductor checks and quadratic-family controls. The real-axis conclusion reaches further left than a near-one exceptional-zero exclusion, but it is finite in conductor.

It does not establish GRH or exclude all complex zeros in a half-plane. This pass inspected the statement and computational method; it did not rerun the census.

## L13 — Full-source Schur certificates for Weil positivity at support radius two

**bramble_trace.** rStation: riemann_hypothesis/papers/60; v1. Date for this record: **2026-10-26**.  
**Status:** AI-community manuscript; full text inspected; certificate not replayed.  
**Primary sources:** [record](https://rstation.ai/problems/riemann_hypothesis/papers/60) · [text/source](https://rstation.ai/problems/riemann_hypothesis/papers/60).  
**Inspection:** Full online manuscript, theorem, domain, Schur constructions and reproduction section.

This manuscript claims positivity of the complete geometric Weil form for complex tests supported in $(-a,a)$, $0<a\le2$, retaining pole terms and the infinite complement. The proposed response matrix has displacement rank two and extremely ill-conditioned finite cores.

**Use:** an audit target for exact core inversion and controlled infinite tails in #1017/#1021. It supersedes the same community's 23 October claimed $(\log11)/2$ endpoint.

rStation is an AI-agent research community. The large certificate was not reproduced here, and the claim is not promoted to an accepted input. Even a correct fixed-window theorem would not establish cofinal positivity, RH, or a new global zero-free strip.

## L14 — Zeta Lab: finite-height Lean verification through height 100

**teal-sea.** GitHub: teal-sea/zeta-lab:rh_height_lean; 42a0e011468801531010404c4c98a07e82b480e0. Date for this record: **2026-10-30**.  
**Status:** actual source inspected; upstream checker acceptance reported; no fresh replay.  
**Primary sources:** [record](https://github.com/teal-sea/zeta-lab/blob/42a0e011468801531010404c4c98a07e82b480e0/hunts/rh_height_lean/RESULTS.md) · [text/source](https://github.com/teal-sea/zeta-lab/blob/42a0e011468801531010404c4c98a07e82b480e0/hunts/rh_height_lean/lean/RHHeight100/Main100.lean).  
**Inspection:** Main100 assembly and CheckMain100 unfolded-type checks; public results log.

The inspected Lean assembly targets Mathlib's $\zeta$: exactly 29 distinct zeros in the open critical strip with $0<\Im\rho\le100$, all simple and on the line. The source reports a 23 October build and a 24 October con-ron acceptance.

**Use:** reusable contour-count/sign-change architecture and checks that statements refer to the actual analytic function. The record's raw checker/export bundle was not public, and this pass performed no replay.

The 30 October date pins the repository tip, not discovery of the height-100 theorem. This is finite formalization, not an advance in the largest numerically verified height.

## L15 — CA2 numbers and the Riemann hypothesis: a numerical investigation of Ramanujan's inequalities

**Dmitry R. Leshchiner; Oleg R. Musin; James Thompson.** arXiv: 2610.39120; v1. Date for this record: **2026-10-29**.  
**Status:** new primary numerical study inspected.  
**Primary sources:** [record](https://arxiv.org/abs/2610.39120v1) · [text/source](https://arxiv.org/html/2610.39120v1).  
**Inspection:** Metadata and full HTML, especially mathematical framework and experiment qualifications.

The authors study the CA2 reduction of Robin's criterion, normalized differences and comparisons with sums over zeta zeros. The logarithmic decay law is derived from Ramanujan's conditional estimates; the numerical residual does not determine its limiting coefficient.

**Use:** refresh experiment design, normalization and truncation controls if the repository resumes the Robin route. Numerical behavior and RH-dependent comparison expressions cannot supply the missing infinite tail theorem. This is a genuinely new 29 October paper, but it gives neither a global zero-free improvement nor a proof of RH.

## L16 — More than 8/9 zeros of the Riemann zeta function are simple or on the critical line

**Cristian Cobeli; Alexandru Zaharescu.** arXiv: 2610.23467; v1. Date for this record: **2026-10-16**.  
**Status:** primary theorem and proof components inspected; interval calculation not replayed.  
**Primary sources:** [record](https://arxiv.org/abs/2610.23467v1) · [text/source](https://arxiv.org/pdf/2610.23467v1).  
**Inspection:** Theorem 1, sections 3–6, Lemma 5.2 and Appendix A computation description.

The lower limiting proportion of zeros, counted with multiplicity, that are **simple OR on the critical line** exceeds $8/9$; the displayed numerical result is approximately 0.88893. This is not an $8/9$ critical-line proportion or an “AND” statement.

A retained Gram spectral remainder, a seven-point inequality and block averaging provide the improvement. **Use:** compare that remainder with the project's positivity diagnostics.

Lemma 5.2 relies on a six-variable interval calculation described in the paper. Obtain or reconstruct the underlying certificate before treating it as a computational input. This pass did not rerun it or assert a defect.

## L17 — An explicit elementary proof of no Landau-Siegel zeros

**Victor Zhenyu Guo.** arXiv: 2610.30476; v1. Date for this record: **2026-10-21**.  
**Status:** primary theorem statement inspected; proof not reconstructed.  
**Primary sources:** [record](https://arxiv.org/abs/2610.30476v1) · [text/source](https://arxiv.org/html/2610.30476v1).  
**Inspection:** Theorem 1.1 and Remark 1.2; abstract and version history.

Theorem 1.1 gives $(1-\beta)\log q>1/100$ for primitive quadratic characters, $q\ge3$, and real zeros $\beta\in(0,1)$. The argument uses explicit polynomial counting and positive weighted sums; the stated uniform parameter choice avoids a separate low-conductor zero census.

**Use:** a smaller explicit test case for the determinant branch. The real-zero logarithmic bound is not a constant complex-zero half-plane. Keep this author's identity, Victor Zhenyu Guo, separate from Jizhou Guo in L18. Full analytic verification was not performed.

## L18 — The Möbius function at N-p

**Jizhou Guo.** author-GitHub: aster2024/openai-math-followups:mobius-goldbach-shift; v2 (author repository). Date for this record: **2026-10-23**.  
**Status:** explicitly conditional; author catalogue inspected.  
**Primary sources:** [record](https://github.com/aster2024/openai-math-followups/tree/main/mobius-goldbach-shift) · [text/source](https://github.com/aster2024/openai-math-followups).  
**Inspection:** Author catalogue, version and explicit dependencies; full 65-page proof not audited.

The author conditions the transplantation on Lü–Wang–Wu §§4.2–4.7 and Appendix A being correct as written, and on a Dirichlet zero-free half-plane for the general formulation. V2 adds uniform signed/reflected shifts and a stated quantitative rate.

**Use:** a section-by-section hypothesis map for #1022's desired coefficient/shift transfer. It is a new follow-up, not independent validation of the original determinant argument. The available catalogue was inspected; the complete manuscript was not independently checked.

## L19 — On the Hardy-Littlewood-Chowla conjecture

**Guangshi Lü; Zhiwei Wang; Jie Wu.** arXiv: 2610.20242; v1. Date for this record: **2026-10-14**.  
**Status:** already imported; version refreshed.  
**Primary sources:** [record](https://arxiv.org/abs/2610.20242v1) · [text/source](https://arxiv.org/html/2610.20242v1).  
**Inspection:** Version history, Theorems 1–2 and method provenance; no complete proof audit.

The current primary record still lists v1. The main statement is $\sum_{p\le x}\mu(p+2)=o(\pi(x))$, with a sign-density consequence among squarefree shifted primes.

**Use:** retain the existing #1022 import and refresh its follow-up links. The title should not be read as a proof of every multi-shift Hardy–Littlewood–Chowla statement.

A fixed-shift qualitative asymptotic does not supply a conductor-uniform power saving for the repository's selected Gauss/Möbius moments. This entry is an overlap check, not a newly discovered paper.

## L20 — Weil's quadratic form via the screw function

**Masatoshi Suzuki.** arXiv: 2606.09096; v3. Date for this record: **2026-09-23**.  
**Status:** primary latest version framework inspected.  
**Primary sources:** [record](https://arxiv.org/abs/2606.09096v3) · [text/source](https://arxiv.org/html/2606.09096v3).  
**Inspection:** Version history, operator framework and limiting conjecture.

The latest checked version is v3 from 23 September, whereas the inspected repository source pins v1. The paper connects the Weil form with continuous functions, operators and de Branges spaces; the limiting Hilbert–Pólya realization remains conjectural.

**Use:** refresh domains and normalization before comparing the repository's resolvents with L13. A valid finite operator framework does not settle the limiting conjecture. This is a version refresh of known work, not a new October breakthrough.

## L21 — A seven-eighths zero-free half-plane for unitary Weil L-functions

**Boyang Hu.** Hexagon: 2610.00216; v1. Date for this record: **2026-10-13**.  
**Status:** broad preprint claim; author discloses incomplete independent human verification.  
**Primary sources:** [record](https://hexagonmath.org/2610.00216v1) · [text/source](https://hexagonmath.org/2610.00216v1).  
**Inspection:** Primary abstract/provenance plus repository's source-interface audit; not complete proof.

The preprint claims a $7/8$ region for unitary Hecke characters over arbitrary number fields and finite-dimensional unitary Weil representations, including infinite-order rank-one characters. Its author discloses that the complete proof lacks independent human verification and that formalization is in development.

**Use:** keep the existing #1023 high-side numerator interface conditional, with infinity type, local tables, masks and principal-inducing exceptions explicit. This is broader-family claimed scope, not a smaller numerical boundary, and it was already present in the inspected branch.

## L22 — A quasi-Riemann hypothesis for Dedekind zeta functions

**Dean Cureton; Jesse Thorner.** Hexagon: 2610.00200; v2. Date for this record: **2026-10-14**.  
**Status:** known source; identity/version checked.  
**Primary sources:** [record](https://hexagonmath.org/2610.00200v2) · [text/source](https://hexagonmath.org/2610.00200v2).  
**Inspection:** Primary abstract, provenance and version history; no formal replay.

This is the all-number-field $31/32$ precursor cited by Liu. The important maintenance correction is bibliographic: **2610.00200 is a Hexagon identifier**, not an arXiv identifier.

The version history dates v2 to 14 October; the page header retains the 12 October original-deposit date. The source reports an AxiomProver formalization, which was not replayed here. Preserve prior repository source audits rather than silently rewriting their historical version identities.

## L23 — A two-slot sextic-cubic probe claiming the boundary 1049/1250

**liqsweep (blueberryvertigo).** GitHub: GTimG/QuasiRiemannTracker#96; ab4c5cc7882a47608a63a9967f72d99040833042. Date for this record: **2026-10-30**.  
**Status:** explicitly no Lean proof; closed unmerged; not an accepted boundary.  
**Primary sources:** [record](https://github.com/GTimG/QuasiRiemannTracker/pull/96) · [text/source](https://github.com/blueberryvertigo/zero-free-1049-1250).  
**Inspection:** Live PR metadata, author claim, proof-status disclosure and linked repository; full 224-page proof not audited.

The 224-page paper claims $\Re s>1049/1250=0.8392$ using a two-slot sextic/cubic construction. Its tracker submission explicitly contains no Lean proof and was closed unmerged.

**Use:** retain as a separately labeled architecture/audit lead. Inspect the proposed block large sieve and its analytic proof before considering the scalar certificates. Neither the numerical improvement nor exact exponent calculations establish that input.

Closure of the PR is not a mathematical refutation. Conversely, this unverified claim must not be listed beside L01 as an admitted formal result or used to update the project's boundary.

## L24 — Sharpness and uniqueness for positive solutions of the explicit formula for zeta(s)

**Nic Johns.** Zenodo/GitHub: 23246727; v1.3. Date for this record: **2026-10-08**.  
**Status:** AI-authored unreviewed preprint; axiom-dependent formal spine.  
**Primary sources:** [record](https://zenodo.org/records/23246727) · [text/source](https://github.com/nic410/zeta-sharpness-uniqueness).  
**Inspection:** Author deposit and repository scope/axiom-ledger descriptions; not full proof.

The work studies positive explicit-formula solutions and an Odlyzko–Poitou–Serre optimization equivalence. Its formal spine uses six Part I and two Part II axioms, including an existence input; the main construction is not thereby formalized.

**Use:** a possible duality/construction lead for Weil research, with the existence and positivity certificates isolated for review. The author describes the work as AI-produced and not human-expert checked. No RH proof is imported.

The deposit displays 8 October; it should not be relabeled a 29 October publication merely because it appeared in a fresh search.

## L25 — Discorrelation of the Möbius function with linear phases in short intervals

**Javier Pliego; Mengdi Wang.** arXiv: 2610.11487; v1 indexed; v2 revision lead unconfirmed. Date for this record: **2026-10-08**.  
**Status:** primary indexed abstract; primary v2 unavailable.  
**Primary sources:** [record](https://arxiv.org/abs/2610.11487) · [text/source](https://arxiv.org/abs/2610.11487).  
**Inspection:** Primary indexed abstract; direct history/HTML/PDF unavailable; v2 date observed only through a mirror.

The primary indexed abstract states cancellation for $\mu(n)e(n\alpha)$ in intervals of length at least $x^{0.58+\varepsilon}$, with logarithmic savings; the von Mangoldt analogue retains a near-rational exception.

**Use:** investigate phase-sensitive Type III decomposition after obtaining the full theorem. The interval exponent is not a zero-free boundary. A mirror suggests a minor v2 revision on 22 October, but primary history was inaccessible, so that revision is explicitly unconfirmed.

## L26 — Zero density in short strips and short-interval bounds toward Hypothesis S

**Yangbo Ye.** arXiv: 2610.15989; initial indexed record; full text unavailable. Date for this record: **2026-10-11**.  
**Status:** primary indexed abstract only.  
**Primary sources:** [record](https://arxiv.org/abs/2610.15989) · [text/source](https://arxiv.org/abs/2610.15989).  
**Inspection:** Indexed primary abstract; full text and version history inaccessible.

The indexed statement gives
$N_\zeta(\sigma;T,T+T^a)\ll
T^{15a(1-\sigma)/(3+5\sigma)+\varepsilon}$
for $2/3\le a\le1$ and $7/10\le\sigma\le4/5$.

**Use:** a candidate local exceptional-set input. Retrieve the full proof and normalization before applying it. Its positive density exponent does not imply zero absence, and this pass did not inspect the complete theorem text.

## L27 — Amplified moments of the Riemann zeta function

**Benjamin Durkan; Timothy Page.** arXiv: 2606.27323; v2. Date for this record: **2026-08-05**.  
**Status:** primary theorem statements inspected.  
**Primary sources:** [record](https://arxiv.org/abs/2606.27323v2) · [text/source](https://arxiv.org/html/2606.27323v2).  
**Inspection:** Theorems 1–9 and introduction; not a complete proof audit.

V2 raises the sixth-moment lower coefficient from 34.1 to 34.4 in the paper's normalization; older indexing still displays 34.1. Two-piece amplified moments and joint-moment lower bounds provide useful benchmark examples.

**Use:** check normalizations and distinguish a lower-bound construction from the upper bounds required by inverse-moment consumers. This August revision is background, not new October research; it proves neither Lindelöf nor RH.

## L28 — Fourier optimization and pair correlation problems

**Mithun Kumar Das; Tolibjon Ismoilov; Antonio Pedro Ramos.** journal/arXiv: 10.4171/RMI/1656; online journal publication; preprint 2502.05106v1. Date for this record: **2026-10-22**.  
**Status:** journal metadata and abstract inspected.  
**Primary sources:** [record](https://ems.press/journals/rmi/articles/14300132) · [text/source](https://arxiv.org/abs/2502.05106).  
**Inspection:** Journal date/abstract and arXiv metadata; full theorem body not audited.

The 22 October online publication is new, while the preprint dates to February 2025. Fourier extremal problems give average form-factor bounds for several zero families, including Dedekind/Selberg-class settings.

**Use:** candidate extremal kernels for comparison experiments. The precise family hypotheses still need full-text review before use. A new journal date does not make the underlying research newly posted, and correlation averages are not all-zero exclusion.

## Known-source maintenance outside the main selection

- **Ben Green, *On Landau–Siegel zeros*, [Hexagon:2610.00311v2](https://hexagonmath.org/2610.00311v2):** v2 is 18 October (v1 17 October). This is also a Hexagon identifier, not arXiv. The version decouples two parameters. It is already represented in the repository's determinant route.
- **Baiying Liu, [arXiv:2610.12234v2](https://arxiv.org/abs/2610.12234v2), 12 October**, and **Yuanda Xu–Hejian Sang, [arXiv:2610.15291v2](https://arxiv.org/abs/2610.15291v2), 15 October:** retained as precursors to L02; no newer versions were established in this pass.
- **Alexandre de Faveri, *Optimal large sieve for fixed order characters*, [arXiv:2610.04045v1](https://arxiv.org/abs/2610.04045v1):** already central to #1023's natural-label density work. The full source and any later revision were not re-audited here.
- **Connes–van Suijlekom 2511.23257 and Connes–Consani–Moscovici 2511.22755:** already pinned by #1021. They are background to the new comparisons, not fresh discoveries.
- **Scott Duke Kominers, *Small algebraic integers and Frobenius prime sums*, [Hexagon:2610.00451](https://hexagonmath.org/2610.00451), 22 October:** author/institution metadata and Banks's citation were located. The current full PDF was not inspected; retain as a further determinant-method lead.

## What this pass does not conclude

No entry is a newly established proof of RH by this repository. Smaller numbers must be compared with the same family and hypothesis set. A finite PF order, finite window, density-one family, real-zero exclusion, conditional moment, or formal specification is not interchangeable with unconditional all-height individual nonvanishing.

The strongest immediate action is to reproduce and understand L01's new input, then assess the exact source transfers suggested in [REPO_MAP.md](REPO_MAP.md).
