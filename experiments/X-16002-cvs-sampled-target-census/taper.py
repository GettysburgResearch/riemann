"""Where are the 4 residual nonreal roots, and does tapering the truncation remove them?"""
from mpmath import mp, mpf, pi, zeta, gamma, nstr, polyroots, cos, exp
from fractions import Fraction as F
import sympy as sp
mp.dps = 120
def xi_(s): return mpf(1)/2*s*(s-1)*pi**(-s/2)*gamma(s/2)*zeta(s)
def Xi(z): return (xi_(mpf(1)/2 + 1j*mpf(z))).real
s = sp.symbols('s')

def build_xi(alpha, N, taper):
    out = {}
    for j in range(-N, N+1):
        v = Xi(2*pi*mpf(alpha)*j)*taper(j, N)
        out[j] = F((-1)**j)*F(mp.nstr(v, 100, strip_zeros=False)) if v != 0 else F(0)
    return out

def analyse(xis, N, alpha, want_roots=False):
    P = sp.Integer(0)
    for j in range(-N, N+1):
        t = sp.Integer(1)
        for k in range(-N, N+1):
            if k != j: t *= (sp.Integer(k)-s)
        P += sp.Rational(xis[j].numerator, xis[j].denominator)*t
    P = sp.Poly(sp.expand(P), s)
    g = sp.gcd(P, P.diff(s)); Psf = P.quo(g)
    deg = int(P.degree()); nre = int(sp.Poly(Psf, s).count_roots())
    roots = None
    if want_roots and deg <= 40:
        co = [mpf(c.p)/mpf(c.q) if isinstance(c, sp.Rational) else mpf(str(c)) for c in P.all_coeffs()]
        rr = polyroots(co, maxsteps=800, extraprec=4000)
        nz = [2*pi*mpf(alpha)*r for r in rr if abs(mp.im(r)) > mpf(10)**(-40)*max(mpf(1), abs(mp.re(r)))]
        roots = sorted(nz, key=lambda w: (abs(mp.im(w)), abs(mp.re(w))))
    return deg, nre, roots

ONE   = lambda j,N: mpf(1)                                   # hard truncation
FEJER = lambda j,N: mpf(1) - mpf(abs(j))/(N+1)               # triangular / Fejer
HANN  = lambda j,N: (1+cos(pi*mpf(j)/(N+1)))/2               # raised cosine
GAUSS = lambda j,N: exp(-mpf(3)*(mpf(j)/N)**2)               # Gaussian taper
TUKEY = lambda j,N: mpf(1) if abs(j) <= N//2 else (1+cos(pi*(abs(j)-N//2)/(N-N//2+1)))/2

print("PART 1 - location of the residual nonreal roots (hard truncation), in the Xi variable w = 2 pi alpha s")
for alpha, N in [(0.8,10),(0.8,12),(0.9,10),(1.0,8)]:
    deg, nre, roots = analyse(build_xi(alpha,N,ONE), N, alpha, want_roots=True)
    rs = "  ".join(nstr(r,7) for r in roots) if roots else "-"
    print(f"  alpha={alpha} N={N}: deg={deg} real={nre} nonreal={deg-nre}   window |w|<={float(2*pi*alpha*N):.1f}")
    print(f"     nonreal roots: {rs}")

print()
print("PART 2 - does TAPERING the truncation remove them?")
print(f"{'taper':>8} {'alpha':>6} {'N':>4} {'deg':>5} {'#real (exact)':>14} {'deficit':>8} {'VERDICT':>8}")
print("-"*62)
for name, tp in [("hard",ONE),("Fejer",FEJER),("Hann",HANN),("Gauss",GAUSS),("Tukey",TUKEY)]:
    for alpha, N in [(0.8,10),(0.8,12),(1.0,8)]:
        deg, nre, _ = analyse(build_xi(alpha,N,tp), N, alpha)
        print(f"{name:>8} {alpha:>6} {N:>4} {deg:>5} {nre:>14} {deg-nre:>8} {'PASS' if nre==deg else 'fail':>8}")
