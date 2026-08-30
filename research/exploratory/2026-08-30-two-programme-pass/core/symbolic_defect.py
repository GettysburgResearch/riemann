"""Symbolic defect extraction for transforms of degree-2 local data (#764).

Generic local object: Satake polynomial  D(T) = 1 - a T + b T^2  over the
rational function field Q(a, b)  (a = trace of A_p, b = det A_p; b = p for an
elliptic curve in weight-1 normalization, b = 1 for a unitarized cusp form).
Coefficients h_k = a_{p^k} satisfy h_0 = 1, h_1 = a, h_k = a h_{k-1} - b h_{k-2}.

For a pointwise transform f applied to (h_k), we compute the EXACT minimal
rational form  sum_k f(h_k) T^k = N(T) / D_f(T)  over Q(a,b) by a generic
Berlekamp-Massey with symbolic zero-testing (sympy.cancel — decidable for
rational functions), then factor D_f against the library of functorial
denominators det(1 - Sym^m(A) T) and report the numerator N as the DEFECT.

Everything here is exact symbolic algebra (sympy 1.14.0, recorded in the
provenance lock).  Instantiation cross-checks at integer (a, b) values are run
separately with the stdlib Fraction core so that two independent routes must
agree.  RH is not addressed; rh_established=false.
"""

import sympy as sp

a, b, T = sp.symbols('a b T')


def coefficients(n):
    """h_0..h_{n-1} in Z[a,b]."""
    h = [sp.Integer(1), a]
    while len(h) < n:
        h.append(sp.expand(a * h[-1] - b * h[-2]))
    return h[:n]


def power_sums(n):
    """p_1..p_n (traces of A^k) in Z[a,b]: p_1 = a, p_2 = a^2-2b, Newton."""
    p = [a, sp.expand(a * a - 2 * b)]
    while len(p) < n:
        p.append(sp.expand(a * p[-1] - b * p[-2]))
    return p[:n]


def sym_power_satake(m):
    """det(1 - Sym^m(A) T) in Z[a,b][T], via elementary symmetric functions of
    the weight monomials computed from power sums of Sym^m(A):
    p_j(Sym^m A) = h_m evaluated at (alpha^j, beta^j), i.e. the coefficient
    recursion driven by (p_j, det^j) = (trace A^j, b^j)."""
    d = m + 1                        # rank of Sym^m for GL_2
    ps = power_sums(m * d + 2)
    # p_j(Sym^m A): h_m with (a, b) -> (trace A^j, det A^j) = (ps[j-1], b^j)
    pj = []
    for j in range(1, d + 1):
        tr, dt = ps[j - 1], b ** j
        h0, h1 = sp.Integer(1), tr
        for _ in range(m - 1):
            h0, h1 = h1, sp.expand(tr * h1 - dt * h0)
        pj.append(h1 if m >= 1 else sp.Integer(1))
    # Newton: e_k from p_1..p_d
    e = [sp.Integer(1)]
    for k in range(1, d + 1):
        acc = sp.Integer(0)
        for i in range(1, k + 1):
            acc += (-1) ** (i - 1) * e[k - i] * pj[i - 1]
        e.append(sp.expand(sp.cancel(acc / k)))
    # det(1 - Sym^m(A) T) = sum_k (-1)^k e_k T^k
    return sp.expand(sum((-1) ** k * e[k] * T ** k for k in range(d + 1)))


def bm_symbolic(seq):
    """Berlekamp-Massey over Q(a,b): returns the minimal connection polynomial
    C(T) with C(0)=1 (list of sympy expressions, low-first)."""
    s = [sp.cancel(x) for x in seq]
    C = [sp.Integer(1)]
    B = [sp.Integer(1)]
    L, m, bb = 0, 1, sp.Integer(1)
    for n in range(len(s)):
        d = s[n]
        for i in range(1, L + 1):
            if i < len(C):
                d = d + C[i] * s[n - i]
        d = sp.cancel(sp.together(d))
        if d == 0:
            m += 1
            continue
        coef = sp.cancel(d / bb)
        if 2 * L <= n:
            Told = list(C)
            need = len(B) + m
            if len(C) < need:
                C = C + [sp.Integer(0)] * (need - len(C))
            for i, bc in enumerate(B):
                C[i + m] = sp.cancel(C[i + m] - coef * bc)
            L = n + 1 - L
            B = Told
            bb = d
            m = 1
        else:
            need = len(B) + m
            if len(C) < need:
                C = C + [sp.Integer(0)] * (need - len(C))
            for i, bc in enumerate(B):
                C[i + m] = sp.cancel(C[i + m] - coef * bc)
            m += 1
    while len(C) > 1 and sp.cancel(C[-1]) == 0:
        C.pop()
    return [sp.cancel(c) for c in C]


def rational_form(seq):
    """(N, D) as sympy polynomials in T over Q(a,b) with D(0)=1, certified to
    reproduce the whole window; None if window too short."""
    D = bm_symbolic(seq)
    L = len(D) - 1
    if 2 * L + 2 > len(seq):
        return None
    Dpoly = sp.expand(sum(c * T ** i for i, c in enumerate(D)))
    Spoly = sum(sp.expand(x) * T ** i for i, x in enumerate(seq))
    prod = sp.expand(Spoly * Dpoly)
    N = sp.Integer(0)
    for i in range(max(L, 1)):
        N += prod.coeff(T, i) * T ** i
    N = sp.expand(N)
    # certify on the full window
    check = sp.series(sp.cancel(N / Dpoly), T, 0, len(seq)).removeO()
    for i in range(len(seq)):
        if sp.cancel(check.coeff(T, i) - seq[i]) != 0:
            return None
    return sp.factor(N), sp.factor(Dpoly)


