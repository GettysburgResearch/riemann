"""Exact high-genus stable-range laws for Frobenius interferometers.

This standard-library-only producer imports the Hughes--Rudnick Gaussian
stable-range trace-moment theorem for Haar USp(2g) and derives exact integer
means and covariances for the source-locked genus-two interferometer packets.
It performs no finite-field enumeration, random sampling, or numerical
integration.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys
from collections import Counter, defaultdict
from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from pathlib import Path
from types import ModuleType

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
DEFAULT_OUTPUT = HERE / "usp_high_genus_interferometer_stability.json"
NOTE = HERE / "USP_HIGH_GENUS_INTERFEROMETER_STABILITY.md"
TEST = ROOT / "tests" / "test_usp_high_genus_interferometer_stability.py"

SOURCE_NOTE = HERE / "FROBENIUS_INTERFEROMETRY_SUBGROUP_SELECTORS.md"
SOURCE_PRODUCER = HERE / "frobenius_interferometry_subgroup_selectors.py"
SOURCE_TEST = ROOT / "tests" / "test_frobenius_interferometry_subgroup_selectors.py"
SOURCE_COMMIT = "6b1154e2589ba1108fc69dcb69e15199599c01cb"
EXPECTED_SOURCE_HASHES = {
    "note": "c7637d454f1fb102555e6723dd8d93a4b6a27363d80cbbb9a03061f614bd3221",
    "producer": "48474ebcbb99efea23227126f66f566fdb525a3c9ae9e81a77bf83d4075f55e7",
    "test": "9751e1f971cf484db88d7267ec28ed05a7b000a9ffd425ac4af3b392ca714897",
}

LITERATURE_URL = "https://arxiv.org/abs/2409.04844"
LITERATURE_ID = "arXiv:2409.04844v1"
MAX_WICK_CONTRACTION_BRANCHES = 4096

Monomial = tuple[int, ...]
TracePolynomial = dict[Monomial, int]

SELECTOR_DEFINITIONS: dict[str, tuple[tuple[int, tuple[int, int]], ...]] = {
    "P": ((1, (2, 2)), (-1, (4, 4))),
    "D": ((-1, (1, 1)), (2, (1, 5)), (1, (4, 4))),
    "S": ((-2, (2, 8)),),
}
INVERSE_POOL: dict[str, tuple[int, int]] = {
    "I_1_7": (1, 7),
    "I_1_9": (1, 9),
    "I_2_4": (2, 4),
    "I_2_8": (2, 8),
}
INVERSE_WINNER = (2, 4, -1, 1)

EXPECTED_SELECTOR_STABLE_MEANS = (-2, 6, -4)
EXPECTED_SELECTOR_STABLE_COVARIANCE = (
    (60, -52, 8),
    (-52, 104, -12),
    (8, -12, 144),
)
EXPECTED_SOURCE_USP4_COVARIANCE = (
    (24, -20, 4),
    (-20, 48, 0),
    (4, 0, 40),
)
EXPECTED_INVERSE_POOL_STABLE_MEANS = (1, 1, 2, 2)


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _lf_sha256(path: Path) -> str:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    return hashlib.sha256(text.encode()).hexdigest()


def _plain_positive_int(name: str, value: object) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be a plain integer")
    if value < 1:
        raise ValueError(f"{name} must be positive")
    return value


def _clean(polynomial: Mapping[Monomial, int]) -> TracePolynomial:
    output: TracePolynomial = {}
    for raw_monomial, raw_coefficient in polynomial.items():
        if isinstance(raw_coefficient, bool) or not isinstance(raw_coefficient, int):
            raise TypeError("trace-polynomial coefficients must be plain integers")
        monomial = tuple(sorted(raw_monomial))
        if any(
            isinstance(frequency, bool)
            or not isinstance(frequency, int)
            or frequency < 1
            for frequency in monomial
        ):
            raise ValueError("trace frequencies must be positive plain integers")
        if raw_coefficient:
            output[monomial] = output.get(monomial, 0) + raw_coefficient
    return {
        monomial: coefficient for monomial, coefficient in output.items() if coefficient
    }


def interferometer(left: object, right: object) -> TracePolynomial:
    """Return I_(r,s)=p_r*p_s-p_(r+s), with 1 <= r <= s."""

    r = _plain_positive_int("left frequency", left)
    s = _plain_positive_int("right frequency", right)
    if r > s:
        raise ValueError("interferometer frequencies must satisfy r <= s")
    return {(r, s): 1, (r + s,): -1}


def linear_combination(
    terms: Iterable[tuple[object, Mapping[Monomial, int]]],
) -> TracePolynomial:
    output: dict[Monomial, int] = defaultdict(int)
    for raw_scale, polynomial in terms:
        if isinstance(raw_scale, bool) or not isinstance(raw_scale, int):
            raise TypeError("linear-combination scales must be plain integers")
        for monomial, coefficient in _clean(polynomial).items():
            output[monomial] += raw_scale * coefficient
    return _clean(output)


def multiply(
    left: Mapping[Monomial, int], right: Mapping[Monomial, int]
) -> TracePolynomial:
    output: dict[Monomial, int] = defaultdict(int)
    for left_monomial, left_coefficient in _clean(left).items():
        for right_monomial, right_coefficient in _clean(right).items():
            output[tuple(sorted(left_monomial + right_monomial))] += (
                left_coefficient * right_coefficient
            )
    return _clean(output)


def maximum_weighted_degree(polynomial: Mapping[Monomial, int]) -> int:
    cleaned = _clean(polynomial)
    return max((sum(monomial) for monomial in cleaned), default=0)


def stable_genus(polynomial: Mapping[Monomial, int]) -> int:
    """Least g for which every monomial has weighted degree <= 2g+1."""

    return maximum_weighted_degree(polynomial) // 2


def eta(frequency: object) -> int:
    j = _plain_positive_int("trace frequency", frequency)
    return int(j % 2 == 0)


@dataclass
class WickGuard:
    """Fail-closed accounting for distinct exact Wick-contraction branches."""

    cap: int = MAX_WICK_CONTRACTION_BRANCHES
    ledger: Counter[str] = field(default_factory=Counter)

    def __post_init__(self) -> None:
        self.cap = _plain_positive_int("Wick branch cap", self.cap)

    @property
    def total(self) -> int:
        return sum(self.ledger.values())

    def charge(self, name: str, units: object = 1) -> None:
        if not isinstance(name, str) or not name:
            raise TypeError("resource name must be a nonempty string")
        if isinstance(units, bool) or not isinstance(units, int):
            raise TypeError("resource units must be a plain integer")
        if units < 0:
            raise ValueError("resource units must be nonnegative")
        if self.total + units > self.cap:
            raise RuntimeError(f"Wick branches would exceed cap {self.cap}")
        self.ledger[name] += units


@dataclass
class GaussianMomentEngine:
    """Exact moments of Z_j=sqrt(j)X_j-eta_j by Wick contraction."""

    guard: WickGuard
    univariate_cache: dict[tuple[int, int], int] = field(default_factory=dict)
    monomial_cache: dict[Monomial, int] = field(default_factory=dict)

    def shifted_moment(self, frequency: object, exponent: object) -> int:
        j = _plain_positive_int("trace frequency", frequency)
        if isinstance(exponent, bool) or not isinstance(exponent, int):
            raise TypeError("moment exponent must be a plain integer")
        if exponent < 0:
            raise ValueError("moment exponent must be nonnegative")
        key = (j, exponent)
        if key in self.univariate_cache:
            return self.univariate_cache[key]

        result = 0
        shift = -eta(j)
        for gaussian_count in range(0, exponent + 1, 2):
            pairing_count = math.prod(range(1, gaussian_count, 2))
            assignment_count = math.comb(exponent, gaussian_count)
            self.guard.charge(
                "Wick_contraction_branches", assignment_count * pairing_count
            )
            result += (
                assignment_count
                * pairing_count
                * j ** (gaussian_count // 2)
                * shift ** (exponent - gaussian_count)
            )
        self.univariate_cache[key] = result
        return result

    def monomial_expectation(self, monomial: Monomial) -> int:
        canonical = tuple(sorted(monomial))
        if canonical in self.monomial_cache:
            return self.monomial_cache[canonical]
        counts = Counter(canonical)
        result = 1
        for frequency, exponent in counts.items():
            result *= self.shifted_moment(frequency, exponent)
        self.monomial_cache[canonical] = result
        return result

    def expectation(self, polynomial: Mapping[Monomial, int]) -> int:
        return sum(
            coefficient * self.monomial_expectation(monomial)
            for monomial, coefficient in _clean(polynomial).items()
        )


def stable_interferometer_mean(left: object, right: object) -> int:
    """Closed stable-range mean r*1_(r=s)+eta_r eta_s+eta_(r+s)."""

    r = _plain_positive_int("left frequency", left)
    s = _plain_positive_int("right frequency", right)
    if r > s:
        raise ValueError("interferometer frequencies must satisfy r <= s")
    return r * int(r == s) + eta(r) * eta(s) + eta(r + s)


def _selector_polynomials() -> dict[str, TracePolynomial]:
    return {
        name: linear_combination(
            (scale, interferometer(*frequencies)) for scale, frequencies in definition
        )
        for name, definition in SELECTOR_DEFINITIONS.items()
    }


def _verify_source_locks(
    paths: Mapping[str, Path] | None = None,
) -> dict[str, str]:
    locked_paths = dict(
        paths
        or {
            "note": SOURCE_NOTE,
            "producer": SOURCE_PRODUCER,
            "test": SOURCE_TEST,
        }
    )
    if set(locked_paths) != set(EXPECTED_SOURCE_HASHES):
        raise ValueError("source-lock path keys changed")
    observed = {name: _lf_sha256(path) for name, path in locked_paths.items()}
    for name, expected in EXPECTED_SOURCE_HASHES.items():
        if observed[name] != expected:
            raise RuntimeError(f"locked interferometer {name} hash changed")
    return observed


def _load_locked_source() -> ModuleType:
    _verify_source_locks()
    module_name = "_locked_frobenius_interferometry_subgroup_selectors"
    specification = importlib.util.spec_from_file_location(module_name, SOURCE_PRODUCER)
    if specification is None or specification.loader is None:
        raise RuntimeError("could not load locked interferometer producer")
    module = importlib.util.module_from_spec(specification)
    previous = sys.modules.get(module_name)
    sys.modules[module_name] = module
    try:
        specification.loader.exec_module(module)
    finally:
        if previous is None:
            sys.modules.pop(module_name, None)
        else:
            sys.modules[module_name] = previous
    return module


def _source_usp4_replay() -> dict[str, object]:
    source = _load_locked_source()
    source_guard = source.ResourceGuard()
    context = source.HaarContext(source_guard)
    pairs = {
        frequencies
        for definition in SELECTOR_DEFINITIONS.values()
        for _, frequencies in definition
    } | set(INVERSE_POOL.values())
    raw = {pair: source.interferometer(*pair, source_guard) for pair in sorted(pairs)}

    def source_linear(definition: tuple[tuple[int, tuple[int, int]], ...]):
        return source.laurent_linear_combination(
            ((scale, raw[pair]) for scale, pair in definition), source_guard
        )

    selector_polynomials = {
        name: source_linear(definition)
        for name, definition in SELECTOR_DEFINITIONS.items()
    }
    selector_names = tuple(SELECTOR_DEFINITIONS)
    selector_means = tuple(
        source.weyl_integral(
            selector_polynomials[name], context.c2_density, 8, source_guard
        )
        for name in selector_names
    )
    if selector_means != (0, 0, 0):
        raise ArithmeticError("source-locked USp(4) selector means drifted")

    inverse_means = tuple(
        source.weyl_integral(raw[pair], context.c2_density, 8, source_guard)
        for pair in INVERSE_POOL.values()
    )
    if inverse_means != (0, 0, 0, 0):
        raise ArithmeticError("source-locked USp(4) inverse-pool means drifted")

    covariance = tuple(
        tuple(
            source.weyl_integral(
                source.laurent_multiply(
                    selector_polynomials[left],
                    selector_polynomials[right],
                    source_guard,
                ),
                context.c2_density,
                8,
                source_guard,
            )
            for right in selector_names
        )
        for left in selector_names
    )
    if covariance != EXPECTED_SOURCE_USP4_COVARIANCE:
        raise ArithmeticError("source-locked USp(4) covariance drifted")

    def exact_integer(value: object) -> int:
        numerator = getattr(value, "numerator", None)
        denominator = getattr(value, "denominator", None)
        if not isinstance(numerator, int) or denominator != 1:
            raise ArithmeticError("source replay produced a nonintegral Haar value")
        return numerator

    return {
        "selector_means": [exact_integer(value) for value in selector_means],
        "selector_covariance": [
            [exact_integer(value) for value in row] for row in covariance
        ],
        "inverse_pool_means": [exact_integer(value) for value in inverse_means],
        "source_accounted_operations": source_guard.total,
    }


def _determinant_three(matrix: tuple[tuple[int, ...], ...]) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def build_fixture() -> dict[str, object]:
    source_replay = _source_usp4_replay()
    guard = WickGuard()
    engine = GaussianMomentEngine(guard)
    selectors = _selector_polynomials()
    selector_names = tuple(SELECTOR_DEFINITIONS)

    selector_means = tuple(
        engine.expectation(selectors[name]) for name in selector_names
    )
    if selector_means != EXPECTED_SELECTOR_STABLE_MEANS:
        raise ArithmeticError("stable selector means drifted")

    second_moments = tuple(
        tuple(
            engine.expectation(multiply(selectors[left], selectors[right]))
            for right in selector_names
        )
        for left in selector_names
    )
    covariance = tuple(
        tuple(
            second_moments[row][column] - selector_means[row] * selector_means[column]
            for column in range(len(selector_names))
        )
        for row in range(len(selector_names))
    )
    if covariance != EXPECTED_SELECTOR_STABLE_COVARIANCE:
        raise ArithmeticError("stable selector covariance drifted")

    raw_pool = {name: interferometer(*pair) for name, pair in INVERSE_POOL.items()}
    raw_pool_means = tuple(engine.expectation(raw_pool[name]) for name in INVERSE_POOL)
    if raw_pool_means != EXPECTED_INVERSE_POOL_STABLE_MEANS:
        raise ArithmeticError("stable inverse-pool mean vector drifted")
    for name, pair in INVERSE_POOL.items():
        if raw_pool_means[
            tuple(INVERSE_POOL).index(name)
        ] != stable_interferometer_mean(*pair):
            raise ArithmeticError(f"closed interferometer formula drifted for {name}")

    winner = linear_combination(
        (coefficient, raw_pool[name])
        for coefficient, name in zip(INVERSE_WINNER, INVERSE_POOL)
    )
    winner_mean = engine.expectation(winner)
    if winner_mean != 6 or stable_genus(winner) != 5:
        raise ArithmeticError("inverse winner stable law drifted")

    entrywise_stable_genera = tuple(
        tuple(
            stable_genus(multiply(selectors[left], selectors[right]))
            for right in selector_names
        )
        for left in selector_names
    )
    expected_entrywise_genera = ((8, 8, 9), (8, 8, 9), (9, 9, 10))
    if entrywise_stable_genera != expected_entrywise_genera:
        raise ArithmeticError("entrywise covariance stable genera drifted")

    leading_minors = (
        covariance[0][0],
        covariance[0][0] * covariance[1][1] - covariance[0][1] * covariance[1][0],
        _determinant_three(covariance),
    )
    if leading_minors != (60, 3536, 503872):
        raise ArithmeticError("stable covariance positivity certificate drifted")

    payload: dict[str, object] = {
        "schema": "riemann.function_field.usp_high_genus_interferometer_stability.v1",
        "status": "EXACT_COMPACT_HAAR_CONSEQUENCES_OF_IMPORTED_STABLE_RANGE_THEOREM",
        "scope": {
            "group": "Haar USp(2g)",
            "observable": "p_j=Tr(U^j), I_(r,s)=p_r*p_s-p_(r+s)",
            "arithmetic_claims": False,
            "novelty_claim": False,
            "not_claimed": [
                "arithmetic increasing-genus equidistribution",
                "subgroup or endomorphism diagnosis for a family member",
                "a zero-statistics theorem",
                "an RH or GRH consequence",
            ],
        },
        "literature_dependency": {
            "authors": "Alexei Entin and Noam Pirani",
            "title": "Moments of traces of random symplectic matrices and hyperelliptic L-functions",
            "identifier": LITERATURE_ID,
            "url": LITERATURE_URL,
            "location": "equation (1.4), equation (1.6), and the following paragraph",
            "imported_theorem": (
                "for weighted degree sum_j j*a_j <= 2g+1, Haar USp(2g) trace moments equal those of independent Z_j=sqrt(j)X_j-eta_j"
            ),
            "eta": "eta_j=1 for even j and 0 for odd j",
            "proof_status": "imported, not reproved by this packet",
        },
        "source_locked_genus_two_packet": {
            "source_commit": SOURCE_COMMIT,
            "files": {
                name: {
                    "path": str(path.relative_to(ROOT)).replace("\\", "/"),
                    "sha256_lf_normalized": EXPECTED_SOURCE_HASHES[name],
                }
                for name, path in {
                    "note": SOURCE_NOTE,
                    "producer": SOURCE_PRODUCER,
                    "test": SOURCE_TEST,
                }.items()
            },
            "replayed_USp4": source_replay,
        },
        "stable_interferometer_mean_theorem": {
            "formula": "E[I_(r,s)]=r*1_(r=s)+eta_r*eta_s+eta_(r+s)",
            "validity": "exact whenever r+s<=2g+1",
            "derivation": (
                "E[p_r p_s]=r*1_(r=s)+eta_r*eta_s and E[p_(r+s)]=-eta_(r+s) under the imported independent shifted-Gaussian law"
            ),
        },
        "selectors": {
            "order": list(selector_names),
            "definitions": {
                "P": "I_(2,2)-I_(4,4)",
                "D": "-I_(1,1)+2*I_(1,5)+I_(4,4)",
                "S": "-2*I_(2,8)",
            },
            "USp4_means": source_replay["selector_means"],
            "stable_means": list(selector_means),
            "mean_stable_from_genus": {
                name: stable_genus(selectors[name]) for name in selector_names
            },
            "interpretation": (
                "the genus-two ambient-null calibration is exceptional: the same raw trace packets acquire nonzero universal ambient means in the exact high-genus stable range"
            ),
            "stable_second_moment_matrix": [list(row) for row in second_moments],
            "whole_second_moment_matrix_stable_from_genus": 10,
            "stable_covariance_matrix": [list(row) for row in covariance],
            "covariance_entrywise_stable_from_genus": [
                list(row) for row in entrywise_stable_genera
            ],
            "whole_covariance_stable_from_genus": 10,
            "covariance_positive_definite_leading_minors": list(leading_minors),
        },
        "inverse_raw_pool": {
            "order": list(INVERSE_POOL),
            "definitions": {
                name: f"I_({pair[0]},{pair[1]})" for name, pair in INVERSE_POOL.items()
            },
            "USp4_means": source_replay["inverse_pool_means"],
            "stable_means": list(raw_pool_means),
            "all_pool_means_stable_from_genus": 5,
            "winner": {
                "coefficients": list(INVERSE_WINNER),
                "definition": "2*I_(1,7)+4*I_(1,9)-I_(2,4)+I_(2,8)",
                "USp4_mean": 0,
                "stable_mean": winner_mean,
                "stable_from_genus": stable_genus(winner),
            },
            "simultaneous_USp4_and_stable_null_lattice": {
                "equation": "c1+c2+2*c3+2*c4=0",
                "primitive_Z_basis_rows": [
                    [-1, 1, 0, 0],
                    [-2, 0, 1, 0],
                    [-2, 0, 0, 1],
                ],
                "rank": 3,
                "scope": "mean-null only; not pointwise or L2-null",
            },
        },
        "resource_contract": {
            "arithmetic": "exact integers only",
            "randomness": False,
            "floating_point": False,
            "finite_field_or_curve_enumeration": False,
            "Wick_contraction_branch_cap": guard.cap,
            "Wick_contraction_branches_used": guard.total,
            "Wick_ledger": dict(sorted(guard.ledger.items())),
            "maximum_trace_factors_in_one_monomial": 4,
        },
        "producer": {
            "script": Path(__file__).name,
            "source_sha256_lf_normalized": _lf_sha256(Path(__file__).resolve()),
            "note": NOTE.name,
            "note_sha256_lf_normalized": _lf_sha256(NOTE),
            "test": str(TEST.relative_to(ROOT)).replace("\\", "/"),
            "test_sha256_lf_normalized": _lf_sha256(TEST),
        },
        "firewall": (
            "Every new value is a compact Haar consequence of an imported stable-range theorem. No arithmetic family, increasing-genus limit, subgroup classification, zero law, RH, or GRH statement follows."
        ),
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    return payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", nargs="?", const=DEFAULT_OUTPUT, type=Path)
    parser.add_argument("--write", nargs="?", const=DEFAULT_OUTPUT, type=Path)
    arguments = parser.parse_args(argv)
    if arguments.check and arguments.write:
        parser.error("--check and --write are mutually exclusive")
    fixture = build_fixture()
    if arguments.check:
        expected = json.loads(arguments.check.read_text(encoding="utf-8"))
        if fixture != expected:
            raise SystemExit(
                f"high-genus interferometer fixture mismatch: {arguments.check}"
            )
        print(
            f"OK: exact high-genus interferometer stability matches {arguments.check}"
        )
    elif arguments.write:
        arguments.write.write_text(
            json.dumps(fixture, indent=2) + "\n", encoding="utf-8"
        )
        print(f"WROTE: {arguments.write}")
    else:
        print(json.dumps(fixture, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
