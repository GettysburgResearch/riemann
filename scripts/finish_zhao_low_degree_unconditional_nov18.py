"""Finish an unconditional cubic or quartic Euler screen using certified full-field contours."""
import argparse
import io
import json
from pathlib import Path
from flint import ctx
from check_zhao_low_degree_unconditional_nov18 import verify_caps
from check_zhao_cubic_fields_nov18 import run_gp
from check_zhao_field_threshold_nov18 import process
from check_zhao_dedekind_contour_nov18 import weight


def finish(report,n):
    verify_caps(n)
    rows=report['unresolved']
    if n==3:
        cyclic=run_gp('V=nflist("C3",[1,96900],0);\nfor(i=1,#V,print([0,nfdisc(V[i]),Vec(V[i])]));\n')
        rows+=cyclic
        report['extra_cyclic_cubics']=len(cyclic)
    pending={}
    for j,(r,d,c) in enumerate(rows):
        key=f'{n}.{n-2*r}.{abs(d)}.{j+1}'
        pending[key]={'label':key,'coeffs':list(reversed(c))}
    passed=[]
    checks=[]
    for tol in ('0.03','0.0001','1e-7'):
        if not pending: break
        mem=io.StringIO()
        process(list(pending.values()),tol,mem)
        u=[]
        for line in mem.getvalue().splitlines():
            k,status,ball=json.loads(line)
            if status is None: continue
            if status: passed.append(rows[int(k.split('.')[-1])-1])
            del pending[k]
            u.append([k,status,ball])
        checks.append([tol,len(u),len(pending)])
        print('unconditional contour',n,tol,len(u),len(pending),flush=True)
    for k,item in pending.items():
        w=weight(item,'1e-9')
        if w<2: passed.append(rows[int(k.split('.')[-1])-1])
        elif not w>2: raise ArithmeticError(f'Unresolved field {k}')
    report['accepted']=sorted(passed)
    report['contour_stages']=checks
    report['direct_fallbacks']=len(pending)
    report['unresolved']=[]
    print('unconditional passing',n,len(passed),flush=True)
    return report


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--degree',type=int,choices=[3,4],required=True)
    ap.add_argument('--input',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    ctx.prec=150
    report=finish(json.loads(args.input.read_text()),args.degree)
    args.output.write_text(json.dumps(report,separators=(',',':'))+'\n')
