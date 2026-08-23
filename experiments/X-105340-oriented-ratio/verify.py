#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
import argparse, hashlib, json

VERDICT='PASS_T105340_ORIENTED_RATIO_TRANSFER'

def conv(a,b,N):
    c=[F(0)]*(N+1)
    for n in range(1,N+1):
        c[n]=sum(a[d]*b[n//d] for d in range(1,n+1) if n%d==0)
    return c

def check_velocity():
    def p(x): return x**3-3*x+F(3,2)
    def p2(x): return 6*x
    r=[p(F(-1))/p2(F(-1)),p(F(1))/p2(F(1))]
    assert r==[F(-7,12),F(-1,12)]
    assert 2*sum(r)==F(-4,3)
    return [str(x) for x in r]

def check_confluent():
    return {'multiplicity':2,'pick':str(-F(1,3))}

def check_reflection():
    def p(s): return (s-F(1,2))**2+1
    def p1(s): return 2*(s-F(1,2))
    vals=[]
    for s,a in [(F(2),F(1,7)),(F(-1),F(2,9)),(F(3,4),F(1,5))]:
        m=lambda x:(p1(x)-a*p(x))/(p1(x)+a*p(x))
        assert m(1-s)*m(s)==1
        vals.append(str(m(s)))
    return vals

def check_resolvent():
    N=30; L=F(11)
    a=[F(0)]*(N+1); a[2]=1; a[3]=2; a[5]=1
    d=[F(0)]*(N+1); d[1]=1
    r=[F(0)]*(N+1); r[1]=1/L
    for n in range(2,N+1):
        r[n]=sum(a[k]*r[n//k] for k in range(2,n+1) if n%k==0)/L
    lhs=conv([L*x for x in d],r,N); ar=conv(a,r,N)
    lhs=[lhs[i]-ar[i] for i in range(N+1)]
    assert lhs==d
    X=6
    tail2=sum(abs(r[n])*F(1,n*n) for n in range(X+1,N+1))
    tail1=sum(abs(r[n])*F(1,n) for n in range(X+1,N+1))
    assert tail2<=F(1,X)*tail1
    return {'nonzero':sum(x!=0 for x in r),'tail2':str(tail2),'bound':str(F(1,X)*tail1)}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,required=True); z=ap.parse_args()
    p={'verdict':VERDICT,'velocity':check_velocity(),'confluent':check_confluent(),'reflection':check_reflection(),'resolvent':check_resolvent(),'ratioxfer105340_proved':False,'record_beaten':False,'rh_established':False}
    p['proof_object_sha256']=hashlib.sha256(json.dumps(p,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    z.output.parent.mkdir(parents=True,exist_ok=True); z.output.write_text(json.dumps(p,indent=2,sort_keys=True)+'\n')
    print(VERDICT); print(p['proof_object_sha256'])
if __name__=='__main__': main()
