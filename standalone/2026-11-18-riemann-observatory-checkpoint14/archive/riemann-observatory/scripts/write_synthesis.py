#!/usr/bin/env python3
"""Build original human-readable checkpoint documents; no external prose copied."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def put(p,t):
 (R/p).parent.mkdir(parents=True,exist_ok=True);(R/p).write_text(t.strip()+'\n')
problems=[
('Uniform two-root optimal coefficients','PAPER-E002 Theorem1.4; THM-E007–E009','For Qθ=(1−z)(1−e^(−iθ)z), write the optimal degree≤N coefficients in a numerically stable confluent form, uniformly |θ|≤C/N.','Invert the exact2×2 Gram matrix, replace differences of exponentials by divided differences, and prove a remainder O_C(N^−2) for squared error.','The Gram condition number diverges as θN→0; separate the removable confluence from floating cancellation.','moderate; directly testable'),
('Several shrinking clusters','THM-L004; clustered_root_transition.md','For fixed multiplicities m_j and roots exp(ic_j/N), derive lim N inf||1−Q_N A||² from a confluent exponential Gram matrix, including coincident c_j.','Use residual jet constraints; rescale index k/N and prove Gram convergence in a divided-difference basis.','Uniform invertibility fails in the raw evaluation basis; root-collision strata need separate coordinates.','moderate/high; model problem'),
('Adaptive smoothing with simple nearby roots','THM-E009; PAPER-E003 Theorem2','Construct an explicit reciprocal-coefficient window whose squared H² error is O_C(1/N) for Qθ, uniformly |θ|≤C/N.','Use the exact optimal coefficients as a target, then ask if a bounded-degree family of θ-dependent windows attains its leading constant.','Unchanged triangular smoothing has positive limiting error at generic θ=c/N.','moderate; constructive'),
('Multiplicity-uniform asymptotics','THM-L004','Determine the largest growing m=m(N) for which 1−(N+m)_falling m/(N+m+1)_rising m is asymptotic to m²/N.','Bound the logarithm of the exact product with explicit uniform Taylor remainders.','m²/N ceases to be small when m is of order sqrtN; fixed-m asymptotics cannot be imported unchanged.','moderate; elementary asymptotic'),
('Growing zero-jet Gram sets','PAPER-E002 Theorem5.3','Find explicit separation and cardinality conditions on a zero set Z_N under which Burnol’s rescaled finite Gram limit is uniform.','First derive off-diagonal bounds for one pair in terms of |rho−rho_prime|logN; compare to the clustered polynomial model.','Fixed finite-set convergence is not an operator-norm estimate for growing sets.','high; meaningful NB increment'),
('Grouped reciprocal-derivative residues','PAPER-E003 Lemmas2–3','Replace individual 1/ζ′(ρ) estimates by bounds for sums of residues over clusters, allowing coalescence or multiple poles.','Write contour integrals around a cluster before estimating; compare divided differences to higher principal parts.','Arithmetic infinite-height tails and small derivatives remain uncontrolled; the toy model supplies no bound for ζ.','very high; arithmetic target'),
('Exact fixed-Selberg criterion provenance','PAPER-E004 p1 Proposition1.1','Determine whether RH alone is known to imply L² convergence for the exact fixed coefficient array μ(n)(1−logn/logN).','Trace all cited sequence-convergence results and distinguish n^−epsilon damped arrays, arbitrary optimizing coefficients and fixed Selberg weights.','A mixed-term limit plus existence of optimizers does not by itself imply convergence of a prescribed array.','moderate research audit; unresolved, no error assertion'),
('Weighted frame lemma at lower regularity','af_boundary_repair.md','Find sufficient decay |φhat(r)|≤C min(L,|r|^−p) to preserve exterior squared-tail mass O(LlogL) or better.','Integrate the squared envelope and sum endpoint distances on grid2pi/L, retaining all L-dependence in derivative norms.','For p≤1/2 total mass can diverge; scale-dependent constants can undo apparent gains.','moderate; harmonic-analysis lemma'),
('General signed explicit-formula weights','af_boundary_repair.md','Extend ||∫|ν|vv*||≪BL to weights controlled locally in L² instead of by a pointwise B.','Decompose frequency ranges and use a weighted frame embedding or local large-sieve inequality.','Absolute weight destroys prime cancellation; spikes at sample endpoints are adversarial tests.','high; reusable estimate'),
('Audit the remaining AF quantitative chain','PAPER-A004 §§4–6','Reconstruct every normalized error in Theorem5.7 with the exterior frame repair as an explicit dependency.','Keep separate raw double-integral and normalized matrix errors; check taper, window and prime-power spacing constants.','The repaired E2 estimate does not validate the other propositions or formalization.','high; technical audit'),
('Reproduce a formal theorem boundary','PAPER-A004 AppendixA; PAPER-A005 §8','Build an exact version-pinned formal artifact, inspect top-level theorem types and print all nonstandard axioms.','Fetch the cited commit/tag; build offline-reproducible environment; check comparator definitions equal the intended zero counts.','A source statement about a formal proof is not an executed kernel check; numerical search assumptions must remain visible.','high engineering/audit; no build performed here'),
('Effective fixed-test deweighting','PAPER-A003 Lemma3.2; PAPER-A006 Theorem1','Make Lamzouri’s fixed Q,Q′′ pair-correlation error effective at finiteT with explicit derivative norms.','Follow the original BGSTB mean-value estimates and retain constants for a single smooth eta.','A theorem for each fixed test does not justify a T-dependent optimized test.','high; analytic bookkeeping'),
('Density premise beyond the exponent gap','PAPER-A001 Theorem1.2; PAPER-A006 Theorem3','At sigma=3/4 seek N(sigma,T)=o(T^1/2), or specify the weakest replacement sufficient for the desired pair-correlation implication.','Compare every epsilon loss and uniformity range before proposing a theorem chain.','The Guth–Maynard exponent5/9 leaves a1/18 gap; merely renaming O as o cannot close it.','very high; analytic increment'),
('S3 inverse theorem','PAPER-A001 §13.1','Prove an inverse statement for near-extremizers of the specific S3 bound at sigma7/10 and scales identified by the authors.','Reconstruct their sharpness configuration, then quantify what structural exclusion yields a power saving.','Random-set calculations do not cover worst-case rational concentration.','very high; source-backed target'),
('Finite Li perturbation scale','THM-L001–L003','Optimize the smallest quartet heightT preserving a givenN-prefix for the normalized cosh baseline.','Compute exact rational quartet coefficients, bound baseline paired sums, then prove an explicit lower/upper scaling law.','The current sufficient O(N²) height is crude and not claimed sharp; numerical search alone is insufficient.','moderate; model robustness'),
('Arithmetic tail condition for Li','PAPER-L002 Theorem1; THM-L002','Formulate a ζ-specific, independently checkable tail estimate that, together with finitely many λ_n≥0, forces every λ_n≥0.','Name exactly which Euler-product or explicit-formula property defeats the planted quartet; test the implication on the counting-matched family.','Generic symmetry, orderone and smooth zero-count asymptotic already fail to suffice.','extremely high; may be RH-equivalent'),
('Strict finite positivity under jet constraints','THM-L002','Can a planted off-line quartet preserve an assigned finite list of local ξ-jets as well as a positive Li prefix in a specified nonarithmetic entire class?','Write the finite interpolation constraints and analyze whether zero-free symmetric multipliers can correct them without changing order.','Zero-free order-one symmetric multipliers are highly restricted; arbitrary interpolation can violate the growth class.','high; counterexample-class analysis'),
('Finite-channel sharp curvature','OBS-S-C1','Determine the supremum of |N(4K)−3N(2K)+2N(K)|/E over positive lengths and fixed unitary couplings.','Start with exact phase loops and attainable triples of fractional phase sums; distinguish open supremum from achieved bound.','The universal3E bound need not be sharp under a common linear phase path.','moderate; spectral model'),
('Coupled-graph exact witnesses','OBS-S-C1; spectral_counting_barrier.md','Construct a non-diagonal unitary graph family and rigorously count all eigenphase crossings in a finite interval.','Use a2×2 analytically solvable coupling; certify multiplicities and endpoint conventions.','Decoupled numerical checks do not validate arbitrary coupled spectral flow.','moderate; reproducible model check'),
('Auxiliary-system complexity','OBS-S-C2','If energy dependence S(k) is obtained by eliminating a self-adjoint M-dimensional auxiliary system, bound dyadic count curvature by O(E+M) plus explicit pole contributions.','Derive a secular determinant for one auxiliary level and track scattering phase across its poles.','Arbitrary unitary-valued S(k) need not come from any single self-adjoint operator.','high; potential model-selection advance'),
('Prime trace matching test','PAPER-S001; PAPER-S003 Proposition9.1','State one strip-analytic test space on which a proposed spectral model matches the completed-ζ explicit formula including gamma and trivial-zero terms.','Normalize Fourier/Mellin conventions on both sides before matching one prime frequency.','Leading KlogK density is far weaker than arithmetic trace equality.','very high; spectral missing lemma'),
('Corrected energy boundary flux','PAPER-S004 v5 §8','Extract a reusable sufficient condition under which integrated localized zero-flow energy controls terminal defect.','Separate flux across both moving boundaries and reproduce the corrected proposition dependencies.','Ignoring boundary transport can invalidate a monotonicity inference even when interior dissipation is nonnegative.','high; source reconstruction'),
('Explicit Lagarias slack bound','PAPER-R001 Lemma3.2; lagarias_slack.md','Find explicit C,n0 with |Delta(n)−e^gamma gamma n/logn|≤C n/log²n for every n≥n0.','Use0< H_n−logn−gamma<1/n and explicit logarithm remainder bounds; verify the finite remainder range exactly.','A better comparison constant does not control σ(n) or prove the infinite RH criterion.','moderate; attainable refinement'),
('Sparse arithmetic screening reduction','PAPER-R001 §2; original Robin dependency','Prove a precise reduction for a proposed sparse extremal sequence, including tie conventions, before checking only that sequence.','Read Robin’s original propositions and compare definitions of colossally abundant numbers across Alaoglu–Erdos and Lagarias.','Numerical success on a thin subset does not imply a universal divisor inequality without the reduction.','high audit; possible computation savings'),
('Certified source/version graph','PAPER-S004 v5 correction notice; PAPER-A001 version metadata','Link preprint versions, journal publications, corrections, translations and theorem dependencies without merging distinct mathematical statements.','Resolve the124 flagged candidate duplicates and audit historical primary seeds before increasing selected counts.','Provider metadata conflates editions/manifestations and can miss early works or include lexical collisions.','moderate engineering plus mathematical judgment')]
text='# Twenty-five actionable research opportunities\n\nThese are proposed tasks, not25 discoveries or claims of novelty. Ranking favors near-term verifiability and reusable negative knowledge over promises of resolving RH. Sources below refer to stable archive IDs; original locators and URLs are in paper records. Difficulty is qualitative.\n\n'
for i,(title,source,goal,nxt,barrier,diff) in enumerate(problems,1):
 progress='**Checkpoint progress:** THM-E010 now supplies a uniform explicit remainder bound through all two-root collisions. Coefficient formulas, sharp constants and multi-cluster generalization remain targets.\n\n' if i==1 else ''
 text+=f'## {i}. {title}\n\nSource: {source}.\n\n{progress}**Exact target:** {goal}\n\n**Next step:** {nxt}\n\n**Counterexample/barrier:** {barrier}\n\n**Significance and difficulty:** {diff}.\n\n'
put('final_synthesis/top_25_research_opportunities.md',text)
put('proposals/ranked_research_directions.md',text)
put('proposals/actionable_conjectures.md','''# Proposed statements and open tests

No new conjecture is represented as an established theorem. The25 precise tasks are in ranked_research_directions.md. Most are finite model problems or audits; the arithmetic statements may be as difficult as substantial parts of RH.

Highest-priority testable statements: uniform cluster-aware O(1/N) squared-error smoothing for fixed-multiplicity polynomial families; a confluent Gram limit with quantitative remainder; and an auxiliary-system extension of the finite-channel curvature bound. Their hypotheses and failure controls are specified in the ranked list. The Li arithmetic-tail problem remains deliberately an open request to specify a valid additional hypothesis, rather than a circular conjecture that assumes the desired positivity.
''')
put('connections/strongest_connections.md','''# Strongest source-level and reconstructed connections

## 1. Multiplicity and clustering expose the exact uniformity obstacle

Sources: PAPER-E002 Theorems1.3–1.4,5.3; PAPER-E003 Theorems1–2. The source lower bound weights zeros by m_rho², while the concrete zeta upper-bound approximation assumes a negative derivative moment and hence simple zeros. In the polynomial model the unchanged triangular window has squared error1+4/N at a double root. An optimal degree-m window for(1−z)^m has exact squared error1−(L)_falling m/(L+1)_rising m, L=N+m, asymptoticm²/N for fixedm.

More surprisingly, simplicity alone does not give a *uniform* triangular-window theorem over moving polynomials: two simple roots separated byc/N produce limiting squared error sinc(c/2)², positive for genericc, while the optimizer still has squared errorO(1/N). Both source theorems remain correct in their stated fixed-root/simple-root regimes. See independent_campaigns/clustered_root_transition.md and audits/adversarial_reviews/cluster_skeptic.md. The next arithmetic step is a grouped-residue/zero-jet estimate uniform in clusters; no such estimate forζ is proved here. The finite polynomial model is a rigorous test, not an automatic transfer theorem.

The second pass proves the explicit uniform bound |L E_N(c/L)−F(c)|≤38(12+C²)²/L for allN≥0,|c|≤C, with actual double-root optima at aliases. See uniform_cluster_remainder.md and independent review. This resolves the two-root compact-gap remainder question; next steps are multi-cluster constants and arithmetic transfer.

## 2. Frame orthogonality repairs an exterior truncation estimate

Source: PAPER-A004 Proposition5.2,pp8–9, with definitions§2 and envelope(5.7). The printed exterior bound alone loses a logarithmic factor after normalization. Instead bound the entire sampled Fourier Gram operator by Parseval, then use squared Fourier tails outside the height interval. Under the source's fixed smooth-window assumptions, ||H_nu||≪BL, J≪BLlogL and raw|E2|≪B²L²logL. This supplies the needed normalized remainder with room to spare; the E1 term dominates. See af_boundary_repair.md and frame_third_review.md. This is an independently checked replacement proof for one estimate, not a complete audit of the critical-line claim. Next: transplant this lemma to explicit-formula compressions with weaker local weight control.

## 3. Spectral flow plus three-height curvature forces model complexity

Sources: PAPER-S003 Proposition9.1; established quantum-graph phase-flow machinery cited in spectral_counting_barrier.md. A finite first-order graph withE channels has N(t)=Lt/(2pi)+F(0)−F(t),0≤F<E. Therefore its three-height curvature is<3E, whereas the classical zero-count main term has curvatureKlog2/pi+O(logK). Even graphs retuned at everyK require E_K≥[log2/(3pi)+o(1)]K to match counts atK,2K,4K to o(K). Leading-density fitting alone is insufficient. Energy-dependent coupling and noncompact models fall outside the claim. This is elementary derived negative knowledge with prior phase-flow provenance; no novelty is asserted.

## 4. Li positivity survives finite off-line perturbations

Sources: PAPER-L001 equations1.1–1.8; PAPER-L002 Theorem1/Corollary1. The generic criterion has an every-n quantifier. Explicit normalized symmetric products can have every prescribed finite positive prefix and off-line zeros, even while matching the Riemann–von Mangoldt smooth counting term toO(1). Exact quartet example has first11 positive coefficients and a negative coefficient91. This blocks generic finite-prefix arguments, while leaving arithmetic tail arguments open. No Euler product or completedζ gamma factor is preserved. See li_advocate.md and li_skeptic.md.

## 5. A theorem-chain obstruction at an exact exponent

Sources: PAPER-A001 Theorem1.2; PAPER-A006 Theorem3. Atσ=3/4 the Guth–Maynard density upper exponent is5/9, while the cited strong-density premise asks o(T^1/2). The gap is1/18. An upper bound of the former size does not supply the latter. This is a logical non-implication from known estimates, not evidence that the strong-density statement is false. A growth modelT^(19/36) witnesses the logical gap but is not a possibleζ zero distribution supplied by this investigation.
''')
put('connections/cross_field_opportunities.md','''# Cross-field opportunities with precise interfaces

Harmonic-analysis frame bounds enter explicit-formula truncation through the sampled Fourier Gram operator: the hypotheses are support lengthL, modulation grid2pi/L, uniform derivative norms and controlled weight tails. This interface is proved in the boundary-repair note.

Confluent interpolation and finite differences enter Nyman–Beurling polynomial models through residual jet constraints. Exact finite-dimensional formulas are established here. Transferring them toζ additionally requires arithmetic residue-tail control and uniform Gram estimates for growing zero sets; these are open interfaces, not inferred connections.

Unitary spectral flow enters the quantum-graph model through−iU*U′>0 and determinant total phase. Three-height curvature extracts a complexity lower bound. Extension to eliminated finite-dimensional self-adjoint auxiliary systems is a concrete proposed problem; arbitrary energy-dependent unitary matrices are excluded.

Historical localized-energy techniques are potentially reusable only with boundary-flux control. Rodgers–Tao v5 acknowledges a correction to§8; this is source-version evidence, not a newly detected flaw. Rebuild that argument before importing its energy logic.
''')
put('frontiers/research_programs.md','''# Frontier map: inspected evidence, not a complete survey

This checkpoint prioritizes four tracks. It does not certify global best bounds across all RH literature as of the cutoff.

| Program | Inspected source result | Bottleneck / meaningful increment |
|---|---|---|
| Zero-density / large values | Guth–Maynard PAPER-A001 Theorems1.1–1.2, publication2026 | Their§13.1 identifies S3 worst-case structure; improving it needs control of the actual near-extremizers |
| Critical-line proportions | PAPER-A003 source-stated >2/3 simple/on-line; newer PAPER-A005 source-claimed >67.35% | Recent preprints and computational assumptions must be audited. Extending test support or extracting effective fixed-test errors is meaningful; these are not RH proofs |
| Rigorous finite verification | PAPER-A002 zeros through height3×10^12; computation not rerun here | Certified finite height has no infinite tail implication without a new theorem |
| Nyman–Beurling approximation | PAPER-E001 closure criterion; E002 multiplicity² lower bound; E003 matching upper asymptotic under RH+derivative moment | Uniform cluster and infinite residue-tail control; a finite Gram optimum is not theζ upper bound |
| Li / positivity | PAPER-L002 general every-n criterion, partially inspected | Finite positivity plus generic entire-function axioms fails; specify an additional arithmetic tail mechanism |
| Spectral operators | PAPER-S003 finite compact graph obstruction | Match arithmetic trace distribution and correct spectral growth; retuned finite graphs have a quantitative channel-cost barrier |
| de Bruijn–Newman flow | PAPER-S004 Λ≥0, currentv5§8 correction notice | Corrected localized boundary energy is technically consequential; whole proof not audited |
| Arithmetic equivalent criteria | PAPER-R001 Lagarias, dependent on Robin | An elementary statement hides deep oscillation input; sharper slack helps computation but does not prove the infinite tail |

For historical evolution and exact analytic statements see history/ and analytic_track.md. Geometry/function fields, automorphic methods, de Branges/canonical systems, random matrices, explicit zero-free constants and failed proof literature remain major source-reading gaps. Candidate metadata are not a substitute for those audits.
''')
put('frontiers/missing_lemmas.md','''# Missing lemmas and exact interfaces

1. **Cluster-uniform arithmetic approximation:** an upper bound for the infiniteζ residue/principal-part sums stable under small derivatives and multiple zeros. Finite models show why individual inverse-derivative bounds and fixed finite-set limits may fail to be uniform. SourcesE002,E003.
2. **Uniform growing-set Gram control:** fixed-zero orthogonality in Burnol Theorem5.3 must be upgraded before increasing the number of zeros withN.
3. **Beyond support-one analytic information:** exact longer-support or higher-correlation inputs must be stated with their range and uniformity; no unconditional extension follows from the sources inspected here.
4. **Arithmetic exclusion of Li perturbations:** name a property ofζ that forbids the planted-quartet mechanism; generic order/symmetry/zero count does not do this.
5. **Spectral trace identity:** a self-adjoint candidate must realize the prime explicit formula in a common test space, including archimedean and trivial-zero terms.
6. **Boundary-flux transfer:** any localized energy import needs an explicit boundary defect estimate, not only interior dissipation.

See the25 ranked tasks for precise finite subproblems and proposed tests. None of these missing statements is claimed proved by the archive.
''')
put('frontiers/known_obstructions.md','''# Obstructions with scope

- Arbitrarily long positive Li prefixes do not force a critical-line zero set in the real symmetric order-one entire class, even with matching smooth zero-count main terms. No arithmetic conclusion follows (THM-L001–L002).
- Unchanged triangular reciprocal smoothing at a double boundary root has squared error1+4/N. Even moving simple roots at separationc/N can have nonzero limiting error. Fixed-polynomial theorems are not contradicted (THM-E005,E009).
- Finite fixed-boundary first-order graphs have bounded counting remainder and<3E three-height curvature. Sublinear channels cannot approximate classical zero counts to o(K) atK,2K,4K (OBS-S-C1,C2).
- Guth–Maynard's inspected density bound does not meet the exact strong-density exponent premise atσ=3/4. The target premise may still be true (CONN-A001).
- Density-one or finite-height zero information does not itself exclude sparse high off-line exceptions. Every claimed consequence must retain this quantifier distinction.

A printed exterior bound initially appeared insufficient; an alternate frame argument repairs that precise step. It is preserved as repaired negative research history, not as a surviving obstruction or error allegation.
''')
put('frontiers/unsolved_questions.md','''# Unsolved questions

The Riemann Hypothesis remains unresolved by this archive. No original infinite arithmetic bound, critical-line proportion, zero-free region, zero-density estimate orζ positivity theorem was established here.

The most accessible next questions are uniform cluster-adapted polynomial smoothing, explicit remainder bounds for the confluent Gram limit, and generalization of the repaired frame estimate. The most ambitious are grouped arithmetic residue bounds and a spectral prime-trace realization. Their exact tasks and counterexamples are recorded in final_synthesis/top_25_research_opportunities.md.
''')
put('history/chronological_timeline.md','''# Historical timeline with evidence limits

- **1859:** Riemann replaces prime counting by complex analytic structure, continuation, a functional equation and zeros. English translation read in PAPER-S001; original German manuscript not collated here.
- **1896:** Prime number theorem is a landmark contextual dependency. Original Hadamard/de la Vallée Poussin papers remain unaccessed priority tasks; candidate dates alone are not audits.
- **1914:** Hardy proves infinitely many critical-line zeros. Original French pp1012–1014 read from facsimiles in PAPER-S007; endpoint theta/moment argument reconstructed in scope.
- **Early/mid20th century:** critical-line and density methods, exponential sums, explicit formula and function-field analogues become distinct programs. This broad historical context is not a claim those sources were read.
- **1950s onward:** Hilbert-space closure/positivity criteria change the objects to be controlled; source reconstruction in this checkpoint begins with later Báez-Duarte and Burnol works rather than original Nyman/Beurling/Weil audits.
- **1970s onward:** zero statistics and quantum-chaos analogies motivate spectral approaches. Berry–Keating1999 partially read; the semiclassical analogy is distinguished from an operator realizingζ.
- **1984–2002:** Robin/Lagarias divisor inequalities turn RH into universal arithmetic inequalities. Lagarias source completely read; Robin proof remains external.
- **1997–2007:** Li-type positivity and generalized coefficient frameworks; original Li1997 not independently read here, Bombieri–Lagarias and Lagarias2007 inspected only in specified portions.
- **2001–2013:** Burnol's multiplicity² lower bound, integer-dilation closure criterion, and conditional optimal explicit approximants sharpen what approximation must achieve. Three preprints substantively read.
- **2018–2021:** Rodgers–Tao proveΛ≥0; later arXivv5 explicitly records a§8 boundary-energy correction. Partial source inspection only.
- **2020–2021:** Platt–Trudgian rigorous verification to3×10^12; source read, massive computation not rerun.
- **2024–2026:** Guth–Maynard large-value estimates and recent critical-line preprints enter this checkpoint. Recent claims and their formal/numerical dependencies are tracked separately from independently verified mathematics.

The candidate pool covers all requested date strata but has broad historical lexical matches. It does not establish a balanced historical primary corpus.
''')
put('history/evolution_of_methods.md','''# Conceptual transitions

The primary transition in1859 is from directly counting primes to studying an analytically continued function whose zeros enter an explicit formula (PAPER-S001). Subsequent methods separate into estimates that constrain zero locations/statistics and equivalences that restate the full problem as closure, positivity or universal arithmetic inequalities. The latter can expose a missing object without constructing it (E001–E003,R001,L002).

Spectral analogies add a further demand: a genuine self-adjoint operator and trace distribution, rather than an evocative leading counting asymptotic (S002–S003). Quantitative polynomial models expose local degeneracies that an analogy can hide. Rigorous computation changes finite verification into a theorem within an explicit height range, while leaving the infinite quantifier intact (A002).

The recent source pathway from unconditional pair-correlation inputs to global finite-dimensional positivity/inertia is conceptually distinct from termwise positivity. It is source-stated and partly reconstructed, not discovered by this archive; the recent full claims have not undergone complete technical audit here (A003–A006).
''')
put('history/abandoned_approaches.md','''# Failed attempts and useful negative knowledge

This checkpoint did not read a representative collection of historical claimed RH proofs. That requested corpus component remains incomplete; no author is categorized as having a failed proof based on metadata alone.

Our own rejected or repaired inferences:

1. Keep triangular reciprocal smoothing unchanged at a multiple root: disproved by exact error1+4/N.
2. Assume simplicity makes that smoothing uniform when roots move: disproved at separationc/N with generic positive sinc² limit.
3. Certify a generic critical-line zero set from a finite Li prefix plus order/symmetry/counting main term: explicit far quartet defeats the inference.
4. Fit a spectral model's leading density and assume precise zero-count compatibility: three-height curvature forces a linear channel cost.
5. Feed the Guth–Maynard exponent into the stronger inspected density premise: fails at an exact1/18 exponent gap.
6. Elevate a printed boundary bookkeeping loss to a false theorem: rejected after a frame-operator proof repaired the needed estimate. Retain both calculations.

Known author-acknowledged correction: Rodgers–Tao arXivv5§8. This is version history, not a new discovery of a current gap.
''')
put('experiments/reproducibility.md','''# Reproducibility

Python3.12 with standard library suffices for exact rational/integer scripts. mpmath is used for supplementary high-precision computations; sympy or other imports are documented inside individual scripts. No Lean/Sage/Arb build was performed. Noζ verification computation from a cited paper was rerun.

From the archive root:

```bash
python experiments/code/lagarias_finite.py
python experiments/code/lagarias_review_fraction.py
python experiments/code/li_advocate.py
python experiments/code/li_skeptic.py
python experiments/code/toy_advocate_exact.py
python experiments/code/multiplicity_general_exact.py
python experiments/code/clustered_root_transition.py
python experiments/code/spectral_counting_barrier.py
python experiments/code/analytic_checks.py
python scripts/build_archive.py
python scripts/validate_archive.py
```

Check actual filenames in experiments/code; source hashes and results accompany scripts. Exact integer/Fraction assertions are distinguished from floating displays and random stress tests. The analytic_checks random finite-multiset tests are diagnostics, not theorem proofs. The Li skeptic high-precision paired-zero sum is nonvalidated numerical evidence; the mathematical proof is the paired-product argument. Results are deterministic where seeds or exact inputs are given.

Source PDFs/extracted text are intentionally omitted from the distributable archive. Re-fetch exact source URLs/version IDs recorded in paper records and compare source_file_hashes.jsonl. Re-fetching a mutable author URL may change bytes; retain both hashes rather than overwrite provenance.
''')
print('Wrote synthesis documents and',len(problems),'problems')
