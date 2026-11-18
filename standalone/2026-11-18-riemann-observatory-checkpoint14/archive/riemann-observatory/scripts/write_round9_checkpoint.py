#!/usr/bin/env python3
"""Current synthesis prose, kept separate from preserved earlier-round generators."""
import json
from pathlib import Path

def write_current(R,M):
 def put(p,s):(R/p).write_text(s.strip()+'\n')
 levels=M['whole_work_audit_levels']
 findings=[json.loads(s) for s in (R/'audits/findings.jsonl').read_text().splitlines() if s.strip()]
 nerr=sum(bool(x.get('verified_author_error')) for x in findings)
 count=f"{M['selected_checkpoint_works']} selected works; {M['fulltexts_accessed_selected']} full texts accessed; {M['whole_work_or_translation_read']} complete substantive readings; {levels.get('2',0)} whole-work Level2 and {levels.get('3',0)} whole-work Level3 audits; {M['scoped_level3_claim_groups']} independently adjudicated scoped claim groups."
 table='| Evidence state | Actual |\n|---|---:|\n'+'\n'.join(f'| {k} | {v:,} |' if isinstance(v,int) else f'| {k} | {v} |' for k,v in [
 ('Provider metadata candidates',M['metadata_candidates']),('Selected source records',M['selected_checkpoint_works']),('Selected full texts accessed',M['fulltexts_accessed_selected']),('Selected primary-source excerpts only',M.get('selected_primary_excerpt_accessed',0)),('Complete substantive readings',M['whole_work_or_translation_read']),('Complete paper-wide Level2/3 audits',str(levels.get('2',0))+' / '+str(levels.get('3',0))),('Scoped independently adjudicated claim groups',M['scoped_level3_claim_groups']),('Theorem/conjecture/exercise records',M['theorem_or_exercise_records']),('Connection records',M['connection_records']),('Graph nodes / edges',str(M['graph_nodes'])+' / '+str(M['graph_edges']))])
 scope='The 1,000-work program remains unfinished. No RH resolution, new unconditional zero bound or established publication novelty is claimed. Bibliographic discovery, source access, complete reading, scoped proof verification and whole-paper audits are different evidence states.'
 put('README.md',f'''# Riemann Observatory — active checkpoint

Literature cutoff: 17 November 2026 UTC. {scope}

{table}

Read [START HERE](START_HERE.md), the [current research synthesis](final_synthesis/round9_report.md) and [25 concrete next problems](final_synthesis/top_25_research_opportunities.md). The latest mathematical chain runs from a fixed-generator RH criterion to a prescribed tapered prime array, a derivative-weighted Fourier inverse and a gcd/Poisson high-zero covariance. Exact hypotheses and external dependencies stay attached to every step.

The archive includes one complete adversarial audit of the pinned seven-page Manzur–Noor v1, with an auxiliary covariance-sign correction and an intact main criterion. Other technically reconstructed theorems remain scoped audits, even when their source was read completely.

Structured masters: corpus/bibliography.jsonl, corpus/access_and_audit_manifest.csv, theorems/theorems.jsonl, theorems/proof_dependencies.jsonl, connections/connections.jsonl, audits/findings.jsonl and graphs/knowledge_graph.jsonl. Schemas are in quality/structured_data_schema.md and graphs/graph_schema.md. Original contributor records preserve source versions, corrected drafts and review history.

The 5,203 provider candidates are noisy and overlap selected works. They are not 5,203 importance-reviewed papers and must not be added to selected counts. The 124 possible provider version/duplicate rows remain unresolved. Source PDFs, full extracted texts and private compiler caches are excluded from distribution; authoritative links and hashes are retained. Original analysis, licensed finite data, code and original figures are included.

Run scripts/build_archive.py, scripts/merge_findings.py, scripts/write_live_checkpoint.py, scripts/validate_archive.py and scripts/render_and_package.py sequentially. Validate the immutable ZIP with scripts/validate_sealed_checkpoint.py. Earlier numbered reports are dated history; current metrics and scope overlays supersede their counts and process states. Continue through CONTINUATION.md and corpus/research_queue.jsonl.
''')
 put('executive_report.md',f'''# Current research checkpoint

{scope}

{table}

A prescribed logarithmic prime array now attains the optimized leading error for an explicit factorial target under RH, without simplicity assumptions. Its fixed-target convergence is an RH criterion. Explicit bounds and unconditional finite interval certificates are recorded.

Its limiting constants encode a derivative-weighted measure of simple zeros. Source-matched shifted moments give gcd covariance and Poisson prime phases; a separately reviewed theorem controls covariance on growing polylogarithmic prime blocks, with ineffective onset. Finite inverse-data ambiguity and all-prime nonuniformity remain explicit.

Negative results rule out initial-cell matching as a norm argument, coercive invariant metrics for the integer-spectrum jump group, and count-only weighted-tail inference. Exact model assumptions stay attached to every counterexample.

The first whole-work Level3 audit validates Manzur–Noor's main criterion and corrects two auxiliary signs. The ledger contains {nerr} version-specific assertion counterexamples, not {nerr} false papers. Named classical inputs remain external.

Next: tighten and instantiate the explicit length remainder; sharpen the unconditional derivative tail; make the uniform prime-block onset effective; and find arithmetic control excluding weighted escape. The comprehensive report answers the mission's ten questions and links all proof ledgers.
''')
 put('START_HERE.md',f'''# START HERE — one research day

{count} {scope}

1. Spend 30 minutes on [the current synthesis](final_synthesis/round9_report.md). Read its order-of-limits and source-scope paragraphs before the formulas.
2. Spend two hours reconstructing [the prescribed prime array](audits/adversarial_reviews/director_tapered_prime_array_round9.md) and [the effective/negative controls](audits/adversarial_reviews/director_prime_array_effective_round9.md). Check the actual anchor and the hard-cutoff counterexample.
3. Spend two hours on [HLZ hypothesis matching](audits/adversarial_reviews/director_hlz_prime_torus_round9.md) and [uniform logarithmic blocks](audits/adversarial_reviews/director_hlz_uniform_round9.md). Recheck bounded padding, local Euler quotients, complex shifts, both ordinate signs and the ineffective Siegel boundary.
4. Spend one hour on [the inverse problem](audits/adversarial_reviews/director_prime_array_inverse_round9.md) or [weighted density escapes](audits/adversarial_reviews/director_density_synthesis_round9.md), according to your expertise. The former needs a certified finite-length remainder; the latter needs arithmetic tightness beyond count bounds.
5. Spend one hour on [the complete source audit](audits/adversarial_reviews/director_manzur_noor_whole_round9.md), then inspect the exact versioned findings and independent checklists. A local sign correction leaves the main criterion intact.
6. Use the final hour to choose one [precise next problem](final_synthesis/top_25_research_opportunities.md), query its stable IDs with scripts/query_graph.py, and rerun its smallest reproducible control. Read CONTINUATION.md before commissioning new work.

For corpus work, inspect the CSV/JSONL bibliography and access manifest. Complete access is not complete reading. A claim-level proof is not a paper-level audit. Raw metadata candidates have not been ranked into a final thousand. The ZIP includes original figures and synthesis PDF/HTML, not source PDFs or private compiler caches.
''')
 put('final_synthesis/comprehensive_report.md',f'# Current mathematical synthesis\n\n{scope}\n\n{table}\n\n'+(R/'final_synthesis/round9_report.md').read_text()+'\n\nEarlier rounds remain available as round2_report.md through round8_report.md and checkpoint1_report.md. They document provenance and historical process states; they are not silently relabeled as current.\n')
 put('quality/limitations.md',f'''# Current limits

{count} {scope}

The sole whole-paper Level3 promotion is tied to an exact seven-page source version, two complete independent reviews, a director checklist and an auxiliary correction. Accepted classical upstream results are named; their entire proof ancestry was not reaudited. All other papers retain their explicit reading and scoped-claim levels. The 200–300 deep and 50–100 intensive paper targets remain unmet.

The corpus remains biased and incomplete, with many major sources unread. Provider discovery contains unresolved manifestation duplicates; correction and priority searches are bounded. Partial readings have Level0 even when mathematically substantive. A pre-release correction lowered 23 computational-source rows from mistakenly assigned Level1 to Level0 without changing their access or actual reading scopes.

Conditional theorems keep RH or other global inputs. Uniform logarithmic prime-block asymptotics use an ineffective source bound and do not supply a numerical onset. Exact inverse identities need infinite limiting data; finite observations do not determine zeros. The three finite prime-array certificates do not establish its limiting constant. Finite spectral and counting countermodels are not actual zeta functions.

Formal source builds, declaration/axiom queries, continuum code replays and interval computations have distinct trust boundaries. Standard Lean axioms are explicitly listed. No alternate proof kernel was replayed. The existing K839 checkpoint adapter trusts its own locally generated resume states, not arbitrary external certificates. Source PDFs/full extracted texts and private compiler caches are omitted for distribution.

Research remains active. Weekly usage balance is not exposed, so the archive cannot claim to have exhausted it. Restarts can interrupt agents; persistent records, exact sealed receipts and executable continuation tasks preserve completed work.
''')
 put('quality/evidence_audit.md',f'''# Evidence audit at the active checkpoint

{count}

The sole whole-work Level3 source is PAPER-MN2026-VERTICAL, pinned arXiv2610.03568v1, with the exact SHA, complete coverage checklist, advocate, skeptic and director adjudication in quality/whole_work_audit_promotions.jsonl. Its valid main theorem and false auxiliary covariance display are separated. Named classical upstream theorems remain external inputs; original inaccessible proof ancestry and private assistance history are not claimed audited.

There are {nerr} independently witnessed version-specific assertion counterexamples in the legacy verified_author_error field. This counts exact mathematical displays or assertions, not false papers or author assessments. Missing hypotheses, repaired local proof steps, superseded preprint clauses and existing author-issued errata retain their own classifications. No new external author contact or public flag was sent.

The source-based prime-array theorem, inverse measure theorem, fixed and uniform HLZ transfer, density countermodels and augmented moment geometry each have separate independent reconstructions and director scopes. Three separate source derivations scrutinized the growing-block claim. Numerical certificates include the entire declared tails and preserve actual original code versions; later hardening is not retroactively attributed to old runs.

The main Multiplicity and Palomar targets actually compiled locally; named declaration types and axiom queries passed with propext, Classical.choice and Quot.sound. The later Palomar full-curve query reused the same pinned compiled module and printed its distinct quantifiers. All three K839 numeric tables have independent exact whole-cell checks; all three continuum searches completed, the later two using the separately reviewed checkpoint adapter. Interrupted byte-unmodified attempts remain preserved. None of these facts alone promotes a whole paper or proves RH.

Structural validators check schemas, IDs, scope consistency and graph endpoints. The sealed validator reads one immutable ZIP snapshot, verifies its exact manifest and derived counts, and compares the separately delivered PDF/HTML bytes. It does not prove mathematics or externally verify every bibliographic field. Source PDFs and private caches are excluded; links and hashes remain.
''')
 put('CONTINUATION.md',f'''# Continuous research and executable continuation

The user requests continued work through available execution/usage budget, with GPT‑6.2 Sol subagents. A delivered checkpoint is not completion. Usage balance is unobservable. Read quality/execution_state.json, corpus/research_queue.jsonl and actual process/agent status before restarting work.

{count}

Immediate mathematical tasks are: sharpen and instantiate the independently adjudicated fixed-target prime-array remainder; instantiate a real complete finite zero/derivative package; make uniform prime-block onset effective; prove a new arithmetic weighted-tail tightness lemma or a signed pair estimate; obtain arithmetic prefix endpoint control; and audit unresolved signed reference-block transport. The uniform polylogarithmic covariance theorem is adjudicated and must not be rediscovered as an open fixed-index problem. RST048 Theorem6 and the Manzur–Noor whole-work audit are also complete with their recorded hypotheses/correction.

Corpus work: recover interrupted source caches before searching again, deduplicate all contributor records as well as masters, publish only atomic final JSONL shards, require explicit whole_work_read booleans, and retain rejected candidates/reasons. Metadata counts are not source readings. Correct source version and source hash must remain paired.

Run these sequentially from the archive root:

```bash
python scripts/integrate_round9.py
python scripts/build_archive.py
python scripts/merge_findings.py
python scripts/write_live_checkpoint.py
python scripts/validate_archive.py
python scripts/render_and_package.py
python scripts/validate_sealed_checkpoint.py --help
python scripts/next_tasks.py
```

The director integration script is idempotent for its fixed round9 records; extend its inputs deliberately for a later round rather than overwriting new claims. Do not run first-release write_checkpoint.py/finalize_data.py over current masters. Keep every old sealed receipt immutable. Package from a stable snapshot and validate exact sealed bytes, not mutable workspace files. Report completed, in-progress and interrupted executions separately.

Google Drive folder ID1VErNe2KOeqqw02o7YktqYOcfkixgHU-K contains ZIP1jDCXGRg3h4WzzKItgi2PLlOrEa91gLWq, PDF15Ec2GU64FjpHwZMWLl1TqhQRAgdFmZrr and HTML1TaUMRh5QFnD8j9eJA5i_D1DzDU8czdy0. Replace bytes in place after validation, then read metadata to verify size and identity. Preserve permissions and parents. A new receipt is written after upload and belongs in the next snapshot to avoid self-reference.
''')
 # Current evidence counts supersede a stale historical hardcoded count.
 p=R/'quality/structured_data_schema.md';s=p.read_text().replace('do not increment the four versioned new-error flags.','are not automatically new-error flags. The current count is derived from audits/findings.jsonl; each true flag remains versioned and scoped.')
 p.write_text(s)
 print(json.dumps({'current_prose_round':9,'selected':M['selected_checkpoint_works'],'complete_readings':M['whole_work_or_translation_read'],'whole_Level3':levels.get('3',0),'versioned_assertion_counterexamples':nerr}))

if __name__=='__main__':
 R=Path(__file__).resolve().parents[1];write_current(R,json.loads((R/'quality/metrics.json').read_text()))
