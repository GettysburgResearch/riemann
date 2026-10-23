"""Finite rational bookkeeping checks; analytic identities are separate inputs."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
count=0
def require(ok,label):
    global count
    if not ok:raise ArithmeticError(label)
    count+=1

branches=[]
for a in range(1,6):
    for eps in (0,1):
        v=a+eps
        local=[]
        if (v+1)%6:local.append((v+1,F(-1-eps),'nonprincipal'))
        if v>=5:local.append((6,F(-2-eps if v==5 else -eps),'Ramanujan'))
        for j,omega,kind in local:
            # Exponents of q in four local weights, after the limiting
            # Rankin powers 0,1,1/2,0 of the label norm q^a.
            ex=[omega,omega+j-a-a,omega+F(2*j,3)-F(5*a,6)-F(a,2),omega+F(j,6)-F(a,3)]
            for x in ex:require(x<=-1,'sixth-free local Rankin threshold')
            branches.append([a,eps,j,str(omega),kind])
        j=v%6
        for selected in (False,True):
            if selected and j==5:continue
            core=F(j-6 if selected else j,12)
            require(core-F(23*eps,12)<=F(a,12),'primitive nonvolume fixed prime')
            require(core-F(11*eps,12)<=F(a,12),'first partial pole fixed prime')
            require(core-F(7*eps,12)<=F(a,12),'second partial pole fixed prime')

# S2 after Y=D^(5/6)K^(7/6), on 1/7<=logK/logD<=1.
for k in (F(1,7),F(1)):
    y=F(5,6)+F(7,6)*k;target=F(5,9)+F(7,9)*k
    terms=[F(2,3)*y,F(5,6)-y/6,2*k-y/3,F(5,6)+F(7,6)*k-y/3,
           1+2*k-F(4,3)*y,1+F(7,6)*k-y/2]
    for e in terms:require(e<=target,'optimized residue scale')
# Every difference just checked is affine in k, so endpoints cover the interval.

h=F(6,7);k=F(1,32)
terms=[h+k,F(11,12)+F(13,12)*k,h/3+F(2,3)]
target=F(20,21);old=h/6+F(5,6)
for e in terms:require(e<=target,'whole-projection benchmark')
require(old-target==F(1,42),'strict power saving')
for upper in ((2*h-1)/13,F(5,6)*(1-h),F(1,7),h/2):
    require(k<upper,'projection domain strict margin')
require(max(terms)>F(9,10),'false projection target rejected')

alpha=F(14,15)
cutoffs=[2-2*alpha,F(4,5)-F(7,10)*alpha,F(7,12)-alpha/2,F(3,7)-F(5,14)*alpha]
require(max(cutoffs)==F(11,75),'quartic conditional tail budget')
require(F(11,75)<F(4,27),'new tail budget comparison')
out={'status':'PASS','rational_predicates':count,'sixth_free_local_branches':branches,
     'projection_benchmark':{'U_exponent':str(h),'K_exponent':str(k),
       'terms':[str(x) for x in terms],'bound':str(target),'old_resource':str(old),'saving':str(old-target)},
     'quartic_conditional_cutoff':str(max(cutoffs)),
     'scope':'finite exponents and affine-domain coverage only; no analytic theorem or fixed boundary certified',
     'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_name('STRUCTURAL_EXPONENT_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
