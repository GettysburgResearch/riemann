#!/usr/bin/env python3
"""Fixed source-path seeds with independent outward global-support certification."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from fractions import Fraction as F
from hashlib import sha1, sha256
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFIX = "research/riemann-structures/native-six-hour/"
COMMIT = "fd24a4acb3b9a041bce4fb8701d2a887e77d2def"
SOURCE = PREFIX + "native_monotone_grid_scout.py"
BLOB = "01f94b1576e36319b6b3ed42a1e49057f2e70b85"
MAX_BYTES = 8 * 1024 * 1024
BITS = 512
DEN = 1 << BITS
RADIUS = F(1, 1 << 30)
STARTS = tuple(
    (a, b)
    for a in (F(-1, 2), F(-1, 8), F(1, 8), F(1, 2))
    for b in (F(1, 2), F(1), F(3, 2), F(2))
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def bounded(value):
    require(type(value) in (int, F), "exact interval input")
    value = F(value)
    require(
        max(value.numerator.bit_length(), value.denominator.bit_length()) <= 32768,
        "registered exact arithmetic bit cap",
    )
    return value


def rounded(value):
    lo, hi = map(bounded, value)
    require(lo <= hi, "ordered outward interval")
    return F((lo * DEN).__floor__(), DEN), F((hi * DEN).__ceil__(), DEN)


def point(value):
    return rounded((value, value))


def add(a, b):
    return rounded((a[0] + b[0], a[1] + b[1]))


def neg(a):
    return -a[1], -a[0]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    values = [x * y for x in a for y in b]
    return rounded((min(values), max(values)))


def scale(a, value):
    return mul(a, point(value))


def div(a, b):
    require(b[0] > 0 or b[1] < 0, "certified nonzero divisor")
    values = (1 / b[0], 1 / b[1])
    return mul(a, rounded((min(values), max(values))))


def power(a, exponent):
    require(type(exponent) is int and 0 <= exponent <= 3, "bounded polynomial degree")
    value = point(1)
    for _ in range(exponent):
        value = mul(value, a)
    return value


def total(values):
    result = point(0)
    for value in values:
        result = add(result, value)
    return result


def interval_json(value):
    value = rounded(value)
    require(
        max(max(x.numerator.bit_length(), x.denominator.bit_length()) for x in value)
        <= 2048,
        "serialized interval bit cap",
    )
    return {
        "lower": str(value[0]),
        "upper": str(value[1]),
        "approximate_midpoint": float((value[0] + value[1]) / 2),
    }


def source():
    ref = f"{COMMIT}:{SOURCE}"
    size = int(
        subprocess.check_output(["git", "cat-file", "-s", ref], cwd=ROOT, text=True)
    )
    require(0 < size <= MAX_BYTES, "bounded frozen grid source")
    raw = subprocess.check_output(["git", "show", ref], cwd=ROOT)
    require(
        len(raw) == size
        and sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest() == BLOB,
        "exact frozen original source adapter",
    )
    namespace = {
        "__name__": "authenticated_clipped_source",
        "__file__": str(ROOT / SOURCE),
    }
    # Execute only exact declared Git commit/blob-authenticated source bytes.
    exec(compile(raw, str(ROOT / SOURCE), "exec"), namespace)  # noqa: S102
    grid = SimpleNamespace(**namespace)
    return grid, grid.source()


def float_profile(lam, mu):
    require(
        math.isfinite(lam) and math.isfinite(mu) and -2 < lam < 2 and 1 / 16 < mu < 4,
        "registered floating seed box",
    )
    lo = min(1.0, max(0.0, -lam / mu))
    hi = min(1.0, max(0.0, (1 - lam) / mu))
    width, first, second = hi - lo, (hi * hi - lo * lo) / 2, (hi**3 - lo**3) / 3
    band_a = lam * width + mu * first
    band_b = lam * first + mu * second
    band_c = lam * lam * width + 2 * lam * mu * first + mu * mu * second
    x = (
        band_a + 1 - hi,
        band_b + (1 - hi * hi) / 2,
        (band_c + 1 - hi) / 2,
        0.0,
        0.0,
        0.0,
    )
    derivatives = (
        (width, first, band_a, 0.0, 0.0, 0.0),
        (first, second, band_b, 0.0, 0.0, 0.0),
    )
    return x, derivatives


def float_system(gram, cross, z):
    lam, mu = z
    x, derivatives = float_profile(lam, mu)
    linear = [cross[i] + sum(gram[i][j] * x[j] for j in range(6)) for i in range(6)]
    dlinear = [
        [sum(gram[i][j] * derivative[j] for j in range(6)) for i in range(6)]
        for derivative in derivatives
    ]
    equations = (linear[2] * lam + linear[0], linear[2] * mu + linear[1])
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
        all(math.isfinite(x) for x in equations + sum(jacobian, ())),
        "finite seed arithmetic",
    )
    return equations, jacobian


def seed(model, start):
    gram = [
        [float(F(a + b, 2 * DEN)) for a, b in row] for row in model.intervals["gram"]
    ]
    cross = [float(F(a + b, 2 * DEN)) for a, b in model.intervals["cross"]]
    z = tuple(map(float, start))
    history = []
    status = "fixed_step_cap"
    for iteration in range(32):
        values, jacobian = float_system(gram, cross, z)
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
        step = (
            (d * values[0] - b * values[1]) / determinant,
            (-c * values[0] + a * values[1]) / determinant,
        )
        accepted = False
        for reduction in range(16):
            candidate = tuple(z[i] - step[i] / (2**reduction) for i in range(2))
            try:
                trial, _ = float_system(gram, cross, candidate)
            except ValueError:
                continue
            if max(map(abs, trial)) < residual:
                z = candidate
                accepted = True
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


def interval_profile(z):
    lam, mu = z
    require(
        mu[0] > 0 and lam[1] < 1 and add(lam, mu)[0] > 0,
        "nonempty increasing clipping band",
    )
    if lam[1] < 0:
        lo, lower = div(neg(lam), mu), True
    elif lam[0] > 0:
        lo, lower = point(0), False
    else:
        raise ValueError("root box crosses lower clipping boundary")
    upper_test = sub(add(lam, mu), point(1))
    if upper_test[0] > 0:
        hi, upper = div(sub(point(1), lam), mu), True
    elif upper_test[1] < 0:
        hi, upper = point(1), False
    else:
        raise ValueError("root box crosses upper clipping boundary")
    require(
        lo[0] >= 0 and hi[1] <= 1 and sub(hi, lo)[0] > 0,
        "certified clipping breakpoint order",
    )
    width = sub(hi, lo)
    first = scale(sub(power(hi, 2), power(lo, 2)), F(1, 2))
    second = scale(sub(power(hi, 3), power(lo, 3)), F(1, 3))
    band_a = add(mul(lam, width), mul(mu, first))
    band_b = add(mul(lam, first), mul(mu, second))
    band_c = total(
        (
            mul(power(lam, 2), width),
            scale(mul(mul(lam, mu), first), 2),
            mul(power(mu, 2), second),
        )
    )
    x = (
        add(band_a, sub(point(1), hi)),
        add(band_b, scale(sub(point(1), power(hi, 2)), F(1, 2))),
        scale(add(band_c, sub(point(1), hi)), F(1, 2)),
        point(0),
        point(0),
        point(0),
    )
    derivatives = (
        (width, first, band_a, point(0), point(0), point(0)),
        (first, second, band_b, point(0), point(0), point(0)),
    )
    return (
        x,
        derivatives,
        {
            "lower_clipped": lower,
            "upper_clipped": upper,
            "left_breakpoint": interval_json(lo),
            "right_breakpoint": interval_json(hi),
        },
    )


def interval_system(model, z):
    gram = [
        [tuple(F(x, DEN) for x in entry) for entry in row]
        for row in model.intervals["gram"]
    ]
    cross = [tuple(F(x, DEN) for x in entry) for entry in model.intervals["cross"]]
    x, derivatives, regime = interval_profile(z)
    linear = [
        add(cross[i], total(mul(gram[i][j], x[j]) for j in range(6))) for i in range(6)
    ]
    dlinear = [
        [total(mul(gram[i][j], derivative[j]) for j in range(6)) for i in range(6)]
        for derivative in derivatives
    ]
    lam, mu = z
    equations = (
        add(mul(linear[2], lam), linear[0]),
        add(mul(linear[2], mu), linear[1]),
    )
    jacobian = (
        (
            total((linear[2], mul(lam, dlinear[0][2]), dlinear[0][0])),
            add(mul(lam, dlinear[1][2]), dlinear[1][0]),
        ),
        (
            add(mul(mu, dlinear[0][2]), dlinear[0][1]),
            total((linear[2], mul(mu, dlinear[1][2]), dlinear[1][1])),
        ),
    )
    return equations, jacobian, linear, x, regime


def midpoint(value):
    return F(((value[0] + value[1]) * DEN / 2).__floor__(), DEN)


def interval_energy(model, x):
    value = tuple(F(a, DEN) for a in model.intervals["constant"])
    for i in range(6):
        value = add(
            value,
            scale(mul(tuple(F(a, DEN) for a in model.intervals["cross"][i]), x[i]), 2),
        )
        for j in range(6):
            value = add(
                value,
                mul(
                    tuple(F(a, DEN) for a in model.intervals["gram"][i][j]),
                    mul(x[i], x[j]),
                ),
            )
    return value


def rational_path(center):
    lam, mu = center
    require(mu > 0, "positive rational path slope")
    lo, hi = max(F(), -lam / mu), min(F(1), (1 - lam) / mu)
    require(0 <= lo < hi <= 1, "nonempty rational clipping band")
    clip = lambda value: min(F(1), max(F(), value))
    proposed = [
        (F(), F(), F()),
        (F(), clip(lam), F()),
        (lo, clip(lam + mu * lo), F()),
        (hi, clip(lam + mu * hi), F()),
        (F(1), F(1), F()),
        (F(1), F(1), F(1)),
    ]
    points = []
    for row in proposed:
        if not points or points[-1] != row:
            points.append(row)
    width, first, second = hi - lo, (hi * hi - lo * lo) / 2, (hi**3 - lo**3) / 3
    x = (
        lam * width + mu * first + 1 - hi,
        lam * first + mu * second + (1 - hi * hi) / 2,
        (lam * lam * width + 2 * lam * mu * first + mu * mu * second + 1 - hi) / 2,
        F(),
        F(),
        F(),
    )
    return points, x


def certificate(grid, model, attempt):
    center = tuple(map(F, attempt["proposed_exact_binary_center"]))
    require(
        all(point(x) == (x, x) for x in center),
        "binary center lies exactly on the declared outward lattice",
    )
    box = tuple(rounded((x - RADIUS, x + RADIUS)) for x in center)
    require(
        all(box[i] == (center[i] - RADIUS, center[i] + RADIUS) for i in range(2)),
        "Krawczyk increments cover the exact certified box",
    )
    values, center_jacobian, _, _, _ = interval_system(
        model, tuple(point(x) for x in center)
    )
    box_equations, jacobian, linear, coordinates, regime = interval_system(model, box)
    a, b = map(midpoint, center_jacobian[0])
    c, d = map(midpoint, center_jacobian[1])
    determinant = bounded(a * d - b * c)
    require(determinant != 0, "nonzero rational midpoint Jacobian")
    raw_inverse = (
        (d / determinant, -b / determinant),
        (-c / determinant, a / determinant),
    )
    inverse = tuple(
        tuple(midpoint(point(bounded(x))) for x in row) for row in raw_inverse
    )
    require(
        inverse[0][0] * inverse[1][1] != inverse[0][1] * inverse[1][0],
        "invertible chosen rational preconditioner",
    )
    derivative = tuple(
        tuple(
            sub(
                point(int(i == j)),
                total(scale(jacobian[k][j], inverse[i][k]) for k in range(2)),
            )
            for j in range(2)
        )
        for i in range(2)
    )
    contraction = max(
        sum(max(abs(x) for x in entry) for entry in row) for row in derivative
    )
    require(contraction < 1, "strict rational contraction bound")
    image = []
    for i in range(2):
        base = sub(
            point(center[i]), total(scale(values[k], inverse[i][k]) for k in range(2))
        )
        image.append(
            add(base, total(mul(entry, (-RADIUS, RADIUS)) for entry in derivative[i]))
        )
    require(
        all(box[i][0] < image[i][0] <= image[i][1] < box[i][1] for i in range(2)),
        "strict outward Krawczyk inclusion",
    )
    source_c = scale(linear[2], F(1, 2))
    cone = {
        "f": linear[5],
        "d_plus_e_half": add(linear[3], scale(linear[4], F(1, 2))),
        "d_plus_e": add(linear[3], linear[4]),
    }
    global_certificate = source_c[0] > 0 and all(
        value[0] >= 0 for value in cone.values()
    )
    points, rational_coordinates = rational_path(center)
    literal = model.affine.literal_path(model.curve, points, model.records)
    predicted = [
        model.reference[k]
        + sum(rational_coordinates[i] * model.columns[i][k] for i in range(6))
        for k in range(63)
    ]
    require(literal == predicted, "all63 actual clipped-path source integrals")
    image_rational = model.curve.ratio_image(literal, model.records, model.ratios)
    field = model.affine.source_field(
        model.curve, model.kernel, literal, model.records, model.ratios
    )
    energy = grid.energy(model, rational_coordinates)
    require(
        model.affine.inner(model.kernel, field, field) == energy,
        "all45 original physical-energy cross terms",
    )
    root_energy = interval_energy(model, coordinates)
    return {
        "root_exists_and_unique_in_box": True,
        "root_box": [interval_json(x) for x in box],
        "Krawczyk_image": [interval_json(x) for x in image],
        "contraction_upper": str(contraction),
        "center_equation_intervals": [interval_json(x) for x in values],
        "box_equation_intervals": [interval_json(x) for x in box_equations],
        "box_Jacobian": [[interval_json(x) for x in row] for row in jacobian],
        "rational_preconditioner": [list(map(str, row)) for row in inverse],
        "clipping_regime": regime,
        "original_source_c": interval_json(source_c),
        "original_half_gradient_L": [interval_json(x) for x in linear],
        "full_w_last_support_cone": {
            name: interval_json(value) for name, value in cone.items()
        },
        "global_all_path_source_optimality_certified": global_certificate,
        "unique_optimal_observed_source_if_certified": global_certificate,
        "root_source_coordinates": [interval_json(x) for x in coordinates],
        "root_energy": interval_json(root_energy),
        "nearby_rational_actual_path": {
            "vertices": [list(map(str, row)) for row in points],
            "source_coordinates": list(map(str, rational_coordinates)),
            "complete63_source": list(map(str, literal)),
            "complete45_ratio_image": list(map(str, image_rational)),
            "exact_original_energy": model.kernel.expr_json(energy),
            "original_energy": grid.interval_json(model.kernel.ei(energy)),
        },
    }


def discover():
    grid, model = source()
    attempts = []
    for start in STARTS:
        attempt = seed(model, start)
        try:
            attempt["rational_certificate"] = certificate(grid, model, attempt)
        except ValueError as error:
            attempt["rational_certificate"] = {
                "root_exists_and_unique_in_box": False,
                "global_all_path_source_optimality_certified": False,
                "retained_guard_failure": str(error),
            }
        attempts.append(attempt)
    certified = [
        i
        for i, row in enumerate(attempts)
        if row["rational_certificate"]["global_all_path_source_optimality_certified"]
    ]
    owned = {}
    for path in (
        Path(__file__),
        HERE / "NATIVE_CLIPPED_PATH_PREREGISTRATION.md",
        HERE / "NATIVE_SELF_CONSISTENT_PATH_OPTIMALITY.md",
    ):
        raw = path.read_bytes()
        require(len(raw) <= MAX_BYTES, "owned source byte cap")
        owned[path.relative_to(ROOT).as_posix()] = sha256(
            raw.replace(b"\r\n", b"\n")
        ).hexdigest()
    result = {
        "schema": "riemann.native_six_hour.clipped_path_discovery.v1",
        "source": {"commit": COMMIT, "path": SOURCE, "blob": BLOB},
        "owned_sha256_lf": owned,
        "all16_declared_starts": attempts,
        "globally_certified_attempt_indices": certified,
        "floating_steps_are_seed_only": True,
        "fixed_outward_bits": BITS,
        "fixed_root_radius": str(RADIUS),
        "original_source_records": model.records,
        "full_gamma_identified": False,
        "all_height_path_theorem_claimed": False,
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--discover", action="store_true", required=True)
    parser.parse_args()
    output = json.dumps(discover(), sort_keys=True, indent=2, allow_nan=False) + "\n"
    require(len(output.encode()) <= MAX_BYTES, "bounded retained-attempt artifact")
    print(output, end="")


if __name__ == "__main__":
    main()
