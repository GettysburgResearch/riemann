#!/usr/bin/env python3
"""Independent complete seven-spin Gibbs enumeration, not a theta/zero census."""
import itertools,json,sys
from fractions import Fraction as F
import loop_model as m

def need(ok,msg):
 if not ok:raise ValueError(msg)

def run(mutation=None):
 z=[F(i+4,30) for i in range(11)]+[F(1,100)]+[F(3,5)]*6+[F(0)]
 selected=(0,2,7,9);mult=tuple(int(i in selected) for i in range(11))
 weights=[F(0)];edges=[];roots={}
 for i in selected:
  roots[i]=len(weights);weights.append(z[i] if i<5 else z[i]/2)
  edges.append((0,roots[i],z[11]*m.KS[i]*z[i]))
  if i>=5:
   child=len(weights);weights.append(z[i]/2)
   p=z[17] if i==5 else z[12+i-6]
   edges.append((roots[i],child,2*p-1))
 need(len(weights)==7 and len(edges)==6,'complete base tree')
 cases=[];checks=0
 for pair in [(7,9),(2,7)]:
  for q in [F(0),F(1,11),F(1,3)]:
   z[18]=q
   wsum=F(0);mom=[F(0)]*21
   for spins in itertools.product((-1,1),repeat=7):
    w=F(1)
    for i,j,b in edges:w*=1+b*spins[i]*spins[j]
    w*=1+q*spins[roots[pair[0]]]*spins[roots[pair[1]]]
    y=sum(a*s for a,s in zip(weights,spins));wsum+=w
    power=F(1)
    for j in range(21):mom[j]+=w*power;power*=y
   expected=[v/wsum for v in mom]
   zm=z[:]
   if mutation=='wrong-edge-sign':zm[18]=-q
   if mutation=='erase-edge':zm[18]=0
   _,actual=m.evaluate(zm,pair,True,mult)
   if mutation=='erase-normalizer':
    a,b=pair;normalizer=1+q*(z[11]*m.KS[a]*z[a])*(z[11]*m.KS[b]*z[b]);actual=[v*normalizer for v in actual]
   if mutation=='drop-moment20':actual[20]=0
   for j in range(21):need(actual[j]==expected[j],f'raw moment {pair},{q},{j}');checks+=1
   cases.append({'pair':list(pair),'q':str(q),'states':128,'moments':21})
 # Algebraic lower-moment compensation cannot be dropped, even in dimension one.
 J=F(2);h=F(3);high_x=F(5);high_q=F(7)
 response=high_q if mutation=='erase-compensation' else high_q-high_x*h/J
 need(response==F(-1,2),'compensated derivative toy identity');checks+=1
 return {'status':'PASS: complete finite algebra controls','moment_equalities':checks-1,'other_identities':1,'cases':cases}
if __name__=='__main__':print(json.dumps(run(sys.argv[1] if len(sys.argv)>1 else None),sort_keys=True,indent=2))
