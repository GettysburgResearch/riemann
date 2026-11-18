"""Core routines for campaign C4-weil-window-locality (Riemann Observatory).

Weil quadratic form on test functions g supported in [-L, L] (log variable), in the
normalisation of the campaign brief:

    h_g(r) = int g(x) e^{irx} dx,
    W(g*g~) = sum_rho h_g(gamma) conj(h_g(conj gamma)),   rho = 1/2 + i gamma,
            = T[f],  f = g*g~,  f(y) = int g(x) conj(g(x-y)) dx,

with the explicit formula (Guinand-Weil; Bombieri 2000 Sec. 12, Suzuki 2026 Sec. 1)

    T[f] = int 2cosh(y/2) f(y) dy - sum_n Lambda(n) n^{-1/2} (f(log n) + f(-log n))
           - (log 4 pi + gamma_E) f(0)
           - int_0^inf [e^{-y/2}(f(y)+f(-y)) - 2 e^{-y} f(0)] / (1 - e^{-2y}) dy.

Basis: orthonormal Legendre phi_j(x) = sqrt((2j+1)/(2L)) P_j(x/L) on [-L, L], optionally
modulated: g(x) = e^{-iTx} sum_j c_j phi_j(x), so that h_g(r) = e_j(r) with
e_j(z) = int phi_j(x) e^{i(z-T)x} dx concentrated near r = T.

Matrix convention: W(g*g~) = sum_{jk} c_j conj(c_k) W_jk ; W is Hermitian and the Rayleigh
quotient has the same eigenvalues (Gram matrix = identity). Every finite-basis minimum
eigenvalue is a variational UPPER bound for the true window infimum (Rayleigh-Ritz).

Closed forms used (derived in the C4 report):
  c1 = int_0^1 (u^{-1/2}-1)/(1-u^2) du = (log 2)/2 + pi/4,
  c2(L) = int_0^{e^{-2L}} u^{-1/2}/(1-u^2) du = artanh(e^{-L}) + arctan(e^{-L}),
  Arch_jk = C0(L) delta_jk - int_0^{2L} K(y) [f_jk(y) + f_jk(-y) - 2 delta_jk] dy,
  K(y) = e^{-y/2}/(1-e^{-2y}),  C0(L) = -(log 4pi + gamma_E) + 2(c2(L) - c1).
"""
import math
import functools
import numpy as np
from numpy.polynomial.legendre import leggauss as _leggauss


@functools.lru_cache(maxsize=64)
def _lg(n):
    t, w = _leggauss(n)
    t.setflags(write=False); w.setflags(write=False)
    return t, w


def leggauss(n):
    return _lg(int(n))

EULER_GAMMA = 0.57721566490153286061
LOG4PI = math.log(4 * math.pi)
C1 = 0.5 * math.log(2.0) + math.pi / 4


def C0(L):
    e = math.exp(-L)
    return -(LOG4PI + EULER_GAMMA) + 2.0 * (math.atanh(e) + math.atan(e) - C1)


def prime_powers(X):
    """List of (n, Lambda(n)) with 2 <= n < X."""
    X = int(math.ceil(X))
    if X < 3:
        return []
    sieve = np.ones(X, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(X ** 0.5) + 1):
        if sieve[p]:
            sieve[p * p::p] = False
    out = []
    for p in np.nonzero(sieve)[0]:
        p = int(p)
        lp = math.log(p)
        q = p
        while q < X:
            out.append((q, lp))
            q *= p
    out.sort()
    return out


def legendre_table(t, M):
    """P_m(t) for m < M, t array in [-1,1]; returns (M, len(t))."""
    t = np.asarray(t, dtype=float)
    P = np.empty((M, t.size))
    P[0] = 1.0
    if M > 1:
        P[1] = t
    for m in range(1, M - 1):
        P[m + 1] = ((2 * m + 1) * t * P[m] - m * P[m - 1]) / (m + 1)
    return P


def phi_table(x, L, N):
    """Orthonormal Legendre basis values phi_j(x), zero outside [-L, L]; (N, len(x))."""
    x = np.asarray(x, dtype=float)
    t = x / L
    inside = np.abs(t) <= 1.0
    P = legendre_table(np.clip(t, -1, 1), N)
    norm = np.sqrt((2 * np.arange(N) + 1) / (2 * L))[:, None]
    return P * norm * inside[None, :]


