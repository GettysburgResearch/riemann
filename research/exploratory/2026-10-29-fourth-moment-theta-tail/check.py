#!/usr/bin/env python3
"""Exact independent checks for the six fourth-tail balance faces."""
from fractions import Fraction as F
p = [(F(1,2),F(1),F(4)),(F(1,4),F(1),F(3)),
     (F(11,12),F(1,3),F(2)),(F(2,3),F(1,3),F(1)),
     (F(2,3),F(5,6),F(7,2)),(F(5,12),F(5,6),F(5,2))]
assert [((2*s+3*a)/(3+s),2*s/(3+s),s/(3+s),(-s+3*d)/(3+s)) for a,d,s in p]==[
 (F(19,14),F(8,7),F(4,7),-F(1,7)),(F(9,8),F(1),F(1,2),F(0)),
 (F(27,20),F(4,5),F(2,5),-F(1,5)),(F(1),F(1,2),F(1,4),F(0)),
 (F(18,13),F(14,13),F(7,13),-F(2,13)),(F(25,22),F(10,11),F(5,11),F(0))]
faces=[(-F(29,210),F(17,21),F(25,21)),(F(1,30),F(2,3),F(23,24)),(-F(31,150),F(13,15),F(71,60)),(F(1,30),F(2,3),F(5,6)),(-F(59,390),F(32,39),F(95,78)),(F(1,30),F(2,3),F(32,33))]
for C,E in [(F(7,50),F(21,20)),(F(1925877,15625000),F(19949123,18750000))]:
 cutoffs=[(E-x-y*C)/z for x,y,z in faces]
 b=min(cutoffs); print('C=',C,'b=',b,'value=',float(b),'critical=',cutoffs.index(b)+1)
 assert F(17,10)-4*C-b>0
 if C==F(7,50): assert b==F(223,250)
 else: assert b==F(1357811867,1484375000)
print('All six balanced monomials, minima and mask guard checked.')
