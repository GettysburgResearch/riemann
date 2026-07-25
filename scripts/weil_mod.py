"""
weil_mod.py -- the Weil quadratic form with MODULATED test functions.

Agent: claude-01
Extends weil.py; implements T-0002 part (d) -- the matched filter.

WHY MODULATE
------------
In weil.py the test functions are B-splines centred at u = 0, so

    h(r) = a^2 sinc^{2m}(a r / 2)

is a bump at r = 0.  The Weil functional therefore weighs the zeros near
gamma = 0 heavily and the zeros near gamma = 14 hardly at all -- so the
criterion is nearly blind to a displacement at height 14, which is exactly
where we want to look.  Measured in X-0006 part 3: with the unmodulated basis
the smallest detectable displacement at gamma = 14.13 is delta ~ 0.1.

The cure is a matched filter.  Take

    phi_j(u) = e^{i gamma_0 u} B_m((u - t_j)/a)

so that phi^_j(r) = a e^{i(r-gamma_0)t_j} sinc^m(a(r-gamma_0)/2) is concentrated
at r = gamma_0.  Then h = |phi^|^2 is a bump AT THE SUSPECTED HEIGHT, and the
functional becomes a local probe there.  The whole computation stays finite and
prime-only: the modulation multiplies g by e^{i gamma_0 u}, so the prime sum
picks up the factor n^{i gamma_0} -- i.e. the primes are being asked about the
frequency gamma_0, which is precisely the spectral question of X-0005 but now
inside a POSITIVITY criterion, where a certified negative value is a proof.

WHAT CHANGES IN THE ARITHMETIC
------------------------------
g(u) = e^{i gamma_0 u} G(u) with G(u) = a B_{2m}((u-d)/a) real and even.  Then

  * pole term: closed form, with a complex exponent;
  * g(0): unchanged (real);
  * prime sum: finite, with cos/sin of gamma_0 log n;
  * archimedean: same derivation as weil.py, but now g'(0) = i gamma_0 G(0) is
    NOT zero, so the series terms decay only like c^{-2}.  Subtracting that
    term as well -- and summing it exactly with sum_n c_n^{-2} = psi'(1/4)/4 --
    restores c^{-3} decay.

Everything is done in acb; the symmetrised entry must come out real, and the
imaginary part is checked to enclose 0 as a self-test.
"""

from __future__ import annotations

from math import comb, factorial

from flint import acb, arb

import weil as _w

__all__ = ["weil_entry_mod", "weil_matrix_mod", "F_terms_mod"]


def _laplace_halfline_c(c: acb, a: arb, delta: arb, n: int) -> acb:
    """INT_0^inf B_n((u - delta)/a) e^{-cu} du for COMPLEX c (Re c > 0)."""
    tot = acb(0)
    for k in range(n + 1):
        K = delta + a * (arb(k) - arb(n) / 2)
        coef = acb((-1) ** k * comb(n, k))
        if K >= 0:
            I = (-c * acb(K)).exp() * acb(factorial(n - 1)) / (c ** n)
        else:
            mK = -K
            I = acb(0)
            for j in range(n):
                I += (acb(comb(n - 1, j)) * acb(mK ** (n - 1 - j))
                      * acb(factorial(j)) / (c ** (j + 1)))
        tot += coef * I
    return tot / acb(arb(factorial(n - 1)) * (a ** (n - 1)))


def _G_laplace(c: acb, a: arb, d: arb, m: int) -> acb:
    """INT_0^inf G(u) e^{-cu} du, G(u) = (a/2)[B_{2m}((u-d)/a)+B_{2m}((u+d)/a)]."""
    n = 2 * m
    return (acb(a) / 2) * (_laplace_halfline_c(c, a, d, n)
                           + _laplace_halfline_c(c, a, -d, n))


def _bspline_c(n, x):
    return _w.bspline(n, x)




