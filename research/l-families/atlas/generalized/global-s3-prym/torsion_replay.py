"""Exact source-defined three-torsion graph via Mumford divisor pullback."""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[4]
PRECURSOR = "567ae7aec00f6ee6d3e01bdde2004e76fec8ff6f"
EXPECTED_SOURCE_HASH = (
    "7cfcdb0003e124025210a2cefb8f3571da04fdc2f9c061593702bb5123a5045e"
)
MAX_POLY_DEGREE = 12


def load_source():
    for name in (
        "closure_replay.py",
        "closure_source.json",
        "closure_artifact.json",
        "closure_provenance.json",
        "test_closure_replay.py",
        "GALOIS_CLOSURE_AND_TWO_ELLIPTIC_MAPS.md",
    ):
        path = ROOT / name
        result = subprocess.run(
            ["git", "show", f"{PRECURSOR}:{path.relative_to(REPO).as_posix()}"],
            cwd=REPO,
            capture_output=True,
            check=False,
        )

        def normalize(data):
            return data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")

        if result.returncode or normalize(result.stdout) != normalize(
            path.read_bytes()
        ):
            raise ValueError(f"frozen geometric source changed: {name}")
    spec = importlib.util.spec_from_file_location(
        "torsion_frozen_closure", ROOT / "closure_replay.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


C = load_source()
P = C.P


class Polynomials:
    """Small exact polynomial arithmetic over the authenticated finite field."""

    def __init__(self, field):
        if field.q > 2401:
            raise ValueError("torsion field exceeds declared cap")
        self.f = field
        self.inverse_cache = {}

    def checked(self, a):
        if type(a) not in (tuple, list) or not 1 <= len(a) <= MAX_POLY_DEGREE + 1:
            raise ValueError("polynomial input outside bounded coefficient format")
        for x in a:
            P.require_int(x, "polynomial coefficient", 0, self.f.q - 1)
        return self.trim(a)

    @staticmethod
    def trim(a):
        result = list(a)
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        return tuple(result)

    def inv(self, a):
        P.require_int(a, "inverse argument", 1, self.f.q - 1)
        if a not in self.inverse_cache:
            self.inverse_cache[a] = self.f.power(a, self.f.q - 2)
        return self.inverse_cache[a]

    def add(self, a, b):
        a, b = self.checked(a), self.checked(b)
        return self.trim(
            [
                self.f.add(a[i] if i < len(a) else 0, b[i] if i < len(b) else 0)
                for i in range(max(len(a), len(b)))
            ]
        )

    def scale(self, a, scalar):
        a = self.checked(a)
        P.require_int(scalar, "polynomial field scalar", 0, self.f.q - 1)
        return self.trim([self.f.mul(x, scalar) for x in a])

    def neg(self, a):
        return self.scale(a, (-1) % self.f.p)

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        a, b = self.checked(a), self.checked(b)
        if len(a) + len(b) - 2 > MAX_POLY_DEGREE:
            raise ValueError("polynomial multiplication exceeds degree cap")
        out = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                out[i + j] = self.f.add(out[i + j], self.f.mul(x, y))
        return self.trim(out)

    def divmod(self, a, b):
        a, b = self.checked(a), self.checked(b)
        if b == (0,):
            raise ZeroDivisionError("zero polynomial divisor")
        out = [0] * max(1, len(a) - len(b) + 1)
        invlead = self.inv(b[-1])
        while a != (0,) and len(a) >= len(b):
            shift = len(a) - len(b)
            factor = self.f.mul(a[-1], invlead)
            out[shift] = self.f.add(out[shift], factor)
            a = self.sub(a, (0,) * shift + self.scale(b, factor))
        return self.trim(out), a

    def mod(self, a, b):
        return self.divmod(a, b)[1]

    def exact(self, a, b):
        quotient, remainder = self.divmod(a, b)
        if remainder != (0,):
            raise ArithmeticError("nonexact divisor arithmetic")
        return quotient

    def monic(self, a):
        a = self.checked(a)
        if a == (0,):
            raise ValueError("zero polynomial has no monic normalization")
        return self.scale(a, self.inv(a[-1]))

    def xgcd(self, a, b):
        a, b = self.checked(a), self.checked(b)
        s0, s1, t0, t1 = (1,), (0,), (0,), (1,)
        steps = 0
        while b != (0,):
            q, rem = self.divmod(a, b)
            a, b = b, rem
            s0, s1 = s1, self.sub(s0, self.mul(q, s1))
            t0, t1 = t1, self.sub(t0, self.mul(q, t1))
            steps += 1
            if steps > MAX_POLY_DEGREE + 2:
                raise ArithmeticError(
                    "Euclidean algorithm exceeded proved degree bound"
                )
        inverse = self.inv(a[-1])
        return self.scale(a, inverse), self.scale(s0, inverse), self.scale(t0, inverse)

    def inverse_mod(self, a, modulus):
        d, s, _ = self.xgcd(a, modulus)
        if d != (1,):
            raise ValueError("source map denominator not invertible in this fibre")
        return self.mod(s, modulus)

    def value(self, a, x):
        a = self.checked(a)
        P.require_int(x, "evaluation point", 0, self.f.q - 1)
        out = 0
        for coefficient in reversed(a):
            out = self.f.add(self.f.mul(out, x), coefficient)
        return out


class Jacobian:
    """Genus-two Mumford classes, with checked Cantor composition/reduction."""

    zero = ((1,), (0,))

    def __init__(self, field, A, B):
        C.validate_curve(field, A, B)
        self.field, self.A, self.B = field, A, B
        self.r = Polynomials(field)
        self.f = (B % field.p, A % field.p, 0, 1)
        self.g = ((-4 * A) % field.p, 0, (-3) % field.p)
        self.h = self.r.mul(self.f, self.g)

    def reduced(self, u, v):
        r = self.r
        u = r.monic(u)
        v = r.mod(v, u)
        if r.mod(r.sub(self.h, r.mul(v, v)), u) != (0,):
            raise ValueError("Mumford pair is not on the primitive genus-two curve")
        reductions = 0
        while len(u) > 3:
            u = r.monic(r.exact(r.sub(self.h, r.mul(v, v)), u))
            v = r.mod(r.neg(v), u)
            reductions += 1
            if reductions > MAX_POLY_DEGREE:
                raise ArithmeticError("Cantor reduction failed its degree bound")
        if r.mod(r.sub(self.h, r.mul(v, v)), u) != (0,):
            raise ArithmeticError("reduced divisor left the source curve")
        return u, v

    def validate(self, point):
        if type(point) not in (tuple, list) or len(point) != 2:
            raise TypeError("Jacobian point must be a Mumford pair")
        u, v = map(self.r.checked, point)
        if len(u) > 3 or u[-1] != 1 or (v != (0,) and len(v) >= len(u)):
            raise ValueError("noncanonical reduced divisor")
        if self.reduced(u, v) != (u, v):
            raise ValueError("invalid reduced divisor")
        return u, v

    def neg(self, point):
        u, v = self.validate(point)
        return u, self.r.mod(self.r.neg(v), u)

    def add(self, left, right):
        u1, v1 = self.validate(left)
        u2, v2 = self.validate(right)
        r = self.r
        d1, e1, e2 = r.xgcd(u1, u2)
        d, c1, c2 = r.xgcd(d1, r.add(v1, v2))
        s1, s2, s3 = r.mul(c1, e1), r.mul(c1, e2), c2
        u = r.exact(r.mul(u1, u2), r.mul(d, d))
        numerator = r.add(
            r.add(r.mul(r.mul(s1, u1), v2), r.mul(r.mul(s2, u2), v1)),
            r.mul(s3, r.add(r.mul(v1, v2), self.h)),
        )
        v = r.mod(r.exact(numerator, d), u)
        return self.reduced(u, v)

    def multiple(self, point, n):
        P.require_int(n, "small Jacobian multiplier", 0, 27)
        point = self.validate(point)
        out = self.zero
        for _ in range(n):
            out = self.add(out, point)
        return out

    def first_pullback(self, point):
        point = Elliptic(self.field, self.A, self.B).valid(point)
        if point is None:
            return self.zero
        X, Y = point
        r, field = self.r, self.field
        cubic = (
            field.add_constant(field.scale(X, 4 * self.A), 4 * self.B),
            0,
            field.scale(X, 3),
            1,
        )
        correction = ((-8 * self.B) % field.p, (4 * self.A) % field.p, 0, 1)
        v = r.mod(
            r.scale(r.mul(r.mul(self.g, self.g), r.inverse_mod(correction, cubic)), Y),
            cubic,
        )
        fibre_minus_three_infinity = self.reduced(cubic, v)
        origin_correction = self.reduced(self.g, (0,))
        return self.add(fibre_minus_three_infinity, self.neg(origin_correction))

    def second_pullback(self, point):
        if point is None:
            return self.zero
        if type(point) not in (tuple, list) or len(point) != 2:
            raise TypeError("second elliptic point must have two coordinates")
        U, S = point
        field, r = self.field, self.r
        P.require_int(U, "second elliptic U", 0, field.q - 1)
        P.require_int(S, "second elliptic S", 0, field.q - 1)
        if field.mul(S, S) != field.mul(
            U, C.discriminant_value(field, U, self.A, self.B)
        ):
            raise ValueError("point is not on the primitive second elliptic curve")
        cubic = (field.add_constant(field.scale(U, -1), self.B), self.A % field.p, 0, 1)
        derivative = (self.A % field.p, 0, 3 % field.p)
        v = r.mod(r.scale(r.inverse_mod(derivative, cubic), S), cubic)
        return self.reduced(cubic, v)

    def frobenius(self, point):
        u, v = self.validate(point)
        return tuple(self.field.power(x, self.field.p) for x in u), tuple(
            self.field.power(x, self.field.p) for x in v
        )


class Elliptic:
    """Short Weierstrass arithmetic; the identity is None."""

    def __init__(self, field, a, b):
        if type(a) is not int or type(b) is not int:
            raise TypeError("short elliptic coefficients must be exact integers")
        self.f = field
        self.a, self.b = a % field.p, b % field.p
        self.r = Polynomials(field)
        if (-4 * a**3 - 27 * b**2) % field.p == 0:
            raise ValueError("singular short elliptic model")

    def valid(self, point):
        if point is None:
            return None
        if type(point) not in (tuple, list) or len(point) != 2:
            raise TypeError("elliptic point format")
        x, y = point
        P.require_int(x, "elliptic x", 0, self.f.q - 1)
        P.require_int(y, "elliptic y", 0, self.f.q - 1)
        if self.f.mul(y, y) != self.f.cubic(x, self.a, self.b):
            raise ValueError("point is not on the named elliptic source")
        return x, y

    def neg(self, point):
        point = self.valid(point)
        return None if point is None else (point[0], self.f.scale(point[1], -1))

    def add(self, left, right):
        left, right = self.valid(left), self.valid(right)
        if left is None:
            return right
        if right is None:
            return left
        f = self.f
        x1, y1 = left
        x2, y2 = right
        if x1 == x2:
            if f.add(y1, y2) == 0:
                return None
            numerator = f.add_constant(f.scale(f.mul(x1, x1), 3), self.a)
            denominator = f.scale(y1, 2)
        else:
            numerator = f.add(y2, f.scale(y1, -1))
            denominator = f.add(x2, f.scale(x1, -1))
        slope = f.mul(numerator, self.r.inv(denominator))
        x3 = f.add(f.mul(slope, slope), f.scale(f.add(x1, x2), -1))
        y3 = f.add(f.mul(slope, f.add(x1, f.scale(x3, -1))), f.scale(y1, -1))
        return self.valid((x3, y3))

    def three_torsion(self):
        f = self.f
        roots = C.square_roots(f)
        psi = (
            (-self.a * self.a) % f.p,
            (12 * self.b) % f.p,
            (6 * self.a) % f.p,
            0,
            3 % f.p,
        )
        points = [None]
        for x in range(f.q):
            if self.r.value(psi, x) == 0:
                points.extend((x, y) for y in roots[f.cubic(x, self.a, self.b)])
        if len(points) != 9:
            raise ValueError("declared field does not split all elliptic three-torsion")
        for point in points:
            if self.add(self.add(point, point), point) is not None:
                raise ArithmeticError(
                    "division polynomial produced false three-torsion"
                )
        return points

    def weil3(self, left, right):
        left, right = self.valid(left), self.valid(right)
        for point in (left, right):
            if self.add(self.add(point, point), point) is not None:
                raise ValueError("Weil pairing requires three-torsion")
        if left is None or right is None or right in (left, self.neg(left)):
            return 1

        def tangent_at(point, target):
            x, y = point
            slope = self.f.mul(
                self.f.add_constant(self.f.scale(self.f.mul(x, x), 3), self.a),
                self.r.inv(self.f.scale(y, 2)),
            )
            return self.f.add(
                self.f.add(target[1], self.f.scale(y, -1)),
                self.f.scale(
                    self.f.mul(slope, self.f.add(target[0], self.f.scale(x, -1))), -1
                ),
            )

        value = self.f.scale(
            self.f.mul(tangent_at(left, right), self.r.inv(tangent_at(right, left))), -1
        )
        if self.f.power(value, 3) != 1 or value == 1:
            raise ArithmeticError(
                "normalized tangent-line Weil pairing is not primitive"
            )
        return value

    def frobenius(self, point):
        point = self.valid(point)
        return (
            None
            if point is None
            else (self.f.power(point[0], self.f.p), self.f.power(point[1], self.f.p))
        )


def second_short_model(field, A, B):
    return Elliptic(field, 27 * (4 * A**3 - 9 * B**2), -486 * B * (4 * A**3 + 3 * B**2))


def second_affine_coordinates(field, point, B):
    if point is None:
        return None
    inverse = field.power((-27) % field.p, field.q - 2)
    return field.mul(field.add_constant(point[0], -18 * B), inverse), field.mul(
        point[1], inverse
    )


def panel(source):
    field = P.Field(source["p"], source["degree"])
    A, B = source["A"], source["B"]
    J = Jacobian(field, A, B)
    left = Elliptic(field, A, B)
    right = second_short_model(field, A, B)
    lp, rp = left.three_torsion(), right.three_torsion()
    pull_left = [J.first_pullback(point) for point in lp]
    pull_right = [
        J.second_pullback(second_affine_coordinates(field, point, B)) for point in rp
    ]
    if len(set(pull_left)) != 9 or len(set(pull_right)) != 9:
        raise ArithmeticError("one source pullback loses three-torsion")
    for point in pull_left + pull_right:
        if J.multiple(point, 3) != J.zero:
            raise ArithmeticError("source divisor pullback is not three-torsion")
    kernel = [
        (i, j)
        for i in range(9)
        for j in range(9)
        if J.add(pull_left[i], pull_right[j]) == J.zero
    ]
    if (
        len(kernel) != 9
        or len({i for i, j in kernel}) != 9
        or len({j for i, j in kernel}) != 9
    ):
        raise ArithmeticError("actual divisor kernel is not a nine-point graph")
    graph = dict(kernel)
    for i in range(9):
        for j in range(9):
            li = lp.index(left.add(lp[i], lp[j]))
            rj = rp.index(right.add(rp[graph[i]], rp[graph[j]]))
            if graph[li] != rj:
                raise ArithmeticError("source kernel graph is not a homomorphism")
            if J.add(pull_left[i], pull_left[j]) != pull_left[li]:
                raise ArithmeticError("first divisor pullback is not additive")
            right_sum = rp.index(right.add(rp[i], rp[j]))
            if J.add(pull_right[i], pull_right[j]) != pull_right[right_sum]:
                raise ArithmeticError("second divisor pullback is not additive")
            if (
                field.mul(
                    left.weil3(lp[i], lp[j]), right.weil3(rp[graph[i]], rp[graph[j]])
                )
                != 1
            ):
                raise ArithmeticError("source graph fails Weil-pairing reversal")
        lf = lp.index(left.frobenius(lp[i]))
        rf = rp.index(right.frobenius(rp[graph[i]]))
        if graph[lf] != rf or J.frobenius(pull_left[i]) != pull_left[lf]:
            raise ArithmeticError("source kernel graph fails Frobenius equivariance")
    basis = next(
        (i, j)
        for i in range(1, 9)
        for j in range(1, 9)
        if left.weil3(lp[i], lp[j]) != 1
    )
    return {
        "source": source,
        "field_modulus": field.modulus,
        "E_three_torsion": lp,
        "D2_short_three_torsion": rp,
        "E_pullback_divisors": pull_left,
        "D2_pullback_divisors": pull_right,
        "kernel_index_pairs": kernel,
        "basis_indices": basis,
        "basis_Weil_pairing": left.weil3(lp[basis[0]], lp[basis[1]]),
        "image_basis_Weil_pairing": right.weil3(
            rp[graph[basis[0]]], rp[graph[basis[1]]]
        ),
        "E_Frobenius_indices": [lp.index(left.frobenius(point)) for point in lp],
        "D2_Frobenius_indices": [rp.index(right.frobenius(point)) for point in rp],
        "coverage": {
            "x_coordinates_per_elliptic_curve": field.q,
            "torsion_points_per_curve": 9,
            "kernel_pairs": 81,
            "pairing_pairs": 81,
        },
    }


def build(source):
    if P.digest(source) != EXPECTED_SOURCE_HASH:
        raise ValueError("torsion primitive source differs from frozen identity")
    return {
        "schema": "source-three-torsion-graph-replay-v1",
        "source_hash": P.digest(source),
        "panels": [panel(curve) for curve in source["curves"]],
    }


def bindings():
    names = (
        "torsion_source.json",
        "torsion_replay.py",
        "test_torsion_replay.py",
        "POLARIZED_JACOBIAN_AND_THREE_TORSION.md",
        "TORSION_DIVISOR_REPLAY.md",
        "torsion_artifact.json",
    )
    return {
        "schema": "source-three-torsion-graph-binding-v1",
        "precursor_commit": PRECURSOR,
        "files": {name: P.lf_hash(ROOT / name) for name in names},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--write", action="store_true")
    modes.add_argument("--check", action="store_true")
    args = parser.parse_args()
    source = json.loads((ROOT / "torsion_source.json").read_text(encoding="utf-8"))
    artifact = build(source)
    artifact_path, binding_path = (
        ROOT / "torsion_artifact.json",
        ROOT / "torsion_provenance.json",
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
            "torsion artifact",
        )
        P.require_same_json(
            json.loads(binding_path.read_text(encoding="utf-8")),
            bindings(),
            "torsion binding",
        )
    print(
        "PASS: two source divisor three-torsion graphs with Frobenius and Weil anti-isometry"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
