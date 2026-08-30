"""Exact finite duality and actual-closure grading-boundary controls."""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
from fractions import Fraction
from functools import cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PREFIX = "research/l-families/atlas/generalized/koszul-analytic-parent/"
FREEZE = "e2b0ef1b35fa46e81a1f1b447a70f42dd3b92c2e"
PINS = (
    (
        "global_cohomology_replay.py",
        "87fd6d661a88e7830d234963b8dce16b49caa8f2",
        "da202437478ed4a199deb4b2f05ca2e7ce1062faa5d60c1c29bd80c4a8aacf66",
    ),
    (
        "GLOBAL_COHOMOLOGICAL_COMPLETION.md",
        "8ecc724afc29e048097d955b8eb7a872d26f79a7",
        "fadf5a3e609ce64b6c49cb848186495bab579cba5fdb5a5e594638b635469d66",
    ),
)
OWNED = (
    "GLOBAL_DUALITY_AND_GRADING_BOUNDARY.md",
    "GLOBAL_BOUNDARY_REPLAY.md",
    "global_boundary_replay.py",
    "tests/test_global_boundary.py",
)
FIXTURE = HERE / "global_boundary.verification.json"


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
        need(resolved == blob, "global boundary dependency blob mismatch")
        frozen = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
        need(digest(frozen) == expected, "global boundary dependency hash mismatch")
        need(
            digest((HERE / name).read_bytes()) == expected,
            "working global boundary dependency changed",
        )


authenticate_frozen()
SPEC = importlib.util.spec_from_file_location(
    "frozen_global_cohomology", HERE / "global_cohomology_replay.py"
)
need(
    SPEC is not None and SPEC.loader is not None,
    "cannot load authenticated global source",
)
G = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(G)
C, R, S = G.C, G.R, G.S
ONE = (Fraction(1), Fraction(0))
ZERO = (Fraction(0), Fraction(0))
OMEGA = (Fraction(0), Fraction(1))


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def scale(a, scalar):
    return a[0] * scalar, a[1] * scalar


def multiply(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0] - a[1] * b[1]


def inverse(a):
    norm = a[0] * a[0] - a[0] * a[1] + a[1] * a[1]
    need(norm != 0, "zero Eisenstein denominator")
    return (a[0] - a[1]) / norm, -a[1] / norm


def power(a, exponent: int):
    R.integer(exponent, 0, 48)
    result = ONE
    for _ in range(exponent):
        result = multiply(result, a)
    return result


def real_part(a):
    return a[0] - a[1] / 2


def pair_json(a):
    return [C.interval_json((x, x)) for x in a]


