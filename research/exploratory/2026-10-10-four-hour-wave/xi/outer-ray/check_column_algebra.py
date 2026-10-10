#!/usr/bin/env python3
"""Exact polynomial controls for FC4--FC13, not an actual Xi certificate.

The complete product, actual census, analytic limits and full column remain
proof dependencies. Finite fixtures test signs and complete root sums only.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

from check_exact import C, I, ZERO, at, companion, derivative, multiply, need

HERE = Path(__file__).resolve().parent
WAVE = HERE.parents[1]


def conjugate(z: C) -> C:
    return C(z.re, -z.im)


def fixture(real: list[tuple[Q, int]], nonreal: list[tuple[Q, Q, int]]) -> tuple[list[C], list[tuple[C, int]]]:
    p = [C(Q(1))]
    roots: list[tuple[C, int]] = []
    for alpha, m in real:
        for _ in range(m):
            p = multiply(p, [C(Q(1)), ZERO, C(-1 / alpha**2)])
        roots.extend([(C(alpha), m), (C(-alpha), m)])
    for gamma, eta, m in nonreal:
        rho = C(gamma, eta)
        for _ in range(m):
            p = multiply(p, multiply([C(Q(1)), ZERO, -1 / square(rho)],
                                     [C(Q(1)), ZERO, -1 / square(conjugate(rho))]))
        roots.extend([(C(x, y), m) for x in [gamma, -gamma] for y in [eta, -eta]])
    return p, roots


def square(z: C) -> C:
    return z * z


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE / "column_algebra_controls.json")
    args = parser.parse_args()
    definitions = [
        ([(Q(a), 1) for a in [1, 2, 3, 4]], [(Q(9), Q(1, 2), 1)]),
        ([(Q(a), 1) for a in [1, 2, 3]], [(Q(9), Q(1, 4), 2), (Q(12), Q(1, 2), 1)]),
        ([(Q(a), 1) for a in [1, 2, 3, 4, 5, 6]], []),
        ([], [(Q(9), Q(1, 2), 1), (Q(12), Q(1, 4), 2)]),
        ([(Q(1), 1), (Q(3), 1), (Q(10), 2)], [(Q(12), Q(1, 2), 1)]),
    ]
    cases = rootsums = all_lambda_coefficient_controls = 0
    for real, nonreal in definitions:
        p, roots = fixture(real, nonreal)
        need(all(c.im == 0 for c in p), "real fixture coefficients")
        need(all(p[j] == ZERO for j in range(1, len(p), 2)), "even fixture")
        need(all(abs(root.im) <= Q(1, 2) for root, _ in roots), "declared complete strip")
        need(all(root.im == 0 or abs(root.re) > 8 for root, _ in roots), "complete finite real census premise")
        need(all(m == 1 for root, m in roots if root.im == 0 and abs(root.re) <= 8), "simple central real census")
        h = p
        for r in range(6):
            h1, h2 = derivative(h), derivative(derivative(h))
            for x in [Q(0), Q(1, 2), Q(-1, 2), Q(1), Q(-1), Q(2), Q(-2), Q(4), Q(-4)]:
                need(abs(x) < 8 - Q(r + 2, 2), "strict protected real-part width")
                for y in [Q(1, 16), Q(1, 8), Q(1, 4), Q(1, 2)]:
                    z = C(x, -y)
                    v, v1, v2 = at(h, z), at(h1, z), at(h2, z)
                    need(v != ZERO and v1 != ZERO, "finite logarithmic derivative denominators")
                    q = v1 / v
                    qp = v2 / v - square(q)
                    middle = v1.norm2() - (v * conjugate(v2)).re
                    need(middle == v.norm2() * (2 * q.im**2 - qp.re), "normalized complex Laguerre identity")
                    constant = -(v * conjugate(v1)).im
                    quadratic = -(v1 * conjugate(v2)).im
                    need(constant == v.norm2() * q.im > 0, "strict constant companion coefficient")
                    need(quadratic == v1.norm2() * (v2 / v1).im > 0, "strict quadratic companion coefficient")
                    need(middle > 0, "strict middle companion coefficient")
                    all_lambda_coefficient_controls += 1
                    if r == 0:
                        root_q = ZERO
                        minus_qp = ZERO
                        real_im = Q(0)
                        lower = Q(0)
                        for root, m in roots:
                            term = m / (z - root)
                            root_q += term
                            term2 = m / square(z - root)
                            minus_qp += term2
                            if root.im == 0:
                                real_im += term.im
                                lower += m / (z - root).norm2()
                            else:
                                need(term2.re > 0, "individual nonreal squared-kernel positivity")
                                lower += term2.re
                        need(root_q == q and minus_qp == -qp, "complete declared-root logarithmic sums")
                        need(q.im >= real_im >= 0, "complete conjugate blocks preserve imaginary sum")
                        need(2 * q.im**2 - qp.re >= lower > 0, "complete real-root compensation lower bound")
                        rootsums += 1
                    for lam in [Q(1, 10**10), Q(1), Q(1001)]:
                        e = at(companion(h, lam), z)
                        e1 = at(companion(h1, lam), z)
                        n = (I * e * conjugate(e1)).re
                        need(n == constant + lam * middle + lam**2 * quadratic > 0,
                             "exact three-coefficient companion expansion")
                        need(e != ZERO and e1 != ZERO and (I * e / e1).re > 0,
                             "finite companion strict sector")
                        cases += 1
            h = h1
    sources = [Path(__file__).resolve(), HERE / "check_exact.py", HERE / "CENSUS_FULL_COLUMN_SECTOR.md",
               HERE / "CENSUS_LOCALIZATION.md", HERE / "THEOREM.md"]
    result = {
        "status": "PASS_EXACT_FULL_COLUMN_POLYNOMIAL_ALGEBRA",
        "scope": "exact finite synthetic polynomial controls; no actual Xi evaluation or full-domain authentication",
        "fixtures": len(definitions), "derivative_orders_per_fixture": 6,
        "complete_declared_root_sum_controls": rootsums,
        "three_positive_coefficient_controls": all_lambda_coefficient_controls,
        "exact_companion_point_controls": cases,
        "actual_xi_values_evaluated": False, "native_complete_count_replayed": False,
        "analytic_full_column_authenticated_by_checker": False, "rh_proved": False,
        "source_sha256": {str(p.relative_to(WAVE)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["status"], "COEFFICIENTS", all_lambda_coefficient_controls, "POINTS", cases)


if __name__ == "__main__":
    main()