# ---------------------------------------------------------------------------
# Watson acceleration: subtract the first K+1 terms of the asymptotic expansion
# of Ghat(c) and sum them exactly with Hurwitz zeta.  This is what makes the
# matched filter affordable at LARGE gamma_0: without it the series terms decay
# only like gamma_0^2 / c^3 and one needs N ~ 10^4 gamma_0 terms; with K = 2 the
# decay is gamma_0^6 / c^7 and N ~ 25 gamma_0 suffices.
# ---------------------------------------------------------------------------
def _bspline_deriv(n: int, k: int, x) -> arb:
    """k-th derivative of the cardinal B-spline B_n, as a k-th central
    difference of B_{n-k}:  B_n^{(k)}(x) = sum_j (-1)^j C(k,j) B_{n-k}(x+k/2-j)."""
    if k == 0:
        return _w.bspline(n, arb(x))
    tot = arb(0)
    for j in range(k + 1):
        tot += arb((-1) ** j * comb(k, j)) * _w.bspline(n - k, arb(x) + arb(k) / 2 - j)
    return tot


def _G_even_derivs(a: arb, d: arb, m: int, K: int):
    """G^{(2k)}(0) for k = 0..K, where G(u) = (a/2)[B_{2m}((u-d)/a)+B_{2m}((u+d)/a)].
    For even order the two shifts contribute equally."""
    return [a ** (1 - 2 * k) * _bspline_deriv(2 * m, 2 * k, d / a) for k in range(K + 1)]


def _ghat_even_derivs(a: arb, d: arb, g0f: arb, m: int, K: int):
    """(cos(g0 u) G(u))^{(2k)}(0) = sum_i C(2k,2i) (-1)^i g0^{2i} G^{(2k-2i)}(0)."""
    Gd = _G_even_derivs(a, d, m, K)
    out = []
    for k in range(K + 1):
        tot = arb(0)
        for i in range(k + 1):
            tot += arb((-1) ** i * comb(2 * k, 2 * i)) * (g0f ** (2 * i)) * Gd[k - i]
        out.append(tot)
    return out


def _S(p: int) -> arb:
    """sum_{n>=0} (2n + 1/2)^{-p} = 2^{-p} zeta(p, 1/4)."""
    return (acb(p).zeta(acb(arb(1) / 4)) / acb(2) ** p).real


def _dmax_bound(a: arb, g0f: arb, M: int) -> arb:
    """max |(cos(g0 u) G(u))^{(M)}| <= sum_j C(M,j) g0^j max|G^{(M-j)}|,
    with max|G^{(i)}| <= a^{1-i} 2^i  (|B_n| <= 1 and each derivative is a
    difference, costing a factor 2)."""
    tot = arb(0)
    for j in range(M + 1):
        i = M - j
        tot += arb(comb(M, j)) * (g0f ** j) * (a ** (1 - i)) * arb(2) ** i
    return tot


