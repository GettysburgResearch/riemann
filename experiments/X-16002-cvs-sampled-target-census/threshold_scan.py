#!/usr/bin/env python3
"""
THE DECISIVE TEST: does the finite Connes-van Suijlekom (CvS) real-rootedness
criterion actually PASS at/above the predicted threshold N_0(alpha)=alpha^{-1}e^{1+1/alpha}?

Pipeline (every step after the Xi evaluation is EXACT over Q / Z):

  1. Xi(w) = xi_R(1/2+iw),  xi_R(s)=(1/2)s(s-1)pi^{-s/2}Gamma(s/2)zeta(s)   [mpmath, high dps]
  2. xi_j = (-1)^j Xi(2 pi alpha j),  j=-N..N, rounded to a COMMON absolute scale 10^{-D}
     with D chosen so the SMALLEST |xi_j| still carries >= SIGDIG significant digits.
     => xi_j * 10^D are exact integers; everything downstream is exact.
  3. P(s) = sum_j xi_j prod_{k!=j}(k-s)   built exactly in Z[s]  (degree 2N iff <eta|xi> != 0)
  4. #distinct real roots computed EXACTLY:
       - primary: sympy real-root isolation (Descartes/VCA) on the square-free part,
         returning exact rational isolating intervals  -> a reproducible certificate;
       - cross-check: exact Sturm sequence sign-variation count (dup_count_real_roots).
  PASS  <=>  #distinct real roots == deg P  (all roots real AND simple).

Usage: python3 threshold.py <mode>
"""
import sys, time, json, os
from fractions import Fraction
from mpmath import mp, mpc

SIGDIG = 100          # minimum significant digits retained by the slowest-decaying entry
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "threshold_out.txt")

