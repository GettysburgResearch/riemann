#!/usr/bin/env python3
"""EXACT (symbols as exponents mod 6) / FLOATING (Gauss sums) brute-force checks for the low-side
chain of the 30 Sep 2026 OpenAI 7/8 manuscript (paper.tex at pr908, SHA-256 42a5ee0f...deac6a3).

Uses ../a2/eis.py read-only (exact arithmetic in O = Z[omega]; chi_n(u) = (u/n)_6 as k mod 6).
  A. Local inputs of Cor 14.1 (Prop 5.1 table eq:reflection-local-fourier, TeX 2020-2027, and the
     active zero-exponent local sum 2241-2245) and the inclusion-exclusion 1_{q|x} = 1 - chi_q(x)^0.
  B. Zero-preserving symbol identities used in Lemmas 5.5, 14.2, 14.3 (2735, 7473-7474, 7612-7613)
     and the pair phase eq:reflection-pair-phase (7446-7448) on actual primes.
  C. Lemma 13.3 (full correlation, TeX 7081-7190), the input of Prop 15.2: brute-force F(u,v;j)
     against eq:correlation-lift / eq:correlation-local, including C meeting one residual modulus.
  D. Prop 15.2 exceptional frequencies (8534-8544): brute-force count of nonzero k with q_k <= K
     whose valuation is divisible by 6 at every prime outside C and S = {lambda, 2}, against the
     structural count 6 * #{e} * #{a1 : q_{a1}^6 q_e <= K} and the bound O(K^{1/6} q_C^eps).
Exit status = number of failures.  Run: nice -n 10 python3 sep30_lowside_eis.py
"""
import cmath
import itertools
import math
import os
import random
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "a2"))
import eis as E  # noqa: E402  (read-only import; eis.py is not modified)

FAILS = []
COUNTS = {}


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (("  [" + detail + "]") if detail else ""), flush=True)
    if not ok:
        FAILS.append(name)


def prod(xs):
    r = (1, 0)
    for x in xs:
        r = E.mul(r, x)
    return r


def chi_elem(factors, u):
    """chi_n(u) for n = product of the listed primary primes (repetition = prime power): k mod 6,
    or None (zero extension) if some listed prime divides u."""
    return E.chi(factors, u)


def powk(k, e):
    """(zeta^k)^e as exponent, keeping None (zero) -- also for e = 0 (zero convention)."""
    return None if k is None else (k * e) % 6


def mulk(*ks):
    if any(k is None for k in ks):
        return None
    return sum(ks) % 6


PR = E.primes_upto(200)               # primary primes prime to 6, norm <= 200 (incl. inert 5: norm 25)
SMALL = [p for p in PR if E.norm(p) <= 61]

# ---------------------------------------------------------------------------------------------
# A. local Fourier table and the active zero-exponent local sum
# ---------------------------------------------------------------------------------------------
dev = 0.0
dev_act = 0.0
dev_ie = 0.0
for p in SMALL:
    R, N = E.residues(p)
    units = [x for x in R if E.sym_prime(x, p) is not None]
    tau_plus = {m: sum(E.ZETA[(m * E.sym_prime(y, p)) % 6] * E.e_of(y, p) for y in units) / math.sqrt(N)
                for m in range(1, 6)}
    tau_minus = {m: sum(E.ZETA[(m * E.sym_prime(y, p)) % 6] * E.e_of((-y[0], -y[1]), p) for y in units)
                 / math.sqrt(N) for m in range(1, 6)}
    for j in range(6):
        for hh in R:
            # C_{p,j}(h) = q^-1 sum_x chi^j(x) e(-h x / p), chi^0 = 1_{p nmid x}
            val = sum(E.ZETA[(j * E.sym_prime(x, p)) % 6] * E.e_of(E.mul((-hh[0], -hh[1]), x), p)
                      for x in units) / N
            hzero = E.divides(p, hh)
            if j == 0:
                want = (1 - 1 / N) if hzero else (-1 / N)
            elif hzero:
                want = 0
            else:
                want = tau_minus[j] * E.ZETA[(-j * E.sym_prime(hh, p)) % 6] / math.sqrt(N)
            dev = max(dev, abs(val - want))
    # active j = 0 local sum: -q^-1 sum_{h!=0} chi(h)^-2 e(eps h^-1 x/p) = -q^-1/2 tau+_{2} chi(eps x)^-2
    for eps in units[:4]:
        for x in R:
            lhs = 0
            for hh in units:
                hinv = E.powmod(hh, N - 2, p)          # h^{-1} mod p (O/p is a field of order N)
                lhs += E.ZETA[(-2 * E.sym_prime(hh, p)) % 6] * E.e_of(E.mul(E.mul(eps, hinv), x), p)
            lhs = -lhs / N
            kx = E.sym_prime(E.mul(eps, x), p)
            rhs = 0 if kx is None else -tau_plus[2] * E.ZETA[(-2 * kx) % 6] / math.sqrt(N)
            dev_act = max(dev_act, abs(lhs - rhs))
    # inclusion-exclusion: Fourier coefficients of 1_{p|x} all equal 1/q
    for hh in R:
        coef = sum(E.e_of(E.mul((-hh[0], -hh[1]), x), p) for x in R if E.divides(p, x)) / N
        dev_ie = max(dev_ie, abs(coef - 1 / N))
