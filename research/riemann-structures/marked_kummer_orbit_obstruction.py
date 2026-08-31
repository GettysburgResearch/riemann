#!/usr/bin/env python3
"""Exact source-bound Kummer--Tate expansion and finite divisor-orbit controls."""

from __future__ import annotations

import argparse
import json
import subprocess
from collections import defaultdict
from hashlib import sha1, sha256
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NOTE = HERE / "MARKED_KUMMER_ORBIT_OBSTRUCTION.md"
FIXTURE = HERE / "marked_kummer_orbit_obstruction.json"
TEST = ROOT / "tests" / "test_marked_kummer_orbit_obstruction.py"
SOURCE_COMMIT = "faf74a47dac33927d081a890f2b5a7ead48b869b"
SOURCES = {
    "research/riemann-structures/COMPLETE_MARKED_OWNER_PUSHFORWARD.md": "1c65af708e013cd60c8afffba64a43aee9835d33",
    "research/riemann-structures/complete_marked_owner_pushforward.py": "4564146cc8b3984c5ef5004d7548d6db6263d280",
    "research/riemann-structures/complete_marked_owner_pushforward.json": "ea9da0fa3b3acb63dbf0b68c1cb2ae8efaeefce3",
}
SOURCE_PROOF = "8fa0e40d7ed45b7db82a417e9ac7929cdc0eff01c14c4d62ad0502fceba17671"
MAX_BYTES = 262144
CROSSED = 1 << 8


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def canonical(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def source_bytes(path: str) -> bytes:
    require(path in SOURCES, "frozen primitive identity")
    ref = f"{SOURCE_COMMIT}:{path}"
    size = int(
        subprocess.run(
            ["git", "cat-file", "-s", ref],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout
    )
    require(0 < size <= MAX_BYTES, "frozen primitive byte cap")
    raw = subprocess.run(
        ["git", "show", ref],
        cwd=ROOT,
        capture_output=True,
        check=True,
    ).stdout
    require(len(raw) == size, "frozen primitive byte count")
    blob = sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest()
    require(blob == SOURCES[path], "frozen primitive Git blob")
    return raw


class Poly:
    """Z[n][(Z/2)^9], stored by (n-degree, character mask)."""

    def __init__(self, terms: dict[tuple[int, int], int]):
        require(type(terms) is dict and len(terms) <= 8192, "polynomial term cap")
        for key, value in terms.items():
            require(type(key) is tuple and len(key) == 2, "polynomial key")
            degree, mask = key
            require(type(degree) is int and 0 <= degree <= 16, "degree cap")
            require(type(mask) is int and 0 <= mask < 512, "character mask")
            require(type(value) is int and value.bit_length() <= 256, "coefficient")
        self.terms = {key: value for key, value in terms.items() if value}

    @staticmethod
    def scalar(value: int) -> Poly:
        require(type(value) is int, "integer scalar")
        return Poly({(0, 0): value})

    def __add__(self, other: Poly | int) -> Poly:
        other = other if isinstance(other, Poly) else Poly.scalar(other)
        terms = defaultdict(int, self.terms)
        for key, value in other.terms.items():
            terms[key] += value
        return Poly(dict(terms))

    __radd__ = __add__

    def __neg__(self) -> Poly:
        return Poly({key: -value for key, value in self.terms.items()})

    def __sub__(self, other: Poly | int) -> Poly:
        return self + (-other if isinstance(other, Poly) else -Poly.scalar(other))

    def __mul__(self, other: Poly | int) -> Poly:
        other = other if isinstance(other, Poly) else Poly.scalar(other)
        require(len(self.terms) * len(other.terms) <= 2000000, "product work cap")
        terms = defaultdict(int)
        for (degree, mask), value in self.terms.items():
            for (other_degree, other_mask), other_value in other.terms.items():
                terms[(degree + other_degree, mask ^ other_mask)] += value * other_value
        return Poly(dict(terms))

    __rmul__ = __mul__

    def square(self) -> Poly:
        return self * self

    def evaluate(self, n: int, signs: tuple[int, ...]) -> int:
        require(type(n) is int and 0 <= n <= 10000, "evaluation n cap")
        require(type(signs) is tuple and len(signs) == 9, "nine character signs")
        require(all(type(x) is int and x in (-1, 1) for x in signs), "sign type")
        total = 0
        for (degree, mask), coefficient in self.terms.items():
            sign = 1
            for bit in range(9):
                if mask & (1 << bit):
                    sign *= signs[bit]
            total += coefficient * n**degree * sign
        return total


def source_polynomial() -> Poly:
    n = Poly({(1, 0): 1})
    chars = [Poly({(0, 1 << i): 1}) for i in range(9)]
    r, s, crossed = sum(chars[:4]), sum(chars[4:8]), chars[8]
    omega = -Poly.scalar(1) - sum(chars[i] * chars[i + 4] for i in range(4))
    alpha, beta = -crossed - r, -crossed - s
    a = n * (n - 1) * (n - 2) * (n - 3)
    b = (n - 2) * (n - 3) * (alpha.square() - n)
    c = (n - 2) * (n - 3) * (beta.square() - n)
    t = (
        alpha.square() * beta.square()
        - (n - 4) * (alpha.square() + beta.square())
        - 4 * omega * alpha * beta
        + n.square()
        + 2 * omega.square()
        - 6 * n
    )
    return 81 * (a.square() + b.square() + c.square() + t.square()) - 36 * a


def direct_four_j(n: int, signs: tuple[int, ...]) -> int:
    """Independent scalar evaluation of the frozen three-moment formula."""
    r, s, crossed = sum(signs[:4]), sum(signs[4:8]), signs[8]
    omega = -1 - sum(signs[i] * signs[i + 4] for i in range(4))
    alpha, beta = -crossed - r, -crossed - s
    a = n * (n - 1) * (n - 2) * (n - 3)
    b = (n - 2) * (n - 3) * (alpha * alpha - n)
    c = (n - 2) * (n - 3) * (beta * beta - n)
    t = (
        alpha**2 * beta**2
        - (n - 4) * (alpha**2 + beta**2)
        - 4 * omega * alpha * beta
        + n * n
        + 2 * omega * omega
        - 6 * n
    )
    return 81 * (a * a + b * b + c * c + t * t) - 36 * a


def graph(index: int) -> dict[tuple[int, int], int]:
    require(type(index) is int and -8 <= index <= 8, "graph index cap")
    if index >= 0:
        return {(0, 1): 1, (5**index, 0): 4}
    return {(0, 5 ** (-index)): 1, (1, 0): 4}


def pullback(poly: dict[tuple[int, int], int], side: str):
    require(side in ("left", "right", "total"), "pullback side")
    return {
        (
            a * (5 if side in ("left", "total") else 1),
            b * (5 if side in ("right", "total") else 1),
        ): value
        for (a, b), value in poly.items()
    }


def restrict_to_graph(poly: dict[tuple[int, int], int], index: int):
    graph(index)
    result = defaultdict(int)
    for (a, b), value in poly.items():
        exponent = a + b * 5**index if index >= 0 else b + a * 5 ** (-index)
        result[exponent] = (result[exponent] + value) % 5
    return {key: value for key, value in result.items() if value}


def shifted_support(indices: tuple[int, ...], shift: int) -> tuple[int, ...]:
    require(type(indices) is tuple and len(indices) <= 32, "finite orbit support cap")
    require(all(type(x) is int and -100 <= x <= 100 for x in indices), "support type")
    require(len(set(indices)) == len(indices), "squarefree orbit support")
    require(type(shift) is int and -100 <= shift <= 100, "shift cap")
    return tuple(sorted(x + shift for x in indices))


def build() -> dict[str, object]:
    imported = {path: source_bytes(path) for path in SOURCES}
    owner = json.loads(
        imported["research/riemann-structures/complete_marked_owner_pushforward.json"]
    )
    require(owner["proof_object_sha256"] == SOURCE_PROOF, "frozen owner proof identity")
    polynomial = source_polynomial()
    controls = 0
    for signs in product((-1, 1), repeat=9):
        for n in (19, 119):
            require(
                polynomial.evaluate(n, signs) == direct_four_j(n, signs),
                "full sign character evaluation",
            )
            controls += 1
    odd = Poly(
        {
            (degree, mask ^ CROSSED): coefficient
            for (degree, mask), coefficient in polynomial.terms.items()
            if mask & CROSSED
        }
    )
    require(bool(odd.terms), "nonzero crossed source coefficient")
    external = (1, -1, 1, -1, -1, 1, -1, -1)
    specializations = []
    for n in (19, 119, 619):
        expected = 648 * (n - 3) ** 2 * ((n - 2) ** 2 * (n - 5) + (n - 9))
        require(
            odd.evaluate(n, external + (1,)) == expected > 0, "exact odd coefficient"
        )
        before = polynomial.evaluate(n, external + (1,))
        after = polynomial.evaluate(n, external + (-1,))
        require(after - before == -2 * expected, "crossed sign defect")
        specializations.append(
            {
                "n": n,
                "four_J_odd_coefficient": expected,
                "J_defect": (after - before) // 4,
            }
        )
    for name, sign in (("original", 1), ("left_partial", -1)):
        require(
            polynomial.evaluate(19, external + (sign,))
            == 4 * owner["cases"][0][name]["integer_principal_literal_wick"],
            "frozen complete owner observable",
        )
    graphs = []
    for index in range(-4, 5):
        left = graph(index + 1)
        right = graph(index - 1)
        if index < 0:
            left = pullback(left, "total")
        if index > 0:
            right = pullback(right, "total")
        require(pullback(graph(index), "left") == left, "left orbit identity")
        require(pullback(graph(index), "right") == right, "right orbit identity")
        require(
            pullback(graph(index), "total")
            == {(a * 5, b * 5): c for (a, b), c in graph(index).items()},
            "total Frobenius fifth-power identity",
        )
        incidence = [
            not restrict_to_graph(graph(other), index) for other in range(-4, 5)
        ]
        require(
            incidence == [other == index for other in range(-4, 5)],
            "distinct graph divisor incidence",
        )
        graphs.append({"index": index, "divisor_incidence": incidence})
    hashes = {}
    for path in (NOTE, Path(__file__), TEST):
        raw = path.read_bytes()
        require(len(raw) <= MAX_BYTES, "local source byte cap")
        hashes[path.relative_to(ROOT).as_posix()] = sha256(
            raw.replace(b"\r\n", b"\n")
        ).hexdigest()
    encoded_terms = [
        [degree, mask, value]
        for (degree, mask), value in sorted(polynomial.terms.items())
    ]
    result = {
        "schema": "riemann.marked_kummer_orbit.v1",
        "frozen_source_commit": SOURCE_COMMIT,
        "frozen_sources": SOURCES,
        "frozen_owner_proof": SOURCE_PROOF,
        "source_hashes": hashes,
        "polynomial_four_J_terms": len(polynomial.terms),
        "polynomial_sha256": sha256(canonical(encoded_terms).encode()).hexdigest(),
        "crossed_odd_terms": len(odd.terms),
        "all_sign_evaluations": controls,
        "source_specializations": specializations,
        "finite_graph_controls": graphs,
        "cover_degree_controls": [
            {"independent_lines": n, "minimum_degree": 2**n} for n in (1, 2, 4, 8, 32)
        ],
        "infinite_orbit_proved_by_divisors_not_finite_controls": True,
        "actual_derived_pushforward_identification_asserted": False,
        "all_geometric_parent_impossibility_asserted": False,
        "full_original_carrier_binding_asserted": False,
        "RH_or_GRH_conclusion": False,
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.write:
        FIXTURE.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    else:
        require(FIXTURE.stat().st_size <= MAX_BYTES, "artifact byte cap")
        candidate = json.loads(FIXTURE.read_text(encoding="utf-8"))
        require(canonical(candidate) == canonical(result), "exact canonical replay")
    print(
        json.dumps(
            {"status": "PASS", "proof_object_sha256": result["proof_object_sha256"]}
        )
    )


if __name__ == "__main__":
    main()
