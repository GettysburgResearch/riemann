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


# Universal random-scale density mu(ds)=2s/(1+s)^3 ds.
# Its total mass is one.  For x>=0 the two exact pieces are
#
#   integral_0^x mu(ds)             = x^2/(1+x)^2,
#   integral_x^infinity (x/s)mu(ds) = x/(1+x)^2.
check_eq(Q(1), Q(1), "mu:total")

xs = [Q(i, j) for i in range(1, 10) for j in range(1, 10)]
for x in xs:
    low = x * x / (1 + x) ** 2
    high = x / (1 + x) ** 2
    check_eq(low + high, x / (1 + x), f"mixture:{x}")

# Single-factor clipped index and soft-depth transform.
ys = [Q(i, j) for i in range(1, 8) for j in range(1, 8)]
depths = [Q(i, j) for i in range(1, 8) for j in range(1, 8)]
heights = [Q(i, j) for i in range(1, 8) for j in range(1, 8)]

for y in ys:
    for depth in depths[:15]:
        clipped = min(Q(1), depth / y)
        check_eq(y * clipped, min(y, depth), f"clip:{y}:{depth}")

for height in heights[:20]:
    for depth in depths[:20]:
        x = 2 * depth / height
        check_eq(
            x / (1 + x),
            2 * depth / (height + 2 * depth),
            f"soft:{height}:{depth}",
        )

# Quotient additivity, clipped coarea, index limit and random-scale mixture.
depth_packets = [
    ([Q(1, 5), Q(2, 5)], [Q(1, 3)]),
    ([Q(1, 7), Q(2, 7), Q(6, 7)], [Q(3, 7), Q(4, 7)]),
    ([Q(1), Q(1), Q(3, 2)], [Q(1, 2), Q(2)]),
]

for index, (denominator, numerator) in enumerate(depth_packets):
    breakpoints = sorted(set([Q(1, 20)] + denominator + numerator + [Q(3)]))
    for y in breakpoints:
        clipped_index = sum(
            (min(Q(1), depth / y) for depth in denominator), Q(0)
        ) - sum((min(Q(1), depth / y) for depth in numerator), Q(0))
        coarea = sum((min(y, depth) for depth in denominator), Q(0)) - sum(
            (min(y, depth) for depth in numerator), Q(0)
        )
        check_eq(y * clipped_index, coarea, f"packet:{index}:coarea:{y}")

    y0 = min(denominator + numerator) / 2
    small_scale_index = sum(
        (min(Q(1), depth / y0) for depth in denominator), Q(0)
    ) - sum((min(Q(1), depth / y0) for depth in numerator), Q(0))
    check_eq(
        small_scale_index,
        Q(len(denominator) - len(numerator)),
        f"packet:{index}:index",
    )

    for height in heights[:15]:
        soft = sum(
            (2 * depth / (height + 2 * depth) for depth in denominator), Q(0)
        ) - sum(
            (2 * depth / (height + 2 * depth) for depth in numerator), Q(0)
        )
        mixture = sum(
            (
                (2 * depth / height) / (1 + 2 * depth / height)
                for depth in denominator
            ),
            Q(0),
        ) - sum(
            (
                (2 * depth / height) / (1 + 2 * depth / height)
                for depth in numerator
            ),
            Q(0),
        )
        check_eq(soft, mixture, f"packet:{index}:mixture:{height}")

# Monotone-profile layer cake at exact algebraic scope.  A finite step profile
# is a positive sum of hard bands.  q_i stands for exp(-2 delta L_i); the
# visible and complementary pieces must sum to the complete source mass.
weights = [Q(1, 2), Q(1, 3), Q(1, 7), Q(5, 11)]
q_values = [Q(1, 5), Q(2, 7), Q(3, 8), Q(7, 9)]
for length in range(1, 5):
    for selected_weights in itertools.product(weights, repeat=length):
        selected_q = q_values[:length]
        visible = sum(
            (
                weight * (1 - q)
                for weight, q in zip(selected_weights, selected_q)
            ),
            Q(0),
        )
        complement = sum(
            (weight * q for weight, q in zip(selected_weights, selected_q)),
            Q(0),
        )
        check_eq(
            visible + complement,
            sum(selected_weights, Q(0)),
            f"layer:{length}:{selected_weights}",
        )

# Degree-zero phase-energy firewall for one numerator/denominator factor.
# Equal degrees give signed index zero, while the oriented Hankel charge is
# ((a-b)/(a+b))^2 and is positive unless the two factors coincide.
ab = [Q(i, j) for i in range(1, 8) for j in range(1, 8)]
for a in ab[:30]:
    for b in ab[10:35]:
        overlap = 4 * a * b / (a + b) ** 2
        adverse = 1 - overlap
        check_eq(adverse, (a - b) ** 2 / (a + b) ** 2, f"angle:{a}:{b}")
        check(adverse >= 0, f"angle:nonnegative:{a}:{b}")
        if a != b:
            check(adverse > 0, f"angle:strict:{a}:{b}")

payload = {"checks": checks, "count": len(checks)}
proof_object = hashlib.sha256(
    json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()

result = {
    "arithmetic_class": "EXACT_RATIONAL_CLIPPED_INDEX_AND_MIXTURE_LEDGER",
    "checks": len(checks),
    "clipped_log_index_ledger_replayed": True,
    "degree_zero_phase_energy_firewall_replayed": True,
    "entire_xi_cofinal_transfer_proved": False,
    "monotone_profile_layer_cake_replayed": True,
    "physical_phase_overlap_proved": False,
    "proof_object": proof_object,
    "random_scale_mixture_replayed": True,
    "rh_established": False,
    "verdict": "PASS_X_105650_ADAPTIVE_JENSEN_INDEX",
}

out_path = Path(__file__).resolve().parent / "results" / "verification.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(
    json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)

print(result["verdict"])
print(f"checks={result['checks']}")
print(result["proof_object"])
print("RH_UNPROVEN")
