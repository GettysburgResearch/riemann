"""SIEGEL Level-2 audit, part 1: numerical consequences and barrier illustrations (our own code).
Run: python3 -I s4_consequences_barriers.py

 (C1) Effective L(1,chi) lower bound implied by a zero gap c (c = 1/100, Guo Thm 1.1), derived by the auditor:
      with b0 = 1 - c/log q (no zero in [b0,1) and L(1,chi) > 0, hence L(b0,chi) > 0), the unconditional
      hyperbola identity (tested in s1 (g)) with t = q^k, u = q^{k/2} gives
        L(1,chi) log q >= c e^{-kc} [1 - e^{c}(3/2 + log q) e^{kc/2} q^{-k/2} - (q + 1 + (k/2) log q) e^{kc} q^{-k/2}]
      (we drop -zeta(b0)L(b0,chi) >= 0).  We tabulate g(q) = max_k of the right side.
 (C2) Imaginary class numbers by reduced forms for all fundamental D, -DMAX <= D <= -3; Heegner list; counts for
      h <= 7 compared with Watkins (2004), Table 4 [quoted from memory: counts 9,18,16,54,25,51,31, largest |D|
      163,427,907,1555,2683,3763,5923]; the implied bound h(D) >= sqrt|D| g(q)/(pi log q) against the data.
 (C3) Real quadratic L(1,chi) for 5 <= D <= DMAX_REAL by -(1/sqrt D) sum chi(a) log sin(pi a/D).
 (C4) Guo Prop 3.1 S_-(x) <= (11/20) log x + (29/60) log q + 6 for the inert-heavy (small L(1)) discriminants at
      every prime x <= XMAX, together with the Barreto/van Dijk shape (1/2) log x + (1/4) log q + loglog(3x).
 (C5) Barrier illustration: a 'pretentious' sign pattern (every prime inert, as for Liouville's lambda) violates
      the Prop 3.1 inequality once log x > ((29/60) log q + 6 - E)/(9/20); so Prop 3.1 cannot follow from the
      values chi(p) alone.  We also record, for the Heegner discriminants, the actual first split prime.
"""
import math
import numpy as np
import mpmath as mp

mp.mp.dps = 20
DMAX = 60000
DMAX_REAL = 3000
XMAX = 10**7
out = []
fails = 0


def rep(ok, msg):
    global fails
    if not ok:
        fails += 1
    out.append(("PASS " if ok else "FAIL ") + msg)


def is_fundamental(D):
    if D in (0, 1):
        return False
    if D % 4 == 1:
        m = abs(D)
    elif D % 4 == 0:
        m4 = D // 4
        if m4 % 4 not in (2, 3):
            return False
        m = abs(m4)
    else:
        return False
    k = 2
    while k * k <= m:
        if m % (k * k) == 0:
            return False
        k += 1
    return True


def kron(a, n):
    if n == 0:
        return 1 if abs(a) == 1 else 0
    res = 1
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    if v:
        if a % 2 == 0:
            return 0
        if v % 2 == 1 and a % 8 in (3, 5):
            res = -res
    a = a % n
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                res = -res
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            res = -res
        a = a % n
    return res if n == 1 else 0


# ---------------- (C1) ----------------
def g_bound(q, c=0.01, ks=None):
    L = math.log(q)
    best = (-1e9, None)
    for k in (ks or [2.2 + 0.1 * j for j in range(0, 120)]):
        br = 1 - math.exp(c) * (1.5 + L) * math.exp(k * c / 2) * q ** (-k / 2) \
               - (q + 1 + k / 2 * L) * math.exp(k * c) * q ** (-k / 2)
        val = c * math.exp(-k * c) * br
        if val > best[0]:
            best = (val, k)
    return best


g10_k4 = g_bound(10, ks=[4.0])[0]
g10 = g_bound(10)
rep(abs(g10_k4 - 0.00767) < 5e-5, f"(C1) at q=10, k=4: L(1,chi) log q >= {g10_k4:.6f} (ARCHITECTURE.md quotes 0.00767); optimized k: {g10[0]:.6f} at k={g10[1]:.1f}")
qs = [3, 4, 5, 7, 8, 10, 20, 100, 10**4, 10**8, 10**20]
tbl = ", ".join(f"q={q:.0e}: {g_bound(q)[0]:.5f}" for q in qs)
out.append(f"INFO (C1) g(q) = implied lower bound for L(1,chi) log q from c=1/100 (k optimized): {tbl}; limit c e^(-2c) = {0.01*math.exp(-0.02):.5f}")
mono = all(g_bound(q)[0] <= g_bound(q + 1)[0] + 1e-12 for q in range(10, 400))
rep(mono, "(C1) g(q) nondecreasing on 10 <= q <= 400 (so 0.00767/log q is valid for every q >= 10 with k=4 or better)")

