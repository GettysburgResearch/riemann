#!/usr/bin/env python3
"""Current, metric-driven checkpoint; preserves first-release narrative separately."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
M=json.loads((R/'quality/metrics.json').read_text());B=[json.loads(x) for x in (R/'corpus/bibliography.jsonl').read_text().splitlines()]
if (R/'final_synthesis/round11_report.md').exists():
 from write_round11_checkpoint import write_current
 write_current(R,M)
 raise SystemExit(0)
if (R/'final_synthesis/round10_report.md').exists():
 from write_round10_checkpoint import write_current
 write_current(R,M)
 raise SystemExit(0)
def put(p,t):(R/p).write_text(t.strip()+'\n')
levels=M['whole_work_audit_levels']
read_ids=', '.join(x['id'] for x in B if x['whole_work_read'])
counts=f'''| Evidence state | Actual |\n|---|---:|\n| Metadata candidate records |{M['metadata_candidates']:,}|\n| Deterministic lexical exclusions |{M['metadata_candidates_rejected']}|\n| Provider records surviving lexical screen |{M['metadata_candidates_pending']:,}|\n| Curated metadata/dependency candidate decisions |{M.get('curated_candidate_decisions',0)}|\n| Selected source records |{M['selected_checkpoint_works']}|\n| Selected full texts accessed |{M['fulltexts_accessed_selected']}|\n| Selected primary-source excerpts only |{M.get('selected_primary_excerpt_accessed',0)}|\n| Complete substantive readings |{M['whole_work_or_translation_read']}|\n| Complete paper-wide Level2/3 audits |{levels.get('2',0)} / {levels.get('3',0)}|\n| Scoped independently adjudicated claim groups |{M['scoped_level3_claim_groups']}|\n| Theorem/conjecture/exercise records |{M['theorem_or_exercise_records']}|\n| Connection records |{M['connection_records']}|\n| Graph nodes / edges |{M['graph_nodes']} / {M['graph_edges']}|'''
summary='''The program is active. Its current results include exact source reconstructions, conditional approximation and multiplicity formulas, rigorous model obstructions, and independently checked numerical/formal components. The1000-work substantive-reading target is far from complete. No proof/disproof of RH, new unconditional bound on zeta zeros, or established publication novelty is claimed.'''
put('README.md',f'''# Riemann Observatory — active research checkpoint

Literature cutoff2026-11-17UTC. {summary}

{counts}

Start with START_HERE.md, executive_report.md and final_synthesis/round8_report.md. The first release's narrative is retained as final_synthesis/checkpoint1_report.md; current metrics, source scopes and active process status supersede its counts/status. Source PDFs/full extracted text and private build caches are excluded from distribution. Licensed numeric inputs and reference-code notices are included where redistribution is allowed.

Important current outputs: a scoped reconstruction of the source RH-only optimized Nyman–Beurling theorem with a fixed-Laurent qualification; exact finite Legendre/Bessel prefix costs and joint matching limits; a source-dependent classical shifted-array rate and exact multiplicity slope; general Herglotz boundary energy; an RH-conditional empty-spectrum control for one xi operator; corrected weighted-closure threshold with explicit source counterexamples; sine-Gram law and clipped relative-Hilbert–Schmidt arithmetic interface; finite Lagarias support certificate through720720. Earlier Riesz, grouped-residue, spectral-counting, geometric and historical reconstructions remain in the archive. Each item has its own model, conditional, external-input and review scope.

All substantive claims carry exact scope. A theorem-level scoped reconstruction is not a complete paper audit. Metadata records are not source readings. Candidate and selected pools overlap and must not be added.124 potential provider duplicate/version rows remain unresolved.

Persistent state: corpus/bibliography.jsonl, theorems/theorems.jsonl, connections/connections.jsonl, audits/findings.jsonl and audits/reviewed_claim_groups.jsonl. Run scripts/build_archive.py, merge_findings.py, write_live_checkpoint.py, validate_archive.py and render_and_package.py for a later synthesis checkpoint. Do not run the frozen first-release prose generator write_checkpoint.py without revising its inputs. See CONTINUATION.md for active work.
''')
put('executive_report.md',f'''# Executive checkpoint — research continues

{summary}

{counts}

The earlier confluent-Gram route identified an arithmetic zero-removed-factor and infinite-tail obstacle. The independently reconstructed adaptive source theorem now supplies an alternative RH-conditional optimized upper construction through contour groups, delayed profiles and actual integer quadrature. It does not prove the missing Gram estimate or settle prescribed-array questions. Fixed-size clusters still cannot cover the full unscaled zero multiset.

The Selberg audit recovered established prior art: prescribed logarithmic Möbius convergence implies RH AND simplicity. Stronger fixed spectral downweighting does not remove that obstruction. The unrestricted-coefficient weighted criterion remains valid. Thus existence, fixed-array convergence and subsequential convergence require separate statements.

The formal/numeric audit has pinned source commits, compared definitions/statements, rerun a large first-window search, and independently reconstructed all three kernel tables with exact rational arithmetic. The pinned Multiplicity target actually compiled and all12 type/axiom queries succeeded with the standard three axioms: eight zeta declarations and four dyadic fixed-primitive-character declarations. Source state was clean; intermediate build products were reused. The two later continuum searches completed through the independently reviewed checkpoint adapter and matched all five author counters; earlier byte-unmodified attempts remain recorded as interrupted. The pinned newer Palomar Solution target also compiled, with actual type/axiom queries for the uniform39/17 density and middle-range large-values declarations. Its official pinned Mathlib cache was reused, and an alternate independent kernel/comparator was not replayed locally. See audits/formal_artifact_round2.md for exact process and trust boundaries.

Recent reviewed additions are detailed in final_synthesis/round8_report.md and preceding reports. The adaptive optimal rate is reconstructed for each fixed Selberg-class function under its statedGRH, with arbitrary fixed pole order; a tested Mellin identity and repaired phase proof supply the generalized lower. A universal weak-derivative obstruction and exact regularization cost clarify the source-proof repair. Four Conrey–Li negative examples have validated interval reproductions. Fixed-height optimized upper and finite-phase lower certificates now form a two-sided procedure relative to supplied global analytic and finite-zero inputs; its numerical global threshold has not been instantiated. Four beta cutoffs and one positive zeta one-zero lower bound were independently reproduced. The source fixed-prefix limit has been reconstructed; under RH its fixed-prefix arithmetic limit exists, and its analytic germ at b=0 determines the weighted multiplicity totals, while finite data have explicit obstructions. Finite Euler factors preserve the unrestricted character constant, while a nonprincipal zero-at-one anchor gives exact distance1. Consequential new global zero-free claims remain source-stated pending analytic audits. With the declared modern reciprocal inputs and RH, a classical shifted Möbius array has norm rate(logN loglogN)^(-1/4) and an exact multiplicity-dependent leading coefficient. A general Herglotz energy identity and a specific empty-spectrum semigroup control connect that norm to boundary atoms and operator domains. The corrected weighted criterion has a complete replacement threshold and an explicit reverse-implication counterexample. The finite Lagarias certificate now reaches720720. Historical priority searches remain open. A source's old question is not evidence that a reconstruction is new today.
''')
put('quality/coverage_report.md',f'''# Current quantitative coverage

Generated from metrics and curated source scopes. {summary}

{counts}

Complete readings: {read_ids}.

All other selected records are partial inspections or bibliographic/access-only records. Inaccessible or metadata-only sources are retained explicitly atLevel0; access is counted separately. Inspect access_and_audit_manifest.csv for exact source versions, pages and external dependencies. No whole-paper Level2/3 promotion follows from a locally verified theorem, read translation, compiled lemma or numerical certificate component.

The provider metadata pool retains132/58/368/988/1558/910/1189 records across the seven historical strata. These are search matches, not importance selections or balanced source coverage.124 possible duplicate/version rows remain; three primary seeds remain separately reconciled. The executed discovery provider was OpenAlex, with targeted primary-source searches and later bibliographic checking; multi-provider corpus expansion is incomplete. A separate47-row curated batch verifies45 priority-candidate identities/dependencies, defers one and excludes one withdrawn manifestation from separate selection.43 rows match provider IDs and4 await reconciliation. This triage does not create source readings or selected-work promotions.

The bibliography additionally retains{M.get('deferred_supporting_works',0)} deferred supporting work record(s), excluded from selected counts. See quality/counting_corrections_round5.md for the correction to the earlier catalogued-versus-selected label. Incomplete primary reproductions with missing formulas are excerpt access, not complete mathematical full texts.
''')
report='''# Round two: historical phase record

This section preserves the earlier phase, including its then-unfinished tasks. The later round reports and live manifests supersede its process status, finite coverage and mathematical research queue. In particular the main Multiplicity build is now complete and a later adaptive source theorem supplies an alternative arithmetic upper route.

What changed mathematically

## The arithmetic approximation interface became sharper

THM-E-R201 andR202 prove a uniform fixed-m cluster theorem through every collision stratum, with an explicit Gram lower bound, O(1/L) scaled remainder and a second-order endpoint correction. This uses established divided-difference machinery; Avdonin–Ivanov and de Boor were actually consulted. Constants deteriorate with cluster size and scaled diameter. No claim of historical novelty is made.

THM-E-R204 gives a genuinely discrete block bound with alias denominator sigma_L=min (L+1)|1−exp(i(center_a−center_b)/L)|. A large ordinary center distance can still alias on the finite grid. Cluster comparisons use the SAME residual degree; dropping that convention changes the problem. THM-E-R205 represents an entire cluster of BCF-kernel residues by a Hermite divided difference of the zero-removed factor. This identifies the missing arithmetic quantity, rather than concealing it in individual inverse derivatives. It supplies no summable infinite residue bound.

A global density obstruction was recorded: the unscaled full zero multiset cannot be treated as a bounded-size, uniformly separated cluster system with a uniform unweighted exponential Riesz bound. Local unfolding, growing clusters or weighted spaces require separate theorems.

## A source-provenance question acquired a precise answer

Wei–Wu Proposition1.9 already proves that convergence of the prescribed logarithmically smoothed Möbius family implies both RH and simplicity of all nontrivial zeros. It was independently reconstructed before its prior source was found. Their Problem1 and Balazard–Saias's earlier Question4 ask for the RH-alone reverse. Ehm's introductory fixed-array equivalence needs that additional justification; this is not a proof that the equivalence is false.

The exact Mellin/unitary identity makes the distinction concrete. If C_N=sum mu(n)(1−logn/logN), then the prescribed full weighted error controls |C_N|/sqrtN. Full-sequence convergence gives a little-o Riesz-sum bound; its Mellin transform has poles at zeta zeros, which excludes multiple critical zeros. The same mechanism survives every fixed integer spectral weightq, including Ehm'sq2. Subsequence convergence gives RH through a Hardy evaluation witness, but the full-sequence simplicity proof cannot simply be applied to a subsequence.

For unrestricted Dirichlet-polynomial coefficients, the weightedq criterion is valid: the inner factor(s−1)/s cancels the zeta pole and produces the lower witness sqrt(2Reρ−1)|ρ−1|/|ρ|^(q+1) at an off-line zero. This is a reconstruction of established Hardy-space reasoning, not a new RH criterion advertised as progress.

## Original analytic foundations were read rather than inferred

Robin's27-page original French paper was read completely. Exact CA tie conventions and the oscillation range for everyb in(1−Theta,1/2) were recovered. Global CA-based RH equivalence and finite endpoint certification remain distinct.

Beurling's1955 closure note and1953 semigroup-character dependency were also read completely. The converse uses a character in every weakerL^r closure, not necessarily in the original dualL^q closure. That qualification matters. The deeper Báez-Duarte audit repaired a displayed epsilon majorant and reconstructed the main theorem/corollary; the quantitative shrinking-epsilon dependency has now been closed by a uniform Perron reconstruction, independently reviewed and director-adjudicated. The low-height Borel–Carathéodory patch is essential; fixed-distance big-O constants alone were insufficient. No full-paper Level2 label is forced.

A separate computer-assisted calculus proof gives strict concavity for the smooth Lagarias comparison function on every real x>=1. The170 compact cells have an exact standard-library integer-interval replay; x>=2048 is analytic. Together with a certified shared supporting epsilon, endpoint inequalities certify every integer in the intervening interval. A pair of arbitrary abundant integers or an enumeration assuming prime consecutive ratios is insufficient. The finite integer certificate now covers1..55440. This is finite verification and model reduction, not an infinite-tail proof. The complete proof and portable replay are in lagarias_global_concavity_round2.md and its independent audits.

## Spectral model selection now covers genuine boundary effects

The bounded block-auxiliary theorem has a sharp3M count-curvature difference, including two-sided compact-resolvent spectra. The stronger extension-theory result uses a real resolvent anchor and finite-defect rank: two compact-resolvent self-adjoint extensions of a common dense symmetric operator with defectd have relative count-shift oscillation at mostd and curvature difference at most3d. Momentum boundary phases attain the constant. The modern source's main theorem assumes semiboundedness; the broader assertion is separately proved.

An explicit compact-resolvent self-adjoint boundary realization now covers arbitrary finite Hermitian auxiliary matrices, with dark states counted separately. Its visible transfer is rational inner, its phase increment is nonnegative and at most the visible dimension, and the total count curvature satisfies−3E−2M<Delta N<3E+M. Matching the positive zeta curvature with o(K) errors forces3E+M>=Klog2/pi−o(K). The naive common restriction can be nondense, so the separate finite-defect result cannot erase M. These tests constrain model construction but do not construct the zeta spectrum.

## Geometry supplied exact hypotheses, not a loose analogy

Weil1949 was completely read; DeligneI andII were inspected in specified technical portions. Smooth projective, smooth proper, compact support, ordinary cohomology and the pure image of the natural map are kept distinct. The source explicitly imports analytic positivity methods; later geometric operations contract a weight loss. These are documented historical connections, not inventions of this archive.

A formal genus-one rational zeta expression has reciprocal symmetry, nonnegative integral Euler exponents and off-circle eigenvalues. It is not a curve zeta function. A genuine constant-arithmetic lisse sheaf has rational local polynomials and alternating Tate duality but fails purity because its geometric monodromy is trivial. These controls isolate why positivity and duality alone do not replace Deligne's pole-control hypotheses.

A conditional weakening replaces open symplectic monodromy by sublinear excess weights on an unbounded sequence of even-tensor coinvariants. Independent proofs checked rationality descent, local/global coefficient domination, degree factors and duality. This is a specialization of the source method with no established novelty or classical-number-field transfer.

## Formal and numerical evidence became executable

Actual pinned repositories were inspected. Counting definitions use Mathlib's zeta and analytic multiplicities, with finiteness proved in source. Challenge/Solution types and disclosed computational hypotheses were compared. The formal asymptotic proof uses fixedlambda<1 before taking an epsilon limit; it need not assert every sharper quantitative prose remainder.

A separately written exact-rational program checked733298 whole-cell inequalities across three kernel tables. The first author's60-million-node reference search replay passed, and another reviewer inspected its continuum coverage, pruning, integer bounds and local-to-global summation. These are distinct components. The pinned RankTrace source module actually compiled locally, with its queried theorem axioms exactly propext, Classical.choice, Quot.sound. The full Multiplicity target and headline analytic/kernel trust boundary remain separately tracked in formal_artifact_round2.md. No component is relabeled a full theorem audit.

## What remains worth doing first

Finish and inspect the actual headline Lean target queries; verify the remaining full prime-side moment with all window hypotheses; formalize the pressure-aware finite transfer; quantify the zero-removed factor over a growing cluster system; and continue source-grounded historical/corpus selection. The original shrinking-epsilon dependency and global Lagarias concavity are completed scoped tasks, not work to repeat. The initial25 opportunity list is retained with completed subproblems marked in the live queue. Repeating already disproved generic approaches without a new arithmetic hypothesis is not useful.

No infinite arithmetic theorem about the actual zeta function, publication novelty, or resolution of RH is claimed. The source and model results lower the cost of testing precise next statements.
'''
put('final_synthesis/round2_report.md',report)
for name in ['round3_report.md','round4_report.md','round5_report.md','round6_report.md','round7_report.md','round8_report.md']:
 if (R/'final_synthesis'/name).exists():report+='\n\n'+(R/'final_synthesis'/name).read_text()
put('final_synthesis/comprehensive_report.md',f'''# Current synthesis

{summary}

{counts}

'''+report+'\n\nThe first-phase historical narrative and answers to the original ten synthesis questions are preserved in checkpoint1_report.md. This update supersedes its coverage and process-status statements, and adds source-verified geometry, original foundations and executable certificate audits.\n')
put('quality/limitations.md',f'''# Current limits

The1000-work program is unfinished. There are{M['selected_checkpoint_works']} selected records,{M['fulltexts_accessed_selected']} accessed full texts and{M['whole_work_or_translation_read']} complete substantive readings. Whole-paper Level2/3 counts are {levels.get('2',0)} / {levels.get('3',0)}; scoped reviewed results are listed separately. Metadata scale is not mathematical understanding.

No RH resolution, new unconditional zero bound or established publication novelty emerged. Conditional approximation and multiplicity formulas were independently reconstructed with their explicit RH assumption. Finite random models require additional arithmetic hypotheses before transfer. Exact numerical certificates, author-program replays, static formal inspection, compiled lemmas and complete headline-kernel replay have different statuses. Use the live formal audit rather than old first-checkpoint statements that no build was attempted.

The corpus remains biased, noisy and incompletely manifestation-deduplicated. Many major analytic, arithmetic-geometric, spectral and historical works are unread. Correction-history searches and publication-version comparisons are incomplete. Source statements with hypotheses are not unconditional mathematical conclusions.

The goal remains active; background processes and subagent work may continue. Runtime usage balance is not exposed, so no claim of exhausting a weekly quota is made. Every substantive checkpoint is persistent and resumable. Source fulltexts/private build caches are omitted; licensed finite inputs and reference code carry notices.
''')
put('CONTINUATION.md','''# Active continuation

The user's standing instruction is continuous research through available execution/usage budget. Keep the goal active; a completed checkpoint is not task completion. Review quality/execution_state.json, current metrics and active agent/process logs before starting work. Do not duplicate an interrupted compiler/search run without checking its process/result status.

Current areas: instantiate global inputs for two-sided certificates, arithmetic prefix endpoint control, Suzuki all-tail deficit bound and broader merged-work audit, recent fixed-half-plane analytic source audit, full prime-side arithmetic moment audit, signed mixed-moment bound, classical shifted-array priority/effectivity and recent reciprocal source proof, exact boundary-energy antecedents/rates, alternative spectral spaces and source-grounded corpus expansion. The weighted-target correction, classical q1 transfer, fixed-Selberg adaptive optimal theorem, phase/Hardy proof repairs, exact domain regularization, Conrey–Li negative certificates, general Herglotz energy, empty-spectrum xi control, scalar two-term maximum and shared-support certificate through720720 are completed scoped tasks; so are the source RH-only optimized upper reconstruction, finite Legendre/Bessel costs, the actual main Multiplicity and Palomar Solution build/queries, both reviewed later continuum searches, fixed-prefix theorem and inverse moment analysis, finite phase lower certificates, imprimitive transfer and nonprincipal anchor obstruction. Inspect their director adjudications and exact trust boundaries before repeating them. Historical priority and whole-paper audits remain separate. No new source or theorem is counted merely because planned.

Useful commands:

```bash
python scripts/build_archive.py
python scripts/merge_findings.py
python scripts/write_live_checkpoint.py
python scripts/validate_archive.py
python scripts/package_checkpoint.py
python scripts/next_tasks.py
```

Use render_and_package.py when regenerating the standalone synthesis; package_checkpoint.py retains already delivered PDF bytes. The original write_checkpoint.py/finalize_data.py are first-release generators and must not overwrite current findings/prose. Their snapshots are retained for history.

Before mathematics: read director_adjudication.md, director_round2_adjudication.md, current campaign scopes and independent reviews. Before corpus expansion: distinguish provider metadata, access, partial reading, full reading and scoped vs whole-paper audits.124 possible version duplicates remain. New selected works must have real source-grounded identities; no automatic top1000 admission.

Drive folder1VErNe2KOeqqw02o7YktqYOcfkixgHU-K and ZIPfile1jDCXGRg3h4WzzKItgi2PLlOrEa91gLWq already exist. Update bytes in place only after validation; verify metadata before returning the link. Existing permissions must remain unchanged. Current uploads are checkpoints, not claims the research program is complete.
''')
print(json.dumps({'selected':M['selected_checkpoint_works'],'accessed':M['fulltexts_accessed_selected'],'complete_readings':M['whole_work_or_translation_read'],'scoped_groups':M['scoped_level3_claim_groups']}))

# Current-round prose supersedes historical round2–8 composition.
if (R/'final_synthesis/round9_report.md').exists():
 from write_round9_checkpoint import write_current
 write_current(R,M)
