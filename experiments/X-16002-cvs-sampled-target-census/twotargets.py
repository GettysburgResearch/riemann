"""Do the SAMPLED-Xi target and the WINDOWED-TRANSFORM target differ, and give different verdicts?"""
from mpmath import mp, mpf, pi, zeta, gamma, exp, cos, quad, nstr
from fractions import Fraction as F
import sympy as sp
mp.dps = 60
def xi_(s): return mpf(1)/2*s*(s-1)*pi**(-s/2)*gamma(s/2)*zeta(s)
def Xi(z): return (xi_(mpf(1)/2 + 1j*mpf(z))).real
def Phi(t):
    t=abs(t); tot=mpf(0)
    for n in range(1,40):
        term=(4*pi**2*n**4*exp(9*t/2)-6*pi*n**2*exp(5*t/2))*exp(-pi*n**2*exp(2*t))
        tot+=term
        if n>3 and abs(term)<mpf(10)**(-45)*max(abs(tot),1): break
    return tot
# F(2 pi j) = 2 * int_0^T Phi(t) cos(2 pi alpha j t) dt,  T = 1/(2 alpha)
def Fwin(alpha, j):
    T = mpf(1)/(2*mpf(alpha))
    return 2*quad(lambda t: Phi(t)*cos(2*pi*mpf(alpha)*j*t), [0, T])

s = sp.symbols('s')
def deficit(vals, N):
    xis = {j: F((-1)**j)*F(mp.nstr(vals[j],50,strip_zeros=False)) for j in range(-N,N+1)}
    P = sp.Integer(0)
    for j in range(-N,N+1):
        t = sp.Integer(1)
        for k in range(-N,N+1):
            if k!=j: t *= (sp.Integer(k)-s)
        P += sp.Rational(xis[j].numerator,xis[j].denominator)*t
    P = sp.Poly(sp.expand(P), s); deg=int(P.degree())
    nre = int(sp.Poly(P.quo(sp.gcd(P,P.diff(s))), s).count_roots())
    same = sum(1 for j in range(-N,N) if xis[j]*xis[j+1] > 0)
    return deg, nre, deg-nre, same

for alpha, N in [(1.0,6),(0.9,6),(1.1,6),(0.8,6)]:
    vs = {j: Xi(2*pi*mpf(alpha)*j) for j in range(-N,N+1)}
    vf = {j: Fwin(alpha, j)        for j in range(-N,N+1)}
    ds = deficit(vs,N); df = deficit(vf,N)
    print(f"alpha={alpha} N={N}")
    print(f"   sampled-Xi      : deg={ds[0]} real={ds[1]} deficit={ds[2]} samesign={ds[3]}  {'PASS' if ds[2]==0 else 'fail'}")
    print(f"   windowed F(2pij): deg={df[0]} real={df[1]} deficit={df[2]} samesign={df[3]}  {'PASS' if df[2]==0 else 'fail'}")
    print(f"   ratio F/Xi at j=0,1,..,{N}: " + ", ".join(nstr(vf[j]/vs[j],5) for j in range(0,N+1)))
    print()
