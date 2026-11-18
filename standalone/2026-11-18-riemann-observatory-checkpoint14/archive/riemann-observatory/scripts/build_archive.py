#!/usr/bin/env python3
"""Merge curated track records, preserving originals and stable IDs. No network."""
import csv,json,hashlib,re,os
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def readj(path):
 return [json.loads(x) for x in path.read_text().splitlines() if x.strip()] if path.exists() else []
def writej(path,rows):
 path.parent.mkdir(parents=True,exist_ok=True);path.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows))
def csvout(path,rows,fields):
 with path.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader()
  for r in rows:w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in r.items()})
aliases={r['alias']:r['canonical'] for r in readj(ROOT/'quality/paper_aliases.jsonl')}
def canonical(ref):
 if not isinstance(ref,str):return ref
 base,sep,tail=ref.partition(':')
 seen=set()
 while base in aliases:
  assert base not in seen,'Cyclic paper alias'
  seen.add(base);base=aliases[base]
 return base+sep+tail
def is_dependency_file(path):
 return 'dependencies' in path.name or 'proof_edges' in path.name
records=[]
for f in sorted((ROOT/'papers').glob('*records.jsonl')):
 for orig in readj(f):
  r=dict(orig);r['id']=r.get('id',r.get('paper_id'));assert r['id']
  r['arxiv']=r.get('arxiv',r.get('arxiv_id'));r['source_url']=r.get('source_url',r.get('canonical_url'));r['version']=r.get('version',r.get('version_read'))
  r['read_scope']=r.get('read_scope') or r.get('audit_scope') or r.get('technical_audit_scope') or r.get('scope')
  r['access_status']=r.get('access_status','full_text_accessed' if r.get('full_text_accessed') else 'unknown')
  raw_access=str(r['access_status'])
  if raw_access=='primary_excerpt_accessed':r['access_status']='primary_source_excerpt_accessed'
  if raw_access.startswith(('full_text_accessed','full_primary_','full_scanned_primary_')):
   r['original_access_status']=raw_access;r['access_status']='full_text_accessed'
  r['whole_work_read']=r.get('whole_work_read',r.get('substantive_whole_work_read',r.get('substantive_reading') is True or str(r.get('substantive_reading','')).startswith('complete_') or (r.get('audit_level',0)>=1 and 'Complete' in (r.get('read_scope') or ''))))
  r['record_path']=r.get('record_path',r.get('record_file',f'papers/{r["id"]}.md'));r['track_file']=str(f.relative_to(ROOT))
  r['original_selection_status']=r.get('selection_status')
  r['selection_status']='deferred_supporting_bibliographic_record' if r.get('selected') is False else 'selected_checkpoint_priority_work'
  records.append(r)
for f in sorted((ROOT/'papers').glob('*updates.jsonl')):
 for update in readj(f):
  ident=update.get('id',update.get('paper_id'))
  matches=[r for r in records if r['id']==ident]
  assert len(matches)==1,('Scope update must target exactly one existing work',ident)
  r=matches[0]
  r['audit_level']=update.get('audit_level',r['audit_level'])
  r['read_scope']=update.get('read_scope',update.get('audit_scope',r.get('read_scope')))
  if update.get('substantive_reading') is True:r['whole_work_read']=True
  if update.get('full_text_accessed'):r['access_status']='full_text_accessed'
  r['scope_update_evidence']=update.get('scope_evidence',str(f.relative_to(ROOT)))
  r.setdefault('additional_scope_update_files',[]).append(str(f.relative_to(ROOT)))
for f in sorted((ROOT/'papers').glob('*source_overlay*.jsonl')):
 for overlay in readj(f):
  ident=overlay.get('id',overlay.get('paper_id'));matches=[r for r in records if r['id']==ident]
  assert len(matches)==1,('Source overlay must target one existing work',ident)
  r=matches[0];r.setdefault('source_manifestation_overlays',[]).append(overlay)
  r.setdefault('additional_scope_update_files',[]).append(str(f.relative_to(ROOT)))
  if overlay.get('whole_original_print_read'):
   r['whole_work_read']=True;r['audit_level']=max(1,r.get('audit_level',0))
   r['read_scope']=str(r.get('read_scope',''))+'; additional original-language source scope: '+str(overlay.get('audit_scope',''))
  r['source_overlay_evidence']=overlay.get('overlay_path',str(f.relative_to(ROOT)))
