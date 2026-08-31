#!/usr/bin/env python3
"""X-108513: stdlib-exact replay for the torsion resonance threshold
(standalone/2026-08-31-torsion-resonance-threshold/PROOF.md).

Checks (EXACT_RATIONAL in number fields Q[a]/(C) at b = 1):
  V1  REGROUPING LEMMA directly: at four (point, m) pairs the defect
      numerator N_m computed in K[T] is EXACTLY divisible by the
      prefactor prod_c (1 - alpha^c T)^{n_c - 1} predicted by the
      class-multiplicity count (the cyclotomic factors built inside K
      via alpha + alpha^{-1} = a arithmetic on the z-side... concretely
      via the PAIRED form: (1 - alpha^c T)(1 - alpha^{-c} T) =
      T^2 - z_c T + 1 with z_c = 2cos(c theta) computed by Chebyshev
      recursion z_c = a z_{c-1} - z_{c-2} in K).
  V2  ENTRY TABLE at points with entry <= 27: disc_z M_m = 0 is False
      for every m from 5 to entry-1 and True at entry = 2R + 1
      (converse-half evidence + theorem instance).
  V3  z = a collision at entry: M(a) = M'(a) = 0 at m = 2R + 1, all
      points (the Theorem's collision-at-the-trace).
  V4  the m = 2R near-miss: disc_z M_{2R} != 0 at every point with
      2R in [5, 27] (the boundary-class analysis).

Self-contained standard library only. rh_established: false.
"""
import json
import os
from fractions import Fraction as Fr
from math import comb

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append({"name": name, "ok": bool(ok), "detail": detail})
    print(("PASS " if ok else "FAIL ") + name + (f": {detail}" if detail
                                                 and not ok else ""))


# ---- minimal self-contained copy of the number-field defect engine ----
# (kept in sync with matrix/torsion_field_probe.py; a replay must not
# import campaign code, so the ~120 lines are inlined)

class NF:
    def __init__(self, C):
        self.C = [Fr(c) for c in C]
        assert self.C[-1] == 1
        self.d = len(C) - 1

    def el(self, *coeffs):
        v = [Fr(c) for c in coeffs] + [Fr(0)] * (self.d - len(coeffs))
        return v[:self.d]

    zero = property(lambda s: [Fr(0)] * s.d)
    one = property(lambda s: s.el(1))
    gen = property(lambda s: s.reduce([Fr(0), Fr(1)]))

    def add(self, x, y):
        return [a + b for a, b in zip(x, y)]

    def sub(self, x, y):
        return [a - b for a, b in zip(x, y)]

    def scal(self, c, x):
        return [c * v for v in x]

    def mul(self, x, y):
        prod = [Fr(0)] * (2 * self.d - 1)
        for i, xi in enumerate(x):
            if xi:
                for j, yj in enumerate(y):
                    if yj:
                        prod[i + j] += xi * yj
        return self.reduce(prod)

    def is_zero(self, x):
        return all(v == 0 for v in x)

    def inv(self, x):
        r0, r1 = self.C[:], [v for v in x]
        s0, s1 = [Fr(0)], [Fr(1)]

        def deg(p):
            d = len(p) - 1
            while d >= 0 and p[d] == 0:
                d -= 1
            return d

        def sub_shift(p, q, c, k):
            out = p[:]
            while len(out) < len(q) + k:
                out.append(Fr(0))
            for i, qv in enumerate(q):
                out[i + k] -= c * qv
            return out

        while deg(r1) > 0:
            while deg(r0) >= deg(r1):
                c = r0[deg(r0)] / r1[deg(r1)]
                k = deg(r0) - deg(r1)
                r0 = sub_shift(r0, r1, c, k)
                s0 = sub_shift(s0, s1, c, k)
            r0, r1, s0, s1 = r1, r0, s1, s0
        assert deg(r1) == 0 and r1[0] != 0
        c = r1[0]
        return self.reduce([v / c for v in s1])

    def reduce(self, p):
        p = list(p) + [Fr(0)] * max(0, self.d - len(p))
        for k in range(len(p) - 1, self.d - 1, -1):
            c = p[k]
            if c:
                p[k] = Fr(0)
                for i in range(self.d):
                    p[k - self.d + i] -= c * self.C[i]
        return p[:self.d]


