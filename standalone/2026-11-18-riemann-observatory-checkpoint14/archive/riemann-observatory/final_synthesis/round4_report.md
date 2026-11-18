# New exact interfaces and source repairs

This is an update to an active investigation, not a claim of a completed1000-work archive. Counts are generated separately from actual records. The main value of this phase is a small set of precise constructions, necessary conditions and proof repairs. Historical priority remains unassessed wherever stated; no claim of resolving RH or establishing a new unconditional zero bound is made.

## A prescribed varying-order approximation avoids a fixed multiplicity ceiling

For every fixed c>0 put epsilon_N=c/loglogN and alpha_N=epsilon_N logN. The explicit polynomial

V_(N,c)(s)=Sum_(n<=N)mu(n)(1-logn/logN)^(alpha_N)n^(-s)

uses zero weight at n=N. For every fixed integer q>=1, define d_q by the full critical-line squared norm with measure dt/[2pi|1/2+it|^(2q)]. Scoped independently checked proofs give

RH implies d_q(V_(N,c))=O_(q,c)((loglogN)^(-1/2)).

Conversely convergence of this same array implies RH by the previously reconstructed Hardy evaluation witness. Thus each fixed c gives an equivalent criterion. This does not prove convergence unconditionally. It differs from the fixed-order logarithmic Selberg family, whose convergence already forces simplicity. Here alpha_N tends to infinity, so no fixed finite multiplicity ceiling is imposed.

Two technical points make the forward implication valid. The inverse-Laplace kernel is integrated over the entire contour rather than assigned an arbitrary finite Perron cutoff. Its auxiliary height N^r can use a sufficiently small fixed r chosen after c. This absorbs the full noncompact reciprocal-zeta tail for every fixed c>0. The rate then uses Balazard–de Roton's published exact horizontal-ratio bound J_epsilon=O(epsilon), improving the first reconstructed zero-excision rate. The source deserves credit; the source also proves a stronger optimized-distance bound by a different array. No record distance or novelty claim is made for the present construction.

The next useful step is effective constants and a stated threshold N0. Nothing proved here is uniform for c_N→0 or q_N→infinity. Actual Littlewood/Titchmarsh source ancestry was traced, with inaccessible original formulas retained as access limits. A separately checked Borel–Caratheodory/curved-strip argument obtains every fixed distance parameter from one fixed source curve, rather than treating an unspecified source constant as arbitrary.

Evidence: THM-E-W312–314; director_sine_riesz_round4.md; littlewood_fixed_a_bridge_skeptic_round4.md. The first1/3 rate remains in the historical proof record and is superseded by the1/2 rate for current use.

## The exact small-shift slope records multiplicities

Under RH, let m_gamma be the multiplicity at each distinct ordinate gamma. Both signs are included separately. Three independently reconstructed arguments give

lim_(epsilon down to0) J_epsilon/epsilon
=Sum_gamma m_gamma[1-binomial(2m_gamma,m_gamma)/4^(m_gamma)]/(1/4+gamma²).

This is a scoped accepted reconstruction; its priority search is still open. The limit is at least C0=xi'(1)/xi(1), with equality exactly when every nontrivial zero is simple, assuming RH throughout. This is not a way to certify simplicity from finite computations or a few small shifts. A high multiple zero could create a very small excess.

The essential proof step controls escaped boundary energy. The contractive completed quotient gives a positive real-defect measure whose total mass tends C0. Every multiplicity-m zero has an explicit rescaled local profile. The order-one paired product says that the sum of all local real-defect masses is exactly C0; domination then controls every omitted height and intermediate scale. A different proof bounds product tails by a summable family of Poisson kernels. Completion factors alter squared norms only by o(epsilon).

The negative control F(w)=exp(w²) is useful: its quotient is still even/contractive in the relevant sense, but its first-order boundary energy escapes to infinity despite no zeros. Thus a generic Schur analogy omitting the paired-product mass identity is false. This is a precise reason for retaining the entire-function growth hypothesis.

Evidence: OBS-HR501–503; horizontal_ratio_slope_director_adjudication_round5.md. The old source's request for a precise asymptotic does not demonstrate novelty at the2026 cutoff. Later ratio/Hardy-space literature remains a priority search.

## A random model now has a complete expected law; arithmetic matching remains missing

For the unit-intensity sine process, finite sinc Gram matrices have expected per-length spectral measures converging to a unique probability law. Every fixed moment exists, factorial bounds give determinacy, and the law has no atom at zero. The no-atom proof uses global thinning, fixed block caps, a subcritical Paley–Wiener interpolation theorem, a deterministic quantile of the configuration-dependent Riesz constant, and interlacing. It does not assume an unproved integrated density of states or a uniform Riesz constant.

