"""AUDIT POINT 1: what would it take to CERTIFY the hard-window root counts?

Exact relation:  xi_j^win = Xi(2 pi alpha j) - E_j,   E_j = 2 int_T^inf Phi(t) cos(2 pi alpha j t) dt,
so |E_j| <= eps(T) := 2 int_T^inf Phi  -- the SAME bound for every j.
Rigorous bound for eps(T) derived below.
"""
from mpmath import mp, mpf, pi, exp, zeta, gamma, nstr, quad, cos
mp.dps = 40
def xi_(s): return mpf(1)/2*s*(s-1)*pi**(-s/2)*gamma(s/2)*zeta(s)
def Xi(z): return (xi_(mpf(1)/2 + 1j*mpf(z))).real

# C4 = sum n^4 e^{-pi(n^2-1)},  C2 = sum n^2 e^{-pi(n^2-1)}   (rapidly convergent, bound the tail crudely)
C4 = sum(mpf(n)**4*exp(-pi*(mpf(n)**2-1)) for n in range(1,30))
C2 = sum(mpf(n)**2*exp(-pi*(mpf(n)**2-1)) for n in range(1,30))

def eps_bound(T):
    """RIGOROUS upper bound on 2*int_T^inf Phi = 8*int_T^inf K.
    |K(t)| <= (pi^2 u^{9/4} C4 + (3pi/2) u^{5/4} C2) e^{-pi u},  u = e^{2t} >= 1
    int_T^inf |K| dt = (1/2) int_U^inf (pi^2 C4 u^{5/4} + (3pi/2) C2 u^{1/4}) e^{-pi u} du
                    <= (1/2)[ pi^2 C4 U^{5/4}/(pi-5/4) + (3pi/2) C2 U^{1/4}/(pi-1/4) ] e^{-pi U}
    using int_U^inf u^a e^{-pi u} du <= U^a e^{-pi U}/(pi-a)  for 0<=a<pi, U>=1."""
    U = exp(2*mpf(T))
    body = pi**2*C4*U**mpf('1.25')/(pi-mpf('1.25')) + mpf('1.5')*pi*C2*U**mpf('0.25')/(pi-mpf('0.25'))
    return 8*mpf('0.5')*body*exp(-pi*U)

print("Rigorous uniform error bound eps(T) = 2*int_T^inf Phi, versus the smallest coefficient |Xi(2 pi alpha N)|")
print(f"{'alpha':>6} {'T=1/(2a)':>9} {'eps(T) bound':>14} {'|Xi(2 pi a N)| at N=6':>22} {'N=10':>12}   certifiable?")
print("-"*90)
for alpha in ['1.1','1.0','0.9','0.8','0.7','0.6','0.5','0.4']:
    a = mpf(alpha); T = 1/(2*a)
    e = eps_bound(T)
    x6  = abs(Xi(2*pi*a*6)); x10 = abs(Xi(2*pi*a*10))
    ok = "YES" if e < x10 else "NO  (eps swamps the tail coeffs)"
    print(f"{alpha:>6} {float(T):>9.4f} {nstr(e,5):>14} {nstr(x6,5):>22} {nstr(x10,5):>12}   {ok}")
print()
print("Sanity: the actual (non-rigorous) tail integral vs the bound, to show the bound is not absurd:")
def Phi(t):
    t=abs(t); tot=mpf(0)
    for n in range(1,40):
        tot += (4*pi**2*n**4*exp(9*t/2)-6*pi*n**2*exp(5*t/2))*exp(-pi*n**2*exp(2*t))
    return tot
for T in ['0.5','0.7','1.0']:
    actual = 2*quad(lambda t: abs(Phi(t)), [mpf(T), 3])
    print(f"  T={T}: actual 2*int_T^3 |Phi| = {nstr(actual,6)}   rigorous bound = {nstr(eps_bound(T),6)}")
