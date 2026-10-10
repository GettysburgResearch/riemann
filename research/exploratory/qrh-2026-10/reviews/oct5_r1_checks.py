#!/usr/bin/env python3
"""R1 review checks for OpenAI, "The Quasi-Riemann Hypothesis" (Oct 5 2026, paper2.tex).

Status: EMPIRICAL / finite checks only (floating Gauss sums, exact residue symbols).
Scope: Section 3 (sec:reduction) exponent arithmetic and Section 4 (sec:initialization):
  C1  exponent arithmetic of eq:prime-extract and the interface with Prop prop:canonical (exact rationals)
  C2  composite case of eq:convert2 by direct summation (no CRT), up to 3 prime factors
  C3  the paired-Gauss identity eq:initial-paired-gauss for coprime composite z1,z2, with gamma(conj chi_z1 chi_z2)
      summed directly mod z1 z2 and G evaluated as a class function mod 4 (closed form of App. A), nu of order 3
  C4  Lemma lem:poisson (Poisson summation with excluded primes) with a Gaussian Phi, trivial and nontrivial chi
  C5  the bijection (g,e,v,h) <-> (b,f,k) in the proof of Prop prop:poisson-reduction (checked in Z)
  C6  full replay of the exact identity M_D = Z + sum_xi c_xi S_xi, in the final form eq:initial-column-output,
      for tiny D with Gaussian Phi (Phi-hat not compactly supported; the identity is exact for any Schwartz Phi).
Uses research/exploratory/qrh-2026-10/a2/eis.py (exact symbols (u/p)_6, Gauss sums gamma(j, factors)).
Run:  python3 -I oct5_r1_checks.py [--quick] [--out PATH.json]
"""
import cmath, itertools, json, math, os, sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'a2'))
import numpy as np
from eis import (mul, conj, norm, is_primary, primary, divides, reduce_mod, sym_prime, primes_upto,
                 chi, residues, e_of, gamma, ZETA)

OMEGA = cmath.exp(2j*math.pi/3)
QUICK = '--quick' in sys.argv
out = {}

def cx(z): return z[0] + z[1]*OMEGA

_TAB = {}
def _table(p):
    """chi_p on O/p via an explicit ring map; validated against eis.sym_prime in check_tables()."""
    if p in _TAB: return _TAB[p]
    q = norm(p)
    a, b = p
    if b != 0:                                              # split prime a + b w, N = q prime
        r = (-a*pow(b, -1, q)) % q                          # w -> r in F_q
        tab = [sym_prime((c, 0), p) for c in range(q)]
        f = lambda z, r=r, q=q, tab=tab: tab[(z[0] + z[1]*r) % q]
    else:                                                   # inert prime -l, N = l^2
        l = abs(a)
        tab = {(c, d): sym_prime((c, d), p) for c in range(l) for d in range(l)}
        f = lambda z, l=l, tab=tab: tab[(z[0] % l, z[1] % l)]
    _TAB[p] = f
    return f

def fchi(fs, u):
    s = 0
    for p in fs:
        k = _table(p)(u)
        if k is None: return None
        s += k
    return s % 6

def check_tables(P, trials=4000):
    import random
    rnd = random.Random(1)
    bad = 0
    for _ in range(trials):
        p = rnd.choice(P); u = (rnd.randint(-500, 500), rnd.randint(-500, 500))
        bad += (_table(p)(u) != sym_prime(u, p))
    out['fast_symbol_table_mismatches'] = bad
    print(f'fast symbol tables vs eis.sym_prime: {bad} mismatches in {trials} random trials')
    assert bad == 0

def fgammas(fs, js=(-1, 2, 3)):
    """normalized Gauss sums gamma_j(n), direct summation over a full residue system mod n (no CRT)."""
    n = prod(fs); R, N = residues(n); acc = {j: 0j for j in js}
    for x in R:
        k = fchi(fs, x)
        if k is None: continue
        e = e_of(x, n)
        for j in js: acc[j] += ZETA[(j*k) % 6]*e
    return {j: acc[j]/math.sqrt(N) for j in js}
def prod(fs):
    n = (1, 0)
    for p in fs: n = mul(n, p)
    return n
def mu(fs): return (-1)**len(fs)
def chi_val(fs, u):
    k = fchi(fs, u)
    return 0 if k is None else ZETA[k]