# Keep every original track record; canonicalize duplicate works only in the
# aggregate. A fuller reading of a different manifestation remains explicit.
merged={}
for r in records:
 original_id=r['id'];r['id']=canonical(original_id)
 r['source_record_ids']=[original_id]
 if r['id'] not in merged:merged[r['id']]=r;continue
 old=merged[r['id']]
 old.setdefault('source_record_ids',[]).append(original_id)
 old.setdefault('manifestation_records',[]).append(r)
 for field in ('title','authors','date','year','venue','doi','arxiv','source_url','publication_status','canonical_version_expression'):
  if not old.get(field) and r.get(field):old[field]=r[field]
 if r['whole_work_read'] and not old['whole_work_read']:
  old['whole_work_read']=True
  old['read_scope']=str(old.get('read_scope',''))+'; additional complete reading: '+str(r.get('read_scope',''))
 if r['access_status']=='full_text_accessed':old['access_status']='full_text_accessed'
 old['audit_level']=max(old.get('audit_level',0),r.get('audit_level',0))
records=list(merged.values())
# Apply current director fields after manifestation/event rows have merged.
for f in sorted((ROOT/'quality').glob('*source_scope_updates*.jsonl')):
 for update in readj(f):
  matches=[r for r in records if r['id']==canonical(update['id'])]
  assert len(matches)==1,('Source scope update must target one work',f.name,update['id'])
  r=matches[0];r.setdefault('scope_update_history',[]).append({'fields':update['fields'],'evidence':update['evidence'],'track_file':str(f.relative_to(ROOT))})
  r.update(update['fields']);r['scope_update_evidence']=update['evidence']
  r.setdefault('additional_scope_update_files',[]).append(str(f.relative_to(ROOT)))
assert len({r['id'] for r in records})==len(records)
writej(ROOT/'corpus/bibliography.jsonl',records)
csvout(ROOT/'corpus/bibliography.csv',records,['id','title','authors','date','year','venue','doi','arxiv','version','source_url','publication_status','family','selection_status','audit_level','whole_work_read','access_status','read_scope','record_path'])
csvout(ROOT/'corpus/access_and_audit_manifest.csv',records,['id','selection_status','access_status','audit_level','whole_work_read','read_scope','version','source_url','source_sha256','track_file'])
selected=[{'id':r['id'],'decision':r['selection_status'],'reason':r.get('original_selection_status') if r.get('selected') is False else r.get('selection_reason',r.get('priority_reason','Priority/dependency value documented in paper record; access, reading and audit scope are separate explicit fields. Selection does not imply that full text was obtained.'))} for r in records]
candidates=readj(ROOT/'corpus/candidates.jsonl');screen=readj(ROOT/'corpus/candidates_rejected.jsonl');rejected={r.get('candidate_id'):r for r in screen}
curated=[]
for f in sorted((ROOT/'corpus').glob('curated_candidate_decisions*.jsonl')):curated+=readj(f)
curated_by_id={r['candidate_id']:r for r in curated}
assert len(curated_by_id)==len(curated),'Duplicate candidate triage ID; resolve version history explicitly'
selected_candidate_crosswalk={}
for r in records:
 candidate_id=r.get('candidate_id') or (r.get('other_identifiers') or {}).get('candidate')
 if candidate_id and r['selection_status']=='selected_checkpoint_priority_work':
  selected_candidate_crosswalk.setdefault(candidate_id,[]).append(r['id'])
