#!/usr/bin/env python3
"""Exact native gauge-connection coefficients, observations, and diagonals."""

from __future__ import annotations

import argparse
import json
import subprocess
import types
from fractions import Fraction
from hashlib import sha1, sha256
from math import comb, factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NOTE = HERE / "GAUGE_CONNECTION_SOURCE_TRANSPORT.md"
FIXTURE = HERE / "gauge_connection_source_transport.json"
TEST = ROOT / "tests" / "test_gauge_connection_source_transport.py"
EA = "5ef9a0800e7d0f03bfef1ad4ba467f8843a90058"
ALGEBRA_PATH = "research/riemann-structures/euler_activation_source_adapter.py"
SOURCES = {
    (
        EA,
        "research/riemann-structures/EULER_ACTIVATION_SOURCE_ADAPTER.md",
    ): "8632b4442b9610535078ef55a97b46a77a342dfe",
    (EA, ALGEBRA_PATH): "f8248cd97c4fc72ad4034d9baf83cec91396f27e",
    (
        EA,
        "research/riemann-structures/euler_activation_source_adapter.json",
    ): "fd263b3d49e82daf9171297c635259a48ab4164d",
    (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102706-euler-half-divisor-homotopies-are-subcritically-gauge-equivalent.md",
    ): "6192bec36636e2d35b2aba4fdd64eb4bcf93c2d9",
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/theorems/T-106140-wick-centered-additive-kummer-conjunction-frontier.md",
    ): "d5be8e376c88b63de0be19e0d9e8791624e99ae2",
}
MAX_BYTES = 262144
_ALGEBRA = None


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def canonical(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def source_bytes(key: tuple[str, str]) -> bytes:
    require(key in SOURCES, "frozen source identity")
    ref = f"{key[0]}:{key[1]}"
    size = int(
        subprocess.run(
            ["git", "cat-file", "-s", ref],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout
    )
    require(0 < size <= MAX_BYTES, "source byte cap")
    raw = subprocess.run(
        ["git", "show", ref], cwd=ROOT, capture_output=True, check=True
    ).stdout
    require(len(raw) == size, "source byte count")
    digest = sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest()
    require(digest == SOURCES[key], "frozen source Git blob")
    return raw


def load_algebra():
    global _ALGEBRA
    if _ALGEBRA is None:
        raw = source_bytes((EA, ALGEBRA_PATH))
        module = types.ModuleType("frozen_euler_activation_algebra")
        module.__file__ = str(ROOT / ALGEBRA_PATH)
        # Only the exact hard-coded, rehashed Git blob above is executable here;
        # the working-tree file and user-supplied paths are never imported.
        exec(compile(raw, f"{EA}:{ALGEBRA_PATH}", "exec"), module.__dict__)  # noqa: S102
        _ALGEBRA = module
    return _ALGEBRA


def scalar(poly, value: Fraction):
    require(type(value) is Fraction, "exact rational scale")
    return load_algebra().trim(tuple(value * x for x in poly))


def beta(first: int, second: int) -> Fraction:
    require(
        type(first) is int
        and type(second) is int
        and 1 <= first <= 40
        and 1 <= second <= 40,
        "beta work cap",
    )
    return Fraction(
        factorial(first - 1) * factorial(second - 1), factorial(first + second - 1)
    )


def local_record() -> dict[str, object]:
    m = load_algebra()
    one, zero = (Fraction(1),), (Fraction(0),)
    tau = (Fraction(0), Fraction(1))
    # Coefficients in x of tau*sqrt(1-x)+(1-tau)*sqrt(1-x^2).
    half = [one, scalar(tau, Fraction(-1, 2)), (Fraction(-1, 2), Fraction(3, 8))]
    h = []
    for degree in range(3):
        value = zero
        for left in range(degree + 1):
            value = m.add(value, m.multiply(half[left], half[degree - left]))
        h.append(value)
    e = [one, scalar(tau, Fraction(-1)), (Fraction(-1), Fraction(1))]
    g = [one]
    for degree in (1, 2):
        value = h[degree]
        for left in range(1, degree + 1):
            value = m.add(
                value, scalar(m.multiply(e[left], g[degree - left]), Fraction(-1))
            )
        g.append(value)
    require(
        h[1] == (Fraction(0), Fraction(-1)), "literal half-divisor linear coefficient"
    )
    require(
        h[2] == (Fraction(-1), Fraction(3, 4), Fraction(1, 4)),
        "literal quadratic coefficient",
    )
    require(
        g[1] == zero and g[2] == (Fraction(0), Fraction(-1, 4), Fraction(1, 4)),
        "actual frozen gauge coefficient",
    )
    return {
        "h_x_coefficients": [[str(x) for x in poly] for poly in h],
        "g_x_coefficients": [[str(x) for x in poly] for poly in g],
        "g_quadratic_tau_derivative": [str(x) for x in m.derivative(g[2])],
    }


def connection_record(k: int) -> dict[str, object]:
    require(type(k) is int and 1 <= k <= 16, "nonempty core depth cap")
    m = load_algebra()
    tau = (Fraction(0), Fraction(1))
    tau2, tau4 = m.power(tau, 2), m.power(tau, 4)
    v = (Fraction(1), Fraction(-3, 4), Fraction(-1, 4))
    odd = (Fraction(1), Fraction(-2))
    mu = Fraction((-1) ** k)
    owner = scalar(m.multiply(tau, m.power(v, k)), 2 * mu)
    core_a = scalar(m.multiply(tau2, m.power(v, k - 1)), -k * mu)
    a = m.add(owner, core_a)
    b = scalar(m.multiply(m.multiply(tau2, odd), m.power(v, k - 1)), mu * k / 4)
    full = m.derivative(scalar(m.multiply(tau2, m.power(v, k)), mu))
    require(m.add(a, b) == full, "full derivative including connection")
    ai, bi, oi = m.integral(a), m.integral(b), m.integral(owner)
    require(ai + bi == 0, "complete mixed-core cancellation")
    owner_beta = (
        2
        * mu
        * sum(
            (Fraction(comb(k, j), 4**j) * beta(j + 2, k + 1) for j in range(k + 1)),
            Fraction(0),
        )
    )
    connection_beta = (
        mu
        * k
        / 4
        * sum(
            (
                Fraction(comb(k - 1, j), 4**j) * (beta(j + 3, k) - 2 * beta(j + 4, k))
                for j in range(k)
            ),
            Fraction(0),
        )
    )
    require(oi == owner_beta and bi == connection_beta, "independent beta expansion")
    common = m.multiply(tau4, m.power(v, 2 * k - 2))
    owner_diagonal = scalar(m.multiply(tau2, m.power(v, 2 * k)), Fraction(2))
    bracket = m.add((Fraction(1),), scalar(m.multiply(odd, odd), Fraction(1, 16)))
    expanded_diagonal = m.add(
        owner_diagonal, scalar(m.multiply(common, bracket), Fraction(k))
    )
    vp = m.derivative(v)
    original_diagonal = m.add(
        owner_diagonal, scalar(m.multiply(common, m.multiply(vp, vp)), Fraction(k))
    )
    correction = scalar(m.multiply(common, odd), Fraction(-k, 2))
    require(
        m.add(original_diagonal, scalar(expanded_diagonal, Fraction(-1))) == correction,
        "literal derivative-site diagonal transport",
    )
    require(
        m.integral(original_diagonal) > 0 and m.integral(expanded_diagonal) > 0,
        "positive primitive diagonals",
    )
    return {
        "core_depth": k,
        "transported_Euler_density": [str(x) for x in a],
        "connection_density": [str(x) for x in b],
        "transported_Euler_integral": str(ai),
        "connection_integral": str(bi),
        "half_divisor_owner_integral": str(oi),
        "Euler_owner_integral": str(Fraction((-1) ** k, comb(k + 2, 2))),
        "connection_to_half_owner_ratio": str(bi / oi),
        "observed_Gram_coefficient_times_N_over_Gamma0": str(bi * bi),
        "observed_Gram_sign_matrix": [[1, -1], [-1, 1]],
        "integrated_two_sector_diagonal_times_N_over_Gamma0": str(2 * bi * bi),
        "primitive_expanded_diagonal_times_N": str(m.integral(expanded_diagonal)),
        "primitive_H_diagonal_times_N": str(m.integral(original_diagonal)),
        "primitive_diagonal_correction_times_N": str(m.integral(correction)),
    }


def build() -> dict[str, object]:
    raw = {key: source_bytes(key) for key in SOURCES}
    old = json.loads(
        raw[(EA, "research/riemann-structures/euler_activation_source_adapter.json")]
    )
    require(
        old["proof_object_sha256"]
        == "e9e95f790e92502bc0adb264f51272e186d7b53d5de2b0c004a8308270c0c6e0",
        "frozen Euler adapter proof",
    )
    local = local_record()
    records = [connection_record(k) for k in range(1, 17)]
    require(
        records[0]["transported_Euler_integral"] == "-1/24"
        and records[0]["connection_integral"] == "1/24",
        "nonzero native connection witness",
    )
    require(
        records[2]["half_divisor_owner_integral"] == "-229/1792",
        "actual subcritical depth coefficient",
    )
    hashes = {}
    for path in (NOTE, Path(__file__), TEST):
        data = path.read_bytes()
        require(len(data) <= MAX_BYTES, "local source byte cap")
        hashes[path.relative_to(ROOT).as_posix()] = sha256(
            data.replace(b"\r\n", b"\n")
        ).hexdigest()
    result = {
        "schema": "riemann.gauge_connection_transport.v1",
        "sources": [
            {"commit": key[0], "path": key[1], "git_blob": blob}
            for key, blob in SOURCES.items()
        ],
        "source_hashes": hashes,
        "arithmetic": "EXACT_RATIONAL_POLYNOMIAL",
        "literal_local_gauge": local,
        "complete_coefficient_and_diagonal_controls": records,
        "cofinal_depth_limits_proved_in_note": {
            "k2_half_owner_over_mu": "32/9",
            "k2_connection_over_mu": "32/27",
            "connection_over_half_owner": "1/3",
            "half_owner_over_Euler_owner": "16/9",
        },
        "new_geometric_or_prime_search": False,
        "all_retained_T106140_assembly_identified": False,
        "conductor_amplified_first_jet_bound_asserted": False,
        "RH_conclusion": False,
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.write:
        FIXTURE.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    else:
        require(FIXTURE.stat().st_size <= MAX_BYTES, "artifact byte cap")
        candidate = json.loads(FIXTURE.read_text(encoding="utf-8"))
        require(canonical(candidate) == canonical(result), "canonical exact replay")
    print(
        json.dumps(
            {"status": "PASS", "proof_object_sha256": result["proof_object_sha256"]}
        )
    )


if __name__ == "__main__":
    main()
