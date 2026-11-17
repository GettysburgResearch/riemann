"""SKEPTIC independent re-implementation of C5 experiment E1 (fake curve zeta census).

Written from scratch (does not import ff_common).  Differences from the investigator's code:
  * P is built directly as prod-free expansion of sum_k c_k T^k (1+qT^2)^{g-k} via my own routine;
  * power sums from the reciprocal polynomial with my own Newton recursion;
  * admissibility tail certificate uses the per-root sum  sum_i (|alpha_i|/q)^d  (sharper than 2g r^d),
    so near-boundary cases with one dominant REAL root are decidable; Arb moduli from flint;
  * exact B_d are first screened for d <= 60, then up to the certificate degree D (cap 30000);
  * RH decided by: (#real roots of h, exact Sturm via sympy) and (#roots of k(u)=prod(u-x_i^2) in
    [0,4q], exact Sturm with multiplicities via sqf), i.e. a different route from flint isolation;
  * first indefinite Toeplitz size by float eigvalsh (non-rigorous, only compared with the report);
  * the g=1 boundary a=q+1 (Z=1) is decided exactly (all N_e=0).
Status of output: exact integers for admissibility up to D, Arb tail, exact Sturm for RH.
"""
import sys, os, math, json, time, hashlib, platform
import flint, sympy, numpy as np

flint.ctx.prec = 200


def P_of(c, q):
    """c = [1, c1, ..., cg] (h = x^g + c1 x^{g-1} + ... + cg). Return ascending coeffs of
    P(T) = sum_k c_k T^k (1+qT^2)^{g-k}."""
    g = len(c) - 1
    P = [0] * (2 * g + 1)
    for k, ck in enumerate(c):
        if ck == 0:
            continue
        m = g - k
        for j in range(m + 1):  # (1+qT^2)^m = sum_j binom(m,j) q^j T^{2j}
            P[k + 2 * j] += ck * math.comb(m, j) * q ** j
    return P


def psums(P, K):
    """s_1..s_K of reciprocal roots of P (P[0]=1)."""
    n = len(P) - 1
    s = [0] * (K + 1)
    s[0] = n
    for k in range(1, K + 1):
        v = -k * P[k] if k <= n else 0
        for j in range(1, min(k - 1, n) + 1):
            v -= P[j] * s[k - j]
        s[k] = v
    return s


_mu_cache = {}


def mu(n):
    if n in _mu_cache:
        return _mu_cache[n]
    r, m, p = 1, n, 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0:
                _mu_cache[n] = 0
                return 0
            r = -r
        p += 1
    if m > 1:
        r = -r
    _mu_cache[n] = r
    return r


