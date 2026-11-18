# s5_cube_inversion_checks.py -- Level-2 audit of Section 5 of
# "The Quasi-Riemann Hypothesis" (paper2.tex, l.1254-1631).
# Written from scratch for this audit; no code from the OpenAI repository is used or run.
#
# What is checked (all identities are EXACT algebraic identities, so any weight W works;
# we use a smooth bump to stay close to the paper):
#   C1  (eq:cube-inverse) l.1361-1369: Moebius inversion over the cube index,
#       X^{-1/2} sum*_n a(n) Psi_k(n) W(N n/X)
#         = sum_{(h,S)=1} mu(h) conj(alpha(h))^3 Psi_k(h)^3 / N(h) * T(X/N(h)^3; k, f),
#       with T from (eq:T) l.1287-1293 and Psi_k from (eq:completed-twist) l.1304-1308.
#       Run (a) with the genuine coefficients a(n)=conj(alpha(n)) gamma_2(n) xi(n) at moderate X,
#       and (b) with random unimodular n-coefficients at large X, so that non-squarefree cube
#       indices b (N(b)=49) and composite h occur.  (The identity is formal in the n-coefficients.)
#   C2  the long-part regrouping l.1408-1428: for several cutoffs H_c,
#       P_long(k,f) [definition via h > H_c] equals
#       sum_{N(b)>H_c} beta_0(b,f) chi_b(k)^3 / N(b) * L_b^{-1/2} sum*_n a(n)Psi_k(n) W(N n/L_b),
#       and |beta_0(b,f)| <= tau_div(b).
#   C3  Psi_k(b)^3 = xi(b)^3 chi_b(k)^3 1_{(b,f)=1} for non-squarefree b (l.1415).
#   C4  Prop. 5.2 reduction l.2193-2199: chi_n(u0 s v^2) chi_n(f)^4 = chi_n(u0 s) chi_n(f v^2)^4
#       for primes n (hence for all n by complete multiplicativity), including v divisible by
#       the S-primes 2 and lambda, and T(X; u0 s v^2, f) = T(X; u0 s, f v^2).
#   C5  CRT multiplicativity of gamma_2 used to build composite Gauss sums in C1(a), checked
#       against direct evaluation.
import math, cmath, random, sys
import numpy as np

SQ3 = math.sqrt(3.0)
OMEGA = complex(-0.5, SQ3 / 2)
Z6 = cmath.exp(2j * math.pi / 6)

def cv(x): return x[0] + x[1] * OMEGA
def mul(x, y):
    a, b = x; c, d = y
    return (a * c - b * d, a * d + b * c - b * d)
def sub(x, y): return (x[0] - y[0], x[1] - y[1])
def conj(x): return (x[0] - x[1], -x[1])
def norm(x): return x[0] * x[0] - x[0] * x[1] + x[1] * x[1]
def divides(d, x):
    n = norm(d); z = mul(x, conj(d)); return z[0] % n == 0 and z[1] % n == 0
def prod(xs):
    r = (1, 0)
    for x in xs: r = mul(r, x)
    return r
UNIT = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]   # zeta_6^k, zeta_6 = 1+omega
for _k in range(6): assert abs(cv(UNIT[_k]) - Z6 ** _k) < 1e-12
def is_primary(x): return (x[0] - 1) % 3 == 0 and x[1] % 3 == 0
def make_primary(x):
    for u in UNIT:
        y = mul(u, x)
        if is_primary(y): return y
    raise ValueError(x)
def rmod(x, m):
    n = norm(m); z = mul(x, conj(m))
    q = (round(z[0] / n), round(z[1] / n))
    best = None
    for da in (-1, 0, 1):
        for db in (-1, 0, 1):
            r = sub(x, mul((q[0] + da, q[1] + db), m))
            if best is None or norm(r) < norm(best): best = r
    return best
def powmod(x, e, m):
    r = (1, 0); x = rmod(x, m)
    while e:
        if e & 1: r = rmod(mul(r, x), m)
        x = rmod(mul(x, x), m); e >>= 1
    return r

