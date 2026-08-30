#!/usr/bin/env python3
"""Exact cyclotomic regression for the positive-real rational-angle theorem."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
from collections.abc import Sequence
from functools import lru_cache
from itertools import pairwise
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[4]
NOTE_PATH = SCRIPT_PATH.with_name("RATIONAL_ROTATION_REAL_POWER_EXACT_DEGREE.md")
SOURCES_PATH = SCRIPT_PATH.with_suffix(".sources.json")
OUTPUT_PATH = SCRIPT_PATH.with_suffix(".json")
TEST_PATH = REPO_ROOT / "tests/test_rational_rotation_real_power_exact_degree.py"
BASE_COMMIT = "3fd6c34d1cd8109eab3622d3966e05a0ad8fc7a4"
EXPECTED_MANIFEST_SHA256_LF = (
    "7dd697d7e59dd5e8f5d96386a03a21066652d537988f9bf4c739bdd324f1e4da"
)
EXPECTED_SOURCE_BLOBS = {
    "research/l-families/atlas/generalized/RATIONAL_ROTATION_UNIFORM_DEGREE_GATE.md": "9548280426316237de50c7e71e2dd704aa68f00b",
    "research/l-families/atlas/generalized/RATIONAL_ROTATION_BRANCH_CENSUS.md": "650933e62d3b467ffc3be0f253c9ac65a0bd2e48",
}
MAX_B = 24
MAX_K = 12
MAX_SIGN_B = 64
WORK_CAP_EXCLUSIVE = 10_000_000
SCHEMA = "riemann.atlas.generalized.rational_rotation_real_power_exact_degree.v1"


def require_int(value: object, name: str, low: int, high: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer, not a coercible value")
    if not low <= value <= high:
        raise ValueError(f"{name} must lie in [{low}, {high}]")
    return value


def lf_bytes(data: bytes) -> bytes:
    return data.replace(b"\r\n", b"\n")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_sha(path: Path) -> str:
    return sha256(lf_bytes(path.read_bytes()))


def canonical_sha(value: object) -> str:
    return sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    )


def relative(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def trim(poly: Sequence[int]) -> tuple[int, ...]:
    result = list(poly)
    while result and result[-1] == 0:
        result.pop()
    return tuple(result)


def divide_monic(
    dividend: Sequence[int], divisor: Sequence[int]
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Integer long division; the caller may require remainder zero."""
    a, b = list(trim(dividend)), trim(divisor)
    if not b or b[-1] != 1:
        raise ValueError("divisor must be a nonzero monic integer polynomial")
    if any(isinstance(x, bool) or not isinstance(x, int) for x in (*a, *b)):
        raise TypeError("polynomial coefficients must be integers")
    if len(a) < len(b):
        return (), tuple(a)
    quotient = [0] * (len(a) - len(b) + 1)
    while a and len(a) >= len(b):
        shift, lead = len(a) - len(b), a[-1]
        quotient[shift] = lead
        for j, coeff in enumerate(b):
            a[shift + j] -= lead * coeff
        while a and a[-1] == 0:
            a.pop()
    return trim(quotient), tuple(a)


@lru_cache(maxsize=4 * MAX_B)
def _cyclotomic(n: int) -> tuple[int, ...]:
    poly: tuple[int, ...] = tuple([-1] + [0] * (n - 1) + [1])
    for d in range(1, n):
        if n % d == 0:
            poly, remainder = divide_monic(poly, _cyclotomic(d))
            if remainder:
                raise ArithmeticError("cyclotomic factorization was not exact")
    return poly


def cyclotomic(n: int) -> tuple[int, ...]:
    require_int(n, "root order", 1, 4 * MAX_B)
    return _cyclotomic(n)


