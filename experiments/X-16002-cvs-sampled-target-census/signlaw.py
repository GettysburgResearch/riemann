"""THE SIGN-CHANGE LAW:  #real roots of P  ==  #same-sign adjacent pairs of xi."""
from mpmath import mp, mpf, pi, zeta, gamma, sin, cos, nstr
from fractions import Fraction as F
import sympy as sp
mp.dps = 120
def xi_(s): return mpf(1)/2*s*(s-1)*pi**(-s/2)*gamma(s/2)*zeta(s)
def Xi(z): return (xi_(mpf(1)/2 + 1j*mpf(z))).real
s = sp.symbols('s')
def rat(v): return F(mp.nstr(v, 100, strip_zeros=False)) if v != 0 else F(0)
def count(xis, N):
    P = sp.Integer(0)
    for j in range(-N,N+1):
        t = sp.Integer(1)
        for k in range(-N,N+1):
            if k!=j: t *= (sp.Integer(k)-s)
        P += sp.Rational(xis[j].numerator, xis[j].denominator)*t
    P = sp.Poly(sp.expand(P), s)
    Psf = P.quo(sp.gcd(P,P.diff(s)))
    return int(P.degree()), int(sp.Poly(Psf,s).count_roots())

print(f"{'family':>14} {'params':>16} {'deg=2N':>7} {'same-sign pairs':>16} {'EXACT #real':>12} {'match?':>7}")
print("-"*80)
cases = []
for alpha in [0.3,0.5,0.6,0.8,0.9,1.0]:
    for N in [6,8,10]:
        cases.append(("Xi", f"alpha={alpha},N={N}", alpha, N, "xi"))
for g in [0.2,0.35,0.45]:
    for N in [6,8]:
        cases.append(("sinc", f"gamma={g},N={N}", g, N, "sinc"))
for N in [5,7]:
    cases.append(("positive", f"N={N}", None, N, "pos"))

ok = 0
for fam, lab, prm, N, kind in cases:
    if kind == "xi":
        a = {j: Xi(2*pi*mpf(prm)*j) for j in range(-N,N+1)}
    elif kind == "sinc":
        a = {j: (mpf(1) if j==0 else sin(2*pi*mpf(prm)*j)/(2*pi*mpf(prm)*j)) for j in range(-N,N+1)}
    else:
        a = {j: (-1)**j * mpf(1)/(1+mpf(j)**2) for j in range(-N,N+1)}
    xis = {j: F((-1)**j)*rat(a[j]) for j in range(-N,N+1)}
    same = sum(1 for j in range(-N,N) if xis[j]*xis[j+1] > 0)
    deg, nre = count(xis, N)
    good = (same == nre)
    ok += good
    print(f"{fam:>14} {lab:>16} {deg:>7} {same:>16} {nre:>12} {'YES' if good else 'NO':>7}")
print(f"\nLAW HELD IN {ok}/{len(cases)} CASES")
