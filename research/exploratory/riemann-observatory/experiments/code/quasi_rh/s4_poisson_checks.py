# Level-2 audit, Section 4: Lemma 4.2 (Poisson summation with excluded primes,
# paper2.tex l.875-932), tested as an exact identity with a Gaussian Schwartz weight.
#   Phi(t) = exp(-pi t)  (t = |z|^2),  hatPhi(|w|^2) = (2/sqrt3) int Phi(|z|^2) e(-zw) dx dy
#   claimed closed form for this Phi: hatPhi(t) = (2/sqrt3) exp(-4 pi t / 3).
# Run:  python3 -I s4_poisson_checks.py
import sys, os, math, cmath, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from s4_zw import *

def Phi(t): return np.exp(-np.pi * t)
def hatPhi(t): return (2 / SQ3) * np.exp(-4 * np.pi * t / 3)

fails = 0; tests = 0
def report(name, lhs, rhs, tol=1e-9):
    global fails, tests
    tests += 1
    err = abs(lhs - rhs) / max(1.0, abs(lhs))
    ok = err < tol
    if not ok: fails += 1
    print("%-62s lhs=%-26s rhs=%-26s relerr=%.1e %s" % (name, "%.10g%+.10gj" % (lhs.real, lhs.imag),
          "%.10g%+.10gj" % (rhs.real, rhs.imag), err, "OK" if ok else "FAIL"))
    return ok

# ---- (0) hatPhi by direct quadrature of the defining integral (l.897-902) ----
from scipy import integrate
for w in [0.0, 0.31 + 0.2j, -0.8 + 0.45j, 1.1j]:
    def fr(y, x):
        z = complex(x, y); return (math.exp(-math.pi * abs(z) ** 2) * cmath.exp(-4j * math.pi * (z * w).imag / SQ3)).real
    def fi(y, x):
        z = complex(x, y); return (math.exp(-math.pi * abs(z) ** 2) * cmath.exp(-4j * math.pi * (z * w).imag / SQ3)).imag
    re_ = integrate.dblquad(fr, -7, 7, -7, 7, epsabs=1e-12)[0]
    im_ = integrate.dblquad(fi, -7, 7, -7, 7, epsabs=1e-12)[0]
    report("hatPhi quadrature vs closed form, w=%s" % w, (2 / SQ3) * complex(re_, im_), complex(hatPhi(abs(w) ** 2)))

# ---- (1) plain lattice Poisson: O self-dual under e, covolume 1 for (2/sqrt3)dxdy ----
for H in [0.37, 1.0, 2.9, 13.3]:
    A, B = lattice_points(14 * H + 20)
    lhs = 1 + np.sum(Phi((A * A - A * B + B * B) / H))
    A2, B2 = lattice_points(12 / H + 20)
    rhs = H * (hatPhi(0) + np.sum(hatPhi(H * (A2 * A2 - A2 * B2 + B2 * B2))))
    report("sum_k Phi(Nk/H) = H sum_h hatPhi(H Nh), H=%g" % H, complex(lhs), complex(rhs))
# negative control: wrong pairing e(z conj w) / missing 2/sqrt3 factor would change the answer
H = 2.9
A, B = lattice_points(14 * H + 20); lhs = 1 + np.sum(Phi((A * A - A * B + B * B) / H))
A2, B2 = lattice_points(12 / H + 20)
bad = H * (SQ3 / 2) * (hatPhi(0) + np.sum(hatPhi(H * (A2 * A2 - A2 * B2 + B2 * B2))))
print("negative control (covolume factor omitted): relerr = %.2e (should be large)" % (abs(lhs - bad) / lhs))

# ---- (2) Lemma 4.2 with characters, exclusions, Gauss sums ----
P = eisenstein_primes(130)
byg = {p.g: p for p in P}
TWO = (2, 0); LAM = (1, 2)       # generators of the primes above 2 and 3 (deliberately non-primary for 2)

def div_arr(p, A, B):
    """boolean array: element p divides (A + B omega)"""
    n = norm(p); c0, c1 = conj(p)
    z0 = A * c0 - B * c1; z1 = A * c1 + B * c0 - B * c1
    return (z0 % n == 0) & (z1 % n == 0)

def make_char(spec):
    """spec: list of (Prime, exponent j) -> primitive character prod chi_p^j with modulus prod p"""
    def f(A, B):
        v = np.ones(A.shape, dtype=complex)
        for p, j in spec:
            v = v * chi_arr([p], A, B, j)
        return v
    m = prod([p.g for p, j in spec]) if spec else (1, 0)
    return f, m

