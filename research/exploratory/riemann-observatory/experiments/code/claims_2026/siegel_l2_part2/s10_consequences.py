"""SIEGEL Level-2 audit, part 2: consequences, cross-checked by a route independent of part 1.
Our own code; nothing from the audited repositories is executed.  Run: python3 -I s10_consequences.py

 (C1) Imaginary class numbers from the ANALYTIC class number formula h(D) = w sqrt|D| L(1,chi_D)/(2 pi)
      (L(1,chi) by Euler-Maclaurin accelerated sums), for all fundamental -DMAX <= D <= -3; integrality, the
      Heegner list, and the counts / largest |D| for h = 1..5 (Watkins 2004, Table 4: 9/163, 18/427, 16/907,
      54/1555, 25/2683, as also recalled in part 1).  Part 1 used reduced binary forms; agreement cross-validates.
 (C2) The implied effective bound, re-derived here (auditor's derivation, same mechanism as Kimura Lemma 8):
      with b0 = 1 - c/log q (no zero in [b0, 1) by the gap theorem), H_{b0}(t) >= 1, zeta(b0) L(b0) < 0 and the
      unconditional paired-tail identity,
        L(1,chi) log q >= c e^{-kc} [1 - e^c (3/2 + log q) e^{kc/2} q^{-k/2} - (q + 1 + (k/2) log q) e^{kc} q^{-k/2}]
      at t = q^k; |L(b0,chi)| <= 1 + e^c log q + e^c/2.  Checked against the data for c = 1/100 (Guo), 1/64
      (Guo App. A), 3.0e-3 (Banks, all q via LZZ) and 5.811e-4 (Kimura, all q).
 (C3) For each constant c: the least |D| beyond which the implied bound forces h(D) > 1 and h(D) > 100
      (ordering check: a larger c gives an earlier threshold).
"""
import math
import numpy as np
import mpmath as mp
import sympy as sp

mp.mp.dps = 30
DMAX = 3000
out = []
fails = 0


def rep(ok, msg):
    global fails
    if not ok:
        fails += 1
    out.append(("PASS " if ok else "FAIL ") + msg)


def info(msg):
    out.append("INFO " + msg)


def fundamental(D):
    if D % 4 == 1:
        return abs(D) > 1 and all(e == 1 for e in sp.factorint(abs(D)).values())
    if D % 4 == 0:
        m = D // 4
        return m % 4 in (2, 3) and all(e == 1 for e in sp.factorint(abs(m)).values())
    return False


def L1(D, Kp=20):
    q = abs(D)
    ch = np.array([int(sp.kronecker_symbol(D, n)) for n in range(1, q + 1)], dtype=np.float64)
    n = np.arange(1, Kp * q + 1, dtype=np.float64)
    head = np.sum(np.tile(ch, Kp) / n)
    X = Kp * q + np.arange(1, q + 1, dtype=np.float64)
    s = 1.0
    tail = -np.sum(ch * np.log(X)) / q + np.sum(ch * (0.5 / X + s * q / (12 * X ** 2) - 6 * q ** 3 / (720 * X ** 4)))
    return head + tail


# validation
def L1_exact(D):
    q = abs(D)
    return -mp.fsum(int(sp.kronecker_symbol(D, a)) * mp.digamma(mp.mpf(a) / q) for a in range(1, q)) / q


verr = max(abs(L1(D) - float(L1_exact(D))) for D in (-3, -4, -7, -163, -2683, 5, 2993))
rep(verr < 1e-9, f"(C1) L(1,chi) routine agrees with the exact digamma formula -(1/q) sum chi(a) psi(a/q) to {verr:.1e}")

hs = {}
L1s = {}
intok = True
for a in range(3, DMAX + 1):
    D = -a
    if not fundamental(D):
        continue
    L = L1(D)
    w = 6 if D == -3 else (4 if D == -4 else 2)
    h = w * math.sqrt(a) * L / (2 * math.pi)
    intok &= abs(h - round(h)) < 1e-6
    hs[D] = round(h)
    L1s[D] = L
