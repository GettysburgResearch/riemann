#!/usr/bin/env python3
"""Current evidence-driven prose; earlier reports are preserved as dated history."""
import json
from pathlib import Path
from datetime import datetime,timezone

def write_current(R,M):
 def put(p,s): (R/p).write_text(s.strip()+'\n')
 levels=M['whole_work_audit_levels']
 findings=[json.loads(s) for s in (R/'audits/findings.jsonl').read_text().splitlines() if s.strip()]
 errors=sum(bool(x.get('verified_author_error')) for x in findings)
 rows=[('Provider metadata records',M['metadata_candidates']),('Selected source records',M['selected_checkpoint_works']),('Selected full texts accessed',M['fulltexts_accessed_selected']),('Selected primary-source excerpts only',M.get('selected_primary_excerpt_accessed',0)),('Complete substantive readings',M['whole_work_or_translation_read']),('Complete paper-wide Level2/3 audits',f"{levels.get('2',0)} / {levels.get('3',0)}"),('Scoped independently adjudicated claim groups',M['scoped_level3_claim_groups']),('Theorem/conjecture/exercise records',M['theorem_or_exercise_records']),('Connection records',M['connection_records']),('Graph nodes / edges',f"{M['graph_nodes']} / {M['graph_edges']}")]
 table='| Evidence state | Actual |\n|---|---:|\n'+'\n'.join(f'| {k} | {v:,} |' if isinstance(v,int) else f'| {k} | {v} |' for k,v in rows)
 count=f"{M['selected_checkpoint_works']} selected works; {M['fulltexts_accessed_selected']} full texts accessed; {M['whole_work_or_translation_read']} complete substantive readings; {levels.get('3',0)} whole-work Level3 audits; {M['scoped_level3_claim_groups']} scoped adjudicated groups."
 scope='The 1,000-work research program remains unfinished. No proof or disproof of RH, new zero-free or zero-density exponent, or publication novelty is claimed. Source access, complete reading, scoped proof verification and whole-work audits are distinct evidence states.'
 put('README.md',f'''# Riemann Observatory — active research archive

Literature cutoff: {M['cutoff']} UTC, the latest documented query date rather than a claim of exhaustive coverage. {scope}

{table}

Begin with [START HERE](START_HERE.md), the [current synthesis](final_synthesis/round10_report.md) and [25 precise next problems](final_synthesis/top_25_research_opportunities.md). Current adjudicated results include an effective conditional scalar prime-phase CLT, the RH-conditional real-line heavy-tail law, a central-zero Gaussian limit, a directly weighted unconditional derivative-series enclosure and explicit finite-test countermodels. Every result retains its exact measure, hypotheses and provenance.

The whole-work promotions are registered by exact version and source hash in quality/whole_work_audit_promotions.jsonl. These include Manzur–Noor, Nakamura–Suzuki's classical-zeta criterion, and Lagarias's May preprint, with the local corrections and accepted upstream inputs in their director notes. A valid main theorem and a false auxiliary display are separate findings.

Query the [read-only SQLite index](graphs/archive_index.md), its portable SQL dump, or paper_views/PAPER-ID.md. These derived views preserve original contributor fields and explicit missing analysis. Canonical data are corpus/bibliography.jsonl, theorems/theorems.jsonl, theorems/proof_dependencies.jsonl, connections/connections.jsonl, audits/findings.jsonl and graphs/knowledge_graph.jsonl. Schemas and scope conventions are documented in quality/structured_data_schema.md and graphs/graph_schema.md.

The 5,203 provider rows are noisy overlapping metadata, not importance-reviewed works. The separate reconciliation groups 42 of the old 124 flagged rows, identifies 15 as distinct, and leaves 67 unresolved. Its provisional keys are not a verified unique-candidate count. New corpus batches awaiting director review are under quality/pending_round11 and are excluded from canonical counts.

Source PDFs, full extracted source texts and private compiler caches are excluded from distribution. Original analysis, code, permissible finite data and original figures are included, with source links and hashes. Earlier reports and contributor drafts are dated evidence history; current masters and director overlays determine current status. Continue with CONTINUATION.md. Weekly usage balance is not exposed.
''')
 put('executive_report.md',f'''# Research checkpoint — execution continues

{scope}

{table}

Under RH, a derivative-weighted prime-phase statistic has a Gaussian limit with an effective threshold in principle. No numerical threshold is calculated. A different, multiplicity-weighted law has dense atoms, a precise heavy tail and Cauchy scaling.

The critical-line derivative series is unconditionally enclosed by 0.61649875288731141829<C2<2.35771. Its quartic splice near 0.65339 remains an observation because the asymptotic error constants are unallocated. Complete source audits preserve valid main results alongside exact auxiliary corrections. Next priorities are practical constants, arithmetic weighted-tail tightness and wider primary-source coverage.
''')
 put('START_HERE.md',f'''# START HERE — one research day

{count} {scope}

1. Read the [current synthesis](final_synthesis/round10_report.md) for 30 minutes. Inspect the original probability diagram before comparing its two different laws.
2. Spend 90 minutes on the [effective scalar CLT](audits/adversarial_reviews/director_effective_scalar_clt_round10.md). Reconstruct a(kq) conductor deletion and the restoration of the full fixed statistic before Stieltjes integration. Check why this leaves the prescribed-coordinate problem open.
3. Spend 90 minutes on the [weighted derivative certificate](audits/adversarial_reviews/director_weighted_rolle_round10.md) and [exact quartic](audits/adversarial_reviews/director_q2_quartic_round10.md). Rerun the small finite control; distinguish its unconditional whole-tail bound from the quartic observation.
4. Spend 90 minutes on the [whole Nakamura–Suzuki audit](audits/adversarial_reviews/director_nakamura_whole_round10.md), [heavy-tail deductions](audits/adversarial_reviews/director_probability_tail_round10.md) and [moving central Gaussian component](audits/adversarial_reviews/director_vertical_diffusion_round10.md). Preserve multiplicity versus derivative weights.
5. Spend one hour on the [all-grid obstruction](audits/adversarial_reviews/director_bounded_positivity_round10.md) or [finite integral trace cutoff](audits/adversarial_reviews/director_finite_trace_round10.md). Identify the exact arithmetic ingredient missing from the countermodel.
6. Use the final 90 minutes to inspect the [Lagarias whole-work audit](audits/adversarial_reviews/director_lagarias_whole_round10.md), query a stable theorem ID in the SQLite index, and select one [explicit next problem](final_synthesis/top_25_research_opportunities.md). Read CONTINUATION.md before starting another campaign.

Complete reading is not a complete audit. Named external theorems remain external. A partial source record may have important inspected mathematics while retaining Level0. The original source scope and exact version always accompany the record.
''')
 put('final_synthesis/comprehensive_report.md','# Current mathematical synthesis\n\n'+scope+'\n\n'+table+'\n\n'+(R/'final_synthesis/round10_report.md').read_text()+'\n\nEarlier numbered reports remain as historical checkpoints; their counts, active jobs and open-task labels are not current status.\n')
 put('quality/coverage_report.md',f'''# Coverage at this checkpoint

{table}

{scope}

The catalog includes {M['catalogued_works']} canonical identities, including {M['deferred_supporting_works']} deferred supporting work. All selected records have source-derived mathematical context at their stated reading scope; only the complete-reading count denotes a complete work. Access limitations, missing exact results and uninspected proof portions remain explicit. The planned200–300 deep and50–100 intensive whole-paper targets are unmet.

Family and historical strata are in quality/coverage_taxonomy_report_round10.md and its machine-readable tables. Overlapping family labels do not sum to a unique-work total. Unclassified rows are retained where the inspected metadata do not justify a family. Controversial proof attempts are a small explicitly selected subset; incidental typos do not qualify an entire work for that family.

Provider metadata is not an importance-ranked candidate corpus. See quality/provider_candidate_reconciliation_round10.md for version/group uncertainties and its pinned input snapshot. Its 5162 provisional keys still include unresolved singletons. Do not add provider and selected counts.
''')
 put('quality/limitations.md',f'''# Evidence and resource limits

{count} {scope}

Whole-paper Level3 promotions require exact version/hash, two independent complete readings, a director reconstruction and coverage checklist. Their imported classical inputs are named; entire upstream proof ancestry is not claimed audited. Other technical results remain scoped, even where the underlying source was read completely.

The effective scalar CLT has a computable conditional onset but no numerical threshold. The general prescribed-coordinate uniform estimate remains ineffective. The exact Q2 quartic has a conditional power-saving error with unallocated constants. Its observed splice values near 0.65339 are not tail certificates. The separate unconditional critical-line enclosure is rigorous at its recorded width. RH is needed to identify it with the prime-array limiting constant.

The real-line infinitely divisible law is conditional on RH. Its compound-Poisson jumps, atom and Cauchy limit differ from the derivative-weighted prime-torus law. Neither finite counting models nor entire-function countermodels preserve every zeta arithmetic property. Whole-vector and global weighted-cutoff extensions remain candidates until their separate reviews finish.

Literature and priority searches are bounded, and major works remain unread. Provider duplicates and source manifestation ambiguities remain. Level0 includes targeted mathematical readings, not just metadata. Historical contributor drafts remain for traceability and may contain explicitly superseded claims; canonical status overlays and director adjudications govern.

Formal compilation, declaration/axiom queries, continuum program replay and interval arithmetic have distinct trust boundaries. No alternate Lean kernel was replayed. The K839 adapter checks its generated resume states, not arbitrary outside certificates. Structural validators check data consistency and exact sealed bytes, not mathematical truth. Source PDFs, full extracted texts and private caches are omitted from the ZIP.

Execution is active with GPT-6.2 Sol agents. Weekly usage balance is not observable. Restarts can interrupt jobs; durable checkpoints and executable tasks preserve the actual completed work.
''')
 put('quality/evidence_audit.md',f'''# Evidence audit

{count}

The exact whole-work registry records the source version, SHA256, independent advocate/skeptic paths and coverage checklist. Local corrections and inaccessible publisher editions stay explicit. There are {errors} legacy true finding groups with independently witnessed false version-specific assertions. This counts finding groups, not authors, false papers or all typographical corrections. Already repaired author-manuscript displays and missing hypotheses have separate classifications.

New scoped adjudications include exceptional-prime deletion for the scalar CLT, exact Q2 residues with a separate sharp endpoint proof, weighted vector variation and a complete finite-zero census. The director independently replayed symbolic and small finite checks; a second agent replayed the full 160-bit10000 census. The finite count exhausts an independent all-zero multiplicity count, rather than assuming the critical-line isolation list is complete.

The source-based prime array, inverse theorem, fixed and uniform shifted moments, weighted density countermodels, finite trace criteria and augmented moment geometry have their own scopes. The two probability laws use different zero weights and measures. No independent reconstruction establishes publication priority automatically.

The Multiplicity and Palomar targets compiled locally with recorded declaration types and only propext, Classical.choice and Quot.sound in the inspected axiom outputs. All three K839 tables have independent whole-cell checks; all three continuum searches completed, with the later two using a separately reviewed checkpoint adapter. Interrupted byte-unmodified runs remain preserved. These facts alone do not promote an entire paper.

The sealed validator checks every ZIP payload size/hash against one immutable snapshot, derives counts from the sealed masters, checks promotion/version alignment and code pins, and compares separately delivered PDF/HTML bytes. Mathematical validity still rests on the attached source evidence and proofs.
''')
 put('CONTINUATION.md',f'''# Continuous execution and next checkpoint

The user requests continued research through available execution/usage budget with GPT-6.2 Sol subagents. A checkpoint is a durable handoff, not completion. Usage balance is unobservable. Check actual agent/process status before relaunching work.

{count}

Immediate tasks: independently adjudicate the candidate joint low-influence prime-phase theorem and global weighted Hardy cutoff; allocate practical Q2 quartic error constants; instantiate the finite-length prime-array remainder; derive an arithmetic weighted-tail tightness or signed-pair lemma; resolve the separately reviewed compensated-drift convention in Suzuki's preprint; merge pending corpus batches only after identity and scope review. The scalar effective onset is now proved in principle and must not be rediscovered as an unresolved qualitative issue.

Whole Nakamura–Suzuki, Manzur–Noor and Lagarias promotions are exact-version audits. RST048 Theorem6 and uniform polylogarithmic phase matching retain their established recorded hypotheses. Preserve old pins and rejected experiments. New source records must say whether a complete work or only targeted portions were read.

From the archive root, run sequentially:

```bash
python scripts/integrate_round9.py
python scripts/integrate_round10.py
python scripts/integrate_round10b.py
python scripts/build_archive.py
python scripts/merge_findings.py
python scripts/write_live_checkpoint.py
python scripts/build_coverage_taxonomy.py
python scripts/export_archive_index.py build
python scripts/validate_archive.py
```

Freeze an immutable copy excluding source PDFs, full extracted texts, raw provider responses and private caches. Render with that copy's scripts/render_and_package.py, then validate its exact ZIP using scripts/validate_sealed_checkpoint.py with its metric snapshot and separately delivered PDF/HTML. Inspect the PDF and obtain independent sealed QA before upload. First-release write_checkpoint.py/finalize_data.py must not overwrite current ledgers or prose.

Drive folder1VErNe2KOeqqw02o7YktqYOcfkixgHU-K contains ZIP1jDCXGRg3h4WzzKItgi2PLlOrEa91gLWq, PDF15Ec2GU64FjpHwZMWLl1TqhQRAgdFmZrr and HTML1TaUMRh5QFnD8j9eJA5i_D1DzDU8czdy0. Update bytes in place after validation and read metadata back. Preserve parents and sharing. The post-upload receipt goes into the following snapshot to avoid a self-referential package hash.
''')
 tasks=[
 ('Explicit Q2 error certificate','Bound each sharp product-AFE, stationary-phase, Perron and Cauchy term numerically for fixedQ2; return a verified tail enclosure rather than a chosen asymptotic main term.'),
 ('Global weighted Hardy variation','Prove or refute the candidate variation estimate for a cutoff times Q2Z/t over a complete tail. Control infinite endpoints and weighted Hilbert corrections before adopting improved numerical constants.'),
 ('Joint low-influence prime phases','Under RH extend the scalar transfer to a fixed-dimensional normalized coefficient array with vanishing maximal prime contribution. Check complex sine words, singular covariance and effective convergence rates independently.'),
 ('Practical effective scalar onset','For a fixed rationalD andepsilon=.1, allocate the exceptional-prime contour and finite smoothing constants. Give an explicit conditionalY0, even if enormous, and identify the dominant loss.'),
 ('Prescribed-coordinate effectivity','Determine whether a fixed prime dividing the exceptional conductor can retain an effective individual-character bound. Deletion cannot be justified when that coordinate carries macroscopic influence.'),
 ('Finite-length prime-array remainder','Reduce the explicitN-dependent constants while retaining both the near-zero and infinite-height contributions. A bound for the coefficient-series tail is not this remainder.'),
 ('One-percent C2 enclosure','Produce a complete finite derivative package with declared width and a certified analytic tail; use improved global bounds before choosing a larger zero census. No quartic remainder may be omitted.'),
 ('Arithmetic weighted tightness','Find a zeta-specific hypothesis implying Y^(-1)integral_Y^(2Y)r(t)dt<<Y^(1-kappa), or a comparable positive weighted-tail bound. Count-only off-line estimates admit the recorded escape model.'),
 ('Signed derivative correlations','Identify a signed two-point or shifted-moment estimate that controls weighted mass escape without replacing it by an absolute zero count. State uniformity in both shifts explicitly.'),
 ('Longer prime cutoffs','Determine the largestP(Y) supported by positive word expansion with error uniform at each fixed moment order. Do not infer polynomial cutoffs from the established logarithmic range.'),
 ('Arithmetic prefix endpoint control','For the factorial target, bound the signed residual at cell endpoints using arithmetic cancellation beyond the generic lattice inequalities. Compare against the hard-cutoff counterexample.'),
 ('Moving central law rate','UnderGRH estimate a probability metric for the zero-crossing compensated Poisson law versus its Gaussian limit. Account for the rest of the spectrum and the moving deterministic translation.'),
 ('Compensated-drift source convention','Adjudicate the exact Suzuki2209.12832v2 drift identity using an explicit entireS-sharp example and original sign conventions. Keep the unchanged screw kernel separate from the disputed imaginary linear term.'),
 ('Height-normalized central zeros','Specify the canonical vertical normalization in the degree-one classification. Determine which central-zero statements remain invariant and which require that normalization.'),
 ('Sharper heavy-tail error','For Nakamura–Suzuki underRH, test whether the directO(log³Y/Y²) probability error can be sharpened with cancellation, without assuming an ordinary first moment that does not exist.'),
 ('Atom mass beyond the small census','Improve the zero-atom interval using rigorous collision probabilities of longer finite signed sums. Do not replace the exact atom by the no-jump mass exp(-S).'),
 ('Actual arithmetic positivity obstruction','Find a condition supplied by the prime-side formula that excludes the RVM all-grid countermodel. Local cusp and bounded grids alone provably do not suffice.'),
 ('Finite trace cutoff efficiency','Improve the algebraic norm gap or simultaneous phase recurrence in the explicit integral q-reciprocal criterion. Compare complexity as degree grows and distinguish repeated roots from Jordan information.'),
 ('Sparse extension-degree certificates','Characterize sampling sets of powers that force purity for each fixed integral reciprocal degree. Prime powers alone fail in the recorded degree8 model.'),
 ('A genuine number-field trace bridge','State an operator or cohomological trace with compatible powers, convergence and positive polynomial tests. Identify the exact missing theorem beyond importing finite-field purity.'),
 ('Finite inverse-data stability','Quantify how much of the derivative-weighted zero measure is determined by finitely many noisyC_k. Include diffuse competitors and the declared order of limits.'),
 ('Noncoercive multiplier metrics','Characterize useful weak invariant metrics for the integer-spectrum jump group and whether a target-specific quotient can restore a stable approximation estimate. Coercive global metrics are ruled out.'),
 ('Whole-paper audit expansion','Choose the next 5 whole works by dependency centrality and manageable proof length, obtain two independent complete reviews, and pin exact versions before promotions.'),
 ('Primary corpus selection to1000','Review pending batches and unresolved provider identities, rebalance historical/non-English coverage, retain exclusions and leave access or reading limits explicit.'),
 ('Publication priority and theorem packaging','For each strongest deduction, search exact weights, quantifiers and parameter ranges in prior literature. Package only independently survived claims with explicit novelty boundaries and next lemmas.')]
 put('final_synthesis/top_25_research_opportunities.md','# Twenty-five actionable research problems\n\nThese are ranked next steps at the current checkpoint. Conditional premises and incomplete computations remain explicit.\n\n'+'\n\n'.join(f'{i}. **{title}.** {body}' for i,(title,body) in enumerate(tasks,1)))
 put('final_synthesis/open_problems_for_future_agents.md','# Open problems for future agents\n\nRead CONTINUATION.md for executable operations and exact source scopes.\n\n'+(R/'final_synthesis/top_25_research_opportunities.md').read_text())
 put('proposals/ranked_research_directions.md','# Ranked campaigns\n\n'+(R/'final_synthesis/top_25_research_opportunities.md').read_text())
 put('connections/strongest_connections.md', '''# Strongest currently adjudicated interactions

Each connection has a precise hypothesis match and independent proof record. Publication priority is unestablished unless credited explicitly.

1. The fixed-generator RH criterion, Selberg logarithmic taper and factorial target give a prescribed prime-array approximation with an explicit derivative-weighted limit. [Round9 synthesis](../final_synthesis/round9_report.md)
2. The same constants determine an atomic Fourier measure; shifted discrete moments give its gcd/prime-Poisson covariance on fixed and growing logarithmic supports. [Uniform source match](../audits/adversarial_reviews/director_hlz_uniform_round9.md)
3. Classical exceptional-prime deletion acts directly on HLZ's a(kq) support and makes the scalar arithmetic CLT effective after the full statistic is restored at each prefix. [Adjudication](../audits/adversarial_reviews/director_effective_scalar_clt_round10.md)
4. The sparse Q2 local factor gives the exact shifted quartic and preserves cancellation in a separate unconditional weighted-Hardy certificate. The latter bounds the full series; the former still lacks numerical error constants. [Quartic](../audits/adversarial_reviews/director_q2_quartic_round10.md) · [Certificate](../audits/adversarial_reviews/director_weighted_rolle_round10.md)
5. Riemann–von Mangoldt counting and the classical-zeta infinitely divisible criterion give a precise compound-Poisson heavy tail, dense atoms and conditional Cauchy scaling. This uses multiplicity weights, not the derivative-weighted prime law. [Proof](../audits/adversarial_reviews/director_probability_tail_round10.md)
6. A vertically moving zero turns compensated Poisson jumps continuously into the central Gaussian variance; the drift must be regularized and the arithmetic height convention specified. [Bridge](../audits/adversarial_reviews/director_vertical_diffusion_round10.md)
7. An entire countermodel combines smooth RVM count, the arithmetic cusp and every bounded-grid positive power while retaining a remote quartet. It isolates the missing global arithmetic condition. [Countermodel](../audits/adversarial_reviews/director_bounded_positivity_round10.md)
8. Integrality plus reciprocal spectral symmetry yields a finite trace purity cutoff through a norm gap and simultaneous recurrence. The same logic shows why sparse prime-degree tests fail. [Finite proof](../audits/adversarial_reviews/director_finite_trace_round10.md)

Candidate joint-vector and globally weighted-tail extensions are separately labeled pending. Shared terminology alone is not a connection.
''')
 state=json.loads((R/'quality/execution_state.json').read_text())
 state.update(date=M['cutoff'],updated_at_utc=datetime.now(timezone.utc).isoformat(),last_prepared_checkpoint='checkpoint8_preparing',current_mathematical_work=[x[0] for x in tasks[:9]],background_work='GPT-6.2 Sol source/research/review agents continue; inspect actual agent status. No usage quota is exposed.')
 (R/'quality/execution_state.json').write_text(json.dumps(state,indent=2)+'\n')
 print(json.dumps(dict(current_prose_round=10,selected=M['selected_checkpoint_works'],complete_readings=M['whole_work_or_translation_read'],whole_Level3=levels.get('3',0),versioned_finding_groups=errors)))

if __name__=='__main__':
 R=Path(__file__).resolve().parents[1];write_current(R,json.loads((R/'quality/metrics.json').read_text()))
