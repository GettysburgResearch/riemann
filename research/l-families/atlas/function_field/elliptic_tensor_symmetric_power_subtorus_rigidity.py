"""Exact rigidity of monomial subtori in the tensor/symmetric-power ladder.

The theorem is elementary and valid for every symmetric-power index.  The
bounded search is only a small exact regression in the proof-forced box; it
does not enumerate finite fields, curves, trace ranges, or polynomial models.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Sequence


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "elliptic_tensor_symmetric_power_subtorus_rigidity.json"
NOTE_PATH = HERE / "ELLIPTIC_TENSOR_SYMMETRIC_POWER_SUBTORUS_RIGIDITY.md"
TEST_PATH = ROOT / "tests" / "test_elliptic_tensor_symmetric_power_subtorus_rigidity.py"

PREDECESSOR_FIXTURE_PATH = (
    HERE / "elliptic_tensor_sym2_sym5_spectral_intersection.json"
)
PREDECESSOR_PRODUCER_PATH = (
    HERE / "elliptic_tensor_sym2_sym5_spectral_intersection.py"
)
EXPECTED_PREDECESSOR_SCHEMA = (
    "riemann.function_field.elliptic_tensor_sym2_sym5_spectral_intersection.v1"
)
EXPECTED_PREDECESSOR_PAYLOAD_SHA256 = (
    "e2c9c7ac3d1329b7b911a5214d36935d2694436cbe6d9cce551b94f8486b01ba"
)
EXPECTED_PREDECESSOR_FIXTURE_SHA256_LF = (
    "e583220e7df56765ef198d71a4a94887e8246992ba8fd9d127e8c1ce4e09cc32"
)
EXPECTED_PREDECESSOR_PRODUCER_SHA256_LF = (
    "d414807d8c2bb41ee075c5526e22b243204f3e587e5988a55f91245a99f6d9e7"
)

SCHEMA = (
    "riemann.function_field.elliptic_tensor_symmetric_power_subtorus_rigidity.v1"
)
FROZEN_MAX_R = 16
GRAPH_CERTIFICATE_MAX_R = 12
LARGE_R_DIRECT_CHECKS = (32, 64)
EXPLICIT_WEIGHT_MAX_R = 4096
DICKSON_MAX_DEGREE = 256
MAX_ABS_EXPONENT = 10**12
ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE = 40_000
REGRESSION_WEIGHT_ATOM_CAP_INCLUSIVE = 800_000

Polynomial = tuple[int, ...]


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _lf_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def _require_plain_int(name: str, value: object) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be a plain integer")
    return value


def _require_r(r: object, maximum: int = EXPLICIT_WEIGHT_MAX_R) -> int:
    value = _require_plain_int("r", r)
    if value < 1:
        raise ValueError("r must be a positive integer")
    if value > maximum:
        raise ValueError(f"r exceeds the explicit cap {maximum}")
    return value


def _require_exponent(name: str, value: object, *, nonzero: bool = False) -> int:
    exponent = _require_plain_int(name, value)
    if abs(exponent) > MAX_ABS_EXPONENT:
        raise ValueError(f"{name} exceeds the absolute cap {MAX_ABS_EXPONENT}")
    if nonzero and exponent == 0:
        raise ValueError(f"{name} must be nonzero")
    return exponent


class ResourceGuard:
    """Logical-work ledger with an exclusive hard cap."""

    def __init__(self, cap: object = ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE) -> None:
        cap_value = _require_plain_int("cap", cap)
        if cap_value < 1:
            raise ValueError("cap must be positive")
        self.cap = cap_value
        self.ledger: Counter[str] = Counter()

    @property
    def total(self) -> int:
        return sum(self.ledger.values())

    def charge(self, name: object, units: object = 1) -> None:
        if not isinstance(name, str) or not name:
            raise TypeError("resource name must be a nonempty string")
        count = _require_plain_int("units", units)
        if count < 0:
            raise ValueError("resource charge must be nonnegative")
        if self.total + count >= self.cap:
            raise RuntimeError(
                f"accounted work would meet or exceed exclusive cap {self.cap}"
            )
        self.ledger[name] += count


def _tensor_weights_unchecked(r: int, a: int, b: int) -> tuple[int, ...]:
    return tuple(
        sorted(
            epsilon * a + b * (r - 2 * j)
            for epsilon in (-1, 1)
            for j in range(r + 1)
        )
    )


def tensor_weight_multiset(r: object, a: object, b: object) -> tuple[int, ...]:
    """Sorted weights of Std(w^a) tensor Sym^r(w^b), with multiplicity."""

    r_value = _require_r(r)
    a_value = _require_exponent("a", a)
    b_value = _require_exponent("b", b)
    return _tensor_weights_unchecked(r_value, a_value, b_value)


def target_weight_multiset(r: object, c: object = 1) -> tuple[int, ...]:
    """Sorted weights of Sym^(2r+1)(w^c), with multiplicity."""

    r_value = _require_r(r)
    c_value = _require_exponent("c", c, nonzero=True)
    return tuple(
        sorted(c_value * weight for weight in range(-(2 * r_value + 1), 2 * r_value + 2, 2))
    )


def predicted_scaled_solutions(
    r: object, c: object = 1
) -> tuple[tuple[int, int], ...]:
    """All signed (a,b) solutions for a nonzero target exponent c."""

    r_value = _require_r(r)
    c_abs = abs(_require_exponent("c", c, nonzero=True))
    if c_abs * (r_value + 1) > MAX_ABS_EXPONENT:
        raise ValueError("the predicted source exponent exceeds the absolute cap")
    solutions = {
        (sign_a * c_abs * (r_value + 1), sign_b * c_abs)
        for sign_a in (-1, 1)
        for sign_b in (-1, 1)
    }
    solutions.update(
        {
            (sign_a * c_abs, sign_b * 2 * c_abs)
            for sign_a in (-1, 1)
            for sign_b in (-1, 1)
        }
    )
    return tuple(sorted(solutions))


def is_scaled_spectral_solution(
    r: object, a: object, b: object, c: object = 1
) -> bool:
    """Whether the two formal Laurent weight multisets agree exactly."""

    return tensor_weight_multiset(r, a, b) == target_weight_multiset(r, c)


def cross_branch_overlap(r: object, a: object, b: object) -> bool:
    """Whether a nonzero +a translate meets the corresponding -a translate."""

    r_value = _require_r(r)
    a_abs = abs(_require_exponent("a", a, nonzero=True))
    b_abs = abs(_require_exponent("b", b, nonzero=True))
    return a_abs % b_abs == 0 and a_abs // b_abs <= r_value


def _poly_trim(coefficients: Sequence[int]) -> Polynomial:
    output = list(coefficients)
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return tuple(output or (0,))


def dickson_trace_coefficients(degree: object) -> Polynomial:
    """Coefficients low-to-high of D_n with D_n(w+w^-1)=w^n+w^-n."""

    n = _require_plain_int("degree", degree)
    if n < 0:
        raise ValueError("degree must be nonnegative")
    if n > DICKSON_MAX_DEGREE:
        raise ValueError(f"degree exceeds the exact cap {DICKSON_MAX_DEGREE}")
    if n == 0:
        return (2,)
    previous_previous: Polynomial = (2,)
    previous: Polynomial = (0, 1)
    for _ in range(1, n):
        shifted = (0, *previous)
        width = max(len(shifted), len(previous_previous))
        current = tuple(
            (shifted[index] if index < len(shifted) else 0)
            - (previous_previous[index] if index < len(previous_previous) else 0)
            for index in range(width)
        )
        previous_previous, previous = previous, _poly_trim(current)
    return previous


def dickson_trace_value(degree: object, trace: object) -> int:
    """Evaluate D_n by the same exact recurrence, without floating point."""

    n = _require_plain_int("degree", degree)
    if n < 0:
        raise ValueError("degree must be nonnegative")
    if n > DICKSON_MAX_DEGREE:
        raise ValueError(f"degree exceeds the exact cap {DICKSON_MAX_DEGREE}")
    z = _require_exponent("trace", trace)
    if n == 0:
        return 2
    previous_previous, previous = 2, z
    for _ in range(1, n):
        previous_previous, previous = previous, z * previous - previous_previous
    return previous


def _load_locked_predecessor() -> dict[str, object]:
    if _lf_sha256(PREDECESSOR_PRODUCER_PATH) != EXPECTED_PREDECESSOR_PRODUCER_SHA256_LF:
        raise RuntimeError("locked predecessor producer LF hash mismatch")
    if _lf_sha256(PREDECESSOR_FIXTURE_PATH) != EXPECTED_PREDECESSOR_FIXTURE_SHA256_LF:
        raise RuntimeError("locked predecessor fixture LF hash mismatch")
    fixture = json.loads(PREDECESSOR_FIXTURE_PATH.read_text(encoding="utf-8"))
    if fixture.get("schema") != EXPECTED_PREDECESSOR_SCHEMA:
        raise RuntimeError("locked predecessor schema mismatch")
    if fixture.get("payload_sha256") != EXPECTED_PREDECESSOR_PAYLOAD_SHA256:
        raise RuntimeError("locked predecessor payload mismatch")
    unhashed = dict(fixture)
    claimed = unhashed.pop("payload_sha256", None)
    if claimed != _canonical_sha256(unhashed):
        raise RuntimeError("locked predecessor canonical payload is inconsistent")
    return fixture


def _bounded_regression(
    maximum_r: int, guard: ResourceGuard
) -> tuple[list[dict[str, object]], int]:
    rows: list[dict[str, object]] = []
    total_weight_atoms = 0
    for r in range(1, maximum_r + 1):
        bound = 2 * r + 1
        side = 2 * bound + 1
        candidate_pairs = side * side
        emitted_weight_atoms = candidate_pairs * 2 * (r + 1)
        if total_weight_atoms + emitted_weight_atoms > REGRESSION_WEIGHT_ATOM_CAP_INCLUSIVE:
            raise RuntimeError("bounded regression would exceed the weight-atom cap")
        guard.charge("bounded_signed_candidate_pairs", candidate_pairs)
        total_weight_atoms += emitted_weight_atoms

        target = tuple(range(-bound, bound + 1, 2))
        found: list[tuple[int, int]] = []
        for a in range(-bound, bound + 1):
            for b in range(-bound, bound + 1):
                if _tensor_weights_unchecked(r, a, b) == target:
                    found.append((a, b))
        expected = list(predicted_scaled_solutions(r))
        if found != expected:
            raise ArithmeticError(
                f"subtorus classification regression failed at r={r}: {found} != {expected}"
            )
        guard.charge("closed_form_classification_rows")
        rows.append(
            {
                "r": r,
                "proof_forced_coordinate_bound": bound,
                "signed_candidate_pairs_checked": candidate_pairs,
                "weight_atoms_emitted": emitted_weight_atoms,
                "solution_count": len(found),
                "solutions_a_b": [list(pair) for pair in found],
            }
        )
    return rows, total_weight_atoms


def _scaled_graph_certificates(guard: ResourceGuard) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for r in range(1, GRAPH_CERTIFICATE_MAX_R + 1):
        dickson = dickson_trace_coefficients(r + 1)
        guard.charge("dickson_recurrence_steps", r)
        scale_rows = []
        for c in (-3, -1, 1, 2, 4):
            target = target_weight_multiset(r, c)
            solutions = predicted_scaled_solutions(r, c)
            for a, b in solutions:
                if _tensor_weights_unchecked(r, a, b) != target:
                    raise ArithmeticError("scaled canonical graph certificate failed")
            guard.charge("scaled_canonical_solution_checks", len(solutions))
            scale_rows.append(
                {
                    "target_exponent_c": c,
                    "solutions_a_b": [list(pair) for pair in solutions],
                }
            )
        rows.append(
            {
                "r": r,
                "D_r_plus_1_coefficients_low_to_high": list(dickson),
                "scaled_solution_rows": scale_rows,
            }
        )
    return rows


def _large_r_direct_certificates(guard: ResourceGuard) -> list[dict[str, object]]:
    """Check only the theorem's eight canonical pairs at two larger r values."""

    rows: list[dict[str, object]] = []
    for r in LARGE_R_DIRECT_CHECKS:
        target = target_weight_multiset(r)
        solutions = predicted_scaled_solutions(r)
        for a, b in solutions:
            if _tensor_weights_unchecked(r, a, b) != target:
                raise ArithmeticError("large-r direct canonical certificate failed")
        guard.charge("large_r_direct_canonical_solution_checks", len(solutions))
        rows.append(
            {
                "r": r,
                "candidate_box_enumerated": False,
                "canonical_signed_solutions_checked": len(solutions),
                "weight_count_per_solution": len(target),
                "solutions_a_b": [list(pair) for pair in solutions],
            }
        )
    return rows


