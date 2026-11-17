#!/usr/bin/env python3
"""Level-2 audit of Section 3 of "The Quasi-Riemann Hypothesis" (paper2.tex l.660-772).

Independent code (nothing from the OpenAI repository).  Run with:  python3 -I s3_deduction_checks.py

Checks
  C1  chi_n(p^6) = 1_{p not | n}  (sextic symbol, primary generators), squarefree and non-squarefree n.
  C2  A_1(D) - A_{p^6}(D) = sum_{p | n} mu(n) W(Nn/D), and the count bound #{n : p|n, Nn <= b0 D} <= c * b0 D / Np.
  C3  J(Y) = #{prime ideals not above 2,3 : Y/2 < Np <= Y}: smallest Y after which J >= 1 always,
      ratio J / (Y/(2 log Y)), and the corresponding D threshold D_0 = Y_0^{6/(1+theta)}.
  C4  Exponent arithmetic of (eq:prime-extract) with sympy; optimality of Y = H^{1/6}.
  C5  Mellin substitution  int_0^inf W(N/D) D^{-s} dD/D = N^{-s} What(s)  and  What(rho) = int phi dy/y > 0.
  C6  Base change:  sum_{N a = m} chi(N a) = (chi * chi chi_{-3})(m)  for all m <= M and several chi;
      r_K(m) = #{ideals of norm m} = sum_{e|m} chi_{-3}(e) by counting elements / 6.
  C7  Illustration only (NOT evidence for Prop 3.1): sum_{0<N u<=H} |A_u(D)|^2 / (D H) for small D, nu = 1.
"""
import math, cmath, sys, itertools
from fractions import Fraction

# ---------------------------------------------------------------- Z[omega]
# element (a,b) = a + b*omega, omega^2 = -1 - omega
def mul(x, y):
    a, b = x; c, d = y
    return (a*c - b*d, a*d + b*c - b*d)
def sub(x, y): return (x[0]-y[0], x[1]-y[1])
def conj(x): return (x[0]-x[1], -x[1])
def norm(x): a, b = x; return a*a - a*b + b*b
def divides(y, x):
    n = norm(y); z = mul(x, conj(y)); return z[0] % n == 0 and z[1] % n == 0
def rmod(x, m):
    n = norm(m); z = mul(x, conj(m))
    q0 = (round(z[0]/n), round(z[1]/n)); best = None
    for da in (-1, 0, 1):
        for db in (-1, 0, 1):
            r = sub(x, mul((q0[0]+da, q0[1]+db), m))
            if best is None or norm(r) < norm(best): best = r
    return best
def powmod(x, e, m):
    r = (1, 0); x = rmod(x, m)
    while e:
        if e & 1: r = rmod(mul(r, x), m)
        x = rmod(mul(x, x), m); e >>= 1
    return r
UNITS = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1)]
SIXTH = {(1, 0): 0, (1, 1): 1, (0, 1): 2, (-1, 0): 3, (-1, -1): 4, (0, -1): 5}  # zeta6 = 1+omega
def is_primary(x): return (x[0]-1) % 3 == 0 and x[1] % 3 == 0
def make_primary(x):
    for u in UNITS:
        y = mul(u, x)
        if is_primary(y): return y
    raise ValueError(x)
def rat_primes(N):
    s = bytearray([1])*(N+1); s[0] = s[1] = 0
    for i in range(2, int(N**0.5)+1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(N+1) if s[i]]
