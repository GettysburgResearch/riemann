"""Exact supplemental coefficient checks for the scoped T_1 endpoint audit.

The mathematical noninvertibility proof uses infinite-series comparisons in the
audit, not this finite computation. All computed coefficients/bounds are rational.
"""
from fractions import Fraction
import json
from pathlib import Path


def check_case(k):
    j = k + 1
    for n in range(k + 9):
        derivative = n + 1 if n + 1 <= k else 0
        cumulative = min(n + 1, j)
        actual = derivative - cumulative
        expected = 0 if n < k else -j
        assert actual == expected, (k, n, actual, expected)
    harmonic = sum((Fraction(1, n) for n in range(1, j + 1)), Fraction())
    upper = Fraction(1, 2) + Fraction(1, j)
    return {
        "K": k,
        "domain_norm_squared_exact": str(harmonic),
        "image_norm_squared_rigorous_interval": ["1/2", str(upper)],
        "normalized_image_norm_squared_upper": str(upper / harmonic),
        "operator_coefficients_checked_through": k + 8,
    }


def main():
    cases = [check_case(k) for k in [0, 1, 2, 4, 8, 16, 32, 64, 128, 256]]
    result = {
        "status": "supplemental_exact_checks_not_a_substitute_for_analytic_proof",
        "source": "audits/gallardo_seco_endpoint_round3.md",
        "coefficient_identity": "T_1 sum_(n0..K)z^n=-(K+1)z^K/(1-z)",
        "cases": cases,
    }
    path = Path(__file__).resolve().parents[1] / "results/weighted_dirichlet_endpoint_round3.json"
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Exact polynomial coefficient checks passed: {len(cases)} cases")


if __name__ == "__main__":
    main()
