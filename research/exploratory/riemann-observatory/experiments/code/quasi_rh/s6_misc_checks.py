# s6_misc_checks.py -- remaining finite checks for the Section 6 audit of paper2.tex:
#  (a) Lemma 6.1 / (eq:intro-theta-coefficients): coefficient of conj(theta) at lambda^-3 n b^3
#      equals 3^{5/2}|b| conj(chi_n(lambda)^2) gamma_2(n) (paper's e(.) convention), incl. (n,b) != 1;
#      and c_theta(nb^3) phi_k(nb^3) = 3^{5/2}|b| gamma_2(n) Psi_k(n) Psi_k(b)^3.
#  (b) Lemma 6.5 / GL Def. 1 for x -> (x/k)_2 kappa_lam(x)^{e_k}: unit-triviality, conductor, reciprocity
#      factor (n/k)_2 (k/n)_2 a function of (n mod 4, k mod 4) only.
#  (c) archimedean normalisation of Prop. 6.2: for a single dual mode, the s-integral equals
#      (-i/81) N(l)^{-1/2} V_*^sharp(N(l) X / N(c)^2)   (mpmath).
#  (d) the j_p = 4 re-indexing identity of Lemma 6.6 (l.2041-2051) on random finite data.
import sys, os, math, cmath, random, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s6_theta import *
import mpmath as mp

