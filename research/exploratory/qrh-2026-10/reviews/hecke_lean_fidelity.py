#!/usr/bin/env python3
"""EMPIRICAL float check of a READING of the OAI Lean definition HeckeFamily.LFunction.

Status: EMPIRICAL. IEEE double precision (numpy/scipy) plus mpmath at default 15 digits for
the independent Dirichlet L-values. Nothing here is certified, directed or interval
arithmetic. No Lean, Lake or comparator process is started. This script re-implements, by
hand, what the challenge file's definitions say. It checks the reviewer's reading of those
definitions, not the Lean term itself.

Source read (untrusted data):
  ref 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6,
  standalone/2026-10-07-openai-quasi-riemann-import/upstream/lean/ComparatorChallenges/
  HeckeSevenEighths.lean (245 lines): xShift/yShift (l.143-144), parityPair (l.146-148),
  rectangularPair = product of rescaled hurwitzEvenFEPair (l.111-132), finitePair (l.161-192),
  pair (l.194-197), latticeL = pi^s Gamma(s)^-1 Lambda (l.201-202), Character (l.217-224),
  coefficients (l.230-231), LFunction = continuedLattice / 6 (l.235).
  Mathlib: hurwitzEvenFEPair a = (f = evenKernel a, g = cosKernel a, k = 1/2, eps = 1,
  f0 = [a = 0], g0 = 1); evenKernel a x = sum_n exp(-pi (n+a)^2 x);
  cosKernel a x = sum_n cos(2 pi a n) exp(-pi n^2 x); WeakFEPair.Lambda s =
  Lambda0 s - f0/s - eps g0/(k - s), Lambda0 = mellin f_modif.

Checks:
  P  exact (Fraction) check of the parity decomposition: the 2 N^2 shifted rectangular
     theta functions tile Z^2 exactly once by residue class, with norm form x^2 - x y + y^2,
     and exactly one of them has a nonzero constant term f0.
  R  each test character: MulChar axioms on O/NO, zero exactly off units mod m,
     unit triviality, sum of weights (decides g0, hence the pole at s = 1).
  M1 Lean-literal theta/Mellin evaluation of LFunction(s) = pi^s/Gamma(s) * Lambda(s) / 6.
  M2 direct lattice sum  sum_{z != 0} w(z) N(z)^-s / 6  over a norm disc (s = 2 only).
  M3 independent values: Euler product over prime ideals of Z[omega] (s = 2), and for
     base-change and principal characters mpmath zeta / Dirichlet L products (any s).
  NC negative control: a character NOT trivial on units (cubic residue symbol mod 3 + omega)
     gives an identically zero element sum, so `unit_trivial` is load-bearing.

Run: OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 -I hecke_lean_fidelity.py OUT.json
"""
import cmath
import json
import math
import sys
import time
from fractions import Fraction

import mpmath as mp
import numpy as np
from scipy import integrate

T0 = time.time()
OUT = sys.argv[1] if len(sys.argv) > 1 else None
RES = {"status": "EMPIRICAL (floats); checks a reading of the Lean definitions, not the Lean term",
       "source_ref": "31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6",
       "checks": {}}
W3 = cmath.exp(2j * math.pi / 3)


def log(*a):
    print(*a, flush=True)


# ---------------------------------------------------------------- Z[omega] arithmetic
# element (x, y) <-> x + y*omega, omega^2 = -1 - omega, N(x + y omega) = x^2 - x y + y^2
def zmul(a, b):
    (x1, y1), (x2, y2) = a, b
    return (x1 * x2 - y1 * y2, x1 * y2 + y1 * x2 - y1 * y2)


def znorm(a):
    x, y = a
    return x * x - x * y + y * y


def zconj(a):
    x, y = a
    return (x - y, -y)


def zsub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def zdivround(a, b):
    n = znorm(b)
    c = zmul(a, zconj(b))
    return ((2 * c[0] + n) // (2 * n), (2 * c[1] + n) // (2 * n))


def zgcd(a, b):
    while b != (0, 0):
        q = zdivround(a, b)
        a, b = b, zsub(a, zmul(q, b))
    return a


UNITS = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1)]  # +-1, +-omega, +-omega^2
for u in UNITS:
    assert znorm(u) == 1


