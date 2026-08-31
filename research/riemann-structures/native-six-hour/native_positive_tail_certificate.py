#!/usr/bin/env python3
"""Independent exact checks of the positive original-current completion tail."""

from __future__ import annotations

import argparse
import heapq
import json
import subprocess
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha1, sha256
from itertools import product
from math import isqrt
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFIX = "research/riemann-structures/native-six-hour/"
PINS = {
    "scout": (
        "440570c5707e57347987115aeab2ba5fce80d6c5",
        PREFIX + "native_positive_tail_scout.py",
        "890323b2cb6ebfec8c88acd71a33a49f1bdab7a4",
    ),
    "calibration": (
        "440570c5707e57347987115aeab2ba5fce80d6c5",
        PREFIX + "native_positive_tail.calibration.json",
        "cfd8004e1ef51bf8b94fe0dd186b1aecefc5fba5",
    ),
    "majorant_proof": (
        "440570c5707e57347987115aeab2ba5fce80d6c5",
        PREFIX + "NATIVE_POSITIVE_COMPLETION_TAIL.md",
        "06a2257a094f3b636eefff73f811a8e9f4969182",
    ),
    "preregistration": (
        "440570c5707e57347987115aeab2ba5fce80d6c5",
        PREFIX + "NATIVE_POSITIVE_TAIL_PREREGISTRATION.md",
        "6dfeca78a8ba01b066fecae00461dd394b0afd68",
    ),
    "heldout_scout": (
        "d0ff1c645653d61afd77d5e9a0d9a79b64816d0f",
        PREFIX + "native_positive_tail_scout.py",
        "890323b2cb6ebfec8c88acd71a33a49f1bdab7a4",
    ),
    "heldout": (
        "d0ff1c645653d61afd77d5e9a0d9a79b64816d0f",
        PREFIX + "native_positive_tail.heldout.json",
        "bb66d239c4f45cf48451098e8d35c6e9b943c445",
    ),
    "completion": (
        "822646ffea23d906c385f0273a8c45693e982c4d",
        PREFIX + "FIXED_PRIME_INFINITE_HORIZON_COMPLETION.md",
        "851e4331c12d9f3f073ab73dca26baa33bd5e548",
    ),
    "primitive": (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102707-continuous-half-divisor-geodesic-and-polarized-hankel-current.md",
        "6810bcece309b0c54ae6c8fc84b314990004549c",
    ),
    "kernel": (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102880-logarithmic-derivative-outer-detector-has-zero-square-lattice-moment.md",
        "d7330d114ebba1a7a16e22fa9ba6aa6b5eb7cdd6",
    ),
}
MAX_BYTES = 8 * 1024 * 1024
MAX_COST = 2**20
MAX_ROWS = 4096
MAX_BITS = 8192
DEGREE = 20
NOTE = HERE / "NATIVE_POSITIVE_TAIL_REPLAY.md"
TEST = ROOT / "tests/test_native_six_hour_positive_tail.py"
FIXTURE = HERE / "native_positive_tail_certificate.json"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def strict_equal(left, right):
    require(
        canonical(left) == canonical(right), "typed complete positive-tail equality"
    )


def unique_object(items):
    result = {}
    for key, value in items:
        require(key not in result, "duplicate JSON key")
        result[key] = value
    return result


def decode(raw):
    require(type(raw) is bytes and 0 < len(raw) <= MAX_BYTES, "bounded JSON bytes")

    def reject(value):
        raise ValueError("nonfinite JSON number: " + value)

    return json.loads(raw, object_pairs_hook=unique_object, parse_constant=reject)


def bounded(value):
    require(type(value) in (int, F), "exact rational type")
    value = F(value)
    require(
        max(value.numerator.bit_length(), value.denominator.bit_length()) <= MAX_BITS,
        "exact rational bit cap",
    )
    return value


def rational(value):
    require(type(value) is str and 0 < len(value) <= 2500, "literal rational string")
    result = bounded(F(value))
    require(str(result) == value, "canonical rational string")
    return result


