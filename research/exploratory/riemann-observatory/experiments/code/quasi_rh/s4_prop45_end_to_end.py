# Level-2 audit, Section 4: end-to-end numerical test of the exact identity chain in the
# proof of Proposition 4.5 (paper2.tex l.1024-1173), and of the identity in the proof of
# Lemma 4.4 (l.971-992).
#
# Toy instance (all choices are ours):
#   S = {primes above 2, 3, 5};  nu((t)) = psi(N t), psi the order-4 Dirichlet character mod 5
#   (a ray class character of conductor | 5);  D = 1;  W = arbitrary complex function of N(n)
#   supported on N(n) <= NMAX (the identities are exact and do not use smoothness);
#   Phi(t) = exp(-pi t) (Schwartz, radial), hatPhi(t) = (2/sqrt3) exp(-4 pi t/3).
# Levels compared:
#   L0  M_D = (1/D) sum_{u in O} Phi(N u/H) |A_u(D)|^2                      (eq:expanded-ms)
#   L1  Z + [Lemma 4.2 applied to each (g,z1,z2), Gauss sum gamma(conj chi_z1 chi_z2) computed
#       by brute force, h != 0]                                              (eq:initial-poisson-rows)
#   L2  Z + sum_xi c_xi S_xi in the (g,e,h,z1,z2) form, using (eq:initial-paired-gauss)
#   L3  Z + sum_xi c_xi S_xi in the (b,f,k,m1,m2) form                         (eq:initial-column-output)
# Run:  python3 -I s4_prop45_end_to_end.py
import sys, os, math, cmath, itertools, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from s4_zw import *

random.seed(20261117)
def Phi(t): return np.exp(-np.pi * t)
def hatPhi(t): return (2 / SQ3) * np.exp(-4 * np.pi * t / 3)

H = float(sys.argv[1]) if len(sys.argv) > 1 else 19.7
NMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 100
P = [p for p in eisenstein_primes(NMAX) if p.q != 25]        # primes prime to 30 (split and inert, 5 excluded)
cols = squarefree_products(P, NMAX)                          # squarefree primary n prime to S, N<=NMAX
print("H =", H, " columns:", len(cols))
key = lambda ps: tuple(sorted(p.g for p in ps))
psi = {1: 1, 2: 1j, 4: -1, 3: -1j}
def nu(ps): return psi[nm(ps) % 5]
wval = {N: complex(random.gauss(0, 1), random.gauss(0, 1)) for N in range(1, NMAX + 1)}
def W(N): return wval.get(N, 0.0)
def W0(N): return (N ** -0.5) * np.conj(W(N)) if N <= NMAX else 0.0
mu = lambda ps: (-1) ** len(ps)

# ---- G on the 12 classes mod 4, from brute-force Gauss sums of primary primes ----
G_class = {}
for p in eisenstein_primes(600):
    t = mod4(p.g)
    if t not in G_class:
        G_class[t] = chi([p], (4, 0)).conjugate() * gamma([p], 3)
assert len(G_class) == 12
units4 = [(a, b) for a in range(4) for b in range(4) if norm((a, b)) % 2 == 1]
def inv4(t):
    for u in units4:
        if mod4(mul(u, t)) == (1, 0): return u
def Psi(ps1, ps2):
    """Psi(z1 z2^{-1}) = conj(nu(z1 z2^{-1})) G(z2 z1^{-1}) = sum_xi c_xi xi(z1) conj(xi(z2))"""
    t = mod4(mul(elt(ps2), inv4(mod4(elt(ps1)))))
    return np.conj(nu(ps1)) * nu(ps2) * G_class[t]
acache = {}
def a(ps):
    k = key(ps)
    if k not in acache:
        acache[k] = alpha(elt(ps)).conjugate() * gamma(ps, 2) if ps else 1.0 + 0j
    return acache[k]

# ---- dual lattice points and character tables chi_n(h) for every column n ----
RMAX = 11.0 * NMAX * NMAX / H
HA, HB = lattice_points(RMAX)
HN = HA * HA - HA * HB + HB * HB
print("dual points:", len(HA))
CH = {key(ps): (chi_arr(ps, HA, HB) if ps else np.ones(HA.shape, dtype=complex)) for ps in cols}
def chi_el(ps, x):
    return chi(ps, x) if ps else 1.0