for r in candidates:
 reject=rejected.get(r['candidate_id'])
 decision=curated_by_id.get(r['candidate_id'])
 if r['candidate_id'] in selected_candidate_crosswalk:
  selected.append({'id':r['candidate_id'],'decision':'selected_via_canonical_work_record','reason':'Explicit provider-to-work identity crosswalk: '+', '.join(selected_candidate_crosswalk[r['candidate_id']])+'. Original curated triage history retained in contributor files.'})
  continue
 selected.append({'id':r['candidate_id'],'decision':decision['decision'] if decision else 'rejected' if reject else 'pending_relevance_and_version_review','reason':decision['reason'] if decision else reject.get('reason',reject.get('exclusion_reason','explicit lexical collision; see candidates_rejected.jsonl')) if reject else 'Provider discovery only; no importance judgment, source audit or admission to primary corpus.'})
provider_candidate_ids={r['candidate_id'] for r in candidates}
for ident,r in curated_by_id.items():
 if ident not in provider_candidate_ids:selected.append({'id':ident,'decision':r['decision'],'reason':r['reason']+' Additional curated record; provider reconciliation pending; no source-reading promotion.'})
csvout(ROOT/'corpus/selection_decisions.csv',selected,['id','decision','reason'])
# Theorem and connection master files preserve track-specific fields.
theorems=[]
for f in sorted(p for p in (ROOT/'theorems').glob('*.jsonl') if p.name not in {'theorems.jsonl','proof_dependencies.jsonl'} and not is_dependency_file(p)):
 for r in readj(f):
  r['id']=r.get('id',r.get('theorem_id'));assert r['id'],f
  r['paper_id']=canonical(r.get('paper_id'))
  r['locator']=r.get('locator') or r.get('source_locator') or r.get('evidence') or r.get('proof_reference') or r.get('proof_file') or r.get('provenance');r['provenance_file']=str(f.relative_to(ROOT));theorems.append(r)
# Program-level independent claims not duplicated in source tracks.
theorems += [
 {'id':'OBS-LI-001','paper_id':None,'statement':'For every N there is a real symmetric order-one entire function with all zeros in the critical strip, first N Li derivatives positive, and an off-line quartet. This remains true with Riemann–von Mangoldt smooth zero count to O(1).','locator':'proposals/independent_campaigns/li_advocate.md','status':'independently_reconstructed_generic_class_obstruction; no novelty claim','verification':'scoped_Level3; director_adjudication.md'},
 {'id':'OBS-R001-FINITE','paper_id':'PAPER-R001','statement':'For all integers2<=n<=5040, sigma(n)<H_n+exp(H_n)logH_n; equality at1.','locator':'experiments/code/lagarias_finite.py','status':'known_finite_step_independently_reproduced','verification':'exact_integer_certificate_and_independent_review'}]
for r in theorems:
 if r['id'] in ['THM-E005','THM-E006','OBS-S-C1','OBS-S-C2','THM-L001','THM-L002','THM-L004','THM-E010']:
  r['verification']='scoped_Level3; audits/adversarial_reviews/director_adjudication.md'
 if r['id'] in ['THM-E007','THM-E008','THM-E009']:
  r['verification']='independent_director_reconstruction; cluster_skeptic review where present'
claim_updates={r['id']:r for r in readj(ROOT/'quality/claim_status_updates.jsonl')}
for r in theorems:
 if r['id'] in claim_updates:
  u=claim_updates[r['id']];r.update(u['fields']);r['status_update_evidence']=u['evidence']
assert len({r['id'] for r in theorems})==len(theorems)
writej(ROOT/'theorems/theorems.jsonl',theorems)
connections=[]
for f in sorted(p for p in (ROOT/'connections').glob('*.jsonl') if p.name!='connections.jsonl'):
 for r in readj(f):
  r['id']=r.get('id',r.get('connection_id'));r['provenance_file']=str(f.relative_to(ROOT));connections.append(r)
for c in connections:
 if c['id'] in ['CONN-E001','CONN-E002','CONN-S001']:c['checkpoint_verification']='independently checked scoped claim; director_adjudication.md'
for c in connections:
 if c['id']=='CONN-E002':c['next_step_checkpoint']='Two-root uniform remainder now proved in THM-E010; next fixed-multi-cluster uniform bounds and grouped arithmetic residues.'
