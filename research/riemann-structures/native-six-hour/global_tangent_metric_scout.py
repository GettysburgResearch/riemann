#!/usr/bin/env python3
"""Original-metric source tangents and fixed joint monotone paths on all63 pairs."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from hashlib import sha1
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
COMMIT = "5d7ea752ee84765a7690bdc36bb2bbcaddb38bb4"
SOURCE = "research/riemann-structures/native-six-hour/global_geodesic_scout.py"
SOURCE_BLOB = "32a4c01750e99a37c4d1992fa6bddafeaea8fe06"
MAX_BYTES = 1048576
VERTICES = ((1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1), (0, 1))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def frozen_module():
    raw = subprocess.run(
        ["git", "show", f"{COMMIT}:{SOURCE}"], cwd=ROOT, capture_output=True, check=True
    ).stdout
    require(
        0 < len(raw) <= MAX_BYTES
        and sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        == SOURCE_BLOB,
        "exact frozen finite native source",
    )
    namespace = {
        "__name__": "authenticated_global_native_source",
        "__file__": str(ROOT / SOURCE),
    }
    # Only the declared, exact commit/blob-authenticated source is executed.
    exec(compile(raw, str(ROOT / SOURCE), "exec"), namespace)  # noqa: S102
    module = SimpleNamespace(**namespace)
    module.authenticate()
    return module


def poly(values):
    require(len(values) <= 9, "original source s-degree cap8")
    values = tuple(F(x) for x in values)
    while len(values) > 1 and not values[-1]:
        values = values[:-1]
    return values or (F(),)


def add(a, b):
    return poly(
        tuple(
            (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
            for i in range(max(len(a), len(b)))
        )
    )


def multiply(a, b):
    require(len(a) + len(b) - 2 <= 8, "original source product degree cap8")
    result = [F()] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return poly(result)


def derivative(a):
    return poly(tuple(i * x for i, x in enumerate(a) if i))


def integrate_two_ds(a):
    return 2 * sum((x / (i + 1) for i, x in enumerate(a)), F())


def primitive_square(a):
    return sum(
        (2 * x * y / (i + j + 1) for i, x in enumerate(a) for j, y in enumerate(a)), F()
    )


def schedule_tuple(values):
    require(
        type(values) is tuple
        and len(values) == 3
        and all(type(x) in (int, F) and -1 <= x <= 1 for x in values),
        "three exact monotone source parameters",
    )
    values = tuple(F(x) for x in values)
    require(
        all(
            max(x.numerator.bit_length(), x.denominator.bit_length()) <= 64
            for x in values
        ),
        "source parameter bit cap",
    )
    return values


def source(module, n, parameters):
    exponents = module.rational_exponents(n)
    factors = []
    for degree, epsilon in zip(exponents, parameters, strict=True):
        end = module.sqrt_coefficient(degree)
        start = module.sqrt_coefficient(degree // 2) if degree % 2 == 0 else F()
        difference = end - start
        factors.append(poly((start, difference * (1 + epsilon), -difference * epsilon)))
    value = (F(1),)
    for factor in factors:
        value = multiply(value, factor)
    sites = []
    for j, p in enumerate(module.PRIMES):
        term = (F(1),)
        for i, factor in enumerate(factors):
            term = multiply(term, derivative(factor) if i == j else factor)
        if any(term):
            sites.append((p, term))
    total = (F(),)
    for _, term in sites:
        total = add(total, term)
    require(total == derivative(value), "complete actual derivative-site source")
    return value, sites


def native_field(module, values):
    parameters = schedule_tuple(values)
    numbers = module.panel_numbers()
    sources = {n: source(module, n, parameters) for n in numbers}
    records, ratios, endpoints = [], {}, {}
    diagonals = {
        name: F()
        for name in ("primitive_2ds_site", "integrated_site", "integrated_pair")
    }
    for n in numbers:
        for m in numbers:
            K = n * m
            if K > module.HORIZON:
                continue
            left, sites = sources[n]
            right = sources[m][0]
            coefficient = integrate_two_ds(multiply(derivative(left), right))
            site_polynomials = [(p, multiply(term, right)) for p, term in sites]
            site_values = [(p, integrate_two_ds(term)) for p, term in site_polynomials]
            require(
                sum((x for _, x in site_values), F()) == coefficient,
                "complete actual2ds site integration",
            )
            ratio = F(n, m)
            ratios[ratio] = module.ra(
                ratios.get(ratio, {}),
                module.rs(module.sqrt_rational(F(1, K)), coefficient),
            )
            endpoints[K] = endpoints.get(K, F()) + coefficient
            diagonals["primitive_2ds_site"] += sum(
                (primitive_square(term) / K for _, term in site_polynomials), F()
            )
            diagonals["integrated_site"] += sum(
                (x * x / K for _, x in site_values), F()
            )
            diagonals["integrated_pair"] += coefficient**2 / K
            records.append(
                {
                    "n": n,
                    "m": m,
                    "K": K,
                    "ratio": str(ratio),
                    "coefficient_before_physical_weight": str(coefficient),
                    "literal_derivative_sites": [[p, str(x)] for p, x in site_values],
                }
            )
    require(
        len(records) == 63 and len(ratios) == 45,
        "complete fixed physical source horizon",
    )
    for K, value in endpoints.items():
        exponents = module.rational_exponents(K)
        sign = (-1) ** sum(e > 0 for e in exponents)
        expected = (sign if all(e <= 1 for e in exponents) else 0) - (
            sign if all(e in (0, 2) for e in exponents) else 0
        )
        require(value == expected, "every original product endpoint is preserved")
    coalesced = {}
    for amplitude in ratios.values():
        coalesced = module.ra(coalesced, module.rm(amplitude, amplitude))
    require(set(coalesced) <= {1}, "actual ratio-coalesced diagonal is rational")
    diagonals["ratio_coalesced"] = coalesced.get(1, F())
    return records, ratios, endpoints, diagonals


def inner(module, left, right):
    value = module.ex()
    for ratio, a in left.items():
        for other, b in right.items():
            if a and b:
                value = module.ea(
                    value, module.er(module.gamma(ratio / other), module.rm(a, b))
                )
    return value


def field_add(module, left, right, multiplier=1):
    return {
        ratio: module.ra(
            left.get(ratio, {}), module.rs(right.get(ratio, {}), multiplier)
        )
        for ratio in left.keys() | right.keys()
    }


def inv_interval(value):
    require(value[0] > 0 or value[1] < 0, "certified nonzero interval divisor")
    return min(1 / value[0], 1 / value[1]), max(1 / value[0], 1 / value[1])


def neg_interval(value):
    return -value[1], -value[0]


def tangent_metric(module):
    originals = {p: module.native_field(p) for p in module.PRIMES}
    tangents = {
        p: {ratio: coefficients[1] for ratio, coefficients in originals[p][1].items()}
        for p in module.PRIMES
    }
    baseline = {
        ratio: coefficients[0] for ratio, coefficients in originals[2][1].items()
    }
    for ratio in baseline:
        summed = {}
        for p in module.PRIMES:
            summed = module.ra(summed, tangents[p][ratio])
        require(
            not summed,
            "exact common-time tangent null vector after physical coalescence",
        )
    matrix = [
        [inner(module, tangents[p], tangents[q]) for q in module.PRIMES]
        for p in module.PRIMES
    ]
    directions = [field_add(module, tangents[p], tangents[5], -1) for p in (2, 3)]
    metric = [[inner(module, a, b) for b in directions] for a in directions]
    gradient = [
        module.es(inner(module, baseline, direction), 2) for direction in directions
    ]
    intervals = [[module.ei(x) for x in row] for row in metric]
    determinant = module.ia(
        module.im(intervals[0][0], intervals[1][1]),
        neg_interval(module.im(intervals[0][1], intervals[1][0])),
    )
    require(
        intervals[0][0][0] > 0 and determinant[0] > 0,
        "rank2 original source tangent metric",
    )
    g0, g1 = map(module.ei, gradient)
    first = module.ia(
        module.im(intervals[0][1], g1), neg_interval(module.im(intervals[1][1], g0))
    )
    second = module.ia(
        module.im(intervals[1][0], g0), neg_interval(module.im(intervals[0][0], g1))
    )
    midpoint = [(x[0] + x[1]) / 2 for x in (first, second)]
    three = midpoint + [-sum(midpoint)]
    maximum = max(abs(x) for x in three)
    require(maximum > 0, "nonzero metric steepest-descent direction")

    def rounded(value):
        value *= 1000
        numerator = (2 * abs(value.numerator) + value.denominator) // (
            2 * value.denominator
        )
        return F(numerator if value >= 0 else -numerator, 1000)

    selected = [rounded(x / maximum) for x in midpoint]
    selected.append(-sum(selected))
    scale = max(F(1), *(abs(x) for x in selected))
    selected = tuple(x / scale for x in selected)
    derivative_value = module.ea(
        module.es(gradient[0], selected[0]), module.es(gradient[1], selected[1])
    )
    require(
        module.ei(derivative_value)[1] < 0,
        "actual finite source descent after declared rounding",
    )
    return (
        baseline,
        tangents,
        selected,
        {
            "prime_order": module.PRIMES,
            "exact_tangent_Gram": [
                [module.expr_json(x) for x in row] for row in matrix
            ],
            "quotient_basis": [[1, 0, -1], [0, 1, -1]],
            "exact_quotient_metric": [
                [module.expr_json(x) for x in row] for row in metric
            ],
            "quotient_metric_determinant_interval": module.interval_json(determinant),
            "quotient_energy_gradient": [module.expr_json(x) for x in gradient],
            "selected_rational_direction": [str(x) for x in selected],
            "selected_first_variation_interval": module.interval_json(
                module.ei(derivative_value)
            ),
            "common_tangent_null_vector": [1, 1, 1],
            "exact_rank": 2,
        },
    )


def result_for_path(module, parameters, baseline, baseline_energy):
    records, ratios, endpoints, diagonals = native_field(module, parameters)
    difference = field_add(module, ratios, baseline, -1)
    require(
        all(
            not module.ra(amplitude, difference[1 / ratio])
            for ratio, amplitude in difference.items()
        ),
        "complete path variation remains exchange odd",
    )
    energy = inner(module, ratios, ratios)
    gain = module.ea(baseline_energy, module.es(energy, -1))
    return (
        {
            "epsilon": [str(x) for x in parameters],
            "all63_records": records,
            "exact_observed_energy": module.expr_json(energy),
            "energy_interval": module.interval_json(module.ei(energy)),
            "baseline_minus_energy_interval": module.interval_json(module.ei(gain)),
            "all_product_endpoints": {
                str(k): str(x) for k, x in sorted(endpoints.items())
            },
            "four_distinct_diagonals_before_Gamma0": {
                key: str(value) for key, value in diagonals.items()
            },
            "diagonals_identified_with_T106140": False,
        },
        ratios,
        energy,
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--discover", action="store_true", required=True)
    parser.parse_args()
    module = frozen_module()
    baseline, _, selected, tangent = tangent_metric(module)
    baseline_energy = inner(module, baseline, baseline)
    paths = [(F(), F(), F())]
    for a, b in VERTICES:
        for scale in (F(1), F(1, 2)):
            paths.append((scale * a, scale * b, -scale * (a + b)))
    paths.extend(((F(1), F(), F()), (F(), F(-1, 2), F()), (F(), F(), F(-1))))
    paths.extend((selected, tuple(x / 2 for x in selected)))
    records = []
    energies = {}
    for values in paths:
        values = schedule_tuple(values)
        row, _, energy = result_for_path(module, values, baseline, baseline_energy)
        records.append(row)
        energies[values] = energy
    common = []
    for value in (F(1, 2), F(-1, 2)):
        _, ratios, _, _ = native_field(module, (value, value, value))
        require(
            ratios == baseline,
            "actual common-time reparameterization preserves the complete current",
        )
        common.append({"epsilon": str(value), "complete_current_unchanged": True})
    first, second = (F(1, 2), F(), F(-1, 2)), (F(3, 4), F(1, 4), F(-1, 4))
    rows1, field1, _, _ = native_field(module, first)
    rows2, field2, _, _ = native_field(module, second)
    coefficient1 = F(
        next(
            row["coefficient_before_physical_weight"]
            for row in rows1
            if (row["n"], row["m"]) == (2, 6)
        )
    )
    coefficient2 = F(
        next(
            row["coefficient_before_physical_weight"]
            for row in rows2
            if (row["n"], row["m"]) == (2, 6)
        )
    )
    require(
        coefficient2 - coefficient1 == F(1, 1920),
        "predicted literal mixed-prime-square obstruction",
    )
    defect = field_add(module, field2, field1, -1)
    expected = module.rs(module.sqrt_rational(F(1, 12)), F(1, 1920))
    require(
        defect[F(1, 3)] == expected,
        "nonlinear obstruction survives complete physical ratio coalescence",
    )
    best_axis = energies[(F(), F(), F(-1))]
    comparisons = []
    for values, energy in energies.items():
        difference = module.ea(best_axis, module.es(energy, -1))
        comparisons.append(
            {
                "epsilon": [str(x) for x in values],
                "best_frozen_axis_minus_energy_interval": module.interval_json(
                    module.ei(difference)
                ),
            }
        )
    result = {
        "schema": "riemann.native_six_hour.global_tangent_metric_discovery.v1",
        "source_commit": COMMIT,
        "source_path": SOURCE,
        "source_blob": SOURCE_BLOB,
        "original_horizon": 25,
        "tangent": tangent,
        "all_fixed_paths": records,
        "comparison_to_frozen_best_axis": comparisons,
        "common_reparameterization_controls": common,
        "nonlinear_common_translation_obstruction": {
            "first": [str(x) for x in first],
            "second": [str(x) for x in second],
            "literal_2_6_difference": "1/1920",
            "exact_ratio_one_third_difference": {
                str(d): str(x) for d, x in expected.items()
            },
            "observed_squared_defect_interval": module.interval_json(
                module.ei(inner(module, defect, defect))
            ),
        },
        "independent_tuple_schedules_used": False,
        "global_path_minimality_claimed": False,
        "full_post_renewal_gamma_identified": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
