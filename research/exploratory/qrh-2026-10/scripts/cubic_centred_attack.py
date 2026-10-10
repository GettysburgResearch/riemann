"""cubic_centred_attack.py -- adversarial checks of the inherited centred stage (Lemma
centered-coefficient-invariant, paper.tex l. 13999, and Lemma centered-lattice-cancellation,
l. 14545) as used by the PROPOSED cubic fourth-moment route
(proposed/CUBIC_FOURTH_MOMENT/SKETCH.md, risk item 9).  Source of the lemmas: the external,
unreviewed OpenAI manuscript "The Quasi-Riemann Hypothesis" (30 Sep 2026), pr908 paper.tex,
sha256 42a5ee0f...deac6a3.  Imports a2/eis.py read-only.  Nothing here proves a moment bound.

Sections (each line prints PASS/FAIL; CTRL lines must be DETECTED, i.e. the broken variant fails):
  [P] EXACT (fractions).  Precision ledger of the centred deficit
        A - 2/3 - (5/6) v - beta (L - v - c_lat)_+ + c_C            (M = 1)
      under the two-stage nested order: where the lattice saving is binding, how much lattice
      precision is required against how much the caps provide, and the exact tolerance of three
      loss models (c_C: loss in the whole centred deficit; c_lat: additive loss confined to the
      lattice saving; beta: lattice delivers only a fraction of the min-scale saving).  Sextic
      comparison (kappa = 2/3, threshold 5/6, single window).
  [L] FLOATING weights over an EXACT index set.  The lattice lemma (old-eq:2.18d-f) for the cubic
      Theta: primary z = 1 mod 3 in Z[omega], prime to 2 (one generator per ideal prime to
      S = {2, lambda}); the Theta characters n -> (2/n)_3, (omega/n)_3 evaluated by closed forms
      that are verified EXACTLY against eis.sym_prime; squarefree masks; norm powers q^{it};
      original, reflected-type (conj W^sharp, numerically inverted Mellin) and boxed-derivative
      profiles.  Centred differences L1(U1)L2(U2) - L1(V1)L2(V2) with U1U2 = V1V2 at the cubic
      geometries (L up to 0.43 M, nested C_1 on a reflected comparison) and the sextic one.
  [C] Controls: break one item of the invariant data between the two rectangles (mask, norm
      power, profile, product of scales).  The main term must then survive (no saving).
  [R] FLOATING.  Reflection input: for primitive cubic Hecke characters chi of conductor k
      (N k = 1 mod 9), T_chi(X; W) = eps_k T_{conj chi}(C_k / X; W^sharp) with |eps_k| = 1
      independent of X and W.  So the dual side carries the ORIGINAL (conjugated) coefficients
      and the Gauss-sum phase is a row scalar; control: the unconjugated dual fails.

Run: nice -n 10 python3 -I scripts/cubic_centred_attack.py     (about 1-2 minutes, < 1 GB)
"""
import cmath
import math
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np
from scipy.interpolate import make_interp_spline
from scipy.special import loggamma

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "a2"))
import eis as E  # noqa: E402

RES = []
T0 = time.time()


def check(name, ok, detail=""):
    RES.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + (("   " + detail) if detail else ""))
    sys.stdout.flush()


# =============================================================================================
# [P] exact precision ledger (M = 1)
# =============================================================================================
TWO3, FIVE6, SIX5 = Fr(2, 3), Fr(5, 6), Fr(6, 5)


def lo_hi(A, bprev, mu=Fr(0), cC=Fr(0), clat=Fr(0), beta=Fr(1)):
    """window for L.  deficit(v) = A - 2/3 + cC - (5/6) v - beta (L - v - clat)_+ <= -mu for all
    v in [0, L]: piecewise linear, extreme at v = 0, v = L - clat, v = L."""
    t = A - TWO3 + cC + mu
    lo = max(Fr(0), SIX5 * t + clat, t / beta + clat)
    hi = min((bprev - 1 + A - mu) / 2, A / 2, A - Fr(1, 2) - mu)
    return lo, hi