def corr_matrix(y, L, N, Q=None):
    """A(y)_jk = int phi_j(x) phi_k(x-y) dx for 0 <= y <= 2L (exact Gauss rule)."""
    if Q is None:
        Q = N + 2
    t, w = leggauss(Q)
    a, b = -L + y, L
    x = 0.5 * (a + b) + 0.5 * (b - a) * t
    wx = 0.5 * (b - a) * w
    P1 = phi_table(x, L, N)
    P2 = phi_table(x - y, L, N)
    return (P1 * wx[None, :]) @ P2.T


def q_tensor(L, N):
    """Legendre coefficients q[j,k,m] of A(y)_jk on [0, 2L] in P_m(y/L - 1), m < 2N (exact)."""
    M = 2 * N
    R = 2 * N + 2
    t, w = leggauss(R)
    y = L * (t + 1.0)
    P = legendre_table(t, M)  # (M, R)
    A = np.stack([corr_matrix(yy, L, N) for yy in y], axis=0)  # (R, N, N)
    coef = ((2 * np.arange(M) + 1) / 2.0)[:, None] * P * w[None, :]  # (M, R)  (dy = L dt, (2m+1)/(2L))
    q = np.tensordot(A, coef, axes=([0], [1]))  # (N, N, M)
    return np.ascontiguousarray(q)


