"""Controls: does the pipeline reproduce KNOWN answers?  Separate truncation from aliasing."""
from mpmath import mp, mpf, pi, sin, nstr, polyroots
from fractions import Fraction as F
import sympy as sp
mp.dps = 120
s = sp.symbols('s')

def count(xis, N):
    P = sp.Integer(0)
    for j in range(-N, N+1):
        t = sp.Integer(1)
        for k in range(-N, N+1):
            if k != j: t *= (sp.Integer(k)-s)
        P += sp.Rational(xis[j].numerator, xis[j].denominator)*t
    P = sp.Poly(sp.expand(P), s)
    Psf = P.quo(sp.gcd(P, P.diff(s)))
    return int(P.degree()), int(sp.Poly(Psf, s).count_roots())

def rat(v): return F(mp.nstr(v, 100, strip_zeros=False)) if v != 0 else F(0)

print("CONTROL A - all xi_j > 0.  Nevanlinna guarantees P real-rooted.  Expect deficit 0.")
for N in [4, 6, 8]:
    xis = {j: rat(mpf(1)/(1+mpf(j)**2)) for j in range(-N,N+1)}
    d, r = count(xis, N); print(f"   N={N}: deg={d} real={r} deficit={d-r}  {'OK' if d==r else 'PIPELINE BUG'}")

print()
print("CONTROL B - EXACTLY band-limited, provably real-rooted target: A(z)=sin(g z)/(g z), g<1/2.")
print("   No aliasing possible.  Isolates the effect of TRUNCATION alone.")
for g in [mpf('0.2'), mpf('0.35'), mpf('0.45')]:
    for N in [6, 8, 10]:
        a = {}
        for j in range(-N,N+1):
            x = 2*pi*g*j
            a[j] = mpf(1) if j == 0 else sin(x)/x
        xis = {j: F((-1)**j)*rat(a[j]) for j in range(-N,N+1)}
        d, r = count(xis, N)
        print(f"   gamma={float(g)} N={N}: deg={d} real={r} deficit={d-r}")

print()
print("CONTROL C - band-limited product with several real zeros: A(z)=sin(g z)/(g z) * cos(h z), g+h<1/2.")
from mpmath import cos as mcos
for g,h in [(mpf('0.2'),mpf('0.15')), (mpf('0.25'),mpf('0.2'))]:
    for N in [8, 10]:
        a = {}
        for j in range(-N,N+1):
            x = 2*pi*g*j
            a[j] = (mpf(1) if j==0 else sin(x)/x)*mcos(2*pi*h*j)
        xis = {j: F((-1)**j)*rat(a[j]) for j in range(-N,N+1)}
        d, r = count(xis, N)
        print(f"   g={float(g)} h={float(h)} N={N}: deg={d} real={r} deficit={d-r}")
