"""Exact aliases of complete symmetric-power spectra at even cyclotomic order.

The proof is representation-theoretic.  The bounded replay uses only integer
residue counters and elementary polynomial arithmetic from the standard
library.  It enumerates no field, curve, polynomial model, or trace range.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from pathlib import Path
from typing import Iterable, Sequence


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "elliptic_symmetric_power_even_cyclotomic_aliases.json"
NOTE_PATH = HERE / "ELLIPTIC_SYMMETRIC_POWER_EVEN_CYCLOTOMIC_ALIASES.md"
TEST_PATH = ROOT / "tests" / "test_elliptic_symmetric_power_even_cyclotomic_aliases.py"

ODD_SOURCE_PATH = HERE / "elliptic_symmetric_power_cyclotomic_spectral_aliases.json"
SIGN_SOURCE_PATH = HERE / "elliptic_symmetric_power_full_factor_sign_aliases.json"

EXPECTED_ODD_SOURCE_SCHEMA = (
    "riemann.function_field.elliptic_symmetric_power_cyclotomic_spectral_aliases.v1"
)
EXPECTED_ODD_SOURCE_PAYLOAD_SHA256 = (
    "b783dc120095c5256cacc2eaa79f3f152883f9b33b4074a18b123489f81bc6ff"
)
EXPECTED_ODD_SOURCE_FILE_SHA256_LF = (
    "4321113137615a88f43926c1e92df478160de5a00f0974c1472303de506aabdc"
)
EXPECTED_SIGN_SOURCE_SCHEMA = (
    "riemann.function_field.elliptic_symmetric_power_full_factor_collisions.v1"
)
EXPECTED_SIGN_SOURCE_PAYLOAD_SHA256 = (
    "f1a7f183ee16c98c8f633e9b5ffa5f1bb76c0521cd596d5be71840a35711d983"
)
EXPECTED_SIGN_SOURCE_FILE_SHA256_LF = (
    "5388e4e6819f2b48b08956ab810137054158424931e5e6ac1d516fc54d03c607"
)

SCHEMA = "riemann.function_field.elliptic_symmetric_power_even_cyclotomic_aliases.v1"
FROZEN_MAX_EVEN_ORDER = 64
EXAMPLE_ORDERS = (4, 6, 8, 10, 12, 16, 18, 20)
ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE = 150_000

Polynomial = tuple[int, ...]


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


def _require_even_order(order: int) -> None:
    _require_plain_int("order", order)
    if order < 4 or order % 2:
        raise ValueError("order must be an even integer at least 4")


def _require_nonnegative_m(m: int) -> None:
    _require_plain_int("m", m)
    if m < 0:
        raise ValueError("m must be nonnegative")


class ResourceGuard:
    """Small exact-work ledger with an exclusive hard cap."""

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
    _require_even_order(order)
    return tuple(a for a in range(1, order) if math.gcd(a, order) == 1)


def exponent_multiplicities(order: int, m: int) -> Counter[int]:
    """Multiplicity counter for m,m-2,...,-m modulo an even order."""

    _require_even_order(order)
    _require_nonnegative_m(m)
    return Counter((m - 2 * j) % order for j in range(m + 1))


def cycle_remainder(order: int, m: int) -> tuple[int, int, tuple[int, ...]]:
    """Return k,s,R for m+1=k*(N/2)+s and the residual exponent list."""

    _require_even_order(order)
    _require_nonnegative_m(m)
    half_order = order // 2
    k, s = divmod(m + 1, half_order)
    return k, s, tuple((m - 2 * j) % order for j in range(s))


def reconstructed_cycle_counts(order: int, m: int) -> Counter[int]:
    """Reconstruct E_m from full parity-coset cycles and the remainder."""

    k, _, remainder = cycle_remainder(order, m)
    counts = Counter(
        {residue: k for residue in range(m % 2, order, 2) if k}
    )
    counts.update(remainder)
    return counts


def exact_stabilizer(order: int, m: int) -> tuple[int, ...]:
    """Units a for which multiplication by a fixes E_m with multiplicity."""

    base = exponent_multiplicities(order, m)
    output = []
    for a in units_modulo(order):
        transformed = Counter(
            (a * residue) % order
            for residue, multiplicity in base.items()
            for _ in range(multiplicity)
        )
        if transformed == base:
            output.append(a)
    return tuple(output)


def predicted_stabilizer(order: int, m: int) -> tuple[int, ...]:
    """Closed all-N, all-m even-cyclotomic stabilizer theorem."""

    _require_even_order(order)
    _require_nonnegative_m(m)
    half_order = order // 2
    _, s = divmod(m + 1, half_order)
    units = units_modulo(order)
    if s in {0, 1, half_order - 1}:
        return units
    if m % 2 == 0:
        return tuple(
            a for a in units if a % half_order in {1 % half_order, -1 % half_order}
        )
    return (1, order - 1)


def generic_even_power_lifts(order: int) -> tuple[int, ...]:
    """The inverse/central-sign lifts in a generic even symmetric power."""

    _require_even_order(order)
    half_order = order // 2
    return tuple(
        a
        for a in units_modulo(order)
        if a % half_order in {1 % half_order, -1 % half_order}
    )


def cyclic_interval_autocorrelation(
    modulus: int, length: int, displacement: int
) -> int:
    """Autocorrelation of {0,...,length-1} in Z/modulus Z."""

    _require_plain_int("modulus", modulus)
    _require_plain_int("length", length)
    _require_plain_int("displacement", displacement)
    if modulus < 2:
        raise ValueError("modulus must be at least 2")
    if not 0 <= length <= modulus:
        raise ValueError("length must lie between zero and the modulus")
    d = displacement % modulus
    if d == 0:
        return length
    return max(0, length - d) + max(0, length - (modulus - d))


def half_shift_interval_invariant(modulus: int, length: int) -> bool:
    """Whether a proper initial interval is fixed by the half-period shift."""

    _require_plain_int("modulus", modulus)
    _require_plain_int("length", length)
    if modulus < 2 or modulus % 2:
        raise ValueError("modulus must be positive and even")
    if not 0 <= length < modulus:
        raise ValueError("length must lie from zero through modulus minus one")
    interval = Counter(range(length))
    shifted = Counter((value + modulus // 2) % modulus for value in range(length))
    return interval == shifted


def euler_phi(value: int) -> int:
    _require_plain_int("value", value)
    if value < 1:
        raise ValueError("value must be positive")
    return sum(1 for candidate in range(1, value + 1) if math.gcd(candidate, value) == 1)


def primitive_collapse_certificate(order: int) -> dict[str, object]:
    """Count primitive trace classes and quotient away central sign when valid."""

    _require_even_order(order)
    phi = euler_phi(order)
    trace_classes = phi // 2
    central_sign_stays_primitive = order % 4 == 0
    if central_sign_stays_primitive:
        central_kernel = generic_even_power_lifts(order)
        sign_orbits = phi // len(central_kernel)
    else:
        central_kernel = (1, order - 1)
        sign_orbits = trace_classes
    genuine = sign_orbits > 1
    return {
        "even_root_order_N": order,
        "half_order_M": order // 2,
        "Euler_phi_N": phi,
        "primitive_classes_modulo_inversion": trace_classes,
        "central_sign_preserves_primitive_order_N": central_sign_stays_primitive,
        "inverse_and_available_central_sign_lifts": list(central_kernel),
        "primitive_classes_modulo_inversion_and_available_central_sign": sign_orbits,
        "all_unit_edge_collapses_genuinely_nonsign_classes": genuine,
        "first_all_unit_edge_power_m": order // 2 - 2,
    }


def _poly_trim(values: Iterable[int]) -> Polynomial:
    output = list(values)
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return tuple(output or (0,))


def _poly_mul(left: Sequence[int], right: Sequence[int]) -> Polynomial:
    output = [0] * (len(left) + len(right) - 1)
    for left_degree, left_value in enumerate(left):
        for right_degree, right_value in enumerate(right):
            output[left_degree + right_degree] += left_value * right_value
    return _poly_trim(output)


def _poly_pow(base: Sequence[int], exponent: int) -> Polynomial:
    _require_plain_int("exponent", exponent)
    if exponent < 0:
        raise ValueError("polynomial exponent must be nonnegative")
    result: Polynomial = (1,)
    power = _poly_trim(base)
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = _poly_mul(result, power)
        remaining //= 2
        if remaining:
            power = _poly_mul(power, power)
    return result


def _poly_divide_unit_leading(
    dividend: Sequence[int], divisor: Sequence[int]
) -> Polynomial:
    """Exact integer division when the divisor's leading coefficient is +/-1."""

    numerator = list(_poly_trim(dividend))
    denominator = _poly_trim(divisor)
    leading = denominator[-1]
    if leading not in (-1, 1):
        raise ValueError("divisor must have unit leading coefficient")
    if len(numerator) < len(denominator):
        raise ArithmeticError("polynomial division is not exact")
    quotient = [0] * (len(numerator) - len(denominator) + 1)
    for degree in range(len(numerator) - 1, len(denominator) - 2, -1):
        coefficient = numerator[degree] // leading
        if coefficient * leading != numerator[degree]:
            raise ArithmeticError("polynomial quotient is not integral")
        quotient_degree = degree - len(denominator) + 1
        quotient[quotient_degree] = coefficient
        for offset, value in enumerate(denominator):
            numerator[quotient_degree + offset] -= coefficient * value
    if any(numerator):
        raise ArithmeticError("polynomial division left a nonzero remainder")
    return _poly_trim(quotient)


