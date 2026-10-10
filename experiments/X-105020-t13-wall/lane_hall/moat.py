#!/usr/bin/env python3
"""Lane S part 1: exact/interval certification of the moat death.
A_t exact rationals; B_t rigorous interval enclosures (mpmath.iv);
crossings C(7/20), C(0) for all t<500 with A_t<0; top killers;
H_13(67), H_13(71), H_13(87), H_13(88) sign certification;
fibre-bottom check H_t(t) for A_t>=0; smooth-support variant.
"""
from fractions import Fraction
from mpmath import iv, mp
iv.prec = 250
mp.prec = 250

N = 520

# Mobius sieve
mu = [1]*(N+1)
mu[0] = 0
primes = []
is_comp = [False]*(N+1)
for i in range(2, N+1):
    if not is_comp[i]:
        primes.append(i)
        mu[i] = -1
    for p in primes:
        if i*p > N:
            break
        is_comp[i*p] = True
        if i % p == 0:
            mu[i*p] = 0
            break
        else:
            mu[i*p] = -mu[i]

# smooth flag: all prime factors <= 61
def smallest_pf(n):
    for p in primes:
        if p*p > n: break
        if n % p == 0: return p
    return n
smooth = [False]*(N+1)
for n in range(1, N+1):
    m0, ok = n, True
    for p in primes:
        if p > 61: break
        while m0 % p == 0: m0 //= p
    smooth[n] = (m0 == 1)

def ivfrac(fr):
    return iv.mpf(fr.numerator)/iv.mpf(fr.denominator)

# cumulative A (Fraction), B (interval)
A = [Fraction(0)]*(N+1)
B = [iv.mpf(0)]*(N+1)
As = [Fraction(0)]*(N+1)   # smooth-restricted
Bs = [iv.mpf(0)]*(N+1)
accA, accB = Fraction(0), iv.mpf(0)
accAs, accBs = Fraction(0), iv.mpf(0)
for n in range(1, N+1):
    if mu[n] != 0:
        term_inv_sqrt = iv.mpf(mu[n])/iv.sqrt(iv.mpf(n))
        accA += Fraction(mu[n], n)
        accB = accB + term_inv_sqrt
        if smooth[n]:
            accAs += Fraction(mu[n], n)
            accBs = accBs + term_inv_sqrt
    A[n] = accA; B[n] = accB; As[n] = accAs; Bs[n] = accBs

def pr_iv(x, digits=32, label=""):
    a = mp.nstr(x.a, digits, strip_zeros=False)
    b = mp.nstr(x.b, digits, strip_zeros=False)
    print(f"{label}[{a}, {b}]")

print("== A_13, B_13 exact ==")
print("A_13 =", A[13], " ~", float(A[13]))
pr_iv(B[13], 32, "B_13 in ")
print("A_5 =", A[5], " A_7 =", A[7], " A_11 =", A[11])

def H(t, x_iv):
    """H_t(x) as interval, x_iv an interval for x."""
    return 4*iv.sqrt(x_iv)*ivfrac(A[t]) - 3*B[t]

print("\n== L-99600 cross-check: H_13(67) ==")
H1367 = H(13, iv.mpf(67))
pr_iv(H1367, 20, "H_13(67) in ")
print("claimed: (0.359317660596810, 0.359317660601486)")

print("\n== Clean theorem checks ==")
for xx in (67, 71, 87, 88):
    h = H(13, iv.mpf(xx))
    s = "H_13(%d)" % xx
    pr_iv(h, 20, s+" in ")
    print("   > 7/20 ?", h.a > mp.mpf(7)/20, "  > 0 ?", h.a > 0, "  < 7/20 ?", h.b < mp.mpf(7)/20, "  < 0 ?", h.b < 0)

