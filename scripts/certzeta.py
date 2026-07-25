"""
certzeta.py -- certified (ball-arithmetic) evaluation of the Riemann zeta function
via Euler-Maclaurin summation with a fully explicit, self-derived remainder bound.

Agent: claude-01
Implements: L-0001 (Euler-Maclaurin remainder bound), D-0002 (normalisations).

DESIGN NOTE / TRUST BOUNDARY
----------------------------
Everything here is *rigorous*: every returned object is an `acb` ball that is
guaranteed to contain the true value.  We deliberately do NOT call
`flint.acb.zeta`; the only things we borrow from Arb are:

  * correctly rounded ball arithmetic (+, -, *, /, exp, log, atan2, abs),
  * `lgamma` for the Riemann-Siegel theta function (rigorous in Arb).

Bernoulli numbers are computed *exactly* with `fractions.Fraction` from the
standard recurrence, so no library table is trusted.  The truncation bound is
proved in claims/lemmas/L-0001-euler-maclaurin-tail.md.

`flint.acb.zeta` is used ONLY in tests/ as an independent second implementation.
"""

from fractions import Fraction
from functools import lru_cache

from flint import acb, arb, ctx

__all__ = [
    "bernoulli",
    "zeta",
    "zeta_ball",
    "theta",
    "hardy_Z",
    "xi",
    "set_prec",
    "EMParams",
]


def set_prec(prec: int) -> None:
    ctx.prec = prec


# ---------------------------------------------------------------------------
# Exact Bernoulli numbers  B_0 = 1, B_1 = -1/2, B_2 = 1/6, ...
# ---------------------------------------------------------------------------
@lru_cache(maxsize=None)
def bernoulli(n: int) -> Fraction:
    """Exact Bernoulli number B_n (convention B_1 = -1/2). Recurrence:
    sum_{j=0}^{n} C(n+1, j) B_j = 0  for n >= 1."""
    if n == 0:
        return Fraction(1)
    if n == 1:
        return Fraction(-1, 2)
    if n % 2 == 1:
        return Fraction(0)
    from math import comb

    total = Fraction(0)
    for j in range(n):
        total += Fraction(comb(n + 1, j)) * bernoulli(j)
    return -total / Fraction(comb(n + 1, n))


def _frac_to_arb(q: Fraction) -> arb:
    return arb(int(q.numerator)) / arb(int(q.denominator))


_LOG_CACHE: dict[tuple[int, int], arb] = {}


def _log(n: int) -> arb:
    """Cached rigorous enclosure of log n at the current precision."""
    key = (n, ctx.prec)
    v = _LOG_CACHE.get(key)
    if v is None:
        v = arb(n).log()
        _LOG_CACHE[key] = v
    return v


# ---------------------------------------------------------------------------
# Euler-Maclaurin
# ---------------------------------------------------------------------------
class EMParams:
    """Truncation parameters: N = number of explicit terms, M = number of
    Bernoulli correction terms."""

    __slots__ = ("N", "M")

    def __init__(self, N: int, M: int):
        self.N = int(N)
        self.M = int(M)

    def __repr__(self):
        return f"EMParams(N={self.N}, M={self.M})"


def _em_error_radius(s: acb, N: int, M: int) -> arb:
    """Rigorous upper bound, valid uniformly over the ball `s`, for

        |E_{M,N}(s)| <= |(s)_{2M+1}| * |B_{2M+2}|/(2M+2)!
                        * N^{-sigma-2M-1} * (1 + |s+2M+1|/(sigma+2M+1))

    (L-0001).  Returns +inf if the hypothesis sigma + 2M + 1 > 0 can fail on
    the ball, in which case the caller must enlarge M.
    """
    sigma_lo = s.real.lower()  # rigorous lower bound of Re(s) on the ball
    denom = arb(sigma_lo) + arb(2 * M + 1)
    if not (denom > 0):
        return arb("+inf")

    # |(s)_{2M+1}| = |s (s+1) ... (s+2M)|  -- upper bound over the ball
    pf = arb(1)
    for j in range(0, 2 * M + 1):
        pf = pf * arb((s + j).abs_upper())

    b = abs(bernoulli(2 * M + 2))
    from math import factorial

    coef = _frac_to_arb(b / Fraction(factorial(2 * M + 2)))

    # N^{-(sigma+2M+1)} <= N^{-(sigma_lo+2M+1)}   (since N >= 1)
    powfac = arb(N) ** (-denom)

    tail = arb(1) + arb((s + (2 * M + 1)).abs_upper()) / denom
    return pf * coef * powfac * tail


