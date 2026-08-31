"""Bounded exact replay of the finite-graded virtual-parent classification.

The universal theorem and formal representation-ring recursion are in the note.
This program certifies only its explicitly bounded rational/integer controls.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
from fractions import Fraction
from itertools import pairwise, permutations
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SCRIPT = Path(__file__).resolve()
NOTE = HERE / "FINITE_GRADED_VIRTUAL_PARENT_CLASSIFICATION.md"
FIXTURE = HERE / "finite_graded_virtual_parent_classification.json"
MANIFEST = HERE / "finite_graded_virtual_parent_classification.sources.json"
TEST = ROOT / "tests/test_finite_graded_virtual_parent_classification.py"
PRIOR = HERE / "universal_coefficient_power_euler_obstruction.py"
SOURCE_COMMIT = "3c6dd97bb497d5b25c00883362fd2fff4d5f6af6"
SOURCE_ROWS = (
    (
        "research/l-families/atlas/generalized/UNIVERSAL_COEFFICIENT_POWER_EULER_OBSTRUCTION.md",
        "12fa8ca7dded5ebad41c308ed2b51be27879325a",
        "7d20466862ec8ce5c70760fe626cc6b82ca3d0ae6dfde872b8a235db7e9bc24d",
    ),
    (
        "research/l-families/atlas/generalized/universal_coefficient_power_euler_obstruction.py",
        "bd5abef6a5516a8cef01b0cc083cf423fdbe0afb",
        "947e1be5fefd6550d2c5304e3002047c34dc3d15befe58476f991c8a45e6f019",
    ),
    (
        "research/l-families/atlas/generalized/TRANSFER_MATRIX_SYMMETRIC_PARENT.md",
        "9aef6f8a780e9dff5c3b7a53c012c0956be036dc",
        "84759dc5ca81ef896e2a6ab2d9a7d3d32c3865f5f61bb45db18aaf8633578456",
    ),
)
MAX_N = 5
MAX_K = 5
MAX_GRADE = 16
MAX_DEGREE = (MAX_N - 1) * (MAX_K - 1)
MAX_INPUT_BITS = 256
MAX_BYTES = 262144
WORK_CAP = 5_000_000


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def integer(value: object, name: str, low: int, high: int) -> int:
    require(type(value) is int and low <= value <= high, f"invalid {name}")
    return value


def rank_power(n: int, k: int) -> None:
    integer(n, "rank", 1, MAX_N)
    integer(k, "power", 0, MAX_K)


def rational(value: object) -> Fraction:
    require(type(value) in (int, Fraction), "exact rational required")
    result = Fraction(value)
    require(
        max(result.numerator.bit_length(), result.denominator.bit_length())
        <= MAX_INPUT_BITS,
        "rational input bit cap exceeded",
    )
    return result


def canonical(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False
    ).encode("utf-8")


def render(value: object) -> str:
    return json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True) + "\n"


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")).hexdigest()


def same_json(actual: object, expected: object) -> None:
    require(canonical(actual) == canonical(expected), "typed canonical replay differs")


def _trim(values: list) -> list:
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return values


def int_polynomial(poly: object) -> tuple[int, ...]:
    require(
        type(poly) is tuple and 1 <= len(poly) <= MAX_DEGREE + 1, "polynomial cap/type"
    )
    for value in poly:
        require(type(value) is int, "integer polynomial coefficient required")
        require(value.bit_length() <= MAX_INPUT_BITS, "polynomial input bit cap")
    return tuple(_trim(list(poly)))


def differential_numerator(n: int, k: int) -> dict:
    rank_power(n, k)
    a, denominator, h = n - 1, 1, [1]
    steps = []
    for cycle in range(k):
        for j in range(1, a + 1):
            before = len(h) - 1
            q = denominator - j
            raw = [0] * (len(h) + 1)
            for t, coefficient in enumerate(h):
                raw[t] += (j + t) * coefficient
                raw[t + 1] += (q - t) * coefficient
            require(
                all(value % j == 0 for value in raw),
                "differential noninteger numerator",
            )
            h = _trim([value // j for value in raw])
            if cycle == 0:
                require(h == [1], "first cycle must leave numerator one")
            else:
                require(q - before == a - j + 1 > 0, "interlacing degree hypothesis")
                require(len(h) - 1 == before + 1, "interlacing degree increase")
            steps.append([denominator, j, before, len(h) - 1, q - before])
            denominator += 1
    degree = 0 if n == 1 or k == 0 else (n - 1) * (k - 1)
    require(len(h) - 1 == degree, "final numerator degree mismatch")
    require(h[0] == 1 and all(value > 0 for value in h), "numerator positivity")
    return {
        "numerator": h,
        "pole_order": denominator,
        "steps_d_j_m_newdegree_qminusm": steps,
    }


def _remainder(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    remainder = _trim(list(left))
    require(right != [0], "division by zero polynomial")
    while remainder != [0] and len(remainder) >= len(right):
        shift = len(remainder) - len(right)
        factor = remainder[-1] / right[-1]
        for j, coefficient in enumerate(right):
            remainder[shift + j] -= factor * coefficient
        _trim(remainder)
    return remainder


def _variations(signs: list[int]) -> int:
    nonzero = [sign for sign in signs if sign]
    return sum(left != right for left, right in pairwise(nonzero))


def _sign(value: Fraction) -> int:
    return (value > 0) - (value < 0)


def sturm_data(poly: tuple[int, ...]) -> dict:
    values = int_polynomial(poly)
    require(values[0] != 0, "zero root outside Sturm control")
    degree = len(values) - 1
    if degree == 0:
        return {"degree": 0, "negative_roots": 0, "positive_roots": 0, "simple": True}
    chain = [list(map(Fraction, values))]
    chain.append([Fraction(j * values[j]) for j in range(1, len(values))])
    while True:
        remainder = _remainder(chain[-2], chain[-1])
        if remainder == [0]:
            break
        next_poly = [-value for value in remainder]
        scale = abs(next_poly[-1])
        chain.append([value / scale for value in next_poly])
    left = _variations([_sign(p[-1]) * (-1) ** (len(p) - 1) for p in chain])
    middle = _variations([_sign(p[0]) for p in chain])
    right = _variations([_sign(p[-1]) for p in chain])
    return {
        "degree": degree,
        "negative_roots": left - middle,
        "positive_roots": middle - right,
        "simple": len(chain[-1]) == 1,
        "chain_degrees": [len(p) - 1 for p in chain],
        "variations_minus_infinity_zero_plus_infinity": [left, middle, right],
    }


def coefficients(n: int, k: int, order: int) -> tuple[int, ...]:
    rank_power(n, k)
    integer(order, "grade", 2, MAX_GRADE)
    return tuple(comb(r + n - 1, n - 1) ** k for r in range(order + 1))


def validate_series(values: object) -> tuple[int, ...]:
    require(
        type(values) is tuple and 3 <= len(values) <= MAX_GRADE + 1, "series cap/type"
    )
    require(all(type(value) is int for value in values), "integer series required")
    require(
        all(value.bit_length() <= MAX_INPUT_BITS for value in values), "series bit cap"
    )
    require(values[0] == 1, "series constant must be one")
    return values


def mobius(value: int) -> int:
    integer(value, "Mobius argument", 1, MAX_GRADE)
    answer, divisor, remaining = 1, 2, value
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            remaining //= divisor
            answer = -answer
            if remaining % divisor == 0:
                return 0
        divisor += 1
    return -answer if remaining > 1 else answer


def euler_transform(values: tuple[int, ...]) -> dict:
    f = validate_series(values)
    logarithmic = [0] * len(f)
    dimensions = []
    for m in range(1, len(f)):
        logarithmic[m] = m * f[m] - sum(logarithmic[j] * f[m - j] for j in range(1, m))
        numerator = sum(
            mobius(d) * logarithmic[m // d] for d in range(1, m + 1) if m % d == 0
        )
        require(numerator % m == 0, "Euler transform failed integral divisibility")
        dimensions.append(numerator // m)
    return {
        "logarithmic_coefficients": logarithmic[1:],
        "graded_dimensions": dimensions,
    }


def _multiply_factor(product: list[int], weight: int, grade: int) -> list[int]:
    order = len(product) - 1
    factor = [1]
    for j in range(order // grade):
        numerator = factor[-1] * (weight + j)
        require(
            numerator % (j + 1) == 0, "binomial factor failed integral divisibility"
        )
        factor.append(numerator // (j + 1))
    output = [0] * (order + 1)
    for i, left in enumerate(product):
        for j, right in enumerate(factor):
            if i + j * grade <= order:
                output[i + j * grade] += left * right
    return output


def reconstruct_product(weights: tuple[int, ...]) -> tuple[int, ...]:
    require(
        type(weights) is tuple and 2 <= len(weights) <= MAX_GRADE, "weight count/type"
    )
    require(all(type(value) is int for value in weights), "integer weights required")
    require(
        all(value.bit_length() <= MAX_INPUT_BITS for value in weights), "weight bit cap"
    )
    result = [1] + [0] * len(weights)
    for grade, weight in enumerate(weights, start=1):
        result = _multiply_factor(result, weight, grade)
    return tuple(result)


def triangular_weights(values: tuple[int, ...]) -> tuple[int, ...]:
    f = validate_series(values)
    product = [1] + [0] * (len(f) - 1)
    weights = []
    for grade in range(1, len(f)):
        weight = f[grade] - product[grade]
        weights.append(weight)
        product = _multiply_factor(product, weight, grade)
        require(
            product[: grade + 1] == list(f[: grade + 1]),
            "triangular factor reconstruction",
        )
    require(tuple(product) == f, "triangular product differs")
    return tuple(weights)


def _multiply_polynomials(
    left: list[Fraction], right: list[Fraction]
) -> list[Fraction]:
    result = [Fraction()] * (len(left) + len(right) - 1)
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            result[i + j] += first * second
    return _trim(result)


def matrix(value: object, size: int) -> tuple[tuple[Fraction, ...], ...]:
    integer(size, "matrix size", 1, 4)
    require(type(value) is tuple and len(value) == size, "matrix row count/type")
    require(
        all(type(row) is tuple and len(row) == size for row in value),
        "matrix row shape",
    )
    return tuple(tuple(rational(entry) for entry in row) for row in value)


def determinant_polynomial(value: tuple[tuple, ...]) -> tuple[Fraction, ...]:
    require(type(value) is tuple, "matrix tuple required")
    a = matrix(value, len(value))
    size = len(a)
    result = [Fraction()] * (size + 1)
    for permutation in permutations(range(size)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(size)
            for j in range(i + 1, size)
        )
        term = [Fraction((-1) ** inversions)]
        for i, j in enumerate(permutation):
            term = _multiply_polynomials(term, [Fraction(i == j), -a[i][j]])
        for j, coefficient in enumerate(term):
            result[j] += coefficient
    return tuple(_trim(result))


def _quotient_series(
    numerator: tuple, denominator: tuple, order: int
) -> tuple[Fraction, ...]:
    require(denominator[0] == 1, "quotient denominator constant")
    result = []
    for r in range(order + 1):
        value = numerator[r] if r < len(numerator) else Fraction()
        value -= sum(
            denominator[j] * result[r - j]
            for j in range(1, min(r, len(denominator) - 1) + 1)
        )
        result.append(value)
    return tuple(result)


def rank_two_control(value: tuple[tuple, ...], order: int = 8) -> dict:
    integer(order, "matrix-control grade", 2, MAX_GRADE)
    a = matrix(value, 2)
    trace = a[0][0] + a[1][1]
    delta = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    require(delta != 0, "GL2 control requires nonzero determinant")
    tensor = tuple(
        tuple(a[i // 2][j // 2] * a[i % 2][j % 2] for j in range(4)) for i in range(4)
    )
    denominator = determinant_polynomial(tensor)
    invariant = (
        Fraction(1),
        -(trace**2),
        2 * delta * trace**2 - 2 * delta**2,
        -(delta**2) * trace**2,
        delta**4,
    )
    require(denominator == invariant, "tensor determinant invariant mismatch")
    h = [Fraction(1), trace]
    for _ in range(2, order + 1):
        h.append(trace * h[-1] - delta * h[-2])
    target = tuple(value**2 for value in h)
    numerator = (Fraction(1), Fraction(0), -(delta**2))
    require(
        _quotient_series(numerator, denominator, order) == target,
        "graded rank2 exception mismatch",
    )
    sym_denominator = (
        Fraction(1),
        delta - trace**2,
        delta * trace**2 - delta**2,
        -(delta**3),
    )
    require(
        _quotient_series((Fraction(1), delta), sym_denominator, order) == target,
        "Sym2 quotient mismatch",
    )
    return {
        "matrix": [[str(entry) for entry in row] for row in a],
        "trace": str(trace),
        "determinant": str(delta),
        "tensor_determinant": list(map(str, denominator)),
        "graded_numerator": list(map(str, numerator)),
        "coefficients_checked": list(map(str, target)),
    }


def work_bound(max_n: int, max_k: int, order: int) -> int:
    rank_power(max_n, max_k)
    integer(order, "grade", 2, MAX_GRADE)
    bound = 50000
    for n in range(1, max_n + 1):
        for k in range(max_k + 1):
            a, d = n - 1, k * (n - 1) + 1
            degree = 0 if k == 0 else a * (k - 1)
            finite_difference = sum(min(j, d) + 1 for j in range(2 * d + 4))
            bound += 4 * k * a * (degree + 2) + 8 * (degree + 2) ** 3
            bound += 10 * (order + 1) ** 3 + finite_difference + 32
    return bound


def validate_manifest(payload: object) -> None:
    expected = {
        "schema": "finite-graded-virtual-parent-sources-v1",
        "sources": [
            {"commit": SOURCE_COMMIT, "path": path, "git_blob": blob, "sha256_lf": sha}
            for path, blob, sha in SOURCE_ROWS
        ],
    }
    same_json(payload, expected)


def _bounded_bytes(path: Path) -> bytes:
    require(path.stat().st_size <= MAX_BYTES, "file byte cap exceeded")
    return path.read_bytes()


def source_locks() -> dict:
    payload = json.loads(_bounded_bytes(MANIFEST))
    validate_manifest(payload)
    for path, blob, sha in SOURCE_ROWS:
        ref = f"{SOURCE_COMMIT}:{path}"
        actual = subprocess.check_output(
            ["git", "rev-parse", "--verify", ref], cwd=ROOT, text=True, timeout=10
        ).strip()
        require(actual == blob, "primitive Git blob mismatch")
        size = int(
            subprocess.check_output(
                ["git", "cat-file", "-s", blob], cwd=ROOT, text=True, timeout=10
            )
        )
        require(size <= MAX_BYTES, "primitive blob byte cap exceeded")
        raw = subprocess.check_output(
            ["git", "cat-file", "blob", blob], cwd=ROOT, timeout=10
        )
        require(digest(raw) == sha, "primitive blob LF hash mismatch")
        require(
            digest(_bounded_bytes(ROOT / path)) == sha,
            "primitive worktree bytes differ",
        )
    return {
        "manifest_sha256_canonical": hashlib.sha256(canonical(payload)).hexdigest(),
        **payload,
    }


def _load_authenticated_prior():
    spec = importlib.util.spec_from_file_location("finite_graded_locked_prior", PRIOR)
    require(
        spec is not None and spec.loader is not None,
        "cannot import authenticated prior",
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build_fixture(
    max_n: int = 4, max_k: int = 4, order: int = 12, *, cap: int = WORK_CAP
) -> dict:
    bound = work_bound(max_n, max_k, order)
    integer(cap, "exclusive work cap", 1, 100_000_000)
    require(bound < cap, "exclusive work cap reached")
    locks = source_locks()
    prior = _load_authenticated_prior()
    rows = []
    for n in range(1, max_n + 1):
        for k in range(max_k + 1):
            differential = differential_numerator(n, k)
            numerator = differential["numerator"]
            finite, tail = prior.finite_difference_numerator(n, k)
            require(numerator == finite, "frozen finite-difference numerator mismatch")
            sturm = sturm_data(tuple(numerator))
            require(
                sturm["simple"]
                and sturm["negative_roots"] == len(numerator) - 1
                and sturm["positive_roots"] == 0,
                "negative simple-root census failed",
            )
            f = coefficients(n, k, order)
            euler = euler_transform(f)
            weights = tuple(euler["graded_dimensions"])
            require(
                weights == triangular_weights(f),
                "independent Euler factorization mismatch",
            )
            require(
                reconstruct_product(weights) == f,
                "Euler product reconstruction mismatch",
            )
            delta = comb(n**k + 1, 2) - comb(n + 1, 2) ** k
            symmetric, alternating = comb(n + 1, 2), comb(n, 2)
            even_sum = sum(
                comb(k, j) * symmetric ** (k - j) * alternating**j
                for j in range(2, k + 1, 2)
            )
            require(
                delta == even_sum and weights[0] == n**k and weights[1] == -delta,
                "quadratic relation mismatch",
            )
            exceptional = n == 1 or k <= 1 or (n, k) == (2, 2)
            gap = (numerator[1] if len(numerator) > 1 else 0) - (len(numerator) - 1)
            require(
                exceptional or gap > 0,
                "cyclotomic first-coefficient obstruction failed",
            )
            require(
                n < 2 or k < 2 or delta > 0, "effective second-grade obstruction failed"
            )
            if exceptional:
                require(
                    all(weight == 0 for weight in weights[2:]),
                    "exceptional scalar higher grade",
                )
                require(
                    (n, k) == (2, 2) or weights[1] == 0,
                    "elementary scalar second grade",
                )
            rows.append(
                {
                    "n": n,
                    "k": k,
                    **differential,
                    "frozen_difference_tail_checked_through": tail,
                    "sturm": sturm,
                    **euler,
                    "quadratic_relation_dimension": delta,
                    "even_subset_relation_dimension": even_sum,
                    "first_numerator_coefficient_minus_degree": gap,
                    "finite_graded_chamber": exceptional,
                    "product_coefficients": list(f),
                }
            )
    controls = [
        rank_two_control(a)
        for a in (
            ((1, 1), (0, 1)),
            ((2, 0), (0, 2)),
            ((0, -1), (1, 0)),
            ((2, 1), (1, 3)),
            ((Fraction(1, 2), Fraction(1, 3)), (Fraction(-2, 3), Fraction(3, 2))),
        )
    ]
    result = {
        "schema": "finite-graded-virtual-parent-classification-v1",
        "arithmetic_class": "MIXED",
        "arithmetic_components": ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
        "rounding_contract": "integer and Fraction operations, no rounding or floating roots",
        "source_locks": locks,
        "artifact_sha256_lf": {
            path.relative_to(ROOT).as_posix(): digest(_bounded_bytes(path))
            for path in (SCRIPT, NOTE, TEST, MANIFEST)
        },
        "parameters": {
            "max_n": max_n,
            "max_k": max_k,
            "grade": order,
            "exclusive_cap": cap,
            "declared_coefficient_update_bound": bound,
        },
        "identity_rows": rows,
        "rank_two_matrix_controls": controls,
        "scope": {
            "finite_graded_iff": "n=1 or k=0,1 or (n,k)=(2,2), universal algebraic GL_n representations",
            "formal_escape": "unique virtual symmetric-power factorization in the T-adic representation ring",
            "negative_second_grade": "negative actual quadratic relation representation for n,k>=2",
            "remaining_grades": "infinitely many nonzero representation classes outside the finite chambers, by the theorem not a finite dimension list",
            "external_frobenius_or_arbitrary_scalar_eigenvalues": "outside this representation-only classification",
            "analytic_global_convergence_or_RH_claim": False,
            "unbounded_root_theorem_machine_proved": False,
        },
    }
    result["payload_sha256"] = hashlib.sha256(canonical(result)).hexdigest()
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--max-n", type=int, default=4)
    parser.add_argument("--max-k", type=int, default=4)
    parser.add_argument("--grade", type=int, default=12)
    parser.add_argument("--cap", type=int, default=WORK_CAP)
    args = parser.parse_args()
    report = build_fixture(args.max_n, args.max_k, args.grade, cap=args.cap)
    if args.check:
        same_json(json.loads(_bounded_bytes(FIXTURE)), report)
        print("PASS_FINITE_GRADED_VIRTUAL_PARENT_CLASSIFICATION")
    else:
        print(render(report), end="")


if __name__ == "__main__":
    main()
