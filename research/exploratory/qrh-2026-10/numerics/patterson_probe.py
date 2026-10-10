"""
patterson_probe.py -- EMPIRICAL reconnaissance: growth of normalised cubic Gauss-sum sums

    S_k(X) = sum_{c primary, squarefree, (c,6)=1, N c <= X} gamma_2(c) alpha(c)^k,
    gamma_2(c) = N(c)^{-1/2} sum_{v mod c} chi_c(v)^2 e(v/c),  alpha(c) = c/|c|,

for k in {-2,-1,0,1,2,3}.  Heath-Brown--Patterson theory predicts a main term ~ X^{5/6}
for k = 0 (residue of the cubic theta / metaplectic Eisenstein series) and no X^{5/6} term
when the angular twist kills the residue.  A finite fit is NOT a theorem.

gamma_2 at primes is computed by direct summation over the residue field (float);
gamma_2(conj pi) = conj(gamma_2(pi)) is checked for N <= 20000 and then used to halve the
work; composite c use the CRT rule gamma_2(ab) = gamma_2(a)gamma_2(b) chi_b(a)^4 (OpenAI
(4.7) proof; checked numerically by w5copg `eq:crt-a` for N <= 50000, and re-checked here
directly for N <= 3000).

Run:  python3 -I patterson_probe.py results/patterson_probe.json 200000
"""

import json
import math
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import eisenstein as E  # noqa: E402

ZETA = np.exp(1j * np.pi * np.arange(6) / 3)
KS = [-2, -1, 0, 1, 2, 3]


def gamma2_prime(P):
    if P.kind == "split":
        p = P.p
        x = np.arange(1, p, dtype=np.int64)
        c = P.codes(x, np.zeros_like(x)).astype(np.int64)
        a, b = P.gen
        add = np.exp(-2j * np.pi * ((x * b) % p) / p)        # e(x/pi) = exp(2 pi i coord(x conj pi)/p)
        return complex(np.sum(ZETA[(2 * c) % 6] * add)) / math.sqrt(p)
    q = P.p
    X, Y = np.meshgrid(np.arange(q), np.arange(q), indexing="ij")
    X = X.ravel().astype(np.int64)
    Y = Y.ravel().astype(np.int64)
    c = P.codes(X, Y).astype(np.int64)
    nz = c != E.ZERO
    add = np.exp(-2j * np.pi * Y / q)                       # e(v/(-q)) = exp(-2 pi i y/q)
    return complex(np.sum(ZETA[(2 * c[nz]) % 6] * add[nz])) / q