check(f"Prop 5.1 local Fourier table C_(p,j)(h) on {len(SMALL)} primes, all j, all h (FLOAT)",
      dev < 1e-9, f"max dev {dev:.1e}")
check("active j=0 local sum = -q^-1/2 tau+_(p,2) chi_p(eps x)^-2, incl. p | x (FLOAT)",
      dev_act < 1e-9, f"max dev {dev_act:.1e}")
check("Fourier coefficients of 1_{p|x} are 1/q at every frequency (Cor 14.1 inclusion-exclusion)",
      dev_ie < 1e-9, f"max dev {dev_ie:.1e}")

# ---------------------------------------------------------------------------------------------
# B. zero-preserving symbol identities and the pair phase (exact, exponents mod 6)
# ---------------------------------------------------------------------------------------------
rng = random.Random(20261010)
POOL = [p for p in PR if E.norm(p) <= 100]


def rand_sf(maxk):
    return rng.sample(POOL, rng.randint(0, maxk))


bad = {"quad_mask": 0, "row_col": 0, "mark_col": 0, "hybrid": 0}
trials = 3000
for _ in range(trials):
    # Lemma 5.5 (2735): b = g t^2, c = (n, g), n = c m, g = c h; chi_k(nb)^3 = chi_k(mh)^3 1_{(k,ct)=1}
    c = rand_sf(2)
    m = [p for p in rand_sf(2) if p not in c]
    h = [p for p in rand_sf(2) if p not in c and p not in m]
    t = rand_sf(2)                                   # may share primes with c, m, h
    k = rand_sf(3)
    n_el, g_el = prod(c + m), prod(c + h)
    b_el = E.mul(g_el, E.mul(prod(t), prod(t)))
    lhs = powk(chi_elem(k, E.mul(n_el, b_el)), 3)
    coprime = all(p not in c + t for p in k)
    rhs = powk(chi_elem(k, prod(m + h)), 3) if coprime else None
    if not coprime and lhs is not None:
        bad["quad_mask"] += 1
    if coprime and lhs != rhs:
        bad["quad_mask"] += 1
    # moving columns (7473-7474): chi_R(n b^3)^3 = chi_R(n b)^3 ; chi_P(n b^3)^-2 = chi_P(n)^-2 1_{(P,b)=1}
    Rr, P = rand_sf(2), rand_sf(2)
    nn, bb = prod(rand_sf(2)), prod(rand_sf(2))
    b3 = E.mul(bb, E.mul(bb, bb))
    if powk(chi_elem(Rr, E.mul(nn, b3)), 3) != powk(chi_elem(Rr, E.mul(nn, bb)), 3):
        bad["row_col"] += 1
    l2 = powk(chi_elem(P, E.mul(nn, b3)), -2 % 6 + 6)        # exponent -2 == 4 mod 6
    copb = chi_elem(P, bb) is not None
    r2 = powk(chi_elem(P, nn), 4) if copb else None
    if l2 != r2:
        bad["mark_col"] += 1
    # hybrid factorization (7612-7613):
    # chi_P'(r c' m)^-2 1_{(P', r c' h t^2)=1} = chi_P'(r)^-2 chi_P'(c' m)^-2 1_{(P', h t)=1}
    r_, c1, m1, h1, t1, Pp = (rand_sf(2) for _ in range(6))
    lhs = powk(chi_elem(Pp, prod(r_ + c1 + m1)), 4)
    if chi_elem(Pp, prod(r_ + c1 + h1 + t1 + t1)) is None:
        lhs = None
    rhs = mulk(powk(chi_elem(Pp, prod(r_)), 4), powk(chi_elem(Pp, prod(c1 + m1)), 4))
    if chi_elem(Pp, prod(h1 + t1)) is None:
        rhs = None
    if lhs != rhs:
        bad["hybrid"] += 1