# ---------------- (C2) imaginary class numbers ----------------
amax = int(math.isqrt(DMAX // 3)) + 2
A_list, B_list = [], []
for a in range(1, amax + 1):
    for b in range(-a + 1, a + 1):
        A_list.append(a)
        B_list.append(b)
A = np.array(A_list, dtype=np.int64)
Bv = np.array(B_list, dtype=np.int64)


def class_number(D):
    n = -D
    am = int(math.isqrt(n // 3))
    m = (A <= am) & ((Bv - D) % 2 == 0)
    a = A[m]
    b = Bv[m]
    num = b * b - D
    ok = (num % (4 * a) == 0)
    a, b, num = a[ok], b[ok], num[ok]
    c = num // (4 * a)
    ok = (c >= a)
    a, b, c = a[ok], b[ok], c[ok]
    # boundary: if a == c then b >= 0 ; (|b| = a case: b in (-a, a] already excludes b = -a)
    ok = ~((a == c) & (b < 0))
    return int(ok.sum())


hs = {}
for D in range(-3, -DMAX - 1, -1):
    if is_fundamental(D):
        hs[D] = class_number(D)
heeg = sorted([-D for D, h in hs.items() if h == 1])
rep(heeg == [3, 4, 7, 8, 11, 19, 43, 67, 163], f"(C2) h=1 fundamental |D| <= {DMAX}: {heeg} (Heegner-Baker-Stark)")
watkins = {1: (9, 163), 2: (18, 427), 3: (16, 907), 4: (54, 1555), 5: (25, 2683), 6: (51, 3763), 7: (31, 5923)}
okw = True
wl = []
for h, (cnt, mx) in watkins.items():
    L = [-D for D, hh in hs.items() if hh == h]
    wl.append(f"h={h}: {len(L)} fields, max {max(L)}")
    okw &= (len(L) == cnt and max(L) == mx)
rep(okw, f"(C2) counts/maxima for h<=7 match Watkins Table 4 (as recalled): " + "; ".join(wl))
# L(1,chi) and implied bound
viol = 0
minratio = (1e9, None)
minL1log = (1e9, None)
for D, h in hs.items():
    q = -D
    w = 6 if D == -3 else (4 if D == -4 else 2)
    L1 = 2 * math.pi * h / (w * math.sqrt(q))
    if q >= 10:
        gb = 0.00767
        if L1 * math.log(q) < gb:
            viol += 1
        r = L1 * math.log(q) / 0.00767
        if r < minratio[0]:
            minratio = (r, D)
    if L1 * math.log(q) < minL1log[0]:
        minL1log = (L1 * math.log(q), D)
rep(viol == 0, f"(C2) implied L(1,chi) log q >= 0.00767 (q >= 10): {viol} violations among {len(hs)} imaginary fundamental D; "
               f"min L(1)log q = {minL1log[0]:.4f} at D={minL1log[1]}; min over q>=10 of ratio to the bound = {minratio[0]:.1f} at D={minratio[1]}")
# thresholds where the implied h-bound becomes informative
def h_lower(x):
    return 0.00767 * math.sqrt(x) / (math.pi * math.log(x))
thr = {}
for target in (2, 101, 2001):
    lo, hi = 10.0, 1e40
    for _ in range(300):
        mid = math.sqrt(lo * hi)
        if h_lower(mid) > target - 1:
            hi = mid
        else:
            lo = mid
    thr[target] = hi
out.append("INFO (C2) implied h(D) > N for |D| >= T_N with T_N: " + ", ".join(f"N={k-1}: {v:.3e}" for k, v in thr.items())
           + "  (cf. Kimura 2610.21511v2 Table 1, with his own Lean-certified gap c_2000 = 0.005965 < 1/100: h > 2000 for |d| >= 1.6069e15)")

# ---------------- (C3) real quadratic ----------------
minreal = (1e9, None)
nreal = 0
for D in range(5, DMAX_REAL + 1):
    if not is_fundamental(D):
        continue
    nreal += 1
    s = mp.mpf(0)
    for a in range(1, D):
        c = kron(D, a)
        if c:
            s += c * mp.log(mp.sin(mp.pi * a / D))
    L1 = -s / mp.sqrt(D)
    val = float(L1 * mp.log(D))
    if val < minreal[0]:
        minreal = (val, D)
eps5 = (1 + mp.sqrt(5)) / 2
chk5 = 2 * mp.log(eps5) / mp.sqrt(5)
s5 = -sum(kron(5, a) * mp.log(mp.sin(mp.pi * a / 5)) for a in range(1, 5)) / mp.sqrt(5)
rep(abs(chk5 - s5) < 1e-20 and minreal[0] > 0.00767, f"(C3) real D <= {DMAX_REAL} ({nreal} fields): min L(1,chi) log D = {minreal[0]:.4f} at D={minreal[1]}; "
                                                    f"formula cross-check D=5: 2 log eps/sqrt5 = {mp.nstr(chk5, 12)}")

# ---------------- (C4) Prop 3.1 on inert-heavy discriminants ----------------
def sieve(n):
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.nonzero(s)[0].astype(np.int64)


P = sieve(XMAX)
lpp = np.log(P.astype(np.float64)) / P
worst = (-1e9, None)
worstB = (-1e9, None)
for D in [-3, -4, -7, -8, -11, -19, -43, -67, -163, -427, -907, -1555, -2683, -3763, -5923, 5, 8, 13, 101, 677]:
    q = abs(D)
    chi = np.empty(len(P), dtype=np.int64)
    odd = P > 2
    Po = P[odd]
    e = (Po - 1) // 2
    base = np.mod(D, Po)
    res = np.ones_like(Po)
    bb = base.copy()
    ee = e.copy()
    while np.any(ee > 0):
        m = (ee & 1) == 1
        res[m] = (res[m] * bb[m]) % Po[m]
        bb = (bb * bb) % Po
        ee >>= 1
    chi[odd] = np.where(res == 0, 0, np.where(res == 1, 1, -1))
    chi[~odd] = kron(D, 2)
    Sm = np.cumsum(np.where(chi == -1, lpp, 0.0))
    lx = np.log(P.astype(np.float64))
    exc = Sm - (0.55 * lx + 29 / 60 * math.log(q) + 6)
    excB = Sm - (0.5 * lx + 0.25 * math.log(q) + np.log(np.log(3 * P.astype(np.float64))))
    i = int(exc.argmax())
    if exc[i] > worst[0]:
        worst = (float(exc[i]), D, int(P[i]))
    j = int(excB.argmax())
    if excB[j] > worstB[0]:
        worstB = (float(excB[j]), D, int(P[j]))
rep(worst[0] < 0, f"(C4) Prop 3.1 on 20 inert-heavy D, all primes x <= {XMAX:.0e}: max excess {worst[0]:.3f} (D={worst[1]}, x={worst[2]})")
out.append(f"INFO (C4) Barreto/van Dijk shape S_- - (1/2 log x + 1/4 log q + loglog 3x): max {worstB[0]:.3f} (D={worstB[1]}, x={worstB[2]}); "
           f"it is O(1) as claimed (no constant is asserted there)")

# ---------------- (C5) barrier illustration ----------------
E = -1.332582275733220881765828776071027748
for q in (163, 10**6, 10**12):
    # all-inert pattern: S_-(x) = M(x) ~ log x + E ; violation once (9/20) log x > (29/60) log q + 6 - E
    lx = ((29 / 60) * math.log(q) + 6 - E) / 0.45
    out.append(f"INFO (C5) fake 'all primes inert' pattern with q={q:.0e}: Prop 3.1 bound fails for x > q^{lx / math.log(q):.2f} "
               f"(= e^{lx:.1f}); real characters cannot keep chi(p) = -1 that long (least prime with chi(p)=1 is << q^(1/4+o(1)), Linnik-Vinogradov)")
fs = []
for D in [-3, -4, -7, -8, -11, -19, -43, -67, -163]:
    p = next(int(p) for p in P if kron(D, int(p)) == 1)
    fs.append(f"{D}:{p}")
out.append("INFO (C5) first split prime for Heegner D: " + ", ".join(fs) + " (x^2+x+41 phenomenon: the longest inert runs among h=1 fields)")

print("\n".join(out))
print(f"\nSUMMARY: {sum(1 for o in out if o.startswith('PASS'))} PASS, {fails} FAIL")