def lemma42(spec, r_primes, H, label):
    """r_primes: list of prime *elements* (generators) of rad r"""
    ch, m = make_char(spec)
    Nm = norm(m)
    # LHS
    R = 14 * H + 30
    A, B = lattice_points(R)
    mask = np.ones(A.shape, dtype=bool)
    for p in r_primes:
        mask &= ~div_arr(p, A, B)
    lhs = complex(np.sum(ch(A, B) * mask * Phi((A * A - A * B + B * B) / H)))
    # k = 0 term: chi(0) 1_{(0,r)=1}; chi(0) = 1 only for the principal character mod 1
    if not spec and not r_primes:
        lhs += 1.0
    # RHS
    gam = gauss_general(m, ch) if spec else 1.0 + 0j
    tot = 0j
    for sub in itertools.chain.from_iterable(itertools.combinations(r_primes, k) for k in range(len(r_primes) + 1)):
        d = prod(list(sub)) if sub else (1, 0)
        Nd = norm(d); mu = (-1) ** len(sub)
        chd = complex(ch(np.array([d[0]]), np.array([d[1]]))[0]) if spec else 1.0
        if chd == 0: continue
        Rh = 11 * Nd * Nm / H + 30
        A2, B2 = lattice_points(Rh)
        vals = np.conj(ch(A2, B2)) if spec else np.ones(A2.shape)
        s = np.sum(vals * hatPhi(H * (A2 * A2 - A2 * B2 + B2 * B2) / (Nd * Nm)))
        if not spec:
            s += hatPhi(0.0)        # h = 0 term, conj(chi(0)) = 1 for the principal character
        tot += mu * chd / Nd * s
    rhs = H * gam / math.sqrt(Nm) * tot
    return report(label, lhs, complex(rhs))

p7, p7b, p13, p19 = P[0].g, P[1].g, P[2].g, P[4].g
pr = {p.g: p for p in P}
q5 = next(p for p in P if not p.split)         # inert prime 5
print("\nprimes used:", P[0], P[1], P[2], P[4], q5)
for H in [0.7, 3.3, 17.0]:
    lemma42([], [], H, "principal, no exclusion, H=%g" % H)
    lemma42([], [TWO, LAM, p7], H, "principal, r=2*lam*p7 (zero-frequency product), H=%g" % H)
    lemma42([(P[0], 1)], [], H, "chi_p7, H=%g" % H)
    lemma42([(P[0], 5)], [p13, TWO], H, "chi_p7^5, r=p13*2, H=%g" % H)
    lemma42([(q5, 2)], [p7, LAM], H, "chi_5^2 (inert), r=p7*lam, H=%g" % H)
    lemma42([(P[0], -1), (P[2], 1)], [p19], H, "conj(chi_z1) chi_z2, z1=p7,z2=p13, r=p19, H=%g" % H)
    lemma42([(P[0], -1), (P[1], 1)], [p13, p19], H, "conj(chi_p7) chi_p7bar, r=p13*p19, H=%g" % H)
    lemma42([(P[0], -1), (q5, 1)], [p7, p13], H, "conj(chi_p7) chi_5, r shares p7 with m, H=%g" % H)
    lemma42([(P[2], 3), (P[4], 1)], [TWO, LAM], H, "chi_p13^3 chi_p19, r=2*lam, H=%g" % H)

# negative control: imprimitive character (chi_p7 viewed mod p7*p13) breaks the formula
ch0, _ = make_char([(P[0], 1)])
def ch_imp(A, B): return ch0(A, B) * (~div_arr(p13, A, B))
m_imp = mul(p7, p13); H = 3.3
A, B = lattice_points(14 * H + 30)
lhs = complex(np.sum(ch_imp(A, B) * Phi((A * A - A * B + B * B) / H)))
gam = gauss_general(m_imp, ch_imp)
A2, B2 = lattice_points(11 * norm(m_imp) / H + 30)
rhs = H * gam / math.sqrt(norm(m_imp)) * np.sum(np.conj(ch_imp(A2, B2)) * hatPhi(H * (A2 * A2 - A2 * B2 + B2 * B2) / norm(m_imp)))
print("negative control (imprimitive character): |lhs-rhs| = %.3e (should be nonzero)" % abs(lhs - rhs))

print("\nLemma 4.2 / Poisson tests: %d, failures: %d" % (tests, fails))

