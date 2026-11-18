#!/usr/bin/env python3
"""U3 adjudication, independent pass: certified (ball-arithmetic) positivity of L(sigma, chi_d)
for small fundamental discriminants d. Our own code; nothing from any audited repository.

For every fundamental discriminant d with 3 <= |d| <= X_FULL we certify L(sigma, chi_d) > 0 on [1/2, 1].
For X_FULL < |d| <= X_LZZ we certify L(sigma, chi_d) > 0 on [1 - 1/(5 log q), 1] (LZZ's interval).
By the functional equation for real primitive chi (root number 1, Gamma factor zero-free on (0,1)),
positivity on [1/2, 1] gives L(sigma, chi_d) != 0 on (0, 1].

Method (rigorous given arb's acb_dirichlet_l series enclosures):
  * chi_d is realised as a python-flint dirichlet_char(q, l) with l^2 = 1 mod q, primitive, and
    parity = [d < 0]; its values are checked against our own Kronecker symbol on a full period.
  * At an exact grid point a we get c_k = L^{(k)}(a)/k!, k < K, from acb_series.dirichlet_l.
  * Remainder: for sigma >= a > 0 and K >= 1,
        |L^{(K)}(sigma)| = |sum_n chi(n) (log n)^K n^{-sigma}| <= B * TV(f) = 2 B max_x f(x)
                         = 2 B (K/a)^K e^{-K},           f(x) = (log x)^K x^{-sigma},
    by Abel summation with S(x) = sum_{n<=x} chi(n), B = max |S| over one period (S(q) = 0),
    f(1) = 0, f -> 0, and f unimodal with max at log x = K/sigma.
  * On [a, a+h]:  L >= c_0 + sum_{1<=k<K} min(0, c_k) h^k - M_K h^K / K!.
  Steps are halved adaptively; a failure is reported (never silently skipped).
Usage: python3 -I adj_U3_indep_smallq_cert.py X_FULL X_LZZ NPROC OUT.json
"""
import sys, json, time, math
from multiprocessing import Pool
from flint import acb, arb, ctx, dirichlet_char, acb_series

ctx.prec = 80
K = 6  # Taylor terms c_0..c_5, remainder from the 6th derivative


def kronecker(d, n):
    """Kronecker symbol (d/n) for n >= 1 (our own implementation)."""
    if n == 0:
        return 1 if abs(d) == 1 else 0
    res = 1
    # factor 2 out of n
    while n % 2 == 0:
        n //= 2
        if d % 2 == 0:
            return 0
        if d % 8 in (3, 5):
            res = -res
    # now n odd: Jacobi symbol (d/n)
    a = d % n
    while a != 0:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                res = -res
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            res = -res
        a %= n
    return res if n == 1 else 0


def squarefree(m):
    m = abs(m)
    p = 2
    while p * p <= m:
        if m % (p * p) == 0:
            return False
        p += 1
    return True


def fundamental(d):
    if d % 4 == 1:
        return d != 1 and squarefree(d)
    if d % 4 == 0:
        m = d // 4
        return m % 4 in (2, 3) and squarefree(m)
    return False


def find_char(d):
    q = abs(d)
    par = 1 if d < 0 else 0
    cands = []
    for l in range(1, q):
        if (l * l) % q == 1 and math.gcd(l, q) == 1:
            c = dirichlet_char(q, l)
            if c.is_primitive() and c.parity() == par and c.order() == 2:
                cands.append(c)
    assert len(cands) == 1, (d, len(cands))
    c = cands[0]
    vals = [kronecker(d, n) for n in range(1, q + 1)]
    for n in range(1, q + 1):
        v = c(n)
        assert v.real.contains(vals[n - 1]) and v.imag.contains(0) and v.real.is_exact(), (d, n)
    S, B = 0, 0
    for v in vals:
        S += v
        B = max(B, abs(S))
    assert S == 0
    return c, B


def taylor(c, a):
    s = acb_series([acb(a), acb(1)], prec=K)
    co = acb_series.dirichlet_l(s, c).coeffs()
    out = []
    for z in co:
        assert z.imag.contains(0)
        out.append(z.real)
    return out


