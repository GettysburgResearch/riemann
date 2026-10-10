"""
b2_common.py -- set-up for the B2 bilinear-form numerics (EMPIRICAL; binary64, NOT certified).

Object (BILINEAR_B2.md Sec. 1; [OAI] TeX l. 3428-3476, 2818-2829, 8097): the separated low-side
form at a fixed height v = 0,

    S = sum_m w(m) xi(m) A_m B_m,
    A_m = Y^{-1} sum_s W(q_s/Y) (q_s/Y)^{-1/2} gamma_1(s) conj(chi_s(-m))      [= TeX l. 3461 with
          q_s^{-1/2} g_{chi_s}(s,-m) = gamma_1(s) conj(chi_s(-m)) for squarefree s]
    B_m = sum_{c sf, n} gamma_2(c) conj(alpha(c n^3)) chi_c(m) chi_n(m)^3 q_c^{-1/2} q_n^{-1}
          V(q_c q_n^3 / Z)                                                       [TeX l. 2818-2829]

Simplifications (documented in B2_NUMERICS.md): nu = 1 (fixed ray twists nu_sigma theta, the
G-expansion coefficients a_theta, eta, chi_s(b*)/(tau xi(s)) and the ray class sigma dropped);
s squarefree; V = W = the bump of moments/common.py on (1, 2) instead of the Gaussian V_G;
row weight w(m) = W(q_m/Q) instead of Omega; v = 0 (plus a grid of heights for statistics).
xi(m) (the primitive character mod 2*lambda of TeX l. 3349) is kept; it masks (m, 6) = 1.

Reused unchanged: moments/eisenstein.py (residue tables, PrimeIdeal), moments/common.py (W),
a2/eis.py (exact symbols / direct Gauss sums for validation).  New C: b2_kernel.c (compiled
into the scratchpad only).
"""
import ctypes
import math
import os
import subprocess
import sys

for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "2")
HERE = os.path.dirname(os.path.abspath(__file__))
QRH = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(QRH, "moments"))
sys.path.insert(0, os.path.join(QRH, "a2"))
import numpy as np  # noqa: E402

import eisenstein as E  # noqa: E402  (moments/eisenstein.py)
from common import W  # noqa: E402     (moments/common.py)
import eis  # noqa: E402               (a2/eis.py, exact arithmetic)

SCR = os.environ.get("B2_SCRATCH", "/tmp/claude-0/-home-user-riemann/"
                     "0f40aeb7-3b99-59f5-bdd3-8b0e9e4502dc/scratchpad/b2")
ZERO = E.ZERO
ZETA = E.ZETA
UNITS = E.ZETA_O                    # zeta^k as (a, b)


# ----------------------------------------------------------------------------- C kernel
def load_kernel():
    src = os.path.join(HERE, "b2_kernel.c")
    lib = os.path.join(SCR, "b2_kernel.so")
    os.makedirs(SCR, exist_ok=True)
    if not os.path.exists(lib) or os.path.getmtime(lib) < os.path.getmtime(src):
        subprocess.check_call(["gcc", "-O3", "-march=native", "-fopenmp", "-shared", "-fPIC",
                               "-o", lib, src, "-lm"])
    L = ctypes.CDLL(lib)
    P = np.ctypeslib.ndpointer
    i32, i64 = P(dtype=np.int32, flags="C"), P(dtype=np.int64, flags="C")
    u8, f64 = P(dtype=np.uint8, flags="C"), P(dtype=np.float64, flags="C")
    L.gauss2_split.argtypes = [ctypes.c_int64, i64, i64, i64, f64, f64]
    L.gauss2_split.restype = None
    L.eval_B.argtypes = [i32, i64, i64, i64, u8, u8,
                         ctypes.c_int64, i32, i32, i64, i32, i32,
                         ctypes.c_int32, u8, u8,
                         ctypes.c_int64, i64, i64, u8, i32, i32,
                         ctypes.c_int, f64, f64, f64, f64]
    L.eval_B.restype = None
    return L


# ----------------------------------------------------------------------------- integers
def spf_sieve(N):
    spf = np.zeros(N + 1, dtype=np.int32)
    for i in range(2, int(N ** 0.5) + 1):
        if spf[i] == 0:
            blk = spf[i * i::i]
            blk[blk == 0] = i
    idx = np.nonzero(spf == 0)[0]
    spf[idx] = idx
    return spf


