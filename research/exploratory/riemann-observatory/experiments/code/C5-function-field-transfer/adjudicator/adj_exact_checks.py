"""C5-function-field-transfer, ADJUDICATOR exact checks (independent implementation).

Nothing here imports ff_common.py or the skeptic scripts. The investigator's census JSON is
read only as a list of input polynomials (data).

Checks:
  (1) the 41 g>=2 'undecided_cap' cases of the investigator census: exact B_d, d<=12;
  (2) the g=1 boundary a = +-(q+1);
  (3) worked examples (a) q=9,g=1; (b) q=3,g=3 (h=x^3-10x-7); (c) q=2,g=3:
      exact N_r, B_r, first Hasse-Weil violation, all-d positivity certificate, exact inertia of T_N;
  (4) confluent inertia theorem (skeptic 3.1): inertia(T_N) = (r-m, m, N-r) for N >= r,
      on synthetic FE polynomials with repeated roots, RH true and false;
  (5) first indefinite Toeplitz size for every fake listed in fake_census.json (exact),
      to count window-sharpness witnesses (first indefinite N = 2g).

Exactness: T_N is congruent to the integer matrix G_N = (q^min(m,n) s_|m-n|) via D=diag(q^(m/2)),
so inertia(T_N) = inertia(G_N). Inertia of G_N is read from its integer characteristic polynomial
by sympy's exact real-root counting (Sturm/Vincent-type isolation; not Descartes), and the sum
n_+ + n_- + n_0 = N is asserted (real-rootedness check). Root moduli use flint (Arb) balls with
exact fall-back. Status of outputs: exact integers / exact decisions (NUMERICAL-RIGOROUS).
"""
import json, math, sys, time, hashlib, platform
from fractions import Fraction
import sympy
import flint

flint.ctx.prec = 300
X = sympy.Symbol('x')
t0 = time.time()


# ------------------------------------------------------------------ basic objects
def P_of_h(h_asc, q):
    """P(T) = T^g h(1/T + qT) as ascending integer list; own implementation via sympy."""
    T = sympy.Symbol('T')
    g = len(h_asc) - 1
    expr = sum(c * T**(g - k) * (1 + q * T**2)**k for k, c in enumerate(h_asc))
    p = sympy.Poly(sympy.expand(expr), T)
    co = p.all_coeffs()[::-1]
    co += [0] * (2 * g + 1 - len(co))
    return [int(c) for c in co]


def check_FE(P, q):
    n = len(P) - 1
    g = n // 2
    # P(T) = q^g T^{2g} P(1/(qT))  <=>  P[2g-j] = q^{g-j} P[j]
    return all(P[n - j] * 1 == q**(g - j) * P[j] if j <= g else True for j in range(n + 1))


def psums(P, K):
    """s_k = sum alpha^k for P(T)=prod(1-alpha T); log-derivative recursion k p_k = -sum_{j<k} p_j s_{k-j}."""
    n = len(P) - 1
    s = [None] * (K + 1)
    s[0] = n
    for k in range(1, K + 1):
        acc = k * P[k] if k <= n else 0
        for j in range(1, min(k - 1, n) + 1):
            acc += P[j] * s[k - j]
        s[k] = -acc
    return s


def mu(n):
    r, m, p = 1, n, 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0:
                return 0
            r = -r
        p += 1
    return -r if m > 1 else r


