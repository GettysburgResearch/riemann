#!/usr/bin/env python3
"""Absorption identities for candidate leverage families (LEVERAGE_FAMILIES.md, Sections 1-2).

Labels:  EXACT = Jacobi sums and residue symbols computed in Z[omega] / Z[i] with integer arithmetic.
         FLOAT = normalized Gauss sums in double precision (not directed, not certified).

Part S (K = Q(omega), sextic symbol chi_n = (./n)_6, conventions of a2/eis.py = the Oct 5 manuscript):
  S1 EXACT  J(chi^2, chi^2) = -p                      (Stickelberger sign = the Moebius sign)
  S2 EXACT  chi(4) J(chi, chi) = J(chi, chi^3)        (Hasse-Davenport duplication, paper's proof)
  S3 FLOAT  gamma_2^3 = mu alpha;  gamma_1 gamma_2 = mu alpha G,  G = conj(chi(4)) gamma_3   [eq:gj]
  S4 FLOAT  eq:convert2  mu gamma_{-1} = chi(-1) G^{-1} conj(alpha) gamma_2, primes AND composites
  S5 FLOAT  product family (two cubic Poisson sums): mu gamma_2^2 = alpha gamma_4, primes and composites
  S6 FLOAT  cubic family (one cubic Poisson sum):  mu gamma_2 = chi(-1) alpha G gamma_{-1}
            (mu x cubic Gauss sum = Hecke x quadratic x SEXTIC Gauss sum; no cubic-theta coefficient)
  S7 FLOAT  cubic family vs cubic theta: f = mu gamma_2 / gamma_4 satisfies f^3 = -alpha^2 (so f is
            not a Hecke character: its infinity type would be alpha^{2/3}); mu gamma_2/gamma_2 = -1.
Part Q (K = Q(i), quartic symbol chi = (./pi)_4, pi primary = 1 mod (2+2i)):
  Q1 EXACT  J(chi, chi) = -chi(-1) pi                  (Ireland-Rosen Prop. 9.9.4; the Moebius sign)
  Q2 FLOAT  mu gamma(chi)^2 = chi(-1) alpha gamma(rho),  rho = chi^2 quadratic
  Q3 FLOAT  mu gamma(chi) = chi(-1) alpha gamma(rho) conj(gamma(chi))
            (mu x quartic Poisson Gauss sum = Hecke x quadratic x conj quartic Gauss sum, which is the
             shape of the 4-fold GL(3) theta coefficient tau(p,1) = |p|^{-1/2} conj g(p) of FG15)
  Q4 FLOAT  quadratic family over Q(i): mu gamma(rho) / gamma(rho) = -1 (nothing to absorb into)

Usage: python3 leverage_gauss_checks.py [MAXNORM_PRIME=400] [MAXNORM_COMPOSITE=1500] [OUT.json]
Runtime about 10 s.  Imports a2/eis.py (read-only)."""
import cmath, itertools, json, math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import eis
from eis import UNITS, ZETA, mul, norm, sym_prime, primes_upto, residues, gamma

MAXP = int(sys.argv[1]) if len(sys.argv) > 1 else 400
MAXC = int(sys.argv[2]) if len(sys.argv) > 2 else 1500
OUT = sys.argv[3] if len(sys.argv) > 3 else None
res = {'params': {'MAXP': MAXP, 'MAXC': MAXC}}

# ---------------------------------------------------------------- Part S: Z[omega], sextic
def eis_add(x, y): return (x[0] + y[0], x[1] + y[1])
def eis_c(x): return complex(x[0] - x[1]/2, x[1]*math.sqrt(3)/2)
def jacobi_sextic(p, a, b):
    """J(chi^a, chi^b) = sum_x chi^a(x) chi^b(1-x), exact in Z[omega]; zero extension."""
    R, N = residues(p)
    s = (0, 0)
    for x in R:
        kx = sym_prime(x, p); ky = sym_prime((1 - x[0], -x[1]), p)
        if kx is None or ky is None: continue
        s = eis_add(s, UNITS[(a*kx + b*ky) % 6])
    return s

