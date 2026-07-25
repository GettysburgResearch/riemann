"""
weil.py -- the Weil explicit-formula quadratic form, in certified arithmetic.

Agent: claude-01
Implements: T-0002 (Weil positivity as a finite, prime-only witness).

THE IDEA
--------
Weil's explicit formula turns a sum over the zeros of zeta into a sum over
PRIMES plus an archimedean term.  For a test function pair (g, h) with

    h(r) = INT g(u) e^{iru} du,      g compactly supported,

the formula reads

  sum_rho h(gamma_rho)
      =  h(i/2) + h(-i/2)                              (the pole at s = 1)
       -  g(0) log pi
       +  (1/2 pi) INT h(r) Re psi(1/4 + i r/2) dr     (archimedean)
       -  sum_n (Lambda(n)/sqrt n) [ g(log n) + g(-log n) ]      (primes)

where rho = 1/2 + i gamma_rho runs over the nontrivial zeros.

Now take g = phi * phi~ for a real phi, so that h = |phi^|^2 >= 0 on the REAL
axis.  If RH holds every gamma_rho is real, so every term of the left side is
>= 0 and the sum is >= 0.  If RH fails, some gamma_rho is non-real and the sum
can go negative.  That is Weil's positivity criterion:

    RH   <=>   W(phi) := sum_rho h(gamma_rho)  >=  0   for every such phi.

WHY THIS IS A DIFFERENT KIND OF WITNESS
---------------------------------------
The right-hand side contains **no zeta evaluation at all**.  If phi is
supported in an interval of length A, then g is supported in [-A, A] and the
prime sum is FINITE -- only prime powers n <= e^A appear.  Everything else is a
Gamma-function integral.  So W(phi) is computable exactly, from finitely many
primes, and

    a certified NEGATIVE value of W  is a counterexample to RH,

with no contour, no analytic continuation, and no zero-finding anywhere in the
computation.  Compare T-0001, which needs certified enclosures of zeta on a
contour: this needs a list of primes.

W is a quadratic form in phi, so on a finite-dimensional space of test
functions it is a MATRIX, and the search for a counterexample becomes: is that
matrix positive semidefinite?  A certified negative eigenvalue is the witness.
The PSD certification reuses the interval LDL of hermite.py.

BASIS
-----
phi_j(u) = B_m((u - t_j)/a), a shifted cardinal B-spline of order m.  Then

    phi^_j(r) = a e^{i r t_j} sinc^m(a r / 2),
    g_jk(u)   = a B_{2m}((u - d)/a),          d = t_j - t_k,
    h_jk(r)   = a^2 e^{i r d} sinc^{2m}(a r / 2),

because B_m * B_m = B_{2m}.  Symmetrising in (j,k) replaces e^{ird} by
cos(rd) and makes g even.  Three of the four terms are then available in
CLOSED FORM (see below); only the archimedean integral needs quadrature.

TRUST BOUNDARY
--------------
Certified: exact integers for Lambda(n), exact rational B-spline coefficients,
arb ball arithmetic throughout, a rigorous tail bound for the archimedean
integral.  Borrowed from Arb: ball arithmetic and `digamma`.  Borrowed from the
literature and NOT reproved here: the explicit formula itself (validated
numerically against certified zeros in X-0006) and the standard remainder bound
for the asymptotic expansion of psi (used only for the tail estimate).
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from math import comb, factorial

from flint import arb, acb, ctx

__all__ = ["bspline", "weil_entry", "weil_matrix", "prime_powers", "F_terms"]


# ---------------------------------------------------------------------------
# cardinal B-splines:  B_n = box^{*n},  supported on [-n/2, n/2]
#   B_n(x) = 1/(n-1)! * sum_k (-1)^k C(n,k) (x + n/2 - k)_+^{n-1}
# ---------------------------------------------------------------------------
def bspline(n: int, x: arb) -> arb:
    """Cardinal B-spline of order n, evaluated in ball arithmetic.

    Exact rational coefficients; the only inexactness is the arithmetic.  For a
    ball input the result is a valid enclosure (each truncated power is
    monotone, and arb's max(0, .) is handled by the branch below)."""
    x = arb(x)
    half = arb(n) / 2
    if x <= -half or x >= half:
        return arb(0)
    total = arb(0)
    for k in range(n + 1):
        t = x + half - k
        if t > 0:
            total += arb((-1) ** k * comb(n, k)) * (t ** (n - 1))
        elif not (t <= 0):
            # ball straddles the knot: enclose by [0, t_up^{n-1}]
            up = arb(t.upper())
            if up > 0:
                val = up ** (n - 1)
                total += arb((-1) ** k * comb(n, k)) * arb(val.mid(), val.upper())
    return total / arb(factorial(n - 1))


@lru_cache(maxsize=None)
def prime_powers(limit_log: float, cap: int = 10**7):
    """[(n, Lambda(n))] for prime powers n <= e^{limit_log}.  Exact integers."""
    import math

    N = min(cap, int(math.exp(limit_log)) + 1)
    if N < 2:
        return ()
    sieve = bytearray([1]) * (N + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, int(N**0.5) + 1):
        if sieve[i]:
            sieve[i * i:: i] = bytearray(len(sieve[i * i:: i]))
    out = []
    for p in range(2, N + 1):
        if sieve[p]:
            q = p
            while q <= N:
                out.append((q, p))     # (n, p) with Lambda(n) = log p
                q *= p
    out.sort()
    return tuple(out)


# ---------------------------------------------------------------------------
# the four terms of the explicit formula, for the symmetrised pair
#     g(u) = (a/2) [ B_{2m}((u-d)/a) + B_{2m}((u+d)/a) ]
#     h(r) = a^2 cos(r d) sinc^{2m}(a r / 2)
# ---------------------------------------------------------------------------
def _pole_term(a: arb, d: arb, m: int) -> arb:
    """h(i/2) + h(-i/2) = 2 INT g(u) cosh(u/2) du, in CLOSED FORM.

    INT B_{2m}(t) e^{ct} dt = (2 sinh(c/2)/c)^{2m}, so with u = d + a t,

        INT a B_{2m}((u-d)/a) e^{u/2} du = a^2 e^{d/2} (4 sinh(a/4)/a)^{2m}.

    Averaging the +-d shifts and adding the e^{-u/2} companion gives
        2 a^2 cosh(d/2) (4 sinh(a/4)/a)^{2m}.
    """
    s = 4 * (a / 4).sinh() / a
    return 2 * a**2 * (d / 2).cosh() * (s ** (2 * m))


def _g0(a: arb, d: arb, m: int) -> arb:
    """g(0) = a B_{2m}(d/a)  (the two shifts coincide at u = 0)."""
    return a * bspline(2 * m, d / a)


def _g_at(u: arb, a: arb, d: arb, m: int) -> arb:
    """The symmetrised g at u."""
    return a * (bspline(2 * m, (u - d) / a) + bspline(2 * m, (u + d) / a)) / 2


def _prime_term(a: arb, d: arb, m: int) -> arb:
    """- sum_n (Lambda(n)/sqrt n) [g(log n) + g(-log n)] = -2 sum_n ... g(log n)
    since g is even.  FINITE: g is supported in |u| <= m a + |d|."""
    A = float(m * a + abs(d)) + 1e-9
    total = arb(0)
    for n, p in prime_powers(round(A, 9)):
        u = arb(n).log()
        gv = _g_at(u, a, d, m)
        if gv == 0:
            continue
        total += arb(p).log() / arb(n).sqrt() * gv
    return -2 * total


def _laplace_halfline(c: arb, a: arb, delta: arb, n: int) -> arb:
    """L1(c) = INT_0^inf B_n((u - delta)/a) e^{-cu} du, in CLOSED FORM.

    Using B_n(x) = 1/(n-1)! sum_k (-1)^k C(n,k) (x + n/2 - k)_+^{n-1}, the k-th
    truncated power turns on at u = K_k := delta + a(k - n/2), so

      K_k >= 0 :  INT_{K_k}^inf ((u-K_k)/a)^{n-1} e^{-cu} du
                     = e^{-c K_k} (n-1)! / (a^{n-1} c^n)
      K_k <  0 :  INT_0^inf ((u-K_k)/a)^{n-1} e^{-cu} du
                     = sum_j C(n-1,j) (-K_k)^{n-1-j} j! / (a^{n-1} c^{j+1}).
    """
    tot = arb(0)
    for k in range(n + 1):
        K = delta + a * (arb(k) - arb(n) / 2)
        coef = arb((-1) ** k * comb(n, k))
        if K >= 0:
            I = (-c * K).exp() * arb(factorial(n - 1)) / (c ** n)
        else:
            mK = -K
            I = arb(0)
            for j in range(n):
                I += (arb(comb(n - 1, j)) * (mK ** (n - 1 - j))
                      * arb(factorial(j)) / (c ** (j + 1)))
        tot += coef * I
    return tot / (arb(factorial(n - 1)) * (a ** (n - 1)))


def _L(c: arb, a: arb, d: arb, m: int) -> arb:
    """INT_0^inf g(u) e^{-cu} du for the symmetrised g."""
    n = 2 * m
    return (a / 2) * (_laplace_halfline(c, a, d, n)
                      + _laplace_halfline(c, a, -d, n))


def _arch_term(a: arb, d: arb, m: int, N: int = 20000, **kw) -> arb:
    """(1/2 pi) INT h(r) Re psi(1/4 + i r/2) dr, in closed form up to a
    rapidly convergent series with a rigorous tail bound.

    DERIVATION (from psi(z) = -gamma + sum_{n>=0} [1/(n+1) - 1/(n+z)]):

      Re 1/(n + 1/4 + ir/2) = (n+1/4)/((n+1/4)^2 + r^2/4),  whose inverse
      Fourier transform is e^{-(2n+1/2)|u|}.  Hence

        (1/2pi) INT h Re psi dr
              = -gamma g(0) + sum_n [ g(0)/(n+1) - INT g(u) e^{-c_n|u|} du ]

      with c_n = 2n + 1/2.  That series converges only like 1/n^2, so add and
      subtract the exactly summable part, using
      sum_n [1/(n+1) - 1/(n+1/4)] = psi(1/4) + gamma:

        (1/2pi) INT h Re psi dr = g(0) psi(1/4) - 2 sum_n [ L(c_n) - g(0)/c_n ]

      where L(c) = INT_0^inf g e^{-cu} du (g is even).  Now, because g is even
      and C^1, g(u) - g(0) = O(u^2) and

        | L(c) - g(0)/c |  =  | INT_0^inf (g(u)-g(0)) e^{-cu} du |
                           <= (max|g''|/2) INT_0^inf u^2 e^{-cu} du
                           =  max|g''| / c^3 ,

      so the terms decay like n^{-3} and the tail beyond N is bounded by
      max|g''| INT_N^inf (2t+1/2)^{-3} dt = max|g''| / (4 (2N+1/2)^2).
      For g(u) = a B_{2m}((u-d)/a) we have |g''| <= 4/a (B-splines are bounded
      by 1 and a second difference costs a factor 4).
    """
    g0 = _g0(a, d, m)
    total = arb(0)
    for n in range(N):
        c = arb(2 * n) + arb(1) / 2
        total += _L(c, a, d, m) - g0 / c
    gpp = 4 / a
    tail = gpp / (4 * (arb(2 * N) + arb(1) / 2) ** 2)
    total += arb(0, tail.upper())
    psi_quarter = acb(arb(1) / 4).digamma().real
    return g0 * psi_quarter - 2 * total


def F_terms(a, d, m: int = 2, nsub: int = 20000):
    """All four terms of the explicit formula for the symmetrised (g, h)."""
    a, d = arb(a), arb(d)
    pole = _pole_term(a, d, m)
    logpi = -_g0(a, d, m) * arb.pi().log()
    arch = _arch_term(a, d, m, N=nsub)
    primes = _prime_term(a, d, m)
    return {"pole": pole, "logpi": logpi, "arch": arch, "primes": primes,
            "total": pole + logpi + arch + primes}


def weil_entry(a, d, m: int = 2, nsub: int = 20000) -> arb:
    """The Weil functional W for the symmetrised pair at shift d."""
    return F_terms(a, d, m, nsub)["total"]


def weil_matrix(a, shifts, m: int = 2, nsub: int = 20000, verbose=False):
    """The Weil quadratic form on span{ phi_j = B_m((u - t_j)/a) }.

    Q_{jk} depends only on d = t_j - t_k, so only the distinct differences are
    computed."""
    a = arb(a)
    shifts = [arb(t) for t in shifts]
    n = len(shifts)
    cache = {}
    Q = [[arb(0)] * n for _ in range(n)]
    for j in range(n):
        for k in range(j, n):
            d = shifts[j] - shifts[k]
            key = round(float(d), 12)
            if key not in cache:
                cache[key] = weil_entry(a, d, m, nsub)
                if verbose:
                    print(f"    d={key:+.4f} -> {cache[key]}", flush=True)
            Q[j][k] = Q[k][j] = cache[key]
    return Q
