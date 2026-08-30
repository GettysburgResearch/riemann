"""Epstein-Eisenstein lattice-moduli zero-bifurcation lab (programme #764, exp 16; parent-shadow mode 7).

ARITHMETIC CLASS: NON_DIRECTED_HIGH_PRECISION.  All outputs are conjecture-generating
numerical evidence with stated truncation bounds and non-directed floating rounding.
Nothing here is a theorem; "zero" and "departure" always mean "numerically located to
the stated precision".  RH is NOT established and nothing below claims otherwise.

Moduli parametrization
----------------------
For z = x + iy in the upper half plane, the determinant-1 positive binary quadratic form is

    Q_z(m,n) = |m z + n|^2 / y = (m^2 (x^2+y^2) + 2 m n x + n^2) / y ,   det = 1.

Epstein zeta:  Z_z(s) = sum_{(m,n) != (0,0)} Q_z(m,n)^{-s}   (Re s > 1, then continued).

Completed function and the convention actually used (derived, then oracle-validated)
-----------------------------------------------------------------------------------
Let theta_z(t) = sum_{(m,n) in Z^2} exp(-pi t Q_z(m,n))  (the (0,0) term included).
Because det Q_z = 1, Poisson summation gives theta_z(1/t) = t * theta_z(t)
(numerically asserted at t = 0.7 and t = 1.3 to 30 digits in selftest()).

With Lambda_z(s) = pi^{-s} Gamma(s) Z_z(s) = int_0^inf (theta_z(t) - 1) t^{s-1} dt,
splitting the integral at t = 1 and applying the transformation on (0,1):

    Lambda_z(s) = -1/s - 1/(1-s)
                  + sum_{(m,n) != (0,0)} [ (pi Q)^{-s} Gamma(s, pi Q) + (pi Q)^{s-1} Gamma(1-s, pi Q) ],

with Q = Q_z(m,n) and Gamma(a,x) the UPPER incomplete gamma (mpmath.gammainc(a, x)).
NOTE the sum runs over ALL nonzero (m,n), with NO extra factor 1/2: this convention is
the one validated by oracle O1 (direct lattice sum at z=i) and O2 (Z_i = 4 zeta beta).
The functional equation Lambda_z(s) = Lambda_z(1-s) is manifest, and Lambda_z is real
on the critical line (real coefficients + FE; verified numerically in O3/O4).

Truncation
----------
The lattice sum is truncated at Q_z(m,n) <= X_max where X_max = choose_Xmax(dps) is the
smallest half-integer X with  20 * (pi X + 10) * exp(-pi X) < 10^{-(dps+10)}.
Justification of the stated bound (non-formal, documented):
|Gamma(s,x)| <= Gamma(sigma, x) <= 2 x^{sigma-1} e^{-x} for x >= 2|sigma|+4, so each
discarded term has modulus <= 2 e^{-pi Q} / (pi Q) * (1 + (pi Q)^{2 sigma - 1}) <= 4 e^{-pi Q}
for sigma in [-6, 7] once pi Q >= 100, and the number of lattice points in the shell
Q in (X+k, X+k+1] is <= pi + 10 sqrt(X+k+1); summing the geometric-type series gives the
factor 20 (pi X + 10) margin.  For dps = 40 this yields X_max = 40.5 and a stated tail
< 1e-50 (absolute), uniform over the strip |Re s - 1/2| <= 6.5, |Im s| <= 40 used here.

Parent-shadow
-------------
Z_z(s) = 2 zeta(2s) E_1(z,s) with E_1(z,s) = (1/2) sum_{gcd(m,n)=1} y^s / |mz+n|^{2s}
       = (1/2) sum_{gcd(m,n)=1} Q_z(m,n)^{-s}; equivalently Lambda_z(s) = 2 E*(z,s) with
E*(z,s) = xi(2s) E_1(z,s) = xi(2s) y^s + xi(2s-1) y^{1-s}
          + 4 sqrt(y) sum_{n>=1} n^{s-1/2} sigma_{1-2s}(n) K_{s-1/2}(2 pi n y) cos(2 pi n x).
Both identities are verified numerically (see run_experiments E5 / parent_shadow.json).

All zero-finding runs at mp.dps >= 40; zero locations are reported to 12 digits.
"""

