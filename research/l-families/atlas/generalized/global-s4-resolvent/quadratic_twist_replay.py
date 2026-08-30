"""Actual S4 quadratic-twist quotient curves and diagonal-inertia replay."""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[4]
HELPER = "3d3b52541ed33b516c25ec0a27ba3eb568ec513b"
SOURCE_HASH = "3724d303ecef59e3504f958e416381b4f87d865b433d8301d2ce9a1c18d09cf0"


def load_helper():
    path = ROOT / "closed_euler.py"
    result = subprocess.run(
        ["git", "show", f"{HELPER}:{path.relative_to(REPO).as_posix()}"],
        cwd=REPO,
        capture_output=True,
        check=False,
    )

    def normalize(data):
        return data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")

    if result.returncode or normalize(result.stdout) != normalize(path.read_bytes()):
        raise ValueError("quadratic twist helper differs from frozen source")
    spec = importlib.util.spec_from_file_location("s4_twist_frozen", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


C = load_helper()
S, P = C.S, C.P
NAMES = S.NAMES
DIMS = S.CHARACTERS["identity"]


def inverse_table(field):
    """All nonzero inverses with one exponentiation and O(q) products."""
    if field.q > 15625:
        raise ValueError("inverse table exceeds the declared field cap")
    prefix = [1] * field.q
    for x in range(1, field.q):
        prefix[x] = field.mul(prefix[x - 1], x)
    carry = field.power(prefix[-1], field.q - 2)
    result = [0] * field.q
    for x in range(field.q - 1, 0, -1):
        result[x] = field.mul(carry, prefix[x - 1])
        carry = field.mul(carry, x)
    if carry != 1:
        raise ArithmeticError("batch inverse reconstruction failed")
    return result


def twisted_infinity(field):
    delta = 1 if field.q % 4 == 1 else -1
    return dict(zip(NAMES, (0, 0, 0, 1 + delta, 1 + delta)))


def count_source(field, b, c):
    if field.q > 15625 or field.p not in (5, 7) or field.n > (6 if field.p == 5 else 4):
        raise ValueError("quadratic twist field exceeds the declared source caps")
    S.validate_curve(field, b, c)
    q = field.q
    square, fourth = [0] * q, [0] * q
    for value in range(q):
        value2 = field.mul(value, value)
        square[value2] += 1
        fourth[field.mul(value2, value2)] += 1
    delta, epsilon = square[(-1) % field.p] - 1, square[(-2) % field.p] - 1
    infinity = {"Dchi": 1, "X": 3 + delta, "Rchi": 2 + delta, "Cchi": 4 * (1 + delta)}
    counts = dict(infinity)
    old = {"E": 2, "D": 1 + delta, "R": 1 + delta, "C": 2 * (1 + delta)}
    quartic_hist = [0] * q
    inverses = inverse_table(field)
    inverse_four = pow(4, -1, field.p)
    for x in range(q):
        fx, gx = S.quartic(field, x, b, c), S.remaining_discriminant(field, x, b)
        quartic_hist[fx] += 1
        counts["X"] += fourth[fx]
        counts["Cchi"] += fourth[fx] * square[gx]
        old["E"] += square[fx]
        old["C"] += square[fx] * square[gx]
        old["R"] += square[S.resolvent_rhs(field, x, b, c)]
        disc = S.discriminant(field, x, b, c)
        old["D"] += square[disc]
        counts["Dchi"] += square[field.mul(x, disc)]
        if x:
            numerator = field.add_constant(
                field.add(
                    field.scale(field.mul(field.mul(x, x), x), -1),
                    field.scale(x, 4 * c),
                ),
                b * b,
            )
            rhs = field.mul(numerator, field.scale(inverses[x], inverse_four))
            counts["Rchi"] += fourth[rhs]
    sums = twisted_infinity(field)
    regular_old = 12 if delta == 1 else 0
    regular_joint = 2 * regular_old
    census = Counter()
    rational_branch_twists = []
    for u in range(q):
        disc = S.discriminant(field, u, b, c)
        label, traces = S.finite_class(
            quartic_hist[field.mul(u, u)], square[disc] - 1, epsilon
        )
        character = square[u] - 1
        census[f"{label}:chi={character}"] += 1
        if label.startswith("branch_"):
            rational_branch_twists.append(
                {"u": u, "chi_u": character, "old_class": label}
            )
        old_fibre = sum(d * t for d, t in zip(DIMS, traces))
        if old_fibre not in (0, 12, 24):
            raise ArithmeticError("invalid normalized S4 regular fibre")
        regular_old += old_fibre
        regular_joint += (1 + character) * old_fibre
        for name, trace in zip(NAMES, traces):
            sums[name] += character * trace
    expected = {
        "one": 0,
        "sign": counts["Dchi"] - q - 1,
        "two": counts["Rchi"] - old["R"],
        "std": counts["X"] - old["E"],
    }
    expected["tw"] = counts["Cchi"] - old["C"] - expected["sign"] - expected["std"]
    P.require_same_json(
        sums, expected, "twisted quotient count versus all local stalk traces"
    )
    if regular_joint != regular_old + sum(
        d * sums[name] for d, name in zip(DIMS, NAMES)
    ):
        raise ArithmeticError("joint regular-character source decomposition failed")
    if regular_old < 0 or regular_joint < 0 or regular_joint > 2 * regular_old:
        raise ArithmeticError("quadratic cover has impossible rational fibre count")
    return {
        "extension": field.n,
        "field_order": q,
        "modulus": field.modulus,
        "counts": counts,
        "old_counts": old,
        "projective_exceptional_points": infinity,
        "twisted_stalk_sums": sums,
        "twisted_infinity_stalk_traces": twisted_infinity(field),
        "twisted_infinity_stalk_dimensions": dict(zip(NAMES, (0, 0, 0, 2, 2))),
        "finite_class_census": dict(sorted(census.items())),
        "rational_branch_twists": rational_branch_twists,
        "Z_points_from_normalized_regular_character": regular_old,
        "Ztilde_points_from_normalized_joint_regular_character": regular_joint,
        "signed_regular_source_sum": regular_joint - regular_old,
    }


def build_panel(curve, old_panel):
    p, b, c = curve["p"], curve["b"], curve["c"]
    if (p, b, c, curve["id"]) != (
        old_panel["p"],
        old_panel["b"],
        old_panel["c"],
        old_panel["id"],
    ):
        raise ValueError("twist source is not the declared frozen S4 curve")
    rows = [count_source(S.make_field(p, n), b, c) for n in curve["extensions"]]
    factors = {}
    for name, genus in (("sign", 3), ("two", 3), ("std", 2), ("tw", 5)):
        sums = [row["twisted_stalk_sums"][name] for row in rows]
        if len(rows) >= genus:
            factors[name] = S.reciprocal_from_sums(sums, p, genus)
            if P.local_sums_from_polynomial(factors[name], len(rows)) != sums:
                raise ArithmeticError(
                    "twisted factor fails independent extension trace"
                )
        else:
            factors[name] = None
    tw_prefix = P.newton_from_local_sums(
        [row["twisted_stalk_sums"]["tw"] for row in rows[:4]]
    )
    old_polys = old_panel["polynomials"]
    curve_polys = {
        "Dchi": factors["sign"],
        "X": C.product(old_polys["E"], factors["std"]),
        "Rchi": C.product(old_polys["R"], factors["two"]),
        "Cchi": None,
        "Ztilde": None,
    }
    if factors["tw"] is not None:
        curve_polys["Cchi"] = C.product(
            old_polys["C"], factors["sign"], factors["std"], factors["tw"]
        )
        anti = factors["sign"]
        for name, exponent in (("two", 2), ("std", 3), ("tw", 3)):
            for _ in range(exponent):
                anti = C.product(anti, factors[name])
        if len(anti) != 61:
            raise ArithmeticError("regular anti cohomology has wrong rank")
        curve_polys["Ztilde"] = C.product(old_polys["Z"], anti)
    for name, polynomial in curve_polys.items():
        if polynomial is None:
            continue
        source_sums = [
            (
                row["counts"][name]
                if name != "Ztilde"
                else row["Ztilde_points_from_normalized_joint_regular_character"]
            )
            - row["field_order"]
            - 1
            for row in rows
        ]
        if P.local_sums_from_polynomial(polynomial, len(rows)) != source_sums:
            raise ArithmeticError(
                "twisted curve factorization fails primitive point counts"
            )
    for row, old_row in zip(rows, old_panel["rows"]):
        for name, value in row["old_counts"].items():
            if value != old_row["curve_points"][name]:
                raise ArithmeticError("untwisted companion changed from frozen source")
        if (
            row["Z_points_from_normalized_regular_character"]
            != old_row["Z_points_from_normalized_local_regular_character"]
        ):
            raise ArithmeticError("untwisted regular source differs")
    return {
        "id": curve["id"],
        "p": p,
        "b": b,
        "c": c,
        "rows": rows,
        "twisted_polynomials": factors,
        "tw_prefix_mod_T5": tw_prefix,
        "curve_polynomials": curve_polys,
        "full_degree_ten_available": factors["tw"] is not None,
        "degree_ten_held_out_extensions": [row["extension"] for row in rows[5:]],
    }


def build(source):
    if P.digest(source) != SOURCE_HASH:
        raise ValueError(
            "quadratic twist primitive source differs from frozen identity"
        )
    precursor = json.loads((ROOT / "artifact.json").read_text(encoding="utf-8"))
    if len(source["curves"]) != len(precursor["panels"]):
        raise ValueError("twist panel roster is incomplete")
    return {
        "schema": "bring-s4-quadratic-twist-artifact-v1",
        "source_hash": P.digest(source),
        "panels": [
            build_panel(curve, old)
            for curve, old in zip(source["curves"], precursor["panels"])
        ],
    }


def bindings():
    return {
        "schema": "bring-s4-quadratic-twist-binding-v1",
        "helper_commit": HELPER,
        "files": {
            name: P.lf_hash(ROOT / name)
            for name in (
                "quadratic_twist_source.json",
                "quadratic_twist_replay.py",
                "test_quadratic_twist_replay.py",
                "QUADRATIC_TWIST_SOURCE_AND_DIAGONAL_INERTIA.md",
                "quadratic_twist_artifact.json",
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
        json.loads((ROOT / "quadratic_twist_source.json").read_text(encoding="utf-8"))
    )
    if args.write:
        (ROOT / "quadratic_twist_artifact.json").write_text(
            json.dumps(artifact, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        (ROOT / "quadratic_twist_provenance.json").write_text(
            json.dumps(bindings(), indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    else:
        for name, expected in (
            ("quadratic_twist_artifact.json", artifact),
            ("quadratic_twist_provenance.json", bindings()),
        ):
            P.require_same_json(
                json.loads((ROOT / name).read_text(encoding="utf-8")), expected, name
            )
    print(
        "PASS: actual S4 quadratic twist, diagonal infinity inertia and quotient determinants"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
