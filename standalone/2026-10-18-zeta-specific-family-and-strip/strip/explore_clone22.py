#!/usr/bin/env python3
"""Empirical dominant-dimer clone continuation; no finite root certificate.

Run explore_field22.py --mode dimer first. That run reconstructs the raw22
theta input with explicit directed tails; this script records its JSON hash.
"""
from decimal import Decimal as D, getcontext
from itertools import product
from math import comb
from pathlib import Path
import argparse,hashlib,json,sys
import check_strip
from explore_field22 import quotient,exponential,legal

ROOT=Path(__file__).resolve().parent
SOURCE_DEFAULT=ROOT.parent.parent/"2026-10-18-theta20-and-native-cancellation"/"theta"


def evaluate(z,delta,lam,cumulants,unit,degree=22):
    zero=z[0]*0;one=zero+1;eta=D("1e-10")
    total=[zero for _ in range(degree+1)]
    for i,count in enumerate((256,10)+(1,)*14):
        if i==2:continue
        A,B,p=z[3*i:3*i+3]
        mu=[one]+[(A**n if i==0 else p*A**n+(one-p)*B**n)
                  *(one if n%2==0 else eta) for n in range(1,degree+1)]
        kk=cumulants(mu);total=[x+count*y for x,y in zip(total,kk)]
    A,B,p=z[6:9];U=(A+B)/2;W=(A-B)/2
    # p is a fixed passive coordinate in the inherited active chart.
    if hasattr(p,"d"):
        if any(p.d):raise ValueError("this experiment fixes p of cloned dimer")
        pp=p.v
    else:pp=p
    qorig=2*pp-1
    qinner=qorig/(1+(1-qorig*qorig).sqrt())
    qhub=eta/(1+(1-eta*eta).sqrt())
    qclone=1-delta
    raw=[zero for _ in range(degree+1)]
    for s1,s2,t1,t2 in product((-1,1),repeat=4):
        mass=((1+qhub*s1)*(1+qhub*s2)*(1+qinner*s1*t1)*
              (1+qinner*s2*t2)*(1+qclone*s1*s2)*(1+qclone*t1*t2))
        field=lam*(U*(s1-s2)+W*(t1-t2))/2
        y=(U*(s1+s2)+W*(t1+t2))/2
        mass=mass*exponential(field)
        for n in range(degree+1):
            power=one if n==0 else y if n==1 else y**n
            raw[n]+=mass*power
    mu=[quotient(x,raw[0]) for x in raw]
    kk=cumulants(mu);total=[x+y for x,y in zip(total,kk)]
    mu=[one]
    for n in range(1,degree+1):
        mu.append(sum((comb(n-1,j-1)*total[j]*mu[n-j] for j in range(1,n+1)),zero))
    mu=[x if n%2==0 else zero for n,x in enumerate(mu)]
    kap=cumulants(mu)
    return [kap[2*j]/unit[2*j] for j in range(1,degree//2+1)],mu


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--source",type=Path,default=SOURCE_DEFAULT)
    args=parser.parse_args()
    check_strip.authenticate(args.source.resolve())
    sys.path.insert(0,str(args.source.resolve()))
    from tree_core import Dual,cumulants,unit_cumulants,linear_solve
    for name,expected in {
            "tree_core.py":"fefac86e70bff53266818c25035d8869dcdffdcc",
            "parameters20.json":"2d43d43f2b027b2a9a1b67374626cc3fd14b2684"}.items():
        content=(args.source/name).read_bytes()
        blob=hashlib.sha1(b"blob "+str(len(content)).encode()+b"\0"+content).hexdigest()
        check_strip.require(blob==expected,"inherited "+name)
    source_data=(ROOT/"theta_source_replay.json").read_bytes()
    check_strip.require(hashlib.sha256(source_data).hexdigest()==
        "206cc313744e3ef24796f24e07e6232d8645ea77eb0235047a1730898da41a58","source replay digest")
    target_data=(ROOT/"field22_dimer_exploration.json").read_bytes()
    extra=json.loads(target_data);src=json.loads(source_data)
    getcontext().prec=90;scale=2**src["bits"];unit=unit_cumulants(22)
    target=[D(lo+hi)/D(2*scale) for lo,hi in src["standardized_cumulant_ratios"]]
    target.append(D(sum(extra["theta_target22_ratio_interval"]))/D(2*scale))
    v=D(sum(src["variance"]))/D(2*scale)
    p=json.loads((args.source/"parameters20.json").read_text());active=p["active"]
    z=[D(x) for x in p["centers"]];lam=D(".0716");rows=[]
    for delta in map(D,["0","0.000001","0.00001","0.0001"]):
        print("CLONE_DELTA",delta,flush=True)
        try:
            for iteration in range(14):
                dual=[Dual(x,[D(int(i==j)) for j in active]) for i,x in enumerate(z)]
                outputs,_=evaluate(dual,delta,lam,cumulants,unit)
                value=[x.v for x in outputs];jac=[list(x.d) for x in outputs]
                step=linear_solve(jac[:10],[target[i]-value[i] for i in range(10)])
                damping=D(1)
                while damping>D("1e-12"):
                    trial=z[:]
                    for i,dx in zip(active,step):trial[i]+=damping*dx
                    if legal(trial):break
                    damping/=2
                else:raise ArithmeticError("positive-domain line search failed")
                z=trial
                if max(abs(damping*dx) for dx in step)<D("1e-65"):break
            else:raise ArithmeticError("ten-moment Newton continuation did not settle")
            value,_=evaluate(z,delta,lam,cumulants,unit)
            _,zero_mu=evaluate(z,delta,D(0),cumulants,unit)
            row={"delta":str(delta),"q_clone":str(1-delta),
                 "finite_couplings":delta>0,
                 "physical_field_weight_ratio":str(lam/v.sqrt()),
                 "physical_reference_variance":str(v*zero_mu[2]),
                 "max_first_ten_cumulant_ratio_residual":str(max(abs(value[i]-target[i]) for i in range(10))),
                 "order22_cumulant_ratio_residual":str(value[10]-target[10]),
                 "parameters":[str(x) for x in z],"legal_positive_model":legal(z),
                 "status":"NONDIRECTED_CONTINUATION_SETTLED"}
            print("CLONE_RESIDUAL22",row["order22_cumulant_ratio_residual"],flush=True)
        except (ArithmeticError,ValueError) as error:
            row={"delta":str(delta),"status":"NONDIRECTED_CONTINUATION_FAILED","reason":str(error)}
            rows.append(row);break
        rows.append(row)
    result={"status":"EMPIRICAL_CLONE_CONTINUATION_NOT_A_CERTIFICATE",
            "source_commit":"c93ca65a510b6acaf167f929b9bf7e67d742b05a",
            "target22_input_sha256":hashlib.sha256(target_data).hexdigest(),
            "decimal_precision":90,"standardized_field_weight_ratio":str(lam),
            "vertices":307,"edges":308,"observed_vertices":306,"zero_weight_hubs":1,
            "clone_model":"replace unique type2 dimer by two half-weight replicas; duplicate inner and hub couplings are halved in J; cross-clone couplings have tanh=1-delta; opposite replica fields",
            "rows":rows,
            "delta_zero_scope":"Only a limiting perfectly locked model, not finite couplings.",
            "claim_limit":"Numerical retuning and residuals are not a root certificate or an order22 theorem."}
    (ROOT/"field22_clone_exploration.json").write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print("CLONE_EXPLORATION_COMPLETE",flush=True)


if __name__=="__main__":main()
