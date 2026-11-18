"""Rigorous Dedekind spectral-weight evaluator with a truncated Euler logarithm."""
import argparse
from functools import cache
import json
from pathlib import Path
from flint import acb, arb, ctx
from check_zhao_field_weight_nov18 import primes_through
from check_zhao_high_degree_nov18 import gp_rows

B = 8
J = 320


@cache
def kernel(n, r2):
    h = arb(1)/4
    values = []
    for j in range(J+1):
        w = acb(B, j*h)
        g = (w/2).gamma()**(n-r2) * ((w+1)/2).gamma()**r2
        v = (2*w-1)*g*((w-arb(1)/2)**2/36).exp()
        v *= h*(1 if j==0 else 2)/(2*arb.pi())
        values.append((v, v/(w*(w-1))))
    return values


@cache
def prime_wave(m):
    h=arb(1)/4
    step=acb(0,-h*arb(m).log()).exp()
    value=acb(1)/m**B
    vals=[]
    for j in range(J+1):
        if j and j%32==0:
            value=step**j/m**B
        vals.append(value)
        value*=step
    return vals


def weight(item, tolerance="1e-6"):
    n,r1,d,_=map(int,item["label"].split("/")[-1].split("."))
    r2=(n-r1)//2
    h=arb(1)/4
    pi=arb.pi()
    c=arb(d).sqrt()/pi**(arb(n)/2)
    def const(sigma):
        s=arb(sigma)
        return (c**sigma*(s/2).gamma()**(n-r2)*((s+1)/2).gamma()**r2
                *((s-arb(1)/2)**2/36).exp()*s.zeta()**n)
    def norm(s):
        return (2*s*6*pi.sqrt()+72)*const(s)
    strip=(norm(2)+norm(14))/(2*pi*((12*pi/h).exp()-1))
    t=J*h
    ends=const(B)*72*(1+B/t)*(-t**2/36).exp()/(2*pi)
    # The two integrands' moduli are bounded by the same Gaussian times
    # (2B+2|t|). Enclose the discrete sum by the integral plus two peaks.
    sum_bound=const(B)*(2*B*6*pi.sqrt()+72+4*h*(2*B+12))/(2*pi)
    target=arb(tolerance)
    limit=max(2,int(float((2*n*sum_bound/(7*target))**(arb(1)/7)))+2)
    log_error=arb(n)/(7*arb(limit)**7)
    finite=sum_bound*log_error.expm1()
    err=strip+ends+finite
    if not err < 2*target:
        raise ArithmeticError(f"Insufficient quadrature bounds: {err}")
    primes=primes_through(limit)
    (row,)=gp_rows([item],primes)
    logs=[acb(0) for _ in range(J+1)]
    for p,code in zip(primes,row[-1]):
        k=1
        m=p
        while m<=limit:
            numer=sum(f*(code//10**(f-1)%10) for f in range(1,n+1) if k%f==0)
            if numer:
                a=arb(numer)/k
                for j,z in enumerate(prime_wave(m)):
                    logs[j]+=a*z
            m*=p
            k+=1
    den,num=arb(0),arb(0)
    logc=c.log()
    for j,(z,(v,v1)) in enumerate(zip(logs,kernel(n,r2))):
        factor=(z+acb(B,j*h)*logc).exp()
        den+=(factor*v).real
        num+=(factor*v1).real
    den+=arb(0,err.upper())
    num+=arb(0,err.upper())
    if not den>0:
        raise ArithmeticError("Failed to enclose a positive residue")
    return 2*(num/den-arb(1)/36)


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("input",type=Path)
    ap.add_argument("--tolerance",default="1e-6")
    opt=ap.parse_args()
    ctx.prec=160
    obj=json.loads(opt.input.read_text())
    for item in obj["unresolved"]:
        w=weight(item,opt.tolerance)
        print(json.dumps(dict(label=item["label"],weight=str(w),
                              passed=True if w<2 else False if w>2 else None)),flush=True)
