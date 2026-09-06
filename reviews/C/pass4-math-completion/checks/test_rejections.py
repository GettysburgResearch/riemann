#!/usr/bin/env python3
"""Actual normal/-O subprocess refusal tests; outputs a receipt, never reseals production."""
import argparse,copy,csv,hashlib,io,json,subprocess,sys,tempfile,shutil
from pathlib import Path
R=Path(__file__).resolve().parents[1]

def seal(root):
 entries=[]
 for p in sorted(root.rglob('*')):
  if p.is_file() and p.name!='MANIFEST.json':
   d=p.read_bytes();entries.append({'path':p.relative_to(root).as_posix(),'bytes':len(d),'sha256':hashlib.sha256(d).hexdigest()})
 (root/'MANIFEST.json').write_text(json.dumps({'schema':'riemann.review.C4.manifest.v1','files':entries},indent=2)+'\n')
def setrow(path,selector,col,val):
 with path.open() as f:r=csv.DictReader(f,delimiter='\t');headers=r.fieldnames;rows=list(r)
 for row in rows:
  if selector(row):row[col]=val;break
 else:raise ValueError('mutation target missing')
 with path.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=headers,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
def packet_mutate(q,kind):
 if kind=='unsealed_proof':
  with (q/'proofs/XI_SOURCE_REPAIR.md').open('a') as f:f.write('\nchanged\n')
  return
 if kind=='missing_proof':(q/'proofs/XI_SOURCE_REPAIR.md').unlink()
 elif kind=='extra_file':(q/'unexpected.txt').write_text('extra')
 elif kind=='empty_claims':
  p=q/'CLAIMS.tsv';p.write_text(p.read_text().splitlines()[0]+'\n')
 elif kind=='duplicate_claim':
  p=q/'CLAIMS.tsv';p.write_text(p.read_text()+p.read_text().splitlines()[1]+'\n')
 elif kind=='promote_open_node':setrow(q/'NODES.tsv',lambda r:r['node_id']=='H.MELLIN.NEGATIVE_MASS','status','ASSUMPTION')
 elif kind=='unknown_premise':setrow(q/'EDGES.tsv',lambda r:r['edge_id']=='C4-E06','premise_ids','["FAKE"]')
 elif kind=='changed_source_pin':setrow(q/'SOURCES.tsv',lambda r:r['source_id']=='SRC-X0','commit_sha','1'*40)
 elif kind=='empty_scope':(q/'SCOPE.json').write_text('{}\n')
 elif kind=='compiled_alias':
  p=q/'SCOPE.json';x=json.loads(p.read_text());x['lean_compiled']=True;p.write_text(json.dumps(x))
 elif kind=='empty_manifest':
  (q/'MANIFEST.json').write_text('{"schema":"riemann.review.C4.manifest.v1","files":[]}');return
 else:raise ValueError(kind)
 seal(q)
def run(cmd,prefix='FAIL: '):
 p=subprocess.run(cmd,capture_output=True,text=True,timeout=40)
 if p.returncode!=2 or not p.stderr.startswith(prefix):raise ValueError('mutation not rejected: '+repr((cmd,p.returncode,p.stdout,p.stderr)))
 return {'exit_code':p.returncode,'stderr_prefix':p.stderr.strip()[:180]}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--mode',choices=['normal','optimized','both'],default='both');ap.add_argument('--suite',choices=['packet','math_result','both'],default='both');a=ap.parse_args()
 out=[]
 pkg=['unsealed_proof','missing_proof','extra_file','empty_claims','duplicate_claim','promote_open_node','unknown_premise','changed_source_pin','empty_scope','compiled_alias','empty_manifest']
 for mode in (['normal','optimized'] if a.mode=='both' else [a.mode]):
  flags=['-B']+(['-O'] if mode=='optimized' else [])
  for kind in (pkg if a.suite in ['packet','both'] else []):
   with tempfile.TemporaryDirectory(prefix='c4-refusal-') as d:
    q=Path(d)/'packet';shutil.copytree(R,q);packet_mutate(q,kind)
    rec=run([sys.executable,*flags,str(q/'checks/validate_packet.py')]);out.append({'suite':'packet','mode':mode,'case':kind,**rec})
  base=json.loads((R/'checks/result.json').read_text())
  for kind in (['empty_scope','rh_true','bool_count','float_count','missing_field','extra_field','duplicate_key','changed_constant','changed_count'] if a.suite in ['math_result','both'] else []):
   x=copy.deepcopy(base)
   if kind=='empty_scope':x['scope']={}
   elif kind=='rh_true':x['scope']['rh_proved']=True
   elif kind=='bool_count':x['groups'][next(iter(x['groups']))]=True
   elif kind=='float_count':k=next(iter(x['groups']));x['groups'][k]=float(x['groups'][k])
   elif kind=='missing_field':del x['constants']
   elif kind=='extra_field':x['extra']=0
   elif kind=='changed_constant':x['constants'][next(iter(x['constants']))]='0'
   elif kind=='changed_count':x['groups'][next(iter(x['groups']))]+=1
   text=json.dumps(x)
   if kind=='duplicate_key':text=text[:-1]+',"schema":"again"}'
   with tempfile.TemporaryDirectory(prefix='c4-result-') as d:
    p=Path(d)/'bad.json';p.write_text(text)
    rec=run([sys.executable,*flags,str(R/'checks/math_checks.py'),'--check',str(p)],prefix='REJECT: ')
    out.append({'suite':'math_result','mode':mode,'case':kind,**rec})
 print(json.dumps({'status':'PASS_C4_REJECTION_TESTS','selected_mode':a.mode,'selected_suite':a.suite,'package_cases_per_mode':len(pkg) if a.suite in ['packet','both'] else 0,'math_result_cases_per_mode':9 if a.suite in ['math_result','both'] else 0,'executions':len(out),'results':out},indent=2))
if __name__=='__main__':main()