The first four moments are exactly1,4/3,2,13/4. A clipped polynomial plus relative Hilbert–Schmidt control transfers a positive-index lower bound without an operator-norm error tending to zero. The finite eigenvalue-displacement and Lipschitz-test lemmas actually compiled in Lean; the whole random-model and zeta argument did not.

For the arithmetic matrix, the concrete remaining target is D=84m3-16m4. With the exact source window/normalization, dimension ratio tending to1, low moments1 and4/3, and the inspected relative-HS approximation, D>31699883/275355 would improve the stated current source fraction1669159/2478195. The sine model gives D=116 and would lead to13/18, but supplies no arithmetic estimate. Proving this signed combination may be more efficient than proving separate full third/fourth moment asymptotics; no claim that it is easy is justified.

Evidence: THM-SG301–310; director_sine_riesz_round4.md; frontiers/moment_combination_missing_lemma.md. There is no almost-sure law, effective convergence rate, growing-moment theorem or actual prime-side higher-moment estimate in this model result.

## A source endpoint fails, and its critical application has a separate repair

In the inspected preprint and publisher versions of Gallardo–Gutiérrez–Seco2025, auxiliary Proposition5.1 includes the equality case of a weighted-Dirichlet bounded-bijection criterion. At alpha=-3,a=1, the exact polynomial sequence f_K=1+...+z^K has domain norm squared H_(K+1) tending to infinity while its image norm stays bounded. An explicit vector with coefficients (n+1)/log(n+2) lies outside the range. These are mathematical witnesses to the printed endpoint failure, not numerical suspicions.

The correct general classification is strict: with delta=a+(alpha+1)/2, positive delta gives a bounded bijection, negative delta gives a surjection with a one-dimensional kernel, and zero delta gives injective proper dense nonclosed range. Independent weighted-Hardy proofs agree. The finding is version-specific, and correction-history/priority searches have their stated finite scope.

A separate argument establishes unconditional density of Noor's generators in the area Bergman space D_-1. Quantitative classical Mobius cancellation gives bounded approximants converging weakly to1; weak closedness and invariant dilations then give full density. Raw norm convergence of those particular approximants is not claimed. This supplies the critical(-3,1) approximation target independently, without restoring the false inverse. General a>1 weighted-target transport is an active distinct investigation; an unbounded inverse multiplier cannot be silently used.

Evidence: FIND-DIRECTOR-GS-ENDPOINT; director_source_repairs_round4.md; THM-NOOR-A401/A402. Earlier main zero-free implications are not refuted by the endpoint witness.

## Historical reading changed both credit and error classification

Riemann's original1859 print, Genocchi's1860 correction and the later collected-work editorial note were compared at their actual passages. The constant correction in the prime formula is historically known; it is not a discovery of this program. A wrong integration endpoint in a modern transcription is distinguished from the correct original print. German originals, translations and later editions are manifestations of works, not extra papers used to pad counts.

Hadamard's original1896 paper was completely read. Von Mangoldt's announcement was read in full translation, and original1894/1895 grouped-limit passages were inspected. A local reconstruction gives O(log²h/h) for the grouped zero remainder under exactly stated local counts and a fixed contour margin. The full1895 publication explicitly controls the growing sums and predates a later accusation that those sums were forgotten. That accusation is not accepted as a verified historical error. This scoped check does not certify all earlier entire-function/Perron steps or the entire51-page paper.

Rodgers–Tao's actual61-page v5 was also substantively read. Its author-acknowledged boundary-energy revision was compared against older versions. Two local auxiliary expressions received independent scale/endpoint challenges, and a GPT-6.2 Sol reviewer reconstructed a signed far-field replacement for the consequential X4 use. These current reviews retain their own incomplete downstream scopes; no false-main-theorem claim follows.

## What a team should investigate next

First, attempt the signed arithmetic moment inequality with the exact fixed-window hypotheses and all normalization factors. Second, make the prescribed Riesz construction effective and finish its priority search. Third, resolve the weighted-target core problem using explicit continuous functionals or constructive approximants. Fourth, finish the actual headline Lean build and remaining author-program searches without conflating successful components with the headline theorem. The active primary-source search also covers2024–November2026 moment, zero-density and critical-line work; new preprints retain preprint status and are not called established records merely because their abstracts claim improvements.

The reusable advance is a sharper map of what assumptions each route really needs, backed by complete local proofs, negative controls and source locators. The corpus remains far below1000 substantive readings and its gaps remain explicit.