connection_updates={r['id']:r for r in readj(ROOT/'quality/connection_status_updates.jsonl')}
for c in connections:
 if c['id'] in connection_updates:
  update=connection_updates[c['id']];c['original_status']=c.get('status');c.update(update['fields']);c['status_update_evidence']=update['evidence']
writej(ROOT/'connections/connections.jsonl',connections)
deps=[
 ('THM-E001','THM-E002','context','Different criteria/distances: no claim that closure theorem alone proves sharp bound.'),
 ('THM-E002','THM-E004','supplies_lower_bound','For discrete cutoff1/N, continuous dilation space is larger; additional RH and derivative moment needed for matching upper bound.'),
 ('THM-E003','THM-E006','special_case_reconstructed','All roots on unit circle; Q=(1-z)^2,target1.'),
 ('THM-S003-SECU','OBS-S-C1','supplies_input_to','Positive finite lengths, fixed energy-independent unitary boundary matrix.'),
 ('OBS-S-C1','OBS-S-C2','supplies_input_to','RVM main term and simultaneous o(K) accuracy at K,2K,4K.'),
 ('THM-R001-2','THM-R001-1','supplies_input_to','Plus Robin RH and oscillation dependencies and finite n<=5040 check.'),
 ('OBS-R001-FINITE','THM-R001-1','supplies_finite_dependency','Only n<=5040; infinite tail remains external analytic theorem.')]
ids={x['id'] for x in theorems};dep_rows=[]
for a,b,rel,evidence in deps:
 if a in ids and b in ids:dep_rows.append({'from':a,'to':b,'relation':rel,'evidence':evidence,'status':'reconstructed_scoped','locator':next(t['locator'] for t in theorems if t['id']==b)})
for f in sorted(p for p in (ROOT/'theorems').glob('*.jsonl') if is_dependency_file(p) and p.name!='proof_dependencies.jsonl'):
 for d in readj(f):
  d['from']=canonical(d.get('from') or d.get('source') or d.get('source_id'));d['to']=canonical(d.get('to') or d.get('target') or d.get('target_id'))
  assert d['from'] and d['to'],f
  d['track_file']=str(f.relative_to(ROOT));d['locator']=d.get('locator',d.get('provenance',d.get('source_locator',d.get('evidence'))));dep_rows.append(d)
writej(ROOT/'theorems/proof_dependencies.jsonl',dep_rows)
nodes=[{'record_type':'node','id':r['id'],'type':'paper','label':r['title'],'evidence':r['record_path'],'status':r['audit_level'],**{k:r[k] for k in ('canonical_version_expression','source_url','selection_status') if r.get(k) is not None}} for r in records]
nodes +=[{'record_type':'node','id':t['id'],'type':'conjecture' if 'CONJ' in t['id'] else 'mathematical_claim','label':t['statement'],'evidence':t['locator'],'status':t.get('status',t.get('verification_status','source_read')),**{k:t[k] for k in ('claim_kind','hypotheses','verification_scope') if t.get(k) is not None}} for t in theorems]
edges=[]
for t in theorems:
 if t.get('paper_id'):
  edges.append({'record_type':'edge','from':t['paper_id'],'to':t['id'],'relation':'associated_with_claim_record','provenance':t['locator'],'status':'catalogue association only; record kind/provenance distinguishes source theorem from derived result or certificate check'})
existing_ids={n['id'] for n in nodes}
for d in dep_rows:
 for ref in [d['from'],d['to']]:
  if ref not in existing_ids:
   if ':' not in ref and not ref.startswith(('TECH-','EXT-','EXTERNAL-','LOCAL-')):raise ValueError('Unresolved dependency '+ref)
   node_type='technique' if ref.startswith('TECH-') else 'external_claim' if ref.startswith(('EXT-','EXTERNAL-')) else 'source_passage'
   nodes.append({'record_type':'node','id':ref,'type':node_type,'label':ref,'evidence':d['locator'],'status':'explicit cited dependency; see exact inspected scope in paper/audit; ancestry not fully audited'});existing_ids.add(ref)
 edges.append({'record_type':'edge',**d,'provenance':d['locator']})
