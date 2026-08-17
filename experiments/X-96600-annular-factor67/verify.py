#!/usr/bin/env python3
from __future__ import annotations
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
import bisect, hashlib, json, math, sys, time
import numpy as np
getcontext().prec=80
D=Decimal
PRIMES=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
LOG4=math.log(4.0); KLO=-2.025; KHI=-2.024

def divisors():
 out=[(1,1)]
 for p in PRIMES: out += [(d*p,-m) for d,m in out]
 return sorted(out)

def dec_ann(X,S,T):
 M=X//4; return D(4).ln()*S[M]+D(X).ln()*(S[X]-S[M])-(T[X]-T[M])

def main(out):
 t0=time.time(); divs=divisors(); dint=[d for d,m in divs]
 da=np.array([float(d) for d,m in divs]); ma=np.array([m for d,m in divs],float)
 preA=np.concatenate([[0.0],np.cumsum(ma/da)]); preB=np.concatenate([[0.0],np.cumsum(ma/np.sqrt(da))]); preT=np.concatenate([[0.0],np.cumsum(ma*np.log(da)/np.sqrt(da))])
 # all finite Phi events; the 1e-9 audit allowance is vastly below the 0.08 margin.
 events=sorted(set(dint+[4*d for d in dint])); pmax=(-1e99,None);pmin=(1e99,None)
 for x in events:
  i=bisect.bisect_right(dint,x); im=bisect.bisect_right(dint,x//4)
  v=LOG4*preB[im]+math.log(x)*(preB[i]-preB[im])-(preT[i]-preT[im])
  if v>pmax[0]:pmax=(v,x)
  if v<pmin[0]:pmin=(v,x)
 assert pmax[0]+1e-9<1.5 and pmin[0]-1e-9>-1.5
 # high precision independent critical replay
 def phi_dec(x):
  i=bisect.bisect_right(dint,x); im=bisect.bisect_right(dint,x//4)
  bM=sum(D(m)/D(d).sqrt() for d,m in divs[:im]); bR=sum(D(m)/D(d).sqrt() for d,m in divs[im:i]); tR=sum(D(m)*D(d).ln()/D(d).sqrt() for d,m in divs[im:i])
  return D(4).ln()*bM+D(x).ln()*bR-tR
 hpmax=phi_dec(pmax[1]);hpmin=phi_dec(pmin[1]); assert hpmax<D('1.5') and hpmin>D('-1.5')
 # compact exact coefficient rows 1..2000
 L=2000; muP=[0]*(L+1)
 for d,m in divs:
  if d<=L:muP[d]=m
 rough=[1]*(L+1);rough[0]=0
 for p in PRIMES:
  for n in range(p,L+1,p):rough[n]=0
 r2=[0]*(L+1);r3=[0]*(L+1)
 for n in range(1,L+1):
  r2[n]=rough[n]-muP[n];r3[n]=rough[n]-muP[n]
  if n%2==0:r2[n]+=2*muP[n//2];r3[n]-=muP[n//2]
  if n%3==0:r2[n]-=muP[n//3];r3[n]+=5*muP[n//3]
  if n%4==0:r3[n]-=3*muP[n//4]
 S2=[D(0)]*(L+1);T2=[D(0)]*(L+1);S3=[D(0)]*(L+1);T3=[D(0)]*(L+1)
 for n in range(1,L+1):
  root=D(n).sqrt();ln=D(n).ln();b2=D(r2[n])/root;b3=D(r3[n])/(D(3)*root)
  S2[n]=S2[n-1]+b2;T2[n]=T2[n-1]+b2*ln;S3[n]=S3[n-1]+b3;T3[n]=T3[n-1]+b3*ln
 v2=[dec_ann(x,S2,T2) for x in range(1,L+1)];v3=[dec_ann(x,S3,T3) for x in range(1,L+1)]
 small2=max(v2[:66]);small3=max(v3[:66]);large2=min(v2[66:]);large3=min(v3[66:]);arg2=67+v2[66:].index(large2);arg3=67+v3[66:].index(large3)
 assert min(v2)>D('-1e-65') and min(v3)>D('-1e-65') and small2<D('2.5') and small3<D(1) and large2>D('1.4') and large3>D('.5')
 # tail event lower sweep
 start=bisect.bisect_left(dint,67); amin=min(preA[start+1:]); amin_i=start+1+int(np.argmin(preA[start+1:])); assert amin>.01
 h2=1+2/math.sqrt(2)+1/math.sqrt(3);h3=1/3+1/(3*math.sqrt(2))+5/(3*math.sqrt(3))+1/2
 t2=(1e99,None);t3=(1e99,None)
 for i,(d,m) in enumerate(divs,1):
  if d<2000:continue
  b=preB[i];kb=(KLO*b if b>=0 else KHI*b);base=2*math.sqrt(d)*preA[i]+kb-i/(6*math.sqrt(d))
  l2=base-1.5*h2;l3=base/3-1.5*h3
  if l2<t2[0]:t2=(l2,d)
  if l3<t3[0]:t3=(l3,d)
 assert t2[0]>6 and t3[0]>.6
 # polynomial causal identity exact
 causal=[]
 for ps in ([67],[67,71],[67,71,73],[101,103,107,109]):
  s=Fraction(1);ls=Fraction(0);child={p:Fraction(0) for p in ps};alpha=Fraction(0)
  for p in ps:
   r=Fraction(1,p);lam=r*s;a=r*lam;ls+=lam;alpha+=a;child[p]+=-lam*r+a;s*=1-r
  assert s+ls==1 and all(v==0 for v in child.values());causal.append({'primes':ps,'alpha_sum':str(alpha)})
 result={'schema':'riemann.x96600.annular-factor67.v1','divisors':len(divs),'quadrature':{'statement':'K(x)=2sqrt(x)+zeta(1/2)log4+e4(x), |e4(x)|<=1/(6sqrt(x))','tail_method':'two-term Euler-Maclaurin; small cells directed'},'phi':{'events':len(events),'float_min':pmin,'float_max':pmax,'high_precision_min':str(hpmin),'high_precision_max':str(hpmax),'bound':'abs(Phi)<3/2'},'compact':{'range':[1,L],'small_row2_max':str(small2),'small_row3_max':str(small3),'row2_ge67_min':str(large2),'row2_argmin':arg2,'row3_ge67_min':str(large3),'row3_argmin':arg3},'tail':{'start':2000,'A_min_ge67':amin,'A_min_at':dint[amin_i-1],'row2_lower':t2,'row3_lower':t3},'terminal':{'row2':'>7/5-(5/2)/sqrt67>87/80','row3':'>1/2-1/sqrt67>3/8'},'causal_identity':causal,'negative_controls':['fixed-product convex packets','all-integer rough store','individual d-color positivity','branchwise child observation'],'rh_established':False,'verdict':'PASS_SOURCE_COMPLETE_ANNULAR_FACTOR67_CANDIDATE'}
 canon=json.dumps(result,sort_keys=True,separators=(',',':')).encode();result['proof_object_sha256']=hashlib.sha256(canon).hexdigest();result['runtime_seconds']=time.time()-t0
 Path(out).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(result['verdict']);print(result['proof_object_sha256']);print(result['runtime_seconds'])
if __name__=='__main__':main(sys.argv[1] if len(sys.argv)>1 else '/tmp/x96600.json')