def defect_and_spectrum(K, m):
    a = K.gen
    dim = m + 1
    q = [K.el(2), a]
    for j in range(2, m * (dim + 1) + 2):
        q.append(K.sub(K.mul(a, q[-1]), q[-2]))
    ps = []
    for j in range(1, dim + 1):
        s = K.zero
        i = 0
        while 2 * i < m:
            s = K.add(s, q[(m - 2 * i) * j])
            i += 1
        if m % 2 == 0:
            s = K.add(s, K.one)
        ps.append(s)
    e = [K.one]
    for k in range(1, dim + 1):
        s = K.zero
        for i in range(1, k + 1):
            t = K.mul(e[k - i], ps[i - 1])
            s = K.add(s, t) if i % 2 == 1 else K.sub(s, t)
        e.append(K.scal(Fr(1, k), s))
    h = [K.one, a]
    for k in range(2, m + 5):
        h.append(K.sub(K.mul(a, h[-1]), h[-2]))
    hm = []
    for hk in h:
        v = K.one
        for _ in range(m):
            v = K.mul(v, hk)
        hm.append(v)

    def c(r):
        s = K.zero
        for u in range(r + 1):
            if r - u <= dim:
                t = K.mul(e[r - u], hm[u])
                s = K.add(s, t) if (r - u) % 2 == 0 else K.sub(s, t)
        return s

    N = [c(r) for r in range(m)]
    for r in range(m, m + 4):
        assert K.is_zero(c(r)), "tail certification failed"
    eps = 1 if m % 2 == 0 else 0
    nu = (m - 1 - eps) // 2
    Nspec = N
    if eps:
        quo = [K.zero] * (len(N) - 1)
        rem = [v[:] for v in N]
        for i in range(len(N) - 2, -1, -1):
            quo[i] = rem[i + 1]
            rem[i] = K.sub(rem[i], quo[i])
            rem[i + 1] = K.zero
        assert K.is_zero(rem[0]), "even division failed"
        Nspec = quo
    mus = [K.zero] * (nu + 1)
    work = [v[:] for v in Nspec]
    for j in range(nu, -1, -1):
        mu = work[nu + j][:]
        mus[j] = mu
        for i in range(j + 1):
            work[nu + 2 * i - j] = K.sub(work[nu + 2 * i - j],
                                         K.scal(Fr(comb(j, i)), mu))
    assert all(K.is_zero(v) for v in work)
    assert K.is_zero(K.sub(mus[nu], K.one)), "monicity failed"
    return N, mus, nu


def poly_deg(K, p):
    d = len(p) - 1
    while d >= 0 and K.is_zero(p[d]):
        d -= 1
    return d


def poly_mod(K, P, Q):
    dQ = poly_deg(K, Q)
    lcQ_inv = K.inv(Q[dQ])
    R = [v[:] for v in P]
    while poly_deg(K, R) >= dQ:
        dR = poly_deg(K, R)
        f = K.mul(R[dR], lcQ_inv)
        for i in range(dQ + 1):
            R[dR - dQ + i] = K.sub(R[dR - dQ + i], K.mul(f, Q[i]))
    dR = poly_deg(K, R)
    return R[:dR + 1] if dR >= 0 else []


def disc_is_zero(K, M, nu):
    P = [v[:] for v in M]
    Q = [K.scal(Fr(j), M[j]) for j in range(1, nu + 1)]
    while True:
        if poly_deg(K, Q) < 0:
            return poly_deg(K, P) >= 1
        P, Q = Q, poly_mod(K, P, Q)


POINTS = {
    "ord6": ([-1, 1], 6), "ord8": ([-2, 0, 1], 8),
    "ord5": ([-1, 1, 1], 5), "ord10": ([-1, -1, 1], 10),
    "ord12": ([-3, 0, 1], 12), "ord9": ([1, -3, 0, 1], 9),
    "ord18": ([-1, -3, 0, 1], 18), "ord20": ([5, 0, -5, 0, 1], 20),
    "ord11": ([1, 3, -3, -4, 1, 1], 11),
    "ord13": ([-1, 3, 6, -4, -5, 1, 1], 13),
    "ord16": ([2, 0, -4, 0, 1], 16), "ord24": ([1, 0, -4, 0, 1], 24),
}


def R_of(M):
    return M if M % 2 else M // 2


# ---- V1: regrouping lemma direct divisibility ----------------------------

