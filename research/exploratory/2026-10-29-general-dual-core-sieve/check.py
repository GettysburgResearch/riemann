#!/usr/bin/env python3
from fractions import Fraction as F
p=F(6,5)
targets=[(F(21,20),F(7,50),F(1421,2150)),(F(19949123,18750000),F(1925877,15625000),F(458975011,671875000))]
for target,C,b in targets:
 assert F(49,120)+(17*C+43*b)/48==target
 # max(5d+12k) = 85C/11 at d=k=5C/11.
 assert 6-7*b-F(85,11)*C>0
 assert target-(F(9,10)+F(10,11)*C)>0
 assert b < F(7,5)-2*C  # nonempty-root ceiling even with k=0
 assert b < 3*(p-C)      # remaining Θ face, k=0 is worst
 print('target',target,'b',b,'decimal',float(b),'G guard margin',6-7*b-F(85,11)*C,'low margin',target-(F(9,10)+F(10,11)*C))
for target,C,b in [(F(21,20),F(7,50),F(27,40)),(F(19949123,18750000),F(1925877,15625000),F(8699123,12500000))]:
 assert F(1,30)+F(5,6)*C+F(4,3)*b==target
 d=k=F(5,11)*C
 assert d+F(6,5)*k==C
 assert d/6+F(17,30)*k==C/3
 print('core-restricted',target,'b',b,'decimal',float(b))
for C,b,expected in [(F(7,50),F(27,40),F(17,528)),(F(1925877,15625000),F(8699123,12500000),F(24207893,825000000))]:
 d=k=F(5,11)*C
 assert (6-5*d-12*k-7*b)/6==expected
print('Exact core maxima, guards and margins passed.')