def factor_int(n, spf):
    out = {}
    while n > 1:
        p = int(spf[n])
        out[p] = out.get(p, 0) + 1
        n //= p
    return out


def primary_lattice(lo, hi):
    """All primary (a, b) (a = 1 mod 3, b = 0 mod 3) with lo < N(a + b w) <= hi."""
    bmax = int(2 * math.sqrt(hi / 3)) + 3
    A, B = [], []
    for b in range(-bmax - (-bmax) % 3, bmax + 1, 3):
        disc = hi - 0.75 * b * b
        if disc < 0:
            continue
        a0 = int(math.floor(b / 2 - math.sqrt(disc))) - 2
        a1 = int(math.ceil(b / 2 + math.sqrt(disc))) + 2
        a0 += (1 - a0) % 3
        a = np.arange(a0, a1 + 1, 3, dtype=np.int64)
        n = a * a - a * b + b * b
        k = (n > lo) & (n <= hi)
        A.append(a[k])
        B.append(np.full(int(k.sum()), b, dtype=np.int64))
    a, b = np.concatenate(A), np.concatenate(B)
    return a, b, a * a - a * b + b * b


def divides(p, z):
    """p | z in O, p, z = (a, b) tuples of python ints."""
    c, d = E.mul(z, E.conj(p))
    n = E.norm(p)
    return c % n == 0 and d % n == 0


