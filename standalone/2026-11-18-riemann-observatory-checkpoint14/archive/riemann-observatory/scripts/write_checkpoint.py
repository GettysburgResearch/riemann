#!/usr/bin/env python3
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
M=json.loads((R/'quality/metrics.json').read_text())
def put(p,t):
 (R/p).parent.mkdir(parents=True,exist_ok=True);(R/p).write_text(t.strip()+'\n')
put('README.md',f'''# Riemann Observatory — research checkpoint

**Incomplete, evidence-calibrated checkpoint. Search cutoff2026-11-17 UTC.** Start with [START HERE](START_HERE.md), then [the synthesis](final_synthesis/comprehensive_report.md) and [coverage](quality/coverage_report.md).

This archive contains original mathematical analysis, source-linked records, exact computations, independent reviews and a resumable candidate discovery pipeline. It does not contain1,000 completed paper analyses or a proof of RH.

| Count | Meaning |
|---|---|
| {M['metadata_candidates']:,} | provider-deduplicated metadata candidate records; relevance/version review unfinished |
|56| deterministic lexical exclusions, preserved |
|5,147| metadata candidates pending substantive relevance review |
|20| selected checkpoint works with verified identity/source access and scoped records |
|8| complete inspected works or translations substantively read |
|12| selected works inspected only in specified portions |
|0| complete paper-wide Level2 or Level3 audits |
|6| independently reviewed scoped elementary claim groups; not whole-paper audits |
|39| theorem/conjecture/exercise records |
|11| cross-paper connection records |
|25| proposed actionable tasks, not discoveries |

The8 complete readings are PAPER-A002,A003,E001,E002,E003,R001,S001,S007 (S001 an English translation). Candidates and selected records overlap; do not add the counts.124 provider rows remain potential duplicate/version collisions. Three separately saved historical primary seeds must also be reconciled, not automatically added.

## Most useful results

- Exact multiplicity-aware polynomial approximants and a shrinking-gap counterexample to uniform triangular smoothing.
- A reusable Parseval/frame proof repairing one exterior-integral estimate in a recent source.
- A three-height spectral-count obstruction quantifying finite graph channel complexity.
- Explicit generic entire functions showing finite Li-positivity blindness, including a zero-count-matched construction.
- An exact integer certificate reconstructing Lagarias’s finite n≤5040 dependency.

These are elementary reconstructions and scoped proofs, not established novel research results. Every scope limitation is retained in campaign/reviewer files. No new infinite arithmetic estimate or RH resolution is claimed.

## Use and update

Structured entry points: corpus/bibliography.jsonl (curated), corpus/candidates.jsonl (metadata only), theorems/theorems.jsonl, audits/findings.jsonl, connections/connections.jsonl and graphs/knowledge_graph.jsonl. Schemas are documented in corpus/schema.md and graphs/graph_schema.md. Run `python scripts/validate_archive.py` and consult CONTINUATION.md.

The distributable ZIP omits source PDFs, complete extracted copyrighted source text and the86.9MB provider response cache. Source links, hashes and request provenance are included. All original analyses, code, results and reviews are included. No background process or future quota-reset trigger is installed; continuation requires another execution session.
''')
put('START_HERE.md','''# START HERE — one research day

This is a small audited core inside a large unreviewed discovery pool. Begin with quality/coverage_report.md before drawing conclusions from counts.

**First hour:** read connections/strongest_connections.md and the claim scopes in audits/adversarial_reviews/director_adjudication.md. The most reusable finding is that clustering matters even when every polynomial root is simple.

**Hours2–3:** reconstruct proposals/independent_campaigns/clustered_root_transition.md and multiplicity_general.md. Re-run exact coefficient/Gram checks. Compare fixed-root source hypotheses in PAPER-E002 and E003. Do not infer an arithmeticζ upper bound from the model.

**Hours4–5:** inspect audits/adversarial_reviews/af_boundary_repair.md and frame_third_review.md. Reproduce Parseval and exterior squared-tail summation before attempting a full audit of PAPER-A004.

**Hour6:** inspect spectral_counting_barrier.md and graph_skeptic.md. Ask whether a proposed spectral model changes the fixed-boundary assumption or merely tunes a leading density.

**Hour7:** read li_advocate.md and li_skeptic.md, including the derivative convention. Test any finite-positivity proposal against the counting-matched planted quartet.

**Hour8:** choose one finite task from final_synthesis/top_25_research_opportunities.md, write its exact hypotheses and failure controls, and update the durable queue. Prefer a proved cluster-uniform model lemma or a completed source audit before inventing another RH-equivalent conjecture.

For a historical rather than technical day, read PAPER-S001 translation record, PAPER-R001 and history/chronological_timeline.md; the original twentyth-century dependency literature remains largely unread in this checkpoint.
''')
report='''# What this research checkpoint actually learned

## Status and intellectual outcome

The thousand-work undertaking is unfinished. This execution produced a broad provisional candidate pool and a small source-grounded research core. It did not substantially resolve RH, prove a new infinite arithmetic bound, or establish publication novelty for any calculation. Its value is concrete negative knowledge, exact model calculations, one reconstructed truncation estimate, and an evidence-preserving continuation path.

The best discovery is a precise *uniformity* obstruction. A fixed-polynomial asymptotic with simple roots can fail badly across a family in which two simple roots approach at the approximation scale. That phenomenon is directly relevant to the unresolved step between finite-zero Gram calculations and infinite arithmetic approximation, although the polynomial result is not itself aζ theorem.

## 1. Conceptual transitions from1859 onward

The inspected Riemann translation shifts prime counting into analytic continuation, functional symmetry and zeros entering an explicit formula. Later estimates and equivalent criteria attack different objects: locations and statistics of zeros, closure of arithmetic approximation spaces, every-index positivity, or universal divisor inequalities. These are exact equivalences only with their hypotheses and infinite quantifiers retained.

The spectral transition adds the requirement of a genuine operator with a matching trace distribution. A semiclassical density match does not provide that operator. Rigorous computation adds certified finite ranges rather than an infinite limit theorem. Recent inspected sources replace termwise zero-side positivity by global finite-dimensional inequalities; those connections are already in the literature and are not discoveries of this archive.

Historical coverage is selective. Original PNT papers, Weil/Deligne geometry, much of mollifier/moment theory, de Branges and failed-proof literature were not audited here. See the timeline for the distinction between contextual history and actual source readings.

## 2. Which strategies seem closest to meaningful incremental progress?

This execution cannot rank approaches by likelihood of resolving RH. For achievable, reviewable increments, it favors: cluster-aware approximation models; effective fixed-test explicit-formula estimates; and rigorous evaluation of spectral model complexity before fitting zeros. These have explicit finite subproblems and counterexample controls.

For arithmetic progress, grouped residue bounds or a quantitative growing-zero-set Gram theorem would be consequential. Both require new estimates not supplied by the model calculations. The recent critical-line preprints merit full source and formal-artifact audits before their strongest claims are used as foundations. PAPER-A005's disclosed computational assumptions are kept visible.

## 3. Neglected ideas worth revisiting

Burnol's derivative-jet blocks make multiplicity a structural object rather than a nuisance. They suggest confluent coordinates for clusters, instead of individually estimating inverse derivatives. This is a historically grounded research direction, not a claim that the literature neglected it. Likewise, localized energy imports should begin from the corrected Rodgers–Tao version, and spectral-flow counting machinery should be used as an early model filter. No archival search was deep enough to establish that a particular old lemma was genuinely forgotten.

## 4. Strongest connections reconstructed here

**Clustering and approximation.** For Q=(1−z)^m, integer m≥1, degree boundN≥0 and L=N+m, the exact optimal squared circle error is

1−(L)_falling m/(L+1)_rising m,

with coefficient a_n=binom(n+m−1,m−1)(L−n)_falling m/(L+1)_rising m. It is asymptotic to m²/N for fixedm, consistent with Burnol's source result. For m=2, unchanged BCF triangular reciprocal smoothing instead has squared error1+4/N.

Even for the simple roots of Qθ=(1−z)(1−e^(−iθ)z), triangular smoothing has exact squared error[2N+2ReS+|S|²]/N², S=sum_{k=1}^N e^(−ikθ). At θ=c/N it tends to sinc(c/2)², positive except nonzero2pi resonances, while the optimal squared error remainsO(1/N). The exact optimal two-root Gram formula and confluent limit are preserved in the campaign. This does not contradict BCF's fixed-polynomial theorem. Next: a cluster-uniform arithmetic residue estimate, beginning with a finite confluent model.

**Frames and explicit-formula truncation.** In PAPER-A004's normalization, a Parseval frame bound and squared Fourier tails give ||H_nu||≪BL, J≪BLlogL and raw|E2|≪B²L²logL. After division by a²L⁴ this is stronger than required for the exterior piece; the printed E1 estimate dominates. This repairs the inspected bookkeeping path. Independent proofs appear in af_boundary_repair.md and frame_third_review.md. No full validation of that paper's analytic chain or main theorem follows.

**Spectral flow and complexity.** ForE finite first-order graph channels with fixed energy-independent unitary boundary data, N(t)=Lt/(2pi)+F(0)−F(t),0≤F<E. Therefore|N(4K)−3N(2K)+2N(K)|<3E. The Riemann–von Mangoldt target has curvatureKlog2/pi+O(logK). Even graphs retuned at eachK need E_K≥[log2/(3pi)+o(1)]K to achieve o(K) count errors at all three heights. Prior phase-flow machinery was located in Gnutzmann–Smilansky; novelty of the elementary consequence is not established. Infinite butterfly models illustrate a complementary issue: matching a renormalized oscillatory trace need not produce a locally finite positive spectral measure.

**Li finite blindness.** Explicit real symmetric entire products preserve every prescribed finite positive Li prefix while inserting an off-line quartet. A second construction also matches the smooth zero-count main terms toO(1). These functions lackζ's arithmetic Dirichlet series, Euler product and prescribed gamma factor. The result rules out generic finite-prefix arguments; it says nothing against Li's every-index criterion or against a futureζ-specific tail theorem.

## 5. Repeated obstacles across approaches

The same failures of quantifier transfer recur: fixed finite sets versus growing sets; fixed tests versus height-dependent tests; simple roots versus uniformly separated roots; existence of some approximants versus one chosen coefficient array; finite verification versus an infinite tail; leading asymptotics versus complete spectral measures. The archive supplies exact witnesses for several of these distinctions. Replacing such a missing lemma by a plausible analogy was the most common unproductive step.

## 6. Credible technical issues and source versions

No published argument is classified here as a verified mathematical error. The Endres–Steiner positive-count coefficient conflicts with its one-edge example under a literal reading; an absolute-spectrum convention plausibly explains it. This remains a counting-convention ambiguity, and the finite-graph no-go conclusion survives either way.

Ehm's introductory fixed-Selberg equivalence sentence needs a provenance check: a mixed-term limit and an existence criterion alone do not prove convergence of a prescribed array. The missing contextual theorem may exist; no error allegation is made. Only specified portions were read.

The AF printed exterior estimate was insufficient at the displayed rate under direct bookkeeping, but an alternate frame argument repairs that exact estimate. This is a successful repair, not evidence of a false main theorem. Rodgers–Tao's later arXiv version acknowledges a boundary-energy correction; it is version history, not an independently discovered current flaw. Formal repositories were not built in this execution.

## 7. What was independently established?

Self-contained ordinary mathematical reconstructions establish the multiplicity-aware exact polynomial optimum, moving-root nonuniformity, the generic Li-prefix counterexamples, the finite-channel curvature consequence and the exterior frame estimate under explicit hypotheses. Advocate/skeptic/adjudicator files preserve independent reasoning. These are not claimed historically new, formally verified, or publishable as they stand.

An exact integer lower-bound certificate independently reproduces Lagarias's finite n≤5040 step:5039 strict inequalities and equality at1. It uses no floating-point assertion. The sharper comparison slack Delta(n)~e^gamma gamma n/logn is an elementary consequence of the inspected harmonic-number formula, not an RH advance. No new infinite theorem about the actualζ function was proved.

## 8. Which ideas failed?

Unchanged triangular smoothing failed at multiplicity and at shrinking simple gaps. Generic finite Li certificates failed under planted quartets. A leading spectral density fit failed the three-height count test. A density-bound theorem chain failed by an exact exponent gap1/18 atσ=3/4. An apparent quantitative source defect did *not* survive further investigation as an obstruction: the frame repair resolved it. All are preserved with their scope and counterexamples.

## 9. Twenty-five actionable problems

The complete ranked list, with exact targets, source locators, next steps and counterexample controls, is in top_25_research_opportunities.md. The first tasks are finite cluster-uniform approximation and confluent Gram estimates; the hardest ask for grouped arithmetic residues or a prime-trace operator. The list contains25 proposed tasks, not25 findings.

## 10. What should a strong team do first?

Reproduce the exact clustered-root calculation, then attempt a uniform multi-cluster theorem in confluent coordinates. In parallel, finish a complete source audit of the recent pair-correlation/critical-line chain, treating the frame repair as a separately proved lemma and verifying formal theorem types and axioms against pinned artifacts. Assign another team to original Burnol/BCF dependencies and growing-set error bounds. Expand the bibliography by source-grounded dependency centrality rather than mass-producing records from metadata.

Before a publication claim, perform a serious novelty search, obtain expert mathematical review, and establish a result beyond the elementary model. The archive's strongest outcomes currently reduce the cost of asking the right next question; they do not answer RH.
'''
report += '\n## Second-pass mathematical increment\n\nTHM-E010 upgrades the fixed-c cluster limit to the uniform bound |L E_N(c/L)−F(c)|≤38(12+C²)²/L for allN≥0 and |c|≤C, L=N+2. The statement uses the actual polynomial optimum at every alias c=2pi*j*L. A divided-difference Gram basis and the explicit variance lower bound1/(12+c²) avoid small-gap cancellation; independent proofs and adjudication are saved. This is a finite-model theorem with no established novelty or arithmetic transfer. The next step is multi-cluster constants rather than repeating the two-root limit.\n\nHardy’s1914 three-page original French note was also completely read from facsimiles (PAPER-S007), including the endpoint moment argument. Its result is infinitely many critical-line zeros, with no proportion bound. Original scans corrected a missing-power transcription hazard; no error in Hardy’s note is alleged.\n'
put('final_synthesis/comprehensive_report.md',report)
put('executive_report.md','''# Executive checkpoint

Twenty selected works were accessed and recorded; eight complete inspected works/translations were read. Twelve records describe partial inspection. No entire paper received a completed Level2 or Level3 audit. The discovery pool contains5203 metadata records,56 exclusions and5147 pending relevance reviews, with124 possible duplicate/version rows. This is not a completed1000-paper corpus.

The reusable mathematical core is exact approximation behavior under multiplicities and shrinking gaps, a scoped frame estimate repairing an exterior truncation bound, finite graph complexity bounds and generic finite-Li blindness. Six scoped claim groups received independent reconstruction and adjudication; no historical novelty or new infiniteζ theorem is claimed. A finite Lagarias dependency was checked by exact integer arithmetic.

The archive includes39 theorem/conjecture/exercise records, eleven connections,25 actionable proposed tasks, source/version links, code/results, independent reviews and continuation scripts. No published error is asserted. Read final_synthesis/comprehensive_report.md for the substantive synthesis and quality/limitations.md before reuse.
''')
insights=[
('Simple does not mean uniformly separated','Moving simple roots separated byc/N can defeat triangular reciprocal smoothing; generic limiting squared error is sinc(c/2)². THM-E009.'),
('Multiplicity can be handled exactly in a finite model','An explicit degree-m reciprocal window achieves exact error1−(L)_falling m/(L+1)_rising m. THM-L004.'),
('Confluent coordinates expose noncommuting limits','Fixed distinct roots yield constant2 while merging roots yield4 in the scaled two-root optimum. THM-E007–E008. The intermediate curve need not be monotone or≥2.'),
('A full Gram bound can beat individual-entry estimates','Parseval plus squared tails repairs one explicit-formula exterior estimate. af_boundary_repair.md.'),
('Spectral count curvature measures hidden complexity','Three-height accuracy o(K) forces linearly many finite first-order channels. OBS-S-C2.'),
('Infinite oscillatory trace matching may hide infinite positive spectral mass','The butterfly construction source admits divergent mean density; a renormalized oscillatory distribution is not theζ counting measure. PAPER-S006.'),
('Finite Li positivity has explicit generic countermodels','Even smooth zero-count main terms and entire orderone do not close the infinite quantifier. THM-L001–L002.'),
('Root-sum conventions matter','The derivative at1 naturally gives inverse-power coefficients; reflection is needed for the familiar positive-power form. PAPER-L001–L002.'),
('A density premise can fail by a small exact exponent','Atσ3/4,5/9 does not imply o(T^1/2); gap1/18. CONN-A001.'),
('Fixed-test deweighting retains quantifiers','A fixed Q and Q′′ can be used before takingT→∞; optimizing aT-dependent test requires extra uniformity. PAPER-A003.'),
('Arithmetic criteria hide analytic input','Lagarias’s elementary inequality relies on Robin oscillations for the reverse implication. PAPER-R001.'),
('The finite arithmetic step can be checked exactly','A directed integer-series certificate verifies1..5040 independently; it does not control the tail. OBS-R001-FINITE.'),
('Source corrections change the right starting point','Rodgers–Tao v5 records corrected boundary-energy handling; later source version matters. PAPER-S004.'),
('Formal claims need boundary inspection','The inspected later critical-line preprint distinguishes computational search axioms from kernel checks. No build was run here. PAPER-A005.'),
('A uniform remainder can survive coalescence','THM-E010 proves an explicit compact-gap O_C(1/N) scaled-error remainder by stable divided differences; aliases need their genuine double-root optimum.'),
('An apparent flaw may be an invitation to repair','The exterior bookkeeping issue was resolved by a replacement estimate, preventing a premature false-theorem allegation. director_adjudication.md.')]
s='# Supported insights —16 of the requested100\n\nThis filename preserves the requested archive structure. Only16 supported synthesis insights are listed; no padding, novelty claim or claim of100 discoveries.\n\n'
for i,(a,b) in enumerate(insights,1):s+=f'{i}. **{a}.** {b}\n\n'
put('final_synthesis/top_100_insights.md',s)
put('quality/coverage_report.md',f'''# Quantitative coverage

Generated from quality/metrics.json. Cutoff2026-11-17.

| State | Actual | Requested scale |
|---|---:|---:|
| Metadata candidates |5203|2000–3000+ desired |
| Deterministically rejected lexical collisions |56|retain exclusions |
| Pending candidate relevance review |5147|fully classify before admission |
| Possible duplicate/version rows |124|resolve |
| Selected checkpoint works |20|approximately1000 |
| Full texts accessed among selected |20|all accessible selected |
| Complete inspected works/translations read |8|all1000 subject to access |
| Partial source inspections |12|do not silently treat as complete |
| Complete paper-wide Level2 audits |0|200–300 deeper target |
| Complete paper-wide Level3 audits |0|50–100 intensive target |
| Scoped elementary claim groups independently reconstructed |6|not comparable to paper targets |
| Theorem/conjecture/exercise records |39|grow with source evidence |
| Cross-paper connection records |11|no target padding |
| Proposed research tasks |25|25 |
| Supported synthesis insights |16|100 desired |

Whole readings: A002,A003,E001,E002,E003,R001,S001 (translation),S007 (original French). The Riemann source is an English translation rather than a collation with original German. Some partially inspected works have a locally reconstructed Level2 claim; their whole-work audit remains0. Source theorem statements are not independently re-proved merely because entered into the graph.

Provider historical strata counts:132 (1859–1900),58 (1901–1950),368 (1951–1980),988 (1981–2000),1558 (2001–2015),910 (2016–2023),1189 (2024–cutoff). These count metadata search matches, not relevant works, source audits or balanced importance selection. Language labels are provider output and can be wrong. Broad historical Riemann matches include surfaces and acoustics; substantial manual rejection remains.

Three separately source-grounded seeds(Riemann,DeligneI,DeligneII) are retained for reconciliation and are not added to5203. Curated works overlap metadata pool; do not add those counts either. DOI/provider dedup does not remove all preprint/publication manifestations.
''')
put('quality/limitations.md','''# Limitations and unfinished requirements

The requested1000-work analysis and200–300/50–100 deeper-audit program are not complete. Twenty works have durable records; only eight were completely substantively read in their inspected versions. Bibliographic metadata scale is much larger than source understanding. Whole-paper technical and independent audit counts are zero.

No new infiniteζ theorem, proof/disproof of RH, or established publishable novelty emerged. Scoped model proofs are useful but do not meet arithmetic hypotheses automatically. Numerical experiments without interval/exact certificates remain observations. Exact finite certificates do not imply infinite tails. No Lean build, source-published massive zero computation, or full correction-history sweep was executed.

Geometry/function fields, automorphic methods, moments/mollifiers, random matrices, non-English original sources, de Branges/canonical systems and controversial proof literature remain inadequately read. The discovery pool has lexical noise, possible duplicates, selection bias and incomplete forward/backward citation expansion. OpenAlex was the executed large-scale provider; the full requested multi-provider literature strategy remains pending. MathSciNet access was not obtained or assumed.

Search cutoff is2026-11-17, not a certification that every publication available that day was found. Recent preprint claims remain source-stated. The graph is a small theorem-level seed, not an exhaustive mathematical dependency graph. Some source-reported external dependencies are deliberately unaudited.

Public distribution omits source PDFs/full text and raw API payload cache. Included hashes identify local working copies; URLs and request index permit retrieval, subject to future availability. A later retrieval may have a different hash.

The runtime exposes no weekly usage balance or reset trigger. This checkpoint must not be described as exhausting a weekly allowance or as continuously running after this turn. Resume explicitly using CONTINUATION.md; all accumulated results are saved and reviewable.
''')
put('quality/evidence_audit.md','''# Evidence audit and epistemic boundary

Curated records link exact sources, versions and inspected scope. Theorem records distinguish source statements, conditions, conjectures and exercises. Six scoped mathematical groups have independent reconstructions recorded in director_adjudication.md. This does not upgrade source papers to full Level3 audits.

No verified source error is asserted. Two issues remain unresolved: Endres–Steiner positive/absolute counting conventions; Ehm's fixed-coefficient equivalence provenance. A separate exterior-integral estimate was repaired; record it as an alternate proof, not a false main-theorem finding. Rodgers–Tao correction history is source-acknowledged.

Experiments using integer/Fraction arithmetic carry exact assertions. Floating displays, high-precision sums and random stress tests carry no proof status. The independently reviewed all-n model proofs are ordinary mathematical arguments, not proof-assistant certificates. The exact Lagarias finite certificate was rerun and its directed-rounding logic independently reviewed.

Novelty assessment is incomplete. Established phase-flow provenance was found after independent reconstruction, demonstrating why independent derivation is insufficient to claim a new theorem. The general-m approximation formula and cluster limits require a serious approximation-theory literature search before publication claims.

Reviewable provenance is retained in track JSONL and logs even when master status is updated by adjudication. A stale 'pending' string in an original track is historical; consult master records plus director_adjudication.md for current checkpoint status.
''')
put('final_synthesis/open_problems_for_future_agents.md','''# Future-agent handoff

Read CONTINUATION.md and quality/metrics.json first. Do not count metadata candidates as read. Do not repeat finite Li or double-root experiments without a new hypothesis or quantitative target; their negative conclusions are already recorded.

Priority1: uniform multi-cluster approximation with a confluent Gram matrix and explicit remainder. Priority2: complete audit of recent pair-correlation/critical-line source chain and pinned formal artifacts. Priority3: arithmetic grouped-residue estimates and growing-set Gram control. Priority4: source-grounded importance selection and citation expansion for missing historical and geometric families.

The25 proposed tasks are fully specified in top_25_research_opportunities.md. Every new claimed discovery needs an exact statement, source hypotheses, independent counterexample attempt, novelty search and retained failed variants. Communicate no author-error allegation without explicit evidence and adjudication.
''')
print('Wrote checkpoint and reports')
