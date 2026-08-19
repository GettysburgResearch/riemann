#!/usr/bin/env python3
from fractions import Fraction
from math import isqrt
import hashlib,json
from pathlib import Path

def dec(s):
    neg=s.startswith('-')
    if neg:s=s[1:]
    a,b=(s.split('.')+[''])[:2]
    q=Fraction(int(a+b),10**len(b))
    return -q if neg else q

def log_ratio_interval(a,b,K=90):
    y=Fraction(a-b,a+b)
    s=Fraction(0)
    yp=y
    for k in range(K):
        s += yp/Fraction(2*k+1)
        yp *= y*y
    lo=2*s
    rem=2*yp/Fraction((2*K+1)) / (1-y*y)
    return lo,lo+rem

def invsqrt_interval(n,bits=300):
    S=1<<bits
    L=isqrt(n*S*S)
    return Fraction(S,L+1),Fraction(S,L)

def mul_iv(a,b):
    vals=[a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]]
    return min(vals),max(vals)

def live_witness():
    F0=(dec('10.69357964877382995080531550498'),dec('10.69357964877382995080531550500'))
    M0=(dec('445.85760354260283631557807730110'),dec('445.85760354260283631557807730112'))
    logiv=log_ratio_interval(92,67)
    cinv=invsqrt_interval(134)
    c=mul_iv((15*logiv[0],15*logiv[1]),cinv)
    k=Fraction(11,476)
    gap_hi=F0[1]-c[0]-k*(M0[0]+c[0])
    gap_lo=F0[0]-c[1]-k*(M0[1]+c[1])
    return {'gap_lo':str(gap_lo),'gap_hi':str(gap_hi),'child_lo':str(c[0]),'child_hi':str(c[1])}

def projective_identity(m,f,mc,fc,p):
    a=Fraction(1,p)
    D=f*mc-m*fc
    lhs=f-a*fc
    rhs=(1-a*mc/m)*f+a*D/m
    return lhs,rhs,D

def quadrilateral_identity(vals,p):
    m,f,mp,fp,mq,fq,mpq,fpq=vals
    a=Fraction(1,p)
    D=f*mq-m*fq
    Dc=fp*mpq-mp*fpq
    Xi=f*mpq+m*fpq-fp*mq-mp*fq
    direct=(f-a*fp)*(mq+a*mpq)-(m+a*mp)*(fq-a*fpq)
    formula=D+a*Xi-a*a*Dc
    return direct,formula,D,Dc,Xi

def build_result():
    lhs,rhs,_=projective_identity(Fraction(7),Fraction(3),Fraction(5),Fraction(2),67)
    assert lhs==rhs
    vals=tuple(map(Fraction,[1,1,1,1,1,1,1,0]))
    direct,formula,Dq,Dc,Xi=quadrilateral_identity(vals,67)
    assert direct==formula==Fraction(-68,67*67)
    assert Dq==0 and Dc==1 and Xi==-1
    live=live_witness()
    assert Fraction(live['gap_hi']) < Fraction(-3,100)
    core={
      'schema':'riemann.x99200.projective-bellman.v1',
      'verdict':'PASS_T99200_PROJECTIVE_BELLMAN_AND_QUADRILATERAL_FIREWALL',
      'projective_identity':'exact',
      'quadrilateral_identity':'exact',
      'abstract_updated_determinant':str(direct),
      'live_p67_x184_gap_interval':[live['gap_lo'],live['gap_hi']],
      'product_aperture_survives':False,
      'two_scale_cone_invariant':False,
      'rh_established':False}
    payload=json.dumps(core,sort_keys=True,separators=(',',':')).encode()
    core['proof_object_sha256']=hashlib.sha256(payload).hexdigest()
    return core

def main():
    r=build_result();out=Path(__file__).parent/'results'/'verification.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n')
    print(r['verdict']);print(r['proof_object_sha256'])
if __name__=='__main__':main()
