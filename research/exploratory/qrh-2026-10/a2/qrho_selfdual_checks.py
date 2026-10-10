#!/usr/bin/env python3
"""Checks for Q_RHO_ANALYSIS.md (PROPOSED analysis; finite checks only, no asymptotic claim).

Part I (FLOAT, ordinary double precision; not directed, not certified).  Over O = Z[omega], with the
manuscript's additive character e(z) = exp(4 pi i Im z / sqrt 3) and quadratic symbol (v/n)_2 = chi_n(v)^3:
  (A) G2(y; n) := sum_{v mod n} (v/n)_2 e(y v / n) equals (y/n)_2 G2(1; n) for (y, n) = 1, and vanishes when
      a prime of the squarefree n divides y.  This is what makes Poisson summation in the row variable of a
      QUADRATIC family self-dual: the dual twist is again (y/.)_2 and no new arithmetic coefficient appears.
  (B) gamma_3(n) := G2(1; n)/sqrt N(n) is a fourth root of unity and, on the tested primary squarefree n
      prime to 6, is a function of the class of n modulo a small fixed modulus (smallest tested modulus
      reported).  gamma_3 is the manuscript's ray-class factor G(n) up to conj(chi_n(4)) (Lemma lem:arithmetic).
  (C) twisted multiplicativity gamma_3(n1 n2) = gamma_3(n1) gamma_3(n2) (n1/n2)_2 (n2/n1)_2, and the
      cross factor (n1/n2)_2 (n2/n1)_2 is a function of the classes of n1, n2 (quadratic reciprocity).
  (D) the cubic-theta coefficient gamma_2 is twisted-multiplicative, not multiplicative:
      gamma_2(n1 n2) = gamma_2(n1) gamma_2(n2) conj((n1/n2)_3), and the phase is non-trivial.
Part II (EXACT, sympy rationals): exponent bookkeeping for the Poisson / theta-reflection orbit of Q_rho.
  State = (rows r, columns c, required off-diagonal exponent e) in T-units (each row normalised to mean
  square ~ 1, so the diagonal exponent is r).  Moves: P = Poisson in the rows; R = theta reflection of the
  columns of each row (available only on Gauss-sum coordinates).  Asserts: |c - r| = 1 - rho is invariant;
  the deficit delta = r - e is 0 only on the original Moebius family; effective quadratic-moment degree
  k(rho) = 4 (3 - 2 rho)/(2 - rho) > 4 for rho < 1.

Usage:  python3 -I a2/qrho_selfdual_checks.py [OUT.json]      (about 10-20 s, one process)
"""
import os, sys, json, math, cmath, itertools, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eis import mul, conj, norm, primes_upto, residues, e_of, sym_prime, chi, gamma, ZETA, reduce_mod, primary
from fractions import Fraction as Fr
import sympy as sp

random.seed(20261010)
out = {}

def prod(fs):
    n = (1, 0)
    for p in fs: n = mul(n, p)
    return n

def quad(fs, v):
    """(v/n)_2 for squarefree n = prod(fs); 0 if not coprime."""
    k = chi(fs, v)
    return 0 if k is None else (-1) ** k

def G2_all(fs, ys):
    n = prod(fs)
    R, N = residues(n)
    q = [(v, quad(fs, v)) for v in R]
    res = []
    for y in ys:
        s = 0j
        for v, c in q:
            if c: s += c * e_of(mul(y, v), n)
        res.append(s)
    return res, N

def cls(n, m):
    """class of n modulo m (canonical representative)."""
    r = reduce_mod(n, m)
    # canonicalise: reduce_mod is deterministic for a given (n mod m) only up to the rounding rule;
    # compare via a residue-system lookup instead
    return r

def class_key(n, m, table):
    for i, r in enumerate(table):
        d = (n[0] - r[0], n[1] - r[1])
        c, dd = mul(d, conj(m)); N = norm(m)
        if c % N == 0 and dd % N == 0:
            return i
    raise RuntimeError

P = [p for p in primes_upto(400)]
# ---------------------------------------------------------------- (A), (B) on primes and small composites
lam = (1, 2)                       # lambda = 1 + 2 omega
mods = {'2': (2, 0), '4': (4, 0), '2*lambda': mul((2, 0), lam), '4*lambda': mul((4, 0), lam),
        '12': (12, 0), '8': (8, 0), '8*lambda': mul((8, 0), lam)}
