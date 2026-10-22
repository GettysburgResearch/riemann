"""Exact cyclotomic aliases of complete elliptic symmetric-power spectra.

The packet is representation-theoretic.  It enumerates no field, curve, or
polynomial model.  Its bounded replay uses only integer residue counters and
small polynomial arithmetic from the Python standard library.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from collections import Counter
from pathlib import Path
from typing import Iterable, Sequence


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "elliptic_symmetric_power_cyclotomic_spectral_aliases.json"
NOTE_PATH = HERE / "ELLIPTIC_SYMMETRIC_POWER_CYCLOTOMIC_SPECTRAL_ALIASES.md"
TEST_PATH = ROOT / "tests" / "test_elliptic_symmetric_power_cyclotomic_spectral_aliases.py"
SOURCE_FIXTURE_PATH = HERE / "elliptic_symmetric_power_trace_aliasing.json"
SOURCE_PRODUCER_PATH = HERE / "elliptic_symmetric_power_trace_aliasing.py"

EXPECTED_SOURCE_SCHEMA = "riemann.function_field.elliptic_symmetric_power_trace_aliasing.v1"
EXPECTED_SOURCE_PAYLOAD_SHA256 = (
    "046f76f43a2af3ac296f5c18c258e61f138e122bee38ec618af489e7e3a9e50e"
)
EXPECTED_SOURCE_FIXTURE_SHA256_LF = (
    "7a6e249fd696f9526154375f60bd97c2c40d251791f08eec6ecdc70b3177b941"
)
EXPECTED_SOURCE_PRODUCER_SHA256_LF = (
    "74d3f8cb65a99ab0c5c7943df6a4aba9f29ba91f6876ea935e0673cfd1dcf043"
)

FROZEN_ODD_ORDER_MAX = 51
EXAMPLE_ORDERS = (5, 7, 9, 11)
ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE = 100_000

# Coefficients are low-to-high.  These are verified below from the recurrence
# C_0=2, C_1=X, C_n=X*C_(n-1)-C_(n-2), where C_n(z+z^-1)=z^n+z^-n.
EXPECTED_PRIMITIVE_TRACE_POLYNOMIALS = {
    5: (-1, 1, 1),
    7: (-1, -2, 1, 1),
    9: (1, -3, 0, 1),
    11: (1, 3, -3, -4, 1, 1),
}


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _lf_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def _require_plain_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be a plain integer")


def _require_odd_order(order: int) -> None:
    _require_plain_int("order", order)
    if order < 3 or order % 2 == 0:
        raise ValueError("order must be an odd integer at least 3")


def _require_nonnegative_m(m: int) -> None:
    _require_plain_int("m", m)
    if m < 0:
        raise ValueError("m must be nonnegative")


class ResourceGuard:
    """Ledger for bounded high-level exact checks."""

    def __init__(self, cap: int = ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE) -> None:
        _require_plain_int("cap", cap)
        if cap <= 0:
            raise ValueError("cap must be positive")
        self.cap = cap
        self.ledger: Counter[str] = Counter()

    @property
    def total(self) -> int:
        return sum(self.ledger.values())

    def charge(self, name: str, units: int = 1) -> None:
        _require_plain_int("units", units)
        if units < 0:
            raise ValueError("resource charge must be nonnegative")
        if self.total + units >= self.cap:
            raise RuntimeError(
                f"accounted work would meet or exceed exclusive cap {self.cap}"
            )
        self.ledger[name] += units


def units_modulo(order: int) -> tuple[int, ...]:
    _require_odd_order(order)
    return tuple(a for a in range(1, order) if math.gcd(a, order) == 1)


def exponent_multiplicities(order: int, m: int) -> Counter[int]:
    """Residues of m,m-2,...,-m modulo an odd order."""

    _require_odd_order(order)
    _require_nonnegative_m(m)
    return Counter((m - 2 * j) % order for j in range(m + 1))


def remainder_residues(order: int, m: int) -> tuple[int, ...]:
    """The nonuniform remainder after removing complete residue cycles."""

    _require_odd_order(order)
    _require_nonnegative_m(m)
    _, s = divmod(m + 1, order)
    return tuple((s - 1 - 2 * j) % order for j in range(s))


def scaled_remainder_interval(order: int, m: int) -> tuple[int, ...]:
    """Scale the remainder by 2^-1; the result is a cyclic interval."""

    inverse_two = pow(2, -1, order)
    return tuple((inverse_two * value) % order for value in remainder_residues(order, m))


def interval_autocorrelation(order: int, length: int, displacement: int) -> int:
    """Autocorrelation of {0,...,length-1} in Z/order Z."""

    _require_odd_order(order)
    _require_plain_int("length", length)
    _require_plain_int("displacement", displacement)
    if not 0 <= length <= order:
        raise ValueError("interval length must lie between 0 and order")
    d = displacement % order
    if d == 0:
        return length
    return max(0, length - d) + max(0, length - (order - d))


def exact_stabilizer(order: int, m: int) -> tuple[int, ...]:
    """Units a for which the complete spectra at zeta and zeta^a agree."""

    counts = exponent_multiplicities(order, m)
    stabilizer = []
    for a in units_modulo(order):
        transformed = Counter({(a * residue) % order: count for residue, count in counts.items()})
        if transformed == counts:
            stabilizer.append(a)
    return tuple(stabilizer)


def predicted_stabilizer(order: int, m: int) -> tuple[int, ...]:
    """Closed stabilizer theorem for primitive odd-order classes."""

    _require_odd_order(order)
    _require_nonnegative_m(m)
    if m % order in ((order - 2) % order, order - 1, 0):
        return units_modulo(order)
    return (1, order - 1)


def exponent_edge_signature(order: int, m: int) -> tuple[int, ...]:
    """Multiplicity vector indexed by residues 0,...,order-1."""

    counts = exponent_multiplicities(order, m)
    return tuple(counts[residue] for residue in range(order))


def _poly_trim(coefficients: Iterable[int]) -> tuple[int, ...]:
    output = list(coefficients)
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return tuple(output or (0,))


def _poly_add(left: Sequence[int], right: Sequence[int]) -> tuple[int, ...]:
    size = max(len(left), len(right))
    return _poly_trim(
        (left[i] if i < len(left) else 0) + (right[i] if i < len(right) else 0)
        for i in range(size)
    )


def _poly_scale(coefficients: Sequence[int], scalar: int) -> tuple[int, ...]:
    return _poly_trim(scalar * value for value in coefficients)


def _poly_mul(left: Sequence[int], right: Sequence[int]) -> tuple[int, ...]:
    output = [0] * (len(left) + len(right) - 1)
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            output[i + j] += first * second
    return _poly_trim(output)


def trace_chebyshev_polynomial(order: int) -> tuple[int, ...]:
    """C_order with C_order(z+z^-1)=z^order+z^-order."""

    _require_plain_int("order", order)
    if order < 0:
        raise ValueError("order must be nonnegative")
    if order == 0:
        return (2,)
    previous_previous = (2,)
    previous = (0, 1)
    for _ in range(2, order + 1):
        current = _poly_add(_poly_mul((0, 1), previous), _poly_scale(previous_previous, -1))
        previous_previous, previous = previous, current
    return previous


def _monic_divides_mod(
    dividend: Sequence[int], divisor: Sequence[int], prime: int
) -> bool:
    remainder = [value % prime for value in _poly_trim(dividend)]
    divisor_mod = [value % prime for value in _poly_trim(divisor)]
    if divisor_mod[-1] != 1:
        raise ValueError("modular trial divisor must be monic")
    while len(remainder) >= len(divisor_mod):
        coefficient = remainder[-1]
        shift = len(remainder) - len(divisor_mod)
        if coefficient:
            for index, value in enumerate(divisor_mod):
                remainder[index + shift] = (
                    remainder[index + shift] - coefficient * value
                ) % prime
        while remainder and remainder[-1] == 0:
            remainder.pop()
    return not remainder


def irreducibility_certificate_mod_two(coefficients: Sequence[int]) -> dict[str, object]:
    """Exhaust all possible smaller monic factors over F_2."""

    polynomial = _poly_trim(coefficients)
    if len(polynomial) < 2 or polynomial[-1] % 2 != 1:
        raise ValueError("certificate requires a positive-degree monic polynomial")
    degree = len(polynomial) - 1
    tested = 0
    for trial_degree in range(1, degree // 2 + 1):
        for lower in itertools.product(range(2), repeat=trial_degree):
            tested += 1
            trial = tuple(lower) + (1,)
            if _monic_divides_mod(polynomial, trial, 2):
                raise ArithmeticError(f"polynomial has a mod-2 factor {trial}")
    return {
        "prime": 2,
        "degree": degree,
        "monic_candidate_degrees": list(range(1, degree // 2 + 1)),
        "monic_candidates_exhausted": tested,
        "proper_factor_found": False,
        "conclusion": "irreducible over F_2, hence irreducible over Q by Gauss's lemma",
    }


def primitive_trace_certificate(order: int) -> dict[str, object]:
    """Exact minimal-polynomial certificate for one frozen odd order."""

    if order not in EXPECTED_PRIMITIVE_TRACE_POLYNOMIALS:
        raise ValueError(f"order must be one of {EXAMPLE_ORDERS}")
    minimal = EXPECTED_PRIMITIVE_TRACE_POLYNOMIALS[order]
    left = _poly_add(trace_chebyshev_polynomial(order), (-2,))
    right = _poly_mul((-2, 1), _poly_mul(minimal, minimal))
    lower_order_factors: list[tuple[int, ...]] = []
    if order == 9:
        lower_order_factors.append((1, 1))
        right = _poly_mul(right, _poly_mul((1, 1), (1, 1)))
    if left != right:
        raise ArithmeticError(f"cyclotomic trace factorization failed at order {order}")
    representatives = tuple(
        a for a in range(1, (order + 1) // 2) if math.gcd(a, order) == 1
    )
    if 2 * len(representatives) != len(units_modulo(order)):
        raise ArithmeticError("primitive trace class count failed")
    return {
        "root_order": order,
        "primitive_class_representatives_modulo_inversion": list(representatives),
        "primitive_class_count": len(representatives),
        "minimal_polynomial_coefficients_low_to_high": list(minimal),
        "trace_recurrence_polynomial_C_N_minus_2_low_to_high": list(left),
        "factorization": (
            "C_9(X)-2=(X-2)*(X+1)^2*M_9(X)^2"
            if order == 9
            else f"C_{order}(X)-2=(X-2)*M_{order}(X)^2"
        ),
        "lower_order_trace_factors": [list(value) for value in lower_order_factors],
        "irreducibility": irreducibility_certificate_mod_two(minimal),
        "first_alias_power": order - 2,
        "shared_factor_coefficients_T0_up": [1] * order,
    }


def special_factor_certificate(order: int) -> dict[str, object]:
    """The three adjacent universal factor identities for primitive order N."""

    _require_odd_order(order)
    if order < 5:
        raise ValueError("special examples require odd order at least 5")
    signatures = {
        "N_minus_2": exponent_edge_signature(order, order - 2),
        "N_minus_1": exponent_edge_signature(order, order - 1),
        "N": exponent_edge_signature(order, order),
    }
    expected = {
        "N_minus_2": (0,) + (1,) * (order - 1),
        "N_minus_1": (1,) * order,
        "N": (2,) + (1,) * (order - 1),
    }
    if signatures != expected:
        raise ArithmeticError(f"special exponent multiplicities failed at order {order}")

    factor_n_minus_1 = [0] * (order + 1)
    factor_n_minus_1[0] = 1
    factor_n_minus_1[order] = -1
    factor_n = [0] * (order + 2)
    factor_n[0] = 1
    factor_n[1] = -1
    factor_n[order] = -1
    factor_n[order + 1] = 1
    return {
        "root_order_N": order,
        "primitive_power_condition": "gcd(a,N)=1; all compared classes use the same scalar lift",
        "m_N_minus_2": {
            "residue_multiplicities_0_through_N_minus_1": list(signatures["N_minus_2"]),
            "spectrum": "every nontrivial N-th root exactly once",
            "factor_SL2": "(1-T^N)/(1-T)",
            "coefficients_T0_through_T_to_N_minus_1": [1] * order,
        },
        "m_N_minus_1": {
            "residue_multiplicities_0_through_N_minus_1": list(signatures["N_minus_1"]),
            "spectrum": "every N-th root exactly once",
            "factor_SL2": "1-T^N",
            "coefficients_T0_through_T_to_N": factor_n_minus_1,
        },
        "m_N": {
            "residue_multiplicities_0_through_N_minus_1": list(signatures["N"]),
            "spectrum": "every N-th root exactly once, with 1 occurring once more",
            "factor_SL2": "(1-T)*(1-T^N)",
            "coefficients_T0_through_T_to_N_plus_1": factor_n,
        },
        "fixed_determinant_scalar_substitution": "for eigenvalues rho*zeta^a,rho*zeta^-a with common rho^2=q, replace T by rho^m*T in the displayed SL2 factor",
        "lift_sign_audit": {
            "same_lift": "the scalar rho^m is identical for all primitive powers a, so all three factor equalities are exact",
            "negative_lift": "replacing rho by -rho multiplies every Sym^m eigenvalue by (-1)^m",
            "m_N_minus_1": "N-1 is even, so the negative lift has the same factor",
            "m_N_minus_2_and_m_N": "N-2 and N are odd, so the negative lift sends F(T) to F(-T) and is not silently included",
        },
    }


def _load_locked_source() -> dict[str, object]:
    if _lf_sha256(SOURCE_FIXTURE_PATH) != EXPECTED_SOURCE_FIXTURE_SHA256_LF:
        raise RuntimeError("locked scalar-trace fixture file hash mismatch")
    if _lf_sha256(SOURCE_PRODUCER_PATH) != EXPECTED_SOURCE_PRODUCER_SHA256_LF:
        raise RuntimeError("locked scalar-trace producer file hash mismatch")
    source = json.loads(SOURCE_FIXTURE_PATH.read_text(encoding="utf-8"))
    if source.get("schema") != EXPECTED_SOURCE_SCHEMA:
        raise RuntimeError("locked scalar-trace schema mismatch")
    claimed = source.get("payload_sha256")
    if claimed != EXPECTED_SOURCE_PAYLOAD_SHA256:
        raise RuntimeError("locked scalar-trace payload hash mismatch")
    unhashed = dict(source)
    unhashed.pop("payload_sha256", None)
    if _canonical_sha256(unhashed) != claimed:
        raise RuntimeError("locked scalar-trace payload is internally inconsistent")
    return source


def _file_lock(path: Path, *, payload_sha256: str | None = None) -> dict[str, object]:
    lock: dict[str, object] = {
        "path": _relative(path),
        "sha256_lf_normalized": _lf_sha256(path),
    }
    if payload_sha256 is not None:
        lock["payload_sha256"] = payload_sha256
    return lock


def _bounded_regression(max_order: int, guard: ResourceGuard) -> list[dict[str, object]]:
    rows = []
    for order in range(3, max_order + 1, 2):
        units = units_modulo(order)
        nontrivial_observed: set[int] = set()
        candidate_checks = 0
        for m in range(2 * order):
            actual = exact_stabilizer(order, m)
            expected = predicted_stabilizer(order, m)
            guard.charge("bounded_stabilizer_unit_candidates", len(units))
            candidate_checks += len(units)
            if actual != expected:
                raise ArithmeticError(
                    f"stabilizer theorem failed for order={order}, m={m}: {actual} != {expected}"
                )
            if any(a not in (1, order - 1) for a in actual):
                nontrivial_observed.add(m % order)

        autocorrelation_checks = 0
        for length in range(2, order - 1):
            interval = set(range(length))
            for displacement in range(1, order):
                direct = len(
                    interval
                    & {(value + displacement) % order for value in interval}
                )
                closed = interval_autocorrelation(order, length, displacement)
                guard.charge("bounded_autocorrelation_formula_checks")
                autocorrelation_checks += 1
                if direct != closed:
                    raise ArithmeticError("cyclic interval autocorrelation formula failed")
                if displacement not in (1, order - 1) and closed >= length - 1:
                    raise ArithmeticError("autocorrelation maximum was not unique at +/-1")

        expected_nontrivial = (
            [order - 2, order - 1, 0]
            if any(a not in (1, order - 1) for a in units)
            else []
        )
        observed_ordered = [
            residue for residue in (order - 2, order - 1, 0) if residue in nontrivial_observed
        ]
        if observed_ordered != expected_nontrivial:
            raise ArithmeticError("bounded nontrivial alias residue signature changed")
        rows.append(
            {
                "odd_order": order,
                "unit_group": list(units),
                "tested_m_range_inclusive": [0, 2 * order - 1],
                "stabilizer_unit_candidate_checks": candidate_checks,
                "autocorrelation_formula_checks": autocorrelation_checks,
                "theorem_special_m_residues": [order - 2, order - 1, 0],
                "observed_nontrivial_alias_m_residues": observed_ordered,
            }
        )
    return rows


def build_fixture(max_odd_order: int = FROZEN_ODD_ORDER_MAX) -> dict[str, object]:
    """Build the canonical exact packet."""

    _require_plain_int("max_odd_order", max_odd_order)
    if max_odd_order != FROZEN_ODD_ORDER_MAX:
        raise ValueError(f"max_odd_order must be exactly {FROZEN_ODD_ORDER_MAX}")
    source = _load_locked_source()
    guard = ResourceGuard()
    guard.charge("locked_source_files_verified", 2)

    bounded_rows = _bounded_regression(max_odd_order, guard)
    trace_certificates = []
    factor_certificates = []
    for order in EXAMPLE_ORDERS:
        trace_certificates.append(primitive_trace_certificate(order))
        factor_certificates.append(special_factor_certificate(order))
        guard.charge("cyclotomic_trace_factorizations")
        guard.charge("special_factor_identity_certificates", 3)

    fixture: dict[str, object] = {
        "schema": "riemann.function_field.elliptic_symmetric_power_cyclotomic_spectral_aliases.v1",
        "packet_id": "FUNCTION_FIELD.ELLIPTIC.SYMMETRIC_POWER.CYCLOTOMIC_SPECTRAL_ALIASES.V1",
        "status": "EXACT_ODD_ORDER_STABILIZER_THEOREM_PLUS_BOUNDED_DEPENDENCY_FREE_REPLAY",
        "rigor_level": {
            "odd_order_stabilizer": "PROVED_FOR_EVERY_ODD N BY_COMPLETE_CYCLES_AND_CYCLIC_INTERVAL_AUTOCORRELATION",
            "special_factor_identities": "PROVED_BY_EXACT_EXPONENT_MULTIPLICITIES_AND_X_N_MINUS_1_ROOT_FACTORIZATION",
            "minimal_trace_polynomials": "CERTIFIED_BY_C_N_MINUS_2_FACTORIZATION_AND_EXHAUSTIVE_MOD_2_IRREDUCIBILITY",
            "rational_recovery": "PROVED_FROM_THE_INTRINSIC_SPECTRAL_QUOTIENT_GROUP_AND_RATIONAL_ROOT_OF_UNITY_TRACES",
            "global_arithmetic_or_novelty": "NOT_INFERRED",
        },
        "spectral_setup": {
            "SL2_class": "diag(z,z^-1), modulo z~z^-1",
            "complete_Sym_m_spectrum": "S_m(z)={z^(m-2j):0<=j<=m}, with multiplicity",
            "complete_factor": "F_m(z;T)=product_(j=0)^m (1-z^(m-2j)*T)",
            "primitive_comparison": "z=zeta and w=zeta^a for zeta of odd order N and gcd(a,N)=1",
            "distinction_from_upstream": "the bound source classifies one scalar character tau_m; this packet classifies equality of the complete eigenvalue multiset in a cyclotomic stratum",
        },
        "odd_order_stabilizer_theorem": {
            "scope": "every odd N>=3, every m>=0, every unit a modulo N",
            "statement": "S_m(zeta)=S_m(zeta^a) iff a=+/-1 mod N or m mod N belongs to {N-2,N-1,0}",
            "complete_cycle_decomposition": "if m+1=kN+s with 0<=s<N, the exponent multiset is k copies of every residue plus R_s={s-1-2j:0<=j<s}",
            "scaling_step": "because N is odd, multiplication by 2^-1 turns R_s into a cyclic interval of length s",
            "interior_proof": {
                "range": "2<=s<=N-2",
                "autocorrelation": "C_s(d)=max(0,s-d)+max(0,s-(N-d)) for 1<=d<=N-1",
                "unique_maximum": "C_s(d)=s-1 exactly for d=+/-1; every other nonzero d gives at most s-2",
                "stabilizer_conclusion": "aR_s=R_s implies C_s(a)=C_s(1)=s-1, hence a=+/-1",
            },
            "edge_cases": {
                "s_0_equivalently_m_N_minus_1": "R_s is empty; every unit stabilizes it",
                "s_1_equivalently_m_0": "R_s={0}; every unit stabilizes it",
                "s_N_minus_1_equivalently_m_N_minus_2": "R_s is every nonzero residue; every unit stabilizes it",
            },
            "class_level_nuance": "a=+/-1 is one semisimple conjugacy class; the three exceptional m residues collapse all primitive classes modulo inversion",
            "nontriviality_boundary": "for N=3 there is only one primitive class modulo inversion, so the collapse is vacuous; every odd N>=5 has genuine non-sign primitive-class aliases in the three exceptional residues",
        },
        "special_factor_identities": factor_certificates,
        "orders_5_7_9_11": trace_certificates,
        "rational_fixed_determinant_recovery_theorem": {
            "hypotheses": "m>=1 and x,y,q are rational with q!=0; P_x(U)=U^2-xU+q and P_y(U)=U^2-yU+q are semisimple over an algebraic closure",
            "statement": "equality of the complete Sym^m factors implies x=+y or x=-y",
            "quotient_group_certificate": {
                "spectrum": "A_x={alpha^(m-j)*beta^j:0<=j<=m}, alpha*beta=q",
                "intrinsic_group": "Gamma(A_x)=<u/v:u,v in A_x>=<alpha/beta>; the j=0 and j=1 terms exhibit the generator",
                "consequence": "equal complete factors give equal multisets and hence equal eigenratio groups, including repeated spectra and m=1",
            },
            "nontorsion_case": "two generators of one infinite cyclic group are inverse; r_y=r_x^+/-1 and y^2/q-2=r_y+r_y^-1=x^2/q-2",
            "torsion_table": [
                {"eigenratio_order": 1, "r_plus_r_inverse": 2, "trace_square_over_q": 4},
                {"eigenratio_order": 2, "r_plus_r_inverse": -2, "trace_square_over_q": 0},
                {"eigenratio_order": 3, "r_plus_r_inverse": -1, "trace_square_over_q": 1},
                {"eigenratio_order": 4, "r_plus_r_inverse": 0, "trace_square_over_q": 2},
                {"eigenratio_order": 6, "r_plus_r_inverse": 1, "trace_square_over_q": 3},
            ],
            "torsion_exhaustion": "r+r^-1=x^2/q-2 is a rational algebraic integer in [-2,2], hence one of -2,-1,0,1,2 and the eigenratio order is exactly one of 2,3,4,6,1",
            "why_cyclotomic_examples_do_not_contradict_it": "orders 5,7,9,11 have irrational primitive trace squares; their algebraic SL2 traces are not rational fixed-determinant elliptic traces",
        },
        "bounded_exact_regression": {
            "odd_orders_inclusive": [3, max_odd_order],
            "odd_order_count": len(bounded_rows),
            "per_order": bounded_rows,
            "method": "integer residue Counters, unit multiplication, and direct cyclic-interval intersections only",
        },
        "source_and_file_locks": {
            "upstream_role": "scope/provenance binding only; no finite histogram is transformed and no in-progress sign packet is consumed",
            "source_schema": source["schema"],
            "locks": {
                "scalar_trace_fixture": _file_lock(
                    SOURCE_FIXTURE_PATH, payload_sha256=EXPECTED_SOURCE_PAYLOAD_SHA256
                ),
                "scalar_trace_producer": _file_lock(SOURCE_PRODUCER_PATH),
            },
        },
        "resource_contract": {
            "exclusive_accounted_work_unit_cap": guard.cap,
            "accounted_work_unit_ledger": {
                **dict(sorted(guard.ledger.items())),
                "total_accounted_work_units": guard.total,
            },
            "unit_definition": "one candidate unit stabilizer comparison, one direct autocorrelation comparison, or one named exact certificate; not CPU instructions",
            "field_curve_or_polynomial_model_enumerations": 0,
            "symbolic_packages": 0,
            "random_samples": 0,
            "floating_point_results": 0,
            "maximum_root_order_in_bounded_replay": max_odd_order,
            "maximum_local_factor_degree_in_examples": max(EXAMPLE_ORDERS) + 1,
        },
        "scope_firewall": {
            "no_scalar_full_factor_conflation": "scalar-character collisions need not be complete-factor collisions; this packet studies only the latter in a cyclotomic stratum",
            "no_rational_example_claim": "the non-sign aliases at orders 5,7,9,11 have algebraic irrational traces and are not advertised as elliptic local factors over Q with rational q and trace",
            "no_curve_or_global_family_claim": "a compact semisimple local conjugacy class does not supply a curve, motive, compatible Euler product, automorphy, or monodromy family",
            "no_negative_lift_conflation": "at odd m the negative scalar lift sends F(T) to F(-T); it is not merged with the same-lift cyclotomic aliases",
            "no_even_order_classification_claim": "the closed stabilizer theorem is for odd root order; the exact residue-multiset criterion still decides any individually supplied finite order, but even orders are not globally classified here",
            "no_priority_claim": "the cyclic-interval proof and project packaging are recorded without a literature-priority or novelty claim",
            "no_RH_or_GRH_claim": "finite local spectral aliases imply no analytic continuation, zero-free region, RH, or GRH statement",
        },
        "next_targets": [
            "classify the affine parity cosets for even root order without conflating scalar-lift signs",
            "study which algebraic cyclotomic strata can occur in coefficient fields of genuine compatible L-function families",
            "combine quotient-group recovery with integral and local-global constraints across many primes",
        ],
    }
    if guard.total >= guard.cap:
        raise RuntimeError("resource cap was not respected")
    fixture["payload_sha256"] = _canonical_sha256(fixture)
    return fixture


def _write(path: Path) -> None:
    path.write_text(
        json.dumps(build_fixture(), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {path}")


def _check(path: Path) -> None:
    expected = build_fixture()
    actual = json.loads(path.read_text(encoding="utf-8"))
    if actual != expected:
        raise SystemExit(f"fixture is stale: {path}")
    print(
        f"fixture is current: {path} "
        f"({expected['resource_contract']['accounted_work_unit_ledger']['total_accounted_work_units']} accounted units)"
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    actions = parser.add_mutually_exclusive_group(required=True)
    actions.add_argument("--write", nargs="?", const=str(OUTPUT_PATH), metavar="PATH")
    actions.add_argument("--check", nargs="?", const=str(OUTPUT_PATH), metavar="PATH")
    arguments = parser.parse_args(argv)
    if arguments.write is not None:
        _write(Path(arguments.write))
    else:
        _check(Path(arguments.check))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
