"""Exact closed-place Euler multiplication through degree four."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[4]
PREFIX = ROOT.relative_to(REPO).as_posix()
FROZEN_COMMIT = "23ad35cc8010f72cf1df54f09eccb4dcba108879"
PRECURSOR_FILES = (
    "source.json",
    "producer.py",
    "test_producer.py",
    "GLOBAL_S3_PRYM_SOURCE.md",
    "README.md",
    "artifact.json",
    "provenance.json",
)
MAX_DEGREE = 4


def normalize(data: bytes) -> bytes:
    return data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def authenticate_precursor() -> dict:
    hashes = {}
    for name in PRECURSOR_FILES:
        result = subprocess.run(
            ["git", "show", f"{FROZEN_COMMIT}:{PREFIX}/{name}"],
            cwd=REPO,
            capture_output=True,
            check=False,
        )
        if result.returncode:
            raise ValueError(f"missing frozen precursor object: {name}")
        frozen = normalize(result.stdout)
        if normalize((ROOT / name).read_bytes()) != frozen:
            raise ValueError(
                f"precursor file differs from reviewed source identity: {name}"
            )
        hashes[name] = hashlib.sha256(frozen).hexdigest()
    return hashes


def load_primitive():
    authenticate_precursor()
    spec = importlib.util.spec_from_file_location(
        "gsp_frozen_primitive", ROOT / "producer.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


P = load_primitive()


def mobius(n: int) -> int:
    sign, divisor = 1, 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            n //= divisor
            sign = -sign
            if n % divisor == 0:
                return 0
        divisor += 1
    return -sign if n > 1 else sign


def closed_point_count(p: int, n: int) -> int:
    numerator = sum(mobius(n // d) * p**d for d in range(1, n + 1) if n % d == 0)
    if numerator % n:
        raise ArithmeticError("closed point count is not integral")
    return numerator // n


def minimal_polynomial(field, orbit: list[int]) -> list[int]:
    result = [1]
    for root in orbit:
        output = [0] * (len(result) + 1)
        for i, c in enumerate(result):
            output[i] = field.add(output[i], field.scale(field.mul(c, root), -1))
            output[i + 1] = field.add(output[i + 1], c)
        result = output
    if any(c >= field.p for c in result):
        raise ArithmeticError(
            "Frobenius orbit polynomial is not defined over the base field"
        )
    if not P.irreducible(result, field.p):
        raise ArithmeticError("closed place polynomial is reducible")
    return result


def closed_places(field) -> list[dict]:
    visited = set()
    rows = []
    for t in range(field.q):
        if t in visited:
            continue
        orbit, current = [], t
        for _ in range(field.n):
            if current in orbit:
                break
            orbit.append(current)
            current = field.power(current, field.p)
        if current != t or any(x in visited for x in orbit) or field.n % len(orbit):
            raise ArithmeticError("invalid or overlapping Frobenius orbit")
        visited.update(orbit)
        if len(orbit) == field.n:
            rows.append(
                {
                    "representative": t,
                    "minimal_polynomial": minimal_polynomial(field, orbit),
                }
            )
    if len(visited) != field.q or len(rows) != closed_point_count(field.p, field.n):
        raise ArithmeticError("closed-place coverage is incomplete")
    return rows


def local_denominators(
    field,
    A: int,
    B: int,
    t: int,
    cubic_histogram: list[int],
    square_histogram: list[int],
) -> tuple[list[int], list[int]]:
    roots = cubic_histogram[field.mul(t, t)]
    coefficient = field.add_constant(field.scale(field.mul(t, t), -1), B)
    discriminant = field.add_constant(
        field.scale(field.mul(coefficient, coefficient), -27), -4 * A**3
    )
    if discriminant == 0:
        if A % field.p:
            if roots != 2:
                raise ArithmeticError(
                    "simple discriminant fibre does not have two rational points"
                )
            standard = [1, -1]
        else:
            if roots != 1:
                raise ArithmeticError(
                    "cyclic discriminant fibre does not have one rational point"
                )
            standard = [1]
    else:
        if roots not in (0, 1, 3):
            raise ArithmeticError("invalid separable cubic factorization")
        standard = {0: [1, 1, 1], 1: [1, 0, -1], 3: [1, -2, 1]}[roots]
    if t == 0:
        twisted = [1]
    else:
        chi = square_histogram[t] - 1
        if chi not in (-1, 1):
            raise ArithmeticError("invalid nonzero Kummer character")
        twisted = [c * chi**i for i, c in enumerate(standard)]
    return standard, twisted


def histograms(field, A: int, B: int) -> tuple[list[int], list[int]]:
    cubic, square = [0] * field.q, [0] * field.q
    for x in range(field.q):
        cubic[field.cubic(x, A, B)] += 1
        square[field.mul(x, x)] += 1
    return cubic, square


def reciprocal_factor(denominator: list[int], degree: int, cutoff: int) -> list[int]:
    P.require_int(degree, "closed-place degree", 1, MAX_DEGREE)
    P.require_int(cutoff, "Euler cutoff", 1, MAX_DEGREE)
    if (
        type(denominator) is not list
        or not denominator
        or denominator[0] != 1
        or any(type(c) is not int for c in denominator)
    ):
        raise ValueError(
            "local denominator must have exact integral coefficients and constant term one"
        )
    embedded = [0] * (cutoff + 1)
    for i, c in enumerate(denominator):
        if degree * i <= cutoff:
            embedded[degree * i] = c
    inverse = [1] + [0] * cutoff
    for n in range(1, cutoff + 1):
        inverse[n] = -sum(embedded[j] * inverse[n - j] for j in range(1, n + 1))
    return inverse


def multiply_series(left: list[int], right: list[int], cutoff: int) -> list[int]:
    return [
        sum(left[i] * right[n - i] for i in range(n + 1)) for n in range(cutoff + 1)
    ]


def field_census(field, A: int, B: int, places: list[dict]) -> dict:
    cubic, square = histograms(field, A, B)
    census = Counter()
    records = []
    for row in places:
        standard, twisted = local_denominators(
            field, A, B, row["representative"], cubic, square
        )
        census[(tuple(standard), tuple(twisted))] += 1
        records.append(
            {
                "minimal_polynomial": row["minimal_polynomial"],
                "standard": standard,
                "twisted": twisted,
            }
        )
    return {
        "degree": field.n,
        "field_order": field.q,
        "closed_place_count": len(places),
        "all_closed_records_sha256": P.digest(records),
        "factors": [
            {"standard": list(key[0]), "twisted": list(key[1]), "count": value}
            for key, value in sorted(census.items())
        ],
    }


def multiply_censuses(censuses: list[dict], cutoff: int) -> tuple[list[int], list[int]]:
    P.require_int(cutoff, "Euler cutoff", 1, MAX_DEGREE)
    if [c["degree"] for c in censuses] != list(range(1, cutoff + 1)):
        raise ValueError(
            "Euler multiplication requires complete ordered degree coverage"
        )
    outputs = []
    for channel in ("standard", "twisted"):
        result = [1] + [0] * cutoff
        for census in censuses:
            for factor in census["factors"]:
                count = P.require_int(
                    factor["count"], "factor multiplicity", 1, P.MAX_FIELD
                )
                inverse = reciprocal_factor(factor[channel], census["degree"], cutoff)
                for _ in range(count):
                    result = multiply_series(result, inverse, cutoff)
        outputs.append(result)
    return tuple(outputs)


def build() -> dict:
    source = json.loads((ROOT / "source.json").read_text(encoding="utf-8"))
    if P.digest(source) != P.EXPECTED_SOURCE_HASH:
        raise ValueError("precursor primitive source is not canonical")
    artifact = json.loads((ROOT / "artifact.json").read_text(encoding="utf-8"))
    expected = {panel["source"]["id"]: panel for panel in artifact["panels"]}
    models, place_cache, rows = {}, {}, []
    for panel in source["panels"]:
        p, A, B = panel["p"], panel["A"], panel["B"]
        censuses = []
        for n in range(1, MAX_DEGREE + 1):
            if (p, n) not in models:
                models[p, n] = P.Field(p, n)
                place_cache[p, n] = closed_places(models[p, n])
            censuses.append(field_census(models[p, n], A, B, place_cache[p, n]))
        standard, twisted = multiply_censuses(censuses, MAX_DEGREE)
        match = expected[panel["id"]]
        P.require_same_json(
            standard, match["P_E"] + [0, 0], "closed Euler elliptic product"
        )
        P.require_same_json(twisted, match["P_prym"], "closed Euler Prym product")
        rows.append(
            {
                "source_id": panel["id"],
                "closed_place_censuses": censuses,
                "standard_product_mod_T5": standard,
                "twisted_product_mod_T5": twisted,
                "infinity_factors": {"standard": [1], "twisted": [1]},
            }
        )
    return {
        "schema": "closed-point-euler-v1",
        "precursor_commit": FROZEN_COMMIT,
        "precursor_source_hash": P.EXPECTED_SOURCE_HASH,
        "cutoff": MAX_DEGREE,
        "coverage": "Every closed place of degree <=4 for each source, including infinity; larger degrees do not affect this truncation.",
        "panels": rows,
    }


def bindings() -> dict:
    names = (
        "closed_euler.py",
        "test_closed_euler.py",
        "CLOSED_POINT_EULER_REPLAY.md",
        "closed_artifact.json",
    )
    return {
        "schema": "closed-euler-binding-v1",
        "precursor": authenticate_precursor(),
        "files": {name: P.lf_hash(ROOT / name) for name in names},
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--write", action="store_true")
    modes.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    artifact_path = ROOT / "closed_artifact.json"
    binding_path = ROOT / "closed_provenance.json"
    if args.write:
        artifact_path.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        binding_path.write_text(
            json.dumps(bindings(), indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    else:
        P.require_same_json(
            json.loads(artifact_path.read_text(encoding="utf-8")),
            result,
            "closed-place artifact",
        )
        P.require_same_json(
            json.loads(binding_path.read_text(encoding="utf-8")),
            bindings(),
            "closed-place source bindings",
        )
    print(
        "PASS: complete closed-place Euler products through degree four for all six frozen curves"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