def divide_out(D_f, library):
    """Factor D_f as a product of library denominators times a residual.
    library: list of (name, poly).  Greedy exact division, returns
    (factors: list of names with multiplicity, residual poly)."""
    residual = sp.factor(D_f)
    used = []
    changed = True
    while changed:
        changed = False
        for name, poly in library:
            q = sp.cancel(residual / poly)
            if q.is_polynomial(T):
                num, den = sp.fraction(sp.together(q))
                if sp.cancel(den - 1) == 0:
                    residual = sp.factor(num)
                    used.append(name)
                    changed = True
    return used, residual


def analyze_pointwise_power(m_power, terms=None):
    """Exact defect factorization of  sum_k h_k^{m} T^k  for the generic
    degree-2 local object.  Returns dict with numerator (defect), denominator,
    and its factorization against Sym^j denominators."""
    # denominator degree is at most m+1 (weights alpha^{m-j} beta^j), so a
    # window of 2(m+1)+4 terms certifies.
    n = terms or (2 * (m_power + 1) + 6)
    h = coefficients(n)
    seq = [sp.expand(x ** m_power) for x in h]
    nf = rational_form(seq)
    if nf is None:
        return {"power": m_power, "status": "WINDOW_TOO_SHORT"}
    N, D = nf
    lib = [(f"Sym^{j}", sym_power_satake(j)) for j in range(1, m_power + 1)]
    used, residual = divide_out(D, lib)
    return {"power": m_power, "numerator_defect": sp.expand(N),
            "denominator": D, "denominator_factors": used,
            "denominator_residual": sp.expand(residual),
            "window": n, "status": "OK"}


def analyze_hadamard_pair():
    """sum_k h_k(A) h_k(B) T^k for independent degree-2 objects: expect the
    Cauchy identity  (1 - det A det B T^2) / det(1 - (A tensor B) T)."""
    c, d = sp.symbols('c d')
    n = 14
    hA = coefficients(n)
    hB = [x.subs({a: c, b: d}) for x in coefficients(n)]
    seq = [sp.expand(x * y) for x, y in zip(hA, hB)]
    nf = rational_form(seq)
    if nf is None:
        return {"status": "WINDOW_TOO_SHORT"}
    N, D = nf
    # tensor denominator via power sums p_k(A(x)B) = p_k(A) p_k(B)
    psA = power_sums(10)
    psB = [x.subs({a: c, b: d}) for x in psA]
    pt = [sp.expand(x * y) for x, y in zip(psA, psB)]
    e = [sp.Integer(1)]
    for k in range(1, 5):
        acc = sp.Integer(0)
        for i in range(1, k + 1):
            acc += (-1) ** (i - 1) * e[k - i] * pt[i - 1]
        e.append(sp.expand(sp.cancel(acc / k)))
    tensorD = sp.expand(sum((-1) ** k * e[k] * T ** k for k in range(5)))
    match = sp.cancel(sp.expand(D) - tensorD) == 0
    expectedN = sp.expand(1 - b * d * T ** 2)
    return {"status": "OK", "numerator_defect": sp.expand(N),
            "denominator_is_tensor": bool(match),
            "numerator_is_cauchy": sp.cancel(sp.expand(N) - expectedN) == 0}


def analyze_hankel_minor(shift=1):
    """The 2x2 Hankel-minor transform  g_k = h_k h_{k+2} - h_{k+1}^2
    (shift=1) — Jacobi-Trudi says g_k = s_{(k+1,k+1)}(alpha,beta) = b^{k+1}:
    an EFFECTIVE degree-1 object (twist by det).  Verify exactly."""
    n = 16
    h = coefficients(n + 2)
    g = [sp.expand(h[k] * h[k + 2] - h[k + 1] ** 2) for k in range(n)]
    ok = all(sp.cancel(g[k] - (-1) ** 0 * b ** (k + 1)) == 0 or
             sp.cancel(g[k] + b ** (k + 1)) == 0 for k in range(n))
    # determine the sign exactly
    sign = sp.cancel(g[0] / b)
    return {"status": "OK", "identity": f"h_k h_(k+2) - h_(k+1)^2 = ({sign}) * b^(k+1)",
            "verified_terms": n, "all_match": bool(ok)}


def analyze_adams2():
    """sum_k h_{2k} T^k — even-part/Adams-flavoured relabelling."""
    n = 20
    h = coefficients(2 * n)
    seq = [h[2 * k] for k in range(n)]
    nf = rational_form(seq)
    if nf is None:
        return {"status": "WINDOW_TOO_SHORT"}
    N, D = nf
    lib = [(f"Sym^{j}", sym_power_satake(j)) for j in (1, 2)]
    used, residual = divide_out(D, lib)
    return {"status": "OK", "numerator_defect": sp.expand(N),
            "denominator": D, "denominator_factors": used,
            "denominator_residual": sp.expand(residual)}
