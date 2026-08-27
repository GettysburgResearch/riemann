#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction as Q
from pathlib import Path
import hashlib
import itertools
import json

checks: list[str] = []


def check(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)
    checks.append(label)


def check_eq(left: object, right: object, label: str) -> None:
    if left != right:
        raise AssertionError(f"{label}: {left!r} != {right!r}")
    checks.append(label)


# Exact strong-log-concavity constant ledger.
margin = Q(1) - Q(1881, 7000)
check_eq(margin, Q(5119, 7000), "strong:margin")

mass_tail = Q(1, 250) + Q(1, 1000)
check_eq(mass_tail, Q(1, 200), "strong:theta-tail")

p1_lower = Q(1) / (Q(1) + mass_tail)
check_eq(p1_lower, Q(200, 201), "strong:first-orbit-weight")

curvature_lower = p1_lower * Q(4) * Q(3) * margin
check_eq(curvature_lower, Q(20476, 2345), "strong:curvature-ledger")
check(curvature_lower > 8, "strong:curvature-over-eight")
check_eq(curvature_lower - Q(8), Q(1716, 2345),
         "strong:margin-over-eight")

# Exact union/product defect used in the finite Blaschke trace bound.
values = [Q(1, 10), Q(1, 4), Q(1, 2), Q(3, 4), Q(9, 10)]
for length in range(1, 6):
    for values_tuple in itertools.product(values, repeat=length):
        product = Q(1)
        for value in values_tuple:
            product *= value
        left = Q(1) - product
        right = sum((Q(1) - value for value in values_tuple), Q(0))
        tag = ",".join(map(str, values_tuple))
        check(left <= right, f"product:{length}:{tag}")

# Exact simple-factor trace and depth inequalities.
for h_integer in range(1, 9):
    total_height = Q(h_integer)
    for y_integer in range(1, 13):
        depth = Q(y_integer, 7)
        mid_height = total_height / 2

        # Pi cancels from the Poisson-defect integral.
        from_integral = (
            Q(4) * mid_height * depth / (mid_height + depth)
        ) / (Q(2) * total_height)
        trace = Q(2) * depth / (total_height + Q(2) * depth)

        check_eq(from_integral, trace,
                 f"trace:{total_height}:{depth}:formula")
        check(Q(0) < trace < Q(1),
              f"trace:{total_height}:{depth}:range")
        check(trace <= Q(2) * depth / total_height,
              f"trace:{total_height}:{depth}:depth-bound")

# Finite layer-cake identity and the collar majorant.
depth_sets = [
    [Q(1, 10)],
    [Q(1, 10), Q(1, 5)],
    [Q(1, 7), Q(2, 7), Q(5, 7)],
    [Q(i, 11) for i in range(1, 8)],
    [Q(1, 3), Q(1, 3), Q(2, 3), Q(5, 3)],
]

for index, depths in enumerate(depth_sets):
    points = sorted(set([Q(0)] + depths))
    layer_integral = Q(0)
    for left, right in zip(points[:-1], points[1:]):
        count = sum(1 for depth in depths if depth > left)
        layer_integral += (right - left) * count

    check_eq(layer_integral, sum(depths, Q(0)),
             f"layer:{index}:identity")

    for h_integer in (1, 2, 5):
        total_height = Q(h_integer)
        trace_sum = sum(
            (Q(2) * depth / (total_height + Q(2) * depth)
             for depth in depths),
            Q(0),
        )
        depth_majorant = Q(2) * layer_integral / total_height
        check(trace_sum <= depth_majorant,
              f"layer:{index}:bound:{total_height}")

# Exact critical-height Maxwell-sandwich constants.
kappa = Q(20476, 2345)
check_eq(Q(1, 4) / kappa, Q(2345, 81904),
         "maxwell:critical-exponent")
critical_factor = Q(1) - Q(1, 4) / kappa
check_eq(critical_factor, Q(79559, 81904),
         "maxwell:critical-factor")
check(critical_factor > Q(97, 100),
      "maxwell:factor-over-97-percent")
check_eq(critical_factor - Q(97, 100), Q(2803, 2047600),
         "maxwell:97-percent-margin")

payload = {
    "checks": checks,
    "count": len(checks),
}
proof_object = hashlib.sha256(
    json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()

result = {
    "arithmetic_class": "EXACT_RATIONAL_CONSTANT_AND_DEPTH_LEDGER",
    "checks": len(checks),
    "finite_blaschke_trace_ledger_replayed": True,
    "finite_layer_cake_ledger_replayed": True,
    "height_owner_physical_transfer_proved": False,
    "maxwell_constant_ledger_replayed": True,
    "model_space_functional_analysis_replayed": False,
    "proof_object": proof_object,
    "rh_established": False,
    "strong_logconcavity_constant_ledger_replayed": True,
    "strong_logconcavity_infinite_theta_proof_replayed": False,
    "verdict": "PASS_X_105640_STRONG_LC_DEPTH_COLLAR",
    "xi_collar_index_conversion_proved": False,
}

out_path = Path(__file__).resolve().parent / "results" / "verification.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8")

print(result["verdict"])
print(f"checks={result['checks']}")
print(result["proof_object"])
print("RH_UNPROVEN")
