#!/usr/bin/env python3
"""Authenticate payloads, rerun full directed evidence, and reject actual mutations."""
import hashlib,json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
MUTATIONS=['erase-normalizer','wrong-edge-sign','erase-edge','drop-moment20','erase-compensation']

def need(ok,msg):
 if not ok:raise ValueError(msg)

def main():
 data=json.loads((ROOT/'MANIFEST.json').read_text())
 for name,entry in data.items():
  b=(ROOT/name).read_bytes()
  need(len(b)==entry['bytes'] and hashlib.sha256(b).hexdigest()==entry['sha256'],'payload '+name)
 checks=[]
 for script,receipt in [('verify.py','CHECKS.json'),('controls.py','CONTROLS.json')]:
  expected=(ROOT/receipt).read_bytes()
  for mode in [[],['-O']]:
   p=subprocess.run([sys.executable,*mode,str(ROOT/script)],cwd=ROOT,capture_output=True)
   need(p.returncode==0,p.stderr.decode())
   need(p.stdout==expected,'replay mismatch '+script+str(mode))
   checks.append({'script':script,'optimized':bool(mode),'matched':True})
 mutations=[]
 for name in MUTATIONS:
  p=subprocess.run([sys.executable,'-O',str(ROOT/'controls.py'),name],cwd=ROOT,capture_output=True)
  expected='compensated derivative toy identity' if name=='erase-compensation' else 'raw moment'
  need(p.returncode!=0 and expected in p.stderr.decode(),'mutation not rejected at intended gate '+name)
  mutations.append({'mutation':name,'rejected':True,'gate':expected})
 out={'manifested_payloads':len(data),'accepting_runs':checks,'mutations':mutations,'status':'PASS'}
 print(json.dumps(out,sort_keys=True,indent=2))
if __name__=='__main__':main()
