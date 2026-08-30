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


def direct_Z_i(s, R=2000, head=50000, navg=257, nstep=1000):
    """Direct lattice sum Z_i(s) = sum_{(m,n)!=0} (m^2+n^2)^{-s} truncated at radius R
    (i.e. n <= N = R^2), with tail estimate.  Returns (value, spread) where spread is the
    max-min over the navg tail-corrected truncations (empirical residual indicator).

    Method: r2 sieve to N; head n <= `head` summed in mpmath (dps 35); the rest in float
    with math.fsum (exactly-rounded double sums; term magnitudes there total < 1e-4 so
    double rounding contributes < 1e-19 absolute); tail estimate with the EXACT counting
    function A(N) = sum_{n<=N} r2(n):
        tail_est(N) = s * pi * N^{1-s}/(s-1) - (A(N) + 1) * N^{-s}.
    (The +1: A(u) = pi u + E(u) - 1 with E the Gauss-circle error INCLUDING the origin;
    E has mean ~0 but the excluded origin shifts P = E - 1 to mean -1, contributing a
    systematic -N^{-s} to the Abel-summation residual, which the +1 removes.)
    The remaining residual s int_N^inf E(u) u^{-s-1} du (oscillatory
    with local frequency ~ pi sqrt(n/N)) is suppressed by a TRIANGULAR (Cesaro) weighted
    average over navg truncation points N_j = N - j*nstep: a triangular window of span S
    damps a frequency-omega oscillation like (2/(omega S/2))^2, quadratically better than
    a flat average."""
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
            tail = (smp * mp.pi * mp.power(Nj, 1 - smp) / (smp - 1)
                    - (Acur + 1) * mp.power(Nj, -smp))
            vals.append(S + tail)
        # triangular (Cesaro) weights
        c = (navg - 1) / 2
        ws = [1 - abs(j - c) / (c + 1) for j in range(navg)]
        wsum = math.fsum(ws)
        avg = sum(w * v for (w, v) in zip(ws, vals)) / wsum
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
# MACHINERY: on_line_scan / box_count / off_line_detector / departure_finder
# All accept pluggable batch evaluators (serial defaults below; the driver plugs
# in a multiprocessing pool).  Batch evaluators:
#   line_batch(x, y, ts)          -> [float F_z(t)]
#   lam_batch(x, y, [(sig,t)..])  -> [complex Lambda_z(sig+it)]
#   refine_batch(x, y, [(a,b,fa,fb)..]) -> [float root]
# ----------------------------------------------------------------------------

def serial_line_batch(x, y, ts, X=None):
    return [float(lam_line(x, y, t, X)) for t in ts]


def serial_lam_batch(x, y, pts, X=None):
    return [complex(lam(x, y, mpc(sg, t), X)) for (sg, t) in pts]


def serial_refine_batch(x, y, ivs, X=None):
    out = []
    for (a, b, fa, fb) in ivs:
        out.append(illinois(lambda t: float(lam_line(x, y, t, X)), a, b, fa, fb))
    return out


def tgrid(ta, tb, dt):
    n = max(1, int(round((tb - ta) / dt)))
    return [ta + (tb - ta) * j / n for j in range(n + 1)]


def hunt_sign_changes(x, y, ta, tb, dt, depth=2, line_batch=None):
    """Grid scan for sign changes of F_z(t), recursively rescanning dip cells (local
    minima of |F| without a sign change) at dt/10 down to `depth` extra levels.
    Returns (intervals, unresolved_dips): intervals = [(a,b,fa,fb)] each containing a
    sign change; unresolved_dips = [(t, F)] dips still unresolved at the finest level
    (candidate near-line pair or off-line pair; the box count disambiguates)."""
    lb = line_batch or serial_line_batch
    ts = tgrid(ta, tb, dt)
    fs = lb(x, y, ts)
    ints = []
    dips = []
    for k in sign_change_cells(ts, fs):
        ints.append((ts[k], ts[k + 1], fs[k], fs[k + 1]))
    for k in dip_cells(ts, fs):
        if depth > 0:
            si, sd = hunt_sign_changes(x, y, ts[k - 1], ts[k + 1], dt / 10, depth - 1, lb)
            ints += si
            dips += sd
        else:
            dips.append((ts[k], fs[k]))
    ints.sort()
    dedup = []
    for iv in ints:
        if dedup and abs(iv[0] - dedup[-1][0]) < 1e-12:
            continue
        dedup.append(iv)
    return dedup, dips