def _owned_file_locks() -> dict[str, dict[str, str]]:
    return {
        "note": {
            "path": _relative(NOTE_PATH),
            "sha256_lf_normalized": _lf_sha256(NOTE_PATH),
        },
        "producer": {
            "path": _relative(Path(__file__).resolve()),
            "sha256_lf_normalized": _lf_sha256(Path(__file__).resolve()),
        },
        "test": {
            "path": _relative(TEST_PATH),
            "sha256_lf_normalized": _lf_sha256(TEST_PATH),
        },
    }


def build_fixture(maximum_r: object = FROZEN_MAX_R) -> dict[str, object]:
    """Build the canonical source-locked rigidity packet."""

    max_r = _require_plain_int("maximum_r", maximum_r)
    if max_r != FROZEN_MAX_R:
        raise ValueError(f"maximum_r must be exactly {FROZEN_MAX_R}")
    _load_locked_predecessor()
    guard = ResourceGuard()
    guard.charge("locked_predecessor_files_verified", 2)
    regression_rows, emitted_weight_atoms = _bounded_regression(max_r, guard)
    graph_rows = _scaled_graph_certificates(guard)
    large_r_rows = _large_r_direct_certificates(guard)
    guard.charge("named_degenerate_and_swap_certificates", 2)

    fixture: dict[str, object] = {
        "schema": SCHEMA,
        "packet_id": "FUNCTION_FIELD.ELLIPTIC.TENSOR_SYMMETRIC_POWER.SUBTORUS_RIGIDITY.V1",
        "status": "EXACT_ALL_R_INTEGER_MONOMIAL_SUBTORUS_CLASSIFICATION_PLUS_BOUNDED_REPLAY",
        "rigor_level": {
            "fixed_target_theorem": "PROVED_FOR_EVERY_INTEGER_r_AT_LEAST_1",
            "scaled_target_theorem": "PROVED_FOR_EVERY_NONZERO_INTEGER_c",
            "bounded_replay": "EXACT_STDLIB_REGRESSION_NOT_USED_AS_THE_PROOF",
            "full_rational_intersection": "NOT_CLASSIFIED",
            "arithmetic_realization_or_novelty": "NOT_INFERRED",
        },
        "formal_weight_problem": {
            "source": "W_r(a,b)={epsilon*a+b*(r-2j):epsilon=+/-1,0<=j<=r}, with multiplicity",
            "primitive_target": "O_r={-(2r+1),-(2r-1),...,2r+1}, with multiplicity one",
            "scaled_target": "c*O_r is the weight multiset of Sym^(2r+1)(w^c)",
            "meaning": "equality of Laurent-character multisets for a formal or generic torus parameter w",
        },
        "primitive_subtorus_rigidity_theorem": {
            "scope": "every r>=1 and all integers a,b",
            "classification": "W_r(a,b)=O_r iff (|a|,|b|)=(r+1,1) or (1,2)",
            "all_signed_solutions": "(a,b)=(sigma*(r+1),tau) or (sigma,2*tau), independently sigma,tau in {+/-1}",
            "proof": [
                "independent Weyl involutions a->-a and b->-b preserve W_r, so put A=|a| and B=|b|",
                "A=0 repeats every b-branch weight and B=0 repeats +/-A exactly r+1 times, so multiplicity-freeness forces A,B>=1",
                "the maximum source weight is A+rB and the maximum target weight is 2r+1, hence A+rB=2r+1",
                "A>=1 gives B<=2; B=1 forces A=r+1 and B=2 forces A=1",
                "the first pair splits O_r into its positive and negative halves, while the second pair interlaces its even- and odd-indexed weights",
            ],
            "no_search_dependency": "the maximum-weight argument is the proof; the r<=16 enumeration is regression only",
        },
        "scaled_subtorus_rigidity_theorem": {
            "scope": "every r>=1 and every nonzero integer c",
            "classification": "W_r(a,b)=c*O_r iff (|a|,|b|)=|c|*(r+1,1) or |c|*(1,2)",
            "divisibility_proof": (
                "successive weights in either source progression differ by 2b, "
                "whereas every target difference is divisible by 2c; hence c divides b. "
                "One source weight then forces c to divide a. Divide by |c| and apply "
                "the primitive theorem."
            ),
            "interpretation": "all integer one-parameter subtorus homomorphisms, modulo a common nonprimitive reparametrization",
            "c_zero_corner": "if c=0, equality holds only for a=b=0; this collapsed map is not a subtorus and the producer API refuses it",
        },
        "multiplicity_and_symmetry_audit": {
            "cross_branch_overlap": "for A,B>0 the +A and -A progressions meet iff A/B is an integer in {1,...,r}",
            "overlap_consequence": "any meeting creates multiplicity at least two, forbidden by O_r",
            "canonical_nonoverlap": "A/B=r+1 in the first family and A/B=1/2 in the second",
            "independent_Weyl_signs": "a->-a swaps epsilon and b->-b reverses j; the two signs are independent",
            "torus_inversion": "w->w^-1 gives simultaneous exponent inversion, already contained in the independent Weyl signs",
            "r_1_swap_orbit": "W_1(a,b)=W_1(b,a), so the two canonical classes form one orbit under factor swap",
            "r_greater_than_1": "the factors have dimensions 2 and r+1; swapping is not a symmetry and swaps no classified solution to a solution",
        },
        "dickson_chebyshev_graph_equations": {
            "recurrence": "D_0(z)=2, D_1(z)=z, D_(n+1)(z)=z*D_n(z)-D_(n-1)(z)",
            "torus_identity": "if z=w+w^-1 then D_n(z)=w^n+w^-n",
            "first_graph": "x=D_(r+1)(z), y=z, corresponding to u=w^(r+1), v=w",
            "second_graph": "x=z, y=D_2(z)=z^2-2, corresponding to u=w, v=w^2",
            "Weyl_note": "negative a or b gives the same trace equation because D_(-n)=D_n",
            "central_sign_note": (
                "Weyl inversion is not multiplication by -I. With target w fixed, "
                "source central signs delta_u,delta_v are allowed exactly when "
                "delta_u+r*delta_v=0 mod 2; at r=2 this recovers the independent +/-y branches of the predecessor."
            ),
            "exact_bounded_coefficients_and_scaled_checks": graph_rows,
        },
        "raw_weight_bookkeeping": {
            "source_weight": "Std(E_A) tensor Sym^r(E_B) has motivic weight r+1",
            "target_weight": "Sym^(2r+1)(E_C) has motivic weight 2r+1",
            "typed_comparison": "P_source(q^(r/2)*T)=P_target(T)",
            "even_r": "q^(r/2) is an integer power of q",
            "odd_r": "the raw formula requires a chosen square root of q; the normalized torus theorem itself does not",
        },
        "predecessor_source_lock": {
            "fixture_path": _relative(PREDECESSOR_FIXTURE_PATH),
            "fixture_schema": EXPECTED_PREDECESSOR_SCHEMA,
            "fixture_payload_sha256": EXPECTED_PREDECESSOR_PAYLOAD_SHA256,
            "fixture_sha256_lf_normalized": EXPECTED_PREDECESSOR_FIXTURE_SHA256_LF,
            "producer_path": _relative(PREDECESSOR_PRODUCER_PATH),
            "producer_sha256_lf_normalized": EXPECTED_PREDECESSOR_PRODUCER_SHA256_LF,
            "use": "lock the r=2 complete rational intersection packet whose two universal graph identities are sharpened here",
        },
        "bounded_exact_regression": {
            "maximum_r": max_r,
            "search_box": "every signed pair |a|,|b|<=2r+1 for each 1<=r<=16",
            "box_is_proof_forced": "a solution has |a|+r|b|=2r+1 unless a or b is zero, already excluded by multiplicity",
            "rows": regression_rows,
            "finite_search_is_not_the_proof": True,
        },
        "large_r_direct_canonical_checks": {
            "purpose": "retain long-r regression coverage without enumerating either surrounding candidate box",
            "rows": large_r_rows,
        },
        "source_and_owned_file_locks": {
            "owned_file_locks": _owned_file_locks(),
            "authentication": "the predecessor fixture is schema-, canonical-payload-, payload-, and LF-file-locked; its producer and all three owned source files are LF-file-locked",
        },
        "resource_contract": {
            "exclusive_accounted_work_unit_cap": guard.cap,
            "accounted_work_unit_ledger": {
                **dict(sorted(guard.ledger.items())),
                "total_accounted_work_units": guard.total,
            },
            "logical_unit_definition": "one signed candidate pair, one canonical scaled-solution comparison, one recurrence step, one locked file, or one named theorem row; not CPU instructions",
            "bounded_weight_atoms_emitted": emitted_weight_atoms,
            "bounded_weight_atom_cap_inclusive": REGRESSION_WEIGHT_ATOM_CAP_INCLUSIVE,
            "maximum_explicit_r": EXPLICIT_WEIGHT_MAX_R,
            "field_curve_polynomial_model_or_trace_range_enumerations": 0,
            "random_samples": 0,
            "floating_point_results": 0,
            "runtime_symbolic_packages": 0,
            "arithmetic": "standard-library exact Python integers and sorted tuples only",
        },
        "scope_firewall": {
            "generic_monomial_only": "the theorem classifies integer cocharacters of a formal one-dimensional torus, not arbitrary rational or algebraic curves in trace space",
            "roots_of_unity": "at torsion w, exponents are compared modulo its order and extra cyclotomic coincidences or multiplicities can occur",
            "full_rational_intersection": "the theorem does not classify all rational coefficient solutions for r other than the locked r=2 predecessor",
            "no_representation_homomorphism": "spectral equality along a subtorus is not an isomorphism of the ambient source representations",
            "no_arithmetic_realization": "no Hasse-lattice point is asserted to arise from linked elliptic curves, a variety, or a compatible family",
            "no_local_to_global_upgrade": "no motive, correspondence, Euler product, automorphy, modularity, or global family is constructed",
            "no_novelty_priority_claim": "the elementary Laurent-weight rigidity is recorded without a literature-priority claim",
            "no_RH_GRH_or_zero_claim": "the local identity has no asserted consequence for analytic continuation, zeros, RH, or GRH",
        },
        "next_targets": [
            "classify cyclotomic residuals for each r after reducing exponents modulo the torsion order",
            "seek nonmonomial positive-dimensional components of the full rational coefficient intersection",
            "test whether either rigid graph can occur coherently across primes in a geometric compatible family",
        ],
    }
    if guard.total >= guard.cap:
        raise RuntimeError("accounted resource cap was not respected")
    if emitted_weight_atoms > REGRESSION_WEIGHT_ATOM_CAP_INCLUSIVE:
        raise RuntimeError("weight-atom cap was not respected")
    fixture["payload_sha256"] = _canonical_sha256(fixture)
    return fixture


def _serialized_fixture() -> str:
    return json.dumps(build_fixture(), indent=2, sort_keys=True) + "\n"


def _write(path: Path) -> None:
    path.write_text(_serialized_fixture(), encoding="utf-8")
    print(f"wrote {path}")


def _check(path: Path) -> None:
    if not path.exists() or path.read_text(encoding="utf-8") != _serialized_fixture():
        raise SystemExit(f"fixture is stale: {path}")
    print(f"fixture is current: {path}")


def main(argv: Sequence[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--write", nargs="?", const=OUTPUT_PATH, type=Path)
    action.add_argument("--check", nargs="?", const=OUTPUT_PATH, type=Path)
    arguments = parser.parse_args(argv)
    if arguments.write is not None:
        _write(arguments.write)
    elif arguments.check is not None:
        _check(arguments.check)
    else:
        print(json.dumps(build_fixture(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
