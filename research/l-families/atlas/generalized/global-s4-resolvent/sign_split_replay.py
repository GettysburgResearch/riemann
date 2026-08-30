"""Source elliptic quotient maps and polarized two-torsion graph replay."""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[4]
HELPER = "3d3b52541ed33b516c25ec0a27ba3eb568ec513b"
SOURCE_HASH = "ecebf695ad5df78af16d943e245681f60c65ee2359e6398e3a190ee76f1657a4"


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
        raise ValueError("sign split helper differs from frozen source")
    spec = importlib.util.spec_from_file_location("s4_sign_frozen_helper", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


C = load_helper()
S, P = C.S, C.P


class Elliptic:
    """Exact Y^2=X^3+a2 X^2+a4 X+a6 law in the bounded field model."""

    def __init__(self, field, a2, a4, a6):
        if any(type(v) is not int for v in (a2, a4, a6)):
            raise TypeError("elliptic coefficients must be exact integers")
        self.field = field
        self.a2, self.a4, self.a6 = a2 % field.p, a4 % field.p, a6 % field.p
        # Discriminant of the monic cubic; nonzero is sufficient for smoothness.
        delta = (
            a2 * a2 * a4 * a4
            - 4 * a4**3
            - 4 * a2**3 * a6
            - 27 * a6 * a6
            + 18 * a2 * a4 * a6
        )
        if delta % field.p == 0:
            raise ValueError("singular elliptic source")

    def rhs(self, x):
        f = self.field
        return f.add_constant(
            f.add(f.mul(f.add_constant(x, self.a2), f.mul(x, x)), f.scale(x, self.a4)),
            self.a6,
        )

    def valid(self, point):
        if point is None:
            return None
        if type(point) is not tuple or len(point) != 2:
            raise TypeError("point must be a coordinate tuple or infinity")
        x, y = point
        P.require_int(x, "elliptic x", 0, self.field.q - 1)
        P.require_int(y, "elliptic y", 0, self.field.q - 1)
        if self.field.mul(y, y) != self.rhs(x):
            raise ValueError("point is not on its source elliptic curve")
        return point

    def add(self, left, right):
        self.valid(left)
        self.valid(right)
        if left is None:
            return right
        if right is None:
            return left
        f = self.field
        x1, y1 = left
        x2, y2 = right
        if x1 == x2 and f.add(y1, y2) == 0:
            return None
        if left == right:
            numerator = f.add_constant(
                f.add(f.scale(f.mul(x1, x1), 3), f.scale(x1, 2 * self.a2)), self.a4
            )
            denominator = f.scale(y1, 2)
        else:
            numerator = f.add(y2, f.scale(y1, -1))
            denominator = f.add(x2, f.scale(x1, -1))
        slope = f.mul(numerator, f.power(denominator, f.q - 2))
        x3 = f.add_constant(
            f.add(f.mul(slope, slope), f.scale(f.add(x1, x2), -1)), -self.a2
        )
        y3 = f.add(f.mul(slope, f.add(x1, f.scale(x3, -1))), f.scale(y1, -1))
        return self.valid((x3, y3))


def elliptic_sources(field, b, c):
    S.validate_curve(field, b, c)
    delta = 256 * c**3 - 27 * b**4
    return (
        Elliptic(field, 0, 0, -432 * b**4),
        Elliptic(field, -768 * c * c, 768 * c * delta, -256 * delta * delta),
        delta,
    )


def source_h(field, r, b, c):
    value = field.add_constant(field.scale(r, -1), c)
    return field.add_constant(
        field.scale(field.mul(field.mul(value, value), value), 256), -27 * b**4
    )


def quotient_maps(field, b, c, point):
    plus, minus, delta = elliptic_sources(field, b, c)
    if type(point) is not tuple or len(point) != 2:
        raise TypeError("source affine point must be an exact pair")
    u, s = point
    P.require_int(u, "source u", 0, field.q - 1)
    P.require_int(s, "source s", 0, field.q - 1)
    r = field.mul(u, u)
    if field.mul(s, s) != source_h(field, r, b, c):
        raise ValueError("point is not on the source sign curve")
    plus_point = (
        field.scale(field.add_constant(field.scale(r, -1), c), 16),
        field.scale(s, 4),
    )
    if u == 0:
        minus_point = None
    else:
        inverse = field.power(u, field.q - 2)
        minus_point = (
            field.scale(field.mul(inverse, inverse), delta),
            field.scale(
                field.mul(s, field.mul(field.mul(inverse, inverse), inverse)), delta
            ),
        )
    plus.valid(plus_point)
    minus.valid(minus_point)
    return plus_point, minus_point


def count_maps(field, b, c):
    plus, minus, delta = elliptic_sources(field, b, c)
    roots = [[] for _ in range(field.q)]
    for y in range(field.q):
        roots[field.mul(y, y)].append(y)
    counts = {"plus": 1, "minus": 1, "D": len(roots[(-256) % field.p])}
    map_checks, minus_origin_hits = 0, 0
    for x in range(field.q):
        counts["plus"] += len(roots[plus.rhs(x)])
        counts["minus"] += len(roots[minus.rhs(x)])
        source_roots = roots[source_h(field, field.mul(x, x), b, c)]
        counts["D"] += len(source_roots)
        for y in source_roots:
            _, image = quotient_maps(field, b, c, (x, y))
            minus_origin_hits += int(image is None)
            map_checks += 1
    if minus_origin_hits != len(roots[delta % field.p]):
        raise ArithmeticError("minus origin divisor has wrong rational fibre")
    infinity_images = []
    for leading in roots[(-256) % field.p]:
        image = (0, field.scale(leading, delta))
        minus.valid(image)
        infinity_images.append(
            {"source_s_over_u3": leading, "plus": None, "minus": list(image)}
        )
    if counts["D"] != counts["plus"] + counts["minus"] - field.q - 1:
        raise ArithmeticError("primitive elliptic quotient point identity failed")
    if field.q % 3 == 2 and counts["plus"] != field.q + 1:
        raise ArithmeticError("cube-bijection forced elliptic trace failed")
    return {
        "degree": field.n,
        "q": field.q,
        "modulus": field.modulus,
        "counts": counts,
        "affine_map_checks": map_checks,
        "minus_origin_hits": minus_origin_hits,
        "infinity_images": infinity_images,
    }


def two_pairing(left, right, p):
    # On a full elliptic 2-torsion group the alternating nondegenerate Weil
    # pairing is 1 on dependent pairs and -1 on independent pairs.
    return 1 if left is None or right is None or left == right else p - 1


def torsion_graph(field, b, c):
    plus, minus, delta = elliptic_sources(field, b, c)
    common_roots = [r for r in range(field.q) if source_h(field, r, b, c) == 0]
    if len(common_roots) != 3 or 0 in common_roots:
        raise ValueError("declared torsion field must split the nonzero cubic roots")
    positive, negative = [None], [None]
    for r in common_roots:
        positive.append(
            plus.valid((field.scale(field.add_constant(field.scale(r, -1), c), 16), 0))
        )
        negative.append(
            minus.valid((field.scale(field.power(r, field.q - 2), delta), 0))
        )
    if len(set(positive)) != 4 or len(set(negative)) != 4:
        raise ArithmeticError("source two-torsion points collide")
    frobenius = []
    addition_table = []
    for i in range(4):
        row = []
        if (
            plus.add(positive[i], positive[i]) is not None
            or minus.add(negative[i], negative[i]) is not None
        ):
            raise ArithmeticError("displayed point is not two-torsion")
        for j in range(4):
            left = positive.index(plus.add(positive[i], positive[j]))
            right = negative.index(minus.add(negative[i], negative[j]))
            if left != right:
                raise ArithmeticError("common-root graph is not a group map")
            if (
                field.mul(
                    two_pairing(positive[i], positive[j], field.p),
                    two_pairing(negative[i], negative[j], field.p),
                )
                != 1
            ):
                raise ArithmeticError("graph is not a two-torsion anti-isometry")
            row.append(left)
        addition_table.append(row)
        fp = None if i == 0 else tuple(field.power(x, field.p) for x in positive[i])
        fm = None if i == 0 else tuple(field.power(x, field.p) for x in negative[i])
        index = positive.index(fp)
        if negative.index(fm) != index:
            raise ArithmeticError("source torsion graph fails Frobenius equivariance")
        frobenius.append(index)
    return {
        "p": field.p,
        "degree": field.n,
        "q": field.q,
        "b": b,
        "c": c,
        "modulus": field.modulus,
        "common_roots_r": common_roots,
        "plus_points": positive,
        "minus_points": negative,
        "addition_table": addition_table,
        "frobenius_indices": frobenius,
        "kernel_pairs": [[i, i] for i in range(4)],
        "common_source_divisor_polynomials_u": [
            [field.scale(r, -1), 0, 1] for r in common_roots
        ],
        "origin_difference_principal_function": "u",
    }


def build(source):
    if P.digest(source) != SOURCE_HASH:
        raise ValueError("sign splitting primitive source differs from frozen identity")
    precursor = json.loads((ROOT / "artifact.json").read_text(encoding="utf-8"))
    if [r["id"] for r in precursor["panels"]] != source["source_panels"]:
        raise ValueError("source panel roster differs")
    panels = []
    for panel in precursor["panels"]:
        p, b, c = panel["p"], panel["b"], panel["c"]
        rows = [count_maps(P.Field(p, n), b, c) for n in source["count_extensions"]]
        factors = {}
        for name in ("plus", "minus"):
            sums = [r["counts"][name] - r["q"] - 1 for r in rows]
            factors[name] = P.newton_from_local_sums(sums[:2])
            if (
                factors[name][2] != p
                or P.local_sums_from_polynomial(factors[name], len(rows)) != sums
            ):
                raise ArithmeticError(
                    "elliptic determinant fails independent extension counts"
                )
        if C.product(factors["plus"], factors["minus"]) != panel["polynomials"]["D"]:
            raise ArithmeticError(
                "elliptic product differs from frozen sign determinant"
            )
        if any((a - b) % 2 for a, b in zip(factors["plus"], factors["minus"])):
            raise ArithmeticError("source torsion graph Frobenius congruence failed")
        for row, old in zip(rows, panel["rows"]):
            if row["counts"]["D"] != old["curve_points"]["D"]:
                raise ArithmeticError(
                    "source sign curve count differs from predecessor"
                )
        panels.append(
            {
                "id": panel["id"],
                "p": p,
                "b": b,
                "c": c,
                "rows": rows,
                "polynomials": factors,
            }
        )
    graphs = [
        torsion_graph(P.Field(r["p"], r["degree"]), r["b"], r["c"])
        for r in source["torsion_fields"]
    ]
    return {
        "schema": "bring-s4-sign-split-artifact-v1",
        "source_hash": P.digest(source),
        "panels": panels,
        "torsion_graphs": graphs,
    }


def bindings():
    return {
        "schema": "bring-s4-sign-split-binding-v1",
        "helper_commit": HELPER,
        "files": {
            name: P.lf_hash(ROOT / name)
            for name in (
                "sign_split_source.json",
                "sign_split_replay.py",
                "test_sign_split_replay.py",
                "SIGN_SECTOR_POLARIZATION_AND_TWO_TORSION.md",
                "sign_split_artifact.json",
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
        json.loads((ROOT / "sign_split_source.json").read_text(encoding="utf-8"))
    )
    if args.write:
        (ROOT / "sign_split_artifact.json").write_text(
            json.dumps(artifact, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        (ROOT / "sign_split_provenance.json").write_text(
            json.dumps(bindings(), indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    else:
        for name, expected in (
            ("sign_split_artifact.json", artifact),
            ("sign_split_provenance.json", bindings()),
        ):
            P.require_same_json(
                json.loads((ROOT / name).read_text(encoding="utf-8")), expected, name
            )
    print(
        "PASS: explicit S4 sign elliptic maps, polarized two-torsion graph and forced factor"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