# ---------- class functions mod 4 (App. app:gauss-identities closed forms) ----------
def mod4(z): return (z[0] % 4, z[1] % 4)
UNITS4 = [c for c in itertools.product(range(4), repeat=2) if norm(c) % 2 == 1]   # (O/4)^x, 12 classes
def inv4(c):
    for d in UNITS4:
        if mod4(mul(c, d)) == (1, 0): return d
    raise ValueError(c)
def gamma_quad(c):                      # Gamma_quad(a+b w) = (1 + i^{-b} + i^a + i^{b-a})/2
    a, b = c; I = 1j
    return (1 + I**((-b) % 4) + I**(a % 4) + I**((b - a) % 4))/2
def chi4(c):                            # chi_c(4) = (c/(-2))_3 = cube root of unity == c mod 2
    r = (c[0] % 2, c[1] % 2)
    return {(1, 0): 1, (0, 1): OMEGA, (1, 1): OMEGA**2}[r]
def G_cls(c): return chi4(c).conjugate()*gamma_quad(c)
def nu3(c):                             # an order-3 ray class character of conductor (2): c mod 2 -> F_4^x
    return chi4(c)

# ---------- squarefree primary n prime to 6 ----------
def squarefree_upto(P, Nmax):
    res = []
    def rec(i, fs, N):
        res.append((list(fs), N))
        for j in range(i, len(P)):
            q = norm(P[j])
            if N*q > Nmax: break
            fs.append(P[j]); rec(j + 1, fs, N*q); fs.pop()
    rec(0, [], 1)
    return res

# ===================== C1: exponent arithmetic =====================
def c1():
    r = {}
    th = Fr(1, 10)
    for th in [Fr(1, 10), Fr(1, 20), Fr(1, 1000)]:
        H = 1 + th; Y = H/6
        t1 = (2 + th) - Y            # D^{2+th}/Y
        t2 = 2 - 2*Y                 # D^2/Y^2
        assert t1 == Fr(11, 6) + 5*th/6 and t2 == Fr(5, 3) - th/3
        assert t1/2 == Fr(11, 12) + 5*th/12 and t2/2 < t1/2
        # outline form: D^{1}H^{5/6}, D^2 H^{-1/3}
        assert 1 + H*Fr(5, 6) == t1 and 2 - H/3 == t2
        # interface with prop:canonical: calH <= C D^{1-th}/B^2, Sigma = D/B -> calH/Sigma <= C D^{-th}/B
        # kappa = th/2 works for large D since C D^{-th} <= D^{-th/2} iff D^{th/2} >= C
        r[str(th)] = {'A1_exponent': str(t1/2), 'second_term_exponent': str(t2/2)}
    out['C1_exponents'] = r
    print('C1 exponent arithmetic: OK', r)

# ===================== C2: eq:convert2 composite, direct sums =====================
def c2(P):
    N_max = 1200 if QUICK else 2500
    sf = [s for s in squarefree_upto(P, N_max) if len(s[0]) >= 2]
    worst = 0.0; cnt = 0; by_k = {}
    for fs, N in sf:
        n = prod(fs)
        gs = fgammas(fs); gm1, g2, g3 = gs[-1], gs[2], gs[3]
        if cnt < 25:
            worst = max(worst, abs(g2 - gamma(2, fs)), abs(gm1 - gamma(-1, fs)))
        G = chi_val(fs, (4, 0)).conjugate()*g3
        lhs = mu(fs)*gm1
        rhs = chi_val(fs, (-1, 0))*(1/G)*(cx(n)/abs(cx(n))).conjugate()*g2
        d = abs(lhs - rhs); worst = max(worst, d); cnt += 1
        by_k[len(fs)] = by_k.get(len(fs), 0) + 1
        # G as class function mod 4 (closed form) agrees with the direct definition
        worst = max(worst, abs(G - G_cls(mod4(n))))
    out['C2_convert2_composite'] = {'count': cnt, 'by_num_prime_factors': by_k, 'max_abs_err': worst, 'N_max': N_max}
    print(f'C2 eq:convert2 on {cnt} composite squarefree n (N<= {N_max}, {by_k}): max err {worst:.2e}')
    assert worst < 1e-9

# ===================== C3: eq:initial-paired-gauss =====================
def gauss_pair(f1, f2):
    """gamma(conj chi_z1 chi_z2) = N(m)^{-1/2} sum_{x mod m} conj chi_z1(x) chi_z2(x) e(x/m), m = z1 z2, direct."""
    m = prod(f1 + f2)
    R, N = residues(m)
    s = 0
    for x in R:
        a = fchi(f1, x); b = fchi(f2, x)
        if a is None or b is None: continue
        s += ZETA[(b - a) % 6]*e_of(x, m)
    return s/math.sqrt(N)