# ---- L0: direct mean square ----
UA, UB = lattice_points(14 * H + 40)
UN = UA * UA - UA * UB + UB * UB
Au = np.zeros(UA.shape, dtype=complex)
for ps in cols:
    Au += mu(ps) * nu(ps) * (chi_arr(ps, UA, UB) if ps else 1.0) * W(nm(ps))
L0 = complex(np.sum(Phi(UN / H) * np.abs(Au) ** 2)) + abs(W(1)) ** 2   # u = 0: A_0 = W(1) (n = 1 only)

# ---- zero frequency Z ----
Z = 0.0
for g in cols:
    pr = 1.0
    for p in g: pr *= (1 - 1 / p.q)
    Z += H * hatPhi(0.0) * abs(W(nm(g))) ** 2 * pr

def divisors(ps):
    return [list(c) for k in range(len(ps) + 1) for c in itertools.combinations(ps, k)]

# enumerate (g, z1, z2) with g z1, g z2 in cols, (z1,z2)=1
colset = {key(ps): ps for ps in cols}
triples = []
for n1 in cols:
    for n2 in cols:
        s1 = set(p.g for p in n1); s2 = set(p.g for p in n2)
        g = [p for p in n1 if p.g in s2]
        z1 = [p for p in n1 if p.g not in s2]; z2 = [p for p in n2 if p.g not in s1]
        triples.append((g, z1, z2, n1, n2))
print("pairs (n1,n2):", len(triples))

# ---- L1: after Lemma 4.2, Gauss sum by brute force ----
L1 = 0j
gcache = {}
for g, z1, z2, n1, n2 in triples:
    m = mul(elt(z1), elt(z2)); Nm = norm(m)
    kk = (key(z1), key(z2))
    if kk not in gcache:
        if z1 or z2:
            def chf(A_, B_, z1=z1, z2=z2):
                v = np.ones(A_.shape, dtype=complex)
                if z1: v = v * np.conj(chi_arr(z1, A_, B_))
                if z2: v = v * chi_arr(z2, A_, B_)
                return v
            gcache[kk] = gauss_general(m, chf)
        else:
            gcache[kk] = 1.0 + 0j
    gam = gcache[kk]
    coef = mu(z1) * mu(z2) * np.conj(nu(z1)) * nu(z2) * np.conj(W(nm(n1))) * W(nm(n2))
    chih = np.conj(np.conj(CH[key(z1)]) * CH[key(z2)])          # conj(chi(h)), chi = conj(chi_z1) chi_z2
    inner = 0j
    for e in divisors(g):
        Ne = nm(e); ev = elt(e)
        chie = np.conj(chi_el(z1, ev)) * chi_el(z2, ev)
        inner += mu(e) * chie / Ne * np.sum(chih * hatPhi(H * HN / (Ne * Nm)))
    L1 += coef * H * gam / math.sqrt(Nm) * inner

# ---- L2: (g,e,h,z1,z2) form with a_xi and Psi ----
L2 = 0j
for g, z1, z2, n1, n2 in triples:
    Nm = nm(z1) * nm(z2)
    base = Psi(z1, z2) * a(z1) * np.conj(a(z2)) * W0(nm(n1)) * np.conj(W0(nm(n2)))
    for e in divisors(g):
        Ne = nm(e); e5 = power(elt(e), 5)
        fac = chi_el(z1, e5) * np.conj(chi_el(z2, e5))
        s = np.sum(CH[key(z1)] * np.conj(CH[key(z2)]) * hatPhi(H * HN / (Ne * Nm)))
        L2 += H * mu(e) * nm(g) / Ne * base * fac * s

# ---- L3: (b,f,k,m1,m2) form, (eq:initial-column-output) ----
L3 = 0j
nterms = 0
for b in cols:
    for f in cols:
        if set(p.g for p in b) & set(p.g for p in f): continue
        Nbf = nm(b) * nm(f)
        if Nbf > NMAX: continue
        f4 = power(elt(f), 4)
        ms = [m for m in cols if not (set(p.g for p in m) & set(p.g for p in b)) and Nbf * nm(m) <= NMAX]
        for m1 in ms:
            c1 = chi_el(m1, f4)
            if c1 == 0: continue
            for m2 in ms:
                c2 = chi_el(m2, f4)
                if c2 == 0: continue
                coef = mu(f) * nm(b) * Psi(m1, m2) * a(m1) * np.conj(a(m2)) * c1 * np.conj(c2) \
                       * W0(Nbf * nm(m1)) * np.conj(W0(Nbf * nm(m2)))
                s = np.sum(CH[key(m1)] * np.conj(CH[key(m2)]) * hatPhi(H * HN / (nm(f) ** 2 * nm(m1) * nm(m2))))
                L3 += H * coef * s
                nterms += 1
