"""Exact optimistic 130-face return barrier, not a Lean theorem.

Requires the pinned PR94 Chain.lean. Count-face optimality and the old-branch
comparison are proved separately by check_chain_point.py and
independent_obstruction.py; the latter assumes kappa >= 373/500.
"""
import argparse, hashlib, re
from fractions import Fraction as F
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('--chain',required=True);args=ap.parse_args()
data=Path(args.chain).read_bytes()
assert hashlib.sha256(data).hexdigest()=='ab1fc1b2303404bf57fa2d978ea6b3d7ea3b77e689fc59ff40b50f99e8824570'
pat=r'theorem\s+(boot|source_\d+)\s*\([^\n]*\)\s*:\s*QRH\.Record1252270103Source\.GlobalSource\s*\(\s*(\d+)\s*/\s*(\d+)\s*:\s*ℝ\)\s*\(\s*(\d+)\s*/\s*(\d+)\s*:\s*ℝ\)\s*\(\s*(\d+)\s*/\s*(\d+)\s*:\s*ℝ\)'
raw=re.findall(pat,data.decode());assert [x[0] for x in raw]==['boot']+[f'source_{i:02}' for i in range(1,130)]
faces=[(n,F(int(a),int(b)),F(int(c),int(d))) for n,a,b,c,d,_,_ in raw]
d=F(223,500);p=F(1,2);count=F(137478360780643,225606975000000)
# Exact Formulas.lean rowAt evaluated with the unlimited physical conductor line.
# Giving the scheme this line even where a schedule is unavailable can only
# improve its row estimate, and hence makes the resulting barrier conservative.
def gap(theta,h,B,lam):
 ell=F(11,3)-4*theta;y=h-2*ell
 line=(2*y-(2-B)*h)/lam
 base=F(1,2)+F(13,75)*h-y/2-ell/2-F(9,100)*h+d/2+d*p*(ell-line/2)
 return base+F(3,4)*h*count-theta
h=F(403,500); theta=F(803672422246031,919671258000000)
slopes=[];v=[]
for name,B,lam in faces:
 g=gap(theta,h,B,lam);dt=gap(theta+1,h,B,lam)-g;dh=gap(theta,h+1,B,lam)-g
 assert dt<0 and dh<0,(name,dt,dh)
 assert g>=0,(name,g)
 slopes.append((name,dt,dh));v.append((g,name))
v.sort();assert v[0]==(F(0),'source_66') and v[1][1]=='source_65'
# Each is affine in theta and h, so monotonicity and h<403/500 show that
# every face gives positive return gap whenever theta <= theta*.
print('threshold',theta,'=',float(theta),'limiting source',v[0][1]);print('next gap',v[1],float(v[1][0]));print('validated faces',len(v),'with strict negative theta and h derivatives')