def sum_power(n: int, degree: int) -> int:
    R.integer(n, 0, 256)
    R.integer(degree, 1, 4)
    if degree == 1:
        return n * (n + 1) // 2
    if degree == 2:
        return n * (n + 1) * (2 * n + 1) // 6
    if degree == 3:
        return (n * (n + 1) // 2) ** 2
    return n * (n + 1) * (2 * n + 1) * (3 * n * n + 3 * n - 1) // 30


def kappa(n: int) -> int:
    R.integer(n, 0, 256)
    dimension = (n + 1) ** 2 * (n + 2) // 2
    reflection = n // 2 + 1 if n % 2 == 0 else 0
    cycle = int(n % 3 == 0)
    need((dimension - cycle) % 3 == 0, "source standard multiplicity is not integral")
    return (dimension - cycle) // 3 - reflection


def prefactor_exponents(cut: int) -> tuple[int, int]:
    R.integer(cut, 0, 256)
    even, thirds = cut // 2, cut // 3
    k = (
        Fraction(
            sum_power(cut, 3)
            + 4 * sum_power(cut, 2)
            + 5 * sum_power(cut, 1)
            + 2 * (cut + 1),
            6,
        )
        - Fraction(thirds + 1, 3)
        - Fraction((even + 1) * (even + 2), 2)
    )
    w = (
        Fraction(
            sum_power(cut, 4)
            + 4 * sum_power(cut, 3)
            + 5 * sum_power(cut, 2)
            + 2 * sum_power(cut, 1),
            6,
        )
        - sum_power(thirds, 1)
        - 2 * (sum_power(even, 2) + sum_power(even, 1))
    )
    need(
        k.denominator == w.denominator == 1, "finite duality exponents are nonintegral"
    )
    return int(k), int(w)


def finite_global(
    source: dict[str, object], z: Fraction, T: Fraction, cut: int
) -> Fraction:
    R.integer(cut, 0, 4)
    z, T = C.exact(z), C.exact(T)
    need(
        0 < z <= 100 and 0 < T <= 100, "bounded nonzero finite duality inputs required"
    )
    q = source["parameters_p_A_B"][0]
    pe, pd = source["polynomials"]["E"], source["polynomials"]["D"]
    result = Fraction(1)
    for n, row in enumerate(S.source_rows(cut)):
        a, b, c = row["multiplicities_1_sign_std"]
        u = T * z**n
        denominator = (1 - u) * (1 - q * u)
        need(denominator != 0, "finite duality input hits a pole")
        result *= (
            (1 + pd[1] * u + q * u * u) ** b
            * (1 + pe[1] * u + q * u * u) ** c
            / denominator**a
        )
    return result


def duality_control(source: dict[str, object], cut: int) -> dict[str, object]:
    q = source["parameters_p_A_B"][0]
    z, T = Fraction(1, 4), Fraction(1, 10)
    k, w = prefactor_exponents(cut)
    lhs = finite_global(source, z, T, cut)
    opposite = finite_global(source, 1 / z, 1 / (q * T), cut)
    prefactor = Fraction(q) ** k * T ** (2 * k) * z ** (2 * w)
    need(lhs == prefactor * opposite, "actual finite global functional equation failed")
    return {
        "cut": cut,
        "K_N": k,
        "W_N": w,
        "finite_global_value": C.qjson(lhs),
        "native_prefactor": C.qjson(prefactor),
        "exact_reciprocal_identity": True,
    }


def closure_counts(source: dict[str, object], degree: int) -> list[int]:
    R.integer(degree, 2, 48)
    q = source["parameters_p_A_B"][0]
    ed = G.frobenius_traces(source["polynomials"]["D"], degree)
    ee = G.frobenius_traces(source["polynomials"]["E"], degree)
    counts = [1 + q**m - ed[m - 1] - 2 * ee[m - 1] for m in range(1, degree + 1)]
    need(
        all(0 <= value <= 6 * (q**m + 1) for m, value in enumerate(counts, 1)),
        "source closure count violates its geometric bound",
    )
    for row in source["primitive_rows"]:
        need(
            counts[row["degree"] - 1] == row["counts"]["Z"],
            "closure Frobenius module disagrees with primitive point count",
        )
    need(
        all(counts[m - 1] >= 2 for m in range(2, degree + 1, 2)),
        "even-extension infinity points were lost",
    )
    return counts


def boundary_parameters(q: int, T: Fraction, order: int, degree: int) -> Fraction:
    R.integer(q, 5, 7)
    need(q in (5, 7), "bounded source field required")
    R.integer(order, 1, 12)
    R.integer(degree, 2, 48)
    need(degree >= 2 * order, "cutoff must include the positive infinity-point term")
    T = C.exact(T)
    need(0 < q * T < 1, "fixed real positive T in the initial Euler disk required")
    return T


def constant_interval(
    source: dict[str, object], T: Fraction, order: int, degree: int
) -> tuple[Fraction, Fraction]:
    q = source["parameters_p_A_B"][0]
    T = boundary_parameters(q, T, order, degree)
    counts = closure_counts(source, degree)
    partial = sum(
        (
            Fraction(counts[m - 1], 2 * m**5) * T**m
            for m in range(order, degree + 1, order)
        ),
        Fraction(0),
    )
    h = q * T
    tail = 4 * h ** (degree + 1) / ((degree + 1) ** 5 * (1 - h))
    need(
        partial >= T ** (2 * order) / (2 * order) ** 5 > 0,
        "source geometric positivity lower bound failed",
    )
    return partial, partial + tail


def source_rational_functions(w):
    one_minus = add(ONE, scale(w, -1))
    fe = multiply(add(ONE, scale(w, 2)), inverse(power(one_minus, 4)))
    fs = inverse(power(add(ONE, scale(power(w, 2), -1)), 2))
    fc = inverse(add(ONE, scale(power(w, 3), -1)))
    return fe, fs, fc


def radial_functions(radius: Fraction, order: int, degree: int):
    radius = C.exact(radius)
    R.integer(order, 1, 3)
    R.integer(degree, 2, 32)
    need(0 < radius < 1, "strict radial source probe required")
    return _radial_functions(radius, order, degree)


@cache
def _radial_functions(radius: Fraction, order: int, degree: int):
    root = (ONE, scale(ONE, -1), OMEGA)[order - 1]
    z = scale(root, radius)
    w = ONE
    rows = []
    for _ in range(degree):
        w = multiply(w, z)
        rows.append(source_rational_functions(w))
    return tuple(rows)


def radial_control(
    source: dict[str, object],
    T: Fraction,
    radius: Fraction,
    order: int,
    degree: int = 24,
) -> dict[str, object]:
    q = source["parameters_p_A_B"][0]
    T = boundary_parameters(q, T, order, degree)
    values = radial_functions(radius, order, degree)
    radius = C.exact(radius)
    ed = G.frobenius_traces(source["polynomials"]["D"], degree)
    ee = G.frobenius_traces(source["polynomials"]["E"], degree)
    counts = closure_counts(source, degree)
    total = ZERO
    for m, (fe, fs, fc) in enumerate(values, 1):
        alpha = Fraction(counts[m - 1], 6)
        beta = Fraction(1 + q**m + ed[m - 1], 2)
        gamma = Fraction(1 + q**m - ed[m - 1] + ee[m - 1], 3)
        term = add(add(scale(fe, alpha), scale(fs, beta)), scale(fc, gamma))
        total = add(total, scale(term, T**m / m))
    scaled = scale(total, (1 - radius) ** 4)
    h = q * T
    tail = 8 * h ** (degree + 1) / ((degree + 1) * (1 - h))
    observed = real_part(scaled) - tail, real_part(scaled) + tail
    target = constant_interval(source, T, order, degree)
    need(
        observed[0] > target[1] / 2,
        "declared radial probe has not reached the certified positive leading regime",
    )
    return {
        "root_order": order,
        "radius": C.qjson(radius),
        "T": C.qjson(T),
        "power_cut": degree,
        "finite_scaled_log_Eisenstein_coordinate_intervals": pair_json(scaled),
        "scaled_log_absolute_tail": C.qjson(tail),
        "certified_real_scaled_log": C.interval_json(observed),
        "positive_limit_constant": C.interval_json(target),
        "source_infinity_lower_bound": C.qjson(T ** (2 * order) / (2 * order) ** 5),
        "finite_probe_real_part_above_half_positive_constant": True,
    }


def build_payload() -> dict[str, object]:
    authenticate_frozen()
    G.authenticate_frozen()
    for n in range(257):
        k, w = prefactor_exponents(n)
        need(
            k == sum(kappa(j) for j in range(n + 1)), "closed native K_N formula failed"
        )
        need(
            w == sum(j * kappa(j) for j in range(n + 1)),
            "closed native W_N formula failed",
        )
    for n, row in enumerate(S.source_rows(24)):
        a, b, c = row["multiplicities_1_sign_std"]
        need(
            kappa(n) == b + c - a,
            "prefactor exponent disagrees with genuine source sectors",
        )
    panels = []
    for q in (5, 7):
        source = G.native_source(q, 1, 1)
        T = Fraction(1, 2 * q)
        panels.append(
            {
                "source_parameters_p_A_B": source["parameters_p_A_B"],
                "closure_counts_first24_from_source_Frobenius": closure_counts(
                    source, 24
                ),
                "primitive_count_coverage": [1, 2],
                "finite_functional_equations": [
                    duality_control(source, n) for n in range(5)
                ],
                "boundary_constants": [
                    {
                        "order": order,
                        "constant_interval": C.interval_json(
                            constant_interval(source, T, order, 24)
                        ),
                    }
                    for order in range(1, 13)
                ],
                "radial_source_controls": [
                    radial_control(source, T, radius, order)
                    for radius in (Fraction(99, 100), Fraction(999, 1000))
                    for order in (1, 2, 3)
                ],
            }
        )
    return {
        "schema": "source-global-duality-and-grading-boundary-v1",
        "provenance": {
            "frozen_global_completion": FREEZE,
            "pins": [list(pin) for pin in PINS],
            "owned_sha256_lf": {
                name: digest((HERE / name).read_bytes()) for name in OWNED
            },
        },
        "finite_prefactor_formula_checked_through": 256,
        "prefactor_samples": [
            {"cut": n, "K_N_W_N": list(prefactor_exponents(n))}
            for n in (0, 1, 2, 3, 6, 24, 128, 256)
        ],
        "source_panels": panels,
        "scope": "fixed real 0<T<1/Q; grading-variable boundary only",
        "not_machine_proved": [
            "compact operator perfect-duality obstruction",
            "Hilbert-scale duality",
            "all-root source positivity",
            "root-of-unity density",
            "meromorphic natural boundary",
        ],
    }


def check_payload(candidate: object) -> None:
    need(
        json.dumps(candidate, sort_keys=True)
        == json.dumps(build_payload(), sort_keys=True),
        "global boundary fixture differs from authenticated complete replay",
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
            "global boundary fixture differs from complete replay",
        )
    print("PASS source global duality and grading-boundary exact replay")


if __name__ == "__main__":
    main()
