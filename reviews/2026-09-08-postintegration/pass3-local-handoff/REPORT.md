# Intensive post-integration review — pass three

**Review disposition:** sixteen further research packets now have substantive manuscript review. Several complete component arguments and finite certificates merit extraction after the remaining source/package checks. No RH completion, canonical acceptance change, integration branch, or main merge is recommended by this review alone.

**Exact baseline:** main `f99d9e3908dde4865377c75d9ca051c1f545bf4f`; published review PR #827 at `13ac26caae546c8a6481a85b2f61ecc524dbbb27`. The published pass-two directory is sealed at `df7c4436784ab3a545da63427da5392e0c074662`, subtree `fac8ab751e2e629601f377b03bb2968c540b1322`. This pass is an add-only local continuation, **not pushed**. Keep the current cumulative public-facing main unchanged.

The recommendations concern the exact commits and files in [FILES.tsv](FILES.tsv), not moving branch names or the entirety of their packages. [CENSUS.tsv](CENSUS.tsv) distinguishes manuscript reading from package clearance. Mathematical reconstruction by this reviewer and independently written finite code do not, by themselves, establish a separate non-author referee identity.

## 1. Coverage and the version reconciliation

The published record, rather than the earlier downloadable draft, controls the inherited coverage. It records source-stability (ST) as read and entropy-feedback (EF) as still queued. The downloadable variant interchanges those statuses. The published record also explicitly leaves the three rational-residual minima unreplayed, whereas the downloadable variant reports additional calculations. Neither is silently overwritten or relabeled here. EF is now read in this pass; ST retains only its published prior scope. The known N=32 divisor graph uses **eleven**, not ten, prime bases.

This pass newly reads HT, AN, ES, FM, PC, SS, MC, CR, PR, RN and ANT on #803; DC and MW on #804; EF on #811; and GCP/CCS on #828/#829. That is **16 new main-manuscript packets, with 23 individually pinned mathematical/synthesis files**. The cumulative total is **37 of 45 identified packets at substantive main-manuscript depth**, leaving the eight-packet #805 lineage. This is not a claim that 37 packages, all their supporting code, or every imported theorem are cleared.

The closing dated-ref sweep retained the same eighteen observed heads. The #803 comparison from `31a35a90b0b924dc98a2c89c463fb59577f45a4e` to `db175de165a9077e709b1cb482998171ffc0c6e7` is one commit ahead and adds exactly nine ANT files, with no predecessor modifications. Thus the prior file reading is preserved without pretending the ANT addition had already been reviewed. The concurrent #828/#829 overlap comment was read. Searches and snapshots are sequential, not globally atomic, and do not exhaust arbitrary unpublished/deleted branches or all historical discussions.

## 2. Arithmetic norm transfer: a real improvement and a sharp obstruction