def on_line_scan(x, y, t0, t1, dt, depth=2, refine=True, line_batch=None, refine_batch=None):
    """Sample the REAL function F_z(t) = Lambda_z(1/2+it) on [t0,t1] (reality verified in
    oracles O3/O4), record sign changes, refine each by bracketed iteration to 12 digits.
    Returns {'zeros': [t..], 'n', 'unresolved_dips', 'dt', 'depth'}."""
    ints, dips = hunt_sign_changes(x, y, t0, t1, dt, depth, line_batch)
    if refine and ints:
        zeros = (refine_batch or serial_refine_batch)(x, y, ints)
    else:
        zeros = [0.5 * (a + b) for (a, b, _, _) in ints]
    zeros = sorted(zeros)
    return {'zeros': zeros, 'n': len(zeros),
            'unresolved_dips': [(t, f) for (t, f) in dips], 'dt': dt, 'depth': depth}


class _NudgeNeeded(Exception):
    pass


def box_count(x, y, t0, t1, delta=0.2, init_step_t=0.2, n_sigma=9,
              lam_batch=None, max_rounds=64, nudge_max=3):
    """Argument-principle winding number of Lambda_z around the boundary of
    [1/2-delta, 1/2+delta] x [t0, t1] (counterclockwise), t0 > 0 so the poles s=0,1 are
    outside.  Exploits the exact symmetry Lambda(1/2-d+it) = conj(Lambda(1/2+d+it))
    (FE + real coefficients) so only the right edge is evaluated.  Adaptive sampling:
    any consecutive phase jump >= pi/2 triggers subdivision.  The winding/2pi must be a
    near-integer within 1e-6 (asserted).  If a boundary point sits (numerically) on a
    zero, the box is re-run with delta nudged by +0.0137 (up to nudge_max times).
    Returns (count, info)."""
    lb = lam_batch or serial_lam_batch
    last_err = None
    for attempt in range(nudge_max + 1):
        d = delta + 0.0137 * attempt
        try:
            cnt, info = _box_once(x, y, t0, t1, d, init_step_t, n_sigma, lb, max_rounds)
            info['delta_used'] = d
            info['nudges'] = attempt
            return cnt, info
        except _NudgeNeeded as e:
            last_err = e
            continue
    raise RuntimeError(f"box_count: failed after {nudge_max} nudges: {last_err}")