P = primes_upto(MAXP)
S1 = S2 = 0; S1_fail = []; S2_fail = []
dev = {k: 0.0 for k in ['S3a', 'S3b', 'S4', 'S5', 'S6', 'S7a', 'S7b']}
ctrl = {'S3b_without_mu_min': 9.0, 'S5_without_mu_min': 9.0}   # controls: drop mu, expect |.| = 2
nprime = 0
for p in P:
    nprime += 1
    k4, km1 = sym_prime((4, 0), p), sym_prime((-1, 0), p)
    J22 = jacobi_sextic(p, 2, 2)
    if J22 == (-p[0], -p[1]): S1 += 1
    else: S1_fail.append((p, J22))
    J11, J13 = jacobi_sextic(p, 1, 1), jacobi_sextic(p, 1, 3)
    if mul(UNITS[k4], J11) == J13: S2 += 1
    else: S2_fail.append((p, J11, J13))
    g = {j: gamma(j, [p]) for j in (-1, 1, 2, 3, 4)}
    al = eis_c(p)/abs(eis_c(p)); mu = -1
    G = ZETA[(-k4) % 6]*g[3]
    dev['S3a'] = max(dev['S3a'], abs(g[2]**3 - mu*al))
    dev['S3b'] = max(dev['S3b'], abs(g[1]*g[2] - mu*al*G))
    dev['S4'] = max(dev['S4'], abs(mu*g[-1] - ZETA[km1]*al.conjugate()*g[2]/G))
    dev['S5'] = max(dev['S5'], abs(mu*g[2]**2 - al*g[4]))
    dev['S6'] = max(dev['S6'], abs(mu*g[2] - ZETA[km1]*al*G*g[-1]))
    ctrl['S3b_without_mu_min'] = min(ctrl['S3b_without_mu_min'], abs(g[1]*g[2] - al*G))
    ctrl['S5_without_mu_min'] = min(ctrl['S5_without_mu_min'], abs(g[2]**2 - al*g[4]))
    f = mu*g[2]/g[4]
    dev['S7a'] = max(dev['S7a'], abs(f**3 + al**2))
    dev['S7b'] = max(dev['S7b'], abs(mu*g[2]/g[2] + 1))
res['S'] = {'primes': nprime, 'S1_J22_eq_minus_p': f'{S1}/{nprime}', 'S1_fail': S1_fail,
            'S2_HD_duplication': f'{S2}/{nprime}', 'S2_fail': S2_fail,
            'max_dev_prime': dev.copy(), 'controls_min_dev': ctrl,
            'inert_primes_included': [p for p in P if p[1] == 0]}

# composites: squarefree products of 2 or 3 distinct primes, norm <= MAXC
comp = []
for r in (2, 3):
    for fac in itertools.combinations(P, r):
        if math.prod(norm(q) for q in fac) <= MAXC: comp.append(list(fac))
cdev = {'S4': 0.0, 'S5': 0.0, 'S6': 0.0}
for fac in comp:
    n = (1, 0)
    for q in fac: n = mul(n, q)
    mu = (-1)**len(fac)
    k4 = sum(sym_prime((4, 0), q) for q in fac) % 6
    km1 = sum(sym_prime((-1, 0), q) for q in fac) % 6
    g = {j: gamma(j, fac) for j in (-1, 2, 3, 4)}
    al = eis_c(n)/abs(eis_c(n)); G = ZETA[(-k4) % 6]*g[3]
    cdev['S4'] = max(cdev['S4'], abs(mu*g[-1] - ZETA[km1]*al.conjugate()*g[2]/G))
    cdev['S5'] = max(cdev['S5'], abs(mu*g[2]**2 - al*g[4]))
    cdev['S6'] = max(cdev['S6'], abs(mu*g[2] - ZETA[km1]*al*G*g[-1]))
res['S']['composites'] = len(comp)
res['S']['max_dev_composite'] = cdev

# ---------------------------------------------------------------- Part Q: Z[i], quartic
I4 = [(1, 0), (0, 1), (-1, 0), (0, -1)]          # i^k
def gmul(x, y): return (x[0]*y[0] - x[1]*y[1], x[0]*y[1] + x[1]*y[0])
def gconj(x): return (x[0], -x[1])
def gnorm(x): return x[0]*x[0] + x[1]*x[1]
def gdivides(m, z):
    c, d = gmul(z, gconj(m)); n = gnorm(m)
    return c % n == 0 and d % n == 0
