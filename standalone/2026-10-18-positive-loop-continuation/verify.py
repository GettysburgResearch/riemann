#!/usr/bin/env python3
"""Directed full-source local-continuation certificate. No RH or degree-20 match."""
from pathlib import Path
from fractions import Fraction as F
import json
from inherited import BASE,I,SCALE,source
from theta20 import reconstruct
from loop_model import values_jac,evaluate,CK,KS
ROOT=Path(__file__).resolve().parent

def need(ok,msg):
    if not ok: raise ValueError(msg)
def mm(A,x):
    return [sum((a*b for a,b in zip(row,x)),I.coerce(0)) for row in A]
def bounds(x):return [str(F(x.lo,SCALE)),str(F(x.hi,SCALE))]
def absnorm(v):return F(max(x.absup() for x in v),SCALE)

def certify(data,src,pair,radius):
    center=list(map(F,data['centers']))
    if len(center)==18:center.append(F(0))
    active=data['active']; R=[[I.coerce(F(x)) for x in row] for row in data['preconditioner']]
    need(len(active)==9 and len(set(active))==9,'nine active coordinates')
    need(18 not in active,'q is fixed during lower-moment certification')
    rho=F(radius); cen=list(map(I.coerce,center));rad=I.coerce(rho).hi
    box=[I(x.lo-rad,x.hi+rad) if j in active else x for j,x in enumerate(cen)]
    target=[I(*x) for x in src['s'][:9]]
    v0=evaluate(cen,pair)
    beta=absnorm(mm(R,[v0[i]-target[i] for i in range(9)]))
    v,jac=values_jac(box,active+[18],pair)
    J=[row[:9] for row in jac[:9]]
    E=[[I.coerce(int(i==j))-sum((R[i][k]*J[k][j] for k in range(9)),I.coerce(0)) for j in range(9)] for i in range(9)]
    L=F(max(sum(x.absup() for x in row) for row in E),SCALE)
    need(L<F(1,1000),'contractive lower-moment chart')
    need(beta+L*rho<rho,'strict self map')
    need(all(x.lo>0 for x in box[:12]),'positive weights and eta')
    need(all(SCALE//2<x.lo and x.hi<SCALE for x in box[12:18]),'ferromagnetic dimers')
    need(all((box[11]*KS[i]*box[i]).hi<SCALE for i in range(11)),'finite positive hub edges')
    need(0<=center[18]<1,'nonnegative finite added edge')
    # Neumann error for the EXACT tangent y=-(R J)^(-1) R h.
    h=[jac[i][9] for i in range(10)]
    y0=[-x for x in mm(R,h[:9])]
    terr=L*absnorm(y0)/(1-L)
    g=h[9]+sum((jac[9][j]*y0[j] for j in range(9)),I.coerce(0))
    gerr=terr*F(sum(x.absup() for x in jac[9][:9]),SCALE)
    err=I.coerce(gerr).hi
    gamma=I(g.lo-err,g.hi+err)*CK[20]
    # Raw moment at the actual root: direct complete interval polynomial.
    _,raw=evaluate(box,pair,True)
    excess=raw[20]-I(*src['standardized_moments'][20])
    return {'pair':list(pair),'radius':str(rho),'beta':str(beta),'L':str(L),
            'gamma20':bounds(gamma),'excess20':bounds(excess),
            'q':str(center[18]),'tangent_error':str(terr)},gamma,excess

def run():
    src=reconstruct();data=json.loads((BASE/'parameters.json').read_text())
    out=[]
    for pair,lo,hi in [((7,9),F(-3423,1000),F(-3421,1000)),((2,7),F(107,1000),F(109,1000))]:
        rec,g,ex=certify(data,src,pair,'1e-36')
        need(g.lo>lo*SCALE and g.hi<hi*SCALE,'compensated response sign and range')
        need(ex.lo>F(474,1000)*SCALE and ex.hi<F(475,1000)*SCALE,'original degree-20 excess')
        out.append(rec)
    extra=None
    if (ROOT/'POSITIVE_LOOP.json').exists():
        cp=json.loads((ROOT/'POSITIVE_LOOP.json').read_text())
        rec,g,ex=certify(cp,src,(7,9),cp['radius'])
        need(rec['q']=='1/10000','declared positive loop')
        need(ex.lo>F(4737,10000)*SCALE and ex.hi<F(4738,10000)*SCALE,'new excess range')
        # Independent old/new interval estimates, not a first-order extrapolation.
        oldlo=F(out[0]['excess20'][0]); newhi=F(rec['excess20'][1])
        need(oldlo-newhi>F(4,10000),'strict improvement over 0.0004')
        extra=rec
    return {'status':'PASS: finite local continuation, NOT degree-20 matching or RH',
            'source_reconstructed':True,'degree':20,'bits':src['bits'],
            'cells':src['cells'],'theta_indices':src['explicit_indices'],
            'responses':out,'positive_loop':extra}
if __name__=='__main__':print(json.dumps(run(),sort_keys=True,indent=2))