**Source:** [ANT proof](https://github.com/GettysburgResearch/riemann/blob/db175de165a9077e709b1cb482998171ffc0c6e7/standalone/2026-09-08-arithmetic-norm-transfer/PROOF.md), together with its pinned `SYNTHESIS.md`.

Three different quantities must remain separate. For a finite balanced Dirichlet polynomial, the original target error is

\[
E(p)=\int_1^\infty\left|1-\sum_n a_n\lfloor x/n\rfloor\right|^2\frac{dx}{x^2}.
\]

For a balanced variation, the homogeneous physical norm is \(R(q)=\int|\sum c_n\lfloor x/n\rfloor|^2dx/x^2\). The coefficient norm is \(S(q)=\sum|c_n|^2/n\). The complete divisor graph energy is

\[
G_N(q)=\sum_{p^kj\le N}\frac{\log p}{p^kj}|c_{p^kj}-c_j|^2.
\]

All lower vertices are still present, with coefficient zero when outside the variation's support. Removing those vertices would destroy the lower-diagonal argument.

### Constructive all-scale result

The explicit three-block completion preserves the literal Möbius prefix below every integer \(Y\ge2\), and satisfies \(p(1)=0,p'(1)=1,p(0)=-2\), support below \(8Y\), coefficients bounded by 84, and \(S(p)<1924+\log Y\). Its linear moment equations, disjoint blocks, elementary harmonic-divisor estimate, and coefficient bounds reconstruct correctly. The centering condition concerns the period mean, not vanishing of the physical error.

Using the **classical unconditional** Mertens estimate of Lee–Leong and a soft convexity bound for zeta, the source-specific argument gives

\[
E(p_Y^c)\ll Y\exp\{-c(\log Y)^{3/5}(\log\log Y)^{-1/5}\}.
\]

I checked the complete moment tails, the factor \(1+|t|\) in twisted partial summation, and the split over the entire critical frequency line. The estimate \(|p(1/2+it)|/\sqrt Y\le\min(B,\delta_Y(1+|t|))\), together with \(|\zeta|^2\ll(1+|t|)^{5/8}\), yields \(E\le2+CY\delta_Y^{3/8}\). No reciprocal-zeta bound in an unproved zero-free region is used.

**Recommendation:** retain this as an unconditional application of the named classical bounds, with non-instantiated constants. It gives \(o(Y)\) and every fixed logarithmic saving from the elementary linear bound. It gives neither a fixed power saving nor subpower energy; the exponent is still \(1-o(1)\). The external Mertens theorem is not newly proved or computationally rerun by this review.

### The uniform graph-to-physical comparison really loses a power

For balanced variations supported in \([Y,AY]\), with fixed \(A\), the manuscript proves

\[
R(q)\le A^2YS(q),\qquad
G_N(q)\ge(\log Y-\psi(A))S(q),\qquad
G_N(q)=(\log Y+O_A(1))S(q).
\]

The explicit variation

\[
q_Y(s)=Q_Y(s)(1-2^{1-s})^2(1-2^{-s})
\]

preserves all three zero moments, has support below \(16Y\), and satisfies \(R(q_Y)\ge Y/24\) while its coefficient norm stays bounded. Hence the optimal coefficient-uniform comparison factor has order **\(Y/\log Y\)**. The same obstruction persists for any fixed number of the indicated jets. No uniform assertion for a growing jet order follows.

The parallelogram comparison for \(p_Y^c\pm q_Y\) remains within the actual prefix/normalization class. It refutes a cheap estimate uniform over all such completions, **not** a bound for a selected native minimizer, the divisor spectral-gap theorem, or RH.

### Complete independent profile certificate

I reconstructed the variation profile from its rational cell formula rather than executing the author's producer. All 4,095 cells through 4096 and the full tail \(10000/(3\cdot4096^3)\) are retained. The outward result is

\[
1.70421945003684071009<C_*<1.70421949854322480466.
\]

This supports the stated asymptotic variation coefficient. It is not an actual-zeta residual minimum or the optimal leading constant of the uniform comparison problem. Author package authentication and rejection suites remain separate, unexecuted work.

## 3. Sharp anchoring and the native coherent channel

**Sources:** [GCP](https://github.com/GettysburgResearch/riemann/blob/528b33ac8d57b5a046260ee45d585cd3fe720f4c/standalone/2026-09-08-astra-grounding-capacity/PROOF.md); [CCS](https://github.com/GettysburgResearch/riemann/blob/f782788933dc21a0fe6a844950f5ca532eba7d86/standalone/2026-09-08-astra-coherent-channel-synthesis/PROOF.md); [CCS literal source](https://github.com/GettysburgResearch/riemann/blob/f782788933dc21a0fe6a844950f5ca532eba7d86/standalone/2026-09-08-astra-coherent-channel-synthesis/COHERENT_SOURCE.md). Both synthesis documents were read.

### An absolute centered gap coexists with growing anchoring cost

The squarefree prime box has centered gap \((3/2)\log2\); the all-exponent reservoir over a **fixed finite** prime alphabet has gap \(2\log2\). These are product spaces, not the conditioned set \(n\le N\).

Nevertheless, for the root contrast \(f(1)-\mathbb E_\mu f\), the exact inverse cost is

\[
G_P=\sum_{\varnothing\ne D}\frac{b_D}{\lambda_D},\qquad
\lambda_D=\sum_{p\in D}a_p.
\]

The optimal anchored constant \(C_P\) is the unique root above the inverse centered gap of

\[
\sum_{\varnothing\ne D}\frac{b_D}{C_P\lambda_D-1}=1.
\]

Here \((b_p,a_p)=(p^{-1},(1+p^{-1})\log p)\) in the squarefree case, and \(((p-1)^{-1},p\log p/(p-1))\) in the geometric-exponent case. The latter's countable reservoir reduces to finitely many root-visible modes; higher exponent eigenmodes vanish at the root. No infinite numerical enumeration is claimed.

The leading costs are \(G_{\rm sf}=(1/\zeta(2))\log\log P+O(1)\) and \(G_{\rm geo}=\log\log P+O(1)\), with \(C_P-G_P=O(1/\log\log P)\). The proofs' prime-tail comparison, real Euler factorization and bounded second inverse moment account for the remainder. They do not use PNT or RH to derive these asymptotics. This establishes sharpness of the **anchored** order, not sharpness of a centered bound on arbitrary divisor ideals.

For the specified root-shaped retained coupling, completing the square gives the exact Schur test \(c\ge|\tau|^2G_P\). It does not identify the actual missing Weil coupling as root-shaped or show its gamma/continuum reserve pays the cost.

### Independent finite enclosures and the overlap

A reviewer-written atanh-log implementation reconstructs every one of the 63 nonempty visible subsets at \(P=13\), and tests the monotone secular residual at both endpoints:

| Reservoir | Root contrast \(G_P\), outward enclosure | Anchored root \(C_P\), strict bracket |
|---|---|---|
| Squarefree | 1.18532285971072888629 to 1.18532285971072888630 | 1.91594153472685 to 1.91594153472687 |
| All exponents, six prime bases | 1.82250119177775968452 to 1.82250119177775968453 | 2.37221708831717 to 2.37221708831720 |

The squarefree conclusions in #828/#829 overlap and should be extracted once with both source histories. Agreement is not a second independent acceptance vote. GCP adds the geometric reservoir and specified root-Schur test. CCS additionally proves the stationary root-killed survival law, with uniformly small rescaled exponential error of order \((\log\log P)^{-2}\). Its normalization is **squared norm** \(1+V_P\), and its stationary mean lifetime is \(G_P\). The complete spectral weights and root boundary condition are load-bearing.

### The actual Möbius field identifies what is still uncontrolled

For the stopped shifted-exponential source, CCS gives exactly

\[
J_N=\sum_{k<N}\frac{M(k)^2}{k(k+1)}+\frac{M(N)^2}{N}.
\]

The final term is the complete stopped-input future. In the original Hilbert-valued divisor metric, its harmonic projection has squared norm \(J_N/H_N\). The same literal field's full prime-power edge energy is \((6/\pi^2)N\log N+O(N)\). All higher powers remain; the centered gap therefore points the wrong way for an upper bound on \(J_N\).

The exact work identity is

\[
J_N=\sum_{n\le N}\frac{\mu(n)^2}{n}
 +2\sum_{n\le N}\frac{\mu(n)M(n-1)}n.
\]

Convolution with the unchanged factorial source gives a legitimate causal output and a full-depth hypothetical-zero lower bound. A subpower upper bound on an unbounded cutoff sequence would close that route, but the signed-work estimate remains open. This is a useful literal-source obstruction to a proposed graph-only synthesis, not merely a changed-source example.

Independent controls reconstruct the finite pair norm, projection, work law, and complete prime-power energy. They do not machine-prove the asymptotic, infinite-domain spectral argument, or the root-hitting limit.

## 4. The annular-source sequence: finite range, regularity, and a stronger conditional criterion

The ten older #803 manuscripts are now read together, so their successive refinements need not be integrated as ten unrelated routes. Their common source is

\[
D(m)=m^{-1}\sum_n\Lambda(n)w(n/m^2)-45m/128+1/4,
\]

with the compact two-piece weight on \([1/4,4]\) and **all** prime powers. Source roots and exact hashes are in FILES.tsv.

### HT and AN: a substantial finite continuum result, not all-scale positivity

HT combines the named finite-height zero theorem with a complete tail budget. Its lower bound gives \(D(m)>1/10\) for all real \(2\le m\le5\cdot10^{10}\), and \(D(m)>1/200\) through \(m=10^{11}\). Thus this is a continuous parameter theorem reaching \(X=m^2=10^{22}\), not just sampled prime sums.

The external zero-height input is the Platt–Trudgian theorem through \(3\cdot10^{12}\). This review did not rerun that census. I independently enclosed the elementary constants, including \(C_0<237/5000\), the high-zero inverse-square tail \(<37/(25\cdot10^{12})\), and the two finite-range margin budgets. The tail bound grows with scale, so the finite-height theorem does not settle the unbounded estimate.

AN's unshifted scalar \(I(m)=D(m)-1/4\) is negative at the actual point \(m=2\). The independently reconstructed interval is

\[
-0.03371719408640352243<I(2)<-0.03371719408640352242.
\]

This rejects that unshifted sign proposal, not the shifted \(D\) criterion. The fixed-filter Mellin/pole argument and integer-to-continuum control retain their actual normalization. A unit-window operator sign is not an automatic proof of this separate scalar sign.

### ES: the sharp precision scale and a genuine Euler counterfamily

ES establishes uniform Lipschitz control of the native \(D\), and \(D'(m)\to0\) in essential supremum using the unconditional PNT. All jumps of the derivative weight are included. Slow variation still permits unbounded slowly varying excursions.

For perturbations bounded coefficientwise by \(C\Lambda(n)n^{-\eta}\), the exact normalized error scale is \(X^{1/2-\eta}\). At the critical precision \(\eta=1/2\), the coefficient is \(49C/144\). A strictly positive comparison margin transfers only with the requisite smallness, not merely a finite-prefix agreement.

The counterfamily is supported on ordinary prime powers and has a meromorphic Euler product, positive multiplicative coefficients, an exactly matched safe moment, and unchanged small-prime factors. Its existence proof selects parameters outside countably many cancellation sets. It has new zeros and scalar excursions because its large-prime factors and completion are changed. It does **not** retain zeta's full functional equation or infinite arithmetic identity; it is not an off-line zeta zero. No numerical parameter pair is certified.

### FM, PC and SS: which count argument survives

FM reconstructs the exact centered prime-correlation Gram, its summable lattice correction, and the unconditional \(M\log M\) diagonal asymptotic. Under RH the off-diagonal must cancel that leading diagonal. Moreover, every fixed even moment has positive logarithmic mean under RH. Thus a hoped-for sublinear fixed-even-moment bound is incompatible even with the case one is trying to prove. This refutes that proposed sufficient estimate, not the failure-count target.

PC supplies the complete distributional curvature measure: the activation, central and exit prime-power atoms have their different signs and coincident atoms are added. Green interpolation and negative-run estimates then connect a hypothetical off-line zero to a lower growth exponent for the count of failures. The absolute-value divisor renewal is not a contraction.

SS strengthens the criterion. For either integer samples \(D(j)\) or square samples \(D(j^2)\), at any fixed depth \(-h\), **any fixed power saving**

\[
\#\{2\le j\le K:D(j^r)<-h\}=O(K^{1-\delta}),
\quad r\in\{1,2\},\quad\delta>0,
\]

would imply RH. The proof converts sparse bad cells plus amplitude \(m^u\) into a lower pole boundary, then improves the amplitude and iterates a fixed number of times. It does not assume a zero attaining the rightmost supremum, a spectral gap near it, or simple zeros. The Landau continuation step distinguishes an actual convergent transform from a merely continued integral.

**Recommendation:** retain the complete curvature and bootstrap arguments as conditional components, and make SS the sharper public count target. The native saving is not proved; none of the finite controls supplies it.

## 5. Completions and residual minimization: the correct order of implications

### MC and CR: a solved variational problem with an unknown intercept

The bounded two-block completion matches \(\mu\) below \(Y\), has \(p(1)=0,p'(1)=1\), support below \(4Y\), coefficients below 20, and logarithmic diagonal norm. The quadratic convolution identity agrees with the native Mangoldt source below its exact cutoff. Its critical-line integral is justified without RH, retaining the complete frequency tail.

CR proves that this **real signed**, non-Hermitian quadratic functional satisfies

\[
\mathcal I_m(p)=D(m)-1/4+(45/128)m(p'(1)-1)^2.
\]

Its Hessian has rank one. On the two-jet class the full functional is constant. Optimizing free completion coefficients therefore cannot change its unknown intercept. A positive Hessian is not a nonnegative minimum.

The uniform tail bound applies before choosing a frequency cutoff and shortens the remaining interval to \(Y^\nu\) for fixed \(\nu>2/3\). It does not supply the sign on that interval. I separately checked the general Laurent residue polynomial, including all three Taylor data; deleting its terms would misnormalize a contour argument.

### PR and RN: the positive norm is a genuinely different optimization

PR's complete positive residual is the physical floor error \(E(p)\), equal to its full Mellin-Plancherel norm. This is not the preceding signed \(p(s)^2\) integral. Balance gives finite complete-period control, and delayed Hardy evaluation gives lower growth forced by a hypothetical zero.

The two explicit small trial bounds reproduce independently: approximately 0.19000634 for the two-scale example, and a conservative complete-period enclosure contained in \((0.057,0.059)\) for the second. The latter retains an explicit future-period upper bound. These are **trial values, not optimal minima**.

RN's bounded oblique correction imposes \(p'(1)=1\) with priced norm cost; it is not a contraction to iterate. The finite floor Gram minorant, pairwise-period formula, and stationarity-residual enclosure give a valid route to exact finite minimum certificates. Its strengthened two-evaluation zero lower bound retains the prescribed derivative datum.

**Numerical hold retained:** I have not replayed RN's four optimized two-jet minima. Nor does this pass convert the published pass-two hold on RC's three balance-only minima into a successful replay. Their feasible classes differ, and the local downloadable review variant must not be silently substituted for the published record. The original author numerical producers, accepting code and rejection tests still need source-matched audit or an explicitly accepted independent replacement.

## 6. Domain cutoff, resonance and entropy work

### DC: genuine local realization, but not a free global cutoff

The complete DC manuscript consists of `CONSTRUCTION.md`, `GRAM_FLOOR.md`, and `TAIL_AND_DAMPING.md`, all read. Möbius inversion constructs ordinary compact inputs whose outputs lie in the original causal source space and match the fixed target through the requested horizon. The target has a prescribed removable zero at the real half-node, not a zero selected from zeta. Selected hypothetical zero jets produce a full-future Gram lower bound, including multiplicities.

The uniform finite Gram floor is a legitimate small-frequency interpolation bound, with an explicit enormous finite cutoff preserving a fraction of the margin. It proves finite invertibility, not vanishing intrinsic distance or practical complexity.

Dense spans formed by damping nearby sources can change the source domain. The actual-source counterexample to naive output contraction and the exact damping/convolution commutator prevent treating such damping as a cost-free map inside the original space. The weighted coefficient mass is an upper-error budget; its nonvanishing does not prove an equal lower bound for the commutator norm.

### MW: signed work is real, and fixed-target inputs necessarily resonate

The four-state realization has an explicitly positive observability Gram. Its Lyapunov identity, four positive pivots, source/target norms and full-future work accounting reconstruct independently. At the literal first three Möbius impulses,

\[
0.05961877853773261039<W_3<0.05961877853773261040.
\]

Thus universal diagonal domination of this input energy is already false at \(N=3\).

The resonance theorem tests a fixed finite packet of actual critical-line zeros, with multiplicities, using stable boundary division and finite adjoint probes. It yields polynomial lower growth for the ordinary-input energy; a single classical critical-line zero already implies a logarithmic cutoff lower bound. It assumes neither RH nor simplicity.

This obstructs bounded **input** cost for that exact target. Stable source convolution may cancel the resonant mode in the **output**, so it is not a disproof of bounded outputs or arbitrary re-chosen controllers. The original 65,536-event campaign and the earlier compact-domain numerical trial remain unreplayed here.

### EF: complete entropy drift and one still-open signed work term

EF keeps all prime powers and the original one-dimensional Cauchy frequency measure. Its log-cosh drift, full prime jumps, nonnegative curvature remainder, signed higher-power contribution and initial term give

\[
|2E(X)-W(X)|<8+24\log(1+\log X).
\]

This is a useful reduction of the full entropy cost to source-specific signed feedback work. Positive feedback kernels still have mixed-prime correlations and do not upper-bound that work by their diagonal or an independent prime-phase average. The earlier endpoint/prime-discrepancy adapters retain their original norms and targets; EF does not manufacture a new estimate by identifying them with the divisor graph.

## 7. Evidence, repair obligations, and the next review

The new independent checker imports **no author module** and uses only integers, Fractions and outward dyadic intervals. The full ordinary/optimized outputs agree byte-for-byte. There are 4,966 accepting assertions, **4,095 of which are the coverage cells of one profile certificate**, not 4,095 independent mathematical results. See [VALIDATION.md](VALIDATION.md), [the source](independent_checks.py), and [the complete exact output](evidence/independent-normal.json).

The actual capacity calculations use all visible modes and directed logarithms. Product-basis algebra controls use explicitly synthetic rational rates. Möbius norm/graph controls keep all prime powers. The independent small trial checks use their own complete-period bounds. None of these finite checks machine-proves the asymptotic arguments, source identities on an infinite domain, or imported zero verification.

No fatal error was found in the main component arguments reconstructed here. That is a recommendation at the stated hypotheses, not blanket acceptance. The concrete handoff requirements are: keep all source metrics distinct; merge the overlapping squarefree capacity result only once; retain higher-power and endpoint/future terms; do not promote finite/inverse/conditioning results into the missing native upper bound; and finish the named numerical/package holds.

The remaining eight main manuscripts are DO, BG, GT, BL, GE, TE, BH and CL on #805 at `602d7ddf9dbd2ba79bd6cada149772111ca72150`. The next pass should read that complete lineage and settle the remaining certificate and auxiliary-source obligations, including the separately required preintegration #790 adapters. Later arrivals should be compared against the locks here, not silently added to this pass's coverage. [RESUME.md](RESUME.md) supplies the exact queue and commands.

A future integration should start from then-current main and extract scoped mathematics from all passes into its cumulative account. Do not merge the review branch as though it were an accepted research branch. This pass has not changed main, review PR #827, active research, publication settings, or any mathematical verdict.

## External inputs checked at their stated use

- Ethan S. Lee and Nicol Leong, *New explicit bounds for Mertens function and the reciprocal of the Riemann zeta-function*, [arXiv:2208.06141](https://arxiv.org/abs/2208.06141). The imported qualitative Vinogradov–Korobov-shaped Mertens bound is unconditional. No numerical constants or source experiment were reproduced here.
- Dave Platt and Tim Trudgian, *The Riemann hypothesis is true up to 3·10^12*, [arXiv:2004.09765](https://arxiv.org/abs/2004.09765). This is the finite-height input, not a global RH premise. The external computation was not rerun.
- The soft zeta convexity/approximate-functional-equation input is the standard one recorded by the manuscripts; see [DLMF 25.9](https://dlmf.nist.gov/25.9). It supplies existence bounds, not an effective finite certificate in this review.
- Classical Landau, Plancherel/Hardy, squarefree counting, Green-function and finite-product spectral mechanisms are credited in the exact manuscripts. Their use does not establish external novelty or separate formal-kernel acceptance.
