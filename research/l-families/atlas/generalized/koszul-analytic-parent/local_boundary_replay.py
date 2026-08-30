"""Exact local continuation residues and fractional-cutoff controls.

This producer has no prime-indexed Euler product. Prime indices below
are only exponents of one local source variable.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import subprocess
from fractions import Fraction
from functools import cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
FREEZE = "6365e26a5a77d2944e720470fec0b28855777f1c"
PREFIX = "research/l-families/atlas/generalized/koszul-analytic-parent/"
PINS = (
    (
        "nonscalar_replay.py",
        "2603e7b808907700b7f7d7f5b7036816f0126e9a",
        "ad46fa9184ea284c6106ee9b1304e31152b84820b5d1d948e9b46663214ae6a9",
    ),
    (
        "NONSCALAR_GRADE_RADIUS.md",
        "83f3cb6ebb3c4d6f9f4562ad4ad80c421245b17c",
        "3e5a340b3e7d30d354ad77f3151a5e049b98524dbc3323a5fddf569711fa2ca5",
    ),
)
OWNED = (
    "LOCAL_NATURAL_BOUNDARY.md",
    "LOCAL_BOUNDARY_REPLAY.md",
    "local_boundary_replay.py",
    "tests/test_local_boundary.py",
)
FIXTURE = HERE / "local_boundary.verification.json"


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
        need(resolved == blob, "frozen local dependency blob mismatch")
        frozen = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
        need(digest(frozen) == expected, "frozen local dependency hash mismatch")
        need(
            digest((HERE / name).read_bytes()) == expected,
            "working local dependency changed",
        )


authenticate_frozen()
SPEC = importlib.util.spec_from_file_location(
    "frozen_nonscalar_replay", HERE / "nonscalar_replay.py"
)
need(
    SPEC is not None and SPEC.loader is not None, "cannot load authenticated dependency"
)
N = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(N)
C, M, R = N.C, N.C.M, N.R


def gscale(value, factor):
    return value[0] * factor, value[1] * factor


def gpower(value, exponent: int):
    R.integer(exponent, 0, 2048)
    out = R.ONE
    while exponent:
        if exponent % 2:
            out = R.mul(out, value)
        value = R.mul(value, value)
        exponent //= 2
    return out


@cache
def deviation(q: int, n: int) -> int:
    R.integer(q, 2, 8)  # q=8 is the explicitly permitted source rank (2,9)
    R.integer(n, 1, 64)
    top = (-1) ** (n + 1) * sum(
        R.mobius(d) * (q + 2 + (-1) ** (n // d + 1) * q ** (n // d))
        for d in range(1, n + 1)
        if n % d == 0
    )
    need(top >= 0 and top % n == 0, "source deviation integrality failed")
    return top // n


def checked_case(q: int, p: int, tau: object, radius: object):
    R.integer(q, 2, 8)
    R.integer(p, 2, 6)
    need(
        isinstance(tau, tuple) and len(tau) == 2, "Gaussian-rational tau pair required"
    )
    tau = R.rational(tau[0]), R.rational(tau[1])
    radius = R.rational(radius)
    need(0 < radius < 1, "strict rational radius bound required")
    need(tau[0] ** 2 + tau[1] ** 2 <= radius**2, "claimed radius does not bound tau")
    need(
        gscale(gpower(tau, p), q) == R.neg(R.ONE), "tau must satisfy q*tau^p=-1 exactly"
    )
    need(
        q * radius ** (p + 1) < 1,
        "higher-power source tail is outside its convergence domain",
    )
    return tau, radius


def parent_constant(
    q: int, p: int, tau: object, radius: object, cut: int = 24, powers: int = 40
):
    tau, radius = checked_case(q, p, tau, radius)
    R.integer(cut, 2, 32)
    R.integer(powers, p + 1, 48)
    rho = Fraction(1, q)
    correction = (
        -sum(
            (deviation(q, n) * rho**n - Fraction(1, n) for n in range(1, cut + 1)),
            Fraction(0),
        )
        / p
    )
    middle = correction, Fraction(0)
    for n in range(1, cut + 1):
        eigenvalue = gpower(tau, n)
        current = gpower(eigenvalue, p)
        for j in range(p + 1, powers + 1):
            current = R.mul(current, eigenvalue)
            middle = R.add(
                middle, gscale(current, Fraction((-1) ** (n + 1) * deviation(q, n), j))
            )
    error = 2 * rho ** (cut // 2) / (p * (1 - rho))
    error += (
        3
        * (q * radius ** (p + 1)) ** (cut + 1)
        / ((p + 1) * (1 - radius) * (1 - q * radius ** (p + 1)))
    )
    error += (
        3
        * q
        * radius ** (powers + 1)
        / ((powers + 1) * (1 - radius) * (1 - q * radius ** (powers + 1)))
    )
    return middle, error


def adams_constant(
    q: int, p: int, tau: object, radius: object, indices: int = 40, powers: int = 40
):
    tau, radius = checked_case(q, p, tau, radius)
    R.integer(indices, p + 1, 48)
    R.integer(powers, 8, 48)
    rho = Fraction(1, q)
    real_log = N.log1p_interval(rho)
    real_mid = (real_log[0] + real_log[1]) / 2
    middle = -Fraction(q + 2, p) * real_mid, Fraction(0)
    error = Fraction(q + 2, p) * (real_log[1] - real_log[0]) / 2
    for index in range(p + 1, indices + 1):
        weight = Fraction(-M.a_coefficient(p, index), index)
        z = gpower(tau, index)
        current, scalar_log = R.ONE, R.ZERO
        for j in range(1, powers + 1):
            current = R.mul(current, z)
            scalar_log = R.add(
                scalar_log, gscale(current, Fraction(q + 2 + (-1) ** (j + 1) * q**j, j))
            )
        middle = R.add(middle, gscale(scalar_log, weight))
        error += (
            abs(weight)
            * 3
            * (q * radius**index) ** (powers + 1)
            / ((powers + 1) * (1 - q * radius**index))
        )
    error += (
        3
        * q
        * (p - 1)
        * radius ** (indices + 1)
        / ((indices + 1) * (1 - radius) * (1 - q * radius ** (p + 1)))
    )
    return middle, error


def complex_interval(middle, error):
    need(error >= 0, "negative enclosure radius")
    return {
        "real": C.interval_json((middle[0] - error, middle[0] + error)),
        "imaginary": C.interval_json((middle[1] - error, middle[1] + error)),
    }


def constant_control(q: int, p: int, tau: object, radius: object) -> dict[str, object]:
    tau, radius = checked_case(q, p, tau, radius)
    parent, parent_error = parent_constant(q, p, tau, radius)
    adams, adams_error = adams_constant(q, p, tau, radius)
    need(
        all(abs(parent[j] - adams[j]) <= parent_error + adams_error for j in (0, 1)),
        "independent source and Adams prefactor enclosures are disjoint",
    )
    return {
        "source_ranks": [2, q + 1],
        "q": q,
        "regularization_order": p,
        "tau": R.gjson(tau),
        "rational_norm_bound": R.qjson(radius),
        "tau_power_identity": R.gjson(gscale(gpower(tau, p), q)),
        "parent_log_G_interval": complex_interval(parent, parent_error),
        "Adams_log_G_interval": complex_interval(adams, adams_error),
        "parent_error": R.qjson(parent_error),
        "Adams_error": R.qjson(adams_error),
        "critical_exponent": [1, p],
        "cutoff_limit": "exp(-EulerGamma/p)*G_p(tau), with N^(1/p), no additional p factor",
        "ordinary_Sp_at_point": False,
        "cuts": {
            "source_grades": 24,
            "source_powers": 40,
            "Adams_indices": 40,
            "scalar_log_powers": 40,
        },
    }


def is_prime(n: int) -> bool:
    R.integer(n, 1, 64)
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))


def residue_control(p: int, index: int) -> dict[str, object]:
    R.integer(p, 2, 6)
    R.integer(index, 1, 64)
    primitive = Fraction(R.mobius(index), index)
    regularized = (
        Fraction(-M.a_coefficient(p, index), index) if index >= p else Fraction(0)
    )
    if index == p:
        need(regularized == Fraction(1, p), "first critical residue must be 1/p")
    if is_prime(index) and index >= p:
        need(regularized == Fraction(1, index), "prime lifted residue must be 1/index")
    return {
        "p": p,
        "index": index,
        "primitive_derivative_residue": R.qjson(primitive),
        "regularized_log_derivative_residue": R.qjson(regularized),
        "prime_index": is_prime(index),
        "nonintegral_regularized_monodromy_exponent": regularized.denominator != 1,
    }


def build_payload() -> dict[str, object]:
    authenticate_frozen()
    N.authenticate_frozen()
    C.authenticate_frozen()
    M.authenticate_frozen()
    R.authenticate()
    cases = (
        (4, 2, (Fraction(0), Fraction(1, 2)), Fraction(1, 2)),
        (8, 3, (Fraction(-1, 2), Fraction(0)), Fraction(1, 2)),
        (4, 4, (Fraction(1, 2), Fraction(1, 2)), Fraction(5, 7)),
    )
    return {
        "schema": "koszul-local-natural-boundary-v1",
        "provenance": {
            "frozen_nonscalar_commit": FREEZE,
            "pins": [list(pin) for pin in PINS],
            "owned_sha256_lf": {
                name: digest((HERE / name).read_bytes()) for name in OWNED
            },
        },
        "primitive_source": {
            "algebra": "Segre ranks (2,q+1), identity action, genuine quadratic-dual Lie parent",
            "q_cap": 8,
            "source_rank_second_factor_cap": 9,
            "p_cap": 6,
            "degree_cap": 64,
            "arithmetic": "integers and Gaussian fractions; directed rational enclosures",
        },
        "residue_controls": [
            residue_control(p, index) for p in range(2, 7) for index in range(1, 33)
        ],
        "fractional_cutoff_constants": [constant_control(*case) for case in cases],
        "not_machine_proved": [
            "infinitely many prime-index branch points",
            "dense unit-circle accumulation",
            "meromorphic natural boundary",
            "fractional critical-cutoff limit",
            "any arithmetic Euler-product statement",
        ],
    }


def check_payload(candidate: object) -> None:
    need(
        json.dumps(candidate, sort_keys=True)
        == json.dumps(build_payload(), sort_keys=True),
        "local continuation fixture differs from authenticated complete replay",
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
            "local continuation fixture differs from complete replay",
        )
    print("PASS local parent natural-boundary exact replay")


if __name__ == "__main__":
    main()
