#!/usr/bin/env python3
from fractions import Fraction
import argparse, json

def pi(N,k): return Fraction(6*(k+1)*(N-k+1),(N+1)*(N+2)*(N+3))
def lam(N,k): return (k+2)*(N-k)
def mean(N,f): return sum(pi(N,k)*f[k] for k in range(N+1))

def check():
    c={"mode_norms":0,"edge_currents":0,"continuum_moments":0}
    for N in range(2,101):
        x=[Fraction(2*k-N,2) for k in range(N+1)]
        v=Fraction(N*(N+4),20)
        h=[z*z-v for z in x]
        assert mean(N,[z*z for z in x])==v
        hnorm=mean(N,[z*z for z in h])
        assert hnorm==Fraction(N*(N-1)*(N+4)*(N+5),350)
        c["mode_norms"]+=2
        tau=[Fraction(lam(N,k),4) for k in range(N+1)]
        for d in range(7):
            g=[Fraction(k**d) for k in range(N+1)]
            lhs=mean(N,[(tau[k]-v)*g[k] for k in range(N+1)])
            rhs=-sum(pi(N,k)*lam(N,k)*Fraction(2*k-N+6,40)*(g[k+1]-g[k]) for k in range(N))
            assert lhs==rhs
            c["edge_currents"]+=1
    ev2=Fraction(1,5); ev4=Fraction(3,35)
    h2norm=ev4-ev2*ev2
    assert h2norm==Fraction(8,175)
    vartau=h2norm/Fraction(16)
    assert vartau==Fraction(1,350)
    c["continuum_moments"]+=2
    return c

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--json'); a=ap.parse_args()
    out={"classification":"PASS_X_91411_HAHN_EDGE_CURRENT","checks":check(),"theta_schur_completion_proved":False,"rh_proved":False,"scope":"exact low-mode norms and edge-current identities only"}
    s=json.dumps(out,indent=2,sort_keys=True)+"\n"
    if a.json: open(a.json,'w').write(s)
    print(s,end='')
if __name__=='__main__': main()
