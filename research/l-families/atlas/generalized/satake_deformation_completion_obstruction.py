"""Exact bounded controls, not a machine proof of Delta's Sato--Tate theorem."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from fractions import Fraction
from math import comb, factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SCRIPT = Path(__file__).resolve()
NOTE = HERE / "SATAKE_DEFORMATION_COMPLETION_OBSTRUCTION.md"
FIXTURE = HERE / "satake_deformation_completion_obstruction.json"
MANIFEST = HERE / "satake_deformation_completion_obstruction.sources.json"
TEST = ROOT / "tests/test_satake_deformation_completion_obstruction.py"
SOURCE_COMMIT = "e2f469142cd55086e74751293877ab533001e786"
CONTEXT_PATH = (
    "research/l-families/atlas/generalized/"
    "FINITE_GRADED_VIRTUAL_PARENT_CLASSIFICATION.md"
)
CONTEXT_BLOB = "3932273279d43ffa34d929247152cb43b932fa1d"
CONTEXT_HASH = "50daa223c5b6d0f061d771f24775a0a7a2d470f9185a1d6304f3b49e9fc799bc"
MAX_ORDER = 24
MAX_FREQUENCY = 6
MAX_PHASE = 72
MAX_INPUT_BITS = 128
MAX_BYTES = 262144
WORK_CAP = 2_000_000
DEFAULT_ORDER = 12
Q = Fraction


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def integer(value: object, name: str, low: int, high: int) -> int:
    require(type(value) is int and low <= value <= high, f"invalid {name}")
    return value


def rational(value: object) -> Fraction:
    require(type(value) in (int, Fraction), "exact rational required")
    result = Q(value)
    require(
        max(result.numerator.bit_length(), result.denominator.bit_length())
        <= MAX_INPUT_BITS,
        "rational input bit cap exceeded",
    )
    return result


def qjson(value: Fraction | int) -> list[int]:
    value = Q(value)
    return [value.numerator, value.denominator]


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


def bounded_bytes(path: Path) -> bytes:
    require(path.stat().st_size <= MAX_BYTES, "file byte cap exceeded")
    raw = path.read_bytes()
    require(len(raw) <= MAX_BYTES, "file byte cap exceeded")
    return raw


def _pairs_no_duplicates(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        require(key not in result, "duplicate JSON key")
        result[key] = value
    return result


def _reject_constant(value: str) -> None:
    raise ValueError(f"nonfinite JSON constant: {value}")


def strict_json(raw: bytes) -> object:
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "JSON byte cap/type")
    return json.loads(
        raw,
        object_pairs_hook=_pairs_no_duplicates,
        parse_constant=_reject_constant,
    )


def work_bound(order: int) -> int:
    integer(order, "order", 2, MAX_ORDER)
    return 10_000 + 100 * (order + 1) ** 3


def preflight(order: int, cap: int = WORK_CAP) -> int:
    integer(cap, "work cap", 1, WORK_CAP)
    bound = work_bound(order)
    require(bound < cap, "work bound must be strictly below cap")
    return bound


def _add(*polys: dict[int, Fraction]) -> dict[int, Fraction]:
    result = {}
    for poly in polys:
        for power, value in poly.items():
            result[power] = result.get(power, Q(0)) + value
    return {power: value for power, value in result.items() if value}


def _mul(a: dict[int, Fraction], b: dict[int, Fraction]) -> dict[int, Fraction]:
    result = {}
    for j, x in a.items():
        for k, y in b.items():
            result[j + k] = result.get(j + k, Q(0)) + x * y
    return {power: value for power, value in result.items() if value}


def _scale(poly: dict[int, Fraction], scalar: Fraction) -> dict[int, Fraction]:
    return {power: scalar * value for power, value in poly.items() if scalar * value}


def exponential_coefficients(frequency: int, order: int) -> list[dict[int, Fraction]]:
    """Coefficients of exp(epsilon*(z^f-z^-f)/2); finite formal algebra only."""
    integer(frequency, "frequency", 1, MAX_FREQUENCY)
    preflight(order)
    generator = {frequency: Q(1, 2), -frequency: Q(-1, 2)}
    result = [{0: Q(1)}]
    for degree in range(1, order + 1):
        result.append(_scale(_mul(result[-1], generator), Q(1, degree)))
    return result


def phase_constant_terms(frequency: int, phase: int, order: int) -> list[Fraction]:
    integer(phase, "phase", -MAX_PHASE, MAX_PHASE)
    return [row.get(-phase, Q(0)) for row in exponential_coefficients(frequency, order)]


def cube_root_sum(phase: int) -> tuple[int, int]:
    """Return 1+w^phase+w^(2phase), reduced in Z[w]/(w^2+w+1)."""
    integer(phase, "phase", -MAX_PHASE, MAX_PHASE)
    powers = ((1, 0), (0, 1), (-1, -1))
    return tuple(sum(powers[(j * phase) % 3][k] for j in range(3)) for k in range(2))


def mean_coefficients(order: int) -> list[Fraction]:
    exponent = exponential_coefficients(3, order)
    weight = {0: Q(1), 1: Q(-1, 2), -1: Q(-1, 2)}
    result = []
    for degree, row in enumerate(exponent):
        trace = _add(
            {0: Q(1)} if degree == 0 else {},
            _mul({1: Q(1)}, row),
            _mul({-1: Q((-1) ** degree)}, row),
        )
        result.append(_mul(weight, trace).get(0, Q(0)))
    return result


def mean_coefficient_formula(degree: int) -> Fraction:
    integer(degree, "degree", 0, MAX_ORDER)
    if degree == 0 or degree % 2:
        return Q(0)
    j = degree // 2
    return Q((-1) ** (j + 1), 4**j * factorial(j) ** 2)


def sine_even_moment(frequency: int, half_degree: int) -> Fraction:
    integer(frequency, "frequency", 1, MAX_FREQUENCY)
    integer(half_degree, "half degree", 0, MAX_ORDER // 2)
    power = {0: Q(1)}
    for _ in range(2 * half_degree):
        power = _mul(power, {frequency: Q(1), -frequency: Q(-1)})
    return power.get(0, Q(0)) * Q((-1) ** half_degree, 4**half_degree)


def mean_bounds(epsilon: Fraction | int) -> dict:
    epsilon = rational(epsilon)
    require(abs(epsilon) <= 1, "epsilon outside proved chamber")
    lower = epsilon**2 / 4 - epsilon**4 / 64
    upper = epsilon**2 / 4
    if epsilon:
        require(0 < lower <= upper < 1, "noninteger-order interval failed")
    else:
        require(lower == upper == 0, "zero control failed")
    return {
        "epsilon": qjson(epsilon),
        "lower": qjson(lower),
        "upper": qjson(upper),
        "noninteger_order_obstruction": bool(epsilon),
    }


def _matrix(value: object) -> tuple[tuple[Fraction, ...], ...]:
    require(type(value) is tuple and len(value) == 3, "3x3 tuple matrix required")
    for row in value:
        require(type(row) is tuple and len(row) == 3, "3x3 tuple matrix required")
    return tuple(tuple(rational(x) for x in row) for row in value)


def _transpose(a: tuple) -> tuple:
    return tuple(tuple(a[j][i] for j in range(3)) for i in range(3))


def _matmul(a: tuple, b: tuple) -> tuple:
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )


def _matscale(a: tuple, scalar: Fraction) -> tuple:
    return tuple(tuple(scalar * x for x in row) for row in a)


def _matsub(a: tuple, b: tuple) -> tuple:
    return tuple(tuple(a[i][j] - b[i][j] for j in range(3)) for i in range(3))


def _trace(a: tuple) -> Fraction:
    return sum(a[j][j] for j in range(3))


def _det(a: tuple) -> Fraction:
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def _inverse(a: tuple) -> tuple:
    det = _det(a)
    require(det != 0, "singular matrix")
    cofactors = []
    for i in range(3):
        row = []
        for j in range(3):
            minor = [[a[r][c] for c in range(3) if c != j] for r in range(3) if r != i]
            row.append(
                Q((-1) ** (i + j))
                * (minor[0][0] * minor[1][1] - minor[0][1] * minor[1][0])
                / det
            )
        cofactors.append(tuple(row))
    return _transpose(tuple(cofactors))


def matrix_generator(value: object) -> tuple:
    a = _matrix(value)
    inverse = _inverse(a)
    return _matscale(
        _matsub(_matmul(_matmul(a, a), a), _matmul(_matmul(inverse, inverse), inverse)),
        Q(1, 2),
    )


def _rotation(c: Fraction | int, s: Fraction | int) -> tuple:
    c, s = rational(c), rational(s)
    require(c * c + s * s == 1, "nonunit circle pair")
    return ((c, -s, Q(0)), (s, c, Q(0)), (Q(0), Q(0), Q(1)))


def matrix_controls() -> dict:
    identity = ((Q(1), Q(0), Q(0)), (Q(0), Q(1), Q(0)), (Q(0), Q(0), Q(1)))
    zero = _matscale(identity, Q(0))
    conjugator = (
        (Q(3, 5), Q(0), Q(-4, 5)),
        (Q(0), Q(1), Q(0)),
        (Q(4, 5), Q(0), Q(3, 5)),
    )
    rows = []
    for c, s in (
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (Q(3, 5), Q(4, 5)),
        (Q(-5, 13), Q(12, 13)),
    ):
        a = _rotation(c, s)
        g = matrix_generator(a)
        conjugate = _matmul(_matmul(conjugator, a), _transpose(conjugator))
        require(_det(a) == 1 and _matmul(a, _transpose(a)) == identity, "SO3 control")
        require(_matsub(_transpose(g), _matscale(g, Q(-1))) == zero, "skew generator")
        require(_trace(g) == 0 and _matmul(a, g) == _matmul(g, a), "trace/commutator")
        require(
            matrix_generator(_transpose(a)) == _matscale(g, Q(-1)), "inverse generator"
        )
        require(
            matrix_generator(conjugate)
            == _matmul(_matmul(conjugator, g), _transpose(conjugator)),
            "conjugation generator",
        )
        rows.append(
            {
                "c": qjson(c),
                "s": qjson(s),
                "generator": [[qjson(x) for x in row] for row in g],
            }
        )
    bad = ((Q(2), Q(0), Q(0)), (Q(0), Q(3), Q(0)), (Q(0), Q(0), Q(1, 6)))
    bad_trace = _trace(matrix_generator(bad))
    require(_det(bad) == 1 and bad_trace != 0, "generic SL3 negative control")
    return {"so3_controls": rows, "generic_sl3_generator_trace": qjson(bad_trace)}


def local_control(c: Fraction | int, order: int) -> dict:
    c = rational(c)
    require(-1 <= c <= 1, "cosine outside unitary interval")
    preflight(order)
    t = 1 + 2 * c
    coefficients = [Q(1)]
    for n in range(1, order + 1):
        coefficients.append(
            t * coefficients[n - 1]
            - (t * coefficients[n - 2] if n >= 2 else 0)
            + (coefficients[n - 3] if n >= 3 else 0)
        )
    quadratic = [Q(1), 2 * c]
    for n in range(2, order + 1):
        quadratic.append(2 * c * quadratic[-1] - quadratic[-2])
    require(
        coefficients == [sum(quadratic[: n + 1]) for n in range(order + 1)],
        "independent factor convolution",
    )
    require(
        all(abs(value) <= comb(n + 2, 2) for n, value in enumerate(coefficients)),
        "local coefficient majorant",
    )
    evaluations = []
    for x in (Q(1, 2), Q(1, 3), Q(2, 5)):
        denominator = 1 - t * x + t * x**2 - x**3
        factored = (1 - x) * ((1 - x) ** 2 + 2 * (1 - c) * x)
        require(denominator == factored > 0, "real local positivity")
        evaluations.append({"x": qjson(x), "denominator": qjson(denominator)})
    return {
        "c": qjson(c),
        "denominator": [qjson(x) for x in (1, -t, t, -1)],
        "coefficients": [qjson(x) for x in coefficients],
        "positive_evaluations": evaluations,
    }


def expected_manifest() -> dict:
    return {
        "schema": "satake-deformation-completion-sources-v1",
        "repository_context": {
            "role": "context-only-not-a-mathematical-premise",
            "commit": SOURCE_COMMIT,
            "path": CONTEXT_PATH,
            "git_blob": CONTEXT_BLOB,
            "sha256_lf": CONTEXT_HASH,
        },
        "external_theorems": [
            {
                "id": "D1",
                "author": "Pierre Deligne",
                "title": "La conjecture de Weil : I",
                "year": 1974,
                "doi": "10.1007/BF02684373",
                "locator": "Theorem (8.2), printed p.302, PDF page 31",
                "url": "https://www.numdam.org/article/PMIHES_1974__43__273_0.pdf",
                "import": "absolute values of normalized Delta prime parameters are one",
            },
            {
                "id": "D2",
                "author": "Tom Barnet-Lamb; David Geraghty; Michael Harris; Richard Taylor",
                "title": "A Family of Calabi-Yau Varieties and Potential Automorphy II",
                "year": 2011,
                "doi": "10.2977/PRIMS/31",
                "locator": "Corollary C, printed p.32, PDF page 4",
                "url": "https://ems.press/content/serial-article-files/41128?nt=1",
                "import": "qualitative semicircle equidistribution of tau(p)/(2 p^(11/2)) over all primes",
            },
        ],
        "external_authentication": "declarations pinned; external PDFs and their theorems are not machine-replayed",
    }


def source_locks() -> dict:
    manifest = strict_json(bounded_bytes(MANIFEST))
    same_json(manifest, expected_manifest())
    address = f"{SOURCE_COMMIT}:{CONTEXT_PATH}"

    def git(*args: str) -> bytes:
        result = subprocess.run(
            ["git", *args], cwd=ROOT, capture_output=True, check=True, timeout=10
        )
        return result.stdout

    require(
        git("rev-parse", address).decode().strip() == CONTEXT_BLOB,
        "context blob identity mismatch",
    )
    size_text = git("cat-file", "-s", address).decode().strip()
    require(
        size_text.isdecimal() and int(size_text) <= MAX_BYTES, "context Git byte cap"
    )
    raw = git("show", address)
    require(
        len(raw) <= MAX_BYTES and digest(raw) == CONTEXT_HASH,
        "frozen context digest mismatch",
    )
    require(
        digest(bounded_bytes(ROOT / CONTEXT_PATH)) == CONTEXT_HASH,
        "current context digest mismatch",
    )
    return {
        "context_authenticated": True,
        "external_theorems_machine_proved": False,
        "manifest_sha256_lf": digest(bounded_bytes(MANIFEST)),
    }


def build_report(order: int = DEFAULT_ORDER, cap: int = WORK_CAP) -> dict:
    bound = preflight(order, cap)
    sources = source_locks()
    coefficients = mean_coefficients(order)
    formula = [mean_coefficient_formula(degree) for degree in range(order + 1)]
    require(coefficients == formula, "mean formula replay failed")
    phase_rows = []
    for phase in (1, 2):
        values = phase_constant_terms(3, phase, order)
        require(all(value == 0 for value in values), "frequency-three cancellation")
        require(cube_root_sum(phase) == (0, 0), "cube-root cancellation")
        phase_rows.append(
            {
                "frequency": 3,
                "phase": phase,
                "constant_terms": [qjson(x) for x in values],
            }
        )
    negatives = []
    for frequency, phase in ((1, 1), (2, 2), (3, 3)):
        first = phase_constant_terms(frequency, phase, order)[1]
        require(first == Q(-1, 2), "wrong-frequency/divisible-mode negative control")
        negatives.append(
            {"frequency": frequency, "phase": phase, "linear_coefficient": qjson(first)}
        )
    moments = []
    for j in range(order // 2 + 1):
        value = sine_even_moment(3, j)
        require(value == Q(comb(2 * j, j), 4**j), "independent sine moment formula")
        moments.append(qjson(value))
    require(moments[1] == [1, 2], "quadratic moment")
    if order >= 4:
        require(moments[2] == [3, 8], "quartic moment")
    bounds = [
        mean_bounds(x)
        for x in (0, 1, -1, Q(1, 2), Q(-1, 2), Q(1, 3), Q(-1, 3), Q(2, 5), Q(-2, 5))
    ]
    artifacts = {
        str(path.relative_to(ROOT)).replace("\\", "/"): digest(bounded_bytes(path))
        for path in (NOTE, SCRIPT, TEST, MANIFEST)
    }
    report = {
        "schema": "satake-deformation-completion-controls-v1",
        "claim": "GLO764.SATAKE_FIXED_PARAMETER_NONMEROMORPHY_V1",
        "scope": "bounded exact synthetic controls; infinite theorem is written proof using imported D1/D2",
        "arithmetic": {
            "class": "MIXED",
            "components": ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
            "rounding": "none",
        },
        "coverage": {
            "formal_degrees_inclusive": [0, order],
            "sine_half_degrees_inclusive": [0, order // 2],
            "epsilon_controls": 9,
            "local_cosine_controls": 7,
            "so3_controls": 6,
            "actual_delta_prime_samples": 0,
        },
        "resources": {
            "max_order": MAX_ORDER,
            "max_input_bits": MAX_INPUT_BITS,
            "max_bytes": MAX_BYTES,
            "work_majorant": bound,
            "work_cap_exclusive": cap,
        },
        "sources": sources,
        "artifact_sha256_lf": artifacts,
        "phase_cancellations": phase_rows,
        "negative_frequency_controls": negatives,
        "mean_coefficients": [qjson(x) for x in coefficients],
        "sine_even_moments": moments,
        "epsilon_bound_controls": bounds,
        "matrix_controls": matrix_controls(),
        "local_controls": [
            local_control(c, order)
            for c in (-1, Q(-5, 13), Q(-1, 2), 0, Q(1, 3), Q(3, 5), 1)
        ],
        "verdict": "EXACT_BOUNDED_CONTROLS_PASS_NOT_A_MACHINE_PROOF_OF_THE_GLOBAL_THEOREM",
    }
    report["payload_sha256"] = hashlib.sha256(canonical(report)).hexdigest()
    require(len(render(report).encode()) <= MAX_BYTES, "report byte cap")
    return report


def check_fixture() -> dict:
    actual = strict_json(bounded_bytes(FIXTURE))
    expected = build_report()
    same_json(actual, expected)
    return {
        "status": "PASS",
        "payload_sha256": expected["payload_sha256"],
        "external_theorems_machine_proved": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--check", action="store_true")
    group.add_argument(
        "--write", action="store_true", help="regenerate only the fixed fixture"
    )
    args = parser.parse_args()
    if args.check:
        result = check_fixture()
    elif args.write:
        report = build_report()
        FIXTURE.write_text(render(report), encoding="utf-8", newline="\n")
        result = {
            "status": "FIXTURE_WRITTEN",
            "payload_sha256": report["payload_sha256"],
        }
    else:
        result = build_report()
    print(render(result), end="")


if __name__ == "__main__":
    main()
