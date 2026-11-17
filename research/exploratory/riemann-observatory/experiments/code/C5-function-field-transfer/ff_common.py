"""Common routines for campaign C5-function-field-transfer (Riemann Observatory).

Objects (function-field side, all exact or Arb-rigorous):

  q      : prime power (only the integer q enters; no field arithmetic needed here)
  h(x)   : monic integer "real Weil-type" polynomial of degree g, h(x) = prod_i (x - x_i)
  P(T)   : prod_i (1 - x_i T + q T^2) = T^g h(1/T + q T)     (integer coefficients, P(0)=1)
           P satisfies the curve functional equation P(T) = q^g T^{2g} P(1/(qT)).
  alpha  : reciprocal roots of P, i.e. roots of R(T) = T^{2g} P(1/T); x_i = alpha + q/alpha
  s_k    : sum_i alpha_i^k  (k >= 1), integers (Newton identities), s_0 = 2g
  N_k    : q^k + 1 - s_k  (would be #C(F_{q^k}) if P came from a curve C)
  B_d    : (1/d) sum_{e|d} mu(d/e) N_e  (would be the number of closed points of degree d)
  Z(T)   : P(T)/((1-T)(1-qT)) = prod_{d>=1} (1-T^d)^{-B_d}   (B_d in Z automatically)

RH for P  <=>  |alpha_i| = sqrt(q) for all i  <=>  all x_i real with |x_i| <= 2 sqrt(q).

Normalized power sums t_k = q^{-k/2} s_k; Toeplitz matrix T_N = (t_{|m-n|})_{0<=m,n<N}.
THEOREM (report C5-T2): RH <=> T_N >= 0 for all N <=> |t_k| <= 2g for all k.

Library versions are recorded by the drivers.
"""
from fractions import Fraction
import math
import flint
import sympy

flint.ctx.prec = 256


# ---------------------------------------------------------------- polynomials
def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return out


def P_from_h(hcoef, q):
    """hcoef: integer list, ascending, monic of degree g (hcoef[g] == 1).
    Returns ascending integer coefficients of P(T) = T^g h(1/T + qT), degree 2g."""
    g = len(hcoef) - 1
    assert hcoef[-1] == 1
    # y = (1 + q T^2)/T ; T^g h(y) = sum_k c_k (1+qT^2)^k T^{g-k}
    P = [0] * (2 * g + 1)
    base = [1, 0, q]  # 1 + q T^2
    powk = [1]
    for k in range(g + 1):
        if k > 0:
            powk = poly_mul(powk, base)
        ck = hcoef[k]
        if ck:
            for i, c in enumerate(powk):
                P[i + g - k] += ck * c
    return P


def power_sums(P, kmax):
    """Newton identities for reciprocal roots alpha of P(T)=prod(1-alpha T) = 1 + e1' T + ...
    P ascending, P[0]=1. Returns [s_0, s_1, ..., s_kmax] exact integers, s_0 = deg P."""
    n = len(P) - 1
    # P(T) = sum_j p_j T^j with p_j = (-1)^j e_j(alpha)
    s = [n]
    for k in range(1, kmax + 1):
        # s_k + p_1 s_{k-1} + ... + p_{k-1} s_1 + k p_k = 0  (p_j = 0 for j > n)
        acc = 0
        for j in range(1, min(k - 1, n) + 1):
            acc += P[j] * s[k - j]
        if k <= n:
            acc += k * P[k]
        s.append(-acc)
    return s


def mobius(n):
    res, m, p = 1, n, 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0:
                return 0
            res = -res
        p += 1
    if m > 1:
        res = -res
    return res