def crossing(t, s_frac, Avec, Bvec):
    """solve 4 sqrt(C) A_t - 3 B_t = s => sqrt(C) = (s+3B_t)/(4A_t).
    Requires A_t<0 and s+3B_t<0 (certified via interval bounds). Returns iv C or None."""
    At = Avec[t]
    if At >= 0: return None
    num = 3*Bvec[t] + ivfrac(s_frac)
    if not (num.b < 0):   # not certifiably negative -> crossing invalid/flag
        return "FLAG_num_sign"
    r = num/ivfrac(4*At)
    return r*r

print("\n== crossings for t=13 ==")
c720 = crossing(13, Fraction(7,20), A, B)
c0 = crossing(13, Fraction(0), A, B)
pr_iv(c720, 32, "C_13(7/20) in ")
pr_iv(c0, 32, "C_13(0)    in ")

print("\n== full profile: all t<500 with A_t<0 (full support) ==")
neg_ts = [t for t in range(1, 500) if A[t] < 0]
# group into blocks of consecutive t
blocks = []
for t in neg_ts:
    if blocks and t == blocks[-1][1]+1:
        blocks[-1][1] = t
    else:
        blocks.append([t, t])
print("count:", len(neg_ts), " blocks:", blocks)
# genuine demand thresholds: mu(t) = -1  (binding prefixes)
rows = []
for t in neg_ts:
    c7 = crossing(t, Fraction(7,20), A, B)
    cz = crossing(t, Fraction(0), A, B)
    rows.append((t, mu[t], A[t], c7, cz))

from mpmath import mpf as _mpf
def mid(x):
    return (_mpf(x.a) + _mpf(x.b))/2

print("t  mu(t)  A_t(float)   C(7/20)mid   C(0)mid")
for (t, m, a, c7, cz) in rows:
    c7s = mp.nstr(mid(c7), 12) if not isinstance(c7, str) and c7 is not None else str(c7)
    czs = mp.nstr(mid(cz), 12) if not isinstance(cz, str) and cz is not None else str(cz)
    print(f"{t:4d}  {m:+d}  {float(a):+.8f}  {c7s:>14}  {czs:>14}")

print("\n== sorted top-5 killers by C(7/20) (odd thresholds only) ==")
odd_rows = [(t, c7, cz) for (t, m, a, c7, cz) in rows if m == -1 and not isinstance(c7, str)]
odd_rows.sort(key=lambda r: mid(r[1]))
for (t, c7, cz) in odd_rows[:5]:
    print(f"t={t:4d}  C(7/20)={mp.nstr(mid(c7),15)}  C(0)={mp.nstr(mid(cz),15)}")
# certify strict ordering of top 2 by intervals
if len(odd_rows) >= 2:
    print("top1 < top2 certified:", odd_rows[0][1].b < odd_rows[1][1].a)

print("\n== fibre-bottom check: min H_t(t) over t<500 with A_t>=0 ==")
worst = None
below_720 = []
for t in range(1, 500):
    if mu[t] == 0: continue
    if A[t] >= 0:
        h = H(t, iv.mpf(t))
        if worst is None or mid(h) < mid(worst[1]):
            worst = (t, h)
        if not (h.a > mp.mpf(7)/20):
            below_720.append((t, mp.nstr(mid(h),10)))
print("min H_t(t) at t =", worst[0]); pr_iv(worst[1], 20, "   value in ")
print("thresholds with H_t(t) not certified > 7/20:", below_720[:20], "count", len(below_720))
neg_bottom = [t for t in range(1,500) if mu[t]!=0 and A[t]>=0 and not (H(t,iv.mpf(t)).a>0)]
print("thresholds with H_t(t) not certified > 0:", neg_bottom)

