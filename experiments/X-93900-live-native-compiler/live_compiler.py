#!/usr/bin/env python3
"""Generate the live (p,y)=(67,13) native leaf certificate from P61 data."""
from __future__ import annotations
import argparse, hashlib, json
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
getcontext().prec=80
D=Decimal
P=(2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61)

def s(x): return format(+x,'.60E')
def fd(x): return D(x.numerator)/D(x.denominator)
def sq(x): return fd(x).sqrt() if x>0 else D(0)
def mu(n):
    z=n;c=0
    for p in P:
        if z%p==0:
            z//=p;c+=1
            if z%p==0:return 0
    if z!=1:return 0
    return -1 if c%2 else 1

def divisors(limit):
    a=[1]
    for p in P:a += [x*p for x in a if x*p<=limit]
    return sorted(set(x for x in a if x<=limit))

def zext(Y,f): return f(Y) if Y>=1 else D(0)
def T(Y): return zext(Y,lambda x:D(4)*sq(x)-3)
def S(Y): return zext(Y,lambda x:D(5)*sq(x)-3)
def E0(Y): return zext(Y,lambda x:D(2)*sq(x)-1)
def R0(Y): return zext(Y,lambda x:sq(x)-1)

@lru_cache(None)
def data(n,d):
    Y=Fraction(n,d);N=Y.numerator//Y.denominator
    h=[D(0)]*(N+3);tail=[D(0)]*(N+4);ent=D(0);yd=fd(Y)
    for m in range(1,N+1):
        L=(yd/D(m)).ln() if yd!=D(m) else D(0);h[m]=L/D(m).sqrt()
        if m>1:ent+=D(m).ln()*h[m]
    for m in range(N,0,-1):tail[m]=tail[m+1]+h[m]
    q=[D(0)]*(N+3);o=[D(0)]*(N+3)
    for j in range(2,N+1):
        q[j]=D(j+1)/D(j-1)*(h[j]-h[j+1])+D(2*(j+1))/(D(j)*D(j-1))*h[j+1]+D(2)/(D(j)*D(j-1))*tail[j+2]
    for k in range(2,N+1):
        Z=Y/k;M=Z.numerator//Z.denominator;zd=fd(Z);H=D(0)
        for m in range(1,M+1):H+=((zd/D(m)).ln() if zd!=D(m) else D(0))/D(m).sqrt()
        o[k]=H/D(k).sqrt()
    return q,o,ent

def at(Y,j,which):
    a=data(Y.numerator,Y.denominator)[which]
    return a[j] if j<len(a) else D(0)

def atom(p,y,d,N):
    a=Fraction(p)*y/d;b=y/d;rp=D(p).sqrt();sd=D(d).sqrt()
    f=lambda fn:(fn(a)-fn(b)/rp)/sd
    eq,rv,kt,ks=f(E0),f(R0),f(T),f(S)
    assert abs(kt-eq-2*rv)<D('1e-60') and abs(ks-2*eq-rv)<D('1e-60')
    row=[(at(a,j,0)-at(b,j,0)/rp)/sd for j in range(2,N+1)]
    ordinary=[(at(a,q,1)-at(b,q,1)/rp)/sd for q in range(2,N+1)]
    detail=[]
    for q in range(2,N+1):
        oq=ordinary[q-2];o4=(at(a,4*q,1)-at(b,4*q,1)/rp)/sd
        detail.append(oq-2*o4)
    ent=(data(a.numerator,a.denominator)[2]-data(b.numerator,b.denominator)[2]/rp)/sd
    return {'d':d,'mu':mu(d),'parent':str(a),'child':str(b),'child_coefficient':f'1/sqrt({p})','owner':p,
            'equality':s(eq),'reserve':s(rv),'target':s(kt),'declared_score':s(ks),'literal_score':s(ent)},row,ordinary,detail,kt,ks,ent

