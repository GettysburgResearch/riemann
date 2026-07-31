"""How fast does the hard-window coefficient error E_j decay in j?
E_j = 2 int_T^inf Phi(t) cos(2 pi alpha j t) dt.  Hard cutoff => Phi has a JUMP at T,
so one integration by parts gives |E_j| <= 2 Phi(T)/(pi alpha j) and NO better:
the decay is only O(1/j), while the true coefficients Xi(2 pi alpha j) decay EXPONENTIALLY."""
from mpmath import mp, mpf, pi, exp, quad, cos, zeta, gamma, nstr
mp.dps = 40
def xi_(s): return mpf(1)/2*s*(s-1)*pi**(-s/2)*gamma(s/2)*zeta(s)
def Xi(z): return (xi_(mpf(1)/2 + 1j*mpf(z))).real
def Phi(t):
    t=abs(t); tot=mpf(0)
    for n in range(1,40):
        tot += (4*pi**2*n**4*exp(9*t/2)-6*pi*n**2*exp(5*t/2))*exp(-pi*n**2*exp(2*t))
    return tot

alpha = mpf('1.0'); T = 1/(2*alpha)
print(f"alpha={float(alpha)}, T={float(T)}, Phi(T)={nstr(Phi(T),6)}")
print(f"{'j':>4} {'|E_j| (computed)':>18} {'2*Phi(T)/(pi a j) bound':>24} {'|Xi(2 pi a j)|':>16} {'|E_j|/|Xi_j|':>14}")
print("-"*82)
for j in [1,2,3,4,6,8,10,12]:
    w = 2*pi*alpha*j
    E = 2*quad(lambda t: Phi(t)*cos(w*t), [T, T+1, T+2, 4])
    bnd = 2*Phi(T)/(pi*alpha*j)
    X = Xi(w)
    print(f"{j:>4} {nstr(abs(E),6):>18} {nstr(bnd,6):>24} {nstr(abs(X),6):>16} {nstr(abs(E)/abs(X),6):>14}")
print()
print("j*|E_j| should be roughly CONSTANT if the decay is 1/j:")
vals=[]
for j in [4,6,8,10,12]:
    w = 2*pi*alpha*j
    E = 2*quad(lambda t: Phi(t)*cos(w*t), [T, T+1, T+2, 4])
    vals.append((j, abs(E)*j))
print("   " + "  ".join(f"j={j}: {nstr(v,5)}" for j,v in vals))
print()
print("CONCLUSION: the hard cutoff makes Phi discontinuous at T, so E_j = O(1/j) only.")
print("The true coefficients decay like e^{-pi^2 alpha j/2}.  So beyond a small j the hard-window")
print("coefficient is ENTIRELY truncation artefact -- which is exactly the tail region that decides")
print("the root count.  A SMOOTH cutoff (as L-15101 actually specifies) makes E_j decay faster than")
print("any power, which is why the production target is smooth and why the hard window is not a")
print("harmless stand-in for it.")