def divisors(n):
    small, large = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            small.append(i)
            if i * i != n:
                large.append(n // i)
        i += 1
    return small + large[::-1]


def place_counts(P, q, dmax):
    s = power_sums(P, dmax)
    N = [None] + [q ** k + 1 - s[k] for k in range(1, dmax + 1)]
    B = [None]
    for d in range(1, dmax + 1):
        tot = sum(mobius(d // e) * N[e] for e in divisors(d))
        assert tot % d == 0, ("non-integral place count", d)
        B.append(tot // d)
    return s, N, B


# ---------------------------------------------------------------- RH decision (exact)
def rh_exact(hcoef, q):
    """Exact decision via Sturm sequences (sympy): RH <=> every root x of h is real and x^2 <= 4q.
    For each squarefree factor F of h, K(u) = F(sqrt u) F(-sqrt u) = +-prod_i (u - x_i^2) is an
    integer polynomial; a root x_i is real with x_i^2 > 4q iff u_i = x_i^2 is a real root of K in
    (4q, oo) (non-real x_i give non-real u_i or u_i < 0).  Returns (rh, n_real, n_outside),
    counts with multiplicity."""
    x, u = sympy.symbols('x u')
    h = sympy.Poly(list(reversed(hcoef)), x, domain='ZZ')
    g = h.degree()
    nreal = 0
    nout = 0
    for fac, mult in h.sqf_list()[1]:
        nreal += fac.count_roots() * mult
        e = fac.as_expr()
        K = sympy.Poly(sympy.expand(e.subs(x, sympy.sqrt(u)) * e.subs(x, -sympy.sqrt(u))), u, domain='ZZ')
        for kf, km in K.sqf_list()[1]:
            c = kf.count_roots(4 * q, None)          # closed interval [4q, oo)
            if kf.eval(4 * q) == 0:
                c -= 1
            nout += c * km * mult
    return (nreal == g and nout == 0), nreal, nout


def alpha_balls(P):
    """Rigorous enclosures (Arb) of the reciprocal roots alpha of P: roots of R(T)=T^{2g}P(1/T)."""
    R = flint.fmpz_poly(list(reversed(P)))  # ascending coefficients of R
    out = []
    for z, m in R.complex_roots():
        out.extend([z] * m)
    return out


def max_modulus_upper(P):
    """Rigorous upper bound (float, rounded up via Arb) for A = max |alpha_i|, and the balls."""
    balls = alpha_balls(P)
    up = max(float(abs(z).upper()) for z in balls) if balls else 0.0
    # make float upward-safe: add relative epsilon
    return up * (1 + 1e-12) + 1e-300, balls


def positivity_all_degrees(P, q, g, dcap=4000):
    """Decide B_d >= 0 for all d >= 1.
    Returns dict(status in {'positive_all_d','negative_at_d','undecided_boundary','undecided_cap'},
                 D0, first_negative_d, min_B (over checked range))."""
    A_up, balls = max_modulus_upper(P)
    # exact check up to D0, analytic tail beyond D0 (requires A_up < q)
    if A_up >= q:
        # either A > q (then some B_d < 0 exists by Lemma C5-L1) or boundary |alpha| = q.
        s, N, B = place_counts(P, q, min(dcap, 400))
        neg = [d for d in range(1, len(B)) if B[d] < 0]
        if neg:
            return dict(status='negative_at_d', first_negative_d=neg[0], D0=None, A_up=A_up)
        return dict(status='undecided_boundary', first_negative_d=None, D0=None, A_up=A_up)
    # tail bound: for d >= D0, B_d >= (1/d)[ q^d - 2g A^d - 1 - (d/2)(2g+2) q^{d/2} ] > 0 if
    #   (i) 2g (A/q)^d <= 1/2  and (ii) q^{d/2} >= 2(2g+2) d/2 * 1 + 2 ... we use the sufficient
    #   condition  q^d/2 > 1 + d (g+1) q^{d/2}, i.e. f(d) := q^{d/2} - 2(g+1) d - 2 q^{-d/2} > 0,
    #   f increasing once q^{d/2} ln(q)/2 >= 2(g+1).
    lnq = math.log(q)
    r = A_up / q
    d1 = 1
    while 2 * g * r ** d1 > 0.5:
        d1 += 1
        if d1 > dcap:
            return dict(status='undecided_cap', first_negative_d=None, D0=None, A_up=A_up)
    d2 = 1
    while q ** (d2 / 2) * lnq / 2 < 2 * (g + 1):
        d2 += 1
    d3 = 1
    while q ** (d3 / 2) - 2 * (g + 1) * d3 - 2 <= 0:
        d3 += 1
    D0 = max(d1, d2, d3)
    # verify the three conditions at D0 in exact/Arb arithmetic (guard against float slop)
    Aa = flint.arb(A_up)
    assert (2 * g * (Aa / q) ** D0 <= flint.arb(1) / 2)
    assert (flint.arb(q) ** (flint.arb(D0) / 2) * flint.arb(q).log() / 2 >= 2 * (g + 1))
    assert (flint.arb(q) ** (flint.arb(D0) / 2) - 2 * (g + 1) * D0 - 2 > 0)
    s, N, B = place_counts(P, q, D0)
    neg = [d for d in range(1, D0 + 1) if B[d] < 0]
    if neg:
        return dict(status='negative_at_d', first_negative_d=neg[0], D0=D0, A_up=A_up)
    return dict(status='positive_all_d', first_negative_d=None, D0=D0, A_up=A_up,
                minB=min(B[1:]))


def weil_bound_first_violation(P, q, g, kmax=4000):
    """Smallest k with |s_k| > 2g q^{k/2} (exact: s_k^2 > 4 g^2 q^k), or None up to kmax."""
    s = power_sums(P, kmax)
    for k in range(1, kmax + 1):
        if s[k] * s[k] > 4 * g * g * q ** k:
            return k
    return None


def toeplitz_negative_witness(P, q, g, Nmax=200):
    """Find the smallest N <= Nmax such that T_N = (t_{|m-n|}) has a certified negative direction.
    Candidate vector from floating-point eigen-decomposition, rounded to rationals, and the value
    v^T T_N v evaluated in Arb (t_k = s_k q^{-k/2} as Arb balls).  Returns (N, upper bound of the
    certified negative value) or (None, None)."""
    import numpy as np
    s = power_sums(P, Nmax)
    qa = flint.arb(q)
    tk_arb = [flint.arb(s[k]) / qa ** (flint.arb(k) / 2) for k in range(Nmax)]
    tk_f = [float(s[k]) / q ** (k / 2) for k in range(Nmax)]
    for N in range(2, Nmax + 1):
        T = np.array([[tk_f[abs(m - n)] for n in range(N)] for m in range(N)])
        w, V = np.linalg.eigh(T)
        if w[0] >= -1e-9 * max(1.0, abs(w).max()):
            continue
        v = V[:, 0]
        v = v / np.abs(v).max()
        vr = [Fraction(round(x * 10 ** 12), 10 ** 12) for x in v]
        val = flint.arb(0)
        for m in range(N):
            if vr[m] == 0:
                continue
            for n in range(N):
                if vr[n] == 0:
                    continue
                val += flint.arb(vr[m].numerator) / vr[m].denominator * \
                    (flint.arb(vr[n].numerator) / vr[n].denominator) * tk_arb[abs(m - n)]
        if val < 0:
            return N, float(val.upper())
    return None, None


def h_from_P(P, q):
    """Inverse of P_from_h: P(T) = sum_k c_k T^k (1+qT^2)^{g-k}; coefficient of T^j (j<=g) is
    sum_{k<=j, k=j mod 2} c_k binom(g-k,(j-k)/2) q^{(j-k)/2}, triangular with unit diagonal.
    Returns h ascending (monic).  Asserts the functional equation and exact reconstruction."""
    n = len(P) - 1
    assert n % 2 == 0
    g = n // 2
    c = []
    for j in range(g + 1):
        acc = P[j]
        for k in range(j):
            if (j - k) % 2 == 0:
                acc -= c[k] * math.comb(g - k, (j - k) // 2) * q ** ((j - k) // 2)
        c.append(acc)
    hcoef = list(reversed(c))
    assert P_from_h(hcoef, q) == list(P), "P does not satisfy the functional equation"
    return hcoef