def Ns_Bs(P, q, K):
    s = psums(P, K)
    N = [None] + [q**e + 1 - s[e] for e in range(1, K + 1)]
    B = [None]
    for d in range(1, K + 1):
        tot = sum(mu(d // e) * N[e] for e in range(1, d + 1) if d % e == 0)
        assert tot % d == 0
        B.append(tot // d)
    return s, N, B


def gram(s, q, N):
    return sympy.Matrix(N, N, lambda m, n: q**min(m, n) * s[abs(m - n)])


def inertia(M):
    """exact (n_+, n_-, n_0) of a real symmetric integer matrix via charpoly + exact real-root counting."""
    N = M.shape[0]
    cp = M.charpoly(X)
    p = sympy.Poly(cp.as_expr(), X)
    n0 = 0
    while p.eval(0) == 0:
        p = sympy.Poly(sympy.cancel(p.as_expr() / X), X)
        n0 += 1
    npos = p.count_roots(0, None)
    nneg = p.count_roots(None, 0)
    assert npos + nneg + n0 == N, (npos, nneg, n0, N)
    return (int(npos), int(nneg), int(n0))


def h_of_P(P, q):
    """inverse of P_of_h: monic integer h of degree g with P(T) = T^g h(1/T+qT) (linear solve, exact)."""
    g = (len(P) - 1) // 2
    cs = sympy.symbols('c0:%d' % g)
    T = sympy.Symbol('T')
    expr = sum(c * T**(g - k) * (1 + q * T**2)**k for k, c in enumerate(list(cs) + [1]))
    p = sympy.Poly(sympy.expand(expr), T)
    eqs = [sympy.Eq(p.coeff_monomial(T**j), P[j]) for j in range(g + 1)]
    sol = sympy.solve(eqs, cs, dict=True)[0]
    h = [int(sol[c]) for c in cs] + [1]
    assert P_of_h(h, q) == list(P)
    return h


def root_data(P, q):
    """r = #distinct reciprocal roots, m = #distinct with |alpha| > sqrt q.
    Exact classification through h (x = alpha + q/alpha): squarefree part of h, flint ball roots
    (real roots certified real), comparison x^2 vs 4q in balls with exact fallback for x^2 = 4q.
    Cross-checked against deg sqf_part(R), R(T) = T^n P(1/T). Also returns max|alpha| upper bound."""
    T = sympy.Symbol('T')
    R = sympy.Poly(list(P), T)  # coefficient list read as descending -> R(T) = T^n P(1/T)
    r_direct = sympy.degree(sympy.sqf_part(R), T)
    h = h_of_P(P, q)
    hs = sympy.Poly(sympy.sqf_part(sympy.Poly(h[::-1], X)), X)
    # exact factor x^2 - 4q (covers x = +-2 sqrt q, rational or not)
    edge = 0
    for cand in [sympy.Poly(X**2 - 4 * q, X)] + ([sympy.Poly(X - 2 * sympy.sqrt(q), X), sympy.Poly(X + 2 * sympy.sqrt(q), X)]
                                                if sympy.sqrt(q).is_Integer else []):
        pass
    sq = sympy.sqrt(4 * q)
    edge_roots = [e for e in (sq, -sq) if sympy.simplify(hs.as_expr().subs(X, e)) == 0]
    edge = len(edge_roots)
    hs_c = [int(c) for c in hs.all_coeffs()[::-1]]
    r = 0
    m = 0
    four_q = flint.arb(4 * q)
    for z, mult in flint.fmpz_poly(hs_c).complex_roots():
        assert mult == 1
        if z.imag == 0:
            x = z.real
            x2 = x * x
            if x2 < four_q:
                r += 2
            elif x2 > four_q:
                r += 2
                m += 1
            else:
                r += 1  # must be an exact edge root; verified by the count below
        else:
            r += 2
            m += 1
    amb = r - 2 * (r // 2)
    assert r == r_direct, (r, r_direct, P, h)
    co = [int(c) for c in sympy.Poly(sympy.sqf_part(R), T).all_coeffs()[::-1]]
    amax = max(float(abs(z).upper()) for z, _ in flint.fmpz_poly(co).complex_roots())
    return r, m, amax


def first_HW_violation(s, q, g, K):
    for k in range(1, K + 1):
        if s[k] * s[k] > 4 * g * g * q**k:
            return k
    return None


def alld_certificate(P, q, g, A_up, Dmax=400):
    """B_d >= 0 for all d: exact for d < D0; for d >= D0, d B_d >= q^d (1 - eps(d)) with
    eps(d) = 2g (A/q)^d + (d/2)(q^{-d/2} + q^{-d} + 2g (sqrt(A)/q)^d), each term nonincreasing for
    d >= D0 >= max(1/ln(q^{1/2}), 1/ln(q/sqrt A)) (d x^d is nonincreasing for d >= 1/ln(1/x)).
    Uses exact rational upper bound for A (A_up rounded up)."""
    A = Fraction(A_up).limit_denominator(10**6)
    if A < A_up:
        A += Fraction(1, 10**6)
    assert A < q
    sqrtA = Fraction(math.sqrt(float(A)) * (1 + 1e-12)).limit_denominator(10**6) + Fraction(1, 10**6)
    assert sqrtA * sqrtA >= A
    dmono = max(1 / math.log(math.sqrt(q)), 1 / math.log(q / float(sqrtA))) + 1
    def eps(d):
        qinvhalf = Fraction(1, math.isqrt(q**d))  # >= q^{-d/2} (exact for even d)
        return 2 * g * (A / q)**d + Fraction(d, 2) * (qinvhalf + Fraction(1, q**d) + 2 * g * (sqrtA / q)**d)
    D0 = None
    for d in range(max(2, math.ceil(dmono)), Dmax):
        if eps(d) < 1:
            D0 = d
            break
    assert D0 is not None
    s, N, B = Ns_Bs(P, q, D0)
    ok = all(B[d] >= 0 for d in range(1, D0 + 1))
    return ok, D0, (min(B[1:]) if B[1:] else None)


# NOTE on eps(): for odd d, q^{-d/2} is replaced by 1/isqrt(q^d) >= q^{-d/2} (an upper bound), so eps is an upper bound.

out = {'meta': {'script': 'adj_exact_checks.py', 'python': platform.python_version(),
                'sympy': sympy.__version__, 'flint': flint.__version__, 'arb_prec_bits': 300}}

# ------------------------------------------------------------------ (1) investigator undecided cases
cen = json.load(open(sys.argv[1]))
und = []
for row in cen['results']:
    if row['g'] >= 2:
        for u in row.get('undecided_list', []):
            h = u['h_asc']
            q, g = row['q'], row['g']
            P = P_of_h(h, q)
            assert check_FE(P, q)
            s, N, B = Ns_Bs(P, q, 12)
            fn = next((d for d in range(1, 13) if B[d] < 0), None)
            und.append({'q': q, 'g': g, 'h_asc': h, 'first_negative_B_d': fn, 'B_1_12': B[1:]})
out['undecided_g_ge_2'] = {'count': len(und),
                           'all_nonadmissible_by_d12': all(u['first_negative_B_d'] is not None for u in und),
                           'max_first_negative_d': max(u['first_negative_B_d'] or 99 for u in und),
                           'hist_first_negative_d': {str(k): sum(1 for u in und if u['first_negative_B_d'] == k)
                                                     for k in sorted(set(u['first_negative_B_d'] for u in und))},
                           'cases': und}
print('(1) undecided g>=2:', len(und), 'all non-admissible:', out['undecided_g_ge_2']['all_nonadmissible_by_d12'],
      out['undecided_g_ge_2']['hist_first_negative_d'])

# ------------------------------------------------------------------ (2) g=1 boundary
bd = []
for q in [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 25, 27, 32, 49]:
    for a in (q + 1, -(q + 1)):
        P = [1, -a, q]
        s, N, B = Ns_Bs(P, q, 24)
        bd.append({'q': q, 'a': a, 'N_1_6': N[1:7], 'B_1_6': B[1:7], 'min_B_d_le_24': min(B[1:]),
                   'Z_identically_1': all(n == 0 for n in N[1:])})
out['g1_boundary'] = bd
print('(2) g=1 a=q+1: Z==1 for all q:', all(x['Z_identically_1'] for x in bd if x['a'] > 0),
      '; a=-(q+1): min B_d<0 for all q:', all(x['min_B_d_le_24'] < 0 for x in bd if x['a'] < 0))

# ------------------------------------------------------------------ (3) worked examples
ex = {}
for name, q, g, h, Pgiven in [('a_q9_g1', 9, 1, [-7, 1], [1, -7, 9]),
                              ('b_q3_g3', 3, 3, [-7, -10, 0, 1], [1, 0, -1, -7, -3, 0, 27]),
                              ('c_q2_g3', 2, 3, None, [1, -3, 4, -5, 8, -12, 8])]:
    P = P_of_h(h, q) if h else Pgiven
    assert P == Pgiven, (name, P)
    assert check_FE(P, q)
    s, N, B = Ns_Bs(P, q, 40)
    r, m, amax = root_data(P, q)
    s200 = psums(P, 200)
    hw = first_HW_violation(s200, q, g, 200)
    cert = alld_certificate(P, q, g, amax)
    inert = {str(n): inertia(gram(s200, q, n)) for n in range(1, 2 * g + 3)}
    first_indef = next((n for n in range(1, 2 * g + 3) if inert[str(n)][1] > 0), None)
    ex[name] = {'q': q, 'g': g, 'P_asc': P, 'N_1_6': N[1:7], 'B_1_6': B[1:7], 'r_distinct': r, 'm_outside': m,
                'max_abs_alpha_over_sqrtq_upper': amax / math.sqrt(q), 'first_HW_violation_k': hw,
                'alld_positivity_certified': cert[0], 'D0': cert[1], 'inertia_T_N': inert,
                'first_indefinite_N': first_indef,
                'confluent_formula_holds_N_ge_r': all(inert[str(n)] == (r - m, m, n - r) for n in range(r, 2 * g + 3))}
    print('(3)', name, ex[name]['N_1_6'], ex[name]['B_1_6'], 'HW viol k=', hw, 'alld', cert, 'first indef N', first_indef,
          'inertia', inert)
out['examples'] = ex

# ------------------------------------------------------------------ (4) confluent inertia, synthetic
def quad(a, q):
    return [1, -a, q]


def quart(b, c, q):
    # T^2 h(1/T+qT), h = x^2 - b x + c
    return P_of_h([c, -b, 1], q)


def pmul(a, b):
    o = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            o[i + j] += x * y
    return o


syn = []
import itertools, random
random.seed(20261117)
for q in [2, 3, 4, 5, 9]:
    rq = math.isqrt(q)
    circ = [a for a in range(-2 * rq - 1, 2 * rq + 2) if a * a < 4 * q]
    offr = [a for a in range(-(q + 3), q + 4) if a * a > 4 * q]
    edge = [2 * rq, -2 * rq] if rq * rq == q else []
    cplx = [(b, c) for b in range(-3, 4) for c in range(-3, 8) if b * b < 4 * c][:12]
    pool = ([('c', quad(a, q)) for a in circ] + [('o', quad(a, q)) for a in offr] +
            [('e', quad(a, q)) for a in edge] + [('x', quart(b, c, q)) for b, c in cplx])
    for trial in range(40):
        k = random.randint(1, 3)
        facs = [random.choice(pool) for _ in range(k)]
        # force a repeated factor in half the trials
        if trial % 2 == 0:
            facs.append(random.choice(facs))
        P = [1]
        for _, f in facs:
            P = pmul(P, f)
        if len(P) - 1 > 12:
            continue
        g = (len(P) - 1) // 2
        assert check_FE(P, q)
        r, m, _ = root_data(P, q)
        s = psums(P, 2 * g + 4)
        res = {}
        ok = True
        for n in sorted(set([r, r + 1, 2 * g, 2 * g + 2])):
            if n < 1:
                continue
            inn = inertia(gram(s, q, n))
            res[str(n)] = inn
            if inn != (r - m, m, n - r):
                ok = False
        rh = (m == 0)
        T2g = res[str(2 * g)]
        syn.append({'q': q, 'g': g, 'factors': [t for t, _ in facs], 'P_asc': P, 'r': r, 'm': m, 'RH': rh,
                    'inertia': res, 'formula_ok': ok, 'RH_iff_T2g_psd': (rh == (T2g[1] == 0)),
                    'squarefree': r == 2 * g})
nf = sum(1 for x in syn if not x['formula_ok'])
out['confluent_synthetic'] = {'count': len(syn), 'non_squarefree': sum(1 for x in syn if not x['squarefree']),
                              'RH_false': sum(1 for x in syn if not x['RH']), 'formula_failures': nf,
                              'RH_iff_T2g_psd_failures': sum(1 for x in syn if not x['RH_iff_T2g_psd']),
                              'cases': syn}
print('(4) confluent synthetic:', len(syn), 'cases;', out['confluent_synthetic']['non_squarefree'], 'non-squarefree;',
      out['confluent_synthetic']['RH_false'], 'RH-false; formula failures', nf)

# ------------------------------------------------------------------ (5) first indefinite N for listed fakes
fi = {}
for row in cen['results']:
    q, g = row['q'], row['g']
    cnt = {}
    nlisted = 0
    for f in row['fakes']:
        P = f['P_asc']
        s = psums(P, 2 * g + 1)
        fN = None
        for n in range(1, 2 * g + 1):
            if inertia(gram(s, q, n))[1] > 0:
                fN = n
                break
        assert fN is not None  # RH-false => T_2g indefinite (C5-T3 / skeptic 3.1)
        if 'first_indefinite_toeplitz_N' in f:
            assert f['first_indefinite_toeplitz_N'] == fN, (q, g, f, fN)
        cnt[fN] = cnt.get(fN, 0) + 1
        nlisted += 1
    fi[f'{q},{g}'] = {'listed_fakes': nlisted, 'truncated_from': row.get('fakes_truncated_from'),
                      'hist_first_indefinite_N': {str(k): v for k, v in sorted(cnt.items())},
                      'sharpness_witnesses_N_eq_2g': cnt.get(2 * g, 0)}
out['first_indefinite_listed_fakes'] = fi
print('(5) first indefinite N (listed fakes):', {k: v['hist_first_indefinite_N'] for k, v in fi.items() if v['listed_fakes']})

out['meta']['runtime_s'] = round(time.time() - t0, 1)
path = sys.argv[2]
with open(path, 'w') as fh:
    json.dump(out, fh, indent=1, default=str)
print('runtime', out['meta']['runtime_s'], 's ->', path, hashlib.sha256(open(path, 'rb').read()).hexdigest())
