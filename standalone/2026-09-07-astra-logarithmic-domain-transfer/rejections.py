#!/usr/bin/env python3
"""Exercise actual CLIs with corrupt results and packages; does not review math."""
from __future__ import annotations
import argparse,copy,hashlib,json,shutil,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def call(root:Path, optimized:bool, script:str, *args:str)->int:
    cmd=[sys.executable]+(['-O'] if optimized else [])+['-B',script,*args]
    return subprocess.run(cmd,cwd=root,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,
                          timeout=20).returncode

def reseal(root:Path)->None:
    names=[p.name for p in root.iterdir() if p.is_file() and p.name!='SHA256SUMS']
    (root/'SHA256SUMS').write_text(''.join(hashlib.sha256((root/n).read_bytes()).hexdigest()+'  '+n+'\n'
                                        for n in sorted(names)))

def run()->dict:
    result={'result_refusals':[],'package_refusals':[],'pristine_controls':[]}
    for optimized in [False,True]:
        mode='optimized' if optimized else 'normal'
        with tempfile.TemporaryDirectory() as td:
            base=Path(td)/'base';shutil.copytree(ROOT,base,ignore=shutil.ignore_patterns('__pycache__'))
            if call(base,optimized,'validate.py')!=0:
                raise ValueError('pristine package refused')
            result['pristine_controls'].append(mode)
            original=json.loads((base/'checks.normal.json').read_text())
            for name in ['rh_promotion','integer_float_alias','boolean_integer_alias','missing_group','duplicate_key']:
                v=copy.deepcopy(original)
                if name=='rh_promotion':v['rh_proved']=True
                elif name=='integer_float_alias':v['analytic_bound_constants_checked']['X']=2.0
                elif name=='boolean_integer_alias':v['rh_proved']=0
                elif name=='missing_group':v['groups'].pop()
                text=json.dumps(v)
                if name=='duplicate_key':text=text[:-1]+',"rh_proved":false}'
                bad=Path(td)/'bad.json';bad.write_text(text)
                rc=call(base,optimized,'checks.py','--check',str(bad))
                if rc==0:raise ValueError('mutation accepted: '+name)
                result['result_refusals'].append({'mode':mode,'case':name,'exit':rc})
            for name in ['changed_proof','missing_manifest_entry','extra_file','resealed_parent']:
                mutated=Path(td)/name;shutil.copytree(base,mutated)
                if name=='changed_proof':
                    p=mutated/'PROOF.md';p.write_text(p.read_text()+'\nUnbound mutation.\n')
                elif name=='missing_manifest_entry':
                    p=mutated/'SHA256SUMS';p.write_text('\n'.join(p.read_text().splitlines()[1:])+'\n')
                elif name=='extra_file':(mutated/'extra.txt').write_text('unlisted')
                else:
                    p=mutated/'SOURCES.json';s=json.loads(p.read_text());s['remote_baseline_commit']='0'*40
                    p.write_text(json.dumps(s));reseal(mutated)
                rc=call(mutated,optimized,'validate.py')
                if rc==0:raise ValueError('package mutation accepted: '+name)
                result['package_refusals'].append({'mode':mode,'case':name,'exit':rc})
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path);args=parser.parse_args()
    try:
        text=json.dumps(run(),sort_keys=True,indent=2)+'\n'
        if args.output:args.output.write_text(text)
        else:print(text,end='')
    except (ValueError,OSError,subprocess.TimeoutExpired) as exc:
        raise SystemExit('REJECT: '+str(exc))
