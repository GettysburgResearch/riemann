"""Exact prime-5 Fourier orientation check; no analytic-estimate acceptance."""
import json

DEG = 8

def add(a, b):
    return tuple(x+y for x,y in zip(a,b))

def neg(a):
    return tuple(-x for x in a)

def mul(a,b):
    p=[0]*15
    for i,x in enumerate(a):
        for j,y in enumerate(b): p[i+j]+=x*y
    # Phi_20 = X^8-X^6+X^4-X^2+1.
    for j in range(14,7,-1):
        c=p[j]
        p[j]=0
        for off,sgn in ((2,1),(4,-1),(6,1),(8,-1)):
            p[j-off]+=sgn*c
    return tuple(p[:8])

ONE=(1,0,0,0,0,0,0,0)
ZERO=(0,)*8
X=(0,1,0,0,0,0,0,0)
def power(n):
    a=ONE
    for _ in range(n%20): a=mul(a,X)
    return a

# i=zeta_20^5.  In F_5, chi(1,2,3,4)=(1,-i,i,-1).
chi_exp={1:0,2:3,3:1,4:2}
def chi(k,sign=1):
    if k%5==0:return ZERO
    return power(5*sign*chi_exp[k%5])

def gauss(k,sign=1):
    a=ZERO
    for x in range(1,5):
        # DDHL additive character is e(-2*x/5), hence zeta_20^(-8*x).
        a=add(a,mul(chi(x,sign),power(-8*k*x)))
    return a

checks=0
def require(ok,message):
    global checks
    if not ok: raise RuntimeError(message)
    checks+=1

require(power(20)==ONE,"cyclotomic period")
require(gauss(1)!=ZERO and gauss(1,-1)!=ZERO,"nonzero primitive roots")
for k in range(5):
    require(gauss(k)==mul(chi(k,-1),gauss(1)),"native Fourier scaling")
    require(gauss(k,-1)==mul(chi(k),gauss(1,-1)),"inverse Fourier scaling")
    require(gauss(k**3)==mul(chi(k),gauss(1)),"cubic numerator repair")
require(chi(2)!=chi(2,-1),"quadratic mismatch at k=2")
require(mul(gauss(2,-1),gauss(1)) != mul(gauss(2),gauss(1,-1)),
        "wrong native-k identification must fail")
require(mul(gauss(2,-1),gauss(1)) == mul(gauss(8),gauss(1,-1)),
        "native-k-cubed identification")
print(json.dumps({"status":"pass","scope":"exact prime-5 physical/native quartic Fourier orientation",
                  "totalchecks":checks,"negativecontrols":["native-k scalar identification rejected"],
                  "analytic_estimate_certified":False},sort_keys=True))
