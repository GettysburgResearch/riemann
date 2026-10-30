#!/usr/bin/env python3
"""Exact checks of constants in report.md, not a zero or derivative computation.

The analytic inequalities are proved in the report. This small replay checks
their rational endpoints and algebra, using only the standard library.
"""
from fractions import Fraction as F
import json


def main():
    checks = {}

    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks[name] = True

    # Bounds for e and pi are classical analytic inputs, not measured floats.
    check("exp3_gt_17_from_e_gt_8_over_3", F(8, 3) ** 3 > 17)
    check("4pi_lt_13_from_pi_lt_22_over_7", 4 * F(22, 7) < 13)
    check("central_interval_log_ratio", F(39, 40) / (2 * F(22, 7)) > F(1, 7))
    check("log_X_gt_9_from_X_ge_20000_and_e_lt_3", 3 ** 9 < 20000)
    check("central_count_coefficient", F(1, 13) - F(2, 1000) >= F(1, 20))
    check("local_count_coefficient", F(1000, 6) + F(1, 4) + 16 < 1000)

    u = F(1, 2000)
    phase_bound = 60 * u + F(4, 15) * u ** 3
    check("central_phase_lt_half", phase_bound < F(1, 2))
    check("cos_phase_gt_half_using_one_minus_phase_squared_over_two",
          1 - phase_bound ** 2 / 2 > F(1, 2))
    check("tail_geometric_series", F(12, 2 ** 9) / 2 ** 71 == F(3, 2 ** 78))
    check("tail_below_half_central_mass", F(3, 2 ** 76) < F(1, 320))
    check("positive_remaining_coefficient", F(1, 160) - F(3, 2 ** 76) > F(1, 320))

    # (k-1)^2 - (k+71) = (k-10)(k+7), nonnegative for k>=10.
    for k in (10, 11, 17, 100, 10 ** 6):
        check(f"shell_identity_{k}", (k - 1) ** 2 - (k + 71) == (k - 10) * (k + 7))

    check("retained_exponent_margin", F(8, 9) - F(7, 8) == F(1, 72))
    check("low_order_negative_phase", F(2, 5) < F(3, 2))
    check("low_order_log_decay", F(21, 16) - F(6, 5) == F(9, 80))
    check("low_order_envelope_decreasing_at_U1000", F(2 * (400 + 1), 1000) < F(21, 16))
    check("low_order_error_lt_one_at_U1000", 1000 ** 2 < 2 ** 112)
    check("low_order_error_decreases", F(2, 1000) < F(9, 80))
    check("large_time_exponent_margin", F(7, 8) - F(3, 8) == F(1, 2))
    check("large_time_gaussian_decreases_at_U1e6", F(2, 10 ** 6) < 1)
    check("large_time_error_lt_one_at_U1e6", 10 ** 12 < 2 ** 40 and 40 < 500000)
    check("large_time_error_decreases", F(2, 10 ** 6) < F(10 ** 6, 10 ** 6))
    check("all_low_orders_covered", F(2 * 1000, 5) >= 400)

    U = 3 * 10 ** 12
    endpoint = U ** 2 // (8 * 10 ** 6)
    check("published_height_endpoint", endpoint == 1125000000000000000)
    out = {
        "status": "PASS",
        "scope": "exact rational constant and algebra checks only",
        "checks": checks,
        "check_count": len(checks),
        "small_time_phase_bound": str(phase_bound),
        "verified_height_input": U,
        "finite_derivative_endpoint": endpoint,
        "unperformed": [
            "No zeta zero census or external certificate replay",
            "No evaluation of the high derivatives",
            "No numerical substitute for the infinite proof or source assumptions",
        ],
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
