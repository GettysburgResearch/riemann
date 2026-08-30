"""Exact stdlib-only algebra core for the 2026-08-30 two-programme pass.

Arithmetic class: EXACT_RATIONAL throughout. No floating point anywhere in
this module. Polynomials are lists of Fraction, low degree first, with no
trailing zeros (the zero polynomial is []).

Provides:
  - polynomial ring ops over Q;
  - Berlekamp-Massey over Q (minimal linear recurrence of a sequence);
  - exact rational-function reconstruction of a generating series;
  - Newton identities: power sums <-> elementary symmetric functions;
  - power-sum calculus for Adams / symmetric / exterior / tensor / dual
    operations on a "local object" given only by exact trace data;
  - Sturm sequences: exact real-root counting on rational intervals;
  - Faddeev-LeVerrier characteristic polynomial of an integer matrix.

RH status: nothing in this file asserts anything about RH. rh_established=false.
"""

from fractions import Fraction
from typing import List, Sequence, Tuple, Optional

Poly = List[Fraction]


def F(x) -> Fraction:
    return x if isinstance(x, Fraction) else Fraction(x)


def poly_trim(p: Sequence) -> Poly:
    p = [F(c) for c in p]
    while p and p[-1] == 0:
        p.pop()
    return p


def poly_add(a: Sequence, b: Sequence) -> Poly:
    n = max(len(a), len(b))
    return poly_trim([ (F(a[i]) if i < len(a) else Fraction(0))
                     + (F(b[i]) if i < len(b) else Fraction(0)) for i in range(n) ])


def poly_scale(a: Sequence, c) -> Poly:
    c = F(c)
    return poly_trim([F(x) * c for x in a])


def poly_mul(a: Sequence, b: Sequence) -> Poly:
    if not a or not b:
        return []
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x == 0:
            continue
        fx = F(x)
        for j, y in enumerate(b):
            if y == 0:
                continue
            out[i + j] += fx * F(y)
    return poly_trim(out)


def poly_divmod(a: Sequence, b: Sequence) -> Tuple[Poly, Poly]:
    """Exact division with remainder in Q[T]."""
    a = poly_trim(a); b = poly_trim(b)
    if not b:
        raise ZeroDivisionError("poly_divmod by zero polynomial")
    q = [Fraction(0)] * max(0, len(a) - len(b) + 1)
    r = list(a)
    while len(r) >= len(b) and poly_trim(r):
        r = poly_trim(r)
        if len(r) < len(b):
            break
        c = r[-1] / b[-1]
        d = len(r) - len(b)
        q[d] += c
        for i, bc in enumerate(b):
            r[d + i] -= c * bc
        r = poly_trim(r) or [Fraction(0)]
        if r == [Fraction(0)]:
            r = []
            break
    return poly_trim(q), poly_trim(r)


def poly_eval(p: Sequence, x) -> Fraction:
    x = F(x)
    acc = Fraction(0)
    for c in reversed(list(p)):
        acc = acc * x + F(c)
    return acc


def poly_deriv(p: Sequence) -> Poly:
    return poly_trim([F(c) * i for i, c in enumerate(p)][1:])


def poly_monic(p: Sequence) -> Poly:
    p = poly_trim(p)
    if not p:
        return p
    lead = p[-1]
    return [c / lead for c in p]


