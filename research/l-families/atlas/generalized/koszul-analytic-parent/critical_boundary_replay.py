"""Compressed exact controls at the critical Schatten/grade boundary.

Singular values stay in multiplicity blocks; no repeated eigenvalue list
is allocated. Logarithms are rational enclosures with directed rounding.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
FREEZE = "4499c6e44d425b6e43fbf004f2750123a9b20c31"
PREFIX = "research/l-families/atlas/generalized/koszul-analytic-parent/"
PINS = (
    (
        "regularization_replay.py",
        "5c92eb951078a2fa61eca82a46f5ddca5b1883a0",
        "91e0847f820343675bd37a1462e62afa646848553841274b4e818060ab44b3b5",
    ),
    (
        "MIXED_RANKS_AND_REGULARIZATION.md",
        "8a5c94646cce3e88756fa92c7be23757adb96cfe",
        "9d8b635fd87fbb61b50c29e20b3af5c5217c6d34b4f56224ff164e4b1e357ae7",
    ),
)
OWNED = (
    "CRITICAL_GRADE_BOUNDARY.md",
    "CRITICAL_BOUNDARY_REPLAY.md",
    "critical_boundary_replay.py",
    "tests/test_critical_boundary.py",
)
FIXTURE = HERE / "critical_boundary.verification.json"


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def digest(data: bytes) -> str:
    import hashlib

    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def authenticate_frozen() -> None:
    for name, blob, expected in PINS:
        resolved = subprocess.check_output(
            ["git", "rev-parse", FREEZE + ":" + PREFIX + name], cwd=ROOT, text=True
        ).strip()
        need(resolved == blob, "frozen critical dependency blob mismatch")
        frozen = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
        need(digest(frozen) == expected, "frozen critical dependency hash mismatch")
        need(
            digest((HERE / name).read_bytes()) == expected,
            "working critical dependency changed",
        )


authenticate_frozen()
SPEC = importlib.util.spec_from_file_location(
    "frozen_regularization_replay", HERE / "regularization_replay.py"
)
need(
    SPEC is not None and SPEC.loader is not None,
    "cannot import authenticated dependency",
)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)
R = M.R


def rounded(
    interval: tuple[Fraction, Fraction], digits: int = 15
) -> tuple[Fraction, Fraction]:
    R.integer(digits, 6, 15)
    low, high = interval
    need(low <= high, "inverted interval")
    grid = 10**digits
    return Fraction((low * grid).numerator // (low * grid).denominator, grid), Fraction(
        -((-high * grid).numerator // (-high * grid).denominator), grid
    )


def interval_add(left, right):
    return left[0] + right[0], left[1] + right[1]


def interval_scale(interval, factor):
    products = interval[0] * factor, interval[1] * factor
    return min(products), max(products)


def log_interval_raw(
    value: int | Fraction, terms: int = 18
) -> tuple[Fraction, Fraction]:
    value = R.rational(value)
    R.integer(terms, 4, 24)
    need(value > 0, "logarithm requires a positive exact argument")
    reduced, exponent = value, 0
    while reduced > 2:
        reduced /= 2
        exponent += 1
    while reduced < Fraction(1, 2):
        reduced *= 2
        exponent -= 1

    def centered(x):
        v = (x - 1) / (x + 1)
        middle = 2 * sum(
            (v ** (2 * j + 1) / (2 * j + 1) for j in range(terms)), Fraction(0)
        )
        error = 2 * abs(v) ** (2 * terms + 1) / ((2 * terms + 1) * (1 - v * v))
        return middle - error, middle + error

    return interval_add(
        centered(reduced), interval_scale(centered(Fraction(2)), exponent)
    )


def log_interval(value: int | Fraction, terms: int = 18) -> tuple[Fraction, Fraction]:
    return rounded(log_interval_raw(value, terms))


def interval_json(interval):
    return [R.qjson(value) for value in rounded(interval, 12)]


def strip(q: int, cut: int) -> tuple[Fraction, list[int]]:
    R.integer(q, 2, 4)
    R.integer(cut, 2, 24)
    return Fraction(1, q), M.deviations((2, q + 1), cut)


def distribution_control(q: int, cut: int) -> dict[str, object]:
    rho, eps = strip(q, cut)
    total, preceding = sum(eps), sum(eps[:-1])
    singular_power = rho**cut
    lower = interval_scale(
        log_interval(preceding + 1), (preceding + 1) * singular_power
    )
    upper = interval_scale(log_interval(total), total * singular_power)
    partial = sum((count * rho**n for n, count in enumerate(eps, 1)), Fraction(0))
    log_j = log_interval(total)
    need(log_j[0] > 0, "loglog control needs positive first logarithm")
    loglog_j = log_interval(log_j[0])[0], log_interval(log_j[1])[1]
    normalized = partial / loglog_j[1], partial / loglog_j[0]
    target_low = interval_scale(log_interval(q), Fraction(1, q - 1))
    target_high = interval_scale(log_interval(q), Fraction(q, q - 1))
    return {
        "q": q,
        "grade_cut": cut,
        "singular_value_count": total,
        "last_grade_multiplicity": eps[-1],
        "last_block_singular_value_power": R.qjson(singular_power),
        "last_block_lower_jlogj_s_power": interval_json(lower),
        "last_block_upper_jlogj_s_power": interval_json(upper),
        "theorem_liminf": interval_json(target_low),
        "theorem_limsup": interval_json(target_high),
        "partial_singular_power_sum": R.qjson(partial),
        "sum_over_loglog_count": interval_json(normalized),
        "sum_minus_loglog_count": interval_json(
            (partial - loglog_j[1], partial - loglog_j[0])
        ),
        "expanded_singular_value_list": False,
    }


def e_tail_bound(q: int, cut: int) -> Fraction:
    rho, _ = strip(q, cut)
    return 2 * rho ** (cut // 2) / (1 - rho)


def b_tail_bound(q: int, cut: int) -> Fraction:
    rho, _ = strip(q, cut)
    return e_tail_bound(q, cut) + 3 * rho ** (cut + 1) / (2 * (1 - rho) ** 2)


def boundary_log(q: int, cut: int) -> tuple[Fraction, Fraction]:
    rho, eps = strip(q, cut)
    total = Fraction(0), Fraction(0)
    for n, count in enumerate(eps, 1):
        block = log_interval_raw(1 - (-rho) ** n)
        total = interval_add(total, rounded(interval_scale(block, (-1) ** n * count)))
    return rounded(total)


def boundary_rate_control(q: int, cut: int) -> dict[str, object]:
    rho, _ = strip(q, cut)
    observed = boundary_log(q, cut)
    harmonic = sum((Fraction(1, n) for n in range(1, cut + 1)), Fraction(0))
    b_value = interval_add(observed, (harmonic, harmonic))
    source_derivative = (1 + rho) ** (-(q + 2))
    expected = log_interval(source_derivative)
    error = b_tail_bound(q, cut)
    difference = b_value[0] - expected[1], b_value[1] - expected[0]
    need(
        difference[0] <= error and difference[1] >= -error,
        "boundary finite log contradicts the proved infinite tail bound",
    )
    scaled_product_log = interval_add(observed, log_interval(cut))
    gamma_interval = (
        harmonic - log_interval(cut + 1)[1],
        harmonic - log_interval(cut)[0],
    )
    constant_log = expected[0] - gamma_interval[1], expected[1] - gamma_interval[0]
    need(
        scaled_product_log[0] <= constant_log[1] + error + Fraction(1, cut)
        and scaled_product_log[1] >= constant_log[0] - error - Fraction(1, cut),
        "Mertens constant control contradicts proved error",
    )
    return {
        "q": q,
        "grade_cut": cut,
        "rho_Fprime_at_negative_rho": R.qjson(source_derivative),
        "log_DN_plus_HN": interval_json(b_value),
        "log_rho_Fprime": interval_json(expected),
        "proved_B_tail_bound": R.qjson(error),
        "log_N_times_DN": interval_json(scaled_product_log),
        "log_limit_constant": interval_json(constant_log),
        "constant_formula": "exp(-EulerGamma) * rho * Fprime(-rho)",
    }


def gaussian_divide(a, b):
    norm = b[0] ** 2 + b[1] ** 2
    need(norm != 0, "zero Gaussian denominator")
    return ((a[0] * b[0] + a[1] * b[1]) / norm, (a[1] * b[0] - a[0] * b[1]) / norm)


def gaussian_power(a, exponent: int):
    R.integer(exponent, 0, 64)
    out = R.ONE
    while exponent:
        if exponent % 2:
            out = R.mul(out, a)
        a = R.mul(a, a)
        exponent //= 2
    return out


def arc_control(z: object, cut: int = 8) -> dict[str, object]:
    R.integer(cut, 6, 8)
    need(isinstance(z, tuple) and len(z) == 2, "Gaussian phase pair required")
    z = R.rational(z[0]), R.rational(z[1])
    need(z[0] ** 2 + z[1] ** 2 == 1, "unit phase required")
    need((1 + z[0]) ** 2 + z[1] ** 2 >= 1, "finite arc control requires |1+z|>=1")
    t = z[0] / 2, z[1] / 2
    product = R.ONE
    for n in range(1, cut + 1):
        block = R.add(R.ONE, R.neg(gaussian_power(t, n)))
        factor = gaussian_power(block, R.multiplicity(n))
        product = (
            R.mul(product, factor) if n % 2 == 0 else gaussian_divide(product, factor)
        )
    numerator = R.add(R.ONE, (2 * t[0], 2 * t[1]))
    denominator = gaussian_power(R.add(R.ONE, R.neg(t)), 4)
    source = gaussian_divide(numerator, denominator)
    relative_error = R.add(gaussian_divide(product, source), R.neg(R.ONE))
    squared_error = relative_error[0] ** 2 + relative_error[1] ** 2
    log_bound = b_tail_bound(2, cut) + Fraction(2, cut + 1)
    need(log_bound < 1, "arc log tail too coarse for rational exponential bound")
    bound = log_bound / (1 - log_bound)
    need(
        squared_error <= bound**2,
        "exact finite arc product violates proved tail enclosure",
    )
    return {
        "phase_z": R.gjson(z),
        "grade_cut": cut,
        "source_F_at_rho_z": R.gjson(source),
        "relative_error_squared": R.qjson(squared_error),
        "certified_error_squared_bound": R.qjson(bound**2),
        "critical_circle_not_trace_class": True,
    }


def build_payload() -> dict[str, object]:
    authenticate_frozen()
    M.authenticate_frozen()
    R.authenticate()
    return {
        "schema": "koszul-critical-grade-boundary-v1",
        "provenance": {
            "frozen_companion_commit": FREEZE,
            "pins": [list(pin) for pin in PINS],
            "owned_sha256_lf": {
                name: digest((HERE / name).read_bytes()) for name in OWNED
            },
        },
        "arithmetic": "exact integers and fractions; logarithm intervals from atanh series with directed rational rounding",
        "coverage": "identity rank strips (2,k), k=3,4,5; compressed critical singular blocks; named complex boundary phases",
        "distribution_controls": [
            distribution_control(q, cut) for q in (2, 3, 4) for cut in (8, 16, 24)
        ],
        "critical_rate_controls": [
            boundary_rate_control(q, cut) for q in (2, 3, 4) for cut in (8, 16, 24)
        ],
        "critical_arc_controls": [arc_control(z) for z in (R.ONE, R.I, R.neg(R.I))],
        "not_machine_proved": [
            "critical Lorentz classification",
            "all-rank block oscillation and loglog limit",
            "complex boundary convergence",
            "Mertens constant limit",
            "general nonscalar boundary recovery",
        ],
    }


def check_payload(candidate: object) -> None:
    need(
        json.dumps(candidate, sort_keys=True)
        == json.dumps(build_payload(), sort_keys=True),
        "critical fixture differs from authenticated complete replay",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build_payload()
    if args.write:
        FIXTURE.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
            newline="\n",
        )
    else:
        need(
            json.dumps(json.loads(FIXTURE.read_text(encoding="utf-8")), sort_keys=True)
            == json.dumps(payload, sort_keys=True),
            "critical fixture differs from complete replay",
        )
    print("PASS critical grade-boundary exact replay")


if __name__ == "__main__":
    main()
