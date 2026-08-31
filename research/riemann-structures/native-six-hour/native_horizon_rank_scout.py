"""Complete bounded native curvature ranks before and after physical coalescence."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from hashlib import sha1, sha256
from itertools import combinations, product
from math import gcd
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFIX = "research/riemann-structures/native-six-hour/"
PINS = (
    (
        "6b18fbd9bc0a493e739166e6fcb9fbefd8e4d537",
        PREFIX + "native_curvature_span_scout.py",
        "e660bfaa86ca3562189d47c89390984fc1e3117c",
    ),
    (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102707-continuous-half-divisor-geodesic-and-polarized-hankel-current.md",
        "6810bcece309b0c54ae6c8fc84b314990004549c",
    ),
)
PRIMES = (2, 3, 5)
PAIRS = tuple(combinations(range(3), 2))
ZERO = (0, 0, 0)
COORDINATES = tuple(
    (i, j, *exponents)
    for i, j in PAIRS
    for exponents in product(*(range(2) if k in (i, j) else range(3) for k in range(3)))
)
MAX_BYTES = 32 * 1024 * 1024


def need(condition, message):
    if not condition:
        raise ValueError(message)


def exact(value):
    need(type(value) in (int, F), "literal exact rational")
    value = F(value)
    need(
        max(value.numerator.bit_length(), value.denominator.bit_length()) <= 4096,
        "registered rational bit cap",
    )
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def source():
    provenance, raw = [], []
    for commit, path, blob in PINS:
        ref = f"{commit}:{path}"
        size = int(
            subprocess.check_output(["git", "cat-file", "-s", ref], cwd=ROOT, text=True)
        )
        need(0 < size <= 4 * 1024 * 1024, "bounded frozen source")
        data = subprocess.check_output(["git", "show", ref], cwd=ROOT)
        need(
            len(data) == size
            and sha1(b"blob " + str(size).encode() + b"\0" + data).hexdigest() == blob,
            "exact source Git identity",
        )
        raw.append(data)
        provenance.append({"commit": commit, "path": path, "blob": blob})
    namespace = {
        "__name__": "authenticated_horizon_polynomials",
        "__file__": str(ROOT / PINS[0][1]),
    }
    exec(compile(raw[0], str(ROOT / PINS[0][1]), "exec"), namespace)  # noqa: S102
    return SimpleNamespace(**namespace), provenance


def exponents(n):
    need(type(n) is int and 1 <= n <= 900, "registered source index")
    result = []
    for prime in PRIMES:
        degree = 0
        while n % prime == 0:
            n //= prime
            degree += 1
        result.append(degree)
    return tuple(result) if n == 1 else None


def coefficient(degree):
    need(type(degree) is int and 0 <= degree <= 9, "registered half-source exponent")
    value = F(1)
    for k in range(1, degree + 1):
        value *= -(F(1, 2) - k + 1) / k
    return exact(value)


def half_source(module, n):
    result = {ZERO: F(1)}
    for k, degree in enumerate(exponents(n)):
        start = coefficient(degree // 2) if degree % 2 == 0 else F()
        key = tuple(int(i == k) for i in range(3))
        result = module.multiply(
            result, module.poly({ZERO: start, key: coefficient(degree) - start})
        )
    if n <= 25:
        need(
            result == module.half_source(n), "unchanged actual H25 source coefficients"
        )
    return result


def curvature(module, left, right):
    values = {}
    for i, j in PAIRS:
        first = module.multiply(module.derivative(left, i), module.derivative(right, j))
        second = module.multiply(
            module.derivative(left, j), module.derivative(right, i)
        )
        for key, value in module.scale(
            module.add(first, module.scale(second, -1)), 2
        ).items():
            coordinate = (i, j, *key)
            need(coordinate in COORDINATES, "complete fixed curvature coordinate box")
            values[COORDINATES.index(coordinate)] = value
    return values


def row_rank(rows):
    need(len(rows) <= 5000, "registered rank row cap")
    pivots, selected = {}, []
    for index, row in enumerate(rows):
        need(
            all(type(k) is int and 0 <= k < 36 for k in row), "fixed source coordinates"
        )
        vector = {k: exact(v) for k, v in row.items() if v}
        while vector:
            pivot = min(vector)
            if pivot not in pivots:
                lead = vector[pivot]
                pivots[pivot] = {k: exact(v / lead) for k, v in vector.items()}
                selected.append(index)
                break
            lead = vector[pivot]
            for k, v in pivots[pivot].items():
                value = exact(vector.get(k, F()) - lead * v)
                if value:
                    vector[k] = value
                else:
                    vector.pop(k, None)
    return {
        "rank": len(pivots),
        "independent_rows": selected,
        "pivot_coordinates": list(pivots),
        "normalized_rows": [sparse(row) for row in pivots.values()],
    }


def sparse(row):
    return [[i, str(v)] for i, v in sorted(row.items()) if v]


def rectangles(module):
    result = []
    for i, j in PAIRS:
        unused = next(k for k in range(3) if k not in (i, j))
        for x, y, z in product(
            (F(1, 3), F(2, 3)), (F(1, 3), F(2, 3)), (F(1, 4), F(1, 2), F(3, 4))
        ):
            lower, upper = [F()] * 3, [F()] * 3
            for k, center in ((i, x), (j, y)):
                lower[k], upper[k] = center - F(1, 48), center + F(1, 48)
            lower[unused] = upper[unused] = z
            row = {}
            for c, (a, b, *powers) in enumerate(COORDINATES):
                if (a, b) == (i, j):
                    row[c] = module.integrate_rectangle(
                        {tuple(powers): F(1)}, (i, j), lower, upper
                    )
            result.append(
                {
                    "pair": (i, j),
                    "lower": tuple(lower),
                    "upper": tuple(upper),
                    "evaluation": row,
                }
            )
    need(
        len(result) == 36 and row_rank([r["evaluation"] for r in result])["rank"] == 36,
        "full rectangle interpolation rank",
    )
    return result


def geometric_checks(module, records, rows, polynomials):
    design = rectangles(module)
    basis = row_rank(rows)["independent_rows"]
    checks = []
    for index in basis:
        n, m, _, _, _ = records[index]
        values = []
        for rect in design:
            i, j = rect["pair"]
            lower, upper = rect["lower"], rect["upper"]
            corner_i, corner_j = list(lower), list(lower)
            corner_i[i], corner_j[j] = upper[i], upper[j]
            edge = lambda a, b, left=polynomials[n], right=polynomials[m]: (
                module.edge_integral(left, right, a, b)
            )
            actual = (
                edge(lower, corner_j)
                + edge(corner_j, upper)
                - edge(lower, corner_i)
                - edge(corner_i, upper)
            )
            expected = sum(
                (v * rect["evaluation"].get(k, F()) for k, v in rows[index].items()),
                F(),
            )
            need(
                actual == expected,
                "four literal source edges equal original curvature area",
            )
            values.append(str(actual))
        checks.append(
            {
                "record_index": index,
                "n": n,
                "m": m,
                "all36_actual_rectangle_differences": values,
            }
        )
    return {
        "rectangle_coordinate_matrix_rank": 36,
        "complete_row_basis_four_edge_checks": checks,
        "rectangles": [
            {
                "pair": r["pair"],
                "lower": list(map(str, r["lower"])),
                "upper": list(map(str, r["upper"])),
                "evaluation": sparse(r["evaluation"]),
            }
            for r in design
        ],
    }


def discover(phase):
    need(phase in ("calibration", "heldout"), "declared phase")
    module, provenance = source()
    maximum = 30 if phase == "calibration" else 900
    numbers = [n for n in range(1, maximum + 1) if exponents(n) is not None]
    thresholds = [h for h in numbers if phase == "calibration" or h > 30]
    need(len(thresholds) <= 200, "registered complete threshold cap")
    polynomials = {n: half_source(module, n) for n in numbers}
    records = [
        (n, m, gcd(n, m), n // gcd(n, m), m // gcd(n, m))
        for n in numbers
        for m in numbers
        if n * m <= maximum
    ]
    need(len(records) <= 5000, "registered complete pair cap")
    rows = [
        curvature(module, polynomials[n], polynomials[m]) for n, m, _, _, _ in records
    ]
    panels = []
    for horizon in thresholds:
        indices = [i for i, (n, m, _, _, _) in enumerate(records) if n * m <= horizon]
        physical = {}
        for index in indices:
            _, _, d, a, b = records[index]
            vector = physical.setdefault((a, b), {})
            for k, value in rows[index].items():
                vector[k] = exact(vector.get(k, F()) + value / d)
        ratios = sorted(physical)
        need(len(ratios) <= 2000, "complete physical ratio cap")
        raw_rank = row_rank([rows[i] for i in indices])
        image_rank = row_rank([physical[ratio] for ratio in ratios])
        if horizon == 25:
            need(
                (len(indices), raw_rank["rank"], image_rank["rank"]) == (63, 6, 6),
                "frozen H25 calibration",
            )
        panels.append(
            {
                "horizon": horizon,
                "complete_record_indices": indices,
                "record_count": len(indices),
                "ratio_count": len(ratios),
                "source_rank": raw_rank,
                "physical_rank": image_rank,
                "all_physical_curvature_rows": [
                    {"ratio": ratio, "coordinates": sparse(physical[ratio])}
                    for ratio in ratios
                ],
            }
        )
    geometry = geometric_checks(module, records, rows, polynomials)
    if maximum == 900:
        need(
            row_rank(rows)["rank"] == 20,
            "declared full three-schedule source-rank theorem at H900",
        )
    owned = {
        p.relative_to(ROOT).as_posix(): sha256(
            p.read_bytes().replace(b"\r\n", b"\n")
        ).hexdigest()
        for p in (Path(__file__), HERE / "NATIVE_HORIZON_RANK_PREREGISTRATION.md")
    }
    result = {
        "schema": "native-original-horizon-curvature-discovery-v1",
        "phase": phase,
        "source": provenance,
        "owned_sha256_lf": owned,
        "coordinates": COORDINATES,
        "complete_source_records": [
            {"n": n, "m": m, "d": d, "a": a, "b": b, "curvature": sparse(row)}
            for (n, m, d, a, b), row in zip(records, rows, strict=True)
        ],
        "all_declared_thresholds": panels,
        "geometry": geometry,
        "source_theory_full_rank_prediction": 20,
        "predicted_rank_is_not_assigned": True,
        "all_height_physical_rank_theorem_claimed": False,
        "native_gamma_decoder_claimed": False,
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    raw = canonical(result) + "\n"
    need(len(raw.encode()) <= MAX_BYTES, "registered retained artifact byte cap")
    summary = {
        "phase": phase,
        "proof_object_sha256": result["proof_object_sha256"],
        "complete_records": len(records),
        "panels": [
            {
                "horizon": row["horizon"],
                "source_rank": row["source_rank"]["rank"],
                "physical_rank": row["physical_rank"]["rank"],
            }
            for row in panels
        ],
    }
    return raw, summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--phase", choices=("calibration", "heldout"), required=True)
    args = parser.parse_args()
    raw, summary = discover(args.phase)
    target = HERE / f"native_horizon_rank.{args.phase}.json"
    target.write_text(raw, encoding="utf-8")
    print(canonical(summary))


if __name__ == "__main__":
    main()