import math
import mpmath
from mpmath import mp, mpf, mpc

DPS_DEFAULT = 40
DPS_CLASSES = 60  # precision at which Q-class lists are precomputed


# ----------------------------------------------------------------------------
# lattice enumeration
# ----------------------------------------------------------------------------

def Q_of(x, y, m, n):
    """Q_z(m,n) = (m^2(x^2+y^2) + 2mnx + n^2)/y with mpf x,y."""
    return (m * m * (x * x + y * y) + 2 * m * n * x + n * n) / y


def lattice_points(x, y, X):
    """All (m,n) != (0,0) with Q_z(m,n) <= X (tolerance 1e-25). Norm-bounded enumerator:
    for fixed m, n ranges over the interval solved from the quadratic; |m| <= sqrt(X/y)."""
    x = mpf(x); y = mpf(y); X = mpf(X)
    tol = mpf('1e-25')
    out = []
    mmax = int(mp.floor(mp.sqrt(X / y) + tol))
    for m in range(-mmax, mmax + 1):
        disc = X * y - m * m * y * y
        if disc < 0:
            continue
        D = mp.sqrt(disc)
        c = -m * x
        nlo = int(mp.ceil(c - D - tol))
        nhi = int(mp.floor(c + D + tol))
        for n in range(nlo, nhi + 1):
            if m == 0 and n == 0:
                continue
            Q = Q_of(x, y, m, n)
            if Q <= X + tol:
                out.append((m, n, Q))
    return out


def brute_count(x, y, X, box=60):
    """Test oracle: brute-force double loop count of (m,n) != 0 with Q <= X."""
    x = mpf(x); y = mpf(y); X = mpf(X)
    tol = mpf('1e-25')
    cnt = 0
    for m in range(-box, box + 1):
        for n in range(-box, box + 1):
            if m == 0 and n == 0:
                continue
            if Q_of(x, y, m, n) <= X + tol:
                cnt += 1
    return cnt


_CLASS_CACHE = {}


def q_classes(x, y, X):
    """Sorted list of (Q, multiplicity) for 0 < Q <= X, computed at DPS_CLASSES and cached.
    Grouping key is Q rounded to 40 significant digits (values closer than that are merged,
    which perturbs the sum by < 1e-38 relative and is far below the stated tail bound)."""
    key = (float(x), float(y), float(X))
    got = _CLASS_CACHE.get(key)
    if got is not None:
        return got
    with mp.workdps(DPS_CLASSES):
        pts = lattice_points(mpf(x), mpf(y), mpf(X))
        d = {}
        for (m, n, Q) in pts:
            k = mp.nstr(Q, 40)
            if k in d:
                d[k][1] += 1
            else:
                d[k] = [Q, 1]
        cls = sorted(((v[0], v[1]) for v in d.values()), key=lambda p: float(p[0]))
    _CLASS_CACHE[key] = cls
    return cls


_XMAX_CACHE = {}


def choose_Xmax(dps):
    """Smallest half-integer X with 20*(pi X + 10)*exp(-pi X) < 10^{-(dps+10)}."""
    got = _XMAX_CACHE.get(dps)
    if got is not None:
        return got
    with mp.workdps(30):
        target = mpf(10) ** (-(dps + 10))
        X = mpf(10)
        while 20 * (mp.pi * X + 10) * mp.exp(-mp.pi * X) >= target:
            X += mpf('0.5')
    Xf = float(X)
    _XMAX_CACHE[dps] = Xf
    return Xf


# ----------------------------------------------------------------------------
# theta and its transformation (build-time assertion)
# ----------------------------------------------------------------------------

def theta_minus_1(x, y, t):
    """theta_z(t) - 1 = sum_{(m,n)!=0} exp(-pi t Q).  Truncated so the stated tail < 1e-(dps+8)."""
    t = mpf(t)
    X = (mp.dps + 12) * mp.log(10) / (mp.pi * t) + 5
    cls = q_classes(x, y, float(mp.ceil(X)))
    tot = mpf(0)
    for Q, mult in cls:
        tot += mult * mp.exp(-mp.pi * t * Q)
    return tot