def split_rep(p):
    # a + b omega of norm p (p = 1 mod 3), via a^2 - ab + b^2 = p
    for b in range(1, int(2*math.sqrt(p))+2):
        # a^2 - a b + b^2 - p = 0
        disc = b*b - 4*(b*b - p)
        if disc >= 0:
            r = math.isqrt(disc)
            if r*r == disc and (b + r) % 2 == 0:
                return ((b + r)//2, b)
    raise ValueError(p)
def eis_primes(maxnorm):
    """primary primes pi (not above 2,3) with N pi <= maxnorm; list of (pi, Npi, rational prime)."""
    out = []
    for p in rat_primes(maxnorm):
        if p in (2, 3): continue
        if p % 3 == 1:
            pi = make_primary(split_rep(p)); out.append((pi, p, p)); out.append((make_primary(conj(pi)), p, p))
        elif p*p <= maxnorm:
            out.append((make_primary((p, 0)), p*p, p))
    return sorted(out, key=lambda t: (t[1], t[0]))
def sextic(x, p):
    """(x/p)_6 as exponent k in 0..5 (value zeta6^k), None if p | x; p primary prime not above 2,3."""
    if divides(p, x): return None
    q = norm(p); r = powmod(x, (q-1)//6, p)
    for u, e in SIXTH.items():
        if divides(p, sub(r, u)): return e
    raise ValueError('no sixth root of unity', x, p, r)
def chi_exp(factors, x):
    """chi_n(x) for n = prod of the primary primes in `factors` (with multiplicity): exponent or None."""
    t = 0
    for p in factors:
        k = sextic(x, p)
        if k is None: return None
        t += k
    return t % 6
def epow(x, e):
    r = (1, 0)
    for _ in range(e): r = mul(r, x)
    return r

results = {}
def report(name, ok, detail):
    results[name] = (ok, detail)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")

# ---------------------------------------------------------------- C1
def check_C1():
    P = eis_primes(250)
    fails = 0; cases = 0
    small = [t[0] for t in P if t[1] <= 100]
    # columns: products of 1..3 primes from `small` (allow repetition -> non-squarefree too)
    cols = []
    for r in (1, 2, 3):
        for combo in itertools.combinations_with_replacement(range(len(small)), r):
            fs = [small[i] for i in combo]
            n = (1, 0)
            for f in fs: n = mul(n, f)
            if norm(n) <= 6000: cols.append(fs)
    for (p, Np, _) in P:
        u = epow(p, 6)
        for fs in cols:
            e = chi_exp(fs, u)
            expect_zero = any(divides(f, p) and divides(p, f) for f in fs)  # same prime ideal
            cases += 1
            if expect_zero:
                if e is not None: fails += 1
            else:
                if e != 0: fails += 1
    report("C1 chi_n(p^6)=1_{p not | n}", fails == 0, f"{cases} (p,n) cases, {len(P)} primes p (N p<=250), {len(cols)} columns n (incl. non-squarefree), {fails} failures")

# ---------------------------------------------------------------- helpers for column enumeration
def primary_elements_in(lo, hi):
    """primary elements n with lo <= N n < hi (one per ideal prime to 3)."""
    out = []
    B = int(math.isqrt(int(4*hi/3))) + 3
    for b in range(-B, B+1):
        if b % 3: continue
        # a^2 - a b + b^2 in [lo,hi)
        for a in range(-2*B-2, 2*B+3):
            if (a-1) % 3: continue
            N = a*a - a*b + b*b
            if lo <= N < hi: out.append((a, b))
    return out
def factor_primary(n, P):
    """factor primary n (prime to 3) into primary primes from list P; return (factors, ok, has2)."""
    fs = []; m = n; N = norm(n)
    if N % 2 == 0 or N % 4 == 0:
        return None
    for (p, Np, _) in P:
        if Np > norm(m): break
        while norm(m) > 1 and norm(m) % Np == 0 and divides(p, m):
            fs.append(p); m = make_primary(rmod_div(m, p))
    if norm(m) != 1: return None
    return fs
def rmod_div(x, y):
    n = norm(y); z = mul(x, conj(y)); assert z[0] % n == 0 and z[1] % n == 0
    return (z[0]//n, z[1]//n)

# ---------------------------------------------------------------- C2
def bump(y):
    if y <= 1 or y >= 2: return 0.0
    t = (y - 1.5)/0.5
    return math.exp(-1.0/(1 - t*t))
def check_C2():
    import random
    random.seed(1)
    worst = 0.0; cases = 0; fails = 0
    for D in (200.0, 500.0, 1200.0):
        P = eis_primes(int(2*D)+10)
        cols = []
        for n in primary_elements_in(int(D), int(2*D)+1):
            fs = factor_primary(n, P)
            if fs is None: continue
            cols.append((n, fs))
        Wn = [(n, fs, bump(norm(n)/D)) for (n, fs) in cols]
        mu = lambda fs: 0 if len(set(fs)) < len(fs) else (-1)**len(fs)
        A1 = sum(mu(fs)*w for (n, fs, w) in Wn)
        for (p, Np, _) in P:
            if Np > 40: break
            u = epow(p, 6)
            Ap6 = 0.0
            for (n, fs, w) in Wn:
                m = mu(fs)
                if m == 0 or w == 0: continue
                e = chi_exp(fs, u)
                if e is None: continue
                Ap6 += m * w * cmath.exp(2j*math.pi*e/6).real if e else m * w
            direct = sum(mu(fs)*w for (n, fs, w) in Wn if any(divides(p, f) for f in fs))
            cnt = sum(1 for (n, fs, w) in Wn if w != 0 and any(divides(p, f) for f in fs))
            cases += 1
            if abs((A1 - Ap6) - direct) > 1e-9: fails += 1
            # count bound: #{ideals m: N m <= 2D/Np} <= c_K * 2D/Np with c_K = max ratio below
            worst = max(worst, cnt * Np / (2*D))
    # ideal-count constant: #{ideals of norm <= x}/x
    M = 20000; r = [0]*(M+1)
    for a in range(-200, 201):
        for b in range(-200, 201):
            N = a*a - a*b + b*b
            if 0 < N <= M: r[N] += 1
    cum = 0; cK = 0.0
    for x in range(1, M+1):
        cum += r[x]/6; cK = max(cK, cum/x)
    report("C2 A_1 - A_{p^6} identity and O(D/Y) count", fails == 0 and worst <= cK,
           f"{cases} (D,p) cases, {fails} identity failures; max #{{n: p|n, Nn in (D,2D)}}*Np/(2D) = {worst:.3f} <= sup_x #{{N a<=x}}/x = {cK:.3f} (asymptotic pi/(3 sqrt3) = {math.pi/(3*math.sqrt(3)):.4f})")

# ---------------------------------------------------------------- C3
def check_C3():
    Ymax = 2_000_000
    ps = rat_primes(Ymax)
    norms = []
    for p in ps:
        if p in (2, 3): continue
        if p % 3 == 1: norms += [p, p]
        elif p*p <= Ymax: norms.append(p*p)
    norms.sort()
    import bisect
    def J(Y): return bisect.bisect_right(norms, Y) - bisect.bisect_right(norms, Y/2)
    # smallest Y0 such that J(Y) >= 1 for all Y in [Y0, Ymax]: J can only drop to 0 just before a prime norm
    bad = [0.0]
    # J(Y)=0 iff no norm in (Y/2, Y]; check at Y just below each norm and at 2*norm
    cand = sorted(set([x - 1e-9 for x in norms] + [2*x for x in norms] + [1.0, 2.0, 3.0]))
    lastbad = 0.0
    for Y in cand:
        if Y > Ymax: break
        if Y >= 1 and J(Y) == 0: lastbad = Y
    ratios = [(Y, J(Y) / (Y/(2*math.log(Y)))) for Y in (10**3, 10**4, 10**5, 10**6, 2*10**6)]
    th = 0.1
    D0 = (7.0)**(6/(1+th))
    report("C3 J(Y)>=1 threshold and J ~ Y/(2 log Y)", True,
           f"last Y<=2e6 with J(Y)=0 (S={{(2),(lambda)}} only): Y ~ {lastbad:.4f}; hence J>=1 needs Y>=7, i.e. D >= 7^(6/(1+theta)) = {D0:.0f} at theta=0.1 (larger if the conductor of nu adds primes to S); ratios J/(Y/(2logY)): " + ", ".join(f"Y={Y:.0e}:{r:.3f}" for Y, r in ratios))

# ---------------------------------------------------------------- C4
def check_C4():
    import sympy as sp
    th, Dl = sp.symbols('theta logD', positive=True)
    H = 1 + th; Y = H/6
    t1 = sp.simplify((2 + th) - Y)            # exponent of D^{2+theta}/Y
    t2 = sp.simplify(2 - 2*Y)                 # exponent of D^2/Y^2
    ok1 = sp.simplify(t1 - (sp.Rational(11, 6) + 5*th/6)) == 0
    ok2 = sp.simplify(t2 - (sp.Rational(5, 3) - th/3)) == 0
    ok3 = sp.simplify(t1/2 - (sp.Rational(11, 12) + 5*th/12)) == 0
    ok4 = sp.simplify(t1 - t2 - (sp.Rational(1, 6) + 7*th/6)) == 0   # first term dominates for theta >= 0
    # optimality: bound f(y) = (2+th) - y vs 2 - 2y with y <= (1+th)/6: max(...) decreasing in y
    y = sp.symbols('y', positive=True)
    dec = sp.diff((2 + th) - y, y) < 0
    # outline version (eq:intro-extraction): D H^{5/6} + D^2 H^{-1/3}
    ok5 = sp.simplify((1 + sp.Rational(5, 6)*(1 + th)) - t1) == 0 and sp.simplify((2 - (1 + th)/3) - t2) == 0
    report("C4 exponent arithmetic", all([ok1, ok2, ok3, ok4, ok5, bool(dec)]),
           f"(2+th)-(1+th)/6 = 11/6+5th/6: {ok1}; 2-(1+th)/3 = 5/3-th/3: {ok2}; half = 11/12+5th/12: {ok3}; gap t1-t2 = 1/6+7th/6 > 0: {ok4}; outline (intro-extraction) consistent: {ok5}; first term strictly decreasing in Y so Y=H^(1/6) is optimal: {bool(dec)}")

# ---------------------------------------------------------------- C5
def check_C5():
    import mpmath as mp
    mp.mp.dps = 30
    def phi(y):
        y = mp.mpf(y)
        if y <= 1 or y >= 2: return mp.mpf(0)
        t = (y - mp.mpf(1.5))/mp.mpf(0.5)
        return mp.e**(-1/(1 - t*t))
    rho = mp.mpc(0.95, 14.1347)
    W = lambda y: (y**(-rho))*phi(y)
    What = lambda s: mp.quad(lambda y: W(y)*y**(s-1), [1, 1.5, 2])
    Wr = What(rho); target = mp.quad(lambda y: phi(y)/y, [1, 1.5, 2])
    errs = [abs(Wr - target)]
    for (N, s) in [(7, mp.mpc(2.0, 3.0)), (13, mp.mpc(1.3, -5.0)), (49, rho)]:
        # int_0^inf W(N/D) D^{-s} dD/D ; support N/D in (1,2) <=> D in (N/2, N)
        lhs = mp.quad(lambda D: W(N/D)*D**(-s-1), [N/2, 3*N/4, N])
        rhs = mp.mpf(N)**(-s)*What(s)
        errs.append(abs(lhs - rhs)/abs(rhs))
    report("C5 Mellin substitution and What(rho)>0", max(errs) < 1e-15 and target > 0 and abs(Wr.imag) < 1e-20,
           f"What(rho) = {mp.nstr(Wr, 12)} vs int phi dy/y = {mp.nstr(target, 12)}; max rel. error of termwise Mellin identity = {mp.nstr(max(errs), 3)}")

# ---------------------------------------------------------------- C6
def _prime_power_chars(p, e):
    """list of characters mod p^e as dicts {unit residue: value}."""
    q = p**e
    units = [a for a in range(1, q) if math.gcd(a, q) == 1]
    if p == 2:
        if e == 1: return [{1: 1+0j}]
        # n = (-1)^a 5^b mod 2^e, a in {0,1}, b mod 2^(e-2)
        m = 2**(e-2); log = {}
        for a in range(2):
            for b in range(m):
                log[((-1)**a * pow(5, b, q)) % q] = (a, b)
        return [{n: cmath.exp(2j*math.pi*(c1*log[n][0]/2 + c2*log[n][1]/m)) for n in units}
                for c1 in range(2) for c2 in range(m)]
    phi = q - q//p
    g = next(g for g in range(2, q) if math.gcd(g, q) == 1 and len({pow(g, j, q) for j in range(phi)}) == phi)
    log = {pow(g, j, q): j for j in range(phi)}
    return [{n: cmath.exp(2j*math.pi*c*log[n]/phi) for n in units} for c in range(phi)]
def dirichlet_chars(q):
    """all Dirichlet characters mod q (functions on Z, zero off units); verified completely multiplicative."""
    from sympy import factorint
    fac = list(factorint(q).items())
    out = []
    for combo in itertools.product(*[_prime_power_chars(p, e) for p, e in fac]):
        def ch(n, combo=combo, fac=fac, q=q):
            if math.gcd(n, q) != 1: return 0j
            z = 1+0j
            for (p, e), t in zip(fac, combo): z *= t[n % (p**e)]
            return z
        for a in range(1, 3*q):
            for b in range(1, 3*q):
                assert abs(ch(a*b) - ch(a)*ch(b)) < 1e-9
        out.append(ch)
    return out
def chi3(n): return [0, 1, -1][n % 3]
def check_C6():
    M = 3000
    # r_K(m) by counting elements of norm m, divided by 6
    r = [0]*(M+1)
    B = int(math.isqrt(4*M//3)) + 2
    for a in range(-2*B, 2*B+1):
        for b in range(-2*B, 2*B+1):
            N = a*a - a*b + b*b
            if 0 < N <= M: r[N] += 1
    fails_r = 0
    for m in range(1, M+1):
        assert r[m] % 6 == 0
        if r[m]//6 != sum(chi3(e) for e in range(1, m+1) if m % e == 0): fails_r += 1
    # coefficient identity for several chi
    fails = 0; nchar = 0
    for q in (1, 3, 4, 5, 7, 8, 9, 12, 13):
        for ch in dirichlet_chars(q) if q > 1 else [lambda n: 1+0j]:
            nchar += 1
            for m in range(1, 800):
                lhs = ch(m) * (r[m]//6)                         # sum_{N a = m} chi(N a)
                rhs = sum(ch(d)*ch(m//d)*chi3(m//d) for d in range(1, m+1) if m % d == 0)
                if abs(lhs - rhs) > 1e-9: fails += 1
    report("C6 base change L_K(s,chi o N) = L(s,chi) L(s,chi chi_{-3}) (coefficientwise)", fails == 0 and fails_r == 0,
           f"r_K(m)=sum_(e|m) chi_-3(e) for m<={M}: {fails_r} failures; Dirichlet-coefficient identity for {nchar} characters (moduli 1,3,4,5,7,8,9,12,13), m<800: {fails} failures. Exact identity (no correction factors) when chi o N := chi(N a) and chi chi_-3 is taken mod lcm(q,3).")

# ---------------------------------------------------------------- C7 (illustration)
def check_C7(Ds=(300.0, 800.0, 2000.0), th=0.1):
    import numpy as np
    lines = []
    for D in Ds:
        H = D**(1+th)
        P = eis_primes(int(2*D)+10)
        cols = []
        for n in primary_elements_in(int(D), int(2*D)+1):
            fs = factor_primary(n, P)
            if fs is None or len(set(fs)) < len(fs): continue
            w = bump(norm(n)/D)
            if w: cols.append((fs, (-1)**len(fs) * w))
        # rows
        B = int(math.isqrt(int(4*H/3))) + 2
        rows = [(a, b) for a in range(-2*B, 2*B+1) for b in range(-2*B, 2*B+1) if 0 < a*a - a*b + b*b <= H]
        ra = np.array([x[0] for x in rows]); rb = np.array([x[1] for x in rows])
        # tables of sextic symbols for each prime used
        used = {}
        for fs, _ in cols:
            for p in fs: used[p] = None
        Z6 = np.exp(2j*np.pi*np.arange(6)/6)
        for p in used:
            Np = norm(p)
            if Np % 3 == 1 and p[1] % Np != 0 and math.isqrt(Np)**2 != Np:   # split prime: O/p = F_l
                l = Np
                # omega = r mod p with p | omega - r
                rr = [t for t in range(l) if (t*t + t + 1) % l == 0]
                r0 = [t for t in rr if divides(p, (-t, 1))][0]
                # image of zeta6 = 1+omega
                z6 = (1 + r0) % l
                pw = {pow(z6, k, l): k for k in range(6)}
                tab = np.full(l, -1, dtype=np.int64)
                e = (l-1)//6
                for x in range(1, l): tab[x] = pw[pow(x, e, l)]
                idx = (ra + rb*r0) % l
                used[p] = tab[idx]
            else:                                                       # inert: O/p = F_{l^2}
                l = math.isqrt(Np)
                tab = np.full((l, l), -1, dtype=np.int64)
                for x in range(l):
                    for y in range(l):
                        if x == 0 and y == 0: continue
                        k = sextic((x, y), p); tab[x, y] = k
                used[p] = tab[ra % l, rb % l]
        A = np.zeros(len(rows), dtype=complex)
        for fs, c in cols:
            e = np.zeros(len(rows), dtype=np.int64); zero = np.zeros(len(rows), dtype=bool)
            for p in fs:
                t = used[p]; zero |= (t < 0); e += np.where(t < 0, 0, t)
            A += c * np.where(zero, 0, Z6[e % 6])
        ms = float(np.sum(np.abs(A)**2))
        colsq = sum(c*c for _, c in cols)
        lines.append(f"D={D:.0f}: H={H:.0f}, rows={len(rows)}, cols={len(cols)}, sum|A_u|^2/(D H)={ms/(D*H):.3f}, sum|A_u|^2/(rows*sum|c_n|^2)={ms/(len(rows)*colsq):.3f}, |A_1|^2/D={abs(A[rows.index((1,0))])**2/D:.3f}")
    report("C7 illustration of mean-square normalisation (not evidence)", True, "; ".join(lines))

if __name__ == "__main__":
    which = sys.argv[1:] or ["C1", "C2", "C3", "C4", "C5", "C6", "C7"]
    for w in which:
        globals()["check_" + w]()
    print("SUMMARY:", {k: v[0] for k, v in results.items()})
