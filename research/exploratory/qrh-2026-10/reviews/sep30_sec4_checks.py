#!/usr/bin/env python3
"""sep30_sec4_checks.py -- checks for the Section 4 helper lemmas 4.1, 4.6-4.10 and Lemma 13.1 of the
OpenAI QRH manuscript (30 Sep 2026; pr908 paper.tex, sha256 42a5ee0f...deac6a3). Line numbers refer to
that file. External, unreviewed source; nothing here proves any lemma for all moduli or heights.

Labels.  EXACT = integer arithmetic in O = Z[omega] (pairs (a,b) <-> a + b*omega) via a2/eis.py, which is
imported unchanged.  MP = mpmath at the stated working precision (ordinary high precision: NOT directed,
NOT certified).  FLOAT = numpy double precision.  EMPIRICAL = a finite-range observation.

  A  Lemma 4.1 (lem:fixed-numerator-ray, l. 646-699), EXACT on prime ideals of norm <= X.
     A1 residue degree: for split p, X^6 - a mod pi factors (sympy, GF(p)) into irreducibles whose
        degree is the order of (a/pi)_6, as Frobenius = symbol requires; inert p: the number of
        x in O/p with x^6 = a is 6 or 0 exactly as the symbol is 1 or not.
     A2 ray periodicity / conductor: for numerators a, the symbol on prime ideals is tested for being a
        function of the ray class mod m (residue of a generator modulo units) for m = 2^i lambda^j x
        (good part).  A collision is an exact certificate that the character does NOT factor through
        Cl_m; absence of collisions with every class of Cl_m hit is EMPIRICAL evidence that it does.
        The minimal passing m is reported as the (empirical) conductor; it must be supported on 6a.
     A3 the S-family {u lambda^v1 2^v2}: all 216 characters periodic for one common modulus, values
        depend on (u, v mod 6) only, and the 216 characters are pairwise distinct (at most 6^{|S|+1}).
     A4 control: a numerator with a good prime (5, pi_7, ...) is NOT periodic modulo any 2^i lambda^j
        in range but is periodic modulo (2,3-part) * rad(good part): conductor exponent 1 there.
        Also the Prop 16.1 claim (l. 8985-8990, outside scope): chi_n(u) depends on primary n only
        modulo 36 rad(u).
  D  Lemma 4.8 (lem:hecke-strip-growth, l. 1425-1529), MP.
     D1 the paper's theta/Poisson formula (l. 1460-1475), turned into an incomplete-gamma series
        valid for all s, is checked against L(s,chi)L(s,chi chi_{-3}) (mpmath.dirichlet) for
        base-change characters chi o N: this tests the normalizations 2/(sqrt3 v), 4 pi|.|^2/(3v).
     D2 functional equation Lambda = (3Q)^{s/2}(2pi)^{-s}Gamma(s)L: |Lambda(s)| = |Lambda(1-conj s)|
        holds with Q = norm of the A2 conductor of each Kummer character, and fails for wrong Q.
     D3 the explicit absolute constant of the proof, C = max(boundary sups), and the ratio
        |L|/(Q^{3/5}|s+2|^2) <= C on a grid of the strip -1/10 <= sigma <= 11/10, for Kummer
        characters (theta series) and base-change characters with Q = q^2 up to 961, plus the
        principal function (s-1)zeta_F(s)/(s+1).
  E  Lemma 4.9 (lem:logarithmic-control, l. 1531-1600), MP: on circles about 2+it for a base-change
     character and for the principal function: the zero-free hypothesis (winding number), the
     Borel-Caratheodory, three-circles and Cauchy steps with the paper's radii R_j = 2-a-je and
     r0 = 49/100, compared with log C; and the exponent theta(a,e) table.
  F  Lemma 4.10 (lem:deleted-euler-factors, l. 1602-1646), FLOAT: random squarefree R, |a_p| <= 1.
  B  Lemma 4.6 (lem:gaussian-annular, l. 1288-1340), FLOAT/MP: partition of unity, p_j(w_k) decay
     against C_j(1+|k|)^j exp(-((|k|-C)_+)^2/4), summability with e^{A|k|}, M W_G(s) = e^{s^2}.
  C  Lemma 4.7 (lem:kernel-seminorms, l. 1347-1413), MP: the Mellin-kernel derivative bound and its
     twisted form for W = W_G, m(s) = (s+3)^2 (h = 2); symbolic r d_r = (xi . grad)/2.
  G  Lemma 13.1 (lem:ray-prime-normalizer, l. 7006-7040), EXACT counting + FLOAT sums (EMPIRICAL):
     sum_{p in 1_T} W(q_p/P) q_p^{-5/6} against P^{1/6}/(|T| log P) int W y^{-5/6} for T = Cl_6
     (|T| = 3, the kernel of (2/.)_3 by A2) and T = Cl_12 (|T| = 12).

Usage:  nice -n 10 python3 -I sep30_sec4_checks.py [OUT.json] [quick]
"""
import sys, os, math, cmath, time, json, hashlib, random
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
A2DIR = os.path.abspath(os.path.join(HERE, '..', 'a2'))
EIS_SHA = '87ca11d98bf3ee130a6dab613b5f7efe444058320b7c22b005327686f2798e65'
with open(os.path.join(A2DIR, 'eis.py'), 'rb') as fh:
    _h = hashlib.sha256(fh.read()).hexdigest()
assert _h == EIS_SHA, ('eis.py changed', _h)
sys.path.insert(0, A2DIR)
import eis                                   # noqa: E402
from eis import mul, conj, norm, primary, divides, reduce_mod, sym_prime, UNITS   # noqa: E402

import numpy as np                           # noqa: E402
import mpmath as mp                          # noqa: E402
import sympy                                 # noqa: E402

QUICK = 'quick' in sys.argv[1:]
OUT = {}
FAILS = []


def say(*a):
    print(*a, flush=True)


def check(name, ok, info=''):
    say(('PASS ' if ok else 'FAIL ') + name + ((' : ' + str(info)) if info != '' else ''))
    if not ok:
        FAILS.append(name)
    return ok


LAM = (1, 2)           # lambda = 1 + 2 omega = sqrt(-3)
TWO = (2, 0)
ZETA6 = UNITS[1]       # 1 + omega = e^{i pi/3}


def epow(x, k):
    r = (1, 0)
    for _ in range(k):
        r = mul(r, x)
    return r


