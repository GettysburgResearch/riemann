"""lemma18_moments.py -- EMPIRICAL sanity check of case 1 (z = 0) of Lemma 18.1
("Fourth moment with short prime factors", label lem:plain) of the OpenAI manuscript
"The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8" (30 Sep 2026; PR 908 import).

Nothing here proves anything.  It evaluates, for exact sextic residue symbols and finitely many K,

    M(K; N1, N2) = (1/#rows) * sum_{k in R_0, 0 < N k <= K} |S_k(N1) S_k(N2)|^2,
    S_k(N)       = N^{-1/2} sum_{l} chi_l(k) W(N l / N),

where k runs over ELEMENTS of O = Z[omega] (rows, as in the lemma), l over all integral ideals
prime to 6 (primary generators; not only squarefree), chi_l(k) = prod_p chi_p(k)^{v_p(l)} with the
manuscript's zero extension, tau = 1, S = {(2), (lambda)}, and W(y) = exp(4 - 1/((y-1)(2-y))) on (1,2).
R_0 = rows whose character n -> chi_n(k) (n prime to 6) is nonprincipal.

Lemma 18.1 case 1 asserts sum_{k in R_0} |S S|^2 << Z^{m+eps} for every bounded n1, n2, i.e.
M(K; N1, N2) << K^eps.  We report M for a K-ladder, the per-class split of the rows, the
contribution of the excluded principal rows, and (for N1 N2 <= 4K) the generalized diagonal
    Diag = sum_{l ~ l'} a_l conj(a_l') prod_{p | l l'} (1 - 1/Np),
where l ~ l' means v_p(l) = v_p(l') mod 6 for all p, and a_l is the coefficient of S(N1) S(N2).

Usage: python3 -I lemma18_moments.py OUT.json K1,K2,... MODE [chunk]
  MODE = bal   : (N1, N2) = (sqrt K, sqrt K)  [this is |S_k(sqrt K)|^4]  and (K^{1/4}, K^{3/4})
  MODE = sq    : (N1, N2) = (sqrt K, sqrt K) only (cheap; used for the largest K)
  MODE = long  : (N1, N2) = (K, K)
  For every length N used, the second moment mean_R0 |S_k(N)|^2 is also recorded.
Single process, single thread.  Uses numerics/eisenstein.py (sha256 bc6af658...e584ae9) unchanged.
"""
import json
import math
import os
import sys
import time

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "numerics"))
import numpy as np                      # noqa: E402
import eisenstein as E                  # noqa: E402

ZERO = E.ZERO
ZETA = E.ZETA


def W(y):
    y = np.asarray(y, dtype=float)
    out = np.zeros_like(y)
    m = (y > 1) & (y < 2)
    out[m] = np.exp(4.0 - 1.0 / ((y[m] - 1.0) * (2.0 - y[m])))
    return out


# ---------------------------------------------------------------- columns: all ideals prime to 6
def all_ideals(primes, X):
    """List of (norm, generator, ((prime_index, exponent), ...)) for all ideals prime to 6, N <= X,
    including the unit ideal.  Generators are products of primary prime generators (primary)."""
    out = [(1, (1, 0), ())]

    def rec(start, gen, n, facs):
        for i in range(start, len(primes)):
            P = primes[i]
            if n * P.N > X:
                break
            g, nn, v = gen, n, 0
            while nn * P.N <= X:
                g, nn, v = E.mul(g, P.gen), nn * P.N, v + 1
                f2 = facs + ((i, v),)
                out.append((nn, g, f2))
                rec(i + 1, g, nn, f2)

    rec(0, (1, 0), 1, ())
    return out