def v1():
    ok = True
    for name, m in (("ord6", 8), ("ord8", 11), ("ord5", 12),
                    ("ord9", 21)):
        C, Mo = POINTS[name]
        K = NF(C)
        a = K.gen
        N, mus, nu = defect_and_spectrum(K, m)
        # class multiplicities n_c for exponents 2j - m mod Mo
        from collections import Counter
        n = Counter((2 * j - m) % Mo for j in range(m + 1))
        # prefactor in K[T]: pair classes c and -c into
        # T^2 - z_c T + 1 (z_c = 2cos(c theta), Chebyshev in K);
        # unpaired classes c == 0 -> (1 - T), c == Mo/2 -> (1 + T)
        z = [K.el(2), a]
        for j in range(2, Mo + 1):
            z.append(K.sub(K.mul(a, z[-1]), z[-2]))
        pref = [K.one]

        def pmul(P, Q):
            out = [K.zero] * (len(P) + len(Q) - 1)
            for i, pi in enumerate(P):
                for jj, qj in enumerate(Q):
                    out[i + jj] = K.add(out[i + jj], K.mul(pi, qj))
            return out

        done = set()
        for c_, nc in n.items():
            if nc < 2 or c_ in done:
                continue
            cc = (-c_) % Mo
            if c_ == cc:  # self-paired: alpha^c = +-1
                lin = [K.one, K.scal(Fr(-1), K.one)] if c_ == 0 \
                    else [K.one, K.one]
                for _ in range(nc - 1):
                    pref = pmul(pref, lin)
                done.add(c_)
            else:
                quad = [K.one, K.scal(Fr(-1), z[c_]), K.one]
                nc2 = n[cc]
                # apply (T^2 - z_c T + 1)^{min(nc,nc2)-1} for the pair,
                # plus leftover linear-free handling: classes come in
                # conjugate pairs with equal multiplicity here
                assert nc2 == nc, f"asymmetric pair at {name} m={m}"
                for _ in range(nc - 1):
                    pref = pmul(pref, quad)
                done.add(c_)
                done.add(cc)
        # exact division N / pref in K[T]
        rem = [v[:] for v in N]
        dp = poly_deg(K, pref)
        lc_inv = K.inv(pref[dp])
        while poly_deg(K, rem) >= dp:
            dr = poly_deg(K, rem)
            f = K.mul(rem[dr], lc_inv)
            for i in range(dp + 1):
                rem[dr - dp + i] = K.sub(rem[dr - dp + i],
                                         K.mul(f, pref[i]))
        if poly_deg(K, rem) >= 0:
            ok = False
            check("V1-case", False, f"{name} m={m}")
    check("V1 regrouping lemma: prefactor prod (1-alpha^c T)^{n_c-1} "
          "divides N_m exactly in K[T] (4 point/m cases)", ok)


# ---- V2 + V3 + V4 --------------------------------------------------------

def v234():
    ok2 = ok3 = ok4 = True
    for name, (C, Mo) in POINTS.items():
        R = R_of(Mo)
        entry = 2 * R + 1
        if entry > 27:
            continue
        K = NF(C)
        for m in range(5, entry + 1):
            _, mus, nu = defect_and_spectrum(K, m)
            dz = disc_is_zero(K, mus, nu) if nu >= 1 else False
            if m < entry and dz:
                ok2 = False
                check("V2-early", False, f"{name} m={m}")
            if m == entry and not dz:
                ok2 = False
                check("V2-entry", False, f"{name} m={m}")
            if m == 2 * R and dz:
                ok4 = False
                check("V4-nearmiss", False, f"{name} m={m}")
        # V3: (z - a)^2 | M at entry
        _, mus, nu = defect_and_spectrum(K, entry)
        a = K.gen
        val, dval, p = K.zero, K.zero, K.one
        for j in range(nu + 1):
            val = K.add(val, K.mul(mus[j], p))
            if j + 1 <= nu:
                dval = K.add(dval, K.scal(Fr(j + 1), K.mul(mus[j + 1], p)))
            p = K.mul(p, a)
        if not (K.is_zero(val) and K.is_zero(dval)):
            ok3 = False
            check("V3-case", False, f"{name}")
    check("V2 entry table: disc_z M zero first at exactly m = 2R+1 "
          "(all points with entry <= 27, every earlier m checked)", ok2)
    check("V3 collision at the trace: (z-a)^2 | M_{2R+1} at every "
          "point", ok3)
    check("V4 the m = 2R near-miss: no collision at m = 2R", ok4)


def main():
    v1()
    v234()
    os.makedirs(os.path.join(os.path.dirname(__file__), "results"),
                exist_ok=True)
    allok = all(c["ok"] for c in CHECKS)
    with open(os.path.join(os.path.dirname(__file__), "results",
                           "verification.json"), "w") as f:
        json.dump({"experiment": "X-108513-torsion-threshold",
                   "checks": CHECKS, "all_ok": allok,
                   "arithmetic_class": "EXACT_RATIONAL (number fields)",
                   "rh_established": False}, f, indent=1)
    print("ALL OK" if allok else "FAILURES PRESENT")
    return 0 if allok else 1


if __name__ == "__main__":
    raise SystemExit(main())
