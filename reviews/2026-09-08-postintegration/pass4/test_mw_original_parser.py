from pathlib import Path
import json, subprocess, sys, hashlib, tempfile
ROOT=Path(__file__).resolve().parent
source=ROOT/'sources/MW/certify.py'
raw=(ROOT/'evidence/mw-normal.json').read_text()
base=json.loads(raw)
cases={}
x=json.loads(raw);x['integer_events']=65536.0;x['checkpoints'][0]=True
cases['float_event_count_boolean_checkpoint']=json.dumps(x,sort_keys=True,indent=2)+'\n'
cases['duplicate_key_last_wins']=raw.replace('"integer_events": 65536,','"integer_events": 1,\n  "integer_events": 65536,')
x=json.loads(raw);x['results'][-1]['J']['hi']=str(int(x['results'][-1]['J']['hi'])+1)
cases['changed_numerical_endpoint']=json.dumps(x,sort_keys=True,indent=2)+'\n'
rows=[]
with tempfile.TemporaryDirectory() as d:
 for mode in ('normal','optimized'):
  for name,text in [('pristine',raw),*cases.items()]:
   p=Path(d)/(name+'.json');p.write_text(text)
   cmd=[sys.executable,'-I','-S','-B']+(['-O'] if mode=='optimized' else [])+[str(source),'--expect',str(p)]
   r=subprocess.run(cmd,capture_output=True,text=True,timeout=30)
   rows.append({'mode':mode,'case':name,'returncode':r.returncode,'stdout_sha256':hashlib.sha256(r.stdout.encode()).hexdigest(),'stderr':r.stderr,'observed_accepted':r.returncode==0})
   print(mode,name,r.returncode,flush=True)
result={'schema':'riemann-final-review-original-mw-parser-probe-v1','source_git_blob':'3d1e3b10135a8504a5d3639b507211014be7eecc','boundary':'The producer recomputes its mathematics. Python structural equality is not a strict typed or duplicate-key receipt contract. No numerical theorem is refuted by the alias acceptances.','observations':rows}
(ROOT/'evidence/mw-original-parser.json').write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
expected={'pristine':0,'float_event_count_boolean_checkpoint':0,'duplicate_key_last_wins':0,'changed_numerical_endpoint':2}
if any(r['returncode']!=expected[r['case']] for r in rows):raise RuntimeError('unexpected parser behavior')
