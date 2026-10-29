#!/usr/bin/env python3
from fractions import Fraction as F
p=F(6,5)
def values(b):
 g=(5*p-7*b)/8
 K=(5*p+17*b)/16
 D=p-g
 return g,K,[b,D,5*b/6+D/3,b/3+5*D/6]
for b in (p/3, p*F(5,7)):
 g,K,terms=values(b)
 assert g>=0 and all(x<=K for x in terms)
 # The old theta term 3b/2+g/2 is exactly K.
 assert 3*b/2+g/2==K
for target,expected in [(F(21,20),F(154,215)),(F(19949123,18750000),F(12292873,16796875))]:
 b=(target-F(49,120))*F(48,43)
 assert b==expected and p/3<=b<=p*F(5,7)
 assert F(49,120)+F(43,48)*b==target
 print('target',target,'b',b,'decimal',float(b))
print('All exact endpoint and threshold identities passed.')