def _box_once(x, y, t0, t1, delta, init_step_t, n_sigma, lb, max_rounds):
    s0 = 0.5 - delta
    s1 = 0.5 + delta
    tg = tgrid(t0, t1, init_step_t)
    sg = [s0 + (s1 - s0) * j / (n_sigma - 1) for j in range(n_sigma)]
    R = {}   # right edge  sigma = s1, keyed by t
    B = {}   # bottom edge t = t0, keyed by sigma
    T = {}   # top edge    t = t1, keyed by sigma
    n_evals = 0
    for _ in range(max_rounds):
        missing = []
        for t in tg:
            if t not in R:
                missing.append((s1, t, 'R', t))
        for sig in sg:
            if sig not in B:
                missing.append((sig, t0, 'B', sig))
            if sig not in T:
                missing.append((sig, t1, 'T', sig))
        if missing:
            vals = lb(x, y, [(p[0], p[1]) for p in missing])
            n_evals += len(missing)
            for (p, v) in zip(missing, vals):
                if v == 0:
                    raise _NudgeNeeded("exact zero on contour")
                {'R': R, 'B': B, 'T': T}[p[2]][p[3]] = v
        # assemble counterclockwise cycle; left edge derived from right by conjugation
        nodes = ([('b', s) for s in sg] +
                 [('r', t) for t in tg[1:]] +
                 [('t', s) for s in reversed(sg[:-1])] +
                 [('l', t) for t in reversed(tg[:-1])])

        def val(nd):
            tag, c = nd
            if tag == 'b':
                return B[c]
            if tag == 't':
                return T[c]
            if tag == 'r':
                return R[c]
            v = R[c]
            return complex(v.real, -v.imag)

        def point(nd):
            tag, c = nd
            if tag == 'b':
                return (c, t0)
            if tag == 't':
                return (c, t1)
            if tag == 'r':
                return (s1, c)
            return (s0, c)

        total = 0.0
        bad = []
        nn = len(nodes)
        for k in range(nn):
            a = val(nodes[k])
            b = val(nodes[(k + 1) % nn])
            q = b / a
            dphi = math.atan2(q.imag, q.real)
            total += dphi
            if abs(dphi) >= math.pi / 2:
                bad.append((nodes[k], nodes[(k + 1) % nn]))
        if not bad:
            w = total / (2 * math.pi)
            cnt = round(w)
            if abs(w - cnt) > 1e-6:
                raise _NudgeNeeded(f"winding not near-integer: {w}")
            return cnt, {'n_evals': n_evals, 'winding': w,
                         'n_tgrid': len(tg), 'n_sgrid': len(sg)}
        newt = set()
        news = set()
        for (na, nb) in bad:
            (sa, ta) = point(na)
            (sb, tb) = point(nb)
            if sa == sb:
                if abs(tb - ta) < 1e-8:
                    raise _NudgeNeeded("zero pinned on vertical edge")
                newt.add(0.5 * (ta + tb))
            elif ta == tb:
                if abs(sb - sa) < 1e-8:
                    raise _NudgeNeeded("zero pinned on horizontal edge")
                news.add(0.5 * (sa + sb))
            # else: wrap duplicate segment, zero length -- never bad
        tg = sorted(set(tg) | newt)
        sg = sorted(set(sg) | news)
    raise _NudgeNeeded("box refinement did not converge")


def off_line_detector(x, y, t0, t1, dt=0.05, depth=2, delta=0.2, refine=False,
                      line_batch=None, lam_batch=None, refine_batch=None):
    """Compare the argument-principle count in [1/2-delta,1/2+delta] x [t0,t1] with the
    number of on-line sign changes.  disc = n_box - n_line; a discrepancy of 2 signals a
    symmetric off-line pair (numerically, to the stated precision)."""
    scan = on_line_scan(x, y, t0, t1, dt, depth=depth, refine=refine,
                        line_batch=line_batch, refine_batch=refine_batch)
    nbox, info = box_count(x, y, t0, t1, delta=delta, lam_batch=lam_batch)
    disc = nbox - scan['n']
    anomaly = None
    if disc < 0 or disc % 2 != 0:
        anomaly = f"nbox={nbox} < n_line={scan['n']} or odd disc -- investigate"
    return {'n_line': scan['n'], 'n_box': nbox, 'disc': disc, 'scan': scan,
            'box_info': info, 'anomaly': anomaly}


def muller_zero(x, y, s0, X=None, maxsteps=60):
    """Complex zero of Lambda_z near s0 via Muller iteration; returns mpc or None.
    Accepts (sigma, t) tuple or complex seed."""
    f = lambda s: lam(x, y, s, X)
    seed = mpc(s0[0], s0[1]) if isinstance(s0, tuple) else mpc(s0)
    try:
        r = mp.findroot(f, seed, solver='muller', maxsteps=maxsteps, tol=mpf('1e-40'))
    except Exception:
        return None
    # residual sanity: compare with a nearby non-zero value
    try:
        ref = abs(lam(x, y, r + mpf('0.07'), X))
        if not (abs(f(r)) < mpf('1e-15') * max(ref, mpf('1e-40'))):
            return None
    except Exception:
        return None
    return r


