#!/usr/bin/env python3
"""Checks for the Gaussian quartic envelope note (README.md in this directory).

Part A: exact finite identities for quartic Gauss sums over Z[i], computed in
        Z[i][zeta_N] with integer arithmetic (no floating point).
Part B: exact rational exponent bookkeeping for the two proof architectures,
        with the Eisenstein sextic arena as a control.

Standard library only.  Run:  python3 verify.py
It prints a JSON summary and exits nonzero if any check fails (also under -O).

What this does NOT do: it verifies no analytic continuation, functional
equation, large-sieve inequality or zero-free region.  Those are imported
inputs, named in the README.
"""
from fractions import Fraction as Fr
from math import gcd
import json
import sys

# --------------------------------------------------------------------------
# Part A.  Gaussian integers as (re, im) pairs of Python ints.
# --------------------------------------------------------------------------
I_POW = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def check(cond, info=None):
    """Like assert, but still active under python -O."""
    if not cond:
        raise SystemExit(f"CHECK FAILED: {info!r}")


def gmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def gconj(x):
    return (x[0], -x[1])


def gnorm(x):
    return x[0] * x[0] + x[1] * x[1]


def gpow(x, e):
    r = (1, 0)
    for _ in range(e):
        r = gmul(r, x)
    return r


def is_primary(c):
    """c = 1 mod (1+i)^3."""
    a, b = c
    return b % 2 == 0 and (a + b) % 4 == 1


def split_prime(p):
    """The two primary Gaussian primes of norm p (p = 1 mod 4)."""
    for a in range(1, p, 2):
        b2 = p - a * a
        if b2 <= 0:
            break
        b = int(round(b2 ** 0.5))
        if b * b == b2 and b % 2 == 0:
            out = []
            for bb in (b, -b):
                for s in (1, -1):
                    c = (s * a, s * bb)
                    if is_primary(c):
                        out.append(c)
            check(len(out) == 2)
            return out
    raise ValueError(p)


def inert_prime(q):
    c = (-q, 0)
    check(q % 4 == 3 and is_primary(c))
    return c


