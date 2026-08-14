#!/usr/bin/env python3
from bisect import bisect_left,bisect_right
from fractions import Fraction
from math import isqrt,prod
from functools import lru_cache
import json,hashlib
from pathlib import Path
PR=(2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61);P=prod(PR);S=10**16;C=2000

def bd(limit):
 v=[(1,1)]
 for q in PR:v += [(d*q,-m) for d,m in list(v) if d*q<=limit]
 return sorted(v)
D=bd(C+8); TH=[d for d,m in D if m==-1 and d<C]; CHILD=sorted({1,67}|{d for d,m in D if d<67})
def ps(n):
 a=bytearray(b'\1')*(n+1);a[:2]=b'\0\0'
 for p in range(2,isqrt(n)+1):
  if a[p]:a[p*p:n+1:p]=b'\0'*((n-p*p)//p+1)
 return [p for p in range(67,n+1) if a[p]]
PRGH=ps(C+7)
@lru_cache(None)
def sq(n):
 lo=isqrt(n*S*S); return lo,lo if lo*lo==n*S*S else lo+1
@lru_cache(None)
def invsq(n):
 lo=isqrt(S*S//n)
 while (lo+1)*(lo+1)*n<=S*S:lo+=1
 return lo,lo if lo*lo*n==S*S else lo+1

def mul(a,b,c,d):
 x=(a*c,a*d,b*c,b*d);return min(x),max(x)
DATA={}
for t in TH:
 sel=[(d,m) for d,m in D if (m==1 and d<=t+8) or (m==-1 and d<=t)]
 ds=[];A=[0];L=[0];H=[0]
 for d,m in sel:
  ds.append(d);A.append(A[-1]+m*(P//d));lo,hi=invsq(d)
  if m==1:L.append(L[-1]+lo);H.append(H[-1]+hi)
  else:L.append(L[-1]-hi);H.append(H[-1]-lo)
 DATA[t]=(ds,A,L,H)
def pref(t,num,den,inc):
 ds,A,L,H=DATA[t]
 lo=0;hi=len(ds)
 while lo<hi:
  mid=(lo+hi)//2
  ok=ds[mid]*den<=num if inc else ds[mid]*den<num
  if ok:lo=mid+1
  else:hi=mid
 return A[lo],L[lo],H[lo]

def eval_state(t,p,kind,n,inc_c,inc_p):
 if kind=='I':
  Ap,Bpl,Bph=pref(t,p*n,1,inc_p);Ac,Bcl,Bch=pref(t,n,1,inc_c)
  ylo,yhi=sq(n);plo,phi=sq(p);rlo,rhi=invsq(p)
  x1lo,x1hi=mul(ylo,yhi,plo,phi);x2lo,x2hi=mul(ylo,yhi,rlo,rhi)
  slope_lo=x1lo*Ap-x2hi*Ac
  const_lo=(-3*Bph*S*P)+(3*mul(rlo,rhi,Bcl,Bch)[0]*P)
  return 4*slope_lo+const_lo,5*slope_lo+const_lo,S*S*P
 else:
  e=n;Ap,Bpl,Bph=pref(t,e,1,inc_p);Ac,Bcl,Bch=pref(t,e,p,inc_c)
  elo,ehi=sq(e);rlo,rhi=invsq(p)
  slope_lo=elo*Ap*S*p-ehi*Ac*S
  const_lo=-3*Bph*S*P*p+3*mul(rlo,rhi,Bcl,Bch)[0]*P*p
  return 4*slope_lo+const_lo,5*slope_lo+const_lo,S*S*P*p

def child_state(t,n,include):
 A,Bl,Bh=pref(t,n,1,include); ylo,yhi=sq(n)
 return 4*ylo*A*S-3*Bh*S*P,5*ylo*A*S-3*Bh*S*P,S*S*P

def check_child_margins():
 mins={4:None,5:None}; checks=0
 for t in TH:
  for idx,n in enumerate(CHILD):
   if n<67:
    a,b,den=child_state(t,n,True); checks+=2
    assert a>0 and b>0,(t,n,'right',a,b)
    for aa,v in ((4,a),(5,b)):
     rec=(Fraction(v,den),t,n,'right',v,den)
     if mins[aa] is None or rec[0]<mins[aa][0]: mins[aa]=rec
   if idx>0:
    a,b,den=child_state(t,n,False); checks+=2
    assert a>0 and b>0,(t,n,'left',a,b)
    for aa,v in ((4,a),(5,b)):
     rec=(Fraction(v,den),t,n,'left',v,den)
     if mins[aa] is None or rec[0]<mins[aa][0]: mins[aa]=rec
 return mins,checks

def bps(t,p):
 low_num=t if t>p else 1; low_den=p if t>p else 1
 pts={('R',t) if t>p else ('I',1),('I',67)}
 for d in CHILD:
  if d*low_den>low_num and d<67:pts.add(('I',d))
 for e,m in D:
  if m==1 and t<e<=t+8 and e*low_den>low_num and e<67*p:pts.add(('R',e))
 def key(z):return z[1]/(p if z[0]=='R' else 1)
 return sorted(pts,key=key)

def main():
 child_mins,child_checks=check_child_margins()
 mins={4:None,5:None};checks=cases=0
 for t in TH:
  assert DATA[t][1][-1]>0
  tail=max(67,t+8); finite=[p for p in PRGH if p<tail]
  for p in finite+[tail]:
   cases+=1; points=bps(t,p)
   for idx,(kind,n) in enumerate(points):
    y=n/(p if kind=='R' else 1)
    if y<67:
     a,b,den=eval_state(t,p,kind,n,True,True);checks+=2
     assert a>0 and b>0,(t,p,kind,n,'R',a,b)
     for aa,v in ((4,a),(5,b)):
      rec=(Fraction(v,den),t,p,kind,n,'right',v,den)
      if mins[aa] is None or rec[0]<mins[aa][0]:mins[aa]=rec
    if idx>0:
     a,b,den=eval_state(t,p,kind,n,False,False);checks+=2
     assert a>0 and b>0,(t,p,kind,n,'L',a,b)
     for aa,v in ((4,a),(5,b)):
      rec=(Fraction(v,den),t,p,kind,n,'left',v,den)
      if mins[aa] is None or rec[0]<mins[aa][0]:mins[aa]=rec
 payload={'classification':'PASS_P61_CAUSAL_COALESCED_TARGET_SCORE_HALL','thresholds':len(TH),'cases':cases,'checks':checks,'child_margin_checks':child_checks,
 'child_target_minimum':{'decimal':float(child_mins[4][0]),'location':list(child_mins[4][1:4]),'lower_fraction':f'{child_mins[4][4]}/{child_mins[4][5]}'},
 'child_score_minimum':{'decimal':float(child_mins[5][0]),'location':list(child_mins[5][1:4]),'lower_fraction':f'{child_mins[5][4]}/{child_mins[5][5]}'},
 'target_minimum':{'decimal':float(mins[4][0]),'location':list(mins[4][1:6]),'lower_fraction':f'{mins[4][6]}/{mins[4][7]}'},
 'score_minimum':{'decimal':float(mins[5][0]),'location':list(mins[5][1:6]),'lower_fraction':f'{mins[5][6]}/{mins[5][7]}'},
 'scope':'P61 exact causal K4/K5 Hall, displacement 8, all p>=67 and 1<=y<67. The infinite prime tail uses positive full reciprocal prefixes and the separately replayed positive child margins. Row gain remains separate.'}
 payload['proof_object_sha256']=hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 out=Path(__file__).resolve().parent/'results'/'verification.json';out.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
 print(json.dumps(payload,indent=2,sort_keys=True))
if __name__=='__main__':main()
