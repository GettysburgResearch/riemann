#!/usr/bin/env python3
"""Bounded exact source-algebra, diagonal, and source-aware Adams controls."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NOTE = HERE / "SOURCE_ALGEBRA_DIAGONAL_ADAMS_ADAPTER.md"
FIXTURE = HERE / "source_algebra_diagonal_adams_adapter.json"
MANIFEST = HERE / "source_algebra_diagonal_adams_adapter.sources.json"
TEST = ROOT / "tests/test_source_algebra_diagonal_adams_adapter.py"
MAX_ATOMS, MAX_ORDER, MAX_BITS = 8, 72, 32
SOURCE_ROWS = [
    {
        "commit": "6675c19f20760301d8c91dedc4a7836170003512",
        "path": "research/l-families/atlas/function_field/FFPS_SHARED_FIBRE_WICK_OCCUPANCY_SPECTRUM.md",
        "git_blob": "3e7fff53f5cdbb3a660b24b2e765f4ac35c434c3",
    },
    {
        "commit": "3a595dda92ef827a41e50d2395309692a93748ad",
        "path": "research/l-families/atlas/function_field/FFPS_RELATIVE_EXTERNAL_DIAGONAL_ADAMS.md",
        "git_blob": "884f2fc949bbd5b076df0c0c7afd4711f81ce37e",
    },
    {
        "commit": "3a595dda92ef827a41e50d2395309692a93748ad",
        "path": "research/l-families/atlas/function_field/FFPS_RELATIVE_TRACE_TENSOR_CLOSURE.md",
        "git_blob": "37647db8c43b983dc64bfc71a0c112539119a98a",
    },
]


def render(value: object) -> str:
    return json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True) + "\n"


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest()


def exact(value: int | Fraction) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError("exact integer or Fraction required")
    answer = Fraction(value)
    if max(answer.numerator.bit_length(), answer.denominator.bit_length()) > MAX_BITS:
        raise ValueError("input exceeds bounded rational size")
    return answer


def order(value: int) -> int:
    if type(value) is not int or not 1 <= value <= MAX_ORDER:
        raise ValueError("order must be an integer in 1..72")
    return value


@dataclass(frozen=True)
class Source:
    sigma: tuple[int, ...]
    weights: tuple[Fraction, ...]

    def __post_init__(self) -> None:
        if type(self.sigma) is not tuple or type(self.weights) is not tuple:
            raise TypeError("source fields must be tuples")
        size = len(self.sigma)
        if not 1 <= size <= MAX_ATOMS or len(self.weights) != size:
            raise ValueError("source size must agree and be in 1..8")
        if any(type(x) is not int for x in self.sigma) or sorted(self.sigma) != list(range(size)):
            raise ValueError("sigma must be an exact permutation")
        values = tuple(exact(value) for value in self.weights)
        if any(value == 0 for value in values):
            raise ValueError("Weil transition weights must be invertible")
        object.__setattr__(self, "weights", values)


def orbit_data(source: Source) -> tuple[tuple[int, Fraction], ...]:
    seen = set()
    rows = []
    for start in range(len(source.sigma)):
        if start in seen:
            continue
        point, length, monodromy = start, 0, Fraction(1)
        while point not in seen:
            seen.add(point)
            monodromy *= source.weights[point]
            point = source.sigma[point]
            length += 1
        rows.append((length, monodromy))
    return tuple(rows)


def power_at(source: Source, start: int, exponent: int) -> tuple[int, Fraction]:
    order(exponent)
    if type(start) is not int or not 0 <= start < len(source.sigma):
        raise ValueError("invalid source point")
    point, coefficient = start, Fraction(1)
    for _ in range(exponent):
        coefficient *= source.weights[point]
        point = source.sigma[point]
    return point, coefficient


def pushed_trace(source: Source, exponent: int) -> Fraction:
    order(exponent)
    answer = Fraction(0)
    for x in range(len(source.sigma)):
        point, coefficient = power_at(source, x, exponent)
        if point == x:
            answer += coefficient
    return answer


def orbit_trace(source: Source, exponent: int) -> Fraction:
    n = order(exponent)
    return sum((d * a ** (n // d) for d, a in orbit_data(source) if n % d == 0), Fraction(0))


def source_adams_trace(source: Source, exponent: int, adams: int) -> Fraction:
    n, e = order(exponent), order(adams)
    order(n * e)
    return sum((d * a ** (e * n // d) for d, a in orbit_data(source) if n % d == 0), Fraction(0))


def pushed_adams_trace(source: Source, exponent: int, adams: int) -> Fraction:
    return pushed_trace(source, order(order(exponent) * order(adams)))


def mobius(number: int) -> int:
    value = order(number)
    answer, prime = 1, 2
    while prime * prime <= value:
        if value % prime == 0:
            value //= prime
            answer = -answer
            if value % prime == 0:
                return 0
            while value % prime == 0:
                value //= prime
        prime += 1
    if value > 1:
        answer = -answer
    return answer


def primitive_trace(source: Source, degree: int) -> Fraction:
    d = order(degree)
    return sum((a for length, a in orbit_data(source) if length == d), Fraction(0))


def extract_primitive(source: Source, degree: int, *, after_pushforward: bool = False) -> Fraction:
    if type(after_pushforward) is not bool:
        raise TypeError("after_pushforward must be Boolean")
    d = order(degree)
    trace = pushed_adams_trace if after_pushforward else source_adams_trace
    return sum((mobius(e) * trace(source, d // e, e) for e in range(1, d + 1) if d % e == 0), Fraction(0)) / d


def tensor_over_source(left: Source, right: Source) -> Source:
    if left.sigma != right.sigma:
        raise ValueError("balanced source tensor requires the same Frobenius set")
    return Source(left.sigma, tuple(a * b for a, b in zip(left.weights, right.weights)))


def projected_diagonal_trace(left: Source, right: Source, exponent: int) -> Fraction:
    if left.sigma != right.sigma:
        raise ValueError("literal diagonal requires identical source point identification")
    order(exponent)
    answer = Fraction(0)
    for x, y in product(range(len(left.sigma)), repeat=2):
        fx, a = power_at(left, x, exponent)
        gy, b = power_at(right, y, exponent)
        if x == y and fx == x and gy == y:
            answer += a * b
    return answer


def projector_commutator_size(source: Source, *, partial: bool) -> int:
    if type(partial) is not bool:
        raise TypeError("partial must be Boolean")
    mismatches = 0
    for x, y in product(range(len(source.sigma)), repeat=2):
        target_x = source.sigma[x]
        target_y = y if partial else source.sigma[y]
        mismatches += int((x == y) != (target_x == target_y))
    return mismatches


def counterfeit() -> dict:
    cycle = Source((1, 0), (1, 1))
    split = Source((0, 1), (1, -1))
    fc, fs, p = ((0, 1), (1, 0)), ((1, 0), (0, -1)), ((1, 1), (1, -1))

    def matmul(a, b):
        return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)) for i in range(2))

    if matmul(fc, p) != matmul(p, fs) or p[0][0] * p[1][1] - p[0][1] * p[1][0] != -2:
        raise ArithmeticError("counterfeit conjugacy failed")
    traces = [pushed_trace(cycle, n) for n in range(1, 9)]
    if traces != [pushed_trace(split, n) for n in range(1, 9)]:
        raise ArithmeticError("counterfeit aggregate trace mismatch")
    dc = [pushed_trace(tensor_over_source(cycle, cycle), n) for n in range(1, 9)]
    ds = [pushed_trace(tensor_over_source(split, split), n) for n in range(1, 9)]
    if dc[0] != 0 or ds[0] != 2:
        raise ArithmeticError("counterfeit diagonal did not distinguish sources")
    return {
        "cycle_F": fc, "split_F": fs, "intertwiner": p, "intertwiner_determinant": -2,
        "common_power_traces_1_to_8": list(map(str, traces)),
        "cycle_diagonal_traces_1_to_8": list(map(str, dc)),
        "split_diagonal_traces_1_to_8": list(map(str, ds)),
        "cycle_P2": str(primitive_trace(cycle, 2)), "split_P2": str(primitive_trace(split, 2)),
        "source_Adams2_trace1": str(source_adams_trace(cycle, 1, 2)),
        "pushed_Adams2_trace1": str(pushed_adams_trace(cycle, 1, 2)),
        "incorrect_pushed_P2_extraction": str(extract_primitive(cycle, 2, after_pushforward=True)),
        "cycle_geometric_normal_order_degree2": str(traces[1] ** 2 - dc[1]),
        "cycle_closed_point_normal_order_degree2": str(
            primitive_trace(cycle, 2) ** 2 - primitive_trace(tensor_over_source(cycle, cycle), 2)
        ),
        "cycle_single_cell_Wick_at_d24over35": "0",
        "split_single_cell_Wick_at_d24over35": str(-2 * Fraction(24, 35)),
        "universal_all_n_equality_proof": "explicit invertible intertwiner, not the eight displayed traces",
    }


def source_locks() -> dict:
    expected = {
        "schema": "source-algebra-diagonal-adams-sources-v1",
        "sources": SOURCE_ROWS,
        "external_reference": "https://stacks.math.columbia.edu/tag/04JI",
        "external_reference_scope": "finite-etale/Galois-set interpretation only; algebraic proofs are in the note",
    }
    actual = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if render(actual) != render(expected):
        raise ValueError("source manifest differs from exact declared lock")
    rows = []
    for source in SOURCE_ROWS:
        ref = f"{source['commit']}:{source['path']}"
        blob = subprocess.check_output(["git", "rev-parse", ref], cwd=ROOT, text=True).strip()
        if blob != source["git_blob"]:
            raise ValueError(f"frozen source blob differs: {source['path']}")
        raw = subprocess.check_output(["git", "show", ref], cwd=ROOT)
        rows.append({**source, "sha256_lf": digest(raw)})
    return {"authenticated_frozen_sources": rows, "current_files_sha256_lf": {
        str(path.relative_to(ROOT)).replace("\\", "/"): digest(path.read_bytes())
        for path in (NOTE, Path(__file__).resolve(), TEST, MANIFEST)
    }}


def check_source(source: Source, upto: int = 6) -> dict:
    order(upto)
    partner = Source(source.sigma, tuple(Fraction(2 if j % 2 == 0 else -3) for j in range(len(source.sigma))))
    balanced = tensor_over_source(source, partner)
    for n in range(1, upto + 1):
        if pushed_trace(source, n) != orbit_trace(source, n):
            raise ArithmeticError("geometric point and orbit trace disagree")
        if projected_diagonal_trace(source, partner, n) != pushed_trace(balanced, n):
            raise ArithmeticError("source tensor and diagonal projector disagree")
        if extract_primitive(source, n) != primitive_trace(source, n):
            raise ArithmeticError("source-aware primitive extraction failed")
        if n > 1 and extract_primitive(source, n, after_pushforward=True) != 0:
            raise ArithmeticError("incorrect pushed extraction should erase higher degrees")
    if projector_commutator_size(source, partial=False) != 0:
        raise ArithmeticError("total Frobenius failed to preserve diagonal")
    is_split = source.sigma == tuple(range(len(source.sigma)))
    if (projector_commutator_size(source, partial=True) == 0) != is_split:
        raise ArithmeticError("partial Frobenius diagonal criterion failed")
    return {"sigma": source.sigma, "weights": list(map(str, source.weights)),
            "orbits": [[d, str(a)] for d, a in orbit_data(source)],
            "partial_commutator_size": projector_commutator_size(source, partial=True)}


def build_report() -> dict:
    census = []
    for size in range(1, 5):
        for sigma in permutations(range(size)):
            for weights in product((-1, 1), repeat=size):
                census.append(check_source(Source(sigma, weights)))
    heldout = Source((1, 2, 3, 4, 0), (1, 2, 3, -1, Fraction(1, 2)))
    return {
        "schema": "source-algebra-diagonal-adams-adapter-v1",
        "scope": "exact finite Frobenius-set algebra; native source realization remains open",
        "arithmetic_class": "MIXED",
        "arithmetic_components": ["CERTIFIED_INTEGER_COVERAGE", "EXACT_RATIONAL"],
        "coverage": "declared bounded permutation corpus only; not complete native coverage",
        "source_lock": source_locks(),
        "census_source_count": len(census),
        "census_order_max": 6,
        "census_sha256": hashlib.sha256(render(census).encode("ascii")).hexdigest(),
        "heldout_five_cycle": check_source(heldout),
        "all_traces_counterfeit": counterfeit(),
        "firewalls": {
            "diagonal": "tensor over retained source algebra, not aggregate scalar square",
            "Hermitian_partner": "conjugate traces must be specified; dual is not automatically conjugate",
            "Adams": "source local Adams before pushforward; pushed Adams has extra orbit terms",
            "partial_Frobenius": "not required on literal diagonal, following frozen #760",
            "rank_tax": "faithful source-algebra module only, not arbitrary nonlinear statistics",
            "native_uniform_realization": "open",
            "signed_trace_estimate": "open",
            "RH_GRH": "not proved",
            "novelty": "not claimed; classical algebra used to sharpen the source interface",
        },
    }


def check_fixture(actual: dict, expected: dict) -> None:
    if render(actual) != render(expected):
        raise ValueError("fixture differs from exact typed replay")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    report = build_report()
    if args.write:
        FIXTURE.write_text(render(report), encoding="utf-8")
        print(f"wrote {FIXTURE.name}")
    else:
        check_fixture(json.loads(FIXTURE.read_text(encoding="utf-8")), report)
        print(f"source-algebra adapter: {report['census_source_count']} exact sources and held-out controls PASS")


if __name__ == "__main__":
    main()
