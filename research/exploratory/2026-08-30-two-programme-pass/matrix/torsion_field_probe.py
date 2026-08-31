"""Torsion-entry probe in exact number-field arithmetic (stdlib only).

For a torsion point theta with irreducible minimal polynomial C(a) of
2cos(theta), run the WHOLE defect computation at b = 1 with a = the
class of 'a' in K = Q[a]/(C): h-recurrence, pointwise m-th powers,
Sym^m power sums p_j = sum_i q_{(m-2i)j} (b = 1), elementary via
Newton, the T-108500 numerator formula with a 4-term tail
certification, even-m division by (1 + T), triangular Laurent peeling
to the spectrum polynomial M_m over K, and disc_z M_m via the Sylvester
resultant of (M, dM/dz) over K. Since C is irreducible,

    disc_z M_m(a, 1) vanishes at theta  <=>  C(a) | disc_z M_m(a, 1),

so 'disc == 0 in K' is EXACTLY the torsion-locus membership tested in
O-108512 — computed in seconds instead of hours because every scalar
is a <= deg C vector of rationals.

Fourth held-out round predictions (written before the run):
  m = 16, 17, 18: ord-9, ord-18, ord-20, ord-11 all ABSENT;
  m = 19: ord-9 (a^3-3a+1) and ord-18 (a^3-3a-1) PRESENT jointly;
          ord-20 (a^4-5a^2+5, entry m=21) and ord-11 (quintic,
          entry m=23) ABSENT.
Consistency controls at every m: ord-6 (a-1) PRESENT for all m >= 7,
and the machinery re-derives the known m <= 15 table.

Writes matrix/torsion_field_probe.json. rh_established = false.
"""
import json
import sys
import time
from fractions import Fraction as Fr

# ---------------- K = Q[a]/(C) arithmetic (vectors of Fractions) ----------


class NF:
    """Number field Q[a]/(C), C monic with integer coefficients
    (constant first). Elements: coefficient lists length deg C."""

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
        for k in range(len(prod) - 1, self.d - 1, -1):
            c = prod[k]
            if c:
                prod[k] = Fr(0)
                for i in range(self.d):
                    prod[k - self.d + i] -= c * self.C[i]
        return prod[:self.d]

    def is_zero(self, x):
        return all(v == 0 for v in x)

    def inv(self, x):
        # extended Euclid in Q[a] between x (as poly) and C
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
        assert deg(r1) == 0 and r1[0] != 0, "not invertible (C reducible?)"
        c = r1[0]
        out = [v / c for v in s1] + [Fr(0)] * self.d
        return self.reduce(out)

    def reduce(self, p):
        p = list(p) + [Fr(0)] * max(0, self.d - len(p))
        for k in range(len(p) - 1, self.d - 1, -1):
            c = p[k]
            if c:
                p[k] = Fr(0)
                for i in range(self.d):
                    p[k - self.d + i] -= c * self.C[i]
        return p[:self.d]


# ---------------- defect machinery over K (b = 1) -------------------------

def defect_and_spectrum(K, m):
    """Return (M_m as z-coeff list over K, nu) at the point a = gen(K),
    b = 1, with tail certification; None on degeneration (denominator
    collapse makes the formula tail fail — not expected here)."""
    a = K.gen
    dim = m + 1
    # q_j = alpha^j + beta^j with alpha beta = 1, alpha + beta = a
    q = [K.el(2), a]
    for j in range(2, m * (dim + 1) + 2):
        q.append(K.sub(K.mul(a, q[-1]), q[-2]))
    # power sums of Sym^m eigenvalues (b = 1)
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
    # elementary via Newton
    e = [K.one]
    for k in range(1, dim + 1):
        s = K.zero
        for i in range(1, k + 1):
            t = K.mul(e[k - i], ps[i - 1])
            s = K.add(s, t) if i % 2 == 1 else K.sub(s, t)
        e.append(K.scal(Fr(1, k), s))
    # h-sequence and m-th powers
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
        if not K.is_zero(c(r)):
            return None
    # even m: divide by (1 + T)
    eps = 1 if m % 2 == 0 else 0
    nu = (m - 1 - eps) // 2
    if eps:
        quo = [K.zero] * (len(N) - 1)
        rem = [v[:] for v in N]
        for i in range(len(N) - 2, -1, -1):
            quo[i] = rem[i + 1]
            rem[i] = K.sub(rem[i], quo[i])
            rem[i + 1] = K.zero
        if not K.is_zero(rem[0]):
            return None
        N = quo
    # triangular peel on w_j = T^nu (T + 1/T)^j  (b = 1: leading coeff 1)
    from math import comb
    mus = [K.zero] * (nu + 1)
    work = [v[:] for v in N]
    for j in range(nu, -1, -1):
        mu = work[nu + j][:]
        mus[j] = mu
        for i in range(j + 1):
            work[nu + 2 * i - j] = K.sub(work[nu + 2 * i - j],
                                         K.scal(Fr(comb(j, i)), mu))
    if not all(K.is_zero(v) for v in work):
        return None
    # monicity (mu_nu = 1 identically, T-108509): certifies that
    # specialization commutes with the discriminant below
    if not K.is_zero(K.sub(mus[nu], K.one)):
        return None
    return mus, nu