def check_theta_transform(x, y, ts=(0.7, 1.3), digits=30):
    """Assert theta_z(1/t) = t * theta_z(t) to `digits` digits at each t. Returns worst |diff|."""
    worst = mpf(0)
    with mp.workdps(digits + 15):
        for t in ts:
            t = mpf(str(t))
            lhs = 1 + theta_minus_1(x, y, 1 / t)
            rhs = t * (1 + theta_minus_1(x, y, t))
            diff = abs(lhs - rhs)
            worst = max(worst, diff)
            assert diff < mpf(10) ** (-digits), \
                f"theta transform failed at t={t}: |diff|={mp.nstr(diff, 5)}"
    return worst


# ----------------------------------------------------------------------------
# the completed Epstein zeta Lambda_z(s)  (incomplete-gamma engine)
# ----------------------------------------------------------------------------

def lam(x, y, s, X=None):
    """Lambda_z(s), full complex, via the incomplete-gamma representation (see module docstring)."""
    if X is None:
        X = choose_Xmax(mp.dps)
    s = mpc(s)
    cls = q_classes(x, y, X)
    tot = -1 / s - 1 / (1 - s)
    pi = +mp.pi
    for Q, mult in cls:
        P = pi * Q
        term = mp.power(P, -s) * mp.gammainc(s, P) + mp.power(P, s - 1) * mp.gammainc(1 - s, P)
        tot += mult * term
    return tot


def lam_line(x, y, t, X=None):
    """F_z(t) = Lambda_z(1/2 + i t) as an exactly-real mpf.
    On the line 1-s = conj(s) and Gamma(conj s, x) = conj Gamma(s, x) (x real), so each
    lattice term is 2 Re[(pi Q)^{-s} Gamma(s, pi Q)]; -1/s - 1/(1-s) = -1/(1/4 + t^2).
    That Im Lambda vanishes on the line is verified independently in oracle O4 with lam()."""
    if X is None:
        X = choose_Xmax(mp.dps)
    t = mpf(t)
    s = mpc(mpf(1) / 2, t)
    cls = q_classes(x, y, X)
    tot = -1 / (mpf(1) / 4 + t * t)
    pi = +mp.pi
    for Q, mult in cls:
        P = pi * Q
        tot += 2 * mult * mp.re(mp.power(P, -s) * mp.gammainc(s, P))
    return tot


def Z_from_lam(x, y, s, X=None):
    """Z_z(s) = pi^s Lambda_z(s) / Gamma(s)."""
    s = mpc(s)
    return mp.power(mp.pi, s) * lam(x, y, s, X) / mp.gamma(s)


# ----------------------------------------------------------------------------
# Fourier/Bessel cross-check engine: Lambda_z(s) = 2 E*(z,s)
# ----------------------------------------------------------------------------

def xi_riemann(u):
    """xi(u) = pi^{-u/2} Gamma(u/2) zeta(u)  (completed Riemann zeta; poles at u=0,1)."""
    u = mpc(u)
    return mp.power(mp.pi, -u / 2) * mp.gamma(u / 2) * mp.zeta(u)


def _sigma_div(n, w):
    """sigma_w(n) = sum_{d | n} d^w, complex w."""
    tot = mpc(0)
    d = 1
    while d * d <= n:
        if n % d == 0:
            tot += mp.power(d, w)
            e = n // d
            if e != d:
                tot += mp.power(e, w)
        d += 1
    return tot


