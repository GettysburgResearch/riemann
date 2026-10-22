"""High-precision + exact-Sturm study of the CvS target polynomial for the true Xi samples."""
from mpmath import mp, mpf, mpc, pi, zeta, gamma, nstr, polyroots
from fractions import Fraction as F
import sympy as sp
mp.dps = 150
def xi_(s): return mpf(1)/2*s*(s-1)*pi**(-s/2)*gamma(s/2)*zeta(s)
def Xi(z): return (xi_(mpf(1)/2 + 1j*mpf(z))).real

s = sp.symbols('s')

def build(alpha, N, digits=100):
    xis = {}
    for j in range(-N, N+1):
        v = Xi(2*pi*mpf(alpha)*j)
        xis[j] = F((-1)**j)*F(mp.nstr(v, digits, strip_zeros=False))
    P = sp.Integer(0)
    for j in range(-N, N+1):
        term = sp.Integer(1)
        for k in range(-N, N+1):
            if k != j: term *= (sp.Integer(k) - s)
        P += sp.Rational(xis[j].numerator, xis[j].denominator)*term
    return sp.Poly(sp.expand(P), s)

print("HIGH-PRECISION (150 dps) study.  w = 2*pi*alpha*s is the Xi argument; RH strip is |Im w| < 1/2.")
print(f"{'alpha':>6} {'N':>4} {'deg':>5} {'#real (exact Sturm)':>20} {'#nonreal':>9} {'min|Im w|':>14} {'  root w with min |Im w|'}")
print("-"*112)
for alpha in [0.6, 0.5, 0.4, 0.3]:
    for N in [6, 8, 10, 12, 14]:
        P = build(alpha, N)
        deg = int(P.degree())
        Psf = P.quo(sp.gcd(P, P.diff(s)))
        nreal = int(sp.Poly(Psf, s).count_roots())
        coeffs = [mpf(str(c)) if not isinstance(c, sp.Rational) else mpf(c.p)/mpf(c.q)
                  for c in P.all_coeffs()]
        try:
            rts = polyroots(coeffs, maxsteps=800, extraprec=3000)
        except Exception as e:
            print(f"{alpha:>6} {N:>4} {deg:>5} {nreal:>20} {'polyroots failed':>9}"); continue
        nz = [r for r in rts if abs(mp.im(r)) > mpf(10)**(-40)*max(mpf(1), abs(mp.re(r)))]
        if nz:
            ws = [2*pi*mpf(alpha)*r for r in nz]
            best = min(ws, key=lambda w: abs(mp.im(w)))
            print(f"{alpha:>6} {N:>4} {deg:>5} {nreal:>20} {len(nz):>9} {nstr(abs(mp.im(best)),8):>14}   {nstr(best,8)}")
        else:
            print(f"{alpha:>6} {N:>4} {deg:>5} {nreal:>20} {0:>9} {'ALL REAL':>14}")