def c3(P):
    N_max = 700 if QUICK else 1500
    sf = squarefree_upto(P, N_max)
    beta = {}
    def B(fs):
        key = tuple(fs)
        if key not in beta:
            n = prod(fs); beta[key] = (cx(n)/abs(cx(n))).conjugate()*fgammas(fs, (2,))[2] if fs else 1.0
        return beta[key]
    worst = {'nu_trivial': 0.0, 'nu_order3': 0.0}; cnt = 0; comp = 0
    for (f1, N1), (f2, N2) in itertools.combinations_with_replacement(sf, 2):
        for (fa, Na), (fb, Nb) in [((f1, N1), (f2, N2)), ((f2, N2), (f1, N1))]:
            if Na*Nb > N_max or set(fa) & set(fb): continue
            if not fa and not fb: continue
            z1, z2 = prod(fa), prod(fb)
            lhs0 = mu(fa)*mu(fb)*gauss_pair(fa, fb)
            t = mod4(mul(z2, inv4(mod4(z1))))            # class of z2 z1^{-1}
            rhs0 = G_cls(t)*B(fa)*B(fb).conjugate()
            worst['nu_trivial'] = max(worst['nu_trivial'], abs(lhs0 - rhs0))
            # with nu: multiply lhs by conj nu(z1) nu(z2); rhs is sum_xi c_xi xi(z1/z2) a.. = conj nu(t') G(t'^{-1}) ...
            lhs1 = nu3(mod4(z1)).conjugate()*nu3(mod4(z2))*lhs0
            tp = mod4(mul(z1, inv4(mod4(z2))))           # t' = z1 z2^{-1}
            rhs1 = nu3(tp).conjugate()*G_cls(inv4(tp))*B(fa)*B(fb).conjugate()
            worst['nu_order3'] = max(worst['nu_order3'], abs(lhs1 - rhs1))
            cnt += 1; comp += (len(fa) >= 2 or len(fb) >= 2)
    out['C3_paired_gauss'] = {'pairs': cnt, 'pairs_with_composite_member': comp, 'max_abs_err': worst, 'N_max': N_max}
    print(f'C3 eq:initial-paired-gauss on {cnt} ordered coprime pairs ({comp} with a composite member): {worst}')
    assert max(worst.values()) < 1e-9

# ===================== C4: Lemma lem:poisson with Gaussian Phi =====================
def Phi(t): return math.exp(-math.pi*t)
def Phihat(t): return (2/math.sqrt(3))*math.exp(-4*math.pi*t/3)   # self-dual measure, covol(O)=1

def lattice(Rmax):
    pts = []
    A = int(2*math.sqrt(Rmax)) + 3
    for a in range(-A, A + 1):
        for b in range(-A, A + 1):
            if norm((a, b)) <= Rmax: pts.append((a, b))
    return pts

