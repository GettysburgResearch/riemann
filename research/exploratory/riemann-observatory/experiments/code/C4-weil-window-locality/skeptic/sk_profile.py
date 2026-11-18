"""SKEPTIC (C4) -- independent re-implementation of the even-sector window profile lambda_min(L).

Written from scratch (does not import any investigator module).  mpmath, non-rigorous high precision.

Explicit formula (Bombieri 2000, Sec. 12, eq. before Thm 12), f = g*g~, f(y) = int g(x) g(x-y) dx (real g):
  W = int 2cosh(y/2) f(y) dy - sum_n Lambda(n) n^{-1/2} (f(log n)+f(-log n))
      - (log 4pi + gamma) f(0) - int_0^inf [e^{-y/2}(f(y)+f(-y)) - 2 e^{-y} f(0)]/(1-e^{-2y}) dy.
The normalisation is validated independently against the zeros side in sk_validate.py.

Basis: even orthonormal Legendre phi_j(x) = sqrt((2j+1)/(2L)) P_j(x/L), j = 0,2,...,2(n-1).
Route (different from the investigator's Legendre-coefficient tensor + composite rule):
  A(y)_jk = int_{y-L}^{L} phi_j(x) phi_k(x-y) dx by an exact Gauss rule at each outer node y;
  outer integral int_0^{2L} K(y)[A(y)+A(y)^T-2I] dy by a single high-order Gauss-Legendre rule
  (integrand analytic on a neighbourhood of [0,2L]; nearest singularity y = +-i pi);
  scalar constant C0(L) by mpmath.quad (no closed forms used).
Usage: python3 sk_profile.py L n_even dps S_outer
"""
import sys, time, json
import mpmath as mp


def gauss_legendre(n):
    """Nodes/weights on [-1,1] by Newton iteration at current mp precision."""
    xs, ws = [], []
    for i in range(1, n + 1):
        x = mp.cos(mp.pi * (i - mp.mpf(1) / 4) / (n + mp.mpf(1) / 2))
        for _ in range(100):
            p0, p1 = mp.mpf(1), x
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
            dp = n * (x * p1 - p0) / (x * x - 1)
            dx = p1 / dp
            x -= dx
            if abs(dx) < mp.mpf(10) ** (-mp.mp.dps + 3):
                break
        p0, p1 = mp.mpf(1), x
        for k in range(2, n + 1):
            p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
        dp = n * (x * p1 - p0) / (x * x - 1)
        xs.append(x)
        ws.append(2 / ((1 - x * x) * dp * dp))
    return xs, ws


def leg_vals(t, M):
    P = [mp.mpf(1), t]
    for m in range(1, M - 1):
        P.append(((2 * m + 1) * t * P[m] - m * P[m - 1]) / (m + 1))
    return P[:M]


def phi_vec(x, L, degs, M):
    t = x / L
    if abs(t) > 1:
        return [mp.mpf(0)] * len(degs)
    P = leg_vals(t, M)
    return [mp.sqrt(mp.mpf(2 * j + 1) / (2 * L)) * P[j] for j in degs]


def corr(y, L, degs, M, gq):
    """A(y)_jk = int_{y-L}^{L} phi_j(x) phi_k(x - y) dx, 0 <= y <= 2L."""
    xs, ws = gq
    a, b = y - L, L
    n = len(degs)
    A = mp.matrix(n, n)
    h = (b - a) / 2
    c = (b + a) / 2
    for x0, w0 in zip(xs, ws):
        x = c + h * x0
        u = phi_vec(x, L, degs, M)
        v = phi_vec(x - y, L, degs, M)
        wh = w0 * h
        for j in range(n):
            uj = u[j] * wh
            for k in range(n):
                A[j, k] += uj * v[k]
    return A


def prime_powers(X):
    out = []
    for p in range(2, int(X) + 1):
        if all(p % q for q in range(2, int(p ** 0.5) + 1)):
            q = p
            while q < X:
                out.append((q, mp.log(p)))
                q *= p
    return sorted(out)


def assemble(L, n_even, S_outer):
    L = mp.mpf(L)
    degs = [2 * i for i in range(n_even)]
    M = degs[-1] + 2
    gq = gauss_legendre(degs[-1] + 2)          # exact for the polynomial integrand (deg <= 2*maxdeg)
    K = lambda y: mp.exp(-y / 2) / (1 - mp.exp(-2 * y))
    # constant part
    I1 = mp.quad(lambda y: (mp.exp(-y / 2) - mp.exp(-y)) / (1 - mp.exp(-2 * y)), [0, 2 * L])
    I2 = mp.quad(lambda y: mp.exp(-y) / (1 - mp.exp(-2 * y)), [2 * L, mp.inf])
    C0 = -(mp.log(4 * mp.pi) + mp.euler) - 2 * I1 + 2 * I2
    n = n_even
    W = mp.matrix(n, n)
    for j in range(n):
        W[j, j] = C0
    # archimedean integral
    yo, wo = gauss_legendre(S_outer)
    for y0, w0 in zip(yo, wo):
        y = L * (y0 + 1)
        A = corr(y, L, degs, M, gq)
        kw = K(y) * w0 * L
        for j in range(n):
            for k in range(n):
                W[j, k] -= kw * (A[j, k] + A[k, j] - (2 if j == k else 0))
    # primes
    for (m, lam) in prime_powers(mp.exp(2 * L)):
        y = mp.log(m)
        if y >= 2 * L:
            continue
        A = corr(y, L, degs, M, gq)
        c = lam / mp.sqrt(m)
        for j in range(n):
            for k in range(n):
                W[j, k] -= c * (A[j, k] + A[k, j])
    # pole: 2 (C_j C_k - S_j S_k); S_j = 0 in the even sector
    gp = gauss_legendre(M // 2 + 30)
    C = [mp.mpf(0)] * n
    for x0, w0 in zip(*gp):
        x = L * x0
        u = phi_vec(x, L, degs, M)
        for j in range(n):
            C[j] += w0 * L * u[j] * mp.cosh(x / 2)
    for j in range(n):
        for k in range(n):
            W[j, k] += 2 * C[j] * C[k]
    return W


def main():
    L = sys.argv[1]
    n_even = int(sys.argv[2])
    mp.mp.dps = int(sys.argv[3])
    S_outer = int(sys.argv[4])
    t0 = time.time()
    W = assemble(L, n_even, S_outer)
    ev = mp.eigsy(W, eigvals_only=True)
    lam = min(ev)
    out = {"L": L, "n_even": n_even, "N_total_equiv": 2 * n_even, "dps": mp.mp.dps, "S_outer": S_outer,
           "lam_even_min": mp.nstr(lam, 15), "seconds": round(time.time() - t0, 1)}
    print(json.dumps(out), flush=True)


if __name__ == "__main__":
    main()
