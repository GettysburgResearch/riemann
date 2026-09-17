#!/usr/bin/env python3
"""Bounded exact algebra and actual search/parser refusals.
Run after verify.py --keep-dir WORK. Not an independent all-box proof.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse, importlib.util, json, subprocess, tempfile
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('local_verify',ROOT/'verify.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
def need(x,message):
    if not x:raise RuntimeError(message)
def psi(x):return (x-1)**2 if x<=2 else 2*x-3

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--work-dir',type=Path,required=True);a=ap.parse_args()
    v.authenticate();counts={}
    ncases=0
    for n in [7,8,9,16,31,64,308]:
        pairs={(i,j):F(((i+1)*(j+3))%23,29) for i in range(n) for j in range(i+1,n)}
        gaps=[F((i*7)%11,13) for i in range(n-1)]
        left=2*sum(pairs.values())+F(6,3433)*sum(gaps)
        right=F(0)
        for first in range(n-6):
            right+=F(1,3433)*sum(gaps[first:first+6])
            for r in range(1,7):
                for j in range(first,first+7-r):right+=F(2,7-r)*pairs[j,j+r]
        need(left>=right,'seven-window coefficient count');ncases+=1
    counts['complete_window_panels']=ncases
    ncases=0
    for n in [2,3,7,31,308]:
        for j in range(0,21):
            r=F(j,20)
            eigen=[1+(n-1)*r]+[1-r]*(n-1)
            E=sum((x-1)**2 for x in eigen);D=sum(psi(x) for x in eigen)
            if E<=F(n,n-1):need(D==E,'quadratic branch')
            elif E<2:
                u=D+1-E/n;need(u>=0 and u*u==4*F(n-1,n)*E,'sharp one-large-mode identity')
            else:need(D+1>=0 and (D+1)**2>=8,'large-energy floor')
            ncases+=1
    counts['trace_spectral_panels']=ncases
    parser=0
    for s in ['{"x":1,"x":2}','{"x":NaN}','{"x":Infinity}']:
        try:v.strict_load(s)
        except ValueError:parser+=1
        else:raise RuntimeError('malformed JSON accepted')
    need(not v.same({'a':True},{'a':1}),'Boolean alias accepted');parser+=1
    need(not v.same({'a':1.0},{'a':1}),'float alias accepted');parser+=1
    counts['strict_parser_comparison_controls']=parser
    search=a.work_dir/'search';table=a.work_dir/'kernel.txt'
    # The independent rational witness in rational_audit.py refutes this target.
    bad=subprocess.run([str(search),str(table),'13778','4000000','3433'],capture_output=True,text=True)
    need(bad.returncode==1 and 'UNRESOLVED' in bad.stderr,'false higher target not refused')
    counts['actual_false_global_target_refusal']=1
    with tempfile.TemporaryDirectory(prefix='spl26-controls-') as td:
        f=Path(td)/'broken.txt';f.write_text('MPFR_KERNEL_V1 4000 48016 160\n')
        bad=subprocess.run([str(search),str(f),'13777','4000000','3433'],capture_output=True,text=True)
        need(bad.returncode==2 and 'truncated table' in bad.stderr,'truncated table not refused')
    counts['actual_truncated_table_refusal']=1
    bad=subprocess.run([str(search),str(table),'13777x','4000000','3433'],capture_output=True,text=True)
    need(bad.returncode==2 and 'bad integer argument' in bad.stderr,'integer suffix not refused')
    counts['actual_malformed_parameter_refusal']=1
    print(json.dumps({'passed':True,'coverage':counts},sort_keys=True))
if __name__=='__main__':main()