def build():
    p=67;y=Fraction(13);N=p*13;ds=divisors(N);A={};recs=[]
    for d in ds:
        rec,*vals=atom(p,y,d,N);recs.append(rec);A[d]=vals
    even=[d for d in ds if mu(d)==1];odd=[d for d in ds if mu(d)==-1]
    demand=sum((A[d][3] for d in odd),D(0));rem=demand;u={d:D(0) for d in even};cut=-1
    for d in even:
        take=min(rem,A[d][3]);u[d]=take/A[d][3];rem-=take;cut=d
        if rem<=0:break
    assert abs(rem)<D('1e-55')
    for r in recs:
        d=r['d'];r['target_lorenz_use']=s(u[d]) if r['mu']==1 else '1';r['residual_coefficient']=s(1-u[d]) if r['mu']==1 else '0'
    rows=[];ords=[];dets=[]
    for i,j in enumerate(range(2,N+1)):
        used=sum((u[d]*A[d][0][i] for d in even),D(0));od=sum((A[d][0][i] for d in odd),D(0));ev=sum((A[d][0][i] for d in even),D(0))
        rows.append({'j':j,'residual':s(ev-used),'bonus':s(used-od),'total':s(ev-od)})
    for i,q in enumerate(range(2,N+1)):
        used=sum((u[d]*A[d][1][i] for d in even),D(0));od=sum((A[d][1][i] for d in odd),D(0));ev=sum((A[d][1][i] for d in even),D(0));tot=ev-od
        used4=sum((u[d]*A[d][2][i] for d in even),D(0));od4=sum((A[d][2][i] for d in odd),D(0));ev4=sum((A[d][2][i] for d in even),D(0));det=ev4-od4
        ords.append({'q':q,'total':s(tot)});dets.append({'q':q,'ordinary_q':s(tot),'ordinary_4q':s((tot-det)/2),'detail':s(det),'bonus':s(used4-od4)})
    usedS=sum((u[d]*A[d][4] for d in even),D(0));oddS=sum((A[d][4] for d in odd),D(0));evenS=sum((A[d][4] for d in even),D(0))
    payload={'schema':'riemann.t93900.live.v2','frozen_pr507':'dfaa70cd2eefcabbf6717e3da060792904c7f357',
      'x2_separator':{'tau_from_k2':'1','k1_difference':'2*(sqrt(2)-1)>0'},
      'leaf':{'p':67,'y':13,'endpoint':871,'occurrences':recs,'cutoff':cut,'odd_target':s(demand)},
      'score':{'signed':s(evenS-oddS),'residual':s(evenS-usedS),'surplus':s(oddS-usedS)},
      'rows':rows,'ordinary':ords,'detail':dets,
      'normalization':{'target':'E+2R','score':'2E+R','same_coefficient_both_channels':True,'rough_lift_parent':False,'q4_after_common_ordinary':True},
      'endpoint':{'native_cost':60989,'orientation':'F_Lambda <= native_deficit','benchmark_bridge':False,'rh_proved':False}}
    raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode();payload['proof_object_sha256']=hashlib.sha256(raw).hexdigest();return payload

def summary(x):
    h=lambda z:hashlib.sha256(json.dumps(z,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    pos=lambda a,key:min((D(v[key]) for v in a if D(v[key])>D('1e-45')),default=D(0))
    return {'schema':'riemann.t93900.live.summary.v2','proof_object_sha256':x['proof_object_sha256'],'frozen_pr507':x['frozen_pr507'],
      'occurrence_count':len(x['leaf']['occurrences']),'row_count':len(x['rows']),'ordinary_count':len(x['ordinary']),'detail_count':len(x['detail']),
      'occurrences_sha256':h(x['leaf']['occurrences']),'rows_sha256':h(x['rows']),'ordinary_sha256':h(x['ordinary']),'detail_sha256':h(x['detail']),
      'minimum_positive_row':s(pos(x['rows'],'total')),'minimum_positive_ordinary':s(pos(x['ordinary'],'total')),'minimum_positive_detail':s(pos(x['detail'],'detail')),
      'score':x['score'],'cutoff':x['leaf']['cutoff'],'x2_separator':x['x2_separator'],'normalization':x['normalization'],'endpoint':x['endpoint']}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);ap.add_argument('--summary',type=Path);a=ap.parse_args();x=build()
    if a.output:a.output.write_text(json.dumps(x,indent=2,sort_keys=True)+'\n')
    if a.summary:a.summary.write_text(json.dumps(summary(x),indent=2,sort_keys=True)+'\n')
    print('PASS_LIVE_NATIVE_SOURCE_TO_PHYSICAL_ROW_CERTIFICATE');print(x['proof_object_sha256']);print(len(x['leaf']['occurrences']),len(x['rows']),len(x['detail']))
if __name__=='__main__':main()
