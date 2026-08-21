"""Does the CvS finite criterion PASS at N >= N_0(alpha)?  Exact Sturm counts."""
from mpmath import mp, mpf, pi, zeta, gamma, zetazero, nstr, exp
from fractions import Fraction as F
import sympy as sp, math
mp.dps = 120
def xi_(s): return mpf(1)/2*s*(s-1)*pi**(-s/2)*gamma(s/2)*zeta(s)
def Xi(z): return (xi_(mpf(1)/2 + 1j*mpf(z))).real

# Xi zero ordinates (= zeta zero imaginary parts)
ZEROS = [mp.im(zetazero(n)) for n in range(1, 61)]

def predicted_real(alpha, N):
    W = 2*pi*mpf(alpha)*N
    return 2*sum(1 for g in ZEROS if g < W)

s = sp.symbols('s')
def exact_count(alpha, N, digits=100):
    xis = {}
    for j in range(-N, N+1):
        v = Xi(2*pi*mpf(alpha)*j)
        xis[j] = F((-1)**j)*F(mp.nstr(v, digits, strip_zeros=False))
    P = sp.Integer(0)
    for j in range(-N, N+1):
        t = sp.Integer(1)
        for k in range(-N, N+1):
            if k != j: t *= (sp.Integer(k)-s)
        P += sp.Rational(xis[j].numerator, xis[j].denominator)*t
    P = sp.Poly(sp.expand(P), s)
    g = sp.gcd(P, P.diff(s))
    Psf = P.quo(g)
    return int(P.degree()), int(sp.Poly(Psf, s).count_roots()), int(sp.Poly(g,s).degree())

print("PREDICTION: P is real-rooted  <=>  2*#{Xi zeros in |w| <= 2*pi*alpha*N}  >=  deg P = 2N")
print(f"N_0(alpha) = alpha^-1 e^(1+1/alpha):  a=1.0 -> {1*math.exp(2):.1f}   a=0.9 -> {math.exp(1+1/0.9)/0.9:.1f}   a=0.8 -> {math.exp(1+1/0.8)/0.8:.1f}   a=0.7 -> {math.exp(1+1/0.7)/0.7:.1f}")
print()
print(f"{'alpha':>6} {'N':>4} {'deg':>5} {'predicted #real':>16} {'EXACT #real':>12} {'multiple roots':>15} {'VERDICT':>10}")
print("-"*80)
for alpha, Ns in [(1.0,[4,5,6,7,8,10]), (0.9,[6,7,8,9,10,12]), (0.8,[8,9,10,11,12,14])]:
    for N in Ns:
        pr = predicted_real(alpha, N)
        deg, nreal, gdeg = exact_count(alpha, N)
        verdict = "PASS" if nreal == deg else f"fail(-{deg-nreal})"
        print(f"{alpha:>6} {N:>4} {deg:>5} {min(pr,deg):>16} {nreal:>12} {gdeg:>15} {verdict:>10}")
