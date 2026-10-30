from fractions import Fraction as F
from pathlib import Path
import re,hashlib
chain=Path('/workspace/scratch/pr94-prepared/submission/src/Submissions/arvi_density/ChainF50/Chain.lean')
assert hashlib.sha256(chain.read_bytes()).hexdigest()=='ab1fc1b2303404bf57fa2d978ea6b3d7ea3b77e689fc59ff40b50f99e8824570'
formulas=chain.parent.parent/'Return'/'Formulas.lean'
assert hashlib.sha256(formulas.read_bytes()).hexdigest()=='e7dfed2c335372dde5a609ec2b53bf268d6fe7c40807bdb7ee83c5d7f3f3216b'
s=chain.read_text()
pat=r'theorem (boot|source_\d+)\s*\(hβ.*?:\s*QRH\.Record1252270103Source\.GlobalSource\s*\((\d+)\s*/\s*(\d+)\s*:\s*ℝ\)\s*\((\d+)\s*/\s*(\d+)\s*:\s*ℝ\)\s*\((\d+)\s*/\s*(\d+)\s*:\s*ℝ\)'
data=[(name,F(int(a),int(b)),F(int(c),int(d)),F(int(e),int(f))) for name,a,b,c,d,e,f in re.findall(pat,s)]
assert len(data)==130
S=F(3,100); nat=(1-F(9,2)*S)/2; eps=F(1,10**7); mm=F(377,1000)
def candidate(d,p,b,l,cap,iscap):
 v=F(5,6)-d;z=cap-eps
 dd=3-p if iscap else 3-p-4*p/l
 aa=F(2) if iscap else 2-4*p/l
 c0=1-2*p*z if iscap else 1-2*p*b/l
 zz=2*p*z if iscap else 2*p*b/l
 u=(1-p)*c0;j=v*dd+d*(1-p)*aa;T=j+d*u
 rn=aa*T+(zz-p)*j; mn=dd*T-rn; dj=dd*j
 low=mm+eps if iscap else max(mm+eps,(b-l*(cap-eps))/2+eps)
 high=min(F(11,25)-eps,nat-eps,(b-l*(z if iscap else S+eps))/2-eps)
 derd=-1 if iscap else -1-4/l; dera=0 if iscap else -4/l
 derc=-2*z if iscap else -2*b/l
 deru=-c0+(1-p)*derc; derj=v*derd+d*(-aa+(1-p)*dera)
 n=(1-d)*j+v*d*u
 guard=[dd,aa,c0,j,T-j,F(12499,10000)*j-T,rn-F(23,37)*dj,dj-rn,mn-low*dj,high*dj-mn,n-(1-2*d*nat-2*d*p*S)*j,u*derj-deru*j,F(11,25)-nat-eps,b-2*nat-l*(S+eps)-2*eps,(z-S-eps)*dj if iscap else 1]
 return n/j,guard
D=F(223,500);P=F(1,2)
arr=[]
for name,b,l,c in data:
 for iscap in (False,True):
  z,g=candidate(D,P,b,l,c-eps,iscap)
  if min(g)>=0:arr.append((z,name,iscap))
print('source count:',len(data),'admitted point branches:',len(arr))
for z,name,iscap in sorted(arr)[:12]: print('best',name,'cap' if iscap else 'uncap',f'{float(z):.12f}','exact',z)
print('admissible physical slopes:',sum(F(2)<=l<=F(9,2) for _,b,l,c in data))
q=F(8738694,10**7);H=F(80599,100000); C=1-q;ell=4*C-F(1,3);y=H-2*ell;lo=F(19,25);hi=H+F(1,10**10);cap=F(619,10000)
lines=[]
for name,b,l,scap in data:
 if F(2)<=l<=F(9,2) and 0<b<=1 and 0<=1-b/2-(F(9,2)-l/2)*cap and cap<=scap:
  lines.append((name,2*y/l,-(2-b)/l))
changes={lo,hi}
for _,b,m in lines:
 if cap!=m:
  x=b/(cap-m)
  if lo<x<hi: changes.add(x)
for _,b1,m1 in lines:
 for _,b2,m2 in lines:
  if m1!=m2:
   x=(b2-b1)/(m1-m2)
   if lo<x<hi: changes.add(x)
xs=sorted(changes)
parts=[]
for u,v in zip(xs,xs[1:]):
 d=(u+v)/2
 name,b,m=max(lines,key=lambda t:t[1]+t[2]*d)
 iscap=b+m*d >= cap*d
 key='cap' if iscap else name
 if parts and parts[-1][0]==key:parts[-1]=(key,parts[-1][1],v)
 else:parts.append((key,u,v))
print('physical eligible incl lambda and small-plain:',len(lines))
print('upper envelope by d, including cap-crossing subdivision:')
for name,u,v in parts:print(name,f'{float(u):.12f}',f'{float(v):.12f}')
print('top three capacities at endpoint:')
for name,b,m in sorted(lines,key=lambda z: z[1]+z[2]*hi,reverse=True)[:3]:print(name, float(min(cap*hi,b+m*hi)))
line_by_name={name:(b,m) for name,b,m in lines}
b64,m64=line_by_name['source_64'];b66,m66=line_by_name['source_66']
for d in (lo,hi):
 gap=(b66+m66*d)-(b64+m64*d)
 assert gap>0
 print('66 minus 64 uncapped line at',str(d),'is',str(gap),'=',f'{float(gap):.12g}')
