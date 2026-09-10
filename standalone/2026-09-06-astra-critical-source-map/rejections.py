#!/usr/bin/env python3
"""Execute actual checker CLIs on corrupted retained records."""
from __future__ import annotations
import argparse, copy, json, subprocess, sys, tempfile
from pathlib import Path
P=Path(__file__).resolve().parent

def run(optimized:bool):
    records=[]
    for script,baseline in [('checks.py','checks.normal.json'),('source_certificate.py','source.normal.json')]:
        data=json.loads((P/baseline).read_text())
        mutations=[]
        d=copy.deepcopy(data);d['RH_proved']=True;mutations.append(('RH promotion',d))
        d=copy.deepcopy(data);d['schema']='wrong';mutations.append(('schema mutation',d))
        d=copy.deepcopy(data)
        if script=='checks.py':d['fixtures']+=1
        else:d['integer_cutoff']=4095
        mutations.append(('coverage mutation',d))
        d=copy.deepcopy(data)
        if script=='checks.py':d['checks']=d['checks'][:-1]
        else:d['norm_squared']['upper_numerator']=d['norm_squared']['lower_numerator']
        mutations.append(('proof record mutation',d))
        with tempfile.TemporaryDirectory(prefix='csm26-reject-') as td:
            for name,bad in mutations:
                f=Path(td)/'mutated.json';f.write_text(json.dumps(bad,sort_keys=True,indent=2)+'\n')
                cmd=[sys.executable,'-B']+(['-O'] if optimized else [])+[str(P/script),'--compare',str(f)]
                p=subprocess.run(cmd,capture_output=True,text=True,timeout=30)
                if p.returncode==0:raise RuntimeError('corruption was accepted: '+name)
                records.append({'script':script,'case':name,'rejected':True,'exit_code':p.returncode})
    return {'optimized':optimized,'rejected':len(records),'records':records}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);args=p.parse_args()
    out={'schema':'csm26.actual-cli-rejections.v1','runs':[run(False),run(True)]}
    text=json.dumps(out,sort_keys=True,indent=2)+'\n'
    if args.output:args.output.write_text(text)
    else:print(text,end='')