class Prime:
    """primary prime of O not dividing 6, with a fast sextic-symbol routine"""
    def __init__(self, pi):
        self.pi = pi; self.N = norm(pi)
        a, b = pi
        if self.N % 3 == 1 and b % self.N != 0 and math.gcd(b, self.N) == 1:   # split: O/pi = F_p
            p = self.N
            self.split = True; self.p = p
            self.w0 = (-a * pow(b, -1, p)) % p          # omega = -a/b mod pi
            assert (self.w0 * self.w0 + self.w0 + 1) % p == 0
            self.units = {(u[0] + u[1] * self.w0) % p: k for k, u in enumerate(UNIT)}
        else:
            self.split = False
    def sym(self, x):
        """(x/pi)_6 as exponent k (value zeta_6^k), or None if pi | x"""
        if self.split:
            p = self.p; y = (x[0] + x[1] * self.w0) % p
            if y == 0: return None
            return self.units[pow(y, (p - 1) // 6, p)]
        if divides(self.pi, x): return None
        r = powmod(x, (self.N - 1) // 6, self.pi)
        for k, u in enumerate(UNIT):
            if divides(self.pi, sub(r, u)): return k
        raise ValueError
def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]: s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]
def prime_list(maxnorm):
    out = []
    for p in primes_upto(maxnorm):
        if p in (2, 3): continue                      # 2 and lambda are in S
        if p % 3 == 1:
            found = None
            for b in range(1, int(2 * math.sqrt(p / 3)) + 2):
                disc = 4 * p - 3 * b * b
                if disc < 0: break
                s = math.isqrt(disc)
                if s * s == disc and (b + s) % 2 == 0:
                    found = ((b + s) // 2, b); break
            assert found and norm(found) == p
            pi1 = make_primary(found); pi2 = make_primary(conj(found))
            out += [Prime(pi1), Prime(pi2)]
        elif p * p <= maxnorm:
            out.append(Prime(make_primary((p, 0))))
    out.sort(key=lambda P: (P.N, P.pi))
    return out

def alpha(x):
    z = cv(x); return z / abs(z)

# --- setup -----------------------------------------------------------------------------
def xi_mod2(x):
    """cubic character mod 2 on primary generators: O/2 = F_4, value omega^k"""
    a, b = x[0] % 2, x[1] % 2
    return {(1, 0): 1.0 + 0j, (0, 1): OMEGA, (1, 1): OMEGA ** 2}[(a, b)]

def bump(u, v):
    def W(y):
        y = np.asarray(y, dtype=float); out = np.zeros_like(y)
        m = (y > u) & (y < v)
        t = (y[m] - u) / (v - u)
        out[m] = np.exp(-1.0 / (t * (1 - t)) + 4.0)
        return out
    return W

def squarefree_ideals(primes, M):
    """list of (generator, list-of-prime-indices) for squarefree ideals of norm <= M (incl. 1)"""
    out = [((1, 0), [])]
    def dfs(start, g, nrm, idx):
        for i in range(start, len(primes)):
            P = primes[i]
            if nrm * P.N > M: break
            g2 = mul(g, P.pi); out.append((g2, idx + [i])); dfs(i + 1, g2, nrm * P.N, idx + [i])
    dfs(0, (1, 0), 1, [])
    return out

def all_ideals(primes, M):
    """all ideals (with multiplicity in the factorisation) of norm <= M, primary generators"""
    out = [((1, 0), [])]
    def dfs(start, g, nrm, idx):
        for i in range(start, len(primes)):
            P = primes[i]
            if nrm * P.N > M: break
            g2 = mul(g, P.pi); out.append((g2, idx + [i])); dfs(i, g2, nrm * P.N, idx + [i])
    dfs(0, (1, 0), 1, [])
    return out

def psi_prime(P, k, g, xi):
    """Psi(p) = xi(p) chi_p(k) chi_p(g)^4 as a complex number (zero extension)"""
    a = P.sym(k); b = P.sym(g)
    if a is None or b is None: return 0j
    return xi(P.pi) * Z6 ** ((a + 4 * b) % 6)

def chi_val(primes, idx, x, j=1):
    tot = 0
    for i in idx:
        s = primes[i].sym(x)
        if s is None: return 0j
        tot += j * s
    return Z6 ** (tot % 6)

# --- Gauss sums ----------------------------------------------------------------------------
def residues(n):
    a, b = n; N = norm(n); g = math.gcd(a, b); g = abs(g) if g else N
    return [(c, d) for d in range(g) for c in range(N // g)]
def gamma2_direct(primes, idx, n):
    N = norm(n); s = 0j
    for x in residues(n):
        c = chi_val(primes, idx, x, 2)
        if c == 0: continue
        dprime = mul(x, conj(n))[1]
        s += c * cmath.exp(2j * math.pi * dprime / N)
    return s / math.sqrt(N)

def run():
    rng = random.Random(20261117)
    report = []
    def log(s):
        print(s); report.append(s); sys.stdout.flush()

    # ---------- C5: gamma_2 CRT ---------------------------------------------------------
    primes_small = prime_list(3200)
    g2p = {}
    for i, P in enumerate(primes_small):
        if P.N <= 3200: g2p[i] = gamma2_direct(primes_small, [i], P.pi)
    def gamma2_crt(idx):
        # gamma_2(ab) = gamma_2(a) gamma_2(b) chi_a(b)^2 chi_b(a)^2 for coprime squarefree a,b
        val = 1 + 0j; acc_idx = []; acc = (1, 0)
        for i in idx:
            P = primes_small[i]
            cross = chi_val(primes_small, acc_idx, P.pi, 2) * chi_val(primes_small, [i], acc, 2)
            val = val * g2p[i] * cross
            acc_idx = acc_idx + [i]; acc = mul(acc, P.pi)
        return val
    sq = squarefree_ideals(primes_small, 400)
    maxerr = 0.0; cnt = 0
    for g, idx in sq:
        if len(idx) < 2: continue
        d = gamma2_direct(primes_small, idx, g); c = gamma2_crt(idx)
        maxerr = max(maxerr, abs(d - c)); cnt += 1
    log(f"C5 gamma_2 CRT vs direct: {cnt} composite squarefree n with N(n)<=400, max |diff| = {maxerr:.2e}")
    # |gamma_2(p)|=1 sanity
    log(f"C5 |gamma_2(p)| range over {len(g2p)} primes: [{min(abs(v) for v in g2p.values()):.12f}, {max(abs(v) for v in g2p.values()):.12f}]")

    # ---------- C1/C2/C3 core ------------------------------------------------------------
    def cube_inversion_test(primes, coeff, X, u, v, k, f, xi, Hc_list, label, hpow=1.0, bconj=True):
        # hpow, bconj: negative controls (hpow=0.5, or alpha^3 instead of conj(alpha)^3 on the h-side
        # only, must make C1 FAIL).  NB: changing the cube weight consistently on BOTH sides keeps
        # the identity (it is formal in any completely multiplicative cube weight).
        W = bump(u, v)
        Vstar = lambda y: np.sqrt(np.asarray(y, float)) * W(y)
        ns = squarefree_ideals(primes, int(v * X) + 1)
        psi_p = [psi_prime(P, k, f, xi) for P in primes]
        Nn = np.array([float(norm(g)) for g, idx in ns])
        vals = np.array([coeff(g, idx) * np.prod([psi_p[i] for i in idx]) if idx else coeff(g, idx)
                         for g, idx in ns], dtype=complex)
        bmax = int((v * X) ** (1 / 3)) + 1
        bs = all_ideals(primes, bmax)
        def psi_of(idx):
            return np.prod([psi_p[i] for i in idx]) if idx else 1 + 0j
        def T(Xp):
            tot = 0j
            for bg, bidx in bs:
                Nb = float(norm(bg))
                if Nb ** 3 > v * Xp: continue
                coef = np.conj(alpha(bg)) ** 3 * psi_of(bidx) ** 3 / Nb
                if coef == 0: continue
                tot += coef * np.sum(vals / np.sqrt(Nn) * Vstar(Nn * Nb ** 3 / Xp))
            return tot
        lhs = X ** -0.5 * np.sum(vals * W(Nn / X))
        hs = [(g, idx) for g, idx in squarefree_ideals(primes, bmax) if norm(g) ** 3 <= v * X]
        terms = {}
        for hg, hidx in hs:
            Nh = float(norm(hg)); mu = (-1) ** len(hidx)
            terms[(hg, tuple(hidx))] = mu * (np.conj(alpha(hg)) ** 3 if bconj else alpha(hg) ** 3) * psi_of(hidx) ** 3 / Nh ** hpow * T(X / Nh ** 3)
        rhs = sum(terms.values())
        err1 = abs(lhs - rhs)
        nb_nonsqf = sum(1 for bg, bidx in bs if len(set(bidx)) < len(bidx) and norm(bg) ** 3 <= v * X)
        log(f"C1[{label}] X={X}, supp W=[{u},{v}], #n={len(ns)}, #h={len(hs)}, #b={len(bs)} "
            f"(non-squarefree b in range: {nb_nonsqf}); |LHS|={abs(lhs):.6f}, |LHS-RHS|={err1:.2e}")
        # C3: Psi_k(b)^3 = xi(b)^3 chi_b(k)^3 1_{(b,f)=1}
        e3 = 0.0
        for bg, bidx in bs:
            lhs3 = psi_of(bidx) ** 3
            cop = all(primes[i].sym(f) is not None for i in bidx)
            rhs3 = (xi(bg) ** 3 if bidx else 1) * chi_val(primes, bidx, k, 3) * (1 if cop else 0)
            e3 = max(e3, abs(lhs3 - rhs3))
        log(f"C3[{label}] Psi_k(b)^3 = xi(b)^3 chi_b(k)^3 1_(b,f)=1 over {len(bs)} b (incl. prime powers): max err {e3:.2e}")
        # C2: long part regrouping
        for Hc in Hc_list:
            Plong_def = sum(val for (hg, hidx), val in terms.items() if norm(hg) > Hc)
            tot = 0j; tau_ok = True
            for bg, bidx in bs:
                Nb = float(norm(bg))
                if Nb <= Hc or Nb ** 3 > v * X: continue
                # divisors h of b (squarefree only matter), N(h) > Hc
                distinct = sorted(set(bidx))
                s = 0
                for mask in range(1 << len(distinct)):
                    sub_idx = [distinct[t] for t in range(len(distinct)) if mask >> t & 1]
                    Nh = 1
                    for i in sub_idx: Nh *= primes[i].N
                    if Nh > Hc: s += (-1) ** len(sub_idx)
                cop = all(primes[i].sym(f) is not None for i in bidx)
                xib = xi(bg) if bidx else 1
                beta0 = np.conj(alpha(bg)) ** 3 * xib ** 3 * (1 if cop else 0) * s
                # tau_div(b) = prod (e_p + 1)
                tau = 1
                for i in distinct: tau *= bidx.count(i) + 1
                if abs(beta0) > tau + 1e-12: tau_ok = False
                Lb = X / Nb ** 3
                inner = Lb ** -0.5 * np.sum(vals * W(Nn / Lb))
                tot += beta0 * chi_val(primes, bidx, k, 3) / Nb * inner
            log(f"C2[{label}] H_c={Hc}: |P_long(def) - P_long(b-form)| = {abs(Plong_def - tot):.2e}, "
                f"|P_long|={abs(Plong_def):.6f}, |beta_0|<=tau_div: {tau_ok}")
        return err1

    # (a) genuine coefficients a(n) = conj(alpha(n)) gamma_2(n) xi(n)  [xi is inside Psi]
    def genuine(g, idx):
        return np.conj(alpha(g)) * (gamma2_crt(idx) if idx else 1.0)
    pi7 = [P for P in primes_small if P.N == 7]; pi13 = [P for P in primes_small if P.N == 13]
    k_a = mul((0, 1), mul(pi13[0].pi, (2, 0)))            # omega * pi_13 * 2 : non-primary, meets S
    f_a = pi7[1].pi                                         # kills b = pi7' terms
    for xi, xl in ((lambda x: 1.0 + 0j, "xi=1"), (xi_mod2, "xi=cubic mod 2")):
        cube_inversion_test(primes_small, genuine, 3000.0, 0.002, 1.0, k_a, f_a, xi, [1, 7, 10], "genuine," + xl)

    # (b) random unimodular n-coefficients, large X so that b=pi^2 (N=49) and h=pi7*pi7' occur
    primes_big = prime_list(135000)
    rnd = {}
    def randc(g, idx):
        key = g
        if key not in rnd: rnd[key] = cmath.exp(2j * math.pi * rng.random())
        return rnd[key]
    pi7b = [P for P in primes_big if P.N == 7]; pi13b = [P for P in primes_big if P.N == 13]
    pi19b = [P for P in primes_big if P.N == 19]
    k_b = mul((-1, -1), mul(pi19b[0].pi, (1, 2)))          # omega^2 * pi_19 * lambda
    f_b = mul(pi13b[1].pi, pi19b[1].pi)                  # leaves pi7*pi7' (composite h) alive
    for xi, xl in ((lambda x: 1.0 + 0j, "xi=1"), (xi_mod2, "xi=cubic mod 2")):
        cube_inversion_test(primes_big, randc, 130000.0, 0.0005, 1.0, k_b, f_b, xi, [1, 7, 13, 30], "random-coeff," + xl)
    # negative controls: a wrong h-normalisation N(h)^{-1/2}, or alpha(h)^3 instead of
    # conj(alpha(h))^3 on the h-side only, must break C1 (shows the test is sensitive)
    cube_inversion_test(primes_big, randc, 130000.0, 0.0005, 1.0, k_b, f_b, xi_mod2, [], "CONTROL hpow=1/2", hpow=0.5)
    cube_inversion_test(primes_small, genuine, 3000.0, 0.002, 1.0, k_a, f_a, xi_mod2, [], "CONTROL h-side alpha^3 (no conj)", bconj=False)

    # ---------- C4: Prop 5.2 reduction ---------------------------------------------------
    plist = primes_small[:300]
    bad = 0; tot = 0
    for trial in range(200):
        u0 = UNIT[rng.randrange(6)]
        s = prod([plist[rng.randrange(40)].pi for _ in range(rng.randrange(3))] + [(1, 2)] * rng.randrange(2) + [(2, 0)] * rng.randrange(2))
        v_ = prod([plist[rng.randrange(40)].pi for _ in range(rng.randrange(3))] + [(1, 2)] * rng.randrange(2) + [(2, 0)] * rng.randrange(2))
        f_ = prod([plist[rng.randrange(60)].pi for _ in range(rng.randrange(3))])
        k_ = mul(u0, mul(s, mul(v_, v_)))
        for P in plist:
            a1 = P.sym(k_); a2 = P.sym(f_)
            lhs = 0 if (a1 is None or a2 is None) else Z6 ** ((a1 + 4 * a2) % 6)
            b1 = P.sym(mul(u0, s)); b2 = P.sym(mul(f_, mul(v_, v_)))
            rhs = 0 if (b1 is None or b2 is None) else Z6 ** ((b1 + 4 * b2) % 6)
            tot += 1
            if abs(lhs - rhs) > 1e-12: bad += 1
    log(f"C4 chi_p(u0 s v^2)chi_p(f)^4 = chi_p(u0 s)chi_p(f v^2)^4: {tot} (row,prime) cases incl. v with 2|v or lambda|v, failures {bad}")
    # and at the level of T (genuine coefficients, small X)
    X = 1500.0; u, v = 0.002, 1.0; Wf = bump(u, v)
    Vstar = lambda y: np.sqrt(np.asarray(y, float)) * Wf(y)
    ns = squarefree_ideals(primes_small, int(v * X) + 1)
    bs = all_ideals(primes_small, int((v * X) ** (1 / 3)) + 1)
    def T_full(kk, gg):
        psi_p = [psi_prime(P, kk, gg, lambda x: 1.0 + 0j) for P in primes_small]
        tot = 0j
        for bg, bidx in bs:
            Nb = norm(bg)
            if Nb ** 3 > v * X: continue
            pb = np.prod([psi_p[i] for i in bidx]) if bidx else 1 + 0j
            cb = np.conj(alpha(bg)) ** 3 * pb ** 3 / Nb
            for g, idx in ns:
                Nn = norm(g)
                pn = np.prod([psi_p[i] for i in idx]) if idx else 1 + 0j
                if pn == 0: continue
                an = np.conj(alpha(g)) * (gamma2_crt(idx) if idx else 1.0)
                tot += cb * an * pn / math.sqrt(Nn) * float(Vstar(np.array([Nn * Nb ** 3 / X]))[0])
        return tot
    worst = 0.0
    for (u0, s, v_, f_) in [(UNIT[1], pi13[0].pi, (1, 2), pi7[0].pi), (UNIT[4], mul(pi13[1].pi, (2, 0)), pi7[1].pi, (1, 0)),
                            (UNIT[3], (1, 0), (2, 0), pi13[0].pi)]:
        t1 = T_full(mul(u0, mul(s, mul(v_, v_))), f_); t2 = T_full(mul(u0, s), mul(f_, mul(v_, v_)))
        worst = max(worst, abs(t1 - t2))
        log(f"C4 T(X;u0 s v^2,f) vs T(X;u0 s,f v^2): |T|={abs(t1):.6f}, diff={abs(t1-t2):.2e}")
    return report

if __name__ == "__main__":
    run()
