"""High-precision (python-flint Arb) assembly of the arithmetic-side Weil matrix at T = 0.

Same conventions and formulas as weil_core.py (real orthonormal Legendre basis on [-L, L]).
Ball arithmetic is used for every algebraic step; the archimedean integral is an S-node
Gauss-Legendre rule whose truncation error is NOT enclosed (convergence is checked by
varying S), so results are labelled non-rigorous high precision.
"""
import math
import flint
from flint import arb, arb_mat, ctx


def gl_nodes(n):
    out = [arb.legendre_p_root(n, k, weight=True) for k in range(n)]
    return [o[0] for o in out], [o[1] for o in out]


def legendre_vals(t, N):
    P = [arb(1), t]
    for m in range(1, N - 1):
        P.append(((2 * m + 1) * t * P[m] - m * P[m - 1]) / (m + 1))
    return P[:N]


class HPWeil:
    def __init__(self, L, N, prec=300):
        ctx.prec = prec
        self.L = arb(L) if not isinstance(L, arb) else L
        self.N = N
        self.Q = N + 2
        self.tq, self.wq = gl_nodes(self.Q)
        self.norm = [((2 * j + 1) / (2 * self.L)).sqrt() for j in range(N)]

    def phi_row(self, x):
        """phi_j(x), j < N, for x in [-L, L] (arb)."""
        P = legendre_vals(x / self.L, self.N)
        return [P[j] * self.norm[j] for j in range(self.N)]

    def A(self, y):
        L, N = self.L, self.N
        a, b = -L + y, L
        half = (b - a) / 2
        mid = (a + b) / 2
        M1 = arb_mat(N, self.Q)
        M2 = arb_mat(self.Q, N)
        for q in range(self.Q):
            x = mid + half * self.tq[q]
            r1 = self.phi_row(x)
            r2 = self.phi_row(x - y)
            wq = self.wq[q] * half
            for j in range(N):
                M1[j, q] = r1[j] * wq
                M2[q, j] = r2[j]
        return M1 * M2

    def matrix(self, S=200, pp=None):
        L, N = self.L, self.N
        I = arb_mat(N, N)
        for j in range(N):
            I[j, j] = 1
        # constant C0(L)
        e = (-L).exp()
        C1 = arb(2).log() / 2 + arb.pi() / 4
        C0 = -((4 * arb.pi()).log() + arb.const_euler()) + 2 * (e.atanh() + e.atan() - C1)
        W = I * C0
        # archimedean integral over y in [0, 2L]
        ts, ws = gl_nodes(S)
        arch = arb_mat(N, N)
        for s in range(S):
            y = L * (ts[s] + 1)
            K = (-y / 2).exp() / (1 - (-2 * y).exp())
            Ay = self.A(y)
            arch = arch + (Ay + Ay.transpose() - 2 * I) * (K * L * ws[s])
        W = W - arch
        # primes
        if pp is None:
            from weil_core import prime_powers
            pp = prime_powers(math.exp(2 * float(L.mid())) + 1)
        for n, lam in pp:
            ln = arb(n).log()
            if not (ln < 2 * L):
                continue
            p = next(d for d in range(2, n + 1) if n % d == 0)   # n = p^k, Lambda(n) = log p
            An = self.A(ln)
            W = W - (An + An.transpose()) * (arb(p).log() / arb(n).sqrt())
        # pole: a_j = int phi_j e^{x/2}, b_j = (-1)^j a_j
        Qp = N + 60
        tp, wp = gl_nodes(Qp)
        a = [arb(0)] * N
        for q in range(Qp):
            x = L * tp[q]
            r = self.phi_row(x)
            wx = wp[q] * L * (x / 2).exp()
            for j in range(N):
                a[j] = a[j] + r[j] * wx
        for j in range(N):
            for k in range(N):
                if (j + k) % 2 == 0:
                    W[j, k] = W[j, k] + 2 * (-1) ** k * a[j] * a[k]
        return W
