"""Memory-lean stage 1 for the T-108513 converse sieve at large m
(the direct sympy route was OOM-killed at m = 18 stage-1+2 and again
at m = 19 stage 1: expression trees for the univariate expansions).

Route: EVALUATION + INTERPOLATION, everything exact.
  E1  for integer nodes a0 = 0..B, run the ENTIRE committed pipeline
      (defect_numerator_b1 -> spectrum_b1, verbatim ring operations)
      over plain Python ints: the pipeline is a composition of ring
      operations and exact integer divisions, so evaluation at a = a0
      commutes with it. Every structural assert (c(r) = 0 for
      r = m..m+2, remainder 0, mu_nu = 1) is checked AT EVERY NODE.
  E2  B is the RIGOROUS coarse degree bound
      B = m*dim*(dim+1)/2 + (m+4)*m >= deg_a e_dim + deg_a h^m
      >= deg_a mu_j for every j (the peel is an integer-linear
      triangular solve in the N_r, so it cannot raise degree).
  E3  candidate mu_j by Newton interpolation over the first K+1
      nodes (K generous vs the observed degree law deg mu_0 = nu^2
      odd m / nu(nu+1) even m) mod 62-bit primes + CRT with
      symmetric lift, 3-stable;
  E4  PROOF: Horner-evaluate each candidate at ALL B+1 nodes and
      compare. Agreement at B+1 >= deg mu_j + 1 points of two
      polynomials of degree <= B is equality — no degree-law
      assumption survives into the result.
Output: matrix/m{m}_spectrum.json in the schema m18_sieve.py loads.
rh_established = false.
"""
import json
import sys
import time
from math import comb

sys.path.insert(0, 'matrix')
from m18_sieve import interp_mod, crt_pair, small_primes_62, peval


def say(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


def node_mus(m, a0):
    """The committed defect_numerator_b1 + spectrum_b1 pipeline
    evaluated at a = a0 over Z (verbatim operation-for-operation
    from m18_spectrum_only.py, with sympy expand as the identity)."""
    dim = m + 1
    top = m * (dim + 1) + 1
    q = [2, a0]
    for j in range(2, top + 1):
        q.append(a0 * q[-1] - q[-2])
    ps = []
    for j in range(1, dim + 1):
        s = 0
        i = 0
        while 2 * i < m:
            s += q[(m - 2 * i) * j]
            i += 1
        if m % 2 == 0:
            s += 1
        ps.append(s)
    e = [1]
    for k in range(1, dim + 1):
        s = 0
        for i in range(1, k + 1):
            s += (-1) ** (i - 1) * e[k - i] * ps[i - 1]
        assert s % k == 0, (m, a0, k)
        e.append(s // k)
    Q = [(-1) ** k * e[k] for k in range(dim + 1)]
    hh = [1, a0]
    for k in range(2, m + 5):
        hh.append(a0 * hh[-1] - hh[-2])
    hm = [hh[u] ** m for u in range(m + 3)]

    def c(r):
        s = 0
        for u in range(r + 1):
            if r - u <= dim:
                s += Q[r - u] * hm[u]
        return s

    N = [c(r) for r in range(m)]
    for r in range(m, m + 3):
        assert c(r) == 0, (m, a0, r)
    # spectrum peel (verbatim from disc_slice_m18.py at b = 1)
    eps = 1 if m % 2 == 0 else 0
    nu = (m - 1 - eps) // 2
    if eps:
        quo = [0] * (len(N) - 1)
        rem = list(N)
        for i in range(len(N) - 2, -1, -1):
            quo[i] = rem[i + 1]
            rem[i] = rem[i] - quo[i]
            rem[i + 1] = 0
        assert rem[0] == 0, (m, a0)
        N = quo
    mus = [0] * (nu + 1)
    work = list(N)
    for j in range(nu, -1, -1):
        mu = work[nu + j]
        mus[j] = mu
        for i in range(j + 1):
            work[nu + 2 * i - j] -= mu * comb(j, i)
    assert all(v == 0 for v in work), (m, a0)
    assert mus[nu] == 1, (m, a0)
    return mus, nu


def interp_exact(vals, K):
    """Exact integer polynomial of degree <= K through
    (0, vals[0])..(K, vals[K]) via modular Newton + CRT (3-stable),
    then trailing-zero trim. Caller must PROVE against all nodes."""
    primes = small_primes_62(200)
    res = mod = lift = None
    stable = 0
    for p in primes:
        c = interp_mod(vals[:K + 1], p)
        if res is None:
            res, mod = c, p
            lift = [v - mod if v > mod // 2 else v for v in res]
        else:
            res = [crt_pair(r, mod, cc, p)[0] for r, cc in zip(res, c)]
            mod *= p
            nl = [v - mod if v > mod // 2 else v for v in res]
            stable = stable + 1 if nl == lift else 0
            lift = nl
        if stable >= 3:
            break
    assert stable >= 3, "CRT did not stabilize; raise prime count"
    out = lift
    while out and out[-1] == 0:
        out.pop()
    return out


def main():
    m = int(sys.argv[1]) if len(sys.argv) > 1 else 19
    t0 = time.time()
    dim = m + 1
    B = m * dim * (dim + 1) // 2 + (m + 4) * m
    eps = 1 if m % 2 == 0 else 0
    nu = (m - 1 - eps) // 2
    K = (nu * nu if eps == 0 else nu * (nu + 1)) + 30  # generous
    say(f"m = {m}: rigorous node bound B = {B}, interp window K = {K}")
    say("E1: evaluating pipeline at all nodes ...")
    table = []
    for a0 in range(B + 1):
        mus, nu0 = node_mus(m, a0)
        assert nu0 == nu
        table.append(mus)
        if a0 % 500 == 0:
            say(f"  node {a0} ({time.time()-t0:.0f}s)")
    say(f"E1 done: {B+1} nodes, all structural asserts passed "
        f"({time.time()-t0:.0f}s)")
    say("E3: interpolating mu_j over first K+1 nodes ...")
    cands = {}
    for j in range(nu + 1):
        vals = [table[a0][j] for a0 in range(B + 1)]
        cand = interp_exact(vals, K)
        assert len(cand) - 1 <= K, f"mu_{j} degree exceeds window"
        cands[j] = (cand, vals)
    say(f"E3 done; degrees {[len(c)-1 for c, _ in cands.values()]}")
    say("E4 PROOF: exact evaluation of candidates at ALL nodes ...")
    for j, (cand, vals) in cands.items():
        for a0 in range(B + 1):
            if peval(cand, a0) != vals[a0]:
                raise RuntimeError(f"PROOF FAILED: mu_{j} at {a0}")
    say(f"E4 proof complete ({time.time()-t0:.0f}s)")
    out = {str(j): [str(c) for c in cand]
           for j, (cand, _) in cands.items()}
    json.dump({"m": m, "nu": nu, "coeffs_low_to_high": out,
               "method": "exact node evaluation (B+1 nodes, rigorous "
                         "degree bound) + modular interpolation + "
                         "exact re-evaluation proof at all nodes",
               "node_bound": B, "rh_established": False},
              open(f'matrix/m{m}_spectrum.json', 'w'))
    say(f"saved matrix/m{m}_spectrum.json ({time.time()-t0:.0f}s)")


if __name__ == "__main__":
    main()
