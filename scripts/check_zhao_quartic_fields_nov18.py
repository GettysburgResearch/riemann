"""Enumerate and certify nonabelian quartic Zhao spectral weights."""
import argparse
import json
from functools import cache
from pathlib import Path
from flint import arb, ctx
from check_zhao_cubic_fields_nov18 import run_gp
from check_zhao_field_weight_nov18 import field_terms, prime_term, primes_through

BOUNDS=(759909,450317,266855)
GROUPS=("D4","A4","S4")


def polynomial(c):
    return '+'.join(f'({a})*x^{4-i}' for i,a in enumerate(c))


def list_fields(group,r):
    return run_gp('default(parisize,"256M");\n'
                  f'V=nflist("{group}",[1,{BOUNDS[r]}],{r});\n'
                  f'for(i=1,#V, print([{r},nfdisc(V[i]),Vec(V[i])]));\n')


def verify_coverage():
    g,delta,pole,a0,a1=field_terms(3)
    split=4*sum(prime_term(3,p,1) for p in (2,3))
    for r,bound in enumerate(BOUNDS):
        if not ((2*(1+delta)-pole-(4-r)*a0-r*a1+split)/g).exp() < bound:
            raise ArithmeticError("Quartic discriminant coverage failed")


def local_rows(rows,limit):
    for start in range(0,len(rows),128):
        chunk=rows[start:start+128]
        expr=','.join(polynomial(c) for _,_,c in chunk)
        code=('default(parisize,"128M");\nV=['+expr+'];\n'
              f'P=primes([2,{limit}]);\n'
              'for(i=1,#V,F=V[i];N=nfinit(F);print(vector(#P,j,my(v=idealprimedec(N,P[j]));'
              'sum(l=1,#v,10^(v[l].f-1)))));\n')
        got=run_gp(code)
        if len(got)!=len(chunk):
            raise ArithmeticError("Incomplete PARI batch")
        yield from zip(chunk,got)


@cache
def term(limit,p,code):
    deg=[f for f in range(1,5) for _ in range((code//10**(f-1))%10)]
    if not deg or sum(deg)>4:
        raise ArithmeticError("Bad residue degrees")
    return sum(prime_term(limit,p,f) for f in deg)


def screen(rows,limits,group):
    accepted,stats=[],[]
    size=len(rows)
    for limit in limits:
        nextrows=[]
        g,delta,pole,a0,a1=field_terms(limit)
        pp=primes_through(limit)
        good=bad=0
        for row,codes in local_rows(rows,limit):
            r,d,_=row
            if len(codes)!=len(pp):
                raise ArithmeticError("Partial local row")
            w=g*arb(abs(d)).log()+pole+(4-r)*a0+r*a1
            for p,code in zip(pp,codes):
                w-=term(limit,p,code)
            if w<2*(1-delta):
                accepted.append(row)
                good+=1
            elif w>2*(1+delta):
                bad+=1
            else:
                nextrows.append(row)
        rows=nextrows
        stats.append([limit,good,bad,len(rows)])
        print(group,*stats[-1],flush=True)
        term.cache_clear()
        if not rows: break
    return {"enumerated":size,"stages":stats,"accepted":sorted(accepted),"unresolved":sorted(rows)}


if __name__=="__main__":
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output-dir",type=Path,required=True)
    ap.add_argument("--groups",nargs="+",default=GROUPS,choices=GROUPS)
    ap.add_argument("--limits",nargs="+",type=int,default=[8,32,128,512,2048,8192])
    ap.add_argument("--enumeration-cache",type=Path,help="Optional existing PARI enumeration for a replay")
    args=ap.parse_args()
    ctx.prec=96
    verify_coverage()
    for group in args.groups:
        rows=[]
        for r in range(3):
            if args.enumeration_cache:
                f=args.enumeration_cache/f"quartic-{group}-{r}.jsonl"
                if f.exists():
                    rows.extend(json.loads(line) for line in f.read_text().splitlines())
                elif group!="A4" or r!=1:
                    raise RuntimeError(f"Missing {f}")
            else:
                rows.extend(list_fields(group,r))
        if len({(d,tuple(c)) for _,d,c in rows})!=len(rows):
            raise ArithmeticError("Duplicate quartic record")
        result=screen(rows,args.limits,group)
        (args.output_dir/f"quartic-{group}-screen.json").write_text(json.dumps(result,separators=(',',':'))+'\n')
