#!/usr/bin/env python3
"""Exact bounded controls for NGR26. Not a machine proof of RH or the analysis."""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import argparse
import hashlib
import json
import sys

PARENT = '459c3f78b3dc8c95ae6cc7b1bec0154499d76c9f'
NUM = [562949953421312,-562949953421312,-532205406349296,
 -58291156654044,-441882648513420,328445548501212,-366102615428543,
 18872698772432,-57317966477307,250457476590930,-252425357406167,
 20023818681228,-248939343231540,204789481170078,157840018622805,-149164455120992]
DEN = 562949953421312

def need(ok, message):
    if not ok:
        raise ValueError(message)

def trim(p):
    p = list(p)
    while len(p)>1 and not p[-1]: p.pop()
    return p

def add(p,q):
    r=[F(0)]*max(len(p),len(q))
    for i,v in enumerate(p): r[i]+=v
    for i,v in enumerate(q): r[i]+=v
    return trim(r)

def scale(p,a): return trim([a*x for x in p])

def mul(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): r[i+j]+=a*b
    return trim(r)

def ev(p,x):
    v=F(0)
    for a in reversed(p): v=v*x+a
    return v

def deriv(p): return trim([i*p[i] for i in range(1,len(p))] or [F(0)])

def s_add(a,b,sgn=1):
    out=dict(a)
    for n,p in b.items(): out[n]=add(out.get(n,[F(0)]),scale(p,F(sgn)))
    return {n:p for n,p in out.items() if p!=[0]}

def conv(a,b,N):
    out={}
    for i,p in a.items():
        for j,q in b.items():
            if i*j<=N: out[i*j]=add(out.get(i*j,[F(0)]),mul(p,q))
    return {n:p for n,p in out.items() if p!=[0]}

def slow_conv(a,b,N):
    out={}
    for n in range(1,N+1):
        v=[F(0)]
        for d in range(1,n+1):
            if n%d==0 and d in a and n//d in b: v=add(v,mul(a[d],b[n//d]))
        if v!=[0]: out[n]=v
    return out

def seeds():
    base={n:[F(a,DEN)] for n,a in enumerate(NUM,1)}
    for n,v in [(3,6),(6,-18),(12,12)]: base[n]=add(base[n],[F(0),F(v)])
    bank=[base]
    for r in [2,3]:
        b={n:list(v) for n,v in base.items()}
        for k,v in enumerate([1,-(2*r+1),r*r+2*r,-r*r]):
            n=3*r**k
            b[n]=add(b.get(n,[F(0)]),[F(v,65536)])
        bank.append(b)
    return bank

def gamma_coeff(D,k):
    p=[F(0)]*D
    for j in range(k):
        r=D-k+j
        p[r]+=F(D**D*comb(k-1,j),factorial(r))*(F(1,2)-D)**j
    return trim(p)

def laplace_poly(p,rate):
    return sum((a*factorial(i)/rate**(i+1) for i,a in enumerate(p)),F(0))

