"""SKEPTIC exact check of C5-T3 (inertia of T_N) -- independent of ff_inertia_check.py.

Method: T_N = (q^{-|m-n|/2} s_{|m-n|}) is congruent (D = diag(q^{m/2}), real invertible) to the INTEGER
matrix G_N = (q^{min(m,n)} s_{|m-n|}).  Sylvester: inertia(T_N) = inertia(G_N).  G_N symmetric => its
characteristic polynomial is real-rooted, so Descartes' rule of signs is EXACT:
  n_+ = sign changes of chi(x), n_- = sign changes of chi(-x), n_0 = order of vanishing at 0.
Everything is exact integer arithmetic (flint fmpz_mat.charpoly).  No floating point.

Tests:
  (A) every squarefree admissible P for (q,g) in {(3,2),(4,2),(5,2),(7,2),(2,3),(3,3)}:
      inertia(T_N) == (2g - n_out, n_out, N - 2g) for N = 2g, 2g+1, 2g+3   [report C5-T3]
  (B) non-squarefree P (all admissible ones in the same census plus synthetic FE polynomials with
      repeated roots, RH true and false): SKEPTIC confluent version
      inertia(T_N) == (r - m_out, m_out, N - r) for N >= r, with r = #distinct reciprocal roots,
      m_out = #distinct reciprocal roots with |beta| > 1.
"""
import sys, os, math, json, time, hashlib, itertools
import flint, sympy
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import skeptic_census_indep as S


def inertia_exact(P, q, N):
    s = S.psums(P, N)
    G = flint.fmpz_mat(N, N, [q ** min(m, n) * s[abs(m - n)] for m in range(N) for n in range(N)])
    cp = [int(c) for c in G.charpoly().coeffs()]  # ascending
    z = 0
    while cp[z] == 0:
        z += 1
    nz = cp[z:]

    def changes(seq):
        seq = [c for c in seq if c != 0]
        return sum(1 for a, b in zip(seq, seq[1:]) if (a > 0) != (b > 0))
    npos = changes(nz)
    nneg = changes([c * (-1) ** i for i, c in enumerate(nz)])
    assert npos + nneg + z == N
    return npos, nneg, z


def root_data(c, q):
    """c descending coeffs of h. Return (#distinct reciprocal roots r, #distinct with |beta|>1)
    exactly: distinct x-roots x_j (sqf part of h); each x gives alpha,q/alpha distinct unless
    x^2 = 4q (double alpha = +-sqrt q).  |beta|>1 for exactly one of the pair iff x non-real or x^2>4q."""
    x = sympy.symbols('x')
    h = sympy.Poly(c, x, domain='ZZ')
    r = 0
    mout = 0
    for f, m in h.sqf_list()[1]:
        d = f.degree()
        nreal = f.count_roots()
        # real roots with x^2 > 4q : via k(u) = f(sqrt u) f(-sqrt u)
        ff = (f * f.compose(sympy.Poly(-x, x))).all_coeffs()
        k = sympy.Poly([ff[i] for i in range(0, len(ff), 2)], x, domain='ZZ')
        # roots u of k in (4q, inf): real x with x^2>4q (k squarefree part counts distinct u;
        # distinct real x with same u=x^2 are +-x, both roots of f possibly -> count via f directly)
        big = f.count_roots(None, None) - f.count_roots(-sympy.Integer(4 * q), sympy.Integer(4 * q))
        # f.count_roots on [-4q,4q] is rational window; need [-2sqrt q, 2sqrt q]: refine with k
        n_out_real = sum(kf.count_roots(4 * q, None) - (1 if kf.eval(4 * q) == 0 else 0)
                         for kf, km in k.sqf_list()[1])
        # n_out_real counts distinct u = x^2 > 4q among roots of k; each such u comes from x or -x;
        # if both x and -x are roots of f they give the same u: count them separately
        cnt = 0
        for rt in sympy.Poly(f).real_roots():
            if rt ** 2 > 4 * q:
                cnt += 1
        n_out_real = cnt
        boundary = sum(1 for rt in sympy.Poly(f).real_roots() if rt ** 2 == 4 * q)
        nonreal = d - nreal
        r += 2 * d - boundary
        mout += n_out_real + nonreal
    return r, mout


