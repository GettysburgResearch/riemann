"""Finite exact checks for A4_NO_OLDER_MOVING.md (cubic transcription, n = 3).

Status: EXPLORATION / finite exact checks on small moduli in Z[omega].  They illustrate the
        statements of A4_NO_OLDER_MOVING.md; they do not prove them.  All arithmetic is exact
        (integers and Z[omega] elements stored as pairs (a, b) = a + b*omega).
Run:    python3 -I a4_checks.py
Inputs: none (self-contained; no repository module is imported).

Tags
  [K1]       complete-support correlation at n = 3 (R == 1):
             F(Da, Eb; j) == F(D, E; j) * chi_a(j) * conj(chi_b(-j)), brute-force congruence sums.
             Consequence used: the residual column variable meets the extracted primes p | DE
             only through chi_a(j); no character attached at p acts on the residual column.
  [K1-CTRL]  the formula keeping the un-cancelled factor conj(chi_a(E)) chi_b(D) (a moving
             character attached at the primes of D, E) must FAIL.
  [K2]       every displayed moving residue-symbol factor attached at q (both orientations,
             composite moving moduli, zero-retained principal power) vanishes on every column
             u with q | u; hence it kills every allocation u = D_2 a with q | D_2.
  [K2-CTRL]  a "unit-part extension" chi_q(u / q^{v_q(u)})^e does NOT vanish there.
  [K3]       forced residue at a nonunit i = 1 prime: n -> chi_p(n)^{e_old} chi_n(p^{2+k}) is an
             S-ray character (constant on primary primes in each class mod 18) iff
             e_old + 2 + k == 0 mod 3.  With e_old = 0 (A4) the residue is k == 1 mod 3.
  [K3-CTRL]  e_old = 1 (a hypothetical surviving older character) moves the residue to 0 mod 3.
  [K4]       ledger cost table (Fractions): per-prime F_2 at nonunit i = 1 is 2/3 + r_p/3.
  [K5]       cubic reciprocity chi_a(b) == chi_b(a) on distinct good primary primes (R == 1).
  [K5-CTRL6] the sextic symbol violates chi_a(b) == chi_b(a) for some pair (R != 1 at n = 6).
"""
import sys
from fractions import Fraction as Fr
from math import gcd
sys.dont_write_bytecode = True

RESULTS = []


def report(tag, ok, msg, control=False):
    # for a control, ok = True means the wrong rule was detected (it fails, as it must)
    RESULTS.append((tag, bool(ok), control))
    kind = 'CTRL' if control else 'CHECK'
    print(f"[{tag}] {kind} {'PASS' if ok else 'FAIL'}: {msg}")


# ---------------------------------------------------------------------------------------------
# Z[omega] arithmetic, omega^2 = -1 - omega
# ---------------------------------------------------------------------------------------------
def mul(x, y):
    a, b = x
    c, d = y
    return (a * c - b * d, a * d + b * c - b * d)


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def neg(x):
    return (-x[0], -x[1])


def conj(x):
    return (x[0] - x[1], -x[1])


def norm(x):
    return x[0] * x[0] - x[0] * x[1] + x[1] * x[1]


def divexact(z, m):
    """z / m if m | z in O, else None."""
    t = mul(z, conj(m))
    n = norm(m)
    if t[0] % n or t[1] % n:
        return None
    return (t[0] // n, t[1] // n)


def is_primary(x):
    return x[0] % 3 == 1 and x[1] % 3 == 0


UNITS = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1)]  # 1,-1,w,-w,w^2,-w^2
MU3 = [(1, 0), (0, 1), (-1, -1)]                              # 1, w, w^2 (exponent index)
MU6 = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]   # zeta6^k, zeta6 = -w^2 = 1 + w


def primary_assoc(x):
    for u in UNITS:
        y = mul(u, x)
        if is_primary(y):
            return y
    return None


