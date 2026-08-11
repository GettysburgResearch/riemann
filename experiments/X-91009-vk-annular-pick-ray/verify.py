#!/usr/bin/env python3
import argparse
import json
import math


def eta_vk(log_t: float) -> float:
    return 1.0 / (log_t ** (2.0 / 3.0) * math.log(log_t) ** (1.0 / 3.0))


def phi(w: float) -> float:
    return 1.0 / (2.0 * (1.0 + math.sqrt(1.0 - w)) ** 2)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", required=True)
    args = parser.parse_args()

    c1 = 1.0 / 64.0
    rows = []
    previous_ratio = None
    ratio_decreases = True
    for log_t in [1e3, 1e4, 1e5, 1e6, 1e8]:
        eta = eta_vk(log_t)
        radius = 0.75 + c1 * eta
        r_min = math.sqrt(1.0 - radius)
        linear_lower = 0.5 - 2.0 * c1 * eta
        b_over_log = (1.0 / eta) / log_t
        main_to_error = log_t * eta
        row = {
            "log_T": log_t,
            "eta_vk": eta,
            "radius": radius,
            "radial_t_min": 1.0 - radius,
            "sqrt_lower": r_min,
            "linear_lower": linear_lower,
            "sqrt_inequality_slack": r_min - linear_lower,
            "B_over_logT_model": b_over_log,
            "main_to_error_model": main_to_error,
            "phi_at_radius": phi(radius),
        }
        rows.append(row)
        if previous_ratio is not None and not b_over_log < previous_ratio:
            ratio_decreases = False
        previous_ratio = b_over_log

    depth_rows = []
    for log_t in [1e3, 1e5, 1e8]:
        eta = eta_vk(log_t)
        radius = 0.75 + c1 * eta
        depth_threshold = math.sqrt(1.0 - radius)
        depth_rows.append({
            "log_T": log_t,
            "depth_threshold": depth_threshold,
            "half_minus_depth": 0.5 - depth_threshold,
            "ratio_to_eta": (0.5 - depth_threshold) / eta,
        })

    gates = {
        "sqrt_linear_bound": min(row["sqrt_inequality_slack"] for row in rows) >= 0.0,
        "sublog_model": ratio_decreases and rows[-1]["B_over_logT_model"] < rows[0]["B_over_logT_model"],
        "positive_catalan_background": min(row["phi_at_radius"] for row in rows) > 0.2,
        "annular_penetration": min(row["radius"] for row in rows) > 0.75,
        "radial_penetration": max(row["radial_t_min"] for row in rows) < 0.25,
        "depth_transfer_scale": all(0.0 < row["ratio_to_eta"] < 0.1 for row in depth_rows),
    }
    if not all(gates.values()):
        raise AssertionError(gates)

    result = {
        "status": "PASS_VK_ANNULAR_PICK_RAY",
        "parameters": {"c1": c1},
        "gates": gates,
        "scale_rows": rows,
        "depth_rows": depth_rows,
    }
    with open(args.json, "w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(result["status"])


if __name__ == "__main__":
    main()
