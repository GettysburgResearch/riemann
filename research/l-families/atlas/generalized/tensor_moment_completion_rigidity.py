"""Bounded exact tensor-moment controls; not a machine proof of meromorphy."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from fractions import Fraction
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SCRIPT = Path(__file__).resolve()
NOTE = HERE / "TENSOR_MOMENT_COMPLETION_RIGIDITY.md"
MANIFEST = HERE / "tensor_moment_completion_rigidity.sources.json"
FIXTURE = HERE / "tensor_moment_completion_rigidity.json"
TEST = ROOT / "tests/test_tensor_moment_completion_rigidity.py"
SOURCE_COMMIT = "b895598abd936a2e42e5b7d14a7e10cc2bf41486"
SOURCE_ROWS = (
    (
        "research/l-families/atlas/generalized/SATAKE_DEFORMATION_COMPLETION_OBSTRUCTION.md",
        "907bb4c262939d4f812b282f155857218a97b2e5",
        "131ce880eedd4da62e3f46884529a759e8842a0e556c1f7be26d8565e47201c2",
        "mathematical-parent-D1-D2-Abel-and-integer-log-order",
    ),
    (
        "research/l-families/atlas/generalized/satake_deformation_completion_obstruction.py",
        "e3131456ec7d0f1678645ecfca0c8723ce66dabd",
        "0b17d9c83d70a4f7122274ae172ba808b32cc8cd9e2f59060d21510131e5b094",
        "parent-control-context-not-imported-by-this-producer",
    ),
    (
        "research/l-families/atlas/generalized/satake_deformation_completion_obstruction.sources.json",
        "c50b8eb8f4ea13e232f63bebd034a63ddcf110d7",
        "3b4f77c8e493e4f958bcf4bf7f3c1ff9d9fcb0d34fb4ac56066ed26893bd2c7f",
        "parent-arithmetic-source-declarations",
    ),
)
MAX_J = 12
MAX_M = 24
MAX_INPUT_BITS = 128
MAX_BYTES = 262144
WORK_CAP = 500_000
DEFAULT_J = 8
DEFAULT_M = 12
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
        "rational input bit cap",
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
        raw, object_pairs_hook=_pairs_no_duplicates, parse_constant=_reject_constant
    )


def work_score(j_max: int, m_max: int) -> int:
    integer(j_max, "maximum perturbation degree", 1, MAX_J)
    integer(m_max, "maximum moment", 2, MAX_M)
    require(j_max <= m_max, "moment range must include every first-failure degree")
    return 10_000 + 40 * (j_max + 1) * (m_max + 1) ** 2


def preflight(j_max: int, m_max: int, cap: int = WORK_CAP) -> int:
    integer(cap, "work cap", 1, WORK_CAP)
    score = work_score(j_max, m_max)
    require(score < cap, "work score must be strictly below cap")
    return score


def _mul(a: dict, b: dict) -> dict:
    result = {}
    for j, x in a.items():
        for k, y in b.items():
            result[j + k] = result.get(j + k, 0) + x * y
    return {power: value for power, value in result.items() if value}


def _add(a: dict, b: dict) -> dict:
    result = dict(a)
    for power, value in b.items():
        result[power] = result.get(power, 0) + value
    return {power: value for power, value in result.items() if value}


def _scale(a: dict, scalar: Fraction | int) -> dict:
    return {power: scalar * value for power, value in a.items() if scalar * value}


def tensor_weights(m: int) -> dict[int, int]:
    """Weights of (1+z+z^-1)^m, using direct convolution, not trinomial sums."""
    integer(m, "tensor degree", 0, MAX_M)
    weights = {0: 1}
    for _ in range(m):
        weights = _mul(weights, {-1: 1, 0: 1, 1: 1})
    require(
        all(type(x) is int and x >= 0 for x in weights.values()),
        "noninteger tensor multiplicity",
    )
    require(sum(weights.values()) == 3**m, "tensor dimension")
    require(
        all(weights.get(-k) == value for k, value in weights.items()),
        "inverse-pair multiplicities",
    )
    require(sum(k * value for k, value in weights.items()) == 0, "determinant weight")
    return weights


def trinomial_coefficient(m: int, k: int) -> int:
    integer(m, "tensor degree", 0, MAX_M)
    integer(k, "weight index", -MAX_M - 1, MAX_M + 1)
    k = abs(k)
    if k > m:
        return 0
    return sum(comb(m, r) * comb(m - r, r + k) for r in range((m - k) // 2 + 1))


def baseline_moment(m: int) -> int:
    row = tensor_weights(m)
    return row.get(0, 0) - row.get(1, 0)


def dirichlet_kernel(j: int) -> dict[int, int]:
    integer(j, "perturbation degree", 1, MAX_J)
    return dict.fromkeys(range(-j, j + 1), 1)


def density_laurent(j: int) -> dict[int, Fraction]:
    return _mul({0: Q(1), -1: Q(-1, 2), 1: Q(-1, 2)}, dirichlet_kernel(j))


def perturbation_shift(j: int, m: int) -> int:
    integer(j, "perturbation degree", 1, MAX_J)
    row = tensor_weights(m)
    value = Q(_mul(row, density_laurent(j)).get(0, 0))
    require(value.denominator == 1, "moment shift must be integral")
    return value.numerator


def closed_shift(j: int, m: int) -> int:
    integer(j, "perturbation degree", 1, MAX_J)
    return trinomial_coefficient(m, j) - trinomial_coefficient(m, j + 1)


def kernel_trace_polynomial(j: int) -> dict[int, int]:
    """q_0=1, q_1=t, q_(j+1)=(t-1)q_j-q_(j-1)."""
    integer(j, "kernel degree", 0, MAX_J)
    if j == 0:
        return {0: 1}
    previous, current = {0: 1}, {1: 1}
    for _ in range(1, j):
        previous, current = (
            current,
            _add(_mul({1: 1, 0: -1}, current), _scale(previous, -1)),
        )
    return current


def _substitute_trace(poly: dict[int, int]) -> dict:
    result = {}
    powers = {0: 1}
    for degree in range(max(poly) + 1):
        result = _add(result, _scale(powers, poly.get(degree, 0)))
        powers = _mul(powers, {-1: 1, 0: 1, 1: 1})
    return result


def cdf_perturbation(j: int) -> dict:
    integer(j, "perturbation degree", 1, MAX_J)
    # Coefficients of pi*(F_epsilon,j-F)/epsilon in the sine basis.
    sine = {j: Q(1, j), j + 1: Q(-1, j + 1)}
    derivative = {}
    for frequency, coefficient in sine.items():
        derivative[frequency] = coefficient * frequency / 2
        derivative[-frequency] = coefficient * frequency / 2
    require(derivative == density_laurent(j), "CDF derivative/telescoping mismatch")
    require(derivative.get(0, 0) == 0, "perturbation mass")
    return {
        "sine_coefficients": [[k, *qjson(value)] for k, value in sine.items()],
        "derivative_laurent": [[k, *qjson(derivative[k])] for k in sorted(derivative)],
        "integer_frequency_endpoint_sines_zero": True,
    }


def admissible_epsilon(j: int, epsilon: object) -> Fraction:
    integer(j, "perturbation degree", 1, MAX_J)
    epsilon = rational(epsilon)
    require(
        abs(epsilon) < Q(1, 2 * j + 1),
        "epsilon outside strict positive-density chamber",
    )
    return epsilon


def perturbed_moment(j: int, m: int, epsilon: object) -> Fraction:
    epsilon = admissible_epsilon(j, epsilon)
    return Q(baseline_moment(m)) + epsilon * perturbation_shift(j, m)


def density_control(j: int, epsilon: object) -> dict:
    epsilon = admissible_epsilon(j, epsilon)
    norm = sum(abs(value) for value in dirichlet_kernel(j).values())
    require(norm == 2 * j + 1, "Dirichlet kernel triangle bound")
    margin = 1 - abs(epsilon) * norm
    require(margin > 0, "strict positivity margin")
    lower = [perturbed_moment(j, m, epsilon) for m in range(j)]
    require(
        lower == [Q(baseline_moment(m)) for m in range(j)],
        "lower moments not preserved",
    )
    failure = perturbed_moment(j, j, epsilon)
    require(failure == baseline_moment(j) + epsilon, "first-failure moment")
    require((failure.denominator != 1) == bool(epsilon), "noninteger order control")
    return {
        "j": j,
        "epsilon": qjson(epsilon),
        "density_margin_lower_bound": qjson(margin),
        "preserved_moments": [qjson(x) for x in lower],
        "jth_moment": qjson(failure),
        "jth_nonmeromorphy_obstruction": bool(epsilon),
        "lower_euler_meromorphy_proved": False,
    }


def expected_manifest() -> dict:
    return {
        "schema": "tensor-moment-completion-sources-v1",
        "parent_sources": [
            {
                "commit": SOURCE_COMMIT,
                "path": path,
                "git_blob": blob,
                "sha256_lf": sha,
                "role": role,
            }
            for path, blob, sha, role in SOURCE_ROWS
        ],
        "prior_art": [
            {
                "id": "LARSEN2002",
                "author": "Michael Larsen",
                "title": "Rigidity in the Invariant Theory of Compact Groups",
                "url": "https://arxiv.org/pdf/math/0212193",
                "version": "arXiv:math/0212193v1, 15 December 2002",
                "locator": "Introduction and Theorem 3.3 (PDF p.8)",
                "role": "prior-art-only; compact-group trace moments and isolation, not imported as a proof",
            },
            {
                "id": "LARSEN_PINK",
                "author": "Michael Larsen; Richard Pink",
                "title": "Determining Representations from Invariant Dimensions",
                "url": "https://people.math.ethz.ch/~pink/ftp/LP1.pdf",
                "locator": "Introduction Theorems 1-3 and section 1",
                "role": "prior-art-only; invariant dimensions and reconstruction boundaries",
            },
        ],
        "external_authentication": "declarations pinned; no external PDF or arithmetic theorem is machine-proved",
    }


def source_locks() -> dict:
    same_json(strict_json(bounded_bytes(MANIFEST)), expected_manifest())
    rows = []

    def git(*args: str) -> bytes:
        return subprocess.run(
            ["git", *args], cwd=ROOT, capture_output=True, check=True, timeout=10
        ).stdout

    for path, blob, sha, role in SOURCE_ROWS:
        address = f"{SOURCE_COMMIT}:{path}"
        require(
            git("rev-parse", address).decode().strip() == blob,
            "source Git blob mismatch",
        )
        size = git("cat-file", "-s", address).decode().strip()
        require(size.isdecimal() and int(size) <= MAX_BYTES, "source Git byte cap")
        raw = git("show", address)
        require(
            len(raw) <= MAX_BYTES and digest(raw) == sha,
            "frozen source digest mismatch",
        )
        require(
            digest(bounded_bytes(ROOT / path)) == sha, "current source digest mismatch"
        )
        rows.append({"path": path, "git_blob": blob, "sha256_lf": sha, "role": role})
    return {
        "authenticated_parent_files": rows,
        "external_theorems_machine_proved": False,
        "manifest_sha256_lf": digest(bounded_bytes(MANIFEST)),
    }


def build_report(
    j_max: int = DEFAULT_J, m_max: int = DEFAULT_M, cap: int = WORK_CAP
) -> dict:
    score = preflight(j_max, m_max, cap)
    sources = source_locks()
    tensors = []
    moments = []
    for m in range(m_max + 1):
        row = tensor_weights(m)
        require(
            all(
                row.get(k, 0) == trinomial_coefficient(m, k)
                for k in range(-m - 1, m + 2)
            ),
            "independent trinomial replay",
        )
        baseline = baseline_moment(m)
        require(
            baseline == trinomial_coefficient(m, 0) - trinomial_coefficient(m, 1),
            "baseline moment replay",
        )
        moments.append(baseline)
        tensors.append(
            {"m": m, "dimension": 3**m, "weights": [[k, row[k]] for k in sorted(row)]}
        )
    perturbations = []
    for j in range(1, j_max + 1):
        poly = kernel_trace_polynomial(j)
        require(
            _substitute_trace(poly) == dirichlet_kernel(j),
            "trace polynomial kernel identity",
        )
        shifts = [perturbation_shift(j, m) for m in range(m_max + 1)]
        require(
            shifts == [closed_shift(j, m) for m in range(m_max + 1)],
            "independent perturbation matrix",
        )
        require(shifts[:j] == [0] * j and shifts[j] == 1, "first-failure coverage")
        controls = [
            density_control(j, epsilon)
            for epsilon in (
                Q(0),
                Q(1, 2 * (2 * j + 1)),
                Q(-1, 2 * (2 * j + 1)),
                Q(1, 3 * (2 * j + 1)),
                Q(-1, 3 * (2 * j + 1)),
            )
        ]
        perturbations.append(
            {
                "j": j,
                "trace_polynomial": [[k, poly[k]] for k in sorted(poly)],
                "moment_shifts": shifts,
                "cdf_control": cdf_perturbation(j),
                "density_controls": controls,
            }
        )
    require(kernel_trace_polynomial(2) == {0: -1, 1: -1, 2: 1}, "q2=t^2-t-1")
    artifacts = {
        str(path.relative_to(ROOT)).replace("\\", "/"): digest(bounded_bytes(path))
        for path in (NOTE, SCRIPT, TEST, MANIFEST)
    }
    report = {
        "schema": "tensor-moment-completion-controls-v1",
        "claims": [
            "GLO764.TENSOR_MOMENT_COMPLETION_RIGIDITY_V1",
            "GLO764.FINITE_MOMENT_PRESERVING_DEFORMATION_V1",
        ],
        "scope": "finite algebra only; no machine proof of infinite moment rigidity or Euler meromorphy",
        "arithmetic": {
            "class": "MIXED",
            "components": ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
            "rounding": "none",
        },
        "coverage": {
            "j_inclusive": [1, j_max],
            "m_inclusive": [0, m_max],
            "complete_shift_cells": j_max * (m_max + 1),
            "density_controls_per_j": 5,
            "actual_delta_prime_samples": 0,
            "numerical_inverse_cdf_evaluations": 0,
        },
        "resources": {
            "max_j": MAX_J,
            "max_m": MAX_M,
            "max_input_bits": MAX_INPUT_BITS,
            "max_bytes": MAX_BYTES,
            "work_budget_score": score,
            "work_cap_exclusive": cap,
        },
        "sources": sources,
        "artifact_sha256_lf": artifacts,
        "baseline_moments": moments,
        "tensor_weights": tensors,
        "perturbations": perturbations,
        "verdict": "EXACT_BOUNDED_CONTROLS_PASS_NOT_A_MEROMORPHY_CERTIFICATE",
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
        "--write", action="store_true", help="regenerate only this packet's fixture"
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
