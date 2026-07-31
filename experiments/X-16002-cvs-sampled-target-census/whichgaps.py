"""WHICH node gaps fail to contain a root of P?  Prediction: the low-frequency ones, where Xi has no zeros."""
from mpmath import mp, mpf, pi, zeta, gamma, nstr, polyroots
from fractions import Fraction as F
import sympy as sp
mp.dps = 150
def xi_(s): return mpf(1)/2*s*(s-1)*pi**(-s/2)*gamma(s/2)*zeta(s)
def Xi(z): return (xi_(mpf(1)/2 + 1j*mpf(z))).real
s = sp.symbols('s')

def study(alpha, N):
    a = {j: Xi(2*pi*mpf(alpha)*j) for j in range(-N,N+1)}
    xis = {j: F((-1)**j)*F(mp.nstr(a[j],100,strip_zeros=False)) for j in range(-N,N+1)}
    P = sp.Integer(0)
    for j in range(-N,N+1):
        t = sp.Integer(1)
        for k in range(-N,N+1):
            if k!=j: t *= (sp.Integer(k)-s)
        P += sp.Rational(xis[j].numerator, xis[j].denominator)*t
    P = sp.Poly(sp.expand(P), s)
    co = [mpf(c.p)/mpf(c.q) if isinstance(c,sp.Rational) else mpf(str(c)) for c in P.all_coeffs()]
    rts = polyroots(co, maxsteps=900, extraprec=4000)
    real = sorted(mp.re(r) for r in rts if abs(mp.im(r)) <= mpf(10)**(-40)*max(mpf(1),abs(mp.re(r))))
    nonreal = [r for r in rts if abs(mp.im(r)) > mpf(10)**(-40)*max(mpf(1),abs(mp.re(r)))]
    # which gaps (j, j+1) contain a real root?
    empty = []
    for j in range(-N, N):
        cnt = sum(1 for x in real if mpf(j) < x < mpf(j+1))
        if cnt == 0: empty.append(j)
    return len(rts), len(real), len(nonreal), empty, real

W1 = mpf('14.134725141734693790')  # first zero of Xi
for alpha, N in [(1.0,8),(0.9,10),(0.8,10),(0.5,12)]:
    deg, nre, nnr, empty, real = study(alpha, N)
    sp_w = 2*pi*mpf(alpha)          # sample spacing in the Xi variable w
    jstar = float(W1/sp_w)          # node index where the first Xi zero falls
    print(f"alpha={alpha} N={N}: deg={deg} real={nre} nonreal={nnr}")
    print(f"   sample spacing in w = {float(sp_w):.4f};  first Xi zero 14.1347 falls at node index |j| = {jstar:.3f}")
    print(f"   node gaps (j,j+1) containing NO real root: {empty}")
    print(f"   i.e. in the Xi variable, empty gaps span |w| in "
          f"{[(round(float(sp_w*j),2), round(float(sp_w*(j+1)),2)) for j in empty]}")
    print()
