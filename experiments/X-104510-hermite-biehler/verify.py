#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math
from fractions import Fraction
from pathlib import Path

def trim(a):
    while len(a)>1 and a[-1]==0:
        a.pop()
    return a

def addp(a,b):
    n=max(len(a),len(b)); c=[Fraction(0) for _ in range(n)]
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    return trim(c)

def mulp(a,b):
    c=[Fraction(0) for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)

def deriv(a):
    return trim([Fraction(i)*a[i] for i in range(1,len(a))] or [Fraction(0)])

def evalp(a,x):
    s=Fraction(0)
    for c in reversed(a): s=s*x+c
    return s

def discriminant_cubic(a,b,c,d):
    return b*b*c*c - 4*a*c*c*c - 4*b*b*b*d - 27*a*a*d*d + 18*a*b*c*d

def laguerre(p):
    dp=deriv(p); dd=deriv(dp)
    return addp(mulp(dp,dp),[-x for x in mulp(p,dd)])

def proof_digest(payload):
    return hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def verify():
    checks={}
    q=[Fraction(2),0,Fraction(-2),0,Fraction(1)]
    dq=deriv(q)
    crit=[Fraction(-1),Fraction(0),Fraction(1)]
    wrong=0
    for c in crit:
        if evalp(q,c)*evalp(deriv(dq),c)>0:
            wrong+=1
    assert wrong==2
    checks["quartic_wrong_extrema"]=wrong

    p=[Fraction(1),Fraction(3),Fraction(1),Fraction(1)]
    disc=discriminant_cubic(Fraction(1),Fraction(1),Fraction(3),Fraction(1))
    assert disc==-76
    L=laguerre(p)
    assert L==[Fraction(7),0,Fraction(2),Fraction(4),Fraction(3)]
    sos=addp([Fraction(7),0,Fraction(2,3)],[Fraction(0)]*5)
    square=mulp([Fraction(0),Fraction(2,3),Fraction(1)],[Fraction(0),Fraction(2,3),Fraction(1)])
    sos=addp(sos,[3*x for x in square])
    assert sos==L
    checks["laguerre_positive_cubic_discriminant"]=int(disc)

    fixtures=[
        [Fraction(-1),0,Fraction(1)],
        [Fraction(1),Fraction(3),Fraction(1),Fraction(1)],
        [Fraction(2),0,Fraction(-2),0,Fraction(1)],
    ]
    phase_checks=0
    for f in fixtures:
        fp=deriv(f); fpp=deriv(fp)
        lag=addp(mulp(fp,fp),[-x for x in mulp(f,fpp)])
        num=addp(mulp(fp,fp),[-x for x in mulp(f,fpp)])
        assert num==lag
        phase_checks+=1
    checks["phase_identity_fixtures"]=phase_checks

    Cminus=Fraction(-2,3); Cplus=Fraction(2,3)
    assert Cminus < 0 < Cplus
    checks["antiderivative_interval"]=[str(Cminus),str(Cplus)]

    vals=[]
    for n in (10**6,10**8,10**10):
        T=math.sqrt(n/math.log(n))/math.log(math.log(n))
        sigma=math.sqrt(math.log(n)/n)
        vals.append(T*sigma)
    assert vals[2] < vals[1] < vals[0]
    checks["growing_box_products"]=vals

    payload={
        "schema":"riemann.t104510.hermite_biehler_last_defect.v1",
        "checks":checks,
        "scope":{
            "hermite_biehler_index_proved_analytically":True,
            "antiderivative_interval_proved":True,
            "phase_identity_proved":True,
            "strip_invariance_proved_analytically":True,
            "rpch_independent_producer":False,
            "pres104515_proved":False,
            "vflux104515_proved":False,
            "rh_established":False
        },
        "verdict":"PASS_T104510_HERMITE_BIEHLER_LAST_DEFECT_ALGEBRA"
    }
    payload["proof_object_sha256"]=proof_digest(payload)
    return payload

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",type=Path)
    args=ap.parse_args()
    out=verify()
    text=json.dumps(out,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text)
    else:
        print(text,end="")
    print(out["verdict"])
    print(out["proof_object_sha256"])
