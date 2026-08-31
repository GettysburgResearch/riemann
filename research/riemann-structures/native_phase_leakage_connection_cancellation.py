#!/usr/bin/env python3
"""Source-authenticated exact cancellation of a selector-changing gauge column."""

from __future__ import annotations

import argparse
import json
import subprocess
import types
from fractions import Fraction
from hashlib import sha1, sha256
from math import factorial, isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NOTE = HERE / "NATIVE_PHASE_LEAKAGE_CONNECTION_CANCELLATION.md"
FIXTURE = HERE / "native_phase_leakage_connection_cancellation.json"
TEST = ROOT / "tests" / "test_native_phase_leakage_connection_cancellation.py"
EA = "5ef9a0800e7d0f03bfef1ad4ba467f8843a90058"
PSG = "ce0cc6e48e3cdaedd9d5f52fb087b03e8f86c257"
EA_PATH = "research/riemann-structures/euler_activation_source_adapter.py"
PSG_PATH = "research/riemann-structures/principal_selector_gauge_obstruction.py"
FAMILY = "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b"
OLD = "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc"
SOURCES = {
    (EA, EA_PATH): "f8248cd97c4fc72ad4034d9baf83cec91396f27e",
    (PSG, PSG_PATH): "5007fc3a3a6f5cff1d7aaacece78829ec6e4616d",
    (
        EA,
        "research/riemann-structures/EULER_ACTIVATION_SOURCE_ADAPTER.md",
    ): "8632b4442b9610535078ef55a97b46a77a342dfe",
    (
        "e501c45ecc39f71b3f26abfe952366eb529c7c2d",
        "research/riemann-structures/GAUGE_CONNECTION_SOURCE_TRANSPORT.md",
    ): "35390e5f48304e8c586c1268b8ae215bbb252aaf",
    (
        PSG,
        "research/riemann-structures/PRINCIPAL_SELECTOR_GAUGE_OBSTRUCTION.md",
    ): "a4757412c5e9d085e2970e768cbb1d5c4953e554",
    (
        OLD,
        "claims/lemmas/L-102706-euler-half-divisor-homotopies-are-subcritically-gauge-equivalent.md",
    ): "6192bec36636e2d35b2aba4fdd64eb4bcf93c2d9",
    (
        OLD,
        "claims/lemmas/L-102746-wick-tail-has-a-canonical-equal-pair-owner.md",
    ): "db018c64dde45ff4ad17541eb6ba00b4f6fa9d49",
    (
        FAMILY,
        "claims/lemmas/L-106080-squarefree-boolean-vaughan-keeps-the-balanced-core-literal.md",
    ): "346cc52420ec65457c2a5accc045d4a85635cc24",
    (
        FAMILY,
        "claims/lemmas/L-106090-least-discrepancy-prime-triangularizes-the-coprime-boolean-core.md",
    ): "dadf3a4a65d2575983d692dafc0c94142c9a038d",
    (
        FAMILY,
        "claims/lemmas/L-106120-bilateral-least-prime-phases-form-a-tensor-kummer-family.md",
    ): "a8d829dc10611adb7bfb4853902bdff0ab02a065",
    (
        FAMILY,
        "claims/lemmas/L-106121-bilateral-tensor-moment-has-a-paid-atomic-diagonal.md",
    ): "955c3ed0363ca330439eedbae1bf0041a4c96468",
    (
        FAMILY,
        "claims/theorems/T-106140-wick-centered-additive-kummer-conjunction-frontier.md",
    ): "d5be8e376c88b63de0be19e0d9e8791624e99ae2",
}
MAX_BYTES = 262144
ZERO, ONE = Fraction(0), Fraction(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def canonical(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def source_bytes(key):
    require(key in SOURCES, "frozen primitive identity")
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
    require(digest == SOURCES[key], "frozen primitive Git blob")
    return raw


def load_primitive(key, raw):
    require(key in ((EA, EA_PATH), (PSG, PSG_PATH)), "executable primitive identity")
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "executable bytes cap")
    digest = sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    require(digest == SOURCES[key], "executable primitive Git blob")
    module = types.ModuleType("frozen_phase_leakage_primitive")
    module.__file__ = str(ROOT / key[1])
    # Only the fixed Git bytes above are executed after their blob is rehashed.
    exec(compile(raw, f"{key[0]}:{key[1]}", "exec"), module.__dict__)  # noqa: S102
    return module


def beta(j: int, k: int) -> Fraction:
    require(
        type(j) is int and type(k) is int and 1 <= j <= 40 and 1 <= k <= 40,
        "beta integer/range cap",
    )
    return Fraction(factorial(j - 1) * factorial(k - 1), factorial(j + k - 1))


def scaled(algebra, poly, factor: Fraction):
    require(type(factor) is Fraction, "exact scale")
    return algebra.trim(tuple(factor * x for x in algebra.trim(poly)))


def activation_column(algebra, owners: int = 4, cores: int = 6, p: int = 3):
    require(
        type(owners) is int
        and type(cores) is int
        and 1 <= owners <= 8
        and 1 <= cores <= 12,
        "activation-depth cap",
    )
    require(type(p) is int and 2 <= p <= 1000000, "physical insertion integer cap")
    require(all(p % d for d in range(2, isqrt(p) + 1)), "physical insertion prime")
    t, s = (ZERO, ONE), (ONE, -ONE)
    sign = Fraction((-1) ** (owners + cores))
    f = scaled(
        algebra,
        algebra.multiply(algebra.power(t, owners), algebra.power(s, cores)),
        sign,
    )
    owner_site = scaled(
        algebra,
        algebra.multiply(algebra.power(t, owners - 1), algebra.power(s, cores)),
        sign,
    )
    core_site = scaled(
        algebra,
        algebra.multiply(algebra.power(t, owners), algebra.power(s, cores - 1)),
        -sign,
    )
    b = scaled(algebra, algebra.multiply(t, s), Fraction(-1, 4 * p))
    owner = algebra.multiply(b, algebra.scale(owner_site, owners))
    core = algebra.multiply(b, algebra.scale(core_site, cores))
    connection = algebra.multiply(algebra.derivative(b), f)
    transport = algebra.add(owner, core)
    full = algebra.add(transport, connection)
    require(
        full == algebra.derivative(algebra.multiply(b, f)), "literal gauge product rule"
    )
    values = [algebra.integral(poly) for poly in (owner, core, connection)]
    beta_values = [
        sign * Fraction(-owners, 4 * p) * beta(owners + 1, cores + 2),
        sign * Fraction(cores, 4 * p) * beta(owners + 2, cores + 1),
        sign
        * Fraction(-1, 4 * p)
        * (beta(owners + 1, cores + 1) - 2 * beta(owners + 2, cores + 1)),
    ]
    require(values == beta_values and sum(values) == 0, "independent beta cancellation")
    weighted = algebra.integral(algebra.multiply(t, full))
    require(
        weighted == -algebra.integral(algebra.multiply(b, f)),
        "nonconstant density integration by parts",
    )
    d_two = (values[0] + values[1]) ** 2 + values[2] ** 2
    d_three = sum(value * value for value in values)
    d_sites = values[0] ** 2 / owners + values[1] ** 2 / cores + values[2] ** 2
    primitive_d = algebra.integral(
        algebra.add(
            algebra.add(
                algebra.multiply(transport, transport),
                algebra.multiply(connection, connection),
            ),
            (ZERO,),
        )
    )
    return {
        "owner_count": owners,
        "core_count": cores,
        "inserted_prime": p,
        "input_polynomial": [str(x) for x in f],
        "gauge_polynomial": [str(x) for x in b],
        "owner_transport_polynomial": [str(x) for x in owner],
        "core_transport_polynomial": [str(x) for x in core],
        "connection_polynomial": [str(x) for x in connection],
        "integrated_three_terms": [str(x) for x in values],
        "beta_integral_route": [str(x) for x in beta_values],
        "integrated_total": "0",
        "tau_density_residual": str(weighted),
        "two_mechanism_diagonal": str(d_two),
        "three_group_diagonal": str(d_three),
        "individual_activation_site_diagonal": str(d_sites),
        "two_mechanism_continuous_tau_diagonal": str(primitive_d),
        "owner_plus_connection_residual": str(values[0] + values[2]),
        "transport_without_connection_residual": str(values[0] + values[1]),
    }


def build():
    raw = {key: source_bytes(key) for key in SOURCES}
    algebra = load_primitive((EA, EA_PATH), raw[(EA, EA_PATH)])
    selector = load_primitive((PSG, PSG_PATH), raw[(PSG, PSG_PATH)])
    column = activation_column(algebra)
    u = Fraction(1, 166320)
    require(
        [Fraction(x) for x in column["integrated_three_terms"]]
        == [-14 * u, 15 * u, -u],
        "native three-term coefficient",
    )
    require(
        Fraction(column["tau_density_residual"]) == Fraction(1, 123552),
        "weighted homotopy countercontrol",
    )
    require(
        Fraction(column["two_mechanism_diagonal"]) == 2 * u * u
        and Fraction(column["three_group_diagonal"]) == 422 * u * u
        and Fraction(column["individual_activation_site_diagonal"])
        == Fraction(175, 2) * u * u,
        "three distinct integrated diagonal resolutions",
    )
    transition = selector.insertion((5, 1009, 1021), (3, 1201, 1223), 3, Fraction(1, 2))
    before, after = transition["before"], transition["after"]
    require(
        (before["ell"], before["rho"], after["ell"], after["rho"]) == (5, 3, 5, 1201),
        "actual off-phase output",
    )
    amplitude_square = Fraction(1, before["N"] * before["M"])
    observed_common = Fraction(after["weight"]) * amplitude_square * u * u
    v = (-14, 15, -1)
    gram = [[observed_common * a * b for b in v] for a in v]
    require(
        sum(sum(row) for row in gram) == 0 and sum(gram[i][i] for i in range(3)) > 0,
        "common observed Gram cancels but literal diagonal survives",
    )
    hashes = {}
    for path in (NOTE, Path(__file__), TEST):
        data = path.read_bytes()
        require(len(data) <= MAX_BYTES, "local source cap")
        hashes[path.relative_to(ROOT).as_posix()] = sha256(
            data.replace(b"\r\n", b"\n")
        ).hexdigest()
    result = {
        "schema": "riemann.native_phase_leakage_connection.v1",
        "sources": [
            {"commit": key[0], "path": key[1], "git_blob": blob}
            for key, blob in SOURCES.items()
        ],
        "source_hashes": hashes,
        "actual_source_column": column,
        "native_selector_transition": transition,
        "input_amplitude_square": str(amplitude_square),
        "observed_gram_divided_by_Gamma0": [[str(x) for x in row] for row in gram],
        "observed_three_group_diagonal_divided_by_Gamma0": str(422 * observed_common),
        "observed_two_mechanism_diagonal_divided_by_Gamma0": str(2 * observed_common),
        "observed_individual_site_diagonal_divided_by_Gamma0": str(
            Fraction(175, 2) * observed_common
        ),
        "common_output_mellin_ratio": str(Fraction(after["N"], after["M"])),
        "conjugated_left_mellin_shift": "9^(it)",
        "unconjugated_left_mellin_shift": "9^(-it)",
        "all_three_terms_share_physical_output_and_primitive_phase": True,
        "tau_dependent_density_correction_retained": True,
        "full_T106140_balanced_gamma_adapter_asserted": False,
        "literal_native_diagonal_resolution_identified": False,
        "complete_integrated_connection_column_cancels": True,
        "RH_conclusion": False,
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    return result


def main():
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
        require(FIXTURE.stat().st_size <= MAX_BYTES, "artifact cap")
        candidate = json.loads(FIXTURE.read_text(encoding="utf-8"))
        require(canonical(candidate) == canonical(result), "exact canonical replay")
    print(
        json.dumps(
            {"status": "PASS", "proof_object_sha256": result["proof_object_sha256"]}
        )
    )


if __name__ == "__main__":
    main()