def Bvals(P, q, D):
    s = psums(P, D)
    N = [0] + [q ** e + 1 - s[e] for e in range(1, D + 1)]
    B = [0]
    for d in range(1, D + 1):
        t = 0
        e = 1
        while e * e <= d:
            if d % e == 0:
                t += mu(d // e) * N[e]
                f = d // e
                if f != e:
                    t += mu(e) * N[f]
            e += 1
        assert t % d == 0
        B.append(t // d)
    return s, N, B


def moduli_upper(P):
    R = flint.fmpz_poly(list(reversed(P)))
    mods = []
    for z, m in R.complex_roots():
        mods += [abs(z).upper()] * m
    return mods  # arb upper endpoints (as arb)


def admissible(P, q, g, Dcap=30000):
    """Return ('yes', D) / ('no', d_neg) / ('undecided', info)."""
    if len(P) == 3 and P == [1, -(q + 1), q]:
        return ('yes_degenerate_Z_equals_1', 0)
    s, N, B = Bvals(P, q, 60)
    for d in range(1, 61):
        if B[d] < 0:
            return ('no', d)
    mods = moduli_upper(P)
    A = max(mods)
    qa = flint.arb(q)
    if not (A < qa):
        # if A>q some B_d<0 exists (Lemma C5-L1) -- search further
        s, N, B = Bvals(P, q, 3000)
        for d in range(1, 3001):
            if B[d] < 0:
                return ('no', d)
        return ('undecided', 'A>=q, no negative B_d up to 3000')
    # F(d) = 1 - sum_i (|a_i|/q)^d - q^{-d} - (d/2) q^{-d} (q^{d/2} + 1 + 2g A^{d/2})  > 0 implies B_d>0
    # monotone (increasing) for d >= Dm
    Af = float(A.upper())
    lnq = math.log(q)
    Dm = int(max(2 / lnq, 1 / math.log(q / math.sqrt(Af)), 1 / lnq) + 2)

    def F(d):
        da = flint.arb(d)
        tot = flint.arb(1)
        for m in mods:
            tot -= (m / qa) ** d
        tot -= qa ** (-da)
        tot -= da / 2 * qa ** (-da) * (qa ** (da / 2) + 1 + 2 * g * A ** (da / 2))
        return tot
    D = max(Dm, 2)
    # geometric search for D with F(D)>0
    while not (F(D) > 0):
        D = int(D * 1.3) + 1
        if D > Dcap:
            return ('undecided', 'tail cap')
    s, N, B = Bvals(P, q, D)
    for d in range(1, D + 1):
        if B[d] < 0:
            return ('no', d)
    return ('yes', D)


def rh_exact(c, q):
    x, u = sympy.symbols('x u')
    h = sympy.Poly(c, x, domain='ZZ')  # c descending
    g = h.degree()
    nreal = sum(m * f.count_roots() for f, m in h.sqf_list()[1])
    if nreal < g:
        return False, nreal
    # k(u) = prod (u - x_i^2):  h(x) h(-x) = (-1)^g k(x^2)
    hh = (h * h.compose(sympy.Poly(-x, x))).all_coeffs()  # descending, even poly
    kk = [hh[i] for i in range(0, len(hh), 2)]
    k = sympy.Poly(kk, u, domain='ZZ')
    inside = sum(m * f.count_roots(0, 4 * q) for f, m in k.sqf_list()[1])
    return inside == g, nreal


def first_hw_violation(P, q, g, K=3000):
    s = psums(P, K)
    for k in range(1, K + 1):
        if s[k] * s[k] > 4 * g * g * q ** k:
            return k
    return None


def first_indef_float(P, q, g, Nmax=12):
    s = psums(P, Nmax)
    t = [s[k] / q ** (k / 2) for k in range(Nmax + 1)]
    for N in range(2, Nmax + 1):
        T = np.array([[t[abs(i - j)] for j in range(N)] for i in range(N)])
        if np.linalg.eigvalsh(T)[0] < -1e-9:
            return N
    return None


def census(q, g):
    bnd = [math.comb(g, k) * (q + 1) ** k for k in range(g + 1)]
    out = dict(q=q, g=g, leaves=0, adm=0, rh_true=0, rh_false=0, nonreal=0, undecided=[],
               degenerate=[], maxk=0, maxN=0, fakes_sample=[], maxD=0)

    def rec(c):
        k = len(c) - 1
        if k == g:
            out['leaves'] += 1
            P = P_of(c, q)
            st, info = admissible(P, q, g)
            if st == 'no':
                return
            if st == 'undecided':
                out['undecided'].append((c, info))
                return
            if st.startswith('yes_degenerate'):
                out['degenerate'].append(c)
            out['adm'] += 1
            out['maxD'] = max(out['maxD'], info)
            rh, nreal = rh_exact(c, q)
            if rh:
                out['rh_true'] += 1
            else:
                out['rh_false'] += 1
                if nreal < g:
                    out['nonreal'] += 1
                kv = first_hw_violation(P, q, g)
                Nv = first_indef_float(P, q, g)
                out['maxk'] = max(out['maxk'], kv or 0)
                out['maxN'] = max(out['maxN'], Nv or 0)
                if len(out['fakes_sample']) < 5:
                    out['fakes_sample'].append(dict(c=c, P=P, k=kv, N=Nv))
            return
        for ck in range(-bnd[k + 1], bnd[k + 1] + 1):
            cc = c + [ck]
            Pp = P_of(cc + [0] * (g - k - 1), q)
            # B_1..B_{k+1} depend only on c_1..c_{k+1}
            s, N, B = Bvals(Pp, q, k + 1)
            if all(B[d] >= 0 for d in range(1, k + 2)):
                rec(cc)
    rec([1])
    return out


if __name__ == '__main__':
    cases = [(q, 1) for q in [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 25, 27, 32, 49]] + \
            [(q, 2) for q in [2, 3, 4, 5, 7, 8, 9]] + [(2, 3), (3, 3), (4, 3)]
    if len(sys.argv) > 1:
        sel = sys.argv[1]
        if sel == 'small':
            cases = [c for c in cases if c[1] <= 2] + [(2, 3), (3, 3)]
        elif sel == 'q4g3':
            cases = [(4, 3)]
    t0 = time.time()
    res = []
    for q, g in cases:
        t1 = time.time()
        r = census(q, g)
        r['runtime_s'] = round(time.time() - t1, 1)
        print(q, g, 'leaves', r['leaves'], 'adm', r['adm'], 'T', r['rh_true'], 'F', r['rh_false'],
              'nonreal', r['nonreal'], 'und', len(r['undecided']), 'degen', r['degenerate'],
              'maxk', r['maxk'], 'maxN', r['maxN'], 'maxD', r['maxD'], 't', r['runtime_s'], flush=True)
        res.append(r)
    meta = dict(python=platform.python_version(), flint=flint.__version__, sympy=sympy.__version__,
                numpy=np.__version__, runtime_s=round(time.time() - t0, 1), cases=cases)
    tag = sys.argv[1] if len(sys.argv) > 1 else 'all'
    OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'results',
                       'C5-function-field-transfer', 'skeptic_census_%s.json' % tag)
    with open(OUT, 'w') as f:
        json.dump(dict(meta=meta, results=res), f, indent=1, default=str)
    print('wrote', OUT, hashlib.sha256(open(OUT, 'rb').read()).hexdigest())
