#!/usr/bin/env python3
"""Directed, source-specific compensated ferromagnetic edge response."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import json,argparse,hashlib
import pr886_primitive as b
import theta_source as t
from tree_core import UNIT,cumulants
I=b.I;SCALE=b.SCALE;ROOT=Path(__file__).resolve().parent

def constants():
    dc=cumulants([F(1)]+[F(0)if n%2 else F(3,5)for n in range(1,19)])
    return [dc[2*r]/UNIT[2*r]for r in range(1,10)]

def response(a):
    zero=a*0;one=zero+1
    den=[one]+[F(3,5)*a**n/factorial(n)if n%2==0 else zero for n in range(1,19)]
    num=[zero]+[F(3,5)*a**n/factorial(n)if n%2 else zero for n in range(1,19)]
    rat=[zero]*19
    for n in range(1,19):rat[n]=num[n]-sum((den[k]*rat[n-k]for k in range(1,n+1)),zero)
    return rat

def reconstruct(src=None):
    b.require(hashlib.sha256((ROOT/'pr886_primitive.py').read_bytes()).hexdigest()==
      '2eba75b7fc82617342c20f6a06270462b6d82f1e7162f66847c029e7e5a9fa55','inherited primitive source identity')
    b.require(hashlib.sha256((ROOT/'pr886_parameters.json').read_bytes()).hexdigest()==
      '20202a816a85ccbdd543ae77532b79990bf8fdffb9186f0798c968d2f797c608','inherited D16 parameters identity')
    if src is None:src=t.reconstruct()
    s=[I(*q)for q in src['standardized_cumulant_ratios']]
    data=json.loads((ROOT/'edge_parameters.json').read_text())
    b.require(data['schema']=='CER.parameters.v1','schema')
    c=[F(x)for x in data['centers']];active=data['active'];rad=F(data['radius'])
    b.require(active==[0,1,2,3,4,5,7,9]and len(c)==11,'D16 active/fixed scope')
    b.require(rad==F(1,10**30),'fixed root box')
    old=json.loads((ROOT/'pr886_parameters.json').read_text())
    for k,x in enumerate(c):
        if k in active:b.require(abs(x-F(old['centers'][k]))+rad<F(1,10**14),'contained in original D16 box')
        else:b.require(x==F(old['centers'][k]),'original D16 fixed coordinates')
    nu=[256,10,1,1,1,1];ar=constants()
    box=[I(I.coerce(x-(rad if k in active else 0)).lo,I.coerce(x+(rad if k in active else 0)).hi)for k,x in enumerate(c)]
    b.require(all(x.lo>I.rat(1,2000).hi for x in box),'positive squared weights')
    def val(r,z):return sum((nu[k]*z[k]**r for k in range(6)),I.coerce(0))+ar[r-1]*sum((z[k]**r for k in range(6,11)),I.coerce(0))
    J0=[[r*(nu[k]if k<6 else ar[r-1])*c[k]**(r-1)for k in active]for r in range(1,9)]
    R=b.inverse(J0)
    for i in range(8):
        for j in range(8):
            b.require(sum(R[i][k]*J0[k][j]for k in range(8))==F(i==j),'exact inverse')
            b.require(sum(J0[i][k]*R[k][j]for k in range(8))==F(i==j),'exact right inverse')
    J=[[r*(nu[k]if k<6 else ar[r-1])*box[k]**(r-1)for k in active]for r in range(1,10)]
    res=[val(r,c)-s[r-1]for r in range(1,9)]
    beta=max(b.absup(sum((R[i][k]*res[k]for k in range(8)),I.coerce(0)))for i in range(8))
    L=max(sum(b.absup(I.coerce(int(i==j))-sum((R[i][k]*J[k][j]for k in range(8)),I.coerce(0)))for j in range(8))for i in range(8))
    b.require(F(L,SCALE)<F(1,1000),'root contraction')
    b.require(F(beta,SCALE)+F(L,SCALE)*rad<rad,'root invariance')
    q0=response(box[6].sqrt());q1=response(box[7].sqrt())
    prod=[sum((q0[k]*q1[n-k]for k in range(n+1)),I.coerce(0))for n in range(19)]
    d=[factorial(2*r)*prod[2*r]/UNIT[2*r]for r in range(1,10)]
    w=[-sum((R[i][k]*d[k]for k in range(8)),I.coerce(0))for i in range(8)]
    Lf=F(L,SCALE);W=max(F(b.absup(x),SCALE)for x in w)
    er=Lf*W/(1-Lf);eri=I.coerce(er).hi
    v=[I(x.lo-eri,x.hi+eri)for x in w]
    slope=UNIT[18]*(d[8]+sum((J[8][i]*v[i]for i in range(8)),I.coerce(0)))
    b.require(slope.lo>I.rat(-785,1000).hi and slope.hi<I.rat(-784,1000).lo,'strict negative response interval')
    defect=UNIT[18]*(val(9,box)-s[8])
    b.require(defect.lo>I.rat(169,1000).hi and defect.hi<I.rat(170,1000).lo,'original next-moment gap')
    return {'schema':'CER.certificate.v1','status':'proposed-computer-assisted-local-component',
      'matched_even_orders':list(range(2,17,2)),'rh_proved':False,'new_edge_root_components':[6,7],
      'edge_variable':'h=tanh(J)','radius':str(rad),'beta_upper':str(F(beta,SCALE)),
      'contraction_upper':str(Lf),'slope18':slope.record(),'old_defect18':defect.record(),
      'inverse_response_tail_upper':str(er),'source_sha256':hashlib.sha256(json.dumps(src,sort_keys=True,separators=(',',':')).encode()).hexdigest()}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--emit',type=Path);ap.add_argument('--check',type=Path);args=ap.parse_args()
    b.require(bool(args.emit)!=bool(args.check),'choose --emit or --check')
    result=reconstruct();text=json.dumps(result,sort_keys=True,separators=(',',':'))+'\n'
    if args.check:b.require(json.loads(args.check.read_text())==result,'reconstructed result differs')
    else:args.emit.write_text(text)
    print('COMPENSATED_EDGE_PASS',hashlib.sha256(text.encode()).hexdigest())
    print('slope18',*[float(F(x,SCALE))for x in result['slope18']])

if __name__=='__main__':main()