_fh = None
def log(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    if _fh:
        _fh.write(s + "\n"); _fh.flush()

# ---------------------------------------------------------------- Xi ---------
_xicache = {}
def Xi(w, dps):
    """xi_R(1/2+iw), real for real w."""
    key = (str(w), dps)
    if key in _xicache: return _xicache[key]
    old = mp.dps
    mp.dps = dps
    s = mpc(mp.mpf(1)/2, w)
    v = mp.re(mp.mpf(1)/2 * s * (s-1) * mp.power(mp.pi, -s/2) * mp.gamma(s/2) * mp.zeta(s))
    mp.dps = old
    _xicache[key] = v
    return v

def xi_vector(alpha, N, sigdig=SIGDIG):
    """Return (list of ints xi_j*10^D for j=-N..N, D, dps, list of mpf raw values)."""
    # first pass at moderate precision to size the dynamic range
    mp.dps = 60
    a = mp.mpf(str(alpha))
    raw0 = [Xi(2*mp.pi*a*j, 60) for j in range(0, N+1)]
    mn = min(abs(v) for v in raw0 if v != 0)
    D = sigdig + int(mp.ceil(-mp.log10(mn))) + 2
    D = min(D, 900)
    dps = D + 60
    mp.dps = dps
    a = mp.mpf(str(alpha))
    vals = {}
    for j in range(0, N+1):
        vals[j] = Xi(2*mp.pi*a*j, dps)
    scale = mp.mpf(10)**D
    ints = {}
    for j in range(0, N+1):
        ints[j] = int(mp.nint(vals[j]*scale))
    out = []
    for j in range(-N, N+1):
        v = ints[abs(j)]
        out.append(v * (-1 if (j % 2) else 1))   # (-1)^j ; xi is even in j
    return out, D, dps, [vals[abs(j)] for j in range(-N, N+1)]

# ------------------------------------------------------- exact polynomial ----
def build_P(xis, N):
    """P(s) = sum_j xi_j prod_{k!=j}(k-s).  Coeff lists ASCENDING in s, ints."""
    idx = list(range(-N, N+1))
    m = len(idx)
    # prefix[i] = prod_{t<i}(idx[t]-s), suffix[i] = prod_{t>i}(idx[t]-s)
    def mul_linear(c, k):
        # multiply poly c (ascending) by (k - s)
        r = [0]*(len(c)+1)
        for i, ci in enumerate(c):
            if ci:
                r[i] += k*ci
                r[i+1] -= ci
        return r
    prefix = [[1]]
    for t in range(m):
        prefix.append(mul_linear(prefix[-1], idx[t]))
    suffix = [None]*(m+1)
    suffix[m] = [1]
    for t in range(m-1, -1, -1):
        suffix[t] = mul_linear(suffix[t+1], idx[t])
    P = [0]*(m)          # degree m-1 = 2N
    for t in range(m):
        A, B = prefix[t], suffix[t+1]
        # convolve A*B  (lengths t+1 and m-t)
        c = [0]*(len(A)+len(B)-1)
        for i, ai in enumerate(A):
            if ai:
                for jj, bj in enumerate(B):
                    if bj:
                        c[i+jj] += ai*bj
        x = xis[t]
        if x:
            for i, ci in enumerate(c):
                if ci:
                    P[i] += x*ci
    while len(P) > 1 and P[-1] == 0:
        P.pop()
    return P   # ascending

# ------------------------------------------------------- exact root count ----
from sympy import Poly, Symbol, ZZ
from sympy.polys.rings import ring
_s = Symbol('s')

def exact_real_root_data(Pasc, want_intervals=False, sturm_check=False):
    """Returns dict with degree, n_distinct_real, n_real_with_mult, intervals, sturm."""
    desc = list(reversed(Pasc))
    p = Poly(desc, _s, domain='ZZ')
    deg = p.degree()
    res = {'degree': deg}
    g = p.sqf_part()
    res['sqf_degree'] = g.degree()
    t0 = time.time()
    iv = g.intervals(sqf=True)
    res['n_distinct_real'] = len(iv)
    res['t_isolate'] = time.time()-t0
    if want_intervals:
        res['intervals'] = [(str(Fraction(int(a.p), int(a.q))), str(Fraction(int(b.p), int(b.q))))
                            for (a, b) in iv]
    if sturm_check:
        t0 = time.time()
        from sympy.polys.rootisolation import dup_count_real_roots
        from sympy.polys.densebasic import dup_strip
        f = [ZZ(int(c)) for c in g.all_coeffs()]
        # count over QQ (dup_count_real_roots needs a field for sturm)
        from sympy import QQ
        fq = [QQ(int(c)) for c in g.all_coeffs()]
        res['sturm_count'] = dup_count_real_roots(fq, QQ)
        res['t_sturm'] = time.time()-t0
    return res

def N0(alpha):
    import math
    return math.exp(1+1/alpha)/alpha

# ------------------------------------------------------------------ driver ---
def run_case(alpha, N, want_intervals=False, sturm_check=False, tag=""):
    t0 = time.time()
    xis, D, dps, raw = xi_vector(alpha, N)
    eta = sum(xis)
    P = build_P(xis, N)
    d = exact_real_root_data(P, want_intervals, sturm_check)
    deg = d['degree']
    nr = d['n_distinct_real']
    deficit = deg - nr
    verdict = "PASS" if deficit == 0 else "FAIL"
    mp.dps = 30
    log(f"alpha={alpha:<5} N={N:<3} D={D:<4} deg={deg:<4} #distinct_real={nr:<4} "
        f"deficit={deficit:<4} sqfdeg={d['sqf_degree']:<4} {verdict:<4} "
        f"N0={N0(alpha):.1f}  <eta|xi>*10^D={'%+d'%eta if abs(eta)<10**12 else ('%+.3e'%eta)}  "
        f"t={time.time()-t0:.1f}s {tag}")
    d.update(alpha=alpha, N=N, D=D, deficit=deficit, verdict=verdict,
             N0=N0(alpha), eta_int=str(eta), t=time.time()-t0)
    return d, P, xis

def main():
    global _fh
    mode = sys.argv[1] if len(sys.argv) > 1 else "grid"
    _fh = open(OUT, "a")
    log("="*110)
    log(f"### RUN mode={mode}  {time.strftime('%Y-%m-%d %H:%M:%S')}  SIGDIG={SIGDIG}")
    results = []
    if mode == "grid":
        grid = [(1.0, [6, 8, 10, 12, 14]),
                (0.9, [8, 10, 12, 14, 16]),
                (0.8, [10, 12, 14, 16, 18, 20]),
                (0.7, [14, 16, 18, 20, 22, 24]),
                (0.6, [20, 22, 24, 26, 28, 30])]
        for alpha, Ns in grid:
            for N in Ns:
                r, _, _ = run_case(alpha, N)
                results.append(r)
    elif mode == "big":
        for alpha, Ns in [(0.5, [34, 38, 40, 44])]:
            for N in Ns:
                r, _, _ = run_case(alpha, N)
                results.append(r)
    elif mode == "scan":
        alphas = [0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95,
                  1.00, 1.05, 1.10, 1.15, 1.20]
        for alpha in alphas:
            for N in [6, 8, 10, 12, 14, 16, 18, 20]:
                r, _, _ = run_case(alpha, N)
                results.append(r)
    elif mode == "custom":
        for spec in sys.argv[2:]:
            a, n = spec.split(",")
            r, _, _ = run_case(float(a), int(n))
            results.append(r)
    fn = os.path.join(os.path.dirname(OUT), f"results_{mode}.json")
    prev = []
    if os.path.exists(fn):
        prev = json.load(open(fn))
    json.dump(prev + [{k: v for k, v in r.items() if k != 'intervals'} for r in results],
              open(fn, "w"), indent=1)
    log(f"### wrote {fn}")

if __name__ == "__main__":
    main()
