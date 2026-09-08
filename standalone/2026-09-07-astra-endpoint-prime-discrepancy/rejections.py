#!/usr/bin/env python3
"""Actual CLI mutation tests; no success is inferred from internal flags."""
from pathlib import Path
import json
import argparse
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parent

def call(mode,script,*args):
    cmd=[sys.executable]+(['-O'] if mode=='optimized' else [])+[str(script),*map(str,args)]
    return subprocess.run(cmd,capture_output=True,text=True,timeout=20).returncode

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--mode',choices=('normal','optimized','both'),default='both')
    args=parser.parse_args()
    modes=('normal','optimized') if args.mode=='both' else (args.mode,)
    rows=[]
    for mode in modes:
        if call(mode,ROOT/'validate.py')!=0: raise ValueError('pristine byte validation failed')
        if call(mode,ROOT/'checks.py','--expect',ROOT/'checks.normal.json')!=0:
            raise ValueError('pristine exact checker failed')
        original=(ROOT/'checks.normal.json').read_text()
        mutations={
          'rh_flag':original.replace('"rh_proved": false','"rh_proved": true'),
          'count':original.replace('"total_cases": 115','"total_cases": 116'),
          'float_alias':original.replace('"total_cases": 115','"total_cases": 115.0'),
          'duplicate_key':original[:-2]+',"status":"PASS_BOUNDED_EXACT_CONTROLS"}\n'}
        with tempfile.TemporaryDirectory() as td:
            temp=Path(td)
            for name,text in mutations.items():
                f=temp/(name+'.json');f.write_text(text)
                rc=call(mode,ROOT/'checks.py','--expect',f)
                if rc==0: raise ValueError('accepted result mutation '+name)
                rows.append({'mode':mode,'kind':'result','name':name,'exit_code':rc})
            for name in ('changed_proof','extra_file','missing_member','symlink'):
                dest=temp/name;shutil.copytree(ROOT,dest)
                if name=='changed_proof':
                    with (dest/'PROOF.md').open('a') as f: f.write('\nchanged\n')
                elif name=='extra_file': (dest/'extra.txt').write_text('unexpected')
                elif name=='missing_member': (dest/'EDGES.tsv').unlink()
                else:
                    p=dest/'README.md';p.unlink();p.symlink_to(ROOT/'README.md')
                rc=call(mode,dest/'validate.py')
                if rc==0: raise ValueError('accepted packet mutation '+name)
                rows.append({'mode':mode,'kind':'packet','name':name,'exit_code':rc})
    print(json.dumps({'pristine_controls':2*len(modes),'rejections':rows,'total_refusals':len(rows)},indent=2,sort_keys=True))

if __name__=='__main__':
    try: main()
    except Exception as exc:
        print('REJECT: '+str(exc),file=sys.stderr)
        sys.exit(1)