def gred(z, m):
    c, d = gmul(z, gconj(m)); n = gnorm(m)
    q = ((2*c + n)//(2*n), (2*d + n)//(2*n)); qm = gmul(q, m)
    return (z[0] - qm[0], z[1] - qm[1])
def gpow(z, e, m):
    r, b = (1, 0), gred(z, m)
    while e:
        if e & 1: r = gred(gmul(r, b), m)
        b = gred(gmul(b, b), m); e >>= 1
    return r
def gprimary(x):
    for u in I4:
        y = gmul(u, x)
        if gdivides((2, 2), (y[0] - 1, y[1])): return y
    raise ValueError(x)
def qsym(x, p):
    """(x/p)_4 as k (value i^k), None if p | x."""
    if gdivides(p, x): return None
    t = gpow(x, (gnorm(p) - 1)//4, p)
    for k, z in enumerate(I4):
        if gdivides(p, (t[0] - z[0], t[1] - z[1])): return k
    raise RuntimeError
def gauss_primes(N):
    out = []
    for q in range(3, N + 1):
        if any(q % d == 0 for d in range(2, int(q**0.5) + 1)): continue
        if q % 4 == 1:
            a = next(a for a in range(1, q) if int(round((q - a*a)**0.5))**2 == q - a*a)
            b = int(round((q - a*a)**0.5))
            out += [gprimary((a, b)), gprimary((a, -b))]
        elif q*q <= N:
            out.append(gprimary((q, 0)))
    return sorted(set(out), key=gnorm)
def gres(p):
    if p[1] == 0: q = abs(p[0]); return [(a, b) for a in range(q) for b in range(q)]
    return [(a, 0) for a in range(gnorm(p))]
def gpsi(x, p):
    c, d = gmul(x, gconj(p)); return cmath.exp(2j*math.pi*(c % gnorm(p))/gnorm(p))  # exp(2 pi i Re(x/p))
def ggamma(j, p):
    s = 0
    for x in gres(p):
        k = qsym(x, p)
        if k is None: continue
        s += (1j**((j*k) % 4))*gpsi(x, p)
    return s/math.sqrt(gnorm(p))

GP = gauss_primes(MAXP)
Q1 = 0; Q1_fail = []; qdev = {'Q2': 0.0, 'Q3': 0.0, 'Q4': 0.0, 'gauss_jacobi': 0.0}
qctrl = {'Q2_without_mu_min': 9.0}
for p in GP:
    J = (0, 0)
    for x in gres(p):
        kx, ky = qsym(x, p), qsym((1 - x[0], -x[1]), p)
        if kx is None or ky is None: continue
        u = I4[(kx + ky) % 4]; J = (J[0] + u[0], J[1] + u[1])
    km1 = qsym((-1, 0), p)
    target = gmul(I4[(km1 + 2) % 4], p)            # -chi(-1) pi
    if J == target: Q1 += 1
    else: Q1_fail.append((p, J, target))
    g1, g2 = ggamma(1, p), ggamma(2, p)
    al = complex(*p)/abs(complex(*p)); mu = -1; cm1 = 1j**km1
    qdev['gauss_jacobi'] = max(qdev['gauss_jacobi'], abs(g1*g1 - complex(*J)/abs(complex(*p))*g2))
    qdev['Q2'] = max(qdev['Q2'], abs(mu*g1*g1 - cm1*al*g2))
    qdev['Q3'] = max(qdev['Q3'], abs(mu*g1 - cm1*al*g2*g1.conjugate()))
    qctrl['Q2_without_mu_min'] = min(qctrl['Q2_without_mu_min'], abs(g1*g1 - cm1*al*g2))
    qdev['Q4'] = max(qdev['Q4'], abs(mu*g2/g2 + 1))
res['Q'] = {'primes': len(GP), 'inert': [p for p in GP if p[1] == 0],
            'Q1_J_eq_minus_chi(-1)_pi': f'{Q1}/{len(GP)}', 'Q1_fail': Q1_fail, 'max_dev': qdev,
            'controls_min_dev': qctrl}

print(json.dumps(res, indent=1, default=str))
if OUT:
    with open(OUT, 'w') as fh: json.dump(res, fh, indent=1, default=str)
