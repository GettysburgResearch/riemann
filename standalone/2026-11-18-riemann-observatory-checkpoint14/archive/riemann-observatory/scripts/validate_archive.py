#!/usr/bin/env python3
"""Structural and epistemic validation, not mathematical proof verification."""
import ast,csv,json,sys,os
from pathlib import Path
R=Path(__file__).resolve().parents[1]
errors=[];checks=0
distributed=[]
for current,dirs,names in os.walk(R):
 dirs[:]=[d for d in dirs if d not in {'sources','raw_discovery','__pycache__','.git','.lake'}]
 distributed.extend(Path(current)/n for n in names)
for f in (p for p in distributed if p.suffix=='.jsonl'):
 try:
  for n,line in enumerate(f.read_text().splitlines(),1):
   if line.strip():json.loads(line);checks+=1
 except Exception as e:errors.append(f'{f.relative_to(R)}:{n}: {e}')
for f in (p for p in distributed if p.suffix=='.py'):
 try:ast.parse(f.read_text());checks+=1
 except Exception as e:errors.append(f'{f.relative_to(R)}: {e}')
def rows(p):return [json.loads(x) for x in (R/p).read_text().splitlines() if x.strip()]
bib=rows('corpus/bibliography.jsonl');th=rows('theorems/theorems.jsonl');graph=rows('graphs/knowledge_graph.jsonl')
promotion_path=R/'quality/whole_work_audit_promotions.jsonl'
promotions={r['id']:r for r in rows('quality/whole_work_audit_promotions.jsonl')} if promotion_path.exists() else {}
for label,rr in [('papers',bib),('theorems',th)]:
 ids=[x['id'] for x in rr]
 if len(ids)!=len(set(ids)):errors.append('duplicate '+label+' ID')
for r in bib:
 if not (R/r['record_path']).exists():errors.append('missing '+r['record_path'])
 if not r.get('source_url'):errors.append('missing source URL '+r['id'])
 if r['audit_level']>=2:
  promotion=promotions.get(r['id'])
  if not promotion or promotion.get('level')!=r['audit_level'] or not promotion.get('evidence') or not promotion.get('whole_work_coverage_checklist'):
   errors.append('whole-paper audit promotion lacks explicit coverage/evidence registry: '+r['id'])
  elif any(promotion.get(k)!=r.get(k) for k in ('version','source_sha256') if k in promotion):
   errors.append('whole-paper promotion version/hash differs from source: '+r['id'])
  if promotion:
   for ref in [promotion.get('evidence'),*promotion.get('independent_reviews',[])]:
    if not ref or not (R/ref).is_file():errors.append('missing whole-paper audit evidence '+str(ref))
 if r['whole_work_read'] and r['audit_level']<1:errors.append('inconsistent reading level '+r['id'])
 if r['audit_level']>=1 and not r['whole_work_read']:errors.append('audit level exceeds whole-work reading scope '+r['id'])
for t in th:
 if not t.get('locator'):errors.append('missing theorem evidence '+t['id'])
 if t.get('paper_id') and t['paper_id'] not in {b['id'] for b in bib}:errors.append('unresolved paper '+t['id'])
nodes={x['id'] for x in graph if x['record_type']=='node'}
if len(nodes)!=sum(x['record_type']=='node' for x in graph):errors.append('duplicate graph node ID')
for e in graph:
 if e['record_type']=='edge':
  if e['from'] not in nodes or e['to'] not in nodes:errors.append('unresolved edge '+str(e))
  if not e.get('provenance'):errors.append('missing edge provenance')
required=['README.md','START_HERE.md','CONTINUATION.md','executive_report.md','methodology.md','corpus/bibliography.csv','corpus/bibliography.jsonl','corpus/selection_decisions.csv','corpus/access_and_audit_manifest.csv','theorems/theorems.jsonl','theorems/proof_dependencies.jsonl','theorems/notation_dictionary.md','audits/findings.jsonl','audits/verified_findings.md','audits/unresolved_findings.md','connections/connections.jsonl','connections/strongest_connections.md','connections/cross_field_opportunities.md','history/chronological_timeline.md','history/evolution_of_methods.md','history/abandoned_approaches.md','frontiers/research_programs.md','frontiers/missing_lemmas.md','frontiers/known_obstructions.md','frontiers/unsolved_questions.md','experiments/reproducibility.md','proposals/ranked_research_directions.md','proposals/actionable_conjectures.md','graphs/knowledge_graph.jsonl','graphs/graph_schema.md','quality/coverage_report.md','quality/evidence_audit.md','quality/limitations.md','final_synthesis/comprehensive_report.md','final_synthesis/top_100_insights.md','final_synthesis/top_25_research_opportunities.md','final_synthesis/open_problems_for_future_agents.md']
for p in required:
 if not (R/p).is_file() or (R/p).stat().st_size==0:errors.append('missing/empty required '+p)
metrics=json.loads((R/'quality/metrics.json').read_text())
if metrics['selected_checkpoint_works']!=sum(r.get('selection_status')=='selected_checkpoint_priority_work' for r in bib):errors.append('stale selected-paper count')
if metrics.get('catalogued_works',len(bib))!=len(bib):errors.append('stale catalogued-paper count')
if metrics['theorem_or_exercise_records']!=len(th):errors.append('stale theorem count')
for f in rows('audits/findings.jsonl'):
 if f['verified_author_error'] and not (f.get('director_adjudication') and len(f.get('independent_reviews',[]))>=2 and f.get('explicit_witness')):
  errors.append('alleged verified error lacks director, independent evidence or explicit witness: '+f['id'])
checks+=len(required)+len(bib)+len(th)+len(graph)
report={'validation':'PASS' if not errors else 'FAIL','structural_checks_and_parsed_records':checks,'errors':errors,'limitations':'Structural, identity, provenance-field and scope consistency only; does not prove mathematics or verify bibliographic fields externally.'}
(R/'quality/validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
if errors:sys.exit(1)