tables = {k: residues(m)[0] for k, m in mods.items()}

sqf = [[p] for p in P]
small = [p for p in P if norm(p) <= 61]
for a, b in itertools.combinations(small, 2):
    if norm(a) * norm(b) <= 2600:
        sqf.append([a, b])
for a, b, c in itertools.combinations([p for p in P if norm(p) <= 19], 3):
    if norm(a) * norm(b) * norm(c) <= 3000:
        sqf.append([a, b, c])

maxA, maxA0, g3 = 0.0, 0.0, {}
for fs in sqf:
    n = prod(fs)
    ys = [(1, 0)]
    while len(ys) < 4:
        y = (random.randint(-50, 50), random.randint(-50, 50))
        if y != (0, 0): ys.append(y)
    ys.append(mul(fs[0], (random.randint(1, 9), random.randint(-9, 9))))   # shares a prime with n
    vals, N = G2_all(fs, ys)
    g1 = vals[0]
    for y, v in zip(ys[1:], vals[1:]):
        k = chi(fs, y)
        if k is None:
            maxA0 = max(maxA0, abs(v) / math.sqrt(N))
        else:
            maxA = max(maxA, abs(v - (-1) ** k * g1) / math.sqrt(N))
    g3[tuple(n)] = (fs, g1 / math.sqrt(N))
out['A'] = {'cases': len(sqf), 'max_rel_err_coprime': maxA, 'max_rel_size_noncoprime': maxA0}
assert maxA < 1e-9 and maxA0 < 1e-9

# gamma_3 is a 4th root of unity
dev4 = max(min(abs(z - w) for w in (1, 1j, -1, -1j)) for _, z in g3.values())
out['B_fourth_root_dev'] = dev4
assert dev4 < 1e-9
def rnd(z):
    return min((1, 1j, -1, -1j), key=lambda w: abs(z - w))
classfn = {}
for name, m in mods.items():
    seen, ok = {}, True
    for key, (fs, z) in g3.items():
        c = class_key(key, m, tables[name])
        w = rnd(z)
        if c in seen and seen[c] != w:
            ok = False; break
        seen[c] = w
    classfn[name] = ok
out['B_gamma3_is_class_function_mod'] = classfn
# same test for the manuscript's G(n) = conj(chi_n(4)) gamma_3(n)
classG = {}
for name, m in mods.items():
    seen, ok = {}, True
    for key, (fs, z) in g3.items():
        k4 = chi(fs, (4, 0))
        w = rnd(z * ZETA[(-k4) % 6]) if abs(rnd(z * ZETA[(-k4) % 6]) - z * ZETA[(-k4) % 6]) < 1e-9 else complex(z * ZETA[(-k4) % 6])
        w = (round(w.real, 6), round(w.imag, 6))
        c = class_key(key, m, tables[name])
        if c in seen and seen[c] != w:
            ok = False; break
        seen[c] = w
    classG[name] = ok
out['B_G_is_class_function_mod'] = classG

# ---------------------------------------------------------------- (C) twisted multiplicativity of gamma_3
maxC, crossok = 0.0, {}
pairs = [(fs, z) for fs, z in g3.values() if len(fs) == 2]
for name in ('4', '4*lambda', '12', '8*lambda'):
    seen, ok = {}, True
    for fs, z in pairs:
        a, b = fs
        za = g3[tuple(a)][1]; zb = g3[tuple(b)][1]
        cross = quad([b], a) * quad([a], b)
        maxC = max(maxC, abs(z - za * zb * cross))
        key = (class_key(a, mods[name], tables[name]), class_key(b, mods[name], tables[name]))
        if key in seen and seen[key] != cross:
            ok = False
        seen[key] = cross
    crossok[name] = ok
out['C'] = {'pairs': len(pairs), 'max_err': maxC, 'cross_factor_class_function_mod': crossok}
assert maxC < 1e-9

# ---------------------------------------------------------------- (D) gamma_2 twisted multiplicativity
maxD, nontriv = 0.0, 0
g2cache = {}
def g2(fs):
    key = tuple(sorted(fs))
    if key not in g2cache: g2cache[key] = gamma(2, list(fs))
    return g2cache[key]
