#!/usr/bin/env python3
"""Complete twenty-moment source decoding and original higher-horizon path tests."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from fractions import Fraction as F
from hashlib import sha1, sha256
from itertools import pairwise, permutations, product
from math import gcd
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFIX = "research/riemann-structures/native-six-hour/"
PINS = {
    "polynomial": (
        "6b18fbd9bc0a493e739166e6fcb9fbefd8e4d537",
        "native_curvature_span_scout.py",
        "e660bfaa86ca3562189d47c89390984fc1e3117c",
    ),
    "kernel": (
        "5d7ea752ee84765a7690bdc36bb2bbcaddb38bb4",
        "global_geodesic_scout.py",
        "32a4c01750e99a37c4d1992fa6bddafeaea8fe06",
    ),
    "interval": (
        "a10385170ae8d1555299b6e1ed981e44c5d1c6e5",
        "native_clipped_path_scout.py",
        "76764bbe7e3a234f57dce2bad86ce11b40915d24",
    ),
    "H25_Gram": (
        "46c8453e3976d242479202bf4d58489282a64d2a",
        "native_affine_floor.discovery.json",
        "350f264fb314d075388564089c04a080d8cb2c28",
    ),
}
PRIMES = (2, 3, 5)
ZERO = (0, 0, 0)
ONE = (1, 1, 1)
MAX_BYTES = 8 * 1024 * 1024
MAX_RECORDS = 200
MAX_RATIOS = 100
# Differential coordinate, then exponents of its monomial integrand.
BASIS = (
    (0, (0, 1, 0)),
    (0, (0, 0, 1)),
    (1, (0, 0, 1)),
    (0, (0, 1, 1)),
    (1, (1, 0, 1)),
    (0, (0, 0, 2)),
    (0, (0, 2, 0)),
    (0, (0, 2, 2)),
    (1, (0, 0, 2)),
    (1, (2, 0, 0)),
    (1, (2, 0, 2)),
    (2, (0, 2, 0)),
    (2, (2, 0, 0)),
    (2, (2, 2, 0)),
    (0, (0, 1, 2)),
    (1, (1, 0, 2)),
    (0, (0, 2, 1)),
    (2, (1, 2, 0)),
    (1, (2, 0, 1)),
    (2, (2, 1, 0)),
)
INDEX = {
    (tuple(p[k] + int(k == i) for k in range(3)), i): j
    for j, (i, p) in enumerate(BASIS)
}
CORNERS = tuple(product((0, 1), repeat=3))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def frozen(name, execute=False):
    commit, name, blob = PINS[name]
    ref = f"{commit}:{PREFIX}{name}"
    size = int(
        subprocess.check_output(["git", "cat-file", "-s", ref], cwd=ROOT, text=True)
    )
    require(0 < size <= MAX_BYTES, "bounded authenticated primitive")
    raw = subprocess.check_output(["git", "show", ref], cwd=ROOT)
    require(
        len(raw) == size
        and sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest() == blob,
        "exact primitive Git identity",
    )
    if not execute:
        return raw
    namespace = {
        "__name__": "authenticated_horizon_path_" + name.replace(".", "_"),
        "__file__": str(HERE / name),
    }
    # Only the fixed Git commit/blob-authenticated primitive is executable.
    exec(compile(raw, str(HERE / name), "exec"), namespace)  # noqa: S102
    return SimpleNamespace(**namespace)


def exponents(n):
    require(type(n) is int and 1 <= n <= 60, "declared primitive integer horizon")
    result = []
    for prime in PRIMES:
        degree = 0
        while n % prime == 0:
            n //= prime
            degree += 1
        result.append(degree)
    return tuple(result) if n == 1 else None


def square_root_coefficient(degree):
    require(type(degree) is int and 0 <= degree <= 5, "declared local exponent cap")
    result = F(1)
    for k in range(1, degree + 1):
        result *= -(F(1, 2) - k + 1) / k
    return result


def half_source(poly, n):
    degrees = exponents(n)
    require(degrees is not None, "actual three-prime support")
    result = {ZERO: F(1)}
    for i, degree in enumerate(degrees):
        constant = square_root_coefficient(degree // 2) if degree % 2 == 0 else F()
        linear = square_root_coefficient(degree) - constant
        variable = tuple(int(j == i) for j in range(3))
        result = poly.multiply(result, poly.poly({ZERO: constant, variable: linear}))
    if n <= 25:
        require(result == poly.half_source(n), "unchanged authenticated H25 source")
    return result


def monomial_decoder(a, b):
    require(a in CORNERS and b in CORNERS, "two literal multilinear source monomials")
    total = tuple(x + y for x, y in zip(a, b, strict=True))
    result = [F()] * 21
    if total == ZERO:
        return result
    active = [i for i in range(3) if total[i] == 1]
    sign = tuple(x - y for x, y in zip(a, b, strict=True))
    result[0] = F(1)
    if 2 in total:
        for i in active:
            result[INDEX[total, i] + 1] += sign[i]
    elif active:
        anchor = active[-1]
        result[0] += sign[anchor]
        for i in active[:-1]:
            result[INDEX[total, i] + 1] += sign[i] - sign[anchor]
    return result


def record_decoder(left, right):
    result = [F()] * 21
    for a, ca in left.items():
        for b, cb in right.items():
            row = monomial_decoder(a, b)
            for j, value in enumerate(row):
                result[j] += ca * cb * value
    return result


def path_moments(poly, points):
    result = []
    for i, powers in BASIS:
        variable = tuple(int(j == i) for j in range(3))
        result.append(
            sum(
                (
                    poly.edge_integral({variable: F(1, 2)}, {powers: F(1)}, a, b)
                    for a, b in pairwise(points)
                ),
                F(),
            )
        )
    return result


def literal_path(poly, polynomials, records, points):
    return [
        sum(
            (
                poly.edge_integral(polynomials[row["n"]], polynomials[row["m"]], a, b)
                for a, b in pairwise(points)
            ),
            F(),
        )
        for row in records
    ]


def decoded_records(decoders, moments):
    return [
        row[0] + sum(value * x for value, x in zip(row[1:], moments, strict=True))
        for row in decoders
    ]


def fixed_paths():
    paths = []
    for order in permutations(range(3)):
        points = [tuple(map(F, ZERO))]
        for i in order:
            value = list(points[-1])
            value[i] = F(1)
            points.append(tuple(value))
        paths.append(("axis_" + "".join(str(PRIMES[i]) for i in order), points))
    paths.append(("diagonal", [tuple(map(F, ZERO)), tuple(map(F, ONE))]))
    paths.append(
        (
            "fixed_irregular",
            [
                tuple(map(F, ZERO)),
                (F(1, 3), F(1, 4), F(1, 5)),
                (F(2, 3), F(3, 4), F(2, 5)),
                tuple(map(F, ONE)),
            ],
        )
    )
    return paths


def sum_expressions(kernel, values):
    result = kernel.ex()
    for value in values:
        result = kernel.ea(result, value)
    return result


def exact_dot(kernel, coefficients, expressions):
    return sum_expressions(
        kernel,
        (
            kernel.es(value, coefficient)
            for coefficient, value in zip(coefficients, expressions, strict=True)
            if coefficient
        ),
    )


def build_model(poly, kernel, interval, horizon, calibration):
    require(
        type(horizon) is int and horizon in (25, 30, 60), "registered horizon panel"
    )
    numbers = [n for n in range(1, horizon + 1) if exponents(n) is not None]
    polynomials = {n: half_source(poly, n) for n in numbers}
    records, decoders = [], []
    for n in numbers:
        for m in numbers:
            if n * m <= horizon:
                d = gcd(n, m)
                records.append({"n": n, "m": m, "d": d, "a": n // d, "b": m // d})
                decoders.append(record_decoder(polynomials[n], polynomials[m]))
    require(len(records) <= MAX_RECORDS, "complete ordered-record cap")
    ratios = sorted({(row["a"], row["b"]) for row in records})
    require(len(ratios) <= MAX_RATIOS, "complete physical-ratio cap")
    ratio_index = {ratio: i for i, ratio in enumerate(ratios)}
    columns = [[F()] * len(ratios) for _ in range(21)]
    for record, decoder in zip(records, decoders, strict=True):
        position = ratio_index[record["a"], record["b"]]
        for j, value in enumerate(decoder):
            columns[j][position] += value / record["d"]
    base_moments = [F(int(i == 2 or j == 9)) for j, (i, _) in enumerate(BASIS)]
    plane_base = [
        columns[0][r] + sum(base_moments[j] * columns[j + 1][r] for j in range(20))
        for r in range(len(ratios))
    ]
    plane = [
        plane_base,
        columns[1],
        [-2 * x for x in columns[10]],
        [2 * x for x in columns[7]],
    ]
    controls = []
    for name, points in fixed_paths():
        moments = path_moments(poly, points)
        actual = literal_path(poly, polynomials, records, points)
        require(
            actual == decoded_records(decoders, moments),
            "every literal record equals exact20-moment decoder",
        )
        controls.append(
            {
                "name": name,
                "moments": list(map(str, moments)),
                "complete_source": list(map(str, actual)),
            }
        )
    require(
        next(row["moments"] for row in controls if row["name"] == "axis_235")
        == list(map(str, base_moments)),
        "actual last-activation reference moments",
    )
    matrix = [[None] * len(ratios) for _ in ratios]
    matrix_digest = sha256()
    for r, (a, b) in enumerate(ratios):
        for s in range(r, len(ratios)):
            c, d = ratios[s]
            entry = kernel.er(
                kernel.gamma(F(a * d, b * c)), kernel.sqrt_rational(F(1, a * b * c * d))
            )
            matrix[r][s] = matrix[s][r] = entry
            matrix_digest.update(
                (
                    str(r)
                    + ","
                    + str(s)
                    + ":"
                    + canonical(kernel.expr_json(entry))
                    + "\n"
                ).encode()
            )
    responses = [[exact_dot(kernel, vector, row) for row in matrix] for vector in plane]
    constant = exact_dot(kernel, plane[0], responses[0])
    cross = [exact_dot(kernel, vector, responses[0]) for vector in plane[1:]]
    gram = [
        [exact_dot(kernel, vector, response) for response in responses[1:]]
        for vector in plane[1:]
    ]
    full_couplings = [
        [exact_dot(kernel, vector, response) for response in responses]
        for vector in columns[1:]
    ]
    for i, (j, scale) in enumerate(((0, 1), (9, -2), (6, 2))):
        require(
            [kernel.es(value, scale) for value in full_couplings[j]]
            == [cross[i]] + gram[i],
            "exact full20 to planar3 gradient coefficient identity",
        )
    if horizon == 25:
        require(
            len(records) == 63 and len(ratios) == 45, "complete H25 census calibration"
        )
        require(
            [kernel.expr_json(x) for x in cross] == calibration["exact_cross_terms"][:3]
            and kernel.expr_json(constant) == calibration["exact_reference_energy"]
            and [[kernel.expr_json(x) for x in row] for row in gram]
            == [row[:3] for row in calibration["exact_Gram"][:3]],
            "same original H25 planar physical Gram",
        )
        require(
            next(
                row["complete_source"] for row in controls if row["name"] == "axis_235"
            )
            == next(
                row["complete_source"]
                for row in calibration["actual_paths"]
                if row["name"] == "axis_235"
            ),
            "unchanged literal H25 reference",
        )
    return SimpleNamespace(
        poly=poly,
        kernel=kernel,
        interval=interval,
        horizon=horizon,
        numbers=numbers,
        polynomials=polynomials,
        records=records,
        decoders=decoders,
        ratios=ratios,
        ratio_index=ratio_index,
        columns=columns,
        plane=plane,
        matrix=matrix,
        constant=constant,
        cross=cross,
        gram=gram,
        full_couplings=full_couplings,
        gram_I=[[interval.rounded(kernel.ei(x)) for x in row] for row in gram],
        cross_I=[interval.rounded(kernel.ei(x)) for x in cross],
        constant_I=interval.rounded(kernel.ei(constant)),
        coupling_I=[
            [interval.rounded(kernel.ei(x)) for x in row] for row in full_couplings
        ],
        controls=controls,
        matrix_digest=matrix_digest.hexdigest(),
    )


def float_system(model, z):
    h = model.interval
    x, derivatives = h.float_profile(*z)
    x, derivatives = x[:3], [row[:3] for row in derivatives]
    gram = [[float((lo + hi) / 2) for lo, hi in row] for row in model.gram_I]
    cross = [float((lo + hi) / 2) for lo, hi in model.cross_I]
    linear = [cross[i] + sum(gram[i][j] * x[j] for j in range(3)) for i in range(3)]
    dlinear = [
        [sum(gram[i][j] * dx[j] for j in range(3)) for i in range(3)]
        for dx in derivatives
    ]
    lam, mu = z
    values = (linear[2] * lam + linear[0], linear[2] * mu + linear[1])
    jacobian = (
        (
            linear[2] + lam * dlinear[0][2] + dlinear[0][0],
            lam * dlinear[1][2] + dlinear[1][0],
        ),
        (
            mu * dlinear[0][2] + dlinear[0][1],
            linear[2] + mu * dlinear[1][2] + dlinear[1][1],
        ),
    )
    require(
        all(math.isfinite(x) for x in values + sum(jacobian, ())),
        "finite seed arithmetic",
    )
    return values, jacobian


def seed(model, start):
    z = tuple(map(float, start))
    history, status = [], "fixed_step_cap"
    for iteration in range(32):
        values, jacobian = float_system(model, z)
        residual = max(map(abs, values))
        history.append({"step": iteration, "center": list(z), "residual_max": residual})
        if residual < 1e-12:
            status = "floating_seed_converged_only"
            break
        a, b = jacobian[0]
        c, d = jacobian[1]
        determinant = a * d - b * c
        if abs(determinant) < 1e-24:
            status = "retained_floating_singular_jacobian"
            break
        delta = (
            (d * values[0] - b * values[1]) / determinant,
            (-c * values[0] + a * values[1]) / determinant,
        )
        accepted = False
        for reduction in range(16):
            trial = tuple(z[i] - delta[i] / (2**reduction) for i in range(2))
            try:
                residual_trial, _ = float_system(model, trial)
            except ValueError:
                continue
            if max(map(abs, residual_trial)) < residual:
                z, accepted = trial, True
                break
        if not accepted:
            status = "retained_no_decreasing_seed_step"
            break
    return {
        "start": list(map(str, start)),
        "status": status,
        "steps": history,
        "proposed_exact_binary_center": [str(F.from_float(x)) for x in z],
    }


def interval_system(model, z):
    h = model.interval
    x, derivatives, regime = h.interval_profile(z)
    x, derivatives = x[:3], [row[:3] for row in derivatives]
    linear = [
        h.add(
            model.cross_I[i], h.total(h.mul(model.gram_I[i][j], x[j]) for j in range(3))
        )
        for i in range(3)
    ]
    dlinear = [
        [h.total(h.mul(model.gram_I[i][j], dx[j]) for j in range(3)) for i in range(3)]
        for dx in derivatives
    ]
    lam, mu = z
    values = (
        h.add(h.mul(linear[2], lam), linear[0]),
        h.add(h.mul(linear[2], mu), linear[1]),
    )
    jacobian = (
        (
            h.total((linear[2], h.mul(lam, dlinear[0][2]), dlinear[0][0])),
            h.add(h.mul(lam, dlinear[1][2]), dlinear[1][0]),
        ),
        (
            h.add(h.mul(mu, dlinear[0][2]), dlinear[0][1]),
            h.total((linear[2], h.mul(mu, dlinear[1][2]), dlinear[1][1])),
        ),
    )
    return values, jacobian, linear, x, regime


def quadratic_minimum(coefficients):
    require(
        type(coefficients) is tuple
        and len(coefficients) == 3
        and all(type(x) in (int, F) for x in coefficients),
        "three exact univariate coefficients",
    )
    c, b, a = map(F, coefficients)
    require(
        max(
            max(x.numerator.bit_length(), x.denominator.bit_length()) for x in (c, b, a)
        )
        <= 4096,
        "bounded exact quadratic coefficients",
    )
    candidates = [(c, F()), (a + b + c, F(1))]
    if a > 0 and -2 * a < b < 0:
        z = -b / (2 * a)
        candidates.append((c - b * b / (4 * a), z))
    value, position = min(candidates)
    require(
        max(
            max(x.numerator.bit_length(), x.denominator.bit_length())
            for x in (value, position)
        )
        <= 32768,
        "bounded exact quadratic minimum",
    )
    return value, position


def cone_quadratics(h, gradient):
    def c(j):
        return gradient[j - 1]

    result = []
    for sigma, tau in product((0, 1), repeat=2):
        p = (
            h.total((c(2), h.scale(c(13), -2 * sigma), h.scale(c(6), tau))),
            h.total((c(4), h.scale(c(20), -2 * sigma), h.scale(c(15), tau))),
            h.total(
                (c(17), h.neg(c(18)), h.scale(c(14), -2 * sigma), h.scale(c(8), tau))
            ),
        )
        q = (
            h.total((c(3), h.scale(c(12), -2 * sigma), h.scale(c(9), tau))),
            h.total((c(5), h.scale(c(18), -2 * sigma), h.scale(c(16), tau))),
            h.total(
                (c(19), h.neg(c(20)), h.scale(c(14), -2 * sigma), h.scale(c(11), tau))
            ),
        )
        for family, coefficients in (("p", p), ("q", q)):
            lower, upper = [
                quadratic_minimum(tuple(x[side] for x in coefficients))
                for side in (0, 1)
            ]
            status = "PASS" if lower[0] >= 0 else "FAIL" if upper[0] < 0 else "UNKNOWN"
            result.append(
                {
                    "family": family,
                    "sigma": sigma,
                    "tau": tau,
                    "coefficient_intervals_constant_linear_quadratic": [
                        h.interval_json(x) for x in coefficients
                    ],
                    "lower_envelope_minimum": str(lower[0]),
                    "lower_minimizer": str(lower[1]),
                    "upper_envelope_minimum": str(upper[0]),
                    "upper_minimizer": str(upper[1]),
                    "status": status,
                }
            )
    return result


def plane_energy(model, x):
    kernel = model.kernel
    value = model.constant
    for i in range(3):
        value = kernel.ea(value, kernel.es(model.cross[i], 2 * x[i]))
        for j in range(3):
            value = kernel.ea(value, kernel.es(model.gram[i][j], x[i] * x[j]))
    return value


def rational_witness(model, center):
    h, kernel = model.interval, model.kernel
    points, x6 = h.rational_path(center)
    x = x6[:3]
    moments = path_moments(model.poly, points)
    actual = literal_path(model.poly, model.polynomials, model.records, points)
    require(
        actual == decoded_records(model.decoders, moments),
        "all actual higher-horizon source records",
    )
    require(
        (moments[0], (1 - moments[9]) / 2, moments[6] / 2) == x,
        "exact actual last-activation planar coordinates",
    )
    image = [F()] * len(model.ratios)
    for row, value in zip(model.records, actual, strict=True):
        image[model.ratio_index[row["a"], row["b"]]] += value / row["d"]
    predicted = [
        model.plane[0][r] + sum(x[j] * model.plane[j + 1][r] for j in range(3))
        for r in range(len(model.ratios))
    ]
    require(image == predicted, "complete original physical ratio collection")
    direct = exact_dot(
        kernel, image, [exact_dot(kernel, image, row) for row in model.matrix]
    )
    energy = plane_energy(model, x)
    require(direct == energy, "direct complete physical energy equals planar Gram")
    return {
        "exact_center": list(map(str, center)),
        "actual_path_vertices": [list(map(str, p)) for p in points],
        "twenty_moments": list(map(str, moments)),
        "planar_A_B_C_half": list(map(str, x)),
        "all_ordered_source_coefficients": list(map(str, actual)),
        "all_physical_rational_coefficients": list(map(str, image)),
        "exact_original_energy": kernel.expr_json(energy),
        "original_energy": h.interval_json(kernel.ei(energy)),
    }


def certify(model, attempt):
    h = model.interval
    center = tuple(map(F, attempt["proposed_exact_binary_center"]))
    require(all(h.point(x) == (x, x) for x in center), "exact outward-lattice center")
    box = tuple(h.rounded((x - h.RADIUS, x + h.RADIUS)) for x in center)
    require(
        all(box[i] == (center[i] - h.RADIUS, center[i] + h.RADIUS) for i in range(2)),
        "whole certified root box",
    )
    values, center_jacobian, _, _, _ = interval_system(
        model, tuple(h.point(x) for x in center)
    )
    _, jacobian, linear, coordinates, regime = interval_system(model, box)
    a, b = map(h.midpoint, center_jacobian[0])
    c, d = map(h.midpoint, center_jacobian[1])
    determinant = h.bounded(a * d - b * c)
    require(determinant != 0, "nonzero midpoint Jacobian")
    inverse = tuple(
        tuple(h.midpoint(h.point(h.bounded(x))) for x in row)
        for row in (
            (d / determinant, -b / determinant),
            (-c / determinant, a / determinant),
        )
    )
    require(
        inverse[0][0] * inverse[1][1] != inverse[0][1] * inverse[1][0],
        "invertible rational preconditioner",
    )
    derivative = tuple(
        tuple(
            h.sub(
                h.point(int(i == j)),
                h.total(h.scale(jacobian[k][j], inverse[i][k]) for k in range(2)),
            )
            for j in range(2)
        )
        for i in range(2)
    )
    contraction = max(sum(max(map(abs, x)) for x in row) for row in derivative)
    require(contraction < 1, "strict original-source contraction")
    image = [
        h.add(
            h.sub(
                h.point(center[i]),
                h.total(h.scale(values[k], inverse[i][k]) for k in range(2)),
            ),
            h.total(h.mul(x, (-h.RADIUS, h.RADIUS)) for x in derivative[i]),
        )
        for i in range(2)
    ]
    require(
        all(box[i][0] < image[i][0] <= image[i][1] < box[i][1] for i in range(2)),
        "strict original-source Krawczyk inclusion",
    )
    gradient = [
        h.add(row[0], h.total(h.mul(row[j + 1], coordinates[j]) for j in range(3)))
        for row in model.coupling_I
    ]
    # The actual twenty-moment decoder independently fixes the planar gradient convention.
    relations = (gradient[0], h.scale(gradient[9], -2), h.scale(gradient[6], 2))
    require(
        all(
            x[0] <= y[1] and y[0] <= x[1]
            for x, y in zip(relations, linear, strict=True)
        ),
        "full20 and planar3 source-gradient enclosures agree",
    )
    cone = cone_quadratics(h, gradient)
    source_c = h.scale(linear[2], F(1, 2))
    planar = source_c[0] > 0
    global_certificate = planar and all(row["status"] == "PASS" for row in cone)
    energy = model.constant_I
    for i in range(3):
        energy = h.add(energy, h.scale(h.mul(model.cross_I[i], coordinates[i]), 2))
        for j in range(3):
            energy = h.add(
                energy, h.mul(model.gram_I[i][j], h.mul(coordinates[i], coordinates[j]))
            )
    return {
        "root_exists_and_unique_in_box": True,
        "root_box": [h.interval_json(x) for x in box],
        "Krawczyk_image": [h.interval_json(x) for x in image],
        "contraction_upper": str(contraction),
        "preconditioner": [list(map(str, row)) for row in inverse],
        "clipping_regime": regime,
        "planar_source_c": h.interval_json(source_c),
        "full20_half_gradient": [h.interval_json(x) for x in gradient],
        "eight_source_quadratics": cone,
        "last_activation_subclass_optimum_certified": planar,
        "global_all_path_source_optimum_certified": global_certificate,
        "root_energy": h.interval_json(energy),
    }


def panel(poly, kernel, interval, horizon, calibration):
    model = build_model(poly, kernel, interval, horizon, calibration)
    attempts, witnesses, witness_indices = [], [], {}
    for start in interval.STARTS:
        attempt = seed(model, start)
        try:
            attempt["certificate"] = certify(model, attempt)
            center = tuple(map(F, attempt["proposed_exact_binary_center"]))
            if center not in witness_indices:
                witness_indices[center] = len(witnesses)
                witnesses.append(rational_witness(model, center))
            attempt["exact_actual_witness_index"] = witness_indices[center]
        except ValueError as error:
            attempt["certificate"] = {
                "root_exists_and_unique_in_box": False,
                "global_all_path_source_optimum_certified": False,
                "retained_guard_failure": str(error),
            }
        attempts.append(attempt)
    return {
        "H": horizon,
        "complete_record_count": len(model.records),
        "complete_ratio_count": len(model.ratios),
        "all_ordered_records": model.records,
        "all21_decoder_columns_per_record": [
            list(map(str, row)) for row in model.decoders
        ],
        "all_physical_ratio_order": [{"a": a, "b": b} for a, b in model.ratios],
        "all21_physical_rational_columns": [
            list(map(str, row)) for row in model.columns
        ],
        "original_Gamma_matrix_upper_triangle_sha256": model.matrix_digest,
        "fixed_path_decoder_controls": model.controls,
        "exact_planar_Gram": [[kernel.expr_json(x) for x in row] for row in model.gram],
        "exact_planar_cross": [kernel.expr_json(x) for x in model.cross],
        "exact_planar_reference_energy": kernel.expr_json(model.constant),
        "exact_full20_by4_physical_couplings": [
            [kernel.expr_json(x) for x in row] for row in model.full_couplings
        ],
        "all16_declared_start_outcomes": attempts,
        "all_distinct_rational_actual_witnesses": witnesses,
        "global_certificate_attempts": [
            i
            for i, x in enumerate(attempts)
            if x["certificate"]["global_all_path_source_optimum_certified"]
        ],
        "all20_physical_directions_claimed_independent": False,
        "full_gamma_identified": False,
    }


def discover(phase):
    require(phase in ("calibration", "heldout"), "declared source-horizon phase")
    poly, kernel, interval = (
        frozen(name, True) for name in ("polynomial", "kernel", "interval")
    )
    kernel.authenticate()
    calibration = json.loads(frozen("H25_Gram"))
    owned = {}
    for path in (
        Path(__file__),
        HERE / "NATIVE_HORIZON_PATH_PREREGISTRATION.md",
        HERE / "ALL_HORIZON_THREE_PRIME_SOURCE_MOMENTS.md",
        HERE / "EIGHT_QUADRATIC_LAST_ACTIVATION_CONE.md",
    ):
        raw = path.read_bytes()
        require(len(raw) <= MAX_BYTES, "bounded owned source")
        owned[path.relative_to(ROOT).as_posix()] = sha256(
            raw.replace(b"\r\n", b"\n")
        ).hexdigest()
    result = {
        "schema": "riemann.native_six_hour.higher_horizon_path_discovery.v1",
        "phase": phase,
        "sources": [
            {"commit": commit, "path": PREFIX + name, "blob": blob}
            for commit, name, blob in PINS.values()
        ],
        "owned_sha256_lf": owned,
        "twenty_moment_basis": [{"differential": i, "powers": p} for i, p in BASIS],
        "panels": [
            panel(poly, kernel, interval, horizon, calibration)
            for horizon in ((25,) if phase == "calibration" else (30, 60))
        ],
        "physical_measure_is_original": True,
        "all_height_global_optimum_claimed": False,
        "full_retained_gamma_identified": False,
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--phase", choices=("calibration", "heldout"), required=True)
    args = parser.parse_args()
    output = (
        json.dumps(discover(args.phase), sort_keys=True, indent=2, allow_nan=False)
        + "\n"
    )
    require(
        len(output.encode()) <= MAX_BYTES, "bounded complete source-horizon artifact"
    )
    print(output, end="")


if __name__ == "__main__":
    main()
