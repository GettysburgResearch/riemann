import argparse
import hashlib
import re
import json
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--windows", required=True, help="Path to PR94 pinned Return/Windows.lean")
parser.add_argument("--certificate", help="Write exact edge-leaf data as JSON")
args = parser.parse_args()
expected_sha256 = "3d436434bf8a76f2246f12bb942840f33e4d8ce3d2155660e4572dccab15a799"
assert hashlib.sha256(Path(args.windows).read_bytes()).hexdigest() == expected_sha256, "Unexpected PR94 window source"

"""Rational Bernstein check of the PR94 scalar return candidate; see README."""
import sympy as s

D,P=s.symbols('D P'); R=s.Rational
B=R(96232839,10**8); L=R(3853,2000); cap=R(9999,100000); PB=R(49283557,50000000); PL=R(4503,2000); PC=R(31,500)
theta=R(87386926,10**8);h=R(80599,100000); c=1-theta; ell=4*c-R(1,3); x=1+ell-h;y=h-2*ell;k=1-2*c;dm=R(19,25);dp=h+R(1,10**10); eps=R(1,10**7);sm=R(3,100);mm=R(377,1000);nat=(1-R(9,2)*sm)/2
physicalB2=R(98507071,10**8); physicalL2=R(4483,2000)
edges=[(R(1,200), min(R(1,200),2*y-R(1,200))/(6*k)), (dm,min(dm,2*y-dm)/(6*k)), (dm,min(R(619,10000)*dm,(2*y-(2-physicalB2)*dm)/physicalL2)),(dp,min(R(619,10000)*dp,(2*y-(2-physicalB2)*dp)/physicalL2))]
windows = [
    ('capP', R('9/32'), R('3/8'), R('3/8')),
    ('capP', R('9/32'), R('21/64'), R('7/16')),
    ('capC', R('21/64'), R('3/8'), R('7/16')),
    ('capP', R('3/8'), R('27/64'), R('3/8')),
    ('capP', R('3/8'), R('51/128'), R('13/32')),
    ('capP', R('51/128'), R('27/64'), R('13/32')),
    ('C', R('27/64'), R('15/32'), R('3/8')),
    ('capC', R('3/8'), R('51/128'), R('7/16')),
    ('weakC7', R('397/1000'), R('27/64'), R('43/100')),
    ('capC', R('3/8'), R('51/128'), R('15/32')),
    ('weakC7', R('51/128'), R('27/64'), R('15/32')),
    ('C', R('27/64'), R('15/32'), R('7/16')),
    ('C', R('27/64'), R('57/128'), R('15/32')),
    ('C', R('57/128'), R('15/32'), R('15/32')),
    ('C', R('57/128'), R('117/256'), R('31/64')),
    ('C', R('57/128'), R('231/512'), R('63/128')),
    ('C', R('57/128'), R('459/1024'), R('127/256')),
    ('C', R('459/1024'), R('231/512'), R('127/256')),
    ('C', R('459/1024'), R('921/2048'), R('255/512')),
    ('C', R('459/1024'), R('1839/4096'), R('511/1024')),
    ('C', R('459/1024'), R('3675/8192'), R('1023/2048')),
    ('C', R('3675/8192'), R('1839/4096'), R('1023/2048')),
    ('C', R('3675/8192'), R('7353/16384'), R('2047/4096')),
    ('C', R('7353/16384'), R('1839/4096'), R('2047/4096')),
    ('C', R('1839/4096'), R('921/2048'), R('511/1024')),
    ('C', R('921/2048'), R('231/512'), R('255/512')),
    ('C', R('231/512'), R('117/256'), R('63/128')),
    ('C', R('117/256'), R('15/32'), R('31/64')),
    ('C', R('15/32'), R('33/64'), R('7/16')),
    ('C', R('33/64'), R('69/128'), R('15/32')),
    ('capP', R('69/128'), R('141/256'), R('31/64')),
]
windows.append(('capC', R(39,100), R(3971,10000), R(43,100)))
assert len(windows) == 32
windows.append(("Cnew", R(11,25), R(9,20), R(49,100)))

