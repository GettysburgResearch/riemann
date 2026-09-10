"""E3 - adversarial minimisation of the Weil explicit-formula quadratic form.

No zeta evaluator and no zero table enters the acceptance path: the form is
built from Lambda(n) below an explicit cutoff plus Gamma-function integrals.
(e3_validate.py cross-checks against zeros; that file is not an acceptance path.)

Test functions. Let Lam_k be the hat of half-width d centred at u_k = k d, and
f = sum_{k=1..N} c_k Lam_k, supported in [0, A], A = (N+1) d. Put

    g = f * f~   (even, supported in [-A, A])
    h(r) = |int f(u) e^{i r u} du|^2 >= 0   for real r.

Then g(v) = d sum_m a_m B(v/d - m), a_m = sum_{j-k=m} c_j c_k, with B the
autocorrelation of the unit triangle (a cubic B-spline).

Weil's explicit formula (validated in e3_validate.py):

    sum_rho h(gamma_rho)
        =  2 h(i/2)  -  g(0) log(pi)
           + int_0^inf [ g(0) e^{-2v}/v - K(v) g(v) ] dv
           - 2 sum_{n>=2} Lambda(n) n^{-1/2} g(log n),
    K(v) = 2 e^{-v/2} / (1 - e^{-2v}),   2 h(i/2) = 4 int_0^inf g(v) cosh(v/2) dv.

Under RH every gamma_rho is real and h >= 0 there, so the left side is >= 0. The
right side is a quadratic form in c depending on (j,k) only through |j-k|: the
matrix M is symmetric TOEPLITZ, M_jk = tau(|j-k|).

    A CERTIFIED c^T M c < 0 (or a certified negative LDL^T pivot) proves that
    some zero lies off the critical line: RH IS FALSE.

A certified LDL^T with all pivots positive proves M is positive definite, i.e.
no test function in the family violates Weil positivity.

Rigour notes. Arb's integrator requires a HOLOMORPHIC integrand, and B is only
piecewise polynomial, so every integral is split at the knots of E_m and each
piece uses that piece's polynomial branch written without abs() or .real. The
1/v singularity of the archimedean integrand is cut at EPS_CUT with an explicit
remainder bound.
"""

import argparse
import json
import time

from flint import acb, arb, ctx

import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from common import ball, certified_negative, set_prec, write_json  # noqa: E402

EPS_CUT = arb(2) ** -400


# ------------------------------------------------------------------ von Mangoldt


def mangoldt_upto(limit):
    """[(n, Lambda(n))] for 2 <= n <= limit, via a smallest-prime-factor sieve."""
    limit = int(limit)
    if limit < 2:
        return []
    spf = list(range(limit + 1))
    i = 2
    while i * i <= limit:
        if spf[i] == i:
            for j in range(i * i, limit + 1, i):
                if spf[j] == j:
                    spf[j] = i
        i += 1
    out = []
    for n in range(2, limit + 1):
        p = spf[n]
        m = n
        while m % p == 0:
            m //= p
        if m == 1:                     # n is a prime power p^k
            out.append((n, p))         # store the PRIME; Lambda(n) = log p
    return out


# ------------------------------------------------------- B-spline, branch-safe


def _Bbranch(w, br):
    """One ANALYTIC branch of B as a polynomial in w (no abs, no .real).

    c+ : 2/3 - w^2 + w^3/2   on [0, 1]      r+ : (2 - w)^3 / 6   on [1, 2]
    c- : 2/3 - w^2 - w^3/2   on [-1, 0]     r- : (2 + w)^3 / 6   on [-2, -1]
    z  : 0                                   on |w| >= 2
    """
    if br == "z":
        return 0 * w
    if br == "c+":
        return 2 * one_like(w) / 3 - w * w + w * w * w / 2
    if br == "c-":
        return 2 * one_like(w) / 3 - w * w - w * w * w / 2
    if br == "r+":
        return (2 - w) ** 3 / 6
    return (2 + w) ** 3 / 6


def one_like(w):
    return acb(1) if isinstance(w, acb) else arb(1)


def _branch_at(wmid):
    """The single branch valid on a subinterval whose midpoint maps to wmid."""
    if wmid >= 2 or wmid <= -2:
        return "z"
    if wmid >= 1:
        return "r+"
    if wmid >= 0:
        return "c+"
    if wmid >= -1:
        return "c-"
    return "r-"


