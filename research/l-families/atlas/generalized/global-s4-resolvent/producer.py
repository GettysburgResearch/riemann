"""Bounded exact S4 arithmetic replay from six explicit quotient curves."""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[4]
PRECURSOR = "dc4db621017ddaa8aeca1acfb211374dc0f04501"
EXPECTED_SOURCE_HASH = (
    "358242be11b7eb6e893c45e666d57e53bdf8c1c60adc8e03c0c8666589ccd6af"
)
NAMES = ("one", "sign", "two", "std", "tw")
CHARACTERS = {
    "identity": (1, 1, 2, 3, 3),
    "transposition": (1, -1, 0, 1, -1),
    "double_transposition": (1, 1, 2, -1, -1),
    "three_cycle": (1, 1, -1, 0, 0),
    "four_cycle": (1, -1, 0, -1, 1),
}
CLASS_SIZES = (1, 6, 3, 8, 6)


def load_helper():
    path = ROOT.parent / "global-s3-prym" / "descent_replay.py"
    result = subprocess.run(
        ["git", "show", f"{PRECURSOR}:{path.relative_to(REPO).as_posix()}"],
        cwd=REPO,
        capture_output=True,
        check=False,
    )

    def normalize(data):
        return data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")

    if result.returncode or normalize(result.stdout) != normalize(path.read_bytes()):
        raise ValueError("bounded field helper differs from its frozen source")
    spec = importlib.util.spec_from_file_location("s4_frozen_descent", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


D = load_helper()
P = D.P


def make_field(p, degree):
    P.require_int(p, "source prime", 5, 7)
    P.require_int(degree, "source extension", 1, 6)
    if p == 5:
        return D.DescentField(p, degree)
    if p == 7 and degree <= 4:
        return P.Field(p, degree)
    raise ValueError("field outside separately declared p5/n6 or p7/n4 caps")


def validate_curve(field, b, c):
    P.require_int(b, "b", -32, 32)
    P.require_int(c, "c", -32, 32)
    if b % field.p == 0:
        raise ValueError("b=0 is the cyclic rather than S4 stratum")
    if (256 * c**3 - 27 * b**4) % field.p == 0:
        raise ValueError("singular quartic discriminant")


def quartic(field, x, b, c):
    x2 = field.mul(x, x)
    return field.add_constant(field.add(field.mul(x2, x2), field.scale(x, b)), c)


def remaining_discriminant(field, x, b):
    x3 = field.mul(field.mul(x, x), x)
    return field.add_constant(
        field.add(field.scale(field.mul(x3, x3), -16), field.scale(x3, -40 * b)),
        -27 * b * b,
    )


def discriminant(field, u, b, c):
    value = field.add_constant(field.scale(field.mul(u, u), -1), c)
    return field.add_constant(
        field.scale(field.mul(field.mul(value, value), value), 256), -27 * b**4
    )


def resolvent_rhs(field, z, b, c):
    z2 = field.mul(z, z)
    return field.add(
        field.add(field.scale(field.mul(z2, z2), -1), field.scale(z2, 4 * c)),
        field.scale(z, b * b),
    )


def finite_class(roots, sign, minus_two):
    P.require_int(roots, "quartic distinct roots", 0, 4)
    P.require_int(sign, "discriminant character", -1, 1)
    if type(minus_two) is not int or minus_two not in (-1, 1):
        raise ValueError("minus-two character must be exactly plus or minus one")
    if sign == 0:
        if roots != 2 + minus_two:
            raise ArithmeticError("ramified residual quadratic has wrong splitting")
        return (
            "branch_split" if minus_two == 1 else "branch_nonsplit",
            (1, 0, 1, 1 + minus_two, minus_two),
        )
    classes = {
        (4, 1): "identity",
        (2, -1): "transposition",
        (0, 1): "double_transposition",
        (1, 1): "three_cycle",
        (0, -1): "four_cycle",
    }
    if (roots, sign) not in classes:
        raise ArithmeticError("impossible smooth quartic root/discriminant class")
    label = classes[roots, sign]
    return label, CHARACTERS[label]


def infinity_traces(minus_one):
    if type(minus_one) is not int or minus_one not in (-1, 1):
        raise ValueError("minus-one character must be exactly plus or minus one")
    return (1, minus_one, 1 + minus_one, 1, minus_one)


def count_source(field, b, c):
    validate_curve(field, b, c)
    q = field.q
    square_roots = [[] for _ in range(q)]
    for value in range(q):
        square_roots[field.mul(value, value)].append(value)
    chi_minus_one = len(square_roots[(-1) % field.p]) - 1
    chi_minus_two = len(square_roots[(-2) % field.p]) - 1
    infinity = {
        "E": 2,
        "D": 1 + chi_minus_one,
        "R": 1 + chi_minus_one,
        "C": 2 * (1 + chi_minus_one),
        "G": 1 + chi_minus_one,
        "H": 1 + chi_minus_one,
    }
    counts = dict(infinity)
    e_fibres = [0] * q
    c_fibres = [0] * q
    r_fibres = [0] * q
    map_coverage = 0
    for x in range(q):
        fx = quartic(field, x, b, c)
        gx = remaining_discriminant(field, x, b)
        counts["E"] += len(square_roots[fx])
        counts["G"] += len(square_roots[gx])
        counts["H"] += len(square_roots[field.mul(fx, gx)])
        counts["C"] += len(square_roots[fx]) * len(square_roots[gx])
        counts["R"] += len(square_roots[resolvent_rhs(field, x, b, c)])
        for y in square_roots[fx]:
            e_fibres[y] += 1
            c_fibres[y] += len(square_roots[gx])
        # R -> P1_u is defined here away from the extra infinity point (0,0).
        if x != 0:
            inverse_2x = field.power(field.scale(x, 2), q - 2)
            for y in square_roots[resolvent_rhs(field, x, b, c)]:
                u = field.mul(y, inverse_2x)
                rhs = field.add(
                    field.mul(field.mul(x, x), x),
                    field.scale(
                        field.mul(
                            field.add_constant(field.scale(field.mul(u, u), -1), c), x
                        ),
                        -4,
                    ),
                )
                if field.add_constant(rhs, -b * b) != 0:
                    raise ArithmeticError("resolvent map misses its primitive cubic")
                r_fibres[u] += 1
                map_coverage += 1
    stalk_sums = list(infinity_traces(chi_minus_one))
    class_census = Counter()
    branch_points = []
    regular_count = 12 if chi_minus_one == 1 else 0
    for u in range(q):
        d_value = discriminant(field, u, b, c)
        d_roots = len(square_roots[d_value])
        counts["D"] += d_roots
        label, traces = finite_class(e_fibres[u], d_roots - 1, chi_minus_two)
        class_census[label] += 1
        if label.startswith("branch_"):
            branch_points.append(u)
        if e_fibres[u] != traces[0] + traces[3]:
            raise ArithmeticError("standard stalk fails its original quartic fibre")
        if r_fibres[u] != traces[0] + traces[2]:
            raise ArithmeticError("pair-partition stalk fails its resolvent fibre")
        if c_fibres[u] != traces[0] + traces[1] + traces[3] + traces[4]:
            raise ArithmeticError("sign-standard stalk fails its A3 source fibre")
        for i, trace in enumerate(traces):
            stalk_sums[i] += trace
        regular_count += sum(d * t for d, t in zip(CHARACTERS["identity"], traces))
    if map_coverage != counts["R"] - infinity["R"] - 1:
        raise ArithmeticError("resolvent coverage omitted affine points")
    if counts["C"] != counts["E"] + counts["G"] + counts["H"] - 2 * (q + 1):
        raise ArithmeticError("primitive V4 source identity failed")
    for name, index in (("D", 1), ("R", 2), ("E", 3)):
        if stalk_sums[index] != counts[name] - q - 1:
            raise ArithmeticError("complete curve trace differs from its stalk sum")
    if stalk_sums[4] != counts["C"] - counts["D"] - counts["E"] + q + 1:
        raise ArithmeticError("sign-standard cohomology extraction failed")
    if regular_count != q + 1 + sum(
        d * s for d, s in zip(CHARACTERS["identity"][1:], stalk_sums[1:])
    ):
        raise ArithmeticError("normalized regular cover trace failed")
    return {
        "extension": field.n,
        "field_order": q,
        "modulus": field.modulus,
        "curve_points": counts,
        "projective_infinity_points": infinity,
        "infinity_stalk_traces": dict(zip(NAMES, infinity_traces(chi_minus_one))),
        "finite_branch_character_minus_two": chi_minus_two,
        "finite_branch_points": branch_points,
        "finite_class_census": dict(sorted(class_census.items())),
        "local_stalk_sums": dict(zip(NAMES, stalk_sums)),
        "Z_points_from_normalized_local_regular_character": regular_count,
        "resolvent_affine_map_checks": map_coverage,
    }


def reciprocal_from_sums(sums, q, genus):
    if len(sums) < genus:
        raise ValueError("not enough independent source traces for first half")
    first_half = P.newton_from_local_sums(sums[:genus])
    return D.reciprocal_completion(first_half, q, genus)


def build_panel(curve):
    p, b, c = curve["p"], curve["b"], curve["c"]
    rows = [count_source(make_field(p, n), b, c) for n in curve["extensions"]]
    factors = {}
    for name, genus in (("E", 1), ("D", 2), ("R", 1), ("G", 2), ("H", 4)):
        sums = [r["curve_points"][name] - r["field_order"] - 1 for r in rows]
        factors[name] = reciprocal_from_sums(sums, p, genus)
        if P.local_sums_from_polynomial(factors[name], len(rows)) != sums:
            raise ArithmeticError("curve polynomial fails independent extension counts")
    tw_sums = [r["local_stalk_sums"]["tw"] for r in rows]
    factors["tw"] = reciprocal_from_sums(tw_sums, p, 4)
    if P.local_sums_from_polynomial(factors["tw"], len(rows)) != tw_sums:
        raise ArithmeticError("degree-eight determinant fails held-out extensions")
    if D.int_product(factors["G"], factors["H"]) != D.int_product(
        factors["D"], factors["tw"]
    ):
        raise ArithmeticError(
            "independently reconstructed polynomial quotient identity failed"
        )
    factors["C"] = D.int_product(
        D.int_product(factors["E"], factors["D"]), factors["tw"]
    )
    z = factors["D"]
    for name, exponent in (("R", 2), ("E", 3), ("tw", 3)):
        for _ in range(exponent):
            z = D.int_product(z, factors[name])
    factors["Z"] = z
    for name in ("C", "Z"):
        sums = [
            (
                r["curve_points"]["C"]
                if name == "C"
                else r["Z_points_from_normalized_local_regular_character"]
            )
            - r["field_order"]
            - 1
            for r in rows
        ]
        if P.local_sums_from_polynomial(factors[name], len(rows)) != sums:
            raise ArithmeticError(
                "factored larger-curve determinant fails local counts"
            )
    return {
        "id": curve["id"],
        "p": p,
        "b": b,
        "c": c,
        "rows": rows,
        "polynomials": factors,
    }


def build(source):
    if P.digest(source) != EXPECTED_SOURCE_HASH:
        raise ValueError("source differs from its frozen typed primitive identity")
    return {
        "schema": "bring-quartic-s4-resolvent-artifact-v1",
        "source_hash": P.digest(source),
        "panels": [build_panel(curve) for curve in source["curves"]],
    }


def bindings():
    return {
        "schema": "bring-quartic-s4-resolvent-binding-v1",
        "precursor_commit": PRECURSOR,
        "files": {
            name: P.lf_hash(ROOT / name)
            for name in (
                "source.json",
                "producer.py",
                "test_producer.py",
                "S4_RESOLVENT_AND_RAMIFIED_FROBENIUS.md",
                "REPLAY_CONTRACT.md",
                "artifact.json",
            )
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    source = json.loads((ROOT / "source.json").read_text(encoding="utf-8"))
    artifact = build(source)
    if args.write:
        (ROOT / "artifact.json").write_text(
            json.dumps(artifact, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        (ROOT / "provenance.json").write_text(
            json.dumps(bindings(), indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    else:
        for name, expected in (
            ("artifact.json", artifact),
            ("provenance.json", bindings()),
        ):
            P.require_same_json(
                json.loads((ROOT / name).read_text(encoding="utf-8")), expected, name
            )
    print(
        "PASS: complete S4 quotient curves, normalized ramified Frobenius, and source determinants"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
