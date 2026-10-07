#!/usr/bin/env python3
"""Exact exponent bookkeeping; no estimate of zeta or any infinite sum.

Default: record consequences of the two external endpoint hypotheses and
the obstruction from the written MHB32 estimate.

Optional hypothetical recurrence:
  python checks/hybrid_exponent_budget.py --a 1/4 --p 4/3 --seed 3/4

The optional recurrence is an ASSUMPTION, not a bound proved by this script.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import json


def rational(value: Q) -> dict[str, object]:
    return {"exact": str(value), "decimal": float(value)}


def consequences(alpha: Q) -> dict[str, object]:
    energy = 2 * alpha - 1
    mhb = (191 + 82 * energy) / 273
    cap = 6 * alpha - 4
    square_seed = 4 * alpha - 2
    # All identities use exact rational arithmetic, not sampled exponent fits.
    assert mhb - energy == Q(191, 273) * (1 - energy)
    assert square_seed - cap == 2 - 2 * alpha
    return {
        "status": "conditional on external strip plus classical summation interface",
        "zero_free_boundary": rational(alpha),
        "M_summatory_exponent": rational(alpha),
        "m_reciprocal_sum_exponent": rational(alpha - 1),
        "native_energy_exponent": rational(energy),
        "current_complete_MHB32_output": rational(mhb),
        "MHB32_improves_seed": mhb < energy,
        "CAP36_width_exponent": rational(alpha),
        "CAP36_D_exponent_bounded_phase": rational(4 * alpha - 3),
        "CAP36_transport_error_exponent_in_Y": rational(cap),
        "CAP36_transport_error_exponent_in_output_X": rational(cap / 2),
        "square_step_energy_seed_exponent_in_Y": rational(square_seed),
        "saving_between_upper_bound_scales_in_Y": rational(square_seed - cap),
        "CAP36_limits": "difference bound; anchored |tau|<=1; exact observation hypotheses retained",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--a", type=Q)
    parser.add_argument("--p", type=Q)
    parser.add_argument("--seed", type=Q, default=Q(3, 4))
    args = parser.parse_args()
    if (args.a is None) != (args.p is None):
        parser.error("--a and --p must be supplied together")
    seven = consequences(Q(7, 8))
    eleven = consequences(Q(11, 12))
    assert seven["current_complete_MHB32_output"]["exact"] == "505/546"
    assert eleven["current_complete_MHB32_output"]["exact"] == "778/819"
    threshold = Q(3, 4) * (2 - Q(4, 3))
    assert threshold == Q(1, 2)
    report = {
        "status": "PASS",
        "arithmetic": "EXACT_RATIONAL",
        "proves_new_analytic_estimate": False,
        "source_scope": "conditional exponents from CONDITIONAL_BRIDGES.md and RESEARCH_PLAN.md",
        "endpoints": [seven, eleven],
        "p_4_over_3_candidate": {
            "status": "sufficient threshold only; full recurrence not established",
            "strict_improvement_requires_a_less_than": rational(threshold),
        },
    }
    if args.a is not None:
        if args.a < 0 or not Q(1) <= args.p < 2 or args.seed < 0:
            parser.error("Require a>=0, 1<=p<2 and seed>=0")
        new = (args.a + args.p * args.seed) / 2
        limit = args.a / (2 - args.p)
        report["hypothetical_recurrence"] = {
            "status": "UNPROVED_USER_SUPPLIED_RECURRENCE",
            "a": rational(args.a), "p": rational(args.p), "seed": rational(args.seed),
            "one_step_output": rational(new), "improves_seed": new < args.seed,
            "formal_fixed_point": rational(limit),
            "corresponding_zero_abscissa_if_all_bridges_hold": rational((1 + limit) / 2),
            "iteration_requires": "same valid complete recurrence at every step, with all costs paid",
        }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
