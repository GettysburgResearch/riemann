"""Exact defect factorization for pointwise powers m=2..5 (+ Adams psi library),
with independent integer-instantiation cross-checks. Writes matrix/defects.json."""
import json, sys
import sympy as sp
sys.path.insert(0, '.')
from core.symbolic_defect import (analyze_pointwise_power, coefficients,
                                  sym_power_satake, a, b, T)
from core.exact import (F, coefficient_sequence_from_satake, minimal_rational_form,
                        power_sums_from_satake, satake_poly_from_power_sums, op_sym_k)
from fractions import Fraction

out = {"transforms": [], "sympy_version": sp.__version__, "rh_established": False}

for m in range(2, 6):
    r = analyze_pointwise_power(m)
    assert r["status"] == "OK", (m, r)
    N = sp.expand(r["numerator_defect"])
    res = sp.expand(r["denominator_residual"])
    # coefficient list of the defect
    coeffs = [sp.factor(N.coeff(T, i)) for i in range(sp.degree(N, T) + 1)]
    # analytic prediction: linear coefficient should equal a^m - h_m
    h = coefficients(m + 1)
    lin_pred = sp.expand(a**m - h[m])
    lin_ok = sp.cancel(N.coeff(T, 1) - lin_pred) == 0
    # integer cross-check at 12 instantiations via the stdlib Fraction core
    import itertools
    checks = 0
    for (av, bv) in [(1,2),(2,3),(-1,2),(3,5),(0,7),(5,2),(-2,11),(4,7),(1,1),(2,1),(-3,13),(6,5)]:
        sat = [Fraction(1), Fraction(-av), Fraction(bv)]
        hseq = coefficient_sequence_from_satake(sat, 2*(m+1)+8)
        seq = [x**m for x in hseq]
        pq = minimal_rational_form(seq)
        assert pq is not None, (m, av, bv)
        P, Q = pq
        # symbolic instantiation must match
        # compare as rational functions: N/D == P/Q  <=>  N*Q - D*P == 0.
        # (On degenerate loci, e.g. the trace-zero/supersingular locus a=0,
        # the generic defect cancels against a Sym^m denominator factor and
        # Berlekamp-Massey correctly returns the REDUCED form; cross-
        # multiplication is the honest equality. The degeneration itself is
        # recorded in the claim.)
        Nn = sp.expand(N.subs({a: av, b: bv}))
        Dn = sp.expand(r["denominator"].subs({a: av, b: bv}))
        Pp = sum(sp.Rational(str(F(c))) * T**i for i, c in enumerate(P))
        Qp = sum(sp.Rational(str(F(c))) * T**i for i, c in enumerate(Q))
        ok = sp.expand(Nn * Qp - Dn * Pp) == 0
        assert ok, (m, av, bv, P, Q)
        checks += 1
    out["transforms"].append({
        "name": f"pointwise_power_{m}",
        "denominator_factors": r["denominator_factors"],
        "denominator_residual": str(res),
        "defect_coefficients": [str(c) for c in coeffs],
        "defect_degree": int(sp.degree(N, T)),
        "linear_coeff_equals_a^m_minus_h_m": bool(lin_ok),
        "integer_instantiation_checks": checks,
    })
    print(f"m={m}: defect deg {sp.degree(N,T)}, coeffs {[str(c) for c in coeffs]}, lin-law {lin_ok}, {checks} integer checks OK", flush=True)

# Adams psi^2 with correct library
from core.symbolic_defect import rational_form
n = 20
h = coefficients(2*n)
seq = [h[2*k] for k in range(n)]
Nf, Df = rational_form(seq)
psi2 = sp.expand(1 - (a*a - 2*b)*T + b*b*T*T)
resid = sp.cancel(Df / psi2)
out["transforms"].append({"name": "adams_relabel_2",
    "identity": f"sum h_2k T^k = ({sp.expand(Nf)}) / det(1 - psi^2(A) T), residual {sp.expand(resid)}",
    "residual_is_one": sp.cancel(resid - 1) == 0})
print("adams2 residual is psi^2 exactly:", sp.cancel(resid - 1) == 0, flush=True)

with open("matrix/defects.json", "w") as f:
    json.dump(out, f, indent=1)
print("WROTE matrix/defects.json", flush=True)
