"""Independent all-constituent Euler multiplication at actual S4 closed places."""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[4]
PRECURSOR = "d19f421b438485c953469be59c4df8f79a30d2bf"
CLOSED_HELPER = "4ba9cf883ecf49fe0034d6b05a878caf2768d263"
SOURCE_HASH = "11923cda2c37b39952e70d67f3810ea64923059afe97529407f064e480b1df0b"
CUTOFF = 4


def authenticate(commit, directory, names):
    def normalize(data):
        return data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")

    for name in names:
        path = directory / name
        result = subprocess.run(
            ["git", "show", f"{commit}:{path.relative_to(REPO).as_posix()}"],
            cwd=REPO,
            capture_output=True,
            check=False,
        )
        if result.returncode or normalize(result.stdout) != normalize(
            path.read_bytes()
        ):
            raise ValueError(f"frozen S4 Euler dependency differs: {name}")


def load_sources():
    authenticate(
        PRECURSOR,
        ROOT,
        (
            "source.json",
            "producer.py",
            "test_producer.py",
            "artifact.json",
            "provenance.json",
            "S4_RESOLVENT_AND_RAMIFIED_FROBENIUS.md",
            "REPLAY_CONTRACT.md",
        ),
    )
    helper_dir = ROOT.parent / "global-s3-prym"
    authenticate(CLOSED_HELPER, helper_dir, ("closed_euler.py",))
    modules = []
    for name, path in (
        ("s4_euler_source", ROOT / "producer.py"),
        ("s4_closed_helper", helper_dir / "closed_euler.py"),
    ):
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        modules.append(module)
    return tuple(modules)


S, E = load_sources()
P = S.P
NAMES = S.NAMES


def product(*factors):
    result = [1]
    for factor in factors:
        result = S.D.int_product(result, factor)
    return result


def finite_denominators(label):
    if type(label) is not str:
        raise TypeError("source class must be a literal class label")
    minus, plus = [1, -1], [1, 1]
    if label == "identity":
        values = (
            minus,
            product(minus, minus),
            product(minus, minus, minus),
            product(minus, minus, minus),
        )
    elif label == "transposition":
        values = (
            plus,
            [1, 0, -1],
            product(minus, [1, 0, -1]),
            product(minus, plus, plus),
        )
    elif label == "double_transposition":
        values = (
            minus,
            product(minus, minus),
            product(minus, plus, plus),
            product(minus, plus, plus),
        )
    elif label == "three_cycle":
        values = (minus, [1, 1, 1], [1, 0, 0, -1], [1, 0, 0, -1])
    elif label == "four_cycle":
        values = (plus, [1, 0, -1], product(plus, [1, 0, 1]), product(minus, [1, 0, 1]))
    elif label in ("branch_split", "branch_nonsplit"):
        epsilon = 1 if label == "branch_split" else -1
        values = ([1], minus, product(minus, [1, -epsilon]), [1, -epsilon])
    else:
        raise ValueError("unknown S4 arithmetic source class")
    return dict(zip(NAMES, (minus,) + values))


def infinity_denominators(p):
    P.require_int(p, "base prime", 5, 7)
    if p not in (5, 7):
        raise ValueError("undeclared base prime")
    delta = 1 if p % 4 == 1 else -1
    minus, signed = [1, -1], [1, -delta]
    return dict(zip(NAMES, (minus, signed, product(minus, signed), minus, signed)))