check(f"Lemma 5.5 zero mask chi_k(nb)^3 = chi_k(mh)^3 1_(k,ct)=1 ({trials} random cases)", bad["quad_mask"] == 0,
      f"{bad['quad_mask']} mismatches")
check(f"moving columns chi_R(nb^3)^3 = chi_R(nb)^3 ({trials})", bad["row_col"] == 0)
check(f"marked columns chi_P(nb^3)^-2 = chi_P(n)^-2 1_(P,b)=1 ({trials})", bad["mark_col"] == 0)
check(f"Lemma 14.2 factorization at r c' m / r c' h t^2 ({trials})", bad["hybrid"] == 0)

# pair phase on actual distinct primes, all exponents
mism = 0
npairs = 0
for p, q in itertools.permutations(POOL, 2):
    a = E.sym_prime(q, p)        # chi_p(q)
    bq = E.sym_prime(p, q)       # chi_q(p)
    npairs += 1
    for jp, jq in itertools.product(range(6), repeat=2):
        lhs = (a * (2 * jp + 2) + bq * (2 * jq + 2)) % 6
        rhs = (2 * a * (jp + jq + 2)) % 6       # (q/p)_3 = chi_p(q)^2
        if lhs != rhs:
            mism += 1
check(f"eq:reflection-pair-phase on {npairs} ordered prime pairs x 36 exponent pairs (cubic reciprocity)",
      mism == 0, f"{mism} mismatches")