random.seed(3)
Z6 = cmath.exp(2j * math.pi / 6)
def sextic(x, p):
    if divides(p, x): return None
    q = norm(p); r = powmod(x, (q - 1) // 6, p)
    for k in range(6):
        if divides(p, sub(r, power((1, 1), k))): return k
def chi_n(x, n):
    u, fac = factor(n); tot = 0
    for p, e in fac:
        k = sextic(x, p)
        if k is None: return 0
        tot += k * e
    return Z6 ** (tot % 6)
def gamma_j(n, j):
    return sum(chi_n(x, n) ** j * e_add(cv(x) / cv(n)) for x in residues(n) if chi_n(x, n) != 0) / math.sqrt(norm(n))

# (a)
ps = [p for q in sympy.primerange(5, 60) for p in primes_over(q) if norm(p) < 60]
ns = [ONE] + ps + [mul(ps[0], ps[1]), mul(ps[0], ps[3])]
bs = [ONE, ps[0], ps[1], make_primary((-2, 0))]
worst = 0; cnt = 0
for n in ns:
    for b in bs:
        m = mul(n, power(b, 3))
        if norm(m) > 3000: continue
        lhs = np.conj(tau(neg(m), 3))                     # coefficient of conj(theta) at l = lambda^-3 m is conj(tau(-l))
        rhs = 3 ** 2.5 * math.sqrt(norm(b)) * np.conj(chi_n(LAM, n) ** 2) * gamma_j(n, 2)
        worst = max(worst, abs(lhs - rhs)); cnt += 1
print("(a) Patterson coefficient identity: %d (n,b) pairs (incl. (n,b)!=1), max error %.2e" % (cnt, worst))

# (b)
def quad(x, k):
    """(x/k)_2 = chi_k(x)^3 for primary squarefree k (zero extension)."""
    c = chi_n(x, k)
    return 0 if c == 0 else round((c ** 3).real)
def kap_lam(x):
    r = rmod(x, LAM)
    for t in ((1, 0), (-1, 0)):
        if divides(LAM, sub(x, t)): return 1 if t == (1, 0) else -1
    return 0
sqf = []
for a in range(-12, 13):
    for b in range(-12, 13):
        x = (a, b)
        if is_zero(x) or not is_primary(x) or norm(x) == 1 or norm(x) > 120: continue
        if divides((2, 0), x): continue
        u, fac = factor(x)
        if all(e == 1 for _, e in fac): sqf.append(x)
bad_unit = 0; bad_cond = 0
for k in sqf:
    ek = 0 if norm(k) % 4 == 1 else 1
    f = lambda x: quad(x, k) * (kap_lam(x) ** ek)
    for u in UNITS:
        if f(u) != 1: bad_unit += 1
    # primitivity: for each prime p | k the character is nontrivial mod p; kap_lam nontrivial mod lam
    u_, fac = factor(k)
    for p, _ in fac:
        if all(quad(x, p) in (0, 1) for x in residues(p)): bad_cond += 1
table = {}; bad_rec = 0; npairs = 0
for n in sqf:
    for k in sqf:
        if norm(egcd(n, k)[0]) != 1: continue
        val = quad(n, k) * quad(k, n); npairs += 1
        key = (canon_mod(n, (4, 0)), canon_mod(k, (4, 0)))
        if key in table and table[key] != val: bad_rec += 1
        table[key] = val
print("(b) GL family: %d squarefree primary k; unit-triviality failures %d; nonprimitive local factors %d; "
      "reciprocity factor depends only on classes mod 4: %d pairs, %d violations, %d classes"
      % (len(sqf), bad_unit, bad_cond, npairs, bad_rec, len(table)))

# (c) archimedean normalisation
mp.mp.dps = 30
Vhat = lambda s: mp.sqrt(mp.pi) * mp.e ** (s * s / 4)       # Mellin transform of V(x) = exp(-(log x)^2)
def Vsharp(x):
    f = lambda u: Vhat(-1j * u) * mp.gamma(mp.mpf(7) / 6 + 1j * u) * mp.gamma(mp.mpf(5) / 6 + 1j * u) / (
        mp.gamma(mp.mpf(7) / 6 - 1j * u) * mp.gamma(mp.mpf(5) / 6 - 1j * u)) * ((2 * mp.pi) ** 4 * x / 27) ** (-1j * u)
    return mp.quad(f, [-mp.inf, 0, mp.inf]) / (2 * mp.pi)
def single_mode(Nl, Nc, X, sig=-0.6):
    # T-contribution of one dual mode, read off from (eq:ray-mellin), (eq:theta-mellin-functional-equation),
    # (eq:dual-cusp-mellin-series) with all unimodular arithmetic factors set to 1:
    def K(s):
        pre = (4 / mp.mpf(3) ** 2.5) * ((2 * mp.pi) ** 2 / 27) ** s / (mp.gamma(s + mp.mpf(1) / 3) * mp.gamma(s + mp.mpf(2) / 3))
        fe = -1 * Nc ** (1 - 2 * s)
        sp = 1 - s
        dual = 1j * mp.gamma(sp + mp.mpf(1) / 3) * mp.gamma(sp + mp.mpf(2) / 3) / (4 * (2 * mp.pi) ** (2 * sp)) * Nl ** (-sp)
        return pre * fe * dual
    f = lambda u: Vhat(sig + 1j * u - 0.5) * K(sig + 1j * u) * X ** (sig + 1j * u - 0.5)
    return mp.quad(f, [-mp.inf, 0, mp.inf]) / (2 * mp.pi)
for (Nl, Nc, X) in [(3, 7, 2.0), (12, 49, 30.0), (1.0 / 3, 13, 0.5)]:
    lhs = single_mode(Nl, Nc, X)
    rhs = (-1j / 81) * Nl ** -0.5 * Vsharp(Nl * X / Nc ** 2)
    print("(c) N(l)=%s N(c)=%s X=%s: contour integral %s   (-i/81) N(l)^-1/2 V#  %s   rel.err %.1e"
          % (Nl, Nc, X, mp.nstr(lhs, 12), mp.nstr(rhs, 12), float(abs(lhs - rhs) / abs(rhs))))

# (d) j_p = 4 re-indexing identity
def S(A, Y, k0chi, m, Vs, ns, bs_, H0, Nk0):
    tot = 0
    for n in ns:
        for b in bs_:
            tot += A(n, b) * k0chi(mul(n, b)) / (3 ** (m / 3) * math.sqrt(norm(n)) * norm(b)) * Vs(3 ** m * norm(n) * norm(b) ** 3 * H0 ** 2 / (Y * Nk0 ** 2))
    return tot
p = ps[2]; q = norm(p); k0 = mul(ps[0], ps[4]); Nk0 = norm(k0)
def k0chi(x):
    c = chi_n(x, k0); return 0 if c == 0 else c ** 3
small = [x for x in [ONE] + ps[:8] if x != p]
sqf_n = sorted(set([ONE] + small + [p] + [mul(p, x) for x in small[1:4]] + [mul(small[1], small[2])]), key=norm)
b_list = sorted(set([ONE, small[1], p, mul(p, small[1]), mul(p, p), small[2]]), key=norm)
coef = {}
def A0(n, b):
    if (n, b) not in coef: coef[(n, b)] = complex(random.gauss(0, 1), random.gauss(0, 1))
    return coef[(n, b)]
Vs = lambda x: math.exp(-x) * (1 + math.sin(x))
m = 1; Y = 7.3; H0 = 5.0
def Bp4(n, b):
    return -q ** -0.5 + q ** 0.5 * (1 if divides(p, n) else 0) + q ** 0.5 * (1 if (not divides(p, n) and divides(p, b)) else 0)
lhs = S(lambda n, b: A0(n, b) * Bp4(n, b), q * q * Y, k0chi, m, Vs, sqf_n, b_list, H0, Nk0)
# A^{(p,n)}(n,b) = 1_{p nmid n} A(pn,b); A^{(p,b)}(n,b) = 1_{p nmid n} A(n,pb); the ranges of n,b are mapped accordingly
ns_n = [exact_div(x, p) for x in sqf_n if divides(p, x)]
bs_b = [exact_div(x, p) for x in b_list if divides(p, x)]
t1 = -q ** -0.5 * S(A0, q * q * Y, k0chi, m, Vs, sqf_n, b_list, H0, Nk0)
t2 = k0chi(p) * S(lambda n, b: (0 if divides(p, n) else 1) * A0(mul(p, n), b), q * Y, k0chi, m, Vs, ns_n, b_list, H0, Nk0)
t3 = q ** -0.5 * k0chi(p) * S(lambda n, b: (0 if divides(p, n) else 1) * A0(n, mul(p, b)), Y / q, k0chi, m, Vs, sqf_n, bs_b, H0, Nk0)
print("(d) j_p=4 re-indexing identity: lhs %s  rhs %s  |diff| %.1e" % (np.round(lhs, 10), np.round(t1 + t2 + t3, 10), abs(lhs - t1 - t2 - t3)))