def reciprocal(denominator, degree):
    P.require_int(degree, "place degree", 1, CUTOFF)
    if type(denominator) is not list or not denominator or denominator[0] != 1:
        raise ValueError("local denominator must start at one")
    if len(denominator) > 4 or any(
        type(x) is not int or abs(x) > 3 for x in denominator
    ):
        raise ValueError("local denominator outside the source contract")
    result = [1] + [0] * CUTOFF
    for n in range(1, CUTOFF + 1):
        result[n] = -sum(
            denominator[k] * result[n - k * degree]
            for k in range(1, min(len(denominator) - 1, n // degree) + 1)
        )
    return result


def multiply(left, right):
    if len(left) != CUTOFF + 1 or len(right) != CUTOFF + 1:
        raise ValueError("Euler multiplication uses the fixed degree-four cutoff")
    return [
        sum(left[j] * right[i - j] for j in range(i + 1)) for i in range(CUTOFF + 1)
    ]


def census(field, b, c):
    if field.n > CUTOFF or field.q > 2401:
        raise ValueError("closed-place field exceeds the separate degree-four cap")
    S.validate_curve(field, b, c)
    roots, squares = [0] * field.q, [0] * field.q
    for x in range(field.q):
        roots[S.quartic(field, x, b, c)] += 1
        squares[field.mul(x, x)] += 1
    epsilon = squares[(-2) % field.p] - 1
    places = E.closed_places(field)
    records, histogram = [], Counter()
    for place in places:
        u = place["representative"]
        label, _ = S.finite_class(
            roots[field.mul(u, u)], squares[S.discriminant(field, u, b, c)] - 1, epsilon
        )
        records.append(
            {"minimal_polynomial": place["minimal_polynomial"], "source_class": label}
        )
        histogram[label] += 1
    return {
        "degree": field.n,
        "field_order": field.q,
        "field_modulus": field.modulus,
        "place_count": len(places),
        "all_primitive_places_digest": P.digest(records),
        "classes": {
            label: {
                "count": histogram[label],
                "denominators": finite_denominators(label),
            }
            for label in sorted(histogram)
        },
    }


def multiply_censuses(rows, infinity):
    expected_degrees = list(range(1, CUTOFF + 1))
    if [r["degree"] for r in rows] != expected_degrees:
        raise ValueError("all four closed-place degrees are required exactly once")
    result = {name: reciprocal(infinity[name], 1) for name in NAMES}
    for row in rows:
        for group in row["classes"].values():
            for name in NAMES:
                local = reciprocal(group["denominators"][name], row["degree"])
                for _ in range(group["count"]):
                    result[name] = multiply(result[name], local)
    return result


def build(source):
    if P.digest(source) != SOURCE_HASH:
        raise ValueError("closed-place primitive source identity differs")
    precursor = json.loads((ROOT / "artifact.json").read_text(encoding="utf-8"))
    panels = []
    if [p["id"] for p in precursor["panels"]] != source["source_panels"]:
        raise ValueError("precursor panel roster differs")
    for panel in precursor["panels"]:
        p, b, c = panel["p"], panel["b"], panel["c"]
        rows = [census(P.Field(p, degree), b, c) for degree in range(1, CUTOFF + 1)]
        infinity = infinity_denominators(p)
        products = multiply_censuses(rows, infinity)
        expected = {"one": [sum(p**j for j in range(k + 1)) for k in range(CUTOFF + 1)]}
        for name, factor in (("sign", "D"), ("two", "R"), ("std", "E"), ("tw", "tw")):
            coefficients = panel["polynomials"][factor]
            expected[name] = (coefficients + [0] * (CUTOFF + 1))[: CUTOFF + 1]
        P.require_same_json(products, expected, "all five closed-place Euler products")
        panels.append(
            {
                "id": panel["id"],
                "p": p,
                "b": b,
                "c": c,
                "censuses": rows,
                "infinity_denominators": infinity,
                "euler_products_mod_T5": products,
            }
        )
    return {
        "schema": "bring-s4-closed-place-artifact-v1",
        "source_hash": P.digest(source),
        "panels": panels,
    }


def bindings():
    return {
        "schema": "bring-s4-closed-place-binding-v1",
        "precursor_commit": PRECURSOR,
        "files": {
            name: P.lf_hash(ROOT / name)
            for name in (
                "euler_source.json",
                "closed_euler.py",
                "test_closed_euler.py",
                "CLOSED_PLACE_EULER_FACTORS.md",
                "euler_artifact.json",
            )
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    artifact = build(
        json.loads((ROOT / "euler_source.json").read_text(encoding="utf-8"))
    )
    if args.write:
        (ROOT / "euler_artifact.json").write_text(
            json.dumps(artifact, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        (ROOT / "euler_provenance.json").write_text(
            json.dumps(bindings(), indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    else:
        for name, expected in (
            ("euler_artifact.json", artifact),
            ("euler_provenance.json", bindings()),
        ):
            P.require_same_json(
                json.loads((ROOT / name).read_text(encoding="utf-8")), expected, name
            )
    print(
        "PASS: all S4 closed-place Euler factors agree with the geometric determinants modulo T5"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