def covers(b1, top, grid=300, **kw):
    for (a0, a1, bprev) in ((TWO3, b1, TWO3), (b1, top, b1)):
        for s in range(0, grid + 1):
            A = a0 + (a1 - a0) * Fr(s, grid)
            if s == 0 and a0 == TWO3:
                A = a0 + Fr(1, 10 ** 9)
            lo, hi = lo_hi(A, bprev, **kw)
            if lo > hi:
                return False
    return True


def best_split_ok(top, step=Fr(1, 2000), span=40, centre=Fr(31, 36), **kw):
    return any(covers(centre + k * step, top, **kw) for k in range(-span, span + 1))


def part_P():
    print("--- [P] exact precision ledger (M = 1) ---")
    for delta in (Fr(0), Fr(1, 100)):
        mu = (11 - 147 * delta) / 612
        b1 = (4 + 7 * delta + 17 * mu) / 5
        top = 1 + delta
        Ltop = SIX5 * (top - TWO3 + mu)
        ok = covers(b1, top, mu=mu) and not best_split_ok(top, centre=b1, mu=mu + Fr(1, 10 ** 6))
        # lattice precision: required r_req(v) = A - 2/3 - (5/6) v (+ mu); available (L - v)_+
        req0, avail0 = top - TWO3, Ltop
        # slack of the lattice step at v (to the margin mu): L - v - (A - 2/3 - 5v/6 + mu); min at v = L
        slack = [Ltop - v - (top - TWO3 - FIVE6 * v + mu) for v in (Fr(0), Ltop / 2, Ltop)]
        check("[P1] delta=%s: two stages close with mu* = %s at b1 = %s; L(top) = %s (%.4f)"
              % (delta, mu, b1, Ltop, float(Ltop)), ok)
        check("[P2] delta=%s: at v = 0 the lattice must deliver Z^-%s (%.4f); caps give Z^-%s (%.4f); "
              "lattice slack over v: %s -> the binding v = L uses ZERO lattice saving"
              % (delta, req0, float(req0), Ltop, float(Ltop), [round(float(s), 4) for s in slack]),
              slack[-1] == 0 and slack[0] > 0 and avail0 > req0)
    # tolerances (delta = 0 and 1/100)
    for delta in (Fr(0), Fr(1, 100)):
        top = 1 + delta
        cC = (11 - 147 * delta) / 432
        clat = SIX5 * cC
        b1C = (4 + 7 * delta + 12 * cC) / 5
        okC = covers(b1C, top, cC=cC) and not best_split_ok(top, centre=b1C, cC=cC + Fr(1, 10 ** 6))
        okL = covers(b1C, top, clat=clat) and not best_split_ok(top, centre=b1C, clat=clat + Fr(1, 10 ** 6))
        check("[P3] delta=%s: whole-deficit loss tolerated iff c_C < %s (%.5f); lattice-only additive loss iff "
              "c_lat < %s (%.5f)" % (delta, cC, float(cC), clat, float(clat)), okC and okL)
    # beta: fraction of the min-scale saving actually delivered
    mu0 = Fr(11, 612)
    ok56 = covers(Fr(31, 36), Fr(1), mu=mu0, beta=FIVE6)
    lo_b, hi_b = Fr(2, 3), FIVE6
    for _ in range(22):
        mid = (lo_b + hi_b) / 2
        if best_split_ok(Fr(1), step=Fr(1, 400), span=60, centre=Fr(31, 36), beta=mid, grid=120):
            hi_b = mid
        else:
            lo_b = mid
    check("[P4] lattice precision fraction beta: beta >= 5/6 costs nothing (mu* unchanged); two stages need "
          "beta > %.4f; infinitely many stages need beta > 2/3" % float(hi_b), ok56 and Fr(7, 10) < hi_b < FIVE6)
    # sextic single window, for scale: kappa = 2/3, threshold 5/6, (R): 1 - A + 2L <= 5/6
    def sext(A, cC=Fr(0), clat=Fr(0)):
        t = A - FIVE6 + cC
        lo = max(Fr(0), Fr(3, 2) * t + clat, t + clat)
        hi = min((A - Fr(1, 6)) / 2, A / 2, A - Fr(1, 2))
        return lo <= hi
    grid = [FIVE6 + Fr(k, 600) for k in range(1, 101)]
    sC = all(sext(A, cC=Fr(1, 9)) for A in grid) and not sext(Fr(1), cC=Fr(1, 9) + Fr(1, 10 ** 6))
    sL = all(sext(A, clat=Fr(1, 6)) for A in grid) and not sext(Fr(1), clat=Fr(1, 6) + Fr(1, 10 ** 6))
    check("[P5] sextic for scale (L free in its window): tolerates c_C < 1/9 = 0.111 and c_lat < 1/6 = 0.167; "
          "at its own L = M/4 the v = L point is exactly tight (old-eq:2.19 max = A - M)", sC and sL,
          "cubic/sextic tolerance ratio: c_C %.3f, c_lat %.3f" % (float(Fr(11, 432) / Fr(1, 9)), float(Fr(11, 360) / Fr(1, 6))))


