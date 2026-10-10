"""End-to-end numerical test of paper2 eq:reflection (Prop. lem:reflection), OCT5_REFLECTION_E2E.md.

Status: EXPLORATORY.  FLOAT = ordinary double precision (not directed, not certified); residue symbols
and all matrix / CRT constructions are EXACT (Python integers).

Setting: K = Q(omega), S = {(2), (lambda)}, Psi_0 = trivial ray class character (zero on S),
L = 18 (phi(n) = 1_{n=1 (3)} 1_{2 not| n} (lambda/n)_3 is 18-periodic: checked), M = lambda^12 L^4,
Psi(n) = Psi_0(n) prod_{p in P} chi_p^{j_p}(n).

LHS : T(X; Psi) from paper2 eq:T, summed directly over squarefree primary n and primary b.
RHS1: per-translate dual sums (this file's own derivation from eq:theta-cusp-automorphy,
      eq:theta-mellin-functional-equation, eq:dual-cusp-mellin-series):
        sum_h  -(i/81) c_F(h) conj(kappa(g_1,h)) conj(alpha(c_h))^2
               sum_l d_sigma_h(l) alpha(l) N(l)^{-1/2} echeck(-delta'_h l / c_h) Vsharp(N(l) X / N(c_h)^2),
      with kappa(g_1) = (c_1/a_1)_3 computed directly by a cubic Jacobi-symbol algorithm (not the
      paper's eq:ray-multiplier) and c_F(h) from direct finite Fourier sums (not eq:ray-fourier).
RHS2: the paper's grouped formula eq:reflection with the paper's C, psi, B_{p,j}, omega_{p,j},
      sigma_p, epsilon_p, kappa_0 (kappa_0 := kappa(g_1) prod chi_p(a)^{-2}; constancy is checked).
Vsharp from its Mellin-Barnes definition eq:theta-weight (trapezoid on Re t = 0, closed-form Mellin
transforms of the test functions), cross-checked with mpmath (Mellin-Barnes quad and Meijer-G).

Usage: python3 -I oct5_reflection_e2e.py TABLES.npz OUT.json
"""
import sys, os, math, cmath, json, time, itertools
import numpy as np
from scipy.special import loggamma
from scipy.interpolate import CubicSpline

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'a2'))
import oct5_r3_theta_checks as r3
import eis
from eis import mul, conj, norm, is_primary, primary, divides, reduce_mod, UNITS

OM = r3.OM
LAM = (1, 2)
ONE = (1, 0)
ZERO = (0, 0)
ZETA = [cmath.exp(1j * math.pi * k / 3) for k in range(6)]
add, sub, neg, exact_div, pw, toc = r3.add, r3.sub, r3.neg, r3.exact_div, r3.pw, r3.toc


def log(*a):
    print(time.strftime('%H:%M:%S'), *a, flush=True)


def alpha(x):
    z = toc(x)
    return z / abs(z)


# ------------------------------------------------------------------ cubic Jacobi symbol (big integers)
SUPW, SUPL = {}, {}


def build_sup():
    """(omega/beta)_3, (lambda/beta)_3 exponents for primary beta, as functions of beta mod 9 (from primes)."""
    for p in r3.PRIMES[:400]:
        key = (p[0] % 9, p[1] % 9)
        kw = r3.cub_prime((0, 1), p); kl = r3.cub_prime(LAM, p)
        if key in SUPW:
            assert SUPW[key] == kw and SUPL[key] == kl, ('supplementary law not mod 9', p)
        SUPW[key] = kw; SUPL[key] = kl
    assert len(SUPW) == 9


def cubic_jacobi(a, b):
    """exponent k with (a/b)_3 = omega^k for b prime to 3 (symbol depends on the ideal (b)); None if not coprime."""
    b = primary(b)
    res = 0
    while True:
        if norm(b) == 1:
            return res % 3
        a = reduce_mod(a, b)
        if a == ZERO:
            return None
        key = (b[0] % 9, b[1] % 9)
        while divides(LAM, a):
            a = exact_div(a, LAM); res += SUPL[key]
        for k, u in enumerate(UNITS):          # zeta^k a primary; a = zeta^{-k} y, zeta^{-k} = (-1)^k omega^k
            y = mul(u, a)
            if is_primary(y):
                break
        res += k * SUPW[key]
        a, b = b, y                             # cubic reciprocity for primary a, b


