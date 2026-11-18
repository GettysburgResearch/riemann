"""Detection-threshold machinery for C4 (synthetic off-line quadruple injected on the zero side).

Model ("additive single-defect model"): the spectral side is
    W_mod(g) = W_true(g) + sum_{gamma in {+-T0 +- i delta}} h_g(gamma) conj(h_g(conj gamma)),
where W_true is evaluated EXACTLY on the arithmetic side (it equals the sum over the true zeros,
all of which are on the line up to height 3e12 by Platt-Trudgian), and T0 is the midpoint between
two consecutive true ordinates.  Variant ("collision"): additionally remove the two neighbouring
true zeros (so the quadruple replaces them).

Detection at window L means: min eigenvalue of W_mod restricted to the N-term modulated Legendre
basis {e^{-iT0 x} phi_j(x)} on [-L, L] is < -tau.  By Rayleigh-Ritz this certifies (up to floating
point) that the true window infimum is negative; the finite-N threshold is an UPPER bound for the
true threshold L*(T0, delta).
"""
import math
import numpy as np
from weil_core import WeilWindow, quad_matrix, real_zero_matrix, prime_powers, pi_moments, legendre_table
from scipy.special import loggamma, digamma

_WW = {}


def window(L, N):
    key = (round(L, 12), N)
    if key not in _WW:
        if len(_WW) > 64:
            _WW.clear()
        _WW[key] = WeilWindow(L, N)
    return _WW[key]


def psi_arch(r):
    """Re psi(1/4 + i r/2) - log pi (archimedean symbol)."""
    return float(np.real(digamma(0.25 + 0.5j * r))) - math.log(math.pi)


def W_true(T0, L, N, asym=False):
    """Arithmetic-side Weil matrix in the basis modulated at T0.

    asym=True (for T0 >= 1e5): archimedean part replaced by psi_arch(T0) * I (error O(log T0 / T0)),
    pole term dropped (O(1/T0)); prime part exact."""
    ww = window(L, N)
    if not asym:
        return ww.matrix(float(T0))
    pi = pi_moments(T0, L, ww.M, ww.pp)
    X = np.tensordot(ww.q, pi, axes=([2], [0]))
    W = psi_arch(float(T0)) * np.eye(N) - X - X.conj().T
    return 0.5 * (W + W.conj().T)


def lam_min(M):
    return float(np.linalg.eigvalsh(M)[0])


def lam_mod(T0, delta, L, N, model="add", neighbors=None, asym=False, W=None):
    if W is None:
        W = W_true(T0, L, N, asym=asym)
    Mq = quad_matrix(T0, delta, T0, L, N)
    Wm = W + Mq
    if model == "collision":
        Wm = Wm - real_zero_matrix(np.asarray(neighbors), T0, L, N)
    return lam_min(0.5 * (Wm + Wm.conj().T))


def threshold(T0, delta, N, Lgrid, model="add", neighbors=None, asym=False, tau=1e-9, nbis=7):
    """Smallest L (to bisection accuracy) with lam_mod < -tau, scanning Lgrid upward."""
    prev = None
    for L in Lgrid:
        lm = lam_mod(T0, delta, L, N, model, neighbors, asym)
        if lm < -tau:
            if prev is None:
                return {"L_star": L, "bracket": [None, L], "lam_at": lm}
            lo, hi = prev, L
            for _ in range(nbis):
                mid = 0.5 * (lo + hi)
                if lam_mod(T0, delta, mid, N, model, neighbors, asym) < -tau:
                    hi = mid
                else:
                    lo = mid
            return {"L_star": 0.5 * (lo + hi), "bracket": [lo, hi], "lam_at": lm}
        prev = L
    return {"L_star": None, "bracket": [prev, None], "lam_at": None}


# ---- model predictions -----------------------------------------------------------------------

def L_nyquist(T):
    return 0.5 * math.log(T / (2 * math.pi))


def L_flat(T, delta, Psi0=None):
    """Flat-symbol prediction: sinh(2 delta L)/(2 delta) - L = Psi0/2, Psi0 = log(T/2pi) by default."""
    if Psi0 is None:
        Psi0 = math.log(T / (2 * math.pi))
    f = lambda L: math.sinh(2 * delta * L) / (2 * delta) - L - Psi0 / 2
    lo, hi = 1e-9, 1.0
    while f(hi) < 0:
        hi *= 2
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def kappa_cross():
    """kappa with sinh(kappa) = 2 kappa (flat growth threshold equals the Nyquist window)."""
    lo, hi = 1.0, 3.0
    for _ in range(200):
        m = 0.5 * (lo + hi)
        if math.sinh(m) - 2 * m < 0:
            lo = m
        else:
            hi = m
    return 0.5 * (lo + hi)