def mu_moments(T, L, M, S=None, panel_nodes=16, chunk=40000):
    """mu_m(T) = int_0^{2L} K(y)[e^{-iTy} P_m(y/L-1) - P_m(-1)] dy, m < M.

    Composite Gauss-Legendre rule: panels of length <= min(2L/16, 2 wavelengths, 2L/(M/4)),
    `panel_nodes` nodes per panel (>= 8 nodes per wavelength).  S (if given) overrides the
    number of panels."""
    if S is None:
        npan = int(max(16, M // 2, math.ceil(abs(T) * 2 * L / (4 * math.pi)) + 1))
    else:
        npan = int(S)
    t0, w0 = leggauss(panel_nodes)
    edges = np.linspace(0.0, 2 * L, npan + 1)
    Pm1 = (-1.0) ** np.arange(M)
    acc = np.zeros(M, dtype=complex)
    ppc = max(1, chunk // panel_nodes)
    for c0 in range(0, npan, ppc):
        c1 = min(c0 + ppc, npan)
        a = edges[c0:c1][:, None]
        b = edges[c0 + 1:c1 + 1][:, None]
        y = (0.5 * (a + b) + 0.5 * (b - a) * t0[None, :]).ravel()
        wy = (0.5 * (b - a) * w0[None, :]).ravel()
        K = np.exp(-y / 2) / (-np.expm1(-2 * y))
        P = legendre_table(y / L - 1.0, M)
        ph = np.exp(-1j * np.mod(T * y, 2 * np.pi))
        integrand = (K * wy)[None, :] * (ph[None, :] * P - Pm1[:, None])
        acc += integrand.sum(axis=1)
    return acc


def pi_moments(T, L, M, pp=None):
    """pi_m(T) = sum_{log n < 2L} Lambda(n) n^{-1/2} e^{-iT log n} P_m(log n / L - 1)."""
    if pp is None:
        pp = prime_powers(math.exp(2 * L))
    pp = [(n, lam) for (n, lam) in pp if math.log(n) < 2 * L]
    if not pp:
        return np.zeros(M, dtype=complex)
    ln = np.array([math.log(n) for n, _ in pp])
    lam = np.array([l for _, l in pp])
    amp = lam / np.sqrt(np.array([float(n) for n, _ in pp]))
    if abs(float(T)) > 1e6:
        # phases T log n mod 2pi computed in 60-digit arithmetic (T may be passed as a decimal string)
        import mpmath as mp
        with mp.workdps(60):
            Tm = mp.mpf(T)
            twopi = 2 * mp.pi
            ph = [float(mp.fmod(Tm * mp.log(n), twopi)) for n, _ in pp]
        phase = np.exp(-1j * np.array(ph))
    else:
        phase = np.exp(-1j * np.mod(float(T) * ln, 2 * np.pi))
    P = legendre_table(ln / L - 1.0, M)
    return P @ (amp * phase)


def e_vals(z, T, L, N, Q=None):
    """e_j(z) = int phi_j(x) e^{i(z - T)x} dx = i^j sqrt(2L(2j+1)) j_j((z-T)L), complex z; (N, len(z))."""
    from scipy.special import spherical_jn
    z = np.atleast_1d(np.asarray(z, dtype=complex))
    w = (z - T) * L
    j = np.arange(N)
    pref = (1j ** j) * np.sqrt(2 * L * (2 * j + 1))
    J = np.stack([spherical_jn(jj, w) for jj in j])
    return pref[:, None] * J


def e_vals_quad(z, T, L, N, Q=None):
    """Quadrature version of e_vals (used only as a cross-check)."""
    z = np.atleast_1d(np.asarray(z, dtype=complex))
    if Q is None:
        Q = int(max(80, np.max(np.abs(z - T)) * L * 0.8 + N + 60))
    t, w = leggauss(Q)
    x = L * t
    wx = L * w
    P = phi_table(x, L, N)
    E = np.exp(1j * np.outer(x, z - T))
    return (P * wx[None, :]) @ E


def pole_matrix(T, L, N):
    """Pole_jk = a+_j conj(a-_k) + a-_j conj(a+_k), a+-_j = int phi_j e^{-iTx} e^{+-x/2} dx."""
    # a+-_j = int phi_j e^{-iTx} e^{+-x/2} = e_j(z) with z = -+ i/2 (since e_j(z) = int phi_j e^{i(z-T)x})
    E2 = e_vals(np.array([-0.5j, 0.5j]), T, L, N)
    ap, am = E2[:, 0], E2[:, 1]
    return np.outer(ap, am.conj()) + np.outer(am, ap.conj())


class WeilWindow:
    """Arithmetic-side Weil matrix on [-L, L] in an N-term (modulated) Legendre basis."""

    def __init__(self, L, N):
        self.L, self.N, self.M = L, N, 2 * N
        self.q = q_tensor(L, N)
        self.pp = prime_powers(math.exp(2 * L))
        self.C0 = C0(L)

    def matrix(self, T=0.0, S=None):
        L, N, M = self.L, self.N, self.M
        mu = mu_moments(T, L, M, S)
        pi = pi_moments(T, L, M, self.pp)
        v = mu + pi
        X = np.tensordot(self.q, v, axes=([2], [0]))
        W = self.C0 * np.eye(N) - X - X.conj().T + pole_matrix(T, L, N)
        return 0.5 * (W + W.conj().T)


def quad_matrix(T0, delta, T, L, N, sides=(1, -1)):
    """Contribution of an off-line quadruple {+-T0 +- i delta}: sum_gamma e(gamma) conj(e(conj gamma))."""
    G = []
    for s in sides:
        G += [s * T0 - 1j * delta * s, s * T0 + 1j * delta * s]
    G = np.array(G)
    E = e_vals(G, T, L, N)
    Ec = e_vals(G.conj(), T, L, N)
    Mq = np.zeros((N, N), dtype=complex)
    for i in range(len(G)):
        Mq += np.outer(E[:, i], Ec[:, i].conj())
    return Mq


def real_zero_matrix(gammas, T, L, N):
    """sum over real ordinates (both signs) of e(gamma) conj(e(gamma))."""
    g = np.concatenate([np.asarray(gammas, float), -np.asarray(gammas, float)])
    E = e_vals(g, T, L, N)
    return E @ E.conj().T


def spectral_matrix_T0(L, N, zeros, tail=True):
    """Spectral side at T = 0 (real Legendre basis) from real ordinates + smooth tail."""
    from scipy.special import spherical_jn
    c = np.sqrt(2 * L * (2 * np.arange(N) + 1))
    Jz = np.stack([spherical_jn(j, L * zeros) for j in range(N)])  # (N, nz)
    S = Jz @ Jz.T
    jj = np.arange(N)
    par = ((jj[:, None] - jj[None, :]) % 2 == 0)
    sgn = np.where(par, (-1.0) ** (((jj[:, None] - jj[None, :]) // 2) % 2), 0.0)
    if tail:
        # smooth tail: j_j(z) j_k(z) ~ cos((j-k)pi/2)/(2 z^2) on average; dN = log(t/2pi)/(2pi) dt
        gm = zeros[-1]
        S = S + sgn * (math.log(gm / (2 * math.pi)) + 1) / (2 * math.pi * gm) / (2 * L * L)
    return 2 * sgn * np.outer(c, c) * S
