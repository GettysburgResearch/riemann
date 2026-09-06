#!/usr/bin/env python3
"""Run actual checker/validator subprocess refusals; bounded resource contract."""
import argparse,copy,json,subprocess,sys,tempfile,shutil
from pathlib import Path

def run(mode,part):
    root=Path(__file__).resolve().parent
    flags=['-O'] if mode=='optimized' else []
    records=[]
    def call(script,args,cwd):
        p=subprocess.run([sys.executable,*flags,str(script),*args],cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,timeout=40)
        if p.returncode==0:raise ValueError('mutant was accepted')
        return p.returncode
    with tempfile.TemporaryDirectory() as td:
        td=Path(td)
        baseline=json.loads((root/'checks.json').read_text())
        variants=[]
        x=copy.deepcopy(baseline);x['fixtures']+=1;variants.append(('fixtures',x))
        x=copy.deepcopy(baseline);x['checks'].pop();variants.append(('missing_control',x))
        x=copy.deepcopy(baseline);x['checks'][0]['status']='FAIL';variants.append(('changed_verdict',x))
        x=copy.deepcopy(baseline);x['arithmetic']='DIRECTED_FLOAT';variants.append(('false_arithmetic',x))
        for name,x in (variants if part=='controls' else []):
            p=td/'mutant.json';p.write_text(json.dumps(x,sort_keys=True,indent=2)+'\n')
            code=call(root/'checks.py',['--compare',str(p)],root)
            records.append({'mutation':name,'checker':'checks.py','exit':code,'rejected':True})
        baseline=json.loads((root/'certificate.json').read_text())
        for name in ([part] if part in ('tail_removed','wrong_source_error') else []):
            x=copy.deepcopy(baseline)
            if name=='tail_removed':x['rows'][0]['complete_infinite_tail']=False
            else:x['rows'][6]['normalized_error_squared']['hi']='0'
            p=td/'mutant.json';p.write_text(json.dumps(x,sort_keys=True,indent=2)+'\n')
            code=call(root/'certificate.py',['--compare',str(p)],root)
            records.append({'mutation':name,'checker':'certificate.py','exit':code,'rejected':True})
        for name in (('source_changed','file_missing') if part=='package' else []):
            dest=td/name;shutil.copytree(root,dest,ignore=shutil.ignore_patterns('__pycache__'))
            if name=='source_changed':
                p=dest/'certificate.py';p.write_text(p.read_text()+'\n# alteration\n')
            else:(dest/'PROOF.md').unlink()
            code=call(dest/'validate.py',[],dest)
            records.append({'mutation':name,'checker':'validate.py','exit':code,'rejected':True})
    return {'mode':mode,'part':part,'subprocess_refusals':len(records),'records':records,
            'scope':'Altered record/source rejection; not a mathematical proof of infinite claims.'}

def main():
    p=argparse.ArgumentParser();p.add_argument('--mode',choices=['normal','optimized'],required=True);p.add_argument('--part',choices=['controls','tail_removed','wrong_source_error','package'],required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    a.output.write_text(json.dumps(run(a.mode,a.part),sort_keys=True,indent=2)+'\n')
if __name__=='__main__':main()