def find_offline_pair_near(x, y, t_center, delta=0.2, t0=None, t1=None, X=None):
    """Locate the right-half member (sigma > 1/2) of an off-line pair near t_center by
    Muller iteration from a deterministic ladder of seeds.  Returns (sigma, t) floats or None."""
    seeds = [(0.54, t_center), (0.58, t_center), (0.63, t_center),
             (0.56, t_center + 0.15), (0.56, t_center - 0.15),
             (0.52, t_center), (0.67, t_center)]
    for sd in seeds:
        r = muller_zero(x, y, sd, X)
        if r is None:
            continue
        sig = float(mp.re(r))
        tt = float(mp.im(r))
        if tt < 0:
            tt = -tt   # conjugate zero; reflect
        if not (0.5 + 1e-9 < sig < 0.5 + delta):
            continue
        if t0 is not None and not (t0 - 0.2 <= tt <= t1 + 0.2):
            continue
        return (sig, tt)
    return None


def count_window(x, y, wa, wb, dt=0.02, depth=2, line_batch=None):
    """Number of on-line sign changes in [wa,wb] at fine resolution (classifier for
    merge bisection: a merging pair goes 2 -> 0)."""
    ints, _ = hunt_sign_changes(x, y, wa, wb, dt, depth, line_batch)
    return len(ints)


def dip_location(x, y, wa, wb, dt=0.02, levels=3, line_batch=None):
    """Location and value of the minimum of |F| on [wa,wb] via `levels` nested rescans
    (resolution dt/10^levels).  Returns (t_min, F(t_min))."""
    lb = line_batch or serial_line_batch
    a, b, d = wa, wb, dt
    best_t, best_f = None, None
    for _ in range(levels + 1):
        ts = tgrid(a, b, d)
        fs = lb(x, y, ts)
        k = min(range(len(ts)), key=lambda j: abs(fs[j]))
        best_t, best_f = ts[k], fs[k]
        a = ts[max(0, k - 1)]
        b = ts[min(len(ts) - 1, k + 1)]
        d = d / 10
    return best_t, best_f


def departure_finder(pathfun, taus, t0, t1, dt=0.05, depth=2, delta=0.2, tau_tol=1e-6,
                     line_batch=None, lam_batch=None, refine_batch=None, log=None):
    """Along z(tau) = pathfun(tau) (returns (x, y)), at each tau: refined on-line zeros +
    box count in [t0,t1].  Departure event: between consecutive grid taus the box-line
    discrepancy jumps by +2 (a pair leaves the line: two on-line zeros merge, the on-line
    count drops by 2, the box count stays).  tau* refined by bisection (to tau_tol) with
    the local classifier count_window (2 sign changes -> 0).  A disc jump of -2 is
    recorded as a re-entry event and refined the same way.  Returns (records, events)."""
    def _log(msg):
        if log:
            log(msg)

    records = []
    for tau in taus:
        x, y = pathfun(tau)
        det = off_line_detector(x, y, t0, t1, dt=dt, depth=depth, delta=delta, refine=True,
                                line_batch=line_batch, lam_batch=lam_batch,
                                refine_batch=refine_batch)
        records.append({'tau': tau, 'x': x, 'y': y, 'n_line': det['n_line'],
                        'n_box': det['n_box'], 'disc': det['disc'],
                        'zeros': det['scan']['zeros'],
                        'unresolved_dips': det['scan']['unresolved_dips'],
                        'anomaly': det['anomaly']})
        _log(f"  tau={tau:.3f}: n_line={det['n_line']} n_box={det['n_box']} disc={det['disc']}")

    events = []
    for j in range(len(records) - 1):
        ra, rb = records[j], records[j + 1]
        if ra['disc'] is None or rb['disc'] is None:
            continue
        jump = rb['disc'] - ra['disc']
        if jump == 0:
            continue
        direction = 'departure' if jump > 0 else 'reentry'
        n_units = abs(jump) // 2
        # identify candidate merge windows from the refined zero lists
        za, zb = (ra['zeros'], rb['zeros']) if jump > 0 else (rb['zeros'], ra['zeros'])
        cands = _merge_candidates(za, zb, t0, t1)
        _log(f"  event {direction} between tau={ra['tau']:.3f} and {rb['tau']:.3f}: "
             f"jump={jump}, candidates={[(round(u,3),round(v,3)) for (u,v,_,_) in cands]}")
        used = 0
        for (u, v, wa, wb) in cands:
            if used >= n_units:
                break
            ev = _refine_event(pathfun, ra['tau'], rb['tau'], u, v, wa, wb,
                               direction, tau_tol, line_batch, lam_batch, _log)
            if ev is not None:
                ev['path_tau_lo'] = ra['tau']
                ev['path_tau_hi'] = rb['tau']
                events.append(ev)
                used += 1
        if used < n_units:
            events.append({'type': direction, 'tau_star': None,
                           'tau_bracket': [ra['tau'], rb['tau']],
                           'note': f"{n_units - used} unit(s) of |disc| jump {jump} not resolved "
                                   f"to a specific merging pair (possible window-boundary "
                                   f"entry/exit near t={t1}); see records."})
    return records, events