def check_jacobi(rng, n=400):
    bad = 0
    for _ in range(n):
        while True:
            b = (rng.randint(-60, 60), rng.randint(-60, 60))
            if norm(b) > 1 and not divides(LAM, b):
                break
        a = (rng.randint(-10 ** 6, 10 ** 6), rng.randint(-10 ** 6, 10 ** 6))
        ref = r3.cub_el(a, primary(b))
        if ref != cubic_jacobi(a, b):
            bad += 1
    return bad


# ------------------------------------------------------------------ small helpers in O
def vq(x, q):
    k = 0
    while x != ZERO and divides(q, x):
        x = exact_div(x, q); k += 1
    return k


def sext_exp(x, p):
    return eis.sym_prime(x, p)        # (x/p)_6 = zeta^k, None if p | x


def chi_pow(x, p, j):
    k = sext_exp(x, p)
    return 0j if k is None else ZETA[(j * k) % 6]


def e_frac(w, n):
    return eis.e_of(w, n)             # e(w/n), e(z) = exp(4 pi i Im z / sqrt 3)


def hnf(Q):
    v1, v2 = Q, mul(Q, (0, 1))
    a1, b1 = v1; a2, b2 = v2
    N = abs(a1 * b2 - a2 * b1)

    def eg(a, b):
        if b == 0:
            return (a, 1, 0)
        q_, x, y = eg(b, a % b); return (q_, y, x - (a // b) * y)
    g, x, y = eg(b1, b2)
    if g < 0:
        g, x, y = -g, -x, -y
    wx = x * a1 + y * a2
    d1 = N // g
    assert d1 * g == N == norm(Q)
    return d1, wx, g


def res_index(mx, my, d1, wx, g):
    j = np.mod(my, g); k = (my - j) // g
    i = np.mod(mx - k * wx, d1)
    return j * d1 + i


# ------------------------------------------------------------------ test functions and Vsharp
TESTFNS = {
    # V_*(y) = exp(-(ln(y/y0))^2/(2 s^2)):  Vhat(w) = y0^w sqrt(2 pi) s exp(s^2 w^2/2)
    'TF1_loggauss_s0.5_y01': dict(kind='g', s=0.5, y0=1.0),
    # V_*(y) = ln(y/y0) exp(-(ln(y/y0))^2/(2 s^2)):  Vhat(w) = y0^w sqrt(2 pi) s^3 w exp(s^2 w^2/2)
    'TF2_logxgauss_s0.45_y02': dict(kind='xg', s=0.45, y0=2.0),
}


def Vstar(tf, y):
    v = np.log(y / tf['y0']); g = np.exp(-v * v / (2 * tf['s'] ** 2))
    return g if tf['kind'] == 'g' else v * g


def Vhat(tf, w):
    s, y0 = tf['s'], tf['y0']
    base = np.exp(w * math.log(y0)) * math.sqrt(2 * math.pi) * s * np.exp(s * s * w * w / 2)
    return base if tf['kind'] == 'g' else base * s * s * w


def Qgam(t):
    return np.exp(loggamma(7 / 6 + t) + loggamma(5 / 6 + t) - loggamma(7 / 6 - t) - loggamma(5 / 6 - t))


def vsharp_direct(tf, lnx, U=25.0, du=0.02):
    u = np.arange(-U, U + du / 2, du); t = 1j * u
    coef = Vhat(tf, -t) * Qgam(t) * du / (2 * math.pi)
    lnY = np.asarray(lnx) + math.log((2 * math.pi) ** 4 / 27)
    out = np.empty(len(lnY), dtype=complex)
    for i0 in range(0, len(lnY), 2000):
        blk = lnY[i0:i0 + 2000]
        out[i0:i0 + 2000] = np.exp(-np.outer(blk, t)) @ coef
    return out


def vsharp_mp(tf, x, dps=20):
    import mpmath as mp
    mp.mp.dps = dps
    s, y0 = mp.mpf(tf['s']), mp.mpf(tf['y0'])
    Y = (2 * mp.pi) ** 4 * mp.mpf(x) / 27

    def f(u):
        t = 1j * u; w = -t
        vh = y0 ** w * mp.sqrt(2 * mp.pi) * s * mp.exp(s * s * w * w / 2)
        if tf['kind'] == 'xg':
            vh *= s * s * w
        q = mp.exp(mp.loggamma(mp.mpf(7) / 6 + t) + mp.loggamma(mp.mpf(5) / 6 + t)
                   - mp.loggamma(mp.mpf(7) / 6 - t) - mp.loggamma(mp.mpf(5) / 6 - t))
        return vh * q * Y ** (-t) / (2 * mp.pi)
    return complex(mp.quad(f, mp.linspace(-30, 30, 61)))


def vsharp_meijer(tf, x, dps=20):
    """independent real-space representation: Vsharp(x) = int V_*(y) G(y (2pi)^4 x/27) dy/y,
    G = Meijer G^{2,0}_{0,4}( . | 7/6, 5/6, -1/6, 1/6) (inverse Mellin of the gamma quotient)."""
    import mpmath as mp
    mp.mp.dps = dps
    c = (2 * mp.pi) ** 4 * mp.mpf(x) / 27
    s, y0 = mp.mpf(tf['s']), mp.mpf(tf['y0'])

    def f(v):           # y = y0 e^v
        g = mp.exp(-v * v / (2 * s * s))
        if tf['kind'] == 'xg':
            g *= v
        return g * mp.meijerg([[], []], [[mp.mpf(7) / 6, mp.mpf(5) / 6], [-mp.mpf(1) / 6, mp.mpf(1) / 6]], y0 * mp.exp(v) * c)
    return complex(mp.quad(f, mp.linspace(-8 * s, 8 * s, 17)))


class VS:
    def __init__(self, tf, lo=-22.0, hi=15.0, h=0.0005):
        self.tf = tf
        self.grid = np.arange(lo, hi + h / 2, h)
        vals = vsharp_direct(tf, self.grid)
        self.re = CubicSpline(self.grid, vals.real); self.im = CubicSpline(self.grid, vals.imag)
        self.lo, self.hi = lo, hi
        self.absmax = float(np.max(np.abs(vals)))
        # tail: largest |Vsharp| beyond x
        a = np.abs(vals)
        self.tailmax = np.maximum.accumulate(a[::-1])[::-1]

    def __call__(self, x):
        lx = np.log(x)
        out = self.re(lx) + 1j * self.im(lx)
        out[lx > self.hi] = 0.0
        assert np.all(lx >= self.lo)
        return out

    def tail_beyond(self, x):
        i = np.searchsorted(self.grid, math.log(x))
        return float(self.tailmax[min(i, len(self.grid) - 1)])


# ------------------------------------------------------------------ the arithmetic set-up
L = (18, 0)
M = mul(pw(LAM, 12), pw(L, 4))
M2 = mul(M, M)
V_LAM_M, V_2_M = vq(M, LAM), vq(M, (2, 0))


def phi_val(x, e0):
    """phi(n) = chi_n(lambda)^2 Psi_0(n) = (lambda/n)_3^{1+e0} on primary n prime to S; Psi_0 = (lambda/.)_3^{e0}."""
    if not is_primary(x) or divides((2, 0), x):
        return 0j
    return OM ** (((1 + e0) * cubic_jacobi(LAM, x)) % 3)


def setup_phi(rng, e0):
    R, N = eis.residues(L)
    phi = {x: phi_val(x, e0) for x in R}
    # periodicity check of phi modulo 18 on random shifts
    bad = 0
    for _ in range(300):
        x = R[rng.randrange(len(R))]
        t = (rng.randint(-50, 50), rng.randint(-50, 50))
        if abs(phi_val(add(x, mul(L, t)), e0) - phi[x]) > 1e-12:
            bad += 1
    phihat = {}
    for h in R:
        phihat[h] = sum(phi[x] * e_frac(neg(mul(h, x)), L) for x in R) / N
    return R, phi, phihat, bad


def Cpj(p, j):
    R, N = eis.residues(p)
    out = {}
    for h in R:
        out[h] = sum(chi_pow(y, p, j) * e_frac(neg(mul(h, y)), p) for y in R) / N
    return R, out


def normalise_frac(num, den):
    if num == ZERO:
        return ZERO, ONE
    g = r3.egcd(num, den)[0]
    a = exact_div(num, g); c = exact_div(den, g)
    if divides(LAM, c):
        for u in UNITS:
            if is_primary(mul(u, a)):
                return mul(u, a), mul(u, c)
    for u in UNITS:
        if is_primary(mul(u, c)):
            return mul(u, a), mul(u, c)
    raise RuntimeError


def build_delta(a, c, c0, r):
    mods = []
    vl0, v20 = vq(c0, LAM), vq(c0, (2, 0))
    m1 = pw(LAM, V_LAM_M + vl0)
    mods.append((r3.inv_mod(a, m1) if vl0 > 0 else ZERO, m1))
    m2 = pw((2, 0), V_2_M + v20)
    mods.append((r3.inv_mod(a, m2) if v20 > 0 else ZERO, m2))
    if norm(r) > 1:
        mods.append((r3.inv_mod(a, r), r))
    x, m = mods[0]
    for x2, m2_ in mods[1:]:
        x = r3.crt(x, m, x2, m2_); m = mul(m, m2_)
    return x


def choose_H(a, c):
    vl = vq(c, LAM) if c != ZERO else 0
    if vl >= 2:
        return ((ONE, ZERO), (ZERO, ONE)), '0', None
    if vl == 1:
        for u0, sg in ((LAM, '-'), (neg(LAM), '+')):
            if divides((3, 0), sub(u0, c)):
                return ((ONE, ZERO), (u0, ONE)), sg, u0
        raise RuntimeError
    for i in range(3):
        for j in range(3):
            if divides((3, 0), sub((i, j), a)):
                return (((i, j), neg(ONE)), (ONE, ZERO)), {0: '0', 1: '-', 2: '+'}[j], (i, j)
    raise RuntimeError


def echeck_params(delta, c):
    """echeck(-delta' l / c) for l = m/lambda^4  ->  exp(2 pi i (P1 m1 + P2 m2)/ND)."""
    D = mul(pw(LAM, 4), c)
    dr = reduce_mod(delta, mul(pw(LAM, 3), c))
    u, v = mul(neg(dr), conj(D)); ND = norm(D)
    return (2 * u - v) % ND, (-(u + v)) % ND, ND


def e_params(w, D):
    """e(w m / D) = exp(2 pi i * (Q1 m1 + Q2 m2)/ND):  e(z) = exp(2 pi i d) for z = (c + d omega)/ND."""
    u, v = mul(w, conj(D)); ND = norm(D)
    # (u + v w)(m1 + m2 w) = u m1 - v m2 + (u m2 + v m1 - v m2) w  -> d = u m2 + v m1 - v m2
    return v % ND, (u - v) % ND, ND


def build_config(cfg, R18, phihat, rng):
    """cfg: list of (p, j). Returns modulus data and F arrays (dict key (sigma, Nc) -> array over residues)."""
    P = [p for p, j in cfg]; J = {p: j for p, j in cfg}
    Q = (54, 0)
    for p in P:
        Q = mul(Q, p)
    d1, wx, g = hnf(Q)
    RI = np.tile(np.arange(d1, dtype=np.int64), g); RJ = np.repeat(np.arange(g, dtype=np.int64), d1)
    nres = d1 * g
    Cs = {p: Cpj(p, J[p]) for p in P}
    Rp = {p: Cs[p][0] for p in P}
    variants = ['RHS1', 'RHS1_ctrl_conj_kappa', 'RHS1_ctrl_alpha_c_sq', 'RHS1_ctrl_drop_cusp_phase',
                'RHS2', 'RHS2_ctrl_drop_psi', 'RHS2_ctrl_B_conj_convention', 'RHS2_ctrl_conj_kappa0',
                'RHS2_ctrl_scalar_plus_i_over_81']
    F = {}

    def acc(var, key, vec):
        k = (var, key[0], key[1])
        if k not in F:
            F[k] = np.zeros(nres, dtype=complex)
        F[k] += vec

    groups = {}
    ntr = 0
    for h0 in R18:
        ph = phihat[h0]
        if abs(ph) < 1e-13:
            continue
        for hs in itertools.product(*[Rp[p] for p in P]):
            cF = ph
            for p, hp in zip(P, hs):
                cF *= Cs[p][1][hp]
            if abs(cF) < 1e-15:
                continue
            A = tuple(p for p, hp in zip(P, hs) if hp != ZERO)
            H_lift = {p: r3.crt(hp, p, ZERO, M2) for p, hp in zip(P, hs) if hp != ZERO}
            r = ONE; den = L
            for p in A:
                r = mul(r, p); den = mul(den, p)
            num = mul(h0, r)
            for p in A:
                t = mul(L, H_lift[p])
                for p2 in A:
                    if p2 != p:
                        t = mul(t, p2)
                num = add(num, t)
            num = mul(mul(LAM, LAM), num)
            a, c = normalise_frac(num, den)
            c0 = exact_div(c, r)
            # c0 must be the reduced denominator of lambda^2 h0/L (up to a unit)
            a0, c0ref = normalise_frac(mul(mul(LAM, LAM), h0), L)
            assert norm(c0) == norm(c0ref) and divides(c0, c0ref), (h0, c0, c0ref)
            delta = build_delta(a, c, c0, r)
            bg = exact_div(sub(mul(a, delta), ONE), c)
            gmat = ((a, bg), (c, delta))
            H, sg, u0 = choose_H(a, c)
            g1 = r3.mmul(gmat, r3.minv(H))
            assert r3.det(g1) == ONE and r3.cong_I_mod3(g1)
            kap = 0 if g1[1][0] == ZERO else cubic_jacobi(g1[1][0], g1[0][0])
            Nc = norm(c)
            key = (sg, Nc)
            ac2 = alpha(c).conjugate() ** 2
            P1, P2, ND = echeck_params(delta, c)
            phase = np.exp(2j * math.pi * ((P1 * RI + P2 * RJ) % ND) / ND)
            base = -(1j / 81) * cF
            acc('RHS1', key, base * (OM ** kap).conjugate() * ac2 * phase)
            acc('RHS1_ctrl_conj_kappa', key, base * OM ** kap * ac2 * phase)
            acc('RHS1_ctrl_alpha_c_sq', key, base * (OM ** kap).conjugate() * ac2.conjugate() * phase)
            acc('RHS1_ctrl_drop_cusp_phase', key, base * (OM ** kap).conjugate() * ac2 * np.ones(nres))
            ntr += 1
            # group bookkeeping for RHS2
            kp = sum(sext_exp(a, p) for p in A) if A else 0           # prod chi_p(a)^2 = omega^{sum k}
            kap0 = (kap - kp) % 3
            gk = (h0, A)
            D0 = mul(pw(LAM, 3), c0)
            if gk not in groups:
                groups[gk] = dict(c=c, c0=c0, r=r, sg=sg, kap0=kap0, delta=delta, D0=D0, a=a, n=0, kap0_bad=0,
                                  delta_bad=0, c_bad=0)
            G_ = groups[gk]
            G_['n'] += 1
            if c != G_['c'] or sg != G_['sg']:
                G_['c_bad'] += 1
            if kap0 != G_['kap0']:
                G_['kap0_bad'] += 1
            if not divides(D0, sub(delta, G_['delta'])):
                G_['delta_bad'] += 1
    # RHS2: the paper's grouped formula
    gam = {p: {j: eis.gamma(j, [p]) for j in range(1, 6)} for p in P}
    nbad = {'c': 0, 'kap0': 0, 'delta0': 0}
    for (h0, A), G_ in groups.items():
        nbad['c'] += G_['c_bad']; nbad['kap0'] += G_['kap0_bad']; nbad['delta0'] += G_['delta_bad']
        c, c0, r, D0 = G_['c'], G_['c0'], G_['r'], G_['D0']
        rinv = r3.inv_mod(r, D0) if norm(D0) > 1 else ZERO
        w = neg(mul(G_['delta'], rinv))
        Q1, Q2, ND0 = e_params(w, D0)
        psi = np.exp(2j * math.pi * ((Q1 * RI + Q2 * RJ) % ND0) / ND0)
        Cconst = -(1j / 81) * alpha(c).conjugate() ** 2 * phihat[h0]
        Bprod = np.ones(nres, dtype=complex); Bprod_c = np.ones(nres, dtype=complex)
        for p in P:
            j = J[p]; Np = norm(p)
            if p not in A:
                Cconst *= (1 - 1 / Np)
                continue
            lam3c_p = exact_div(mul(pw(LAM, 3), c), p)
            sig_p = reduce_mod(exact_div(mul(mul(LAM, LAM), c), p), p)
            eps_p = reduce_mod(neg(r3.inv_mod(mul(lam3c_p, sig_p), p)), p)
            chim1 = chi_pow(neg(ONE), p, 1)
            if j not in (0, 4):
                omg = chim1 ** j * gam[p][j] * gam[p][(j + 2) % 6 or 6] * chi_pow(eps_p, p, -j - 2)
            elif j == 4:
                omg = gam[p][4]
            else:
                omg = -gam[p][2] * chi_pow(eps_p, p, -2)
            Cconst *= chi_pow(sig_p, p, -2) * omg
            # B_{p,j}(m) on residues: need chi_p(m) for m = (RI, RJ)
            k6 = sext_table(p, RI, RJ)
            zero = k6 < 0
            if j not in (0, 4):
                B = np.where(zero, 0, np.exp(1j * math.pi * ((-j - 2) * k6 % 6) / 3))
                Bc = np.where(zero, 0, np.exp(1j * math.pi * ((-j + 2) * k6 % 6) / 3))
            elif j == 4:
                B = Np ** -0.5 * (-1 + Np * zero)
                Bc = np.where(zero, 0, Np ** -0.5 * np.exp(1j * math.pi * ((-j + 2) * k6 % 6) / 3))
            else:
                B = np.where(zero, 0, Np ** -0.5 * np.exp(1j * math.pi * ((-2) * k6 % 6) / 3))
                Bc = np.where(zero, 0, Np ** -0.5 * np.exp(1j * math.pi * ((2) * k6 % 6) / 3))
            Bprod = Bprod * B; Bprod_c = Bprod_c * Bc
        key = (G_['sg'], norm(c))
        kap0v = OM ** G_['kap0']
        acc('RHS2', key, Cconst * kap0v.conjugate() * psi * Bprod)
        acc('RHS2_ctrl_drop_psi', key, Cconst * kap0v.conjugate() * Bprod)
        acc('RHS2_ctrl_B_conj_convention', key, Cconst * kap0v.conjugate() * psi * Bprod_c)
        acc('RHS2_ctrl_conj_kappa0', key, Cconst * kap0v * psi * Bprod)
        acc('RHS2_ctrl_scalar_plus_i_over_81', key, -Cconst * kap0v.conjugate() * psi * Bprod)
    info = dict(translates=ntr, groups=len(groups), modulus_norm=nres, group_inconsistencies=nbad,
                sigma_Nc_keys=sorted(set((k[1], k[2]) for k in F)))
    return dict(Q=Q, hnf=(d1, wx, g), F=F, variants=variants, info=info)


_sext_cache = {}


def sext_table(p, RI, RJ):
    """k with chi_p(i + j omega) = zeta^k on the residue arrays, -1 where p | x."""
    q = norm(p)
    if p[1] != 0:
        a, b = p
        rr = (-a * pow(b, -1, q)) % q
        if p not in _sext_cache:
            tab = np.full(q, -1, dtype=np.int64)
            z = (1 + rr) % q; zk = [pow(z, k, q) for k in range(6)]
            for t in range(1, q):
                v = pow(t, (q - 1) // 6, q); tab[t] = zk.index(v)
            _sext_cache[p] = (tab, rr)
        tab, rr = _sext_cache[p]
        return tab[np.mod(RI + RJ * rr, q)]
    out = np.array([(-1 if (k := sext_exp((int(i), int(j)), p)) is None else k) for i, j in zip(RI, RJ)])
    return out


def sext_vec(p, X, Y):
    return sext_table(p, X, Y)


def main():
    tabp, outp = sys.argv[1], sys.argv[2]
    import random
    rng = random.Random(20261010)
    t0 = time.time()
    res = {'python': sys.version.split()[0], 'numpy': np.__version__}
    build_sup()
    res['cubic_jacobi_vs_factor_based_mismatches'] = check_jacobi(rng)
    log('jacobi check', res['cubic_jacobi_vs_factor_based_mismatches'])
    PH = {}
    for e0 in (0, 2):
        PH[e0] = setup_phi(rng, e0)
        res['Psi0_exp%d' % e0] = {'phi_18_periodicity_failures': PH[e0][3],
                                  'phihat_nonzero': int(sum(abs(v) > 1e-13 for v in PH[e0][2].values()))}
        log('phi', e0, res['Psi0_exp%d' % e0])
    T = np.load(tabp)
    NM = int(T['NM'])
    res['tables'] = {'NM': NM, 'checks[gauss_n,gauss_err,conj_pair_err,tau_n,tau_err,g2_n,g2_err]': [float(v) for v in T['checks']],
                     'dual_entries': int(len(T['N'])), 'lhs_n': int(len(T['lN']))}
    mx, my, Nm = T['mx'], T['my'], T['N']
    am = (mx - 0.5 * my + 1j * (math.sqrt(3) / 2) * my); am = am / np.abs(am)
    dual = {}
    for sg, arr in (('0', T['d0']), ('+', T['dp']), ('-', T['dm'])):
        nz = np.nonzero(arr != 0)[0]
        dual[sg] = dict(idx=nz, w=arr[nz] * am[nz] * 9 / np.sqrt(Nm[nz]), N=Nm[nz], x=mx[nz], y=my[nz])
    lx, ly, lN, lg = T['lx'], T['ly'], T['lN'], T['lg']
    an = (lx - 0.5 * ly + 1j * (math.sqrt(3) / 2) * ly); an = an / np.abs(an)
    # b: primary, prime to 6, N(b)^3 <= NM
    bl = []
    bm = int(round(NM ** (1 / 3))) + 1
    for y in range(-2 * bm, 2 * bm + 1):
        for x in range(-2 * bm, 2 * bm + 1):
            if 0 < norm((x, y)) and norm((x, y)) ** 3 <= NM and is_primary((x, y)) and not divides((2, 0), (x, y)):
                bl.append((x, y))
    res['b_count'] = len(bl)
    # V sharp tables + validation
    vs = {}
    res['vsharp'] = {}
    for name, tf in TESTFNS.items():
        vs[name] = VS(tf)
        chk = []
        for x in (0.003, 0.5, 7.0, 60.0, 400.0):
            sp = complex(vs[name](np.array([x]))[0])
            d2 = complex(vsharp_direct(tf, np.array([math.log(x)]), U=35.0, du=0.01)[0])
            mpq = vsharp_mp(tf, x)
            chk.append({'x': x, 'spline': [sp.real, sp.imag], 'abs(spline-mpmath_MB)': abs(sp - mpq),
                        'abs(trapezoid_refined-mpmath_MB)': abs(d2 - mpq), 'abs_value': abs(mpq)})
        mg = []
        for x in (0.5, 7.0):
            mgv = vsharp_meijer(tf, x)
            mg.append({'x': x, 'abs(spline-meijerG_realspace)': abs(complex(vs[name](np.array([x]))[0]) - mgv), 'abs_value': abs(mgv)})
        res['vsharp'][name] = {'checks_MB': chk, 'checks_meijerG': mg, 'max_abs': vs[name].absmax,
                               'tail_beyond_x=1e3': vs[name].tail_beyond(1e3), 'tail_beyond_x=3e3': vs[name].tail_beyond(3e3)}
        log('vsharp', name, json.dumps(res['vsharp'][name], default=str)[:600])
    # configurations: list of (P, X list)
    p7 = primary((1, 3)) if norm((1, 3)) == 7 else None
    p7 = [p for p in r3.PRIMES if norm(p) == 7]
    p13 = [p for p in r3.PRIMES if norm(p) == 13]
    # (name, Psi_0 exponent e0: Psi_0 = (lambda/.)_3^{e0}, P with exponents, X list)
    configs = [
        ('rho0_P=empty', 0, [], [600, 3000, 20000]),
        ('rho2_P=empty', 2, [], [30, 300, 3000]),
        ('rho2_p7a_j1', 2, [(p7[0], 1)], [300, 3000, 20000]),
        ('rho2_p7a_j0', 2, [(p7[0], 0)], [300, 3000]),
        ('rho2_p7a_j2', 2, [(p7[0], 2)], [300, 3000]),
        ('rho2_p7a_j3', 2, [(p7[0], 3)], [300, 3000]),
        ('rho2_p7a_j4', 2, [(p7[0], 4)], [300, 3000]),
        ('rho2_p7a_j5', 2, [(p7[0], 5)], [300, 3000]),
        ('rho2_p7b_j1', 2, [(p7[1], 1)], [300, 3000]),
        ('rho2_p13a_j1', 2, [(p13[0], 1)], [3000, 20000]),
        ('rho2_p7a_j1_p13a_j1', 2, [(p7[0], 1), (p13[0], 1)], [20000]),
        ('rho0_p7a_j1', 0, [(p7[0], 1)], [10000, 20000]),
        ('rho0_p7a_j4', 0, [(p7[0], 4)], [10000, 20000]),
    ]
    only = os.environ.get('E2E_ONLY')
    res['configs'] = {}
    for cname, e0, cfg, Xs in configs:
        R18, phi, phihat, _ = PH[e0]
        if only and cname not in only.split(','):
            continue
        if os.environ.get('E2E_X'):
            Xs = [float(v) for v in os.environ['E2E_X'].split(',')]
        tc = time.time()
        C = build_config(cfg, R18, phihat, rng)
        d1, wx, g = C['hnf']
        ridx = {sg: res_index(dual[sg]['x'], dual[sg]['y'], d1, wx, g) for sg in dual}
        # Psi on LHS n and b
        psin = np.ones(len(lN), dtype=complex)
        psib = []
        for p, j in cfg:
            k = sext_vec(p, lx, ly)
            psin *= np.where(k < 0, 0, np.exp(1j * math.pi * ((j * k) % 6) / 3))
        for b in bl:
            v = 1 + 0j
            for p, j in cfg:
                v *= chi_pow(b, p, j)
            psib.append(v)
        if e0:
            kl = np.array([SUPL[(int(a) % 9, int(b) % 9)] for a, b in zip(lx, ly)])
            psin *= np.exp(2j * math.pi * ((e0 * kl) % 3) / 3)
            psib = [v * OM ** ((e0 * cubic_jacobi(LAM, b)) % 3) for v, b in zip(psib, bl)]
        lhs_base = an.conjugate() * lg * psin / np.sqrt(lN)
        cres = {'Psi0': '(lambda/.)_3^%d' % e0, 'P': [[list(p), j] for p, j in cfg], 'info': C['info'], 'X': {}}
        log('config', cname, C['info'], 'build %.1fs' % (time.time() - tc))
        for X in Xs:
            for name, tf in TESTFNS.items():
                # LHS
                lhs = 0j
                for b, pb in zip(bl, psib):
                    Nb = norm(b)
                    y = lN * Nb ** 3 / X
                    keep = lN * Nb ** 3 <= NM
                    lhs += alpha(b).conjugate() ** 3 * pb ** 3 / Nb * np.sum(lhs_base[keep] * Vstar(tf, y[keep]))
                lhs_cut = float(np.max(np.abs(Vstar(tf, np.array([NM / X])))))
                # RHS variants
                out = {v: 0j for v in C['variants']}
                absscale = 0.0
                half = {v: 0j for v in C['variants']}
                Ncs = sorted(set(k[2] for k in C['F']))
                for sg in ('0', '+', '-'):
                    dd = dual[sg]
                    for Nc in Ncs:
                        keys = [v for v in C['variants'] if (v, sg, Nc) in C['F']]
                        if not keys:
                            continue
                        xv = dd['N'] * X / (81.0 * Nc * Nc)
                        Vs = vs[name](xv)
                        wv = dd['w'] * Vs
                        hmask = dd['N'] <= NM // 2
                        for v in keys:
                            Fv = C['F'][(v, sg, Nc)][ridx[sg]]
                            term = wv * Fv
                            out[v] += term.sum(); half[v] += term[hmask].sum()
                            if v == 'RHS1':
                                absscale += float(np.abs(term).sum())
                Ncmax = max(Ncs)
                xcut = NM * X / (81.0 * Ncmax ** 2)
                row = {'LHS': [lhs.real, lhs.imag], 'abs_LHS': abs(lhs),
                       'sum_abs_RHS1_terms': absscale,
                       'LHS_weight_at_cut V*(NM/X)': lhs_cut,
                       'dual_x_at_cut': xcut, 'Vsharp_tail_beyond_cut': vs[name].tail_beyond(xcut)}
                for v in C['variants']:
                    row[v] = [out[v].real, out[v].imag]
                    row['relerr_' + v] = abs(out[v] - lhs) / abs(lhs)
                    row['change_NM/2->NM_' + v] = abs(out[v] - half[v]) / abs(lhs)
                cres['X'].setdefault(str(X), {})[name] = row
                log(cname, X, name, 'LHS=%.12g%+.12gi' % (lhs.real, lhs.imag),
                    ' '.join('%s=%.2e' % (v, row['relerr_' + v]) for v in C['variants']))
        cres['seconds'] = round(time.time() - tc, 1)
        res['configs'][cname] = cres
        with open(outp, 'w') as f:
            json.dump(res, f, indent=1, default=str)
    res['seconds'] = round(time.time() - t0, 1)
    with open(outp, 'w') as f:
        json.dump(res, f, indent=1, default=str)
    log('done', res['seconds'])


if __name__ == '__main__':
    main()
