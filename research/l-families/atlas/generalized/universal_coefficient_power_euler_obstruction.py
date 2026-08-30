"""Exact bounded replay for the universal Euler obstruction and trace repair.

The companion note proves the unbounded representation and combinatorial
statements. This producer replays exact finite differences against independent
multiset descent counting, positive two-jet defects, and balanced trace weights
with finite formal exponential/determinant coefficients. No finite rectangle
is treated as a proof of a universal representation quantifier.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
from collections.abc import Iterator, Sequence
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve()
PACKET_ROOT = SCRIPT_PATH.parent
REPO_ROOT = SCRIPT_PATH.parents[4]
OUTPUT_PATH = PACKET_ROOT / "universal_coefficient_power_euler_obstruction.json"
SOURCES_PATH = PACKET_ROOT / "universal_coefficient_power_euler_obstruction.sources.json"
NOTE_PATH = PACKET_ROOT / "UNIVERSAL_COEFFICIENT_POWER_EULER_OBSTRUCTION.md"
TEST_PATH = REPO_ROOT / "tests" / "test_universal_coefficient_power_euler_obstruction.py"
EXPECTED_BASE_COMMIT = "02e53055b6bdff73fa136ff28cced239d1627f80"
EXPECTED_SOURCES_SHA256_LF = (
    "af2a7ebe6e3cfbe27f90a3e77a48a736154a16df81fdba8af17a7c3913196bd1"
)
EXPECTED_SOURCE_OBJECTS = {
    "research/l-families/atlas/generalized/NONINTEGRAL_LOCAL_POWER_RATIONALITY.md": (
        "5eeb1e7c6129646ac646c697276bcd4adb04aa0c"
    ),
    "research/l-families/atlas/generalized/TRANSFER_MATRIX_SYMMETRIC_PARENT.md": (
        "9aef6f8a780e9dff5c3b7a53c012c0956be036dc"
    ),
    "research/l-families/atlas/generalized/DENSE_TORUS_TRACE_ABSOLUTE_POWER_RATIONALITY.md": (
        "f8d08185ce73d83c1ebe4088a1d32591cfadc2e9"
    ),
}
DEFAULT_MAX_N = 4
DEFAULT_MAX_K = 4
MAX_ALLOWED_N = 5
MAX_ALLOWED_K = 5
MAX_BALANCED_M = 2
TRACE_CUTOFF = 4
DEFAULT_RESOURCE_CAP_EXCLUSIVE = 10_000_000
IDENTITY_ROW_CAP_EXCLUSIVE = 2_000_000
BALANCED_ROW_CAP_EXCLUSIVE = 20_000
Exponent = tuple[int, ...]


def _relative(path: Path) -> str:
    return path.resolve().relative_to(REPO_ROOT).as_posix()


def _normalized_bytes(raw: bytes) -> bytes:
    return raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def _lf_sha256(path: Path) -> str:
    return hashlib.sha256(_normalized_bytes(path.read_bytes())).hexdigest()


def _canonical_sha256(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode(
            "utf-8"
        )
    ).hexdigest()


def _git_blob_at(commit: str, path: str) -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--verify", f"{commit}:{path}"],
            cwd=REPO_ROOT, check=False, capture_output=True, text=True,
        )
    except OSError as exc:
        raise RuntimeError("git object lookup could not be executed") from exc
    blob = result.stdout.strip()
    if (
        result.returncode != 0 or len(blob) != 40
        or any(character not in "0123456789abcdef" for character in blob)
    ):
        raise RuntimeError(f"git object lookup failed: {commit}:{path}")
    return blob


def _git_blob_bytes(blob: str) -> bytes:
    try:
        result = subprocess.run(
            ["git", "cat-file", "blob", blob],
            cwd=REPO_ROOT, check=False, capture_output=True,
        )
    except OSError as exc:
        raise RuntimeError("git blob read could not be executed") from exc
    if result.returncode != 0:
        raise RuntimeError(f"git blob read failed: {blob}")
    return result.stdout


def _integer(value: int, name: str, minimum: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value < minimum:
        raise ValueError(f"{name} must be at least {minimum}")


def _rank_power(n: int, k: int) -> None:
    _integer(n, "n", 1)
    _integer(k, "k", 0)
    if n > MAX_ALLOWED_N or k > MAX_ALLOWED_K:
        raise ValueError("rank/power exceeds bounded replay range")


def identity_work_bound(n: int, k: int) -> dict[str, int]:
    """Bound counted loop terms, not CPU time or bit operations."""
    _rank_power(n, k)
    e = k * (n - 1)
    d = e + 1
    state_bound = n**k * (k + 1)
    transition_coefficient_bound = state_bound * max(k, 1) * (e + 1)
    tail_end = 2 * d + 3
    difference_summands = sum(min(j, d) + 1 for j in range(tail_end + 1))
    return {
        "dp_state_upper_bound": state_bound,
        "dp_transition_coefficient_upper_bound": transition_coefficient_bound,
        "finite_difference_summands": difference_summands,
        "declared_work_upper_bound": transition_coefficient_bound + difference_summands,
    }


def identity_coefficient(n: int, k: int, r: int) -> int:
    _rank_power(n, k)
    _integer(r, "r", 0)
    if r > 2 * (MAX_ALLOWED_K * (MAX_ALLOWED_N - 1) + 1) + 3:
        raise ValueError("coefficient index exceeds bounded replay range")
    return math.comb(n + r - 1, n - 1) ** k


def finite_difference_numerator(n: int, k: int) -> tuple[list[int], int]:
    _rank_power(n, k)
    e = k * (n - 1)
    d = e + 1
    tail_end = 2 * d + 3
    values = [
        sum(
            (-1) ** i * math.comb(d, i) * identity_coefficient(n, k, j - i)
            for i in range(min(d, j) + 1)
        )
        for j in range(tail_end + 1)
    ]
    if any(values[e + 1 :]):
        raise ArithmeticError("polynomial finite-difference tail is nonzero")
    numerator = values[: e + 1]
    while len(numerator) > 1 and numerator[-1] == 0:
        numerator.pop()
    return numerator, tail_end


def multiset_descent_numerator(
    n: int, k: int, *, resource_cap: int = IDENTITY_ROW_CAP_EXCLUSIVE
) -> tuple[list[int], dict[str, int]]:
    _rank_power(n, k)
    _integer(resource_cap, "resource_cap", 1)
    bounds = identity_work_bound(n, k)
    if bounds["declared_work_upper_bound"] >= resource_cap:
        raise RuntimeError("identity work bound reaches exclusive cap")
    additions = 0

    @lru_cache(maxsize=None)
    def walk(remaining: tuple[int, ...], last: int) -> tuple[int, ...]:
        nonlocal additions
        if not any(remaining):
            return (1,)
        result = [0] * (sum(remaining) + 1)
        for letter, count in enumerate(remaining):
            if not count:
                continue
            reduced = list(remaining)
            reduced[letter] -= 1
            suffix = walk(tuple(reduced), letter)
            shift = int(last > letter)
            for degree, value in enumerate(suffix):
                result[degree + shift] += value
                additions += 1
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        return tuple(result)

    numerator = list(walk((n - 1,) * k, -1))
    states = walk.cache_info().currsize
    if states > bounds["dp_state_upper_bound"]:
        raise ArithmeticError("dynamic-program state bound failed")
    if additions > bounds["dp_transition_coefficient_upper_bound"]:
        raise ArithmeticError("dynamic-program addition bound failed")
    return numerator, {"visited_states": states, "coefficient_additions": additions}


def identity_row(n: int, k: int) -> dict[str, object]:
    _rank_power(n, k)
    numerator, tail_end = finite_difference_numerator(n, k)
    descent_numerator, dp_stats = multiset_descent_numerator(n, k)
    if numerator != descent_numerator:
        raise ArithmeticError("finite differences disagree with multiset descents")
    e = k * (n - 1)
    d = e + 1
    dimension = n**k
    word_count = math.factorial(e) // math.factorial(n - 1) ** k
    degree = (k - 1) * (n - 1) if k else 0
    a = math.comb(n + 1, 2)
    b = math.comb(n, 2)
    target_second = a**k
    forced_second = math.comb(dimension + 1, 2)
    defect = forced_second - target_second
    even_terms = [
        {"j": j, "dimension": math.comb(k, j) * a ** (k - j) * b**j}
        for j in range(2, k + 1, 2)
    ]
    no_go = n >= 2 and k >= 2
    if numerator[0] != 1 or any(value < 0 for value in numerator):
        raise ArithmeticError("descent numerator normalization or positivity failed")
    if len(numerator) - 1 != degree or sum(numerator) != word_count:
        raise ArithmeticError("numerator degree or total word count failed")
    if (numerator[1] if len(numerator) > 1 else 0) != dimension - d:
        raise ArithmeticError("first numerator coefficient failed")
    if defect != sum(row["dimension"] for row in even_terms):
        raise ArithmeticError("even-flip decomposition failed")
    if (dimension > d) != no_go or (defect > 0) != no_go:
        raise ArithmeticError("obstruction and exception chambers disagree")
    return {
        "n": n, "k": k,
        "no_go_chamber": no_go,
        "first_coefficient_forced_virtual_dimension": dimension,
        "exact_identity_pole_order": d,
        "pole_order_gap": dimension - d,
        "target_second_coefficient": target_second,
        "forced_euler_second_coefficient": forced_second,
        "second_coefficient_defect": defect,
        "omitted_even_flip_summands": even_terms,
        "identity_numerator": numerator,
        "independent_descent_numerator_equal": True,
        "numerator_degree": degree,
        "numerator_at_one_multiset_word_count": word_count,
        "finite_difference_zero_tail_start": e + 1,
        "finite_difference_zero_tail_end_inclusive": tail_end,
        "dynamic_program": dp_stats,
        "resource_bound": identity_work_bound(n, k),
    }


def _balanced_parameters(n: int, m: int) -> None:
    _rank_power(n, m)
    if m < 1 or m > MAX_BALANCED_M:
        raise ValueError("balanced power m is outside bounded replay range")


def _compositions(total: int, parts: int) -> Iterator[Exponent]:
    _integer(total, "composition total", 0)
    _integer(parts, "composition parts", 1)
    if total > MAX_BALANCED_M or parts > MAX_ALLOWED_N:
        raise ValueError("composition request exceeds bounded replay range")
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for suffix in _compositions(total - first, parts - 1):
            yield (first,) + suffix


def balanced_work_bound(n: int, m: int) -> int:
    _balanced_parameters(n, m)
    pair_bound = math.comb(m + n - 1, n - 1) ** 2
    end_convolution_bound = sum(n ** (2 * j) for j in range(1, m + 1))
    size = TRACE_CUTOFF + 1
    return (
        pair_bound + end_convolution_bound
        + (2 * n + 2 * size**2) * pair_bound
        + size**2 + 2 * n * size
    )


def balanced_weights(
    n: int, m: int, *, resource_cap: int = BALANCED_ROW_CAP_EXCLUSIVE
) -> dict[Exponent, int]:
    _balanced_parameters(n, m)
    _integer(resource_cap, "resource_cap", 1)
    if balanced_work_bound(n, m) >= resource_cap:
        raise RuntimeError("balanced work bound reaches exclusive cap")
    compositions = list(_compositions(m, n))
    weighted = [
        (row, math.factorial(m) // math.prod(math.factorial(v) for v in row))
        for row in compositions
    ]
    coefficients: dict[Exponent, int] = {}
    for alpha, left in weighted:
        for beta, right in weighted:
            exponent = tuple(a - b for a, b in zip(alpha, beta))
            coefficients[exponent] = coefficients.get(exponent, 0) + left * right
    convolution: dict[Exponent, int] = {(0,) * n: 1}
    for _ in range(m):
        updated: dict[Exponent, int] = {}
        for exponent, coefficient in convolution.items():
            for i in range(n):
                for j in range(n):
                    vector = list(exponent)
                    vector[i] += 1
                    vector[j] -= 1
                    key = tuple(vector)
                    updated[key] = updated.get(key, 0) + coefficient
        convolution = updated
    if coefficients != convolution:
        raise ArithmeticError("multinomial and End-convolution weights disagree")
    return coefficients


def _fraction_pair(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def balanced_trace_row(n: int, m: int) -> dict[str, object]:
    coefficients = balanced_weights(n, m)
    rank = n ** (2 * m)
    if sum(coefficients.values()) != rank or any(c <= 0 for c in coefficients.values()):
        raise ArithmeticError("balanced representation rank or positivity failed")
    if any(sum(v) != 0 for v in coefficients):
        raise ArithmeticError("scalar-twist invariance failed")
    if any(coefficients[tuple(-x for x in v)] != c for v, c in coefficients.items()):
        raise ArithmeticError("self-dual weight symmetry failed")
    determinant_exponent = [
        sum(v[i] * c for v, c in coefficients.items()) for i in range(n)
    ]
    if determinant_exponent != [0] * n:
        raise ArithmeticError("determinant-one weight sum failed")
    diagonal = [Fraction(value) for value in (2, 3, 5, 7, 11)[:n]]
    weight_values = [
        (math.prod(z**v for z, v in zip(diagonal, exponent)), coefficient)
        for exponent, coefficient in sorted(coefficients.items())
    ]
    traces = [
        sum(z**r for z in diagonal) ** m * sum(z ** (-r) for z in diagonal) ** m
        for r in range(TRACE_CUTOFF + 1)
    ]
    if any(
        traces[r] != sum(multiplicity * value**r for value, multiplicity in weight_values)
        for r in range(TRACE_CUTOFF + 1)
    ):
        raise ArithmeticError("balanced algebraic power-trace identity failed")
    exponential = [Fraction(1)]
    for degree in range(1, TRACE_CUTOFF + 1):
        exponential.append(
            sum(traces[r] * exponential[degree - r] for r in range(1, degree + 1))
            / degree
        )
    determinant = [Fraction(1)] + [Fraction(0)] * TRACE_CUTOFF
    for value, multiplicity in weight_values:
        factor = [
            math.comb(multiplicity + j - 1, j) * value**j
            for j in range(TRACE_CUTOFF + 1)
        ]
        determinant = [
            sum(determinant[j] * factor[degree - j] for j in range(degree + 1))
            for degree in range(TRACE_CUTOFF + 1)
        ]
    if exponential != determinant:
        raise ArithmeticError("formal exponential and determinant product disagree")
    records = [
        {"exponent": list(exponent), "multiplicity": coefficients[exponent]}
        for exponent in sorted(coefficients)
    ]
    return {
        "n": n, "m": m,
        "representation_rank_and_euler_denominator_degree": rank,
        "distinct_character_count_dense_scalar_recurrence_degree": len(coefficients),
        "weight_multiplicities_sha256": _canonical_sha256(records),
        "constant_weight_multiplicity": coefficients[(0,) * n],
        "self_dual_weight_symmetry": True,
        "all_weights_scalar_twist_blind": True,
        "determinant_character_exponent": determinant_exponent,
        "multinomial_equals_independent_End_convolution": True,
        "sample_diagonal": [_fraction_pair(z) for z in diagonal],
        "sample_is_nonunitary_algebraic_trace_pair_not_absolute_trace": True,
        "trace_indices": list(range(TRACE_CUTOFF + 1)),
        "balanced_power_traces": [_fraction_pair(value) for value in traces],
        "exponential_coefficients": [_fraction_pair(value) for value in exponential],
        "independent_determinant_coefficients_equal": True,
        "identity_scalar_recurrence_degree": 1,
        "identity_euler_denominator_degree": rank,
        "declared_work_upper_bound": balanced_work_bound(n, m),
    }


def verify_sources_manifest() -> dict[str, object]:
    actual_hash = _lf_sha256(SOURCES_PATH)
    if actual_hash != EXPECTED_SOURCES_SHA256_LF:
        raise RuntimeError("universal-Euler sources manifest hash mismatch")
    manifest = json.loads(SOURCES_PATH.read_text(encoding="utf-8"))
    if manifest.get("base_commit") != EXPECTED_BASE_COMMIT:
        raise RuntimeError("universal-Euler source base commit mismatch")
    sources = manifest.get("sources")
    if not isinstance(sources, list) or any(not isinstance(row, dict) for row in sources):
        raise TypeError("sources must be a list of objects")
    index = {row.get("path"): row for row in sources}
    if len(index) != len(sources) or set(index) != set(EXPECTED_SOURCE_OBJECTS):
        raise RuntimeError("source path set mismatch")
    verified = []
    for path, expected_blob in EXPECTED_SOURCE_OBJECTS.items():
        row = index[path]
        if row.get("git_blob") != expected_blob:
            raise RuntimeError(f"manifest Git blob mismatch for {path}")
        actual_blob = _git_blob_at(EXPECTED_BASE_COMMIT, path)
        if actual_blob != expected_blob:
            raise RuntimeError(f"authenticated Git blob mismatch for {path}")
        content = _normalized_bytes(_git_blob_bytes(actual_blob))
        blob_hash = hashlib.sha256(content).hexdigest()
        if blob_hash != row.get("file_sha256_lf_normalized"):
            raise RuntimeError(f"Git blob content hash mismatch for {path}")
        if _lf_sha256(REPO_ROOT / path) != blob_hash:
            raise RuntimeError(f"working-tree source hash mismatch for {path}")
        verified.append(dict(row))
    references = manifest.get("external_references")
    if not isinstance(references, list) or len(references) != 3:
        raise RuntimeError("expected three literature boundary records")
    return {
        "manifest": _relative(SOURCES_PATH),
        "manifest_sha256_lf_normalized": actual_hash,
        "base_commit": EXPECTED_BASE_COMMIT,
        "git_blob_contents_compared_to_working_tree": True,
        "verified_sources": verified,
        "external_references": references,
        "scope_firewall": manifest["scope_firewall"],
    }


def build_fixture(
    *, max_n: int = DEFAULT_MAX_N, max_k: int = DEFAULT_MAX_K,
    resource_cap: int = DEFAULT_RESOURCE_CAP_EXCLUSIVE,
) -> dict[str, object]:
    _rank_power(max_n, max_k)
    _integer(resource_cap, "resource_cap", 1)
    identity_parameters = [(n, k) for n in range(1, max_n + 1) for k in range(max_k + 1)]
    balanced_parameters = [
        (n, m) for n in range(2, min(4, max_n) + 1)
        for m in range(1, min(MAX_BALANCED_M, max_k) + 1)
    ]
    identity_bound = sum(
        identity_work_bound(n, k)["declared_work_upper_bound"] for n, k in identity_parameters
    )
    constructive_bound = sum(balanced_work_bound(n, m) for n, m in balanced_parameters)
    declared_work = identity_bound + constructive_bound
    if declared_work >= resource_cap:
        raise RuntimeError("total declared work reaches exclusive cap")
    source_lock = verify_sources_manifest()
    rows = [identity_row(n, k) for n, k in identity_parameters]
    constructive_rows = [balanced_trace_row(n, m) for n, m in balanced_parameters]
    fixture: dict[str, object] = {
        "schema": "riemann.atlas.generalized.universal_coefficient_power_euler_obstruction.v1",
        "programme_issue": {"number": 764, "url": "https://github.com/gfreund123/riemann/issues/764"},
        "claims": {
            "GLO764.UNIVERSAL_VIRTUAL_REPRESENTATION_POWER_OBSTRUCTION": {
                "status": "PROVED_IN_COMPANION_NOTE",
                "scope": "n>=2,k>=2; finite virtual algebraic GL_n representations; universal or Zariski-dense equality",
                "conclusion": "no universal representation Euler factor for sum h_r(A)^k T^r",
            },
            "GLO764.IDENTITY_SECOND_COEFFICIENT_OBSTRUCTION": {
                "status": "PROVED_IN_COMPANION_NOTE_AND_BOUNDED_EXACT_REPLAY",
                "defect": "binom(n^k+1,2)-binom(n+1,2)^k>0 for n,k>=2",
            },
            "GLO764.IDENTITY_POWER_SEGRE_EULERIAN_NUMERATOR": {
                "status": "PROVED_IN_COMPANION_NOTE_AND_INDEPENDENT_BOUNDED_CONSTRUCTIONS",
                "scope": "n>=1,k>=0; identity coefficients; k=0 means polynomial x^0=1",
                "numerator": "multiset descent polynomial, each of k letters repeated n-1 times",
            },
            "GLO764.BALANCED_TRACE_EXPONENTIAL_EULER_REPAIR": {
                "status": "PROVED_IN_COMPANION_NOTE_AND_BOUNDED_EXACT_REPLAY",
                "representation": "End(V)^tensor_m = V^tensor_m tensor (V_dual)^tensor_m",
                "trace": "p_r(A)^m*p_r(A^-1)^m, equal to abs(p_r(A))^(2m) only under unitarity",
                "euler_degree": "n^(2m), with all weight multiplicities",
            },
        },
        "source_lock": source_lock,
        "identity_controls": {
            "row_count": len(rows), "rows": rows, "rows_sha256": _canonical_sha256(rows),
            "no_go_row_count": sum(bool(row["no_go_chamber"]) for row in rows),
        },
        "constructive_controls": {
            "row_count": len(constructive_rows), "rows": constructive_rows,
            "rows_sha256": _canonical_sha256(constructive_rows),
            "formal_trace_cutoff": TRACE_CUTOFF,
            "m_one_is_classical_tensor_dual_Rankin_Selberg_local_algebra": True,
        },
        "universal_proof_obligations": {
            "identity": "every group representation sends the identity to the identity",
            "regular_extension": "coefficient functions agree at the identity if they agree on a Zariski-dense set",
            "pole_order": "degree-e polynomial coefficient sequence has exact pole order e+1",
            "stable_sort": "merged weak lists are words with value increases at every descent",
            "formal_exponential": "-log det(I-TB)=sum trace(B^r)T^r/r",
            "finite_rows_do_not_prove_universal_quantifiers": True,
        },
        "scope_firewall": source_lock["scope_firewall"],
        "resource_contract": {
            "arithmetic_class": "EXACT_INTEGER_AND_RATIONAL",
            "maximum_n": max_n, "maximum_k": max_k,
            "maximum_allowed_n": MAX_ALLOWED_N, "maximum_allowed_k": MAX_ALLOWED_K,
            "maximum_balanced_m": MAX_BALANCED_M,
            "identity_work_upper_bound": identity_bound,
            "constructive_work_upper_bound": constructive_bound,
            "declared_work_upper_bound": declared_work,
            "work_unit_definition": "named primary loops: DP coefficient additions, difference summands, weight-pair/convolution updates and finite trace/factor summands; not every diagnostic, hashing operation or bit operation",
            "work_unit_cap_exclusive": resource_cap,
            "identity_row_cap_exclusive": IDENTITY_ROW_CAP_EXCLUSIVE,
            "balanced_row_cap_exclusive": BALANCED_ROW_CAP_EXCLUSIVE,
            "float_operations": 0, "random_samples": 0, "external_symbolic_engine": False,
        },
        "producer": {
            "script": _relative(SCRIPT_PATH), "script_sha256_lf_normalized": _lf_sha256(SCRIPT_PATH),
            "note": _relative(NOTE_PATH), "note_sha256_lf_normalized": _lf_sha256(NOTE_PATH),
            "test": _relative(TEST_PATH), "test_sha256_lf_normalized": _lf_sha256(TEST_PATH),
        },
    }
    fixture["payload_sha256"] = _canonical_sha256(fixture)
    return fixture


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail unless stored fixture is current")
    args = parser.parse_args(argv)
    serialized = json.dumps(build_fixture(), indent=2, sort_keys=True) + "\n"
    if args.check:
        if not OUTPUT_PATH.exists() or OUTPUT_PATH.read_text(encoding="utf-8") != serialized:
            raise SystemExit("stored universal-Euler fixture is stale")
        print(f"verified {OUTPUT_PATH}")
        return 0
    OUTPUT_PATH.write_text(serialized, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
