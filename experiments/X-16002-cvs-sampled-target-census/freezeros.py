"""Is xi -> P a linear BIJECTION, so the 2N roots of P can be prescribed arbitrarily?
And does the zero-matched target pass?"""
from mpmath import mp, mpf, pi, zetazero, nstr
from fractions import Fraction as F
import sympy as sp
mp.dps = 120
s = sp.symbols('s')

def xi_from_P(P, N):
    """Lagrange inverse: xi_i = P(lambda_i) / prod_{k != i} (lambda_k - lambda_i)."""
    out = {}
    for i in range(-N, N+1):
        num = sp.Rational(P.eval(i))
        den = sp.Integer(1)
        for k in range(-N, N+1):
            if k != i: den *= (k - i)
        out[i] = sp.Rational(num, den)
    return out

def P_from_xi(xis, N):
    P = sp.Integer(0)
    for j in range(-N, N+1):
        t = sp.Integer(1)
        for k in range(-N, N+1):
            if k != j: t *= (sp.Integer(k) - s)
        P += xis[j]*t
    return sp.Poly(sp.expand(P), s)

def count_real(P):
    deg = int(P.degree()); g = sp.gcd(P, P.diff(s))
    return deg, int(sp.Poly(P.quo(g), s).count_roots()), int(sp.Poly(g,s).degree())

print("TEST 1 - can the 2N roots of P be prescribed ARBITRARILY?  (N=5, wild roots)")
N = 5
roots = [sp.Integer(r) for r in (-77777, -4321, -13, -2, -1, 1, 2, 13, 4321, 77777)]
Pt = sp.Poly(sp.expand(sp.prod([(s - r) for r in roots])), s)
xis = xi_from_P(Pt, N)
Pback = P_from_xi(xis, N)
deg, nre, gd = count_real(Pback)
print(f"   prescribed roots: {[int(r) for r in roots]}")
print(f"   round-trip P identical to prescribed? {sp.simplify(Pback.as_expr() - Pt.as_expr()) == 0}")
print(f"   deg={deg}  EXACT #real roots={nre}  deficit={deg-nre}  {'PASS' if nre==deg else 'fail'}")
print(f"   xi even? {all(xis[-i]==xis[i] for i in range(-N,N+1))}   eta^T xi = {sum(xis.values())}")

print()
print("TEST 2 - the ZERO-MATCHED target: prescribe roots at +- gamma_n/(2 pi)")
for N in [4, 6, 8]:
    gam = [mp.im(zetazero(n)) for n in range(1, N+1)]
    rr = []
    for g in gam:
        r = F(mp.nstr(g/(2*pi), 60, strip_zeros=False))
        rr += [sp.Rational(r.numerator, r.denominator), -sp.Rational(r.numerator, r.denominator)]
    Pt = sp.Poly(sp.expand(sp.prod([(s - r) for r in rr])), s)
    xis = xi_from_P(Pt, N)
    Pb = P_from_xi(xis, N)
    deg, nre, gd = count_real(Pb)
    ev = all(xis[-i]==xis[i] for i in range(-N,N+1))
    print(f"   N={N}: deg={deg} EXACT #real={nre} deficit={deg-nre} {'PASS' if nre==deg else 'fail'}"
          f"  xi even? {ev}  eta^T xi != 0? {sum(xis.values())!=0}")
