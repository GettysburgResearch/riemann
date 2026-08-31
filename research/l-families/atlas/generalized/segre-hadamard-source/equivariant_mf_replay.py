"""Source-weighted matrix-factorization traces over exact Gaussian integers."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
FREEZE = "a895f47628b0bc7c7ee5e0392df2f79c24166f92"
PREFIX = "research/l-families/atlas/generalized/segre-hadamard-source/"
PINS = (
    ("MATHEMATICS.md", "bbd847461b4955a93b4533fa687cdd8724e2347c"),
    ("verification.json", "310ffc95cb6eaf19281de52dd18d2f2884bc0f49"),
)
OWNED = (
    "EQUIVARIANT_MATRIX_FACTORIZATION_TRACE.md",
    "EQUIVARIANT_MF_REPLAY.md",
    "equivariant_mf_replay.py",
)
TEST = ROOT / "tests/test_segre_hadamard_equivariant_mf.py"
FIXTURE = HERE / "equivariant_mf.verification.json"
ZERO, ONE, I = (0, 0), (1, 0), (0, 1)


def need(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, low, high, label="integer"):
    need(type(value) is int and low <= value <= high, f"{label} outside declared cap")
    return value


def scalar(value):
    need(
        isinstance(value, (list, tuple)) and len(value) == 2,
        "Gaussian integer pair required",
    )
    need(all(type(a) is int for a in value), "Gaussian coordinates must be integers")
    need(
        any(value) and max(abs(a) for a in value) <= 7,
        "invertible bounded source diagonal required",
    )
    return tuple(value)


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def neg(a):
    return (-a[0], -a[1])


def times(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def power(a, n):
    integer(n, 0, 128, "Gaussian power")
    result = ONE
    for _ in range(n):
        result = times(result, a)
    return result


def total(values):
    result = ZERO
    for value in values:
        result = add(result, value)
    return result


def source_weights(a, b):
    a, b = scalar(a), scalar(b)
    x, z = power(a, 3), times(a, power(b, 2))
    r, s = times(power(a, 2), b), power(b, 3)
    return {"a": a, "b": b, "x": x, "z": z, "r": r, "s": s, "delta": times(r, s)}


def multiply(a, b, cut):
    answer = [ZERO] * (cut + 1)
    for i, x in enumerate(a[: cut + 1]):
        for j, y in enumerate(b[: cut + 1 - i]):
            answer[i + j] = add(answer[i + j], times(x, y))
    return answer


def divide(numerator, denominator, cut):
    need(denominator[0] == ONE, "unit-constant Gaussian denominator required")
    answer = [ZERO] * (cut + 1)
    for n in range(cut + 1):
        value = numerator[n] if n < len(numerator) else ZERO
        for j in range(1, min(n, len(denominator) - 1) + 1):
            value = add(value, neg(times(denominator[j], answer[n - j])))
        answer[n] = value
    return answer


def source_base_characters(weights, cut):
    even, odd = [], []
    for n in range(cut + 1):
        sectors = [ZERO, ZERO]
        for y_degree in range(n + 1):
            x_degree = n - y_degree
            for y1 in range(y_degree + 1):
                y_weight = times(
                    power(weights["r"], y1), power(weights["s"], y_degree - y1)
                )
                for x1 in range(x_degree + 1):
                    value = times(
                        y_weight,
                        times(
                            power(weights["x"], x1), power(weights["z"], x_degree - x1)
                        ),
                    )
                    sectors[y_degree % 2] = add(sectors[y_degree % 2], value)
        even.append(sectors[0])
        odd.append(sectors[1])
    return even, odd


def literal_chow_invariants(a, b, n):
    return total(
        times(power(a, 3 * n - sum(word)), power(b, sum(word)))
        for word in itertools.product(range(n + 1), repeat=3)
        if sum(word) % 2 == 0
    )


def equivariant_columns(weights, cap=6):
    integer(cap, 1, 8, "homological cutoff")
    r, s, delta = (weights[key] for key in ("r", "s", "delta"))
    rows = []
    for i in range(cap + 1):
        generators = [times(power(delta, i), r), times(power(delta, i), s)]
        if i:
            previous = [times(power(delta, i - 1), r), times(power(delta, i - 1), s)]
            need(
                times(previous[0], delta) == generators[0],
                "first D column first row not equivariant",
            )
            need(
                times(previous[1], power(r, 2)) == generators[0],
                "first D column second row not equivariant",
            )
            need(
                times(previous[0], power(s, 2)) == generators[1],
                "second D column first row not equivariant",
            )
            need(
                times(previous[1], delta) == generators[1],
                "second D column second row not equivariant",
            )
        rows.append(
            {
                "homological_degree": i,
                "internal_degree": 1 + 2 * i,
                "generator_eigenvalues": generators,
                "trace": total(generators),
                "dimension": 2,
            }
        )
    need(
        times(power(r, 2), power(s, 2)) == power(delta, 2), "relation character differs"
    )
    for i in range(cap - 1):
        need(
            rows[i + 2]["generator_eigenvalues"]
            == [
                times(power(delta, 2), value)
                for value in rows[i]["generator_eigenvalues"]
            ],
            "twisted two-periodicity failed",
        )
    return rows


def character_control(a, b, cut=12):
    integer(cut, 4, 14, "character cutoff")
    weights = source_weights(a, b)
    a, b = weights["a"], weights["b"]
    even, odd = source_base_characters(weights, cut)
    denominator = [ONE] + [ZERO] * cut
    for weight, degree in (
        (weights["x"], 1),
        (weights["z"], 1),
        (power(weights["r"], 2), 2),
        (power(weights["s"], 2), 2),
    ):
        denominator = multiply(
            denominator, [ONE] + [ZERO] * (degree - 1) + [neg(weight)], cut
        )
    need(
        even == divide([ONE, ZERO, weights["delta"]], denominator, cut),
        "invariant-base monomials versus rational character",
    )
    need(
        odd == divide([ZERO, add(weights["r"], weights["s"])], denominator, cut),
        "odd-module monomials versus rational character",
    )
    bplus = [ONE, times((2, 0), times(a, power(b, 2)))]
    bminus = [
        ZERO,
        times((2, 0), times(power(a, 2), b)),
        times(power(a, 3), power(b, 3)),
    ]
    module = [
        add(x, y)
        for x, y in zip(
            multiply(even, bplus, cut), multiply(odd, bminus, cut), strict=True
        )
    ]
    source = [literal_chow_invariants(a, b, n) for n in range(cut + 1)]
    need(
        source == module,
        "literal Chow invariant source versus equivariant decomposition",
    )
    alternating = [ZERO] * (cut + 1)
    for i in range((cut + 1) // 2):
        value = times(power(weights["delta"], i), add(weights["r"], weights["s"]))
        alternating[1 + 2 * i] = value if i % 2 == 0 else neg(value)
    need(
        multiply(even, alternating, cut) == odd,
        "equivariant infinite-resolution Euler character failed",
    )
    return {
        "diagonal": [a, b],
        "source_generator_weights": weights,
        "invariant_base_character": even,
        "odd_module_character": odd,
        "actual_Chow_invariant_character": source,
        "Tor_weight_rows": equivariant_columns(weights),
        "visible_resolution_Euler_rows_checked": True,
    }


def finite_order_controls():
    primary = character_control(I, ONE)
    other = character_control(ONE, I)
    denominator = [ONE, ZERO, ZERO, ZERO, neg(ONE)]
    need(
        primary["actual_Chow_invariant_character"]
        == divide([ONE, (0, 2)], denominator, 12),
        "primary residual trace-collapse identity",
    )
    need(
        other["actual_Chow_invariant_character"]
        == divide([ONE, (-2, 0)], denominator, 12),
        "second residual trace-collapse identity",
    )
    for row in (primary, other):
        need(
            not any(value != ZERO for value in row["odd_module_character"]),
            "odd module trace did not vanish",
        )
        need(
            all(
                part["trace"] == ZERO and part["dimension"] == 2
                for part in row["Tor_weight_rows"]
            ),
            "Tor trace/dimension distinction lost",
        )
    squared = character_control(neg(ONE), ONE)
    need(
        all(row["trace"] == (2, 0) for row in squared["Tor_weight_rows"]),
        "second-power Tor traces do not recover the module",
    )
    eigenvalues = primary["Tor_weight_rows"][0]["generator_eigenvalues"]
    determinant = [ONE, neg(total(eigenvalues)), times(*eigenvalues)]
    need(
        determinant == [ONE, ZERO, neg(ONE)],
        "degree-one ordinary determinant is not 1-u^2",
    )
    return {
        "primary": primary,
        "independent_finite_order_control": other,
        "primary_squared_operator": squared,
        "degree_one_ordinary_determinant_low_to_high": determinant,
        "second_power_degree_one_trace": total(
            power(value, 2) for value in eigenvalues
        ),
        "arithmetic_Frobenius_realization_asserted": False,
    }


def canonical_bytes(path):
    return path.read_bytes().replace(b"\r\n", b"\n")


def authenticate_source():
    for name, expected in PINS:
        revision = subprocess.check_output(
            ["git", "rev-parse", f"{FREEZE}:{PREFIX}{name}"], cwd=ROOT, text=True
        ).strip()
        data = canonical_bytes(HERE / name)
        blob = hashlib.sha1(
            b"blob " + str(len(data)).encode() + b"\0" + data
        ).hexdigest()
        need(revision == expected and blob == expected, "frozen Chow source differs")


def build_payload():
    authenticate_source()
    return {
        "schema": "segre-hadamard-equivariant-MF-trace/v1",
        "source": {"freeze": FREEZE, "pins": [list(row) for row in PINS]},
        "owned_sha256_lf": {
            name: hashlib.sha256(canonical_bytes(HERE / name)).hexdigest()
            for name in OWNED
        },
        "test_sha256_lf": hashlib.sha256(canonical_bytes(TEST)).hexdigest(),
        "finite_order_trace_controls": finite_order_controls(),
        "generic_noncollapse_controls": [
            character_control((2, 0), (3, 0)),
            character_control((3, 0), (1, 0)),
        ],
        "all_degree_trace_claim_uses_explicit_delta_power_formula": True,
        "finite_resolution_or_module_vanishing_inferred_from_trace": False,
    }


def serialized(payload):
    return json.dumps(payload, sort_keys=True, indent=2) + "\n"


def check_payload(candidate):
    need(
        serialized(candidate) == serialized(build_payload()),
        "equivariant MF payload differs",
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = serialized(build_payload())
    if args.write:
        FIXTURE.write_text(data, encoding="utf-8", newline="\n")
    else:
        need(FIXTURE.exists(), "missing equivariant MF fixture")
        need(
            FIXTURE.read_text(encoding="utf-8") == data,
            "equivariant MF fixture differs",
        )
    print(
        json.dumps(
            {"status": "PASS", "source_panels": 5, "Gaussian_integer_arithmetic": True}
        )
    )


if __name__ == "__main__":
    main()