def lam_fourier(x, y, s, N=None):
    """Lambda_z(s) via the Eisenstein Fourier expansion (cross-check engine only):
    Lambda_z(s) = 2 xi(2s) y^s + 2 xi(2s-1) y^{1-s}
                  + 8 sqrt(y) sum_{n=1}^N n^{s-1/2} sigma_{1-2s}(n) K_{s-1/2}(2 pi n y) cos(2 pi n x)
    with N chosen from the stated bound |K_nu(v)| <= K_{Re nu}(v) <= 2 e^{-v} e^{(Re nu)^2/(2v)}
    sqrt(pi/(2v)) so that the discarded tail is < 1e-(dps+8) absolute for y >= 0.5."""
    x = mpf(x); y = mpf(y); s = mpc(s)
    if N is None:
        N = int(math.ceil((mp.dps + 15) * math.log(10) / (2 * math.pi * float(y)))) + 5
    tot = 2 * xi_riemann(2 * s) * mp.power(y, s) + 2 * xi_riemann(2 * s - 1) * mp.power(y, 1 - s)
    pref = 8 * mp.sqrt(y)
    nu = s - mpf(1) / 2
    for n in range(1, N + 1):
        term = (mp.power(n, nu) * _sigma_div(n, 1 - 2 * s)
                * mp.besselk(nu, 2 * mp.pi * n * y) * mp.cos(2 * mp.pi * n * x))
        tot += pref * term
    return tot


# ----------------------------------------------------------------------------
# Dirichlet beta (chi_{-4}) helpers for the z = i oracles
# ----------------------------------------------------------------------------

def beta_dirichlet(s):
    """beta(s) = L(s, chi_{-4}) = 4^{-s} (zeta(s,1/4) - zeta(s,3/4)) (Hurwitz)."""
    s = mpc(s)
    return mp.power(4, -s) * (mp.zeta(s, mpf(1) / 4) - mp.zeta(s, mpf(3) / 4))


def beta_dirichlet_nsum(s):
    """Independent series evaluation beta(s) = sum (-1)^k (2k+1)^{-s} (Richardson+Shanks)."""
    s = mpc(s)
    return mp.nsum(lambda k: (-1) ** int(k) * mp.power(2 * k + 1, -s), [0, mp.inf], method='r+s')


def completed_beta_line(t):
    """Re of Lambda_beta(1/2+it), Lambda_beta(s) = (pi/4)^{-(s+1)/2} Gamma((s+1)/2) beta(s);
    real on the line (odd primitive character mod 4, root number 1)."""
    s = mpc(mpf(1) / 2, t)
    v = mp.power(mp.pi / 4, -(s + 1) / 2) * mp.gamma((s + 1) / 2) * beta_dirichlet(s)
    return mp.re(v)


# ----------------------------------------------------------------------------
# O1: independent direct lattice sum at z = i (pure python sieve, radius R)
# ----------------------------------------------------------------------------

def r2_sieve(N):
    """r[n] = #{(m,k): m^2+k^2 = n} = 4 sum_{d|n} chi_{-4}(d) for 1 <= n <= N (list of ints)."""
    r = [0] * (N + 1)
    for d in range(1, N + 1, 4):        # chi_{-4}(d) = +1
        for k in range(d, N + 1, d):
            r[k] += 4
    for d in range(3, N + 1, 4):        # chi_{-4}(d) = -1
        for k in range(d, N + 1, d):
            r[k] -= 4
    return r


def direct_Z_i(s, R=2000, head=50000, navg=64, nstep=1000):
    """Direct lattice sum Z_i(s) = sum_{(m,n)!=0} (m^2+n^2)^{-s} truncated at radius R
    (i.e. n <= N = R^2), with tail estimate.  Returns (value, spread) where spread is the
    max-min over the navg tail-corrected truncations (empirical residual indicator).

    Method: r2 sieve to N; head n <= `head` summed in mpmath (dps 35); the rest in float
    with math.fsum (exactly-rounded double sums; term magnitudes there total < 1e-4 so
    double rounding contributes < 1e-19 absolute); tail estimate with the EXACT counting
    function A(N) = sum_{n<=N} r2(n):
        tail_est(N) = s * pi * N^{1-s}/(s-1) - A(N) * N^{-s},
    whose residual s int_N^inf P(u) u^{-s-1} du (P = circle-problem error) is suppressed
    by averaging over navg truncation points N_j = N - j*nstep."""
    import cmath
    N = R * R
    r = r2_sieve(N)
    sc = complex(mpc(s))
    with mp.workdps(35):
        smp = mpc(s)
        headsum = mpc(0)
        for n in range(1, head + 1):
            if r[n]:
                headsum += r[n] * mp.power(n, -smp)
        # float mid part, up to smallest averaging point
        N_lo = N - (navg - 1) * nstep
        re_terms = []
        im_terms = []
        for n in range(head + 1, N_lo + 1):
            if r[n]:
                v = r[n] * cmath.exp(-sc * math.log(n))
                re_terms.append(v.real)
                im_terms.append(v.imag)
        mid = mpc(math.fsum(re_terms), math.fsum(im_terms))
        # cumulative A up to N_lo
        A = 0
        for n in range(1, N_lo + 1):
            A += r[n]
        base = headsum + mid   # sum over n <= N_lo
        # walk the averaging points upward, keeping exact partial sums in mpmath
        vals = []
        S = base
        Acur = A
        ncur = N_lo
        for j in range(navg):
            Nj = N_lo + j * nstep
            while ncur < Nj:
                ncur += 1
                if r[ncur]:
                    S += r[ncur] * mp.power(ncur, -smp)
                    Acur += r[ncur]
            tail = smp * mp.pi * mp.power(Nj, 1 - smp) / (smp - 1) - Acur * mp.power(Nj, -smp)
            vals.append(S + tail)
        avg = sum(vals) / len(vals)
        spread = max(abs(v - avg) for v in vals) * 2
    return avg, spread


