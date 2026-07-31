"""
Core routines for the Loewner detectability experiment.

Model (synthetic, following L-16004):

    psi(x) = sum_p  w_p / (mu_p - x)        (poles mu_p, weights w_p)

    Loewner matrix on nodes lam_j = j, j = -N..N:
        Q_{ij} = (psi(lam_i)-psi(lam_j))/(lam_i-lam_j)   i != j
        Q_{ii} = psi'(lam_i)
    Closed form (L-16004 (i)):
        Q = sum_p w_p ell(mu_p) ell(mu_p)^T,   ell(mu)_j = 1/(lam_j - mu)

Everything is mpmath at caller-chosen dps.  Inertia is computed by a
Bunch-Parlett symmetric-indefinite LDL^T congruence with 1x1 and 2x2
pivots -- NOT by an eigenvalue routine (mpmath.eigsy is known to be
unreliable on these matrices; see O-16004 erratum).
"""

import mpmath as mp


# ---------------------------------------------------------------- matrices

def nodes(N):
    return [mp.mpf(j) for j in range(-N, N + 1)]


def ell(mu, lam):
    """ell(mu)_j = 1/(lam_j - mu).  mu may be mpf or mpc."""
    out = []
    for lj in lam:
        d = lj - mu
        if d == 0:
            raise ValueError("pole mu=%s coincides with node %s; the Loewner "
                             "matrix is undefined there" % (mu, lj))
        out.append(1 / d)
    return out


