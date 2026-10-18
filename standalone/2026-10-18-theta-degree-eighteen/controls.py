#!/usr/bin/env python3
"""Complete seven-spin check, directed arithmetic controls, and rejected corruptions.
The 282-spin law is evaluated by exact factorization, not 2**282 enumeration.
No independent mathematical referee or independent transcendental backend.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
from interval_source import I,SCALE,require
from model import evaluate,KS
from certify import certify
ROOT=Path(__file__).resolve().parent

def run():
    count=0
    # Exact rational seven-spin fixture: hub, two signs, two dimers (one newly split).
    z=[F(i+2,20) for i in range(11)]+[F(1,10)]+[F(3,5)]*5+[F(4,5)]
    mult=(1,1,0,0,0,1,1,0,0,0,0)
    _,mom=evaluate(z,True,mult);direct=[F(0)]*19
    for hub,s0,s1,r5,c5,r6,c6 in product((-1,1),repeat=7):
        prob=F(1,2)
        for idx,spin in ((0,s0),(1,s1),(5,r5),(6,r6)):
            m=z[11]*KS[idx]*z[idx];prob*=F(1,2)*(1+m*hub*spin)
        prob*=F(1,2)*(1+(2*z[17]-1)*r5*c5)
        prob*=F(1,2)*(1+(2*z[12]-1)*r6*c6)
        val=z[0]*s0+z[1]*s1+z[5]*(r5+c5)/2+z[6]*(r6+c6)/2
        require(prob>0,'strict positive fixture Gibbs probability');count+=1
        for n in range(19):direct[n]+=prob*val**n
    for n in range(19):require(mom[n]==direct[n],f'complete direct moment {n}');count+=1
    # Interval operations enclose exact rational endpoint extrema.
    for a,b,c,d in product(range(-2,3),repeat=4):
        lo,hi=sorted((F(a,7),F(b,11)));x,y=sorted((F(c,13),F(d,17)))
        A=I(I.coerce(lo).lo,I.coerce(hi).hi);B=I(I.coerce(x).lo,I.coerce(y).hi)
        for V,lower,upper in ((A+B,lo+x,hi+y),(A*B,min(lo*x,lo*y,hi*x,hi*y),max(lo*x,lo*y,hi*x,hi*y))):
            require(F(V.lo,SCALE)<=lower<=upper<=F(V.hi,SCALE),'outward algebra');count+=1
    # Actual certificate failures against temporary parameter changes; no original changes.
    original=(ROOT/'parameters.json').read_bytes();data=json.loads(original)
    certificate=json.loads((ROOT/'CERTIFICATE.json').read_text())
    source={'s':certificate['source_target_intervals'],'bits':320,'cells':98,'explicit_indices':6}
    failures=[]
    try:
        for name in ('old-sign','zero-preconditioner','moved-amplitude','antiferromagnetic'):
            bad=json.loads(original)
            if name=='old-sign':bad['centers'][17]='1'
            elif name=='zero-preconditioner':bad['preconditioner']=[['0']*9 for _ in range(9)]
            elif name=='moved-amplitude':bad['centers'][5]=str(F(bad['centers'][5])+F(1,10**6))
            else:bad['centers'][14]='49/100'
            (ROOT/'parameters.json').write_text(json.dumps(bad))
            try:certify(source)
            except ValueError as ex:failures.append({'mutation':name,'rejected_by':str(ex)})
            else:raise ValueError('mutation incorrectly accepted: '+name)
    finally:(ROOT/'parameters.json').write_bytes(original)
    return {'status':'finite controls only','seven_spin_states':128,'exact_moment_equalities':19,
            'arithmetic_checks':1250,'explicit_predicates':count,'rejected_mutations':failures,
            'same_author_and_backend':True}
if __name__=='__main__':print(json.dumps(run(),sort_keys=True,indent=2))