source_hashes = {'Formulas.lean': 'e7dfed2c335372dde5a609ec2b53bf268d6fe7c40807bdb7ee83c5d7f3f3216b', 'Constants.lean': '96f2a770b68bc4d3ba34e896995514c040315dbc8584e19dbfe479dced8ce4b7', 'CountWindow.lean': '21fb4e2c88be82e3f14cbdc3eec69f55650f42cc188d6c314cc78e80c3f1ebe3'}
for name, digest in source_hashes.items():
 assert hashlib.sha256((Path(args.windows).parent / name).read_bytes()).hexdigest() == digest, name
source_text = Path(args.windows).read_text()
pattern = r'def returnWindow(\d+) : ReturnCountWindow where\s+branch := \.(\w+)\s+nonold := by decide\s+deltaLo := \(([^:]+):ℝ\)\s+deltaHi := \(([^:]+):ℝ\)\s+pLo := \(([^:]+):ℝ\)'
parsed = re.findall(pattern, source_text)
assert len(parsed) == 31
assert [int(i) for i,*_ in parsed] == list(range(1, 32))
source_windows = [(n, R(lo), R(hi), R(pl)) for _,n,lo,hi,pl in parsed]
listing = re.search(r'def returnWindows : List ReturnCountWindow := \[(.*?)\]', source_text, re.S)
assert listing and re.findall(r'returnWindow(\d+)', listing.group(1)) == [f'{i:02}' for i in range(1, 32)]
expected_windows = windows[:31].copy()
expected_windows[8] = ('weakC7', R(51,128), R(27,64), R(7,16))
assert source_windows == expected_windows, "Transcribed window list differs from pinned source"

branches=[('old',0,1,R(1,25)),('C',B,L,cap),('capC',B,L,cap),('weakC7',B-R(7,4000),L,cap),('capP',PB,PL,PC),('Cnew',R(962272712,10**9),R(192583,100000),cap)]

def coeff(e):
 p=s.Poly(e,D,P); return [(int(a),int(b),q) for (a,b),q in p.terms()]
def calc(cs,d,p):
 # Bernstein convex hull on [a,b] x [c,d] via exact rational arithmetic.
 a,b=d; c,e=p; wd=b-a; wp=e-c
 max_i=max(i for i,j,q in cs); max_j=max(j for i,j,q in cs)
 temp={}
 for k in range(max_i+1):
  for l in range(max_j+1):
   temp[k,l]=sum((q*int(s.binomial(i,k))*a**(i-k)*wd**k*int(s.binomial(j,l))*c**(j-l)*wp**l for i,j,q in cs if i>=k and j>=l),R(0))
 values=[]
 for i in range(max_i+1):
  for j in range(max_j+1):
   q=sum((temp[k,l]*int(s.binomial(i,k))/int(s.binomial(max_i,k))*int(s.binomial(j,l))/int(s.binomial(max_j,l)) for k in range(i+1) for l in range(j+1)),R(0))
   values.append(q)
 return min(values)