def egcd(a, b):
    if b == 0:
        return (a, 1, 0) if a >= 0 else (-a, -1, 0)
    g, s, t = egcd(b, a % b)
    return g, t, s - (a // b) * t


_HNF = {}


def hnf(m):
    """Basis (g, y), (0, c) of the Z-lattice (m), g*c = N(m)."""
    if m in _HNF:
        return _HNF[m]
    v1 = m
    v2 = mul(m, (0, 1))
    g, s, t = egcd(v1[0], v2[0])
    w1 = (s * v1[0] + t * v2[0], s * v1[1] + t * v2[1])
    if g == 0:
        raise ValueError
    w2y = (v2[0] // g) * v1[1] - (v1[0] // g) * v2[1]
    c = abs(w2y)
    assert w1[0] == g and g * c == norm(m), (m, g, c)
    _HNF[m] = (g, w1[1], c)
    return _HNF[m]


def red(z, m):
    g, y, c = hnf(m)
    k = z[0] // g
    return (z[0] - k * g, (z[1] - k * y) % c)


def residues(m):
    g, y, c = hnf(m)
    return [(x0, y0) for x0 in range(g) for y0 in range(c)]


def powmod(z, e, m):
    r = red((1, 0), m)
    b = red(z, m)
    while e:
        if e & 1:
            r = red(mul(r, b), m)
        b = red(mul(b, b), m)
        e >>= 1
    return r


# primes of O outside S = {(2), (lambda)}, primary generators
def primes_upto(B):
    out = []
    seen = set()
    R = int(B ** 0.5) + 3
    for a in range(-R, R + 1):
        for b in range(-R, R + 1):
            x = (a, b)
            n = norm(x)
            if n < 2 or n > B or not is_primary(x):
                continue
            ok = False
            if all(n % d for d in range(2, int(n ** 0.5) + 1)) and n % 3 == 1:
                ok = True
            else:
                r = int(round(n ** 0.5))
                if r * r == n and r % 3 == 2 and r != 2 and all(r % d for d in range(2, int(r ** 0.5) + 1)):
                    ok = True
            if ok and x not in seen:
                seen.add(x)
                out.append(x)
    out.sort(key=lambda x: (norm(x), x))
    return out


PRIMES = primes_upto(3000)


def factor(z):
    """factorization of a primary good element as {prime: exponent}; None if an S-prime divides."""
    f = {}
    n = norm(z)
    for p in PRIMES:
        if norm(p) > n:
            break
        while True:
            w = divexact(z, p)
            if w is None:
                break
            f[p] = f.get(p, 0) + 1
            z = w
            n = norm(z)
    if n != 1:
        return None
    return f


def sym_prime(x, p, order=3):
    """residue symbol (x/p)_order as exponent index into MU3 (order 3) or MU6 (order 6); None if p | x."""
    if divexact(x, p) is not None:
        return None
    P = norm(p)
    r = powmod(x, (P - 1) // order, p)
    table = MU3 if order == 3 else MU6
    for k, u in enumerate(table):
        if red(u, p) == r:
            return k
    raise AssertionError("symbol not a root of unity", x, p)


_FAC = {}


def chi(m, x, order=3):
    """chi_m(x) = (x/m)_order for primary good m, exponent mod order; None = zero."""
    if m not in _FAC:
        _FAC[m] = factor(m)
    fm = _FAC[m]
    e = 0
    for p, k in fm.items():
        s = sym_prime(x, p, order)
        if s is None:
            return None
        e += k * s
    return e % order


def zw_from_counts(cnt):
    # sum_k cnt[k] w^k  ->  element of Z[omega]
    z = (0, 0)
    for k, c in enumerate(cnt):
        z = add(z, (MU3[k][0] * c, MU3[k][1] * c))
    return z


def wpow(e):
    return MU3[e % 3]


# ---------------------------------------------------------------------------------------------
# [K1] complete-support correlation at n = 3
# ---------------------------------------------------------------------------------------------
def F_brute(u, v, j):
    """F(u,v;j) = sum_{x mod u, y mod v, v x - u y == j (mod uv)} chi_u(x) conj(chi_v(y))."""
    uv = mul(u, v)
    ru = residues(u)
    rv = residues(v)
    cu = [chi(u, x) for x in ru]
    cv = [chi(v, y) for y in rv]
    target = red(j, uv)
    cnt = [0, 0, 0]
    vys = [red(mul(u, y), uv) for y in rv]
    for x, ex in zip(ru, cu):
        if ex is None:
            continue
        vx = red(mul(v, x), uv)
        for y, ey, uy in zip(rv, cv, vys):
            if ey is None:
                continue
            if red((vx[0] - uy[0], vx[1] - uy[1]), uv) == target:
                cnt[(ex - ey) % 3] += 1
    return zw_from_counts(cnt)


def times_sym(z, e):
    """z * w^e, or 0 if e is None."""
    if e is None:
        return (0, 0)
    return mul(z, wpow(e))


def times_conj_sym(z, e):
    if e is None:
        return (0, 0)
    return mul(z, wpow(-e))


def k1():
    P7 = [p for p in PRIMES if norm(p) == 7]
    P13 = [p for p in PRIMES if norm(p) == 13]
    P19 = [p for p in PRIMES if norm(p) == 19]
    p, pb = P7[0], P7[1]
    a13, b19 = P13[0], P19[0]
    configs = []
    # (label, D, E, a, b)
    configs.append(("i=1 equal, D=E=p", p, p, a13, b19))
    configs.append(("i=1 equal, a=1", p, p, (1, 0), b19))
    configs.append(("i=2 equal, D=E=p^2, b=1", mul(p, p), mul(p, p), a13, (1, 0)))
    configs.append(("D=p*pbar, E=p", mul(p, pb), p, a13, (1, 0)))
    configs.append(("unequal D=p^2, E=p", mul(p, p), p, a13, (1, 0)))
    configs.append(("D=p, E=P13", p, P13[1], P19[1], (1, 0)))
    ok_all = True
    ctrl_detected = False
    ntests = 0
    nonzero = 0
    for lab, D, E, a, b in configs:
        G = (1, 0)
        # common part for frequencies
        for q, k in (factor(D) or {}).items():
            kE = (factor(E) or {}).get(q, 0)
            for _ in range(min(k, kE)):
                G = mul(G, q)
        ks = [(1, 0), p, mul(p, p), (2, 0), (1, 3), mul(p, (4, 3)), (-1, 0), mul(a13, p) if a != a13 else (5, 3)]
        for kk in ks:
            j = mul(G, kk)
            lhs = F_brute(mul(D, a), mul(E, b), j)
            base = F_brute(D, E, j)
            rhs = times_conj_sym(times_sym(base, chi(a, j) if a != (1, 0) else 0),
                                 chi(b, neg(j)) if b != (1, 0) else 0)
            ntests += 1
            if lhs != (0, 0):
                nonzero += 1
            if lhs != rhs:
                ok_all = False
                print("   K1 mismatch", lab, "j=", j, lhs, rhs)
            # control: keep the un-cancelled factors conj(chi_a(E)) * chi_b(D)
            ctrl = rhs
            if a != (1, 0):
                ctrl = times_conj_sym(ctrl, chi(a, E))
            if b != (1, 0):
                ctrl = times_sym(ctrl, chi(b, D))
            if ctrl != lhs:
                ctrl_detected = True
    report("K1", ok_all, f"F(Da,Eb;j) = F(D,E;j) chi_a(j) conj(chi_b(-j)) with R = 1: "
                         f"{ntests} (config, j) cases, {nonzero} with nonzero value, 6 configurations "
                         f"(Np = 7, 13, 19), brute-force congruence sums")
    report("K1-CTRL", ctrl_detected, "formula with un-cancelled conj(chi_a(E)) chi_b(D) (character "
                                     "attached at primes of D,E on the residual column) disagrees",
           control=True)


# ---------------------------------------------------------------------------------------------
# [K2] zero extension at q kills the allocation
# ---------------------------------------------------------------------------------------------
def k2():
    q = [p for p in PRIMES if norm(p) == 7][0]
    r = [p for p in PRIMES if norm(p) == 13][0]
    kold = mul(q, r)
    # good primary columns u of norm <= 2000 divisible by q
    cols = []
    R = 50
    for a in range(-R, R + 1):
        for b in range(-R, R + 1):
            u = (a, b)
            n = norm(u)
            if 1 < n <= 2000 and is_primary(u) and divexact(u, q) is not None:
                if factor(u) is not None:
                    cols.append(u)
    forms = {
        "chi_q(u)^1": lambda u: None if chi(q, u) is None else (chi(q, u) * 1) % 3,
        "chi_q(u)^2": lambda u: None if chi(q, u) is None else (chi(q, u) * 2) % 3,
        "chi_u(q)^1": lambda u: chi(u, q),
        "chi_u(q)^2": lambda u: None if chi(u, q) is None else (2 * chi(u, q)) % 3,
        "chi_u(k_old), k_old=q*r": lambda u: chi(u, kold),
        "chi_q(u)^3 zero-retained": lambda u: None if chi(q, u) is None else 0,
    }
    ok = True
    for name, fn in forms.items():
        vals = [fn(u) for u in cols]
        if any(v is not None for v in vals):
            ok = False
            print("   K2 nonzero value for", name)
    report("K2", ok, f"6 displayed moving factor forms attached at q (Nq = 7) vanish on all {len(cols)} "
                     f"good primary columns u (Nu <= 2000) with q | u")

    # control: unit-part extension chi_q(u / q^{v_q(u)})^e
    def unitpart(u):
        while True:
            w = divexact(u, q)
            if w is None:
                return u
            u = w
    vals = [chi(q, unitpart(u)) for u in cols]
    nz = sum(1 for v in vals if v is not None)
    ram = sum(1 for v in vals if v not in (None, 0))
    report("K2-CTRL", nz > 0 and ram > 0,
           f"unit-part extension chi_q(u q^-v)^1 is nonzero on {nz}/{len(cols)} columns with q | u "
           f"({ram} with a nontrivial value): it would survive into D_2", control=True)


# ---------------------------------------------------------------------------------------------
# [K3] forced residue at a nonunit i = 1 prime, with or without an older character at p
# ---------------------------------------------------------------------------------------------
def classkey(n, m=(18, 0)):
    return red(n, m)


def k3():
    test_primes = [x for x in PRIMES if norm(x) <= 1500]
    ok = True
    ctrl = True
    lines = []
    for Np in (7, 13):
        p = [x for x in PRIMES if norm(x) == Np][0]
        ns = [n for n in test_primes if n != p]
        for e_old in (0, 1, 2):
            pattern = []
            for k in range(6):
                v = (1, 0)
                for _ in range(2 + k):
                    v = mul(v, p)
                # Psi(n) = chi_p(n)^{e_old} * chi_n(p^{2+k})
                byclass = {}
                const = True
                for n in ns:
                    s1 = chi(p, n)
                    s2 = chi(n, v)
                    val = (e_old * s1 + s2) % 3
                    key = classkey(n)
                    if key in byclass and byclass[key] != val:
                        const = False
                        break
                    byclass[key] = val
                pattern.append(const)
                pred = (e_old + 2 + k) % 3 == 0
                if const != pred:
                    ok = False
            res = [k for k in range(6) if pattern[k]]
            lines.append(f"Np={Np}, e_old={e_old}: S-ray for k in {res}")
            if e_old == 1 and res != [0, 3]:
                ctrl = False
    for ln in lines:
        print("   " + ln)
    report("K3", ok, "exceptional (S-ray, constant on primary primes mod 18, Nn <= 1500) iff "
                     "e_old + 2 + k == 0 mod 3; with e_old = 0 the forced residue is k == 1 mod 3")
    report("K3-CTRL", ctrl, "a surviving older chi_p^1 would move the forced residue to k == 0 mod 3 "
                            "(r_p = 0): detected", control=True)


# ---------------------------------------------------------------------------------------------
# [K4] ledger cost of a surviving older character (per-prime F_2, LF formula at theta = 1/3)
# ---------------------------------------------------------------------------------------------
def k4():
    ok = True
    print("   nonunit equal i, older exponent e_old: r_p = -(i+1+e_old) mod 3, "
          "F_2 = 2i - (2/3)i - 1 + 1/3 + r_p/3, b_2 = i")
    for i in (1, 2, 4, 5):
        row = []
        for e_old in (0, 1, 2):
            r = (-(i + 1 + e_old)) % 3
            F2 = 2 * i - Fr(2, 3) * i - 1 + Fr(1, 3) + Fr(r, 3)
            row.append(f"e_old={e_old}: r_p={r}, F_2-b_2={F2 - i}")
            if e_old == 0 and i == 1 and F2 != 1:
                ok = False
            if e_old == 1 and i == 1 and F2 != Fr(2, 3):
                ok = False
        print(f"   i={i}: " + "; ".join(row))
    report("K4", ok, "at nonunit i = 1: e_old = 0 gives F_2 = b_2 (tight, kappa_2 = 1); "
                     "e_old = 1 would give F_2 = (2/3) b_2 (loss 1/3 per unit log-norm); "
                     "i >= 2 types keep F_2 >= b_2 for every e_old")


# ---------------------------------------------------------------------------------------------
# [K5] cubic reciprocity, R == 1 on good primaries; sextic control
# ---------------------------------------------------------------------------------------------
def k5():
    ps = [x for x in PRIMES if norm(x) <= 400]
    ok = True
    npairs = 0
    bad6 = 0
    for i1, a in enumerate(ps):
        for b in ps[i1 + 1:]:
            if norm(a) == norm(b) and a == b:
                continue
            npairs += 1
            if chi(a, b) != chi(b, a):
                ok = False
            if chi(a, b, 6) != chi(b, a, 6):
                bad6 += 1
    report("K5", ok, f"cubic reciprocity chi_a(b) = chi_b(a) on {npairs} pairs of distinct good "
                     f"primary primes (norm <= 400)")
    report("K5-CTRL6", bad6 > 0, f"sextic symbol: chi_a(b) != chi_b(a) on {bad6}/{npairs} pairs "
                                 f"(the manuscript's R is nontrivial at n = 6)", control=True)


if __name__ == "__main__":
    print(f"primes outside S with norm <= 3000: {len(PRIMES)}")
    k5()
    k2()
    k3()
    k4()
    k1()
    nchk = sum(1 for t, o, c in RESULTS if not c)
    nok = sum(1 for t, o, c in RESULTS if not c and o)
    nct = sum(1 for t, o, c in RESULTS if c)
    ncd = sum(1 for t, o, c in RESULTS if c and o)
    print(f"SUMMARY: {nok}/{nchk} checks PASS; {ncd}/{nct} failing controls detected")