def interval(row):
    require(type(row) is dict, "interval object")
    lo, hi = rational(row["lower"]), rational(row["upper"])
    require(lo <= hi, "ordered rational interval")
    return lo, hi


def frozen(role):
    require(role in PINS, "declared source role")
    commit, path, blob = PINS[role]
    ref = commit + ":" + path
    size = int(
        subprocess.check_output(["git", "cat-file", "-s", ref], cwd=ROOT, text=True)
    )
    require(0 < size <= MAX_BYTES, "bounded frozen positive-tail source")
    raw = subprocess.check_output(["git", "show", ref], cwd=ROOT)
    require(
        len(raw) == size
        and sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest() == blob,
        "authenticated positive-tail source",
    )
    return raw


def load_scout(raw):
    namespace = {
        "__name__": "authenticated_positive_tail_final",
        "__file__": str(HERE / "native_positive_tail_scout.py"),
    }
    exec(compile(raw, namespace["__file__"], "exec"), namespace)  # noqa: S102
    return SimpleNamespace(**namespace)


def smooth_costs(maximum):
    require(
        type(maximum) is int and maximum in (60, MAX_COST),
        "declared complete cost maximum",
    )
    seen, pending, answer = {1}, [1], []
    while pending:
        value = heapq.heappop(pending)
        answer.append(value)
        for prime in (2, 3, 5):
            candidate = value * prime
            if candidate <= maximum and candidate not in seen:
                require(len(seen) < MAX_ROWS, "bounded smooth-cost closure")
                seen.add(candidate)
                heapq.heappush(pending, candidate)
    return answer


def powers_of(cost):
    require(type(cost) is int and 1 <= cost <= MAX_COST, "literal bounded cost")
    result = []
    for prime in (2, 3, 5):
        exponent = 0
        while cost % prime == 0:
            cost //= prime
            exponent += 1
        require(exponent <= DEGREE, "bounded source exponent")
        result.append(exponent)
    require(cost == 1, "fixed-prime support")
    return tuple(result)