def poly_deg(K, p):
    d = len(p) - 1
    while d >= 0 and K.is_zero(p[d]):
        d -= 1
    return d


def poly_mod(K, P, Q):
    """P mod Q over the field K (Q with invertible leading coeff)."""
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
    """disc_z(M) = 0 in K  <=>  gcd(M, M') nonconstant. M is MONIC in z
    identically (mu_nu = 1, proved), so specializing to the point
    commutes with taking the discriminant, and the zero test is a gcd
    degree test over the field K."""
    P = [v[:] for v in M]
    Q = [K.scal(Fr(j), M[j]) for j in range(1, nu + 1)]
    while True:
        if poly_deg(K, Q) < 0:
            return poly_deg(K, P) >= 1
        P, Q = Q, poly_mod(K, P, Q)


POINTS = {
    "ord6_a1": [-1, 1],                       # a - 1   (R=3,  entry 7)
    "ord8_a2m2": [-2, 0, 1],                  # a^2 - 2 (R=4,  entry 9)
    "ord5_golden": [-1, 1, 1],                # a^2+a-1 (R=5,  entry 11)
    "ord10_golden": [-1, -1, 1],              # a^2-a-1 (R=5,  entry 11)
    "ord12_a2m3": [-3, 0, 1],                 # a^2 - 3 (R=6,  entry 13)
    "ord9_2cos2pi9": [1, -3, 0, 1],           # (R=9,  entry 19)
    "ord18_2cospi9": [-1, -3, 0, 1],          # (R=9,  entry 19)
    "ord20_2cospi10": [5, 0, -5, 0, 1],       # (R=10, entry 21)
    "ord11_2cos2pi11": [1, 3, -3, -4, 1, 1],  # (R=11, entry 23)
    "ord13_2cos2pi13": [-1, 3, 6, -4, -5, 1, 1],  # (R=13, entry 27)
}


ENTRY = {"ord6_a1": 7, "ord8_a2m2": 9, "ord5_golden": 11,
         "ord10_golden": 11, "ord12_a2m3": 13, "ord9_2cos2pi9": 19,
         "ord18_2cospi9": 19, "ord20_2cospi10": 21,
         "ord11_2cos2pi11": 23, "ord13_2cos2pi13": 27}


def entry_z_equals_a(K, m):
    """(z - a)^2 | M_m over K?  (the Theorem's collision-at-the-trace
    statement: M(a) = M'(a) = 0.)"""
    a = K.gen
    M, nu = defect_and_spectrum(K, m)
    val, dval, p = K.zero, K.zero, K.one
    for j in range(nu + 1):
        val = K.add(val, K.mul(M[j], p))
        if j + 1 <= nu:
            dval = K.add(dval, K.scal(Fr(j + 1), K.mul(M[j + 1], p)))
        p = K.mul(p, a)
    return K.is_zero(val) and K.is_zero(dval)


def main():
    out = {"table": {}, "entry_collision_at_z_equals_a": {}}
    for m in range(5, 28):
        t0 = time.time()
        row = {}
        for name, C in POINTS.items():
            K = NF(C)
            r = defect_and_spectrum(K, m)
            if r is None:
                row[name] = "DEGENERATE"
                continue
            M, nu = r
            row[name] = bool(disc_is_zero(K, M, nu)) if nu >= 1 else False
        out["table"][str(m)] = row
        print(f"m={m} ({time.time()-t0:.1f}s) {row}", flush=True)
        json.dump(out, open("matrix/torsion_field_probe.json", "w"),
                  indent=1)
    for name, m in ENTRY.items():
        ok = entry_z_equals_a(NF(POINTS[name]), m)
        out["entry_collision_at_z_equals_a"][name] = {"m": m, "ok": ok}
        print(f"entry z=a check {name} m={m}: {ok}", flush=True)
    json.dump(out, open("matrix/torsion_field_probe.json", "w"),
              indent=1)


if __name__ == "__main__":
    main()
