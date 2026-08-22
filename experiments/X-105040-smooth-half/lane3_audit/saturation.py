#!/usr/bin/env python3
"""Lane 3 independent saturation check (own implementation, own algebra path).
Stable restructuring:
  T(d) = 4 sqrt(x)/d - 3/sqrt(d)                       (exact)
  Q_Y(j) = 4 C_j sqrt(Y) + R_j(Y)                      (exact split)
  demand equality  =>  4 sqrt(x) * Delta1 = 3 * Delta2 (exact)
  M_j   = 3 C_j Delta2 + [sum_e theta R_j(x/e)/sqrt(e) - sum_o R_j(x/o)/sqrt(o)]
  M_sc  = -(3/4) Delta2,   Delta2 = sum_e theta(e)/sqrt(e) - sum_o 1/sqrt(o)
H(Y) exact from longdouble prefix tables for Y <= NTAB; expansion
H = 4 sqrt(Y) + zeta(1/2) log Y + zeta'(1/2) + E(Y) beyond, with E measured.
"""
import numpy as np
from math import sqrt, log, fsum, floor

PR = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
ZH = -1.4603545088095868  # zeta(1/2)
ZP = -3.9226461392091517  # zeta'(1/2)
NTAB = 10_000_000

def build_lattice():
    divs = [(1,1)]
    for p in PR:
        divs = divs + [(d*p, -mu) for d, mu in divs]
    divs.sort()
    return divs

LAT = build_lattice()
DS  = np.array([float(d) for d, _ in LAT])
MU  = np.array([mu for _, mu in LAT], dtype=np.int8)
P61 = LAT[-1][0]
print(f"lattice 2^18 = {len(LAT)}; P_61 = {P61} = {float(P61):.6e}")

# prefix tables (longdouble)
m = np.arange(1, NTAB+1, dtype=np.longdouble)
inv = 1.0/np.sqrt(m)
S_half = np.cumsum(inv)
S_hlog = np.cumsum(inv*np.log(m))
del m, inv

def Htab(Y):
    M = int(floor(Y))
    if M < 1: return 0.0
    return float(log(Y)*S_half[M-1] - S_hlog[M-1])

def Hexp(Y):
    return 4.0*sqrt(Y) + ZH*log(Y) + ZP

print("E(Y) = Htab - Hexp on a grid:")
for Y in (1e3, 1e4, 1e5, 1e6, 3e6, 855.86, 9.9e6):
    print(f"  Y={Y:>10.5g}: E = {Htab(Y)-Hexp(Y):+.3e}")

COEF = {2: (3.0, 0.0, 1.0), 3: (2.0, 2.0/3.0, 1.0/3.0)}  # A_j, B_j, C_j

def R(Y, j):
    """R_j(Y) = Q_Y(j) - 4 C_j sqrt(Y), exact for Y <= NTAB, expansion beyond."""
    A, B, C = COEF[j]
    if Y < j: return -4.0*C*sqrt(Y)  # Q=0
    # H(Y) - 4 sqrt(Y), formed WITHOUT the cancelling 4 sqrt(Y) in the expansion branch
    Hm4 = (Htab(Y) - 4.0*sqrt(Y)) if Y <= NTAB else (ZH*log(Y) + ZP)
    knot = A*log(Y/j)/sqrt(j)
    if Y >= j+1: knot -= B*log(Y/(j+1))/sqrt(j+1)
    ssub = fsum(log(Y/mm)/sqrt(mm) for mm in range(1, min(j+1, int(floor(Y)))+1))
    return knot + C*(Hm4 - ssub)

def Qfrom_R(Y, j):
    A, B, C = COEF[j]
    return R(Y, j) + 4.0*C*sqrt(Y)

# validate Q against a direct sum at scattered Y
def Q_direct(Y, j):
    if Y < j: return 0.0
    M = int(floor(Y))
    def g(mm):
        if mm == j: return (j+1)/(j-1)
        if mm == j+1: return -((j+1)*(j-2))/(j*(j-1))
        return 2.0/(j*(j-1))
    return fsum(g(mm)/sqrt(mm)*log(Y/mm) for mm in range(j, M+1))

print("Q validation (table/knot form vs direct sum):")
for Y in (2.5, 3.0, 4.7, 7.3, 100.5, 855.86, 12345.678):
    for j in (2, 3):
        a, b = Qfrom_R(Y, j), Q_direct(Y, j)
        print(f"  Y={Y:>10.4f} j={j}: {a:.12f} vs {b:.12f}  diff {a-b:+.2e}")

