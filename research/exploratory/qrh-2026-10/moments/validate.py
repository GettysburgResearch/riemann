"""
validate.py -- checks the C kernel against independent evaluations (EMPIRICAL tooling).

  1. eisenstein.self_test: residue tables vs exact u^{(Np-1)/6} mod p in O.
  2. A_u(D) from the kernel vs a direct Python sum over n using the exact
     symbol sextic_symbol_exact (no tables), for random u, including u
     with N(u) > p and negative coordinates.
  3. A_{conj u} = conj(A_u), A_{-27u} = A_u, A_{64u} = A_u (exact symmetries).
  4. Timing of the kernel.

Usage: python3 -I validate.py D [n_random_u]
"""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np  # noqa: E402

import common as C
import eisenstein as E


def direct_A(primes, ns, w, u):
    tot = 0j
    cache = {}
    for (g, N, f), wt in zip(ns, w):
        val = 1 + 0j
        for i in f:
            if i not in cache:
                c = E.sextic_symbol_exact(u, primes[i].gen)
                cache[i] = 0 if c == E.ZERO else E.ZETA[c]
            val *= cache[i]
            if val == 0:
                break
        tot += wt * val
    return tot


def kernel_at(lib, pd, tree, pts):
    sb = np.array([p[1] for p in pts], dtype=np.int64)
    sa0 = np.array([p[0] for p in pts], dtype=np.int64)
    slen = np.ones(len(pts), dtype=np.int64)
    return C.eval_rows(lib, pd, tree, (sb, sa0, slen), workers=1, nchunks=1)


def main():
    D = int(sys.argv[1])
    nr = int(sys.argv[2]) if len(sys.argv) > 2 else 40
    lib = C.load_kernel()
    primes = E.prime_ideals(2 * D)
    t0 = time.time()
    nchk = E.self_test(primes, n_samples=60)
    print(f"[1] table self-test: {nchk} exact checks passed ({time.time()-t0:.1f}s)")
    pd = C.PrimeData(primes)
    ns, facs, norms, w = C.family(primes, D)
    tree = C.Tree(facs, w)
    print(f"D={D}: #n={len(ns)}, tree nodes={tree.nn}, depth={tree.maxdepth}, primes used={len(tree.used)}")
    rng = np.random.default_rng(7)
    pts = [(int(a), int(b)) for a, b in rng.integers(-3 * D, 3 * D, size=(nr, 2)) if (a, b) != (0, 0)]
    pts += [(1, 0), (-1, 0), (0, 1), (1, 1), E.power(primes[0].gen, 6), E.power((1, 2), 6)]
    Ak = kernel_at(lib, pd, tree, pts)
    t0 = time.time()
    Ad = np.array([direct_A(primes, ns, w, u) for u in pts])
    err = np.max(np.abs(Ak - Ad))
    print(f"[2] kernel vs exact-symbol direct sum at {len(pts)} u: max |diff| = {err:.2e} "
          f"(max |A| = {np.abs(Ad).max():.2f}; {time.time()-t0:.1f}s)")
    assert err < 1e-8
    conj = [(a - b, -b) for a, b in pts]
    m27 = [E.mul((-27, 0), u) for u in pts]
    m64 = [E.mul((64, 0), u) for u in pts]
    e1 = np.max(np.abs(kernel_at(lib, pd, tree, conj) - np.conj(Ak)))
    e2 = np.max(np.abs(kernel_at(lib, pd, tree, m27) - Ak))
    e3 = np.max(np.abs(kernel_at(lib, pd, tree, m64) - Ak))
    print(f"[3] symmetry errors: conj {e1:.1e}, -27u {e2:.1e}, 64u {e3:.1e}")
    assert max(e1, e2, e3) < 1e-8
    segs, (a, b, N) = C.lattice_segments(D ** 1.25)
    t0 = time.time()
    A = C.eval_rows(lib, pd, tree, segs, workers=2)
    dt = time.time() - t0
    print(f"[4] timing: {len(A)} u x {tree.nn} nodes in {dt:.2f}s "
          f"= {dt / len(A) / tree.nn * 1e9:.2f} ns per (u,node) wall, 2 threads")
    # cross-check one segment against the per-point evaluation
    sel = rng.choice(len(A), 200, replace=False)
    Ap = kernel_at(lib, pd, tree, [(int(a[i]), int(b[i])) for i in sel])
    print(f"    segment vs pointwise max diff {np.max(np.abs(Ap - A[sel])):.1e}")


if __name__ == "__main__":
    main()
