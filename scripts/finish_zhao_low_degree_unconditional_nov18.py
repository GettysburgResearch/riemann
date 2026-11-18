"""Finish an unconditional cubic or quartic Euler screen using certified full-field contours."""
import argparse
import io
import json
from math import gcd
from pathlib import Path
from flint import ctx,dirichlet_char
from check_zhao_low_degree_unconditional_nov18 import verify_caps
from check_zhao_quartic_fields_nov18 import polynomial
from check_zhao_cubic_fields_nov18 import run_gp
from check_zhao_field_threshold_nov18 import process
from check_zhao_dedekind_contour_nov18 import weight


def canonical_rows(rows):
    out=[]
    for start in range(0,len(rows),128):
        chunk=rows[start:start+128]
        v=','.join(polynomial(c) for _,_,c in chunk)
        polys=run_gp(f'V=[{v}];\nfor(i=1,#V,print(Vec(polredabs(V[i]))));\n')
        if len(polys)!=len(chunk):
            raise ArithmeticError("Incomplete canonicalization")
        out.extend([r,d,c] for (r,d,_),c in zip(chunk,polys))
    return sorted(out)


def check_match(report,n):
    src=Path(__file__).resolve().parents[1]/"research"/"explorations"
    abelian=json.loads((src/"zhao-abelian-fields-nov18.json").read_text())["fields"]
    prior=[]
    for row in abelian:
        if row["degree"]!=n: continue
        q=row["conductor"]
        chars=[dirichlet_char(a,b) for a,b in row["characters"]]
        ker=[u for u in range(1,q) if gcd(u,q)==1 and all(int(ch.chi_exponent(u))==0 for ch in chars)]
        (coeff,)=run_gp(f'print(Vec(polredabs(galoissubcyclo({q},{ker}))));\n')
        r=0 if row["totally_real"] else n//2
        prior.append([r,(-1)**r*row["abs_discriminant"],coeff])
    if n==3:
        independent=json.loads((src/"zhao-cubic-fields-nov18.json").read_text())
        prior+=canonical_rows([[int(d<0),d,c] for d,c in independent["accepted"]])
    else:
        independent=json.loads((src/"zhao-quartic-fields-nov18.json").read_text())
        prior+=[v for group in independent.values() for v in group["accepted"]]
    actual=canonical_rows(report["accepted"])
    if actual!=sorted(prior):
        raise ArithmeticError("Unconditional and spectral field inventories differ")
    report["accepted"]=actual
    return report


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
    report=check_match(finish(json.loads(args.input.read_text()),args.degree),args.degree)
    args.output.write_text(json.dumps(report,separators=(',',':'))+'\n')
