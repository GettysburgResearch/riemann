#!/usr/bin/env python3
"""Lane 1 / Lemma 1 verification: E(Y) = H(Y) - 4 sqrt(Y) - zeta(1/2) log Y - zeta'(1/2),
H(Y) = sum_{m<=Y} m^{-1/2} log(Y/m) = S(N) log Y - L(N), N = floor(Y).

Per cell [N, N+1): E' = (S(N)-zeta(1/2))/Y - 2/sqrt(Y) has at most one zero
Y* = ((S(N)-zeta(1/2))/2)^2; E is increasing-then-decreasing => cell extrema
are at the integer endpoints and Y*. Checking all N <= 1e5 and all Y* gives the
TRUE sup of |E| on [2, 1e5+1) (up to mpmath rounding at dps=30).

Bounds checked:
  B1(Y) = (log Y + 11)/(8 * floor(Y)^{3/2})   [proved for Y >= 15]
  B2(Y) = (log Y + 11)/(8 * (Y-1)^{3/2})      [weaker corollary]
Also computes: sup |E| on [2,16], on [5,16]; max of |E| sqrt(Y)/(log Y + 2)
(for the requested K (log Y + c)/sqrt(Y) form).
"""
import json, time
from mpmath import mp, mpf, sqrt, log

mp.dps = 30
NMAX = 100000
z = mp.zeta(mpf(1)/2)
zp = mp.zeta(mpf(1)/2, 1, 1)
print("zeta(1/2)  =", mp.nstr(z, 20))
print("zeta'(1/2) =", mp.nstr(zp, 20))

def E_of(Y, S, L):
    lY = log(Y)
    return S*lY - L - 4*sqrt(Y) - z*lY - zp

S = mpf(0); L = mpf(0)
worst_ratio_ge15 = (mpf(-1), None)   # |E| * 8*N^{3/2} / (logY+11), Y >= 15
worst_ratio_all = (mpf(-1), None)    # same with (Y-1)^{3/2}, Y >= 2
sup_2_16 = (mpf(-1), None)
sup_5_16 = (mpf(-1), None)
worst_sqrtY = (mpf(-1), None)        # |E| sqrt(Y)/(log Y + 2), Y >= 2
decade_rows = []
next_decade = 10

t0 = time.time()
for N in range(1, NMAX+1):
    sN = sqrt(N); lN = log(N)
    S += 1/sN; L += lN/sN
    # samples in cell [N, N+1): left endpoint Y=N (>=2), critical point Y*
    samples = []
    if N >= 2:
        samples.append(mpf(N))
    Ystar = ((S - z)/2)**2
    if N < Ystar < N+1:
        samples.append(Ystar)
    for Y in samples:
        E = E_of(Y, S, L)
        aE = abs(E)
        lY = log(Y)
        if Y >= 15:
            r = aE * 8 * mpf(N)**mpf('1.5') / (lY + 11)
            if r > worst_ratio_ge15[0]: worst_ratio_ge15 = (r, float(Y))
        if Y >= 2:
            r2 = aE * 8 * (Y-1)**mpf('1.5') / (lY + 11)
            if r2 > worst_ratio_all[0]: worst_ratio_all = (r2, float(Y))
            rs = aE * sqrt(Y) / (lY + 2)
            if rs > worst_sqrtY[0]: worst_sqrtY = (rs, float(Y))
        if 2 <= Y <= 16 and aE > sup_2_16[0]: sup_2_16 = (aE, float(Y))
        if 5 <= Y <= 16 and aE > sup_5_16[0]: sup_5_16 = (aE, float(Y))
    if N == next_decade:
        E = E_of(mpf(N), S, L)
        decade_rows.append((N, mp.nstr(E, 12), mp.nstr((log(N)+11)/(8*mpf(N)**mpf('1.5')), 6)))
        next_decade *= 10
print(f"scan done in {time.time()-t0:.1f}s")

res = dict(
    dps=mp.dps, NMAX=NMAX,
    zeta_half=mp.nstr(z, 25), zetap_half=mp.nstr(zp, 25),
    worst_ratio_proved_bound_Yge15=[mp.nstr(worst_ratio_ge15[0], 12), worst_ratio_ge15[1]],
    worst_ratio_Ym1_bound_Yge2=[mp.nstr(worst_ratio_all[0], 12), worst_ratio_all[1]],
    sup_absE_on_2_16=[mp.nstr(sup_2_16[0], 12), sup_2_16[1]],
    sup_absE_on_5_16=[mp.nstr(sup_5_16[0], 12), sup_5_16[1]],
    worst_absE_sqrtY_over_logYp2=[mp.nstr(worst_sqrtY[0], 12), worst_sqrtY[1]],
    decade_rows=decade_rows,
)
print(json.dumps(res, indent=1))
with open("lemma1_results.json", "w") as f:
    json.dump(res, f, indent=1)

# spot check: knot-form Q vs direct gamma-sum Q, and Q_direct - Q_exp == C_j E(Y)
def Qdirect(Y, j):
    tot = mpf(0)
    M = int(Y)
    for m in range(j, M+1):
        if m == j: gcoef = mpf(j+1)/(j-1)
        elif m == j+1: gcoef = -mpf((j+1)*(j-2))/(j*(j-1))
        else: gcoef = mpf(2)/(j*(j-1))
        tot += gcoef/sqrt(m)*log(mpf(Y)/m)
    return tot

def Qknot(Y, j, Hval):
    A = mpf(j+1)/(j-1); B = mpf((j+1)*(j-2))/(j*(j-1)); C = mpf(2)/(j*(j-1))
    Y = mpf(Y)
    t = A*log(Y/j)/sqrt(j) - B*log(Y/(j+1))/sqrt(j+1)
    t += C*(Hval - sum(log(Y/m)/sqrt(m) for m in range(1, j+2)))
    return t

def Hdirect(Y):
    return sum(log(mpf(Y)/m)/sqrt(m) for m in range(1, int(Y)+1))

print("\nknot-form and expansion spot checks:")
for Y in (7.3, 88.0, 1009.5, 20000.0):
    Hv = Hdirect(Y)
    Ev = Hv - 4*sqrt(mpf(Y)) - z*log(mpf(Y)) - zp
    for j in (2, 3):
        qd = Qdirect(Y, j); qk = Qknot(Y, j, Hv)
        C = mpf(2)/(j*(j-1))
        lam = mpf(j+1)/(j-1)/sqrt(j) - mpf((j+1)*(j-2))/(j*(j-1))/sqrt(j+1) \
              + C*(z - sum(1/sqrt(mpf(m)) for m in range(1, j+2)))
        kap = -mpf(j+1)/(j-1)*log(mpf(j))/sqrt(j) + mpf((j+1)*(j-2))/(j*(j-1))*log(mpf(j+1))/sqrt(j+1) \
              + C*(zp + sum(log(mpf(m))/sqrt(m) for m in range(1, j+2)))
        qe = 4*C*sqrt(mpf(Y)) + lam*log(mpf(Y)) + kap
        print(f" Y={Y:>8} j={j}: |Qdirect-Qknot|={mp.nstr(abs(qd-qk),3)}  "
              f"|Qdirect-Qexp-C_j*E|={mp.nstr(abs(qd-qe-C*Ev),3)}")
