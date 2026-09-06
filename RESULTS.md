# Results: the cumulative mathematical account

The project has established useful components, not RH. This catalogue selects the strongest surviving results across the project; the [research index](research/RESULTS_INDEX.md) keeps the wider inherited corpus discoverable. Each entry states what it means, where its scope ends, and where to read the current mathematics. Earlier review is retained rather than represented as a fresh replay. Classical ingredients are identified in the sources; no novelty or priority claim is made here.

<a id="arithmetic"></a>
## Arithmetic: exact reductions and genuine positivity

### Robin's inequality: a complete canonical reduction

With $I(n)=\sigma(n)/n$, the classical Robin criterion is $I(n)<e^\gamma\log\log n$ for every integer $n>5040$. The repository's finite barrier excludes violations in $5041\le n\le5582$. Its canonical transform replaces prime support by consecutive primes and sorts exponents decreasingly, decreasing $n$ while increasing $I(n)$. The barrier also prevents a hypothetical violation from being transformed below the admissible threshold.

**Significance:** every hypothetical violation has a canonical representative, not merely a heuristically promising one. The resulting search domain is complete but infinite. An exact rational dynamic programme bounds each specified finite tail; its statement requires a nonempty subtree and certified exponent caps. Large source-reported traversal ranges without their complete streams are not substituted for this result.

[Current statement and proof route](research/integrated/CURRENT_RESULTS.md#robin) · [full resident proof and evidence](research/integrated/robin/finite-robin-foundations.md).

### SHARP: all-scale positivity above the critical power

For $\beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67)$ and $T(y)=(4\sqrt y-3)\mathbf1_{y\ge1}$, the reviewed theorem is

$$\sum_{n\le x}\frac{\beta(n)}{\sqrt n}T(x/n)^m>0\qquad(x\ge1,\ m\ge2),$$

including every real $m\ge2$. The proof uses a labelled Euler expansion, with the extra label at prime 67 retained, and a subunit prime-removal bound. Empty higher levels contribute nonnegative, not strictly positive, pair differences.

**Significance:** this is a global theorem for a literal signed arithmetic source, not just a positive finite scan. It is adjacent to, but does not cross, the critical linear-power problem. Exact distributional descent identifies the missing weighted downward variation; positivity of the quadratic primitive does not bound it.

