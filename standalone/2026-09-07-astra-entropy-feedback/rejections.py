#!/usr/bin/env python3
"""Run actual check/validation CLIs on corrupted copies in both Python modes."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


def call(cmd, expected):
    p=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=30)
    if (p.returncode==0)!=expected:
        raise RuntimeError('unexpected subprocess result: '+repr(cmd)+p.stderr.decode())


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["normal","optimized","both"], default="both")
    args=parser.parse_args()
    root=Path(__file__).resolve().parent
    original=(root/'checks.normal.json').read_text()
    data=json.loads(original)
    altered=[]
    for key,value in [('RH_proved',True),('work_upper_bound_proved',True),
                      ('RH_proved',0),('covariance_prime_2_3','0')]:
        d=dict(data);d[key]=value;altered.append(json.dumps(d))
    altered.append(original.replace('1119','1119.0',1))
    altered.append(original.replace('{','{"RH_proved": false,',1))
    modes=[]
    with tempfile.TemporaryDirectory() as td:
        tmp=Path(td)
        all_flags={"normal":[[]],"optimized":[["-O"]],"both":[[],["-O"]]}
        for flags in all_flags[args.mode]:
            mode='optimized' if flags else 'normal'
            call([sys.executable,*flags,str(root/'checks.py'),'--check',str(root/'checks.normal.json')],True)
            for i,text in enumerate(altered):
                p=tmp/(mode+str(i)+'.json');p.write_text(text)
                call([sys.executable,*flags,str(root/'checks.py'),'--check',str(p)],False)
            packet_cases=[]
            for kind in ['changed_proof','missing_claims','extra_file']:
                cp=tmp/(mode+'_'+kind);shutil.copytree(root,cp)
                if kind=='changed_proof':
                    with (cp/'PROOF.md').open('a') as f:f.write('\nCORRUPTED\n')
                elif kind=='missing_claims':
                    (cp/'CLAIMS.tsv').unlink()
                else:
                    (cp/'unexpected.txt').write_text('extra')
                call([sys.executable,*flags,str(cp/'validate.py')],False)
                packet_cases.append(kind)
            modes.append({'mode':mode,'pristine_result_control':True,
                          'altered_results_rejected':len(altered),
                          'altered_packets_rejected':packet_cases})
    print(json.dumps({'scope':'bounded rejection tests only','modes':modes},indent=2,sort_keys=True))


if __name__=='__main__':
    main()
