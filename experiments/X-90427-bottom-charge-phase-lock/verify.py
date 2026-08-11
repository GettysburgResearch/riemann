#!/usr/bin/env python3
from fractions import Fraction
import json, sys

def mobius(n):
    x=n; parity=0; p=2
    while p*p<=x:
        if x%p==0:
            x//=p; parity^=1
            if x%p==0: return 0
            while x%p==0: x//=p
        p+=1
    if x>1: parity^=1
    return -1 if parity else 1

def beta(n,q):
    return Fraction((n//q)*(q-1-(n%q)),n+1)

omega_poly={1:Fraction(1),2:Fraction(-3,2),4:Fraction(1,2)}
full_poly={1:Fraction(1),2:Fraction(-15,2),4:Fraction(35,2),8:Fraction(-15),16:Fraction(4)}
adjoint={1:Fraction(1),2:Fraction(-6),4:Fraction(8)}

def conv_poly(a,b):
    out={}
    for m,x in a.items():
        for n,y in b.items(): out[m*n]=out.get(m*n,Fraction(0))+x*y
    return {n:x for n,x in out.items() if x}
assert conv_poly(omega_poly,adjoint)==full_poly

def source(poly,n):
    return sum((a*mobius(n//d) for d,a in poly.items() if n%d==0),Fraction(0))

for m in range(1,129,2):
    mu=mobius(m)
    expected=[mu,Fraction(-5,2)*mu,2*mu,Fraction(-1,2)*mu]
    got=[source(omega_poly,(2**a)*m) for a in range(4)]
    assert got==expected
    for a in range(4,8): assert source(omega_poly,(2**a)*m)==0

Komega={n:sum((source(omega_poly,q)*beta(n,q) for q in range(2,n+1)),Fraction(0)) for n in range(2,65)}
assert Komega[2]==Fraction(-5,6) and Komega[3]==Fraction(-1,2)
assert all(Komega[n]==0 for n in range(4,65))

Kstar={n:sum((source(full_poly,q)*beta(n,q) for q in range(2,n+1)),Fraction(0)) for n in range(2,65)}
for n in range(2,65):
    if n==2: want=Fraction(-17,6)
    elif n==3: want=Fraction(-1,2)
    elif 4<=n<=7: want=Fraction(101-11*n,n+1)
    elif 8<=n<=15: want=Fraction(4*(n-31),n+1)
    else: want=Fraction(0)
    assert Kstar[n]==want

assert sum(full_poly.values())==0
assert sum(Fraction(n)*a for n,a in full_poly.items())==0

# Formal three-scale relation: adjoint source layers imply coefficients 1,-3sqrt(2),4
# after the q^(-1/2) scaling of delta_2 and delta_4.
assert adjoint[1]==1
assert adjoint[2]*Fraction(1,2)==-3  # coefficient after extracting 1/sqrt(2), leaving sqrt(2)
assert adjoint[4]*Fraction(1,2)==4

result={
  "classification":"PASS_X_90427_BOTTOM_CHARGE_PHASE_LOCK_BRIDGE",
  "odd_core_rows":64,
  "omega_layer_checks":512,
  "omega_carry_rows":63,
  "phase_locked_carry_rows":63,
  "phase_locked_nonzero_rows":14,
  "source_moment_checks":2,
  "deterministic_rh_proved":False,
  "scope":"exact source, dyadic-layer, carry-image, and critical-adjoint algebra only"
}
path=None
if "--json" in sys.argv: path=sys.argv[sys.argv.index("--json")+1]
text=json.dumps(result,indent=2,sort_keys=True)+"\n"
if path: open(path,"w").write(text)
else: print(text,end="")