[Current theorem and proof](research/integrated/CURRENT_RESULTS.md#sharp) · [source family](research/integrated/sharp_native/README.md).

### Fixed-prime bias and rough-number corridors

For the explicitly defined signed and unsigned $P_{61}$ divisor sums $F$ and $M$,

$$0\le F(x)\le M(x)\quad(1\le x<67),\qquad M(x)/42\le F(x)\le M(x)/8\quad(x\ge67).$$

This is an all-real-endpoint theorem with **one fixed product of primes through 61**. The old $1/40$ bound is false, and the old printed constant enclosure is invalid evidence; a replacement directed-primitive/integer-interval certificate supports the repaired result.

The actual fixed-base weighted-variation argument and Stieltjes transfer also survive. Mesoscopic Dickman/Bellman corridor results retain their specified classical estimates and parameter ranges. None supplies the remaining dynamic small-prime block or uniform growing-primorial estimate.

[Current bias theorem](research/integrated/CURRENT_RESULTS.md#p61) · [rough-number and Bellman source family](research/integrated/dickman_bellman/README.md).

<a id="analytic"></a>
## Analysis: exact criteria, source identities and operator structure

### Fixed Mellin consumers and compact Möbius wavelets

Fixed rows, the fixed 5:3 scalar and zero-safe smoothing give explicit reciprocal-zeta Mellin detectors. For an admissible fixed detector, subpower logarithmic negative mass implies holomorphy of its negative-part transform. The tail Landau argument then turns the appropriate source-specific arithmetic premise into an RH conclusion.

**Significance:** the analytic implication and its arithmetic input can be stated separately. The open estimate is not hidden in a selectable row, a smoothing parameter chosen after a hypothetical zero, or a conditional inequality mislabeled as a proof of its application.

The compact ratio-eight wavelet, Abel–Mertens frame, and same-kernel largest-prime/Vaughan translation are exact tools for attacking the signed source. The two historical wavelet energies have different boundary terms. The corrected Cauchy–Poisson energy has a rightmost-zero abscissa classification, with abscissa interpreted as an infimum and the Hardy/reciprocal-zeta inputs retained.

[Fixed-detector statement](research/integrated/CURRENT_RESULTS.md#mellin) · [corrected energies](research/integrated/CURRENT_RESULTS.md#wavelet) · [Mellin sources](research/integrated/mellin_landau/README.md) · [wavelet sources](research/integrated/wavelet_xd/README.md).

### Q4, half-divisors and source-preserving cancellation coordinates

Fourier, Haar and Jordan identities expose finite Gram structures; exact annularization and divisor/gcd decompositions isolate signed correlation terms. Half-divisor decompositions and subpower diagonal estimates separate an accessible diagonal from the unresolved signed near-collision contribution. Perron, regional Schur and matched-transfer identities describe how genuinely compatible estimates could be combined.

**Significance:** these reductions locate the arithmetic work instead of estimating an unrelated positive surrogate. Periodized/counting-measure bounds do not automatically transfer to the original physical measure. The repaired annular partition includes its small-variable sector; Hilbert cancellation must be kept signed. Fixed invertible filters do not justify varying-order inversion. A subpower bound on log-horizon length is automatic, not a second arithmetic achievement.

[Current cancellation boundaries](research/integrated/CURRENT_RESULTS.md#q4) · [Q4 sources](research/integrated/q4/README.md) · [half-divisor sources](research/integrated/vaughan_half_divisor/README.md) · [conditional combination tools](research/integrated/conjunctive/README.md).

### Xi: finite witness geometry and low-order positivity

Under the classical source-qualified RH resolvent representation, horizontal xi responses satisfy value-only secant, divided-difference and cross-Loewner minor inequalities. A hypothetical off-line zero creates a strict finite witness basin. These are proved **conditional criteria and witness-existence statements**, not a produced violation.

Separately, safe-real-axis xi geometry supports the earlier low-order PSD result with its named source inputs and repairs. A corrected entire-function construction gives a conditional source-to-Pick theorem through size three on all positive nodes. It permits empty, finite or countably infinite off-line spectra and keeps multiplicity and reserve accounting explicit.

**Significance:** both the disproof predicates and the limitations of low-order positivity are precise. The arbitrary-height RH-necessary tests are not the same theorem as unconditional safe-axis low-order positivity. Neither result supplies order four and higher. The old Lean input is defective; the conditional paper repair is not a completed formal source implementation.

[Current statements](research/integrated/CURRENT_RESULTS.md#xi) · [early finite criteria](research/integrated/xi/derivative-free-pick-loewner.md) · [low-order source family](research/integrated/xi_pick/README.md).

### Weil, cardinal capture, heat and effective Schur forms

Finite completion-of-squares identities and source-qualified cardinal constructions show how exceptional zero directions can be represented. Later multiplicity-aware complete-background interpolation supports capture in its specified adaptable Gaussian-confined hierarchy. That does not validate every earlier fixed-support or predetermined-grid construction.

For the specific full-source finite-window operator, a positive finite-codimension sector can be eliminated in its **energy completion**. The finite effective matrix retains the coupling to the whole infinite sector. Certified residual bounds enclose it from below; Galerkin matrices alone approach from above. No terminating positive test or residual convergence rate is inferred.

**Significance:** a rigorously bounded lower matrix could certify a whole window, not merely sampled vectors. No actual all-window sign is established. Birman–Schwinger threshold statements use point spectrum, not arbitrary spectrum; a positive complement cannot rescue an existing negative direction.

The heat programme also retains broad-kernel and fixed-resolution exterior results, and its stated large-center First-Hermite region below $(4-\epsilon)\log\log(2+|x|)$. The remaining domain includes bounded centers and unbounded heat parameters. Fixed-compact Brownian expansions and local safe-line Green results are retained at their own scopes, not extended to growing height or the complete critical intertwiner.

[Current operator and heat account](research/integrated/CURRENT_RESULTS.md#operators) · [heat sources](research/integrated/heat_hermite/README.md) · [safe-line sources](research/integrated/safe_line/README.md) · [earlier source-qualified operator spine](research/RESULTS_INDEX.md#inherited-source-results).

### Causal Euler/Dickman completion at the classical line

A horizon-faithful causal correction of the finite Euler product has a full-frequency norm estimate on $\Re s=1$, under its stated quantitative PNT/Mertens inputs. The correction is inactive before the finite product's exact arithmetic horizon.

**Significance:** it controls a complete signed-source error rather than a few selected frequencies. Its kernel being positive does not make the correction contractive. The corresponding local boundedness problem throughout $\Re s>1/2$ remains open; separate bounds on the two factors below one lose too much.

[Current line-one statement](research/integrated/CURRENT_RESULTS.md#causal) · [source-qualified proof discussion](reviews/B/REPORT.md). Acceptance is confined to that component, not every earlier or later layer on its research branch.

<a id="certificates"></a>
## Certificates: what has actually been established

**Finite Robin and complex Pick controls.** The retained Robin finite barrier is used in the complete canonical reduction. Two specified complex $8\times8$ Pick boxes are positive under their supplied primitive rectangles; the first has the recorded strict margin $>2^{-138}$. This excludes those boxes only. Exact matrix algebra does not independently regenerate the intended xi values.

**Fixed-$P_{61}$ replacement.** The all-real bias result above combines finite endpoint coverage with an analytic/divisor-tail argument. Directed MPFR primitives and the analytic ramp bound remain part of its trust contract.

**Seven-point continuum inequality.** A specified Montgomery–Taylor kernel satisfies a lower-pressure inequality for every six nonnegative real gaps. A complete interval cover, not a sample grid, supports the finite analytic inequality. Its 269/280-block simple-zero deductions retain separate trace, mean-square and tail inputs. The corrected scalar near $0.6730085$ is not, by itself, a newly certified zeta proportion or a priority claim.

[Exact seven-point statement](research/integrated/CURRENT_RESULTS.md#seven-point) · [evidence and reproduction entry points](COMPUTATIONS.md).

<a id="structures"></a>
## L-families and generalized structures

Literal Euler restoration, character orthogonality, fixed-conductor Witt expansions, finite-family measure identities, local Fourier geometry and GL2 deflation survive at their stated sources. Recurrence/Segre/cofactor identities and source-quotient constructions distinguish genuine structural relations from resemblance between fitted local factors.

The filtered-complex work retains its finite support/arity results and conditional degree-six Euler/lower-bound conclusions. The transferred differential uses the corrected sign convention and lower-page zigzags. Generic degree laws are not universal specialization laws; torsion boundary exceptions remain essential. The growing native Poincare ladder and complete numerical Epstein certificates remain held at their specified gaps.

**Significance:** this is mathematical work beyond a list of RH reformulations. It also tests which features do not suffice: nonprincipal family control need not control the principal member, and function-field purity is not a number-field transfer theorem. The native arithmetic binding is still an independent task.

[Representative exact statements and transfer boundaries](research/integrated/CURRENT_RESULTS.md#families) · [family proof/evidence account](reviews/B/REPORT.md) · [research programmes](PROGRAMMES.md#families).

## Useful negative results are part of the achievement

Source-blind convexity, uniform-center heat tuning, fixed-degree high-carrier Fredholm detection, positive Schur rescue, and several finite-to-global promotions have explicit obstructions. Other failures concern only a proof or a checker and leave the intended theorem open or repairable. [REFUTATIONS](REFUTATIONS.md) distinguishes these cases and points to viable next directions.

For the complete route inventory, including carry, four-band boundaries, native allocation and older source-only components, continue to [research navigation](research/RESULTS_INDEX.md). For one useful next contribution, choose a [specific open task](OPEN_CUTS.md).