def c4(P):
    res = []
    H = 7.3
    LAT = lattice(16*H)
    # non-vacuous cases: for radial Phi the k-sum vanishes identically unless chi is trivial on the units,
    # so nonprincipal cases are chosen with chi(1+w) = 1 (1+w generates the unit group).
    sf = [fs for fs, N in squarefree_upto(P, 700)]
    cand = []
    for fa, fb in itertools.product(sf, repeat=2):
        if set(fa) & set(fb) or not (fa or fb) or norm(prod(fa + fb)) > 700: continue
        a = fchi(fa, (1, 1)) if fa else 0; b = fchi(fb, (1, 1)) if fb else 0
        if (b - a) % 6: continue                                      # chi not trivial on units -> vacuous
        cand.append((fa, fb))
    simple = [c for c in cand if len(c[0]) + len(c[1]) == 2][:2]
    comp = [c for c in cand if len(c[0]) + len(c[1]) >= 3][:2]
    lone = [c for c in cand if not c[0] and len(c[1]) == 1][:1]
    good = simple + comp + lone
    cases = [([], [], [P[0]]), ([], [], [P[0], P[2]])]
    for fa, fb in good:
        others = [q for q in P[:8] if q not in fa + fb]
        cases.append((fa, fb, others[:2]))
    cases.append((good[0][0], good[0][1], [(good[0][0] + good[0][1])[0], P[7]]))   # exclusion sharing a prime with m
    for f1, f2, r in cases:
        m = prod(f1 + f2)
        def chiv(x):                                  # conj chi_z1 chi_z2
            a = fchi(f1, x); b = fchi(f2, x)
            return 0 if (a is None or b is None) else ZETA[(b - a) % 6]
        lhs = sum(chiv(k)*Phi(norm(k)/H) for k in LAT
                  if all(not divides(p, k) for p in r))
        g = gauss_pair(f1, f2) if (f1 or f2) else 1.0
        Nm = norm(m)
        rhs = 0
        for sub in itertools.chain.from_iterable(itertools.combinations(r, j) for j in range(len(r) + 1)):
            d = prod(list(sub)); Nd = norm(d)
            inner = 0
            Rmax = 12*Nd*Nm/H
            for h in lattice(Rmax):
                inner += chiv(h).conjugate()*Phihat(H*norm(h)/(Nd*Nm))
            rhs += mu(list(sub))*chiv(d)/Nd*inner
        rhs *= H*g/math.sqrt(Nm)
        res.append({'z1': [list(p) for p in f1], 'z2': [list(p) for p in f2], 'r': [list(p) for p in r],
                    'lhs': [lhs.real if isinstance(lhs, complex) else lhs, lhs.imag if isinstance(lhs, complex) else 0.0],
                    'abs_err': abs(lhs - rhs)})
        print(f'C4 lem:poisson z1={f1} z2={f2} r={r}: |lhs|={abs(lhs):.6g} err={abs(lhs-rhs):.2e}')
        assert abs(lhs - rhs) < 1e-8*(1 + abs(lhs))
    out['C4_poisson'] = res

