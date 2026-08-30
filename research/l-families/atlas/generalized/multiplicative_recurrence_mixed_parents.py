"""Small exact controls for the multiplicative/mixed-parent proof note.

The all-parameter results are proved in prose. This replay authenticates the
frozen sources and recomputes finite rational/Gaussian-rational controls.
It performs no approximate arithmetic, scans, external CAS work, or builds.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
STEM = "multiplicative_recurrence_mixed_parents"
NOTE = HERE / "MULTIPLICATIVE_RECURRENCE_AND_MIXED_PARENTS.md"
MANIFEST = HERE / (STEM + ".sources.json")
FIXTURE = HERE / (STEM + ".json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BASE = "ab7ebfa3d4e3f1a657b4127b40796953060b6b3e"
SOURCE_ROWS = (
    (
        "research/l-families/atlas/generalized/IRRATIONAL_ROTATION_ABSOLUTE_POWER_RATIONALITY.md",
        "8f27df80a4983b4d393ee3a2477a744afaeb1d3a",
        "213efe84034449a7ece87b273653bc683c11b28ea4f62e599e3f2b0bbac7c8a2",
    ),
    (
        "research/l-families/atlas/generalized/FINITE_GRADED_VIRTUAL_PARENT_CLASSIFICATION.md",
        "3932273279d43ffa34d929247152cb43b932fa1d",
        "50daa223c5b6d0f061d771f24775a0a7a2d470f9185a1d6304f3b49e9fc799bc",
    ),
)
MAX_RANK = 5
MAX_FACTORS = 5
MAX_SUM_A = 10
MAX_BIDEGREE = 6
MAX_SPECTRUM = 40

G = tuple[Fraction, Fraction]
ZERO: G = (Fraction(0), Fraction(0))
ONE: G = (Fraction(1), Fraction(0))


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def integer(value: object, name: str, low: int, high: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(name + " must be an integer, not Boolean/float")
    need(low <= value <= high, name + " exceeds exact replay limits")
    return value


def rational(value: object) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError("exact rational required")
    answer = Fraction(value)
    need(answer.numerator.bit_length() <= 64, "rational numerator too large")
    need(answer.denominator.bit_length() <= 64, "rational denominator too large")
    return answer


def bidegree(m: int, n: int) -> None:
    integer(m, "m", 0, MAX_BIDEGREE)
    integer(n, "n", 0, MAX_BIDEGREE)
    need(m + n <= MAX_BIDEGREE, "total bidegree exceeds cap")


def profile(ranks: tuple[int, ...]) -> tuple[int, ...]:
    if not isinstance(ranks, tuple):
        raise TypeError("rank profile must be a tuple")
    need(1 <= len(ranks) <= MAX_FACTORS, "factor count exceeds cap")
    for rank in ranks:
        integer(rank, "rank", 1, MAX_RANK)
    need(sum(rank - 1 for rank in ranks) <= MAX_SUM_A, "identity degree exceeds cap")
    return ranks


def compositions(total: int, parts: int) -> list[tuple[int, ...]]:
    integer(total, "composition total", 0, MAX_BIDEGREE)
    integer(parts, "composition parts", 1, 3)
    if parts == 1:
        return [(total,)]
    return [
        (first,) + rest
        for first in range(total + 1)
        for rest in compositions(total - first, parts - 1)
    ]


def multinomial(total: int, row: tuple[int, ...]) -> int:
    return math.factorial(total) // math.prod(math.factorial(j) for j in row)


def circle_spectrum(c: int | Fraction, m: int, n: int) -> dict[int, Fraction]:
    bidegree(m, n)
    c = rational(c)
    need(c > 1, "circle center must be real and strictly greater than one")
    result: dict[int, Fraction] = {}
    for i in range(m + 1):
        for j in range(n + 1):
            value = math.comb(m, i) * math.comb(n, j) * c ** (m + n - i - j)
            result[i - j] = result.get(i - j, Fraction(0)) + value
    return dict(sorted(result.items()))


def periodic_circle_order(c: int | Fraction, m: int, n: int, period: int) -> int:
    integer(period, "period", 1, 32)
    out: dict[int, Fraction] = {}
    for label, value in circle_spectrum(c, m, n).items():
        residue = label % period
        out[residue] = out.get(residue, Fraction(0)) + value
    return sum(value != 0 for value in out.values())


def moduli_count(order_cap: int, weight: int | None = None) -> int:
    integer(order_cap, "order cap", 1, 16)
    if weight is None:
        return order_cap * (order_cap + 1) // 2
    integer(weight, "twist weight", -16, 16)
    return max(0, 1 + (order_cap - 1 - abs(weight)) // 2)


def gadd(a: G, b: G) -> G:
    return a[0] + b[0], a[1] + b[1]


def gneg(a: G) -> G:
    return -a[0], -a[1]


def gsub(a: G, b: G) -> G:
    return gadd(a, gneg(b))


def gmul(a: G, b: G) -> G:
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def gconj(a: G) -> G:
    return a[0], -a[1]


def gdiv(a: G, b: G) -> G:
    norm = b[0] * b[0] + b[1] * b[1]
    need(norm != 0, "division by zero Gaussian rational")
    top = gmul(a, gconj(b))
    return top[0] / norm, top[1] / norm


def gpow(a: G, power: int) -> G:
    out = ONE
    for _ in range(power):
        out = gmul(out, a)
    return out


def gaussian_inputs(
    roots: tuple[tuple[int | Fraction, int | Fraction], ...],
) -> tuple[G, ...]:
    if not isinstance(roots, tuple):
        raise TypeError("roots must be an exact tuple")
    need(1 <= len(roots) <= 3, "root rank exceeds cap")
    out = []
    for root in roots:
        need(isinstance(root, tuple) and len(root) == 2, "invalid Gaussian root")
        item = rational(root[0]), rational(root[1])
        need(item != ZERO, "zero characteristic root excluded")
        out.append(item)
    need(len(set(out)) == len(out), "Binet replay requires distinct roots")
    return tuple(out)


def gpoly_mul(a: list[G], b: list[G]) -> list[G]:
    out = [ZERO] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] = gadd(out[i + j], gmul(left, right))
    return out


def binet_coefficients(roots: tuple[G, ...]) -> tuple[G, ...]:
    answer = []
    for j, root in enumerate(roots):
        denominator = ONE
        for i, other in enumerate(roots):
            if i != j:
                denominator = gmul(denominator, gsub(root, other))
        answer.append(gdiv(gpow(root, len(roots) - 1), denominator))
    return tuple(answer)


def shadow_spectrum(
    roots: tuple[tuple[int | Fraction, int | Fraction], ...], m: int, n: int
) -> dict[G, G]:
    bidegree(m, n)
    roots_g = gaussian_inputs(roots)
    expected = math.comb(len(roots_g) + m - 1, m) * math.comb(len(roots_g) + n - 1, n)
    need(expected <= MAX_SPECTRUM, "symbolic spectrum exceeds cap before expansion")
    coefficients = binet_coefficients(roots_g)
    out: dict[G, G] = {}
    for u in compositions(m, len(roots_g)):
        for v in compositions(n, len(roots_g)):
            root = ONE
            coefficient: G = (
                Fraction(multinomial(m, u) * multinomial(n, v)),
                Fraction(0),
            )
            for j, base in enumerate(roots_g):
                root = gmul(root, gmul(gpow(base, u[j]), gpow(gconj(base), v[j])))
                coefficient = gmul(
                    coefficient,
                    gmul(
                        gpow(coefficients[j], u[j]), gpow(gconj(coefficients[j]), v[j])
                    ),
                )
            out[root] = gadd(out.get(root, ZERO), coefficient)
    return {
        root: coefficient for root, coefficient in out.items() if coefficient != ZERO
    }


def local_h_sequence(roots: tuple[G, ...], count: int) -> list[G]:
    denominator = [ONE]
    for root in roots:
        denominator = gpoly_mul(denominator, [ONE, gneg(root)])
    out = [ONE]
    for r in range(1, count):
        total = ZERO
        for j in range(1, min(r, len(roots)) + 1):
            total = gadd(total, gmul(denominator[j], out[r - j]))
        out.append(gneg(total))
    return out


def shadow_control(
    roots: tuple[tuple[int, int], ...], m: int, n: int
) -> dict[str, object]:
    spectrum = shadow_spectrum(roots, m, n)
    order = len(spectrum)
    denominator = [ONE]
    for root in spectrum:
        denominator = gpoly_mul(denominator, [ONE, gneg(root)])
    h = local_h_sequence(gaussian_inputs(roots), 2 * order + 3)
    transformed = [gmul(gpow(value, m), gpow(gconj(value), n)) for value in h]
    for r, value in enumerate(transformed):
        via_spectrum = ZERO
        for root, coefficient in spectrum.items():
            via_spectrum = gadd(via_spectrum, gmul(coefficient, gpow(root, r)))
        need(value == via_spectrum, "independent coefficient/spectrum disagreement")
    numerator = gpoly_mul(denominator, transformed)
    need(
        all(value == ZERO for value in numerator[order : len(transformed)]),
        "tail not annihilated",
    )
    return {
        "roots": [list(root) for root in roots],
        "bidegree": [m, n],
        "generic_bound": math.comb(len(roots) + m - 1, m)
        * math.comb(len(roots) + n - 1, n),
        "actual_order": order,
        "nonzero_residues": len(spectrum),
        "checked_coefficients": len(transformed),
        "denominator": [gjson(value) for value in denominator],
        "numerator": [gjson(value) for value in numerator[:order]],
    }


def trim(poly: list[Fraction]) -> list[Fraction]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def identity_numerator(ranks: tuple[int, ...]) -> list[int]:
    profile(ranks)
    aa = sorted((rank - 1 for rank in ranks), reverse=True)
    h = [Fraction(1)]
    denominator_degree = 1
    for a in aa:
        for j in range(1, a + 1):
            out = [Fraction(0)] * (len(h) + 1)
            for exponent, coefficient in enumerate(h):
                out[exponent] += Fraction(j + exponent, j) * coefficient
                out[exponent + 1] += (
                    Fraction(denominator_degree - j - exponent, j) * coefficient
                )
            h = trim(out)
            denominator_degree += 1
    need(all(value.denominator == 1 for value in h), "Segre numerator is not integral")
    return [int(value) for value in h]


def finite_difference_numerator(ranks: tuple[int, ...]) -> list[int]:
    profile(ranks)
    degree = sum(rank - 1 for rank in ranks) + 1
    values = [
        math.prod(math.comb(r + rank - 1, rank - 1) for rank in ranks)
        for r in range(degree + 3)
    ]
    out = [
        sum(
            (-1) ** j * math.comb(degree, j) * values[r - j]
            for j in range(min(r, degree) + 1)
        )
        for r in range(len(values))
    ]
    need(all(value == 0 for value in out[degree:]), "finite-difference tail nonzero")
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def remainder(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    a = trim(a[:])
    b = trim(b[:])
    need(b != [0], "zero polynomial divisor")
    while a != [0] and len(a) >= len(b):
        shift = len(a) - len(b)
        scale = a[-1] / b[-1]
        for j, coefficient in enumerate(b):
            a[j + shift] -= scale * coefficient
        trim(a)
    return a


def variations(signs: list[int]) -> int:
    nonzero = [value for value in signs if value]
    return sum(left != right for left, right in itertools.pairwise(nonzero))


def sturm_negative_simple(poly: list[int]) -> tuple[int, bool]:
    need(1 <= len(poly) <= MAX_SUM_A + 2, "Sturm degree outside cap")
    for value in poly:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("Sturm input coefficients must be integers")
        need(value.bit_length() <= 128, "Sturm coefficient too large")
    need(poly[-1] != 0, "untrimmed polynomial")
    if len(poly) == 1:
        need(poly[0] != 0, "zero polynomial")
        return 0, True
    sequence = [
        [Fraction(value) for value in poly],
        [Fraction(j * poly[j]) for j in range(1, len(poly))],
    ]
    while True:
        rem = remainder(sequence[-2], sequence[-1])
        if rem == [0]:
            break
        sequence.append([-value for value in rem])
    signs_left = [(-1 if p[-1] < 0 else 1) * (-1) ** (len(p) - 1) for p in sequence]
    signs_zero = [(p[0] > 0) - (p[0] < 0) for p in sequence]
    return variations(signs_left) - variations(signs_zero), len(sequence[-1]) == 1


def second_grade(ranks: tuple[int, ...]) -> tuple[int, int]:
    profile(ranks)
    direct = math.prod(math.comb(rank + 1, 2) for rank in ranks) - math.comb(
        math.prod(ranks) + 1, 2
    )
    relations = 0
    for mask in range(1 << len(ranks)):
        count = mask.bit_count()
        if count >= 2 and count % 2 == 0:
            relations += math.prod(
                math.comb(rank, 2) if mask & (1 << i) else math.comb(rank + 1, 2)
                for i, rank in enumerate(ranks)
            )
    return direct, -relations


def finite_parent_case(ranks: tuple[int, ...]) -> bool:
    profile(ranks)
    active = tuple(rank for rank in ranks if rank > 1)
    return len(active) <= 1 or active == (2, 2)


def rank_control(ranks: tuple[int, ...]) -> dict[str, object]:
    h = identity_numerator(ranks)
    need(h == finite_difference_numerator(ranks), "two numerator methods disagree")
    a = [rank - 1 for rank in ranks]
    expected_degree = sum(a) - max(a)
    negative, simple = sturm_negative_simple(h)
    need(len(h) - 1 == expected_degree, "degree formula disagrees")
    need(negative == expected_degree and simple, "negative simple-root control failed")
    need(
        sum(h) == math.factorial(sum(a)) // math.prod(math.factorial(j) for j in a),
        "H(1) mismatch",
    )
    direct, relations = second_grade(ranks)
    need(direct == relations, "independent second relation dimension disagrees")
    return {
        "ranks": list(ranks),
        "numerator": h,
        "degree": expected_degree,
        "negative_roots": negative,
        "simple": simple,
        "finite_parent": finite_parent_case(ranks),
        "second_virtual_dimension": direct,
    }


def imatrix(
    matrix: tuple[tuple[int, int], tuple[int, int]],
) -> tuple[tuple[int, int], tuple[int, int]]:
    need(
        isinstance(matrix, tuple) and len(matrix) == 2, "matrix must be a two-row tuple"
    )
    for row in matrix:
        need(isinstance(row, tuple) and len(row) == 2, "matrix row shape invalid")
        for value in row:
            integer(value, "matrix entry", -10, 10)
    need(
        matrix[0][0] * matrix[1][1] != matrix[0][1] * matrix[1][0],
        "invertibility required",
    )
    return matrix


def ipoly_mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] += left * right
    return out


def determinant_polynomial(matrix: list[list[int]]) -> list[int]:
    size = len(matrix)
    need(
        size == 4 and all(len(row) == 4 for row in matrix),
        "determinant replay is exactly four by four",
    )
    out = [0] * 5
    for permutation in itertools.permutations(range(size)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(size)
            for j in range(i + 1, size)
        )
        term = [(-1) ** inversions]
        for i, j in enumerate(permutation):
            term = ipoly_mul(term, [int(i == j), -matrix[i][j]])
        out = [left + right for left, right in zip(out, term)]
    return out


def tensor_pair_control(
    left: tuple[tuple[int, int], tuple[int, int]],
    right: tuple[tuple[int, int], tuple[int, int]],
) -> dict[str, object]:
    imatrix(left)
    imatrix(right)
    tensor = [
        [left[i // 2][j // 2] * right[i % 2][j % 2] for j in range(4)] for i in range(4)
    ]
    denominator = determinant_polynomial(tensor)

    def values(
        matrix: tuple[tuple[int, int], tuple[int, int]],
    ) -> tuple[list[int], int]:
        trace = matrix[0][0] + matrix[1][1]
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        result = [1, trace]
        for _ in range(11):
            result.append(trace * result[-1] - det * result[-2])
        return result, det

    aa, da = values(left)
    bb, db = values(right)
    product = [a * b for a, b in zip(aa, bb)]
    convolution = ipoly_mul(denominator, product)
    expected = [1, 0, -da * db] + [0] * (len(product) - 3)
    need(convolution[: len(product)] == expected, "rank-two tensor numerator mismatch")
    return {
        "left": [list(row) for row in left],
        "right": [list(row) for row in right],
        "tensor_denominator": denominator,
        "numerator": expected[:3],
        "checked_coefficients": len(product),
    }


def normalized(raw: bytes) -> bytes:
    return raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def digest(raw: bytes) -> str:
    return hashlib.sha256(normalized(raw)).hexdigest()


def canonical(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("utf-8")


def sources_contract() -> dict[str, object]:
    return {
        "schema": "riemann.glo764.mulrec.sources.v1",
        "base_commit": BASE,
        "sources": [
            {"path": path, "git_blob": blob, "sha256_lf": sha}
            for path, blob, sha in SOURCE_ROWS
        ],
        "normalization": "continuous scalar multiplicativity; c>1 irrational circle; universal all-matrix graded representation identity",
        "scope": "local exact algebra and prose theorems only; no global L-function or novelty claim",
    }


def authenticate() -> dict[str, object]:
    contract = sources_contract()
    need(
        json.loads(MANIFEST.read_text(encoding="utf-8")) == contract,
        "source manifest differs from compiled contract",
    )
    for path, blob, sha in SOURCE_ROWS:
        result = subprocess.run(
            ["git", "rev-parse", "--verify", BASE + ":" + path],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
            timeout=15,
        )
        need(
            result.returncode == 0 and result.stdout.strip() == blob,
            "source commit/blob mismatch: " + path,
        )
        raw = subprocess.run(
            ["git", "cat-file", "blob", blob],
            cwd=ROOT,
            capture_output=True,
            check=False,
            timeout=15,
        )
        need(
            raw.returncode == 0 and digest(raw.stdout) == sha,
            "frozen source content mismatch: " + path,
        )
        need(
            digest((ROOT / path).read_bytes()) == sha,
            "current primitive differs from frozen source: " + path,
        )
    return contract


def qjson(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def gjson(value: G) -> list[list[int]]:
    return [qjson(value[0]), qjson(value[1])]


def produce() -> dict[str, object]:
    sources = authenticate()
    circles = []
    for m in range(4):
        for n in range(4):
            spectrum = circle_spectrum(Fraction(3, 2), m, n)
            need(
                list(spectrum) == list(range(-n, m + 1)),
                "circle spectrum has missing support",
            )
            need(
                all(value > 0 for value in spectrum.values()),
                "circle Fourier coefficient not positive",
            )
            periods = [periodic_circle_order(2, m, n, b) for b in range(1, 9)]
            need(
                periods == [min(b, m + n + 1) for b in range(1, 9)],
                "periodic collision order mismatch",
            )
            circles.append(
                {
                    "bidegree": [m, n],
                    "coefficients": [
                        [label, qjson(value)] for label, value in spectrum.items()
                    ],
                    "irrational_order": m + n + 1,
                    "periodic_orders_b1_to8": periods,
                }
            )
    ranks = [
        rank_control(row)
        for length in range(1, 5)
        for row in itertools.combinations_with_replacement(range(1, 5), length)
        if sum(rank - 1 for rank in row) <= 8
    ]
    shadows = [
        shadow_control(((2, 1), (3, 2)), m, n)
        for m, n in ((0, 0), (1, 0), (1, 1), (2, 1), (2, 2))
    ]
    shadows += [
        shadow_control(((2, 1), (3, 2), (4, 1)), 2, 1),
        shadow_control(((2, 0), (3, 0)), 1, 1),
        shadow_control(((0, 1), (0, -1)), 1, 1),
    ]
    pairs = [
        tensor_pair_control(a, b)
        for a, b in (
            (((2, 0), (0, 3)), ((5, 0), (0, 7))),
            (((2, 1), (0, 2)), ((3, 0), (1, 3))),
            (((0, -1), (1, 0)), ((1, 1), (0, 1))),
            (((1, 2), (3, 4)), ((-2, 1), (1, 3))),
        )
    ]
    moduli = []
    for cap in range(1, 13):
        lattice = [(m, n) for m in range(cap) for n in range(cap) if m + n < cap]
        need(len(lattice) == moduli_count(cap), "bounded moduli count mismatch")
        slices = []
        for weight in range(-12, 13):
            actual = sum(m - n == weight for m, n in lattice)
            need(actual == moduli_count(cap, weight), "fixed-twist moduli mismatch")
            slices.append([weight, actual])
        moduli.append(
            {"circle_order_cap": cap, "count": len(lattice), "twist_slices": slices}
        )
    payload: dict[str, object] = {
        "schema": "riemann.glo764.mulrec.v1",
        "base_commit": BASE,
        "arithmetic": "EXACT_RATIONAL",
        "theorem_status": "prose proof; finite controls are not the all-parameter proof",
        "novelty": "unreviewed; no external priority claim",
        "claims": [
            "GLO764.MULREC.SHIFTED_CIRCLE_RIGIDITY",
            "GLO764.MULREC.MULTICOEFFICIENT_RIGIDITY",
            "GLO764.MULREC.DISCRETE_DEFORMATION_MODULI",
            "GLO764.MULREC.GENERIC_BIDEGREE_ORDER",
            "GLO764.MULREC.MIXED_RANK_FINITE_GRADED_PARENT",
            "GLO764.MULREC.UNEQUAL_SEGRE_ROOTS",
            "GLO764.MULREC.CONJUGATE_COEFFICIENT_PARENT",
        ],
        "caps": {
            "rank": MAX_RANK,
            "factors": MAX_FACTORS,
            "sum_d_minus_one": MAX_SUM_A,
            "total_bidegree": MAX_BIDEGREE,
            "expanded_spectrum": MAX_SPECTRUM,
        },
        "circles": circles,
        "mixed_ranks": ranks,
        "local_shadows": shadows,
        "tensor_pairs": pairs,
        "bounded_moduli": moduli,
        "hostile_origin_touching": {
            "map": "z^2/conj(z), extended by zero",
            "circle": "1+w",
            "quotient_numerator": [1, 2, 1],
            "quotient_denominator_laurent": [[-1, 1], [0, 1]],
            "reduced_laurent": [[1, 1], [2, 1]],
            "conclusion": "passes c=1 but is excluded by the c>1 theorem",
        },
        "source_manifest": sources,
        "owned_files": {
            path.relative_to(ROOT).as_posix(): digest(path.read_bytes())
            for path in (NOTE, Path(__file__), TEST, MANIFEST)
        },
        "firewalls": [
            "no prime-indexed family",
            "no canonical completion",
            "no analytic infinite-product convergence",
            "no automorphy or motivic realization",
            "no RH or GRH consequence",
            "generic counts require the explicit noncollision hypothesis",
        ],
    }
    payload["payload_sha256"] = hashlib.sha256(canonical(payload)).hexdigest()
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = produce()
    if args.write:
        FIXTURE.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        print("wrote exact multiplicative/mixed-parent controls")
    else:
        need(
            json.loads(FIXTURE.read_text(encoding="utf-8")) == payload,
            "fixture differs from full exact replay",
        )
        print("exact multiplicative/mixed-parent controls: PASS")


if __name__ == "__main__":
    main()
