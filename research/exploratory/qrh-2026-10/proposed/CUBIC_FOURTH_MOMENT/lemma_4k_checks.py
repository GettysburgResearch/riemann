"""Finite checks for LEMMA_4K.md (PROPOSED; exploratory).  Run: python3 -I lemma_4k_checks.py
Exact integer arithmetic in O = Z[omega]; imports a2/eis.py read-only (mul, conj, norm, divides,
reduce_mod, powmod, primary).  lambda = 1 - omega.  Characters are computed from the DEFINITION
(k/p)_3 == k^{(Np-1)/3} mod p, extended multiplicatively over the factorisation of (alpha); no
reciprocity law and no conductor formula is used to evaluate them.
[K-LOC]   exact: cubes of units mod lambda^8 = 81 are exactly +-U^(4); U^(4) is cubed onto (finite).
[K-COND]  for every squarefree k (up to sign) with N(k) <= 500: periodicity of the ideal character
          eta_k((alpha)) = (k/(alpha))_3 mod each divisor of lambda^5*rad(k); the set of periodic
          divisors is exactly the multiples of the predicted conductor f(k) (sampled for "periodic",
          an explicit witness for "not periodic").
[K-REC]   chi_c(n) = (n/c)_3 equals eta_c((n)) for primary c, n (cubic reciprocity, sampled).
[K-FAM]   primary squarefree c, 3 not | c: conductor of n -> chi_c(primary n) is c*lambda^{2[Nc != 1 mod 9]}.
[K-BND]   N(f(k)) <= 81*N(rad_{not 3}(k)) and the maximum is attained.
Controls: [CTRL-NOLAMBDA] omitting the lambda-part fails whenever f_lambda > 0; [CTRL-CAP2] lambda
exponent capped at 2 fails whenever f_lambda >= 3; [CTRL-SPART] the S-part of k does not determine
the lambda-exponent; [CTRL-UNIT] chi_c as an element function is not an ideal function when Nc != 1 (9)."""
import sys, os, itertools
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'a2'))
from eis import mul, conj, norm, divides, reduce_mod, powmod, primary   # read-only import

