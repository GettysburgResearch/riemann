"""Finite checks for the Sep 30 2026 QRH manuscript (7/8), Prop 5.1 and Lemmas 5.5, 5.7 (reflection engine).

Status: EXPLORATORY review script (companion to reviews/SEP30_REFLECTION_DIFF.md).
Labels: EXACT = residue symbols as integer exponents (big-integer arithmetic in Z[omega]);
        FLOAT = ordinary double precision (not directed, not certified); mpmath at 30 digits for H2.
Source: pr908:standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
        The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex
        (sha256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3), lines 1676-3076.
Reuses (read-only import, file unmodified) reviews/oct5_r3_theta_checks.py and a2/eis.py.

Checks
  S   cub_sym: cubic residue symbol by cubic reciprocity (no factorisation) vs Euler-criterion symbol of R3.
  T   Sep 30 local tables (eq:reflection-local-fourier, the tau^{+-} dictionary, omega_{p,j}, B_p, j = 0..5).
  E2E End-to-end finite arithmetic of Prop 5.1, built exactly as in Sep 30 lines 2063-2245 with L = 18:
      sum over nonzero h_p (lifted h_p = 0 mod M^2) of prod C_{p,j}(h_p) conj kappa(G_h) e(-delta'_h x/(D_F r))
        == conj(kappa_F) vartheta(x) prod chi_p(sigma_p)^{-2} omega_{p,j_p} B_p(x),
      with kappa(G_h) = (c_1/a_1)_3 computed directly (EXACT), all three cusp cases, nonunit h_0, j = 0..5;
      plus the full branch sum with inactive j = 0 primes (factor 1 - q_p^{-1}).
      Controls: conjugate multiplier, no M^2 lift, sign of epsilon_p.
  X   eq:reflection-cross-prime-phase: chi_p(sigma_p)^{-2} omega_{p,j} = xi_{p,j} chi_p(c/p)^{2j+2}; control 2j-2.
  K   whole-index mask (Sep 30 2027-2037): phi(nb^3) prod chi_p(nb^3)^{j_p} = chi_n(lambda)^2 Psi(n) Psi(b)^3 on (nb,S)=1.
  Q   Lemma 5.5 eq:completed-quadratic-zero-mask: chi_k(nb)^3 = chi_k(mh)^3 1_{(k,ct)=1}.
  U   Lemma 5.7: prod_{p|R} B_{p,1}(x_F n b^3) = chi_R(x_F)^3 chi_R(nb)^3.
  D   coefficient support/size table (Sep 30 1957-1964, old-eq:4.3) from DR tau, tau_1, tau_2 (R3 transcription).
  H2  archimedean: Sep 30 Bessel form, reflected Mellin scalar (2389-2398), 3^{-4}K^{-t} identity, Gaussian test, Stirling for R.
Usage: python3 -I sep30_reflection_checks.py OUT.json
"""
import sys, os, math, cmath, json, random, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'a2'))
import oct5_r3_theta_checks as R3          # read-only reuse
import eis
from eis import mul, conj, norm, is_primary, primary, divides, reduce_mod, sym_prime, e_of

LAM, ONE, W1, W2, ZERO = (1, 2), (1, 0), (0, 1), (-1, -1), (0, 0)
TWO = (2, 0)
OM = complex(-0.5, math.sqrt(3) / 2)
add, sub, neg, exact_div, pw = R3.add, R3.sub, R3.neg, R3.exact_div, R3.pw


def zpow(k):            # zeta^k, zeta = e^{i pi/3}
    return cmath.exp(1j * math.pi * (k % 6) / 3)


# ---------------------------------------------------------------- S: cubic symbol by reciprocity
def _lam_table():
    tab = {}
    for p in R3.PRIMES[:600]:
        k = R3.cub_prime(LAM, p)
        key = (p[0] % 9, p[1] % 9)
        if key in tab:
            assert tab[key] == k, ('lambda supplementary law not periodic mod 9', p)
        tab[key] = k
    assert len(tab) == 9, tab
    return tab


LAMTAB = _lam_table()