# =============================================================================================
# [L] lattice sums over primary generators of ideals prime to 6
# =============================================================================================
DENS = 1.0 / (6.0 * math.sqrt(3.0))      # primary (1/9) and odd (3/4) elements per unit area / (sqrt3/2)


def fast_primes(Nmax):
    """primary prime elements prime to 6 with norm <= Nmax (split pairs; inert p with p^2 <= Nmax)."""
    out = []
    sieve = np.ones(Nmax + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(Nmax ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    for p in range(5, Nmax + 1):
        if not sieve[p]:
            continue
        if p % 3 == 1:
            for b in range(0, int((4 * p / 3) ** .5) + 2):
                D = 4 * p - 3 * b * b
                s_ = math.isqrt(D) if D >= 0 else -1
                if s_ >= 0 and s_ * s_ == D and (b + s_) % 2 == 0:
                    a = (b + s_) // 2
                    assert a * a - a * b + b * b == p
                    out += [E.primary((a, b)), E.primary(E.conj((a, b)))]
                    break
        elif p % 3 == 2 and p * p <= Nmax:
            out.append(E.primary((p, 0)))
    return sorted(set(out), key=E.norm)


def primary_odd(Nmax):
    """all z = a + b w with a = 1 (3), b = 0 (3), N z odd, N z <= Nmax; returns a, b, N (int64), sorted by N."""
    As, Bs = [], []
    bmax = int(math.isqrt(4 * Nmax // 3)) + 3
    for b in range(-(bmax - bmax % 3), bmax + 1, 3):
        rad = Nmax - 3 * b * b / 4.0
        if rad < 0:
            continue
        r = math.sqrt(rad)
        a_lo, a_hi = math.ceil(b / 2 - r) - 1, math.floor(b / 2 + r) + 1
        a = np.arange(a_lo + ((1 - a_lo) % 3), a_hi + 1, 3, dtype=np.int64)
        As.append(a)
        Bs.append(np.full(a.shape, b, dtype=np.int64))
    a = np.concatenate(As)
    b = np.concatenate(Bs)
    N = a * a - a * b + b * b
    keep = (N <= Nmax) & (N % 2 == 1)
    a, b, N = a[keep], b[keep], N[keep]
    o = np.argsort(N, kind="stable")
    return a[o], b[o], N[o]


def divisible(a, b, p):
    c, d = E.conj(p)                      # z conj(p) = (a c - b d, a d + b c - b d)
    n = E.norm(p)
    return ((a * c - b * d) % n == 0) & ((a * d + b * c - b * d) % n == 0)


def theta_exp_2(a, b):
    """(2/n)_3 = (n/2)_3 = n mod 2 in F_4^x = {1, w, w^2}: exponent 0, 1, 2 (n primary, odd)."""
    am, bm = a % 2, b % 2
    return np.where((am == 1) & (bm == 0), 0, np.where((am == 0) & (bm == 1), 1, 2))


def theta_exp_w(N):
    """(omega/n)_3 = omega^{(N n - 1)/3} (supplement), n primary."""
    return ((N - 1) // 3) % 3


def bump(u, h):
    x = u / h
    out = np.zeros_like(u, dtype=float)
    m = np.abs(x) < 1
    out[m] = np.exp(1.0 - 1.0 / (1.0 - x[m] ** 2))
    return out


H = math.log(4.0)                       # profiles live on y in [1/4, 4]


def sharp_on_grid(sig, gam, u):
    """W^sharp for W(y) = exp(-(log y)^2/(2 sig^2)) y^{i gam}: M W^sharp(s) = M W(1-s) G(s)/G(1-s),
    M W(s) = sig sqrt(2 pi) exp(sig^2 (s + i gam)^2 / 2); inverted on Re s = 1/2 (trapezoid)."""
    tau = np.arange(-30.0, 30.0 + 1e-9, 0.02)
    s = 0.5 + 1j * tau
    MW1 = sig * math.sqrt(2 * math.pi) * np.exp(sig ** 2 * ((1 - s) + 1j * gam) ** 2 / 2)
    ratio = np.exp(loggamma(s) - loggamma(1 - s))
    F = MW1 * ratio * 0.02 / (2 * math.pi)
    out = np.empty(u.shape, dtype=complex)
    for i0 in range(0, len(u), 400):
        uu = u[i0:i0 + 400]
        out[i0:i0 + 400] = (np.exp(-np.outer(uu, s)) * F[None, :]).sum(axis=1)
    return out


def make_profiles():
    ug = np.linspace(-H, H, 4001)
    sh = sharp_on_grid(0.3, 0.7, ug)
    spl = make_interp_spline(ug, np.conj(sh), k=5)
    dspl = spl.derivative()

    def W_orig(u):
        return bump(u, H) * (1 + 0.3 * np.cos(3 * u))

    def W_cplx(u):
        return bump(u, H) * np.exp(0.7j * u)

    def W_ref(u):            # conjugated reflected profile, one annular piece
        return np.where(np.abs(u) < H, spl(np.clip(u, -H, H)), 0) * bump(u, H)

    def W_refd(u):           # boxing derivative profile y d/dy W_ref
        b = bump(u, H)
        x = u / H
        db = np.zeros_like(u)
        m = np.abs(x) < 1
        db[m] = b[m] * (-2 * x[m] / (1 - x[m] ** 2) ** 2) / H
        inside = np.abs(u) < H
        uc = np.clip(u, -H, H)
        return np.where(inside, dspl(uc) * b + spl(uc) * db, 0)
    return {"orig": W_orig, "cplx": W_cplx, "ref": W_ref, "refd": W_refd}


def mellin_I(W, t):
    u = np.linspace(-H, H, 20001)
    f = W(u) * np.exp(u * (1 + 1j * t))
    return np.trapezoid(f, u)


class Lattice:
    def __init__(self, Nmax, masks):
        self.a, self.b, self.N = primary_odd(Nmax)
        self.logN = np.log(self.N.astype(float))
        self.mask_ok = {}
        for name, ps in masks.items():
            ok = np.ones(self.N.shape, dtype=bool)
            for p in ps:
                ok &= ~divisible(self.a, self.b, p)
            self.mask_ok[name] = ok
        self.mfac = {name: float(np.prod([1 - 1 / E.norm(p) for p in ps])) for name, ps in masks.items()}
        self.th = {"1": np.zeros(self.N.shape, dtype=np.int64), "2": theta_exp_2(self.a, self.b),
                   "w": theta_exp_w(self.N)}

    def L(self, X, t, W, th="1", mask="none"):
        key = (round(math.log(X), 12), t, id(W), th, mask)
        if not hasattr(self, "_memo"):
            self._memo = {}
        if key not in self._memo:
            self._memo[key] = self._L(X, t, W, th, mask)
        return self._memo[key]

    def _L(self, X, t, W, th, mask):
        lo = np.searchsorted(self.N, X / 4.0, side="left")
        hi = np.searchsorted(self.N, X * 4.0, side="right")
        assert hi < len(self.N) or self.N[-1] >= 4 * X, "enumeration too short"
        sl = slice(lo, hi)
        u = self.logN[sl] - math.log(X)
        w = W(u) * np.exp(1j * t * self.logN[sl])
        ok = self.mask_ok[mask][sl]
        e = self.th[th][sl]
        val = np.exp(2j * math.pi * e / 3.0)
        return complex(np.sum(np.where(ok, w * val, 0)))

    def main(self, X, t, W, th="1", mask="none"):
        if th != "1":
            return 0j
        return DENS * math.pi * self.mfac[mask] * X ** (1 + 1j * t) * mellin_I(W, t)


def part_L(prof):
    print("--- [L] lattice cancellation (floating weights, exact index set) ---")
    # exact verification of the closed forms for the Theta characters
    PR = fast_primes(3000)
    ok2 = all(E.sym_prime((2, 0), p) % 3 == int(theta_exp_2(np.array([p[0]]), np.array([p[1]]))[0]) for p in PR)
    okw = all(E.sym_prime((0, 1), p) % 3 == ((E.norm(p) - 1) // 3) % 3 for p in PR)
    check("[L0] EXACT: (2/p)_3 = p mod 2 and (omega/p)_3 = omega^{(Np-1)/3} for all %d primary primes p, Np <= 3000"
          % len(PR), ok2 and okw)
    p7, p13, p19, p31, p37 = [next(p for p in PR if E.norm(p) == n) for n in (7, 13, 19, 31, 37)]
    p7b = next(p for p in PR if E.norm(p) == 7 and p != p7)
    p13b = next(p for p in PR if E.norm(p) == 13 and p != p13)
    five = (5, 0) if E.is_primary((5, 0)) else E.primary((5, 0))
    masks = {"none": [], "small": [p7, p13, five], "big": [p7, p7b, p13, p13b, p19, p31, p37],
             "small+19": [p7, p13, five, p19]}
    Zexps = (6, 8)
    lat = Lattice(int(4.2 * 10 ** (0.78 * Zexps[-1])) + 10, masks)
    print("    enumerated %d primary odd z, N <= %d  (%.1f s)" % (len(lat.N), int(lat.N[-1]), time.time() - T0))
    # [L1] single lattice sums: error O(Z^eps) absolute, uniformly in X; nonprincipal Theta has no main term
    worst = {}
    for th in ("1", "2", "w"):
        for mask in ("small", "big"):
            for pn in ("orig", "ref", "refd"):
                for t in (0.0, 2.5):
                    for X in np.logspace(1, 6.2, 7):
                        err = abs(lat.L(X, t, prof[pn], th, mask) - lat.main(X, t, prof[pn], th, mask))
                        key = (th, mask)
                        worst[key] = max(worst.get(key, 0), err)
    okL1 = all(v < 2 ** len(masks[k[1]]) * 3 for k, v in worst.items())
    check("[L1] (old-eq:2.18d) |L(X,t) - c X^{1+it} I(t)| = O(2^{omega(R*)}) for X in [10, 1.6e6], 3 Theta chars, "
          "original/reflected/boxed-derivative profiles", okL1,
          "max abs errors " + ", ".join("%s/%s:%.2g" % (k[0], k[1], v) for k, v in sorted(worst.items())))
    # [L2] centred rectangles at the cubic and sextic geometries
    mu0, mu1 = Fr(11, 612), Fr(953, 61200)
    L2top = float(SIX5 * (1 - TWO3 + mu0))
    L2d = float(SIX5 * (Fr(101, 100) - TWO3 + mu1))
    Ap = 1 - 1 + 2 * L2top                              # reflected comparison of C_2 at A = M: total 2L
    L1n = float(SIX5 * (Fr(Ap).limit_denominator(10 ** 6) - TWO3 + mu0))
    b1 = 31 / 36
    Lb1 = float(SIX5 * (Fr(31, 36) - TWO3 + mu0))
    geoms = [  # name, n1, n2, L, A, required lattice precision at v = 0
        ("sextic A=M, L=M/4", 0.5, 0.5, 0.25, 1.0, 1 / 6),
        ("cubic C2, A=M, L=%.4f" % L2top, 0.5, 0.5, L2top, 1.0, 1 / 3),
        ("cubic C2, A=1.01M, L=%.4f" % L2d, 0.505, 0.505, L2d, 1.01, 1.01 - 2 / 3),
        ("cubic C2 bottom, A=b1, n=(.5,.361), L=%.4f" % Lb1, 0.5, b1 - 0.5, Lb1, b1, b1 - 2 / 3),
        ("nested C1 on reflected comparison (%.4f,%.4f), L'=%.4f" % (L2top, L2top, L1n), L2top, L2top, L1n, Ap,
         Ap - 2 / 3),
    ]
    pairs = [("orig", "orig"), ("cplx", "ref"), ("ref", "refd")]
    K = 40.0
    MASKS = ("none", "small", "big")

    def centred(n1, n2, L, ze, p1, p2, t, mask):
        Z = 10.0 ** ze
        U1, U2 = Z ** n1, Z ** n2
        V1 = Z ** L
        V2 = U1 * U2 / V1
        mins = min(U1, U2, V1, V2)
        W1, W2 = prof[p1], prof[p2]
        a1 = lat.L(U1, t, W1, "1", mask) * lat.L(U2, t, W2, "1", mask)
        a2 = lat.L(V1, t, W1, "1", mask) * lat.L(V2, t, W2, "1", mask)
        mt = abs(lat.main(U1, t, W1, "1", mask) * lat.main(U2, t, W2, "1", mask))
        rel = abs(a1 - a2) / mt
        return rel, -math.log(max(rel, 1e-300)) / math.log(Z), mins
    rows = []
    for (name, n1, n2, L, A, req) in geoms:
        for ze in Zexps:
            for (p1, p2) in pairs:
                for t in (0.0, 2.5):
                    for mask in MASKS:
                        rel, robs, mins = centred(n1, n2, L, ze, p1, p2, t, mask)
                        rows.append(dict(g=name, ze=ze, pr=p1 + "/" + p2, t=t, mask=mask, rel=rel, robs=robs,
                                         mins=mins, req=req, om=len(masks[mask])))
    print("    worst achieved precision r_obs (min over 3 profile pairs x 2 t) per mask none/small/big:")
    for (name, n1, n2, L, A, req) in geoms:
        line = []
        for ze in Zexps:
            line.append("Z=1e%d: " % ze + "/".join("%.3f" % min(r["robs"] for r in rows if r["g"] == name and
                                                               r["ze"] == ze and r["mask"] == mk) for mk in MASKS))
        print("    %-58s r_req=%.3f r_min-scale=%.3f | %s" % (name, req, min(n1, n2, L, A - L), " | ".join(line)))
    worstK = max(r["rel"] * r["mins"] / 2 ** r["om"] for r in rows)
    check("[L2a] (old-eq:2.18f) every centred difference obeys rel <= 2^{omega(R*)} K / min-scale with one K = %g "
          "(5 geometries, 2 Z, 3 profile pairs incl. reflected and boxed-derivative, 2 t, 3 masks)" % K,
          worstK <= K, "max rel*minscale/2^omega = %.3g over %d cases" % (worstK, len(rows)))
    okb = all(r["robs"] >= r["req"] for r in rows if r["mask"] in ("none", "small") and r["ze"] == Zexps[-1])
    nbig = sum(1 for r in rows if r["mask"] == "big" and r["robs"] < r["req"])
    check("[L2b] at Z = 1e%d, masks with 2^omega <= 8: achieved precision >= required (A - 2M/3 cubic, "
          "A - 5M/6 sextic) in every case" % Zexps[-1], okb,
          "7-prime mask (2^omega = 128 ~ Z^0.26 at Z = 1e8): %d/%d cases below r_req -- the Z^eps1 of the lemma is "
          "not small at this scale" % (nbig, sum(1 for r in rows if r["mask"] == "big")))
    # [L3] L-sweep at A = M, n = (1/2, 1/2): achieved precision tracks the min scale Z^L up to the cap
    ze = Zexps[-1]
    sweep = []
    okL3 = True
    for L in (0.25, 0.30, 0.35, 0.40, 0.4216, 0.45, 0.48):
        worst = None
        for (p1, p2) in (("cplx", "ref"), ("ref", "refd")):
            for t in (0.0, 2.5):
                for mask in ("none", "small"):
                    rel, robs, mins = centred(0.5, 0.5, L, ze, p1, p2, t, mask)
                    okL3 &= rel <= 2 ** len(masks[mask]) * K / mins
                    worst = robs if worst is None else min(worst, robs)
        sweep.append((L, worst))
    check("[L3] L-sweep at A = M, Z = 1e%d: rel <= 2^omega K Z^{-L} for L = 0.25 ... 0.48 (no loss growing with L)"
          % ze, okL3, "worst r_obs by L: " + ", ".join("%.2f:%.3f" % s for s in sweep))
    return lat, masks


def part_C(lat, prof):
    print("--- [C] controls: break one invariant datum between the rectangles ---")
    ze = 8
    Z = 10.0 ** ze
    L = float(SIX5 * (1 - TWO3 + Fr(11, 612)))
    U1 = U2 = Z ** 0.5
    V1 = Z ** L
    V2 = U1 * U2 / V1
    t = 2.5

    def rel_of(a1, a2, mt):
        r = abs(a1 - a2) / mt
        return r, -math.log(max(r, 1e-300)) / math.log(Z)
    W = prof["orig"]
    mt = abs(lat.main(U1, t, W, "1", "small") * lat.main(U2, t, W, "1", "small"))
    base = lat.L(U1, t, W, "1", "small") * lat.L(U2, t, W, "1", "small")
    cases = {
        "mask differs (second rectangle also coprime to pi_19)":
            lat.L(V1, t, W, "1", "small+19") * lat.L(V2, t, W, "1", "small+19"),
        "norm power differs (t vs t + 0.05)":
            lat.L(V1, t + 0.05, W, "1", "small") * lat.L(V2, t + 0.05, W, "1", "small"),
        "profile differs (W2 replaced by reflected profile in one rectangle)":
            lat.L(V1, t, W, "1", "small") * lat.L(V2, t, prof["ref"], "1", "small"),
        "product of scales differs by Z^{-0.02} (one-rectangle clipping)":
            lat.L(V1, t, W, "1", "small") * lat.L(V2 * Z ** -0.02, t, W, "1", "small"),
    }
    for nm, a2 in cases.items():
        r, ro = rel_of(base, a2, mt)
        check("[C-CTRL] %s: saving lost (r_obs = %.3f < r_req = 1/3)" % (nm, ro), ro < 1 / 3,
              "rel = %.3g" % r)


# =============================================================================================
# [R] reflection: the dual side carries conj chi; the Gauss-sum phase is a row scalar
# =============================================================================================
def all_elements(Nmax):
    bmax = int(math.isqrt(4 * Nmax // 3)) + 2
    As, Bs = [], []
    for b in range(-bmax, bmax + 1):
        rad = Nmax - 3 * b * b / 4.0
        if rad < 0:
            continue
        r = math.sqrt(rad)
        a = np.arange(math.ceil(b / 2 - r) - 1, math.floor(b / 2 + r) + 2, dtype=np.int64)
        As.append(a)
        Bs.append(np.full(a.shape, b, dtype=np.int64))
    a = np.concatenate(As)
    b = np.concatenate(Bs)
    N = a * a - a * b + b * b
    keep = (N <= Nmax) & (N > 0)
    return a[keep], b[keep], N[keep]


def cubic_char_mod_prime(k):
    """exponent table e(z) of (z/k)_3 = omega^e for z in O (z mod k -> Z/P); -1 if k | z."""
    P = E.norm(k)
    c, d = k
    w0 = (-c * pow(d, -1, P)) % P                 # omega -> w0 under O/k = Z/P
    assert (w0 * w0 + w0 + 1) % P == 0
    cube = np.array([pow(x, (P - 1) // 3, P) for x in range(P)], dtype=np.int64)
    lut = np.full(P, -1, dtype=np.int64)
    lut[cube == 1] = 0
    lut[cube == w0] = 1
    lut[cube == (w0 * w0) % P] = 2
    lut[0] = -1
    return P, w0, lut


def part_R():
    print("--- [R] reflection input: dual coefficients and root number (floating) ---")
    ks = []
    for p in fast_primes(4000):
        P = E.norm(p)
        if P % 9 == 1 and P > 2000 and p[1] % P != 0 and all(E.norm(q) != P for q in ks):
            ks.append(p)
        if len(ks) == 2:
            break
    a, b, N = all_elements(40000)
    logN = np.log(N.astype(float))
    sig = 0.5
    profiles = [(0.0, "real log-Gaussian"), (0.8, "twisted y^{0.8i}")]
    tau = np.arange(-20.0, 20.0 + 1e-9, 0.02)
    s = 0.5 + 1j * tau
    ratio = np.exp(loggamma(s) - loggamma(1 - s))
    okall, okctrl, eps_list = True, True, []
    for k in ks:
        P, w0, lut = cubic_char_mod_prime(k)
        e = lut[(a + b * w0) % P]
        chi = np.where(e < 0, 0, np.exp(2j * math.pi * np.maximum(e, 0) / 3))
        C = 3 * P / (4 * math.pi ** 2)
        eps_seen = []
        for gam, gname in profiles:
            MW1 = sig * math.sqrt(2 * math.pi) * np.exp(sig ** 2 * ((1 - s) + 1j * gam) ** 2 / 2)
            F = MW1 * ratio * 0.02 / (2 * math.pi)
            for X in (math.sqrt(C) / 2, math.sqrt(C), 2 * math.sqrt(C)):
                Y = C / X
                u = logN - math.log(X)
                W = np.exp(-u ** 2 / (2 * sig ** 2) + 1j * gam * u)
                lhs = np.sum(chi * W) / 6 / math.sqrt(X)
                # dual: W^sharp at N/Y for distinct norms (grouped)
                m = N <= 1000 * Y
                assert N[-1] >= 1000 * Y
                Nd, inv = np.unique(N[m], return_inverse=True)
                ud = np.log(Nd / Y)
                Ws = np.empty(len(Nd), dtype=complex)
                for i0 in range(0, len(Nd), 300):
                    Ws[i0:i0 + 300] = (np.exp(-np.outer(ud[i0:i0 + 300], s)) * F[None, :]).sum(axis=1)
                rhs = np.sum(np.conj(chi[m]) * Ws[inv]) / 6 / math.sqrt(Y)
                rhs_bad = np.sum(chi[m] * Ws[inv]) / 6 / math.sqrt(Y)
                eps = lhs / rhs
                eps_seen.append(eps)
                okctrl &= abs(abs(lhs / rhs_bad) - 1) > 1e-3 or abs(lhs / rhs_bad - eps_seen[0]) > 1e-3
        spread = max(abs(x - eps_seen[0]) for x in eps_seen)
        g = E.gamma(2, [k])
        okk = abs(abs(eps_seen[0]) - 1) < 1e-7 and spread < 1e-7 and abs(eps_seen[0] - g) < 1e-7
        okall &= okk
        eps_list.append((P, eps_seen[0], spread, g))
        print("    k=%s Nk=%d: eps=%.6f%+.6fi |eps|=%.9f spread over 3 X x 2 W = %.1e; normalized cubic Gauss "
              "sum (eis convention) %.6f%+.6fi" % (k, P, eps_seen[0].real, eps_seen[0].imag, abs(eps_seen[0]),
                                                   spread, g.real, g.imag))
    rowdep = abs(eps_list[0][1] - eps_list[1][1]) > 1e-3
    check("[R1] T_chi(X;W) = eps_k T_{conj chi}(C_k/X; W^sharp) with eps_k = the normalized cubic Gauss sum of k "
          "(|eps_k| = 1), independent of X and W (a row scalar); different rows have different eps_k",
          okall and rowdep)
    check("[R1-CTRL] the dual side with chi instead of conj chi does not satisfy the identity", okctrl)


def main():
    part_P()
    prof = make_profiles()
    lat, masks = part_L(prof)
    part_C(lat, prof)
    part_R()
    npass = sum(ok for _, ok in RES)
    print("SUMMARY %d/%d   (%.0f s)" % (npass, len(RES), time.time() - T0))


if __name__ == "__main__":
    main()
