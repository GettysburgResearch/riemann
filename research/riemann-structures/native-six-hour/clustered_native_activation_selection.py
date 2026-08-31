#!/usr/bin/env python3
"""Exact original-kernel cluster selection, including all physical factors."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from hashlib import sha1, sha256
from itertools import product
from math import isqrt, prod
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NOTE = HERE / "CLUSTERED_NATIVE_ACTIVATION_SELECTION.md"
FIXTURE = HERE / "clustered_native_activation_selection.json"
TEST = ROOT / "tests" / "test_native_six_hour_cluster_selection.py"
KERNEL_COMMIT = "033bc967f8fd9b5e23e00386dfe81e92b25dc012"
KERNEL_PATH = "research/riemann-structures/native-six-hour/native_activation_kernel.py"
KERNEL_BLOB = "1846674ad08e9f070cc6884c3928d619552f8011"
GE_COMMIT = "15967a52e846f1037bb0446db43f3d4a9c3fc821"
GE_PATH = "research/riemann-structures/native-six-hour/geodesic_factor_exchange.py"
GE_BLOB = "c88f87c164ab1ea5504913c00f257f5b030ab854"
MAX_BYTES = 1048576


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def frozen_bytes(commit, path, blob):
    ref = f"{commit}:{path}"
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
    require(
        len(raw) == size
        and sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest() == blob,
        "frozen source authentication",
    )
    return raw


def module_from_pin(commit, path, blob):
    raw = frozen_bytes(commit, path, blob)
    namespace = {
        "__name__": "authenticated_cluster_source",
        "__file__": str(ROOT / path),
    }
    # Execute only the exact frozen executable after commit/blob authentication.
    exec(compile(raw, str(ROOT / path), "exec"), namespace)  # noqa: S102
    return SimpleNamespace(**namespace)


def modules():
    return (
        module_from_pin(KERNEL_COMMIT, KERNEL_PATH, KERNEL_BLOB),
        module_from_pin(GE_COMMIT, GE_PATH, GE_BLOB),
    )


def validate_primes(primes):
    require(type(primes) is tuple and len(primes) == 3, "three literal prime labels")
    require(all(type(p) is int and 3 <= p <= 101 for p in primes), "bounded odd primes")
    require(primes[0] < primes[1] < primes[2], "ordered distinct labels")
    require(
        all(p % 2 and all(p % d for d in range(3, isqrt(p) + 1, 2)) for p in primes),
        "actual prime verification",
    )
    require(prod(primes) <= 1000000, "full-factor frequency ratio cap")
    require(
        (primes[0] * primes[1]) ** 2 > 8 * primes[2] ** 2, "cardinality-band separation"
    )
    require(primes[2] ** 2 <= 2 * primes[0] ** 2, "tight cluster radius")


def normalize_logs(kernel, value, primes):
    """Compare elementary logarithmic expressions by exact known valuations."""
    basis = (2,) + primes
    logs = {F(p): kernel.ZERO for p in basis}
    for base, coefficient in value[1].items():
        require(
            max(base.numerator.bit_length(), base.denominator.bit_length()) <= 128,
            "log valuation cap",
        )
        numerator, denominator = base.numerator, base.denominator
        for p in basis:
            exponent = 0
            while numerator % p == 0:
                numerator //= p
                exponent += 1
            while denominator % p == 0:
                denominator //= p
                exponent -= 1
            logs[F(p)] = kernel.qa(logs[F(p)], kernel.qs(coefficient, exponent))
        require(
            numerator == denominator == 1, "only declared logarithmic prime factors"
        )
    return kernel.expr(value[0], logs)


def closed_gamma(kernel, ratio):
    require(
        type(ratio) in (int, F) and ratio >= 1 and F(ratio) ** 2 <= 2,
        "small-shift closed formula domain",
    )
    ratio = F(ratio)
    gamma0 = kernel.expr(kernel.q(-288), {F(2): kernel.q(384, 128)})
    linear = kernel.expr(logs={ratio: kernel.q(-1152, -512)})
    exponential = kernel.qa(
        kernel.qs(kernel.q(288, 192), ratio - 1),
        kernel.qs(kernel.q(-576, -192), 1 / ratio - 1),
    )
    return kernel.ea(kernel.ea(gamma0, linear), kernel.expr(exponential))


def actual_records(geodesic, primes, powers):
    validate_primes(primes)
    require(
        type(powers) is tuple
        and len(powers) == 3
        and all(type(a) is int and 1 <= a <= 2 for a in powers),
        "declared bounded native power path",
    )
    activation = tuple(F(a, sum(powers)) for a in powers)
    K = prod(primes)
    records = []
    for bits in product((0, 1), repeat=3):
        left = [
            geodesic.local(bit, power) for bit, power in zip(bits, powers, strict=True)
        ]
        right = geodesic.polynomial_product(
            geodesic.local(1 - bit, power)
            for bit, power in zip(bits, powers, strict=True)
        )
        total, sites = F(), []
        for j, bit in enumerate(bits):
            if not bit:
                continue
            polynomial = geodesic.polynomial_product(
                [geodesic.derivative(left[j]), right] + left[:j] + left[j + 1 :]
            )
            coefficient = 2 * geodesic.integral(polynomial)
            sites.append(
                {
                    "prime": primes[j],
                    "integrand": [str(x) for x in polynomial],
                    "integrated_2ds": str(coefficient),
                }
            )
            total += coefficient
        require(
            total == -sum((activation[j] for j in range(3) if bits[j]), F()) / 4,
            "native chain-rule activation coefficient",
        )
        n = prod(p for p, bit in zip(primes, bits, strict=True) if bit)
        records.append(
            {
                "n": n,
                "m": K // n,
                "cardinality": sum(bits),
                "coefficient": str(total),
                "sites": sites,
            }
        )
    require(
        sum((F(row["coefficient"]) for row in records), F()) == -1,
        "complete native endpoint",
    )
    return records


def full_energy(kernel, primes, records):
    result = kernel.expr()
    for left in records:
        for right in records:
            gamma = kernel.gamma_square_ratio(F(left["n"], right["n"]))
            if left["cardinality"] != right["cardinality"]:
                require(gamma == kernel.expr(), "original-kernel band orthogonality")
            result = kernel.ea(
                result,
                kernel.es(gamma, F(left["coefficient"]) * F(right["coefficient"])),
            )
    return normalize_logs(kernel, kernel.es(result, F(1, prod(primes))), primes)


def band_energy(kernel, primes, activation):
    require(
        type(activation) is tuple
        and len(activation) == 3
        and all(type(x) in (int, F) and x >= 0 for x in activation)
        and sum(activation) == 1,
        "exact activation simplex",
    )
    value = kernel.gamma_square_ratio(F(1))
    for i in range(3):
        for j in range(3):
            value = kernel.ea(
                value,
                kernel.es(
                    kernel.gamma_square_ratio(F(primes[i], primes[j])),
                    activation[i] * activation[j]
                    + (1 - activation[i]) * (1 - activation[j]),
                ),
            )
    return normalize_logs(kernel, kernel.es(value, F(1, 16 * prod(primes))), primes)


def expression_json(value):
    return {
        "constant_Q_sqrt2": [str(x) for x in value[0]],
        "log_terms": [
            {"base": str(base), "coefficient_Q_sqrt2": [str(x) for x in coefficient]}
            for base, coefficient in sorted(value[1].items())
        ],
    }


def cusp_certificate(kernel):
    jumps = (kernel.q(4), kernel.q(-8, -4), kernel.q(4, 8), kernel.q(0, -4))
    half_square_sum = kernel.q()
    for jump in jumps:
        half_square_sum = kernel.qa(
            half_square_sum, kernel.qs(kernel.qm(jump, jump), F(1, 2))
        )
    require(half_square_sum == kernel.q(144, 64), "independent native jump cusp")
    A1, B1 = kernel.q(288, 192), kernel.q(576, 192)
    at_zero = kernel.qs(kernel.qa(A1, kernel.qs(B1, -1)), F(1, 4))
    at_log2 = kernel.qs(
        kernel.qa(
            kernel.qm(A1, kernel.q(0, 1)),
            kernel.qs(kernel.qm(B1, kernel.q(0, F(1, 2))), -1),
        ),
        F(1, 4),
    )
    require(
        at_zero == kernel.q(-72) and at_log2 == kernel.q(48),
        "exact second derivative endpoints",
    )
    require(kernel.log_interval(F(2))[1] < F(7, 10), "certified elementary log2 bound")
    require(F(7, 5) ** 2 < 2, "elementary sqrt2 lower bound")
    margin = 144 + 64 * F(7, 5) - 324 * F(7, 10)
    require(
        margin == F(34, 5) and 2 * margin / 576 == F(17, 720),
        "strict universal improvement constant",
    )
    return {
        "jump_squared_half_sum": [str(x) for x in half_square_sum],
        "Gamma_second_derivative_at_0": -72,
        "Gamma_second_derivative_at_log2": 48,
        "Taylor_remainder_constant": 36,
        "strict_gap_constant": "17/720",
    }


def panel(kernel, geodesic, primes):
    validate_primes(primes)
    equalities = []
    for i in range(3):
        for j in range(i, 3):
            ratio = F(primes[j], primes[i])
            primitive = normalize_logs(kernel, kernel.gamma_square_ratio(ratio), primes)
            closed = normalize_logs(kernel, closed_gamma(kernel, ratio), primes)
            require(
                primitive == closed,
                "independent nine-overlap equals closed cusp formula",
            )
            equalities.append(
                {"ratio": str(ratio), "exact_Gamma": expression_json(closed)}
            )
    uniform_records = actual_records(geodesic, primes, (1, 1, 1))
    selected_records = actual_records(geodesic, primes, (1, 2, 1))
    uniform = full_energy(kernel, primes, uniform_records)
    selected = full_energy(kernel, primes, selected_records)
    require(
        uniform == band_energy(kernel, primes, (F(1, 3),) * 3),
        "complete uniform source energy",
    )
    require(
        selected == band_energy(kernel, primes, (F(1, 4), F(1, 2), F(1, 4))),
        "complete selected source energy",
    )
    gap = normalize_logs(kernel, kernel.ea(uniform, kernel.es(selected, -1)), primes)
    K = prod(primes)
    formula = kernel.es(kernel.gamma_square_ratio(F(1)), -3)
    for ratio, coefficient in (
        (F(primes[1], primes[0]), 4),
        (F(primes[2], primes[1]), 4),
        (F(primes[2], primes[0]), -5),
    ):
        formula = kernel.ea(
            formula, kernel.es(kernel.gamma_square_ratio(ratio), coefficient)
        )
    formula = normalize_logs(kernel, kernel.es(formula, F(1, 576 * K)), primes)
    require(gap == formula, "exact source improvement formula")
    gap_interval = kernel.ei(gap)
    w = kernel.log_interval(F(primes[2], primes[0]))
    lower_bound = kernel.im(w, kernel.point(F(17, 720 * K)))
    require(
        gap_interval[0] > lower_bound[1] > 0,
        "strict physically normalized source improvement",
    )
    return {
        "primes": primes,
        "K": K,
        "all_eight_uniform_source_records": uniform_records,
        "all_eight_selected_source_records": selected_records,
        "closed_primitive_kernel_equalities": equalities,
        "uniform_physical_energy": expression_json(uniform),
        "selected_physical_energy": expression_json(selected),
        "exact_physical_improvement": expression_json(gap),
        "certified_improvement_interval": kernel.summarize_interval(gap_interval),
        "theorem_lower_bound_interval": kernel.summarize_interval(lower_bound),
        "uniform_source_powers": (1, 1, 1),
        "selected_source_powers": (1, 2, 1),
    }


def replay_equal(candidate, expected):
    require(canonical(candidate) == canonical(expected), "typed canonical replay")


def build():
    kernel, geodesic = modules()
    kernel.authenticate()
    source_key = (
        geodesic.OLD,
        "claims/lemmas/L-102707-continuous-half-divisor-geodesic-and-polarized-hankel-current.md",
    )
    geodesic.source_bytes(source_key)
    certificates = [
        panel(kernel, geodesic, primes) for primes in ((71, 73, 79), (41, 43, 47))
    ]
    bindings = {}
    for path in (NOTE, Path(__file__), TEST):
        raw = path.read_bytes()
        require(len(raw) <= MAX_BYTES, "owned byte cap")
        bindings[path.relative_to(ROOT).as_posix()] = sha256(
            raw.replace(b"\r\n", b"\n")
        ).hexdigest()
    result = {
        "schema": "riemann.native_six_hour.cluster_selection.v1",
        "source_hashes": bindings,
        "sources": [
            {"commit": KERNEL_COMMIT, "path": KERNEL_PATH, "blob": KERNEL_BLOB},
            {"commit": GE_COMMIT, "path": GE_PATH, "blob": GE_BLOB},
            {
                "commit": kernel.SOURCE_COMMIT,
                "path": kernel.SOURCE_PATH,
                "blob": kernel.SOURCE_BLOB,
            },
            {
                "commit": source_key[0],
                "path": source_key[1],
                "blob": geodesic.SOURCES[source_key],
            },
        ],
        "cusp": cusp_certificate(kernel),
        "panels": certificates,
        "original_Mellin_measure_and_physical_normalization": True,
        "all_factor_allocations_retained": True,
        "cofinal_claim_is_finite_fixture_extrapolation": False,
        "independent_tuple_optimizers_assembled_as_one_path": False,
        "full_post_renewal_gamma_identified": False,
        "full_principal_moment_estimate_claimed": False,
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
        require(FIXTURE.stat().st_size <= MAX_BYTES, "fixture byte cap")
        replay_equal(json.loads(FIXTURE.read_text(encoding="utf-8")), result)
    print(f"PASS native cluster selection {result['proof_object_sha256']}")


if __name__ == "__main__":
    main()