def certify(d, lo, hi):
    """Certify L(sigma, chi_d) > 0 for sigma in [lo, hi] (lo, hi exact arbs). Returns dict."""
    c, B = find_char(d)
    a = lo
    h = arb(1) / 8
    hcap = arb(1) / 4
    nevals, minlb = 0, None
    fact = arb(math.factorial(K))
    while a < hi:
        hh = h if a + h < hi else hi - a
        co = taylor(c, a)
        nevals += 1
        MK = 2 * B * (arb(K) / a) ** K * arb(-K).exp()
        while True:
            lb = co[0]
            for k in range(1, K):
                if co[k].upper() < 0:
                    lb += co[k] * hh ** k
                elif not (co[k].lower() >= 0):
                    lb -= abs(co[k]) * hh ** k
            lb -= MK * hh ** K / fact
            if lb.lower() > 0:
                break
            hh = hh / 2
            if hh.upper() < 1e-6:
                return {"d": d, "ok": False, "at": float(a.mid()), "nevals": nevals}
        v = float(lb.lower())
        minlb = v if minlb is None else min(minlb, v)
        a = a + hh
        h = hh * 2
        if h > hcap:
            h = hcap
    return {"d": d, "ok": True, "B": B, "nevals": nevals, "min_lower_bound": minlb,
            "L1": float(taylor(c, arb(1))[0].mid()) if d in (-3, -4, 5, 8, -8, 12) else None}


def job(args):
    d, mode = args
    q = abs(d)
    t = time.time()
    if mode == "full":
        r = certify(d, arb(1) / 2, arb(1))
    else:
        lo = arb(1) - 1 / (5 * arb(q).log())
        # use an exact dyadic point <= lo as the left end (covers a superset of the interval)
        lo = arb(math.floor(float(lo.lower()) * 2**20) / 2**20)
        r = certify(d, lo, arb(1))
        r["lo"] = float(lo.mid())
    r["mode"] = mode
    r["sec"] = round(time.time() - t, 3)
    return r


if __name__ == "__main__":
    XF, XL, NP, OUT = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    # self-check of kronecker against direct Legendre via Euler's criterion
    for d in range(-200, 201):
        for p in (3, 5, 7, 11, 13, 101, 103):
            if d % p:
                e = pow(d % p, (p - 1) // 2, p)
                assert kronecker(d, p) == (1 if e == 1 else -1)
    ds = [d for d in range(-XL, XL + 1) if abs(d) >= 3 and fundamental(d)]
    jobs = [(d, "full" if abs(d) <= XF else "lzz") for d in ds]
    jobs.sort(key=lambda j: -abs(j[0]))
    t0 = time.time()
    with Pool(NP) as pool:
        res = pool.map(job, jobs, chunksize=4)
    res.sort(key=lambda r: (abs(r["d"]), r["d"]))
    bad = [r for r in res if not r["ok"]]
    nf = sum(1 for r in res if r["mode"] == "full")
    nl = sum(1 for r in res if r["mode"] == "lzz")
    print(f"fundamental discriminants: {len(res)}  (full [1/2,1]: {nf} with |d|<={XF};"
          f" LZZ interval: {nl} with {XF}<|d|<={XL})")
    print(f"certified: {len(res) - len(bad)}   failures: {len(bad)}   wall {time.time() - t0:.0f}s")
    for r in bad:
        print("FAIL", r)
    full = [r for r in res if r["mode"] == "full" and r["ok"]]
    lz = [r for r in res if r["mode"] == "lzz" and r["ok"]]
    if full:
        w = min(full, key=lambda r: r["min_lower_bound"])
        print("full mode: smallest certified lower bound for L on a step:", w["d"], w["min_lower_bound"])
        print("full mode: total Taylor evaluations", sum(r["nevals"] for r in full))
    if lz:
        w = min(lz, key=lambda r: r["min_lower_bound"])
        print("LZZ mode: smallest certified lower bound for L on a step:", w["d"], w["min_lower_bound"])
    for r in res:
        if r.get("L1") is not None:
            print("sanity L(1,chi_d)", r["d"], r["L1"])
    json.dump(res, open(OUT, "w"))
