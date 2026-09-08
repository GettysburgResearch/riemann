#!/usr/bin/env python3
"""Exercise real SSQ26 command-line acceptance paths on pristine and altered copies."""
from pathlib import Path
import argparse
import json
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).absolute().parent

def run_cmd(mode, cwd, script, *args):
    cmd=[sys.executable,'-I','-S','-B']+(['-O'] if mode else [])+[script,*args]
    return subprocess.run(cmd,cwd=cwd,text=True,stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,timeout=40)

def need(ok, message):
    if not ok:
        raise RuntimeError(message)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--optimized',action='store_true')
    opt=ap.parse_args().optimized
    result=json.loads((ROOT/'result.json').read_text())
    result_cases=[]; package_cases=[]
    with tempfile.TemporaryDirectory(prefix='ssq26-controls-') as td:
        td=Path(td)
        pristine=td/'pristine'; shutil.copytree(ROOT,pristine)
        need(run_cmd(opt,pristine,'validate.py').returncode==0,'pristine bytes rejected')
        need(run_cmd(opt,pristine,'check.py','--check','result.json').returncode==0,
             'pristine mathematics rejected')
        def changed_result(name, mutator=None, duplicate=False):
            d=json.loads(json.dumps(result))
            if mutator:
                mutator(d)
            text=json.dumps(d)
            if duplicate:
                text=text[:-1]+', "rh_proved": false}'
            p=td/(name+'.json');p.write_text(text)
            got=run_cmd(opt,ROOT,'check.py','--check',str(p))
            need(got.returncode!=0,name+' unexpectedly accepted')
            result_cases.append(name)
        changed_result('false_RH',lambda d:d.__setitem__('rh_proved',True))
        changed_result('false_global_tail',lambda d:d.__setitem__('global_coarse_tail_certified',True))
        changed_result('float_alias',lambda d:d['groups'][0].__setitem__('cases',7.0))
        changed_result('missing_prefix',lambda d:d['prefixes'].pop())
        changed_result('wrong_directed_endpoint',lambda d:d['prefixes'][-1]['sample_energy'].__setitem__('hi','0'))
        changed_result('duplicate_JSON',duplicate=True)
        def altered_package(name, mutator):
            p=td/name;shutil.copytree(ROOT,p);mutator(p)
            got=run_cmd(opt,p,'validate.py')
            need(got.returncode!=0,name+' unexpectedly accepted')
            package_cases.append(name)
        altered_package('changed_proof',lambda p:(p/'PROOF.md').write_text((p/'PROOF.md').read_text()+'\nchanged\n'))
        altered_package('missing_file',lambda p:(p/'CLAIMS.json').unlink())
        altered_package('extra_file',lambda p:(p/'extra.txt').write_text('extra'))
        def replace_with_link(p):
            (p/'PROOF.md').unlink();(p/'PROOF.md').symlink_to(ROOT/'PROOF.md')
        altered_package('symlink_payload',replace_with_link)
    print(json.dumps({'schema':'SSQ26-rejection-controls-v1',
          'pristine_controls':2,'altered_result_refusals':result_cases,
          'altered_package_refusals':package_cases},sort_keys=True,indent=2))

if __name__=='__main__':
    main()