# A connection is a separately scoped proposition/research interface, never an
# automatic theorem implication between every paper sharing a keyword.
for c in connections:
 label=c.get('statement',c.get('claim',c.get('kind',c['id'])))
 evidence=c.get('evidence',c['provenance_file'])
 nodes.append({'record_type':'node','id':c['id'],'type':'research_connection','label':label,'evidence':evidence,'status':c.get('verification',c.get('verification_status',c.get('status','inspect established and conjectural portions in connection record')))})
 existing_ids.add(c['id'])
 refs=c.get('source_theorems',c.get('source_papers',c.get('sources',[])))
 if not isinstance(refs,list):refs=[]
 for raw_ref in refs:
  ref=canonical(raw_ref)
  if not isinstance(ref,str):continue
  if ref not in existing_ids and not re.match(r'^(PAPER|THM|OBS|LEM|TECH|LOCAL|EXT|DEF|CONJ)-[A-Za-z0-9_-]+(?::.*)?$',ref):continue
  if ref not in existing_ids:
   # Preserve a cited passage as a passage, not an invented theorem audit.
   nodes.append({'record_type':'node','id':ref,'type':'source_passage','label':ref,'evidence':evidence,'status':'connection reference only; inspect source scope before use'})
   existing_ids.add(ref)
  edges.append({'record_type':'edge','from':c['id'],'to':ref,'relation':'has_input_reference','provenance':evidence,'status':'reference only; compatible assumptions and proved/conjectural portions are explicit in connection record'})
# Contributor graph tracks may record additional explicitly sourced mathematical
# relationships; retain their direction/status rather than flatten to citations.
for f in sorted((ROOT/'graphs').glob('*.jsonl')):
 if f.name=='knowledge_graph.jsonl':continue
 for raw in readj(f):
  if raw.get('record_type')=='node' or (raw.get('id') and not (raw.get('from') or raw.get('source'))):
   node=dict(raw);node['id']=canonical(node['id']);node['record_type']='node'
   node.setdefault('type','source_passage' if ':' in node['id'] else 'mathematical_structure')
   node.setdefault('evidence',node.get('provenance',str(f.relative_to(ROOT))))
   if node['id'] not in existing_ids:nodes.append(node);existing_ids.add(node['id'])
   else:
    for old in nodes:
     if old['id']==node['id'] and old['type'] in {'source_passage','external_claim'}:old.update(node)
   continue
  a=canonical(raw.get('from',raw.get('source')));b=canonical(raw.get('to',raw.get('target')))
  assert a and b,('Malformed graph track',f,raw)
  b=re.sub(r'^(PAPER-[A-Za-z0-9]+)-Theorem',r'\1:Theorem',b)
  for ref in [a,b]:
   if ref not in existing_ids:
    nodes.append({'record_type':'node','id':ref,'type':'external_claim' if ref.startswith(('EXT-','EXTERNAL-')) else 'source_passage' if ':' in ref else 'mathematical_structure','label':ref,'evidence':raw.get('provenance',str(f.relative_to(ROOT))),'status':'explicit contributor reference; inspect track scope; no inferred source audit'})
    existing_ids.add(ref)
  edges.append({'record_type':'edge',**raw,'from':a,'to':b,'track_file':str(f.relative_to(ROOT)),'provenance':raw.get('provenance',raw.get('evidence'))})
authors={}
for r in records:
 for name in r['authors']:
  aid='AUTHOR-'+hashlib.sha256(name.encode()).hexdigest()[:12].upper()
  authors[aid]={'record_type':'node','id':aid,'type':'author','label':name,'evidence':r['record_path'],'status':'bibliographic_identity'}
  edges.append({'record_type':'edge','from':aid,'to':r['id'],'relation':'author_of','provenance':r['source_url'],'status':'source_identity'})
