"""
Core machinery for the CvS "pole detector" resolution study.

Setup
-----
nodes            lam_j = j,  j = -N..N,  dim n = 2N+1
source           psi(x) = sum_k a_k [ 1/(mu_k - x) + 1/(-mu_k - x) ],  a_k>0, mu_k>0
Loewner matrix   Q_{ij} = (psi(lam_i)-psi(lam_j))/(lam_i-lam_j),  Q_{ii}=psi'(lam_i)
L-16004          Q = sum_k a_k [ ell(mu_k) ell(mu_k)^T + ell(-mu_k) ell(-mu_k)^T ],
                 ell(m)_j = 1/(lam_j - m)                       (EXACT identity)
CvS pencil       t* = 1/(eta^T Q^{-1} eta),  ker(Q - t* eta eta^T) = R xi, xi = Q^{-1} eta
normalisation    eta^T xi = 1
polynomial       P_xi(s) = sum_j xi_j prod_{k!=j}(lam_k - s) = Omega(s) <xi, ell(s)>
                 Omega(s) = prod_k (lam_k - s)                  (EXACT identity, one line)
"""
import mpmath as mp
from mpmath import mpf


# ---------------------------------------------------------------- precision
def set_dps(N, extra=0):
    mp.mp.dps = 40 + 5 * N + extra
    return mp.mp.dps


# ---------------------------------------------------------------- matrices
def nodes(N):
    return [mpf(j) for j in range(-N, N + 1)]


def build_Q_rank1(N, poles, weights):
    """Q via the L-16004 rank-one closed form (numerically clean)."""
    lam = nodes(N)
    n = 2 * N + 1
    Q = mp.zeros(n, n)
    for a, mu in zip(weights, poles):
        a = mpf(a)
        for m in (mpf(mu), -mpf(mu)):
            if any(abs(lam[i] - m) < mpf(10) ** (-20) for i in range(n)):
                raise ValueError(f"pole {m} coincides with a node")
            v = [1 / (lam[i] - m) for i in range(n)]
            for i in range(n):
                avi = a * v[i]
                for j in range(i, n):
                    Q[i, j] += avi * v[j]
    for i in range(n):
        for j in range(i):
            Q[i, j] = Q[j, i]
    return Q


def build_Q_divdiff(N, poles, weights):
    """Q from the literal divided-difference definition (independent check)."""
    lam = nodes(N)
    n = 2 * N + 1

    def psi(x):
        s = mpf(0)
        for a, mu in zip(weights, poles):
            s += mpf(a) * (1 / (mpf(mu) - x) + 1 / (-mpf(mu) - x))
        return s

    def dpsi(x):
        s = mpf(0)
        for a, mu in zip(weights, poles):
            s += mpf(a) * (1 / (mpf(mu) - x) ** 2 + 1 / (-mpf(mu) - x) ** 2)
        return s

    b = [psi(l) for l in lam]
    Q = mp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            Q[i, j] = dpsi(lam[i]) if i == j else (b[i] - b[j]) / (lam[i] - lam[j])
    return Q


# ---------------------------------------------------------------- target xi
def target_xi(Q, N, symmetrise=True):
    """xi = Q^{-1} eta normalised so eta^T xi = 1.  Returns (xi, tstar, evenness)."""
    n = 2 * N + 1
    eta = mp.matrix([mpf(1)] * n)
    y = mp.lu_solve(Q, eta)
    s = sum(y[i] for i in range(n))
    tstar = 1 / s
    xi = [y[i] / s for i in range(n)]
    even_res = max(abs(xi[i] - xi[n - 1 - i]) for i in range(n)) / max(abs(x) for x in xi)
    if symmetrise:
        xi = [(xi[i] + xi[n - 1 - i]) / 2 for i in range(n)]
    return xi, tstar, even_res


# ---------------------------------------------------------------- polynomial
def _omega_j_int(N):
    """Integer coefficient lists (increasing powers of s) of Omega_j(s)=prod_{k!=j}(lam_k-s)."""
    lam = list(range(-N, N + 1))
    out = []
    for j in range(len(lam)):
        c = [1]
        for k in range(len(lam)):
            if k == j:
                continue
            kk = lam[k]
            new = [0] * (len(c) + 1)
            for p, cp in enumerate(c):
                new[p] += kk * cp
                new[p + 1] -= cp
            c = new
        out.append(c)
    return out