def cub_sym(a, b):
    """(a/b)_3 as exponent of omega, b prime to lambda (any unit normalisation); None if (a,b) != 1."""
    assert not divides(LAM, b)
    b = primary(b)
    res = 0
    while True:
        if norm(b) == 1:
            return res % 3
        a = reduce_mod(a, b)
        if a == ZERO:
            return None
        while divides(LAM, a):
            a = exact_div(a, LAM)
            res += LAMTAB[(b[0] % 9, b[1] % 9)]
        for m, u in enumerate((ONE, W1, W2)):
            ap = exact_div(a, u)
            if ap[1] % 3 == 0 and ap[0] % 3 in (1, 2):
                break
        else:
            raise RuntimeError(a)
        res += m * (((norm(b) - 1) // 3) % 3)
        if norm(ap) == 1:
            return res % 3
        a, b = b, primary(ap)


def check_S(res):
    rnd = random.Random(3)
    small = [p for p in R3.PRIMES if norm(p) <= 300]
    n = bad = 0
    for _ in range(1500):
        k = rnd.randint(1, 3)
        b = ONE
        for _ in range(k):
            b = mul(b, rnd.choice(small))
        a = (rnd.randint(-60, 60), rnd.randint(-60, 60))
        if a == ZERO:
            continue
        ref = R3.cub_el(a, b)
        got = cub_sym(a, b)
        n += 1
        bad += (ref != got)
    res['S_cubsym_vs_euler'] = {'n': n, 'mismatch': bad}
    print('S', res['S_cubsym_vs_euler'], flush=True)
    assert bad == 0


# ---------------------------------------------------------------- local tables (Sep 30 notation)
class Local:
    def __init__(self, p):
        self.p = p
        self.R, self.N = eis.residues(p)
        self.q = self.N
        self.inv = {x: R3.inv_mod(x, p) for x in self.R if not divides(p, x)}
        self._tau = {}

    def chi(self, x, j):
        """chi_p(x)^j with zero extension."""
        k = sym_prime(x, self.p)
        return 0j if k is None else zpow(j * k)

    def tau(self, m, sign):
        if (m % 6, sign) not in self._tau:
            self._tau[(m % 6, sign)] = sum(self.chi(y, m) * e_of(y if sign > 0 else neg(y), self.p)
                                           for y in self.R) / math.sqrt(self.q)
        return self._tau[(m % 6, sign)]

    def C(self, j):
        out = {}
        for h in self.R:
            out[h] = sum(self.chi(y, j) * e_of(neg(mul(h, y)), self.p) for y in self.R) / self.q
        return out

    def omega(self, j, eps):
        if j % 6 not in (0, 4):
            return self.tau(j, -1) * self.tau((j + 2) % 6, +1) * self.chi(eps, -j - 2)
        if j % 6 == 4:
            return self.tau(4, -1)
        return -self.tau(2, +1) * self.chi(eps, -2)

    def B(self, j, x):
        if j % 6 not in (0, 4):
            return self.chi(x, -j - 2)
        if j % 6 == 4:
            return self.q ** -0.5 * (-1 + (self.q if divides(self.p, x) else 0))
        return self.q ** -0.5 * self.chi(x, -2)


def check_T(res, locs):
    """eq:reflection-local-fourier with tau^-, tau^{+-} vs gamma_j, |tau| = 1, local transform j=0..5."""
    w_four = w_dict = w_mod = w_tr = 0.0
    rnd = random.Random(5)
    for L in locs:
        p, q = L.p, L.q
        gam = {j: eis.gamma(j, [p]) for j in range(1, 6)}
        for m in range(1, 6):
            tp, tm = L.tau(m, +1), L.tau(m, -1)
            w_dict = max(w_dict, abs(tp - gam[m]), abs(tm - L.chi(neg(ONE), m) * gam[m]))
            w_mod = max(w_mod, abs(abs(tp) - 1), abs(abs(tm) - 1))
        nz = [x for x in L.R if not divides(p, x)]
        for j in range(6):
            C = L.C(j)
            for h in L.R:
                if j != 0:
                    pred = 0j if divides(p, h) else q ** -0.5 * L.tau(j, -1) * L.chi(h, -j)
                else:
                    pred = (1 - 1 / q) if divides(p, h) else -1 / q
                w_four = max(w_four, abs(C[h] - pred))
            for _ in range(2):
                sig, eps = rnd.choice(nz), rnd.choice(nz)
                for x in L.R:
                    # a = sigma_p h_p mod p, conj multiplier chi_p(a)^{-2}
                    lhs = sum(C[h] * L.chi(mul(sig, h), -2) * e_of(mul(eps, mul(L.inv[h], x)), p) for h in nz)
                    rhs = L.chi(sig, -2) * L.omega(j, eps) * L.B(j, x)
                    w_tr = max(w_tr, abs(lhs - rhs))
    res['T_local_tables'] = {'primes': [L.p for L in locs], 'norms': [L.q for L in locs],
                             'max_err_local_fourier': w_four, 'max_err_tau_vs_gamma_dictionary': w_dict,
                             'max_abs(|tau|-1)': w_mod, 'max_err_local_transform_j0to5': w_tr}
    print('T', res['T_local_tables'], flush=True)


# ---------------------------------------------------------------- E2E: exact Sep 30 construction
LBIG = (18, 0)                       # (18) | L, prime support S = {lambda, 2}
VQ_L = {'lam': 4, 'two': 1}          # 18 = -lambda^4 * (-2)
VQ_M = {'lam': 12 + 4 * VQ_L['lam'], 'two': 4 * VQ_L['two']}     # M = lambda^12 L^4
M_EL = mul(pw(LAM, 12), pw(LBIG, 4))
M2 = mul(M_EL, M_EL)
QEL = {'lam': LAM, 'two': (-2, 0)}


def val(x, q):
    v = 0
    while x != ZERO and divides(q, x):
        x = exact_div(x, q); v += 1
    return v


def reduced_fraction(h0):
    num = mul(mul(LAM, LAM), h0)
    if num == ZERO:
        aF, cF = ZERO, ONE
    else:
        g = R3.egcd(num, LBIG)[0]
        aF, cF = exact_div(num, g), exact_div(LBIG, g)
    for u in eis.UNITS:
        a2, c2 = mul(u, aF), mul(u, cF)
        if divides(LAM, cF):
            if is_primary(a2):
                return a2, c2
        elif is_primary(c2):
            return a2, c2
    raise RuntimeError(h0)


def build_term(aF, cF, act, hs, lift=True):
    """Sep 30 (eq:reflection-cusp-fraction) and the delta', H, G construction (lines 2063-2181)."""
    r = ONE
    for p in act:
        r = mul(r, p)
    a = mul(aF, r)
    for p, h in zip(act, hs):
        hh = R3.crt(h, p, ZERO, M2) if lift else h
        a = add(a, mul(mul(mul(LAM, LAM), cF), mul(exact_div(r, p), hh)))
    c = mul(cF, r)
    assert norm(R3.egcd(a, c)[0]) == 1, 'fraction not reduced'
    cong = []
    for nm, qel in QEL.items():
        e = val(cF, qel)
        if e > 0:
            mod = pw(qel, VQ_M[nm] + e); cong.append((R3.inv_mod(a, mod), mod))
        else:
            mod = pw(qel, VQ_M[nm]); cong.append((ZERO, mod))
    cong.append((R3.inv_mod(a, r), r))
    dp, mod = cong[0]
    for x2, m2 in cong[1:]:
        dp = R3.crt(dp, mod, x2, m2); mod = mul(mod, m2)
    bg = exact_div(sub(mul(a, dp), ONE), c)
    g = ((a, bg), (c, dp))
    vl = val(c, LAM)
    u0 = None
    if vl >= 2:
        H = ((ONE, ZERO), (ZERO, ONE)); cusp = 0
    elif vl == 1:
        u0 = next(u for u in (LAM, neg(LAM)) if divides((3, 0), sub(u, c)))
        H = ((ONE, ZERO), (u0, ONE)); cusp = 1 if u0 == LAM else 2      # Theta_1 = F_19, Theta_2 = F_10
    else:
        u0 = next((s, t) for s in range(3) for t in range(3) if divides((3, 0), sub((s, t), a)))
        H = ((u0, neg(ONE)), (ONE, ZERO)); cusp = u0[1]
    G = R3.mmul(g, R3.minv(H))
    assert R3.cong_I_mod3(G), G
    a1, c1 = G[0][0], G[1][0]
    kap = 0 if c1 == ZERO else cub_sym(c1, a1)
    # Sep 30 kappa_F formula (three cases)
    if vl >= 2:
        kF = cub_sym(cF, a)
    elif vl == 1:
        A = sub(a, mul(u0, bg))
        kF = (cub_sym(neg(u0), A) + cub_sym(exact_div(cF, u0), a)) % 3
    else:
        kF = 0 if norm(cF) == 1 else cub_sym(a, cF)
    k_ar = sum(cub_sym(a, p) for p in act) % 3              # (a/r)_3 = prod chi_p(a)^2
    DF = mul(pw(LAM, 3), cF)
    return {'a': a, 'c': c, 'r': r, 'dp': dp, 'kap': kap, 'kF': kF, 'k_ar': k_ar, 'vl': vl, 'cusp': cusp,
            'DF': DF, 'dpF': reduce_mod(dp, DF)}


def check_E2E(res, locs_by_p, rng_seed=17):
    rnd = random.Random(rng_seed)
    P2 = [locs_by_p[(2, 1)], locs_by_p[(2, -3)]]            # norms 7, 13
    P3 = P2 + [locs_by_p[(5, 0)]]                           # + inert 5 (norm 25)
    h0s = [ONE, LAM, mul(LAM, LAM), TWO, mul(TWO, LAM), mul(TWO, mul(LAM, LAM)), ZERO, (4, 5), (7, -3)]
    xs = [(rnd.randint(-400, 400), rnd.randint(-400, 400)) for _ in range(110)]
    xs += [mul(P2[0].p, (rnd.randint(-30, 30), rnd.randint(-30, 30))) for _ in range(15)]
    xs += [mul(P2[1].p, (rnd.randint(-30, 30), rnd.randint(-30, 30))) for _ in range(15)]
    xs += [mul(mul(P2[0].p, P2[1].p), (rnd.randint(-9, 9), rnd.randint(-9, 9))) for _ in range(8)]
    xs += [mul(P3[2].p, (rnd.randint(-9, 9), rnd.randint(-9, 9))) for _ in range(8)]
    Ccache = {}

    def Cl(L, j):
        if (L.p, j) not in Ccache:
            Ccache[(L.p, j)] = L.C(j)
        return Ccache[(L.p, j)]

    out = {'cases_seen': {}, 'kappa_direct_eq_formula': [0, 0], 'kappaF_constant': True, 'dpF_constant': True,
           'max_err_active': 0.0, 'n_active_identities': 0, 'max_err_branch_sum': 0.0, 'n_branch_identities': 0,
           'ctrl_conj_multiplier_min_maxerr': 9.0, 'ctrl_no_lift_nonconstant_kappaF_or_deltaF_terms': 0, 'ctrl_no_lift_min_maxerr': 9.0,
           'ctrl_eps_sign_min_maxerr': 9.0}
    term_cache = {}

    def terms(aF, cF, act, lift=True):
        key = (aF, cF, tuple(L.p for L in act), lift)
        if key in term_cache:
            return term_cache[key]
        nzs = [[x for x in L.R if not divides(L.p, x)] for L in act]
        tl = []

        def rec(i, cur):
            if i == len(act):
                tl.append((tuple(cur), build_term(aF, cF, [L.p for L in act], cur, lift))); return
            for h in nzs[i]:
                rec(i + 1, cur + [h])
        rec(0, [])
        term_cache[key] = tl
        return tl

    def rhs_active(aF, cF, act, js, tl, x, eps_sign=1):
        t0 = tl[0][1]
        c, r, DF = t0['c'], t0['r'], t0['DF']
        val_ = OM ** (-t0['kF'])
        val_ *= e_of(neg(mul(mul(t0['dpF'], R3.inv_mod(r, DF)), x)), DF)          # vartheta(x)
        for L, j in zip(act, js):
            p = L.p
            cp = exact_div(c, p)
            sig = mul(mul(LAM, LAM), cp)
            eps = neg(R3.inv_mod(mul(mul(pw(LAM, 3), cp), sig), p))
            if eps_sign < 0:
                eps = neg(eps)
            val_ *= L.chi(sig, -2) * L.omega(j, eps) * L.B(j, x)
        return val_

    def lhs_active(act, js, tl, x, conj_mult=True):
        s = 0j
        for hs, t in tl:
            co = 1 + 0j
            for L, j, h in zip(act, js, hs):
                co *= Cl(L, j)[h]
            if co == 0:
                continue
            kap = OM ** (-t['kap']) if conj_mult else OM ** (t['kap'])
            s += co * kap * e_of(neg(mul(t['dp'], x)), mul(t['DF'], t['r']))
        return s

    for h0 in h0s:
        aF, cF = reduced_fraction(h0)
        for P, jlist in [(P2, [(j1, j2) for j1 in range(6) for j2 in range(6)]),
                         (P3, [(1, 1, 1), (4, 0, 2), (0, 0, 5), (3, 4, 1), (0, 4, 0), (5, 2, 3)] if h0 in h0s[:6] else [])]:
            xs_use = xs if len(P) == 2 else xs[:24] + xs[110:126]
            # ---- all-active identity for every subset containing the nonzero exponents
            for js in jlist:
                act_need = [L for L, j in zip(P, js) if j != 0]
                zero_ps = [L for L, j in zip(P, js) if j == 0]
                subsets = []
                for mask in range(1 << len(zero_ps)):
                    extra = [L for i, L in enumerate(zero_ps) if mask >> i & 1]
                    subsets.append([L for L in P if L in act_need or L in extra])
                branch_rhs = {}
                for act in subsets:
                    if not act:
                        continue
                    tl = terms(aF, cF, act)
                    jsa = [js[P.index(L)] for L in act]
                    for _, t in tl:
                        out['kappa_direct_eq_formula'][1] += 1
                        if t['kap'] == (t['kF'] + t['k_ar']) % 3:
                            out['kappa_direct_eq_formula'][0] += 1
                        if t['kF'] != tl[0][1]['kF']:
                            out['kappaF_constant'] = False
                        if t['dpF'] != tl[0][1]['dpF']:
                            out['dpF_constant'] = False
                        out['cases_seen'][str(min(t['vl'], 2)) + '/cusp' + str(t['cusp'])] = 1
                    errs = []
                    for x in xs_use:
                        l_ = lhs_active(act, jsa, tl, x)
                        r_ = rhs_active(aF, cF, act, jsa, tl, x)
                        errs.append(abs(l_ - r_))
                        branch_rhs.setdefault(x, 0j)
                        inact = 1.0
                        for L in P:
                            if L not in act:
                                inact *= (1 - 1 / L.q)
                        branch_rhs[x] += inact * r_
                    out['max_err_active'] = max(out['max_err_active'], max(errs)); out['n_active_identities'] += 1
                    # controls on a few configurations
                    if len(act) == 2 and js[:2] in [(1, 1), (1, 2), (3, 5), (2, 0)]:
                        e_conj = max(abs(lhs_active(act, jsa, tl, x, conj_mult=False) - rhs_active(aF, cF, act, jsa, tl, x)) for x in xs[:40])
                        out['ctrl_conj_multiplier_min_maxerr'] = min(out['ctrl_conj_multiplier_min_maxerr'], e_conj)
                        e_eps = max(abs(lhs_active(act, jsa, tl, x) - rhs_active(aF, cF, act, jsa, tl, x, eps_sign=-1)) for x in xs[:40])
                        out['ctrl_eps_sign_min_maxerr'] = min(out['ctrl_eps_sign_min_maxerr'], e_eps)
                        tl_nl = terms(aF, cF, act, lift=False)
                        out['ctrl_no_lift_nonconstant_kappaF_or_deltaF_terms'] += sum(1 for _, t in tl_nl if t['kF'] != tl_nl[0][1]['kF'] or t['dpF'] != tl_nl[0][1]['dpF'])
                        e_nl = max(abs(lhs_active(act, jsa, tl_nl, x) - rhs_active(aF, cF, act, jsa, tl, x)) for x in xs[:40])
                        out['ctrl_no_lift_min_maxerr'] = min(out['ctrl_no_lift_min_maxerr'], e_nl)
                # ---- full branch sum over all h (zero frequencies included), only when some j_p = 0
                if zero_ps and len(P) == 2:
                    for x in xs[:60]:
                        s = 0j
                        for hs in [(h1, h2) for h1 in P[0].R for h2 in P[1].R]:
                            co = Cl(P[0], js[0])[hs[0]] * Cl(P[1], js[1])[hs[1]]
                            if co == 0:
                                continue
                            act = [L for L, h in zip(P, hs) if not divides(L.p, h)]
                            if not act:
                                # r = 1: translate by lambda^2 h_0/L only
                                tl0 = terms(aF, cF, [])
                                t = tl0[0][1]
                            else:
                                tl = terms(aF, cF, act)
                                hh = tuple(h for L, h in zip(P, hs) if L in act)
                                t = dict(tl)[hh]
                            s += co * OM ** (-t['kap']) * e_of(neg(mul(t['dp'], x)), mul(t['DF'], t['r']))
                        # empty active set branch (all j = 0, all inactive): scalar prod(1-1/q) * conj kappa_F vartheta
                        if all(j == 0 for j in js):
                            t = terms(aF, cF, [])[0][1]
                            br0 = (1 - 1 / P[0].q) * (1 - 1 / P[1].q) * OM ** (-t['kF']) * e_of(neg(mul(t['dpF'], x)), t['DF'])
                        else:
                            br0 = 0j
                        out['max_err_branch_sum'] = max(out['max_err_branch_sum'], abs(s - branch_rhs[x] - br0))
                    out['n_branch_identities'] += 1
        print('E2E h0', h0, 'aF/cF', aF, cF, 'max_err_active', out['max_err_active'], flush=True)
    res['E2E'] = out
    print('E2E', {k: v for k, v in out.items()}, flush=True)


# ---------------------------------------------------------------- X: cross-prime phase
def check_X(res, locs):
    spread = 0.0; spread_ctrl = 0.0; exact_eps = 0
    for L in locs:
        p = L.p
        nz = [x for x in L.R if not divides(p, x)]
        for j in range(6):
            rat, rat_c = [], []
            for cp in nz:
                sig = mul(mul(LAM, LAM), cp)
                eps = neg(R3.inv_mod(mul(mul(pw(LAM, 3), cp), sig), p))
                eps2 = neg(R3.inv_mod(mul(pw(LAM, 5), mul(cp, cp)), p))
                exact_eps += divides(p, sub(eps, eps2))
                phi = L.chi(sig, -2) * L.omega(j, eps)
                rat.append(phi / L.chi(cp, 2 * j + 2))
                rat_c.append(phi / L.chi(cp, 2 * j - 2))
            spread = max(spread, max(abs(z - rat[0]) for z in rat))
            spread_ctrl = max(spread_ctrl, max(abs(z - rat_c[0]) for z in rat_c))
    res['X_cross_prime_phase'] = {'max_spread_ratio_2j+2': spread, 'ctrl_max_spread_2j-2': spread_ctrl,
                                  'eps_equals_-lam^-5(c/p)^-2_count': exact_eps}
    print('X', res['X_cross_prime_phase'], flush=True)


# ---------------------------------------------------------------- exact symbol helpers on factor lists
def chi_list(R_list, x, j=1):
    """chi_R(x)^j for squarefree R = prod R_list: (zero?, exponent mod 6)."""
    e = 0
    for p in R_list:
        k = sym_prime(x, p)
        if k is None:
            return None
        e += k
    return (j * e) % 6


def check_K(res):
    """whole-index mask with zero extensions, shared primes allowed."""
    rnd = random.Random(23)
    good = [p for p in R3.PRIMES if 7 <= norm(p) <= 100]
    n_ok = n_tot = ctrl_fail = n_shared = 0
    for _ in range(1500):
        P = rnd.sample(good, 3); js = [rnd.randint(0, 5) for _ in P]
        pool = good[:8] + P + [(-2, 0)] * (1 if rnd.random() < 0.1 else 0)
        nf = list({rnd.choice(pool) for _ in range(rnd.randint(1, 3))})
        bf = [rnd.choice(pool) for _ in range(rnd.randint(0, 3))]
        n = R3.prod(nf); b = R3.prod(bf)
        if (-2, 0) in nf or (-2, 0) in bf:
            continue                                        # zero branch (nb,S) != 1: coefficient is 0 by definition
        n_shared += bool(set(nf) & set(bf))
        x = mul(n, pw(b, 3))
        # LHS: phi(nb^3) prod chi_p(nb^3)^{j_p}, phi(x) = (lambda/x)_3 for x primary prime to S (Psi_0 = 1)
        lz = any(divides(p, x) for p in P)
        lhs = 0j if lz else OM ** cub_sym(LAM, x) * zpow(sum(j * sym_prime(x, p) for p, j in zip(P, js)))

        def Psi(y, zero_ext=True):
            v = 1 + 0j
            for p, j in zip(P, js):
                k = sym_prime(y, p)
                if k is None:
                    if j == 0 and not zero_ext:
                        continue
                    return 0j
                v *= zpow(j * k)
            return v
        rhs = OM ** cub_sym(LAM, n) * Psi(n) * Psi(b) ** 3
        rhs_c = OM ** cub_sym(LAM, n) * Psi(n, False) * Psi(b, False) ** 3
        n_tot += 1; n_ok += abs(lhs - rhs) < 1e-12; ctrl_fail += abs(lhs - rhs_c) > 1e-9
    res['K_whole_index_mask'] = {'n': n_tot, 'agree': n_ok, 'with_shared_n_b_primes': n_shared,
                                 'ctrl_no_zero_extension_at_j0_failures': ctrl_fail}
    print('K', res['K_whole_index_mask'], flush=True)


def check_Q(res):
    """Lemma 5.5: chi_k(nb)^3 = chi_k(mh)^3 1_{(k,ct)=1}, b = g t^2, c = (n,g), n = cm, g = ch."""
    rnd = random.Random(29)
    pool = [p for p in R3.PRIMES if 7 <= norm(p) <= 61]
    n_ok = n_tot = ctrl_fail = coll = 0
    for _ in range(3000):
        kf = list(set(rnd.sample(pool, rnd.randint(1, 3))))
        nf = list(set(rnd.sample(pool + [(-2, 0)], rnd.randint(0, 3))))
        gf = list(set(rnd.sample(pool + [(-2, 0)], rnd.randint(0, 3))))
        tf = [rnd.choice(pool + [(-2, 0)]) for _ in range(rnd.randint(0, 2))]
        cf = [p for p in nf if p in gf]; mf = [p for p in nf if p not in cf]; hf = [p for p in gf if p not in cf]
        n = R3.prod(nf); b = mul(R3.prod(gf), pw(R3.prod(tf), 2)) if tf else R3.prod(gf)
        e = chi_list(kf, mul(n, b), 3)
        lhs = 0 if e is None else zpow(e)
        e2 = chi_list(kf, mul(R3.prod(mf), R3.prod(hf)), 3)
        mask = all(p not in kf for p in cf + tf)
        rhs = 0 if (e2 is None or not mask) else zpow(e2)
        rhs_c = 0 if e2 is None else zpow(e2)
        coll += not mask
        n_tot += 1; n_ok += abs(lhs - rhs) < 1e-12; ctrl_fail += abs(lhs - rhs_c) > 1e-9
    res['Q_lemma55_zero_mask'] = {'n': n_tot, 'agree': n_ok, 'with_collision_(k,ct)>1': coll,
                                  'ctrl_without_mask_failures': ctrl_fail}
    print('Q', res['Q_lemma55_zero_mask'], flush=True)


def check_U(res):
    """Lemma 5.7: prod_{p|R} B_{p,1}(x_F n b^3) = chi_R(x_F)^3 chi_R(nb)^3 (zeros included)."""
    rnd = random.Random(31)
    pool = [p for p in R3.PRIMES if 7 <= norm(p) <= 61]
    n_ok = n_tot = ctrl_fail = 0
    for _ in range(3000):
        Rf = list(set(rnd.sample(pool, rnd.randint(1, 3))))
        u = rnd.choice(eis.UNITS); k = rnd.randint(-4, 6)
        NF = R3.prod(list(set(rnd.sample(pool, rnd.randint(0, 2))))); BF = R3.prod([rnd.choice(pool) for _ in range(rnd.randint(0, 1))])
        xF = mul(mul(u, pw(LAM, k + 4)), mul(NF, pw(BF, 3)))
        n = R3.prod(list(set(rnd.sample(pool, rnd.randint(0, 2))))); b = R3.prod([rnd.choice(pool) for _ in range(rnd.randint(0, 2))])
        x = mul(xF, mul(n, pw(b, 3)))
        lhs = 1 + 0j
        for p in Rf:
            kk = sym_prime(x, p)
            lhs *= 0 if kk is None else zpow(-3 * kk)
        e1, e2 = chi_list(Rf, xF, 3), chi_list(Rf, mul(n, b), 3)
        rhs = 0 if (e1 is None or e2 is None) else zpow(e1 + e2)
        lhs_c = 1 + 0j                                   # control: conjugate convention B = chi^{-j+2} = chi^{1}
        for p in Rf:
            kk = sym_prime(x, p)
            lhs_c *= 0 if kk is None else zpow(kk)
        n_tot += 1; n_ok += abs(lhs - rhs) < 1e-12; ctrl_fail += abs(lhs_c - rhs) > 1e-9
    res['U_lemma57_quadratic_factor'] = {'n': n_tot, 'agree': n_ok, 'ctrl_sextic_B_failures': ctrl_fail}
    print('U', res['U_lemma57_quadratic_factor'], flush=True)


# ---------------------------------------------------------------- D: coefficient support/size table
def check_D(res, Nmax):
    ymax = int(math.sqrt(4 * Nmax / 3)) + 2
    worst = {'0': 0.0, '+': 0.0, '-': 0.0}
    mags = {'0': set(), '+': set(), '-': set()}
    support_viol = 0; cnt = 0
    for y in range(-ymax, ymax + 1):
        for x in range(-ymax - abs(y), ymax + abs(y) + 1):
            if x * x - x * y + y * y > Nmax or (x, y) == (0, 0):
                continue
            nu = (x, y)
            vals = {}
            if divides(LAM, nu):
                vals['0'] = R3.tau_nu3(exact_div(nu, LAM))
            vals['+'] = R3.tau12_nu4(mul(W1, nu), 2)
            vals['-'] = R3.tau12_nu4(mul(W2, nu), 1)
            u, e, fac = R3.factor(nu)
            k = e - 4                                        # mu = nu / lambda^4 = u lambda^k n b^3
            ok_shape = all(v % 3 in (0, 1) for v in fac.values()) and k >= -4
            bnorm = 1
            for p, v in fac.items():
                bnorm *= norm(p) ** (v // 3)
            for s, t in vals.items():
                if abs(t) < 1e-12:
                    continue
                cnt += 1
                if not ok_shape:
                    support_viol += 1; continue
                ratio = abs(t) / (27 * 3 ** (k / 6) * math.sqrt(bnorm))
                worst[s] = max(worst[s], ratio)
                mags[s].add(round(math.log(abs(t) / math.sqrt(bnorm), 3) - k / 6, 6) if s == '0' else (k, round(abs(t) / math.sqrt(bnorm), 6)))
    res['D_coefficients'] = {'Nmax_nu': Nmax, 'nonzero': cnt, 'support_violations': support_viol,
                             'max_|d|/(27*3^{k/6}|b|)': worst,
                             'tau: log_3(|d|/|b|) - k/6 values': sorted(mags['0']),
                             'tau_1,tau_2: (k, |d|/|b|)': sorted(mags['+'] | mags['-'])}
    print('D', res['D_coefficients'], flush=True)


# ---------------------------------------------------------------- H2: archimedean bookkeeping in Sep 30 form
def check_H2(res):
    import mpmath as mp
    mp.mp.dps = 30
    out = {}
    w = mp.mpc('2.6', '0.5')
    lhs = mp.quad(lambda y: mp.besselk(mp.mpf(1) / 3, y) * y ** (w - 1), [0, 1, mp.inf])
    rhs = 2 ** (w - 2) * mp.gamma((w - mp.mpf(1) / 3) / 2) * mp.gamma((w + mp.mpf(1) / 3) / 2)
    out['bessel_form_relerr'] = float(abs(lhs - rhs) / abs(rhs))
    # reflected Mellin scalar: -2 pi i c^{-2} q_c^{2-2s} mu int u^{2-2s} K(4 pi|mu|u) du
    #   == -(i/4)(2pi)^{2s-2} conj(alpha(c))^2 q_c^{1-2s} Gamma(4/3-s)Gamma(5/3-s) alpha(mu) q_mu^{-(1-s)}
    errs = []
    for (s, c, mu) in [(mp.mpc('-0.4', '0.9'), mp.mpc('2', '1.3'), mp.mpc('0.31', '-0.52')),
                       (mp.mpc('-1.2', '-2.0'), mp.mpc('-1.5', '4'), mp.mpc('-0.9', '0.2'))]:
        qc, qm = abs(c) ** 2, abs(mu) ** 2
        I = mp.quad(lambda u: u ** (2 - 2 * s) * mp.besselk(mp.mpf(1) / 3, 4 * mp.pi * abs(mu) * u), [0, 1, mp.inf])
        L_ = -2j * mp.pi * c ** -2 * qc ** (2 - 2 * s) * mu * I
        R_ = (-1j / 4) * (2 * mp.pi) ** (2 * s - 2) * mp.conj(c / abs(c)) ** 2 * qc ** (1 - 2 * s) \
            * mp.gamma(mp.mpf(4) / 3 - s) * mp.gamma(mp.mpf(5) / 3 - s) * (mu / abs(mu)) * qm ** (-(1 - s))
        errs.append(float(abs(L_ - R_) / abs(R_)))
    out['reflected_mellin_scalar_relerr'] = max(errs)
    # (2pi)^{4s-2} 27^{-s} 3^{-5/2} = 3^{-4} K^{-t}, t = 1/2 - s
    K = (2 * mp.pi) ** 4 / 27
    e3 = []
    for s in [mp.mpc('-0.7', '1.1'), mp.mpc('0.2', '-3')]:
        t = mp.mpf(1) / 2 - s
        e3.append(float(abs((2 * mp.pi) ** (4 * s - 2) * mp.mpf(27) ** (-s) * mp.mpf(3) ** (-2.5) - mp.mpf(3) ** -4 * K ** (-t))))
    out['scale_identity_abserr'] = max(e3)
    # Gaussian test V(x) = (2 sqrt pi)^{-1} exp(-(log x)^2/4): Mellin e^{t^2}
    t = mp.mpc('0.3', '0.7')
    G = mp.quad(lambda u: mp.exp(-u ** 2 / 4 + t * u), [-mp.inf, 0, mp.inf]) / (2 * mp.sqrt(mp.pi))
    out['gaussian_mellin_relerr'] = float(abs(G - mp.exp(t ** 2)) / abs(mp.exp(t ** 2)))
    # R(t) = prod_{+-} Gamma(1+t+-1/6)/Gamma(1-t+-1/6) equals the Oct 5 quotient; |R(sigma+iu)| (1+|u|)^{-4 sigma} bounded
    Rf = lambda z: mp.gamma(mp.mpf(7) / 6 + z) * mp.gamma(mp.mpf(5) / 6 + z) / (mp.gamma(mp.mpf(7) / 6 - z) * mp.gamma(mp.mpf(5) / 6 - z))
    st = {}
    for sg in [-0.25, 0.0, 1.0, 3.0]:
        vals = [float(abs(Rf(mp.mpc(sg, u))) / (1 + u) ** (4 * sg)) for u in (0.0, 1.0, 10.0, 100.0, 1000.0, 10000.0)]
        st[str(sg)] = [round(v, 4) for v in vals]
    out['stirling_|R|/(1+|u|)^{4sigma}_u=0,1,10,1e2,1e3,1e4'] = st
    res['H2_archimedean'] = out
    print('H2', out, flush=True)


def main():
    outp = sys.argv[1]
    t = time.time()
    res = {'python': sys.version.split()[0]}
    check_S(res)
    test_primes = [p for p in R3.PRIMES if 7 <= norm(p) <= 43 and p[1] != 0] + [primary((5, 0)), primary((11, 0))]
    locs = [Local(p) for p in test_primes]
    by_p = {L.p: L for L in locs}
    check_T(res, locs)
    check_X(res, locs)
    check_K(res)
    check_Q(res)
    check_U(res)
    p7 = next(L for L in locs if L.q == 7); p13 = next(L for L in locs if L.q == 13); p25 = next(L for L in locs if L.q == 25)
    check_E2E(res, {(2, 1): p7, (2, -3): p13, (5, 0): p25})
    check_D(res, 6000)
    check_H2(res)
    res['seconds'] = round(time.time() - t, 1)
    with open(outp, 'w') as f:
        json.dump(res, f, indent=1, default=str)
    print('done', res['seconds'])


if __name__ == '__main__':
    main()
