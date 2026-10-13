"""O1 numerics: dual mean square of the cubic family after Poisson + absorption.

M(H, X; b) = sum_{h primary, 0<N h<=H} | sum_{n in cols(X)} b_n conj(chi_n(h))^2 |^2,
cols(X) = squarefree primary n, composed of SPLIT primes only, X/2 < N n <= X.
chi_n = sextic residue symbol (a2/eis.py conventions), so conj(chi_n(h))^2 is the cubic row twist
produced by Poisson in the row u of A_u = sum mu(n) chi_n(u)^2 W.
Coefficients:
  mu_g2  : b_n = mu(n) gamma_2(n)     (= chi_n(-1) alpha G gamma_{-1}(n): the absorbed dual coefficient)
  g2     : b_n = gamma_2(n)           (cubic Gauss sums: Kubota-pole control, DR/dFDH extremizer type)
  rand   : b_n = random unimodular phase (seeded)
  mu_rnd : b_n = mu(n) * random sign  (multiplicative-free control)
Floating point (numpy complex128), finite; nothing here is certified.
Usage: python3 dual_ms.py X H1,H2,... out.json  [seed]
"""
import sys, json, math, time, cmath
import numpy as np
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..', 'a2'))
import eis

def split_primes(N):
    """primary prime elements pi with split norm q = N pi <= N (q = 1 mod 3)."""
    sieve = np.ones(N + 1, bool); sieve[:2] = False
    for i in range(2, int(N**0.5) + 1):
        if sieve[i]: sieve[i*i::i] = False
    out = []
    for q in range(7, N + 1, 6):           # q = 1 mod 6
        if not sieve[q]: continue
        b = 1
        while 3*b*b <= 4*q:
            d = 4*q - 3*b*b; s = math.isqrt(d)
            if s*s == d and (b + s) % 2 == 0:
                a = (b + s)//2
                if eis.norm((a, b)) == q:
                    pi = eis.primary((a, b)); out += [pi, eis.primary(eis.conj(pi))]; break
            b += 1
    return sorted(set(out), key=eis.norm)