def F_terms_mod(a, d, gamma0, m: int = 2, N: int = 60000, K: int = 2):
    """The four terms of the explicit formula for the modulated, symmetrised
    pair  g(u) = e^{i gamma_0 u} G(u),  h(r) = |...|  (see module docstring)."""
    a, d, g0f = arb(a), arb(d), arb(gamma0)

    # ---- G and its values -------------------------------------------------
    G0 = a * _w.bspline(2 * m, d / a)          # G(0) = g(0) (modulation = 1)
    # ---- pole term  h(i/2) + h(-i/2) = INT g(u)(e^{-u/2} + e^{u/2}) du -----
    # INT e^{i g0 u} G(u) e^{s u} du over R, G even:
    #   = INT G(u) e^{(s + i g0)u} du = a^2 e^{(s+ig0) d}... symmetrised over +-d
    # Using INT B_{2m}(t) e^{ct} dt = (2 sinh(c/2)/c)^{2m}:
    pole = acb(0)
    for sgn in (arb(1) / 2, -arb(1) / 2):
        z = acb(sgn, g0f)                       # exponent s + i gamma0
        c = acb(a) * z
        s2 = 2 * (c / 2).sinh() / c
        # symmetrise the +-d shifts -> cosh(z d)
        pole += acb(a) ** 2 * (z * acb(d)).cosh() * (s2 ** (2 * m))

    logpi = -acb(G0 * arb.pi().log())

    # ---- prime sum --------------------------------------------------------
    A = float(m * a + abs(d)) + 1e-9
    ps = acb(0)
    for n, p in _w.prime_powers(round(A, 9)):
        u = arb(n).log()
        Gv = (a * (_w.bspline(2 * m, (u - d) / a)
                   + _w.bspline(2 * m, (u + d) / a)) / 2)
        if Gv == 0:
            continue
        # g(log n) + g(-log n) = 2 cos(gamma0 log n) G(log n)   (G even)
        ps += arb(p).log() / arb(n).sqrt() * 2 * (g0f * u).cos() * Gv
    primes = -acb(ps)

    # ---- archimedean ------------------------------------------------------
    # A = g(0) psi(1/4) - sum_n [ Ghat(c_n) - 2 g(0)/c_n ],
    #   Ghat(c) := INT_R g(u) e^{-c|u|} du = 2 Re L_G(c - i gamma0),
    # because only the EVEN part of g survives against e^{-c|u|}:
    #   (g(u)+g(-u))/2 = cos(gamma0 u) G(u),  real and even.
    # That even part has vanishing derivative at 0, so the c^{-2} term of
    # Watson's expansion is absent and the series decays like c^{-3} with no
    # extra subtraction:
    #   |Ghat(c) - 2 g(0)/c| <= 2 max|(cos(g0 u)G)''| / c^3.
    if 2 * K + 2 > 2 * m - 2:
        raise ValueError(f"K={K} needs B_{2*m} in C^{2*K+2}; use m >= {K+2}")
    gd = _ghat_even_derivs(a, d, g0f, m, K)          # ghat^{(2k)}(0), k=0..K
    total = arb(0)
    for n in range(N):
        c = arb(2 * n) + arb(1) / 2
        Ghat = 2 * _G_laplace(acb(c, -g0f), a, d, m).real
        asym = arb(0)
        for k in range(K + 1):
            asym += 2 * gd[k] / c ** (2 * k + 1)
        total += Ghat - asym
    # the subtracted asymptotic terms, summed exactly (k = 0 is the 2 G0/c
    # regulariser already removed by the definition of the series)
    for k in range(1, K + 1):
        total += 2 * gd[k] * _S(2 * k + 1)

    # rigorous tail of the accelerated series
    M = 2 * K + 2
    dm = _dmax_bound(a, g0f, M)
    c0 = arb(2 * (N - 1)) + arb(1) / 2
    tail = 2 * dm * (c0 ** (-(M))) / (2 * M)
    total += arb(0, tail.upper())

    psi_quarter = acb(arb(1) / 4).digamma().real
    arch = acb(G0 * psi_quarter - total)

    tot = pole + logpi + arch + primes
    return {"pole": pole, "logpi": logpi, "arch": arch, "primes": primes,
            "total": tot}


def weil_entry_mod(a, d, gamma0, m: int = 2, N: int = 60000, K: int = 2) -> arb:
    """Real symmetrised Weil entry.  Raises if the imaginary part -- which must
    vanish by the symmetry of the construction -- is certified nonzero."""
    t = F_terms_mod(a, d, gamma0, m, N, K)["total"]
    if not t.imag.contains(arb(0)):
        raise ValueError(f"symmetrised Weil entry is not real: {t}")
    return t.real


def weil_matrix_mod(a, shifts, gamma0, m: int = 2, N: int = 60000, K: int = 2, verbose=False):
    a = arb(a)
    shifts = [arb(t) for t in shifts]
    n = len(shifts)
    cache, Q = {}, [[arb(0)] * n for _ in range(n)]
    for j in range(n):
        for k in range(j, n):
            d = shifts[j] - shifts[k]
            key = round(float(d), 12)
            if key not in cache:
                cache[key] = weil_entry_mod(a, d, gamma0, m, N, K)
                if verbose:
                    print(f"    d={key:+.4f} -> {cache[key]}", flush=True)
            Q[j][k] = Q[k][j] = cache[key]
    return Q
