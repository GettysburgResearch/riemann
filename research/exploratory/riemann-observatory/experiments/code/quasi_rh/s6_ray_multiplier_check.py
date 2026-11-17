# s6_ray_multiplier_check.py -- arithmetic end-to-end check of App. A.2 of paper2.tex
# (l.3003-3282): reduced denominators, the matrices g, H, g_1, the Kubota multiplier
# kappa(g_1) = (c_1/a_1)_3 [DR (5.4), confirmed numerically in s6_theta_automorphy.py],
# the three-case formula (eq:ray-multiplier), the decomposition kappa = kappa_0 (a/r)_3 with
# kappa_0 fixed by (h_0, active set, r mod M^2), the additive CRT (eq:ray-additive-crt), and the
# summed local identity
#   sum_{h_p != 0} prod_p C_{p,j_p}(h_p) * conj(kappa(g_1(h))) * ebreve(-delta'(h) l / c)
#      = conj(kappa_0) psi(lam^4 l) prod_p chi_p(sigma_p)^{-2} omega_{p,j_p} B_{p,j_p}(lam^4 l)
# for l in lambda^{-4} O.  Independent code; nothing from the OpenAI repository.
import sys, os, math, cmath, random, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s6_zw import *

Z6 = cmath.exp(2j * math.pi / 6)
LAMC = cv(LAM)

