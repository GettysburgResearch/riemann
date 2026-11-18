#!/usr/bin/env python3
"""C1 / family (b): independent check of hyperbolicity of classical Jensen polynomials J^{d,0} of Farmer's X_j
(cos(z) with the two zeros closest to j, and their negatives, moved to +-j +- i).
Taylor coefficients: X_j = cos z + C1 cos z/(z^2-a^2) + C2 cos z/(z^2-b^2), with the entire functions
cos z/(z^2-a^2) having coefficients a^{-2n-2} sum_{l>n} (-1)^l a^{2l}/(2l)!  (tail form, no cancellation for n>a).
J^{d,0}(z) = sum_k C(d,k) X^{(k)}(0) z^k is even; it is real-rooted iff its d/2 positive-axis zeros are all real,
i.e. iff F(theta) = cos(theta)^d J(tan theta) has d/2 sign changes on (0, pi/2).
Sign changes are counted on a uniform theta-grid with Arb balls (python-flint); a count of d/2 certifies real-rootedness
(each sign change certified by non-overlapping balls); a smaller count is a NUMERICAL-NONRIGOROUS indication of
non-real zeros (close real pairs could be missed) -- near the threshold we refine the grid.
"""
import sys, math, time, json
import mpmath as mp
import flint
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import common

def taylor_X(j, K, dps=200):
    mp.mp.dps = dps
    c = [(m + mp.mpf(1) / 2) * mp.pi for m in range(int(j) + 10)]
    order = sorted(range(len(c)), key=lambda m: abs(c[m] - j))
    a, b = c[order[0]], c[order[1]]
    A = (a**2 + b**2) - 2 * (j**2 - 1); B = (j**2 + 1)**2 - a**2 * b**2
    C1 = (A * a**2 + B) / (a**2 - b**2); C2 = (A * b**2 + B) / (b**2 - a**2)
    def gcoef(n, r):   # coefficient of z^{2n} in cos z/(z^2 - r^2)
        s = mp.mpf(0); l = n + 1
        term = (-1)**l * r**(2 * l) / mp.factorial(2 * l)
        while True:
            s += term
            if l > r and abs(term) < mp.mpf(10)**(-dps + 5) * abs(s):   # purely relative tolerance (bug fix: no absolute floor)
                break
            l += 1; term = term * (-1) * r**2 / ((2 * l) * (2 * l - 1))
        return s / r**(2 * n + 2)
    alpha = []   # alpha_{2n} = X^{(2n)}(0)
    for n in range(K // 2 + 1):
        cf = (-1)**n / mp.factorial(2 * n) + C1 * gcoef(n, a) + C2 * gcoef(n, b)
        alpha.append(cf * mp.factorial(2 * n))
    return alpha, (float(a), float(b))

def count_sign_changes(alpha, d, M_per=40, prec=2000):
    flint.ctx.prec = prec
    coeffs = [flint.arb(0)] * (d + 1)
    for n in range(d // 2 + 1):
        coeffs[2 * n] = flint.arb(mp.nstr(mp.binomial(d, 2 * n) * alpha[n], 400))
    P = flint.arb_poly(coeffs)
    M = M_per * d
    prev, cnt, unresolved = None, 0, 0
    for i in range(1, M):
        th = flint.arb(i) * flint.arb.pi() / (2 * M)
        t = th.tan()
        v = P(t) * th.cos()**d
        if v > 0: s = 1
        elif v < 0: s = -1
        else:
            unresolved += 1; continue
        if prev is not None and s != prev:
            cnt += 1
        prev = s
    return cnt, unresolved

if __name__ == "__main__":
    t0 = time.time()
    res = []
    plan = {10: list(range(116, 124)), 20: [470, 475, 476, 477, 478, 480, 600, 700, 749, 750]}
    for j, ds in plan.items():
        alpha, ab = taylor_X(j, max(ds) + 2, dps=400)
        for d in ds:
            t1 = time.time()
            cnt, unr = count_sign_changes(alpha, d)
            r = {"j": j, "moved": ab, "d": d, "positive_sign_changes": cnt, "needed_for_real_rooted": d // 2,
                 "verdict": "real-rooted (certified count)" if cnt == d // 2 else "fewer sign changes -> non-real zeros indicated",
                 "unresolved_points": unr, "sec": round(time.time() - t1, 1)}
            res.append(r); print(r, flush=True)
    # control: cos itself at d=200
    mp.mp.dps = 250
    alpha_cos = [(-1)**n for n in range(102)]
    cnt, unr = count_sign_changes(alpha_cos, 200)
    res.append({"control": "cos", "d": 200, "positive_sign_changes": cnt, "needed": 100})
    print(res[-1])
    p = common.save_json("jensen_farmer_check.json", {"env": common.env(), "rows": res, "runtime_s": time.time() - t0})
    print("saved", p, common.sha256(p))
