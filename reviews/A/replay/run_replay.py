#!/usr/bin/env python3
"""Run the reviewer controls and actual CLI rejection tests in both Python modes."""
import hashlib, json, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent
checker=ROOT/'verify_review.py'

def main():
    receipt={'schema':'riemann.review.A.execution.v1','status':'RUNNING','modes':{},'rejections':[],
             'upstream_campaigns_rerun':False,'lean_build':False,'rh_proved':False}
    canonical=None
    for label,opts in [('normal',[]),('optimized',['-O'])]:
        p=subprocess.run([sys.executable,*opts,str(checker)],capture_output=True,text=True,timeout=45)
        if p.returncode:raise RuntimeError(label+' failed: '+p.stderr[-2000:])
        data=json.loads(p.stdout)
        if canonical is None:canonical=p.stdout;(ROOT/'result.json').write_text(canonical)
        if p.stdout!=canonical:raise RuntimeError('normal/optimized outputs differ')
        q=subprocess.run([sys.executable,*opts,str(checker),'--check',str(ROOT/'result.json')],capture_output=True,text=True,timeout=45)
        if q.returncode or q.stdout!=canonical:raise RuntimeError('canonical check failed')
        receipt['modes'][label]={'exit_code':p.returncode,'canonical_check_exit_code':q.returncode,
            'sha256':hashlib.sha256(p.stdout.encode()).hexdigest(),'checks':data['total'],'counts':data['counts']}
        variants={}
        for name in ('wrong_total','float_total','boolean_total','rh_promotion','wrong_baseline'):
            v=json.loads(canonical)
            if name=='wrong_total':v['total']+=1
            elif name=='float_total':v['total']=float(v['total'])
            elif name=='boolean_total':v['total']=True
            elif name=='rh_promotion':v['rh_proved']=True
            else:v['base_sha']='0'*40
            variants[name]=json.dumps(v)
        variants['duplicate_json_key']='{"total":0,'+canonical.lstrip()[1:]
        with tempfile.TemporaryDirectory() as td:
            for name,text in variants.items():
                f=Path(td)/(name+'.json');f.write_text(text)
                z=subprocess.run([sys.executable,*opts,str(checker),'--check',str(f)],capture_output=True,text=True,timeout=45)
                if z.returncode==0:raise RuntimeError('mutation unexpectedly accepted: '+name)
                receipt['rejections'].append({'mode':label,'mutation':name,'exit_code':z.returncode,'rejected':True})
    receipt['status']='PASS';receipt['normal_optimized_byte_identical']=True
    receipt['rejection_count']=len(receipt['rejections'])
    (ROOT/'EXECUTION_RECEIPT.json').write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'PASS','checks_per_mode':json.loads(canonical)['total'],'rejections':len(receipt['rejections']),'upstream_campaigns_rerun':False,'rh_proved':False}))
if __name__=='__main__':main()
