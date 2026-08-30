"""Bounded exact replay of the global S3 / ramified Prym source.

No third-party packages, eigenvalue fitting, floating arithmetic, or field tables.
The deterministic polynomial model is reconstructed from the primitive source.
The mathematical all-field assertions are in GLOBAL_S3_PRYM_SOURCE.md.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MAX_FIELD = 2401
EXPECTED_SOURCE_HASH = (
    "51afca1ce7be4cc60bb82a382485a752c3859e5f7ad672abdd09f2a67654ed69"
)


def require_int(value: object, name: str, low: int, high: int) -> int:
    if type(value) is not int:
        raise TypeError(f"{name} must be an integer, not a coercible value")
    if not low <= value <= high:
        raise ValueError(f"{name} must lie in [{low},{high}]")
    return value


def canonical(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def digest(value: object) -> str:
    return hashlib.sha256(canonical(value).encode("ascii")).hexdigest()


def require_same_json(actual: object, expected: object, label: str) -> None:
    # Python equality identifies 1, True and 1.0; the exact source contract does not.
    if canonical(actual) != canonical(expected):
        raise ValueError(f"{label} differs from exact primitive replay")


def lf_hash(path: Path) -> str:
    return hashlib.sha256(
        path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    ).hexdigest()


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def remainder(poly: list[int], divisor: list[int], p: int) -> list[int]:
    value = trim([x % p for x in poly])
    divisor = trim([x % p for x in divisor])
    if divisor == [0]:
        raise ZeroDivisionError("zero polynomial divisor")
    lead_inverse = pow(divisor[-1], -1, p)
    while len(value) >= len(divisor) and value != [0]:
        shift = len(value) - len(divisor)
        factor = value[-1] * lead_inverse % p
        for i, c in enumerate(divisor):
            value[shift + i] = (value[shift + i] - factor * c) % p
        trim(value)
    return value


def polynomial_gcd(left: list[int], right: list[int], p: int) -> list[int]:
    while right != [0]:
        left, right = right, remainder(left, right, p)
    scale = pow(left[-1], -1, p)
    return [(v * scale) % p for v in left]


def polynomial_product(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] = (out[i + j] + x * y) % p
    return trim(out)


def polynomial_power(
    base: list[int], exponent: int, modulus: list[int], p: int
) -> list[int]:
    require_int(exponent, "polynomial exponent", 0, MAX_FIELD)
    result = [1]
    while exponent:
        if exponent & 1:
            result = remainder(polynomial_product(result, base, p), modulus, p)
        base = remainder(polynomial_product(base, base, p), modulus, p)
        exponent >>= 1
    return result


def irreducible(modulus: list[int], p: int) -> bool:
    """Rabin criterion, checked for every proper degree through n/2.

    A reducible degree-n polynomial has an irreducible factor of degree <=n/2.
    Such a factor divides X^(p^j)-X for j equal to its degree.
    """
    n = len(modulus) - 1
    if n < 1 or modulus[-1] != 1:
        return False
    current = remainder([0, 1], modulus, p)
    original = current[:]
    for j in range(1, n + 1):
        current = polynomial_power(current, p, modulus, p)
        difference = current[:] + [0] * max(0, len(original) - len(current))
        for i, c in enumerate(original):
            difference[i] = (difference[i] - c) % p
        difference = trim(difference)
        if j <= n // 2 and len(polynomial_gcd(modulus, difference, p)) > 1:
            return False
    return difference == [0]


def digits(value: int, p: int, n: int) -> tuple[int, ...]:
    out = []
    for _ in range(n):
        out.append(value % p)
        value //= p
    return tuple(out)


def first_modulus(p: int, n: int) -> list[int]:
    if n == 1:
        return [0, 1]
    for code in range(1, p**n):
        candidate = list(digits(code, p, n)) + [1]
        if candidate[0] and irreducible(candidate, p):
            return candidate
    raise ArithmeticError("no monic irreducible polynomial found")


class Field:
    """The model F_p[X]/m with integer base-p encoding, bounded before allocation."""

    def __init__(self, p: int, n: int, modulus: list[int] | None = None):
        self.p = require_int(p, "p", 5, 47)
        self.n = require_int(n, "n", 1, 4)
        if any(p % d == 0 for d in range(2, isqrt(p) + 1)):
            raise ValueError("p must be prime")
        self.q = p**n
        if self.q > MAX_FIELD:
            raise ValueError("field exceeds exact replay resource cap")
        if modulus is not None and type(modulus) is not list:
            raise TypeError("modulus must be a coefficient list")
        self.modulus = first_modulus(p, n) if modulus is None else modulus[:]
        if (
            len(self.modulus) != n + 1
            or any(type(c) is not int or not 0 <= c < p for c in self.modulus)
            or not irreducible(self.modulus, p)
        ):
            raise ValueError("invalid irreducible field modulus")
        self.table = [digits(x, p, n) for x in range(self.q)]

    def add(self, a: int, b: int) -> int:
        p = self.p
        return sum(
            ((x + y) % p) * p**i
            for i, (x, y) in enumerate(zip(self.table[a], self.table[b]))
        )

    def scale(self, a: int, c: int) -> int:
        p = self.p
        return sum((x * c % p) * p**i for i, x in enumerate(self.table[a]))

    def add_constant(self, a: int, c: int) -> int:
        return a - a % self.p + (a + c) % self.p

    def mul(self, a: int, b: int) -> int:
        if self.n == 1:
            return a * b % self.p
        p, n = self.p, self.n
        product = [0] * (2 * n - 1)
        for i, x in enumerate(self.table[a]):
            for j, y in enumerate(self.table[b]):
                product[i + j] += x * y
        for d in range(2 * n - 2, n - 1, -1):
            factor = product[d] % p
            for i in range(n):
                product[d - n + i] -= factor * self.modulus[i]
        return sum((product[i] % p) * p**i for i in range(n))

    def power(self, a: int, exponent: int) -> int:
        require_int(a, "field element", 0, self.q - 1)
        require_int(exponent, "field exponent", 0, MAX_FIELD)
        value = 1
        while exponent:
            if exponent & 1:
                value = self.mul(value, a)
            a = self.mul(a, a)
            exponent >>= 1
        return value

    def cubic(self, x: int, A: int, B: int) -> int:
        return self.add_constant(
            self.add(self.mul(self.mul(x, x), x), self.scale(x, A)), B
        )


def newton_from_local_sums(sums: list[int]) -> list[int]:
    """exp(sum S_n*T^n/n), where S_n is minus the cohomological power trace."""
    coefficients = [1]
    for n in range(1, len(sums) + 1):
        numerator = sum(sums[i - 1] * coefficients[n - i] for i in range(1, n + 1))
        if numerator % n:
            raise ArithmeticError("Newton coefficient is not integral")
        coefficients.append(numerator // n)
    return coefficients


def local_sums_from_polynomial(coefficients: list[int], count: int) -> list[int]:
    """Formal logarithmic derivative, independent of field counting."""
    sums = []
    for n in range(1, count + 1):
        c_n = coefficients[n] if n < len(coefficients) else 0
        value = n * c_n
        for i in range(1, n):
            c = coefficients[n - i] if n - i < len(coefficients) else 0
            value -= sums[i - 1] * c
        sums.append(value)
    return sums


def quartic_weil(coefficients: list[int], q: int) -> bool:
    """Exact root-location criterion after X=alpha+q/alpha, no floating roots."""
    if len(coefficients) != 5 or coefficients[0] != 1:
        return False
    _, c1, c2, c3, c4 = coefficients
    if c3 != q * c1 or c4 != q * q:
        return False
    discriminant = c1 * c1 - 4 * (c2 - 2 * q)
    slack = 16 * q - c1 * c1 - discriminant
    return (
        discriminant >= 0 and slack >= 0 and slack * slack >= 4 * c1 * c1 * discriminant
    )


def count_source(field: Field, A: int, B: int) -> dict:
    p, q = field.p, field.q
    require_int(A, "A", -(10**6), 10**6)
    require_int(B, "B", -(10**6), 10**6)
    delta = (-4 * A**3 - 27 * B**2) % p
    if delta == 0:
        raise ValueError("singular source curve")
    squares, fourths, cubics = [0] * q, [0] * q, [0] * q
    for z in range(q):
        z2 = field.mul(z, z)
        squares[z2] += 1
        fourths[field.mul(z2, z2)] += 1
        cubics[field.cubic(z, A, B)] += 1
    elliptic, cover = 1, 1
    for x in range(q):
        fx = field.cubic(x, A, B)
        elliptic += squares[fx]
        cover += fourths[fx]
    local_sum, twist_sum = 0, 0
    old_branches = []
    types = {
        "identity": 0,
        "transposition": 0,
        "three_cycle": 0,
        "ramified_transposition": 0,
        "ramified_three_cycle": 0,
    }
    for t in range(q):
        t2 = field.mul(t, t)
        roots = cubics[t2]
        character = squares[t] - 1
        coefficient = field.add_constant(field.scale(t2, -1), B)
        d_t = field.add_constant(
            field.scale(field.mul(coefficient, coefficient), -27), -4 * A**3
        )
        if d_t == 0:
            if A % p:
                if roots != 2:
                    raise ArithmeticError(
                        "ramified transposition fibre must have two rational points"
                    )
                r = field.scale(field.add_constant(t2, -B), 3 * pow(2 * A % p, -1, p))
                if (
                    field.cubic(r, A, B) != t2
                    or field.cubic(field.scale(r, -2), A, B) != t2
                ):
                    raise ArithmeticError("source double/simple root formula failed")
                types["ramified_transposition"] += 1
                old_branches.append(
                    {
                        "t": t,
                        "invariant_dimension": 1,
                        "W_frobenius": 1,
                        "twist_frobenius": character,
                    }
                )
            else:
                if roots != 1:
                    raise ArithmeticError(
                        "cyclic ramified fibre must have one rational point"
                    )
                types["ramified_three_cycle"] += 1
                old_branches.append(
                    {
                        "t": t,
                        "invariant_dimension": 0,
                        "W_frobenius": 0,
                        "twist_frobenius": 0,
                    }
                )
        else:
            if roots not in (0, 1, 3):
                raise ArithmeticError(
                    "unramified cubic root count outside Frobenius cycle types"
                )
            types[{0: "three_cycle", 1: "transposition", 3: "identity"}[roots]] += 1
        local_sum += roots - 1
        twist_sum += character * (roots - 1)
    if local_sum != elliptic - q - 1 or twist_sum != cover - elliptic:
        raise ArithmeticError(
            "primitive point counts disagree with middle-extension local traces"
        )
    return {
        "p": p,
        "n": field.n,
        "q": q,
        "modulus_low_to_high": field.modulus,
        "elliptic_points": elliptic,
        "quartic_cover_points": cover,
        "W_local_sum": local_sum,
        "W_twist_local_sum": twist_sum,
        "affine_fibre_types": types,
        "old_branch_factors": old_branches,
        "infinity": {
            "W_invariants": 0,
            "W_twist_invariants": 0,
            "E_points": 1,
            "C_points": 1,
        },
        "twist_zero_invariants": 0,
    }


def permutation_matrix(permutation: tuple[int, ...]) -> list[list[Fraction]]:
    return [
        [Fraction(permutation[j] == i) for j in range(len(permutation))]
        for i in range(len(permutation))
    ]


def matrix_multiply(
    left: list[list[Fraction]], right: list[list[Fraction]]
) -> list[list[Fraction]]:
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(len(right)))
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def transpose(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*matrix)]


def projector_control() -> dict:
    identity = permutation_matrix((0, 1, 2))
    u, v = permutation_matrix((1, 0, 2)), permutation_matrix((0, 2, 1))
    k = matrix_multiply(transpose(matrix_multiply(u, v)), matrix_multiply(v, u))
    h = [[identity[i][j] - (k[i][j] + k[j][i]) / 2 for j in range(3)] for i in range(3)]
    p = [[identity[i][j] - Fraction(1, 3) for j in range(3)] for i in range(3)]
    if matrix_multiply(p, p) != p or h != [
        [Fraction(3, 2) * c for c in row] for row in p
    ]:
        raise ArithmeticError("S3 positive defect/projector identity failed")
    cycle = permutation_matrix((1, 2, 0))
    cyclic_k = matrix_multiply(
        transpose(matrix_multiply(cycle, cycle)), matrix_multiply(cycle, cycle)
    )
    if cyclic_k != identity:
        raise ArithmeticError("cyclic commutator must vanish")
    return {
        "S3_H_equals_three_halves_P": True,
        "augmentation_rank": 2,
        "C3_commutator_H_zero": True,
        "C3_augmentation_P_nonzero": True,
        "P": [[str(c) for c in row] for row in p],
    }


def validate_source(source: dict) -> None:
    if type(source) is not dict or source.get("schema") != "global-s3-prym-source-v1":
        raise ValueError("unknown source schema")
    if (
        source.get("field_limit") != MAX_FIELD
        or type(source.get("field_limit")) is not int
    ):
        raise ValueError("resource cap must be exactly the audited cap")
    panels = source.get("panels")
    if type(panels) is not list or not 1 <= len(panels) <= 12:
        raise ValueError("invalid bounded panel coverage")
    ids = set()
    for panel in panels:
        if type(panel) is not dict or set(panel) != {"id", "p", "A", "B", "extensions"}:
            raise ValueError("unexpected panel shape")
        if type(panel["id"]) is not str or not panel["id"] or panel["id"] in ids:
            raise ValueError("panel IDs must be distinct nonempty strings")
        ids.add(panel["id"])
        require_int(panel["p"], "panel p", 5, 47)
        require_int(panel["A"], "panel A", -(10**6), 10**6)
        require_int(panel["B"], "panel B", -(10**6), 10**6)
        if panel["extensions"] != [1, 2, 3, 4] or any(
            type(n) is not int for n in panel["extensions"]
        ):
            raise ValueError(
                "complete degree-one through degree-four extension coverage required"
            )
        if panel["p"] ** 4 > MAX_FIELD:
            raise ValueError("panel exceeds bounded coverage")


def build(source: dict) -> dict:
    validate_source(source)
    fields = {}
    panels = []
    for panel in source["panels"]:
        p, A, B = panel["p"], panel["A"], panel["B"]
        counts = []
        for n in panel["extensions"]:
            if (p, n) not in fields:
                fields[p, n] = Field(p, n)
            counts.append(count_source(fields[p, n], A, B))
        e_sums = [c["W_local_sum"] for c in counts]
        twist_sums = [c["W_twist_local_sum"] for c in counts]
        e_poly = newton_from_local_sums(e_sums[:2])
        prym_poly = newton_from_local_sums(twist_sums)
        if e_poly[2] != p or e_poly[1] ** 2 > 4 * p:
            raise ArithmeticError(
                "elliptic polynomial normalization/weight control failed"
            )
        if local_sums_from_polynomial(e_poly, 4) != e_sums:
            raise ArithmeticError("held-out elliptic extension prediction failed")
        if not quartic_weil(prym_poly, p):
            raise ArithmeticError("Prym reciprocity/exact weight control failed")
        # An independent reconstruction using only degrees 1,2 plus the proved
        # reciprocity predicts degrees 3,4. It is labelled theorem-assisted.
        assisted = prym_poly[:3] + [p * prym_poly[1], p * p]
        if local_sums_from_polynomial(assisted, 4) != twist_sums:
            raise ArithmeticError("theorem-assisted held-out Prym prediction failed")
        panels.append(
            {
                "source": panel,
                "geometric_monodromy": "S3" if A % p else "C3",
                "arithmetic_monodromy": "S3" if A % p or p % 3 == 2 else "C3",
                "counts": counts,
                "P_E": e_poly,
                "P_prym": prym_poly,
                "elliptic_held_out_degrees": [3, 4],
                "prym_held_out_degrees_using_proved_reciprocity": [3, 4],
                "prym_independent_newton_degrees": [1, 2, 3, 4],
            }
        )
    return {
        "schema": "global-s3-prym-replay-v1",
        "source_hash": digest(source),
        "panels": panels,
        "projector": projector_control(),
        "scope": "Complete exact finite replay for listed panels, not a computational proof of the all-field theorems.",
    }


def binding() -> dict:
    names = [
        "source.json",
        "producer.py",
        "test_producer.py",
        "GLOBAL_S3_PRYM_SOURCE.md",
        "README.md",
    ]
    return {
        "schema": "global-s3-prym-binding-v1",
        "hash_normalization": "UTF-8 bytes; CRLF and CR become LF",
        "files": {name: lf_hash(ROOT / name) for name in names},
        "artifact": {
            "path": "artifact.json",
            "sha256_lf": lf_hash(ROOT / "artifact.json"),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write", action="store_true", help="rebuild artifact and source bindings"
    )
    args = parser.parse_args()
    source = json.loads((ROOT / "source.json").read_text(encoding="utf-8"))
    if digest(source) != EXPECTED_SOURCE_HASH:
        raise ValueError("primitive source differs from the frozen source identity")
    artifact = build(source)
    artifact_path = ROOT / "artifact.json"
    binding_path = ROOT / "provenance.json"
    if args.write:
        artifact_path.write_text(
            json.dumps(artifact, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        binding_path.write_text(
            json.dumps(binding(), indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    else:
        require_same_json(
            json.loads(artifact_path.read_text(encoding="utf-8")), artifact, "artifact"
        )
        require_same_json(
            json.loads(binding_path.read_text(encoding="utf-8")),
            binding(),
            "source binding",
        )
    print(
        f"PASS: {len(artifact['panels'])} exact curve panels, 24 extension-field replays, ramified stalks and projector controls"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
