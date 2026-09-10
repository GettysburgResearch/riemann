#!/usr/bin/env python3
"""Bounded independent rational controls, not the infinite positivity proof."""
from fractions import Fraction as Q
import json
from intervals import I,S,PI,LOG2,GAMMA,P2,BERN,exp_i,log_pos,sincos,psi_real
from verify import strict_equal,reject_pairs
counts={}
def check(group,condition):
    if not condition:raise ValueError('control failed: '+group)
    counts[group]=counts.get(group,0)+1

def contains(x,y):return x.low()<=y<=x.high()
vals=[Q(n,d) for n in range(-3,4) for d in range(1,5)]
for x in vals:
 for y in vals:
    check('rational-add',contains(I(x)+I(y),x+y))
    check('rational-product',contains(I(x)*I(y),x*y))
    if y:check('rational-quotient',contains(I(x)/I(y),x/y))
for x in range(-3,3):
 for y in range(x,4):
  for a in range(-2,3):
   for b in range(a,3):
    z=I.raw(x*S,y*S)*I.raw(a*S,b*S)
    check('interval-corners',all(contains(z,Q(p*q)) for p in [x,y] for q in [a,b]))
for n in range(-12,13):
 si,co=sincos(PI*n/2)
 check('quadrant-sine',contains(si,Q([0,1,0,-1][n%4])))
 check('quadrant-cosine',contains(co,Q([1,0,-1,0][n%4])))
for n in range(-6,7):
 check('exp-reciprocal',contains(exp_i(Q(n,3))*exp_i(Q(-n,3)),Q(1)))
check('exp-straddle',contains(exp_i(I.raw(-1,1)),Q(1)))
check('exp-zero',contains(exp_i(0),Q(1)))
check('exp-source-range',Q(8,3)<exp_i(1).low() and exp_i(1).high()<Q(11,4))
check('log-range',Q(69,100)<LOG2.low() and LOG2.high()<Q(7,10))
check('gamma-range',Q(1,2)<GAMMA.low() and GAMMA.high()<Q(3,5))
check('P2-range',Q(569,1000)<P2.low() and P2.high()<Q(57,100))
check('bernoulli',BERN[2]==Q(1,6) and BERN[4]==Q(-1,30) and BERN[40]==Q(-261082718496449122051,13530))
for a in [Q(1),Q(5,4),Q(3,2)]:
 for t in [0,1,10]:
    z=psi_real(a+1,t)-psi_real(a,t)-I(a)/(a*a+t*t)
    check('psi-recurrence-overlap',contains(z,Q(0)))
# This is a normalization check for the length4 Fourier pairing:
# H=1/4 sum(1+w^2)|psihat|^2; |pair|^2<=H*sum|hhat|^2/(1+w^2)/4.
for h in [(Q(1),Q(2)),(Q(-3),Q(1,2))]:
 for p in [(Q(1),Q(1)),(Q(2),Q(-1))]:
    ww=[Q(1),Q(5)];pair=sum(hh*pp for hh,pp in zip(h,p))/4
    hn=sum(hh*hh/w for hh,w in zip(h,ww));pn=sum(pp*pp*w for pp,w in zip(p,ww))/4
    check('periodic-dual-factor',pair*pair<=pn*hn/4)
for a,b in [(True,1),(False,0),(2049,2049.0),({'a':True},{'a':1}),([False],[0])]:
 check('strict-json-types',not strict_equal(a,b))
try:json.loads('{"a":1,"a":2}',object_pairs_hook=reject_pairs)
except ValueError:check('duplicate-json-rejected',True)
else:raise ValueError('duplicate accepted')
for x in [1.0,True]:
 try:I(x)
 except TypeError:check('inexact-input-rejected',True)
 else:raise ValueError('inexact interval accepted')
print(json.dumps({'status':'PASS_BOUNDED_CONTROLS','counts':counts,'total':sum(counts.values()),'not_a_kernel_proof':True},indent=2,sort_keys=True))