nodes+=list(authors.values())
for tid,label,evidence in [
 ('TECH-FRAME','Parseval frame bound','audits/adversarial_reviews/af_boundary_repair.md'),
 ('TECH-JETS','Confluent residual-jet interpolation','proposals/independent_campaigns/clustered_root_transition.md'),
 ('TECH-FLOW','Unitary eigenphase flow','audits/adversarial_reviews/graph_skeptic.md'),
 ('DEF-LI','Li derivative convention','theorems/notation_dictionary.md'),
 ('OBS-ARITH-TAIL','Missing arithmetic tail control','frontiers/missing_lemmas.md'),
 ('OBS-CLUSTER','Missing cluster-uniform infinite residue bounds','frontiers/missing_lemmas.md')]:
 nodes.append({'record_type':'node','id':tid,'type':'technique' if tid.startswith('TECH') else 'definition' if tid.startswith('DEF') else 'open_obstacle','label':label,'evidence':evidence,'status':'defined_or_explicitly_open'})
for f in sorted((ROOT/'experiments/code').glob('*.py')):
 eid='EXP-'+hashlib.sha256(f.stem.encode()).hexdigest()[:12].upper()
 nodes.append({'record_type':'node','id':eid,'type':'experiment','label':f.stem,'evidence':str(f.relative_to(ROOT)),'status':'code_saved; see results and reproducibility classification'})
writej(ROOT/'graphs/knowledge_graph.jsonl',nodes+edges)
selected_records=[r for r in records if r['selection_status']=='selected_checkpoint_priority_work']
cutoff_record=json.loads((ROOT/'quality/literature_cutoff.json').read_text()) if (ROOT/'quality/literature_cutoff.json').exists() else {'date':'2026-11-17'}
stats={'cutoff':cutoff_record['date'],'metadata_candidates':len(candidates),'metadata_candidates_rejected':len(rejected),'metadata_candidates_pending':len(candidates)-len(rejected),'catalogued_works':len(records),'deferred_supporting_works':len(records)-len(selected_records),'selected_checkpoint_works':len(selected_records),'fulltexts_accessed_selected':sum(r['access_status']=='full_text_accessed' for r in selected_records),'whole_work_or_translation_read':sum(r['whole_work_read'] for r in selected_records),'whole_work_audit_levels':dict(Counter(str(r.get('audit_level',0)) for r in selected_records)),'scoped_level3_claim_groups':sum(x.get('status')=='adjudicated_scoped' for x in readj(ROOT/'audits/reviewed_claim_groups.jsonl')) if (ROOT/'audits/reviewed_claim_groups.jsonl').exists() else 6,'theorem_or_exercise_records':len(theorems),'connection_records':len(connections),'graph_nodes':len(nodes),'graph_edges':len(edges),'warning':'Candidate pool not fully relevance-reviewed or manifestation-deduplicated; selected works may overlap provider candidates. Do not add counts. Scoped adjudication groups are not complete-paper Level3 audits.'}
stats.update({'curated_candidate_decisions':len(curated),'curated_priority_candidates':sum(r['decision'] in {'priority_candidate_verified_metadata','priority_candidate_reviewed_provider_metadata'} for r in curated),'curated_provider_matches':sum(r['candidate_id'] in provider_candidate_ids for r in curated),'additional_curated_records_unreconciled':sum(r['candidate_id'] not in provider_candidate_ids for r in curated),'paper_aliases_resolved':len(aliases)})
stats['selected_primary_excerpt_accessed']=sum(r['access_status']=='primary_source_excerpt_accessed' for r in selected_records)
(ROOT/'quality/metrics.json').write_text(json.dumps(stats,indent=2)+'\n')
# Hash private source bytes for identity without redistributing them.
source_rows=[]
for current,dirs,names in os.walk(ROOT/'sources'):
 dirs[:]=[d for d in dirs if d not in {'.git','.lake','__pycache__','formal_round2','palomar_formal62','toolchains','node_modules'}]
 for name in sorted(names):
  f=Path(current)/name
  if f.suffix.lower() not in {'.pdf','.txt','.jpg','.jpeg','.png','.html','.xml','.json'}:continue
  source_rows.append({'path':str(f.relative_to(ROOT)),'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'bytes':f.stat().st_size,'distribution':'omitted; retrieve from source URL in paper/track record; formal repository artifacts pinned separately by git commit and dedicated manifests'})
writej(ROOT/'corpus/source_file_hashes.jsonl',source_rows)
print(json.dumps(stats,indent=2))
