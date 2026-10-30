"""Exact rational comparison at δ=223/500, p=1/2; not a Lean certificate."""
from pathlib import Path
import re
from fractions import Fraction as F

source=Path('/workspace/scratch/pr94-prepared/submission/src/Submissions/arvi_density/ChainF50/Chain.lean').read_text()
pat=r'theorem (boot|source_\d+) \(hβ[^\n]*\) :\s*QRH\.Record1252270103Source\.GlobalSource \((\d+) / (\d+) : ℝ\) \((\d+) / (\d+) : ℝ\) \((\d+) / (\d+) : ℝ\)'
raw=re.findall(pat,source);assert len(raw)==130
faces=[(x[0],F(int(x[1]),int(x[2])),F(int(x[3]),int(x[4])),F(int(x[5]),int(x[6]))-F(1,100000)) for x in raw]
d,p=F(223,500),F(1,2);V=F(5,6)-d;e=F(1,10**7)
def values(b,l,cap,capped):
 z=cap-e
 D=3-p if capped else 3-p-4*p/l
 A=F(2) if capped else 2-4*p/l
 c0=1-2*p*z if capped else 1-2*p*b/l
 Z=2*p*z if capped else 2*p*b/l
 U=(1-p)*c0;J=V*D+d*(1-p)*A;T=J+d*U
 RN=A*T+(Z-p)*J;DJ=D*J;MN=D*T-RN
 N=(1-d)*J+V*d*U
 # In capped mode the final member of upperM's min gives this upper bound.
 capguard=((b-l*z)/2-e)*DJ-MN
 return N/J,capguard
rank=sorted((values(b,l,c,False)[0],n) for n,b,l,c in faces)
caps=sorted((values(b,l,c,True)[1],n) for n,b,l,c in faces)
assert rank[0][1]=='source_129' and rank[1][1]=='source_128'
assert all(x[0]<0 for x in caps)
print('uncapped top two',rank[:2]);print('uncapped source128 gap',rank[1][0]-rank[0][0],float(rank[1][0]-rank[0][0]))
print('largest relaxed cap upper guard',caps[-1],float(caps[-1][0]))

# Permit arbitrary cap retuning: ignore source cap, floors, all guards except
# MN <= (B-L*z)/2 * DJ. This makes the admissible region larger.
# The upper guard and objective are affine in z on capped branches.
def relaxed(z,b,l):
 D=3-p; A=F(2); c0=1-2*p*z; Z=2*p*z
 U=(1-p)*c0;J=V*D+d*(1-p)*A;T=J+d*U
 RN=A*T+(Z-p)*J;DJ=D*J;MN=D*T-RN
 N=(1-d)*J+V*d*U
 return N/J,(b-l*z)*DJ/2-MN
best=[]
for name,b,l,c in faces:
 n0,g0=relaxed(F(0),b,l); n1,g1=relaxed(F(1),b,l)
 assert g1<g0 and n1<n0
 z=g0/(g0-g1)
 nr,_=relaxed(z,b,l)
 assert nr==values(b,l,c,False)[0]
 best.append((nr,name,z))
best.sort()
print('retuned cap relaxed top two',best[:2])
print('source128 retuned gap',best[1][0]-rank[0][0],float(best[1][0]-rank[0][0]))
assert best[0][0]==rank[0][0] and best[0][1]=='source_129'
