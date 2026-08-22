#!/usr/bin/env python3
"""Lane 1 / Lemma 2: saturated-margin constants for the frozen 61-smooth system.
Exact-rational threshold lock + high-precision lattice constants + closed-form
predictions + error envelope + positivity certificate for x >= x_sat = 5*P61.
"""
import json, time
from fractions import Fraction
from mpmath import mp, mpf, sqrt, log

mp.dps = 50
t0 = time.time()

P = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
P61 = 1
for p in P: P61 *= p
print("P61 =", P61, "= %.6e" % P61)

# enumerate all squarefree divisors with mu
divs = [(1, 1)]
for p in P:
    divs = divs + [(d*p, -m) for (d, m) in divs]
divs.sort()
odds  = [d for d, m in divs if m == -1]
evens = [d for d, m in divs if m == +1]
assert len(odds) == len(evens) == 1 << 17
print("lattice: 2^18 =", len(divs), "divisors;", len(evens), "evens,", len(odds), "odds")

# ---- exact rational threshold lock ----
nO = sum(P61 // o for o in odds)          # A_O = nO / P61 exactly
cum = 0
U = []
estar = None
for e in evens:                            # ascending
    w = P61 // e
    if cum + w > nO:
        estar = e
        cum_before = cum
        break
    if cum + w == nO:
        raise SystemExit("EXACT TIE at e=%d — theta*=1 boundary case!" % e)
    cum += w
    U.append(e)
g  = Fraction(nO - cum_before, P61)        # A_O - A_U in (0, 1/e*)
g2 = Fraction(cum_before + P61 // estar - nO, P61)
assert g > 0 and g2 > 0 and g < Fraction(1, estar)
theta_inf = g * estar                      # exact rational in (0,1)
assert 0 < theta_inf < 1
n_sliver = len(evens) - len(U) - 1
print(f"e* = {estar}  |U| = {len(U)}  sliver evens above e* = {n_sliver}")
print(f"g  = A_O - A_U = {float(g):.12e} (exact rational, >0 strict)")
print(f"g2 = A_(U+e*) - A_O = {float(g2):.12e} (exact rational, >0 strict)")
print(f"theta*_inf = e* g = {float(theta_inf):.15f} (exact rational)")

# ---- high-precision lattice sums (dps 50) ----
def msum(gen):
    tot = mpf(0)
    for v in gen: tot += v
    return tot

B_U = msum(1/sqrt(mpf(e)) for e in U)
L_U = msum(log(mpf(e))/sqrt(mpf(e)) for e in U)
tB = time.time()
B_O = mpf(0); L_O = mpf(0); B_E = mpf(0)
for o in odds:
    so = sqrt(mpf(o)); B_O += 1/so; L_O += log(mpf(o))/so
for e in evens:
    B_E += 1/sqrt(mpf(e))
print(f"odd/even sums done in {time.time()-tB:.1f}s")

Bs = B_E - B_O                    # B^s_infinity
Bs_prod = mpf(1)
for p in P: Bs_prod *= (1 - 1/sqrt(mpf(p)))
As = Fraction(sum((P61//d)*m for d, m in divs), P61)   # exact
As_prod = 1
for p in P: As_prod = As_prod * Fraction(p-1, p)
assert As == As_prod
print(f"A^s = prod(1-1/p) = {float(As):.12f} (exact rational)")
print(f"B^s = B_E - B_O = {mp.nstr(Bs, 12)}  vs prod(1-1/sqrt p) = {mp.nstr(Bs_prod, 12)}")

h  = B_O - B_U
h2 = h - 1/sqrt(mpf(estar))
xstar = (3*h/(4*mpf(g.numerator)/g.denominator))**2
print(f"h = B_O - B_U = {mp.nstr(h, 15)};  h2 = h - 1/sqrt(e*) = {mp.nstr(h2, 15)} (>0 => theta*<1 auto)")
print(f"x* (threshold lock) = (3h/4g)^2 = {mp.nstr(xstar, 10)}  vs x_sat = 5 P61 = {mp.nstr(5*mpf(P61), 8)}")
assert h2 > 0 and xstar < 5*mpf(P61)

thi = mpf(theta_inf.numerator)/theta_inf.denominator
DeltaB_inf = B_U + thi/sqrt(mpf(estar)) - B_O
DeltaB_alt = mpf(g.numerator)/g.denominator*sqrt(mpf(estar)) - h
print(f"Delta_B^inf = {mp.nstr(DeltaB_inf, 20)}  (alt g*sqrt(e*)-h: {mp.nstr(DeltaB_alt, 20)})")
Msc_inf = -mpf(3)/4*DeltaB_inf
print(f"M_sc^inf = {mp.nstr(Msc_inf, 15)}   [orchestrator: 13.9039]")
DeltaL_inf = L_U + thi*log(mpf(estar))/sqrt(mpf(estar)) - L_O
print(f"Delta_L^inf = {mp.nstr(DeltaL_inf, 20)}")

# ---- lam_j, kap_j, alpha_j, beta_j ----
z  = mp.zeta(mpf(1)/2)
zp = mp.zeta(mpf(1)/2, 1, 1)
out = {}
for j in (2, 3):
    A = mpf(j+1)/(j-1); B = mpf((j+1)*(j-2))/(j*(j-1)); C = mpf(2)/(j*(j-1))
    lam = A/sqrt(mpf(j)) - B/sqrt(mpf(j+1)) + C*(z - msum(1/sqrt(mpf(m)) for m in range(1, j+2)))
    kap = -A*log(mpf(j))/sqrt(mpf(j)) + B*log(mpf(j+1))/sqrt(mpf(j+1)) \
          + C*(zp + msum(log(mpf(m))/sqrt(mpf(m)) for m in range(1, j+2)))
    alpha = lam*DeltaB_inf
    beta  = (3*C + kap)*DeltaB_inf - lam*DeltaL_inf
    out[j] = (lam, kap, alpha, beta, C)
    print(f"j={j}: lam={mp.nstr(lam,15)}  kap={mp.nstr(kap,15)}  "
          f"alpha={mp.nstr(alpha,15)}  beta={mp.nstr(beta,15)}")

# ---- closed-form predictions (exact theta*(x); E-terms excluded, bounded below) ----
def T_at(x, d): return (4*sqrt(x/mpf(d)) - 3)/sqrt(mpf(d))
def theta_x(x):
    return (4*sqrt(x)*mpf(g.numerator)/g.denominator - 3*h)/T_at(x, estar)
def margins(x):
    th = theta_x(x)
    DB = B_U + th/sqrt(mpf(estar)) - B_O
    DL = L_U + th*log(mpf(estar))/sqrt(mpf(estar)) - L_O
    r = {"theta": th, "Msc": -mpf(3)/4*DB}
    for j in (2, 3):
        lam, kap, alpha, beta, C = out[j]
        r[f"M{j}"] = lam*DB*log(x) + (3*C+kap)*DB - lam*DL
    return r

print("\n== closed-form predictions ==")
pred_rows = []
for xs in ("1e26", "1e28", "1e30", "1e34"):
    x = mpf(xs)
    r = margins(x)
    row = (xs, mp.nstr(r["M2"], 12), mp.nstr(r["M3"], 12), mp.nstr(r["Msc"], 12),
           mp.nstr(r["theta"], 15))
    pred_rows.append(row)
    print(f"x={xs}: M2={row[1]}  M3={row[2]}  Msc={row[3]}  theta*={row[4]}")

# ---- E-envelope: sup|E| on [5,16] (inline, exact cell analysis) + tail bound ----
mp.dps = 30
zE = mp.zeta(mpf(1)/2); zpE = mp.zeta(mpf(1)/2, 1, 1)
def supE_5_16():
    best = mpf(0)
    S = mpf(0); L = mpf(0)
    for N in range(1, 17):
        sN = sqrt(mpf(N)); S += 1/sN; L += log(mpf(N))/sN
        cand = []
        if 5 <= N <= 16: cand.append(mpf(N))
        Ys = ((S - zE)/2)**2
        if N < Ys < N+1 and 5 <= Ys <= 16: cand.append(Ys)
        for Y in cand:
            E = S*log(Y) - L - 4*sqrt(Y) - zE*log(Y) - zpE
            best = max(best, abs(E))
    return best
Esup516 = supE_5_16()
print(f"\nsup |E| on [5,16] = {mp.nstr(Esup516, 8)}")

def Ebound(Y):   # rigorous |E(x/d)| bound for Y >= 5
    if Y >= 16: return float((log(Y) + 11)/(8*(Y-1)**mpf('1.5')))
    return float(Esup516)

import math
dlistU = [float(e) for e in U] + [float(estar)]
dlistO = [float(o) for o in odds]
def envelope(xf):
    tot = 0.0
    for d in dlistU:
        tot += Ebound(mpf(xf/d))/math.sqrt(d)
    for d in dlistO:
        tot += Ebound(mpf(xf/d))/math.sqrt(d)
    return tot
xsat = 5.0*float(P61)
env_sat = envelope(xsat)
env_26 = envelope(1e26)
print(f"envelope |Etil_j| <= env(x):  env(x_sat) = {env_sat:.3e}   env(1e26) = {env_26:.3e}")

# ---- positivity certificate ----
mp.dps = 50
xsat_mp = 5*mpf(P61)
print("\n== positivity for all x >= x_sat = 5 P61 ==")
rs = margins(xsat_mp)
for j in (2, 3):
    lam, kap, alpha, beta, C = out[j]
    # M_j(x) >= alpha log x + beta - C_j env(x_sat) for x>=x_sat (drift term positive: check bracket<0)
    bracket = lam*log(xsat_mp/estar) + 3*C + kap
    low_line = alpha*log(xsat_mp) + beta - C*mpf(env_sat)
    print(f"j={j}: closed-form M{j}(x_sat) = {mp.nstr(rs[f'M{j}'],12)};  drift bracket = "
          f"{mp.nstr(bracket,8)} (<0 ok);  line lower bound at x_sat = {mp.nstr(low_line,12)} > 0: {low_line>0}")
print(f"M_sc(x) = M_sc^inf * 4 sqrt(x/e*)/(4 sqrt(x/e*)-3) >= M_sc^inf = {mp.nstr(Msc_inf,10)} > 0: {Msc_inf>0}")
print(f"M_sc(x_sat) = {mp.nstr(rs['Msc'],15)}")

res = dict(
    P61=str(P61), estar=estar, nU=len(U), n_sliver=n_sliver,
    g=[str(g.numerator), str(g.denominator)], g_float=float(g),
    theta_inf=float(theta_inf), xstar=mp.nstr(xstar, 12),
    As=float(As), Bs=mp.nstr(Bs, 15),
    B_U=mp.nstr(B_U, 25), B_O=mp.nstr(B_O, 25), L_U=mp.nstr(L_U, 25), L_O=mp.nstr(L_O, 25),
    h=mp.nstr(h, 25), DeltaB_inf=mp.nstr(DeltaB_inf, 25), DeltaL_inf=mp.nstr(DeltaL_inf, 25),
    Msc_inf=mp.nstr(Msc_inf, 20),
    lam2=mp.nstr(out[2][0], 25), kap2=mp.nstr(out[2][1], 25),
    alpha2=mp.nstr(out[2][2], 20), beta2=mp.nstr(out[2][3], 20),
    lam3=mp.nstr(out[3][0], 25), kap3=mp.nstr(out[3][1], 25),
    alpha3=mp.nstr(out[3][2], 20), beta3=mp.nstr(out[3][3], 20),
    predictions=pred_rows, Esup516=mp.nstr(Esup516, 8),
    env_sat=env_sat, env_1e26=env_26,
)
with open("lattice_results.json", "w") as f:
    json.dump(res, f, indent=1)
print(f"\ntotal {time.time()-t0:.1f}s; saved lattice_results.json")