OMEGA = (0, 1); LAM = (1, -1); ONE = (1, 0)
ROOTS = [(1, 0), (0, 1), (-1, -1)]                    # 1, omega, omega^2
def add(x, y): return (x[0] + y[0], x[1] + y[1])
def sub(x, y): return (x[0] - y[0], x[1] - y[1])
def neg(x): return (-x[0], -x[1])
def exact_div(z, m):
    c, d = mul(z, conj(m)); n = norm(m); assert c % n == 0 and d % n == 0; return (c // n, d // n)
def vval(z, p):
    v = 0
    while z != (0, 0) and divides(p, z): z = exact_div(z, p); v += 1
    return v

_split = {}
def split_prime(p):
    if p not in _split:
        r = int(p ** 0.5) + 2
        _split[p] = next((a, b) for a in range(0, r) for b in range(-r, r) if a*a - a*b + b*b == p)
    return _split[p]
def rat_factor(n):
    out = {}; d = 2
    while d * d <= n:
        while n % d == 0: out[d] = out.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: out[n] = out.get(n, 0) + 1
    return out
def prime_factors(z):
    """[(prime element, exponent)] for z in O, z != 0 (associate classes)."""
    out = []
    for p, e in rat_factor(norm(z)).items():
        if p == 3: out.append((LAM, vval(z, LAM)))
        elif p % 3 == 2: out.append(((p, 0), vval(z, (p, 0))))
        else:
            pi = split_prime(p)
            for q in (pi, conj(pi)):
                v = vval(z, q)
                if v: out.append((q, v))
    return out

def sym(k, pi):
    """(k/pi)_3 as exponent j (value omega^j) for prime pi not dividing 3k; None if pi | k."""
    if divides(pi, k): return None
    t = powmod(k, (norm(pi) - 1) // 3, pi)
    for j, w in enumerate(ROOTS):
        if divides(pi, sub(t, w)): return j
    raise RuntimeError('not a cube root of unity')

_symc = {}
def eta(k, alpha):
    """eta_k((alpha)) = (k/(alpha))_3 as exponent mod 3, or None unless (alpha) is prime to 3k."""
    if divides(LAM, alpha): return None
    s = 0
    for pi, e in prime_factors(alpha):
        key = (k, pi)
        if key not in _symc: _symc[key] = sym(k, pi)
        j = _symc[key]
        if j is None: return None
        s += e * j
    return s % 3

def f_lambda(k):
    """predicted lambda-exponent of the conductor of eta_k (Lemma 4.K(a))."""
    j = vval(k, LAM)
    if j % 3: return 4
    a = k
    for _ in range(j): a = exact_div(a, LAM)
    s = a if divides(LAM, sub(a, ONE)) else neg(a)
    assert divides(LAM, sub(s, ONE))
    t = min(vval(sub(s, ONE), LAM), 3) if s != ONE else 3
    return {1: 3, 2: 2, 3: 0}[t]
def lam_pow(e):
    z = ONE
    for _ in range(e): z = mul(z, LAM)
    return z
def predicted_conductor(k):
    """(good primes with 3 not | v, f_lambda)."""
    good = [(p, v) for p, v in prime_factors(k) if p != LAM and v % 3]
    return [p for p, v in good], f_lambda(k)
def modulus(primes, e):
    z = lam_pow(e)
    for p in primes: z = mul(z, p)
    return z

BOX = [(x, y) for x in range(-3, 4) for y in range(-3, 4)]
def periodic(k, m, need=12, box=BOX):
    """True if eta_k((1 + m*g)) = 1 for every g in box with 1 + m*g prime to 3k (and >= need tested);
    False with a witness otherwise."""
    tested = 0
    for g in box:
        a = add(ONE, mul(m, g))
        if a == (0, 0): continue
        v = eta(k, a)
        if v is None: continue
        tested += 1
        if v != 0: return False, a
    if tested < need:
        box2 = [(x, y) for x in range(-7, 8) for y in range(-7, 8)]
        if box is BOX: return periodic(k, m, need, box2)
        return None, tested
    return True, tested

results = {}
def report(tag, ok, msg):
    results[tag] = results.get(tag, True) and bool(ok)
    print('[%s] %s: %s' % (tag, 'PASS' if ok else 'FAIL', msg))

# ---------------- [K-LOC] local structure at lambda (exact, complete mod 81 = lambda^8 up to unit)
R = 81
units81 = [(a, b) for a in range(R) for b in range(R) if (a + b) % 3 != 0]   # a + b*omega unit at lambda iff a+b != 0 mod 3
def mod81(z): return (z[0] % R, z[1] % R)
def cube(z): return mod81(mul(z, mul(z, z)))
cubes = set(cube(u) for u in units81)
U4 = set(z for z in units81 if divides((9, 0), sub(z, ONE)))       # 1 mod lambda^4 = 1 mod 9
pmU4 = U4 | set(mod81(neg(z)) for z in U4)
report('K-LOC', cubes == pmU4,
       'cubes of units mod 81 = +-U^(4) mod 81 exactly (%d classes); so U^(4) is in K^x3 to this precision and '
       'U^(3) is not (1+lambda^3 not a cube); index [U : +-U^(4)] = %d (= 27, so U/U^3 has order 27)'
       % (len(cubes), len(units81) // len(cubes)))

# ---------------- enumerate squarefree k up to sign, N(k) <= 500
NMAX = 500
ideals = {}
for a in range(-30, 31):
    for b in range(-30, 31):
        z = (a, b)
        if z == (0, 0) or norm(z) > NMAX: continue
        assoc = [mul(u, z) for u in [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]]
        ideals.setdefault(min(assoc), None)
gens = sorted(ideals, key=lambda z: (norm(z), z))
sqf = [g for g in gens if all(v == 1 for _, v in prime_factors(g)) and g != (1, 0)]
rows = []
for g in sqf: rows += [g, mul(OMEGA, g), mul(OMEGA, mul(OMEGA, g))]
rows += [OMEGA, mul(OMEGA, OMEGA)]                     # pure units (N = 1)
print('squarefree ideals with 1 < N <= %d: %d; characters k (up to sign, 3 units each, plus omega, omega^2): %d'
      % (NMAX, len(sqf), len(rows)))

# ---------------- [K-COND] conductor = smallest modulus of periodicity
bad = []; hist = {}; maxratio = 0; ctrl_nol = [0, 0]; ctrl_cap = [0, 0]; ndiv = 0
for k in rows:
    primes, fl = predicted_conductor(k)
    hist[fl] = hist.get(fl, 0) + 1
    allp = [p for p, v in prime_factors(k) if p != LAM]
    pred = set(primes)
    for sub_ in itertools.chain.from_iterable(itertools.combinations(allp, r) for r in range(len(allp) + 1)):
        for e in range(0, 6):
            m = modulus(sub_, e); ndiv += 1
            expect = pred.issubset(set(sub_)) and e >= fl
            ok, info = periodic(k, m)
            if ok is None or ok != expect: bad.append((k, sub_, e, ok, info))
    # controls
    if fl > 0:
        ok, w = periodic(k, modulus(primes, 0)); ctrl_nol[0] += 1; ctrl_nol[1] += (ok is False)
    if fl >= 3:
        ok, w = periodic(k, modulus(primes, 2)); ctrl_cap[0] += 1; ctrl_cap[1] += (ok is False)
    rad = 1
    for p in allp: rad *= norm(p)
    maxratio = max(maxratio, norm(modulus(primes, fl)) / rad)
report('K-COND', not bad,
       '%d characters, %d (modulus, character) pairs: periodic exactly at multiples of the predicted '
       'conductor; lambda-exponent histogram %s; mismatches %d %s'
       % (len(rows), ndiv, dict(sorted(hist.items())), len(bad), bad[:3]))
report('K-BND', maxratio == 81, 'max N(f(k))/N(rad_{not 3}(k)) = %s (bound 81 = N(lambda^4))' % maxratio)
report('CTRL-NOLAMBDA', ctrl_nol[0] > 0 and ctrl_nol[1] == ctrl_nol[0],
       'omitting the lambda-part: %d of %d characters with f_lambda > 0 are NOT periodic (witness found)'
       % tuple(ctrl_nol[::-1]))
report('CTRL-CAP2', ctrl_cap[0] > 0 and ctrl_cap[1] == ctrl_cap[0],
       'lambda-exponent capped at 2: %d of %d characters with f_lambda in {3,4} are NOT periodic' % tuple(ctrl_cap[::-1]))

# ---------------- [K-REC] reciprocity and [K-FAM] family conductor
prim = [primary(g) for g in sqf if not divides(LAM, g)]
sample_n = [primary(z) for z in [(a, b) for a in range(-12, 13) for b in range(-12, 13)]
            if z != (0, 0) and not divides(LAM, z) and norm(z) > 1][:400]
def chi_el(c, a):
    """chi_c(a) = (a/c)_3 = sum over pi | c of (a/pi)_3, element function; None if not coprime."""
    s = 0
    for pi, e in prime_factors(c):
        j = sym(a, pi)
        if j is None: return None
        s += e * j
    return s % 3
nrec = 0; badrec = []
for c in prim:
    for n in sample_n[:60]:
        x = chi_el(c, n); y = eta(c, n)
        if x is None or y is None: continue
        nrec += 1
        if x != y: badrec.append((c, n))
report('K-REC', not badrec and nrec > 1000, '(n/c)_3 = (c/n)_3 for %d primary pairs (c sqfree, N c <= 500)' % nrec)
badfam = []; nf = 0; f9 = 0
for c in prim:
    fl_pred = 0 if norm(c) % 9 == 1 else 2
    nf += 1; f9 += (fl_pred == 0)
    cp = [p for p, v in prime_factors(c)]
    for e in range(0, 4):
        for drop in [None] + cp:
            mods = [p for p in cp if p != drop]
            m = modulus(mods, e)
            tested = 0; per = True
            for g in BOX:
                a = add(ONE, mul(m, g))
                if a == (0, 0) or divides(LAM, a): continue
                v = chi_el(c, primary(a))
                if v is None: continue
                tested += 1
                if v != 0: per = False; break
            expect = (drop is None) and e >= fl_pred
            if per != expect: badfam.append((c, e, drop))
report('K-FAM', not badfam, '%d primary squarefree c: chi_c(primary n) has conductor c*lambda^{0 or 2}, '
       'lambda-exponent 0 exactly when Nc = 1 mod 9 (%d such c); mismatches %d' % (nf, f9, len(badfam)))
q9 = [c for c in prim if divides((9, 0), sub(c, ONE))]
report('K-F3', all(f_lambda(c) == 0 for c in q9) and len(q9) > 0,
       'every squarefree q = 1 mod 9 with N q <= 500 (%d of them; the DDDS family F\'_3) has conductor q O' % len(q9))

# ---------------- [CTRL-SPART] and [CTRL-UNIT]
# 1 + 3 omega (N = 7) and -2 + 3 omega (N = 19) are primary good primes: empty S-part, different f_lambda
ex = [(k, f_lambda(k)) for k in [(1, 3), (-2, 3), (1, 9), (19, 0), (-5, 3)]]
report('CTRL-SPART', f_lambda((1, 3)) == 2 and f_lambda((-2, 3)) == 0 and f_lambda((1, -9)) == 0,
       'rows with empty S-part have lambda-exponents %s: the S-part of k does not fix the S-part of the conductor' % ex)
cu = [c for c in prim if norm(c) % 9 != 1]
viol = sum(1 for c in cu if chi_el(c, OMEGA) != 0)
report('CTRL-UNIT', viol == len(cu) and len(cu) > 0,
       'chi_c(omega) != 1 for all %d primary c with Nc != 1 mod 9: chi_c is not a function of ideals without the primary normalisation' % len(cu))

print('SUMMARY %d/%d' % (sum(results.values()), len(results)))
