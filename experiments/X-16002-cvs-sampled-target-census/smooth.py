"""The production target uses a SMOOTH cutoff (L-15101's chi_L).  How much does that change E_j?
Compare hard indicator vs a C^infty bump cutoff, measuring the coefficient error E_j directly."""
from mpmath import mp, mpf, pi, exp, quad, cos, zeta, gamma, nstr
mp.dps = 40
def xi_(s): return mpf(1)/2*s*(s-1)*pi**(-s/2)*gamma(s/2)*zeta(s)
def Xi(z): return (xi_(mpf(1)/2 + 1j*mpf(z))).real
def Phi(t):
    t=abs(t); tot=mpf(0)
    for n in range(1,40):
        tot += (4*pi**2*n**4*exp(9*t/2)-6*pi*n**2*exp(5*t/2))*exp(-pi*n**2*exp(2*t))
    return tot

def chi_smooth(t, T0, T1):
    """C^infty cutoff: 1 on |t|<=T0, 0 on |t|>=T1, standard bump transition."""
    a = abs(t)
    if a <= T0: return mpf(1)
    if a >= T1: return mpf(0)
    x = (a-T0)/(T1-T0)
    f = exp(-1/(1-x)) ; g = exp(-1/x)
    return f/(f+g)

alpha = mpf('1.0')
T = 1/(2*alpha)              # hard window half-width, for comparability keep the SUPPORT the same
T0, T1 = mpf('0.25'), T      # smooth: flat to 0.25, rolls off to 0 at T

print(f"alpha={float(alpha)}; both cutoffs supported in |t| <= {float(T)}")
print("hard: chi = 1_{|t|<=T}.   smooth: C^inf, flat on |t|<=0.25, 0 at |t|>=T")
print()
print(f"{'j':>3} {'|E_j| HARD':>14} {'|E_j| SMOOTH':>14} {'|Xi(2 pi a j)|':>16} {'hard/Xi':>12} {'smooth/Xi':>12}")
print("-"*78)
for j in [1,2,3,4,6,8,10]:
    w = 2*pi*alpha*j
    # E_j = Xi(w) - F(2 pi j) where F uses the cutoff
    Fh = 2*quad(lambda t: Phi(t)*cos(w*t), [0, T])
    Fs = 2*quad(lambda t: chi_smooth(t,T0,T1)*Phi(t)*cos(w*t), [0, T0, (T0+T)/2, T])
    X  = Xi(w)
    Eh, Es = abs(X-Fh), abs(X-Fs)
    print(f"{j:>3} {nstr(Eh,5):>14} {nstr(Es,5):>14} {nstr(abs(X),5):>16} {nstr(Eh/abs(X),4):>12} {nstr(Es/abs(X),4):>12}")
print()
print("j*|E_j| (hard, expect ~const) vs j^2*|E_j| and j^3*|E_j| (smooth, expect faster decay):")
for j in [4,6,8,10]:
    w = 2*pi*alpha*j
    Fh = 2*quad(lambda t: Phi(t)*cos(w*t), [0, T])
    Fs = 2*quad(lambda t: chi_smooth(t,T0,T1)*Phi(t)*cos(w*t), [0, T0, (T0+T)/2, T])
    Eh, Es = abs(Xi(w)-Fh), abs(Xi(w)-Fs)
    print(f"  j={j:>3}:  j*Eh={nstr(j*Eh,5):>12}   j*Es={nstr(j*Es,5):>12}   j^2*Es={nstr(j*j*Es,5):>12}")
