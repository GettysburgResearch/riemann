from mpmath import mp, mpf, pi, zeta, gamma, sin, nstr
from fractions import Fraction as F
import sympy as sp
mp.dps = 80
def xi_(s): return mpf(1)/2*s*(s-1)*pi**(-s/2)*gamma(s/2)*zeta(s)
def Xi(z): return (xi_(mpf(1)/2 + 1j*mpf(z))).real

print("A. Does the truncated cardinal series F(z) = sum_j a_j sinc((z-2pi j)/2pi) approximate Xi(alpha z)?")
print("   a_j = Xi(2 pi alpha j).  Testing at non-sample points.")
for alpha in [mpf('0.5'), mpf('0.3')]:
    for N in [8, 16, 30]:
        a = {j: Xi(2*pi*alpha*j) for j in range(-N,N+1)}
        def Fser(z):
            tot = mpf(0)
            for j in range(-N,N+1):
                d = (z - 2*pi*j)/2
                tot += a[j]*(sin(d)/d if d != 0 else mpf(1))
            return tot
        errs=[]
        for z in [mpf('1.3'), mpf('4.7'), mpf('9.1'), mpf('20.0')]:
            errs.append(abs(Fser(z)-Xi(alpha*z)))
        print(f"   alpha={float(alpha)} N={N:>3}: max |F(z)-Xi(alpha z)| over test pts = {nstr(max(errs),6)}   (Xi(0)={nstr(Xi(0),6)})")

print()
print("B. Precision stability of the exact real-root count (alpha=0.5, N=6): vary rationalization digits")
s = sp.symbols('s')
alpha = mpf('0.5'); N = 6
for digits in [20, 30, 40, 50, 60]:
    xis = {}
    for j in range(-N,N+1):
        v = Xi(2*pi*alpha*j)
        xis[j] = F((-1)**j)*F(mp.nstr(v, digits, strip_zeros=False))
    P = sp.Integer(0)
    for j in range(-N,N+1):
        term = sp.Integer(1)
        for k in range(-N,N+1):
            if k!=j: term *= (sp.Integer(k)-s)
        P += sp.Rational(xis[j].numerator, xis[j].denominator)*term
    P = sp.Poly(sp.expand(P), s)
    Psf = P.quo(sp.gcd(P,P.diff(s)))
    print(f"   digits={digits:>3}: degree={int(P.degree())}, distinct real roots={int(sp.Poly(Psf,s).count_roots())}")