def parity_cycle_factor(order: int, m: int) -> Polynomial:
    """C_m(T)=product over the parity coset =1-(-1)^m*T^(N/2)."""

    _require_even_order(order)
    _require_nonnegative_m(m)
    half_order = order // 2
    output = [0] * (half_order + 1)
    output[0] = 1
    output[half_order] = -((-1) ** m)
    return tuple(output)


def edge_factor_polynomial(order: int, m: int) -> Polynomial:
    """Closed normalized factor in one of the three all-unit edge cases."""

    _require_even_order(order)
    _require_nonnegative_m(m)
    half_order = order // 2
    k, s = divmod(m + 1, half_order)
    if s not in {0, 1, half_order - 1}:
        raise ValueError("m must lie in one of the three all-unit edge residues")
    cycle = parity_cycle_factor(order, m)
    if s == 0:
        return _poly_pow(cycle, k)
    if s == 1:
        singleton = (1, -((-1) ** k))
        return _poly_mul(_poly_pow(cycle, k), singleton)
    missing = (1, -((-1) ** (k + 1)))
    return _poly_divide_unit_leading(_poly_pow(cycle, k + 1), missing)


def edge_factor_certificate(order: int, m: int) -> dict[str, object]:
    """Exact exponent and integer-polynomial certificate for an edge factor."""

    half_order = order // 2
    k, s, remainder = cycle_remainder(order, m)
    polynomial = edge_factor_polynomial(order, m)
    if len(polynomial) - 1 != m + 1:
        raise ArithmeticError("edge factor degree changed")
    cycle = parity_cycle_factor(order, m)
    formula: str
    denominator: Polynomial | None = None
    if s == 0:
        formula = "C_m(T)^k"
        expected = _poly_pow(cycle, k)
    elif s == 1:
        formula = "C_m(T)^k*(1-(-1)^k*T)"
        expected = _poly_mul(_poly_pow(cycle, k), (1, -((-1) ** k)))
    else:
        formula = "C_m(T)^(k+1)/(1-(-1)^(k+1)*T)"
        denominator = (1, -((-1) ** (k + 1)))
        expected = _poly_divide_unit_leading(_poly_pow(cycle, k + 1), denominator)
    if polynomial != expected:
        raise ArithmeticError("edge factor formula failed")
    return {
        "even_root_order_N": order,
        "half_order_M": half_order,
        "symmetric_power_m": m,
        "division_m_plus_1_equals_kM_plus_s": {"k": k, "s": s},
        "residual_exponents_modulo_N": list(remainder),
        "cycle_factor_C_m_coefficients_T0_up": list(cycle),
        "closed_formula": formula,
        "denominator_coefficients_T0_up": (
            list(denominator) if denominator is not None else None
        ),
        "factor_coefficients_T0_up": list(polynomial),
    }


