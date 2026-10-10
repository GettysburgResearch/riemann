"""R3 review checks for OpenAI QRH (Oct 5 2026) Section sec:reflection / App. app:fixed-ray.

Status: EXPLORATORY review script.  Labels: EXACT = sextic/cubic symbols as integer exponents,
FLOAT = ordinary double precision (not directed, not certified).

Checks
  A  Kubota theta from Dunn-Radziwill (5.6)-(5.8): theta(E w) = theta(w), theta(w+1) = theta(w),
     and theta(g w) = (c/a)_3 theta(w) for g in Gamma_1(3) (discriminates (c/a)_3 from its conjugate).
  B  Cusp expansions: theta(gamma_10 w) = sum t_+(l)..., theta(gamma_19 w) = sum t_-(l)... with
     t_+(l) = omega tau_2(omega l) e(l), t_-(l) = omega^2 tau_1(omega^2 l) e(l)  (paper2 eq:cusp-fourier-coefficients,
     DR (5.13), (5.14), Appendix table rows 10, 19).
  C  paper2 eq:ray-fourier and eq:ray-local-transform for j = 0..5 (EXACT symbols, float sums).
  D  paper2 eq:ray-multiplier: kappa(g_1) = (c_1/a_1)_3 versus the claimed three-case formula (EXACT),
     built with the paper's congruences for delta' (M = lambda^12).
  E  End-to-end translate identity paper2 eq:theta-cusp-automorphy:
     theta(a/c, v) = kappa(g_1) * [cusp-sigma expansion](g^{-1}(a/c, v))   (FLOAT).

Conventions follow paper2 / DR: O = Z[omega], primary = 1 mod 3, lambda = 1+2 omega,
  e-check(z) = exp(2 pi i (z + conj z)),  e(z) = e-check(z/lambda) = exp(4 pi i Im z/sqrt 3),
  chi_p(x) = (x/p)_6 == x^{(Np-1)/6} mod p, (x/p)_3 = chi_p(x)^2.
Usage: python3 -I oct5_r3_theta_checks.py OUT.json
"""
import sys, os, math, cmath, json, time, random

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'a2'))
import eis  # repository module (read before use)
from eis import mul, conj, norm, is_primary, primary, divides, reduce_mod, powmod, sym_prime, e_of, UNITS
import numpy as np
from scipy.special import kv

OM = complex(-0.5, math.sqrt(3) / 2)
LAM = (1, 2)                      # 1 + 2 omega = sqrt(-3)
ONE = (1, 0)
W1 = (0, 1)                       # omega
W2 = (-1, -1)                     # omega^2
SIGMA0 = 3 ** 2.5 / 2


def toc(x):
    return x[0] + x[1] * OM


def add(x, y): return (x[0] + y[0], x[1] + y[1])
def sub(x, y): return (x[0] - y[0], x[1] - y[1])
def neg(x): return (-x[0], -x[1])


