#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,platform,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parent
src=ROOT/'boost_interval_probe.cpp'; binary=ROOT/'boost_interval_probe'
flags=['-std=c++17','-O2','-DNDEBUG','-frounding-math','-fno-fast-math']
subprocess.run(['g++',*flags,str(src),'-o',str(binary)],check=True)
text=subprocess.check_output([str(binary)],text=True)
records=[]
for line in text.splitlines():
    if not line.startswith('VALUE='): continue
    fields=dict(item.split('=',1) for item in line.split())
    records.append(fields)
assert len(records)==4
# sqrt(2), sqrt(3), sqrt(67), sqrt(166000) are irrational because none is a square.
# A singleton finite binary interval therefore cannot contain the exact square root.
failed=[r for r in records if r['SQRT_LO']==r['SQRT_HI']]
assert len(failed)==4
payload={
  'classification':'FAIL_PR508_BOOST_ROUNDED_TRANSC_STD_INCLUSION_CONTRACT',
  'compiler':subprocess.check_output(['g++','--version'],text=True).splitlines()[0],
  'platform':platform.platform(),
  'compile_flags':flags,
  'records':records,
  'exact_reason':'each tested radicand is a nonsquare integer, so its exact square root is irrational; a singleton finite binary interval cannot contain it',
  'scope':'targeted platform witness for the exact interval policy and flags used by X-93780; no large tail sweep rerun',
}
raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
payload['proof_object_sha256']=hashlib.sha256(raw).hexdigest()
(ROOT/'verification.json').write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
(ROOT/'probe.stdout.txt').write_text(text)
print(payload['classification'])
print(payload['proof_object_sha256'])
