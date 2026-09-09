"""Exact defect factorization for pointwise powers m=2..6 via the PROVED
coefficient formula (T-108500 statement 3):

    c_r = sum_{u<=r} (-1)^{r-u} e_{r-u}(Sym^m(A)) h_u^m ,

then verified two independent ways: (i) symbolic series multiplication
N_m = D_m * sum h_k^m T^k to 2(m+1)+6 terms; (ii) stdlib Fraction
instantiation checks at 12 integer (a,b) pairs (cross-multiplied rational
equality, honest on degeneration loci). Also the Adams relabelling law and
the self-duality identity are re-verified. Writes matrix/defects.json.
No Berlekamp-Massey in the symbolic layer (the formula makes it needless).
"""
import json
import sys
import sympy as sp

sys.path.insert(0, '.')
from core.symbolic_defect import coefficients, sym_power_satake, a, b, T
from core.exact import (F, coefficient_sequence_from_satake,
                        minimal_rational_form)
from fractions import Fraction

out = {"transforms": [], "sympy_version": sp.__version__,
       "construction": "proved coefficient formula (T-108500 st.3)",
       "rh_established": False}

for m in range(2, 7):
    D = sym_power_satake(m)                      # det(1 - Sym^m(A) T)
    # e_k(Sym^m) with sign convention: D = sum (-1)^k e_k T^k
    # (coefficient formula = standalone PROOF.md Theorem 1 statement 3,
    # summarized as item 1 in the claim file T-108500)
    e = [sp.Integer(1)] + [sp.expand((-1) ** k * D.coeff(T, k))
                           for k in range(1, m + 2)]
    h = coefficients(m + 1)
    c = []
    for r in range(m):
        acc = sp.Integer(0)
        for u in range(r + 1):
            acc += (-1) ** (r - u) * e[r - u] * h[u] ** m
        c.append(sp.expand(acc))
    N = sum(ci * T ** i for i, ci in enumerate(c))

    # (i) symbolic verification: D * sum h_k^m T^k == N to enough terms.
    # The head coefficients i < m are DEFINITIONAL (c_r is constructed as
    # (D*S)_r), so the real content is the TAIL VANISHING i >= m — checked
    # exclusively here (adversarial-review fix: the old head comparison was
    # tautological). The coefficient VALUES are pinned independently by the
    # stdlib Berlekamp-Massey instantiation checks (ii) and by X-108500.
    n_terms = 2 * (m + 1) + 6
    hs = coefficients(n_terms)
    S = sum(sp.expand(x ** m) * T ** k for k, x in enumerate(hs))
    prod = sp.expand(D * S)
    ok_sym = all(sp.expand(prod.coeff(T, i)) == 0
                 for i in range(m, n_terms - (m + 2)))
    assert ok_sym, f"symbolic tail-vanishing failed at m={m}"

    # self-duality check: N(T) == b^{m(m-1)/2} T^{m-1} N(1/(b^m T))
    rhs = sp.expand(sp.cancel(b ** (m * (m - 1) // 2) * T ** (m - 1)
                              * N.subs(T, 1 / (b ** m * T))))
    ok_dual = sp.expand(N - rhs) == 0
    assert ok_dual, f"self-duality failed at m={m}"

    # (ii) stdlib instantiation cross-checks
    checks = 0
    for (av, bv) in [(1, 2), (2, 3), (-1, 2), (3, 5), (0, 7), (5, 2),
                     (-2, 11), (4, 7), (1, 1), (2, 1), (-3, 13), (6, 5)]:
        sat = [Fraction(1), Fraction(-av), Fraction(bv)]
        hseq = coefficient_sequence_from_satake(sat, 2 * (m + 1) + 8)
        pq = minimal_rational_form([x ** m for x in hseq])
        assert pq is not None
        P, Q = pq
        Nn = sp.expand(N.subs({a: av, b: bv}))
        Dn = sp.expand(D.subs({a: av, b: bv}))
        Pp = sum(sp.Rational(str(F(x))) * T ** i for i, x in enumerate(P))
        Qp = sum(sp.Rational(str(F(x))) * T ** i for i, x in enumerate(Q))
        assert sp.expand(Nn * Qp - Dn * Pp) == 0, (m, av, bv)
        checks += 1

    lin_ok = sp.cancel(c[1] - (a ** m - h[m])) == 0 if m >= 2 else True
    out["transforms"].append({
        "name": f"pointwise_power_{m}",
        "defect_coefficients": [str(sp.factor(x)) for x in c],
        "defect_degree": m - 1,
        "denominator": f"det(1 - Sym^{m}(A) T)",
        "self_duality_verified": bool(ok_dual),
        "linear_coeff_equals_a^m_minus_h_m": bool(lin_ok),
        "symbolic_series_terms_checked": n_terms - (m + 2),
        "integer_instantiation_checks": checks})
    print(f"m={m}: N deg {m-1}, coeffs {[str(sp.factor(x)) for x in c]}, "
          f"self-dual OK, lin-law {lin_ok}, {checks} integer checks OK",
          flush=True)

# Adams relabelling with exact psi^2 library factor
n = 20
h = coefficients(2 * n)
psi2 = sp.expand(1 - (a * a - 2 * b) * T + b * b * T * T)
S2 = sum(h[2 * k] * T ** k for k in range(n))
prod = sp.expand(psi2 * S2)
okA = all(sp.expand(prod.coeff(T, i) - (1 if i == 0 else (b if i == 1 else 0))) == 0
          for i in range(n - 3))
assert okA
out["transforms"].append({"name": "adams_relabel_2",
                          "identity": "sum h_2k T^k = (1 + bT)/det(1 - psi^2(A) T)",
                          "verified_terms": n - 3})
print("adams2 identity verified", flush=True)

with open("matrix/defects.json", "w") as f:
    json.dump(out, f, indent=1)
print("WROTE matrix/defects.json", flush=True)
