"""Unconditional interval test for the sign of 2 xi'_K(1)/xi_K(1) - 2.

Finite Dirichlet coefficients are integrated on Re s=2 using a Taylor table
of an interval Fourier transform. Bound the Dirichlet tail separately on 8.
"""
import argparse
from functools import cache
import json
from pathlib import Path

from flint import acb, arb, ctx
from check_zhao_cubic_fields_nov18 import run_gp

M=8192
J=1024
ORDER=6
PHASE=2**44
SCALE=2**84
RECIP=2**108
H=1/16 # exact dyadic


def floor_mid(x):
    # Always verify the integer approximation itself by a ball comparison.
    v=int(x.mid().floor().unique_fmpz())
    if not abs(x-v)<2:
        raise ArithmeticError("Insufficient fixed-point precision")
    return v


@cache
def coordinates(n):
    return floor_mid(arb(n).log()*M*PHASE/(32*arb.pi()))


@cache
def table(n,r2):
    pi=arb.pi()
    z=[]
    multipliers=[]
    for j in range(J+1):
        w=acb(2,arb(j)/16)
        gamma=(w/2).gamma()**(n-r2)*((w+1)/2).gamma()**r2
        v=gamma*((w-arb(1)/2)**2/36).exp()*(2*w-1)*(1/(w*(w-1))-arb(37)/36)
        z.append(v*(1 if j==0 else 2)/(32*pi))
        multipliers.append(acb(0,-2*pi*j/M))
    # Distance from the exact coordinate, including coordinate rounding.
    eta=arb(1)/2+arb(4)/PHASE
    omitted=sum(abs(v)*(eta*abs(a))**(ORDER+1) for v,a in zip(z,multipliers))
    from math import factorial
    omitted/=factorial(ORDER+1)
    displacement=arb(4)/PHASE*sum(abs(v*a) for v,a in zip(z,multipliers))
    amplitude=sum(abs(v) for v in z)
    polys=[]
    for k in range(ORDER+1):
        transform=acb.dft(z+[acb(0)]*(M-J-1))
        polys.append([floor_mid(v.real*SCALE) for v in transform])
        z=[v*a/(k+1) for v,a in zip(z,multipliers)]
    point_error=omitted+displacement+arb(4*(ORDER+1))/SCALE
    if not point_error<1:
        raise ArithmeticError("Interpolation error exceeds the amplitude allowance")
    return polys,point_error,amplitude


def parameters(item,target):
    n,r1,d,_=map(int,item['label'].split('/')[-1].split('.'))
    r2=(n-r1)//2
    pi=arb.pi()
    c=arb(d).sqrt()/pi**(arb(n)/2)
    def gamma(s):
        return (s/2).gamma()**(n-r2)*((s+1)/2).gamma()**r2
    def bound(s):
        return 3*c**s*gamma(s)*((s-arb(1)/2)**2/36).exp()*s.zeta()**n
    strip=sum((12*s*pi.sqrt()+72)*bound(s) for s in (arb(3)/2,arb(5)/2))
    strip/=2*pi*((16*pi).exp()-1)
    T=arb(J)/16
    ends=72*bound(arb(2))*(1+2/T)*(-T**2/36).exp()/(2*pi)
    s=arb(8)
    tail=3*c**8*gamma(s)*((s-arb(1)/2)**2/36).exp()*(arb(5)/4).zeta()**n
    tail*= (12*s*pi.sqrt()+72)/(2*pi)
    nmax=max(2,int(float((tail/target)**(arb(4)/27)))+2)
    L=floor_mid(c.log()*M*PHASE/(32*pi))
    return n,r2,c,L,nmax,strip+ends+tail/arb(nmax)**(arb(27)/4)


def evaluate(item,coefs,pars):
    n,r2,c,L,nmax,err=pars
    if len(coefs)!=nmax or coefs[0]!=1 or min(coefs)<0:
        raise ValueError("Incomplete ideal coefficients")
    poly,point_err,amplitude=table(n,r2)
    total=0
    for m,a in enumerate(coefs,1):
        if a:
            coord=coordinates(m)-L
            cell=(coord+PHASE//2)//PHASE
            offset=coord-cell*PHASE
            cell%=M
            v=poly[-1][cell]
            for k in range(ORDER-1,-1,-1):
                v=poly[k][cell]+(v*offset)//PHASE
            total+=a*(RECIP//(m*m))*v
    approx=c**2*arb(total)/(SCALE*RECIP)
    err+=c**2*arb(2).zeta()**n*(point_err+(amplitude+1)*nmax**2/RECIP)
    return approx+arb(0,err.upper())


def process(rows,tolerance,stream):
    for lo in range(0,len(rows),32):
        batch=rows[lo:lo+32]
        params=[parameters(r,arb(tolerance)) for r in batch]
        coeff=[r['coeffs'] for r in batch]
        lengths=[p[4] for p in params]
        ds=[int(r['label'].split('/')[-1].split('.')[2]) for r in batch]
        code=(f'V={coeff};N={lengths};D={ds};\n'
              'for(i=1,#V,K=nfinit(Polrev(V[i])); if(abs(K.disc)!=D[i],error("discriminant"));'
              'print(dirzetak(K,N[i])));\n')
        allcoefs=run_gp(code)
        if len(allcoefs)!=len(batch):
            raise ArithmeticError("Incomplete field batch")
        for item,cc,p in zip(batch,allcoefs,params):
            w=evaluate(item,cc,p)
            print(json.dumps([item["label"],True if w<0 else False if w>0 else None,str(w)]),
                  file=stream)
        stream.flush()


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("input",type=Path)
    ap.add_argument("output",type=Path)
    ap.add_argument("--tolerance",default="0.3")
    args=ap.parse_args()
    ctx.prec=150
    with args.output.open("w") as stream:
        process(json.loads(args.input.read_text()),args.tolerance,stream)
