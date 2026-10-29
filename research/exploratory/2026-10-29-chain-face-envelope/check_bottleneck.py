"""Exact pointwise scan of pinned ChainF50 count faces, including all cap z."""
import argparse, hashlib, re
from fractions import Fraction as F
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--chain',required=True);a=p.parse_args();data=Path(a.chain).read_bytes()
assert hashlib.sha256(data).hexdigest()=='ab1fc1b2303404bf57fa2d978ea6b3d7ea3b77e689fc59ff40b50f99e8824570'
pat=r'theorem\s+(boot|source_\d+)\s*\([^\n]*\)\s*:\s*QRH\.Record1252270103Source\.GlobalSource\s*\(\s*(\d+)\s*/\s*(\d+)\s*:\s*ℝ\)\s*\(\s*(\d+)\s*/\s*(\d+)\s*:\s*ℝ\)\s*\(\s*(\d+)\s*/\s*(\d+)\s*:\s*ℝ\)'
raw=re.findall(pat,data.decode());assert len(raw)==130 and [x[0] for x in raw]==['boot']+[f'source_{i:02}' for i in range(1,130)]
faces=[(n,F(int(bn),int(bd)),F(int(ln),int(ld)),F(int(cn),int(cd))) for n,bn,bd,ln,ld,cn,cd in raw]
delta=F(223,500);p=F(1,2);v=F(5,6)-delta;eps=F(1,10**7);sm=F(3,100);mm=F(377,1000);nat=(1-F(9,2)*sm)/2

def branch(B,L,cap,z=None):
 capped=z is not None
 D=3-p if capped else 3-p-4*p/L;A=F(2) if capped else 2-4*p/L
 C=1-2*p*(z if capped else B/L);Z=1-C;U=(1-p)*C;J=v*D+delta*(1-p)*A;T=J+delta*U;RN=A*T+(Z-p)*J;DJ=D*J;MN=D*T-RN
 low=mm+eps if capped else max(mm+eps,(B-L*(cap-eps))/2+eps)
 upper=[F(11,25)-eps,nat-eps,(B-L*(z if capped else sm+eps))/2-eps]
 dD=-1 if capped else -1-4/L; dA=0 if capped else -4/L;dC=-2*z if capped else -2*B/L;dU=-C+(1-p)*dC;dJ=v*dD+delta*(-A+(1-p)*dA)
 guards=[D,A,C,J,T-J,F(12499,10000)*J-T,RN-F(23,37)*DJ,DJ-RN,MN-low*DJ,*[u*DJ-MN for u in upper],(1-delta)*J+v*delta*U-(1-2*delta*nat-2*delta*p*sm)*J,U*dJ-dU*J,F(11,25)-nat-eps,B-2*nat-L*(sm+eps)-2*eps,(z-sm-eps)*DJ if capped else F(1)]
 return (1-delta+v*delta*U/J,guards)

uncap=[];caps=[];fail=[]
for name,B,L,source_cap in faces:
 cap=min(F(9999,100000),source_cap-eps)
 R,guards=branch(B,L,cap)
 if all(x>0 for x in guards):uncap.append((R,name,B,L))
 # Each capped guard is affine in z at this δ,p; find strict interval exactly.
 _,g0=branch(B,L,cap,F(0));_,g1=branch(B,L,cap,F(1));_,g2=branch(B,L,cap,F(2))
 assert all(c==2*b-a for a,b,c in zip(g0,g1,g2)),name
 lo=sm+eps;hi=source_cap-eps
 for A,B1 in zip(g0,g1):
  slope=B1-A
  if slope>0:lo=max(lo,-A/slope)
  elif slope<0:hi=min(hi,-A/slope)
  elif A<=0:hi=lo
 if hi>lo:
  Rhi,_=branch(B,L,cap,hi); caps.append((Rhi,name,lo,hi))
 else:fail.append(name)
assert uncap and caps
best=min(uncap)
print('faces',len(faces),'admissible uncapped',len(uncap),'cap feasible',len(caps))
for r in sorted(uncap)[:8]: print('uncap',r[1],'R',r[0],'=',float(r[0]))
for r in sorted(caps)[:8]: print('cap infimum',r[1],'R',r[0],'=',float(r[0]),'zmax',r[3], '=',float(r[3]))
assert best[1]=='source_129'
assert all(r[0]>=best[0] for r in caps)
print('No freely capped branch beats the admissible final C point; caps are strict, their endpoints are optimistic infima.')
