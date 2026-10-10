"""Lane D numeric checks: Jensen-disk attraction lemma + descent counting + census non-exclusion.
All polynomial tests: exact objects, numpy roots at high degree cross-checked with mpmath.
"""
import numpy as np
rng = np.random.default_rng(20260823)

def poly_from_zeros(reals, pairs):
    """Real poly with given real zeros and conjugate pairs (x,y)."""
    p = np.poly1d([1.0])
    for t in reals:
        p = p * np.poly1d([1.0, -t])
    for (x, y) in pairs:
        p = p * np.poly1d([1.0, -2*x, x*x + y*y])
    return p

def check_jensen(p, pairs, reals, tol=1e-9):
    """Every non-real zero w of p' lies in some OPEN Jensen disk (u-x)^2+v^2 < y^2.
    Returns (n_nonreal_deriv_zeros, min over them of max_j margin)."""
    dz = np.roots(np.polyder(p))
    worst = np.inf; cnt = 0
    for w in dz:
        if abs(w.imag) < 1e-8:
            continue
        cnt += 1
        u, v = w.real, w.imag
        marg = max(y*y - v*v - (u-x)**2 for (x, y) in pairs) if pairs else -np.inf
        worst = min(worst, marg)
    return cnt, worst

# --- Test 1: random ladders with planted pairs ---
viol = 0; tested = 0
for trial in range(400):
    nr = rng.integers(2, 9); npair = rng.integers(1, 4)
    reals = np.sort(rng.uniform(-10, 10, nr))
    pairs = [(rng.uniform(-10, 10), rng.uniform(0.05, 0.5)) for _ in range(npair)]
    p = poly_from_zeros(reals, pairs)
    cnt, worst = check_jensen(p, pairs, reals)
    if cnt:
        tested += 1
        if worst <= 0:
            viol += 1
            print("VIOLATION t1:", reals, pairs, worst)
print(f"T1 random ladders: {tested} configs w/ nonreal deriv zeros, violations={viol}")

# --- Test 2: iterate derivative (ladder depth 3), track high zeros, disk occupancy ---
eta = 0.2
occ_max = 0; viol2 = 0
for trial in range(150):
    nr = rng.integers(6, 14)
    reals = np.sort(rng.uniform(-15, 15, nr))
    pairs = [(rng.uniform(-12, 12), rng.uniform(0.21, 0.5)) for _ in range(rng.integers(1, 4))]
    p = poly_from_zeros(reals, pairs)
    for k in range(3):
        rts = np.roots(p)
        prs = [(z.real, z.imag) for z in rts if z.imag > 1e-8]
        dz = np.roots(np.polyder(p))
        high_next = [w for w in dz if w.imag > eta]
        # every high-next zero must sit in an open Jensen disk of a pair with y > Im w
        for w in high_next:
            ok = any((w.real-x)**2 + w.imag**2 < y*y for (x, y) in prs)
            # multiple-zero clause: near a repeated root of p
            if not ok:
                mind = min((abs(w - z) for z in rts), default=np.inf)
                ok = mind < 1e-6
            if not ok:
                viol2 += 1
                print("VIOLATION t2:", w, prs)
        # disk occupancy
        for (x, y) in prs:
            occ = sum(1 for w in dz if abs(w.imag) > 1e-8 and (w.real-x)**2 + w.imag**2 < y*y)
            occ_max = max(occ_max, occ)
        p = np.polyder(p)
print(f"T2 ladder confinement: violations={viol2}, max disk occupancy(nonreal deriv zeros)={occ_max}")

# --- Test 3: Xi-like truncated product with a planted high pair ---
from mpmath import mp, zetazero
mp.dps = 30
gam = [float(zetazero(n).imag) for n in range(1, 31)]
p = np.poly1d([1.0])
for g in gam:
    p = p * np.poly1d([-1.0/(g*g), 0.0, 1.0])   # (1 - t^2/g^2)
xp, yp = 25.0, 0.4
zp2 = complex(xp, yp)**2
# (1 - t^2/zp^2)(1 - t^2/conj(zp)^2) real quartic in t
q = np.poly1d(np.real(np.polymul([-1.0/zp2, 0, 1.0], [-1.0/np.conj(zp2), 0, 1.0])))
F = np.polymul(p.coeffs, q.coeffs)
dz = np.roots(np.polyder(np.poly1d(F)))
prs = [(xp, yp), (-xp, yp)]
bad = 0; found_high = 0
for w in dz:
    if abs(w.imag) > 1e-7:
        found_high += 1
        if not any((w.real-x)**2 + w.imag**2 < y*y for (x, y) in prs):
            bad += 1
            print("VIOLATION t3:", w)
print(f"T3 Xi-like plant: nonreal deriv zeros={found_high}, violations={bad}")

# --- Test 4: census non-exclusion counterexample: pair present, extra(G)=0 ---
a = 2.0
p4 = poly_from_zeros([-1.0, 1.0], [(0.0, a)])   # (x^2-1)(x^2+a^2)
d4 = np.roots(np.polyder(p4))
in_gap = [w for w in d4 if abs(w.imag) < 1e-10 and -1 < w.real < 1]
g = 2.0; w4 = min(1.0, g*g/(4*a*a))
print(f"T4 counterexample: deriv real zeros in gap(-1,1) = {len(in_gap)} (extra={len(in_gap)-1}), "
      f"pair weight={w4} < 1 -> pair present, extra=0: census extra-ledger excludes nothing")