def exact_div(x, m):
    c, d = mul(x, conj(m)); n = norm(m)
    assert c % n == 0 and d % n == 0, (x, m)
    return (c // n, d // n)


def pw(x, k):
    r = ONE
    for _ in range(k):
        r = mul(r, x)
    return r


def echeck_frac(y, p):
    """e-check(y/p) = exp(2 pi i (2 Re(y/p)))."""
    c, d = mul(y, conj(p)); N = norm(p)
    return cmath.exp(2j * math.pi * ((2 * c - d) % (2 * N)) / N)


# ---------------------------------------------------------------- primes, factorisation
def primary_primes(N):
    isp = bytearray([1]) * (N + 1); isp[0] = isp[1] = 0
    for i in range(2, int(N ** 0.5) + 1):
        if isp[i]:
            isp[i * i::i] = bytearray(len(isp[i * i::i]))
    out = [primary((2, 0))] if N >= 4 else []      # inert prime 2 (norm 4)
    for p in range(5, N + 1):
        if not isp[p]:
            continue
        if p % 3 == 1:
            y = 1
            while 3 * y * y <= 4 * p:
                dd = 4 * p - 3 * y * y; s = math.isqrt(dd)
                if s * s == dd and (y + s) % 2 == 0:
                    x = (y + s) // 2
                    assert x * x - x * y + y * y == p
                    out += [primary((x, y)), primary(conj((x, y)))]
                    break
                y += 1
        elif p % 3 == 2 and p * p <= N:
            out.append(primary((p, 0)))
    out = sorted(set(out), key=norm)
    return out


PRIMES = primary_primes(60000)


def _prime_above(q):
    """a primary prime pi with N(pi) = q for a rational prime q = 1 mod 3."""
    from sympy.ntheory import sqrt_mod
    s = sqrt_mod((-3) % q, q)
    w0 = ((-1 + s) * pow(2, -1, q)) % q
    g = egcd((q, 0), (-w0, 1))[0]
    assert norm(g) == q
    return primary(g)


def factor(x):
    """x = unit * lambda^e * prod p^k (p primary primes)."""
    assert x != (0, 0)
    e = 0
    while divides(LAM, x):
        x = exact_div(x, LAM); e += 1
    fac = {}
    if norm(x) <= 10 ** 6:
        for p in PRIMES:
            if norm(p) * norm(p) > norm(x):
                break
            while divides(p, x):
                x = exact_div(x, p); fac[p] = fac.get(p, 0) + 1
        if norm(x) > 1:
            q = primary(x)
            fac[q] = fac.get(q, 0) + 1
            x = exact_div(x, q)
    else:
        import sympy
        for q, k in sympy.factorint(norm(x)).items():
            if q % 3 == 2:
                cands = [primary((q, 0))]
            else:
                pi = _prime_above(q)
                cands = [pi] if conj(pi) == pi else [pi, primary(conj(pi))]
            for P in cands:
                while divides(P, x):
                    x = exact_div(x, P); fac[P] = fac.get(P, 0) + 1
    assert norm(x) == 1, x
    return x, e, fac


def cub_prime(a, p):
    """cubic symbol (a/p)_3 = a^{(Np-1)/3} mod p as exponent of omega (also for p = 2); None if p | a."""
    if divides(p, a):
        return None
    t = powmod(a, (norm(p) - 1) // 3, p)
    for k, z in enumerate((ONE, W1, W2)):
        if divides(p, sub(t, z)):
            return k
    raise RuntimeError((a, p))


def cub(a, b_fac):
    """exponent k (value omega^k) of the cubic symbol (a/b)_3, b primary given by {p: k}; None if not coprime."""
    s = 0
    for p, k in b_fac.items():
        t = cub_prime(a, p)
        if t is None:
            return None
        s += k * t
    return s % 3


def cub_el(a, b):
    """(a/b)_3 for primary b (element)."""
    assert is_primary(b), b
    u, e, fac = factor(b)
    assert u == ONE and e == 0
    return cub(a, fac)


def sext(a, p):
    return sym_prime(a, p)


# ---------------------------------------------------------------- Gauss sums
_g1p = {}


def generator(p):
    N = norm(p); n = N - 1
    qs = [q for q in range(2, n + 1) if n % q == 0 and all(q % r for r in range(2, int(q ** 0.5) + 1))]
    for a in range(-5, 6):
        for b in range(-5, 6):
            t = (a, b)
            if divides(p, t):
                continue
            if all(powmod(t, n // q, p) != ONE and not divides(p, sub(powmod(t, n // q, p), ONE)) for q in qs):
                return t
    raise RuntimeError(p)


def _vpow(n, e, q):
    r = np.ones_like(n); b = n % q
    while e:
        if e & 1:
            r = (r * b) % q
        b = (b * b) % q; e >>= 1
    return r


def g1_prime(p):
    """unnormalised g(1,p) = sum_{x mod p} (x/p)_3 e-check(x/p)."""
    if p in _g1p:
        return _g1p[p]
    N = norm(p)
    if p[1] != 0:                      # split prime, O/p = Z/N via omega -> w0
        q = N; ap, bp = p
        w0 = (-ap * pow(bp, -1, q)) % q
        assert (w0 * w0 + w0 + 1) % q == 0 and divides(p, (-w0, 1))
        n = np.arange(1, q, dtype=np.int64)
        t = _vpow(n, (q - 1) // 3, q)
        k = np.where(t == 1, 0, np.where(t == w0, 1, 2))
        assert np.all((t == 1) | (t == w0) | (t == (w0 * w0) % q))
        s = complex(np.sum(np.exp(2j * np.pi * k / 3) * np.exp(2j * np.pi * ((n * (2 * ap - bp)) % q) / q)))
    else:
        t = generator(p); kt = cub_prime(t, p)
        s = 0j; y = ONE
        for k in range(N - 1):
            s += OM ** ((kt * k) % 3) * echeck_frac(y, p)
            y = reduce_mod(mul(y, t), p)
    _g1p[p] = s
    return s


def g1_direct(c):
    """direct unnormalised g(1,c) for primary c (any)."""
    R, N = eis.residues(c)
    u, e, fac = factor(c)
    s = 0j
    for x in R:
        k = cub(x, fac)
        if k is None:
            continue
        s += OM ** k * echeck_frac(x, c)
    return s


_gt = {}


def gtilde(cs):
    """normalised g~(c) for squarefree c = prod cs (tuple of primary primes, sorted) via twisted multiplicativity."""
    cs = tuple(sorted(cs, key=lambda q: (norm(q), q)))
    if cs in _gt:
        return _gt[cs]
    if len(cs) == 0:
        v = 1 + 0j
    elif len(cs) == 1:
        v = g1_prime(cs[0]) / math.sqrt(norm(cs[0]))
    else:
        a = cs[0]; rest = cs[1:]
        k = cub(a, {q: 1 for q in rest})                      # (a/b)_3
        v = (OM ** k).conjugate() * gtilde((a,)) * gtilde(rest)
    _gt[cs] = v
    return v


def prod(els):
    r = ONE
    for x in els:
        r = mul(r, x)
    return r


def conj_g(mu, cs):
    """conj(g(mu, c)) for squarefree primary c = prod cs, (mu,c)=1:  g(mu,c) = conj((mu/c)_3) g(1,c)."""
    c = prod(cs)
    g1 = gtilde(cs) * math.sqrt(norm(c))
    k = cub(mu, {q: 1 for q in cs}) if cs else 0
    return ((OM ** k).conjugate() * g1).conjugate()


# ---------------------------------------------------------------- tau, tau_1, tau_2 (DR (5.7), (5.13), (5.14))
E29 = cmath.exp(2j * math.pi / 9)
LAM2 = mul(LAM, LAM)


def split_cd(fac):
    if any(k % 3 == 2 for k in fac.values()):
        return None
    cs = [p for p, k in fac.items() if k % 3 == 1]
    dn = 1
    for p, k in fac.items():
        dn *= norm(p) ** (k // 3)
    return cs, math.sqrt(dn / norm(prod(cs)))      # |d/c|


def tau_nu3(nu):
    """tau(mu) for mu = nu / lambda^3, nu in O nonzero."""
    u, e, fac = factor(nu)
    L = e - 3
    sc = split_cd(fac)
    if sc is None:
        return 0j
    cs, dc = sc
    ui = UNITS.index(u)        # zeta^ui, zeta = 1+omega:  {0,3}=+-1, {2,5}=+-omega, {1,4}=+-omega^2
    if L % 3 == 2:
        n = (L + 4) // 3
        assert n >= 1
        f = 3 ** (n / 2 + 2) * dc
        if ui in (0, 3):
            return conj_g(LAM2, cs) * f
        if ui in (2, 5):
            return E29.conjugate() * conj_g(mul(W1, LAM2), cs) * f
        return E29 * conj_g(mul(W2, LAM2), cs) * f
    if L % 3 == 0:
        n = (L + 3) // 3
        assert n >= 0
        if ui in (0, 3):
            return conj_g(ONE, cs) * dc * 3 ** (n / 2 + 2.5)
        return 0j
    return 0j


def tau12_nu4(nu, which):
    """tau_1 or tau_2 at mu = nu/lambda^4."""
    u, e, fac = factor(nu)
    if e != 0:
        return 0j
    sc = split_cd(fac)
    if sc is None:
        return 0j
    cs, dc = sc
    if which == 1:
        if u == ONE:
            return 9 * OM * conj_g(LAM2, cs) * dc
        if u == W1:
            return 9 * E29.conjugate() * OM ** 2 * conj_g(mul(W1, LAM2), cs) * dc
        if u == W2:
            return 9 * E29 * conj_g(mul(W2, LAM2), cs) * dc
        return 0j
    else:
        if u == neg(ONE):
            return 9 * OM ** 2 * conj_g(LAM2, cs) * dc
        if u == neg(W1):
            return 9 * E29.conjugate() * conj_g(mul(W1, LAM2), cs) * dc
        if u == neg(W2):
            return 9 * OM * E29 * conj_g(mul(W2, LAM2), cs) * dc
        return 0j


LAM4 = pw(LAM, 4)
LAMC = toc(LAM)


def build_series(Nmax):
    """arrays (ell complex, coeff) for sigma in {0,+,-}; ell = nu/lambda^4, 0 < N(nu) <= Nmax."""
    out = {'0': ([], []), '+': ([], []), '-': ([], [])}
    ymax = int(math.sqrt(4 * Nmax / 3)) + 2
    for y in range(-ymax, ymax + 1):
        for x in range(-ymax - abs(y), ymax + abs(y) + 1):
            if x * x - x * y + y * y > Nmax or (x, y) == (0, 0):
                continue
            nu = (x, y)
            ell = toc(nu) / LAMC ** 4
            # sigma = 0 : t_0(l) = tau(l), support lambda^{-3} O
            if divides(LAM, nu):
                t = tau_nu3(exact_div(nu, LAM))
                if t != 0:
                    out['0'][0].append(ell); out['0'][1].append(t)
            # sigma = + : omega tau_2(omega l) e-check(l)
            t2 = tau12_nu4(mul(W1, nu), 2)
            if t2 != 0:
                out['+'][0].append(ell); out['+'][1].append(OM * t2 * cmath.exp(4j * math.pi * ell.real))
            t1 = tau12_nu4(mul(W2, nu), 1)
            if t1 != 0:
                out['-'][0].append(ell); out['-'][1].append(OM ** 2 * t1 * cmath.exp(4j * math.pi * ell.real))
    return {k: (np.array(a), np.array(b)) for k, (a, b) in out.items()}


def series_eval(S, sig, z, v):
    ell, co = S[sig]
    val = np.sum(co * v * kv(1 / 3, 4 * math.pi * np.abs(ell) * v) * np.exp(4j * math.pi * (ell * z).real))
    if sig == '0':
        val += SIGMA0 * v ** (2 / 3)
    return complex(val)


def act(g, z, v):
    """DR (5.1): action of g = ((a,b),(c,d)) (complex entries) on (z,v)."""
    (a, b), (c, d) = g
    den = abs(c * z + d) ** 2 + abs(c) ** 2 * v * v
    zn = ((a * z + b) * (c * z + d).conjugate() + a * c.conjugate() * v * v) / den
    return zn, v / den


def mc(g):
    return tuple(tuple(toc(x) for x in row) for row in g)


def mmul(A, B):
    return ((add(mul(A[0][0], B[0][0]), mul(A[0][1], B[1][0])), add(mul(A[0][0], B[0][1]), mul(A[0][1], B[1][1]))),
            (add(mul(A[1][0], B[0][0]), mul(A[1][1], B[1][0])), add(mul(A[1][0], B[0][1]), mul(A[1][1], B[1][1]))))


def minv(A):
    (a, b), (c, d) = A
    return ((d, neg(b)), (neg(c), a))


def det(A):
    return sub(mul(A[0][0], A[1][1]), mul(A[0][1], A[1][0]))


def cong_I_mod3(A):
    three = (3, 0)
    return (divides(three, sub(A[0][0], ONE)) and divides(three, A[0][1]) and divides(three, A[1][0])
            and divides(three, sub(A[1][1], ONE)))


def kubota(g1):
    """DR (5.4): kappa(g) = (c/a)_3 for g in Gamma_1(3), c != 0; 1 otherwise.  exponent mod 3."""
    (a, b), (c, d) = g1
    if c == (0, 0):
        return 0
    k = cub_el(c, a)
    assert k is not None
    return k


# ---------------------------------------------------------------- Euclid / CRT in O
def divmod_O(x, m):
    c, d = mul(x, conj(m)); n = norm(m)
    q = ((2 * c + n) // (2 * n), (2 * d + n) // (2 * n))
    return q, sub(x, mul(q, m))


def egcd(a, b):
    r0, r1 = a, b; s0, s1 = ONE, (0, 0); t0, t1 = (0, 0), ONE
    while r1 != (0, 0):
        q, r = divmod_O(r0, r1)
        r0, r1 = r1, r
        s0, s1 = s1, sub(s0, mul(q, s1))
        t0, t1 = t1, sub(t0, mul(q, t1))
    return r0, s0, t0


def inv_mod(a, m):
    g, s, t = egcd(a, m)
    assert norm(g) == 1, (a, m, g)
    ginv = conj(g)                     # unit inverse
    return reduce_mod(mul(s, ginv), m)


def crt(x1, m1, x2, m2):
    k = mul(sub(x2, x1), inv_mod(m1, m2))
    return reduce_mod(add(x1, mul(m1, reduce_mod(k, m2))), mul(m1, m2))


# ---------------------------------------------------------------- check C: local transform
def chi_pow(x, p, j):
    """chi_p^j(x) with zero extension (chi_p^0(x) = 1_{p not | x})."""
    k = sext(x, p)
    if k is None:
        return 0j
    return cmath.exp(1j * math.pi * ((j * k) % 6) / 3)


def check_C(results):
    rows = []
    worst = 0.0
    worst_fourier = 0.0
    # primes outside S: split primes of norm <= 43 and the inert primes 5, 11 (2 and lambda lie in S)
    tested = [p for p in PRIMES if 7 <= norm(p) <= 43 and p[1] != 0] + [primary((5, 0)), primary((11, 0))]
    rnd = random.Random(20261010)
    for p in tested:
        R, N = eis.residues(p)
        nz = [x for x in R if not divides(p, x)]
        gam = {j: eis.gamma(j, [p]) for j in range(1, 6)}
        chim1 = chi_pow(neg(ONE), p, 1)
        inv = {x: powmod(x, N - 2, p) for x in nz}
        for j in range(6):
            C = {}
            for h in R:
                C[h] = sum(chi_pow(y, p, j) * e_of(neg(mul(h, y)), p) for y in R) / N
            # eq:ray-fourier
            for h in R:
                if j != 0:
                    pred = 0j if divides(p, h) else N ** -0.5 * chim1 ** j * gam[j] * chi_pow(h, p, -j)
                else:
                    pred = (1 - 1 / N) if divides(p, h) else -1 / N
                worst_fourier = max(worst_fourier, abs(C[h] - pred))
            for trial in range(3):
                sig = rnd.choice(nz); eps = rnd.choice(nz)
                if j not in (0, 4):
                    om = chim1 ** j * gam[j] * gam[(j + 2) % 6 or 6] * chi_pow(eps, p, -j - 2)
                elif j == 4:
                    om = gam[4]
                else:
                    om = -gam[2] * chi_pow(eps, p, -2)
                for x in R:
                    lhs = sum(C[h] * chi_pow(mul(sig, h), p, -2) * e_of(mul(eps, mul(inv[h], x)), p) for h in nz)
                    if j not in (0, 4):
                        B = chi_pow(x, p, -j - 2)
                    elif j == 4:
                        B = N ** -0.5 * (-1 + (N if divides(p, x) else 0))
                    else:
                        B = N ** -0.5 * chi_pow(x, p, -2)
                    rhs = chi_pow(sig, p, -2) * om * B
                    worst = max(worst, abs(lhs - rhs))
                # j = 1 quadratic: B_{p,1} = chi_p^3 takes values +-1, 0
        rows.append({'p': p, 'N': N, 'gamma2^3+alpha': abs(gam[2] ** 3 + toc(p) / abs(toc(p))),
                     'gamma4-conj(gamma2)': abs(gam[4] - gam[2].conjugate())})
    results['C'] = {'primes': [r['p'] for r in rows], 'norms': [r['N'] for r in rows],
                    'max_err_ray_fourier': worst_fourier, 'max_err_ray_local_transform': worst,
                    'max_gamma2cubed_plus_alpha': max(r['gamma2^3+alpha'] for r in rows),
                    'max_gamma4_minus_conj_gamma2': max(r['gamma4-conj(gamma2)'] for r in rows)}
    print('C', results['C'], flush=True)


# ---------------------------------------------------------------- check D/E: multiplier and translate identity
M_LAM = 12          # M = lambda^12 L^4; only the lambda-part enters the multiplier formula


def lam_pow(k):
    return pw(LAM, k)


def build_g(a, c0, r):
    """Paper's construction: c = c0*r, delta' from the three congruences (q | c0 only q = lambda here)."""
    c = mul(c0, r)
    vl = 0; t = c0
    while divides(LAM, t):
        t = exact_div(t, LAM); vl += 1
    assert norm(t) == 1, 'test uses c0 = unit * lambda^k'
    if vl > 0:
        m1 = lam_pow(M_LAM + vl); x1 = inv_mod(a, m1)              # a delta' = 1 mod lambda^{v(M c0)}
    else:
        m1 = lam_pow(M_LAM); x1 = (0, 0)                           # delta' = 0 mod lambda^{v(M)}
    x2 = inv_mod(a, r)                                             # a delta' = 1 mod r
    dp = crt(x1, m1, x2, r)
    bg = exact_div(sub(mul(a, dp), ONE), c)
    g = ((a, bg), (c, dp))
    assert det(g) == ONE
    return g, vl


def choose_H(a, c, vl):
    if vl >= 2:
        return ((ONE, (0, 0)), ((0, 0), ONE)), '0', None
    if vl == 1:
        for u0 in (LAM, neg(LAM)):
            if divides((3, 0), sub(u0, c)):
                return ((ONE, (0, 0)), (u0, ONE)), None, u0
        raise RuntimeError
    # (c, lambda) = 1: u0 = a mod 3 from fixed reps
    reps = [(i, j) for i in range(3) for j in range(3)]
    for u0 in reps:
        if divides((3, 0), sub(u0, a)):
            return ((u0, neg(ONE)), (ONE, (0, 0))), None, u0
    raise RuntimeError


def formula_kappa(a, c0, r, bg, vl, u0):
    """paper2 eq:ray-multiplier, exponent mod 3."""
    kr = cub_el(a, r)                                  # (a/r)_3
    if vl >= 2:
        return (cub_el(c0, a) + kr) % 3                # (c0/a)_3 (a/r)_3
    if vl == 1:
        A = sub(a, mul(u0, bg))
        k1 = cub_el(neg(u0), A)                        # (-u0/(a-u0 b_g))_3
        k2 = cub_el(exact_div(c0, u0), a)              # ((c0/u0)/a)_3
        return (k1 + k2 + kr) % 3
    return (cub_el(a, c0) + kr) % 3 if c0 != ONE else kr   # (a/c0)_3 (a/r)_3


def check_D(results):
    rnd = random.Random(7)
    rs = [p for p in PRIMES if 7 <= norm(p) <= 400]
    c0s = [ONE, LAM, neg(LAM), mul(W1, LAM), (3, 0), mul(W2, (3, 0)), pw(LAM, 3), mul(LAM, (3, 0))]
    n_ok = n_tot = 0; n_conj_ok = 0; cases = {0: 0, 1: 0, 2: 0}; bad = []
    for trial in range(700):
        r = rnd.choice(rs)
        if rnd.random() < 0.3:
            r2 = rnd.choice(rs)
            if r2 != r:
                r = mul(r, r2)
        c0 = rnd.choice(c0s)
        c = mul(c0, r)
        lam_c = divides(LAM, c)
        # random a coprime to c with the paper's normalisation
        while True:
            a = (rnd.randint(-40, 40), rnd.randint(-40, 40))
            if a == (0, 0):
                continue
            g_, _, _ = egcd(a, c)
            if norm(g_) != 1:
                continue
            if lam_c and not is_primary(a):
                continue
            break
        if not lam_c and not is_primary(c):
            continue
        g, vl = build_g(a, c0, r)
        H, _, u0 = choose_H(a, c, vl)
        g1 = mmul(g, minv(H))
        assert cong_I_mod3(g1), (g, H, g1)
        kap = kubota(g1)
        bg = g[0][1]
        f = formula_kappa(a, c0, r, bg, vl, u0)
        n_tot += 1; cases[min(vl, 2)] += 1
        if kap == f:
            n_ok += 1
        else:
            bad.append({'a': a, 'c0': c0, 'r': r, 'kappa': kap, 'formula': f})
        if kap == (-f) % 3:
            n_conj_ok += 1
    results['D'] = {'tested': n_tot, 'agree': n_ok, 'agree_with_conjugate_formula': n_conj_ok,
                    'cases(vlambda(c)=0,1,>=2)': cases, 'first_failures': bad[:5]}
    print('D', results['D'], flush=True)


def check_ABEF(results, Nmax):
    t0 = time.time()
    S = build_series(Nmax)
    results['series'] = {'Nmax_nu': Nmax, 'terms': {k: int(len(v[0])) for k, v in S.items()},
                         'build_seconds': round(time.time() - t0, 1)}
    print('series', results['series'], flush=True)
    th = lambda z, v: series_eval(S, '0', z, v)
    out = {}
    # A1: E and T invariance (SL_2(Z), multiplier 1)
    z, v = complex(0.13, 0.21), 0.93
    zE, vE = act(mc(((((0, 0), neg(ONE)), (ONE, (0, 0))))), z, v)
    out['A_E_invariance_relerr'] = abs(th(zE, vE) - th(z, v)) / abs(th(z, v))
    out['A_T_invariance_relerr'] = abs(th(z + 1, v) - th(z, v)) / abs(th(z, v))
    out['A_T3omega_invariance_relerr'] = abs(th(z + 3 * OM, v) - th(z, v)) / abs(th(z, v))
    out['A_Tomega_NOT_invariant_relerr'] = abs(th(z + OM, v) - th(z, v)) / abs(th(z, v))
    # A2: Gamma_1(3) elements with c = 3 * unit, nontrivial (c/a)_3
    gam_rows = []
    for a in [p for p in PRIMES if norm(p) <= 200]:
        for cu in [(3, 0), mul(W1, (3, 0)), neg((3, 0))]:
            k = cub_el(cu, a)
            if k == 0:
                continue
            d = inv_mod(a, (9, 0))
            if not divides((3, 0), sub(d, ONE)):
                continue
            bnum = sub(mul(a, d), ONE)
            b = exact_div(bnum, cu)
            g = ((a, b), (cu, d))
            assert det(g) == ONE and cong_I_mod3(g)
            for (dz, vv) in [(complex(0.02, -0.03), 1 / 3), (complex(-0.05, 0.04), 0.36)]:
                zz = -toc(d) / toc(cu) + dz
                zg, vg = act(mc(g), zz, vv)
                lhs = th(zg, vg); base = th(zz, vv)
                ratio = lhs / base
                gam_rows.append({'a': a, 'c': cu, 'cubic_exp_(c/a)': k,
                                 'err_vs_(c/a)_3': abs(ratio - OM ** k), 'err_vs_conj': abs(ratio - OM ** (-k)),
                                 'heights': (round(vv, 3), round(vg, 3))})
            if len(gam_rows) >= 12:
                break
        if len(gam_rows) >= 12:
            break
    out['A_Gamma1(3)'] = {'n': len(gam_rows), 'max_err_vs_(c/a)_3': max(r['err_vs_(c/a)_3'] for r in gam_rows),
                          'min_err_vs_conj': min(r['err_vs_conj'] for r in gam_rows), 'sample': gam_rows[:3]}
    # B: cusp expansions at gamma_10 (+) and gamma_19 (-)
    Brows = []
    for (sig, gm) in [('+', ((ONE, (0, 0)), (W1, ONE))), ('-', ((ONE, (0, 0)), (W2, ONE)))]:
        for (zz, vv) in [(complex(0.11, -0.07), 0.62), (complex(-0.3, 0.25), 0.55), (complex(0.4, 0.1), 0.7)]:
            zg, vg = act(mc(gm), zz, vv)
            lhs = th(zg, vg); rhs = series_eval(S, sig, zz, vv)
            Brows.append({'sigma': sig, 'relerr': abs(lhs - rhs) / abs(lhs), 'heights': (vv, round(vg, 3))})
            # wrong-label control
            other = '-' if sig == '+' else '+'
            Brows[-1]['relerr_if_labels_swapped'] = abs(lhs - series_eval(S, other, zz, vv)) / abs(lhs)
    out['B_cusp_expansions'] = Brows
    # F: H -> gamma_sigma reduction with trivial multiplier (paper's rule)
    Frows = []
    Hs = [(((ONE, (0, 0)), (LAM, ONE)), '-'), (((ONE, (0, 0)), (neg(LAM), ONE)), '+')]
    for i in range(3):
        for j in range(3):
            u0 = (i, j)
            # u0 mod (Z + 3O): omega-coordinate j decides: 0 -> sigma 0, 1 -> omega -> '-', 2 -> -omega -> '+'
            Hs.append((((u0, neg(ONE)), (ONE, (0, 0))), {0: '0', 1: '-', 2: '+'}[j]))
    for H, sig in Hs:
        for (zz, vv) in [(complex(0.07, 0.05), 0.8), (complex(-0.12, 0.2), 0.6)]:
            if H[1][0] in (LAM, neg(LAM)):
                zz = -1 / toc(H[1][0]) + complex(0.05, -0.04); vv = 0.58
            zh, vh = act(mc(H), zz, vv)
            lhs = th(zh, vh); rhs = series_eval(S, sig, zz, vv)
            Frows.append({'H': H, 'sigma': sig, 'relerr': abs(lhs - rhs) / abs(lhs), 'heights': (vv, round(vh, 3))})
    out['F_H_reduction'] = {'n': len(Frows), 'max_relerr': max(r['relerr'] for r in Frows)}
    # E: end-to-end translate identity theta(a/c, v) = kappa(g1) S_sigma(g^{-1}(a/c, v))
    Erows = []
    rnd = random.Random(11)
    rs = [p for p in PRIMES if norm(p) in (7, 13, 19)]
    for c0 in [ONE, LAM, neg(LAM), (3, 0), mul(W1, (3, 0))]:
        for r in rs:
            c = mul(c0, r)
            if norm(c) > 63:
                continue
            if not divides(LAM, c) and not is_primary(c):
                continue
            tries = 0
            while tries < 2:
                a = (rnd.randint(-9, 9), rnd.randint(-9, 9))
                if a == (0, 0) or norm(egcd(a, c)[0]) != 1:
                    continue
                if divides(LAM, c) and not is_primary(a):
                    continue
                tries += 1
                g, vl = build_g(a, c0, r)
                H, _, u0 = choose_H(a, c, vl)
                g1 = mmul(g, minv(H))
                kap = kubota(g1)
                if vl >= 2:
                    sig = '0'
                elif vl == 1:
                    sig = '-' if u0 == LAM else '+'
                else:
                    sig = {0: '0', 1: '-', 2: '+'}[u0[1] % 3]
                v = 1 / math.sqrt(norm(c)) * (1.0 + 0.1 * tries)
                zt = toc(a) / toc(c) + complex(0.003, -0.002)
                lhs = th(zt, v)
                zp, vp = act(mc(minv(g)), zt, v)
                rhs_core = series_eval(S, sig, zp, vp)
                err = abs(lhs - OM ** kap * rhs_core) / abs(lhs)
                errc = abs(lhs - OM ** (-kap) * rhs_core) / abs(lhs)
                Erows.append({'c0': c0, 'r': r, 'a': a, 'vlambda': vl, 'sigma': sig, 'kappa_exp': kap,
                              'formula_exp': formula_kappa(a, c0, r, g[0][1], vl, u0),
                              'relerr': err, 'relerr_with_conj_kappa': errc, 'heights': (round(v, 3), round(vp, 3))})
    out['E_translate_identity'] = {'n': len(Erows), 'max_relerr': max(r['relerr'] for r in Erows),
                                   'n_nontrivial_kappa': sum(1 for r in Erows if r['kappa_exp'] != 0),
                                   'min_relerr_with_conj_kappa_over_nontrivial':
                                       min([r['relerr_with_conj_kappa'] for r in Erows if r['kappa_exp'] != 0] or [None]),
                                   'formula_matches_kubota': all(r['kappa_exp'] == r['formula_exp'] for r in Erows),
                                   'rows': Erows}
    results.update(out)
    print('A', {k: v for k, v in out.items() if k.startswith('A')}, flush=True)
    print('B', [(r['sigma'], r['relerr'], r['relerr_if_labels_swapped']) for r in Brows], flush=True)
    print('F', out['F_H_reduction'], flush=True)
    print('E', {k: v for k, v in out['E_translate_identity'].items() if k != 'rows'}, flush=True)


def check_gauss(results):
    errs = []
    for p in [q for q in PRIMES if norm(q) <= 200]:
        errs.append(abs(g1_prime(p) - g1_direct(p)))
    comp = []
    small = [q for q in PRIMES if norm(q) <= 40]
    for i in range(len(small)):
        for j in range(i + 1, len(small)):
            cs = (small[i], small[j]); c = prod(cs)
            if norm(c) > 1200:
                continue
            comp.append(abs(gtilde(cs) * math.sqrt(norm(c)) - g1_direct(c)))
    cube = max(abs(gtilde((p,)) ** 3 + toc(p) / abs(toc(p))) for p in PRIMES if norm(p) <= 3000)
    results['gauss'] = {'prime_fast_vs_direct_max': max(errs), 'composite_twistmult_vs_direct_max': max(comp),
                        'n_composite': len(comp), 'gtilde(p)^3 + p/|p| max (N<=3000)': cube}
    print('gauss', results['gauss'], flush=True)


def check_G(results):
    """paper2 eq:intro-theta-coefficients: c_theta(n b^3) = conj tau(lambda^{-3} n b^3)
    = 3^{5/2} |b| conj(chi_n(lambda)^2) gamma_2(n), incl. (n,b) != 1."""
    ns = []
    small = [q for q in PRIMES if 7 <= norm(q) <= 60]
    for i, q in enumerate(small):
        ns.append([q])
        for q2 in small[i + 1:]:
            if norm(q) * norm(q2) <= 700:
                ns.append([q, q2])
    bs = [ONE] + [q for q in PRIMES if 4 <= norm(q) <= 13]
    worst = 0.0; cnt = 0
    for nf in ns:
        n = prod(nf)
        g2 = eis.gamma(2, nf)
        k = cub(LAM, {q: 1 for q in nf})           # chi_n(lambda)^2 = (lambda/n)_3
        for b in bs + [nf[0]]:
            nb3 = mul(n, pw(b, 3))
            lhs = tau_nu3(nb3).conjugate()
            rhs = 3 ** 2.5 * math.sqrt(norm(b)) * (OM ** k).conjugate() * g2
            worst = max(worst, abs(lhs - rhs) / abs(rhs)); cnt += 1
    results['G_intro_theta_coefficients'] = {'n_cases': cnt, 'max_relerr': worst}
    print('G', results['G_intro_theta_coefficients'], flush=True)


def check_H(results):
    """eq:bessel-mellin (DLMF 10.43.19) and the scalar bookkeeping -i/81 with the gamma quotient of eq:theta-weight:
    composes eq:ray-mellin, eq:theta-mellin-functional-equation, eq:dual-cusp-mellin-series symbolically."""
    import mpmath as mp
    mp.mp.dps = 30
    errs = []
    for (s, L) in [(mp.mpf('1.3'), mp.mpf('0.7')), (mp.mpc('2.1', '0.8'), mp.mpf('1.9')), (mp.mpc('0.6', '-1.5'), mp.mpf('0.25'))]:
        lhs = mp.quad(lambda v: v ** (2 * s) * mp.besselk(mp.mpf(1) / 3, 4 * mp.pi * L * v), [0, 1, mp.inf])
        rhs = 2 ** (2 * s - 1) * mp.gamma(s + mp.mpf(1) / 3) * mp.gamma(s + mp.mpf(2) / 3) / (4 * mp.pi * L) ** (2 * s + 1)
        errs.append(float(abs(lhs - rhs) / abs(rhs)))
    # scalar: T(s) = J(s) / [(3^{5/2}/4)(27/(2pi)^2)^s G(s)],  J(s) = - X N(c)^{1-2s} Jv(1-s),
    # Jv(s') = i G(s') / (4 (2pi)^{2s'}) * Sum d alpha N(l)^{-s'}, G(s) = Gamma(s+1/3)Gamma(s+2/3).
    # Claim: with s = 1/2 - t the coefficient of X * Sum d alpha N(l)^{-1/2} [...]^{-t} * Gamma-quotient is -i/81 and
    # the scale is ((2pi)^4 N(l) X / (27 N(c)^2))^{-t}.
    out = []
    for (t, Nc, Nl, X) in [(mp.mpc('0.3', '0.7'), 21, 5.0, 3.0), (mp.mpc('-0.2', '2.0'), 63, 0.4, 11.0)]:
        s = mp.mpf(1) / 2 - t
        G = lambda z: mp.gamma(z + mp.mpf(1) / 3) * mp.gamma(z + mp.mpf(2) / 3)
        Jv_coeff = 1j * G(1 - s) / (4 * (2 * mp.pi) ** (2 * (1 - s))) * Nl ** (-(1 - s))
        T_coeff = -(Nc ** (1 - 2 * s)) * Jv_coeff / ((3 ** 2.5 / 4) * (27 / (2 * mp.pi) ** 2) ** s * G(s)) * X ** (s - mp.mpf(1) / 2)
        claim = (-1j / 81) * Nl ** (-0.5) * (mp.gamma(mp.mpf(7) / 6 + t) * mp.gamma(mp.mpf(5) / 6 + t)
                 / (mp.gamma(mp.mpf(7) / 6 - t) * mp.gamma(mp.mpf(5) / 6 - t))) * ((2 * mp.pi) ** 4 * Nl * X / (27 * Nc ** 2)) ** (-t)
        out.append(float(abs(T_coeff - claim) / abs(claim)))
    # gamma quotient has modulus 1 on Re t = 0
    q = [float(abs(mp.gamma(mp.mpf(7) / 6 + 1j * u) * mp.gamma(mp.mpf(5) / 6 + 1j * u)
                   / (mp.gamma(mp.mpf(7) / 6 - 1j * u) * mp.gamma(mp.mpf(5) / 6 - 1j * u))) - 1) for u in (0.3, 4.0, 25.0)]
    results['H_mellin'] = {'bessel_mellin_relerr': max(errs), 'scalar_and_scale_relerr': max(out), 'unit_modulus_on_Re_t_0': max(q)}
    print('H', results['H_mellin'], flush=True)


def main():
    outp = sys.argv[1]
    Nmax = int(sys.argv[2]) if len(sys.argv) > 2 else 22000
    res = {'python': sys.version.split()[0], 'numpy': np.__version__}
    t = time.time()
    check_gauss(res)
    check_G(res)
    check_H(res)
    check_C(res)
    check_D(res)
    check_ABEF(res, Nmax)
    res['seconds'] = round(time.time() - t, 1)
    with open(outp, 'w') as f:
        json.dump(res, f, indent=1, default=str)
    print('done', res['seconds'])


if __name__ == '__main__':
    main()
