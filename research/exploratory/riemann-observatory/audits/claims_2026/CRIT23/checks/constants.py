# Recompute the optimisation constants of CRIT23 sources from their stated formulas.
import mpmath as mp
from fractions import Fraction as Fr
mp.mp.dps = 40
s2 = mp.sqrt(2)
u = 1/s2
CMT = mp.mpf(1)/2 + u*mp.cot(u)
print("C_MT = 1/2 + cot(1/sqrt2)/sqrt2      =", mp.nstr(CMT, 20))
print("2 - C_MT  (simple & on line)        =", mp.nstr(2-CMT, 20))
print("(3 - C_MT)/2 (distinct)             =", mp.nstr((3-CMT)/2, 20))
print("Lamzouri C0 = 3/2 - cot(1/s2)/s2    =", mp.nstr(mp.mpf(3)/2 - u*mp.cot(u), 20))
C2 = (5 + 2*s2 - 2*CMT)/(3+2*s2)
print("Lamzouri C2 = (5+2s2-2CMT)/(3+2s2)  =", mp.nstr(C2, 20))
C2b = (1 + 2*s2 + 2*(2-CMT))/(3+2*s2)
print("  abstract form (1+2s2+2C0)/(3+2s2) =", mp.nstr(C2b, 20))
print("BGSTB25 box value (2+C0)/3          =", mp.nstr((2+(2-CMT))/3, 20))
# Lean's cMT
t = mp.tan(u)
cMT = s2*t/(1+u*t)
print("A-F Lean cMT = s2 tan/(1+tan/s2); 1/cMT =", mp.nstr(1/cMT, 20), " 2-1/cMT=", mp.nstr(2-1/cMT,20), " 3/2-1/(2cMT)=", mp.nstr(mp.mpf(3)/2-1/(2*cMT),20))

# R(psi) of A-F (5.13) by direct quadrature
def R(psi):
    I1 = mp.quad(lambda x: psi(x), [-0.5, 0.5])
    I2 = mp.quad(lambda x: psi(x)**2, [-0.5, 0.5])
    # int int |u-v| psi(u) psi(v) = int_{-1}^{1} |w| (psi*psi)(w) dw ; compute directly
    I3 = mp.quad(lambda x, y: abs(x-y)*psi(x)*psi(y), [-0.5, 0.5], [-0.5, 0.5], maxdegree=8)
    return (I2 + I3)/I1**2
R0 = R(lambda x: mp.mpf(1))
RMT = R(lambda x: mp.cos(s2*x))
print("R(psi0) quadrature =", mp.nstr(R0, 15), "(claimed 4/3)")
print("R(psiMT) quadrature=", mp.nstr(RMT, 15), "(claimed C_MT)", " diff", mp.nstr(RMT-CMT, 5))
# Stationarity check of MT: G(u)=psi(u)+int|u-v|psi(v)dv constant on (-1/2,1/2)
G = lambda x: mp.cos(s2*x) + mp.quad(lambda v: abs(x-v)*mp.cos(s2*v), [-0.5, x, 0.5])
print("G(u) at u=0,0.2,0.45:", [mp.nstr(G(mp.mpf(z)),15) for z in (0,0.2,0.45)])
# Remark 6.1: H(lambda)=2-1/lambda-lambda/3
H = lambda l: 2-1/l-l/3
print("H(1)=", H(mp.mpf(1)), " H(0.9)=", mp.nstr(H(mp.mpf('0.9')),10), " argmax unconstrained=sqrt(3)")
# Christoffel claim, A-F 7.2(f): moments 1,1,4/3,2,13/4 -> Lambda_2(0)=5/36, 13/18
import sympy as sp
m = [sp.Integer(1), sp.Integer(1), sp.Rational(4,3), sp.Integer(2), sp.Rational(13,4)]
Hk = sp.Matrix(3,3, lambda i,j: m[i+j])
v = sp.Matrix([1,0,0])
lam = 1/ (v.T*Hk.inv()*v)[0]
print("Christoffel Lambda_2(0) =", lam, "; 1-Lambda =", 1-lam, "; 2(1-Lambda)-1 =", 2*(1-lam)-1)
