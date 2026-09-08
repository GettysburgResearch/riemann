#!/usr/bin/env python3
"""Deliberately corrupt records/sources; require fail-closed rejection in both modes."""
from __future__ import annotations
import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parent

def main():
    original=json.loads((ROOT/'result.json').read_text())
    def boolean(d): d['rh_proved']=True
    def type_alias(d): d['checks']=float(d['checks'])
    def matrix(d):d['counterfeit']['determinant']='2/15625'
    def dimension(d):d['thermal_parameters'][0]['dimension']+=1
    def deletion(d):del d['groups']['finite_pair_inertia']
    cases={'rh_flag':boolean,'numeric_type_alias':type_alias,'determinant_sign':matrix,
           'dimension':dimension,'missing_group':deletion}
    receipts=[]
    with tempfile.TemporaryDirectory(prefix='astra_hankel_refusal_') as temp:
        root=Path(temp)
        for mode in [[],['-O']]:
            for label,change in cases.items():
                d=copy.deepcopy(original);change(d)
                test=root/'bad.json';test.write_text(json.dumps(d))
                p=subprocess.run([sys.executable,*mode,str(ROOT/'verify.py'),'--check',str(test)],capture_output=True,text=True)
                if p.returncode==0 or 'REFUSED:' not in p.stderr:
                    raise RuntimeError('did not explicitly reject '+label)
                receipts.append({'case':label,'mode':'optimized' if mode else 'normal','exit':p.returncode})
            for label in ['changed_proof','changed_parent']:
                testroot=root/('copy_'+label+str(len(mode)))
                testroot.mkdir()
                for name in ['verify.py','PROOF.md','CROSS_REVIEW.md','SOURCE_LOCK.json','result.json']:
                    shutil.copy2(ROOT/name,testroot/name)
                if label=='changed_proof':
                    pth=testroot/'PROOF.md';pth.write_text(pth.read_text().replace('3^(-k)','2^(-k)',1))
                else:
                    pth=testroot/'SOURCE_LOCK.json';d=json.loads(pth.read_text());d['own_parent']='0'*40;pth.write_text(json.dumps(d))
                p=subprocess.run([sys.executable,*mode,str(testroot/'verify.py'),'--check',str(testroot/'result.json')],capture_output=True,text=True)
                if p.returncode==0:raise RuntimeError('accepted '+label)
                receipts.append({'case':label,'mode':'optimized' if mode else 'normal','exit':p.returncode})
    print(json.dumps({'status':'PASS_REJECTION_CONTROLS','refusals':receipts,
                      'count':len(receipts),'rh_proved':False},indent=2,sort_keys=True))

if __name__=='__main__':main()
