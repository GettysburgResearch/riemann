"""Primitive Kummer tower replay with exact quadratic cyclotomic arithmetic."""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[4]
HELPER_COMMIT = "4ba9cf883ecf49fe0034d6b05a878caf2768d263"
EXPECTED_SOURCE_HASH = (
    "3eaf292f276de319dfda022e827a9526f555f4944d8c66a7495db6bf1f7a10cb"
)
ZERO = (0, 0)
ONE = (1, 0)


def load_frozen_helper():
    path = ROOT / "closed_euler.py"
    relative = path.relative_to(REPO).as_posix()
    result = subprocess.run(
        ["git", "show", f"{HELPER_COMMIT}:{relative}"],
        cwd=REPO,
        capture_output=True,
        check=False,
    )

    def normalize(data):
        return data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")

    if result.returncode or normalize(result.stdout) != normalize(path.read_bytes()):
        raise ValueError("closed-point helper differs from its frozen source")
    spec = importlib.util.spec_from_file_location("kummer_frozen_helper", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


E = load_frozen_helper()
P = E.P


class Cyclotomic:
    """Z[zeta_m] for m=3,4,6, in the integral basis 1,zeta_m."""

    def __init__(self, m: int):
        P.require_int(m, "cyclotomic order", 3, 6)
        if m not in (3, 4, 6):
            raise ValueError(
                "only the declared quadratic cyclotomic rings are replayed"
            )
        self.m = m
        self.s = {3: -1, 4: 0, 6: 1}[m]
        self.roots = [self.power((0, 1), k) for k in range(m)]

    def add(self, a, b):
        return (a[0] + b[0], a[1] + b[1])

    def scale(self, a, n):
        return (a[0] * n, a[1] * n)

    def mul(self, a, b):
        x, y = a
        z, w = b
        return (x * z - y * w, x * w + y * z + self.s * y * w)

    def conjugate(self, a):
        return (a[0] + self.s * a[1], -a[1])

    def power(self, a, n):
        P.require_int(n, "cyclotomic exponent", 0, P.MAX_FIELD)
        result = ONE
        while n:
            if n & 1:
                result = self.mul(result, a)
            a = self.mul(a, a)
            n >>= 1
        return result

    def divide_integer(self, a, n):
        P.require_int(n, "exact divisor", 1, P.MAX_FIELD)
        if a[0] % n or a[1] % n:
            raise ArithmeticError("Newton coefficient is not cyclotomic integral")
        return (a[0] // n, a[1] // n)

    def sum(self, values):
        result = ZERO
        for value in values:
            result = self.add(result, value)
        return result


def primitive_generator(p: int) -> int:
    for g in range(2, p):
        if len({pow(g, e, p) for e in range(p - 1)}) == p - 1:
            return g
    raise ArithmeticError("no primitive base-field generator found")


def character_exponents(field, m: int) -> list[int | None]:
    if (field.p - 1) % m:
        raise ValueError("base field does not contain the required roots of unity")
    generator = primitive_generator(field.p)
    eta = pow(generator, (field.p - 1) // m, field.p)
    root_exponents = {pow(eta, j, field.p): j for j in range(m)}
    if len(root_exponents) != m:
        raise ArithmeticError("source eta is not primitive")
    output = [None]
    for t in range(1, field.q):
        norm = field.power(t, (field.q - 1) // (field.p - 1))
        if not 1 <= norm < field.p:
            raise ArithmeticError("extension norm is not in the base field")
        output.append(root_exponents[pow(norm, (field.p - 1) // m, field.p)])
    return output


def newton(ring, sums: list[tuple[int, int]]) -> list[tuple[int, int]]:
    coefficients = [ONE]
    for n in range(1, len(sums) + 1):
        numerator = ring.sum(
            ring.mul(sums[i - 1], coefficients[n - i]) for i in range(1, n + 1)
        )
        coefficients.append(ring.divide_integer(numerator, n))
    return coefficients


def local_sums(ring, coefficients, count):
    values = []
    for n in range(1, count + 1):
        value = ring.scale(coefficients[n] if n < len(coefficients) else ZERO, n)
        for i in range(1, n):
            c = coefficients[n - i] if n - i < len(coefficients) else ZERO
            value = ring.add(value, ring.scale(ring.mul(values[i - 1], c), -1))
        values.append(value)
    return values


def polynomial_product(ring, left, right):
    output = [ZERO] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            output[i + j] = ring.add(output[i + j], ring.mul(a, b))
    return output


def paired_reciprocity(ring, left, right, q):
    if len(left) != len(right) or left[0] != ONE or right[0] != ONE:
        return False
    degree = len(left) - 1
    return all(
        ring.scale(left[k], q ** (degree - k)) == ring.mul(left[-1], right[degree - k])
        for k in range(degree + 1)
    )


def count_tower(field, ring, A: int, B: int) -> dict:
    if A % field.p == 0 or (-4 * A**3 - 27 * B**2) % field.p == 0:
        raise ValueError("the declared tower replay uses the smooth S3 stratum")
    m, d = ring.m, gcd(ring.m, 3)
    exponents = character_exponents(field, m)
    cubic, squares = E.histograms(field, A, B)
    power_counts = [0] * field.q
    for w in range(field.q):
        power_counts[field.power(w, 2 * m)] += 1
    elliptic = 1 + sum(squares[field.cubic(x, A, B)] for x in range(field.q))
    tower = d + sum(power_counts[field.cubic(x, A, B)] for x in range(field.q))
    sums = [ZERO] * m
    for t in range(field.q):
        trace_w = cubic[field.mul(t, t)] - 1
        sums[0] = ring.add(sums[0], (trace_w, 0))
        if t:
            for j in range(1, m):
                sums[j] = ring.add(
                    sums[j], ring.scale(ring.roots[j * exponents[t] % m], trace_w)
                )
    affine_sums = sums[:]
    infinity = [0] + [int(m // gcd(m, j) == 3) for j in range(1, m)]
    for j in range(1, m):
        sums[j] = ring.add(sums[j], (infinity[j], 0))
    if sums[0] != (elliptic - field.q - 1, 0) or ring.sum(sums) != (
        tower - field.q - 1,
        0,
    ):
        raise ArithmeticError(
            "character decomposition disagrees with complete primitive curve counts"
        )
    return {
        "degree": field.n,
        "field_order": field.q,
        "modulus": field.modulus,
        "elliptic_points": elliptic,
        "tower_points": tower,
        "infinity_points": d,
        "infinity_character_traces": infinity,
        "affine_character_sums": [list(v) for v in affine_sums],
        "complete_character_sums": [list(v) for v in sums],
    }


def validate_source(source):
    if P.digest(source) != EXPECTED_SOURCE_HASH:
        raise ValueError(
            "tower primitive source differs from frozen canonical identity"
        )
    if (
        source["extensions"] != [1, 2, 3, 4]
        or source["maximum_field_order"] != P.MAX_FIELD
    ):
        raise ValueError("unreviewed tower coverage")
    for panel in source["panels"]:
        for name in ("p", "m", "A", "B"):
            P.require_int(panel[name], name, -100, 100)
        if (
            panel["m"] not in (3, 4, 6)
            or panel["p"] ** 4 > P.MAX_FIELD
            or (panel["p"] - 1) % panel["m"]
        ):
            raise ValueError("unsupported tower panel")


def build(source):
    validate_source(source)
    fields, panels = {}, []
    for panel in source["panels"]:
        p, m, A, B = (panel[k] for k in ("p", "m", "A", "B"))
        ring = Cyclotomic(m)
        counts = []
        for n in source["extensions"]:
            if (p, n) not in fields:
                fields[p, n] = P.Field(p, n)
            counts.append(count_tower(fields[p, n], ring, A, B))
        factors = []
        for j in range(m):
            degree = 2 if j == 0 else 4 - int(m // gcd(m, j) == 3)
            sums = [tuple(c["complete_character_sums"][j]) for c in counts]
            polynomial = newton(ring, sums[:degree])
            if local_sums(ring, polynomial, 4) != sums:
                raise ArithmeticError("held-out character extension prediction failed")
            factors.append(polynomial)
        product = [ONE]
        for j, polynomial in enumerate(factors):
            partner = factors[-j % m]
            if [
                ring.conjugate(c) for c in polynomial
            ] != partner or not paired_reciprocity(ring, polynomial, partner, p):
                raise ArithmeticError("paired duality or cyclotomic conjugation failed")
            product = polynomial_product(ring, product, polynomial)
        genus = 2 * m - (1 + gcd(m, 3)) // 2
        if len(product) != 2 * genus + 1 or any(b for a, b in product):
            raise ArithmeticError(
                "total curve numerator has wrong degree or nonrational coefficients"
            )
        if local_sums(ring, product, 4) != [
            (c["tower_points"] - c["field_order"] - 1, 0) for c in counts
        ]:
            raise ArithmeticError(
                "product of character factors does not recover primitive tower counts"
            )
        if not paired_reciprocity(ring, product, product, p):
            raise ArithmeticError("full curve numerator is not reciprocal")
        panels.append(
            {
                "source": panel,
                "counts": counts,
                "genus": genus,
                "character_polynomials": [[list(c) for c in f] for f in factors],
                "character_degrees": [len(f) - 1 for f in factors],
                "individual_self_reciprocity": [
                    paired_reciprocity(ring, f, f, p) for f in factors
                ],
                "tower_polynomial": [c[0] for c in product],
                "primitive_prediction_boundary": "Each character factor reconstructed from its proved degree; degree-three factors independently predict extension four. Total high-degree product checked against all four primitive curve counts, not independently reconstructed at every degree.",
            }
        )
    return {
        "schema": "kummer-tower-replay-v1",
        "source_hash": P.digest(source),
        "panels": panels,
    }


def bindings():
    names = (
        "kummer_source.json",
        "kummer_replay.py",
        "test_kummer_replay.py",
        "KUMMER_TOWER_AND_PAIRED_DUALITY.md",
        "kummer_artifact.json",
    )
    return {
        "schema": "kummer-tower-binding-v1",
        "precursor": E.authenticate_precursor(),
        "helper_commit": HELPER_COMMIT,
        "files": {name: P.lf_hash(ROOT / name) for name in names},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    source = json.loads((ROOT / "kummer_source.json").read_text(encoding="utf-8"))
    artifact = build(source)
    artifact_path, binding_path = (
        ROOT / "kummer_artifact.json",
        ROOT / "kummer_provenance.json",
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
            "Kummer artifact",
        )
        P.require_same_json(
            json.loads(binding_path.read_text(encoding="utf-8")),
            bindings(),
            "Kummer bindings",
        )
    print(
        "PASS: six exact Kummer towers, all deck characters, 24 fields, infinity resonance and paired duality"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