def Bspline(w):
    """Ball-safe B for point evaluation: hull over every branch the ball meets."""
    lo, hi = float(arb(w).lower()), float(arb(w).upper())
    brs = []
    if hi >= 1 and lo <= 2:
        brs.append("r+")
    if hi >= 0 and lo <= 1:
        brs.append("c+")
    if hi >= -1 and lo <= 0:
        brs.append("c-")
    if hi >= -2 and lo <= -1:
        brs.append("r-")
    if hi >= 2 or lo <= -2:
        brs.append("z")
    if not brs:
        return arb(0)
    vals = [_Bbranch(w, b) for b in brs]
    if len(vals) == 1:
        return vals[0]
    los = min(float(arb(v).lower()) for v in vals)
    his = max(float(arb(v).upper()) for v in vals)
    return (arb(los) + arb(his)) / 2 + arb(0, 1) * (arb(his) - arb(los)) / 2


def E_even(m, d, v):
    """E_m(v) = d [B(v/d - m) + B(v/d + m)] for m >= 1;  d B(v/d) for m = 0."""
    if m == 0:
        return d * Bspline(v / d)
    return d * (Bspline(v / d - m) + Bspline(v / d + m))


def E_analytic(m, d, v, br_minus, br_plus):
    """E_m on one subinterval as a HOLOMORPHIC expression (v complex allowed)."""
    if m == 0:
        return d * _Bbranch(v / d, br_plus)
    return d * (_Bbranch(v / d - m, br_minus) + _Bbranch(v / d + m, br_plus))


def knots(m, d, lo, hi):
    """Breakpoints of E_m inside [lo, hi], so each piece is a polynomial."""
    ks = {arb(lo), arb(hi)}
    centres = (-m, m) if m else (0,)
    for c in centres:
        for j in (-2, -1, 0, 1, 2):
            k = arb(d) * (c + j)
            if bool(k > arb(lo)) and bool(k < arb(hi)):
                ks.add(k)
    return sorted(ks, key=lambda x: float(arb(x).mid()))


def piecewise(m, d, lo, hi, kernel):
    """int_lo^hi kernel(v) E_m(v) dv, split at knots; kernel must be holomorphic."""
    ks = knots(m, d, lo, hi)
    total = arb(0)
    for a, b in zip(ks, ks[1:]):
        if not bool(b > a):
            continue
        vm = (float(arb(a).mid()) + float(arb(b).mid())) / 2
        w = vm / float(d)
        bp = _branch_at(w + m) if m else _branch_at(w)
        bm = _branch_at(w - m) if m else "z"
        if bp == "z" and (bm == "z" or m == 0):
            continue

        def f(v, _, _bm=bm, _bp=bp):
            return kernel(v) * E_analytic(m, acb(d), v, _bm, _bp)

        total += acb.integral(f, a, b).real
    return total


def Kfun(v):
    return 2 * (-v / 2).exp() / (1 - (-2 * v).exp())


# ------------------------------------------------------- the Weil functional


def weil_functional(m, d, primes, prec):
    """W[E_m] as an arb ball."""
    ctx.prec = prec
    d = arb(d)
    A = float(d * (abs(m) + 2))
    E0 = E_even(m, d, arb(0))

    pole = 4 * piecewise(m, d, 0.0, A, lambda v: (v / 2).cosh())
    logpi = -E0 * arb.pi().log()

    if not bool(E0 != 0):
        # E vanishes at 0 (order >= 3 there), so K*E -> 0; start past the pole
        # of K and bound the cut analytically:  |K E| <= v^2/(3 d^2) on [0,EPS].
        arch = -piecewise(m, d, float(EPS_CUT), A, Kfun)
        arch += arb(0, 1) * EPS_CUT**3 / (3 * d * d)
    else:
        # combined regular integrand on [EPS, A], split at knots of E
        ks = knots(m, d, float(EPS_CUT), A)
        acc = arb(0)
        for a, b in zip(ks, ks[1:]):
            if not bool(b > a):
                continue
            vm = (float(arb(a).mid()) + float(arb(b).mid())) / 2
            w = vm / float(d)
            bp = _branch_at(w + m) if m else _branch_at(w)
            bm = _branch_at(w - m) if m else "z"

            def f(v, _, _bm=bm, _bp=bp):
                K = Kfun(v)
                return acb(E0) * ((-2 * v).exp() / v - K) + K * (
                    acb(E0) - E_analytic(m, acb(d), v, _bm, _bp)
                )

            acc += acb.integral(f, a, b).real

        def f_tail(v, _):
            return acb(E0) * (-2 * v).exp() / v

        tail = acb.integral(f_tail, A, A + 400).real
        cutb = EPS_CUT * (3 * abs(E0) + 4 * EPS_CUT / d)
        arch = acc + tail + arb(0, 1) * cutb + arb(0, 1e-300)

    psum = arb(0)
    for n, p in primes:
        v = arb(n).log()
        if bool(v > arb(A)):
            continue
        # von Mangoldt weight is Lambda(n) = log p, NOT p.
        psum += arb(p).log() * E_even(m, d, v) / arb(n).sqrt()

    return pole + logpi + arch - 2 * psum


