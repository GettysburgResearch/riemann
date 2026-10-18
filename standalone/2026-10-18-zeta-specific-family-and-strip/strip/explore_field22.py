#!/usr/bin/env python3
"""Nondirected continuation experiment on the proposed T20D graph.

The experiment retunes its ten active coordinates while putting opposite
fields on two identical leaves, and measures the unmatched order-22 cumulant.
No empirical root or zero claim from this script is certified. The order-22
theta target is enclosed using the same primitive formula with j=22, paying
the same Taylor, six time, and all omitted-index tails explicitly.
"""
from __future__ import annotations
from decimal import Decimal as D, getcontext
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import argparse
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
DEFAULT_SOURCE = ROOT.parent.parent / "2026-10-18-theta20-and-native-cancellation" / "theta"


def raw22(b):
    I=b.I;pi=b.pi_interval();counts=(32,24,16,12,8,6)
    total=I.coerce(0);j=22
    for n,count in enumerate(counts,1):
        for index in range(count):
            center=F(2*index+1,32)
            total+=b.integrate_moment(b.cell_density(n,center,pi),center,j)
    error=I.rat(16*10**11*2**j,4**(b.DEGREE+1))/F(3,4)
    tails=I.coerce(0)
    for n,count in enumerate(counts,1):
        U=F(count,16);q=pi*n*n;E=b.exp(2*I.coerce(U));lam=2*q*E-F(9,2)
        b.require(lam.lo>0,"positive time-tail exponent")
        tails+=8*q*q*b.exp(F(9,2)*I.coerce(U)-q*E)*sum(
            (comb(j,k)*U**(j-k)*factorial(k)/lam**(k+1) for k in range(j+1)),I.coerce(0))
    omitted=16*pi*pi*7**4*b.exp(-49*pi)*factorial(j)/(98*pi-F(9,2))**(j+1)
    return I(total.lo-error.hi,total.hi+error.hi+tails.hi+omitted.hi)


def quotient(a,b):
    if hasattr(b,"d"):
        return type(b)(a.v/b.v,[(x*b.v-a.v*y)/(b.v*b.v) for x,y in zip(a.d,b.d)])
    return a/b


def exponential(a):
    if hasattr(a,"d"):
        value=a.v.exp()
        return type(a)(value,[value*x for x in a.d])
    return a.exp()