def _load_locked_source(
    path: Path, expected_schema: str, expected_payload: str, expected_lf: str
) -> dict[str, object]:
    if _lf_sha256(path) != expected_lf:
        raise RuntimeError(f"locked source LF hash mismatch: {_relative(path)}")
    source = json.loads(path.read_text(encoding="utf-8"))
    if source.get("schema") != expected_schema:
        raise RuntimeError(f"locked source schema mismatch: {_relative(path)}")
    if source.get("payload_sha256") != expected_payload:
        raise RuntimeError(f"locked source payload mismatch: {_relative(path)}")
    unhashed = dict(source)
    claimed = unhashed.pop("payload_sha256", None)
    if claimed != _canonical_sha256(unhashed):
        raise RuntimeError(f"locked source payload is inconsistent: {_relative(path)}")
    return source


def _bounded_regression(max_order: int, guard: ResourceGuard) -> list[dict[str, object]]:
    rows = []
    for order in range(4, max_order + 1, 2):
        half_order = order // 2
        units = units_modulo(order)
        candidate_checks = 0
        decomposition_checks = 0
        for m in range(2 * order):
            actual = exact_stabilizer(order, m)
            expected = predicted_stabilizer(order, m)
            guard.charge("bounded_stabilizer_unit_candidates", len(units))
            candidate_checks += len(units)
            if actual != expected:
                raise ArithmeticError(
                    f"stabilizer theorem failed for N={order},m={m}: {actual}!={expected}"
                )
            if exponent_multiplicities(order, m) != reconstructed_cycle_counts(order, m):
                raise ArithmeticError("complete-cycle decomposition failed")
            guard.charge("bounded_cycle_decomposition_checks")
            decomposition_checks += 1

        autocorrelation_checks = 0
        for length in range(2, half_order - 1):
            interval = set(range(length))
            correlations = {}
            for displacement in range(1, half_order):
                direct = len(
                    interval
                    & {
                        (value + displacement) % half_order
                        for value in interval
                    }
                )
                closed = cyclic_interval_autocorrelation(
                    half_order, length, displacement
                )
                guard.charge("bounded_autocorrelation_checks")
                autocorrelation_checks += 1
                if direct != closed:
                    raise ArithmeticError("cyclic autocorrelation formula failed")
                correlations[displacement] = direct
            maximizers = {
                displacement
                for displacement, value in correlations.items()
                if value == length - 1
            }
            if maximizers != {1, half_order - 1}:
                raise ArithmeticError("interior interval lost unique +/-1 adjacency")

        half_shift_checks = 0
        if half_order % 2 == 0:
            for length in range(half_order):
                actual = half_shift_interval_invariant(half_order, length)
                if actual != (length == 0):
                    raise ArithmeticError("proper interval half-shift lemma failed")
                guard.charge("bounded_half_shift_checks")
                half_shift_checks += 1

        row = primitive_collapse_certificate(order)
        row.update(
            {
                "unit_group": list(units),
                "tested_m_range_inclusive": [0, 2 * order - 1],
                "stabilizer_unit_candidate_checks": candidate_checks,
                "cycle_decomposition_checks": decomposition_checks,
                "autocorrelation_checks": autocorrelation_checks,
                "half_shift_checks": half_shift_checks,
            }
        )
        rows.append(row)
    return rows