_OMEGA_CACHE = {}


def P_coeffs(N, xi):
    """Coefficients of P_xi in increasing powers of s (mpf)."""
    if N not in _OMEGA_CACHE:
        _OMEGA_CACHE[N] = _omega_j_int(N)
    om = _OMEGA_CACHE[N]
    deg = 2 * N
    c = [mpf(0)] * (deg + 1)
    for j, xj in enumerate(xi):
        oj = om[j]
        for p in range(deg + 1):
            if oj[p]:
                c[p] += xj * oj[p]
    return c


def even_reduce(coeffs):
    """P even => P(s)=R(u), u=s^2.  Returns (R coeffs increasing in u, odd-part relative size)."""
    scale = max(abs(x) for x in coeffs)
    odd = max(abs(coeffs[p]) for p in range(1, len(coeffs), 2)) / scale if len(coeffs) > 1 else 0
    R = [coeffs[p] for p in range(0, len(coeffs), 2)]
    return R, odd


def poly_roots_increasing(coeffs_inc, extraprec=4000, maxsteps=200):
    """mpmath.polyroots wants decreasing powers."""
    dec = list(reversed(coeffs_inc))
    return mp.polyroots(dec, maxsteps=maxsteps, extraprec=extraprec)


def polyval_inc(coeffs_inc, x):
    r = mpf(0)
    for c in reversed(coeffs_inc):
        r = r * x + c
    return r


def rel_residual(coeffs_inc, x):
    """|P(x)| / sum |c_p| |x|^p  -- relative residual of a claimed root."""
    num = abs(polyval_inc(coeffs_inc, x))
    den = mpf(0)
    ax = abs(x)
    for p, c in enumerate(coeffs_inc):
        den += abs(c) * ax ** p
    return num / den if den != 0 else num


# ---------------------------------------------------------------- driver
def detect(N, poles, weights, extraprec=4000, dps_extra=0, check_divdiff=False):
    """Run the whole apparatus.  Returns a dict."""
    set_dps(N, dps_extra)
    Q = build_Q_rank1(N, poles, weights)
    info = {}
    if check_divdiff:
        Q2 = build_Q_divdiff(N, poles, weights)
        n = 2 * N + 1
        num = max(abs(Q[i, j] - Q2[i, j]) for i in range(n) for j in range(n))
        den = max(abs(Q[i, j]) for i in range(n) for j in range(n))
        info['loewner_check'] = num / den
    xi, tstar, even_res = target_xi(Q, N)
    c = P_coeffs(N, xi)
    R, oddrel = even_reduce(c)
    ur = poly_roots_increasing(R, extraprec=extraprec)
    # positive roots s = sqrt(u)
    roots = []
    maximag = mpf(0)
    for u in ur:
        maximag = max(maximag, abs(mp.im(u)) / (abs(u) + mpf(1)))
        s = mp.sqrt(u)
        roots.append(s)
    roots_real = sorted([mp.re(s) for s in roots if abs(mp.im(s)) < mpf(10) ** (-mp.mp.dps // 3)])
    info.update(dict(N=N, dps=mp.mp.dps, tstar=tstar, even_res=even_res, odd_rel=oddrel,
                     u_roots=ur, roots=sorted(roots, key=lambda z: mp.re(z)),
                     pos_roots=roots_real, max_imag_u=maximag,
                     resid=[rel_residual(R, u) for u in ur],
                     P_coeffs=c, R_coeffs=R))
    return info


def match(pos_roots, poles):
    """For each recovered root, nearest true pole + relative error."""
    out = []
    for r in pos_roots:
        best = min(poles, key=lambda m: abs(mpf(m) - r))
        out.append((r, mpf(best), abs(mpf(best) - r) / mpf(best)))
    return out


def match_from_poles(pos_roots, poles):
    """For each true pole, nearest recovered root + relative error (may reuse roots)."""
    out = []
    for m in poles:
        if not pos_roots:
            out.append((mpf(m), None, None))
            continue
        best = min(pos_roots, key=lambda r: abs(mpf(m) - r))
        out.append((mpf(m), best, abs(mpf(m) - best) / mpf(m)))
    return out
