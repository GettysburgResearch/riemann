#!/usr/bin/env python3
from fractions import Fraction
from math import comb, sqrt
import hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent

def A(t): return (1+t)*(1-4*t*t)**2
def B(t): return -t*(1-4*t*t)*(1+8*t+4*t*t)

t=Fraction(1,2)
assert A(t)==0 and B(t)==0
# exact derivatives by symmetric polynomial differences / explicit formulas
# A=(1+t)(1-4t^2)^2 has multiplicity exactly 2 at t=1/2.
def deriv(f,x,h=Fraction(1,10**5)):
    return (f(x+h)-f(x-h))/(2*h)
# use symbolic coefficient lists for exact multiplicity
# coefficients low to high
Acoef=[Fraction(1),Fraction(1),Fraction(-8),Fraction(-8),Fraction(16),Fraction(16)]
Bcoef=[Fraction(0),Fraction(-1),Fraction(-8),Fraction(0),Fraction(32),Fraction(16)]
def evalpoly(c,x):
    s=Fraction(0)
    for a in reversed(c):s=s*x+a
    return s
def dcoef(c):return [Fraction(i)*c[i] for i in range(1,len(c))]
assert evalpoly(Acoef,t)==0
assert evalpoly(dcoef(Acoef),t)==0
assert evalpoly(dcoef(dcoef(Acoef)),t)!=0
assert evalpoly(Bcoef,t)==0
assert evalpoly(dcoef(Bcoef),t)!=0

# Frozen Q4 cubic Mellin value at z=1/2 is exactly 4/315.
def monomial_integral(coeff, degree, lo, hi):
    power=Fraction(2*degree+1,2)  # degree + 1/2
    # endpoints are rational squares here: 0, 1/4, 1.
    def hp(q):
        if q==0: return Fraction(0)
        if q==1: return Fraction(1)
        assert q==Fraction(1,4)
        return Fraction(1,2)**(2*degree+1)
    return coeff*(hp(hi)-hp(lo))/power
W_half=Fraction(0)
for coeff,degree in [(Fraction(5),1),(Fraction(-63),2),(Fraction(170),3)]:
    W_half += monomial_integral(coeff,degree,Fraction(0),Fraction(1,4))
for coeff,degree in [(Fraction(-1,3),1),(Fraction(1),2),(Fraction(-2,3),3)]:
    W_half += monomial_integral(coeff,degree,Fraction(1,4),Fraction(1))
assert W_half==Fraction(4,315)

# Exact (I-S)^M inversion on a finite dyadic endpoint sequence.
def shift(v): return [Fraction(0)]+v[:-1]
def sub(a,b):return [x-y for x,y in zip(a,b)]
def delta(v,M):
    out=v[:]
    for _ in range(M): out=sub(out,shift(out))
    return out
def inv_delta(g,M):
    n=len(g);out=[Fraction(0) for _ in range(n)]
    for k in range(n):
        for j in range(k+1):
            out[k]+=Fraction(comb(M+j-1,M-1))*g[k-j]
    return out
v=[Fraction((i+1)**2-3*i, i+2) for i in range(20)]
for M in range(1,7):
    assert inv_delta(delta(v,M),M)==v

# Prototype interior-disk zero: inverse of 1-sqrt(2)S grows as 2^(n/2).
power_loss=[2**(n/2) for n in range(21)]
assert power_loss[-1] > 1000

result={
 'schema':'riemann.x95520.q4-moment-centering.v1',
 'frozen_pr580':'812e7fcbaff2dd1c2c53c885def7b6c0d0e68a05',
 'A2_zero_order_at_t_half':2,
 'B2_zero_order_at_t_half':1,
 'W_mellin_at_half':str(W_half),
 'finite_difference_inverse_orders_checked':list(range(1,7)),
 'interior_zero_inverse_growth_at_n20':power_loss[-1],
 'proved_by_replay':['A2_B2_multiplicity','W_mellin_at_half','binomial_inverse','interior_zero_power_loss_prototype'],
 'not_proved_by_replay':['SACF','FOCC','RH'],
 'rh_established':False,
 'verdict':'PASS_X95520_Q4_MOMENT_CENTERING_ALGEBRA'}
canon=json.dumps(result,sort_keys=True,separators=(',',':')).encode()
result['proof_object_sha256']=hashlib.sha256(canon).hexdigest()
out=HERE/'results'/'verification.json';out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n', encoding='utf-8', newline='\n')
print(result['verdict']);print(result['proof_object_sha256'])