def integer_mode_remainder(b: int, k: int, j: int, *, a: int = 1) -> tuple[int, ...]:
    """Remainder of (2i)^k times a DFT mode in Q(eta), eta of order 4b.

    A unit a permutes sample locations. The value sin(pi*(a*l mod b)/b)
    is nonnegative, so this is the absolute-power sample even for odd k.
    """
    require_int(b, "b", 2, MAX_B)
    require_int(k, "k", 1, MAX_K)
    require_int(j, "j", 0, b - 1)
    require_int(a, "a", 1, b - 1)
    if math.gcd(a, b) != 1:
        raise ValueError("a must be a unit modulo b")
    order = 4 * b
    raw = [0] * order
    for l in range(b):
        location = (a * l) % b
        for h in range(k + 1):
            exponent = (2 * location * (k - 2 * h) - 4 * j * l) % order
            raw[exponent] += (-1 if h % 2 else 1) * math.comb(k, h)
    return divide_monic(raw, cyclotomic(order))[1]


def integer_spectrum(b: int, k: int, *, a: int = 1) -> dict[str, object]:
    require_int(b, "b", 2, MAX_B)
    require_int(k, "k", 1, MAX_K)
    require_int(a, "a", 1, b - 1)
    if math.gcd(a, b) != 1:
        raise ValueError("a must be a unit modulo b")
    remainders = [integer_mode_remainder(b, k, j, a=a) for j in range(b)]
    support = [j for j, value in enumerate(remainders) if value]
    return {
        "a": a,
        "b": b,
        "integer_lambda": k,
        "support": support,
        "reduced_degree": len(support),
        "mode_remainders_sha256": canonical_sha(remainders),
    }