for a in range(5, DMAX + 1):
    if fundamental(a):
        L1s[a] = L1(a)
heeg = sorted(-D for D, h in hs.items() if h == 1)
watkins = {1: (9, 163), 2: (18, 427), 3: (16, 907), 4: (54, 1555), 5: (25, 2683)}
got = {k: (sum(1 for h in hs.values() if h == k), max(-D for D, h in hs.items() if h == k)) for k in watkins}
rep(intok and heeg == [3, 4, 7, 8, 11, 19, 43, 67, 163] and got == watkins,
    f"(C1) analytic class numbers for all {len(hs)} imaginary fundamental |D| <= {DMAX}: all integral to 1e-6; "
    f"h=1 list {heeg}; (count, max|D|) for h=1..5 = {got} = Watkins Table 4")


def g_bound(q, c, k):
    q = mp.mpf(q)
    lq = mp.log(q)
    return c * mp.e ** (-k * c) * (1 - mp.e ** c * (mp.mpf(3) / 2 + lq) * mp.e ** (k * c / 2) * q ** (-k / 2)
                                   - (q + 1 + k / 2 * lq) * mp.e ** (k * c) * q ** (-k / 2))


def g_opt(q, c):
    return max(g_bound(q, c, k / 4) for k in range(8, 80))


CONSTS = [("Guo 1/100", mp.mpf(1) / 100), ("Guo App.A 1/64", mp.mpf(1) / 64), ("Banks 3.0e-3", mp.mpf('3.0e-3')),
          ("Kimura 5.811e-4", mp.mpf('5.811e-4'))]
gq10 = g_bound(10, mp.mpf(1) / 100, 4)
rep(abs(gq10 - mp.mpf('0.007671')) < 2e-6,
    f"(C2) re-derived bound at q=10, k=4, c=1/100: L(1,chi) log q >= {float(gq10):.6f} (part 1 / ARCHITECTURE: 0.00767)")
viol = 0
minratio = (1e9, None)
for D, L in L1s.items():
    q = abs(D)
    if q < 10:
        continue
    for name, c in CONSTS:
        b = g_opt(q, c)
        if L * math.log(q) < b:
            viol += 1
    r = L * math.log(q) / float(g_opt(q, mp.mpf(1) / 100))
    if r < minratio[0]:
        minratio = (r, D)
rep(viol == 0, f"(C2) implied L(1,chi) lower bounds for all four constants: 0 violations over {len(L1s)} fundamental "
    f"discriminants (imaginary |D| <= {DMAX}, real D <= {DMAX}, q >= 10); smallest ratio data/bound for c=1/100: "
    f"{minratio[0]:.1f} at D = {minratio[1]}")


def threshold(c, H):
    # least |D| (on a log grid, then bisection) with sqrt|D| g/(pi log|D|) > H
    f = lambda x: math.sqrt(x) * float(g_opt(x, c)) / (math.pi * math.log(x)) - H
    lo, hi = 10.0, 10.0
    while f(hi) <= 0:
        lo, hi = hi, hi * 10
    for _ in range(60):
        mid = math.sqrt(lo * hi)
        if f(mid) > 0:
            hi = mid
        else:
            lo = mid
    return hi


rows = []
for name, c in CONSTS:
    rows.append((name, threshold(c, 1), threshold(c, 100)))
mono = all(rows[i][1] <= rows[j][1] for i in range(len(rows)) for j in range(len(rows))
           if CONSTS[i][1] >= CONSTS[j][1])
rep(mono, "(C3) |D| beyond which the implied bound h(D) >= sqrt|D| g(q)/(pi log|D|) exceeds 1 and 100 "
    "(D < -4): " + "; ".join(f"{r[0]}: h>1 for |D| >= {r[1]:.3g}, h>100 for |D| >= {r[2]:.3g}" for r in rows)
    + ". Ordering is monotone in c; every threshold lies far beyond the Heegner range (163), so class-number tables "
      "cannot contradict any of the constants.")

print("\n".join(out))
print(f"\nSUMMARY: {sum(1 for o in out if o.startswith('PASS'))} PASS, {fails} FAIL")