print("L3 (b,f,m1,m2) combinations:", nterms)

def show(name, v):
    print("%-48s %.12g%+.12gj   relerr vs L0 = %.2e" % (name, v.real, v.imag, abs(v - L0) / abs(L0)))
show("L0  direct sum_u Phi |A_u|^2", L0)
show("L1  Z + Poisson (brute-force Gauss sums)", Z + L1)
show("L2  Z + sum_xi c_xi S_xi, (g,e,h) form", Z + L2)
show("L3  Z + sum_xi c_xi S_xi, (b,f,k) form", Z + L3)
print("Z =", Z, "  |L0 - Z| =", abs(L0 - Z))
ok = all(abs(v - L0) / abs(L0) < 1e-9 for v in [Z + L1, Z + L2, Z + L3])
print("PROP 4.5 IDENTITY CHAIN:", "OK" if ok else "FAIL")

# ---- negative control: drop the chi_n(-1) factor in (quotient) by using G(z1 z2^{-1}) ----
L3bad = 0j
for b in cols:
    for f in cols:
        if set(p.g for p in b) & set(p.g for p in f): continue
        Nbf = nm(b) * nm(f)
        if Nbf > NMAX: continue
        f4 = power(elt(f), 4)
        ms = [m for m in cols if not (set(p.g for p in m) & set(p.g for p in b)) and Nbf * nm(m) <= NMAX]
        for m1 in ms:
            for m2 in ms:
                c1 = chi_el(m1, f4); c2 = chi_el(m2, f4)
                if c1 == 0 or c2 == 0: continue
                t = mod4(mul(elt(m1), inv4(mod4(elt(m2)))))
                PsiBad = np.conj(nu(m1)) * nu(m2) * G_class[t]
                coef = mu(f) * nm(b) * PsiBad * a(m1) * np.conj(a(m2)) * c1 * np.conj(c2) \
                       * W0(Nbf * nm(m1)) * np.conj(W0(Nbf * nm(m2)))
                L3bad += H * coef * np.sum(CH[key(m1)] * np.conj(CH[key(m2)]) * hatPhi(H * HN / (nm(f) ** 2 * nm(m1) * nm(m2))))
print("negative control (G(z1/z2) in place of G(z2/z1)): relerr = %.2e (should be O(1))" % (abs(Z + L3bad - L0) / abs(L0)))

# ---- Lemma 4.4 identity: C_r(X;k,f) = sum_{d|r0,(d,f)=1} mu(d) a(d) chi_d(k) chi_d(f)^4 C_1(X/N(d);k,df) ----
def xi(ps): return psi[nm(ps) % 5]                     # a nontrivial ray class character
def axi(ps): return a(ps) * xi(ps)
fails44 = 0; tests44 = 0
for trial in range(300):
    r0 = random.sample(P[:10], random.randint(1, 3))
    f = random.choice([c for c in cols if nm(c) <= 50])
    kk = (random.randint(-40, 40), random.randint(-40, 40))
    if kk == (0, 0): continue
    Xw = {N: complex(random.gauss(0, 1), random.gauss(0, 1)) for N in range(1, NMAX + 1)}   # W(N(n)/X) := Xw[N(n)]
    r0g = set(p.g for p in r0)
    lhs = sum(axi(n) * chi_el(n, kk) * chi_el(n, power(elt(f), 4)) * Xw[nm(n)]
              for n in cols if not (set(p.g for p in n) & r0g))
    rhs = 0j
    for d in divisors(r0):
        if set(p.g for p in d) & set(p.g for p in f): continue
        df = d + f; df4 = power(elt(df), 4)
        # C_1(X/N(d); k, df): sum over squarefree m of a(m) chi_m(k) chi_m(df)^4 W(N(m) N(d)/X)
        C1 = sum(axi(m) * chi_el(m, kk) * chi_el(m, df4) * Xw[nm(m) * nm(d)]
                 for m in cols if nm(m) * nm(d) <= NMAX)
        rhs += mu(d) * axi(d) * chi_el(d, kk) * chi_el(d, power(elt(f), 4)) * C1
    tests44 += 1
    if abs(lhs - rhs) > 1e-9 * max(1, abs(lhs)): fails44 += 1
print("Lemma 4.4 identity: tests %d failures %d" % (tests44, fails44))