# ---- (3) Strengthened test.  For a radial weight, both sides of (eq:poisson) vanish
# identically whenever chi is non-trivial on the units (sum over the unit orbit), so the
# radial tests above only have content for unit-trivial chi.  We therefore also test the
# underlying Poisson mechanism with a SHIFTED Gaussian f(z)=Phi(|z-z0|^2/H); the same proof
# (inclusion-exclusion, k=dl, lattice Poisson, primitive Gauss sum) gives
#   sum_k chi(k)1_{(k,r)=1} f(k)
#     = (H gamma(chi)/sqrt(Nm)) sum_{d|rad r} mu(d)chi(d)/N(d)
#          sum_h conj(chi(h)) e(-z0 h/(d m)) hatPhi(H N(h)/(N(d)N(m))),
# which reduces to (eq:poisson) at z0=0.  This tests the dual lattice m^{-1}O, the
# sign conventions (conj(chi(h)) and e(-zw)), and the 2/sqrt3 normalisation.
def lemma42_shift(spec, r_primes, H, z0, label):
    ch, m = make_char(spec)
    Nm = norm(m)
    A, B = lattice_points(14 * H + 60 + 4 * abs(z0) ** 2)
    mask = np.ones(A.shape, dtype=bool)
    for p in r_primes:
        mask &= ~div_arr(p, A, B)
    Z = A + B * OMEGA
    lhs = complex(np.sum(ch(A, B) * mask * Phi(np.abs(Z - z0) ** 2 / H)))
    if not spec and not r_primes:
        lhs += complex(Phi(abs(z0) ** 2 / H))
    gam = gauss_general(m, ch) if spec else 1.0 + 0j
    tot = 0j
    for sub in itertools.chain.from_iterable(itertools.combinations(r_primes, k) for k in range(len(r_primes) + 1)):
        d = prod(list(sub)) if sub else (1, 0)
        Nd = norm(d); mu = (-1) ** len(sub)
        chd = complex(ch(np.array([d[0]]), np.array([d[1]]))[0]) if spec else 1.0
        if chd == 0: continue
        A2, B2 = lattice_points(11 * Nd * Nm / H + 30)
        Hh = A2 + B2 * OMEGA
        vals = np.conj(ch(A2, B2)) if spec else np.ones(A2.shape)
        ph = np.exp(-4j * np.pi * (z0 * Hh / cv(mul(d, m))).imag / SQ3)
        s = np.sum(vals * ph * hatPhi(H * (A2 * A2 - A2 * B2 + B2 * B2) / (Nd * Nm)))
        if not spec:
            s += hatPhi(0.0)
        tot += mu * chd / Nd * s
    rhs = H * gam / math.sqrt(Nm) * tot
    return report(label, lhs, complex(rhs))

print("\nshifted-Gaussian tests (non-trivial for characters non-trivial on units):")
for H, z0 in [(0.9, 0.37 - 0.21j), (4.1, 1.3 + 0.8j), (12.0, -2.2 + 0.4j)]:
    lemma42_shift([], [TWO, LAM, p7], H, z0, "principal, r=2*lam*p7, H=%g" % H)
    lemma42_shift([(P[0], 1)], [], H, z0, "chi_p7, H=%g" % H)
    lemma42_shift([(P[0], 5)], [p13, TWO], H, z0, "chi_p7^5, r=p13*2, H=%g" % H)
    lemma42_shift([(q5, 2)], [p7, LAM], H, z0, "chi_5^2 (inert), r=p7*lam, H=%g" % H)
    lemma42_shift([(P[0], -1), (P[2], 1)], [p19], H, z0, "conj(chi_p7) chi_p13, r=p19, H=%g" % H)
    lemma42_shift([(P[0], -1), (q5, 1)], [p7, p13], H, z0, "conj(chi_p7) chi_5, r shares p7, H=%g" % H)
    lemma42_shift([(P[2], 3), (P[4], 1)], [TWO, LAM], H, z0, "chi_p13^3 chi_p19, r=2*lam, H=%g" % H)
# negative controls with the shift: imprimitive character; chi(h) in place of conj(chi(h))
H, z0 = 4.1, 1.3 + 0.8j
A, B = lattice_points(14 * H + 80); Z = A + B * OMEGA
lhs = complex(np.sum(ch_imp(A, B) * Phi(np.abs(Z - z0) ** 2 / H)))
gam = gauss_general(m_imp, ch_imp)
A2, B2 = lattice_points(11 * norm(m_imp) / H + 30); Hh = A2 + B2 * OMEGA
ph = np.exp(-4j * np.pi * (z0 * Hh / cv(m_imp)).imag / SQ3)
rhs = H * gam / math.sqrt(norm(m_imp)) * np.sum(np.conj(ch_imp(A2, B2)) * ph * hatPhi(H * (A2 * A2 - A2 * B2 + B2 * B2) / norm(m_imp)))
print("negative control (imprimitive, shifted): |lhs-rhs|/|lhs| = %.3e (should be O(1))" % (abs(lhs - rhs) / abs(lhs)))
ch1, m1 = make_char([(P[0], 1), (P[2], 2)])
lhs = complex(np.sum(ch1(A, B) * Phi(np.abs(Z - z0) ** 2 / H)))
gam = gauss_general(m1, ch1)
A2, B2 = lattice_points(11 * norm(m1) / H + 30); Hh = A2 + B2 * OMEGA
ph = np.exp(-4j * np.pi * (z0 * Hh / cv(m1)).imag / SQ3)
rhs_bad = H * gam / math.sqrt(norm(m1)) * np.sum(ch1(A2, B2) * ph * hatPhi(H * (A2 * A2 - A2 * B2 + B2 * B2) / norm(m1)))
print("negative control (chi(h) instead of conj chi(h)): |lhs-rhs|/|lhs| = %.3e (should be O(1))" % (abs(lhs - rhs_bad) / abs(lhs)))
print("\nTOTAL Lemma 4.2 / Poisson tests: %d, failures: %d" % (tests, fails))