# ----------------------------------------------------------------------------
# E5: coprime (gcd=1) direct sum for the Eisenstein identity check
# ----------------------------------------------------------------------------

def eisenstein_E1_direct(x, y, s, X):
    """E_1(z,s) = (1/2) sum_{gcd(m,n)=1} Q_z(m,n)^{-s} by direct enumeration over Q <= X,
    plus the stated tail bound (returned, not added):  |tail| <= (12/pi) * X^{1-sigma}/(sigma-1)
    using coprime density 6/pi^2 * (pi dQ) points per unit Q and a factor-2 margin.
    Use only with Re s >= 5 so the bound is tiny."""
    x = mpf(x); y = mpf(y); s = mpc(s)
    sigma = float(mp.re(s))
    assert sigma >= 5
    pts = lattice_points(x, y, X)
    groups = {}
    for (m, n, Q) in pts:
        if math.gcd(m, n) == 1:
            k = mp.nstr(Q, 40)
            if k in groups:
                groups[k][1] += 1
            else:
                groups[k] = [Q, 1]
    tot = mpc(0)
    for Q, mult in groups.values():
        tot += mult * mp.power(Q, -s)
    with mp.workdps(20):
        tailbound = float(12 / mp.pi * mp.power(mpf(X), 1 - sigma) / (sigma - 1))
    return tot / 2, tailbound


# ----------------------------------------------------------------------------
# 1-D root machinery on the critical line (float t, mpmath evaluations inside)
# ----------------------------------------------------------------------------

def illinois(f, a, b, fa=None, fb=None, reltol=1e-13, maxit=100):
    """Bracketed Illinois (modified regula falsi) on floats; f returns float.
    Requires sign change on [a,b]; returns root t with |b-a| <= reltol*max(1,|t|)."""
    if fa is None:
        fa = f(a)
    if fb is None:
        fb = f(b)
    if fa == 0.0:
        return a
    if fb == 0.0:
        return b
    assert fa * fb < 0, f"illinois: no sign change on [{a},{b}]"
    side = 0
    for _ in range(maxit):
        c = (a * fb - b * fa) / (fb - fa)
        if not (min(a, b) < c < max(a, b)):
            c = 0.5 * (a + b)
        fc = f(c)
        if fc == 0.0:
            return c
        if fc * fa < 0:
            b, fb = c, fc
            if side == -1:
                fa *= 0.5
            side = -1
        else:
            a, fa = c, fc
            if side == 1:
                fb *= 0.5
            side = 1
        if abs(b - a) <= reltol * max(1.0, abs(a)):
            break
    return 0.5 * (a + b)


def sign_change_cells(ts, fs):
    """Indices k with fs[k]*fs[k+1] < 0 (or an exact zero)."""
    out = []
    for k in range(len(ts) - 1):
        if fs[k] == 0.0 or fs[k] * fs[k + 1] < 0:
            out.append(k)
    return out