# ----------------------------------------------------------------------------------------------
# prime ideals of O (primary generators, prime to 6) up to norm X
# ----------------------------------------------------------------------------------------------
def rational_primes(N):
    s = bytearray([1]) * (N + 1)
    s[0:2] = b'\x00\x00'
    for i in range(2, int(N ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(N + 1) if s[i]]


def gcd_O(x, y):
    while y != (0, 0):
        x, y = y, reduce_mod(x, y)
    return x


def split_generator(p):
    h = 2
    while True:
        r = pow(h, (p - 1) // 3, p)
        if r != 1:
            break
        h += 1
    g = gcd_O((p, 0), (-r, 1))       # omega - r
    assert norm(g) == p, (p, g)
    return primary(g)


def prime_ideals(X):
    out = []
    for p in rational_primes(X):
        if p < 5:
            continue
        if p % 3 == 1:
            pi = split_generator(p)
            out.append((pi, p))
            out.append((primary(conj(pi)), p))
        elif p * p <= X:
            out.append((primary((p, 0)), p * p))
    out.sort(key=lambda t: (t[1], t[0]))
    return out


# ----------------------------------------------------------------------------------------------
# lattice m O : canonical residues and ray classes (residue modulo units)
# ----------------------------------------------------------------------------------------------
def egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    q, x, y = egcd(b, a % b)
    return (q, y, x - (a // b) * y)


class Lat:
    def __init__(self, m):
        self.m = m
        v1, v2 = m, mul(m, (0, 1))
        a1, b1 = v1
        a2, b2 = v2
        self.Q = abs(a1 * b2 - a2 * b1)
        g, x, y = egcd(b1, b2)
        if g < 0:
            g, x, y = -g, -x, -y
        if g == 0:
            raise ValueError
        self.g = g
        self.w0 = x * a1 + y * a2
        self.d1 = self.Q // g

    def canon(self, z):
        x, y = z
        k = y // self.g
        x -= k * self.w0
        y -= k * self.g
        return (x % self.d1, y)

    def ray(self, z):
        return min(self.canon(mul(u, z)) for u in UNITS)

    def residues(self):
        return [(i, j) for j in range(self.g) for i in range(self.d1)]

    def coprime(self, z):
        # (z, m) = 1  iff  z is a unit mod m  iff  gcd has norm 1
        return norm(gcd_O(self.m, z)) == 1


def ray_class_count(m):
    L = Lat(m)
    keys = set()
    for r in L.residues():
        if L.coprime(r):
            keys.add(L.ray(r))
    return len(keys)


def periodic(table, m, primes):
    """table: dict prime -> value (None = zero).  Is value a function of the ray class mod m?"""
    L = Lat(m)
    seen = {}
    for pi, N in primes:
        if not L.coprime(pi):
            continue
        v = table[pi]
        if v is None:          # p | a: outside the domain (ideals prime to 6a) of the ray character
            continue
        k = L.ray(pi)
        if k in seen and seen[k][0] != v:
            return (False, ('collision', seen[k][1], pi))
        seen.setdefault(k, (v, pi))
    return (True, len(seen))


def cl_size(i, j):
    """|Cl_m| for m = 2^i lambda^j: phi(m) / #(image of the units)."""
    phi2 = 1 if i == 0 else 4 ** i - 4 ** (i - 1)
    phil = 1 if j == 0 else 3 ** j - 3 ** (j - 1)
    L = Lat(mod_elem(i, j))
    inj = len({L.canon(u) for u in UNITS})
    return phi2 * phil // inj


def mod_elem(i, j, extra=(1, 0)):
    return mul(mul(epow(TWO, i), epow(LAM, j)), extra)


# ----------------------------------------------------------------------------------------------
# A : Lemma 4.1
# ----------------------------------------------------------------------------------------------
def part_A():
    say('\n=== A: Lemma 4.1 fixed numerators give ray characters (EXACT) ===')
    X = 6000 if QUICK else 30000
    t0 = time.time()
    P = prime_ideals(X)
    say(f'prime ideals of norm <= {X} prime to 6: {len(P)}  ({time.time()-t0:.1f}s)')
    res = {'X': X, 'n_primes': len(P)}

    # A1 residue degree / Frobenius order
    nums = {'zeta6': ZETA6, '-1': (-1, 0), 'lambda': LAM, '2': TWO, '2lambda': mul(TWO, LAM),
            '5': (5, 0), 'pi7': P[0][0] if P[0][1] == 7 else None, '3+omega': (3, 1)}
    x = sympy.symbols('x')
    bad = 0
    tested = 0
    for name, a in nums.items():
        for pi, N in P:
            if N > 400:
                break
            if divides(pi, a):
                continue
            k = sym_prime(a, pi)
            order = 6 // math.gcd(6, k)
            if N % 3 == 1 and sympy.isprime(N):
                p = N                                   # split: O/pi = F_p via omega -> r
                r = [r for r in range(p) if (r * r + r + 1) % p == 0]
                rr = [r0 for r0 in r if (pi[0] + pi[1] * r0) % p == 0][0]
                abar = (a[0] + a[1] * rr) % p
                fl = sympy.Poly(x ** 6 - abar, x, modulus=p).factor_list()[1]
                degs = sorted({f.degree() for f, e in fl})
                ok = (degs == [order]) and all(e == 1 for f, e in fl)
            else:                                       # inert q, O/q = F_{q^2}
                q = int(round(N ** 0.5))
                cnt = 0
                for u in range(q):
                    for v in range(q):
                        if divides(pi, (lambda z: (z[0] - a[0], z[1] - a[1]))(epow((u, v), 6))):
                            cnt += 1
                ok = (cnt == (6 if k == 0 else 0))
            tested += 1
            bad += (not ok)
    check('A1 residue degree of X^6-a equals order of (a/p)_6 (split, sympy GF(p)); '
          'root count 6/0 (inert)', bad == 0, f'{tested} (a,p) pairs, {bad} mismatches')
    res['A1'] = {'pairs': tested, 'mismatches': bad}

    # symbol tables
    def table(a):
        return {pi: sym_prime(a, pi) for pi, N in P}

    gens = {'zeta6': ZETA6, 'lambda': LAM, '2': TWO}
    T = {n: table(a) for n, a in gens.items()}
    # multiplicativity in the numerator (exact, all primes)
    prod_ok = True
    for (u, v1, v2) in [(1, 1, 1), (5, 3, 2), (2, 5, 4), (3, 0, 5)]:
        a = mul(mul(epow(ZETA6, u), epow(LAM, v1)), epow(TWO, v2))
        for pi, N in P[:400]:
            k = sym_prime(a, pi)
            kk = (u * T['zeta6'][pi] + v1 * T['lambda'][pi] + v2 * T['2'][pi]) % 6
            prod_ok &= (k == kk)
    check('A3a numerator multiplicativity chi_A(u lam^v1 2^v2) = sum of exponents', prod_ok)

    # A2: conductor search for several numerators
    def conductor(tab, extra=(1, 0), imax=4, jmax=7, name=''):
        # a modulus counts as passing only if it has no collision AND |Cl_m| <= #primes/5
        # (otherwise absence of collisions is inconclusive); failures are exact certificates.
        passing = []
        certs = {}
        for i in range(imax + 1):
            for j in range(jmax + 1):
                m = mod_elem(i, j, extra)
                ok, info = periodic(tab, m, P)
                if ok and cl_size(i, j) <= len(P) // 5:
                    passing.append((i, j))
                elif not ok:
                    certs[(i, j)] = info
        mins = [(i, j) for (i, j) in passing
                if not any((i2 <= i and j2 <= j and (i2, j2) != (i, j)) for (i2, j2) in passing)]
        return passing, mins, certs

    kummer = {}
    for name, a in [('(2/.)_3', None), ('(lambda/.)_3', None), ('(2/.)_6', None),
                    ('(lambda/.)_6', None), ('(zeta6/.)_6', None), ('(2lambda/.)_3', None),
                    ('(-1/.)_6', None), ('(2/.)_2', None)]:
        if name == '(2/.)_3':
            tab = {p: (2 * T['2'][p]) % 6 for p in T['2']}
        elif name == '(lambda/.)_3':
            tab = {p: (2 * T['lambda'][p]) % 6 for p in T['2']}
        elif name == '(2/.)_6':
            tab = T['2']
        elif name == '(lambda/.)_6':
            tab = T['lambda']
        elif name == '(zeta6/.)_6':
            tab = T['zeta6']
        elif name == '(2lambda/.)_3':
            tab = {p: (2 * T['2'][p] + 2 * T['lambda'][p]) % 6 for p in T['2']}
        elif name == '(-1/.)_6':
            tab = {p: (3 * T['zeta6'][p]) % 6 for p in T['2']}
        elif name == '(2/.)_2':
            tab = {p: (3 * T['2'][p]) % 6 for p in T['2']}
        passing, mins, certs = conductor(tab)
        info = {'minimal_passing': mins}
        if len(mins) == 1:
            i, j = mins[0]
            m = mod_elem(i, j)
            ncls = ray_class_count(m) if norm(m) <= 50000 else None
            ok, nseen = periodic(tab, m, P)
            # strict divisors must fail with an exact collision certificate
            divs_fail = all(((i2, j2) in certs) for i2 in range(i + 1) for j2 in range(j + 1)
                            if (i2, j2) != (i, j))
            info.update({'conductor': f'2^{i} lambda^{j}', 'Q': norm(m), 'classes': ncls,
                         'classes_hit': nseen, 'strict_divisors_certified_fail': divs_fail})
            kummer[name] = (m, tab)
            check(f'A2 {name}: unique minimal modulus 2^{i} lambda^{j} (Q={norm(m)}), supported on 6a; '
                  f'every strict divisor fails by exact collision', divs_fail and (ncls is None or nseen == ncls),
                  f'classes hit {nseen}/{ncls}')
        else:
            check(f'A2 {name}: unique minimal modulus', False, mins)
        res.setdefault('A2', {})[name] = info

    # A3: whole S-family with common modulus
    allmods = [kummer[n][0] for n in ('(2/.)_6', '(lambda/.)_6', '(zeta6/.)_6')]
    ii = max(next(k for k in range(20) if not divides(epow(TWO, k + 1), mm)) for mm in allmods)
    jj = max(next(k for k in range(30) if not divides(epow(LAM, k + 1), mm)) for mm in allmods)
    mc = mod_elem(ii, jj)
    fam_ok = True
    sigs = set()
    sample = P[:600]
    for u in range(6):
        for v1 in range(6):
            for v2 in range(6):
                tab = {p: (u * T['zeta6'][p] + v1 * T['lambda'][p] + v2 * T['2'][p]) % 6 for p in T['2']}
                ok, _ = periodic(tab, mc, P)
                fam_ok &= ok
                sigs.add(tuple(tab[p] for p, N in sample))
                # v -> v + 6 gives the same character (exact, from the definition)
                if (u, v1, v2) in [(1, 2, 3), (5, 5, 0)]:
                    a1 = mul(mul(epow(ZETA6, u), epow(LAM, v1)), epow(TWO, v2))
                    a2 = mul(a1, mul(epow(LAM, 6), epow(TWO, 6)))
                    fam_ok &= all(sym_prime(a1, p) == sym_prime(a2, p) for p, N in P[:300])
    check(f'A3 216 characters A -> chi_A(u lam^v1 2^v2) all periodic mod common 2^{ii} lambda^{jj} '
          f'(Q={norm(mc)}); depend on v mod 6 only', fam_ok)
    check('A3 the 216 characters are pairwise distinct (so the bound 6^{|S|+1} is attained)',
          len(sigs) == 216, len(sigs))
    res['A3'] = {'common_modulus': f'2^{ii} lambda^{jj}', 'Q': norm(mc), 'distinct': len(sigs)}

    # A4 control: good-prime numerators
    ctrl = {}
    p7 = [p for p, N in P if N == 7][0]
    p13 = [p for p, N in P if N == 13][0]
    p19 = [p for p, N in P if N == 19][0]
    for name, a, isgood in [('5', (5, 0), True), ('pi7', p7, True), ('pi13*pi7', mul(p13, p7), True),
                            ('pi7^2', epow(p7, 2), True), ('zeta6*pi19', mul(ZETA6, p19), True),
                            ('lambda*2*pi19', mul(mul(LAM, TWO), p19), False)]:
        tab = {p: sym_prime(a, p) for p, N in P}
        rad = (1, 0)
        good = [p for p, N in P if N <= norm(a) and divides(p, a)]
        for p in good:
            rad = mul(rad, p)
        # (a) no well-covered modulus 2^i lambda^j works: each fails by an exact collision
        covered = [(i, j) for i in range(5) for j in range(8) if cl_size(i, j) <= len(P) // 5]
        no_S_only = all(not periodic(tab, mod_elem(i, j), P)[0] for (i, j) in covered)
        base = (36, 0) if isgood else mc
        # (b) periodic modulo base * rad (EMPIRICAL on the prime range)
        okc, nseen = periodic(tab, mul(base, rad), P)
        # (c) each good prime is needed: not periodic mod base*rad/p (exact collision certificate)
        drop = all(not periodic(tab, mul(base, reduce_div(rad, p)), P)[0] for p in good)
        ncl = (108 if isgood else ray_class_count(mc)) * math.prod(N - 1 for p, N in P if p in good)
        ctrl[name] = {'S-supported moduli tested (all fail)': len(covered), 'no S-supported modulus': no_S_only,
                      '|Cl| of periodicity modulus': ncl, 'primes used': len(P),
                      ('periodic mod 36 rad(u) [Prop 16.1]' if isgood else 'periodic mod common*rad'): okc,
                      'classes hit': nseen, 'each good prime needed (exponent 1)': drop}
        check(f'A4 control numerator {name}: no S-supported modulus (exact collisions); periodic mod '
              f'{"36" if isgood else "common"}*rad; each good prime needed to exponent exactly 1',
              no_S_only and okc and drop, ctrl[name])
    res['A4'] = ctrl
    OUT['A'] = res
    return kummer, P


def reduce_div(x, p):
    """x / p in O (exact division)."""
    c, d = mul(x, conj(p))
    n = norm(p)
    assert c % n == 0 and d % n == 0
    return (c // n, d // n)


# ----------------------------------------------------------------------------------------------
# D : Lemma 4.8 -- theta-series evaluation of Hecke L-functions of F
# ----------------------------------------------------------------------------------------------
def lattice_points(Nmax):
    """all c = (x,y) != 0 with norm <= Nmax."""
    pts = []
    B = int(math.isqrt(4 * Nmax // 3 + 4)) + 2
    for y in range(-B, B + 1):
        for x in range(-2 * B, 2 * B + 1):
            n = x * x - x * y + y * y
            if 0 < n <= Nmax:
                pts.append((x, y))
    return pts


class ThetaL:
    """L(s,phi) = (1/6) sum_{a != 0} phi(a) q_a^{-s} for phi periodic mod f, unit invariant,
    phi(0 mod f) = 0 and hat phi(0) = 0, via the paper's theta formula split at v = 1:
      6 pi^{-s} Gamma(s) L = sum_a phi(a)(pi q_a)^{-s} Gamma(s, pi q_a)
                             + (2/sqrt3) sum_{c != 0} hatphi(c) alpha_c^{s-1} Gamma(1-s, alpha_c),
      alpha_c = 4 pi q_c / (3 Q),  hatphi(c) = Q^{-1} sum_{a mod f} phi(a) e(-ca/f).
    Coefficients are formed at 60 digits from exact exponent multisets."""

    def __init__(self, f, phi_frac, xmax=85.0):
        old = mp.mp.dps
        mp.mp.dps = 60
        self.f = f
        L = Lat(f)
        self.lat = L
        self.Q = Q = L.Q
        R = L.residues()
        vals = {a: phi_frac(a) for a in R}
        ev = lambda r: mp.expjpi(2 * mp.mpf(r.numerator) / r.denominator)
        # hat phi on residues
        hatv = {}
        for c in R:
            acc = {}
            for a, r in vals.items():
                if r is None:
                    continue
                cc, d = mul(mul(c, a), conj(f))          # e(ca/f) = exp(2 pi i d/Q)
                e = (r - Fraction(d % Q, Q)) % 1
                acc[e] = acc.get(e, 0) + 1
            hatv[c] = sum((k * ev(e) for e, k in acc.items()), mp.mpc(0)) / Q
        self.hat0 = hatv[L.canon((0, 0))]
        self.xmax = xmax
        nmax_d = int(xmax / math.pi) + 2
        self.dir = {}
        for c in lattice_points(nmax_d):
            r = vals[L.canon(c)]
            if r is not None:
                n = norm(c)
                self.dir[n] = self.dir.get(n, mp.mpc(0)) + ev(r)
        nmax_h = int(3 * Q * xmax / (4 * math.pi)) + 2
        cnt = {}
        for c in lattice_points(nmax_h):
            key = (norm(c), L.canon(c))
            cnt[key] = cnt.get(key, 0) + 1
        self.dual = {}
        for (n, r), k in cnt.items():
            self.dual[n] = self.dual.get(n, mp.mpc(0)) + k * hatv[r]
        tiny = mp.mpf(10) ** -50
        self.dual = {n: w for n, w in self.dual.items() if abs(w) > tiny}
        mp.mp.dps = old

    def __call__(self, s):
        s = mp.mpc(s)
        tot = mp.mpc(0)
        for n, w in self.dir.items():
            x = mp.pi * n
            if x <= self.xmax:
                tot += w * x ** (-s) * mp.gammainc(s, x)
        tot2 = mp.mpc(0)
        for n, w in self.dual.items():
            al = 4 * mp.pi * n / (3 * self.Q)
            if al <= self.xmax:
                tot2 += w * al ** (s - 1) * mp.gammainc(1 - s, al)
        tot += 2 / mp.sqrt(3) * tot2
        return tot * mp.pi ** s * mp.rgamma(s) / 6


def dirichlet_chars_prime(q):
    """a complex primitive character mod prime q (order q-1) as list of Fractions/None."""
    g = int(sympy.primitive_root(q))
    lst = [None] * q
    x = 1
    for k in range(q - 1):
        lst[x] = Fraction(k, q - 1)
        x = x * g % q
    return lst


def chi_m3(n):
    n %= 3
    return None if n == 0 else (Fraction(0) if n == 1 else Fraction(1, 2))


def frac_list_to_mp(lst):
    return [mp.mpf(0) if r is None else mp.expjpi(2 * mp.mpf(r.numerator) / r.denominator) for r in lst]


def times_m3(lst):
    q = len(lst)
    out = []
    for n in range(3 * q):
        a, b = lst[n % q], chi_m3(n)
        out.append(None if (a is None or b is None) else (a + b) % 1)
    return out


def part_D(kummer, quick=False):
    say('\n=== D: Lemma 4.8 Hecke strip growth (MP, not certified) ===')
    res = {}
    mp.mp.dps = 40
    # explicit constants of the proof
    zF11 = mp.zeta(1.1) * mp.dirichlet(1.1, [0, 1, -1])
    def gq(t):
        return abs(mp.gamma(mp.mpc(1.1, -t)) / mp.gamma(mp.mpc(-0.1, t)))
    ts = [mp.mpf(k) / 4 for k in range(0, 801)]
    supL = max(gq(t) / (mp.mpf(1.9) ** 2 + t * t) for t in ts)
    C_left = 3 ** mp.mpf(0.6) * (2 * mp.pi) ** (-1.2) * zF11 * supL
    C_right = zF11 / mp.mpf(3.1) ** 2
    C = max(C_left, C_right)
    # principal: |(s-1)/(s+1)| <= 1.1/0.9 on Re s = -1/10 (sup at t = 0), <= 1 on Re s = 11/10
    C_pr = max(C_left * mp.mpf(1.1) / mp.mpf(0.9), C_right)
    res['zeta_F(11/10)'] = float(zF11)
    res['C_left'] = float(C_left)
    res['C_right'] = float(C_right)
    res['C'] = float(C)
    res['C_principal'] = float(C_pr)
    say(f'explicit boundary constants: zeta_F(1.1)={float(zF11):.4f}, C_left={float(C_left):.4f}, '
        f'C_right={float(C_right):.4f}  => |L| <= C Q^(3/5)|s+2|^2 with C={float(C):.4f}')
    # stirling exponent on the left line: |Gamma(1.1-it)/Gamma(-0.1+it)| / |t|^{6/5} -> (const)
    st = [float(gq(t) / t ** 1.2) for t in (10, 100, 1000)]
    check('D0 Stirling: |Gamma(11/10-it)/Gamma(-1/10+it)| ~ |t|^{6/5} (ratio at t=10,100,1000)',
          abs(st[2] - 1) < 1e-2, [round(v, 5) for v in st])

    # D1 validation of the theta formula against base change
    def base_change_phi(lst):
        q = len(lst)
        return lambda a: lst[norm(a) % q]
    val = []
    for q in ([5, 7] if quick else [5, 7, 4]):
        if q == 4:
            lst = [None, Fraction(0), None, Fraction(1, 2)]
        else:
            lst = dirichlet_chars_prime(q)
        th = ThetaL((q, 0), base_change_phi(lst), xmax=80.0)
        c1, c2 = frac_list_to_mp(lst), frac_list_to_mp(times_m3(lst))
        for s in [mp.mpc(2, 0), mp.mpc(0.5, 3), mp.mpc(-0.1, 10), mp.mpc(1.1, -7), mp.mpc(0.3, 0)]:
            a = th(s)
            b = mp.dirichlet(s, c1) * mp.dirichlet(s, c2)
            val.append(float(abs(a - b) / abs(b)))
    check('D1 theta/Poisson series (paper l. 1460-1475) = L(s,chi)L(s,chi chi_-3) for chi o N',
          max(val) < 1e-20, f'max rel err {max(val):.2e} over {len(val)} points (dps 40)')
    res['D1_max_rel_err'] = max(val)

    # Kummer characters as theta series; FE test with Q = N(conductor)
    kum_L = {}
    for name, (m, tab) in kummer.items():
        if norm(m) > (40 if quick else 110):
            continue
        L = Lat(m)
        cls = {}
        for p, k in tab.items():
            if L.coprime(p):
                cls[L.ray(p)] = k
        def phi(a, L=L, cls=cls):
            if not L.coprime(a):
                return None
            k = cls.get(L.ray(a))
            if k is None:
                raise KeyError('class not covered')
            return Fraction(k, 6)
        try:
            th = ThetaL(m, phi, xmax=85.0)
        except KeyError:
            continue
        kum_L[name] = th
    fe = {}
    for name, th in kum_L.items():
        Q = th.Q
        out = []
        for s in [mp.mpc(0.2, 3), mp.mpc(-0.1, 7.5), mp.mpc(0.35, 0.4)]:
            s2 = 1 - mp.conj(s)
            v1, v2 = th(s), th(s2)
            lam = lambda z, v, QQ: abs((3 * QQ) ** (z / 2) * (2 * mp.pi) ** (-z) * mp.gamma(z) * v)
            r_true = float(lam(s, v1, Q) / lam(s2, v2, Q))
            r_wrong = float(lam(s, v1, 4 * Q) / lam(s2, v2, 4 * Q))
            out.append((r_true, r_wrong))
        ok = all(abs(a - 1) < 1e-15 for a, b in out) and all(abs(b - 1) > 1e-3 for a, b in out)
        # Euler-product cross-check at s = 3 for the coefficients
        fe[name] = {'Q': Q, 'ratios': out, 'hat_phi(0)': complex(th.hat0)}
        check(f'D2 FE |Lambda(s)|=|Lambda(1-conj s)| for {name} with Q={Q} (and fails with 4Q)', ok,
              [(round(a, 15), round(b, 4)) for a, b in out])
    res['D2'] = {k: {'Q': v['Q'], 'ratios': v['ratios']} for k, v in fe.items()}

    # D3 ratio |L| / (Q^{3/5}|s+2|^2) on the strip
    sig = [-0.1, 0.25, 0.5, 0.8, 1.1]
    tt = [0, 6, -6, 20, -20] if not quick else [0, 6, -6]
    worst = {}
    for name, th in kum_L.items():
        Q = th.Q
        r = 0
        rl = 0
        for s0 in sig:
            for t in tt:
                s = mp.mpc(s0, t)
                v = abs(th(s))
                r = max(r, float(v / (Q ** 0.6 * abs(s + 2) ** 2)))
                if s0 == -0.1:
                    rl = max(rl, float(v / (Q ** 0.6 * (3 + abs(t)) ** 1.2)))
        worst[name] = (Q, r, rl)
    # base-change family with growing Q = q^2
    qs = [4, 5, 7, 8, 11, 13, 17, 19, 23, 29, 31] if not quick else [5, 7, 11]
    tt2 = [0, 2, -2, 5, -5, 10, -10, 20, -20, 40, -40] if not quick else [0, 5, -5]
    for q in qs:
        if q == 4:
            lst = [None, Fraction(0), None, Fraction(1, 2)]
        elif q == 8:
            lst = [None, Fraction(0), None, Fraction(1, 2), None, Fraction(1, 2), None, Fraction(0)]  # chi_8 (primitive, even)
        else:
            lst = dirichlet_chars_prime(q)
        c1, c2 = frac_list_to_mp(lst), frac_list_to_mp(times_m3(lst))
        Q = q * q
        r = 0
        rl = 0
        for s0 in sig:
            for t in tt2:
                s = mp.mpc(s0, t)
                v = abs(mp.dirichlet(s, c1) * mp.dirichlet(s, c2))
                r = max(r, float(v / (Q ** 0.6 * abs(s + 2) ** 2)))
                if s0 == -0.1:
                    rl = max(rl, float(v / (Q ** 0.6 * (3 + abs(t)) ** 1.2)))
        worst[f'chi_{q} o N'] = (Q, r, rl)
    # principal
    r = 0
    for s0 in sig:
        for t in tt2:
            s = mp.mpc(s0, t)
            if abs(s - 1) < 1e-12:
                continue
            v = abs((s - 1) * mp.zeta(s) * mp.dirichlet(s, [0, 1, -1]) / (s + 1))
            r = max(r, float(v / abs(s + 2) ** 2))
    worst['principal (s-1)zeta_F/(s+1)'] = (1, r, None)
    for k, (Q, r, rl) in worst.items():
        say(f'   {k:28s} Q={Q:5d}  max |L|/(Q^.6|s+2|^2) = {r:.4e}' +
            (f'   max on sigma=-1/10 of |L|/(Q^.6(3+|t|)^1.2) = {rl:.4e}' if rl is not None else ''))
    okC = all(r <= float(C) for k, (Q, r, rl) in worst.items() if not k.startswith('principal'))
    okP = worst['principal (s-1)zeta_F/(s+1)'][1] <= float(C_pr)
    check('D3 |L(s,psi)| <= C Q^{3/5}|s+2|^2 with the explicit proof constant C on the strip grid '
          '(Kummer and base-change characters, Q up to 961)', okC)
    check('D3 principal (s-1)zeta_F(s)/(s+1) <= C_pr |s+2|^2', okP)
    res['D3'] = {k: list(v) for k, v in worst.items()}
    OUT['D'] = res


# ----------------------------------------------------------------------------------------------
# E : Lemma 4.9 numerics
# ----------------------------------------------------------------------------------------------
def part_E(quick=False):
    say('\n=== E: Lemma 4.9 logarithmic control (MP, sanity only) ===')
    mp.mp.dps = 25
    res = {}
    # theta(a,e) table
    tab = {}
    for e in (1e-3, 1e-4):
        for a in (0.5, 0.75, 1.0):
            R4, R6 = 2 - a - 4 * e, 2 - a - 6 * e
            tab[f'a={a},e={e}'] = math.log(R6 / 0.49) / math.log(R4 / 0.49)
    say('   theta(a,e) = log(R6/r0)/log(R4/r0):', {k: round(v, 6) for k, v in tab.items()})
    check('E0 theta < 1 for a in [1/2,1], e < 1e-3 (max at a = 1)', max(tab.values()) < 1, max(tab.values()))
    res['theta'] = tab
    lst = dirichlet_chars_prime(5)
    c1, c2 = frac_list_to_mp(lst), frac_list_to_mp(times_m3(lst))
    chi3 = [0, 1, -1]
    fams = {
        'chi_5 o N (Q=25)': (25, lambda s: mp.dirichlet(s, c1) * mp.dirichlet(s, c2),
                             lambda s: mp.dirichlet(s, c1, 1) / mp.dirichlet(s, c1) + mp.dirichlet(s, c2, 1) / mp.dirichlet(s, c2)),
        'principal (Q=1)': (1, lambda s: (s - 1) * mp.zeta(s) * mp.dirichlet(s, chi3) / (s + 1),
                            lambda s: 1 / (s - 1) - 1 / (s + 1) + mp.zeta(s, 1, 1) / mp.zeta(s) + mp.dirichlet(s, chi3, 1) / mp.dirichlet(s, chi3)),
    }
    a, e = 0.56, 9e-4
    R = {j: 2 - a - j * e for j in (2, 3, 4, 6, 8)}
    r0 = 0.49
    M = 96 if quick else 192
    for name, (Q, Lf, dL) in fams.items():
        for t in ([0.0] if quick else [0.0, 14.0]):
            c = mp.mpc(2, t)
            calC = 2 * Q * (3 + abs(t)) ** 2

            def circle_log(rad):
                # continuous log along the circle starting at the rightmost point (Euler region)
                vals = []
                prev = None
                for k in range(M + 1):
                    z = c + rad * mp.expjpi(2 * mp.mpf(k) / M)
                    v = Lf(z)
                    lg = mp.log(v)
                    if prev is not None:
                        while mp.im(lg) - mp.im(prev) > mp.pi:
                            lg -= 2j * mp.pi
                        while mp.im(lg) - mp.im(prev) < -mp.pi:
                            lg += 2j * mp.pi
                    vals.append(lg)
                    prev = lg
                return vals
            g2 = circle_log(R[2] - 1e-6)
            wind = float((mp.im(g2[-1]) - mp.im(g2[0])) / (2 * mp.pi))
            g3 = circle_log(R[3])
            g4 = circle_log(R[4])
            g6 = circle_log(R[6])
            g0 = circle_log(r0)
            gc = mp.log(Lf(c))
            maxRe3 = max(float(mp.re(v)) for v in g3)
            M4 = max(float(abs(v)) for v in g4)
            M6 = max(float(abs(v)) for v in g6)
            M0 = max(float(abs(v)) for v in g0)
            bc = 2 * R[4] / (R[3] - R[4]) * max(maxRe3, 0) + (R[3] + R[4]) / (R[3] - R[4]) * float(abs(gc))
            th = math.log(R[6] / r0) / math.log(R[4] / r0)
            hd = M0 ** (1 - th) * M4 ** th
            d8 = max(float(abs(dL(c + R[8] * mp.expjpi(2 * mp.mpf(k) / M)))) for k in range(M))
            cauchy = M6 / (R[6] - R[8])
            # bound for Re g on R3 from Lemma 4.8 (C=explicit constant from D)
            info = {'winding_R2': round(wind, 6), 'max Re g on R3': maxRe3, '|g(center)|': float(abs(gc)),
                    'max|g| R4': M4, 'B-C bound': bc, 'max|g| r0': M0, 'max|g| R6': M6,
                    'three-circles bound': hd, "max|g'| R8": d8, 'Cauchy bound': cauchy,
                    'log calC': math.log(calC)}
            res[f'{name}, t={t}'] = info
            say(f'   {name}, t={t}: ' + ', '.join(f'{k}={v:.4g}' if isinstance(v, float) else f'{k}={v}'
                                                for k, v in info.items()))
            check(f'E1 {name} t={t}: zero-free hypothesis (winding 0 on R2) and B-C, 3-circles, Cauchy '
                  f'inequalities hold numerically', abs(wind) < 1e-6 and M4 <= bc and M6 <= hd * (1 + 1e-9)
                  and d8 <= cauchy)
    OUT['E'] = res


# ----------------------------------------------------------------------------------------------
# F : Lemma 4.10
# ----------------------------------------------------------------------------------------------
def part_F(P):
    say('\n=== F: Lemma 4.10 deleted Euler factors (FLOAT) ===')
    rng = random.Random(20261010)
    norms = [N for p, N in P]
    bad = 0
    trials = 3000
    for _ in range(trials):
        k = rng.randint(1, 25)
        Rn = rng.sample(norms[:2000], k)
        ap = [cmath.rect(rng.random(), rng.uniform(0, 2 * math.pi)) for _ in Rn]
        s0 = rng.choice([0.05, 0.2, 0.5, 7 / 8])
        s = complex(s0 + rng.random() * 2, rng.uniform(-100, 100))
        D = 1
        dD = 0
        for q, a in zip(Rn, ap):
            D *= (1 - a * q ** (-s))
            dD += a * math.log(q) * q ** (-s) / (1 - a * q ** (-s))
        b1 = math.prod((1 - q ** (-s0)) ** -1 for q in Rn)
        b3 = sum(math.log(q) / (q ** s0 - 1) for q in Rn)
        sg = rng.uniform(-1, 2)
        s2 = complex(sg, rng.uniform(-50, 50))
        D2 = math.prod(abs(1 - a * q ** (-s2)) for q, a in zip(Rn, ap))
        qR = math.prod(Rn)
        b2 = qR ** max(-sg, 0) * 2 ** len(Rn)
        bad += not (abs(D) <= b1 * (1 + 1e-12) and 1 / abs(D) <= b1 * (1 + 1e-12)
                    and abs(dD) <= b3 * (1 + 1e-12) and D2 <= b2 * (1 + 1e-12)
                    and b3 <= math.log(2 * qR) / (2 ** s0 - 1))
    check('F1 |D_R^{+-1}| <= prod(1-q^-s0)^-1, |D\'/D| <= sum log q/(q^s0-1) <= log(2q_R)/(2^s0-1), '
          '|D_R(s)| <= q_R^{(-sigma)+} 2^{omega(R)}', bad == 0, f'{trials} random trials, {bad} violations')
    OUT['F'] = {'trials': trials, 'violations': bad}


# ----------------------------------------------------------------------------------------------
# B : Lemma 4.6
# ----------------------------------------------------------------------------------------------
def part_B():
    say('\n=== B: Lemma 4.6 Gaussian annular decomposition (FLOAT / MP) ===')
    res = {}

    def bump(u):
        u = np.asarray(u, dtype=float)
        out = np.zeros_like(u)
        m = np.abs(u) < 1
        out[m] = np.exp(-1.0 / (1 - u[m] ** 2))
        return out

    def chi(u):
        u = np.asarray(u, dtype=float)
        den = sum(bump(u - k) for k in range(-25, 26))    # periodic, > 0 for |u| < 24
        return np.where(den > 0, bump(u) / np.where(den > 0, den, 1), 0.0)
    uu = np.linspace(-5, 5, 20001)
    S = sum(chi(uu - k) for k in range(-8, 9))
    check('B1 sum_k chi(u-k) = 1 (normalized translates of a bump positive on [-1/2,1/2])',
          np.max(np.abs(S - 1)) < 1e-12, f'{np.max(np.abs(S-1)):.1e}')
    h = 1e-3
    u = np.arange(-1, 1 + h / 2, h)
    cu = chi(u)

    def deriv(f, j):
        g = f.copy()
        for _ in range(j):
            g = np.gradient(g, h, edge_order=2)
        return g
    ratios = {}
    psum = {}
    for j in (0, 1, 2, 3):
        rr = []
        tot = 0.0
        for k in range(-40, 41):
            G = np.exp(-(k + u) ** 2 / 4) / (2 * math.sqrt(math.pi))
            w = G * cu
            pj = sum(np.max(np.abs(deriv(w, i))) for i in range(j + 1))
            env = (1 + abs(k)) ** j * math.exp(-max(abs(k) - 1, 0) ** 2 / 4)
            rr.append(pj / env)
            tot += math.exp(5 * abs(k)) * pj
        ratios[j] = (max(rr[:30] + rr[51:]), max(rr[30:51]))
        psum[j] = tot
    say('   max p_j(w_k)/envelope: |k|>10 vs |k|<=10:', {j: (f'{a:.3g}', f'{b:.3g}') for j, (a, b) in ratios.items()})
    check('B2 p_j(w_k) <= C_j (1+|k|)^j exp(-((|k|-1)_+)^2/4): ratio bounded, not growing in |k| (j<=3)',
          all(a <= 1.5 * b for a, b in ratios.values()))
    check('B3 sum_k e^{5|k|} p_j(w_k) finite (|k|<=40 partial sums)', all(np.isfinite(v) for v in psum.values()),
          {j: f'{v:.3e}' for j, v in psum.items()})
    mp.mp.dps = 30
    errs = []
    for s in [mp.mpc(0.3, 2), mp.mpc(-1.2, 0.5), mp.mpc(2, -3)]:
        I = mp.quad(lambda x: mp.exp(-x * x / 4 + s * x), [-mp.inf, 0, mp.inf]) / (2 * mp.sqrt(mp.pi))
        errs.append(float(abs(I - mp.exp(s * s)) / abs(mp.exp(s * s))))
    check('B4 M W_G(s) = e^{s^2} with M W(s) = int W(y) y^s dy/y', max(errs) < 1e-20, f'{max(errs):.1e}')
    res = {'ratios': {j: list(v) for j, v in ratios.items()}, 'mellin_err': max(errs)}
    OUT['B'] = res


# ----------------------------------------------------------------------------------------------
# C : Lemma 4.7
# ----------------------------------------------------------------------------------------------
def part_C():
    say('\n=== C: Lemma 4.7 finite seminorms (symbolic + MP) ===')
    r = sympy.symbols('r', positive=True)
    x1, x2, x3 = sympy.symbols('x1 x2 x3', real=True)
    F = sympy.Function('F')
    ok = True
    for xs in ((x1, x2), (x1, x2, x3)):
        rr = sum(v ** 2 for v in xs)
        G = F(rr)
        lhs = sum(v * sympy.diff(G, v) for v in xs) / 2
        rhs = (r * sympy.diff(F(r), r)).subs(r, rr)
        ok &= sympy.simplify(lhs - rhs) == 0
    check('C1 radial: r d_r F(r) = (xi . d_xi)/2 [F(|xi|^2)] (d = 2, 3)', ok)
    mp.mp.dps = 20
    sigma, h = mp.mpf(0.5), 2
    m = lambda s: (s + 3) ** 2
    Cm = max(abs(m(mp.mpc(sigma, t))) / (1 + abs(t)) ** h for t in np.linspace(-60, 60, 1201))
    worst = 0
    for om in (0.0, 8.0):
        MW = lambda s: mp.exp((s - 1j * om) ** 2)      # M[W_G y^{i om}](-s) = e^{(s - i om)^2}
        for j in (0, 1, 2):
            Cj = max(abs(mp.mpc(sigma, t)) ** j / (1 + abs(t)) ** j for t in np.linspace(-60, 60, 1201))
            rhs_int = mp.quad(lambda t: abs(MW(mp.mpc(sigma, t))) * (1 + abs(t)) ** (h + j), [-mp.inf, om, mp.inf])
            for x in (0.05, 0.7, 3.0, 40.0):
                val = mp.quad(lambda t: MW(mp.mpc(sigma, t)) * m(mp.mpc(sigma, t)) * (-mp.mpc(sigma, t)) ** j
                              * mp.power(x, -mp.mpc(sigma, t)), [-mp.inf, om, mp.inf]) / (2 * mp.pi)
                bound = x ** (-sigma) * Cm * Cj * rhs_int / (2 * mp.pi)
                worst = max(worst, float(abs(val) / bound))
        if om:
            base = mp.quad(lambda t: abs(mp.exp(mp.mpc(sigma, t) ** 2)) * (1 + abs(t)) ** (h + 2), [-mp.inf, 0, mp.inf])
            tw = mp.quad(lambda t: abs(MW(mp.mpc(sigma, t))) * (1 + abs(t)) ** (h + 2), [-mp.inf, om, mp.inf])
            check('C3 twist costs at most (1+|omega|)^{h+j}', tw <= (1 + om) ** (h + 2) * base,
                  f'{float(tw/base):.3g} <= {(1+om)**(h+2):.3g}')
    check('C2 |(x d_x)^j K_W(x)| <= (1/2pi) x^-sigma C_m C_j int |MW(-sigma-it)|(1+|t|)^{h+j} dt '
          '(W_G, m=(s+3)^2, j<=2, omega in {0,8})', worst <= 1 + 1e-12, f'max ratio {worst:.3g}')
    OUT['C'] = {'max_ratio': worst}


# ----------------------------------------------------------------------------------------------
# G : Lemma 13.1
# ----------------------------------------------------------------------------------------------
def part_G(quick=False):
    say('\n=== G: Lemma 13.1 fixed-ray prime normalizer (EXACT counts, FLOAT sums; EMPIRICAL) ===')
    X = 2 * 10 ** 5 if quick else 2 * 10 ** 6
    t0 = time.time()
    P = prime_ideals(X)
    say(f'   prime ideals of norm <= {X}: {len(P)} ({time.time()-t0:.1f}s)')
    # ray class membership: trivial class of Cl_6 and Cl_12 (primary pi == 1 mod 6, resp. mod 12)
    def in_triv(pi, m):
        return divides((m, 0), (pi[0] - 1, pi[1]))
    # check identity of 1_{Cl_6} with kernel of (2/.)_3 on small primes (exact)
    okk = all(((2 * sym_prime(TWO, p)) % 6 == 0) == in_triv(p, 6) for p, N in P[:3000])
    check('G0 trivial class of Cl_6 = {p : (2/p)_3 = 1} (Lemma 4.1 + A2), first 3000 primes', okk)
    hcount = {6: ray_class_count((6, 0)), 12: ray_class_count((12, 0))}
    say('   |Cl_6| =', hcount[6], ' |Cl_12| =', hcount[12])

    def W(y):
        y = np.asarray(y, dtype=float)
        out = np.zeros_like(y)
        mk = (y > 1) & (y < 2)
        out[mk] = np.exp(-1.0 / ((y[mk] - 1) * (2 - y[mk])))
        return out
    yy = np.linspace(1, 2, 200001)
    IW = np.trapezoid(W(yy) * yy ** (-5 / 6), yy)
    qn = np.array([N for p, N in P], dtype=float)
    res = {}
    for m in (6, 12):
        mask = np.array([in_triv(p, m) for p, N in P])
        T = hcount[m]
        rows = []
        for Pv in ([10 ** 4, 5 * 10 ** 4] if quick else [10 ** 4, 10 ** 5, 10 ** 6]):
            lhs = float(np.sum(W(qn[mask] / Pv) * qn[mask] ** (-5 / 6)))
            main = Pv ** (1 / 6) / (T * math.log(Pv)) * IW
            xx = np.linspace(Pv, 2 * Pv, 200001)
            refined = float(np.trapezoid(W(xx / Pv) * xx ** (-5 / 6) / np.log(xx), xx) / T)
            rows.append((Pv, lhs / main, lhs / refined))
        res[f'Cl_{m}'] = rows
        say(f'   T=Cl_{m} (|T|={T}): (P, LHS/main, LHS/[int W(x/P)x^-5/6 dx/(|T|log x)]) =',
            [(a, round(b, 4), round(c, 4)) for a, b, c in rows])
        check(f'G1 Cl_{m}: LHS/refined -> 1 and LHS/main approaches 1 (slow log correction)',
              abs(rows[-1][2] - 1) < 0.05 and abs(rows[-1][1] - 1) < abs(rows[0][1] - 1) + 0.02)
    OUT['G'] = res


def main():
    t0 = time.time()
    kummer, P = part_A()
    part_B()
    part_C()
    part_D(kummer, quick=QUICK)
    part_E(quick=QUICK)
    part_F(P)
    part_G(quick=QUICK)
    OUT['fails'] = FAILS
    OUT['seconds'] = time.time() - t0
    say(f'\n{len(FAILS)} FAIL(s): {FAILS}' if FAILS else '\nALL PASS')
    say(f'total {time.time()-t0:.0f}s')
    js = [a for a in sys.argv[1:] if a.endswith('.json')]
    if js:
        with open(js[0], 'w') as fh:
            json.dump(OUT, fh, indent=1, default=str)


if __name__ == '__main__':
    main()