print("\n== smooth-support variant (support primes<=61), thresholds t in [67,500) ==")
neg_ts_s = [t for t in range(67, 500) if smooth[t] and mu[t] != 0 and As[t] < 0]
print("smooth thresholds t in [67,500) with A^s_t<0:", len(neg_ts_s))
best_s = None
for t in neg_ts_s:
    cz = crossing(t, Fraction(0), As, Bs)
    c7 = crossing(t, Fraction(7,20), As, Bs)
    if isinstance(cz, str) or cz is None:
        print(t, "FLAG", cz); continue
    if best_s is None or mid(cz) < best_s[1]:
        best_s = (t, mid(cz), mid(c7) if not isinstance(c7,str) else None)
print("earliest smooth-only killer (t>=67):", best_s)
print("(note: t=13 killer is itself 61-smooth, so both variants share C(0)=87.359 cap)")
# also full-support new thresholds t in [67,500): earliest crossing among them
best_f = None
for (t, m, a, c7, cz) in rows:
    if t >= 67 and m == -1 and not isinstance(cz, str):
        if best_f is None or mid(cz) < best_f[1]:
            best_f = (t, mid(cz))
print("earliest full-support killer with t>=67:", best_f)

print("\n== per-C most-violated threshold at x=C^- and slack accounting ==")
Clist = [71, 89, 101, 149, 211, 307, 401]
for C in Clist:
    xiv = iv.mpf(C)   # boundary value (fibre sup)
    best = None; second = None
    for t in range(1, C):
        if mu[t] == 0: continue
        h = H(t, xiv)
        key = mid(h)
        if best is None or key < best[1]:
            second = best; best = (t, key)
        elif second is None or key < second[1]:
            second = (t, key)
    # min slack over whole block: also fibre bottoms
    print(f"C={C}: argmin_t H_t(C^-) = t={best[0]}, H = {mp.nstr(best[1],10)}; runner-up t={second[0]}, H = {mp.nstr(second[1],10)}")

print("\n== extended scan sqrt(t)*A_t and B_t, t<=10^6 (float, context only) ==")
import numpy as np
M = 10**6
mub = np.ones(M+1, dtype=np.int8); mub[0]=0
pr = []
isc = np.zeros(M+1, dtype=bool)
for i in range(2, M+1):
    if not isc[i]:
        pr.append(i); mub[i] = -1
    for p in pr:
        if i*p > M: break
        isc[i*p] = True
        if i % p == 0:
            mub[i*p] = 0; break
        else:
            mub[i*p] = -mub[i]
n = np.arange(M+1, dtype=np.float64); n[0]=1
Af = np.cumsum(mub/n)
Bf = np.cumsum(mub/np.sqrt(n))
sqtA = np.sqrt(np.arange(M+1))*Af
i_min = int(np.argmin(sqtA[3:]))+3
i_max = int(np.argmax(sqtA[1000:]))+1000
print(f"min over t<=1e6 of sqrt(t)*A_t = {sqtA[3:].min():.6f} at t={i_min}")
print(f"max over t in [1000,1e6] of sqrt(t)*A_t = {sqtA[1000:].max():.6f} at t={i_max}")
print(f"B_t range on [100,1e6]: [{Bf[100:].min():.6f}, {Bf[100:].max():.6f}]; B_1e6 = {Bf[M]:.6f}")
print(f"3|B|/4 comparison level = {3*abs(Bf[M])/4:.6f}")
print(f"most negative A_t for t<=1e6: {Af[3:].min():.8f} at t={int(np.argmin(Af[3:]))+3}  (A_13={float(A[13]):.8f})")
# horizon of rescaled target b/a: min over t (with A_t<0) of ((b/a) B_t/A_t)^2 within self-consistent range
negmask = Af < 0
ts = np.nonzero(negmask[2:M+1])[0]+2
ratio2 = (Bf[ts]/Af[ts])**2
order = np.argsort(ratio2)
print("five smallest (B_t/A_t)^2 among A_t<0, t<=1e6:")
for j in order[:5]:
    print(f"   t={ts[j]}  (B/A)^2={ratio2[j]:.4f}  horizon(3/4)={(9/16)*ratio2[j]:.4f}")