# ---------------------------------------------------------------- row classes
def row_classes(K, xs, ys, primes_small):
    """Class code per row: 0 principal, 1 Theta (bounded conductor: u 2^a lambda^b c^6, nonprincipal),
    2 'quadratic-type' (t c^3), 3 'cubic-type' (t c^2), 4 generic.  t = u 2^a lambda^b."""
    def key(x, y):
        return (int(x) + 2**30) * 2**31 + (int(y) + 2**30)
    # fixed parts t = u 2^a lambda^b with N t <= K; principal iff chi_p(t) = 1 for test primes
    lam = (1, 2)                       # lambda = 1 + 2 omega
    fixed = []
    a = 0
    while 4**a <= K:
        b = 0
        while 4**a * 3**b <= K:
            base = E.mul(E.power((2, 0), a), E.power(lam, b))
            for u in E.UNITS:
                t = E.mul(u, base)
                triv = all(E.sextic_symbol_exact(t, P.gen) == 0 for P in primes_small)
                fixed.append((t, 4**a * 3**b, triv))
            b += 1
        a += 1
    # elements c up to units (one per associate class: primary-or-not doesn't matter; take all, dedupe)
    def elements(nmax):
        cx, cy = E.nonzero_lattice(nmax)
        return list(zip(cx.tolist(), cy.tolist()))
    cls = {}
    for e, code in ((6, None), (3, 2), (2, 3)):
        for t, nt, triv in fixed:
            cmax = (K / nt) ** (1.0 / e)
            cs = elements(int(cmax) + 1) + [(1, 0)]
            for c in cs:
                if E.norm(c) ** e * nt > K:
                    continue
                k = E.mul(t, E.power(c, e))
                kk = key(*k)
                if e == 6:
                    newc = 0 if triv else 1
                else:
                    newc = code
                if kk not in cls or cls[kk] > newc:
                    cls[kk] = newc
    out = np.full(xs.shape, 4, dtype=np.int8)
    keys = (xs + 2**30) * 2**31 + (ys + 2**30)
    ks = np.fromiter(cls.keys(), dtype=np.int64)
    vs = np.fromiter(cls.values(), dtype=np.int8)
    order = np.argsort(ks)
    ks, vs = ks[order], vs[order]
    pos = np.searchsorted(ks, keys)
    pos[pos >= len(ks)] = 0
    hit = ks[pos] == keys
    out[hit] = vs[pos[hit]]
    return out


# ---------------------------------------------------------------- plain sums on a row chunk
def plain_sums(xs, ys, primes, ideals, weights):
    """weights: list of arrays (one per length) of w_l = W(Nl/N)/sqrt(N) aligned with `ideals`.
    Returns list of complex arrays S(k) over the rows."""
    nP = max((f[0] for _, _, fs in ideals for f in fs), default=-1) + 1
    codes = np.empty((nP, xs.size), dtype=np.uint8)
    for i in range(nP):
        codes[i] = primes[i].codes(xs, ys)
    zero = codes == ZERO
    c6 = np.where(zero, 0, codes).astype(np.int16)
    S = [np.zeros(xs.size, dtype=np.complex128) for _ in weights]
    live = [np.nonzero(w)[0] for w in weights]
    need = np.zeros(len(ideals), dtype=bool)
    for lv in live:
        need[lv] = True
    # cache code/zero arrays per ideal along the factor tree (parent = ideal without its last factor)
    cache = {(): (np.zeros(xs.size, dtype=np.int16), np.zeros(xs.size, dtype=bool))}
    Lmax = max(n for n, _, _ in ideals)
    # process ideals in DFS order (all_ideals already yields parents before children)
    for j, (n, g, fs) in enumerate(ideals):
        if fs == ():
            code, z = cache[()]
        else:
            pc, pz = cache[fs[:-1]]
            i, v = fs[-1]
            code = (pc + v * c6[i]) % 6
            z = pz | zero[i]
            if i + 1 < len(primes) and n * primes[i + 1].N <= Lmax:
                cache[fs] = (code, z)          # can still be a parent
        if need[j]:
            val = np.where(z, 0.0, ZETA[code])
            for t, w in enumerate(weights):
                if w[j] != 0.0:
                    S[t] += w[j] * val
    del cache
    return S


# ---------------------------------------------------------------- generalized diagonal
def diagonal(ideals, primes, w1, w2):
    """Generalized diagonal of the mean of |S1 S2|^2 over rows (see module docstring)."""
    nz1 = [j for j in range(len(ideals)) if w1[j] != 0]
    nz2 = [j for j in range(len(ideals)) if w2[j] != 0]
    acc = {}
    for j1 in nz1:
        f1 = dict(ideals[j1][2])
        for j2 in nz2:
            f = dict(f1)
            for i, v in ideals[j2][2]:
                f[i] = f.get(i, 0) + v
            key = tuple(sorted(f.items()))
            acc[key] = acc.get(key, 0.0) + w1[j1] * w2[j2]
    groups = {}
    for fac, a in acc.items():
        cls = tuple((i, v % 6) for i, v in fac if v % 6)
        groups.setdefault(cls, []).append((frozenset(i for i, _ in fac), a))
    tot = 0.0
    for members in groups.values():
        for s1, a1 in members:
            for s2, a2 in members:
                dens = 1.0
                for i in s1 | s2:
                    dens *= 1.0 - 1.0 / primes[i].N
                tot += a1 * a2 * dens
    return tot


