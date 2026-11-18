"""Unconditional cubic/quartic B*=2 Xi'(1)/Xi(1) sieve and contour classifier."""
import argparse
from functools import cache
import json
from pathlib import Path
from flint import acb,arb,arb_series,ctx
from check_zhao_quartic_fields_nov18 import local_rows, primes_through
from check_zhao_quartic_tables_nov18 import SOURCE
from check_zhao_cubic_fields_nov18 import list_fields

SCALE=2**28
S_VALUES=[(11,10),(6,5),(4,3),(3,2),(7,4),(2,1),(5,2)]


def lower_int(x):
    return int((x*SCALE).lower().floor().unique_fmpz())


@cache
def dlog(d):
    return lower_int(arb(abs(d)).log()/2)


@cache
def base(n,r,snum,sden,P):
    T=arb(P).log()
    s=arb(snum)/sden
    return lower_int(1/s+1/(s-1)-(1/s**2+1/(s-1)**2)/T
        -n*arb.pi().log()/2+((n-r)*(s/2).digamma()+r*((s+1)/2).digamma())/2
        +((n-r)*acb(s/2).polygamma(1).real+r*acb((s+1)/2).polygamma(1).real)/(4*T)
        -2*(s-arb(1)/2+1/T))


@cache
def local(P,p,code,snum,sden):
    s=arb(snum)/sden
    T=arb(P).log()
    h=arb(p).log()
    total=arb(0)
    for f in range(1,5):
        count=(code//10**(f-1))%10
        if count:
            z=(f*s*h).exp()
            total+=count*f*h*(-1/(z-1)+(f*h/T)*z/(z-1)**2)
    return lower_int(total)


@cache
def worst_local(P,p,n,a,b):
    # Valid for every splitting at a missing index prime: at most n/f
    # ideals of each degree f, with total residue degree at most n.
    return n*min(0,*(local(P,p,10**(f-1),a,b)//f for f in range(1,n+1)))


def classify(rows,limits,coarse=False):
    initial=len(rows)
    stages=[]
    for P in limits:
        pp=primes_through(P)
        rem=[]
        for (r,d,c),codes in local_rows(rows,P,allow_unknown=coarse):
            n=len(c)-1
            if not any(dlog(d)+base(n,r,a,b,P)+sum(local(P,p,code,a,b) if code else worst_local(P,p,n,a,b) for p,code in zip(pp,codes))>0 for a,b in S_VALUES):
                rem.append([r,d,c])
        stages.append([P,len(rows)-len(rem),len(rem)])
        print('unconditional Euler',P,*stages[-1][1:],flush=True)
        rows=rem
        local.cache_clear()
    return {'enumerated':initial,'stages':stages,'unresolved':rows}


def verify_caps(n):
    sig={3:[(109,50,96900),(17,8,55200)],
         4:[(5,2,861000),(61,25,533000),(12,5,326000)]}
    for r,(a,b,bound) in enumerate(sig[n]):
        s=arb(a)/b
        jet=arb_series([s,1],prec=2).zeta()
        zlog=jet[1]/jet[0]
        upper=(4*(s-arb(1)/2)-2/s-2/(s-1)+n*arb.pi().log()
               -(n-r)*(s/2).digamma()-r*((s+1)/2).digamma()-2*n*zlog).exp()
        if not upper<bound:
            raise ArithmeticError(f"Unconditional discriminant bound fails at {n},{r}: {upper}")


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--degree',type=int,choices=[3,4],required=True)
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--table-dir',type=Path)
    ap.add_argument('--coarse',action='store_true',help='Use a certified worst-case bound at index primes')
    ap.add_argument('--limits',nargs='+',type=int,default=[8,32,128,512])
    args=ap.parse_args()
    ctx.prec=96
    verify_caps(args.degree)
    if args.degree==3:
        rows=[[int(d<0),d,c] for d,c in list_fields()]
    else:
        import hashlib
        caps=[861000,533000,326000]
        rows=[]
        for r,(filename,nrows,sha) in SOURCE.items():
            data=(args.table_dir/filename).read_bytes()
            if hashlib.sha256(data).hexdigest()!=sha:
                raise ArithmeticError('Unexpected table checksum')
            for line in data.splitlines():
                d,c,_,_=json.loads(line)
                if abs(d)<=caps[r]:
                    rows.append([r,d,c])
    report=classify(rows,args.limits,args.coarse)
    report['coarse_index_primes']=args.coarse
    args.output.write_text(json.dumps(report,separators=(',',':'))+'\n')
