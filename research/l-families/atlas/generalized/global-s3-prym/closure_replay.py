"""Complete bounded S3-closure and two-elliptic-map primitive replay."""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[4]
HELPER_COMMIT = "4ba9cf883ecf49fe0034d6b05a878caf2768d263"
EXPECTED_SOURCE_HASH = (
    "bb588efaa1e3f6f281a7a8eaa090ea4835e905a854fb024d8ac2085c0c67a296"
)


def load_frozen_helper():
    path = ROOT / "closed_euler.py"
    result = subprocess.run(
        ["git", "show", f"{HELPER_COMMIT}:{path.relative_to(REPO).as_posix()}"],
        cwd=REPO,
        capture_output=True,
        check=False,
    )

    def normalize(data):
        return data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")

    if result.returncode or normalize(result.stdout) != normalize(path.read_bytes()):
        raise ValueError("closed-place helper differs from the frozen source")
    spec = importlib.util.spec_from_file_location("closure_frozen_helper", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


EULER = load_frozen_helper()
P = EULER.P


def validate_curve(field, A, B):
    P.require_int(A, "A", -48, 48)
    P.require_int(B, "B", -48, 48)
    if A % field.p == 0:
        raise ValueError("A=0 degenerates the S3 closure and genus-two source")
    if (-4 * A**3 - 27 * B**2) % field.p == 0:
        raise ValueError("singular discriminant source")


def square_roots(field):
    roots = [[] for _ in range(field.q)]
    for x in range(field.q):
        roots[field.mul(x, x)].append(x)
    return roots


def g_value(field, x, A):
    return field.add_constant(field.scale(field.mul(x, x), -3), -4 * A)


def discriminant_value(field, U, A, B):
    difference = field.add_constant(field.scale(U, -1), B)
    return field.add_constant(
        field.scale(field.mul(difference, difference), -27), -4 * A**3
    )


def r_action(field, x, v):
    half = pow(2, -1, field.p)
    return (
        field.scale(field.add(field.scale(x, -1), v), half),
        field.scale(field.add(field.scale(x, -3), field.scale(v, -1)), half),
    )


def s_action(field, x, v):
    return x, field.scale(v, -1)


def elliptic_map(field, x, w, A, B):
    gx = g_value(field, x, A)
    if gx == 0:
        if w != 0:
            raise ValueError("a point over g=0 must have w=0")
        return None
    inverse = field.power(gx, field.q - 2)
    x3 = field.mul(field.mul(x, x), x)
    numerator = field.add_constant(x3, 4 * B)
    correction = field.add_constant(field.add(x3, field.scale(x, 4 * A)), -8 * B)
    return field.mul(numerator, inverse), field.mul(
        field.mul(w, correction), field.mul(inverse, inverse)
    )


def second_elliptic_map(field, x, w, A, B):
    derivative = field.add_constant(field.scale(field.mul(x, x), 3), A)
    return field.cubic(x, A, B), field.mul(w, derivative)


def count_source(field, A, B, roots=None):
    validate_curve(field, A, B)
    roots = square_roots(field) if roots is None else roots
    if len(roots) != field.q or sum(map(len, roots)) != field.q:
        raise ValueError("incomplete primitive square-root table")
    squares = [field.mul(x, x) for x in range(field.q)]
    f_values = [field.cubic(x, A, B) for x in range(field.q)]
    g_values = [g_value(field, x, A) for x in range(field.q)]
    cubic_hist = [0] * field.q
    for value in f_values:
        cubic_hist[value] += 1
    chi_infinity = len(roots[(-3) % field.p]) - 1
    infinity = {
        "E": 1,
        "H": 1,
        "D": 1 + chi_infinity,
        "D2": 1,
        "Z": 1 + chi_infinity,
        "conic": 1 + chi_infinity,
    }
    counts = dict(infinity)
    z_by_u = [0] * field.q
    deck_points = 0
    deck_fixed_transposition = 0
    map_points = 0
    first_map_affine_to_infinity = 0
    second_map_affine_to_zero = 0
    for x in range(field.q):
        fx, gx = f_values[x], g_values[x]
        hx = field.mul(fx, gx)
        counts["E"] += len(roots[fx])
        counts["H"] += len(roots[hx])
        counts["conic"] += len(roots[gx])
        counts["Z"] += len(roots[fx]) * len(roots[gx])
        for y in roots[fx]:
            z_by_u[y] += len(roots[gx])
            for v in roots[gx]:
                rx, rv = r_action(field, x, v)
                if field.mul(y, y) != field.cubic(rx, A, B) or field.mul(
                    rv, rv
                ) != g_value(field, rx, A):
                    raise ArithmeticError(
                        "S3 deck generator does not preserve the original equations"
                    )
                r2 = r_action(field, rx, rv)
                if r_action(field, *r2) != (x, v) or s_action(
                    field, *s_action(field, x, v)
                ) != (x, v):
                    raise ArithmeticError("deck generator order is false")
                srs = s_action(field, *r_action(field, *s_action(field, x, v)))
                if srs != r2:
                    raise ArithmeticError("S3 conjugation relation is false")
                sign_coordinate = field.mul(
                    v, field.add_constant(field.scale(squares[x], 3), A)
                )
                if field.mul(sign_coordinate, sign_coordinate) != discriminant_value(
                    field, squares[y], A, B
                ):
                    raise ArithmeticError(
                        "explicit discriminant quotient has wrong sign or normalization"
                    )
                deck_points += 1
                deck_fixed_transposition += int(v == 0)
        for w in roots[hx]:
            first = elliptic_map(field, x, w, A, B)
            if first is None:
                first_map_affine_to_infinity += 1
            elif field.mul(first[1], first[1]) != field.cubic(first[0], A, B):
                raise ArithmeticError("first explicit elliptic map misses its target")
            U, S = second_elliptic_map(field, x, w, A, B)
            if field.mul(S, S) != field.mul(U, discriminant_value(field, U, A, B)):
                raise ArithmeticError("second explicit elliptic map misses its target")
            second_map_affine_to_zero += int(U == 0 and S == 0)
            map_points += 1
    quadratic_gauss_sum = 0
    local_hist = Counter()
    sign_sum = chi_infinity
    standard_sum = 0
    for u in range(field.q):
        d_square = discriminant_value(field, squares[u], A, B)
        d_linear = discriminant_value(field, u, A, B)
        counts["D"] += len(roots[d_square])
        counts["D2"] += len(roots[field.mul(u, d_linear)])
        quadratic_gauss_sum += len(roots[d_linear]) - 1
        N, sign = cubic_hist[squares[u]], len(roots[d_square]) - 1
        if (N, sign) not in ((3, 1), (0, 1), (1, -1), (2, 0)):
            raise ArithmeticError("invalid smooth S3 fibre class")
        if z_by_u[u] != 2 * N - 1 + sign:
            raise ArithmeticError(
                "normalized ramified regular-character formula failed"
            )
        local_hist[(N, sign, z_by_u[u])] += 1
        sign_sum += sign
        standard_sum += N - 1
        # Every rational affine D point maps to the displayed D2 equation.
        for s in roots[d_square]:
            S = field.mul(u, s)
            if field.mul(S, S) != field.mul(squares[u], d_square):
                raise ArithmeticError("discriminant degree-two quotient failed")
    if quadratic_gauss_sum != -chi_infinity or counts["D"] != counts["D2"]:
        raise ArithmeticError("independent quadratic-sum isogeny count failed")
    if counts["conic"] != field.q + 1:
        raise ArithmeticError("smooth conic count failed")
    if counts["Z"] != counts["E"] + counts["H"] - (field.q + 1):
        raise ArithmeticError("biquadratic source identity failed")
    if counts["Z"] != counts["D"] + 2 * counts["E"] - 2 * (field.q + 1):
        raise ArithmeticError("complete S3 source identity failed")
    if (
        sign_sum != counts["D"] - field.q - 1
        or standard_sum != counts["E"] - field.q - 1
    ):
        raise ArithmeticError("stalk traces fail complete curve counts")
    if deck_points != counts["Z"] - infinity["Z"] or map_points != counts["H"] - 1:
        raise ArithmeticError("incomplete affine deck or map coverage")
    return {
        "degree": field.n,
        "field_order": field.q,
        "modulus": field.modulus,
        "counts": counts,
        "infinity": infinity,
        "finite_fibre_histogram": [
            {
                "distinct_roots": k[0],
                "sign_trace": k[1],
                "closure_points": k[2],
                "number": value,
            }
            for k, value in sorted(local_hist.items())
        ],
        "complete_finite_fibre_count": sum(local_hist.values()),
        "quadratic_gauss_sum": quadratic_gauss_sum,
        "sign_stalk_sum": sign_sum,
        "standard_stalk_sum": standard_sum,
        "affine_deck_points_checked": deck_points,
        "affine_transposition_fixed_points": deck_fixed_transposition,
        "affine_H_map_points_checked": map_points,
        "first_map_affine_points_to_infinity": first_map_affine_to_infinity,
        "second_map_affine_points_to_zero": second_map_affine_to_zero,
    }


def integer_product(left, right):
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def build(source):
    if P.digest(source) != EXPECTED_SOURCE_HASH:
        raise ValueError("closure source differs from its frozen canonical identity")
    fields = {(p, n): P.Field(p, n) for p in (5, 7) for n in (1, 2, 3, 4)}
    roots = {key: square_roots(field) for key, field in fields.items()}
    panels = []
    for curve in source["curves"]:
        p, A, B = curve["p"], curve["A"], curve["B"]
        rows = [
            count_source(fields[p, n], A, B, roots[p, n]) for n in source["extensions"]
        ]
        sums = {
            name: [row["counts"][name] - row["field_order"] - 1 for row in rows]
            for name in ("E", "D", "D2", "H", "Z")
        }
        polynomials = {
            name: P.newton_from_local_sums(sums[name][:2]) for name in ("E", "D", "D2")
        }
        polynomials["H"] = P.newton_from_local_sums(sums["H"])
        if polynomials["D"] != polynomials["D2"] or polynomials["H"] != integer_product(
            polynomials["E"], polynomials["D"]
        ):
            raise ArithmeticError(
                "independently reconstructed elliptic/genus-two polynomials disagree"
            )
        for name in ("E", "D", "D2"):
            if (
                len(polynomials[name]) != 3
                or polynomials[name][2] != p
                or polynomials[name][1] ** 2 > 4 * p
            ):
                raise ArithmeticError(
                    "elliptic degree, determinant or weight bound failed"
                )
            if P.local_sums_from_polynomial(polynomials[name], 4) != sums[name]:
                raise ArithmeticError("held-out elliptic extension prediction failed")
        if not P.quartic_weil(polynomials["H"], p):
            raise ArithmeticError("exact genus-two reciprocal weight criterion failed")
        polynomials["Z"] = integer_product(polynomials["E"], polynomials["H"])
        if P.local_sums_from_polynomial(polynomials["Z"], 4) != sums["Z"]:
            raise ArithmeticError(
                "closure factorization misses complete primitive traces"
            )
        panels.append(
            {
                "source": curve,
                "extensions": rows,
                "polynomials": polynomials,
                "elliptic_held_out_degrees": [3, 4],
                "scope": "Genus-two polynomial uses four independent complete counts; closure degree-six factorization uses the proved source decomposition and predicts four counted traces, not six independent reconstruction counts.",
            }
        )
    return {
        "schema": "s3-genus-two-closure-replay-v1",
        "source_hash": P.digest(source),
        "panels": panels,
    }


def bindings():
    names = (
        "closure_source.json",
        "closure_replay.py",
        "test_closure_replay.py",
        "GALOIS_CLOSURE_AND_TWO_ELLIPTIC_MAPS.md",
        "closure_artifact.json",
    )
    return {
        "schema": "s3-genus-two-closure-binding-v1",
        "helper_commit": HELPER_COMMIT,
        "files": {name: P.lf_hash(ROOT / name) for name in names},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--write", action="store_true")
    modes.add_argument("--check", action="store_true")
    args = parser.parse_args()
    source = json.loads((ROOT / "closure_source.json").read_text(encoding="utf-8"))
    artifact = build(source)
    artifact_path, binding_path = (
        ROOT / "closure_artifact.json",
        ROOT / "closure_provenance.json",
    )
    if args.write:
        artifact_path.write_text(
            json.dumps(artifact, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        binding_path.write_text(
            json.dumps(bindings(), indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    else:
        P.require_same_json(
            json.loads(artifact_path.read_text(encoding="utf-8")),
            artifact,
            "closure artifact",
        )
        P.require_same_json(
            json.loads(binding_path.read_text(encoding="utf-8")),
            bindings(),
            "closure binding",
        )
    print(
        "PASS: five complete S3 closures, discriminant sectors and two explicit elliptic maps"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