def cosine_sign(b: int, j: int, l: int) -> int:
    """Exact sign of cos(2*pi*j*l/b) using integer quadrant comparisons."""
    require_int(b, "sign b", 2, MAX_SIGN_B)
    require_int(j, "sign j", 1, b // 2)
    require_int(l, "sign l", 1, b // 2)
    four_r = 4 * ((j * l) % b)
    if four_r == b or four_r == 3 * b:
        return 0
    return 1 if four_r < b or four_r > 3 * b else -1


def sign_variation_row(b: int, j: int) -> dict[str, object]:
    require_int(b, "sign b", 2, MAX_SIGN_B)
    require_int(j, "sign j", 1, b // 2)
    signs = [cosine_sign(b, j, l) for l in range(1, b // 2 + 1)]
    nonzero = [s for s in signs if s]
    variations = sum(left != right for left, right in pairwise(nonzero))
    if variations > j or nonzero[-1] != (-1) ** j:
        raise ArithmeticError("coefficient-sign or leading-sign boundary failed")
    return {
        "b": b,
        "j": j,
        "signs_in_increasing_base_order": signs,
        "variations": variations,
        "known_positive_integer_roots": list(range(1, j)),
        "positive_zero_count_from_parity": j - 1,
        "zero_continuation_value": -1,
        "eventual_sign": (-1) ** j,
    }


def positive_zero_continuation_remainder(b: int, j: int) -> tuple[int, ...]:
    """DFT of ones with the zero sample omitted, not a choice of 0^0."""
    require_int(b, "b", 2, MAX_B)
    require_int(j, "nonzero j", 1, b - 1)
    raw = [0] * (4 * b)
    for l in range(1, b):
        raw[(-4 * j * l) % (4 * b)] += 1
    return divide_monic(raw, cyclotomic(4 * b))[1]


def totient(n: int) -> int:
    return sum(math.gcd(a, n) == 1 for a in range(1, n + 1))


def work_bound(max_b: int, max_k: int, sign_b: int) -> dict[str, int]:
    require_int(max_b, "max_b", 2, MAX_B)
    require_int(max_k, "max_k", 1, MAX_K)
    require_int(sign_b, "sign_b", 2, MAX_SIGN_B)
    # Constructing all Phi_n through 4*max_b bounds the cached subset actually used.
    cyclotomic_updates = sum(
        (n + 1) * (d + 1)
        for n in range(1, 4 * max_b + 1)
        for d in range(1, n)
        if n % d == 0
    )
    grouped_terms = sum(
        b * b * (k + 1) for b in range(2, max_b + 1) for k in range(1, max_k + 1)
    )
    mode_division_updates = sum(
        max_k * b * (4 * b - totient(4 * b)) * (totient(4 * b) + 1)
        for b in range(2, max_b + 1)
    )
    sign_evaluations = sum((b // 2) ** 2 for b in range(2, sign_b + 1))
    parts = {
        "cyclotomic_coefficient_updates_bound": cyclotomic_updates,
        "grouped_binomial_additions": grouped_terms,
        "mode_division_coefficient_updates_bound": mode_division_updates,
        "sign_evaluations": sign_evaluations,
    }
    return {**parts, "total": sum(parts.values())}


def verify_sources() -> dict[str, object]:
    if file_sha(SOURCES_PATH) != EXPECTED_MANIFEST_SHA256_LF:
        raise RuntimeError("sources manifest hash mismatch")
    manifest = json.loads(SOURCES_PATH.read_text(encoding="utf-8"))
    if not isinstance(manifest, dict):
        raise TypeError("sources manifest must be an object")
    if manifest.get("schema") != SCHEMA.replace(".v1", ".sources.v1"):
        raise RuntimeError("sources schema mismatch")
    if manifest.get("base_commit") != BASE_COMMIT:
        raise RuntimeError("source commit mismatch")
    rows = manifest.get("sources")
    if not isinstance(rows, list) or any(not isinstance(row, dict) for row in rows):
        raise TypeError("source records must be an object list")
    if any(not isinstance(row.get("path"), str) for row in rows):
        raise TypeError("source paths must be strings")
    indexed = {row["path"]: row for row in rows}
    if len(indexed) != len(rows) or set(indexed) != set(EXPECTED_SOURCE_BLOBS):
        raise RuntimeError("source path set mismatch")
    for path, expected_blob in EXPECTED_SOURCE_BLOBS.items():
        row = indexed[path]
        if set(row) != {"path", "role", "git_blob", "sha256_lf"}:
            raise RuntimeError("source record field mismatch")
        if any(not isinstance(value, str) for value in row.values()):
            raise TypeError("source record values must be strings")
        if row["git_blob"] != expected_blob:
            raise RuntimeError("manifest source blob mismatch")
        actual_blob = (
            subprocess.check_output(
                ["git", "rev-parse", f"{BASE_COMMIT}:{path}"], cwd=REPO_ROOT
            )
            .decode("ascii")
            .strip()
        )
        if actual_blob != expected_blob:
            raise RuntimeError("authenticated source blob mismatch")
        blob_bytes = subprocess.check_output(
            ["git", "cat-file", "blob", expected_blob], cwd=REPO_ROOT
        )
        if sha256(lf_bytes(blob_bytes)) != row["sha256_lf"]:
            raise RuntimeError("frozen source content hash mismatch")
        if file_sha(REPO_ROOT / path) != row["sha256_lf"]:
            raise RuntimeError("worktree source content hash mismatch")
    return {
        "manifest_sha256_lf": EXPECTED_MANIFEST_SHA256_LF,
        "base_commit": BASE_COMMIT,
        "frozen_blobs_and_worktree_bytes_authenticated": True,
        "records": rows,
        "literature_boundary": manifest["literature_boundary"],
        "adjacent_literature": manifest["adjacent_literature"],
        "scope": manifest["scope"],
    }


def build_fixture(
    *,
    max_b: int = 16,
    max_k: int = 8,
    sign_b: int = 64,
    resource_cap: int = WORK_CAP_EXCLUSIVE,
) -> dict[str, object]:
    require_int(resource_cap, "resource_cap", 1, WORK_CAP_EXCLUSIVE)
    work = work_bound(max_b, max_k, sign_b)
    if work["total"] >= resource_cap:
        raise RuntimeError("declared work reaches the strict exclusive cap")
    sources = verify_sources()
    spectra = []
    for b in range(2, max_b + 1):
        for k in range(1, max_k + 1):
            row = integer_spectrum(b, k)
            predicted = b if k % 2 else min(b, k + 1)
            expected_support = [j for j in range(b) if k % 2 or min(j, b - j) <= k // 2]
            if row["reduced_degree"] != predicted or row["support"] != expected_support:
                raise ArithmeticError(
                    "cyclotomic replay contradicts mode classification"
                )
            spectra.append(row)
    signs = [
        sign_variation_row(b, j)
        for b in range(2, sign_b + 1)
        for j in range(1, b // 2 + 1)
    ]
    fixture: dict[str, object] = {
        "schema": SCHEMA,
        "programme_issue": 764,
        "claims": {
            "GLO764.RATIONAL_ABSOLUTE_REAL_EXACT_DEGREE": {
                "status": "PROPOSED_EXACT_THEOREM_WITH_NATIVE_PROOF",
                "scope": "every positive real exponent; every reduced rational angle",
                "non_even_degree": "b",
                "even_degree": "min(b,2m+1) at lambda=2m",
            },
            "GLO764.RATIONAL_ABSOLUTE_REAL_MODE_ZEROS": {
                "status": "PROPOSED_EXACT_THEOREM_WITH_NATIVE_PROOF",
                "positive_zeros_of_mode_j_in_x_lambda_over_2": "1,...,j-1, all simple",
                "method": "generalized Descartes, exact integer roots, and sign parity",
            },
        },
        "sources": sources,
        "integer_power_census": {
            "max_b": max_b,
            "max_k": max_k,
            "row_count": len(spectra),
            "rows_sha256": canonical_sha(spectra),
            "representatives": [spectra[0], spectra[len(spectra) // 2], spectra[-1]],
        },
        "sign_variation_census": {
            "max_b": sign_b,
            "row_count": len(signs),
            "rows_sha256": canonical_sha(signs),
            "maximum_variations_minus_j": max(
                row["variations"] - row["j"] for row in signs
            ),
            "representatives": [signs[0], signs[len(signs) // 2], signs[-1]],
        },
        "complex_counterexample": {
            "b": 4,
            "lambda": "2+4*pi*i/log(2)",
            "unnormalized_sample_block": ["0", "1/2", "1", "1/2"],
            "unnormalized_DFT": [2, -1, 0, -1],
            "reduced_degree": 3,
            "proof": "native positive-real-log exponential identity, not complex floating point",
        },
        "resource_contract": {
            "arithmetic_class": "EXACT",
            "arithmetic_domain": "integer polynomials modulo cyclotomic polynomials",
            "work_bound": work,
            "work_cap_exclusive": resource_cap,
            "hard_max_b": MAX_B,
            "hard_max_k": MAX_K,
            "hard_max_sign_b": MAX_SIGN_B,
            "float_operations": 0,
            "random_samples": 0,
            "external_symbolic_engine": False,
            "counts_named_algebraic_loops_not_bit_operations": True,
        },
        "proof_boundary": {
            "noninteger_real_theorem_is_analytic_not_computational": True,
            "finite_replay_not_an_infinite_quantifier_certificate": True,
            "no_complex_pointwise_full_degree_claim": True,
            "zero_exponent_conventions_excluded": True,
            "no_global_L_function_or_RH_GRH_consequence": True,
            "external_novelty_unreviewed": True,
        },
        "artifacts": {
            relative(path): file_sha(path)
            for path in (SCRIPT_PATH, NOTE_PATH, TEST_PATH)
        },
    }
    fixture["payload_sha256"] = canonical_sha(fixture)
    return fixture


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    serialized = json.dumps(build_fixture(), indent=2, sort_keys=True) + "\n"
    if args.check:
        if (
            not OUTPUT_PATH.exists()
            or OUTPUT_PATH.read_text(encoding="utf-8") != serialized
        ):
            raise SystemExit("stored exact-degree fixture is stale")
        print(f"verified {OUTPUT_PATH}")
    else:
        OUTPUT_PATH.write_text(serialized, encoding="utf-8", newline="\n")
        print(f"wrote {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