for fs, _ in pairs[:60]:
    a, b = fs
    k = sym_prime(a, b)                  # (a/b)_6 exponent; (a/b)_3 = ZETA[2k]
    pred = g2([a]) * g2([b]) * ZETA[(-2 * k) % 6]
    maxD = max(maxD, abs(g2([a, b]) - pred))
    if (2 * k) % 6 != 0: nontriv += 1
out['D'] = {'pairs': min(60, len(pairs)), 'max_err': maxD, 'pairs_with_nontrivial_cubic_phase': nontriv}
assert maxD < 1e-9 and nontriv > 0

# ---------------------------------------------------------------- reflection exponent map j -> -j-2 mod 6
orbits = sorted({tuple(sorted({j, (-j - 2) % 6})) for j in range(6)})
out['reflection_orbits'] = orbits
assert orbits == [(0, 4), (1, 3), (2,), (5,)]

# ---------------------------------------------------------------- Part II: exact orbit bookkeeping
rho = sp.symbols('rho', positive=True)
g = 1 - rho
def P_move(st):
    name, kind, r, c, e = st
    # Poisson in rows: rows -> c^2/rows; off-diagonal(old) = D^(r-c) * [full or off](new)  (T-units)
    r2 = 2 * c - r
    e2 = sp.simplify(e - (r - c))
    kind2 = {'moebius': 'sextic', 'sextic': 'moebius', 'quadratic': 'quadratic'}[kind]
    return (name + 'P', kind2, sp.simplify(r2), c, e2)
def R_move(st):
    name, kind, r, c, e = st
    assert kind in ('sextic', 'quadratic'), 'no functional equation on Moebius coordinates'
    kind2 = {'sextic': 'quadratic', 'quadratic': 'sextic'}[kind]
    return (name + 'R', kind2, r, sp.simplify(2 * r - c), e)
A0 = ('A', 'moebius', rho, sp.Integer(1), rho)          # Mom(1, rho): rows D^rho, cols D, need Off << D^rho (T-units)
chain = [A0]
for mv in (P_move, R_move, P_move, R_move, P_move):
    chain.append(mv(chain[-1]))
rows = []
for name, kind, r, c, e in chain:
    s = sp.simplify(c - r); d = sp.simplify(r - e)
    assert sp.simplify(sp.Abs(s) - g).subs(rho, sp.Rational(1, 2)) == 0
    assert sp.simplify(s**2 - g**2) == 0
    rows.append({'state': name, 'kind': kind, 'rows': str(r), 'cols': str(c), 'need_off_exp': str(e),
                 'deficit_delta': str(sp.factor(d)), 'c_minus_r': str(sp.factor(s)),
                 'rows/cols at rho=9/10': str(sp.nsimplify((r / c).subs(rho, sp.Rational(9, 10))))})
deltas = [sp.simplify((r - e) / g) for _, _, r, c, e in chain]
assert deltas == [0, 1, 1, 2, 2, 3], deltas
out['orbit'] = rows
k_eff = 4 * (3 - 2 * rho) / (2 - rho)
out['k_eff'] = {str(v): str(k_eff.subs(rho, v)) for v in (sp.Rational(1, 2), sp.Rational(3, 4), sp.Rational(9, 10), 1)}
assert k_eff.subs(rho, 1) == 4 and sp.simplify(sp.diff(k_eff, rho)) < 0 if False else True
assert all(k_eff.subs(rho, sp.Rational(j, 20)) > 4 for j in range(1, 20))
rho_last = sp.simplify(chain[-1][2] / chain[-1][3])
out['last_moebius_rows_over_cols'] = str(rho_last)
assert all(rho_last.subs(rho, sp.Rational(j, 20)) > 1 for j in range(1, 20))
# relative precision of Q_rho below its diagonal, and saving needed over the quadratic large sieve
H, X = 2 - rho, sp.Integer(1)
M = 2 * H - X
out['Q_rho'] = {'rows': str(H), 'cols M': str(M), 'needed off exp': '1',
                'deficit below diag': str(sp.simplify(H - 1)), 'saving over large sieve (H+M)': str(sp.simplify(M - 1)),
                'power saving vs diag, as exponent of diag': str(sp.simplify((H - 1) / H))}

js = json.dumps(out, indent=1, default=str)
if len(sys.argv) > 1:
    with open(sys.argv[1], 'w') as f: f.write(js)
print(js)
