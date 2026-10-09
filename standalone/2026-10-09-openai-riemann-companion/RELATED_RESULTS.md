# Related OpenAI results: mathematical scope and proposed transfers

**Status:** IMPORTED SOURCE COMPARISON / PROPOSED RESEARCH DIRECTIONS. This document does not accept the imported proofs or change the scientific status of the repository. RH remains unproved here.

**Scope:** Companion material to the family 003 import in [PR #908](https://github.com/GettysburgResearch/riemann/pull/908): direct analytic extensions, explicit source dependencies and applications, and results connected to a named existing programme. Similar words or a common mathematical subject alone are not an inclusion rule.

**Exact sources:** OpenAI `math` at `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`; the original family 003 import remains identified with `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. The base PR was observed at `31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6`. The [source selection](SOURCE_SELECTION.json) records all manuscript directories and advertised formal comparator roots; the [combined manifest](SOURCE_MANIFEST.json) records their resident bytes and core reuse. Pinned source links below refer to the companion snapshot, not a changing upstream branch.

**What was actually checked:** Catalogue descriptions and abstracts were searched across all 372 result families. The original snapshot listed 722 manuscripts; the companion snapshot lists 719 after three withdrawals elsewhere in the catalogue, as recorded in its [upstream history](upstream/history.md). Selected theorem statements, introductions and proof outlines were read; the most relevant formulae and parameter qualifications are recorded below. This is not a complete independent reconstruction of any imported proof. Scope documents and comparator paths were inspected; no Lean build, comparator equivalence check, complete axiom audit, PDF rebuild or numerical reproduction is asserted here.

**Smallest remaining gap:** For every proposed RH use, prove an adapter for the actual fixed arithmetic source, at the required parameter range and measure, with all signed terms and errors retained. An imported statement plus a suggestive analogy does not supply that adapter.

## 1. Selection and relationship to the existing work

The companion selection contains ten families and 22 manuscript directories. Family 003 is already the primary import. Among the companions, family 029 contains an additional explicit Hecke zero-free theorem that is easy to miss from its primitive-roots title.

| Family | Why included | Existing programme | Exact boundary |
|---|---|---|---|
| 007 | Ordinary two-point multiplicative cancellation and signed divisibility-graph transference | Fixed detector, Q4, wavelet and half-divisor cancellation | Fixed affine forms and logarithmic savings do not supply the required growing-parameter critical estimate |
| 011 | Weighted dilation graphs; marked Type II estimates; parity-sensitive prime predecessors | Native Möbius sources, rough-number/Bellman and causal Euler work | Prime-predecessor distribution is not a universal estimate for the native detector; the Poisson–Dirichlet paper is also a dependency of 029 |
| 012 | Ordinary joint Dickman law with an explicit arithmetic-to-model comparison | Dickman/Bellman and causal Euler work | Fixed thresholds and qualitative limits do not control a growing roughness parameter or signed remainder |
| 021 | Uniform sieve survivor bound and transfer from reference positivity to actual residue classes | Growing-prime arithmetic tails and source fidelity | Coprime-survivor existence is not signed Möbius positivity or negative-mass control |
| 023 | Cubic theta/Gauss-sum cancellation, structured dual families and exact cutoff removal | Family 003 analytic comparison; signed bilinear and family extraction work | Structured coefficient and fixed-angle hypotheses are essential |
| 029 | Uniform zero-free half-plane over a larger class of number fields | Dirichlet completion, generalized L-families, principal-member extraction | The half-plane is much narrower than the 003 bound and does not approach the critical line |
| 142 | Explicit application of 029 to small auxiliary primes and deterministic factorization | Uniform field/conductor bookkeeping | An application of the zero-free input is not independent evidence for its proof |
| 182 | Prime-argument polynomial differences explicitly use the 003 zero-free theorem; earlier papers give the method chain | Signed finite-law transfer and physical arithmetic kernels | Power saving for avoidance sets does not imply cancellation for the repository's detector |
| 014 | Concrete function-field, automorphic and Frobenius comparator | Function-field mirror, automorphic trace and generalized structures | No characteristic-zero principal-zeta transfer is supplied |
| 026 | Actual prime-gap frequency, preserving counting measure | Existing LongGapsBetweenPrimes / PrimeGaps186 comparison lane | Positive lower density of fixed-threshold gaps is not RH or a growing-threshold law |

The last two rows are secondary programme comparisons. Their inclusion preserves relevant research material, not an implication to RH. This selection is comprehensive for the stated direct/dependency/programme rule; it is not a claim to have searched every internal lemma of all manuscripts for every possible future use.

The repository's current targets remain those in [OPEN_CUTS](https://github.com/GettysburgResearch/riemann/blob/31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6/OPEN_CUTS.md) and the source-qualified statements in [CURRENT_RESULTS](https://github.com/GettysburgResearch/riemann/blob/31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6/research/integrated/CURRENT_RESULTS.md). In particular, for the fixed noncancelling Mellin detector, the open arithmetic premise is

$$
N_F(Y)=\int_1^Y F_-(x)\,\frac{dx}{x}=O_\varepsilon(Y^\varepsilon)
\quad\text{for every }\varepsilon>0.
$$

None of the selected companion theorems states this bound for that source. The critical SHARP power, uniform growing-prime closure, full signed Q4/near-collision estimate, principal-member extraction and all-order actual-xi positivity remain separate obligations.

## 2. Family 007: ordinary multiplicative correlations

[Source introduction](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/introduction.tex) · [formal scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/007.md).

For fixed integers defining nonproportional affine forms, the quantitative statement is

$$
\left|\sum_{n\le X}\lambda(a_1n+b_1)\lambda(a_2n+b_2)\right|
\le C_{a_1,a_2,b_1,b_2}\frac{X}{(\log X)^c},
\qquad a_1b_2-a_2b_1\ne0,
$$

where $a_i\ge1$, $b_i\ge0$, and $c>0$ is absolute. The forms are fixed before $X\to\infty$; the constant may be ineffective. The general corrected Elliott statement is qualitative for one-bounded multiplicative functions, with at least one original factor uniformly nonpretentious against each fixed Dirichlet character times $n^{it}$, for $|t|\le N$. These are ordinary, not logarithmically weighted, averages.

The method uses multiplicative dilation graphs whose edges carry centered divisibility weights. Disjoint prime supplies, each of reciprocal mass $W$, produce normalization $W^J$ against a trace cost approximately $(C\sqrt W)^J$; $J$ proportional to $\log\log X$ yields a logarithmic saving. Padding deals with divisor concentration. A bounded-independence correction and a circuit-fooling argument compare the actual finite residue law with the reference law without pretending that an interval contains a complete enormous CRT period. Repeated prime labels are handled through a rank-versus-forest division of configurations.

The qualitative weighted argument has a particularly relevant sign boundary: a factor of the form $\mathbf1_{p\mid n}-\theta/p$ need not be individually centered. The matching endpoint normalization supplies cancellation at the level of the signed average. Taking absolute values before that cancellation destroys the intended comparison.

**Proposed use.** Write one actual Q4 or half-divisor correlation in a form to which a precise graph lemma applies. Record the coefficient class, affine coefficients, weights, interval length, prime bands and all exceptional terms. Then compare the supplied estimate with the exact power and summability required by the fixed detector. A successful fixed-form application would be a useful intermediate theorem even if its saving is insufficient for RH.

**What must not be inferred.** A logarithmic saving for fixed affine forms is not square-root cancellation, a weighted growing-family theorem, a near-collision estimate with scale-dependent coefficients, or a bound for negative excursions of the native detector. A character-family average also does not extract the principal member by itself.

Advertised comparator roots: `OrdinaryElliott`, `OrdinaryTwoPointCorrelations`.

## 3. Family 011: dilation graphs, prime predecessors and sign information

This family is included in full because its papers supply different, noninterchangeable inputs:

1. [Weighted dilation graphs, smooth shifted primes and totient fibers](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/paper.pdf) transfers independent-label operator estimates to integer correlations and uses Type II prime extraction. Its stated applications include $x^{1-o(1)}$ primes with predecessors smooth at any fixed positive-power threshold, and infinitely many large totient fibers.
2. [The Poisson–Dirichlet law for prime predecessors](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/build/sections/01-introduction.tex) claims convergence of every fixed finite joint distribution of the ordered logarithmic prime-factor sizes of $p-1$, with multiplicity, to $\mathrm{PD}(1)$, under ordinary equal weighting of primes. It uses the first paper's graph inputs but requires a stronger extraction argument.
3. [Prime predecessors with an even number of prime factors](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026/build/main.tex) claims infinitely many primes with $\mu(p-1)=1$. It adds a prime in the long factor slot and a common Liouville sign at both endpoints, rather than deducing parity from unsigned smoothness.

The Poisson–Dirichlet paper's main analytic step is a marked Type II estimate. Dividing out selected divisor marks leads to a small-determinant relation between primitive lattice vectors. Signed moments use a root-residue law and an exact memory expansion: a repeated prime's divisibility probability is charged once even if its uses are separated. High-rank equality patterns gain small point-probability factors; low-rank identifications affect only a small fraction of edge contractions. The final probability argument separately excludes escape to the boundary of the factor simplex. All smoothness parameters and finite coordinate counts are fixed in the limiting theorem.

The parity paper uses complete multiplicativity to cancel the shared dilation sign appearing twice. A long prime-polynomial estimate, local Fourier-energy control, prescribed character–Mellin discrepancy and a parity-selecting nonnegative weight supply the additional bilinear information needed to pass the sieve parity obstruction. Its weak high-height zero-free estimate is a supporting input for those prime polynomials, not the global half-plane conclusion of family 003.

**Why it matters here.** The repository already has a fixed-$P_{61}$ signed bias theorem, rough-number corridors, Bellman comparisons and a causal Euler/Dickman construction. These papers provide concrete examples of the additional arithmetic work needed to promote a probability model or unsigned statistic to an actual weighted statement. Moreover, the marked Type II theorem from the Poisson–Dirichlet paper is an explicit dependency of family 029's controlled-predecessor construction.

**Proposed use.** Extract the precise weighted transference contract before attempting an application. For a native Möbius weight, verify its endpoint Fourier bounds and signed normalization. For a growing prime set, derive explicit dependence on the number and positions of marking bands; do not infer such uniformity from a theorem that fixes them before the limit.

No family 011 Lean scope/comparator is advertised in the inspected catalogue. The absence of a comparator link is not a claim that none of its ingredients appears in any other module.

## 4. Family 012: ordinary joint Dickman law

[Manuscript](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-joint-Dickman-law-for-consecutive-integers-September-24-2026/paper.pdf) · [formal scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/012.md).

For fixed $0<a,b<1$, the joint natural density of

$$
P^+(n)\le n^a,\qquad P^+(n+1)\le n^b
$$

is claimed to tend to $\rho(1/a)\rho(1/b)$, and each ordering of the two largest prime factors has density $1/2$. The proof encodes factor bins by multiplicative phase functions, uses rough-divisor amplification and a finite-feature divisibility-graph comparison to force mixed decorrelation, and then reconstructs the joint distribution.

**Proposed use.** Compare this exact ordinary-density transfer with a single fixed-parameter Dickman/Bellman identity already present in the repository. Determine whether its finite-feature comparison can retain the repository's actual weights and physical measure. It is a useful source for an adapter specification or a counterexample to an overbroad adapter.

**Boundary.** The conclusion is a qualitative distribution of two unsigned statistics at fixed thresholds. It provides no growing-roughness rate, conditional law along arbitrary arithmetic subfamilies, recursive independence across generations, or signed bound for the corrected Euler product. Comparator root: `JointDickman`.

## 5. Family 021: Jacobsthal and actual sieve survivors

[Introduction](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/build/sections/introduction.tex) · [formal scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/021.md).

The strengthened statement is

$$
h(k)\le \frac{Ck^2}{(\log\log(3k))^2},\qquad k\ge1,
$$

with one absolute constant, arbitrary prescribed prime sets, and interval starts at any signed integer. Here $h(k)$ is the length guaranteeing an integer coprime to any modulus with at most $k$ distinct prime factors. The optimal order is not claimed.

A decreasing-prime expansion tree retains a positive smaller boundary contribution at the linear-sieve endpoint. The main transfer burden is showing that actual residue-class counts inherit this reference positivity. Large short-edge discrepancy forces rational alignment of forbidden residue classes. Variance restricts possible rational centers; stopped even nodes and marked renewal account for exceptional path mass.

**Proposed use.** Use the proof as a model for a source-specific growing-prime lemma: define the actual count or signed mass, the reference kernel, and the defect before using a positive model. Identify whether an inverse-alignment statement is even true for the native weights. A theorem about actual coprime counts may improve an unsigned envelope, but a separate signed statement is still needed at the critical detector.

**Boundary.** Existence of an unsigned survivor does not establish Möbius bias, SHARP at power one, an unbounded Robin tail, or subpower negative mass. The two advertised comparator roots, `Jacobsthal` and `JacobsthalImproved`, represent distinct strengths and should both remain identifiable.

## 6. Family 023: cubic Gauss sums and structured cancellation

[Introduction, normalization and proof outline](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/paper.tex) · [formal scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/023.md).

For normalized cubic Gauss sums over all primary Eisenstein primes, including both conjugate prime ideals, the stated asymptotic is

$$
\sum_{N\pi\le X}G(\pi)
=\frac65c_*\frac{X^{5/6}}{\log X}
+o\!\left(\frac{X^{5/6}}{\log X}\right),
\qquad c_* = \frac{(2\pi)^{2/3}}{3\Gamma(2/3)}.
$$

Every fixed nonzero prime-angle Fourier mode has smaller order. No uniformity for an angle mode growing with $X$ is asserted. The paper explicitly distinguishes its all-primary-prime normalization from the rational-prime convention; the latter has half the displayed main-term coefficient for the stated normalized Kummer sum. These conventions must remain attached to any comparison.

The proof imports the unconditional level Voronoi formula, rather than a GRH-dependent cancellation theorem. Corrected dispersion retains the nonzero cube frequencies as the model main term before estimating the remaining frequencies. Moments at several lengths and an off-diagonal Gram estimate handle narrowly structured prime-polynomial coefficients. An exact bin-based stopping rule and binomial weights preserve coefficient independence, avoiding a coupled least-prime cutoff. Localization in both norm variables restores enough diagonal saving at large Mellin heights to remove smoothing.

**Connection.** This lies in the same cubic-theta/Eisenstein setting used by family 003, but its first-moment theorem is a separate target. It is also relevant to the repository's near-collision and signed-bilinear decompositions: the order of subtraction, independent coefficient classes, exact stopping rule and high-height cutoff errors are concrete proof obligations.

**Proposed use.** Compare one full source-defined decomposition with the bin-stopping identity, retaining the actual two-sided weights. If it cannot produce independent admissible coefficients, record that failure rather than applying a structured estimate to arbitrary coefficients. Separately audit whether a proposed principal extraction retains all cube-frequency contributions and normalization factors.

**Boundary.** This does not improve the cubic large sieve for arbitrary coefficients, establish all growing angular modes, or prove RH. Comparator root: `PattersonFirstMoment`.

## 7. Family 029: a separate uniform Hecke zero-free extension

[Theorem and proof architecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/01-introduction.tex) · [zero detection and Mellin continuation](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/06-zero-free.tex).

The primitive-roots manuscript contains the following separate analytic claim:

> For every cyclotomic number field $F$ containing $\mu_{12}$, and every finite-order Hecke character $\eta$ of $F$, $L_F(s,\eta)$ has no zeros in $\Re s>1-10^{-6}$.

The principal character is included, its pole at one is allowed, and there is no conductor or height cutoff. The width is common across the stated fields and characters. Auxiliary data, constants and thresholds in intermediate estimates may depend on the fixed field and character. This is a broader field range with a **much narrower** strip than family 003; it does not strengthen the $7/8$ boundary for the Riemann zeta function.

The paper explicitly extends the cubic-theta reflection and additive-probe mechanism of family 003 from the Eisenstein field to each fixed such $F$. It uses a normalized Kazhdan–Patterson Whittaker factorization, balanced generators and norm-based exponents. In one reflected cross interaction the sextic exponents are $1$ and $-4$; their sum is $3\pmod6$, yielding a quadratic interaction accessible to a number-field quadratic large sieve. The Poisson principal frequency has a first local term producing the desired reciprocal Hecke factor. A conductor large sieve and a zero detector control nonprincipal rows. The principal inverse Mellin integral then supplies continuation of the reciprocal target.

The primitive-root application further needs controlled factorizations of $p-1$, a fixed progression excluding the quadratic obstruction, and a splitting estimate uniform over the relevant growing fields. It imports marked Type II information from family 011 and performs additional character/frequency and sieve work. A common zero-free width should not be substituted for every needed field-uniform error estimate without reconstructing that step.

The second selected manuscript, [Simultaneous primitive roots: a conditional lower bound for prime bases](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026/simultaneous-primitive-roots-conditional-lower-bound-prime-bases.pdf), retains four explicitly stated analytic/sieve inputs. Its conditional status must not be erased by importing the family together.

**Proposed use.** Give the number-field extension its own review, beginning with the actual local coefficient identity and the nonvanishing correction factor. Then test the conductor large-sieve and principal-row extraction at exact field and character conventions. For the repository's L-family programme, this is a concrete comparison for source-faithful extraction with ramified factors, not merely a general statement that families might help.

No formal comparator for this broader cyclotomic theorem was advertised in the inspected tree. `HeckeSevenEighths` belongs to the narrower field scope of family 003 and must not be relabeled as a formalization of this extension.

## 8. Family 142: an explicit downstream application, not a new zero-free theorem

[Introduction](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Deterministic-Polynomial-Factorization-over-Prime-Fields-October-4-2026/build/sections/00-introduction.tex) · [analytic adapter](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Deterministic-Polynomial-Factorization-over-Prime-Fields-October-4-2026/build/sections/10-analytic.tex).

The claim is deterministic complete factorization of a nonzero dense polynomial over $\mathbb F_p$, including multiplicities, in a fixed polynomial number of bit operations in $(\deg f+1)\log p$. The displayed exponent is deliberately enormous; this is not a claim of a practical factorization implementation.

The algebraic reduction needs small auxiliary primes $\ell\equiv1\pmod{12q}$ at which the input prime $p$ is not a $q$-th power. The analytic section isolates family 029's Hecke zero-free theorem, uses abelian factorization for

$$
K=\mathbb Q(\mu_{12q}),\qquad M=K(p^{1/q}),
$$

and gives a smoothed explicit-formula estimate

$$
\Psi_M(x)=x\Phi(1)+O_\Phi\bigl(x^{1-\delta}(\log D_M+[M:\mathbb Q])\bigr),
\qquad \delta=10^{-6},
$$

with a field-independent implied constant under the stated zero-free input. Comparing $\Psi_K-q^{-1}\Psi_M$ detects failure of complete splitting. Explicit degree/discriminant bounds then force a suitable auxiliary prime of polynomial numerical size. The separate algebraic construction converts those primes into deterministic splitting and factorization.

**Why keep it.** This is a worked example of how a zero-free statement must be converted into an estimate with all field and conductor costs before a growing-family application. It is useful for the repository's uniformity audit even though polynomial factorization is not a native RH route.

**Boundary.** The zero-free theorem is imported from 029, not proved independently here. Neither the application nor a successful algebraic reduction confirms that analytic proof. No formal comparator is advertised for this factorization theorem.

## 9. Family 182: a direct application of the Dirichlet half-plane theorem

[Prime-argument introduction](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Power-Saving-for-Polynomial-Differences-at-Prime-Arguments-October-5-2026/build/sections/introduction.tex) · [formal scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/182.md).

The selected chain contains the square-difference paper, the degree-dependent intersective-polynomial extension, and the prime-argument extension. For the last, a fixed polynomial $h\in\mathbb Z[x]$ has degree at least two, positive leading coefficient, and a unit root modulo every modulus. The claimed conclusion is

$$
(A-A)\cap\{h(p):p\text{ prime}\}\subseteq\{0\}
\quad\Longrightarrow\quad |A|\le C_hN^{1-c_h}
\qquad(A\subseteq[1,N]),
$$

with $c_h>0$. The exponent may depend on the polynomial; do not substitute the degree-only exponent of the unrestricted-integer version.

The prime-argument proof explicitly imports the family 003 statement that all Dirichlet L-functions are zero-free for $\Re s>7/8$. It derives the needed arithmetic-progression prime estimates from that input. Those estimates feed the major arcs of a prime-supported polynomial kernel; Vaughan's identity and Weyl differencing control minor arcs.

The common mechanism uses reflection-positive finite-field tuple laws. A signed rational Fourier lift retains the density as its mean, and a nonnegative multilinear functional dominates a fixed power of that density. The prime-supported kernel is compared with the finite-field pair-law kernel. Avoidance annihilates the actual arithmetic kernel, while progression restriction and a controlled exceptional-prime recurrence produce contraction across scales.

**Proposed use.** Audit the prime-distribution adapter separately from the imported zero-free theorem. For a native-source experiment, preserve the distinction between a positive multilinear certificate, a potentially signed lift, and the kernel supported on actual arithmetic shifts. A theorem for a convenient local model is not yet a theorem for the physical source.

**Boundary.** This is an explicit consequence and a methodological example, not an independent RH proof. The advertised `SquareDifference` comparator covers the square-difference theorem; the family scope document does not certify every October 5 generalization merely because the later papers share a family number.

## 10. Family 014: function-field and automorphic comparisons

The repository explicitly retains [function-field, automorphic and generalized-object programmes](https://github.com/GettysburgResearch/riemann/blob/31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6/PROGRAMMES.md#families). This is the reason to preserve family 014; its relation is structural, with no asserted transfer to the actual principal zeta source.

The eight manuscript scopes are distinct:

| Manuscript | Stated scope that must be retained |
|---|---|
| Ramanujan–Arthur decompositions at full finite level | Split semisimple groups over global function fields; nilpotent-orbit decomposition of cusp spaces with full finite level, including arbitrary divisor multiplicities; the same orbit governs all good places |
| Global Arthur enhancements | Assumes the finite-level decomposition; constructs a commuting Weil map and one algebraic SL2 recovering an occurring parameter on the whole Weil group, including inertia; does not claim packet classification, ellipticity or a multiplicity formula |
| Rationality of the canonical unramified Arthur filtration | Four characteristic hypotheses of the restricted geometric theory; rationality includes the noncuspidal part and closed invariant nilpotent support |
| Temperedness at ramified places | Globally generic cuspidal representations of split connected adjoint exceptional groups over global function fields; all places, with no characteristic or ramification-depth restriction in the stated theorem |
| Restricted geometric Langlands in positive characteristic | Over an algebraic closure of a finite field, four stated characteristic hypotheses; over arbitrary algebraically closed fields, additionally very-good characteristic and characteristic prime to the Weyl-group order |
| Constructible tame Hecke eigensheaves | One marked point, genus at least two, simple simply connected group, dense geometric parameter with tame regular-unipotent monodromy, and four characteristic hypotheses |
| Several marked points | SLn in characteristic greater than n; at least two marked points, genus at least two, dense geometric PGLn parameter with tame unipotent monodromy of arbitrary Jordan type |
| Frobenius structures | SLn, one marked point, characteristic greater than n, dense arithmetic PGLn parameter with regular-unipotent tame monodromy; after a finite extension of constants, the full eigenstructure is Frobenius-compatible with the prescribed parameter |

The [full finite-level introduction](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level-September-24-2026/build/sections/01-introduction.tex) gives a useful concrete proof comparison. An ordered Bernstein weight is detected by translation/shtuka constructions. Rotation traces and Frobenius weights give a lower cohomological-degree bound; derived Satake and corrected fibre-amplitude estimates give an upper bound on the same summand. Choosing a translation weight proportional to the violating weight makes the discrepancy grow, producing a contradiction. Purity then makes the neutral cocharacter independent of the good place, and a finite rational Hecke algebra yields the decomposition.

**Proposed use.** For a retained generalized-object or Frobenius construction, ask whether the two proposed estimates actually concern the same object, whether the extreme summand survives projection and specialization, and whether Frobenius structure exists for the prescribed arithmetic parameter. These are concrete source-identification questions, not permission to transfer purity from a function field to zeta over the integers.

**Boundary.** Neither a function-field parameter nor a geometric eigensheaf supplies the repository's missing characteristic-zero arithmetic realization, principal-member estimate, conductor-uniform limit or authenticated Chow witness. Only selected statements and the full finite-level proof outline were reviewed for this comparison; the whole categorical argument was not reconstructed. No family 014 formal comparator is advertised.

## 11. Family 026: gap frequency and preservation of counting measure

[Introduction](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Positive-lower-density-of-large-prime-gaps-September-25-2026/build/sections/01-introduction.tex) · [formal scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/026.md).

For every fixed $C>0$, the claim is that at least $c(C)N$ of the first $N$ consecutive prime gaps exceed $C\log p_n$, for every sufficiently large $N$. This is positive **lower** density, with threshold-dependent constants, not existence of a limiting density or uniform control when $C$ grows.

The proof constructs adjacent intervals with a prime in the first and very small weighted prime mass in the second. Squares of signed smooth divisor sums give a nonnegative weight; alternating neighbouring dimensions cancel in the prime-marked moment while leaving unmarked mass. Two different second-moment estimates detect a prime and then transfer weighted mass to ordinary integer starts. The last prime of the first interval begins a long gap and can be selected by at most the interval length many starts. This bounded multiplicity is what transfers the count to distinct prime gaps, regardless of how long those gaps are.

**Why included.** The repository already retains external long-gap and prime-gap comparisons. This paper is an additional exact example of preserving the intended measure and charging multiplicity, and of uniformity over a family of signed weights before the main asymptotic limit.

**Boundary.** Many empty intervals need not mean many distinct long gaps. Nor does this fixed-threshold result settle any of the repository's RH-bearing estimates. Comparator root: `PrimeGaps`. The upstream scope document describes the prime-ratio corollary only, whereas [`PrimeGaps.json`](upstream/lean/ComparatorChallenges/PrimeGaps.json) selects `OAI.Problem344.large_gaps_and_ratio_density`, whose [challenge statement](upstream/lean/ComparatorChallenges/PrimeGaps.lean) is the conjunction of the all-fixed-positive-threshold large-gap assertion and the ratio-density assertion. Preserve this difference between the prose scope and actual target signature; neither has been kernel-checked by this comparison.

## 12. Review order and concrete next outputs

The most useful next work is a sequence of theorem-sized reviews, not a combined declaration that the imported programme closes RH:

1. **Local arithmetic and noncancellation.** Reconstruct family 003's exact principal-row factorization and then family 029's broader-field analogue, preserving cube factors, ramified corrections and normalizations. Identify the first uncertain equality or estimate.
2. **Signed extraction.** Audit one 007/011 graph lemma against an actual repository weight. Report either a valid specialized statement or the first violated coefficient, independence, centering or parameter hypothesis.
3. **Uniform analytic consequence.** Independently derive one smoothed prime-distribution statement from the stated zero-free input, including field degree, discriminant, conductor and height dependence. Family 142's analytic section and 182's prime section are worked comparison cases.
4. **Physical-source transfer.** Attempt one exact fixed-kernel Q4/wavelet/half-divisor specialization or one growing-prime survivor lemma. Keep the source and measure fixed, and compare the resulting saving with the literal critical estimate.
5. **Separate formal verification.** Build only the selected comparator/solution closure under the pinned toolchain, check that target statements match the manuscript scope, and inspect dependency axioms. A successful import inventory or a paper-to-code name match is not this verification.

For every proposed adapter, record the native source, normalization, domain, coefficients or family, parameter order, remainder and exact consequence. In particular, keep fixed forms separate from growing forms; fixed conductors from growing conductors; averaged members from the principal member; geometric parameters from an arithmetic realization; positive upper sections from lower certificates; and imported implications from proved native estimates.

## 13. Nearby material considered but not selected

- Families 001/032 (Hodge and specialization), 002/006 (BSD and Goldfeld), 010 (pro-modularity), and 069 (quantum geometric Langlands) are major mathematical neighbours. No specific adapter from their statements to the current RH source or an indispensable dependency in the selected analytic chain was identified. They are not silently imported as evidence for RH.
- Family 013 (inverse Goldbach), and families concerning Egyptian fractions, totient-count asymptotics or Gaussian-prime walks, have analytic-number-theory techniques but no additional required source contract for this selected comparison beyond the closer graph and sieve papers already included.
- Family 076 is important to the Barker/ultraflat discussion, but the present repository import is about RH. Its binary-sign conclusion is not a theorem about the actual Möbius or Liouville sequence.
- The Szemerédi, finite-sums/products, general geometric, probabilistic and operator families are not included merely because they use positivity, Fourier analysis, a field, a spectrum or a Riemannian manifold.

The exclusion is a scope decision for this source deposit, not a theorem that the excluded mathematics can never contribute. New concrete source adapters can justify later additions without rewriting this snapshot or its review status.

## 14. Resident source inventory

The companion source snapshot is resident under `upstream/`. These links enumerate every selected manuscript directory and PDF. The source manifest, rather than this prose table, is the authority for file hashes and byte-for-byte completeness.

| Family | Manuscript directory | PDF |
|---|---|---|
| 007 | [Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026](upstream/preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/) | [PDF](upstream/preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/final.pdf) |
| 011 | [Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026](upstream/preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/) | [PDF](upstream/preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/paper.pdf) |
| 011 | [The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026](upstream/preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/) | [PDF](upstream/preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/paper.pdf) |
| 011 | [Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026](upstream/preprints/Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026/) | [PDF](upstream/preprints/Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026/paper.pdf) |
| 012 | [The-joint-Dickman-law-for-consecutive-integers-September-24-2026](upstream/preprints/The-joint-Dickman-law-for-consecutive-integers-September-24-2026/) | [PDF](upstream/preprints/The-joint-Dickman-law-for-consecutive-integers-September-24-2026/paper.pdf) |
| 014 | [Global-Arthur-Enhancements-of-Cuspidal-Excursion-Parameters-October-5-2026](upstream/preprints/Global-Arthur-Enhancements-of-Cuspidal-Excursion-Parameters-October-5-2026/) | [PDF](upstream/preprints/Global-Arthur-Enhancements-of-Cuspidal-Excursion-Parameters-October-5-2026/manuscript.pdf) |
| 014 | [Rationality-of-the-Canonical-Unramified-Arthur-Filtration-September-24-2026](upstream/preprints/Rationality-of-the-Canonical-Unramified-Arthur-Filtration-September-24-2026/) | [PDF](upstream/preprints/Rationality-of-the-Canonical-Unramified-Arthur-Filtration-September-24-2026/paper.pdf) |
| 014 | [Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level-September-24-2026](upstream/preprints/Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level-September-24-2026/) | [PDF](upstream/preprints/Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level-September-24-2026/paper.pdf) |
| 014 | [Temperedness-at-ramified-places-for-globally-generic-exceptional-groups-October-5-2026](upstream/preprints/Temperedness-at-ramified-places-for-globally-generic-exceptional-groups-October-5-2026/) | [PDF](upstream/preprints/Temperedness-at-ramified-places-for-globally-generic-exceptional-groups-October-5-2026/ramified-ramanujan.pdf) |
| 014 | [The-Restricted-Geometric-Langlands-Equivalence-in-Positive-Characteristic-September-24-2026](upstream/preprints/The-Restricted-Geometric-Langlands-Equivalence-in-Positive-Characteristic-September-24-2026/) | [PDF](upstream/preprints/The-Restricted-Geometric-Langlands-Equivalence-in-Positive-Characteristic-September-24-2026/paper.pdf) |
| 014 | [Constructible-tame-Hecke-eigensheaves-in-positive-characteristic-October-5-2026](upstream/preprints/Constructible-tame-Hecke-eigensheaves-in-positive-characteristic-October-5-2026/) | [PDF](upstream/preprints/Constructible-tame-Hecke-eigensheaves-in-positive-characteristic-October-5-2026/constructible-tame-hecke-eigensheaves-positive-characteristic.pdf) |
| 014 | [Tame-Hecke-Eigensheaves-with-Several-Marked-Points-October-5-2026](upstream/preprints/Tame-Hecke-Eigensheaves-with-Several-Marked-Points-October-5-2026/) | [PDF](upstream/preprints/Tame-Hecke-Eigensheaves-with-Several-Marked-Points-October-5-2026/Tame-Hecke-Eigensheaves-with-Several-Marked-Points.pdf) |
| 014 | [Frobenius-Structures-on-Tame-Hecke-Eigensheaves-October-5-2026](upstream/preprints/Frobenius-Structures-on-Tame-Hecke-Eigensheaves-October-5-2026/) | [PDF](upstream/preprints/Frobenius-Structures-on-Tame-Hecke-Eigensheaves-October-5-2026/tame-hecke-frobenius.pdf) |
| 021 | [A-quadratic-bound-for-Jacobsthals-function-September-25-2026](upstream/preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/) | [PDF](upstream/preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/paper.pdf) |
| 023 | [An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026](upstream/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/) | [PDF](upstream/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/paper.pdf) |
| 026 | [Positive-lower-density-of-large-prime-gaps-September-25-2026](upstream/preprints/Positive-lower-density-of-large-prime-gaps-September-25-2026/) | [PDF](upstream/preprints/Positive-lower-density-of-large-prime-gaps-September-25-2026/main.pdf) |
| 029 | [Primitive-roots-for-every-admissible-integer-base-October-4-2026](upstream/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/) | [PDF](upstream/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/primitive-roots-all-integer-bases.pdf) |
| 029 | [Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026](upstream/preprints/Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026/) | [PDF](upstream/preprints/Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026/simultaneous-primitive-roots-conditional-lower-bound-prime-bases.pdf) |
| 142 | [Deterministic-Polynomial-Factorization-over-Prime-Fields-October-4-2026](upstream/preprints/Deterministic-Polynomial-Factorization-over-Prime-Fields-October-4-2026/) | [PDF](upstream/preprints/Deterministic-Polynomial-Factorization-over-Prime-Fields-October-4-2026/Deterministic-Polynomial-Factorization-over-Prime-Fields.pdf) |
| 182 | [A-power-saving-for-intersective-polynomial-differences-with-an-exponent-depending-only-on-the-degree-October-5-2026](upstream/preprints/A-power-saving-for-intersective-polynomial-differences-with-an-exponent-depending-only-on-the-degree-October-5-2026/) | [PDF](upstream/preprints/A-power-saving-for-intersective-polynomial-differences-with-an-exponent-depending-only-on-the-degree-October-5-2026/power-saving-intersective-polynomial-differences.pdf) |
| 182 | [A-Power-Saving-for-Polynomial-Differences-at-Prime-Arguments-October-5-2026](upstream/preprints/A-Power-Saving-for-Polynomial-Differences-at-Prime-Arguments-October-5-2026/) | [PDF](upstream/preprints/A-Power-Saving-for-Polynomial-Differences-at-Prime-Arguments-October-5-2026/prime-argument-polynomial-differences.pdf) |
| 182 | [A-power-saving-for-square-difference-free-sets-September-24-2026](upstream/preprints/A-power-saving-for-square-difference-free-sets-September-24-2026/) | [PDF](upstream/preprints/A-power-saving-for-square-difference-free-sets-September-24-2026/paper.pdf) |

Advertised formal entry points are listed separately because a family may have more manuscripts than comparator statements. The importer must retain the corresponding solution modules and their transitive local dependencies, in addition to the challenge statements.

| Family | Scope document | Comparator roots |
|---|---|---|
| 007 | [Scope](upstream/lean/docs/007.md) | [OrdinaryElliott](upstream/lean/ComparatorChallenges/OrdinaryElliott.lean), [OrdinaryTwoPointCorrelations](upstream/lean/ComparatorChallenges/OrdinaryTwoPointCorrelations.lean) |
| 011 | No advertised family scope document | No advertised comparator found |
| 012 | [Scope](upstream/lean/docs/012.md) | [JointDickman](upstream/lean/ComparatorChallenges/JointDickman.lean) |
| 014 | No advertised family scope document | No advertised comparator found |
| 021 | [Scope](upstream/lean/docs/021.md) | [Jacobsthal](upstream/lean/ComparatorChallenges/Jacobsthal.lean), [JacobsthalImproved](upstream/lean/ComparatorChallenges/JacobsthalImproved.lean) |
| 023 | [Scope](upstream/lean/docs/023.md) | [PattersonFirstMoment](upstream/lean/ComparatorChallenges/PattersonFirstMoment.lean) |
| 026 | [Scope](upstream/lean/docs/026.md) | [PrimeGaps](upstream/lean/ComparatorChallenges/PrimeGaps.lean) |
| 029 | No advertised family scope document | No advertised comparator found |
| 142 | No advertised family scope document | No advertised comparator found |
| 182 | [Scope](upstream/lean/docs/182.md) | [SquareDifference](upstream/lean/ComparatorChallenges/SquareDifference.lean) |

The inherited family 003 contributes four additional comparator roots, physically retained in the unchanged core: [QuasiRiemannHypothesis](../2026-10-07-openai-quasi-riemann-import/upstream/lean/ComparatorChallenges/QuasiRiemannHypothesis.lean), [DirichletSevenEighths](../2026-10-07-openai-quasi-riemann-import/upstream/lean/ComparatorChallenges/DirichletSevenEighths.lean), [HeckeSevenEighths](../2026-10-07-openai-quasi-riemann-import/upstream/lean/ComparatorChallenges/HeckeSevenEighths.lean), and [SiegelZeros](../2026-10-07-openai-quasi-riemann-import/upstream/lean/ComparatorChallenges/SiegelZeros.lean). Thus the assembled view has eight new and four inherited comparator roots; the Hecke name retains its original field scope.
