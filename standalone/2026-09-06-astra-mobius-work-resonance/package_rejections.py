#!/usr/bin/env python3
"""Run three real inventory-validation failures per mode.
Write output OUTSIDE this directory to keep its inventory unchanged.
"""
import argparse,json,shutil,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def run():
    rows=[]
    for mode in ('normal','optimized'):
        command=[sys.executable]+(['-O'] if mode=='optimized' else [])
        for name in ('modified_proof','deleted_certificate','extra_file'):
            with tempfile.TemporaryDirectory() as tmp:
                dst=Path(tmp)/'packet'
                shutil.copytree(ROOT,dst,ignore=shutil.ignore_patterns('__pycache__'))
                if name=='modified_proof':
                    p=dst/'RESONANCE.md';p.write_bytes(p.read_bytes()+b'\nCORRUPTION\n')
                elif name=='deleted_certificate':(dst/'certificate.normal.json').unlink()
                else:(dst/'UNDECLARED.txt').write_text('extra\n')
                c=subprocess.run(command+[str(dst/'validate.py')],capture_output=True,text=True,timeout=10)
                if c.returncode!=2:raise RuntimeError(name+' not rejected')
                rows.append({'mode':mode,'mutation':name,'return_code':c.returncode,'stderr':c.stderr.strip()})
    return {'subprocess_refusals':len(rows),'results':rows}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    if a.output.resolve().parent==ROOT:raise SystemExit('output must be outside hashed packet')
    a.output.write_text(json.dumps(run(),sort_keys=True,indent=2)+'\n')
