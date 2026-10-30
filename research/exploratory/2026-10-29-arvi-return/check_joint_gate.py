"""Scalar comparison at the proposed 0.001-improvement target; see note."""
from fractions import Fraction as F
import runpy
from pathlib import Path
n=runpy.run_path(str(Path(__file__).with_name('check_fixed_face_obstruction.py')))
D=F(223,500);p=F(1,2);q=D*p; selected=2*q
assert (1+D)/2==F(723,1000)
assert selected==D==F(223,500)<F(500001,1000000)
assert (1+D)/2<F(3,4)<F(79,100)
gap=F(9488573505575711579,2031816416850000000000)
h=F(403,500)
reduction=gap/(F(3,4)*h)
assert reduction==F(9488573505575711579,1228233023985825000000)
base=F(137478360780643,225606975000000)
target=base-reduction
assert target==F(122828829151237,204154762500000)
assert n['gap'].subs({n['T']:n['R'](43643617,50000000), n['h']:n['R'](403,500)})==n['R'](gap.numerator,gap.denominator)
print('zero level:',(1+D)/2,'squared selected slope:',selected,'PR93 selected floor:',F(500001,1000000))
print('corner gap:',gap,'≈',float(gap))
print('required count decrease:',reduction,'≈',float(reduction),'target count:',target,'≈',float(target))

r=(1-D)/D
assert r==F(277,223) and r>1
for i in range(8):
 e=D+r**i
 assert e>=1+D
print('contraction multiplier:',r,'>',1)
