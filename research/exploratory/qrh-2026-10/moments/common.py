"""
common.py -- shared set-up for the EMPIRICAL moment computations (moments.py,
diag.py, balanced.py).  Nothing here proves anything.

Conventions (same as the w5copg numerics, standalone/2026-10-07-openai-quasi-rh/
numerics on origin/claude/openai-math-riemann-analysis-w5copg):
  * O = Z[omega]; u = a + b*omega is the pair (a, b); N(u) = a^2 - ab + b^2.
  * n runs over squarefree ideals prime to 6, represented by their primary
    generator (product of primary prime generators); chi_n(u) = prod (u/p)_6,
    extended by 0 when (u, n) != 1.  nu = 1.
  * W(y) = exp(4 - 1/((y-1)(2-y))) on (1, 2), 0 elsewhere.
  * A_u(D) = sum_n mu(n) chi_n(u) W(N(n)/D).
"""

import ctypes
import math
import os
import subprocess
import sys

for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_v] = "1"
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import numpy as np  # noqa: E402

import eisenstein as E  # noqa: E402

SRC = os.path.join(HERE, "sextic_kernel.c")
LIB = os.path.join(HERE, "build", "sextic_kernel.so")


def W(y):
    y = np.asarray(y, dtype=float)
    out = np.zeros_like(y)
    m = (y > 1) & (y < 2)
    out[m] = np.exp(4.0 - 1.0 / ((y[m] - 1) * (2 - y[m])))
    return out


def load_kernel():
    if not os.path.exists(LIB) or os.path.getmtime(LIB) < os.path.getmtime(SRC):
        os.makedirs(os.path.dirname(LIB), exist_ok=True)
        subprocess.check_call(["gcc", "-O3", "-march=native", "-shared", "-fPIC",
                               "-o", LIB, SRC, "-lm"])
    lib = ctypes.CDLL(LIB)
    P = np.ctypeslib.ndpointer
    i32 = P(dtype=np.int32, flags="C")
    i64 = P(dtype=np.int64, flags="C")
    u8 = P(dtype=np.uint8, flags="C")
    f64 = P(dtype=np.float64, flags="C")
    lib.eval_segments.argtypes = [ctypes.c_int, i32, i64, i64, i64, u8, u8,
                                  ctypes.c_int, i32, i32, f64,
                                  ctypes.c_int64, i64, i64, i64, f64, f64]
    lib.eval_segments.restype = None
    lib.sample_model.argtypes = [ctypes.c_int, f64, ctypes.c_int, i32, i32, f64,
                                 ctypes.c_int64, ctypes.c_uint64, f64]
    lib.sample_model.restype = None
    return lib


class PrimeData:
    """Flattened residue-symbol tables for a list of PrimeIdeal objects."""

    def __init__(self, primes):
        self.primes = primes
        n = len(primes)
        self.kind = np.zeros(n, dtype=np.int32)
        self.mod = np.zeros(n, dtype=np.int64)
        self.r = np.zeros(n, dtype=np.int64)
        self.off = np.zeros(n, dtype=np.int64)
        self.neg = np.zeros(n, dtype=np.uint8)
        self.norm = np.array([P.N for P in primes], dtype=np.int64)
        chunks, seen, pos = [], {}, 0
        for i, P in enumerate(primes):
            key = id(P.table)
            if key not in seen:
                seen[key] = pos
                chunks.append(P.table)
                pos += len(P.table)
            self.off[i] = seen[key]
            self.kind[i] = 0 if P.kind == "split" else 1
            self.mod[i] = P.p
            self.r[i] = P.r if P.kind == "split" else 0
            self.neg[i] = 1 if P.neg else 0
        self.tables = np.ascontiguousarray(np.concatenate(chunks).astype(np.uint8))


class Tree:
    """Prefix tree of squarefree ideals given as increasing tuples of prime
    indices (into a global prime list) with weights."""

    def __init__(self, facs_list, weights, root_weight=0.0):
        used = sorted({i for f in facs_list for i in f})
        self.used = used                      # global prime index of local prime i
        loc = {g: i for i, g in enumerate(used)}
        node = {(): 0}
        parent, pidx, w = [0], [-1], [root_weight]
        # BFS by length so that parents precede children
        order = sorted(range(len(facs_list)), key=lambda t: len(facs_list[t]))
        wmap = {}
        for t in order:
            wmap[facs_list[t]] = wmap.get(facs_list[t], 0.0) + weights[t]
        allpref = set()
        for f in facs_list:
            for L in range(1, len(f) + 1):
                allpref.add(f[:L])
        for f in sorted(allpref, key=lambda f: (len(f), f)):
            node[f] = len(parent)
            parent.append(node[f[:-1]])
            pidx.append(loc[f[-1]])
            w.append(wmap.get(f, 0.0))
        self.parent = np.array(parent, dtype=np.int32)
        self.pidx = np.array(pidx, dtype=np.int32)
        self.pidx[0] = 0
        self.w = np.array(w, dtype=np.float64)
        self.nn = len(parent)
        self.maxdepth = max((len(f) for f in allpref), default=0)
        assert self.maxdepth <= 7


