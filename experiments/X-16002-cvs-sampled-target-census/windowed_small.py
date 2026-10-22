"""Does the deficit persist for the WINDOWED target as alpha -> 0 (the convergence regime)?"""
from mpmath import mp, mpf, pi, exp, cos, quad, nstr
from fractions import Fraction as F
import sympy as sp
mp.dps = 60
def Phi(t):
    t=abs(t); tot=mpf(0)
    for n in range(1,40):
        term=(4*pi**2*n**4*exp(9*t/2)-6*pi*n**2*exp(5*t/2))*exp(-pi*n**2*exp(2*t))
        tot+=term
        if n>3 and abs(term)<mpf(10)**(-45)*max(abs(tot),1): break
    return tot
def Fwin(alpha, j):
    T = mpf(1)/(2*mpf(alpha))
    return 2*quad(lambda t: Phi(t)*cos(2*pi*mpf(alpha)*j*t), [0, T])
s = sp.symbols('s')
def deficit(vals, N):
    xis = {j: F((-1)**j)*F(mp.nstr(vals[j],45,strip_zeros=False)) for j in range(-N,N+1)}
    P = sp.Integer(0)
    for j in range(-N,N+1):
        t = sp.Integer(1)
        for k in range(-N,N+1):
            if k!=j: t *= (sp.Integer(k)-s)
        P += sp.Rational(xis[j].numerator,xis[j].denominator)*t
    P = sp.Poly(sp.expand(P), s); deg=int(P.degree())
    nre = int(sp.Poly(P.quo(sp.gcd(P,P.diff(s))), s).count_roots())
    return deg, nre, deg-nre
print("WINDOWED target xi_j = (-1)^j F(2 pi j),  F(z)=int_{|t|<=1/(2a)} Phi(t) e^{i a z t} dt")
print(f"{'alpha':>6} {'N':>4} {'deg':>5} {'#real':>6} {'deficit':>8} {'verdict':>8}   (truncation half-width T=1/(2a))")
for alpha in [1.1, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5]:
    for N in [6, 8, 10]:
        vf = {j: Fwin(alpha, j) for j in range(-N,N+1)}
        d = deficit(vf, N)
        print(f"{alpha:>6} {N:>4} {d[0]:>5} {d[1]:>6} {d[2]:>8} {'PASS' if d[2]==0 else 'fail':>8}   T={float(1/(2*alpha)):.4f}")
