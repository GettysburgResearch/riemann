"""Exact local and affine bookkeeping for the physical-support refinement."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json

count=0;branches=[]
def require(ok,label):
    global count
    if not ok:raise ArithmeticError(label)
    count+=1

for a in range(1,6):
    for eps in (0,1):
        v=a+eps;local=[]
        if (v+1)%6:local.append((v+1,F(-1-eps),'nonprincipal'))
        if v>=5:local.append((6,F(-2-eps if v==5 else -eps),'principal'))
        for j,w,kind in local:
            ex=[w,w+F(j,2)-a,w+F(5*j,12)-F(5*a,6),w+F(j,6)-F(a,3)]
            for e in ex:require(e<=-1,'local L-Rankin exponent')
            require(j>=2,'nontrivial local modulus is powerful')
            branches.append({'a':a,'epsilon':eps,'j':j,'omega':str(w),'kind':kind,'exponents':list(map(str,ex))})

for k in (F(0),F(1,7)):
    base=F(11,12)+k/12
    for term in [(1+k)/2,F(1,4)+F(5,4)*k,F(5,6)+k/6]:
        require(term<=base,'all-scale dominated cost')
    for h in ((1+k)/2,F(1),F(2)):
        cutoff=h/6-(1+k)/12
        require(F(1,4)+F(3,4)*k-h/4+F(3,2)*cutoff==F(1,8)+F(5,8)*k,'mixed volume head')
        require(k/2+h/4-F(3,2)*cutoff==F(1,8)+F(5,8)*k,'mixed volume tail')

h=F(6,7);k=F(1,12)
terms=[h+k,F(11,12)+k/12,F(5,6)+k,F(2,3)+h/3]
require(max(terms)==F(20,21),'hypothetical primitive benchmark')
require(F(5,6)+h/6-max(terms)==F(1,42),'hypothetical saving')
require(F(5,6)+F(1,7)==F(5,6)+h/6,'natural label endpoint is equality at h=6/7')
out={'status':'PASS','checks':count,'local_branches':branches,
     'scope':'finite local and affine exponent checks only; primitive extension is not proved by this script',
     'conditional_primitive_benchmark':{'h':str(h),'k':str(k),'terms':list(map(str,terms))},
     'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
print(json.dumps(out,indent=2))