def sextic_exp(x, p):
    if divides(p, x): return None
    q = norm(p); r = powmod(x, (q - 1) // 6, p)
    for k in range(6):
        if divides(p, sub(r, power((1, 1), k))): return k      # zeta6 = 1+omega
    raise ValueError
def chi(x, p, j=1):
    """chi_p(x)^j with zero extension (chi_p^0(x) = 1_{p not | x})."""
    k = sextic_exp(x, p)
    if k is None: return 0.0
    return Z6 ** ((k * j) % 6)
def gam(p, j):
    return sum(chi(x, p, j) * e_add(cv(x) / cv(p)) for x in residues(p)) / math.sqrt(norm(p))
def Cpj(p, j, h):
    return sum(chi(y, p, j) * e_add(-cv(h) * cv(y) / cv(p)) for y in residues(p)) / norm(p)
def B(p, j, x):
    q = norm(p)
    if j == 4: return q ** -0.5 * (-1 + q * (1 if divides(p, x) else 0))
    if j == 0: return q ** -0.5 * chi(x, p, -2)
    return chi(x, p, -j - 2)
def omega_pj(p, j, eps):
    if j == 4: return gam(p, 4)
    if j == 0: return -gam(p, 2) * chi(eps, p, -2)
    return chi((-1, 0), p, j) * gam(p, j) * gam(p, (j + 2) % 6) * chi(eps, p, -j - 2)

def vq(q, x):
    k = 0
    while divides(q, x): x = exact_div(x, q); k += 1
    return k
def crt2(r1, m1, r2, m2):
    # x = r1 mod m1, x = r2 mod m2, (m1,m2)=1
    g, s, t = egcd(m1, m2); assert norm(g) == 1
    gi = conj(g)
    s = mul(s, gi); t = mul(t, gi)          # s m1 + t m2 = 1
    x = add(mul(mul(r1, t), m2), mul(mul(r2, s), m1))
    return rmod(x, mul(m1, m2))
def gcd(x, y):
    g, _, _ = egcd(x, y); return g
def cub(x, y):
    """(x/y)_3 exponent; (x/unit)=0."""
    if norm(y) == 1: return 0
    return cubic_jacobi(x, y)

def unit_to_primary(x):
    for u in UNITS:
        if is_primary(mul(u, x)): return u
    return None

def build(L, h0, primes, hps):
    """Return dict with a,c,c0,r,delta',b_g,H,g1,case,u0,sigma for the translate h=(h0,(h_p))."""
    M = mul(power(LAM, 12), power(L, 4)); M2 = mul(M, M)
    r = ONE
    for p in primes: r = mul(r, p)
    # representatives h_p' = h_p mod p, = 0 mod M^2
    hp_rep = [crt2(rmod(h, p), p, (0, 0), M2) for p, h in zip(primes, hps)]
    den = mul(L, r)
    num = mul(h0, r)
    for p, h in zip(primes, hp_rep):
        num = add(num, mul(L, mul(h, exact_div(r, p))))
    num = mul(power(LAM, 2), num)
    g = gcd(num, den)
    a = exact_div(num, g); c = exact_div(den, g)
    if divides(LAM, c):
        u = unit_to_primary(a); a = mul(u, a); c = mul(u, c)
    else:
        u = unit_to_primary(c); a = mul(u, a); c = mul(u, c)
    # c0: reduced denominator of lam^2 h0/L, normalised so that c = c0 * r exactly
    c0 = exact_div(c, r)
    # check c0 is (up to unit) the reduced denominator of lam^2 h0 / L
    n0 = mul(power(LAM, 2), h0); g0 = gcd(n0, L); c0ref = exact_div(L, g0)
    assert norm(c0) == norm(c0ref) and divides(c0, c0ref) and divides(c0ref, c0)
    # delta' by CRT
    Mc0 = mul(M, c0)
    m1 = ONE; m2 = ONE
    for q in (LAM, make_primary((-2, 0)) if False else (-2, 0)):
        pass
    qs = []
    for p_, _e in sympy.factorint(norm(M)).items():
        qs += list(primes_over(p_))
    qs = sorted(set(qs))
    for q in qs:
        if divides(q, c0): m1 = mul(m1, power(q, vq(q, Mc0)))
        else: m2 = mul(m2, power(q, vq(q, M)))
    ainv = inv_mod(a, mul(m1, r))
    dp = crt2(ainv, mul(m1, r), (0, 0), m2)
    bg = exact_div(sub(mul(a, dp), ONE), c)
    # congruence claims for b_g (l.3066-3074)
    for q in qs:
        e = vq(q, M)
        if divides(q, c0):
            assert divides(power(q, e), bg), "b_g != 0 mod q^v_q(M)"
        else:
            assert divides(power(q, e), add(mul(bg, c), ONE)), "b_g != -c^{-1} mod q^v_q(M)"
    # cusp choice
    if divides((3, 0), c):
        case = 1; H = ((1, 0), (0, 0), (0, 0), (1, 0)); u0 = None
    elif vq(LAM, c) == 1:
        case = 2
        u0 = LAM if divides((3, 0), sub(c, LAM)) else neg(LAM)
        assert divides((3, 0), sub(c, u0))
        H = (ONE, (0, 0), u0, ONE)
    else:
        case = 3
        reps = [(x, y) for x in range(3) for y in range(3)]
        u0 = [t for t in reps if divides((3, 0), sub(a, t))][0]
        H = (u0, (-1, 0), ONE, (0, 0))
    # g1 = g H^{-1};  H^{-1} = (d -b; -c a)
    Ha, Hb, Hc, Hd = H
    Hi = (Hd, neg(Hb), neg(Hc), Ha)
    G = (a, bg, c, dp)
    def mm(X, Y):
        return (add(mul(X[0], Y[0]), mul(X[1], Y[2])), add(mul(X[0], Y[1]), mul(X[1], Y[3])),
                add(mul(X[2], Y[0]), mul(X[3], Y[2])), add(mul(X[2], Y[1]), mul(X[3], Y[3])))
    g1 = mm(G, Hi)
    a1, b1, c1, d1 = g1
    assert divides((3, 0), sub(a1, ONE)) and divides((3, 0), b1) and divides((3, 0), c1) and divides((3, 0), sub(d1, ONE)), "g1 != I mod 3"
    assert sub(mul(a1, d1), mul(b1, c1)) == ONE
    kap = 0 if is_zero(c1) else cub(c1, a1)
    # sigma: which cusp expansion
    if case == 1: sigma = '0'
    elif case == 2: sigma = '-' if u0 == LAM else '+'
    else:
        # u0 mod Z+3O: class of the omega-coefficient mod 3
        k = u0[1] % 3
        sigma = {0: '0', 1: '-', 2: '+'}[k]
    return dict(a=a, c=c, c0=c0, r=r, dp=dp, bg=bg, case=case, u0=u0, kappa=kap, g1=g1, sigma=sigma, M=M)

def claimed_kappa(d):
    a, c0, r, bg, u0 = d['a'], d['c0'], d['r'], d['bg'], d['u0']
    ar = cub(a, r)
    if d['case'] == 1:
        return (cub(c0, a) + ar) % 3
    if d['case'] == 2:
        a1 = sub(a, mul(u0, bg))
        t1 = cub(neg(u0), a1)
        t2 = cub(exact_div(c0, u0), a)
        return (t1 + t2 + ar) % 3
    return (cub(a, c0) + ar) % 3

def run(L, h0, primes, js, nsamp_l=12, seed=0, exhaustive=True):
    rnd = random.Random(seed)
    allh = [[x for x in residues(p) if not is_zero(x)] for p in primes]
    tuples = list(itertools.product(*allh)) if exhaustive else [tuple(rnd.choice(x) for x in allh) for _ in range(30)]
    res = []
    for hps in tuples:
        d = build(L, h0, primes, list(hps))
        ck = claimed_kappa(d)
        assert ck == d['kappa'], ("multiplier formula mismatch", d['case'], ck, d['kappa'])
        kap0 = (d['kappa'] - cub(d['a'], d['r'])) % 3
        res.append((hps, d, kap0))
    # kappa_0, sigma, delta'_0 must not depend on h_p
    k0s = set(x[2] for x in res); sig = set(x[1]['sigma'] for x in res)
    c = res[0][1]['c']; c0 = res[0][1]['c0']; r = res[0][1]['r']
    D0 = mul(power(LAM, 3), c0)
    dp0s = set(rmod(x[1]['dp'], D0) for x in res)
    assert len(k0s) == 1 and len(sig) == 1 and len(dp0s) == 1, (k0s, sig, dp0s)
    kap0 = k0s.pop(); dp0 = dp0s.pop()
    # additive CRT and summed local identity
    rinv = inv_mod(r, D0) if norm(D0) > 1 else ONE
    sig_p = {}; eps_p = {}
    for p in primes:
        s = rmod(mul(power(LAM, 2), exact_div(c, p)), p)
        t = rmod(mul(power(LAM, 3), exact_div(c, p)), p)
        sig_p[p] = s; eps_p[p] = rmod(neg(inv_mod(mul(t, s), p)), p)
    maxerr_crt = 0; maxerr_sum = 0
    lam4 = cv(LAM) ** 4
    for _ in range(nsamp_l):
        x = (rnd.randint(-40, 40), rnd.randint(-40, 40))      # x = lam^4 l
        l = cv(x) / lam4
        psi = e_add(-cv(rmod(mul(mul(dp0, rinv), x), D0)) / cv(D0))
        lhs = 0j
        for hps, d, k0 in res:
            dpr = rmod(d['dp'], mul(power(LAM, 3), c))      # exact reduction: ebreve(-delta' l/c) depends on delta' mod lam^3 c
            ph = ebreve(-cv(dpr) * l / cv(c))
            rhs_crt = psi
            for p, h in zip(primes, hps):
                rhs_crt *= e_add(cv(mul(mul(eps_p[p], inv_mod(h, p)), x)) / cv(p))
            maxerr_crt = max(maxerr_crt, abs(ph - rhs_crt))
            w = 1.0
            for p, h, j in zip(primes, hps, js): w *= Cpj(p, j, h)
            lhs += w * np.conj(omega_pow(d['kappa'])) * ph
        rhs = np.conj(omega_pow(kap0)) * psi
        for p, j in zip(primes, js):
            rhs *= chi(sig_p[p], p, -2) * omega_pj(p, j, eps_p[p]) * B(p, j, x)
        maxerr_sum = max(maxerr_sum, abs(lhs - rhs))
    return dict(n=len(res), case=res[0][1]['case'], sigma=res[0][1]['sigma'], kappa0=kap0,
                err_crt=maxerr_crt, err_sum=maxerr_sum, r=r, c0=c0)

import numpy as np
if __name__ == "__main__":
    L = mul(power(LAM, 5), (-8, 0))
    p7 = primes_over(7)[0]; p13 = primes_over(13)[0]; p19 = primes_over(19)[1]; p5 = primes_over(5)[0]
    tests = []
    # h0 choices giving v_lam(c0) >= 2 (case 1), = 1 (case 2), = 0 (case 3, c0 coprime to lambda)
    h0s = {'v=3': (1, 1), 'v=2': mul(LAM, (2, 0)), 'v=1': mul(power(LAM, 2), (2, 0)), 'v=1b': mul(power(LAM, 2), (-2, 3)),
           'v=0,c0=1': mul(power(LAM, 5), (1, -1)), 'v=0,c0~8': mul(power(LAM, 5), (-2, 1)), 'v=0,c0~4': mul(power(LAM, 5), (-4, 1)),
           'h0=0': (0, 0)}
    for name, h0 in h0s.items():
        for primes, js in [([p7], [1]), ([p7], [0]), ([p7], [4]), ([p7], [2]), ([p13], [3]), ([p13], [5]),
                           ([p7, p13], [1, 1]), ([p7, p13], [1, 4]), ([p5], [1]), ([p7, p19], [0, 1])]:
            out = run(L, h0, primes, js, exhaustive=(len(primes) == 1 or norm(primes[0]) * norm(primes[1]) < 200))
            print("h0 %-9s primes N=%s j=%s : %3d translates, case %d, cusp %s, kappa0=w^%d | CRT err %.1e | summed-identity err %.1e"
                  % (name, [norm(p) for p in primes], js, out['n'], out['case'], out['sigma'], out['kappa0'], out['err_crt'], out['err_sum']))