def gamma2_direct(gen, facs, primes):
    """Direct gamma_2(c) for squarefree c (validation only)."""
    a, b = gen
    N = E.norm(gen)
    g = math.gcd(a, b)
    X, Y = np.meshgrid(np.arange(N // g), np.arange(g), indexing="ij")
    X = X.ravel().astype(np.int64)
    Y = Y.ravel().astype(np.int64)
    tot = np.zeros(len(X), dtype=np.int64)
    zero = np.zeros(len(X), dtype=bool)
    for i in facs:
        cc = primes[i].codes(X, Y).astype(np.int64)
        zero |= cc == E.ZERO
        tot += cc
    ca, cb = a - b, -b
    coord = (X * cb + Y * ca - Y * cb) % N
    vals = ZETA[(2 * tot) % 6] * np.exp(2j * np.pi * coord / N)
    return complex(np.sum(vals[~zero])) / math.sqrt(N)


def main():
    out_path = sys.argv[1]
    X = int(sys.argv[2]) if len(sys.argv) > 2 else 200000
    t0 = time.time()
    primes = E.prime_ideals(X)
    g2 = {}
    conj_dev = 0.0
    cube_dev = 0.0
    by_p = {}
    for i, P in enumerate(primes):
        if P.kind == "split" and P.p in by_p and P.N > 20000:
            g2[i] = by_p[P.p][1].conjugate()
            continue
        g = gamma2_prime(P)
        g2[i] = g
        alpha = E.to_complex(P.gen) / math.sqrt(P.N)
        cube_dev = max(cube_dev, abs(g ** 3 + alpha))       # Lemma 4.2: gamma_2^3 = -alpha
        if P.kind == "split":
            if P.p in by_p:
                conj_dev = max(conj_dev, abs(g - by_p[P.p][1].conjugate()))
            else:
                by_p[P.p] = (i, g)
    print(f"{len(primes)} primes, gamma_2 done ({time.time()-t0:.1f}s); "
          f"max|g^3+alpha|={cube_dev:.1e}, max|g(conj)-conj g|={conj_dev:.1e} (N<=20000)", flush=True)

    # DFS over squarefree primary c, with the CRT rule
    checkpoints = sorted({int(round(v)) for v in np.geomspace(1000, X, 25)})
    nodes = []          # (N, gamma_2, gen, facs)

    def rec(start, gen, N, gam, facs):
        for i in range(start, len(primes)):
            P = primes[i]
            if N * P.N > X:
                break
            if facs:
                cp = int(P.codes(np.array([gen[0]], dtype=np.int64),
                                 np.array([gen[1]], dtype=np.int64))[0])  # chi_p(c)
                gnew = gam * g2[i] * ZETA[(4 * cp) % 6]
            else:
                gnew = g2[i]
            g2gen = E.mul(gen, P.gen)
            nodes.append((N * P.N, gnew, g2gen, facs + (i,)))
            rec(i + 1, g2gen, N * P.N, gnew, facs + (i,))

    sys.setrecursionlimit(10000)
    rec(0, (1, 0), 1, 1.0 + 0j, ())
    print(f"{len(nodes)} squarefree c ({time.time()-t0:.1f}s)", flush=True)
    # validation of the CRT recursion against direct sums
    crt_dev = 0.0
    nval = 0
    for (N, g, gen, facs) in nodes:
        if N <= 3000 and len(facs) >= 2:
            crt_dev = max(crt_dev, abs(g - gamma2_direct(gen, facs, primes)))
            nval += 1
    print(f"CRT recursion vs direct sum: {nval} composites N<=3000, max dev {crt_dev:.1e}", flush=True)
    Ns = np.array([n[0] for n in nodes], dtype=np.float64)
    G = np.array([n[1] for n in nodes])
    A = np.array([E.to_complex(n[2]) for n in nodes])
    A = A / np.abs(A)
    order = np.argsort(Ns)
    Ns, G, A = Ns[order], G[order], A[order]
    res = {}
    for k in KS:
        cs = np.cumsum(G * A ** k)
        idx = np.searchsorted(Ns, checkpoints, side="right") - 1
        vals = cs[idx]
        absv = np.abs(vals)
        lx = np.log(np.array(checkpoints, dtype=np.float64))
        sel = np.array(checkpoints) >= 5000
        slope = float(np.polyfit(lx[sel], np.log(absv[sel]), 1)[0])
        # running max of |S| (less sensitive to sign changes)
        runmax = np.maximum.accumulate(np.abs(cs))[idx]
        slope_max = float(np.polyfit(lx[sel], np.log(runmax[sel]), 1)[0])
        res[str(k)] = dict(X=checkpoints, S_re=vals.real.tolist(), S_im=vals.imag.tolist(),
                           absS=absv.tolist(), fit_exponent_absS=slope,
                           fit_exponent_runmax=slope_max,
                           S_over_X56=(absv / np.array(checkpoints) ** (5 / 6)).tolist(),
                           S_over_X12=(absv / np.array(checkpoints) ** 0.5).tolist())
        print(f"k={k:+d}: |S(X)| = {absv[-1]:.1f} at X={checkpoints[-1]}, "
              f"fit exp (X>=5000) {slope:.3f}, runmax exp {slope_max:.3f}, "
              f"|S|/X^(5/6) = {absv[-1]/checkpoints[-1]**(5/6):.3f}, |S|/X^(1/2) = {absv[-1]/checkpoints[-1]**0.5:.2f}",
              flush=True)
    out = dict(label="EMPIRICAL (FLOATING_RECONNAISSANCE)", X=X, n_terms=len(nodes),
               prime_cube_identity_max_dev=cube_dev, conj_shortcut_max_dev=conj_dev,
               crt_vs_direct_max_dev=crt_dev, crt_validated=nval, sums=res,
               runtime_s=time.time() - t0)
    with open(out_path, "w") as f:
        json.dump(out, f, indent=1)
    print(f"done in {out['runtime_s']:.1f}s -> {out_path}")


if __name__ == "__main__":
    main()
