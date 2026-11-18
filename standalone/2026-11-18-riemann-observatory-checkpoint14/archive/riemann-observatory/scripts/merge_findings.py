#!/usr/bin/env python3
"""Normalize evidence tracks, retaining original schemas and review scopes."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
files=sorted(p for p in (R/'audits').glob('*.jsonl') if 'findings' in p.name and p.name!='findings.jsonl')
rows=[]
for p in files:
 for line in p.read_text().splitlines():
  if not line.strip():continue
  x=json.loads(line);r=dict(x)
  r['id']=x.get('id',x.get('finding_id'));assert r['id']
  r['classification']=x.get('classification',x.get('category','Unresolved ambiguity requiring expert review'))
  r['title']=x.get('title',x.get('scope',x.get('statement','Scoped research finding')))
  r['sources']=x.get('sources',x.get('paper_ids',x.get('paper_id')))
  r['evidence']=x.get('evidence',x.get('provenance'))
  r['scope']=x.get('scope',x.get('result',x.get('statement')))
  r['verified_author_error']=x.get('verified_author_error',False)
  r['track_file']=str(p.relative_to(R));rows.append(r)
assert len({x['id'] for x in rows})==len(rows),'duplicate finding IDs'
# Later source access can resolve an old scope without editing contributor history.
status_path=R/'quality/finding_status_updates.jsonl'
if status_path.exists():
 by_status_id={x['id']:x for x in rows}
 for line in status_path.read_text().splitlines():
  if not line.strip():continue
  update=json.loads(line);assert update['id'] in by_status_id,('Unknown finding status target',update['id'])
  target=by_status_id[update['id']]
  target.setdefault('status_update_history',[]).append({'fields':update['fields'],'evidence':update['evidence']})
  target.update(update['fields']);target['status_update_evidence']=update['evidence']
alias_path=R/'quality/finding_aliases.jsonl'
aliases={x['alias']:x for x in (json.loads(s) for s in alias_path.read_text().splitlines() if s.strip())} if alias_path.exists() else {}
by_id={x['id']:x for x in rows}
for ident,a in aliases.items():
 assert ident in by_id and a['canonical'] in by_id,('Missing finding alias endpoint',a)
 assert a['canonical'] not in aliases,'Chained finding aliases must be resolved explicitly'
 target=by_id[a['canonical']]
 target.setdefault('contributor_records',[]).append(by_id[ident])
 target.setdefault('alias_ids',[]).append(ident)
 target.setdefault('alias_evidence',[]).append(a['evidence'])
rows=[x for x in rows if x['id'] not in aliases]
(R/'audits/findings.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows))
for kind,name in [('Unresolved','unresolved_findings.md'),('checked','verified_findings.md')]:
 chosen=[x for x in rows if (x['classification'].startswith('Unresolved') or x['classification'].startswith('Strongly suspected'))==(kind=='Unresolved')]
 errors=sum(bool(x['verified_author_error']) for x in rows)
 text='# '+('Unresolved issues, not verified source errors' if kind=='Unresolved' else 'Scoped findings and reconstructions')+f'\n\n{errors} version-specific mathematical statement counterexample(s) have director adjudication and explicit independent witnesses. Inspect their exact scope; this count does not characterize entire papers or their main RH results as false. Other items retain their individual verification states. Static, numerical and mathematical scopes remain distinct.\n\n'
 for x in chosen:
  text+=f'## {x["id"]}\n\n{x["classification"]}. {x["title"]}\n\nScope: {x["scope"]}.\n\nEvidence: {x["evidence"]}. Track: {x["track_file"]}.\n\n'
  if x.get('status_update_evidence'):
   text+=f'Current source adjudication: [status update](../{x["status_update_evidence"]}). Original contributor evidence remains above and in the structured history.\n\n'
 (R/'audits'/name).write_text(text)
print(json.dumps({'findings':len(rows),'verified_author_errors':sum(x['verified_author_error'] for x in rows)}))