def inverse(A):
    n=len(A); a=[list(row)+[F(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if a[i][j]),None)
        need(pivot is not None,'singular matrix')
        a[j],a[pivot]=a[pivot],a[j]
        d=a[j][j]; a[j]=[x/d for x in a[j]]
        for i in range(n):
            if i!=j:
                d=a[i][j]; a[i]=[x-d*y for x,y in zip(a[i],a[j])]
    return [r[n:] for r in a]

def quad(A,x): return sum((x[i]*A[i][j]*x[j] for i in range(len(x)) for j in range(len(x))),F(0))

def rat(x): return f'{x.numerator}/{x.denominator}'

def reconstruct():
    counts={}; records={}
    # Exact gamma moments and signed proper-kernel transform/majorants.
    count=0
    for D in range(1,13):
        mass=F(D**D*factorial(D-1),factorial(D-1)*D**D)
        mean=F(D**D*factorial(D),factorial(D-1)*D**(D+1))
        second=F(D**D*factorial(D+1),factorial(D-1)*D**(D+2))
        need(mass==mean==1 and second-mean*mean==F(1,D),'gamma moments'); count+=1
    counts['gamma_moment_cases']=count
    count=0
    for D in range(1,13):
        for k in range(1,D+1):
            p=gamma_coeff(D,k)
            for z in [F(0),F(1,7),F(3,2),F(4)]:
                need(laplace_poly(p,D+z)==(F(D)/(D+z))**D*(z+F(1,2))**(k-1),'proper kernel transform')
                count+=1
            need(laplace_poly([abs(x) for x in p],F(D))==(2*D-F(1,2))**(k-1),'kernel L1 majorant')
            C=F(2**(k-1)*D**D)/(D-F(1,2))**(D-k+1)
            need(laplace_poly([abs(x) for x in p],D-F(1,2))==C,'weighted kernel majorant')
    counts['rational_transform_cases']=count
    counts['pairs_of_kernel_majorants']=sum(range(1,13))
    # Complete exact target norms for declared gamma targets, not native energies.
    norms=[]
    for D in range(1,13):
        c=D-F(1,2); a=(F(D)/c)**D
        poly=[c**j/F(factorial(j)) for j in range(D)]
        norm=a*a*(1-2*laplace_poly(poly,D+F(1,2))+laplace_poly(mul(poly,poly),2*D))
        need(0<norm<1,'target norm range')
        norms.append(rat(norm))
    need(norms[0]=='2/3','D1 target norm')
    records['target_squared_norms_D1_to_D12']=norms
    counts['target_norm_cases']=len(norms)
    # Keep the exact seed correction as a FORMAL variable, not an evaluated log.
    bank=seeds(); N=128
    for p in bank:
        total=[F(0)]; balance=[F(0)]
        for n,a in p.items(): total=add(total,a); balance=add(balance,scale(a,F(1,n)))
        need(total==[-2] and balance==[0] and p[1]==[1] and p[2]==[-1],'seed source data')
    fs=[]
    for p in bank:
        b={}
        for n in range(1,N+1):
            v=[F(int(n==1))]
            for d,a in p.items():
                if n%d==0: v=add(v,scale(a,F(-1)))
            # Independent step-difference reconstruction.
            step=[F(int(n==1))]
            for d,a in p.items(): step=add(step,scale(a,F(-(n//d-(n-1)//d))))
            need(v==step,'floor difference')
            if v!=[0]: b[n]=v
        need(all(n>=3 for n in b),'native starting index'); fs.append(b)
    counts['formal_seed_balance_cases']=3
    counts['formal_floor_increment_cases']=3*N
    unit={1:[F(1)]}; panels=0; hist=[]
    for m in range(1,5):
        local=0
        for a in range(m+1):
            for b in range(m-a+1):
                orders=[0]*a+[1]*b+[2]*(m-a-b)
                prod=unit; telescope={}
                for j in orders:
                    telescope=s_add(telescope,conv(prod,s_add(unit,fs[j],-1),N))
                    nextp=conv(prod,fs[j],N)
                    need(nextp==slow_conv(prod,fs[j],N),'independent Dirichlet convolution')
                    prod=nextp
                need(s_add(unit,prod,-1)==telescope,'source telescope')
                need(all(n>=3**m for n in prod),'feedback horizon')
                panels+=1; local+=1
        hist.append(local)
    counts['full_truncated_feedback_panels']=panels
    records['panels_by_degree_1_to_4']=hist
    records['dirichlet_cutoff']=N
    records['seed_log_correction']='formal variable; exact value not numerically evaluated'
    # Exact full-tail antiderivative coefficients; the factor exp(-T) is symbolic.
    for D in range(1,13):
        W=[F(0)]*D
        for k in range(1,D+1):
            C=F(2**(k-1)*D**D)/(D-F(1,2))**(D-k+1)
            W[k-1]=C*F(3**k,factorial(k-1))
        sq=mul(W,W)
        tail=[sum((sq[r]*factorial(r)/F(factorial(j)) for r in range(j,len(sq))),F(0)) for j in range(len(sq))]
        need(add(tail,scale(deriv(tail),F(-1)))==sq,'full tail derivative')
    counts['complete_polynomial_tail_cases']=12
    # Synthetic finite rank-deficient Grams: verify ridge, not any actual optimum.
    for m in range(1,9):
        C=[[F(1),F(2),F(-1)],[F(0),F(1),F(1)]]
        G=[[sum((row[i]*row[j] for row in C),F(0)) for j in range(3)] for i in range(3)]
        lam=F(1,2**(m*m)); A=[[G[i][j]+lam*(i==j) for j in range(3)] for i in range(3)]
        Ai=inverse(A); v=[sum(row,F(0)) for row in Ai]; denom=sum(v,F(0)); x=[r/denom for r in v]
        need(sum(x,F(0))==1 and quad(A,x)==1/denom,'ridge stationarity')
        for eta in [[F(1),F(-1),F(0)],[F(2),F(1),F(-3)]]:
            need(quad(A,[u+v for u,v in zip(x,eta)])-quad(A,x)==quad(A,eta),'ridge complete square')
    counts['synthetic_ridge_cases']=8
    return {'schema':'NGR26-exact-controls-v1','parent':PARENT,
            'status':'component-proofs-proposed; RH and norm bound unproved',
            'counts':counts,'records':records,
            'actual_high_degree_feedback_energy':'not evaluated',
            'analytic_proofs':'not machine verified'}

def pairs_hook(items):
    out={}
    for k,v in items:
        need(k not in out,'duplicate JSON key'); out[k]=v
    return out

def bad_float(_): raise ValueError('noninteger JSON number')

def check_types(x):
    need(type(x) is not bool,'Boolean alias')
    if isinstance(x,dict):
        for k,v in x.items(): need(type(k) is str,'key type'); check_types(v)
    elif isinstance(x,list):
        for v in x: check_types(v)
    else: need(type(x) in (str,int) or x is None,'JSON type')

def read_json(path):
    x=json.loads(path.read_text(),object_pairs_hook=pairs_hook,parse_float=bad_float,parse_constant=bad_float)
    check_types(x); return x

def inventory(root):
    manifest=root/'SHA256SUMS'
    need(manifest.is_file() and not manifest.is_symlink(),'missing manifest')
    expected={}
    for line in manifest.read_text().splitlines():
        h,sep,name=line.partition('  ')
        need(sep and len(h)==64 and '/' not in name and name not in expected and name!='SHA256SUMS','manifest entry')
        expected[name]=h
    need(expected,'empty manifest')
    actual={p.name for p in root.iterdir()}
    need(actual==set(expected)|{'SHA256SUMS'},'inventory mismatch')
    for name,h in expected.items():
        p=root/name
        need(p.is_file() and not p.is_symlink(),'not regular file')
        need(hashlib.sha256(p.read_bytes()).hexdigest()==h,'hash mismatch: '+name)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--check',type=Path); ap.add_argument('--emit',type=Path)
    args=ap.parse_args(); need(bool(args.check)^bool(args.emit),'choose check or emit')
    root=Path(__file__).resolve().parent
    if args.check: inventory(root)
    result=reconstruct()
    if args.emit: args.emit.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    else: need(read_json(args.check)==result,'reconstruction mismatch')
    print(json.dumps({'status':'PASS_BOUNDED_EXACT_CONTROLS','counts':result['counts']},sort_keys=True))

if __name__=='__main__':
    try: main()
    except (ValueError,OSError,KeyError,TypeError) as exc:
        print('REJECT: '+str(exc),file=sys.stderr); sys.exit(2)