def run():
    t0 = time.time()
    out = dict(squarefree=[], nonsquarefree=[], synthetic=[])
    for (q, g) in [(3, 2), (4, 2), (5, 2), (7, 2), (2, 3), (3, 3)]:
        C = []

        def rec(c):
            k = len(c) - 1
            bnd = [math.comb(g, j) * (q + 1) ** j for j in range(g + 1)]
            if k == g:
                P = S.P_of(c, q)
                st, info = S.admissible(P, q, g)
                if st.startswith('yes'):
                    C.append(c)
                return
            for ck in range(-bnd[k + 1], bnd[k + 1] + 1):
                cc = c + [ck]
                Pp = S.P_of(cc + [0] * (g - k - 1), q)
                s, N, B = S.Bvals(Pp, q, k + 1)
                if all(B[d] >= 0 for d in range(1, k + 2)):
                    rec(cc)
        rec([1])
        ok_sf = bad_sf = ok_nsf = bad_nsf = 0
        nsf_examples = []
        for c in C:
            P = S.P_of(c, q)
            Ppoly = sympy.Poly(list(reversed(P)), sympy.Symbol('T'))
            sqf = sympy.degree(sympy.gcd(Ppoly, Ppoly.diff())) == 0
            r, mout = root_data(c, q)
            for N in (2 * g, 2 * g + 1, 2 * g + 3):
                inn = inertia_exact(P, q, N)
                pred = (r - mout, mout, N - r)
                if sqf:
                    assert r == 2 * g
                    if inn == pred:
                        ok_sf += 1
                    else:
                        bad_sf += 1
                else:
                    if inn == pred:
                        ok_nsf += 1
                    else:
                        bad_nsf += 1
                    if len(nsf_examples) < 6 and N == 2 * g:
                        nsf_examples.append(dict(c=c, P=P, r=r, m_out=mout, inertia_T2g=inn))
        rec_ = dict(q=q, g=g, admissible=len(C), checks_sqf_ok=ok_sf, checks_sqf_bad=bad_sf,
                    checks_nonsqf_ok=ok_nsf, checks_nonsqf_bad=bad_nsf, nonsqf_examples=nsf_examples)
        print({k: v for k, v in rec_.items() if k != 'nonsqf_examples'}, flush=True)
        out['squarefree'].append(rec_)
    # synthetic non-squarefree FE polynomials (need not satisfy B_d>=0): h = prod of chosen factors
    syn = []
    x = sympy.symbols('x')
    for q in (3, 5, 7):
        facs = [x - 1, x + 2, x - (2 * q + 1) // 1, x ** 2 + 1, x ** 2 - 3 * x + 2 * q + 3]
        for combo in itertools.combinations_with_replacement(range(len(facs)), 3):
            hh = sympy.Poly(sympy.prod([facs[i] for i in combo]), x)
            c = [int(v) for v in hh.all_coeffs()]
            g = len(c) - 1
            if g > 5:
                continue
            P = S.P_of(c, q)
            r, mout = root_data(c, q)
            res = []
            for N in (r, r + 1, 2 * g, 2 * g + 2):
                if N < 1:
                    continue
                inn = inertia_exact(P, q, N)
                res.append((N, inn, (r - mout, mout, N - r), inn == (r - mout, mout, N - r)))
            rh = all(v == 0 for v in [mout])
            psd2g = inertia_exact(P, q, 2 * g)[1] == 0
            syn.append(dict(q=q, c=c, g=g, r=r, m_out=mout, rh=rh, T2g_psd=psd2g,
                            all_match=all(t[3] for t in res)))
    nmatch = sum(1 for s_ in syn if s_['all_match'])
    ncrit = sum(1 for s_ in syn if s_['rh'] == s_['T2g_psd'])
    print('synthetic FE polys:', len(syn), 'confluent inertia matches:', nmatch,
          'RH <=> T_2g>=0 holds:', ncrit, flush=True)
    out['synthetic'] = syn
    out['meta'] = dict(runtime_s=round(time.time() - t0, 1), flint=flint.__version__, sympy=sympy.__version__)
    fn = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'results',
                      'C5-function-field-transfer', 'skeptic_inertia_exact.json')
    with open(fn, 'w') as f:
        json.dump(out, f, indent=1, default=str)
    print('wrote', fn, hashlib.sha256(open(fn, 'rb').read()).hexdigest())


if __name__ == '__main__':
    run()