def run(K, pairs, chunk, do_diag):
    t0 = time.time()
    Lmax = max(2 * max(p) for p in pairs)
    primes = E.prime_ideals(max(int(Lmax), 50))
    ideals = all_ideals(primes, Lmax)
    norms = np.array([n for n, _, _ in ideals], dtype=float)
    xs_all, ys_all = E.nonzero_lattice(K)
    small = [P for P in primes if P.N < 400][:40]
    cls = row_classes(K, xs_all, ys_all, small)
    res = {"K": K, "rows": int(xs_all.size), "ideals_used": len(ideals), "Lmax": Lmax,
           "class_counts": {str(c): int((cls == c).sum()) for c in range(5)}, "pairs": []}
    lengths = sorted({N for p in pairs for N in p})
    wts = [W(norms / N) / math.sqrt(N) for N in lengths]
    # rows in chunks
    Svals = {N: np.empty(xs_all.size, dtype=np.complex128) for N in lengths}
    for s in range(0, xs_all.size, chunk):
        xs, ys = xs_all[s:s + chunk], ys_all[s:s + chunk]
        S = plain_sums(xs, ys, primes, ideals, wts)
        for N, arr in zip(lengths, S):
            Svals[N][s:s + chunk] = arr
    R0 = cls != 0
    res["second_moment_mean_R0"] = {str(N): float((np.abs(Svals[N][R0]) ** 2).sum() / xs_all.size)
                                    for N in lengths}
    for (N1, N2) in pairs:
        v = np.abs(Svals[N1] * Svals[N2]) ** 2
        R0 = cls != 0
        rec = {"N1": N1, "N2": N2,
               "mean_R0": float(v[R0].sum() / xs_all.size),
               "mean_all_rows_incl_principal": float(v.sum() / xs_all.size),
               "principal_sum_over_R0_sum": float(v[~R0].sum() / max(v[R0].sum(), 1e-300)),
               "max_R0": float(v[R0].max()),
               "class_mean": {str(c): (float(v[cls == c].mean()) if (cls == c).any() else None)
                              for c in range(5)},
               "class_share_of_R0_sum": {str(c): float(v[cls == c].sum() / v[R0].sum())
                                         for c in range(1, 5)}}
        top = np.sort(v[R0])[::-1]
        rec["top10_share_R0"] = float(top[:10].sum() / top.sum())
        if do_diag and N1 * N2 <= 4 * K + 1:
            i1, i2 = lengths.index(N1), lengths.index(N2)
            d = diagonal(ideals, primes, wts[i1], wts[i2])
            rec["diag"] = d
            rec["mean_R0_over_diag"] = rec["mean_R0"] / d if d > 0 else None
        res["pairs"].append(rec)
    res["seconds"] = time.time() - t0
    return res


def main():
    out = sys.argv[1]
    Ks = [int(float(s)) for s in sys.argv[2].split(",")]
    mode = sys.argv[3]
    chunk = int(sys.argv[4]) if len(sys.argv) > 4 else 32768
    primes = E.prime_ideals(2000)
    nchk = E.self_test(primes, n_samples=40)
    allres = {"self_test_checks": nchk, "mode": mode, "runs": []}
    for K in Ks:
        if mode == "bal":
            r = round(K ** 0.5)
            pairs = [(r, r), (round(K ** 0.25), round(K ** 0.75))]
            do_diag = True
        elif mode == "sq":
            r = round(K ** 0.5)
            pairs = [(r, r)]
            do_diag = True
        else:
            pairs = [(K, K)]
            do_diag = K <= 3000
        res = run(K, pairs, chunk, do_diag)
        allres["runs"].append(res)
        print(json.dumps({k: res[k] for k in ("K", "rows", "seconds", "second_moment_mean_R0")}),
              [(p["N1"], p["N2"], round(p["mean_R0"], 4), p.get("mean_R0_over_diag"),
                round(p["principal_sum_over_R0_sum"], 4)) for p in res["pairs"]], flush=True)
        with open(out, "w") as fh:
            json.dump(allres, fh, indent=1)


if __name__ == "__main__":
    main()