def lattice_segments(Hmax, bmin=0, points=True):
    """Horizontal segments covering {u = a + b omega : 0 < N(u) <= Hmax, b >= bmin}.

    Returns (sb, sa0, slen) and the arrays (a, b, N) of all points in output
    order; the origin is excluded by splitting its segment."""
    bmax = int(2 * math.sqrt(Hmax / 3)) + 2
    sb, sa0, slen = [], [], []
    for b in range(bmin, bmax + 1):
        disc = Hmax - 0.75 * b * b
        if disc < 0:
            continue
        lo = int(math.floor(b / 2 - math.sqrt(disc))) - 1
        hi = int(math.ceil(b / 2 + math.sqrt(disc))) + 1
        while lo * lo - lo * b + b * b > Hmax:
            lo += 1
        while hi * hi - hi * b + b * b > Hmax:
            hi -= 1
        if lo > hi:
            continue
        if b == 0 and lo <= 0 <= hi:
            if lo <= -1:
                sb.append(0); sa0.append(lo); slen.append(-lo)
            if hi >= 1:
                sb.append(0); sa0.append(1); slen.append(hi)
        else:
            sb.append(b); sa0.append(lo); slen.append(hi - lo + 1)
    sb = np.array(sb, dtype=np.int64)
    sa0 = np.array(sa0, dtype=np.int64)
    slen = np.array(slen, dtype=np.int64)
    if not points:
        return sb, sa0, slen
    a = np.concatenate([np.arange(x, x + n, dtype=np.int64) for x, n in zip(sa0, slen)])
    b = np.repeat(sb, slen)
    N = a * a - a * b + b * b
    assert N.min() > 0 and N.max() <= Hmax
    return (sb, sa0, slen), (a, b, N)


def eval_rows(lib, pd, tree, segs, workers=2, nchunks=None):
    """F(u) for all u on the segments, in segment order (threads release the GIL)."""
    from concurrent.futures import ThreadPoolExecutor
    sb, sa0, slen = segs
    # local prime data restricted to the tree's primes
    idx = np.array(tree.used, dtype=np.int64)
    kind = np.ascontiguousarray(pd.kind[idx])
    mod = np.ascontiguousarray(pd.mod[idx])
    r = np.ascontiguousarray(pd.r[idx])
    off = np.ascontiguousarray(pd.off[idx])
    neg = np.ascontiguousarray(pd.neg[idx])
    total = int(slen.sum())
    are = np.empty(total, dtype=np.float64)
    aim = np.empty(total, dtype=np.float64)
    starts = np.concatenate([[0], np.cumsum(slen)])
    nchunks = nchunks or max(1, 4 * workers)
    # split segment list into chunks of roughly equal point count
    cuts = np.searchsorted(starts, np.linspace(0, total, nchunks + 1)[1:-1])
    bounds = [0] + sorted(set(int(c) for c in cuts if 0 < c < len(slen))) + [len(slen)]

    def job(t0, t1):
        n = int(starts[t1] - starts[t0])
        o_re = np.empty(n, dtype=np.float64)
        o_im = np.empty(n, dtype=np.float64)
        lib.eval_segments(len(idx), kind, mod, r, off, neg, pd.tables,
                          tree.nn, tree.parent, tree.pidx, tree.w,
                          t1 - t0, np.ascontiguousarray(sb[t0:t1]),
                          np.ascontiguousarray(sa0[t0:t1]),
                          np.ascontiguousarray(slen[t0:t1]), o_re, o_im)
        are[starts[t0]:starts[t1]] = o_re
        aim[starts[t0]:starts[t1]] = o_im

    with ThreadPoolExecutor(workers) as ex:
        futs = [ex.submit(job, bounds[i], bounds[i + 1]) for i in range(len(bounds) - 1)]
        for f in futs:
            f.result()
    return are + 1j * aim


def lattice_count(H):
    """#{u in O : 0 < N(u) <= H} (exact)."""
    if H < 1:
        return 0
    _, (a, b, N) = lattice_segments(H, bmin=-int(2 * math.sqrt(H / 3)) - 2)
    return len(N)


def family(primes, D):
    """Squarefree primary n prime to 6 with D < N(n) < 2D: (facs, norms, weights mu*W)."""
    sq = E.squarefree_primary(primes, 2 * D)
    ns = [(g, N, f) for g, N, f in sq if D < N < 2 * D]
    facs = [f for _, _, f in ns]
    norms = np.array([N for _, N, _ in ns], dtype=np.int64)
    w = np.array([(-1) ** len(f) for f in facs], dtype=float) * W(norms / D)
    return ns, facs, norms, w