def exact_div(z, p):
    c, d = E.mul(z, E.conj(p))
    n = E.norm(p)
    return (c // n, d // n)


# ----------------------------------------------------------------------------- primes
class Primes:
    """Primary primes of O prime to 6 with norm <= X; split ones carry (p, r, b)."""

    def __init__(self, X, spf):
        a, b, n = primary_lattice(3, X)
        isp = (n >= 5) & (spf[n] == n) & (n % 3 == 1)
        self.split = list(zip(a[isp].tolist(), b[isp].tolist()))
        self.inert = [(-q, 0) for q in range(5, int(math.isqrt(X)) + 1)
                      if spf[q] == q and q % 3 == 2]
        self.by_norm = {}
        for g in self.split:
            self.by_norm.setdefault(E.norm(g), []).append(g)
        for g in self.inert:
            self.by_norm[g[0] * g[0]] = [g]


def gamma2_table(X, spf, lib, log=print):
    """gamma_2 at all primary primes with norm <= X (cached in the scratchpad)."""
    fn = os.path.join(SCR, f"gamma2_{X}.npz")
    if os.path.exists(fn):
        d = np.load(fn)
        return {(int(a), int(b)): complex(g) for a, b, g in zip(d["a"], d["b"], d["g"])}
    pr = Primes(X, spf)
    seen, todo = set(), []
    for g in pr.split:
        cg = (g[0] - g[1], -g[1])
        if cg in seen:
            continue
        seen.add(g)
        todo.append(g)
    P = np.array([E.norm(g) for g in todo], dtype=np.int64)
    Bv = np.array([g[1] for g in todo], dtype=np.int64)
    Rv = np.array([(-g[0] * pow(g[1], -1, E.norm(g))) % E.norm(g) for g in todo], dtype=np.int64)
    ore, oim = np.zeros(len(todo)), np.zeros(len(todo))
    import time
    t0 = time.time()
    lib.gauss2_split(len(todo), P, Bv, Rv, ore, oim)
    log(f"  gamma_2 at {len(todo)} split prime pairs (N <= {X}) in {time.time()-t0:.1f}s")
    out = {}
    for g, re, im in zip(todo, ore, oim):
        out[g] = complex(re, im)
        out[(g[0] - g[1], -g[1])] = complex(re, -im)   # gamma_2(conj pi) = conj gamma_2(pi)
    for g in pr.inert:
        out[g] = gamma_direct_inert(2, -g[0])
    ks = list(out)
    np.savez(fn, a=np.array([k[0] for k in ks]), b=np.array([k[1] for k in ks]),
             g=np.array([out[k] for k in ks]))
    return out


def gamma_direct_inert(j, q):
    """gamma_j(-q) = q^{-1} sum_{x, y mod q} chi(x + y w)^j e((x + y w)/(-q));
    e(v/(-q)) = exp(2 pi i d / q^2) with v * (-q) = c + d w, d = -q y -> exp(-2 pi i y / q)."""
    tab = E._inert_table(q)
    x, y = np.meshgrid(np.arange(q), np.arange(q), indexing="ij")
    codes = tab[x * q + y]
    ok = codes < ZERO
    val = np.where(ok, ZETA[(j * codes.astype(np.int64)) % 6], 0)
    return complex((val * np.exp(-2j * np.pi * y / q)).sum() / q)


def gamma_direct_split(j, g):
    """gamma_j(pi) by direct summation over Z/p (numpy)."""
    p = E.norm(g)
    r = (-g[0] * pow(g[1], -1, p)) % p
    x = np.arange(p)
    codes = E.PrimeIdeal.codes.__get__(_pi_obj(g))(x, np.zeros(p, dtype=np.int64))
    ok = codes < ZERO
    val = np.where(ok, ZETA[(j * codes.astype(np.int64)) % 6], 0)
    return complex((val * np.exp(-2j * np.pi * x * g[1] / p)).sum() / math.sqrt(p))


def _pi_obj(g):
    P = E.PrimeIdeal()
    p = E.norm(g)
    P.gen, P.N, P.p, P.kind = g, p, p, "split"
    P.r = (-g[0] * pow(g[1], -1, p)) % p
    P.table, P.neg = E._split_table(p, P.r), False
    return P


# ----------------------------------------------------------------------------- symbols
_SYM = {}


def sym(u, p):
    """(u/p)_6 code (0..5) or None, exact (a2/eis.py)."""
    key = (u, p)
    v = _SYM.get(key)
    if v is None and key not in _SYM:
        v = eis.sym_prime(eis.reduce_mod(u, p), p)
        _SYM[key] = v
    return v


def unit_code(prime_norms):
    """code of chi_c(zeta) = prod_p zeta^{(Np - 1)/6}."""
    return sum((N - 1) // 6 for N in prime_norms) % 6


def cls4(a, b):
    return (a % 4) * 4 + (b % 4)


def build_R_table(primes, npairs=4000, seed=7):
    """R[cls(m')][cls(c)] = code(chi_c(m')) - code(chi_{m'}(c)) on coprime primary pairs (must
    be 0 or 3 and a function of the classes mod 4)."""
    rng = np.random.default_rng(seed)
    T = -np.ones((16, 16), dtype=np.int64)
    viol = 0
    for _ in range(npairs):
        i, j = rng.choice(len(primes), 2, replace=False)
        x, y = primes[i], primes[j]
        if E.norm(x) == E.norm(y):
            continue
        k1, k2 = sym(x, y), sym(y, x)       # chi_y(x), chi_x(y)
        d = (k1 - k2) % 6
        ci, cj = cls4(*x), cls4(*y)
        if d not in (0, 3):
            viol += 1
        if T[ci, cj] < 0:
            T[ci, cj] = d
        elif T[ci, cj] != d:
            viol += 1
    filled = int((T >= 0).sum())
    T[T < 0] = 0
    return T.astype(np.uint8), viol, filled


# ----------------------------------------------------------------------------- families
def factor_element(z, N, spf, pr):
    """Primary-prime factorisation of z (prime to 6): list of (prime gen, exponent)."""
    out = []
    for p, v in factor_int(N, spf).items():
        if p % 3 == 2:
            out.append(((-p, 0), v // 2))
            continue
        for g in pr.by_norm[p]:
            e, w = 0, z
            while divides(g, w):
                w = exact_div(w, g)
                e += 1
            if e:
                out.append((g, e))
    return out


def theta_terms(Z, spf, pr, g2, cube_seed=11, log=print):
    """Terms (c, n) of B with Z < q_c q_n^3 < 2Z; returns dict of arrays."""
    # n: primary, prime to 6, q_n^3 < 2Z
    nmax = int((2 * Z) ** (1 / 3)) + 1
    na, nb, nN = primary_lattice(0, nmax)
    nl = [(1, 0)] + [(int(a), int(b)) for a, b, N in zip(na, nb, nN) if N % 2 and N ** 3 < 2 * Z
                     and N > 1]
    nl = sorted(set(nl), key=lambda g: (E.norm(g), g))
    cx, cy, cN, uc, cc, ni, gam, alc = [], [], [], [], [], [], [], []
    pairsym = {}
    nsq = 0
    rcube, crand = {}, []
    rng = np.random.default_rng(cube_seed)
    for k, n in enumerate(nl):
        qn = E.norm(n)
        lo, hi = Z / qn ** 3, 2 * Z / qn ** 3
        a, b, N = primary_lattice(math.floor(lo), math.ceil(hi))
        keep = (N > lo) & (N < hi) & (N % 2 == 1)
        an = complex(n[0] - 0.5 * n[1], n[1] * math.sqrt(3) / 2)
        an = an / abs(an)
        for x, y, Nc in zip(a[keep].tolist(), b[keep].tolist(), N[keep].tolist()):
            fac = factor_element((x, y), Nc, spf, pr)
            if any(e > 1 for _, e in fac):
                continue
            nsq += 1
            ps = [g for g, _ in fac]
            gm = 1.0 + 0j
            for g in ps:
                gm *= g2[g]
            for i in range(len(ps)):
                for j in range(i + 1, len(ps)):
                    p1, p2 = sorted((ps[i], ps[j]), key=E.norm)
                    key = (p1, p2)
                    if key not in pairsym:
                        pairsym[key] = sym(p2, p1)       # chi_{p1}(p2); ^4 symmetric
                    gm *= ZETA[(4 * pairsym[key]) % 6]
            rc = 0
            for g in ps:
                if g not in rcube:
                    rcube[g] = int(rng.integers(0, 3))
                rc += 2 * rcube[g]                       # omega^k = zeta^{2k}
            crand.append(rc % 6)
            cx.append(x); cy.append(y); cN.append(Nc)
            uc.append(unit_code([E.norm(g) for g in ps]))
            cc.append(cls4(x, y)); ni.append(k); gam.append(gm)
            ac = complex(x - 0.5 * y, y * math.sqrt(3) / 2)
            alc.append(np.conj(ac / abs(ac)) * np.conj(an) ** 3)
    cN = np.array(cN, dtype=np.float64)
    qn = np.array([E.norm(nl[k]) for k in ni], dtype=np.float64)
    wgt = np.array(alc) * cN ** -0.5 / qn * W(cN * qn ** 3 / Z)
    return dict(cx=np.array(cx, dtype=np.int64), cy=np.array(cy, dtype=np.int64),
                ucode=np.array(uc, dtype=np.uint8), ccls=np.array(cc, dtype=np.int32),
                nidx=np.array(ni, dtype=np.int32), gamma2=np.array(gam), weight=wgt,
                N=cN, nlist=nl, cubecode=np.array(crand, dtype=np.int64))


def rows(Q, spf, pr_small, pidx):
    """Rows m = zeta^u m' with Q < q_m < 2Q, (m, 6) = 1."""
    a, b, N = _lattice_all(Q, 2 * Q)
    keep = (N % 2 == 1) & (N % 3 != 0) & (N > Q) & (N < 2 * Q)
    a, b, N = a[keep], b[keep], N[keep]
    u = np.full(len(a), -1, dtype=np.int32)
    ma, mb = np.zeros_like(a), np.zeros_like(b)
    for k in range(6):
        inv = UNITS[(6 - k) % 6]
        x = a * inv[0] - b * inv[1]
        y = a * inv[1] + b * inv[0] - b * inv[1]
        ok = (x % 3 == 1) & (y % 3 == 0) & (u < 0)
        u[ok] = k
        ma[ok], mb[ok] = x[ok], y[ok]
    assert (u >= 0).all()
    rowptr, ridx, rexp = [0], [], []
    for x, y, n in zip(ma.tolist(), mb.tolist(), N.tolist()):
        for g, e in factor_element((x, y), n, spf, pr_small):
            ridx.append(pidx[g]); rexp.append(e)
        rowptr.append(len(ridx))
    # xi(m): order-3 character mod 2 times quadratic character mod lambda (TeX l. 3349)
    k2 = np.where((a % 2 == 1) & (b % 2 == 0), 0, np.where((a % 2 == 0) & (b % 2 == 1), 1, 2))
    xl = np.where((a + b) % 3 == 1, 0, 3)
    xi = ZETA[(2 * k2 + xl) % 6]
    return dict(a=a, b=b, N=N, u=u, ma=ma, mb=mb, mcls=np.array(
        [cls4(x, y) for x, y in zip(ma.tolist(), mb.tolist())], dtype=np.int32),
        rowptr=np.array(rowptr, dtype=np.int64), ridx=np.array(ridx, dtype=np.int32),
        rexp=np.array(rexp, dtype=np.int32), xi=xi)


def _lattice_all(lo, hi):
    bmax = int(2 * math.sqrt(hi / 3)) + 2
    A, B = [], []
    for b in range(-bmax, bmax + 1):
        disc = hi - 0.75 * b * b
        if disc < 0:
            continue
        a = np.arange(int(math.floor(b / 2 - math.sqrt(disc))) - 1,
                      int(math.ceil(b / 2 + math.sqrt(disc))) + 2, dtype=np.int64)
        n = a * a - a * b + b * b
        k = (n > lo) & (n <= hi)
        A.append(a[k]); B.append(np.full(int(k.sum()), b, dtype=np.int64))
    a, b = np.concatenate(A), np.concatenate(B)
    return a, b, a * a - a * b + b * b


def codes_at(P, x, y):
    return P.codes(np.asarray(x, dtype=np.int64), np.asarray(y, dtype=np.int64))


def add_codes(acc, c, e=1):
    """acc, c uint8 code arrays; returns acc + e*c with ZERO absorbing."""
    out = acc.astype(np.int64) + e * c.astype(np.int64)
    bad = (acc >= ZERO) | (c >= ZERO)
    out = out % 6
    out[bad] = ZERO
    return out.astype(np.uint8)


def ncodes(R, nl, primes_small, gidx, spf, pr):
    """ncode[i, k] = code of chi_{n_k}(m_i)^3 (zero-extended)."""
    out = np.zeros((len(R["a"]), len(nl)), dtype=np.uint8)
    cache = {}
    for k, n in enumerate(nl):
        acc = np.zeros(len(R["a"]), dtype=np.uint8)
        if n != (1, 0):
            fac = factor_element(n, E.norm(n), spf, pr)
            for g, e in fac:
                if g not in cache:
                    cache[g] = codes_at(primes_small[gidx[g]], R["a"], R["b"])
                acc = add_codes(acc, cache[g], 3 * e)
        out[:, k] = acc
    return out


def s_family(Y, primes_small, gidx):
    """Squarefree primary s prime to 6 with Y < q_s < 2Y: factors, gamma_1(s), weights."""
    sq = E.squarefree_primary(primes_small, 2 * Y)
    fam = [(g, N, f) for g, N, f in sq if Y < N < 2 * Y]
    g1p = {}
    out = []
    for g, N, f in fam:
        ps = [primes_small[i].gen for i in f]
        val = 1.0 + 0j
        for p in ps:
            if p not in g1p:
                g1p[p] = gamma1_prime(p)
            val *= g1p[p]
        for i in range(len(ps)):
            for j in range(i + 1, len(ps)):
                # gamma_1(ab) = gamma_1(a) gamma_1(b) chi_a(b) chi_b(a)
                val *= ZETA[(sym(ps[j], ps[i]) + sym(ps[i], ps[j])) % 6]
        out.append((g, N, f, val))
    return out


def gamma1_prime(g):
    if g[1] == 0:
        return gamma_direct_inert(1, -g[0])
    return gamma_direct_split(1, g)


def s_codes(fam, primes_small, R):
    """codes of chi_s(-m) for all s (rows) and m (cols)."""
    mx, my = -R["a"], -R["b"]
    cache = {}
    M = np.zeros((len(fam), len(mx)), dtype=np.uint8)
    for i, (g, N, f, _) in enumerate(fam):
        acc = np.zeros(len(mx), dtype=np.uint8)
        for j in f:
            if j not in cache:
                cache[j] = codes_at(primes_small[j], mx, my)
            acc = add_codes(acc, cache[j])
        M[i] = acc
    return M


def code_val(codes):
    v = np.zeros(codes.shape, dtype=np.complex128)
    ok = codes < ZERO
    v[ok] = ZETA[codes[ok].astype(np.int64) % 6]
    return v