def _merge_candidates(za, zb, t0, t1):
    """Adjacent zero pairs (u,v) in za with no counterpart of BOTH u and v surviving in zb.
    Returns [(u, v, window_a, window_b)] sorted by gap (tightest pair first)."""
    out = []
    for k in range(len(za) - 1):
        u, v = za[k], za[k + 1]
        gap = v - u
        # neighbours for window clipping
        lo = za[k - 1] if k - 1 >= 0 else t0
        hi = za[k + 2] if k + 2 < len(za) else t1
        wa = max(t0, 0.5 * (lo + u) if k - 1 >= 0 else max(t0, u - 0.5))
        wb = min(t1, 0.5 * (v + hi) if k + 2 < len(za) else min(t1, v + 0.5))
        survivors = [w for w in zb if wa <= w <= wb]
        if len(survivors) == 0:
            out.append((u, v, wa, wb, gap))
    out.sort(key=lambda c: c[4])
    return [(u, v, wa, wb) for (u, v, wa, wb, _) in out]


def _refine_event(pathfun, tau_lo, tau_hi, u, v, wa, wb, direction, tau_tol,
                  line_batch, lam_batch, _log):
    """Bisect tau between on-line (2 sign changes in [wa,wb]) and merged (0).
    For a re-entry event the roles of lo/hi are swapped internally (the pair is ON the
    line at tau_hi).  Returns event dict or None if the classifier does not confirm."""
    on_at_lo = (direction == 'departure')

    def n_at(tau):
        x, y = pathfun(tau)
        return count_window(x, y, wa, wb, dt=0.02, depth=2, line_batch=line_batch)

    nlo = n_at(tau_lo)
    nhi = n_at(tau_hi)
    want_lo, want_hi = (2, 0) if on_at_lo else (0, 2)
    if not (nlo == want_lo and nhi == want_hi):
        _log(f"    classifier rejects window [{wa:.3f},{wb:.3f}]: n(tau_lo)={nlo}, n(tau_hi)={nhi}")
        return None
    a, b = tau_lo, tau_hi
    while b - a > tau_tol:
        m = 0.5 * (a + b)
        nm = n_at(m)
        if (nm >= 2) == on_at_lo:
            a = m
        else:
            b = m
    tau_star = 0.5 * (a + b)
    # collision height: dip location on the merged side
    tau_merged = b if on_at_lo else a
    xm, ym = pathfun(tau_merged)
    t_star, f_star = dip_location(xm, ym, wa, wb, dt=0.02, levels=3, line_batch=line_batch)
    # off-line pair location at the merged-side path GRID endpoint
    tau_off = tau_hi if on_at_lo else tau_lo
    xo, yo = pathfun(tau_off)
    pair = find_offline_pair_near(xo, yo, t_star, t0=wa, t1=wb)
    return {'type': direction, 'tau_star': tau_star, 'tau_star_uncertainty': 0.5 * (b - a),
            't_colliding_pair': [u, v], 't_star': t_star, 'F_at_t_star': f_star,
            'z_star': list(pathfun(tau_star)),
            'offline_pair_at_tau': tau_off,
            'offline_pair_sigma_t': list(pair) if pair else None,
            'window': [wa, wb]}


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