def build_tau(N, d, prec, verbose=False):
    """tau(0) = W[E_0]; tau(m) = W[E_m]/2 for m >= 1."""
    A = float(d) * (N + 1)
    limit = int(min(2.718281828459045 ** (A + 2 * float(d)), 8e7)) + 10
    primes = mangoldt_upto(limit)
    taus = []
    for m in range(N):
        W = weil_functional(m, d, primes, prec)
        taus.append(W if m == 0 else W / 2)
        if verbose:
            print(f"  tau({m}) = {taus[-1].str(10)}", flush=True)
    return taus, limit, len(primes)


# ------------------------------------------------------------ certified LDL^T


def certified_ldlt(taus, N):
    M = [[taus[abs(j - k)] for k in range(N)] for j in range(N)]
    piv = []
    for i in range(N):
        p = M[i][i]
        if certified_negative(p):
            return "CERTIFIED_NEGATIVE_PIVOT", piv + [p], i
        if not bool(p > 0):
            return "inconclusive", piv + [p], i
        piv.append(p)
        for j in range(i + 1, N):
            fac = M[j][i] / p
            if bool(fac == 0):
                continue
            for k in range(i, N):
                M[j][k] = M[j][k] - fac * M[i][k]
    return "positive_definite", piv, None


def rayleigh(taus, N, c):
    acc = arb(0)
    for j in range(N):
        for k in range(N):
            acc += arb(c[j]) * arb(c[k]) * taus[abs(j - k)]
    return acc


def adversarial_vector(taus, N):
    import numpy as np

    t = [float(arb(x).mid()) for x in taus]
    M = np.array([[t[abs(j - k)] for k in range(N)] for j in range(N)])
    w, V = np.linalg.eigh(M)
    return w, V[:, 0]


def run(N, d, prec, verbose):
    set_prec(prec)
    t0 = time.time()
    taus, limit, npp = build_tau(N, d, prec, verbose)
    status, piv, fail_at = certified_ldlt(taus, N)
    w, v = adversarial_vector(taus, N)
    ray = rayleigh(taus, N, v)
    return {
        "N": N,
        "delta": d,
        "A_support": d * (N + 1),
        "prime_cutoff": limit,
        "prime_powers_used": npp,
        "prec_bits": prec,
        "elapsed_s": round(time.time() - t0, 1),
        "tau": [ball(x) for x in taus],
        "ldlt_status": status,
        "ldlt_failed_at": fail_at,
        "min_pivot": ball(min(piv, key=lambda p: float(arb(p).lower()))) if piv else None,
        "float_eigenvalues_min5": [float(x) for x in w[:5]],
        "adversarial_rayleigh": ball(ray),
        "adversarial_rayleigh_certified_negative": certified_negative(ray),
        "RH_REFUTED": status == "CERTIFIED_NEGATIVE_PIVOT" or certified_negative(ray),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=48)
    ap.add_argument("--delta", type=float, default=0.25)
    ap.add_argument("--prec", type=int, default=300)
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    res = run(a.N, a.delta, a.prec, a.verbose)
    write_json(a.out, res)
    print(json.dumps({k: val for k, val in res.items() if k != "tau"}, indent=1)[:2500])


if __name__ == "__main__":
    main()