def dip_cells(ts, fs):
    """Grid indices k (interior) that are local minima of |f| WITHOUT a sign change in
    the adjacent cells and small relative to neighbours -- candidates for a close pair
    or an off-line pair sitting near the line."""
    out = []
    n = len(ts)
    for k in range(1, n - 1):
        if fs[k] * fs[k - 1] < 0 or fs[k] * fs[k + 1] < 0:
            continue
        a0, a1, a2 = abs(fs[k - 1]), abs(fs[k]), abs(fs[k + 1])
        if a1 < a0 and a1 < a2 and a1 < 0.5 * max(a0, a2):
            out.append(k)
    return out


# ----------------------------------------------------------------------------
# winding-number utilities (batch-evaluated boundary; caller supplies values)
# ----------------------------------------------------------------------------

def arg_increments(vals):
    """Principal-branch phase increments along a value cycle (closed: last->first included).
    Returns (total, max_abs_increment)."""
    n = len(vals)
    tot = 0.0
    mx = 0.0
    for k in range(n):
        a = vals[k]
        b = vals[(k + 1) % n]
        d = math.atan2((b / a).imag, (b / a).real) if a != 0 else float('nan')
        tot += d
        mx = max(mx, abs(d))
    return tot, mx


# ----------------------------------------------------------------------------
# selftest: enumerator + theta transform + engine cross-checks
# ----------------------------------------------------------------------------

def selftest(verbose=True):
    """Build-time assertions.  Returns a dict of measured diagnostics."""
    diag = {}
    with mp.workdps(45):
        # enumerator vs brute force at z=i, X=10.  The brute-force double loop is the
        # designated test oracle; it gives 36 = sum_{n<=10} r2(n) with
        # r2(1..10) = 4,4,0,4,8,0,0,4,4,8.  (r2(10) = 8 since 10 = 1+9 has the eight
        # representations (+-1,+-3),(+-3,+-1); the value 4 sometimes quoted is a typo.)
        n_enum = len(lattice_points(1e-0 * 0, 1.0, 10))
        n_brute = brute_count(0, 1.0, 10, box=8)
        assert n_enum == n_brute == 36, (n_enum, n_brute)
        # r2 divisor-sieve cross-check of the same count
        r = r2_sieve(10)
        assert sum(r[1:]) == 36 and r[1:11] == [4, 4, 0, 4, 8, 0, 0, 4, 4, 8]
        # generic z enumerator vs brute force
        xg, yg = 0.13, 1.07
        n_enum = len(lattice_points(xg, yg, 15))
        n_brute = brute_count(xg, yg, 15, box=12)
        assert n_enum == n_brute, (n_enum, n_brute)
        diag['enumerator_ok'] = True
        # theta transformation at z=i and generic z, 30 digits
        d1 = check_theta_transform(0.0, 1.0)
        d2 = check_theta_transform(xg, yg)
        diag['theta_transform_maxdiff'] = float(max(d1, d2))
    # engine cross-check: incomplete-gamma vs Fourier/Bessel at 3 points, 28+ digits
    with mp.workdps(40):
        pts = [(0.0, 1.0, mpc('0.5', '9.3')), (0.13, 1.07, mpc('0.62', '5.1')),
               (0.5, math.sqrt(3) / 2, mpc('0.5', '11.7'))]
        worst = mpf(0)
        for (x, y, s) in pts:
            a = lam(x, y, s)
            b = lam_fourier(x, y, s)
            rel = abs(a - b) / max(abs(a), mpf('1e-30'))
            worst = max(worst, rel)
        assert worst < mpf('1e-28'), mp.nstr(worst, 5)
        diag['engine_crosscheck_rel'] = float(worst)
        # x-reflection symmetry Lambda(-x+iy) = Lambda(x+iy) (exact lattice symmetry)
        a = lam(0.05, 1.05, mpc('0.55', '7.7'))
        b = lam(-0.05, 1.05, mpc('0.55', '7.7'))
        assert abs(a - b) < mpf('1e-30')
        diag['x_reflection_ok'] = True
    if verbose:
        print("selftest:", diag)
    return diag


if __name__ == '__main__':
    mp.dps = DPS_DEFAULT
    selftest()
