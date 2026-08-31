"""Exact finite controls; global analysis and imported theorems are in the note."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from fractions import Fraction as Q
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SCRIPT = Path(__file__).resolve()
NOTE = HERE / "GRADED_PARENT_GLOBAL_BOUNDARY.md"
MANIFEST = HERE / "graded_parent_global_boundary.sources.json"
FIXTURE = HERE / "graded_parent_global_boundary.json"
TEST = ROOT / "tests/test_graded_parent_global_boundary.py"
SOURCE = "e2f469142cd55086e74751293877ab533001e786"
SOURCE_ROWS = (
    (
        "research/l-families/atlas/generalized/FINITE_GRADED_VIRTUAL_PARENT_CLASSIFICATION.md",
        "3932273279d43ffa34d929247152cb43b932fa1d",
        "50daa223c5b6d0f061d771f24775a0a7a2d470f9185a1d6304f3b49e9fc799bc",
        "native identity numerator, simple negative roots and integer formal grades",
    ),
    (
        "research/l-families/atlas/generalized/FINITE_GRADED_VIRTUAL_PARENT_CLASSIFICATION_AUDIT.md",
        "c6a9b701f6c4cd410e7dd6b67d6d7d22431f6ce3",
        "a67a1a901cc33f8c42059351325ffc5c8358bb8b2acf2433944676bab45e50d7",
        "independent exact-source parent review",
    ),
)
MAX_N = MAX_K = 5
MAX_ORDER = 32
MAX_DEGREE = 16
MAX_INPUT_BITS = 128
MAX_ARITH_BITS = 4096
MAX_BYTES = 262144
MAX_POINTS = 16
WORK_CAP = 25_000_000
DEFAULT_ORDER = 24


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def integer(value: object, low: int, high: int) -> int:
    require(type(value) is int and low <= value <= high, "integer outside contract")
    return value


def input_integer(value: object) -> int:
    require(type(value) is int, "exact integer required")
    require(abs(value).bit_length() <= MAX_INPUT_BITS, "input integer bit cap")
    return value


def arithmetic(value: int) -> int:
    require(type(value) is int, "exact arithmetic integer required")
    require(abs(value).bit_length() <= MAX_ARITH_BITS, "arithmetic bit cap")
    return value


def rational(value: object) -> Q:
    require(type(value) in (int, Q), "exact rational required")
    result = Q(value)
    require(
        max(result.numerator.bit_length(), result.denominator.bit_length())
        <= MAX_INPUT_BITS,
        "rational input bit cap",
    )
    return result


def parameters(n: int, k: int) -> None:
    integer(n, 1, MAX_N)
    integer(k, 0, MAX_K)


def canonical(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False
    ).encode()


def render(value: object) -> str:
    return json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True) + "\n"


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")).hexdigest()


def bounded_bytes(path: Path) -> bytes:
    require(path.stat().st_size <= MAX_BYTES, "file byte cap")
    raw = path.read_bytes()
    require(len(raw) <= MAX_BYTES, "file byte cap")
    return raw


def strict_json(raw: bytes) -> object:
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "JSON type or byte cap")

    def pairs(items: list) -> dict:
        result = {}
        for key, value in items:
            require(key not in result, "duplicate JSON key")
            result[key] = value
        return result

    def constant(value: str) -> None:
        raise ValueError(f"nonfinite JSON value: {value}")

    return json.loads(raw, object_pairs_hook=pairs, parse_constant=constant)


def same_json(left: object, right: object) -> None:
    require(canonical(left) == canonical(right), "typed canonical replay mismatch")


def preflight(n_max: int, k_max: int, order: int, cap: int = WORK_CAP) -> int:
    parameters(n_max, k_max)
    integer(order, 2, MAX_ORDER)
    integer(cap, 1, WORK_CAP)
    score = 10_000 + 20 * n_max * (k_max + 1) * (order + 1) ** 3
    require(score < cap, "work budget score must be strictly below cap")
    return score


def coefficients(n: int, k: int, order: int) -> tuple[int, ...]:
    parameters(n, k)
    integer(order, 0, MAX_ORDER)
    return tuple(comb(n + j - 1, n - 1) ** k for j in range(order + 1))


def numerator(n: int, k: int) -> dict:
    parameters(n, k)
    d = k * (n - 1) + 1
    q = (k - 1) * (n - 1) if k else 0

    def finite_difference(j: int) -> int:
        return sum(
            (-1) ** r * comb(d, r) * comb(n + j - r - 1, n - 1) ** k
            for r in range(min(d, j) + 1)
        )

    h = tuple(finite_difference(j) for j in range(q + 1))
    tail = tuple(finite_difference(j) for j in range(q + 1, q + 6))
    require(h[0] == 1 and h[-1] > 0, "numerator endpoints")
    require(all(value >= 0 for value in h), "numerator coefficients")
    require(tail == (0,) * 5, "finite vanishing-tail control")
    return {"denominator_power": d, "degree": q, "H": h, "tail": tail}


def polynomial(raw: object) -> tuple[int, ...]:
    require(type(raw) in (tuple, list), "coefficient list required")
    require(1 <= len(raw) <= MAX_DEGREE + 1, "polynomial degree cap")
    values = [input_integer(value) for value in raw]
    require(values[0] == 1, "constant coefficient must be one")
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def reconstruct_series(h: object, d: int, order: int) -> tuple[int, ...]:
    h = polynomial(h)
    integer(d, 1, MAX_K * (MAX_N - 1) + 1)
    integer(order, 0, MAX_ORDER)
    return tuple(
        sum(h[r] * comb(d + j - r - 1, d - 1) for r in range(min(j, len(h) - 1) + 1))
        for j in range(order + 1)
    )


def series(raw: object) -> tuple[int, ...]:
    require(type(raw) in (tuple, list), "series list required")
    require(1 <= len(raw) <= MAX_ORDER + 1, "series order cap")
    result = tuple(input_integer(value) for value in raw)
    require(result[0] == 1, "unit series required")
    return result


def logarithmic_coefficients(raw: object) -> tuple[int, ...]:
    f = series(raw)
    b = [0]
    for m in range(1, len(f)):
        b.append(arithmetic(m * f[m] - sum(b[r] * f[m - r] for r in range(1, m))))
    return tuple(b[1:])


def mobius(n: int) -> int:
    n = integer(n, 1, MAX_ORDER)
    sign, p = 1, 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
        p += 1
    return -sign if n > 1 else sign


def euler_weights(raw: object) -> tuple[int, ...]:
    b = logarithmic_coefficients(raw)
    result = []
    for m in range(1, len(b) + 1):
        total = sum(mobius(r) * b[m // r - 1] for r in range(1, m + 1) if m % r == 0)
        require(total % m == 0, "integer Euler-transform divisibility")
        result.append(arithmetic(total // m))
    return tuple(result)


def newton_sums(raw: object, order: int) -> tuple[int, ...]:
    h = polynomial(raw)
    integer(order, 0, MAX_ORDER)
    q = len(h) - 1
    sums = [q]
    for m in range(1, order + 1):
        value = sum(
            (-1) ** (j + 1) * h[j] * sums[m - j] for j in range(1, min(q, m - 1) + 1)
        )
        if m <= q:
            value += (-1) ** (m + 1) * m * h[m]
        sums.append(arithmetic(value))
    return tuple(sums[1:])


def _binomial(exponent: int, j: int) -> int:
    if exponent >= 0:
        return comb(exponent, j) if j <= exponent else 0
    return (-1) ** j * comb(-exponent + j - 1, j)


def triangular_weights(raw: object) -> tuple[int, ...]:
    residual = list(series(raw))
    order = len(residual) - 1
    weights = []
    for grade in range(1, order + 1):
        weight = residual[grade]
        weights.append(weight)
        factor = [
            arithmetic((-1) ** j * _binomial(weight, j))
            for j in range(order // grade + 1)
        ]
        updated = residual.copy()
        for i, value in enumerate(residual):
            for j in range(1, (order - i) // grade + 1):
                updated[i + j * grade] = arithmetic(
                    updated[i + j * grade] + value * factor[j]
                )
        residual = updated
        require(residual[grade] == 0, "triangular removal")
    require(residual == [1] + [0] * order, "triangular product reconstruction")
    return tuple(weights)


def chamber(n: int, k: int) -> str:
    parameters(n, k)
    if n == 1 or k == 0:
        return "ZETA"
    if k == 1:
        return "ZETA_POWER"
    if (n, k) == (2, 2):
        return "ZETA4_OVER_ZETA2"
    return "ESTERMANN_NATURAL_BOUNDARY"


def row_control(n: int, k: int, order: int) -> dict:
    parameters(n, k)
    integer(order, 2, MAX_ORDER)
    data = numerator(n, k)
    h, d, q = data["H"], data["denominator_power"], data["degree"]
    f = coefficients(n, k, order)
    require(f == reconstruct_series(h, d, order), "numerator-series reconstruction")
    b = logarithmic_coefficients(f)
    sums = newton_sums(h, order)
    require(
        b == tuple(d + (-1) ** (m + 1) * sums[m - 1] for m in range(1, order + 1)),
        "Newton sums versus logarithmic derivative",
    )
    weights = euler_weights(f)
    require(
        weights == triangular_weights(f), "independent integer grade reconstruction"
    )
    kind = chamber(n, k)
    strengthened_gap = None
    if kind == "ESTERMANN_NATURAL_BOUNDARY":
        strengthened_gap = n**k - d - 2 * q
        require(q >= 2 and strengthened_gap >= 0, "strengthened first coefficient")
        require(h[1] == n**k - d, "first coefficient")
        require(
            (strengthened_gap == 0) == ((n, k) in ((2, 3), (3, 2))),
            "equality cases",
        )
    else:
        wanted = [1 if kind == "ZETA" else n] + [0] * (order - 1)
        if kind == "ZETA4_OVER_ZETA2":
            wanted = [4, -1] + [0] * (order - 2)
            require(
                f
                == tuple(
                    comb(m + 3, 3) - (comb(m + 1, 3) if m >= 2 else 0)
                    for m in range(order + 1)
                ),
                "rank-two-square rational identity",
            )
        require(weights == tuple(wanted), "constructive exception grades")
    return {
        "n": n,
        "k": k,
        **data,
        "coefficients": f,
        "logarithmic_coefficients": b,
        "reciprocal_root_power_sums": sums,
        "formal_graded_dimensions": weights,
        "analytic_route_by_written_theorem": kind,
        "h1_minus_2q": strengthened_gap,
        "finite_gamma_same_center_completion_for_unmodified_D": kind
        in ("ZETA", "ZETA_POWER"),
    }


def centered_grade(grade: int) -> dict:
    grade = integer(grade, 1, MAX_ORDER)
    shift = Q(1 - grade, 2)
    require(grade + 2 * shift == 1, "affine reflection covariance")
    return {
        "grade": grade,
        "argument_shift": str(shift),
        "local_prime_weight_exponent": str(-shift),
        "affine_reflection_identity": True,
    }


def halving_forest(raw: object) -> list[dict]:
    require(type(raw) in (tuple, list), "synthetic point list required")
    require(1 <= len(raw) <= MAX_POINTS, "synthetic point cap")
    points = []
    for point in raw:
        require(type(point) in (tuple, list) and len(point) == 2, "point shape")
        x, y = rational(point[0]), rational(point[1])
        require(0 < x < 1 and y != 0, "synthetic point outside open strip")
        points.append((x, y))
    lookup = set(points)
    require(len(lookup) == len(points), "duplicate synthetic point")
    result = []
    for point in sorted(points):
        terminal, depth = point, 0
        while (terminal[0] / 2, terminal[1] / 2) in lookup:
            terminal = (terminal[0] / 2, terminal[1] / 2)
            depth += 1
            require(depth < len(points), "halving cycle")
        require(
            point == (2**depth * terminal[0], 2**depth * terminal[1]),
            "halving reconstruction",
        )
        require(2**depth * terminal[0] < 1, "finite ascending-chain strip bound")
        result.append(
            {
                "point": [str(x) for x in point],
                "terminal": [str(x) for x in terminal],
                "depth": depth,
            }
        )
    return result


def pole_order(denominator_multiplicity: int, numerator_multiplicity: int) -> int:
    integer(denominator_multiplicity, 1, 32)
    integer(numerator_multiplicity, 0, 32)
    return denominator_multiplicity - 4 * numerator_multiplicity


def expected_manifest() -> dict:
    return {
        "schema": "graded-parent-global-boundary-sources-v1",
        "source_commit": SOURCE,
        "parent_sources": [
            {"path": path, "git_blob": blob, "sha256_lf": sha, "role": role}
            for path, blob, sha, role in SOURCE_ROWS
        ],
        "external": [
            {
                "id": "ESTERMANN",
                "url": "https://www.numdam.org/item/10.24033/bsmf.2647.pdf",
                "locator": "Delabarre (2013), section 1.2, printed p.227, one-variable theorem",
                "role": "imported meromorphic continuation and every-point natural boundary theorem",
            },
            {
                "id": "DAHLQUIST",
                "url": "https://doi.org/10.1007/BF02591361",
                "locator": "section 1.2 p.534 and Lemma 2.1 pp.536-537",
                "role": "prior-art comparison; unmodified zeta-product warning and small-prime separation",
            },
            {
                "id": "ZETA_AND_GAMMA",
                "urls": [
                    "https://dlmf.nist.gov/25.10",
                    "https://dlmf.nist.gov/25.6.E1",
                    "https://dlmf.nist.gov/25.2",
                    "https://dlmf.nist.gov/25.4",
                    "https://dlmf.nist.gov/5.2",
                ],
                "role": "standard zeta zero, pole, reflection and gamma divisor facts",
            },
        ],
        "external_theorems_machine_proved": False,
    }


def source_locks() -> dict:
    same_json(strict_json(bounded_bytes(MANIFEST)), expected_manifest())

    def git(*args: str) -> bytes:
        return subprocess.run(
            ["git", *args], cwd=ROOT, capture_output=True, check=True, timeout=10
        ).stdout

    for path, blob, sha, _ in SOURCE_ROWS:
        address = f"{SOURCE}:{path}"
        require(git("rev-parse", address).decode().strip() == blob, "source Git blob")
        size = git("cat-file", "-s", address).decode().strip()
        require(size.isdecimal() and int(size) <= MAX_BYTES, "source Git byte cap")
        raw = git("show", address)
        require(len(raw) <= MAX_BYTES and digest(raw) == sha, "source frozen digest")
        require(digest(bounded_bytes(ROOT / path)) == sha, "source current digest")
    return {
        "authenticated_parent_files": len(SOURCE_ROWS),
        "manifest_sha256_lf": digest(bounded_bytes(MANIFEST)),
        "external_theorems_machine_proved": False,
    }


def build_report(
    n_max: int = 5, k_max: int = 5, order: int = DEFAULT_ORDER, cap: int = WORK_CAP
) -> dict:
    score = preflight(n_max, k_max, order, cap)
    locks = source_locks()
    rows = [
        row_control(n, k, order) for n in range(1, n_max + 1) for k in range(k_max + 1)
    ]
    quadratic = row_control(2, 3, order)
    require(quadratic["H"] == (1, 4, 1), "quadratic numerator control")
    # A=2+sqrt(3); 1<sqrt(3)<2 gives 3<A<4, and 3^2>8.
    center = Q(quadratic["H"][1], 2)
    squared_radius = center**2 - quadratic["H"][2]
    require(
        1 < squared_radius < 4 and (center + 1) ** 2 > 8,
        "symbolic algebraic threshold control",
    )
    report = {
        "schema": "graded-parent-global-boundary-controls-v1",
        "arithmetic": {
            "class": "MIXED",
            "components": ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
            "rounding": "none; algebraic roots, prime weights and logarithms remain symbolic",
        },
        "coverage": {
            "n_inclusive": [1, n_max],
            "k_inclusive": [0, k_max],
            "grade_inclusive": [1, order],
            "complete_rows": len(rows),
            "natural_boundary_rows_by_written_theorem": sum(
                row["analytic_route_by_written_theorem"] == "ESTERMANN_NATURAL_BOUNDARY"
                for row in rows
            ),
            "actual_zeta_zero_samples": 0,
            "floating_root_or_log_evaluations": 0,
        },
        "caps": {
            "max_n": MAX_N,
            "max_k": MAX_K,
            "max_order": MAX_ORDER,
            "input_bits": MAX_INPUT_BITS,
            "arithmetic_bits": MAX_ARITH_BITS,
            "max_bytes": MAX_BYTES,
            "work_budget_score": score,
            "work_cap_exclusive": cap,
        },
        "source_authentication": locks,
        "artifact_sha256_lf": {
            path.relative_to(ROOT).as_posix(): digest(bounded_bytes(path))
            for path in (NOTE, SCRIPT, TEST, MANIFEST)
        },
        "rows": rows,
        "quadratic_control": {
            "H": [1, 4, 1],
            "largest_reciprocal_root": "2+sqrt(3)",
            "exact_bounds": "sqrt(8)<A<4",
            "graded_log_at_sigma_3_over_2": "term test fails by written theorem",
            "graded_log_at_sigma_2": "absolutely convergent by written theorem",
            "real_endpoint": "conditionally convergent, not absolutely",
            "dimensions": quadratic["formal_graded_dimensions"],
        },
        "centered_grade_controls": [centered_grade(d) for d in range(1, order + 1)],
        "centered_square_coefficient": {
            "unmodified_p_squared": 9,
            "modified_polynomial_in_sqrt_p": [10, -1],
            "ordinary_same_center_FE": "written meromorphic identity for a changed object",
            "Ramanujan_coefficient_bound": "fails for every 0<epsilon<1/4 by written proof",
        },
        "synthetic_halving_forest": halving_forest(
            (
                (Q(1, 8), 1),
                (Q(1, 4), 2),
                (Q(1, 2), 4),
                (Q(1, 5), 3),
                (Q(2, 5), 6),
                (Q(4, 5), 12),
                (Q(1, 2), 7),
            )
        ),
        "synthetic_pole_orders": [
            {
                "denominator": den,
                "numerator": num,
                "pole_order_signed": pole_order(den, num),
            }
            for den, num in ((1, 0), (1, 1), (4, 1), (5, 1), (7, 0))
        ],
        "scope": {
            "infinite_analysis_machine_verified": False,
            "zero_free_on_all_Re_greater_than_one": False,
            "D22_arbitrary_meromorphic_multiplier_no_rescue": False,
            "centered_variant_is_the_original_D22": False,
            "positive_virtual_dimension_implies_effective_representation": False,
            "novelty_automorphy_or_RH_claim": False,
        },
    }
    report["payload_sha256"] = hashlib.sha256(canonical(report)).hexdigest()
    require(len(render(report).encode()) <= MAX_BYTES, "report byte cap")
    return report


def check_fixture() -> dict:
    expected = build_report()
    same_json(strict_json(bounded_bytes(FIXTURE)), expected)
    return {"status": "PASS", "payload_sha256": expected["payload_sha256"]}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true")
    group.add_argument("--emit-report", action="store_true")
    group.add_argument("--emit-manifest", action="store_true")
    args = parser.parse_args()
    if args.emit_manifest:
        value = expected_manifest()
    elif args.emit_report:
        value = build_report()
    else:
        value = check_fixture()
    print(render(value), end="")


if __name__ == "__main__":
    main()