def chi_prime(pi):
    """Quartic residue symbol (x/pi)_4 for a primary prime pi.

    Returns f(x) -> exponent j with symbol = i^j, or None if pi | x.
    """
    a, b = pi
    if b != 0:  # split
        p = gnorm(pi)
        r = (-a * pow(b, -1, p)) % p  # image of i in Z[i]/pi = F_p
        table = {pow(r, j, p): j for j in range(4)}
        check(len(table) == 4)

        def f(x):
            t = (x[0] + x[1] * r) % p
            if t == 0:
                return None
            return table[pow(t, (p - 1) // 4, p)]
        return f
    q = abs(a)  # inert, residue field F_q[i]

    def fmul(u, v):
        return ((u[0] * v[0] - u[1] * v[1]) % q, (u[0] * v[1] + u[1] * v[0]) % q)

    targets = {(1, 0): 0, (0, 1): 1, (q - 1, 0): 2, (0, q - 1): 3}

    def f(x):
        t = (x[0] % q, x[1] % q)
        if t == (0, 0):
            return None
        e, base, r = (q * q - 1) // 4, t, (1, 0)
        while e:
            if e & 1:
                r = fmul(r, base)
            base = fmul(base, base)
            e >>= 1
        return targets[r]
    return f


class Modulus:
    """A primary modulus given by its prime factorization [(pi, e), ...]."""

    def __init__(self, factors):
        self.factors = list(factors)
        c = (1, 0)
        for pi, e in self.factors:
            c = gmul(c, gpow(pi, e))
        self.c = c
        self.N = gnorm(c)
        self._chi = [(chi_prime(pi), e) for pi, e in self.factors]
        check(is_primary(c))

    def chi(self, x):
        j = 0
        for f, e in self._chi:
            v = f(x)
            if v is None:
                return None
            j += v * e
        return j % 4

    def mu(self):
        if any(e > 1 for _, e in self.factors):
            return 0
        return (-1) ** len(self.factors)

    def residues(self):
        a, b = self.c
        g = gcd(a, b)
        for u in range(self.N // g):
            for v in range(g):
                yield (u, v)


# ---- the ring Z[i][x]/(x^N - 1); elements are dicts {t: (re, im)} --------
def radd(A, B, sign=1):
    C = dict(A)
    for t, v in B.items():
        w = C.get(t, (0, 0))
        w = (w[0] + sign * v[0], w[1] + sign * v[1])
        if w == (0, 0):
            C.pop(t, None)
        else:
            C[t] = w
    return C


def rscale(A, s):
    return {t: gmul(v, s) for t, v in A.items() if gmul(v, s) != (0, 0)}


def rmul(A, B, N):
    C = {}
    for t1, v1 in A.items():
        for t2, v2 in B.items():
            t = (t1 + t2) % N
            w = gmul(v1, v2)
            o = C.get(t, (0, 0))
            C[t] = (o[0] + w[0], o[1] + w[1])
    return {t: v for t, v in C.items() if v != (0, 0)}


def rconj(A, N):
    return {(-t) % N: gconj(v) for t, v in A.items()}


def rembed(A, M, N):
    """zeta_M = zeta_N^(N/M)."""
    check(N % M == 0)
    k = N // M
    return {(t * k) % N: v for t, v in A.items()}


def prime_powers(N):
    out, p = [], 2
    while p * p <= N:
        if N % p == 0:
            q = 1
            while N % p == 0:
                N //= p
                q *= p
            out.append((p, q))
        p += 1
    if N > 1:
        out.append((N, N))
    return out


def is_zero(A, N):
    """Exact test that A represents 0 in Z[i, zeta_N] (N odd).

    Writes zeta_N^t as a product of zeta_{p^e} powers and reduces each
    direction by 1 + z^(p^(e-1)) + ... + z^((p-1)p^(e-1)) = 0, which leaves
    coordinates in the tensor-product integral basis.
    """
    check(N % 2 == 1)
    pps = prime_powers(N)
    inv = [pow(N // q, -1, q) for _, q in pps]
    cur = {}
    for t, v in A.items():
        key = tuple((t * inv[i]) % q for i, (_, q) in enumerate(pps))
        cur[key] = v
    for i, (p, q) in enumerate(pps):
        step = q // p
        nxt = {}
        for key, v in cur.items():
            j, rho = divmod(key[i], step)
            if j < p - 1:
                o = nxt.get(key, (0, 0))
                nxt[key] = (o[0] + v[0], o[1] + v[1])
            else:
                for jj in range(p - 1):
                    k2 = key[:i] + (jj * step + rho,) + key[i + 1:]
                    o = nxt.get(k2, (0, 0))
                    nxt[k2] = (o[0] - v[0], o[1] - v[1])
        cur = {k: v for k, v in nxt.items() if v != (0, 0)}
    return not cur


def gauss(m, r, conj_char=False):
    """g_4(r, c) = sum_{x mod c} (x/c)_4 e(Tr(r x / c)) in Z[i][zeta_N]."""
    N, cbar = m.N, gconj(m.c)
    rc = gmul(r, cbar)
    A = {}
    for x in m.residues():
        j = m.chi(x)
        if j is None:
            continue
        if conj_char:
            j = (-j) % 4
        t = (2 * gmul(rc, x)[0]) % N
        o = A.get(t, (0, 0))
        w = I_POW[j]
        A[t] = (o[0] + w[0], o[1] + w[1])
    return {t: v for t, v in A.items() if v != (0, 0)}


def sqrt_norm(m):
    """sqrt(N(c)) as an element of Z[zeta_N] (squarefree c)."""
    N = m.N
    A = {0: (1, 0)}
    for pi, e in m.factors:
        check(e == 1)
        if pi[1] == 0:
            A = rscale(A, (abs(pi[0]), 0))
            continue
        p = gnorm(pi)
        G = {}
        for x in range(1, p):
            s = 1 if pow(x, (p - 1) // 2, p) == 1 else -1
            G[(x * (N // p)) % N] = (s, 0)
        A = rmul(A, G, N)
    return A


def part_a():
    P5, P5b = split_prime(5)
    P13, P13b = split_prime(13)
    P17, P17b = split_prime(17)
    P29, _ = split_prime(29)
    Q3, Q7 = inert_prime(3), inert_prime(7)
    report = {}

    # A1. Codec: g_4(c)^2 = mu(c) c sqrt(N c) for primary squarefree c.
    mods = [[(P5, 1)], [(P5b, 1)], [(P13, 1)], [(P17b, 1)], [(P29, 1)],
            [(Q3, 1)], [(Q7, 1)], [(P5, 1), (P13, 1)], [(P5, 1), (P5b, 1)],
            [(P5, 1), (Q3, 1)], [(P13b, 1), (P17, 1)], [(P5, 1), (P13, 1), (Q3, 1)]]
    n = 0
    for fac in mods:
        m = Modulus(fac)
        g = gauss(m, (1, 0))
        lhs = rmul(g, g, m.N)
        rhs = rscale(sqrt_norm(m), gmul((m.mu(), 0), m.c))
        check(is_zero(radd(lhs, rhs, -1), m.N), ("codec", fac))
        # negative controls: wrong sign, and conj(c) in place of c
        check(not is_zero(radd(lhs, rhs, 1), m.N))
        if m.c[1] != 0:
            wrong = rscale(sqrt_norm(m), gmul((m.mu(), 0), gconj(m.c)))
            check(not is_zero(radd(lhs, wrong, -1), m.N))
        check(is_zero(radd(rmul(g, rconj(g, m.N), m.N), {0: (m.N, 0)}, -1), m.N))  # |g|^2 = N
        # consequence used after Poisson: mu g sqrt(N) = c conj(g)
        lhs2 = rscale(rmul(g, sqrt_norm(m), m.N), (m.mu(), 0))
        rhs2 = rscale(rconj(g, m.N), m.c)
        check(is_zero(radd(lhs2, rhs2, -1), m.N), ("codec2", fac))
        n += 1
    report["A1_codec_moduli"] = n

    # A2. Orientation: g(k, c) = conj(chi_c(k)) g(1, c); g(k^3, c) = chi_c(k) g(1, c).
    #     The two differ exactly when chi_c(k)^2 = -1.
    n = diff = 0
    ks = [P5, P5b, P13, P17, Q3, (1, 2), (3, 0), (2, 1), (1, 4)]
    for fac in mods[:8]:
        m = Modulus(fac)
        g1 = gauss(m, (1, 0))
        for k in ks:
            j = m.chi(k)
            if j is None:
                continue
            nat = gauss(m, k)
            phys = gauss(m, gpow(k, 3))
            check(is_zero(radd(nat, rscale(g1, I_POW[(-j) % 4]), -1), m.N))
            check(is_zero(radd(phys, rscale(g1, I_POW[j]), -1), m.N))
            same = is_zero(radd(nat, phys, -1), m.N)
            check(same == (j % 2 == 0))
            diff += (not same)
            n += 1
    report["A2_orientation_pairs"] = n
    report["A2_pairs_where_native_differs_from_physical"] = diff

    # A3. Local values at a prime dividing the row: g(m p^3, p^j).
    for p in (P5, P5b):
        Np = gnorm(p)
        for mult in ((1, 0), P13, Q3):
            num = gmul(mult, gpow(p, 3))
            for j in range(1, 6):
                m = Modulus([(p, j)])
                g = gauss(m, num)
                expect = {0: (-Np ** 3, 0)} if j == 4 else {}
                check(is_zero(radd(g, expect, -1), m.N), ("local", p, mult, j))
    report["A3_local_values"] = "g(m p^3, p^j) = 0, 0, 0, -N(p)^3, 0 for j = 1..5"

    # A4. Twisted multiplicativity and quartic reciprocity.
    pairs = [(P5, P13), (P5, P5b), (P13, P17b), (P5, Q3), (Q3, Q7), (P17, Q3), (P29, P5b)]
    for c1, c2 in pairs:
        m1, m2, m12 = Modulus([(c1, 1)]), Modulus([(c2, 1)]), Modulus([(c1, 1), (c2, 1)])
        j12, j21 = m1.chi(c2), m2.chi(c1)
        sign = (((m1.N - 1) // 4) * ((m2.N - 1) // 4)) % 2
        check((j12 - j21) % 4 == 2 * sign, ("reciprocity", c1, c2))
        for r in ((1, 0), (2, 1), gpow(P29, 3)):
            if m12.chi(r) is None:
                continue
            N = m12.N
            prod = rmul(rembed(gauss(m1, r), m1.N, N), rembed(gauss(m2, r), m2.N, N), N)
            rhs = rscale(prod, I_POW[(j12 + j21) % 4])
            check(is_zero(radd(gauss(m12, r), rhs, -1), N), ("twisted", c1, c2, r))
    report["A4_twisted_multiplicativity_pairs"] = len(pairs)

    # A5. Row Poisson coefficient for a coprime pair (c, d):
    #     sum_u chi_c(u) conj(chi_d(u)) e(Tr(k u / cd))
    #       = chi_c(d) conj(chi_d(c)) g(k, c) conj(g(-k, d)),
    #     and mu(c) g(k, c) sqrt(N c) = c conj(g(k^3, c)).
    n = 0
    for c, d in [(P5, P13), (P13, P5b), (P5, Q3), (P17, P5)]:
        mc, md, mcd = Modulus([(c, 1)]), Modulus([(d, 1)]), Modulus([(c, 1), (d, 1)])
        N, cdbar = mcd.N, gconj(mcd.c)
        for k in ((1, 0), (1, 2), (3, 2), P29):
            if mcd.chi(k) is None:
                continue
            lhs = {}
            kc = gmul(k, cdbar)
            for u in mcd.residues():
                jc, jd = mc.chi(u), md.chi(u)
                if jc is None or jd is None:
                    continue
                t = (2 * gmul(kc, u)[0]) % N
                o = lhs.get(t, (0, 0))
                w = I_POW[(jc - jd) % 4]
                lhs[t] = (o[0] + w[0], o[1] + w[1])
            gc = rembed(gauss(mc, k), mc.N, N)
            gd = rembed(rconj(gauss(md, (-k[0], -k[1])), md.N), md.N, N)
            rhs = rscale(rmul(gc, gd, N), I_POW[(mc.chi(d) - md.chi(c)) % 4])
            check(is_zero(radd(lhs, rhs, -1), N), ("poisson", c, d, k))
            a = rscale(rmul(gauss(mc, k), sqrt_norm(mc), mc.N), (mc.mu(), 0))
            b = rscale(rconj(gauss(mc, gpow(k, 3)), mc.N), mc.c)
            check(is_zero(radd(a, b, -1), mc.N), ("cube numerator", c, k))
            n += 1
    report["A5_poisson_instances"] = n

    # A6. One instance of the local factor behind (Q2): for p | k, p^3 || k^3,
    #     g(k^3, p^4 c') = -N(p)^3 g(k^3, c') and g(k^3, p^j c') = 0 otherwise.
    p = P5
    num = gpow(p, 3)
    for cp in (Q3, P13):
        base = gauss(Modulus([(cp, 1)]), num)
        for j in (1, 2, 3, 4):
            m = Modulus([(p, j), (cp, 1)])
            expect = rscale(rembed(base, gnorm(cp), m.N), (-gnorm(p) ** 3, 0)) if j == 4 else {}
            check(is_zero(radd(gauss(m, num), expect, -1), m.N), ("Q2", cp, j))
    report["A6_local_factor"] = "1 - N(p)^(3-4s) on raw moduli, i.e. 1 - N(p)^(1-4s) normalized"
    return report


# --------------------------------------------------------------------------
# Part B.  Exponent bookkeeping.  All quantities are exponents of one scale.
# --------------------------------------------------------------------------
def theta_quad(k, y):
    """Quadratic large sieve, rows K = D^k, columns Y = D^y: K + Y."""
    return max(k, y)


def theta_sextic(k, y):
    """Sextic sieve as used in the OpenAI 7/8 paper, Lemma 9.1: K + Y + (KY)^(2/3)."""
    return max(k, y, Fr(2, 3) * (k + y))


def theta_quartic(k, y):
    """de Faveri arXiv:2610.04045 Thm 1.1 as recorded in riemann PR 1019 (Q4):
    K + Y + K^(3/4) Y^(1/2) + K^(1/2) Y^(3/4)."""
    return max(k, y, Fr(3, 4) * k + Fr(1, 2) * y, Fr(1, 2) * k + Fr(3, 4) * y)


ARENAS = {
    # m: amplifier order (rows p^m are copies); d: degree of the Poisson-dual
    # family in the row aspect (row k has conductor N(k)^d); direct: sieve for
    # the dual family as it stands; refl: sieve available after reflection.
    "eisenstein_sextic": dict(m=6, d=2, direct=theta_sextic, refl=theta_quad),
    "gaussian_quartic": dict(m=4, d=3, direct=theta_quartic, refl=theta_quartic),
}


def dual_rows(arena, k, length=Fr(1)):
    """Best-case exponent of sum_{N(k) ~ D^k} |S_k|^2 for normalized dual
    column sums of length D^length: the better of the sieve as it stands and
    a lossless reflection to length D^(d k - length) followed by the sieve."""
    direct = arena["direct"](k, length)
    refl_len = arena["d"] * k - length
    if refl_len > length:  # reflection lengthens the sum
        return direct
    return min(direct, arena["refl"](k, max(refl_len, Fr(0))))


def mean_square_architecture(arena, step=Fr(1, 9240)):
    """Rows u <= H = D^a, columns n ~ D.  Normalized:
         sum_u |M_u|^2  <=  H + (H/D) sum_{N(k) <= D^2/H} |S_k|^2,
       then |M_1|^2 <= (that) / H^(1/m); the trivial bound is exponent 1.
       Returns (min exponent of |M_1|^2, argmin a, table of E(a))."""
    ks = [i * step for i in range(int(2 / step) + 1)]
    sig, run = {}, Fr(0)
    for k in ks:
        run = max(run, dual_rows(arena, k))
        sig[k] = run
    best, arg, table = None, None, {}
    for a in ks:
        E = max(a, a - 1 + sig[2 - a])
        P = E - a / arena["m"]
        table[a] = E
        if best is None or P < best:
            best, arg = P, a
    return best, arg, table


def row_count(arena_name, delta):
    """R(delta): exponent of the number of rows u ~ U whose inverse polynomial
    of length U^r (1/2 <= r <= 1) has size^2 >= U^(delta r), from the sieve."""
    th = theta_sextic if arena_name == "eisenstein_sextic" else theta_quartic
    # theta(1, r) - delta r is piecewise linear in r; its max over [1/2, 1] is
    # at an endpoint or a kink, all of which lie on the grid below.
    cands = [Fr(1, 2) + Fr(i, 24) for i in range(13)]
    return min(Fr(1), max(th(Fr(1), r) - delta * r for r in cands))


def three_scale_point(name, lx, ly, beta_grid=120):
    """Transplant of Part I of the 7/8 paper (probe I(X, Y, Z), X = Z^lx,
    Y = Z^ly, completed Gauss index at scale Z, rows m ~ XY, dual rows u up
    to Z/X).  Returns (LOW abscissa, least grid beta passing HIGH or None)."""
    arena = ARENAS[name]
    z0 = Fr(1, arena["m"])
    q = lx + ly
    eB = dual_rows(arena, q)
    low_exp = -q / 2 + max(q, 2 * ly) / 2 - ly / 2 + eB / 2
    low = (1 - z0) - lx * (Fr(1, 2) - z0) + low_exp
    for ib in range(beta_grid // 2 + 1, beta_grid + 1):
        beta = Fr(ib, beta_grid)
        if high_holds(name, lx, ly, beta):
            return low, beta
    return low, None


_DELTAS = [Fr(i, 120) for i in range(121)]
_ROWS = {}


def high_holds(name, lx, ly, beta):
    """HIGH: g(delta) < beta for every bin delta <= 2 beta - 1, where
    g = (1 + delta)(1 - ly)/2 + (1 - lx)(R(delta) + delta/2 - 1/m)."""
    if name not in _ROWS:
        _ROWS[name] = {dl: row_count(name, dl) for dl in _DELTAS}
    z0 = Fr(1, ARENAS[name]["m"])
    top = 2 * beta - 1
    for dl in _DELTAS + [top]:
        if dl > top:
            continue
        R = _ROWS[name][dl] if dl in _ROWS[name] else row_count(name, dl)
        if (1 + dl) * (1 - ly) / 2 + (1 - lx) * (R + dl / 2 - z0) >= beta:
            return False
    return True


def three_scale_architecture(name, grid=40):
    """Least max(LOW, HIGH) over the scale grid, with every grid point's
    (lx, ly, LOW, HIGH)."""
    best, pts = None, []
    for ix in range(grid + 1):
        for iy in range(grid + 1):
            lx, ly = Fr(ix, grid), Fr(iy, grid)
            if lx + ly == 0:
                continue
            low, high = three_scale_point(name, lx, ly)
            pts.append((lx, ly, low, high))
            if high is not None and (best is None or max(low, high) < best):
                best = max(low, high)
    return best, pts


def part_b():
    rep = {}

    # B1. Mean-square architecture.
    P6, a6, _ = mean_square_architecture(ARENAS["eisenstein_sextic"])
    check(P6 == Fr(5, 6) and a6 == 1, (P6, a6))
    rep["B1_sextic_control"] = {"min_exponent_of_M1_squared": str(P6), "at_a": str(a6),
                                "zero_free_abscissa": str(Fr(1, 2) + P6 / 2)}
    P4, a4, tab = mean_square_architecture(ARENAS["gaussian_quartic"])
    check(P4 == 1, P4)  # exactly the trivial bound
    for a in (Fr(0), Fr(1, 2), Fr(1)):
        check(tab[a] == 1 + a / 4)  # principal fourth-power rows, bounded trivially
    check(tab[Fr(1)] == Fr(5, 4))
    check(tab[Fr(4, 3)] == Fr(17, 12))
    # (R) with square-root cancellation, E(a) = a, starts only at a = 15/11:
    first = min(a for a, E in tab.items() if E == a and a > 0)
    check(first == Fr(15, 11), first)
    # the fourth-power amplifier is nontrivial only for a < 4/3 < 15/11.
    check(all(E - a / 4 >= 1 for a, E in tab.items()))
    check(all(E - a / 4 > 1 for a, E in tab.items() if a > 1))
    rep["B1_quartic"] = {"min_exponent_of_M1_squared": str(P4),
                         "attained_for_a_in": "[0, 1]",
                         "E(1)": str(tab[Fr(1)]), "E(4/3)": str(tab[Fr(4, 3)]),
                         "sqrt_cancellation_from_a": str(first),
                         "amplifier_nontrivial_below_a": "4/3"}

    # B1b. Without any reflection (sieve applied to the annular sum as it stands)
    #      square-root cancellation starts at a = 3/2; this part uses only (Q4).
    never = dict(m=4, d=99, direct=theta_quartic, refl=theta_quartic)
    Pn, _, tabn = mean_square_architecture(never)
    check(Pn == 1 and min(a for a, E in tabn.items() if E == a and a > 0) == Fr(3, 2))
    check(all(tabn[a] == tab[a] for a in tab if a <= Fr(4, 3)))  # reflection is idle below 4/3
    rep["B1b_quartic_direct_sieve_only"] = {"sqrt_cancellation_from_a": "3/2",
                                            "same_as_best_case_for_a_up_to": "4/3"}
    #      Comparison with riemann PR 1019, PHYSICAL_QUARTIC_CUBIC_ROW_MEAN.md (Q12):
    #      exponent a - 1 + 2 delta + (2 - a) max(1, 13/8 - 3 delta), 0 < delta < 1/4.
    def q12(a):
        return min(a - 1 + 2 * dl + (2 - a) * max(Fr(1), Fr(13, 8) - 3 * dl)
                   for dl in [Fr(i, 240) for i in range(1, 60)])
    check(q12(Fr(1)) == Fr(17, 12) and tab[Fr(1)] == Fr(5, 4))
    check(all(tab[a] <= q12(a) for a in [Fr(i, 12) for i in range(0, 17)]))
    rep["B1c_versus_PR1019_Q12"] = {"Q12_at_a=1": "17/12", "direct_sieve_at_a=1": "5/4",
                                    "target_at_a=1": "1"}

    # B2. Idealized variant: pretend the reflected quartic family obeyed the
    #     quadratic sieve K + Y.  Degree 3 alone still gives zero margin.
    ideal = dict(m=4, d=3, direct=theta_quartic, refl=theta_quad)
    Pi, ai, tabi = mean_square_architecture(ideal)
    check(Pi == 1)
    check(min(a for a, E in tabi.items() if E == a and a > 0) == Fr(4, 3))
    rep["B2_quartic_with_ideal_dual_sieve"] = {"min_exponent_of_M1_squared": str(Pi),
                                               "sqrt_cancellation_from_a": "4/3"}
    #     Conversely degree 2 with the quartic sieve would already work.
    deg2 = dict(m=4, d=2, direct=theta_quartic, refl=theta_quartic)
    Pd, ad, _ = mean_square_architecture(deg2)
    check(Pd == Fr(6, 7) and ad == Fr(8, 7), (Pd, ad))
    rep["B2_hypothetical_degree_2_quartic"] = {"min_exponent_of_M1_squared": str(Pd),
                                               "at_a": str(ad)}

    # B3. Three-scale architecture (transplant of Part I of the 7/8 paper).
    half, tiny = Fr(1, 2), Fr(1, 1000)
    b6, pts6 = three_scale_architecture("eisenstein_sextic")
    check(b6 == Fr(11, 12), b6)
    low6, _ = three_scale_point("eisenstein_sextic", half, half)
    check(low6 == Fr(11, 12))  # i.e. I << Z^(1/4), Proposition 6.3
    # HIGH threshold at balanced scales is exactly 5/6 (open condition)
    check(not high_holds("eisenstein_sextic", half, half, Fr(5, 6)))
    check(high_holds("eisenstein_sextic", half, half, Fr(5, 6) + tiny))
    rep["B3_sextic_control"] = {"least_abscissa": str(b6), "at": "lx = ly = 1/2",
                                "LOW": str(low6), "HIGH_threshold": "5/6"}
    b4, pts4 = three_scale_architecture("gaussian_quartic")
    check(b4 == 1, b4)
    low4, _ = three_scale_point("gaussian_quartic", half, half)
    check(low4 == 1)
    check(not high_holds("gaussian_quartic", half, half, Fr(3, 4)))
    check(high_holds("gaussian_quartic", half, half, Fr(3, 4) + tiny))
    # LOW < 1 forces lx + ly < 2/3; HIGH < 1 forces lx + ly > 2/3.
    for lx, ly, low, high in pts4:
        check(not (low < 1) or lx + ly < Fr(2, 3), ("LOW", lx, ly))
        check(high is None or lx + ly > Fr(2, 3), ("HIGH", lx, ly))
        check(high is None or low >= 1, ("both", lx, ly))
    rep["B3_quartic"] = {"least_abscissa": str(b4), "at": "lx = ly = 1/2",
                         "LOW": str(low4), "HIGH_threshold": "3/4",
                         "LOW_below_1_requires": "lx + ly < 2/3",
                         "HIGH_below_1_requires": "lx + ly > 2/3"}

    # B4. The structural criterion (m - 2)/(m - 1) < 2/d.
    crit = {}
    for label, (m, d) in {"sextic over Q(omega)": (6, 2), "quartic over Q(i)": (4, 3),
                          "order 10 over Q(zeta_5)": (10, 4), "order 14 over Q(zeta_7)": (14, 6)}.items():
        lhs, rhs = Fr(m - 2, m - 1), Fr(2, d)
        crit[label] = {"amplifier_needs_K_above_D^": str(lhs),
                       "reflection_needs_K_below_D^": str(rhs),
                       "verdict": "open window" if lhs < rhs else ("zero margin" if lhs == rhs else "closed")}
    check(crit["sextic over Q(omega)"]["verdict"] == "open window")
    check(crit["quartic over Q(i)"]["verdict"] == "zero margin")
    rep["B4_criterion"] = crit

    # B5. What would revive the quartic arena: beat the K^(3/4) Y^(1/2) term.
    #     Needed exponent for sum_{N(k) <= D^kappa} |S_k(D)|^2, kappa = 2 - a:
    #     strictly below 3 kappa/4 + 1/2, for some kappa in (2/3, 2).
    for a in (Fr(1), Fr(5, 4), Fr(1, 2)):
        kappa = 2 - a
        need = 1 + a / 4 - (a - 1)  # from a - 1 + s < 1 + a/4
        check(need == Fr(3, 4) * kappa + Fr(1, 2))
    rep["B5_reviving_lemma"] = "sum_{N(k)<=K} |S_k(D)|^2 << D^(-eta) K^(3/4) D^(1/2) for some D^(2/3) < K < D^2"
    return rep


def main():
    out = {"part_A_exact_identities": part_a(), "part_B_exponents": part_b()}
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
