"""CRIT23 part-1 audit helper: the Alpoge-Furman (arXiv:2608.13637v2) test family, built exactly as in AF Section 2.2.

  chi   : C^infinity, nondecreasing, chi = 0 on (-inf,0], chi = 1 on [1,inf)   (AF: "Fix chi ...")
          concrete choice here: chi(t) = f(t)/(f(t)+f(1-t)), f(t) = exp(-1/t) (t>0), f = 0 (t<=0)
  psi   : psi0 = 1_[-1/2,1/2]  or  psiMT(s) = cos(sqrt2 s) 1_[-1/2,1/2]          (AF eq. (2.6))
  phi(u): chi(L/2+u) chi(L/2-u) psi(u/L)^(1/2)                                    (AF eq. (2.7))
  phihat(z) = int phi(u) e^{-iuz} du  (AF Section 1.7 normalisation), evaluated for COMPLEX z
  a     = ||phi||_2^2 / L,  alpha_k = T0 + 2 pi k / L                             (AF Sections 2.2-2.3)

No AF code is used; this is an independent implementation from the paper's text. Non-rigorous floating point
(numpy double precision, composite Gauss-Legendre quadrature)."""
import numpy as np

SQ2 = np.sqrt(2.0)


def chi(t):
    t = np.asarray(t, dtype=float)
    out = np.zeros_like(t)
    inside = (t > 0) & (t < 1)
    ti = t[inside]
    f1 = np.exp(-1.0 / ti)
    f2 = np.exp(-1.0 / (1.0 - ti))
    out[inside] = f1 / (f1 + f2)
    out[t >= 1] = 1.0
    return out


def sqrt_psi(s, window):
    s = np.asarray(s, dtype=float)
    inside = np.abs(s) <= 0.5
    out = np.zeros_like(s)
    if window == "flat":
        out[inside] = 1.0
    elif window == "MT":
        out[inside] = np.sqrt(np.cos(SQ2 * s[inside]))
    else:
        raise ValueError(window)
    return out


def phi(u, L, window):
    u = np.asarray(u, dtype=float)
    return chi(L / 2 + u) * chi(L / 2 - u) * sqrt_psi(u / L, window)


class TestFunction:
    """phi for given L and window, with a quadrature rule on [0, L/2] fine enough for |Re z| <= zmax."""

    def __init__(self, L, window="flat", zmax=200.0, nodes_per_panel=24):
        self.L, self.window = float(L), window
        c = L / 2 - 1.0                      # bulk [0,c], transition [c, L/2]
        # panel width small enough that each panel sees < ~1.5 rad of oscillation at |z| = zmax
        width = min(0.05, 1.5 / max(zmax, 1.0))
        x, w = np.polynomial.legendre.leggauss(nodes_per_panel)
        us, ws = [], []
        for (A, B) in ((0.0, c), (c, L / 2)):
            n = max(4, int(np.ceil((B - A) / width)))
            edges = np.linspace(A, B, n + 1)
            for lo, hi in zip(edges[:-1], edges[1:]):
                us.append(0.5 * (hi - lo) * x + 0.5 * (hi + lo))
                ws.append(0.5 * (hi - lo) * w)
        self.u = np.concatenate(us)
        self.w = np.concatenate(ws)
        self.phiu = phi(self.u, L, window)
        self.norm2 = 2.0 * np.sum(self.w * self.phiu ** 2)          # ||phi||_2^2
        self.a = self.norm2 / L
        self.zmax = zmax

    def hat(self, z, chunk=4000):
        """phihat(z) = 2 int_0^{L/2} phi(u) cos(u z) du  (phi even, so valid for complex z)."""
        z = np.asarray(z, dtype=complex)
        flat = z.ravel()
        out = np.empty(flat.shape, dtype=complex)
        wp = 2.0 * self.w * self.phiu
        for s in range(0, flat.size, chunk):
            zz = flat[s:s + chunk]
            out[s:s + chunk] = np.cos(np.outer(zz, self.u)) @ wp
        return out.reshape(z.shape)

    def hat_phi2(self, z, chunk=4000):
        """(phi^2)^(z) = 2 int_0^{L/2} phi(u)^2 cos(u z) du."""
        z = np.asarray(z, dtype=complex)
        flat = z.ravel()
        out = np.empty(flat.shape, dtype=complex)
        wp = 2.0 * self.w * self.phiu ** 2
        for s in range(0, flat.size, chunk):
            zz = flat[s:s + chunk]
            out[s:s + chunk] = np.cos(np.outer(zz, self.u)) @ wp
        return out.reshape(z.shape)

    def l1_second_derivative(self, n=200001):
        """Numerical ||phi''||_1 (used for explicit integration-by-parts tail bounds |phihat(x)| <= ||phi''||_1 / x^2)."""
        u = np.linspace(-self.L / 2, self.L / 2, n)
        p = phi(u, self.L, self.window)
        du = u[1] - u[0]
        d2 = np.gradient(np.gradient(p, du), du)
        return float(np.sum(np.abs(d2)) * du)


def grid(T0, L, d):
    return T0 + 2.0 * np.pi * np.arange(d) / L