def build_Q_rank1(poles, lam):
    """Q = sum_p w_p ell(mu_p) ell(mu_p)^T, taking the real part.

    `poles` is a list of (mu, w) with mu mpf or mpc and w real.
    Complex mu must appear in conjugate pairs with equal weights so the
    sum is real; we take .real at the end (imaginary residue is a
    numerical-noise diagnostic, returned as `imag_resid`)."""
    n = len(lam)
    Q = [[mp.mpc(0) for _ in range(n)] for _ in range(n)]
    for mu, w in poles:
        v = ell(mu, lam)
        for i in range(n):
            wi = w * v[i]
            row = Q[i]
            for j in range(i, n):
                row[j] += wi * v[j]
    imag_resid = mp.mpf(0)
    R = [[mp.mpf(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            z = Q[i][j]
            imag_resid = max(imag_resid, abs(mp.im(z)))
            R[i][j] = mp.re(z)
            R[j][i] = R[i][j]
    return R, imag_resid


def psi_val(x, poles):
    return sum(w / (mu - x) for mu, w in poles)


def psi_deriv(x, poles):
    return sum(w / (mu - x) ** 2 for mu, w in poles)


def build_Q_divdiff(poles, lam):
    """Independent build straight from the divided-difference definition."""
    n = len(lam)
    p = [psi_val(lj, poles) for lj in lam]
    d = [psi_deriv(lj, poles) for lj in lam]
    Q = [[mp.mpf(0)] * n for _ in range(n)]
    for i in range(n):
        Q[i][i] = mp.re(d[i])
        for j in range(i + 1, n):
            v = mp.re((p[i] - p[j]) / (lam[i] - lam[j]))
            Q[i][j] = v
            Q[j][i] = v
    return Q


def maxabs(Q):
    return max(abs(x) for row in Q for x in row)


# ---------------------------------------------------------------- inertia

_ALPHA = (1 + mp.sqrt(17)) / 8   # Bunch-Parlett constant, recomputed per dps


def inertia(Q, tol=None):
    """Inertia (n_pos, n_neg, n_zero) by Bunch-Parlett LDL^T congruence.

    Q is a list-of-lists of mpf; it is copied, not modified.
    tol: entries whose magnitude falls below this are treated as zero.
    """
    n = len(Q)
    A = [row[:] for row in Q]
    if tol is None:
        s = maxabs(Q)
        if s == 0:
            return (0, 0, n)
        tol = s * mp.mpf(10) ** (-(mp.mp.dps - 8))
    alpha = (1 + mp.sqrt(17)) / 8

    act = list(range(n))
    npos = nneg = nzero = 0

    while act:
        # largest diagonal
        lam1 = mp.mpf(0); p = act[0]
        for i in act:
            a = abs(A[i][i])
            if a > lam1:
                lam1 = a; p = i
        # largest off-diagonal
        mu1 = mp.mpf(0); r = s2 = None
        for ii in range(len(act)):
            for jj in range(ii + 1, len(act)):
                i = act[ii]; j = act[jj]
                a = abs(A[i][j])
                if a > mu1:
                    mu1 = a; r = i; s2 = j

        if lam1 <= tol and mu1 <= tol:
            nzero += len(act)
            break

        if lam1 >= alpha * mu1:
            # ---- 1x1 pivot on p
            d = A[p][p]
            if d > 0:
                npos += 1
            else:
                nneg += 1
            act.remove(p)
            for ii in range(len(act)):
                i = act[ii]
                c = A[i][p] / d
                if c == 0:
                    continue
                for jj in range(ii, len(act)):
                    j = act[jj]
                    A[i][j] -= c * A[j][p]
                    A[j][i] = A[i][j]
        else:
            # ---- 2x2 pivot on (r,s2)
            a11 = A[r][r]; a12 = A[r][s2]; a22 = A[s2][s2]
            det = a11 * a22 - a12 * a12
            if det < 0:
                npos += 1; nneg += 1
            elif det > 0:
                if a11 + a22 > 0:
                    npos += 2
                else:
                    nneg += 2
            else:
                # singular 2x2: rank 1
                nzero += 1
                if a11 + a22 > 0:
                    npos += 1
                elif a11 + a22 < 0:
                    nneg += 1
                else:
                    nzero += 1
            act.remove(r); act.remove(s2)
            # E^{-1}
            i11 = a22 / det; i12 = -a12 / det; i22 = a11 / det
            for ii in range(len(act)):
                i = act[ii]
                u = A[i][r]; v = A[i][s2]
                c1 = i11 * u + i12 * v
                c2 = i12 * u + i22 * v
                for jj in range(ii, len(act)):
                    j = act[jj]
                    A[i][j] -= c1 * A[j][r] + c2 * A[j][s2]
                    A[j][i] = A[i][j]

    return (npos, nneg, nzero)


def n_neg(Q, tol=None):
    return inertia(Q, tol)[1]


def shifted(Q, t):
    n = len(Q)
    R = [row[:] for row in Q]
    for i in range(n):
        R[i][i] -= t
    return R


def count_below(Q, t, tol=None):
    """#eigenvalues of Q strictly below t (via inertia of Q - tI)."""
    return inertia(shifted(Q, t), tol)[1]


# ------------------------------------------------- lambda_min by bisection

def lambda_min(Q, lo_exp=-260, hi_exp=6, steps=40, tol=None):
    """Smallest eigenvalue of Q, located by *logarithmic* bisection on the
    inertia of Q - tI.  Robust: uses only the LDL congruence, never an
    eigensolver.  Log bisection is essential -- linear bisection has an
    absolute floor and would silently report the floor instead of a
    1e-40-size eigenvalue.

    Returns an mpf (signed).  `steps` log-bisection steps give a relative
    accuracy of about 10^(2^-steps) - 1, i.e. ~12 digits at steps=40.
    """
    scale = maxabs(Q)
    if scale == 0:
        return mp.mpf(0)
    pos = (count_below(Q, mp.mpf(0), tol) == 0)
    sgn = 1 if pos else -1

    def below(e):
        """count_below at t = sgn*scale*10^e"""
        return count_below(Q, sgn * scale * mp.mpf(10) ** e, tol)

    if pos:
        # want largest t>0 with count_below(t)==0 ; lam_min lies in
        # (scale*10^e, scale*10^(e+1)) where e is the largest exponent
        # with count 0.
        e = hi_exp
        while e > lo_exp and below(e) >= 1:
            e -= 1
        if below(e) >= 1:
            return mp.mpf(0)      # below the scan floor
        a, b = mp.mpf(e), mp.mpf(e + 1)
        for _ in range(steps):
            m = (a + b) / 2
            if below(m) >= 1:
                b = m
            else:
                a = m
        return scale * mp.mpf(10) ** ((a + b) / 2)
    else:
        # lam_min < 0.  t = -scale*10^e.  For e large (t very negative)
        # count_below(t)==0; as e decreases the count becomes >=1 once
        # |t| < |lam_min|.  Scan down to the crossing, then log-bisect.
        e = hi_exp
        while e > lo_exp and below(e) == 0:
            e -= 1
        if below(e) == 0:
            return mp.mpf(0)
        a, b = mp.mpf(e), mp.mpf(e + 1)   # a: count>=1, b: count==0
        for _ in range(steps):
            m = (a + b) / 2
            if below(m) == 0:
                b = m
            else:
                a = m
        return -scale * mp.mpf(10) ** ((a + b) / 2)


# ------------------------------------------------------------ pole models

def zeta_ordinates(M, dps=30):
    """First M ordinates gamma_k of the zeta zeros, from mpmath.zetazero."""
    old = mp.mp.dps
    mp.mp.dps = dps
    out = [mp.im(mp.zetazero(k)) for k in range(1, M + 1)]
    mp.mp.dps = old
    return [+g for g in out]


def make_poles(mus, weights, star_index=None, delta=None):
    """Build the pole list for psi.

    Unperturbed: for each k, poles at +mu_k and -mu_k, weight a_k each.
    Perturbed (star_index k*, delta>0): the pair at +mu_{k*} is replaced by
        (a/2) at mu_{k*} + i*delta   and   (a/2) at mu_{k*} - i*delta
    and mirrored at -mu_{k*}, so psi stays real and odd.
    """
    poles = []
    for k, (mu, a) in enumerate(zip(mus, weights)):
        if star_index is not None and k == star_index and delta is not None and delta != 0:
            d = mp.mpf(delta)
            h = a / 2
            poles.append((mp.mpc(mu, d), h))
            poles.append((mp.mpc(mu, -d), h))
            poles.append((mp.mpc(-mu, d), h))
            poles.append((mp.mpc(-mu, -d), h))
        else:
            poles.append((mp.mpf(mu), a))
            poles.append((-mp.mpf(mu), a))
    return poles


def Q_of_delta(N, mus, weights, star_index, delta):
    lam = nodes(N)
    poles = make_poles(mus, weights, star_index, delta)
    Q, _ = build_Q_rank1(poles, lam)
    return Q


# ------------------------------------------------------- delta_c bisection

def lambda_max(Q, lo_exp=-260, hi_exp=6, steps=40, tol=None):
    """Largest eigenvalue, by log-bisection on inertia of Q - tI.
    lam_max < t  iff  count_below(Q,t) == n."""
    n = len(Q)
    scale = maxabs(Q)
    if scale == 0:
        return mp.mpf(0)
    e = hi_exp
    while e > lo_exp and count_below(Q, scale * mp.mpf(10) ** e, tol) == n:
        e -= 1
    a, b = mp.mpf(e), mp.mpf(e + 1)   # a: count<n, b: count==n
    for _ in range(steps):
        m = (a + b) / 2
        if count_below(Q, scale * mp.mpf(10) ** m, tol) == n:
            b = m
        else:
            a = m
    return scale * mp.mpf(10) ** ((a + b) / 2)


def delta_critical(N, mus, weights, star_index,
                   lo_exp=-80, hi_exp=2, refine=40, tol=None, thresh=None):
    """Smallest delta at which Q(delta) acquires an eigenvalue below -thresh.

    thresh=None (default, = 0) gives the exact critical delta_c: the point
    where positive-definiteness is first lost.  A positive `thresh` gives
    the *detection* threshold for an observer who can only resolve
    eigenvalues of size thresh.

    Coarse decade scan then log-bisection.  Returns (delta_c, info dict).
    """
    T = mp.mpf(0) if thresh is None else mp.mpf(thresh)

    def neg(d):
        Q = Q_of_delta(N, mus, weights, star_index, d)
        if T != 0:
            Q = shifted(Q, -T)     # Q + T*I ; negative iff lam_min < -T
        return n_neg(Q, tol)

    calls = 0
    # coarse scan upward in decades from 10^lo_exp
    hi = None
    e = lo_exp
    while e <= hi_exp:
        d = mp.mpf(10) ** e
        calls += 1
        if neg(d) >= 1:
            hi = e
            break
        e += 1
    if hi is None:
        return None, {"calls": calls, "note": "no negative eigenvalue up to 10^%d" % hi_exp}
    lo = hi - 1
    if lo < lo_exp:
        # even the smallest tested delta is already negative
        return mp.mpf(10) ** lo_exp, {"calls": calls, "note": "delta_c <= 10^%d (below scan floor)" % lo_exp}
    a, b = mp.mpf(lo), mp.mpf(hi)   # log10 bracket
    for _ in range(refine):
        m = (a + b) / 2
        calls += 1
        if neg(mp.mpf(10) ** m) >= 1:
            b = m
        else:
            a = m
    return mp.mpf(10) ** ((a + b) / 2), {"calls": calls, "log10": float((a + b) / 2)}
