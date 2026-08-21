from mpmath import mp, mpf, pi, zeta, gamma
from fractions import Fraction as F
import sympy as sp, sys
sys.path.insert(0,'/home/user/riemann/experiments/X-16001-finsler-cone-collapse')
from verify import inertia
mp.dps = 120
def xi_(s): return mpf(1)/2*s*(s-1)*pi**(-s/2)*gamma(s/2)*zeta(s)
def Xi(z): return (xi_(mpf(1)/2 + 1j*mpf(z))).real
s = sp.symbols('s')

for alpha, N in [(1.0,6),(1.1,6),(0.9,6)]:
    xis = {j: F((-1)**j)*F(mp.nstr(Xi(2*pi*mpf(alpha)*j),100,strip_zeros=False)) for j in range(-N,N+1)}
    P = sp.Integer(0)
    for j in range(-N,N+1):
        t = sp.Integer(1)
        for k in range(-N,N+1):
            if k!=j: t *= (sp.Integer(k)-s)
        P += sp.Rational(xis[j].numerator,xis[j].denominator)*t
    P = sp.Poly(sp.expand(P), s); deg=int(P.degree())
    nreal = int(sp.Poly(P.quo(sp.gcd(P,P.diff(s))), s).count_roots())
    co = [F(int(c.p),int(c.q)) for c in P.all_coeffs()]           # descending
    def ev(cs, x):
        r=F(0)
        for c in cs: r = r*x + c
        return r
    d1 = [co[i]*(len(co)-1-i) for i in range(len(co)-1)]
    d2 = [d1[i]*(len(d1)-1-i) for i in range(len(d1)-1)]
    idx=list(range(-N,N+1)); n=len(idx)
    b={}; a={}
    for i in idx:
        Pi=ev(co,F(i)); Pdi=ev(d1,F(i)); Pddi=ev(d2,F(i))
        b[i]=-Pdi/Pi; a[i]=(Pdi*Pdi-Pi*Pddi)/(Pi*Pi)
    Q=[[ (a[i] if i==j else (b[i]-b[j])/F(i-j)) for j in idx] for i in idx]
    ine=inertia(Q)
    bodd=all(b[-i]+b[i]==0 for i in idx); aeven=all(a[-i]-a[i]==0 for i in idx)
    print(f"alpha={alpha} N={N}: deg={deg}  EXACT #real={nreal}  {'PASS' if nreal==deg else f'FAIL deficit {deg-nreal}'}")
    print(f"   closed-form Q inertia (pos,neg,zero) = {ine}   PSD? {ine[1]==0}   b odd? {bodd}   a even? {aeven}")