def build_fixture(max_even_order: int = FROZEN_MAX_EVEN_ORDER) -> dict[str, object]:
    """Build the canonical exact even-order packet."""

    _require_plain_int("max_even_order", max_even_order)
    if max_even_order != FROZEN_MAX_EVEN_ORDER:
        raise ValueError(f"max_even_order must be exactly {FROZEN_MAX_EVEN_ORDER}")
    _load_locked_source(
        ODD_SOURCE_PATH,
        EXPECTED_ODD_SOURCE_SCHEMA,
        EXPECTED_ODD_SOURCE_PAYLOAD_SHA256,
        EXPECTED_ODD_SOURCE_FILE_SHA256_LF,
    )
    _load_locked_source(
        SIGN_SOURCE_PATH,
        EXPECTED_SIGN_SOURCE_SCHEMA,
        EXPECTED_SIGN_SOURCE_PAYLOAD_SHA256,
        EXPECTED_SIGN_SOURCE_FILE_SHA256_LF,
    )
    guard = ResourceGuard()
    guard.charge("locked_source_files_verified", 2)
    bounded_rows = _bounded_regression(max_even_order, guard)

    edge_certificates = []
    for order in EXAMPLE_ORDERS:
        half_order = order // 2
        for m in (half_order - 2, half_order - 1, half_order):
            edge_certificates.append(edge_factor_certificate(order, m))
            guard.charge("named_edge_factor_certificates")

    nongenuine = [
        row["even_root_order_N"]
        for row in bounded_rows
        if not row["all_unit_edge_collapses_genuinely_nonsign_classes"]
    ]
    if nongenuine != [4, 6, 8, 12]:
        raise ArithmeticError("genuine primitive-class threshold changed")

    fixture: dict[str, object] = {
        "schema": SCHEMA,
        "packet_id": "FUNCTION_FIELD.ELLIPTIC.SYMMETRIC_POWER.EVEN_CYCLOTOMIC_ALIASES.V1",
        "status": "EXACT_ALL_EVEN_ORDERS_STABILIZER_THEOREM_PLUS_BOUNDED_REPLAY",
        "rigor_level": {
            "stabilizer_theorem": "PROVED_FOR_EVERY_EVEN_N_AT_EVERY_m",
            "edge_factors": "PROVED_BY_PARITY_COSET_ROOT_FACTORIZATION",
            "central_sign_interpretation": "PROVED_FROM_SYM_m(-g)=(-1)^m*SYM_m(g)",
            "bounded_replay": "EXACT_DEPENDENCY_FREE_REGRESSION_NOT_USED_AS_THE_PROOF",
            "arithmetic_realization_or_novelty": "NOT_INFERRED",
        },
        "spectral_setup": {
            "even_root_order": "N=2M>=4",
            "primitive_class": "g_a=diag(zeta^a,zeta^-a), gcd(a,N)=1",
            "complete_spectrum": "S_m(zeta^a)={zeta^(a*(m-2j)):0<=j<=m}, with multiplicity",
            "factor": "F_m(zeta^a;T)=product_(j=0)^m(1-zeta^(a*(m-2j))*T)",
            "comparison": "same primitive zeta and the same determinant-one scalar lift",
        },
        "even_order_stabilizer_theorem": {
            "scope": "every N=2M>=4, every m>=0, every a in U(N)",
            "division": "m+1=kM+s with 0<=s<M",
            "statement": {
                "edge_s_0_1_M_minus_1": "the stabilizer is all of U(N)",
                "interior_even_m": "the stabilizer is {a in U(N):a=+/-1 mod M}",
                "interior_odd_m": "the stabilizer is {+/-1 mod N}",
            },
            "complete_cycle_reduction": (
                "the step -2 has period M; k cycles give k copies of the parity "
                "coset; indexing the residual atoms by I_s={0,...,s-1}, "
                "multiplication by a induces A_a(j)=a*j-(a-1)*m/2 modulo M"
            ),
            "interior_adjacency_proof": (
                "for 2<=s<=M-2, cyclic-interval autocorrelation has its unique "
                "nonzero maximum s-1 at displacements +/-1; the affine map has "
                "slope a and therefore forces a=+/-1 mod M"
            ),
            "edge_proof": (
                "s=0 is empty; at s=1 the affine map fixes index 0 because "
                "m=kM; at s=M-1 it fixes the omitted index -1 because "
                "m=(k+1)M-2"
            ),
            "odd_power_lift_separation": (
                "when 4 divides N, the two lifts of each sign modulo M differ by "
                "M and negate every odd exponent; the proper consecutive remainder "
                "is not invariant under the resulting M/2 shift, so only +/-1 mod N remain"
            ),
            "multiplicities_are_retained": True,
            "composite_orders_are_included": True,
        },
        "central_sign_audit": {
            "central_element": "-I sends zeta^a to -zeta^a=zeta^(a+M)",
            "primitive_order_condition": "a+M is a unit modulo 2M exactly when M is even, i.e. 4 divides N",
            "representation_kernel": "Sym^m(-g)=(-1)^m Sym^m(g)",
            "even_m": (
                "the extra lifts a=M+1 and a=M-1 (when distinct) are central-sign "
                "mates of +1 and -1, so generic even-m equality is not a new nonsign alias"
            ),
            "odd_m": (
                "central sign negates the full spectrum and is excluded in every "
                "interior case; at s=0 the full parity cycles make all units aliases"
            ),
            "N_4_corner": "at N=4 the central lift M+1 equals -1, so the generic subgroup has only two elements",
        },
        "edge_factor_theorem": {
            "cycle_factor_definition": "C_m(T)=1-(-1)^m*T^M",
            "s_0": "F_m=C_m^k",
            "s_1": "F_m=C_m^k*(1-(-1)^k*T)",
            "s_M_minus_1": "F_m=C_m^(k+1)/(1-(-1)^(k+1)*T)",
            "denominator_parity_note": "(-1)^(k+1)=(-1)^(k-1), but k+1 remains meaningful at k=0",
            "fixed_determinant_scalar": (
                "for a common lift rho with rho^2=q, replace T by rho^m*T; "
                "changing the lift is the separately audited central-sign operation"
            ),
            "certificates": edge_certificates,
        },
        "primitive_class_collapse": {
            "trace_classes": "primitive determinant-one classes are U(N)/{+/-1}, count phi(N)/2",
            "sign_quotient_when_4_divides_N": (
                "at even m also quotient by a->a+M; for N>4 this gives phi(N)/4 classes"
            ),
            "sign_quotient_when_N_is_2_mod_4": (
                "the negative root has order M rather than N, so within the primitive-N stratum the count remains phi(N)/2"
            ),
            "genuine_nonsign_edge_criterion": (
                "phi(N)>2 when M is odd, and phi(N)>4 when M is even"
            ),
            "exact_nongenuine_orders": [4, 6, 8, 12],
            "exception_proof": {
                "M_odd": (
                    "phi(2M)<=2 and N=2 mod 4 leaves N=6 from the exact "
                    "classification phi(n)<=2 iff n is in {1,2,3,4,6}"
                ),
                "M_even": (
                    "if 4 divides N and phi(N)<=4, an odd prime is 3 or 5; "
                    "5 makes phi(N)>=phi(20)=8, while 3 leaves only N=12; "
                    "without odd primes, N=2^r leaves N=4 or 8"
                ),
            },
            "smallest_genuine_order": 10,
            "first_all_unit_edge_power": "m=M-2",
            "bounded_exact_table": bounded_rows,
        },
        "corner_cases": {
            "N_4_M_2": (
                "s is always 0 or 1, both edge cases; U(4)={+/-1}, so all-unit "
                "stabilization creates no second primitive trace class"
            ),
            "N_6_M_3": (
                "s is always 0,1,2, all edge cases; U(6)={+/-1}, again no second primitive class"
            ),
            "N_8_and_N_12": (
                "there are two primitive trace classes, but they are a central-sign pair; "
                "generic even equality is the central kernel and an odd all-cycle edge "
                "is invariant under spectral negation, so neither is genuinely nonsign"
            ),
            "N_10": (
                "the first genuine case: two primitive trace classes are not sign mates, "
                "and all units already collapse at m=M-2=3"
            ),
        },
        "source_locks": [
            {
                "path": _relative(ODD_SOURCE_PATH),
                "schema": EXPECTED_ODD_SOURCE_SCHEMA,
                "payload_sha256": EXPECTED_ODD_SOURCE_PAYLOAD_SHA256,
                "file_sha256_lf_normalized": EXPECTED_ODD_SOURCE_FILE_SHA256_LF,
                "use": "bind the complementary exact odd-root-order classification",
            },
            {
                "path": _relative(SIGN_SOURCE_PATH),
                "schema": EXPECTED_SIGN_SOURCE_SCHEMA,
                "payload_sha256": EXPECTED_SIGN_SOURCE_PAYLOAD_SHA256,
                "file_sha256_lf_normalized": EXPECTED_SIGN_SOURCE_FILE_SHA256_LF,
                "use": "bind the rational fixed-determinant full-factor and central-sign classification",
            },
        ],
        "resource_contract": {
            "maximum_even_order": max_even_order,
            "tested_m_per_order": "0 through 2N-1 inclusive",
            "accounted_work_unit_ledger": dict(sorted(guard.ledger.items())),
            "total_accounted_work_units": guard.total,
            "exclusive_accounted_work_unit_cap": guard.cap,
            "field_curve_polynomial_or_trace_range_enumerations": 0,
            "random_samples": 0,
            "floating_point_results": 0,
            "symbolic_packages": 0,
            "arithmetic": "exact Python integers and residue Counters only",
        },
        "scope_firewall": {
            "local_representation_theory_only": True,
            "no_curve_or_isogeny_realization_claim": True,
            "no_global_Euler_product_or_compatible_family_constructed": True,
            "no_automorphy_modularity_or_motive_claim": True,
            "no_scalar_character_full_factor_conflation": True,
            "no_rational_nonsign_counterexample_claim": True,
            "no_literature_priority_or_novelty_claim": True,
            "no_RH_GRH_or_zero_distribution_consequence": True,
            "finite_replay_is_not_the_proof": True,
        },
        "next_targets": [
            "classify simultaneous cyclotomic aliases across several symmetric powers",
            "impose coefficient-field Galois orbits and cross-prime compatibility",
            "determine which local strata can occur in geometric compatible systems",
            "study how central kernels alter detectors for other algebraic representations",
        ],
        "producer": {
            "script": _relative(Path(__file__).resolve()),
            "script_sha256_lf_normalized": _lf_sha256(Path(__file__).resolve()),
            "note": _relative(NOTE_PATH),
            "note_sha256_lf_normalized": _lf_sha256(NOTE_PATH),
            "test": _relative(TEST_PATH),
            "test_sha256_lf_normalized": _lf_sha256(TEST_PATH),
        },
    }
    if guard.total >= guard.cap:
        raise RuntimeError("resource cap was not respected")
    fixture["payload_sha256"] = _canonical_sha256(fixture)
    return fixture


def _serialized_fixture() -> str:
    return json.dumps(build_fixture(), indent=2, sort_keys=True) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="fail unless stored JSON equals a fresh build"
    )
    arguments = parser.parse_args(argv)
    serialized = _serialized_fixture()
    if arguments.check:
        if not OUTPUT_PATH.exists() or OUTPUT_PATH.read_text(encoding="utf-8") != serialized:
            raise SystemExit("stored even-cyclotomic fixture is stale")
        print(f"verified {OUTPUT_PATH}")
        return 0
    OUTPUT_PATH.write_text(serialized, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
