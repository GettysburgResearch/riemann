#!/usr/bin/env python3
"""Finite checks for OCT5_RESIDUAL_ITEMS.md (Oct 5 quasi-RH manuscript, residual items).

Run:  python3 -I oct5_residual_checks.py [--out OUT.json] [--norm-bound B]

Part G (EXACT, integer arithmetic in Z[omega]):
  hypotheses of Goldmakher-Louvel (GL), arXiv:1112.1642v2, Definition 1, for the family
  psi_k(x) = (x/k)_2 * kappa_lambda(x)^{e_k} used in the proof of lem:quadratic
  (paper2.tex lines 1886-1913):
  G1 psi_k is trivial on the units -1 and omega (so it is a function of ideals);
  G2 psi_k is primitive of conductor k * lambda^{e_k};
  G3 R(a,b) = (a/b)_2 (b/a)_2 is a function of (a mod 4, b mod 4) (GL property (2));
     control: it is NOT a function of (a mod 2, b mod 2);
  G4 a == b mod 4 implies e_a = e_b (GL property (3): the kappa factors cancel);
  G5 the S-part factor (-2/k)_2 depends only on k mod 8 (manuscript: "classes modulo 24 fix the
     supplementary characters"); not load-bearing, since |(s/k)_2| <= 1 is all that is used.
  G6 ILLUSTRATION ONLY (FLOAT): largest eigenvalue of A A^* for A = [(n/k)_2], divided by H + U.

Part C (FLOAT, ordinary double precision; not directed, not certified):
  C1 Stirling exponents of the two gamma quotients used in the contour shifts;
  C2 the kernel contour shift for V_*^sharp (eq:theta-weight): the integral on Re t = 0 equals the
     integrals on lines to its right and on Re t = -0.25; on Re t = -1 it differs by exactly the
     residue at t = -5/6 (discriminating control). Two weights: a log-Gaussian with closed-form
     Mellin transform (lines 0.75, 2.0, -0.25, -1), and the compactly supported bump sqrt(y)W(y)
     with W = exp(-1/((y-1)(2-y))) (lines 0.5, -0.25, -1; quadrature noise limits the right shift).
These are finite numerical checks. They replay no analytic estimate.
"""
import argparse
import hashlib
import json
import math
import sys
import time

import numpy as np
from scipy.special import loggamma

# ----------------------------------------------------------------------------------------------
# Z[omega] arithmetic: x = (a, b) means a + b*omega, omega^2 = -1 - omega.


def mul(x, y):
    a, b = x
    c, d = y
    return (a * c - b * d, a * d + b * c - b * d)


def sub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def norm(x):
    a, b = x
    return a * a - a * b + b * b


def conj(x):
    a, b = x
    return (a - b, -b)  # conj(omega) = omega^2 = -1 - omega


def rdiv(p, q):
    # nearest integer to p/q, q > 0, exact
    return (2 * p + q) // (2 * q)


def mod(x, m):
    n = norm(m)
    num = mul(x, conj(m))
    q = (rdiv(num[0], n), rdiv(num[1], n))
    r = sub(x, mul(q, m))
    assert norm(r) < n
    return r


def divides(m, x):
    n = norm(m)
    num = mul(x, conj(m))
    return num[0] % n == 0 and num[1] % n == 0


