"""Independent audit of PR94 fixed-face obstruction; pass exact Windows.lean path."""
import argparse, hashlib, re
from fractions import Fraction as F
import sympy as s

a=argparse.ArgumentParser(); a.add_argument('--windows',required=True); args=a.parse_args()
source=open(args.windows,'rb').read(); digest=hashlib.sha256(source).hexdigest(); assert digest=='3d436434bf8a76f2246f12bb942840f33e4d8ce3d2155660e4572dccab15a799'; print('Windows.lean SHA-256:',digest)
text=source.decode(); pattern=r'def returnWindow(\d+) : ReturnCountWindow where\s+branch := \.(\w+)\s+nonold := by decide\s+deltaLo := \(([^:]+):ℝ\)\s+deltaHi := \(([^:]+):ℝ\)\s+pLo := \(([^:]+):ℝ\)'
windows=re.findall(pattern,text);assert len(windows)==31
D=F(223,500); p=F(1,2); active=[(int(i),n) for i,n,lo,hi,p0 in windows if F(lo)<=D<=F(hi) and F(p0)<=p<=F(1,2)]
assert active==[(7,'C'),(12,'C'),(14,'C'),(15,'C'),(16,'C'),(17,'C')]
# The ordered declared list really does contain exactly these 31 items.
listing=re.search(r'def returnWindows : List ReturnCountWindow := \[(.*?)\]',text,re.S)
assert listing and re.findall(r'returnWindow(\d+)',listing.group(1))==[f'{i:02}' for i in range(1,32)]
B=F(96232839,100000000); L=F(3853,2000); PB=F(49283557,50000000); PL=F(4503,2000);z=F(9999,100000)-F(1,10000000);V=F(5,6)-D
# C source is the actual, uncapped affine moment.
Dc=3-p-4*p/L;Ac=2-4*p/L;Uc=(1-p)*(1-2*p*B/L);Jc=V*Dc+D*(1-p)*Ac;Rc=1-D+V*D*Uc/Jc
assert Rc==F(137478360780643,225606975000000) and Jc>0
# capC guard 9 is the strict upper plain-length condition.
Dcap=3-p;Acap=2;Ucap=(1-p)*(1-2*p*z);Jcap=V*Dcap+D*(1-p)*Acap;Tcap=Jcap+D*Ucap;Rnum=Acap*Tcap+(2*p*z-p)*Jcap;Mnum=Dcap*Tcap-Rnum;DJ=Dcap*Jcap
naturalM=(1-F(9,2)*F(3,100))/2;eps=F(1,10000000);upper=min(F(11,25)-eps,naturalM-eps,(B-L*z)/2-eps)
g9=upper*DJ-Mnum; assert g9==F(-600197344421,48000000000000) and g9<0
# old−C = positive constant * (linear positive)/(linear positive).
k=s.symbols('k',real=True);kr=s.Rational;Vx=kr(V.numerator,V.denominator);dx=kr(D.numerator,D.denominator)
oldD=3-kr(1,2)-2*kr(1,2)/(3*k);oldA=2*(1-kr(1,2))*(1-kr(1,2)/(3*k));oldJ=Vx*oldD+dx*oldA;old=1-dx+dx*oldA*Vx/(2*oldJ)
rc=kr(Rc.numerator,Rc.denominator);diff=s.factor(old-rc)
expected=kr(129563)*(126347807631*k-49067153209)/(225606975000000*(12729*k-1831));assert s.simplify(diff-expected)==0
assert 126347807631*F(373,500)-49067153209>0 and 12729*F(373,500)-1831>0
# Give full conductor-line capacity, with no cap; this only lowers rowAt.
t,h=s.symbols('t h',real=True);pB=kr(PB.numerator,PB.denominator);pL=kr(PL.numerator,PL.denominator);ell=kr(11,3)-4*t;y=h-2*ell;line=(2*y-(2-pB)*h)/pL
base=kr(1,2)+kr(13,75)*h-y/2-ell/2-kr(9,100)*h+dx/2+dx*kr(1,2)*(ell-line/2)
gap=s.factor(base+kr(3,4)*h*rc-t);hs=s.factor(s.diff(gap,h));ts=s.factor(s.diff(gap,t));assert hs==-kr(11447677710517817,1354544277900000000);assert ts==-kr(5273419,1125750);assert hs<0 and ts<0
v=s.factor(gap.subs({t:kr(87386,100000),h:kr(806,1000)}));assert v==kr(88261806706387247,2031816416850000000000) and v>0
print('active windows:',active,'C count:',Rc)
print('capC upper-plain guard:',g9,'old−C positive for k>=373/500')
print('derivatives:',hs,ts,'upper-corner gap:',v,'≈',float(v))
star=kr(8317278773899883959247,9517760867980200000000)
assert gap.subs({t:star,h:kr(806,1000)})==0
assert kr(873,1000)<kr(87386,100000)<star<kr(7,8)
print('exact threshold:',star,'≈',float(star),'; strict h < 0.806 makes gap positive at theta <= threshold')