def margins_sat(x, verbose=True):
    act = DS <= x
    ev = act & (MU == 1); od = act & (MU == -1)
    E = DS[ev]; O = DS[od]           # ascending
    S1o = fsum(1.0/o for o in O); S2o = fsum(1.0/sqrt(o) for o in O)
    S1e = fsum(1.0/e for e in E); S2e = fsum(1.0/sqrt(e) for e in E)
    sx4 = 4.0*sqrt(x)
    D = sx4*S1o - 3.0*S2o
    TB = sx4*(S1e - S1o) - 3.0*(S2e - S2o)
    A_s = fsum(mu/d for d, mu in LAT if d <= x)
    B_s = fsum(mu/sqrt(d) for d, mu in LAT if d <= x)
    # coarse threshold
    C1 = np.cumsum(1.0/E); C2 = np.cumsum(1.0/np.sqrt(E))
    cum = sx4*C1 - 3.0*C2
    idx = int(np.searchsorted(cum, D))
    # refine with fsum in a window
    def cum_exact(k):  # capacity of first k evens
        return sx4*fsum(1.0/e for e in E[:k]) - 3.0*fsum(1.0/sqrt(e) for e in E[:k])
    while idx > 0 and cum_exact(idx) >= D: idx -= 1
    while cum_exact(idx+1) < D: idx += 1
    kstar = idx  # 0-based index of the partial even
    estar = E[kstar]
    Tstar = sx4/estar - 3.0/sqrt(estar)
    theta_star = (D - cum_exact(kstar))/Tstar
    assert -1e-9 < theta_star < 1 + 1e-9, theta_star
    nfull = kstar
    sliver = len(E) - nfull
    # Delta2 and margins
    th = np.zeros(len(E)); th[:kstar] = 1.0; th[kstar] = theta_star
    Delta2 = fsum(list(th/np.sqrt(E)) + [-1.0/sqrt(o) for o in O])
    Msc = -0.75*Delta2
    res = dict(x=x, TB=TB, A_s=A_s, B_s=B_s, D=D, estar=int(estar),
               theta_star=theta_star, nfull=nfull, sliver=sliver, Msc=Msc,
               Delta2=Delta2)
    for j in (2, 3):
        _, _, C = COEF[j]
        dR = fsum([th[i]*R(x/E[i], j)/sqrt(E[i]) for i in range(len(E))]
                  + [-R(x/o, j)/sqrt(o) for o in O])
        res[f"M{j}"] = 3.0*C*Delta2 + dR
        res[f"dR{j}"] = dR
    if verbose:
        print(f"x = {x:.3e}: TB = {TB:.6e}  B_s = {B_s:+.7f}")
        print(f"  threshold even e* = {res['estar']} (index {nfull+1} of {len(E)}), "
              f"theta* = {theta_star:.9f}, full-filled = {nfull}, sliver(theta<1) = {sliver}")
        print(f"  M_2 = {res['M2']:.4f}   M_3 = {res['M3']:.4f}   M_sc = {Msc:.6f}   "
              f"Delta2 = {Delta2:.9f}")
        print(f"  identity check: M_2 - (dR2 - 4*C2*Msc*4/3)*... M_j = dR_j - 4C_j*Msc: "
              f"{res['M2'] - (res['dR2'] - 4*1.0*Msc):.2e}, "
              f"{res['M3'] - (res['dR3'] - 4*(1/3)*Msc):.2e}")
    return res

print("\n== limiting threshold from 1/e prefix vs S1o (x -> infinity) ==")
Einf = DS[MU == 1]; Oinf = DS[MU == -1]
S1o_inf = fsum(1.0/o for o in Oinf)
c1 = 0.0
for i, e in enumerate(Einf):
    c1 += 1.0/e
    if c1 > S1o_inf:
        print(f"  limit threshold index {i+1}, even e = {int(e)}; "
              f"prefix-excess = {c1 - S1o_inf:.3e}")
        break
print(f"  prod(1-1/p) = {np.prod([1-1/np.longdouble(p) for p in PR]):.10f}  "
      f"prod(1-1/sqrt(p)) = {np.prod([1-1/np.sqrt(np.longdouble(p)) for p in PR]):.10f}")

print("\n== exact slope prediction sigma_j * Delta2 (theta frozen) ==")
def sigma(j):
    A, B, C = COEF[j]
    return A/sqrt(j) - (B/sqrt(j+1) if True else 0) + C*(ZH - fsum(1/sqrt(mm) for mm in range(1, j+2)))
print(f"  sigma_2 = {sigma(2):.6f}  sigma_3 = {sigma(3):.6f}")

print("\n== saturation table ==")
import json, os
out = {}
for x in (1e6, 1e26, 1e28, 1e30, 1e34):
    r = margins_sat(x)
    out[f"{x:.0e}"] = {k: (float(v) if isinstance(v, (int, float, np.floating)) else v)
                       for k, v in r.items()}
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "saturation_results.json"), "w") as f:
    json.dump(out, f, indent=1)
print("saved saturation_results.json")