def exact_div(x, m):
    n = norm(m)
    num = mul(x, conj(m))
    assert num[0] % n == 0 and num[1] % n == 0
    return (num[0] // n, num[1] // n)


def powmod(x, e, m):
    r = (1, 0)
    x = mod(x, m)
    while e:
        if e & 1:
            r = mod(mul(r, x), m)
        x = mod(mul(x, x), m)
        e >>= 1
    return r


def quad_symbol_prime(x, p):
    """(x/p)_2 for a primary prime p coprime to 6."""
    if divides(p, x):
        return 0
    y = powmod(x, (norm(p) - 1) // 2, p)
    if divides(p, sub(y, (1, 0))):
        return 1
    if divides(p, sub(y, (-1, 0))):
        return -1
    raise AssertionError("Euler criterion failed")


def is_prime_int(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def primary_elements(B):
    """All primary a + b*omega (a == 1, b == 0 mod 3) with norm <= B, i.e. ideals prime to 3."""
    out = []
    R = int(math.isqrt(4 * B // 3 + 4)) + 3
    for a in range(-R, R + 1):
        if a % 3 != 1:
            continue
        for b in range(-R, R + 1):
            if b % 3 != 0:
                continue
            x = (a, b)
            n = norm(x)
            if 1 <= n <= B:
                out.append(x)
    return out


def setup(B):
    prim = primary_elements(B)
    primes = []
    for x in prim:
        n = norm(x)
        if n % 2 == 0 or n % 3 == 0:
            continue
        if is_prime_int(n) and n % 3 == 1:
            primes.append(x)
        else:
            r = math.isqrt(n)
            if r * r == n and is_prime_int(r) and r % 3 == 2 and x == (-r, 0):
                primes.append(x)
    primes.sort(key=norm)
    sqfree = {}  # element -> list of prime factors; squarefree, prime to 6
    for x in prim:
        n = norm(x)
        if n % 2 == 0 or n % 3 == 0:
            continue
        y = x
        fac = []
        ok = True
        for p in primes:
            if norm(p) > norm(y):
                break
            if divides(p, y):
                y = exact_div(y, p)
                if divides(p, y):
                    ok = False
                    break
                fac.append(p)
        if not ok:
            continue
        # y is now a unit; x primary and all p primary => y == 1
        assert y == (1, 0), (x, y)
        sqfree[x] = fac
    return primes, sqfree


def qsym(x, fac):
    """(x/k)_2 for squarefree k with prime factors fac."""
    s = 1
    for p in fac:
        s *= quad_symbol_prime(x, p)
        if s == 0:
            return 0
    return s


def kappa(x):
    r = (x[0] + x[1]) % 3  # omega == 1 mod lambda
    return 0 if r == 0 else (1 if r == 1 else -1)


def e_of(k):
    return 0 if norm(k) % 4 == 1 else 1


def psi(x, k, fac):
    return qsym(x, fac) * (kappa(x) ** e_of(k))


def part_g(B, B_pairs, rec):
    t0 = time.time()
    primes, sqfree = setup(B)
    ks = sorted(sqfree, key=norm)
    res = {"norm_bound": B, "num_primary_primes": len(primes), "num_squarefree_rows": len(ks)}

    # G1 units
    bad = 0
    for k in ks:
        fac = sqfree[k]
        if psi((-1, 0), k, fac) != 1 or psi((0, 1), k, fac) != 1:
            bad += 1
        # the unmodified symbol is NOT trivial on -1 when e_k = 1 (control)
    ctrl = sum(1 for k in ks if qsym((-1, 0), sqfree[k]) != 1)
    res["G1_unit_failures"] = bad
    res["G1_control_rows_with_(-1/k)_2=-1"] = ctrl
    assert bad == 0 and ctrl > 0

    # G2 primitivity of psi_k with conductor k*lambda^{e_k}; periodicity sampled
    lam = (1, 2)  # 1 + 2 omega = sqrt(-3)
    rng = np.random.default_rng(20261010)
    prim_fail = 0
    per_fail = 0
    tested = 0
    for k in ks:
        if norm(k) > 400:
            break
        fac = sqfree[k]
        e = e_of(k)
        f = mul(k, lam) if e else k
        # periodicity mod f (sampled)
        for _ in range(20):
            x = (int(rng.integers(-50, 50)), int(rng.integers(-50, 50)))
            z = (int(rng.integers(-5, 5)), int(rng.integers(-5, 5)))
            if psi(x, k, fac) != psi((x[0] + mul(f, z)[0], x[1] + mul(f, z)[1]), k, fac):
                per_fail += 1
        # for each prime q | f, find x == 1 mod f/q, (x, f) = 1, psi(x) != 1
        qs = list(fac) + ([lam] if e else [])
        for q in qs:
            fq = exact_div(f, q)
            found = False
            for y0 in range(-6, 7):
                for y1 in range(-6, 7):
                    x = (1 + mul(fq, (y0, y1))[0], mul(fq, (y0, y1))[1])
                    v = psi(x, k, fac)
                    if v == -1:
                        found = True
                        break
                if found:
                    break
            if not found:
                prim_fail += 1
        tested += 1
    res["G2_rows_tested"] = tested
    res["G2_primitivity_failures"] = prim_fail
    res["G2_periodicity_failures"] = per_fail
    assert prim_fail == 0 and per_fail == 0

    # G3 reciprocity factor; G4 e_a = e_b on classes mod 4
    pk = [k for k in ks if norm(k) <= B_pairs]
    table4 = {}
    table2 = {}
    pairs = 0
    nonconst = set()
    e_fail = 0
    for i, a in enumerate(pk):
        fa = sqfree[a]
        for b in pk[i + 1:]:
            fb = sqfree[b]
            if set(fa) & set(fb):
                continue
            Rab = qsym(a, fb) * qsym(b, fa)
            assert Rab in (1, -1)
            pairs += 1
            nonconst.add(Rab)
            c4 = ((a[0] % 4, a[1] % 4), (b[0] % 4, b[1] % 4))
            c2 = ((a[0] % 2, a[1] % 2), (b[0] % 2, b[1] % 2))
            table4.setdefault(c4, set()).add(Rab)
            table2.setdefault(c2, set()).add(Rab)
            if (a[0] - b[0]) % 4 == 0 and (a[1] - b[1]) % 4 == 0 and e_of(a) != e_of(b):
                e_fail += 1
    amb4 = sum(1 for v in table4.values() if len(v) > 1)
    amb2 = sum(1 for v in table2.values() if len(v) > 1)
    res["G3_coprime_pairs"] = pairs
    res["G3_R_values_seen"] = sorted(nonconst)
    res["G3_classes_mod4_seen"] = len(table4)
    res["G3_classes_mod4_with_two_values"] = amb4
    res["G3_control_classes_mod2_with_two_values"] = amb2
    res["G4_e_mismatch_within_class_mod4"] = e_fail
    assert amb4 == 0 and amb2 > 0 and e_fail == 0 and nonconst == {1, -1}

    # G5 (-2/k)_2 as a function of k mod 8
    t8 = {}
    for k in ks:
        v = qsym((-2, 0), sqfree[k])
        t8.setdefault((k[0] % 8, k[1] % 8), set()).add(v)
    res["G5_classes_mod8"] = len(t8)
    res["G5_classes_mod8_with_two_values"] = sum(1 for v in t8.values() if len(v) > 1)
    assert res["G5_classes_mod8_with_two_values"] == 0

    # G6 illustration: operator norm of [(n/k)_2] (rows k, columns n), both squarefree primary prime to 6
    illus = []
    for HU in (250, 500, 1000):
        if HU > B:
            break
        rows = [k for k in ks if norm(k) <= HU]
        cols = rows
        A = np.array([[qsym(n, sqfree[k]) for n in cols] for k in rows], dtype=float)
        smax2 = float(np.linalg.norm(A, 2) ** 2)
        illus.append({"H=U": HU, "rows": len(rows), "lambda_max(AA*)": smax2,
                      "ratio_to_H+U": smax2 / (2 * HU)})
    res["G6_illustration"] = illus
    print("G part: %.1f s" % (time.time() - t0))
    rec["G"] = res
    return res


# ----------------------------------------------------------------------------------------------
# Part C: contour-shift checks (FLOAT)


def stirling_checks(rec):
    out = []
    # left line: |Gamma(4/3-s)Gamma(5/3-s)/(Gamma(1/3+s)Gamma(2/3+s))| ~ |T|^{2-4 sigma}
    for sigma in (-0.25, -1.1):
        for T in (1e2, 1e3, 1e4):
            s = complex(sigma, T)
            lg = (loggamma(4 / 3 - s) + loggamma(5 / 3 - s) - loggamma(1 / 3 + s) - loggamma(2 / 3 + s)).real
            out.append({"quotient": "left-line s", "sigma": sigma, "T": T,
                        "ratio_to_|T|^(2-4sigma)": math.exp(lg - (2 - 4 * sigma) * math.log(T))})
    # kernel: |Gamma(5/6+t)Gamma(7/6+t)/(Gamma(5/6-t)Gamma(7/6-t))| ~ |u|^{4c}
    for c in (-0.25, 0.0, 0.75, 2.0):
        for u in (1e2, 1e3, 1e4):
            t = complex(c, u)
            lg = (loggamma(5 / 6 + t) + loggamma(7 / 6 + t) - loggamma(5 / 6 - t) - loggamma(7 / 6 - t)).real
            out.append({"quotient": "kernel t", "c": c, "u": u,
                        "ratio_to_|u|^(4c)": math.exp(lg - 4 * c * math.log(u))})
    # 1/|Gamma(s+1/3)Gamma(s+2/3)| ~ (2pi)^{-1} e^{pi|T|} |T|^{-2 sigma}: finite order (order 1)
    for sigma in (-0.25, 0.5, 1.5):
        for T in (1e1, 1e2, 1e3):
            s = complex(sigma, T)
            lg = -(loggamma(s + 1 / 3) + loggamma(s + 2 / 3)).real
            out.append({"quotient": "1/G(s)", "sigma": sigma, "T": T,
                        "ratio_to_e^(pi T)|T|^(-2sigma)/(2pi)":
                            math.exp(lg - math.pi * T + 2 * sigma * math.log(T) + math.log(2 * math.pi))})
    for r in out:
        v = [x for k, x in r.items() if k.startswith("ratio")][0]
        if (r.get("T", 0) >= 1e3 or r.get("u", 0) >= 1e3):
            assert abs(v - 1) < 1e-2, r
    rec["C1"] = out
    return out


def bump(x):
    y = np.zeros_like(x)
    m = (x > 1) & (x < 2)
    y[m] = np.exp(-1.0 / ((x[m] - 1) * (2 - x[m])))
    return y


def make_vhat(nodes=1600):
    g, w = np.polynomial.legendre.leggauss(nodes)
    x = 1.5 + 0.5 * g
    wx = 0.5 * w
    V = np.sqrt(x) * bump(x)  # V_*(y) = sqrt(y) W(y), W = bump on [1,2]
    L = np.log(x)

    def vhat(wc):
        """V_*^(w) = int V_*(x) x^w dx/x for an array of complex w."""
        wc = np.atleast_1d(wc)
        out = np.empty(wc.shape, dtype=complex)
        for i0 in range(0, wc.size, 4000):
            ww = wc[i0:i0 + 4000]
            out[i0:i0 + 4000] = np.exp(np.outer(ww - 1, L)) @ (wx * V)
        return out
    return vhat


def gamma_quotient_log(t):
    return loggamma(7 / 6 + t) + loggamma(5 / 6 + t) - loggamma(7 / 6 - t) - loggamma(5 / 6 - t)


def line_integrals(vhat_on_line, xs, c, umax, h):
    """(1/2 pi i) int_{(c)} V^(-t) G(t) ((2pi)^4 x/27)^{-t} dt for each x, G the gamma quotient of
    eq:theta-weight; trapezoid rule on [-umax, umax] (the integrand is entire and decays rapidly)."""
    u = np.arange(-umax, umax + h / 2, h)
    t = c + 1j * u
    base = vhat_on_line(t) * np.exp(gamma_quotient_log(t))
    out = []
    for x in xs:
        Y = (2 * math.pi) ** 4 * x / 27
        f = base * np.exp(-t * math.log(Y))
        out.append((complex(np.sum(f) * h / (2 * math.pi)), float(np.sum(np.abs(f)) * h / (2 * math.pi)),
                    float(max(np.abs(f[0]), np.abs(f[-1])))))
    return out


def residue_at_minus_5_6(vhat_at, x):
    # Gamma(5/6+t) has residue 1 at t = -5/6; the other factors are regular there.
    Y = (2 * math.pi) ** 4 * x / 27
    return complex(vhat_at(5 / 6)) * math.gamma(1 / 3) / (math.gamma(2.0) * math.gamma(5 / 3)) * Y ** (5 / 6)


def kernel_shift_check(rec):
    """Contour shift of the kernel in eq:theta-weight. Moving Re t between -5/6 and +infinity crosses
    no pole; moving to Re t = -1 crosses the simple pole at t = -5/6 (control)."""
    rows = []
    xs = (1e2, 1e4, 1e6)
    # (a) log-Gaussian weight V_*(y) = exp(-(log y)^2): V^(w) = sqrt(pi) exp(w^2/4) in closed form.
    #     Not compactly supported, but the shift uses only that V^ is entire and decays rapidly in
    #     vertical strips; the closed form removes quadrature noise.
    vg_line = lambda t: math.sqrt(math.pi) * np.exp((-t) ** 2 / 4)
    vg_at = lambda w: math.sqrt(math.pi) * np.exp(w * w / 4)
    # (b) the compactly supported weight V_*(y) = sqrt(y) W(y), W = exp(-1/((y-1)(2-y))) on (1,2),
    #     Mellin transform by 1600-point Gauss-Legendre (noise floor about 1e-17 in V^).
    vb = make_vhat(1600)
    vb_line = lambda t: vb(-t)
    vb_at = lambda w: vb(np.array([complex(w)]))[0]
    cases = [("log-gaussian", vg_line, vg_at, (0.0, 0.75, 2.0, -0.25, -1.0), 40.0, 0.005, 1e-12),
             ("compact-bump", vb_line, vb_at, (0.0, 0.5, -0.25, -1.0), 1300.0, 0.02, 1e-8)]
    for name, vline, vat, cs, umax, h, rtol in cases:
        per_c = {c: line_integrals(vline, xs, c, umax, h) for c in cs}
        for i, x in enumerate(xs):
            ref, l1ref, _ = per_c[0.0][i]
            res_ = residue_at_minus_5_6(vat, x)
            row = {"weight": name, "x": x, "V#_on_Re_t=0": [ref.real, ref.imag], "L1_on_Re_t=0": l1ref,
                   "residue_at_t=-5/6": [res_.real, res_.imag]}
            scale = max(l1ref, abs(res_))
            ok = True
            for c in cs:
                if c == 0.0:
                    continue
                v, l1, edge = per_c[c][i]
                d = abs(v + (res_ if c < -5 / 6 else 0) - ref)
                row["c=%g" % c] = {"absdiff_after_residue_correction" if c < -5 / 6 else "absdiff": d,
                                   "L1": l1, "edge_integrand": edge}
                ok &= d < rtol * max(scale, l1)
                if c < -5 / 6:
                    row["c=%g" % c]["absdiff_without_residue"] = abs(v - ref)
                    ok &= abs(v - ref) > 1e3 * rtol * max(scale, l1)
            row["pass"] = bool(ok)
            rows.append(row)
            assert ok, row
    rec["C2"] = rows
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None)
    ap.add_argument("--norm-bound", type=int, default=2000)
    ap.add_argument("--pair-bound", type=int, default=700)
    args = ap.parse_args()
    rec = {"script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
           "python": sys.version.split()[0], "numpy": np.__version__}
    t0 = time.time()
    g = part_g(args.norm_bound, args.pair_bound, rec)
    print("G:", json.dumps({k: v for k, v in g.items() if k != "G6_illustration"}))
    for r in g["G6_illustration"]:
        print("G6 (illustration):", r)
    for r in stirling_checks(rec):
        print("C1:", r)
    for r in kernel_shift_check(rec):
        print("C2:", r)
    print("ALL CHECKS PASSED in %.1f s" % (time.time() - t0))
    if args.out:
        with open(args.out, "w") as fh:
            json.dump(rec, fh, indent=1, sort_keys=True)


if __name__ == "__main__":
    main()
