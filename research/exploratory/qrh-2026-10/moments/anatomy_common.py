"""
anatomy_common.py -- shared helpers for the anatomy_*.py scripts (EMPIRICAL, floating point).

Nothing here proves anything.  Conventions are those of common.py / eisenstein.py:
  * O = Z[omega], u = (a, b) = a + b*omega, N(u) = a^2 - ab + b^2;
  * columns n: primary ideals prime to 6 with D < N(n) < 2D; chi_n(u) = prod_p (u/p)_6^{e_p},
    0 if (u, n) != 1; mu-family = squarefree n with weight mu(n) W(N n / D);
  * rows: ALL nonzero u with N(u) <= H (units and non-primary u included).

The C kernel sextic_kernel.c is compiled into a scratch directory given by the environment
variable ANATOMY_BUILD (default: a temporary directory), never into the repository.
"""
import ctypes
import math
import os
import subprocess
import sys
import tempfile

for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "2")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import numpy as np  # noqa: E402

import common as C  # noqa: E402
import eisenstein as E  # noqa: E402

ZETA = E.ZETA


def load_kernel_scratch():
    """Compile sextic_kernel.c into $ANATOMY_BUILD (not the repo) and load it with the
    argtypes of common.load_kernel."""
    bdir = os.environ.get("ANATOMY_BUILD") or tempfile.mkdtemp(prefix="anatomy_build_")
    os.makedirs(bdir, exist_ok=True)
    lib_path = os.path.join(bdir, "sextic_kernel.so")
    if not os.path.exists(lib_path) or os.path.getmtime(lib_path) < os.path.getmtime(C.SRC):
        subprocess.check_call(["gcc", "-O3", "-march=native", "-shared", "-fPIC",
                               "-o", lib_path, C.SRC, "-lm"])
    lib = ctypes.CDLL(lib_path)
    P = np.ctypeslib.ndpointer
    i32 = P(dtype=np.int32, flags="C")
    i64 = P(dtype=np.int64, flags="C")
    u8 = P(dtype=np.uint8, flags="C")
    f64 = P(dtype=np.float64, flags="C")
    lib.eval_segments.argtypes = [ctypes.c_int, i32, i64, i64, i64, u8, u8,
                                  ctypes.c_int, i32, i32, f64,
                                  ctypes.c_int64, i64, i64, i64, f64, f64]
    lib.eval_segments.restype = None
    return lib


def all_primary(primes, X):
    """All primary ideals prime to 6 with 1 < N(n) <= X, as (gen, N, primes tuple, exps tuple)."""
    out = []

    def rec(start, gen, n, facs, exps):
        for i in range(start, len(primes)):
            P = primes[i]
            if n * P.N > X:
                break
            g, nn, e = gen, n, 0
            while nn * P.N <= X:
                g = E.mul(g, P.gen)
                nn *= P.N
                e += 1
                out.append((g, nn, facs + (i,), exps + (e,)))
                rec(i + 1, g, nn, facs + (i,), exps + (e,))

    rec(0, (1, 0), 1, (), ())
    return out


def columns(primes, D):
    """Columns of the extended family: all primary n prime to 6 with D < N n < 2D.
    Returns dict with gens, norms, facs, exps, squarefree mask, mu, liouville, W."""
    allp = [t for t in all_primary(primes, 2 * D) if D < t[1] < 2 * D]
    allp.sort(key=lambda t: (t[1], t[0]))
    norms = np.array([t[1] for t in allp], dtype=np.int64)
    facs = [t[2] for t in allp]
    exps = [t[3] for t in allp]
    sqf = np.array([all(e == 1 for e in ex) for ex in exps])
    omega_big = np.array([sum(ex) for ex in exps])
    lam = (-1.0) ** omega_big
    mu = np.where(sqf, lam, 0.0)
    Wv = C.W(norms / D)
    return dict(gens=[t[0] for t in allp], norms=norms, facs=facs, exps=exps, sqf=sqf,
                mu=mu, lam=lam, W=Wv)


def rows_sorted(Hmax):
    """All nonzero u with N(u) <= Hmax, sorted by norm: (a, b, N)."""
    a, b = E.nonzero_lattice(Hmax)
    N = a * a - a * b + b * b
    o = np.lexsort((b, a, N))
    return a[o], b[o], N[o]


def prime_codes(primes, used, a, b):
    return {i: primes[i].codes(a, b) for i in used}


def chi_block(cols, codes, sl):
    """chi_n(u) for all columns n (rows of the output) and the rows u in slice sl."""
    facs, exps = cols["facs"], cols["exps"]
    R = sl.stop - sl.start
    X = np.empty((len(facs), R), dtype=np.complex128)
    for j, (f, ex) in enumerate(zip(facs, exps)):
        s = np.zeros(R, dtype=np.int64)
        z = np.zeros(R, dtype=bool)
        for i, e in zip(f, ex):
            c = codes[i][sl]
            z |= c == E.ZERO
            s += e * c.astype(np.int64)
        v = ZETA[s % 6]
        v[z] = 0
        X[j] = v
    return X


def row_classes(a, b, Hmax):
    """Disjoint row classes sixth/cube/square/generic (+ rational diagnostic), as in moments.py."""
    import moments as Mo
    sk = Mo.special_keys(Hmax)
    return Mo.classify(a, b, sk)


def prime_gcd_matrix(cols, primes):
    """Boolean matrices: share[n,m] = n, m share a prime ideal; conjshare[n,m] = n shares a prime
    with conj(m) but not with m (i.e. a split prime pi | n with conj(pi) | m)."""
    nc = len(cols["facs"])
    used = sorted({i for f in cols["facs"] for i in f})
    idx = {g: k for k, g in enumerate(used)}
    M = np.zeros((nc, len(used)), dtype=np.float32)
    for j, f in enumerate(cols["facs"]):
        for i in f:
            M[j, idx[i]] = 1
    # conjugate prime index map
    gen2i = {primes[i].gen: i for i in used}
    Mc = np.zeros_like(M)
    for j, f in enumerate(cols["facs"]):
        for i in f:
            P = primes[i]
            if P.kind == "split":
                cg = E.conj(P.gen)          # conj of a primary element is primary
                ci = gen2i.get(cg)
                if ci is not None:
                    Mc[j, idx[ci]] = 1
    share = (M @ M.T) > 0
    conjshare = ((Mc @ M.T) > 0) & ~share
    return share, conjshare


def pair_conductor(cols, primes):
    """Norm of the conductor of chi_n conj(chi_m) as a character on O/(nm):
    product of N p over primes where the exponents of n and m differ mod 6."""
    nc = len(cols["facs"])
    used = sorted({i for f in cols["facs"] for i in f})
    idx = {g: k for k, g in enumerate(used)}
    Ex = np.zeros((nc, len(used)), dtype=np.int8)
    for j, (f, ex) in enumerate(zip(cols["facs"], cols["exps"])):
        for i, e in zip(f, ex):
            Ex[j, idx[i]] = e
    logN = np.array([math.log(primes[i].N) for i in used])
    out = np.zeros((nc, nc))
    for j in range(nc):
        d = (Ex[j][None, :] - Ex) % 6 != 0
        out[j] = d.astype(float) @ logN
    return out          # log of the conductor norm
