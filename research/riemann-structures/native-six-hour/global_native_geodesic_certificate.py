#!/usr/bin/env python3
"""Full finite native-source improvements and an exterior-curvature parent."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from hashlib import sha1, sha256
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NOTE = HERE / "GLOBAL_NATIVE_GEODESIC_VARIATION.md"
FIXTURE = HERE / "global_native_geodesic_certificate.json"
TEST = ROOT / "tests" / "test_native_six_hour_global_geodesic.py"
COMMIT = "5d7ea752ee84765a7690bdc36bb2bbcaddb38bb4"
SCOUT = "research/riemann-structures/native-six-hour/global_geodesic_scout.py"
SCOUT_BLOB = "32a4c01750e99a37c4d1992fa6bddafeaea8fe06"
DISCOVERY = "research/riemann-structures/native-six-hour/global_geodesic.discovery.json"
DISCOVERY_BLOB = "86d7301d1fd510d4b0f6d47f3e660d4f81695b2f"
PREREG = (
    "research/riemann-structures/native-six-hour/GLOBAL_GEODESIC_PREREGISTRATION.md"
)
PREREG_BLOB = "e6206bc344082b1ad1398bfc0ddc793df0d5a993"
MAX_BYTES = 2097152


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def frozen_bytes(path, blob):
    ref = f"{COMMIT}:{path}"
    size = int(
        subprocess.run(
            ["git", "cat-file", "-s", ref],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout
    )
    require(0 < size <= MAX_BYTES, "frozen byte cap")
    raw = subprocess.run(
        ["git", "show", ref], cwd=ROOT, capture_output=True, check=True
    ).stdout
    require(
        len(raw) == size
        and sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest() == blob,
        "exact frozen source authentication",
    )
    return raw


def scout_module():
    raw = frozen_bytes(SCOUT, SCOUT_BLOB)
    namespace = {
        "__name__": "authenticated_global_source",
        "__file__": str(ROOT / SCOUT),
    }
    # Only the exact frozen executable is compiled after commit/blob authentication.
    exec(compile(raw, str(ROOT / SCOUT), "exec"), namespace)  # noqa: S102
    return SimpleNamespace(**namespace)


def component(module, polynomial, degree):
    require(type(degree) is int and degree in (0, 1), "affine source component")
    return module.bp(
        {
            (0, s): value
            for (epsilon, s), value in polynomial.items()
            if epsilon == degree
        }
    )


def negate(module, polynomial):
    return module.bp({key: -value for key, value in polynomial.items()})


def curvature_control(module, native_records):
    numbers = module.panel_numbers()
    sources = {p: {n: module.source(n, p)[0] for n in numbers} for p in module.PRIMES}
    A = {n: component(module, sources[2][n], 0) for n in numbers}
    B = {
        p: {n: component(module, sources[p][n], 1) for n in numbers}
        for p in module.PRIMES
    }
    eta = module.bp({(0, 1): 1, (0, 2): -1})
    for n in numbers:
        total = module.bp()
        for p in module.PRIMES:
            require(
                component(module, sources[p][n], 0) == A[n],
                "same full undeformed source",
            )
            require(
                all(epsilon <= 1 for epsilon, _ in sources[p][n]),
                "one-prime source affine before integration",
            )
            require(
                B[p][n].get((0, 0), 0) == 0 and sum(B[p][n].values(), F()) == 0,
                "endpoint-zero actual source displacement",
            )
            total = module.ba(total, B[p][n])
        require(
            total == module.bm(eta, module.bd(A[n])),
            "pointwise common-reparametrization source identity",
        )
    records = []
    nonzero = {p: [0, 0] for p in module.PRIMES}
    for row_index, original in enumerate(native_records[2]):
        n, m = original["n"], original["m"]
        all_first = F()
        pointwise_sum = module.bp()
        values = {}
        for p in module.PRIMES:
            bracket = module.ba(
                module.bm(module.bd(A[n]), B[p][m]),
                negate(module, module.bm(B[p][n], module.bd(A[m]))),
            )
            first = module.bi(bracket)[0]
            second_bracket = module.ba(
                module.bm(module.bd(B[p][n]), B[p][m]),
                negate(module, module.bm(B[p][n], module.bd(B[p][m]))),
            )
            # Integrating the straight deformation surface contributes integral_0^1 r dr=1/2.
            second = module.bi(second_bracket)[0] / 2
            expected = native_records[p][row_index]
            require(
                (expected["n"], expected["m"]) == (n, m),
                "complete ordered-record alignment",
            )
            require(
                (first, second)
                == tuple(
                    F(x)
                    for x in expected["epsilon_coefficients_before_physical_weight"][1:]
                ),
                "independent curvature/Stokes equals complete source derivative",
            )
            pointwise_sum = module.ba(pointwise_sum, bracket)
            all_first += first
            nonzero[p][0] += first != 0
            nonzero[p][1] += second != 0
            values[str(p)] = [str(first), str(second)]
        require(
            not pointwise_sum and all_first == 0,
            "common parameter direction vanishes before integration",
        )
        records.append({"n": n, "m": m, "curvature_and_Stokes_coefficients": values})
    require(nonzero[5][1] == 0 and nonzero[5][0] > 0, "actual prime-five affine field")
    return {
        "physical_record_count": len(records),
        "complete_source_index_count": len(numbers),
        "records": records,
        "nonzero_first_and_second_variations": {
            str(p): row for p, row in nonzero.items()
        },
        "pointwise_common_direction_zero": True,
        "source_parameter_augmentation_intertwining": True,
        "parameter_augmentation_is_residue_or_Walsh_projector": False,
    }


def derivative(module, coefficients):
    require(
        type(coefficients) is tuple and 1 <= len(coefficients) <= 5,
        "bounded exact energy polynomial",
    )
    return tuple(module.es(coefficients[j], j) for j in range(1, len(coefficients)))


def polynomial_value(module, coefficients, value):
    require(
        type(value) in (int, F) and -1 <= value <= 1,
        "admissible exact schedule parameter",
    )
    result = module.ex()
    for coefficient in reversed(coefficients):
        result = module.ea(module.es(result, value), coefficient)
    return result


def uniform_interval(module, coefficients):
    """An absolute-power enclosure valid throughout the complete interval [-1,1]."""
    intervals = [module.ei(value) for value in coefficients]
    radius = sum((max(abs(a), abs(b)) for a, b in intervals[1:]), F())
    return intervals[0][0] - radius, intervals[0][1] + radius


def gap(module, coefficients, value):
    return module.ea(
        coefficients[0], module.es(polynomial_value(module, coefficients, value), -1)
    )


def monotonicity_certificate(module, energy):
    certificates = {}
    for p, coefficients in energy.items():
        first = derivative(module, coefficients)
        second = derivative(module, first)
        if p == 5:
            require(
                coefficients[3] == coefficients[4] == module.ex(),
                "exact prime-five quadratic energy",
            )
            slope = uniform_interval(module, first)
            require(
                slope[0] > 3,
                "strictly increasing on the whole native parameter interval",
            )
            value, gain = F(-1), gap(module, coefficients, F(-1))
            require(
                module.ei(gain)[0] > F(341, 100), "source-global prime-five improvement"
            )
            certificates[str(p)] = {
                "unique_axis_minimum": str(value),
                "derivative_uniform_interval": module.interval_json(slope),
                "exact_physical_gain": module.expr_json(gain),
                "gain_interval": module.interval_json(module.ei(gain)),
                "actual_global_schedule": ["s", "s", "s^2"],
            }
        elif p == 2:
            slope = uniform_interval(module, first)
            require(
                slope[1] < -2,
                "strictly decreasing on the whole native parameter interval",
            )
            value, gain = F(1), gap(module, coefficients, F(1))
            require(
                module.ei(gain)[0] > F(339, 100), "source-global prime-two improvement"
            )
            certificates[str(p)] = {
                "unique_axis_minimum": str(value),
                "derivative_uniform_interval": module.interval_json(slope),
                "exact_physical_gain": module.expr_json(gain),
                "gain_interval": module.interval_json(module.ei(gain)),
                "actual_global_schedule": ["2s-s^2", "s", "s"],
            }
        else:
            require(p == 3, "declared primary/control parameters")
            convexity = uniform_interval(module, second)
            require(
                convexity[0] > F(165, 100),
                "strict original-kernel convexity certificate",
            )
            lo, hi = F(-53, 100), F(-52, 100)
            at_lo = module.ei(polynomial_value(module, first, lo))
            at_hi = module.ei(polynomial_value(module, first, hi))
            require(at_lo[1] < 0 < at_hi[0], "unique interior critical point enclosure")
            grid_gain = gap(module, coefficients, F(-1, 2))
            require(
                module.ei(grid_gain)[0] > F(23, 100),
                "preregistered primary grid improvement",
            )
            certificates[str(p)] = {
                "unique_axis_minimum_interval": [str(lo), str(hi)],
                "second_derivative_uniform_interval": module.interval_json(convexity),
                "derivative_at_lower": module.interval_json(at_lo),
                "derivative_at_upper": module.interval_json(at_hi),
                "preregistered_parameter": "-1/2",
                "grid_gain_interval": module.interval_json(module.ei(grid_gain)),
            }
    return certificates


def replay_equal(candidate, expected):
    require(canonical(candidate) == canonical(expected), "typed canonical replay")


def build():
    module = scout_module()
    module.authenticate()
    frozen = json.loads(frozen_bytes(DISCOVERY, DISCOVERY_BLOB))
    frozen_bytes(PREREG, PREREG_BLOB)
    require(
        frozen.get("schema") == "riemann.native_six_hour.global_geodesic_discovery.v1",
        "frozen discovery schema",
    )
    require(
        [row["deformed_prime"] for row in frozen["models"]] == [3, 2, 5],
        "preregistered primary/control order",
    )
    records, energy, summaries = {}, {}, []
    for original in frozen["models"]:
        p = original["deformed_prime"]
        current, ratios, endpoints, diagonals = module.native_field(p)
        coefficients = module.energy_polynomial(ratios)
        replay_equal(current, original["records"])
        replay_equal(
            [module.expr_json(row) for row in coefficients],
            original["exact_energy_polynomial"],
        )
        replay_equal(
            {name: [str(x) for x in row] for name, row in diagonals.items()},
            original["diagonal_polynomials_before_Gamma0"],
        )
        replay_equal(
            {str(K): [str(x) for x in row] for K, row in endpoints.items()},
            original["every_product_endpoint"],
        )
        records[p], energy[p] = current, coefficients
        summaries.append(
            {
                "prime": p,
                "ordered_factor_count": len(current),
                "coalesced_ratio_count": len(ratios),
                "energy_polynomial": [module.expr_json(row) for row in coefficients],
                "diagonals_before_Gamma0": {
                    name: [str(x) for x in row] for name, row in diagonals.items()
                },
            }
        )
    require(
        all(energy[p][0] == energy[2][0] for p in module.PRIMES),
        "same undeformed observed source",
    )
    require(
        F(16672, 100)
        < module.ei(energy[2][0])[0]
        <= module.ei(energy[2][0])[1]
        < F(16673, 100),
        "actual original energy interval",
    )
    first_sum = module.ex()
    for p in module.PRIMES:
        first_sum = module.ea(first_sum, energy[p][1])
    require(first_sum == module.ex(), "exact observed common-direction relation")
    curvature = curvature_control(module, records)
    decisions = monotonicity_certificate(module, energy)
    bindings = {}
    for path in (NOTE, Path(__file__), TEST):
        raw = path.read_bytes()
        require(len(raw) <= MAX_BYTES, "owned byte cap")
        bindings[path.relative_to(ROOT).as_posix()] = sha256(
            raw.replace(b"\r\n", b"\n")
        ).hexdigest()
    result = {
        "schema": "riemann.native_six_hour.global_geodesic_certificate.v1",
        "source_hashes": bindings,
        "sources": [
            {"commit": COMMIT, "path": path, "blob": blob}
            for path, blob in (
                (SCOUT, SCOUT_BLOB),
                (DISCOVERY, DISCOVERY_BLOB),
                (PREREG, PREREG_BLOB),
            )
        ]
        + [
            {"commit": module.OLD, "path": path, "blob": blob}
            for path, blob in module.SOURCES.items()
        ],
        "full_finite_models": summaries,
        "source_curvature": curvature,
        "axis_variational_decisions": decisions,
        "all_cross_product_interference_and_physical_weights_retained": True,
        "independent_tuple_schedules_used": False,
        "same_T106140_Wick_diagonal_claimed": False,
        "full_post_renewal_gamma_identified": False,
        "minimizer_over_all_global_paths_claimed": False,
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
        require(FIXTURE.stat().st_size <= MAX_BYTES, "artifact byte cap")
        replay_equal(json.loads(FIXTURE.read_text(encoding="utf-8")), result)
    print(f"PASS global native geodesic certificate {result['proof_object_sha256']}")


if __name__ == "__main__":
    main()