# ---------------------------------------------------------------- test characters
# Each: period N (with N in the modulus m), modulus generator mu, weight table w[a][b] =
# residue((a + b omega) mod m) for 0 <= a, b < N  (= Lean `coefficients`).
def legendre(v, p):
    v %= p
    if v == 0:
        return 0
    return 1 if pow(v, (p - 1) // 2, p) == 1 else -1


def chi_m4(n):
    return [0, 1, 0, -1][n % 4]


def make_chars():
    C = []
    C.append(dict(name="A_trivial_mod_1", N=1, mu=(1, 0), f=lambda x, y: 1.0 + 0j,
                  kind="principal", note="modulus = top ideal, O/m zero ring, residue = 1; zeta_K"))
    C.append(dict(name="B_principal_mod_2", N=2, mu=(2, 0),
                  f=lambda x, y: 0j if (x % 2 == 0 and y % 2 == 0) else 1.0 + 0j,
                  kind="principal", note="imprimitive principal mod (2): zeta_K(s)(1 - 4^-s)"))
    C.append(dict(name="C_chi-4_o_Norm_mod_4", N=4, mu=(4, 0),
                  f=lambda x, y: complex(chi_m4(x * x - x * y + y * y)),
                  kind="basechange", dir=([0, 1, 0, -1],),
                  note="quadratic, base change of chi_-4: L(chi_-4) L(chi_-4 chi_-3)"))
    C.append(dict(name="D_chi5_o_Norm_mod_5", N=5, mu=(5, 0),
                  f=lambda x, y: complex(legendre(x * x - x * y + y * y, 5)),
                  kind="basechange", dir=([0, 1, -1, -1, 1],),
                  note="quadratic, base change of (./5): L(chi_5) L(chi_5 chi_-3)"))
    # pi = 4 + omega, N(pi) = 13, omega = -4 = 9 mod pi
    C.append(dict(name="E_quadratic_mod_(4+w)_N13", N=13, mu=(4, 1),
                  f=lambda x, y: complex(legendre(x + 9 * y, 13)),
                  kind="genuine", note="quadratic ray character mod a split prime; not Galois-invariant"))
    # pi = 5 + 2 omega, N(pi) = 19 = 1 mod 9, omega = 7 mod pi; cubic residue symbol (trivial on units)
    cub19 = {1: 1.0 + 0j, 7: W3, 11: W3 ** 2}

    def f19(x, y):
        v = (x + 7 * y) % 19
        return 0j if v == 0 else cub19[pow(v, 6, 19)]
    C.append(dict(name="F_cubic_mod_(5+2w)_N19", N=19, mu=(5, 2), f=f19,
                  kind="genuine", note="cubic residue symbol mod pi, N pi = 19 = 1 mod 9, so trivial on units"))
    # negative control: pi = 3 + omega, N = 7, omega = 4 mod pi, cubic symbol NOT trivial on omega
    cub7 = {1: 1.0 + 0j, 2: W3, 4: W3 ** 2}

    def f7(x, y):
        v = (x + 4 * y) % 7
        return 0j if v == 0 else cub7[pow(v, 2, 7)]
    C.append(dict(name="NC_cubic_mod_(3+w)_N7_not_unit_trivial", N=7, mu=(3, 1), f=f7,
                  kind="control", note="violates unit_trivial; not a Character"))
    for c in C:
        N = c["N"]
        c["w"] = np.array([[c["f"](a, b) for b in range(N)] for a in range(N)], dtype=complex)
    return C


def chi_val(c, z):
    N = c["N"]
    return c["w"][z[0] % N, z[1] % N]


def residue_checks(c):
    N, w, mu = c["N"], c["w"], c["mu"]
    out = {}
    # unit triviality
    out["unit_values"] = [complex(chi_val(c, u)) for u in UNITS]
    out["unit_trivial"] = bool(all(abs(chi_val(c, u) - 1) < 1e-12 for u in UNITS))
    # zero exactly at non-units mod m: z is a unit mod (mu) iff gcd(z, mu) is a unit
    bad = 0
    mult_bad = 0
    elems = [(a, b) for a in range(N) for b in range(N)]
    for z in elems:
        unit = (mu == (1, 0)) or znorm(zgcd(mu, z)) == 1 if z != (0, 0) else (mu == (1, 0))
        if unit != (abs(chi_val(c, z)) > 0.5):
            bad += 1
    for z in elems:
        for z2 in elems:
            if abs(chi_val(c, zmul(z, z2)) - chi_val(c, z) * chi_val(c, z2)) > 1e-12:
                mult_bad += 1
    out["nonunit_zero_mismatches"] = bad
    out["multiplicativity_failures"] = mult_bad
    out["weight_sum"] = complex(w.sum())
    out["principal_residue_eq_1"] = bool(np.all(np.abs(np.abs(w) - np.round(np.abs(w))) < 1e-12)
                                         and np.all(np.abs(w[np.abs(w) > 0.5] - 1) < 1e-12))
    return out


# ---------------------------------------------------------------- P: parity decomposition
def parity_check():
    out = {}
    for N in range(1, 7):
        seen = {}
        f0_count = 0
        ok_norm = True
        for a in range(N):
            for b in range(N):
                for e in (0, 1):
                    X = Fraction(2 * a - b - N * e, 2 * N)
                    Y = Fraction(b + N * e, 2 * N)
                    if X.denominator == 1 and Y.denominator == 1:
                        f0_count += 1
                        f0_cell = (a, b, e)
                    for n in range(-6, 7):
                        for m in range(-6, 7):
                            q = N * N * (n + X) ** 2 + 3 * N * N * (m + Y) ** 2
                            x = a + N * (n + m)
                            y = b + N * (2 * m + e)
                            if q != x * x - x * y + y * y:
                                ok_norm = False
                            seen[(x, y)] = seen.get((x, y), 0) + 1
        box = [(x, y) for x in range(-2 * N, 2 * N) for y in range(-2 * N, 2 * N)]
        cover = all(seen.get(p, 0) == 1 for p in box)
        dup = max(seen.values())
        out[N] = dict(norm_identity=ok_norm, box_covered_once=cover, max_multiplicity=dup,
                      f0_count=f0_count, f0_cell=f0_cell)
    return out


# ---------------------------------------------------------------- M1: Lean-literal theta/Mellin
class LeanPair:
    """finitePair over p = ((a,b),e) of parityPair a b N e with weight w(a,b)."""

    def __init__(self, c):
        N = c["N"]
        self.N = N
        A, B, E = np.meshgrid(np.arange(N), np.arange(N), np.arange(2), indexing="ij")
        A, B, E = A.ravel(), B.ravel(), E.ravel()
        self.X = (2 * A - B - N * E) / (2.0 * N)          # xShift
        self.Y = (B + N * E) / (2.0 * N)                  # yShift
        self.wt = c["w"][A, B]                           # fun p => w p.1
        self.u, self.v = float(N * N), float(3 * N * N)   # L^2, 3 L^2
        # rescale: eps = P.eps * u^(-P.k), k = 1/2; product: eps = eps1 * eps2
        self.eps = self.u ** -0.5 * self.v ** -0.5
        Xi = np.isclose(self.X, np.round(self.X))
        Yi = np.isclose(self.Y, np.round(self.Y))
        self.f0 = complex(np.sum(self.wt * (Xi & Yi)))    # sum w_i * f0_i
        self.g0 = complex(np.sum(self.wt * self.eps))     # sum w_i * eps_i * g0_i
        self.nn = np.arange(-40, 41)
        self.cosX = np.cos(2 * np.pi * np.outer(self.X, self.nn))
        self.cosY = np.cos(2 * np.pi * np.outer(self.Y, self.nn))
        nmax = int(math.ceil(math.sqrt(60 * 3 * N * N / math.pi))) + 2
        self.mm = np.arange(1, nmax + 1)
        self.cX1 = 2 * np.cos(2 * np.pi * np.outer(self.X, self.mm))
        self.cY1 = 2 * np.cos(2 * np.pi * np.outer(self.Y, self.mm))

    def even(self, alpha, x):
        # evenKernel alpha x = sum_n exp(-pi (n + alpha)^2 x); alpha array, x scalar
        sh = alpha[:, None] + self.nn[None, :]
        return np.exp(-np.pi * sh ** 2 * x).sum(axis=1)

    def F(self, t):
        return np.sum(self.wt * self.even(self.X, self.u * t) * self.even(self.Y, self.v * t))

    def F_minus_f0(self, t):
        return self.F(t) - self.f0

    def G_minus_g0(self, t):
        # g_p(t) = cosKernel X (t/u) * cosKernel Y (t/v); cosKernel a x = 1 + sum_{m>=1} 2cos(2pi a m) e^{-pi m^2 x}
        eX = np.exp(-np.pi * self.mm ** 2 * (t / self.u))
        eY = np.exp(-np.pi * self.mm ** 2 * (t / self.v))
        dX = self.cX1 @ eX
        dY = self.cY1 @ eY
        return np.sum(self.wt * self.eps * (dX + dY + dX * dY))

    def G(self, t):
        return self.G_minus_g0(t) + self.g0

    def cquad(self, fn, s, a, b):
        re = integrate.quad(lambda t: (fn(t) * t ** s).real, a, b, limit=400, epsabs=1e-14, epsrel=1e-12)[0]
        im = integrate.quad(lambda t: (fn(t) * t ** s).imag, a, b, limit=400, epsabs=1e-14, epsrel=1e-12)[0]
        return complex(re, im)

    def Lambda(self, s):
        s = complex(s)
        brk = [1, 3, 10, 30, 100, 300, 1000, 3000, 1e4, 3e4, 1e5, 1e6]
        I1 = sum(self.cquad(self.F_minus_f0, s - 1, brk[i], brk[i + 1]) for i in range(3))
        I1 += self.cquad(self.F_minus_f0, s - 1, brk[3], np.inf)
        I2 = 0j
        for i in range(len(brk) - 1):
            I2 += self.cquad(self.G_minus_g0, -s, brk[i], brk[i + 1])
        I2 += self.cquad(self.G_minus_g0, -s, brk[-1], np.inf)
        # Lambda = Lambda0 - f0/s - eps g0/(k - s), with eps = 1, k = 1 for finitePair
        return I1 + I2 - self.f0 / s - self.g0 / (1 - s)

    def LFunction(self, s):
        s = complex(s)
        return complex(mp.power(mp.pi, s) * mp.rgamma(s)) * self.Lambda(s) / 6


# ---------------------------------------------------------------- M2: direct lattice sum
def lattice_sum(c, s, X):
    N, w = c["N"], c["w"]
    tot = 0j
    ymax = int(math.isqrt(4 * X // 3)) + 1
    for y in range(-ymax, ymax + 1):
        r = X - 0.75 * y * y
        if r < 0:
            continue
        lo = int(math.floor(y / 2 - math.sqrt(r))) - 1
        hi = int(math.ceil(y / 2 + math.sqrt(r))) + 1
        xs = np.arange(lo, hi + 1)
        q = xs * xs - xs * y + y * y
        m = (q <= X) & (q > 0)
        xs, q = xs[m], q[m].astype(float)
        tot += np.sum(w[xs % N, y % N] * q ** (-s))
    mean = complex(w.sum()) / N ** 2
    tail = mean * (2 * math.pi / math.sqrt(3)) * X ** (1 - s) / (s - 1)
    return tot / 6, (tot + tail) / 6


# ---------------------------------------------------------------- M3: independent values
def primes_upto(P):
    sv = bytearray([1]) * (P + 1)
    sv[0:2] = b"\x00\x00"
    for i in range(2, int(P ** 0.5) + 1):
        if sv[i]:
            sv[i * i::i] = bytearray(len(sv[i * i::i]))
    return [i for i in range(P + 1) if sv[i]]


def split_generator(p):
    # find r with r^2 + r + 1 = 0 mod p, then pi = gcd(p, omega - r)
    for g in range(2, p):
        r = pow(g, (p - 1) // 3, p)
        if r != 1:
            break
    pi = zgcd((p, 0), (-r, 1))
    assert znorm(pi) == p, (p, pi)
    return pi


def euler_product(c, s, P):
    prod = 1 + 0j
    for p in primes_upto(P):
        if p == 3:
            facs = [((1, -1), 3.0)]
        elif p % 3 == 1:
            pi = split_generator(p)
            facs = [(pi, float(p)), (zconj(pi), float(p))]
        else:
            facs = [((p, 0), float(p) ** 2)]
        for z, Nz in facs:
            prod *= 1 / (1 - chi_val(c, z) * Nz ** (-s))
    return prod


def chi_prod(a, b):
    qa, qb = len(a), len(b)
    q = qa * qb // math.gcd(qa, qb)
    return [a[n % qa] * b[n % qb] for n in range(q)]


CHI_M3 = [0, 1, -1]


def independent(c, s):
    s = mp.mpc(s)
    if c["name"].startswith("A_"):
        return complex(mp.zeta(s) * mp.dirichlet(s, CHI_M3))
    if c["name"].startswith("B_"):
        return complex(mp.zeta(s) * mp.dirichlet(s, CHI_M3) * (1 - mp.power(4, -s)))
    if c["kind"] == "basechange":
        d = c["dir"][0]
        return complex(mp.dirichlet(s, d) * mp.dirichlet(s, chi_prod(d, CHI_M3)))
    return None


# ---------------------------------------------------------------- main
def main():
    RES["checks"]["P_parity_decomposition"] = parity_check()
    log("P parity decomposition:", RES["checks"]["P_parity_decomposition"])
    chars = make_chars()
    per = {}
    for c in chars:
        log(f"\n=== {c['name']}  (N = {c['N']}; {c['note']})")
        rc = residue_checks(c)
        log("  R:", {k: v for k, v in rc.items() if k != "unit_values"})
        rec = {"note": c["note"], "period": c["N"], "residue_checks": {
            k: (str(v) if isinstance(v, complex) else v) for k, v in rc.items() if k != "unit_values"}}
        rec["residue_checks"]["unit_values"] = [str(complex(round(v.real, 12), round(v.imag, 12)))
                                                for v in rc["unit_values"]]
        lp = LeanPair(c)
        rec["lean_pair"] = {"f0": str(lp.f0), "g0": str(lp.g0), "eps_each": lp.eps,
                            "count": 2 * c["N"] ** 2}
        log(f"  Lean pair: f0 = {lp.f0:.12g}, g0 = {lp.g0:.12g}, eps_i = {lp.eps:.6g}")
        # functional-equation sanity: F(t) = t^-1 G(1/t)
        fe = []
        for t in (0.37, 0.8):
            lhs, rhs = lp.F(t), lp.G(1 / t) / t
            fe.append(abs(lhs - rhs) / max(1.0, abs(lhs)))
        rec["feq_rel_err"] = fe
        log(f"  F(t) vs G(1/t)/t rel err at t=0.37, 0.8: {fe}")
        # s = 2: M1, M2, M3
        rows = []
        X = 10 ** 6 if c["N"] < 19 else 4 * 10 ** 5
        m1 = lp.LFunction(2)
        m2raw, m2 = lattice_sum(c, 2.0, X)
        ep = euler_product(c, 2.0, 200000)
        ind = independent(c, 2)
        row = {"s": "2", "M1_lean_theta": str(m1), "M2_lattice_raw": str(m2raw),
               "M2_lattice_tailcorr": str(m2), "M2_disc_X": X, "M3_euler_P2e5": str(ep),
               "M3_mpmath": None if ind is None else str(ind),
               "absdiff_M1_M2": abs(m1 - m2), "absdiff_M1_euler": abs(m1 - ep),
               "absdiff_M1_mpmath": None if ind is None else abs(m1 - ind)}
        rows.append(row)
        log(f"  s=2: M1 {m1:.12f}\n       M2 {m2:.12f} (raw {m2raw:.12f}, X={X})"
            f"\n       Euler {ep:.12f}" + ("" if ind is None else f"\n       mpmath {ind:.12f}"))
        if c["kind"] != "control":
            for s in (1.5, 0.9, complex(0.95, 3.0), complex(0.876, 6.0)):
                m1s = lp.LFunction(s)
                inds = independent(c, s)
                rows.append({"s": str(s), "M1_lean_theta": str(m1s),
                             "M3_mpmath": None if inds is None else str(inds),
                             "absdiff_M1_mpmath": None if inds is None else abs(m1s - inds)})
                log(f"  s={s}: M1 {m1s:.12f}" + ("" if inds is None else f"   mpmath {inds:.12f}  diff {abs(m1s - inds):.2e}"))
        rec["values"] = rows
        per[c["name"]] = rec
    # analytic cross-check: residue of the Lean trivial-character LFunction at s = 1 is
    # pi * g0 / 6 with g0 = 2/sqrt(3) (N = 1), versus the class number formula pi/(3 sqrt 3)
    res_lean = math.pi * (2 / math.sqrt(3)) / 6
    res_cnf = 2 * math.pi / (6 * math.sqrt(3))
    RES["checks"]["trivial_residue_at_1"] = {"lean_reading": res_lean, "class_number_formula": res_cnf}
    log(f"\nresidue at 1 (trivial): Lean reading {res_lean:.15f}, class number formula {res_cnf:.15f}")
    RES["checks"]["characters"] = per
    RES["runtime_s"] = round(time.time() - T0, 1)
    if OUT:
        with open(OUT, "w") as fh:
            json.dump(RES, fh, indent=1, default=str)
    log(f"done in {RES['runtime_s']} s")


if __name__ == "__main__":
    main()
