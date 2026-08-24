"""Prong B1 step 1: the C_N(L) cell machinery for R_X sign structure.
C_N(L) = sum_{k<=N} mu(k)/sqrt(k) * (1 + (L - log k)/2),  L in [log N, log(N+1)].
R_X(m) = X^{-1/2} int_{m/X}^{(m+1)/X} t^{-3/2} C_{N(t)}(log 1/t) dt  (exact, N(t)=floor(1/t)).
Check: signs of C_N on cells N=1..60; endpoint values; slope M_N/2."""
from mpmath import mp, mpf, log, sqrt, quad, zeta
mp.dps = 40

def mobius_list(n):
    mu = [0]*(n+1); mu[1]=1
    for i in range(1, n+1):
        if mu[i]:
            for j in range(2*i, n+1, i):
                mu[j] -= mu[i]
    return mu

N_MAX = 60
mu = mobius_list(N_MAX+1)
def M(N): return sum(mpf(mu[k])/sqrt(k) for k in range(1, N+1))
def A(N): return sum(mpf(mu[k])*log(k)/sqrt(k) for k in range(1, N+1))
def C(N, L): return (1 + L/2)*M(N) - A(N)/2

print("N | C_N(logN) | C_N(log(N+1)) | slope=M_N/2 | sign on cell")
for N in range(1, N_MAX+1):
    a, b = C(N, log(N)), C(N, log(N+1))
    s = "POS" if (a>0 and b>0) else ("NEG" if (a<0 and b<0) else "MIXED")
    print(f"{N:3d} {float(a):+12.6f} {float(b):+12.6f} {float(M(N)/2):+10.6f} {s}")