def source_tables():
    # Independent binomial recurrence, not the acquisition's central-binomial formula.
    half = [F(1)]
    for degree in range(1, DEGREE + 1):
        half.append(bounded(half[-1] * F(2 * degree - 3, 2 * degree)))
    endpoint = [half[e // 2] if e % 2 == 0 else F() for e in range(DEGREE + 1)]
    alpha = tuple(max(abs(x), abs(y)) for x, y in zip(half, endpoint, strict=True))
    derivative = tuple(abs(x - y) for x, y in zip(half, endpoint, strict=True))
    return tuple(half), alpha, derivative


@lru_cache(maxsize=4096)
def _literal_tensor_coefficient(powers):
    _, alpha, derivative = source_tables()
    result = F()
    # Enumerate every assignment of the three product exponents to n and m.
    # Then sum all three literal derivative sites before applying source factor two.
    for left in product(*(range(e + 1) for e in powers)):
        right = tuple(e - a for e, a in zip(powers, left, strict=True))
        right_bound = alpha[right[0]] * alpha[right[1]] * alpha[right[2]]
        sites = sum(
            (
                derivative[left[i]]
                * alpha[left[(i + 1) % 3]]
                * alpha[left[(i + 2) % 3]]
                for i in range(3)
            ),
            F(),
        )
        result += 2 * right_bound * sites
    return bounded(result)


def literal_tensor_coefficient(powers):
    require(
        type(powers) is tuple
        and len(powers) == 3
        and all(type(e) is int and 0 <= e <= DEGREE for e in powers),
        "literal exponent triple",
    )
    require(
        2 ** powers[0] * 3 ** powers[1] * 5 ** powers[2] <= MAX_COST,
        "declared tensor cost cap",
    )
    return _literal_tensor_coefficient(powers)


def product2(left, right):
    return [
        sum((left[j] * right[e - j] for j in range(e + 1)), F())
        for e in range(DEGREE + 1)
    ]


def validate_tables(data):
    half, alpha, derivative = source_tables()
    strict_equal(data["all_local_alpha_coefficients"], list(map(str, alpha)))
    strict_equal(
        data["all_local_absolute_derivative_coefficients"], list(map(str, derivative))
    )
    strict_equal(
        data["all_local_Amax_squared_coefficients"],
        list(map(str, product2(alpha, alpha))),
    )
    strict_equal(
        data["all_local_D_Amax_coefficients"],
        list(map(str, product2(derivative, alpha))),
    )
    require(
        product2(half, half) == [F(1), F(-1)] + [F()] * (DEGREE - 1),
        "independent exact source square",
    )
    return {
        "degree": DEGREE,
        "recurrence_source_square_verified": True,
        "coefficientwise_even_degree_two": str(alpha[2]),
        "absolute_derivative_degree_two": str(derivative[2]),
    }


def root_enclosure(bounds, value):
    lo, hi = bounds
    value = bounded(value)
    require(
        0 <= lo <= hi and lo * lo <= value <= hi * hi,
        "independent exact square bracket",
    )


# This second interval route uses exact interval operations and only 256-bit
# integer root brackets. It does not call the acquisition's rounded helpers.
def ia(x, y):
    return bounded(x[0] + y[0]), bounded(x[1] + y[1])


def im(x, y):
    values = [bounded(a * b) for a in x for b in y]
    return min(values), max(values)


def isc(x, value):
    return im(x, (bounded(value), bounded(value)))


def isub(x, y):
    return ia(x, (-y[1], -y[0]))


def ip(values):
    result = (F(1), F(1))
    for value in values:
        result = im(result, value)
    return result


def isum(values):
    result = (F(), F())
    for value in values:
        result = ia(result, value)
    return result


def independent_root(x):
    require(0 <= x[0] <= x[1], "independent nonnegative root interval")
    scale = 2**256
    answers = []
    for upper, value in enumerate(x):
        value = bounded(value)
        require(
            value.numerator.bit_length() + 512 <= MAX_BITS, "root integer shift cap"
        )
        numerator = value.numerator * scale * scale
        floor = isqrt(numerator // value.denominator)
        require(
            floor * floor * value.denominator
            <= numerator
            < (floor + 1) * (floor + 1) * value.denominator,
            "independent integer root calculation",
        )
        if upper and floor * floor * value.denominator < numerator:
            floor += 1
        answers.append(F(floor, scale))
    return tuple(answers)


def independent_closed_bounds():
    one, two = (F(1), F(1)), (F(2), F(2))
    locals_ = []
    for prime in (2, 3, 5):
        rho = independent_root((F(1, prime), F(1, prime)))
        minus, plus = independent_root(isub(one, rho)), independent_root(ia(one, rho))
        even = independent_root((1 - F(1, prime), 1 - F(1, prime)))
        locals_.append(
            {
                "prime": prime,
                "rho": rho,
                "D": isub(plus, even),
                "A_actual": isub(two, minus),
                "A_max": ia(isub(two, even), isc(isub(plus, minus), F(1, 2))),
            }
        )

    def total_for(key):
        return isc(
            isum(
                im(
                    im(row["D"], row[key]),
                    ip(
                        im(other[key], other[key])
                        for j, other in enumerate(locals_)
                        if i != j
                    ),
                )
                for i, row in enumerate(locals_)
            ),
            2,
        )

    # Independent 128-term positive series versus the acquisition's 256 terms.
    log_lower = bounded(
        2 * sum((F(1, (2 * j + 1) * 3 ** (2 * j + 1)) for j in range(128)), F())
    )
    log_upper = bounded(log_lower + F(2, 257 * 3**257) / F(8, 9))
    root2 = independent_root(two)
    mass = isub(
        isc(im(ia((F(3), F(3)), root2), (log_lower, log_upper)), 128), (F(288), F(288))
    )
    return locals_, total_for("A_actual"), total_for("A_max"), mass


def contained(inner, outer):
    require(
        outer[0] <= inner[0] <= inner[1] <= outer[1],
        "independent closed-value enclosure",
    )


def validate_constants(data):
    local, physical, majorant, mass = independent_closed_bounds()
    require(len(data["local_closed_sums"]) == 3, "complete local closed sums")
    for captured, fresh in zip(data["local_closed_sums"], local, strict=True):
        require(
            type(captured["prime"]) is int and captured["prime"] == fresh["prime"],
            "literal local prime",
        )
        for key in ("rho", "D", "A_actual", "A_max"):
            contained(interval(captured[key]), fresh[key])
        root_enclosure(interval(captured["rho"]), F(1, fresh["prime"]))
        require(
            interval(captured["A_actual"])[1] < interval(captured["A_max"])[0],
            "aggregate and coefficientwise majorants stay distinct",
        )
    contained(interval(data["uniform_physical_source_bound"]), physical)
    contained(interval(data["closed_positive_majorant_total"]), majorant)
    contained(interval(data["original_kernel_mass"]), mass)
    root_enclosure(interval(data["unweighted_endpoint_source_bound"]), F(73728))
    require(interval(data["original_kernel_mass"])[0] > 0, "positive original measure")


def validate_records(data, maximum):
    expected = smooth_costs(maximum)
    rows = data["complete_smooth_cost_records"]
    require(
        type(rows) is list and len(rows) == len(expected), "complete smooth-cost census"
    )
    for cost, row in zip(expected, rows, strict=True):
        require(
            type(row["cost"]) is int and row["cost"] == cost,
            "ordered literal smooth cost",
        )
        powers = powers_of(cost)
        strict_equal(row["powers"], list(powers))
        value = literal_tensor_coefficient(powers)
        require(
            rational(row["exact_majorant_coefficient"]) == value,
            "literal full tensor coefficient",
        )
        root_enclosure(interval(row["directed_contribution"]), value * value / cost)
    return rows


def validate_panel(panel, records, data):
    horizon = panel["H"]
    require(
        type(horizon) is int and horizon in (25, 30, 60, 900, MAX_COST),
        "declared final horizon",
    )
    prefix = [row for row in records if row["cost"] <= horizon]
    require(
        type(panel["complete_prefix_count"]) is int
        and panel["complete_prefix_count"] == len(prefix),
        "complete prefix count",
    )
    strict_equal(panel["complete_prefix_costs"], [row["cost"] for row in prefix])
    require(
        panel["prefix_sha256"] == sha256(canonical(prefix).encode()).hexdigest(),
        "complete prefix digest",
    )
    bounds = tuple(
        sum((interval(row["directed_contribution"])[i] for row in prefix), F())
        for i in (0, 1)
    )
    require(
        interval(panel["positive_majorant_prefix"]) == bounds,
        "sum of complete directed contributions",
    )
    majorant = interval(data["closed_positive_majorant_total"])
    raw = majorant[0] - bounds[1], majorant[1] - bounds[0]
    require(
        interval(panel["raw_total_minus_prefix"]) == raw,
        "same positive majorant subtraction",
    )
    require(raw[1] >= 0, "nonnegative tail upper endpoint")
    tail = max(F(), raw[0]), raw[1]
    require(
        interval(panel["positive_majorant_remainder"]) == tail,
        "positivity only clips lower endpoint",
    )
    endpoint = interval(panel["independent_endpoint_rate"])
    root_enclosure(endpoint, F(73728, horizon))
    field = rational(panel["uniform_field_error_upper"])
    require(
        field == min(tail[1], endpoint[1]) and field >= 0,
        "minimum of two certified field upper bounds",
    )
    mass, physical = (
        interval(data["original_kernel_mass"]),
        interval(data["uniform_physical_source_bound"]),
    )
    hilbert = rational(panel["uniform_Hilbert_error_upper"])
    energy = rational(panel["uniform_energy_and_minimum_error_upper"])
    require(
        hilbert >= 0 and hilbert * hilbert >= mass[1] * field * field,
        "original Hilbert upper bound",
    )
    require(
        energy >= 2 * mass[1] * physical[1] * field,
        "original energy and minimum upper bound",
    )
    return {
        "H": horizon,
        "complete_prefix_count": len(prefix),
        "uniform_field_error_upper": str(field),
        "uniform_Hilbert_error_upper": str(hilbert),
        "uniform_energy_and_minimum_error_upper": str(energy),
        "positive_tail_nonnegative": True,
    }


def validate_capture(data, phase):
    require(phase in ("calibration", "heldout"), "declared capture phase")
    require(
        data["phase"] == phase
        and type(data["interval_bits"]) is int
        and data["interval_bits"] == 512,
        "unchanged capture phase and precision",
    )
    for key in (
        "signed_observed_tail_evaluated",
        "optimal_path_persistence_claimed",
        "full_gamma_identified",
        "all_prime_limit_claimed",
    ):
        require(data[key] is False, "original finite-prime completion scope")
    require(type(data["proof_object_sha256"]) is str, "literal capture proof hash")
    unsigned = {
        key: value for key, value in data.items() if key != "proof_object_sha256"
    }
    require(
        sha256(canonical(unsigned).encode()).hexdigest() == data["proof_object_sha256"],
        "complete capture proof hash",
    )
    tables = validate_tables(data)
    validate_constants(data)
    horizons = [25, 30, 60] if phase == "calibration" else [900, MAX_COST]
    strict_equal([row["H"] for row in data["panels"]], horizons)
    rows = validate_records(data, max(horizons))
    return tables, [validate_panel(panel, rows, data) for panel in data["panels"]]


def build():
    raw = {role: frozen(role) for role in PINS}
    require(
        raw["scout"] == raw["heldout_scout"],
        "unchanged positive-tail heldout executable",
    )
    captures = {phase: decode(raw[phase]) for phase in ("calibration", "heldout")}
    strict_equal(
        captures["calibration"]["owned_sha256_lf"],
        captures["heldout"]["owned_sha256_lf"],
    )
    scout = load_scout(raw["scout"])
    summaries, controls = [], []
    for phase in ("calibration", "heldout"):
        strict_equal(scout.discover(phase), captures[phase])
        table, panels = validate_capture(captures[phase], phase)
        controls.append(
            {
                "phase": phase,
                "source_tables": table,
                "complete_cost_count": len(
                    captures[phase]["complete_smooth_cost_records"]
                ),
                "capture_proof_sha256": captures[phase]["proof_object_sha256"],
            }
        )
        summaries.extend(panels)
    result = {
        "schema": "riemann.native_six_hour.positive_tail_certificate.v1",
        "sources": [
            {"role": role, "commit": commit, "path": path, "blob": blob}
            for role, (commit, path, blob) in PINS.items()
        ],
        "panels": summaries,
        "independent_controls": controls,
        "literal_tensor_allocation_controls": {
            str(cost): str(literal_tensor_coefficient(powers_of(cost)))
            for cost in (1, 2, 4, 6, 8)
        },
        "original_measure_retained": True,
        "all_monotone_paths_covered": True,
        "signed_observed_tail_evaluated": False,
        "optimizer_persistence_claimed": False,
        "all_prime_limit_claimed": False,
        "full_gamma_identified": False,
        "owned_sha256_lf": {
            path.relative_to(ROOT).as_posix(): sha256(
                path.read_bytes().replace(b"\r\n", b"\n")
            ).hexdigest()
            for path in (Path(__file__), NOTE, TEST)
        },
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--write", action="store_true")
    modes.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    encoded = (
        json.dumps(result, sort_keys=True, indent=2, allow_nan=False) + "\n"
    ).encode()
    require(len(encoded) <= MAX_BYTES, "bounded final positive-tail artifact")
    if args.write:
        FIXTURE.write_bytes(encoded)
    else:
        strict_equal(decode(FIXTURE.read_bytes()), result)
    print(
        "PASS complete positive-tail source, exact enclosures and original minimum bounds"
    )


if __name__ == "__main__":
    main()