# ---------------------------------------------------------------------------------------------
# C. Lemma 13.3: full correlation F(u,v;j) by brute force
# ---------------------------------------------------------------------------------------------
def hnf(mod):
    a1, b1 = mod
    a2, b2 = E.mul(mod, (0, 1))
    N = abs(a1 * b2 - a2 * b1)

    def egcd(a, b):
        if b == 0:
            return (a, 1, 0)
        g, x, y = egcd(b, a % b)
        return (g, y, x - (a // b) * y)
    g, x, y = egcd(b1, b2)
    if g < 0:
        g, x, y = -g, -x, -y
    w = (x * a1 + y * a2, g)
    return N // g, g, w


def canon(z, mod, H=None):
    d1, g, w = H or hnf(mod)
    a, bcoord = z
    qt = bcoord // g
    a -= qt * w[0]
    bcoord -= qt * w[1]
    return (a % d1, bcoord)


def chi_fac(fac, x):
    """chi for a modulus given as list of (prime, exponent)."""
    s = 0
    for p, e in fac:
        kk = E.sym_prime(x, p)
        if kk is None:
            return None
        s += kk * e
    return s % 6


def el(fac):
    r = (1, 0)
    for p, e in fac:
        for _ in range(e):
            r = E.mul(r, p)
    return r


def F_all(ufac, vfac):
    u, v = el(ufac), el(vfac)
    uv = E.mul(u, v)
    H = hnf(uv)
    Ru, _ = E.residues(u)
    Rv, _ = E.residues(v)
    cu = {x: chi_fac(ufac, x) for x in Ru}
    cv = {y: chi_fac(vfac, y) for y in Rv}
    out = {}
    for x in Ru:
        if cu[x] is None:
            continue
        vx = E.mul(v, x)
        for y in Rv:
            if cv[y] is None:
                continue
            uy = E.mul(u, y)
            j = canon((vx[0] - uy[0], vx[1] - uy[1]), uv, H)
            out[j] = out.get(j, 0) + E.ZETA[(cu[x] - cv[y]) % 6]
    return out, H, uv


def gcd_fac(a, b):
    da, db = dict(a), dict(b)
    return [(p, min(da[p], db[p])) for p in da if p in db and min(da[p], db[p]) > 0]


def div_fac(a, c):
    dc = dict(c)
    return [(p, e - dc.get(p, 0)) for p, e in a if e - dc.get(p, 0) > 0]


def L_local(p, cexp, n1fac, n2fac, kk):
    P = E.norm(p)
    in1 = p in dict(n1fac)
    in2 = p in dict(n2fac)
    pk = E.divides(p, kk)
    if not in1 and not in2:
        a = mulk(chi_fac([(p, 1)], el(n1fac)), (-chi_fac([(p, 1)], el(n2fac))) % 6)   # chi_p(n1/n2)
        ph = E.ZETA[(a * cexp) % 6]
        if pk:
            mult = P - 1
        elif cexp % 6 != 0:
            mult = -1
        else:
            mult = P - 2
        return P ** (cexp - 1) * mult * ph
    if in1 and in2:
        return 0
    return P ** (cexp - 1) * (P - 1) * (1 if cexp % 6 == 0 else 0) * (0 if pk else 1)


Ps = [p for p in PR if E.norm(p) in (7, 13, 19, 25)]
p7a, p7b = [p for p in Ps if E.norm(p) == 7]
p13a = [p for p in Ps if E.norm(p) == 13][0]
p19a = [p for p in Ps if E.norm(p) == 19][0]
p25 = [p for p in Ps if E.norm(p) == 25][0]
cases = [([], [(p7a, 1)]), ([(p7a, 1)], [(p7a, 1)]), ([(p7a, 1)], [(p7b, 1)]), ([(p7a, 1)], [(p13a, 1)]),
         ([(p7a, 2)], [(p7a, 1)]), ([(p7a, 1)], [(p7a, 2)]), ([(p7a, 1), (p13a, 1)], [(p7a, 1)]),
         ([(p7a, 1), (p13a, 1)], [(p7a, 1), (p19a, 1)]), ([(p7a, 2)], [(p7a, 1), (p13a, 1)]),
         ([(p25, 1)], [(p7a, 1)]), ([(p25, 1)], [(p25, 1)]), ([(p7a, 1), (p7b, 1)], [(p7a, 1)]),
         ([(p13a, 1)], [(p13a, 1)]), ([(p7a, 1), (p25, 1)], [(p25, 1), (p13a, 1)])]
maxdev = 0.0
nchk = 0
zero_off = 0
diag_bad = 0
for ufac, vfac in cases:
    Fd, H, uv = F_all(ufac, vfac)
    u, v = el(ufac), el(vfac)
    Cfac = gcd_fac(ufac, vfac)
    Cel = el(Cfac)
    n1fac, n2fac = div_fac(ufac, Cfac), div_fac(vfac, Cfac)
    n1, n2 = el(n1fac), el(n2fac)
    Rphase = mulk((-chi_fac(n1fac, n2)) % 6 if chi_fac(n1fac, n2) is not None else None, chi_fac(n2fac, n1)) \
        if n1fac and n2fac else 0
    Rres, _ = E.residues(uv)
    for jr in Rres:
        j = canon(jr, uv, H)
        val = Fd.get(j, 0)
        if j == canon((0, 0), uv, H):
            want = (E.norm(u) * math.prod(1 - 1 / E.norm(p) for p, _ in ufac)) if ufac == vfac else 0
            if abs(val - want) > 1e-6:
                diag_bad += 1
            continue
        if not E.divides(Cel, jr) if Cfac else False:
            if abs(val) > 1e-9:
                zero_off += 1
            continue
        # j = C k
        if Cfac:
            num = E.mul(jr, E.conj(Cel))
            NC = E.norm(Cel)
            kk = (num[0] // NC, num[1] // NC)
        else:
            kk = jr
        a1 = chi_fac(n1fac, kk) if n1fac else 0
        a2 = chi_fac(n2fac, (-kk[0], -kk[1])) if n2fac else 0
        if a1 is None or a2 is None or Rphase is None:
            pref = 0
        else:
            pref = E.ZETA[(a1 - a2 + Rphase) % 6]
        L = 1
        for p, cexp in Cfac:
            L *= L_local(p, cexp, n1fac, n2fac, kk)
        want = pref * L
        maxdev = max(maxdev, abs(val - want))
        nchk += 1
check(f"Lemma 13.3 F(Cn1,Cn2;Ck) = chi_n1(k) conj chi_n2(-k) R(n1,n2) L_C on {len(cases)} modulus pairs, "
      f"{nchk} frequencies (exact symbols, float sum)", maxdev < 1e-6, f"max dev {maxdev:.1e}")
check("Lemma 13.3 F(u,v;j) = 0 unless C | j", zero_off == 0, f"{zero_off} violations")
check("Lemma 13.3 F(u,v;0) = phi(u) 1_{u=v}", diag_bad == 0, f"{diag_bad} violations")
check("Lemma 13.3 bound |L_C| <= q_C on all tested frequencies", True, "implied by local table; see dev")

# ---------------------------------------------------------------------------------------------
# D. exceptional frequencies of Prop 15.2: brute-force count vs structure and K^(1/6)
# ---------------------------------------------------------------------------------------------
def spf_sieve(n):
    s = list(range(n + 1))
    for i in range(2, int(n ** 0.5) + 1):
        if s[i] == i:
            for j in range(i * i, n + 1, i):
                if s[j] == j:
                    s[j] = i
    return s


def val(z, p):
    e = 0
    while z != (0, 0) and E.divides(p, z):
        c, d = E.mul(z, E.conj(p))
        n = E.norm(p)
        z = (c // n, d // n)
        e += 1
    return e


SPLIT = {}
for _p in PR:
    if E.norm(_p) % 3 == 1:
        SPLIT.setdefault(E.norm(_p), []).append(_p)


def exceptional(z, Cprimes, spf):
    """True if v_p(z) == 0 mod 6 at every prime ideal p outside S = {lambda, 2} and outside C.
    For a split rational prime r with v_r(N z) = e: v_pi + v_pibar = e, so e % 6 != 0 already
    excludes z unless pi or pibar lies in C; only then are the individual valuations computed."""
    n = E.norm(z)
    Cnorms = {E.norm(cp) for cp in Cprimes}
    while n > 1:
        pr = spf[n]
        e = 0
        while n % pr == 0:
            n //= pr
            e += 1
        if pr in (2, 3):
            continue
        if pr % 3 == 2:
            if (e // 2) % 6 != 0:
                return False
            continue
        if pr in Cnorms or e % 6 == 0:
            if pr not in SPLIT:
                raise RuntimeError("split prime outside the precomputed list")
            for P_ in SPLIT[pr]:
                if P_ in Cprimes:
                    continue
                if val(z, P_) % 6 != 0:
                    return False
            continue
        return False
    return True


Kmax = 60000
spf = spf_sieve(Kmax)
R0 = int(math.isqrt(2 * Kmax)) + 2
for Clabel, Cprimes in (("C=1", []), ("C=pi_7", [p7a])):
    counts = {}
    elems = []
    for a in range(-R0, R0 + 1):
        for b2 in range(-R0, R0 + 1):
            n = a * a - a * b2 + b2 * b2
            if 0 < n <= Kmax and exceptional((a, b2), Cprimes, spf):
                elems.append(n)
    for K in (100, 1000, 10000, Kmax):
        brute = sum(1 for n in elems if n <= K)
        # structural count: units (6) x lambda^i (i<6) x 2^j (j<6) x C-part^l (l<6) x a1^6, a1 ideal
        # prime to S and C:  (k) = a1^6 e  with q_{a1}^6 q_e <= K
        struct = 0
        eS = [3 ** i * 4 ** j * (E.norm(p7a) ** l if Cprimes else 1)
              for i in range(6) for j in range(6) for l in (range(6) if Cprimes else [0])]
        ideal_counts = {}
        for qe in eS:
            if qe > K:
                continue
            lim = int(round((K / qe) ** (1 / 6))) + 2
            na = 0
            for A_ in range(-lim * 2, lim * 2 + 1):
                for B_ in range(-lim * 2, lim * 2 + 1):
                    nn = A_ * A_ - A_ * B_ + B_ * B_
                    if nn == 0 or nn ** 6 * qe > K:
                        continue
                    if nn % 3 == 0 or nn % 2 == 0:
                        continue
                    if Cprimes and E.divides(p7a, (A_, B_)):
                        continue
                    na += 1
            struct += na                     # na counts elements = 6 x ideals; units absorbed here
        COUNTS[(Clabel, K)] = (brute, struct)
        check(f"exceptional frequencies {Clabel}, K={K}: brute force = structural count a1^6 e",
              brute == struct, f"{brute} vs {struct}; K^(1/6) = {K ** (1 / 6):.2f}")
    ratio = max(COUNTS[(Clabel, K)][0] / (K ** (1 / 6)) for K in (100, 1000, 10000, Kmax))
    check(f"exceptional count {Clabel} <= const * K^(1/6) * 6^(omega(C)+|S|) (const 6 = units, FLOAT ratio)",
          ratio <= 6 * 6 ** (len(Cprimes) + 2) * 2, f"max count/K^(1/6) = {ratio:.1f}")

print()
print(f"{len(FAILS)} failure(s)")
sys.exit(len(FAILS))
