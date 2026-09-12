"""Resealed executable-mutation tests, each through the full verifier CLI.

Copies the packet to temporary directories, mutates one producer expression,
regenerates hashes, and requires rejection AFTER authentication. No repository
file is modified. These two cases complement verify.py's receipt/parser tests.
"""
import argparse
import hashlib
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parent

def seal(path):
    files=sorted(p for p in path.iterdir() if p.name!='SHA256SUMS')
    (path/'SHA256SUMS').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n' for p in files))


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--optimized',action='store_true');p.add_argument('--case',choices=('native-theta-coefficient','star-bias-rule'));a=p.parse_args()
    changes=(
        ('native-theta-coefficient','native_source.py','p=4*PI*PI*(n**4);q=6*PI*(n*n)','p=5*PI*PI*(n**4);q=6*PI*(n*n)'),
        ('star-bias-rule','star.py','poly(C[k],a/100)','poly(C[k],a/101)'),
    )
    if a.case:changes=tuple(x for x in changes if x[0]==a.case)
    for name,filename,old,new in changes:
        with tempfile.TemporaryDirectory(prefix='star26-mutation-') as temp:
            dest=Path(temp)/'packet';shutil.copytree(ROOT,dest)
            target=dest/filename;text=target.read_text()
            if text.count(old)!=1:raise RuntimeError('mutation locator is not unique')
            target.write_text(text.replace(old,new));seal(dest)
            cmd=[sys.executable,'-S','-B']+(['-O'] if a.optimized else [])+['verify.py','--check','result.json']
            run=subprocess.run(cmd,cwd=dest,text=True,capture_output=True,timeout=180)
            if run.returncode==0 or 'authenticated payloads:' not in run.stdout:
                raise RuntimeError('mutation not rejected after successful authentication: '+name)
            if 'root contraction failed' not in run.stderr:
                raise RuntimeError('unexpected mutation failure: '+name+'\n'+run.stderr)
            print(name+': REJECTED AFTER RESEALED AUTHENTICATION',flush=True)
            print(run.stderr.strip().splitlines()[-1],flush=True)
    print(str(len(changes))+' complete executable-mutation CLI refusals; mode='+('optimized' if a.optimized else 'normal'))

if __name__=='__main__':main()