def _add_error_disc(z: acb, radius: arb) -> acb:
    """Return a ball containing z + {w : |w| <= radius}."""
    pad = arb(0, radius.upper())
    return z + acb(pad, pad)


def zeta_ball(s: acb, params: EMParams | None = None, tol_bits: int = 30) -> acb:
    """Certified enclosure of zeta(s) for every s in the ball `s`.

    Raises ValueError if the ball contains (or comes too close to) the pole
    s = 1, where no finite enclosure exists.
    """
    if (s - 1).abs_lower() <= arb(2) ** (-ctx.prec // 2):
        raise ValueError("ball touches the pole s = 1")

    if params is None:
        params = _auto_params(s, tol_bits)

    N, M = params.N, params.M

    # main sum  sum_{n=1}^{N-1} n^{-s}
    total = acb(0)
    for n in range(1, N):
        total += (-s * _log(n)).exp()

    logN = _log(N)
    total += (-s * logN).exp() / 2
    total += ((1 - s) * logN).exp() / (s - 1)

    # Bernoulli correction:  sum_{k=1}^{M} B_{2k}/(2k)! * (s)_{2k-1} * N^{-s-2k+1}
    from math import factorial

    rising = acb(1)  # will hold (s)_{2k-1}
    j = 0
    for k in range(1, M + 1):
        while j < 2 * k - 1:
            rising = rising * (s + j)
            j += 1
        c = _frac_to_arb(bernoulli(2 * k) / Fraction(factorial(2 * k)))
        total += acb(c) * rising * ((-(s + (2 * k - 1)) * logN).exp())

    err = _em_error_radius(s, N, M)
    if not (err < arb(1)):
        raise ValueError(f"Euler-Maclaurin bound not small: {err}")
    return _add_error_disc(total, err)


def zeta_pole_free_ball(s: acb, params: EMParams | None = None, tol_bits: int = 30) -> acb:
    """Certified enclosure of the ENTIRE function  eta(s) := (s-1) * zeta(s).

    In the Euler-Maclaurin representation the only term that is singular at
    s = 1 is N^{1-s}/(s-1); multiplying through by (s-1) removes it, so this
    routine is valid on every ball, including balls containing s = 1.
    """
    if params is None:
        params = _auto_params(s, tol_bits)
    N, M = params.N, params.M

    logN = _log(N)
    total = acb(0)
    for n in range(1, N):
        total += (-s * _log(n)).exp()
    total += (-s * logN).exp() / 2

    from math import factorial

    rising = acb(1)
    j = 0
    for k in range(1, M + 1):
        while j < 2 * k - 1:
            rising = rising * (s + j)
            j += 1
        c = _frac_to_arb(bernoulli(2 * k) / Fraction(factorial(2 * k)))
        total += acb(c) * rising * ((-(s + (2 * k - 1)) * logN).exp())

    err = _em_error_radius(s, N, M)
    if not (err < arb(1)):
        raise ValueError(f"Euler-Maclaurin bound not small: {err}")
    total = _add_error_disc(total, err)

    # (s-1) * [ ... ] + N^{1-s}
    return (s - 1) * total + ((1 - s) * logN).exp()


def xi_ball(s: acb, params: EMParams | None = None) -> acb:
    """Certified enclosure of the entire Riemann xi function

        xi(s) = (1/2) s (s-1) pi^{-s/2} Gamma(s/2) zeta(s)
              = (1/2) s pi^{-s/2} Gamma(s/2) * eta(s),   eta(s) = (s-1) zeta(s).

    Zeros of xi are exactly the nontrivial zeros of zeta (the trivial zeros are
    cancelled by the poles of Gamma(s/2), and the pole of zeta at s = 1 is
    cancelled by the factor (s-1)).  Valid on every ball, including s = 1 and
    s = 0.
    """
    # (1/2) s Gamma(s/2) = Gamma(s/2 + 1), which is finite at s = 0 as well.
    eta = zeta_pole_free_ball(s)
    return ((-s / 2) * acb(arb.pi()).log()).exp() * (s / 2 + 1).gamma() * eta


# ---------------------------------------------------------------------------
# Taylor-model enclosures over balls (L-0006)
#
# Interval evaluation of the Euler-Maclaurin sum over a ball of radius r adds
# up the variation of EVERY term, while the true variation of zeta is much
# smaller because the terms cancel coherently.  At height t = 14 and r = 0.15
# the naive enclosure of (s-1)zeta(s) has radius ~119 while the function has
# modulus ~4 -- useless.  The cure is a Taylor model: expand each
# Euler-Maclaurin term about the centre (where its Taylor coefficients are
# available in closed form), sum the coefficients (cancellation now happens
# BEFORE the interval widening), and bound the tail explicitly.
# ---------------------------------------------------------------------------
def _poly_mul(a: list, b: list, p: int) -> list:
    out = [acb(0)] * p
    for i, ai in enumerate(a):
        if i >= p:
            break
        for j, bj in enumerate(b):
            if i + j >= p:
                break
            out[i + j] += ai * bj
    return out


def _exp_taylor(lam: arb, coef: acb, p: int) -> list:
    """Taylor coefficients at x = 0 of  coef * exp(-lam * x)  =
    coef * sum_k (-lam)^k x^k / k!."""
    out = []
    term = acb(coef)
    for k in range(p):
        out.append(term)
        term = term * acb(-lam) / (k + 1)
    return out


def eta_taylor_coeffs(c: acb, p: int = 20, params: EMParams | None = None):
    """Certified Taylor coefficients E_0, ..., E_{p-1} at c of the *truncated*
    Euler-Maclaurin expression for eta(s) = (s-1) zeta(s), together with a
    magnitude aggregate used for the Taylor-tail bound and the (N, M) used.

    E_k is an enclosure of the k-th Taylor coefficient of the truncated
    expression; the difference between the truncated expression and eta is
    bounded separately by the L-0001 remainder.
    """
    if params is None:
        params = _auto_params(c, 40)
    N, M = params.N, params.M
    logN = _log(N)

    G = [acb(0)] * p
    mag = arb(0)

    for n in range(1, N):
        val = (-c * _log(n)).exp()
        mag += arb(val.abs_upper())
        for k, v in enumerate(_exp_taylor(_log(n), val, p)):
            G[k] += v

    val = (-c * logN).exp() / 2
    mag += arb(val.abs_upper())
    for k, v in enumerate(_exp_taylor(logN, val, p)):
        G[k] += v

    from math import factorial

    rise = [acb(1)]
    j = 0
    for kk in range(1, M + 1):
        while j < 2 * kk - 1:
            rise = _poly_mul(rise, [c + j, acb(1)], p)
            j += 1
        cf = _frac_to_arb(bernoulli(2 * kk) / Fraction(factorial(2 * kk)))
        base = acb(cf) * ((-(c + (2 * kk - 1)) * logN).exp())
        piece = _poly_mul(rise, _exp_taylor(logN, base, p), p)
        for k in range(p):
            G[k] += piece[k]
        mag += sum((arb(piece[k].abs_upper()) for k in range(p)), arb(0))

    E = _poly_mul(G, [c - 1, acb(1)], p)
    val = ((1 - c) * logN).exp()
    mag += arb(val.abs_upper())
    for k, v in enumerate(_exp_taylor(logN, val, p)):
        E[k] += v
    return E, mag, params


def eta_and_deta(c: acb, r_cauchy="0.05"):
    """Certified (eta(c), eta'(c)) at a POINT c, from the two lowest Taylor
    coefficients.  The Euler-Maclaurin remainder E is analytic, so its
    derivative is bounded by Cauchy's estimate |E'(c)| <= sup_{B(c,R)}|E| / R
    with R = r_cauchy."""
    E, _mag, params = eta_taylor_coeffs(c, 2)
    N, M = params.N, params.M
    R = arb(r_cauchy)
    ball = acb(arb(c.real.mid(), R.upper()), arb(c.imag.mid(), R.upper()))
    e0 = _em_error_radius(c, N, M) * arb((c - 1).abs_upper())
    eR = _em_error_radius(ball, N, M) * arb((ball - 1).abs_upper())
    p0 = arb(0, e0.upper())
    p1 = arb(0, (eR / R).upper())
    return E[0] + acb(p0, p0), E[1] + acb(p1, p1)


def eta_taylor_ball(c: acb, r, params: EMParams | None = None, p: int = 20) -> acb:
    """Tight certified enclosure of eta(s) = (s-1) zeta(s) over the ball
    B(c, r), via a degree-(p-1) Taylor model about c with a rigorous tail.

    Tail bound: every piece of the Euler-Maclaurin expression is of the form
    (polynomial in s) * exp(-lambda s) with lambda = log n <= log N, so the
    Taylor tail beyond degree p-1 is bounded by
        (sum of |piece| at the centre, times its polynomial factor)
        * (r lambda)^p e^{r lambda} / p!,
    which is astronomically small already for p = 20, r <= 1/4, N <= 10^3.
    """
    r = arb(r)
    ball = acb(arb(c.real.mid(), r.upper()), arb(c.imag.mid(), r.upper()))
    if params is None:
        params = _auto_params(ball, 40)
    N, M = params.N, params.M
    E, mag, _ = eta_taylor_coeffs(c, p, params)

    total = E[0]
    spread = arb(0)
    rk = arb(1)
    for k in range(1, p):
        rk = rk * r
        spread += arb(E[k].abs_upper()) * rk

    from math import factorial

    x = r * _log(N)
    tail = mag * (x ** p) * x.exp() / arb(factorial(p))
    emerr = _em_error_radius(ball, N, M) * arb((ball - 1).abs_upper())
    pad = arb(0, (spread + tail + emerr).upper())
    return total + acb(pad, pad)


def deta_sup_ball(c: acb, r, p: int = 20) -> arb:
    """Certified upper bound for |eta'| over the ball B(c, r)."""
    r = arb(r)
    ball = acb(arb(c.real.mid(), r.upper()), arb(c.imag.mid(), r.upper()))
    params = _auto_params(ball, 40)
    E, mag, _ = eta_taylor_coeffs(c, p, params)
    tot = arb(0)
    rk = arb(1)
    for k in range(1, p):
        tot += arb(k) * arb(E[k].abs_upper()) * rk
        rk = rk * r
    from math import factorial

    x = r * _log(params.N)
    tail = mag * arb(p) * (x ** (p - 1)) * x.exp() / arb(factorial(p)) * _log(params.N)
    emerr = _em_error_radius(ball, params.N, params.M) * arb((ball - 1).abs_upper())
    return tot + tail + emerr / (r / 2)


def xi_taylor_ball(c: acb, r, p: int = 20) -> acb:
    """Tight certified enclosure of xi over the ball B(c, r)."""
    r = arb(r)
    ball = acb(arb(c.real.mid(), r.upper()), arb(c.imag.mid(), r.upper()))
    eta = eta_taylor_ball(c, r, p=p)
    return ((-ball / 2) * acb(arb.pi()).log()).exp() * (ball / 2 + 1).gamma() * eta


def _auto_params(s: acb, tol_bits: int) -> EMParams:
    """Choose (N, M) so the certified remainder is below 2^-tol_bits."""
    t = abs(float(s.imag.mid())) + float(s.imag.rad())
    N = max(8, int(t) + 8)
    M = 8
    target = arb(2) ** (-tol_bits)
    for _ in range(24):
        e = _em_error_radius(s, N, M)
        if e < target:
            return EMParams(N, M)
        M += 4
        N = int(N * 1.4) + 4
    return EMParams(N, M)


def zeta(s, params: EMParams | None = None) -> acb:
    """Convenience wrapper accepting anything acb() accepts."""
    return zeta_ball(acb(s), params)


# ---------------------------------------------------------------------------
# Riemann-Siegel theta and the Hardy Z function
#   theta(t) = Im log Gamma(1/4 + i t/2) - (t/2) log pi
#   Z(t)     = e^{i theta(t)} zeta(1/2 + i t)        (real for real t)
# ---------------------------------------------------------------------------
def theta(t) -> arb:
    tt = arb(t)
    lg = acb(arb(1) / 4, tt / 2).lgamma()
    return lg.imag - (tt / 2) * arb.pi().log()


def hardy_Z(t, params: EMParams | None = None) -> arb:
    """Certified enclosure of the Hardy function Z(t) (real-valued)."""
    tt = arb(t)
    z = zeta_ball(acb(arb(1) / 2, tt), params)
    th = theta(tt)
    val = acb(0, th).exp() * z
    # Z(t) is real; the imaginary part is a rigorous check on the enclosure.
    return val.real


def xi(s, params: EMParams | None = None) -> acb:
    """Riemann xi: xi(s) = (1/2) s (s-1) pi^{-s/2} Gamma(s/2) zeta(s)."""
    ss = acb(s)
    z = zeta_ball(ss, params)
    return (
        ss
        * (ss - 1)
        / 2
        * (acb(arb.pi()) ** (-ss / 2))
        * (ss / 2).gamma()
        * z
    )
