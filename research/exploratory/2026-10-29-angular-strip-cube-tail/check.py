#!/usr/bin/env python3
from fractions import Fraction as F
for target,C,b in [(F(21,20),F(7,50),F(7779,11165)),(F(19949123,18750000),F(1925877,15625000),F(2504453563,3489062500))]:
 E=F(-11,750)+F(287,330)*C+F(203,150)*b
 assert E==target
 EBK=F(1,30)+F(2,3)*C+F(5,6)*b
 assert EBK<target
 assert b<F(7,5)-2*C
 print('target',target,'b',b,'decimal',float(b),'BK margin',target-EBK)
print('Exact angular-tail core arithmetic passed.')
# General prefix parameter: a=1/2 is the hypothetical GRH-quality endpoint.
a=F(1,2); alpha=F(3,1)/(8-2*a)
for target,C,b in [(F(21,20),F(7,50),F(2433,3245)),(F(19949123,18750000),F(1925877,15625000),F(782027209,1014062500))]:
 E=F(1,30)+F(6,5)*(2*alpha-1)+(F(115,66)-F(20,11)*alpha)*C+(F(11,6)-alpha)*b
 assert E==target
 assert F(1,30)+F(2,3)*C+F(5,6)*b<target
 print('hypothetical GRH prefix target',target,'b',b)