# ===================== C5: change of variables (in Z) =====================
def c5():
    """Z-model of the bijection b=g/e, f=ev, k=eh  <->  e=(f,k), v=f/e, g=be, h=k/e (positive integers stand
    for primary generators; the map only uses gcd/divisibility, identical in any Dedekind domain)."""
    from sympy import factorint
    def sqf(n): return all(e == 1 for e in factorint(n).values())
    L = 40 if QUICK else 80; K = 60
    fwd = {}
    for g in range(1, L + 1):
        if not sqf(g): continue
        for e in [d for d in range(1, g + 1) if g % d == 0]:
            for v in range(1, L + 1):
                if not sqf(v) or math.gcd(g, v) != 1: continue
                for h in range(1, K + 1):
                    if math.gcd(h, v) != 1: continue
                    b, f, k = g//e, e*v, e*h
                    assert sqf(b) and sqf(f) and math.gcd(b, f) == 1
                    assert h*e**5*v**4 == k*f**4 and g*v == b*f and math.gcd(f, k) == e
                    assert (g, e, v, h) == (b*math.gcd(f, k), math.gcd(f, k), f//math.gcd(f, k), k//math.gcd(f, k))
                    assert (b, f, k) not in fwd
                    fwd[(b, f, k)] = (g, e, v, h)
    # every (b,f,k) with b,f squarefree coprime and k>=1 comes from a legal source
    surj = 0
    for b in range(1, 31):
        for f in range(1, 31):
            if not (sqf(b) and sqf(f) and math.gcd(b, f) == 1): continue
            for k in range(1, 61):
                e = math.gcd(f, k); g, v, h = b*e, f//e, k//e
                assert sqf(g) and g % e == 0 and math.gcd(g, v) == 1 and math.gcd(h, v) == 1 and sqf(v)
                surj += 1
    out['C5_bijection_in_Z'] = {'L': L, 'K': K, 'forward_images_distinct': len(fwd), 'inverse_checked': surj}
    print(f'C5 change of variables (Z model): {len(fwd)} distinct images, inverse legal on {surj} targets')

# ===================== C6: full replay of M_D = Z + sum_xi c_xi S_xi =====================
def bump(y):
    if not (1 < y < 2): return 0.0
    return math.exp(4 - 1/((y - 1)*(2 - y)))

def c6(P, D, H, nu=None):
    """nu: None (trivial) or 'order3'. Checks (1/D) sum_u Phi(N u/H)|A_u|^2 = Z + RHS of eq:initial-column-output
    (with sum_xi c_xi a_xi(m1) conj a_xi(m2) = conj nu(m1) nu(m2) G(m2 m1^{-1}) beta(m1) conj beta(m2))."""
    nuf = (lambda z: 1.0) if nu is None else (lambda z: nu3(mod4(z)))
    W = lambda y: bump(y)
    W0 = lambda x: x**-0.5*W(x)                      # W real
    cols = [(fs, N) for fs, N in squarefree_upto(P, 2*D) if W(N/D) != 0]
    # ---- LHS ----
    U = lattice(16*H)
    lhs = 0.0
    for u in U:
        A = sum(mu(fs)*nuf(prod(fs))*chi_val(fs, u)*W(N/D) for fs, N in cols)
        lhs += Phi(norm(u)/H)*abs(A)**2
    lhs /= D
    # ---- Z ----
    Z = 0.0
    for fs, N in cols:
        Z += W(N/D)**2*np.prod([1 - 1/norm(p) for p in fs])
    Z *= H/D*Phihat(0)
    # ---- S: sum over b,f coprime sqf, k != 0, m1,m2 with (m_j, b f) = 1 ----
    allsf = squarefree_upto(P, 2*D)
    beta = {}
    def Bt(fs):
        k = tuple(fs)
        if k not in beta:
            beta[k] = (cx(prod(fs))/abs(cx(prod(fs)))).conjugate()*fgammas(fs, (2,))[2] if fs else 1.0
        return beta[k]
    # k-lattice large enough for the Gaussian Phi-hat
    Kmax = 9*(2*D)**2/H                              # exp(-4 pi/3 * 9) ~ 4e-17
    KL = [k for k in lattice(Kmax) if k != (0, 0)]
    KN = np.array([norm(k) for k in KL], dtype=float)
    chik = {}
    def chivec(fs):
        key = tuple(fs)
        if key not in chik:
            chik[key] = np.array([chi_val(fs, k) for k in KL], dtype=complex)
        return chik[key]
    S = 0.0 + 0.0j
    for (fb, Nb) in allsf:
        for (ff, Nf) in allsf:
            if Nb*Nf >= 2*D or set(fb) & set(ff): continue
            ms = [(fm, Nm) for fm, Nm in allsf if W(Nb*Nf*Nm/D) != 0 and not (set(fm) & (set(fb) | set(ff)))]
            if not ms: continue
            f = prod(ff)
            pre = (H/D**2)*mu(ff)*Nb
            for (f1, N1) in ms:
                c1v = chivec(f1)*(chi_val(f1, f)**4)
                for (f2, N2) in ms:
                    c2v = chivec(f2)*(chi_val(f2, f)**4)
                    z1, z2 = prod(f1), prod(f2)
                    coef = (nuf(z1).conjugate()*nuf(z2)*G_cls(mod4(mul(z2, inv4(mod4(z1)))))
                            *Bt(f1)*Bt(f2).conjugate())
                    w = W0(Nb*Nf*N1/D)*W0(Nb*Nf*N2/D)
                    ph = (2/math.sqrt(3))*np.exp(-4*math.pi/3*H*KN/(Nf**2*N1*N2))
                    S += pre*coef*w*np.sum(c1v*np.conj(c2v)*ph)
    rhs = Z + S
    err = abs(lhs - rhs)
    rec = {'D': D, 'H': H, 'nu': nu or 'trivial', 'columns': len(cols), 'M_D': lhs, 'Z': Z,
           'S_real': S.real, 'S_imag': S.imag, 'abs_err': err, 'rel_err': err/abs(lhs)}
    print(f'C6 replay D={D} H={H} nu={nu}: M_D={lhs:.10f} Z={Z:.10f} S={S:.3e} err={err:.2e}')
    assert err < 1e-8*abs(lhs)
    return rec

if __name__ == '__main__':
    P = primes_upto(2600)
    check_tables(P)
    c1()
    c2(P)
    c3(P)
    c4(P)
    c5()
    runs = [(30, 6.0, None), (30, 6.0, 'order3')] if QUICK else \
           [(30, 6.0, None), (30, 6.0, 'order3'), (30, 40.0, 'order3'), (45, 4.0, None), (60, 9.0, 'order3')]
    out['C6_full_replay'] = [c6(P, D, H, nu) for D, H, nu in runs]
    if '--out' in sys.argv:                               # optional JSON record, e.g. in a scratch directory
        path = sys.argv[sys.argv.index('--out') + 1]
        with open(path, 'w') as fh: json.dump(out, fh, indent=1, default=str)
        print('wrote', path)
    print('ALL CHECKS PASSED')