certificates = []
for idx,(dist,C) in enumerate(edges):
 checks=[]
 for name,b,l,capb in branches:
  V=R(5,6)-D
  if name=='old':
   dd=3-P-2*P/(3*k);aa=2*(1-P)*(1-P/(3*k)); J=V*dd+D*aa; N=(1-D)*J+D*aa*V/2;guards=[J]
  else:
   ic=name in ('capC','capP');z=capb-eps;dd=3-P if ic else 3-P-4*P/l;aa=2 if ic else 2-4*P/l;c0=1-2*P*z if ic else 1-2*P*b/l;zz=2*P*z if ic else 2*P*b/l;U=(1-P)*c0;J=V*dd+D*(1-P)*aa;T=J+D*U;rn=aa*T+(zz-P)*J;mn=dd*T-rn;dj=dd*J
   low=mm+eps if ic else max(mm+eps,(b-l*(capb-eps))/2+eps);high=min(R(11,25)-eps,nat-eps, (b-l*(z if ic else sm+eps))/2-eps); derd=-1 if ic else -1-4/l;dera=0 if ic else -4/l;derc=-2*z if ic else -2*b/l;deru=-c0+(1-P)*derc;derj=V*derd+D*(-aa+(1-P)*dera);N=(1-D)*J+V*D*U
   guards=[dd,aa,c0,J,T-J,R(12499,10000)*J-T,rn-R(23,37)*dj,dj-rn,mn-low*dj,high*dj-mn,N-(1-2*D*nat-2*D*P*sm)*J,U*derj-deru*J,R(11,25)-nat-eps,b-2*nat-l*(sm+eps)-2*eps,(z-sm-eps)*dj if ic else 1]
  base=R(1,2)+R(13,75)*h-y/2-ell/2-R(9,100)*dist+D/2+D*P*(ell-C/2)
  margin=(theta-R(1,10**8)-base)*J-R(3,4)*dist*N
  checks.append((name,[coeff(e) for e in guards],coeff(margin)))
 if idx==3:
  admission_tests=[('weakC7',R(397,1000),R(27,64),R(43,100)),('capC',R(39,100),R(3971,10000),R(43,100)),('Cnew',R(11,25),R(9,20),R(49,100))]
  for nm,lo,hi,pl in admission_tests:
   guards=next(g for n,g,m in checks if n==nm)
   vals=[calc(g,(lo,hi),(pl,R(1,2))) for g in guards]
   assert all(v>0 for v in vals), (nm,vals)
   print('full window admission',nm,'minimum',str(min(vals)),flush=True)
 stack=[(R(0),R(3,4),R(0),R(1,2),0)]; leaves=0; nodes=0; maxdep=0; names={}; certificate_leaves=[]
 while stack:
  a,b,c,d,dep=stack.pop();nodes+=1
  da=(a,b);pa=(c,d)
  valid=False
  for name,guards,mar in checks:
   matched = [i + 1 for i,(n,lo,hi,pl) in enumerate(windows) if name==n and a>=lo and b<=hi and c>=pl]
   if name!='old' and not matched:
    continue
   guard_mins=[calc(g,da,pa) for g in guards]
   margin_min=calc(mar,da,pa)
   if all(v>=0 for v in guard_mins) and margin_min>=0:
    certificate_leaves.append({'box':[str(a),str(b),str(c),str(d)],'branch':name,'window':matched[0] if matched else None,'guard_bernstein_minima':[str(v) for v in guard_mins],'margin_bernstein_minimum':str(margin_min)})
    valid=True;names[name]=names.get(name,0)+1;break
  if valid: leaves+=1;maxdep=max(maxdep,dep);continue
  if dep>40:raise RuntimeError((idx,dep,a,b,c,d))
  if dep%2==0:
   m=(a+b)/2;stack.extend([(a,m,c,d,dep+1),(m,b,c,d,dep+1)])
  else:
   m=(c+d)/2;stack.extend([(a,b,c,m,dep+1),(a,b,m,d,dep+1)])
  if nodes%10000==0:print('working',idx,nodes,dep,flush=True)
 print('edge',idx,'nodes',nodes,'leaves',leaves,'maxdepth',maxdep,'branches',names,flush=True)
 certificates.append({'index':idx,'distance':str(dist),'capacity':str(C),'leaves':certificate_leaves})
if args.certificate:
 Path(args.certificate).write_text(json.dumps({'source_windows_sha256':expected_sha256,'theta':str(theta),'h':str(h),'reserve':'1/100000000','edges':certificates},indent=2)+'\n')