def poly_content_primitive(p: Sequence) -> Tuple[Fraction, List[int]]:
    """Write p = content * primitive with primitive integer coefficients, gcd 1,
    positive leading coefficient."""
    from math import gcd
    p = poly_trim(p)
    if not p:
        return Fraction(0), []
    from functools import reduce
    L = reduce(lambda a, b: a * b // gcd(a, b), [F(c).denominator for c in p], 1)
    ints = [int(F(c) * L) for c in p]
    g = reduce(gcd, [abs(c) for c in ints if c != 0])
    ints = [c // g for c in ints]
    sign = 1 if ints[-1] > 0 else -1
    ints = [sign * c for c in ints]
    return Fraction(sign * g, L), ints


def is_integer_poly(p: Sequence) -> bool:
    return all(F(c).denominator == 1 for c in p)


# ---------------------------------------------------------------------------
# Berlekamp-Massey over Q
# ---------------------------------------------------------------------------

def berlekamp_massey(seq: Sequence) -> Poly:
    """Minimal connection polynomial C(T) = 1 + c1 T + ... + cL T^L over Q with
    s_n = -(c1 s_{n-1} + ... + cL s_{n-L}) for all n >= L.  Returns C as a
    low-first coefficient list; the minimal recurrence order is len(C)-1.
    Exact over Q; deterministic."""
    s = [F(x) for x in seq]
    C = [Fraction(1)]
    B = [Fraction(1)]
    L, m, b = 0, 1, Fraction(1)
    for n in range(len(s)):
        d = s[n]
        for i in range(1, L + 1):
            if i < len(C):
                d += C[i] * s[n - i]
        if d == 0:
            m += 1
        elif 2 * L <= n:
            T = list(C)
            coef = d / b
            # C(T) -= coef * T^m * B(T)
            need = len(B) + m
            if len(C) < need:
                C = C + [Fraction(0)] * (need - len(C))
            for i, bc in enumerate(B):
                C[i + m] -= coef * bc
            L = n + 1 - L
            B = T
            b = d
            m = 1
        else:
            coef = d / b
            need = len(B) + m
            if len(C) < need:
                C = C + [Fraction(0)] * (need - len(C))
            for i, bc in enumerate(B):
                C[i + m] -= coef * bc
            m += 1
    return poly_trim(C) or [Fraction(1)]


def minimal_rational_form(series: Sequence, check_all: bool = True
                          ) -> Optional[Tuple[Poly, Poly]]:
    """Given series coefficients a_0..a_N of f(T) = sum a_k T^k, return (P, Q)
    with f = P/Q exactly on the given window, Q(0)=1, Q the Berlekamp-Massey
    minimal denominator.  IMPROPER numerators (deg P >= deg Q) are supported:
    the coefficients of P = (series * Q) are exact for every index < window
    length, so P is read off directly and certified by re-expansion; this is
    required e.g. for trace generating series -T Q'(T)/Q(T), whose numerator
    degree equals deg Q (adversarial-review fix, 2026-08-30).  Returns None
    when the window cannot certify: the recurrence needs 2L+2 <= N+1 AND the
    read-off numerator must be followed by an observed zero tail of length
    >= 2 inside the window."""
    a = [F(x) for x in series]
    Q = berlekamp_massey(a)
    L = len(Q) - 1
    if 2 * L + 2 > len(a):
        return None
    prod = poly_mul(a, Q)
    P = poly_trim(prod[: len(a)])
    if len(P) > len(a) - 2:
        return None            # no observed zero tail: cannot certify
    if not P:
        P = []
    if check_all:
        recon = series_of_rational(P if P else [Fraction(0)], Q, len(a))
        if recon != a[: len(recon)] or len(recon) < len(a):
            return None
    return P, Q


def series_of_rational(P: Sequence, Q: Sequence, n: int) -> List[Fraction]:
    """First n coefficients of P(T)/Q(T) with Q(0) != 0."""
    P = [F(x) for x in P]; Q = [F(x) for x in Q]
    if not Q or Q[0] == 0:
        raise ZeroDivisionError("Q(0)=0 in series_of_rational")
    out = []
    q0 = Q[0]
    for k in range(n):
        c = P[k] if k < len(P) else Fraction(0)
        for j in range(1, min(k, len(Q) - 1) + 1):
            c -= Q[j] * out[k - j]
        out.append(c / q0)
    return out


# ---------------------------------------------------------------------------
# Newton identities
# ---------------------------------------------------------------------------

def elementary_from_power_sums(p: Sequence, d: int) -> List[Fraction]:
    """Given power sums p_1..p_d (p[0] is p_1), return e_1..e_d via Newton's
    identities: k e_k = sum_{i=1}^{k} (-1)^{i-1} e_{k-i} p_i, with e_0 = 1."""
    p = [F(x) for x in p]
    e = [Fraction(1)]
    for k in range(1, d + 1):
        acc = Fraction(0)
        for i in range(1, k + 1):
            acc += (-1) ** (i - 1) * e[k - i] * p[i - 1]
        e.append(acc / k)
    return e[1:]


def power_sums_from_elementary(e: Sequence, n: int) -> List[Fraction]:
    """Given e_1..e_d (rest zero), return p_1..p_n."""
    e = [F(x) for x in e]
    d = len(e)
    p = []
    for k in range(1, n + 1):
        acc = Fraction(0)
        for i in range(1, min(k, d) + 1):
            acc += (-1) ** (i - 1) * e[i - 1] * (p[k - i - 1] if k - i >= 1 else k)
        # note: when i == k the term is (-1)^{k-1} e_k * k handled via p_0 := k
        p.append(acc)
    return p


def charpoly_from_power_sums(p: Sequence, d: int) -> Poly:
    """det(T I - A) as a monic degree-d polynomial (low-first) from power sums
    p_1..p_d of A."""
    e = elementary_from_power_sums(p, d)
    # char poly: T^d - e1 T^{d-1} + e2 T^{d-2} - ...
    coeffs = [Fraction(0)] * (d + 1)
    coeffs[d] = Fraction(1)
    for i, ei in enumerate(e, start=1):
        coeffs[d - i] = (-1) ** i * ei
    return coeffs


def satake_poly_from_power_sums(p: Sequence, d: int) -> Poly:
    """det(1 - A T) (low-first, degree d, constant term 1) from power sums."""
    e = elementary_from_power_sums(p, d)
    out = [Fraction(1)]
    for i, ei in enumerate(e, start=1):
        out.append((-1) ** i * ei)
    return poly_trim(out) if out[-1] != 0 else out


def power_sums_from_satake(satake: Sequence, n: int) -> List[Fraction]:
    """Power sums p_1..p_n of A given det(1 - A T) = satake (constant term 1).
    Uses -T d/dT log det(1 - A T) = sum_{k>=1} p_k T^k."""
    s = [F(x) for x in satake]
    assert s and s[0] == 1, "satake polynomial must have constant term 1"
    dlog_num = poly_scale(poly_deriv(s), -1)  # -(d/dT) det
    # p-series: T * dlog_num / s  -> coefficient of T^k is p_k
    ser = series_of_rational(dlog_num, s, n)
    return [ser[k] for k in range(n)]  # ser[k] = p_{k+1}


def coefficient_sequence_from_satake(satake: Sequence, n: int) -> List[Fraction]:
    """a_0=1, a_1, ..., a_{n-1} of 1/det(1 - A T): complete homogeneous h_k."""
    return series_of_rational([Fraction(1)], satake, n)


# ---------------------------------------------------------------------------
# Power-sum calculus: local-object operations without eigenvalues
# ---------------------------------------------------------------------------

def op_adams(p: Sequence, m: int, n: int) -> List[Fraction]:
    """Power sums of psi^m(A): p_k(psi^m A) = p_{mk}(A). Requires p up to m*n."""
    p = [F(x) for x in p]
    assert len(p) >= m * n, "need p_1..p_{m n} for Adams"
    return [p[m * k - 1] for k in range(1, n + 1)]


def op_direct_sum(pa: Sequence, pb: Sequence, n: int) -> List[Fraction]:
    return [F(pa[k]) + F(pb[k]) for k in range(n)]


def op_tensor(pa: Sequence, pb: Sequence, n: int) -> List[Fraction]:
    return [F(pa[k]) * F(pb[k]) for k in range(n)]


def op_sym2(p: Sequence, n: int) -> List[Fraction]:
    """p_k(Sym^2 A) = (p_k(A)^2 + p_{2k}(A)) / 2. Requires p up to 2n."""
    p = [F(x) for x in p]
    assert len(p) >= 2 * n
    return [(p[k - 1] ** 2 + p[2 * k - 1]) / 2 for k in range(1, n + 1)]


def op_ext2(p: Sequence, n: int) -> List[Fraction]:
    """p_k(Ext^2 A) = (p_k(A)^2 - p_{2k}(A)) / 2."""
    p = [F(x) for x in p]
    assert len(p) >= 2 * n
    return [(p[k - 1] ** 2 - p[2 * k - 1]) / 2 for k in range(1, n + 1)]


def op_sym_k(p: Sequence, m: int, d: int, n: int) -> List[Fraction]:
    """Power sums p_1..p_n of Sym^m(A) for A of rank d, given p_1..p_{m*n}(A).

    Uses p_j(Sym^m A) = h_m(eigenvalues of A^j), and h_m of A^j is computed
    by Newton from the power sums of A^j, which are p_{j*i}(A)."""
    p = [F(x) for x in p]
    out = []
    for j in range(1, n + 1):
        pj = [p[j * i - 1] for i in range(1, m + 1)]  # p_i(A^j), i=1..m
        # h_m from power sums via Newton for complete homogeneous:
        # k h_k = sum_{i=1}^k p_i h_{k-i}
        h = [Fraction(1)]
        for k in range(1, m + 1):
            acc = Fraction(0)
            for i in range(1, k + 1):
                acc += pj[i - 1] * h[k - i]
            h.append(acc / k)
        out.append(h[m])
    return out


def op_ext_k(p: Sequence, m: int, d: int, n: int) -> List[Fraction]:
    """Power sums of Ext^m(A) (rank C(d,m)), analogous via e_m of A^j."""
    p = [F(x) for x in p]
    out = []
    for j in range(1, n + 1):
        pj = [p[j * i - 1] for i in range(1, m + 1)]
        e = elementary_from_power_sums(pj, m)
        out.append(e[m - 1])
    return out


def op_dual_satake(satake: Sequence, det_value: Fraction) -> Poly:
    """det(1 - A^{-1} T) from det(1 - A T) when det A = det_value != 0:
    det(1 - A^{-1} T) = (-T)^d / det(A) * det(1 - A / T) reversed; concretely
    reverse coefficients and normalize constant term to 1."""
    s = poly_trim(satake)
    d = len(s) - 1
    rev = list(reversed(s))
    lead = rev[0]
    if lead == 0:
        raise ValueError("dual undefined: top Satake coefficient vanishes")
    return [c / lead for c in rev]


# ---------------------------------------------------------------------------
# Sturm sequences: exact real-root counting
# ---------------------------------------------------------------------------

def sturm_chain(p: Sequence) -> List[Poly]:
    p0 = poly_trim(p)
    p1 = poly_deriv(p0)
    chain = [p0, p1]
    while poly_trim(chain[-1]):
        _, r = poly_divmod(chain[-2], chain[-1])
        if not r:
            break
        chain.append(poly_scale(r, -1))
    return [c for c in chain if poly_trim(c)]


def _sign_changes(vals: List[Fraction]) -> int:
    signs = [1 if v > 0 else (-1 if v < 0 else 0) for v in vals if v != 0]
    return sum(1 for a, b in zip(signs, signs[1:]) if a != b)


def count_real_roots_in(p: Sequence, a, b) -> int:
    """Number of distinct real roots of p in (a, b], exact (a,b rational)."""
    chain = sturm_chain(p)
    va = [poly_eval(c, a) for c in chain]
    vb = [poly_eval(c, b) for c in chain]
    return _sign_changes(va) - _sign_changes(vb)


def certify_root_above(p: Sequence, bound) -> bool:
    """Exact certificate that p has at least one real root strictly above
    `bound` (rational). Uses a Cauchy bound for the upper end."""
    p = poly_trim(p)
    if not p:
        return False
    lead = abs(p[-1])
    cauchy = 1 + max(abs(c) for c in p[:-1]) / lead if len(p) > 1 else Fraction(1)
    hi = F(bound) + cauchy + 1
    return count_real_roots_in(p, F(bound), hi) > 0


# ---------------------------------------------------------------------------
# Characteristic polynomial of an exact matrix (Faddeev-LeVerrier)
# ---------------------------------------------------------------------------

def charpoly_of_matrix(M: Sequence[Sequence]) -> Poly:
    """Monic char poly det(T I - M), low-first, exact for rational matrices."""
    n = len(M)
    A = [[F(M[i][j]) for j in range(n)] for i in range(n)]
    # Faddeev-LeVerrier
    c = [Fraction(1)]  # will hold c_0=1 leading; we build downward
    Mk = [[Fraction(0)] * n for _ in range(n)]
    for i in range(n):
        Mk[i][i] = Fraction(1)
    coeffs = [Fraction(1)]
    N = [row[:] for row in Mk]
    for k in range(1, n + 1):
        # N = A * (previous N + c_{k-1} I) done stepwise
        AN = [[sum(A[i][t] * N[t][j] for t in range(n)) for j in range(n)]
              for i in range(n)]
        ck = -sum(AN[i][i] for i in range(n)) / k
        coeffs.append(ck)
        for i in range(n):
            AN[i][i] += ck
        N = AN
    # coeffs are [1, c1, ..., cn] for T^n + c1 T^{n-1} + ... + cn
    out = [Fraction(0)] * (n + 1)
    for i, cc in enumerate(coeffs):
        out[n - i] = cc
    return out
