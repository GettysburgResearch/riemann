"""Certify cubic S3-field Zhao weights from a PARI/GP enumeration and Arb intervals."""
import argparse
import json
import os
import subprocess
from functools import cache
from pathlib import Path
from flint import arb, ctx
from check_zhao_field_weight_nov18 import field_terms, prime_term, primes_through


def run_gp(code, *, lines=False):
    proc = subprocess.run([os.getenv("PARI_GP", "gp"), "-fq"], input=code,
                          text=True, capture_output=True, check=True)
    errors = [s for s in proc.stderr.splitlines() if s.strip() and "Warning: new stack" not in s]
    if errors:
        raise RuntimeError("\n".join(errors))
    rows = proc.stdout.strip().splitlines()
    return rows if lines else [json.loads(row) for row in rows]


def list_fields():
    return run_gp('default(parisize,"160M");\n'
                  'V=concat(nflist("S3",[1,96900],0),nflist("S3",[1,55200],1));\n'
                  'for(i=1,#V, f=V[i]; print([nfdisc(f),Vec(f)]));\n')


def polynomial(coeff):
    return f"x^3+({coeff[1]})*x^2+({coeff[2]})*x+({coeff[3]})"


def decomposition_rows(fields, limit):
    # Split into modest batches to bound the size of the GP parser input.
    for start in range(0, len(fields), 64):
        sub = fields[start:start+64]
        expr = ','.join(polynomial(c) for _, c in sub)
        code = ('default(parisize,"160M");\nV=['+expr+'];\n'
                f'P=primes([2,{limit}]);\n'
                'for(i=1,#V,F=V[i]; N=nfinit(F); '
                'print(vector(#P,j,my(v=idealprimedec(N,P[j]));sum(l=1,#v,10^(v[l].f-1)))));\n')
        rows = run_gp(code)
        if len(rows) != len(sub):
            raise ArithmeticError("PARI returned an incomplete batch")
        yield from zip(sub, rows)


@cache
def euler_table(limit, p, code):
    degrees = [f for f in range(1,4) for _ in range((code//10**(f-1))%10)]
    if not degrees or sum(degrees)>3:
        raise ArithmeticError(f"Invalid local degree code {code}")
    return sum(prime_term(limit,p,f) for f in degrees)


def classify(fields, limits):
    accepted, undecided = [], fields
    stats = []
    for limit in limits:
        g, delta, pole, a0, a1 = field_terms(limit)
        primes = primes_through(limit)
        unresolved, good, bad = [], 0, 0
        for row, codes in decomposition_rows(undecided, limit):
            disc, _ = row
            if len(codes) != len(primes):
                raise ArithmeticError("Incomplete Euler prime inventory")
            base = 3*a0 if disc>0 else 2*a0+a1
            w = g*arb(abs(disc)).log()+pole+base
            for p, code in zip(primes,codes):
                w -= euler_table(limit,p,code)
            if w < 2*(1-delta):
                accepted.append(row)
                good += 1
            elif w > 2*(1+delta):
                bad += 1
            else:
                unresolved.append(row)
        print(limit,good,bad,len(unresolved),flush=True)
        stats.append([limit,good,bad,len(unresolved)])
        undecided = unresolved
        euler_table.cache_clear()
        if not undecided:
            break
    return {"enumerated":len(fields),"stages":stats,
            "accepted":sorted(accepted),"unresolved":sorted(undecided)}


def verify_discriminant_coverage():
    g, delta, pole, a0, a1 = field_terms(4)
    max_prime_term = 3*sum(prime_term(4,p,1) for p in (2,3))
    for r1,r2,bound in [(3,0,96900),(1,1,55200)]:
        log_bound=(2*(1+delta)-pole-(r1+r2)*a0-r2*a1+max_prime_term)/g
        if not log_bound.exp() < bound:
            raise ArithmeticError("Enumeration misses part of the conductor bound")


def theta_weight(disc, coeff):
    c = 2*arb.pi()/arb(abs(disc)).sqrt()
    if not c > arb(1)/64:
        raise ArithmeticError("Discriminant exceeds proved theta bounds")
    # Keep every term whose exponential argument might be smaller than 128.
    nmax = int(129/float(c))+2
    poly = polynomial(coeff)
    cmd=(f'F={poly};N={nmax};\n'
         'print(dirdiv(dirzetak(nfinit(F),N),vector(N,i,1)));\n')
    (coefficients,)=run_gp(cmd)
    if len(coefficients)!=nmax or coefficients[0]!=1:
        raise ArithmeticError("Incomplete Artin coefficient vector")
    h=arb(1)/20
    den,num=arb(0),arb(0)
    for j in range(1000):
        u=j*h
        t=u.exp()
        z=c*t
        if z>128:
            break
        kmax=min(nmax,int(129/float(z))+1)
        if not (kmax+1)*z>128:
            raise ArithmeticError("Uncertified theta cutoff")
        v=arb(0)
        if disc<0:
            q=(-z).exp()
            for a in reversed(coefficients[:kmax]):
                v=v*q+a
            v*=q
        else:
            for k,a in enumerate(coefficients[:kmax],1):
                if a:
                    v+=a*(k*z).bessel_k(0)
        if j==0:
            den+=v
        else:
            den+=(t+1)*v
            num+=u*(t-1)*v
    else:
        raise ArithmeticError("Trapezoid did not reach the tail")
    err=arb(0,"1e-12")
    den=den*h+err
    num=num*h+err
    if not den>0:
        raise ArithmeticError("Theta denominator unresolved")
    return 2+arb.const_euler()-(4*arb.pi()).log()+2*num/den


def finish_theta(report):
    report["theta"]=[]
    for d,coeff in report["unresolved"]:
        w=theta_weight(d,coeff)
        if w<2:
            report["accepted"].append([d,coeff])
        elif not w>2:
            raise ArithmeticError(f"Threshold unresolved at {d}: {w}")
        report["theta"].append([d,coeff,str(w)])
    report["accepted"].sort()
    report["unresolved"]=[]
    print("complete",len(report["accepted"]),len(report["theta"]),flush=True)


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--limits",type=int,nargs="+",default=[16,64,256,1024,4096,16384])
    args=parser.parse_args()
    ctx.prec=96
    verify_discriminant_coverage()
    fields=list_fields()
    if len({(d,tuple(c)) for d,c in fields})!=len(fields):
        raise ArithmeticError("Duplicated field record")
    report=classify(fields,args.limits)
    finish_theta(report)
    args.output.write_text(json.dumps(report,separators=(",",":"))+"\n")
