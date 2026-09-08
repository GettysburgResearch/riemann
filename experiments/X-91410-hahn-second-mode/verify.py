#!/usr/bin/env python3
from fractions import Fraction
import argparse, json


def pi(N,k):
    return Fraction(6*(k+1)*(N-k+1),(N+1)*(N+2)*(N+3))

def lam(N,k):
    return (k+2)*(N-k)

def mu(N,k):
    return k*(N-k+2)

def L_apply(N,f,k):
    out=Fraction(0)
    if k<N:
        out += Fraction(lam(N,k),4)*(f[k+1]-f[k])
    if k>0:
        out += Fraction(mu(N,k),4)*(f[k-1]-f[k])
    return out

def mean(N,f):
    return sum(pi(N,k)*f[k] for k in range(N+1))

def check():
    counts={"normalization":0,"balance":0,"hahn_modes":0,"stein":0,"variance":0,"cone":0}
    for N in range(2,81):
        assert sum(pi(N,k) for k in range(N+1))==1
        counts["normalization"]+=1
        for k in range(N):
            assert pi(N,k)*lam(N,k)==pi(N,k+1)*mu(N,k+1)
            counts["balance"]+=1
        x=[Fraction(2*k-N,2) for k in range(N+1)]
        v=Fraction(N*(N+4),20)
        h2=[xx*xx-v for xx in x]
        assert mean(N,x)==0 and mean(N,h2)==0 and mean(N,[x[k]*h2[k] for k in range(N+1)])==0
        for k in range(N+1):
            assert -L_apply(N,x,k)==x[k]
            assert -L_apply(N,h2,k)==Fraction(5,2)*h2[k]
            counts["hahn_modes"]+=2
        tau=[Fraction(lam(N,k),4) for k in range(N+1)]
        assert mean(N,tau)==v
        for k in range(N+1):
            assert tau[k]-v == -x[k]/2-h2[k]/4
            counts["stein"]+=1
        var_tau=mean(N,[(t-v)**2 for t in tau])
        target=Fraction(N*(N+4)*(N*N+4*N+65),5600)
        assert var_tau==target
        counts["variance"]+=1
    shares=[(Fraction(5,2),Fraction(1,2)),(Fraction(7,3),Fraction(2,3)),(Fraction(4),Fraction(1))]
    assert all(x>=y>=0 for x,y in shares)
    sx=sum(x for x,_ in shares); sy=sum(y for _,y in shares)
    assert sx>=sy>=0
    counts["cone"]+=1
    assert Fraction(1)-2*Fraction(1)<0
    counts["cone"]+=1
    return counts

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--json')
    args=ap.parse_args()
    counts=check()
    out={
      "classification":"PASS_X_91410_HAHN_SECOND_MODE",
      "checks":counts,
      "factor54_signed_detail_margin_proved":False,
      "green_boundary_square_proved":False,
      "theta_dtn_proved":False,
      "rh_proved":False,
      "scope":"exact beta-binomial spectrum, Stein-mode collapse, and abstract detail-cone algebra only"
    }
    text=json.dumps(out,indent=2,sort_keys=True)+"\n"
    if args.json:
        open(args.json,'w').write(text)
    print(text,end='')

if __name__=='__main__':
    main()
