"""Pilot-scale timings, so full-scale runs can be planned rather than guessed.
Every number is wall-clock on this machine, single core. Ordinary timing, no statistics."""
import time, sys, math
sys.path.insert(0,'/home/user/riemann/experiments/X-16001-finsler-cone-collapse')
from verify import inertia
from fractions import Fraction as F
from mpmath import mp, mpf, pi, zeta, gamma, exp, log, sqrt
import sympy as sp
s = sp.symbols('s')

def t(f):
    a=time.time(); r=f(); return r, time.time()-a

def Xi(z, dps):
    with mp.workdps(dps):
        return (mpf(1)/2*(mpf(1)/2+1j*mpf(z))*((mpf(1)/2+1j*mpf(z))-1)*pi**(-(mpf(1)/2+1j*mpf(z))/2)
                *gamma((mpf(1)/2+1j*mpf(z))/2)*zeta(mpf(1)/2+1j*mpf(z))).real

print("=== A. Xi evaluation cost vs precision (per call) ===")
for dps in [50,100,150,250]:
    _,dt = t(lambda: [Xi(2*pi*mpf('0.5')*j, dps) for j in range(1,11)])
    print(f"   dps={dps:>4}: {dt/10*1000:8.1f} ms per Xi call")

print()
print("=== B. exact Sturm real-root count of P vs N (100-digit rational coeffs) ===")
print(f"   {'N':>4} {'deg':>5} {'build P (s)':>12} {'Sturm (s)':>12} {'total (s)':>11}")
prev=None
for N in [4,6,8,10,12]:
    xis = {j: F((-1)**j)*F(mp.nstr(Xi(2*pi*mpf('0.5')*j,150),100,strip_zeros=False)) for j in range(-N,N+1)}
    def build():
        P=sp.Integer(0)
        for j in range(-N,N+1):
            tt=sp.Integer(1)
            for k in range(-N,N+1):
                if k!=j: tt*= (sp.Integer(k)-s)
            P += sp.Rational(xis[j].numerator,xis[j].denominator)*tt
        return sp.Poly(sp.expand(P),s)
    P,tb = t(build)
    def count():
        return int(sp.Poly(P.quo(sp.gcd(P,P.diff(s))),s).count_roots())
    n,tc = t(count)
    tot=tb+tc
    ratio = f"  x{tot/prev:.1f}" if prev else ""
    print(f"   {N:>4} {2*N:>5} {tb:>12.2f} {tc:>12.2f} {tot:>11.2f}{ratio}")
    prev=tot

print()
print("=== C. exact Loewner inertia vs dimension n=2N+1 (rational entries) ===")
print(f"   {'N':>4} {'n':>5} {'inertia (s)':>13}")
for N in [4,6,8,10,12,16]:
    n=2*N+1
    Q=[[F(1,(abs(i-j)+1)*(i+j+2*N+3)) for j in range(-N,N+1)] for i in range(-N,N+1)]
    for i in range(n): Q[i][i]=F(3)
    _,ti = t(lambda: inertia([r[:] for r in Q]))
    print(f"   {N:>4} {n:>5} {ti:>13.2f}")