def evaluate(z,r,cumulants,unit,degree=22,mode="leaf"):
    counts=(256,10)+(1,)*14
    zero=z[0]*0;one=zero+1;eta=D("1e-10")
    total=[zero for _ in range(degree+1)]
    for i,count in enumerate(counts):
        A,B,p=z[3*i:3*i+3]
        number=count-2 if i==(0 if mode=="leaf" else 1) else count
        mu=[one]+[(A**n if i==0 else p*A**n+(one-p)*B**n)
                  *(one if n%2==0 else eta) for n in range(1,degree+1)]
        kk=cumulants(mu)
        total=[x+number*y for x,y in zip(total,kk)]
    for signed_r in (r,-r):
        if mode=="leaf":
            mean=(eta+signed_r)/(1+eta*signed_r)
            mu=[one]+[z[0]**n*(one if n%2==0 else mean)
                      for n in range(1,degree+1)]
        else:
            A,B,p=z[3:6]
            epA,emA=exponential(signed_r*A),exponential(-signed_r*A)
            epB,emB=exponential(signed_r*B),exponential(-signed_r*B)
            ca,sa=(epA+emA)/2,(epA-emA)/2
            cb,sb=(epB+emB)/2,(epB-emB)/2
            normalization=p*(ca+eta*sa)+(one-p)*(cb+eta*sb)
            mu=[one]+[quotient(
                p*A**n*((ca+eta*sa) if n%2==0 else (sa+eta*ca))+
                (one-p)*B**n*((cb+eta*sb) if n%2==0 else (sb+eta*cb)),
                normalization) for n in range(1,degree+1)]
        kk=cumulants(mu)
        total=[x+y for x,y in zip(total,kk)]
    mu=[one]
    for n in range(1,degree+1):
        mu.append(sum((comb(n-1,j-1)*total[j]*mu[n-j]
                       for j in range(1,n+1)),zero))
    mu=[x if n%2==0 else zero for n,x in enumerate(mu)]
    kap=cumulants(mu)
    return [kap[2*j]/unit[2*j] for j in range(1,degree//2+1)],mu


def jet(z,r,active,Dual,cumulants,unit,mode):
    dual=[Dual(x,[D(int(i==j)) for j in active]) for i,x in enumerate(z)]
    values,_=evaluate(dual,r,cumulants,unit,mode=mode)
    return [x.v for x in values], [list(x.d) for x in values]


def legal(z):
    return (z[0]>0 and all(z[i]>z[i+1]>0 and D(".5")<z[i+2]<1
                          for i in range(3,len(z),3)))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--source",type=Path,default=DEFAULT_SOURCE)
    parser.add_argument("--source-replay",type=Path,default=ROOT/"theta_source_replay.json")
    parser.add_argument("--mode",choices=["leaf","dimer"],default="leaf")
    args=parser.parse_args()
    import check_strip
    identities=check_strip.authenticate(args.source.resolve())
    for name,expected in {
            "tree_core.py":"fefac86e70bff53266818c25035d8869dcdffdcc",
            "parameters20.json":"2d43d43f2b027b2a9a1b67374626cc3fd14b2684"}.items():
        content=(args.source/name).read_bytes()
        blob=hashlib.sha1(b"blob "+str(len(content)).encode()+b"\0"+content).hexdigest()
        check_strip.require(blob==expected,"inherited "+name)
        identities[name]={"git_blob":blob,"sha256":hashlib.sha256(content).hexdigest()}
    data=args.source_replay.read_bytes()
    check_strip.require(hashlib.sha256(data).hexdigest()==
        "206cc313744e3ef24796f24e07e6232d8645ea77eb0235047a1730898da41a58",
        "fresh replay input digest")
    src=json.loads(data)
    sys.path.insert(0,str(args.source.resolve()))
    import pr886_primitive as b
    from tree_core import Dual,cumulants,unit_cumulants,linear_solve
    getcontext().prec=90
    unit=unit_cumulants(22)
    high=raw22(b)
    variance=b.I(*src["variance"])
    mass=b.I(*src["raw"]["0"])
    moments=[b.I(*x) for x in src["standardized_moments"]]
    moments.extend([b.I.coerce(0),high/mass/variance**11])
    caps=cumulants(moments)
    ratio=[caps[2*j]/unit[2*j] for j in range(1,12)]
    target=[D(x.lo+x.hi)/D(2*b.SCALE) for x in ratio]
    p=json.loads((args.source/"parameters20.json").read_text())
    z=[D(s) for s in p["centers"]]
    active=p["active"]
    rows=[]
    grid=(["0","0.0003","0.0006","0.0009","0.0012","0.0015"]
          if args.mode=="leaf" else ["0","0.0143","0.0286","0.0430","0.0573","0.0716"])
    for r in map(D,grid):
        print("FIELD_POINT",r,flush=True)
        for iteration in range(12):
            value,jacobian=jet(z,r,active,Dual,cumulants,unit,args.mode)
            step=linear_solve(jacobian[:10],[target[i]-value[i] for i in range(10)])
            damping=D(1)
            while damping>D("1e-12"):
                trial=z[:]
                for i,delta in zip(active,step):trial[i]+=damping*delta
                if legal(trial):break
                damping/=2
            else:raise ArithmeticError("positive-domain line search failed")
            z=trial
            if max(abs(v*damping) for v in step)<D("1e-65"):break
        else:raise ArithmeticError("nondirected continuation failed to settle")
        value,mu=evaluate(z,r,cumulants,unit,mode=args.mode)
        zero_values,zero_mu=evaluate(z,D(0),cumulants,unit,mode=args.mode)
        h=((1+r)/(1-r)).ln()/2
        v=D(sum(src["variance"]))/D(2*b.SCALE)
        row={"field_parameter":str(r),"mode":args.mode,
             "field_parameter_kind":"tanh(h)" if args.mode=="leaf" else "standardized field/weight ratio",
             "physical_field_weight_ratio":str((h/z[0] if args.mode=="leaf" else r)/v.sqrt()),
             "physical_reference_variance":str(v*zero_mu[2]),
             "max_first_ten_cumulant_ratio_residual":str(max(abs(value[i]-target[i]) for i in range(10))),
             "order22_cumulant_ratio":str(value[10]),
             "target22_cumulant_ratio":str(target[10]),
             "order22_cumulant_ratio_residual":str(value[10]-target[10]),
             "parameters":[str(s) for s in z],"legal_positive_model":legal(z)}
        rows.append(row)
        print("PHYSICAL_BAND",row["physical_field_weight_ratio"],
              "RESIDUAL22",row["order22_cumulant_ratio_residual"],flush=True)
    result={"status":"EMPIRICAL_CONTINUATION_NOT_A_CERTIFICATE",
            "source_commit":"c93ca65a510b6acaf167f929b9bf7e67d742b05a",
            "source_files":identities,"decimal_precision":90,
            "field_pair":("two of 256 identical leaves; fields +atanh(r),-atanh(r)"
                if args.mode=="leaf" else "two of ten identical dimers; vertex fields +lambda*weight and -lambda*weight"),
            "all_other_fields":0,
            "full_model":"305-spin tree; 304 positive edges; all components retained",
            "theta_raw22_directed_interval":high.record(),
            "theta_target22_ratio_interval":ratio[10].record(),
            "interval_bits":b.BITS,"rows":rows,
            "claim_limit":"No root existence or order22 equality follows from these ordinary Decimal iterates."}
    (ROOT/("field22_"+args.mode+"_exploration.json")).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print("FIELD22_EXPLORATION_COMPLETE",flush=True)


if __name__=="__main__":
    main()