def prim_root(q):
    f = []; m = q - 1; p = 2
    while p*p <= m:
        if m % p == 0:
            f.append(p)
            while m % p == 0: m //= p
        p += 1
    if m > 1: f.append(m)
    for g in range(2, q):
        if all(pow(g, (q - 1)//r, q) != 1 for r in f): return g

_DL = {}
def _dlog(q, g):
    if q in _DL: return _DL[q]
    B = 1024; pw = np.empty(q - 1, np.int64); x = 1
    for k in range(min(B, q - 1)): pw[k] = x; x = x*g % q
    gB = pow(g, B, q); k = B
    while k < q - 1:
        m = min(B, q - 1 - k); pw[k:k + m] = (pw[k - B:k - B + m]*gB) % q; k += m
    dl = np.zeros(q, np.int64); dl[pw] = np.arange(q - 1); _DL.clear(); _DL[q] = dl
    return dl

class Prime:
    def __init__(self, pi):
        self.pi = pi; a, b = pi; q = eis.norm(pi); self.q = q
        self.w0 = (-a * pow(b, -1, q)) % q           # omega = w0 mod pi
        g = prim_root(q)
        dlog = _dlog(q, g)
        z = (1 + self.w0) % q                          # zeta = 1 + omega
        t = pow(g, (q - 1)//6, q); k0 = None
        for k in range(6):
            if pow(z, k, q) == t: k0 = k
        self.tab = (k0 * dlog) % 6                     # chi(x) = zeta^{tab[x]} for x != 0
        x = np.arange(q)
        ch = np.exp(2j*np.pi*self.tab[1:]/6)
        # e(x/pi) = exp(4 pi i Im(x conj(pi)/q)/sqrt3) = exp(-2 pi i b x / q)
        ad = np.exp(-2j*np.pi*((b*x[1:]) % q)/q)
        self.g2 = (ch**2 * ad).sum()/math.sqrt(q)
    def red(self, h):  # h = (x, y) arrays -> residue mod q
        return (h[0] + h[1]*self.w0) % self.q
    def chi_exp(self, h):  # exponent mod 6, or -1 if pi | h
        r = self.red(h); e = self.tab[r].astype(np.int8); e[r == 0] = -1; return e

def run(X, Hs, seed=1):
    t0 = time.time(); Hmax = max(Hs)
    P = [Prime(pi) for pi in split_primes(X)]
    # rows: primary h with N h <= Hmax
    R = int(math.isqrt(4*Hmax//3)) + 2
    xs, ys = np.meshgrid(np.arange(-2*R, 2*R + 1), np.arange(-2*R, 2*R + 1), indexing='ij')
    xs = xs.ravel(); ys = ys.ravel(); nrm = xs*xs - xs*ys + ys*ys
    sel = (nrm > 0) & (nrm <= Hmax) & (xs % 3 == 1) & (ys % 3 == 0)
    hx, hy, hn = xs[sel], ys[sel], nrm[sel]
    order = np.argsort(hn, kind='stable'); hx, hy, hn = hx[order], hy[order], hn[order]
    H = (hx, hy)
    # squarefree columns via DFS over split primes
    cols = []
    def dfs(start, prod_norm, facs):
        if prod_norm > X // 2: cols.append(list(facs))
        for i in range(start, len(P)):
            if prod_norm * P[i].q > X: break
            facs.append(i); dfs(i + 1, prod_norm * P[i].q, facs); facs.pop()
    dfs(0, 1, [])
    cache = {}
    def ex(i):
        if P[i].q > X // 7: return P[i].chi_exp(H)
        if i not in cache: cache[i] = P[i].chi_exp(H)
        return cache[i]
    # gamma_2 of composites by twisted multiplicativity gamma_2(m p) = gamma_2(m) gamma_2(p) chi_m(p)^2 chi_p(m)^2
    def elem(facs):
        z = (1, 0)
        for i in facs: z = eis.mul(z, P[i].pi)
        return z
    rng = np.random.default_rng(seed)
    coefs = {k: [] for k in ('mu_g2', 'g2', 'rand', 'mu_rnd')}
    for facs in cols:
        g = 1 + 0j; m_el = (1, 0); mf = []
        for i in facs:
            p = P[i]
            if mf:
                cp = sum(int(p.tab[p.red(m_el)]) for _ in [0])  # chi_p(m)
                cm = sum(eis.sym_prime(p.pi, P[j].pi) for j in mf)  # chi_m(p)
                g *= p.g2 * cmath.exp(2j*math.pi*2*(cp + cm)/6)
            else:
                g = p.g2
            mf.append(i); m_el = eis.mul(m_el, p.pi)
        mu = (-1)**len(facs)
        coefs['mu_g2'].append(mu*g); coefs['g2'].append(g)
        coefs['rand'].append(cmath.exp(2j*math.pi*rng.random())); coefs['mu_rnd'].append(mu*rng.choice([-1, 1]))
    coefs = {k: np.array(v) for k, v in coefs.items()}
    nh = len(hn)
    B = {k: np.zeros(nh, complex) for k in coefs}
    zeta_m2 = np.exp(-2j*np.pi*2*np.arange(6)/6)     # conj(chi)^2 = zeta^{-2e}
    for c, facs in enumerate(cols):
        e = np.zeros(nh, np.int16); bad = np.zeros(nh, bool)
        for i in facs:
            ei = ex(i); bad |= (ei < 0); e += np.where(ei < 0, 0, ei)
        tw = zeta_m2[e % 6]; tw[bad] = 0
        for k in B: B[k] += coefs[k][c]*tw
    out = {'X': X, 'ncols': len(cols), 'nprimes': len(P), 'time_s': None, 'rows': []}
    for Hc in sorted(Hs):
        m = hn <= Hc; nr = int(m.sum())
        rec = {'H': Hc, 'nrows': nr}
        for k in B:
            nb = float((np.abs(coefs[k])**2).sum()); M = float((np.abs(B[k][m])**2).sum())
            ls = nr + len(cols); bgl = nr + len(cols) + (nr*len(cols))**(2/3)
            rec[k] = {'M': M, 'norm2': nb, 'M_over_rows_norm': M/(nr*nb),
                      'M_over_LS': M/(ls*nb), 'M_over_BGL': M/(bgl*nb)}
        out['rows'].append(rec)
    out['time_s'] = time.time() - t0
    return out

def selfcheck():
    """compare gamma_2 (prime and composite) with eis.gamma (direct sums)."""
    P = [Prime(pi) for pi in split_primes(200)]
    dev = 0
    for p in P:
        dev = max(dev, abs(p.g2 - eis.gamma(2, [p.pi])))
    # composite check via the same twisted-multiplicativity code path
    worst = 0
    for i in range(4):
        for j in range(i + 1, 6):
            a, b = P[i], P[j]
            cp = int(b.tab[b.red((np.array([a.pi[0]]), np.array([a.pi[1]])))[0]])
            cm = eis.sym_prime(b.pi, a.pi)
            g = a.g2*b.g2*cmath.exp(2j*math.pi*2*(cp + cm)/6)
            worst = max(worst, abs(g - eis.gamma(2, [a.pi, b.pi])))
    # chi table check
    wc = 0
    for p in P[:10]:
        for u in [(2, 1), (5, -3), (7, 2), (-4, 9)]:
            k = eis.sym_prime(u, p.pi)
            r = (u[0] + u[1]*p.w0) % p.q
            if k is not None and int(p.tab[r]) != k: wc += 1
    return {'prime_gamma2_maxdev': dev, 'composite_gamma2_maxdev': worst, 'chi_table_mismatches': wc}

if __name__ == '__main__':
    if sys.argv[1] == 'check':
        print(json.dumps(selfcheck())); sys.exit()
    X = int(sys.argv[1]); Hs = [int(v) for v in sys.argv[2].split(',')]
    res = run(X, Hs, int(sys.argv[4]) if len(sys.argv) > 4 else 1)
    res['selfcheck'] = selfcheck()
    with open(sys.argv[3], 'w') as f: json.dump(res, f, indent=1)
    for r in res['rows']:
        print(r['H'], r['nrows'], res['ncols'], ' '.join('%s:%.3f/%.3f/%.3f' % (k, r[k]['M_over_rows_norm'], r[k]['M_over_LS'], r[k]['M_over_BGL']) for k in ('mu_g2', 'g2', 'rand', 'mu_rnd')))
    print('time', res['time_s'], res['selfcheck'])
