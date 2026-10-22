"""Exact real-root count of the CvS interpolation polynomial for the true Xi target."""
from mpmath import mp, mpf, pi, zeta, gamma, nstr
from fractions import Fraction as F
import sympy as sp
mp.dps = 80

def xi_(s): return mpf(1)/2*s*(s-1)*pi**(-s/2)*gamma(s/2)*zeta(s)
def Xi(z): return (xi_(mpf(1)/2 + 1j*mpf(z))).real

def rat(x, digits=50):
    """rationalize an mpf to `digits` significant decimal digits, exactly."""
    if x == 0: return F(0)
    s = mp.nstr(x, digits, strip_zeros=False)
    return F(s)

s = sp.symbols('s')
print(f"{'alpha':>6} {'N':>4} {'deg':>5} {'#real roots (exact Sturm)':>26} {'all real?':>10}  {'#sign changes of xi':>20}")
print("-"*90)
for alpha in ['0.6','0.5','0.4','0.3']:
    a = mpf(alpha)
    for N in [3,4,5,6,7,8]:
        xis = {j: F((-1)**j) * rat(Xi(2*pi*a*j)) for j in range(-N, N+1)}
        # P(s) = sum_j xi_j prod_{k!=j} (k - s)
        P = sp.Integer(0)
        for j in range(-N, N+1):
            term = sp.Integer(1)
            for k in range(-N, N+1):
                if k != j: term *= (sp.Integer(k) - s)
            P += sp.Rational(xis[j].numerator, xis[j].denominator) * term
        P = sp.Poly(sp.expand(P), s)
        deg = P.degree()
        # exact count of distinct real roots
        Psf = P.quo(sp.gcd(P, P.diff(s)))
        nreal = sp.Poly(Psf, s).count_roots()
        seq = [xis[j] for j in range(-N, N+1)]
        sc = sum(1 for i in range(len(seq)-1) if seq[i]*seq[i+1] < 0)
        print(f"{alpha:>6} {N:>4} {int(deg):>5} {int(nreal):>26} {'YES' if nreal==deg else 'NO':>10}  {sc:>20}")
