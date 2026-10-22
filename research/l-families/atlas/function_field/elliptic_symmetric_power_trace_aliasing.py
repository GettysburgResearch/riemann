"""Exact scalar-trace aliasing for elliptic symmetric powers.

This packet studies only the scalar character

    tau_m(t; q) = E_m(t, q),
    E_0 = 1, E_1 = t, E_m = t E_{m-1} - q E_{m-2}.

It does not identify equality of ``tau_m`` with equality of the full degree
``m+1`` symmetric-power local factor.  The finite rows below are transforms
of the already locked genus-one trace histograms; no curve or field is
enumerated here.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from pathlib import Path
from typing import Iterable, Mapping, Sequence


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "elliptic_symmetric_power_trace_aliasing.json"
NOTE_PATH = HERE / "ELLIPTIC_SYMMETRIC_POWER_TRACE_ALIASING.md"
TEST_PATH = ROOT / "tests" / "test_elliptic_symmetric_power_trace_aliasing.py"
SOURCE_FIXTURE_PATH = HERE / "genus1_cubic_family_laws.json"
SOURCE_PRODUCER_PATH = HERE / "genus1_cubic_family_laws.py"

FROZEN_Q_VALUES = (3, 5, 7, 11, 13)
MAX_SYMMETRIC_POWER = 18
ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE = 2_000

EXPECTED_SOURCE_SCHEMA = "riemann.function_field.genus1_cubic_family_laws.v1"
EXPECTED_SOURCE_PAYLOAD_SHA256 = (
    "183ffb31ae2f5776944e162e59390c40bd7081827b8731246e72e25a882e50df"
)
EXPECTED_SOURCE_FIXTURE_SHA256_LF = (
    "b9016ae801cff40d15c53d96210b66a7d44fae7d916e827a0526b9dd42017227"
)
EXPECTED_SOURCE_PRODUCER_SHA256_LF = (
    "3d5baace952240c162c83bd5c66eb81db1704aee35e770de3d8df43fff669b79"
)
EXPECTED_SOURCE_NORMALIZATION = {
    "family": "H_3(q)={monic squarefree cubic D over F_q}",
    "curve": "E_D:y^2=D(x), with the rational point at infinity",
    "trace": "a_D=q+1-#E_D(F_q)=-sum_x quadratic_character(D(x))",
    "l_polynomial": "L_D(T)=1-a_D*T+q*T^2",
    "model_count": "q^2*(q-1)",
}

PARITY_PAIRS = ((0, 0), (0, 1), (1, 0), (1, 1))

# Complete frozen list of collisions after quotienting only the automatic
# t ~ -t symmetry for even m.  Each item is
# (m, scalar trace, expected-domain-class representatives).
EXPECTED_EXTRA_FIBER_SIGNATURE = (
    (3, 4, 9, (0, 3)),
    (3, 5, 0, (-3, 0, 3)),
    (3, 6, -27, (0, 3)),
    (3, 6, 13, (1, 2)),
    (3, 10, -243, (0, 3)),
    (3, 11, 0, (-3, 0, 3)),
    (3, 12, 729, (0, 3)),
    (3, 16, 6561, (0, 3)),
    (3, 17, 0, (-3, 0, 3)),
    (3, 18, -19683, (0, 3)),
)


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _lf_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def _require_integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _require_odd_q(q: int) -> None:
    _require_integer("q", q)
    if q % 2 == 0:
        raise ValueError("q must be odd")


class ResourceGuard:
    """A small ledger of declared high-level exact work units."""

    def __init__(self, cap: int = ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE) -> None:
        self.cap = cap
        self.ledger: Counter[str] = Counter()

    @property
    def total(self) -> int:
        return sum(self.ledger.values())

    def charge(self, name: str, units: int = 1) -> None:
        if units < 0:
            raise ValueError("resource charge must be nonnegative")
        if self.total + units >= self.cap:
            raise RuntimeError(
                f"accounted work would meet or exceed exclusive cap {self.cap}"
            )
        self.ledger[name] += units


def tau(m: int, t: int, q: int) -> int:
    """Return the scalar trace of Sym^m from its defining recurrence."""

    _require_integer("m", m)
    _require_integer("t", t)
    _require_odd_q(q)
    if m < 0:
        raise ValueError("m must be nonnegative")
    if m == 0:
        return 1
    previous_previous, previous = 1, t
    for _ in range(2, m + 1):
        previous_previous, previous = previous, t * previous - q * previous_previous
    return previous


def tau_closed(m: int, t: int, q: int) -> int:
    """Independent binomial formula for ``tau``."""

    _require_integer("m", m)
    _require_integer("t", t)
    _require_odd_q(q)
    if m < 0:
        raise ValueError("m must be nonnegative")
    return sum(
        (-1) ** j * math.comb(m - j, j) * q**j * t ** (m - 2 * j)
        for j in range(m // 2 + 1)
    )


def homogeneous_sum(degree: int, x: int, y: int) -> int:
    """Return H_degree(x,y)=sum_{i=0}^degree x^(degree-i)y^i."""

    _require_integer("degree", degree)
    _require_integer("x", x)
    _require_integer("y", y)
    if degree < 0:
        raise ValueError("homogeneous degree must be nonnegative")
    return sum(x ** (degree - i) * y**i for i in range(degree + 1))


def odd_collision_quotient(m: int, x: int, y: int, q: int) -> int:
    """Polynomial quotient (tau_m(x)-tau_m(y))/(x-y) for odd m."""

    _require_integer("m", m)
    _require_integer("x", x)
    _require_integer("y", y)
    _require_odd_q(q)
    if m < 1 or m % 2 == 0:
        raise ValueError("odd collision quotient requires positive odd m")
    r = (m - 1) // 2
    return sum(
        (-1) ** (r - s)
        * math.comb(r + s + 1, 2 * s + 1)
        * q ** (r - s)
        * homogeneous_sum(2 * s, x, y)
        for s in range(r + 1)
    )


def even_collision_quotient(m: int, x: int, y: int, q: int) -> int:
    """Polynomial quotient (tau_m(x)-tau_m(y))/(x^2-y^2) for even m."""

    _require_integer("m", m)
    _require_integer("x", x)
    _require_integer("y", y)
    _require_odd_q(q)
    if m < 2 or m % 2:
        raise ValueError("even collision quotient requires positive even m")
    r = m // 2
    return sum(
        (-1) ** (r - s - 1)
        * math.comb(r + s + 1, 2 * s + 2)
        * q ** (r - s - 1)
        * sum(x ** (2 * (s - i)) * y ** (2 * i) for i in range(s + 1))
        for s in range(r)
    )


def v2(value: int) -> int:
    """Exact 2-adic valuation of a nonzero integer."""

    _require_integer("value", value)
    if value == 0:
        raise ValueError("v2(0) is not finite")
    value = abs(value)
    return (value & -value).bit_length() - 1


def odd_higher_coefficient_valuation_margin(r: int, s: int, q: int) -> int:
    """Valuation margin over the constant term in the odd quotient at 2X,2Y."""

    _require_integer("r", r)
    _require_integer("s", s)
    _require_odd_q(q)
    if r < 1 or not 1 <= s <= r:
        raise ValueError("odd valuation indices require r>=1 and 1<=s<=r")
    constant = (r + 1) * q**r
    higher = math.comb(r + s + 1, 2 * s + 1) * q ** (r - s) * 2 ** (2 * s)
    return v2(higher) - v2(constant)


def odd_interval_margin_formula(r: int, s: int) -> int:
    """The numerator-interval expression equal to the preceding margin."""

    _require_integer("r", r)
    _require_integer("s", s)
    if r < 1 or not 1 <= s <= r:
        raise ValueError("odd interval indices require r>=1 and 1<=s<=r")
    remaining = math.prod(
        value
        for value in range(r - s + 1, r + s + 2)
        if value != r + 1
    )
    return v2(remaining) + (2 * s + 1).bit_count() - 1


def even_higher_coefficient_valuation_margin(r: int, s: int, q: int) -> int:
    """Valuation margin over the constant term in the even quotient at 2X,2Y."""

    _require_integer("r", r)
    _require_integer("s", s)
    _require_odd_q(q)
    if r < 2 or not 1 <= s <= r - 1:
        raise ValueError("even valuation indices require r>=2 and 1<=s<=r-1")
    constant = math.comb(r + 1, 2) * q ** (r - 1)
    higher = math.comb(r + s + 1, 2 * s + 2) * q ** (r - s - 1) * 2 ** (2 * s)
    return v2(higher) - v2(constant)


def even_interval_margin_formula(r: int, s: int) -> int:
    """The numerator-interval expression equal to the preceding margin."""

    _require_integer("r", r)
    _require_integer("s", s)
    if r < 2 or not 1 <= s <= r - 1:
        raise ValueError("even interval indices require r>=2 and 1<=s<=r-1")
    remaining = math.prod(
        value
        for value in range(r - s, r + s + 2)
        if value not in (r, r + 1)
    )
    return v2(remaining) + (2 * s + 2).bit_count() - 1


def _fibonacci_polynomial_point_states(
    z: int, initial_one_value: int
) -> list[tuple[int, int]]:
    """Values and formal derivatives mod 2 for P_r=zP_(r-1)+P_(r-2)."""

    z %= 2
    states = [(1, 0), (initial_one_value % 2, 1)]
    while len(states) <= 36:
        previous_previous_value, previous_previous_derivative = states[-2]
        previous_value, previous_derivative = states[-1]
        states.append(
            (
                (z * previous_value + previous_previous_value) % 2,
                (
                    previous_value
                    + z * previous_derivative
                    + previous_previous_derivative
                )
                % 2,
            )
        )
    return states


def quotient_parity_table() -> list[dict[str, object]]:
    """Return the exact 12-residue quotient table, indexed by r mod 12."""

    # A_r=E_(2r+1)(t)/t has A_0=1,A_1=z mod 2.
    odd_zero = _fibonacci_polynomial_point_states(0, 0)
    odd_one = _fibonacci_polynomial_point_states(1, 1)
    # F_r=E_(2r)(t) has F_0=1,F_1=z+1 mod 2.
    even_zero = _fibonacci_polynomial_point_states(0, 1)
    even_one = _fibonacci_polynomial_point_states(1, 0)

    rows: list[dict[str, object]] = []
    for residue in range(12):
        odd_r = residue
        odd_bits = (
            odd_zero[odd_r][0],
            odd_one[odd_r][0],
            odd_one[odd_r][0],
            odd_one[odd_r][0],
        )
        # There is no even quotient at r=0; residue zero is represented by 12.
        even_r = residue or 12
        even_off_diagonal = (even_zero[even_r][0] + even_one[even_r][0]) % 2
        even_bits = (
            even_zero[even_r][1],
            even_off_diagonal,
            even_off_diagonal,
            even_one[even_r][1],
        )

        direct_odd = tuple(
            odd_collision_quotient(2 * odd_r + 1, x, y, 1) % 2
            for x, y in PARITY_PAIRS
        )
        direct_even = tuple(
            even_collision_quotient(2 * even_r, x, y, 1) % 2
            for x, y in PARITY_PAIRS
        )
        if direct_odd != odd_bits or direct_even != even_bits:
            raise ArithmeticError("mod-2 recurrence and quotient formulas disagree")

        odd_target = residue % 3 in (0, 1)
        even_target = residue % 3 == 1
        odd_roots = [list(PARITY_PAIRS[index]) for index, bit in enumerate(odd_bits) if bit == 0]
        even_roots = [list(PARITY_PAIRS[index]) for index, bit in enumerate(even_bits) if bit == 0]
        if odd_target and any(root != [0, 0] for root in odd_roots):
            raise ArithmeticError("odd target row has a forbidden parity root")
        if even_target and any(root != [0, 0] for root in even_roots):
            raise ArithmeticError("even target row has a forbidden parity root")

        rows.append(
            {
                "r_mod_12": residue,
                "odd_m_2r_plus_1_mod_2_values_at_00_01_10_11": list(odd_bits),
                "odd_target_m_mod_6_in_1_3": odd_target,
                "odd_zero_parity_pairs": odd_roots,
                "even_m_2r_positive_representative_r": even_r,
                "even_m_2r_mod_2_values_at_00_01_10_11": list(even_bits),
                "even_target_m_mod_6_eq_2": even_target,
                "even_zero_parity_pairs": even_roots,
            }
        )

    # Global period certificate from recurrence states, not a bounded m search.
    for residue in range(12):
        if odd_zero[residue] != odd_zero[residue + 12]:
            raise ArithmeticError("odd z=0 recurrence state lacks period 12")
        if odd_one[residue] != odd_one[residue + 12]:
            raise ArithmeticError("odd z=1 recurrence state lacks period 12")
    for r in range(1, 13):
        if even_zero[r] != even_zero[r + 12]:
            raise ArithmeticError("even z=0 recurrence state lacks period 12")
        if even_one[r] != even_one[r + 12]:
            raise ArithmeticError("even z=1 recurrence state lacks period 12")
    return rows


def elliptic_power_sum(order: int, t: int, q: int) -> int:
    """Return alpha^order+beta^order for alpha+beta=t, alpha*beta=q."""

    _require_integer("order", order)
    _require_integer("t", t)
    _require_odd_q(q)
    if order < 0:
        raise ValueError("power-sum order must be nonnegative")
    if order == 0:
        return 2
    previous_previous, previous = 2, t
    for _ in range(2, order + 1):
        previous_previous, previous = previous, t * previous - q * previous_previous
    return previous


def sym_power_root_power_sum(m: int, order: int, t: int, q: int) -> int:
    """Power sum of the m+1 roots in the full Sym^m local factor."""

    _require_integer("order", order)
    if order < 1:
        raise ValueError("root power-sum order must be positive")
    return tau(m, elliptic_power_sum(order, t, q), q**order)


def sym_power_local_factor(
    m: int,
    t: int,
    q: int,
    *,
    guard: ResourceGuard | None = None,
) -> tuple[int, ...]:
    """Newton reconstruction of det(1-Sym^m(Frob) T)."""

    _require_integer("m", m)
    _require_integer("t", t)
    _require_odd_q(q)
    if m < 0:
        raise ValueError("m must be nonnegative")
    root_power_sums = [0] + [
        sym_power_root_power_sum(m, order, t, q)
        for order in range(1, m + 2)
    ]
    coefficients = [1]
    for degree in range(1, m + 2):
        numerator = -sum(
            coefficients[degree - order] * root_power_sums[order]
            for order in range(1, degree + 1)
        )
        if numerator % degree:
            raise ArithmeticError("Newton reconstruction lost integrality")
        coefficients.append(numerator // degree)
        if guard is not None:
            guard.charge("newton_coefficients_reconstructed")
    if coefficients[1] != -tau(m, t, q):
        raise ArithmeticError("local-factor first coefficient lost scalar trace")
    return tuple(coefficients)


def sym4_second_elementary_coefficient(t: int, q: int) -> int:
    """Raw T^2 coefficient in the full Sym^4 local factor."""

    _require_integer("t", t)
    _require_odd_q(q)
    u = t * t - 2 * q
    return q * u * (u * u + q * u - q * q)


def sym4_local_factor_closed(t: int, q: int) -> tuple[int, ...]:
    """Closed degree-five Sym^4 factor used only for the scalar/full check."""

    scalar = tau(4, t, q)
    second = sym4_second_elementary_coefficient(t, q)
    return (1, -scalar, second, -(q**2) * second, q**6 * scalar, -(q**10))


def m5_collision_quotient_closed(x: int, y: int, q: int) -> int:
    """Closed quotient for a scalar Sym^5 collision."""

    _require_integer("x", x)
    _require_integer("y", y)
    _require_odd_q(q)
    h2 = x * x + x * y + y * y
    h4 = x**4 + x**3 * y + x * x * y * y + x * y**3 + y**4
    return 3 * q * q - 4 * q * h2 + h4


def m5_collision_quartic(x: int, y: int) -> int:
    """Binary quartic obtained by eliminating q from the Sym^5 quotient."""

    _require_integer("x", x)
    _require_integer("y", y)
    return x**4 + 5 * x**3 * y + 9 * x * x * y * y + 5 * x * y**3 + y**4


def m5_elimination_square(x: int, y: int, q: int) -> tuple[int, int]:
    """Return ((3q-2H2)^2, binary quartic) for the m=5 elimination."""

    _require_integer("x", x)
    _require_integer("y", y)
    _require_odd_q(q)
    h2 = x * x + x * y + y * y
    return (3 * q - 2 * h2) ** 2, m5_collision_quartic(x, y)


def _load_locked_source() -> dict[str, object]:
    if _lf_sha256(SOURCE_FIXTURE_PATH) != EXPECTED_SOURCE_FIXTURE_SHA256_LF:
        raise RuntimeError("locked genus-one fixture file hash mismatch")
    if _lf_sha256(SOURCE_PRODUCER_PATH) != EXPECTED_SOURCE_PRODUCER_SHA256_LF:
        raise RuntimeError("locked genus-one producer file hash mismatch")
    source = json.loads(SOURCE_FIXTURE_PATH.read_text(encoding="utf-8"))
    if source.get("schema") != EXPECTED_SOURCE_SCHEMA:
        raise RuntimeError("locked genus-one schema mismatch")
    if source.get("normalization") != EXPECTED_SOURCE_NORMALIZATION:
        raise RuntimeError("locked genus-one normalization mismatch")
    payload_hash = source.get("payload_sha256")
    if payload_hash != EXPECTED_SOURCE_PAYLOAD_SHA256:
        raise RuntimeError("locked genus-one payload hash mismatch")
    unhashed = dict(source)
    unhashed.pop("payload_sha256", None)
    if _canonical_sha256(unhashed) != payload_hash:
        raise RuntimeError("genus-one canonical payload is internally inconsistent")
    return source


def _source_rows(
    source: Mapping[str, object], q_values: Sequence[int]
) -> list[Mapping[str, object]]:
    finite = source.get("finite_regressions")
    if not isinstance(finite, list):
        raise RuntimeError("locked source lacks finite regressions")
    by_q = {int(row["q"]): row for row in finite}
    rows: list[Mapping[str, object]] = []
    for q in q_values:
        if q not in by_q:
            raise ValueError(f"q={q} is absent from the locked source")
        row = by_q[q]
        histogram = {int(t): int(count) for t, count in row["model_trace_histogram"].items()}
        if sum(histogram.values()) != int(row["squarefree_model_count"]):
            raise RuntimeError("locked source histogram mass mismatch")
        if sum(histogram.values()) != q * q * (q - 1):
            raise RuntimeError("locked source model count violates q^2(q-1)")
        if any(t * t > 4 * q for t in histogram):
            raise RuntimeError("locked source trace violates the Hasse bound")
        rows.append(row)
    return rows


def _expected_domain_class(m: int, t: int) -> int:
    return t if m % 2 else abs(t)


def _transform_source_row(
    source_row: Mapping[str, object], max_m: int, guard: ResourceGuard
) -> dict[str, object]:
    q = int(source_row["q"])
    histogram = {
        int(t): int(count)
        for t, count in source_row["model_trace_histogram"].items()
    }
    guard.charge("source_histogram_atoms_loaded", len(histogram))
    transforms: list[dict[str, object]] = []
    for m in range(1, max_m + 1):
        transformed: Counter[int] = Counter()
        classes: dict[int, dict[str, object]] = {}
        output_classes: dict[int, set[int]] = {}
        for t, count in histogram.items():
            guard.charge("source_atom_trace_transforms")
            scalar = tau(m, t, q)
            transformed[scalar] += count
            representative = _expected_domain_class(m, t)
            record = classes.setdefault(
                representative,
                {"class_representative": representative, "source_traces": [], "source_mass": 0},
            )
            record["source_traces"].append(t)
            record["source_mass"] += count
            output_classes.setdefault(scalar, set()).add(representative)

        for record in classes.values():
            record["source_traces"].sort()
        extra_fibers = []
        for scalar, representatives in sorted(output_classes.items()):
            if len(representatives) <= 1:
                continue
            extra_fibers.append(
                {
                    "scalar_trace": scalar,
                    "expected_domain_classes": [
                        classes[representative]
                        for representative in sorted(representatives)
                    ],
                }
            )

        if sum(transformed.values()) != sum(histogram.values()):
            raise ArithmeticError("trace histogram pushforward lost mass")
        if m % 6 in (1, 3) and extra_fibers:
            raise ArithmeticError("odd injectivity theorem failed on locked support")
        if m % 6 == 2 and extra_fibers:
            raise ArithmeticError("even sign-quotient theorem failed on locked support")

        transforms.append(
            {
                "m": m,
                "m_mod_6": m % 6,
                "expected_domain_quotient": (
                    "singleton traces" if m % 2 else "quadratic-twist classes t~-t"
                ),
                "expected_domain_class_count": len(classes),
                "transformed_scalar_trace_histogram": {
                    str(value): transformed[value] for value in sorted(transformed)
                },
                "transformed_support_size": len(transformed),
                "injective_after_expected_domain_quotient": not extra_fibers,
                "extra_collision_fibers_after_expected_domain_quotient": extra_fibers,
            }
        )
    return {
        "q": q,
        "source_histogram_atom_count": len(histogram),
        "source_member_count": sum(histogram.values()),
        "powers_1_through": max_m,
        "transforms": transforms,
    }


def _extra_fiber_signature(rows: Iterable[Mapping[str, object]]) -> tuple[tuple[object, ...], ...]:
    signature: list[tuple[object, ...]] = []
    for q_row in rows:
        q = int(q_row["q"])
        for transform in q_row["transforms"]:
            m = int(transform["m"])
            for fiber in transform["extra_collision_fibers_after_expected_domain_quotient"]:
                representatives = tuple(
                    int(item["class_representative"])
                    for item in fiber["expected_domain_classes"]
                )
                signature.append((q, m, int(fiber["scalar_trace"]), representatives))
    return tuple(signature)


def _factor_sha256(coefficients: Sequence[int]) -> str:
    return _canonical_sha256(list(coefficients))


def build_fixture(
    q_values: Sequence[int] = FROZEN_Q_VALUES,
    max_m: int = MAX_SYMMETRIC_POWER,
) -> dict[str, object]:
    """Build the exact fixture from the locked source histograms."""

    q_values = tuple(q_values)
    if not q_values:
        raise ValueError("at least one q is required")
    if len(set(q_values)) != len(q_values):
        raise ValueError("q values must be distinct")
    for q in q_values:
        _require_odd_q(q)
        if q <= 0:
            raise ValueError("frozen field sizes must be positive")
    _require_integer("max_m", max_m)
    if not 1 <= max_m <= MAX_SYMMETRIC_POWER:
        raise ValueError(f"max_m must lie in 1..{MAX_SYMMETRIC_POWER}")

    source = _load_locked_source()
    source_rows = _source_rows(source, q_values)
    guard = ResourceGuard()
    parity_table = quotient_parity_table()
    guard.charge("mod_2_recurrence_rows", len(parity_table))
    frozen = [_transform_source_row(row, max_m, guard) for row in source_rows]

    if q_values == FROZEN_Q_VALUES and max_m == MAX_SYMMETRIC_POWER:
        observed_signature = _extra_fiber_signature(frozen)
        if observed_signature != EXPECTED_EXTRA_FIBER_SIGNATURE:
            raise ArithmeticError("frozen extra-fiber signature changed")

    factor_cache: dict[tuple[int, int, int], tuple[int, ...]] = {}

    def factor(m: int, t: int, q: int) -> tuple[int, ...]:
        key = (m, t, q)
        if key not in factor_cache:
            factor_cache[key] = sym_power_local_factor(m, t, q, guard=guard)
        return factor_cache[key]

    complementary_diagnostics = []
    if 3 in q_values:
        for m in range(1, max_m + 1):
            if m % 6 not in (0, 4, 5):
                continue
            zero_factor = factor(m, 0, 3)
            positive_factor = factor(m, 3, 3)
            negative_factor = factor(m, -3, 3)
            if zero_factor == positive_factor:
                raise ArithmeticError("constructed zero/nonzero scalar alias became a full-factor alias")
            expected_sign_equality = m % 2 == 0 or m % 6 == 5
            if (positive_factor == negative_factor) != expected_sign_equality:
                raise ArithmeticError("q=3 sign-factor diagnostic changed")
            complementary_diagnostics.append(
                {
                    "m": m,
                    "common_scalar_trace_for_t_0_and_3": tau(m, 0, 3),
                    "t_0_vs_t_3_full_factor_equal": False,
                    "t_3_vs_t_minus_3_full_factor_equal": positive_factor == negative_factor,
                    "t_0_factor_sha256": _factor_sha256(zero_factor),
                    "t_3_factor_sha256": _factor_sha256(positive_factor),
                    "t_minus_3_factor_sha256": _factor_sha256(negative_factor),
                }
            )

    m4_zero = sym4_local_factor_closed(0, 3)
    m4_three = sym4_local_factor_closed(3, 3)
    if m4_zero != factor(4, 0, 3) or m4_three != factor(4, 3, 3):
        raise ArithmeticError("closed and Newton Sym^4 factors disagree")

    m5_zero = factor(5, 0, 3)
    m5_three = factor(5, 3, 3)
    m5_minus_three = factor(5, -3, 3)
    q31_minus_seven = factor(5, -7, 31)
    q31_three = factor(5, 3, 31)
    if tau(5, -7, 31) != 5544 or tau(5, 3, 31) != 5544:
        raise ArithmeticError("q=31 ordinary-looking scalar witness changed")
    if q31_minus_seven == q31_three:
        raise ArithmeticError("q=31 scalar alias unexpectedly became a factor alias")

    q3_histogram = {
        int(t): int(count)
        for t, count in next(row for row in source_rows if int(row["q"]) == 3)[
            "model_trace_histogram"
        ].items()
    } if 3 in q_values else {}

    fixture: dict[str, object] = {
        "schema": "riemann.function_field.elliptic_symmetric_power_trace_aliasing.v1",
        "packet_id": "FUNCTION_FIELD.ELLIPTIC.SYMMETRIC_POWER.SCALAR_TRACE_ALIASING.V1",
        "status": "EXACT_INTEGER_THEOREM_PLUS_SOURCE_LOCKED_HISTOGRAM_TRANSFORMS",
        "rigor_level": "PROVED_ALGEBRAIC_CLASSIFICATION_WITH_BOUNDED_EXACT_REPLAY",
        "scalar_trace_definition": {
            "notation": "tau_m(t;q)=E_m(t,q)",
            "initial_values": {"E_0": "1", "E_1": "t"},
            "recurrence": "E_m=t*E_(m-1)-q*E_(m-2)",
            "closed_formula": "sum_(j=0)^floor(m/2) (-1)^j binom(m-j,j) q^j t^(m-2j)",
            "representation_meaning": "sum_(i=0)^m alpha^(m-i) beta^i for alpha+beta=t, alpha*beta=q",
            "firewall": "one scalar trace, not the full degree-(m+1) Sym^m local factor",
        },
        "integer_collision_theorem": {
            "scope": "every odd integer q and all x,y in Z; elliptic applications take q a positive odd prime power",
            "odd_classes": "if m=1 or 3 mod 6, tau_m(x;q)=tau_m(y;q) iff x=y",
            "even_class": "if m=2 mod 6, tau_m(x;q)=tau_m(y;q) iff x=+y or x=-y",
            "hasse_bound_used": False,
            "odd_quotient": {
                "definition": "(tau_(2r+1)(x;q)-tau_(2r+1)(y;q))/(x-y)",
                "expanded_term_s": "(-1)^(r-s) binom(r+s+1,2s+1) q^(r-s) H_(2s)(x,y)",
                "after_x_2X_y_2Y": "same coefficient times 2^(2s) H_(2s)(X,Y)",
                "constant_term": "(-1)^r (r+1) q^r",
            },
            "even_quotient": {
                "definition": "(tau_(2r)(x;q)-tau_(2r)(y;q))/(x^2-y^2)",
                "expanded_term_s": "(-1)^(r-s-1) binom(r+s+1,2s+2) q^(r-s-1) sum_(i=0)^s x^(2(s-i))y^(2i)",
                "after_x_2X_y_2Y": "same coefficient times 2^(2s)",
                "constant_term": "(-1)^(r-1) binom(r+1,2) q^(r-1)",
            },
        },
        "mod_2_quotient_recurrence_certificate": {
            "table_index": "r mod 12, with m=2r+1 in the odd column and positive m=2r in the even column",
            "warning": "this is not a claim that the even quotient table has period 12 in m; its period is 12 in r",
            "parity_column_order": ["(0,0)", "(0,1)", "(1,0)", "(1,1)"],
            "recurrences": {
                "odd": "A_r(z)=z A_(r-1)(z)+A_(r-2)(z), A_0=1,A_1=z over F_2",
                "even": "F_r(z)=z F_(r-1)(z)+F_(r-2)(z), F_0=1,F_1=z+1 over F_2",
                "diagonal_values": "formal derivatives at z=0,1; finite recurrence states return after 12 steps",
            },
            "target_conclusion": "every zero in a target row has parity (x,y)=(0,0)",
            "rows": parity_table,
        },
        "two_adic_valuation_certificate": {
            "odd": {
                "numerator_interval": "[r-s+1,r+s+1] contains r+1",
                "factorial_valuation": "v2((2s+1)!)=2s+1-popcount(2s+1)",
                "margin": "v2(product of remaining interval terms)+popcount(2s+1)-1 >= 1 for s>=1",
                "reason": "the odd integer 2s+1>=3 has popcount at least 2",
            },
            "even": {
                "numerator_interval": "[r-s,r+s+1] contains r(r+1)",
                "factorial_valuation": "v2((2s+2)!)=2s+2-popcount(2s+2)",
                "margin": "v2(product after removing r,r+1)+popcount(2s+2)-1 >= 1",
                "power_of_two_case": "if 2s+2 is a power of two, the interval has at least two even terms, so one remains after removing r,r+1",
            },
            "conclusion": "after the parity step, the constant term is the unique least-2-adic-valuation term, so neither quotient can vanish",
        },
        "sharp_complement": {
            "classes": [0, 4, 5],
            "construction": "for k>=0 set q=3^(2k+1), t=3^(k+1), so t^2=3q",
            "hasse_check": "t^2=3q<=4q",
            "six_step_identity": "tau_(m+6)(t;q)=-q^3*tau_m(t;q)",
            "initial_values_m_0_through_5_at_t_squared_3q": [
                "1", "t", "2q", "qt", "q^2", "0"
            ],
            "equality": "tau_m(0;q)=tau_m(t;q) for every positive m=0,4,5 mod 6",
            "realization_firewall": "the construction supplies Hasse-admissible integer traces; only q=3 is source-witnessed here",
            "q_3_locked_source_witness": {
                "source_trace_weights": {str(t): q3_histogram[t] for t in (-3, 0, 3)} if q3_histogram else {},
                "complementary_rows_through_m_18": complementary_diagnostics,
            },
        },
        "full_factor_diagnostics": {
            "scope": "diagnostics only; the theorem above classifies scalar tau_m fibers, not full-factor fibers",
            "general_zero_vs_nonzero_resolution": {
                "second_root_power_sum_at_t_0": "(-1)^m (m+1) q^m",
                "second_root_power_sum_at_t_squared_3q": "q^m U_m(1/2)",
                "conclusion": "these differ for every positive m=0,4,5 mod 6, so the constructed t=0 versus t collision is not a full-factor collision",
            },
            "sign_nuance": {
                "even_m": "t and -t always give the same full Sym^m factor",
                "odd_m_5_mod_6_at_t_squared_3q": "the normalized spectrum is a union of complete six-cycles and is invariant under negation, so the t and -t full factors coincide",
            },
            "q_3_m_4": {
                "common_scalar_trace": 9,
                "t_0_raw_second_coefficient": sym4_second_elementary_coefficient(0, 3),
                "t_3_raw_second_coefficient": sym4_second_elementary_coefficient(3, 3),
                "t_0_normalized_second_coefficient": [-2, 1],
                "t_3_normalized_second_coefficient": [1, 1],
                "t_0_full_factor": list(m4_zero),
                "t_3_full_factor": list(m4_three),
            },
            "q_3_m_5": {
                "common_scalar_trace_for_t_minus3_0_3": 0,
                "t_0_full_factor": list(m5_zero),
                "t_3_full_factor": list(m5_three),
                "t_minus_3_full_factor": list(m5_minus_three),
                "t_3_equals_t_minus_3_but_not_t_0": m5_three == m5_minus_three and m5_three != m5_zero,
            },
            "q_31_m_5_ordinary_looking_scalar_witness": {
                "traces": [-7, 3],
                "hasse_check": {
                    "trace_squares": [49, 9],
                    "four_q": 124,
                    "both_within_bound": True,
                },
                "both_traces_prime_to_q": True,
                "common_scalar_trace": 5544,
                "t_minus_7_full_factor": list(q31_minus_seven),
                "t_3_full_factor": list(q31_three),
                "full_factors_equal": False,
                "curve_realization_claimed": False,
            },
        },
        "m_5_collision_curve_target": {
            "quotient_equation": "3q^2-4q(x^2+xy+y^2)+(x^4+x^3y+x^2y^2+xy^3+y^4)=0",
            "elimination_substitution": "z=3q-2(x^2+xy+y^2)",
            "binary_quartic_model": "z^2=x^4+5x^3y+9x^2y^2+5xy^3+y^4",
            "dehomogenized_quartic_discriminant": 189,
            "geometric_status": "the nonzero discriminant gives a nonsingular genus-one smooth projective model over characteristic zero",
            "q_31_point": {
                "x": -7,
                "y": 3,
                "q": 31,
                "z": 19,
                "quotient": m5_collision_quotient_closed(-7, 3, 31),
                "quartic_value": m5_collision_quartic(-7, 3),
            },
            "scope": "recorded as a future Diophantine target, not solved or claimed novel here",
        },
        "source_lock": {
            "fixture": _relative(SOURCE_FIXTURE_PATH),
            "producer": _relative(SOURCE_PRODUCER_PATH),
            "schema": EXPECTED_SOURCE_SCHEMA,
            "payload_sha256": EXPECTED_SOURCE_PAYLOAD_SHA256,
            "fixture_sha256_lf_normalized": EXPECTED_SOURCE_FIXTURE_SHA256_LF,
            "producer_sha256_lf_normalized": EXPECTED_SOURCE_PRODUCER_SHA256_LF,
            "normalization": EXPECTED_SOURCE_NORMALIZATION,
            "consumed_measure": "uniform monic squarefree cubic models, equivalently normalized elliptic-moduli-stack measure; not uniform coarse isomorphism classes",
        },
        "frozen_histogram_transforms": frozen,
        "frozen_extra_fiber_signature": [
            {
                "q": q,
                "m": m,
                "scalar_trace": scalar,
                "expected_domain_class_representatives": list(representatives),
            }
            for q, m, scalar, representatives in _extra_fiber_signature(frozen)
        ],
        "literature_boundary": {
            "references": [
                {
                    "authors": "Stephen D. Cohen",
                    "title": "Dickson Polynomials of the Second Kind that Are Permutations",
                    "venue": "Canadian Journal of Mathematics 46 (1994), 225-238",
                    "doi": "10.4153/CJM-1994-009-8",
                    "url": "https://doi.org/10.4153/CJM-1994-009-8",
                },
                {
                    "authors": "Longjiang Qu and Cunsheng Ding",
                    "title": "Dickson Polynomials of the Second Kind that Permute Z_m",
                    "venue": "SIAM Journal on Discrete Mathematics 28 (2014), 722-735",
                    "doi": "10.1137/130942589",
                    "url": "https://doi.org/10.1137/130942589",
                },
                {
                    "authors": "Phil Martin and Mark Watkins",
                    "title": "Symmetric powers of elliptic curve L-functions",
                    "identifier": "arXiv:math/0604095",
                    "url": "https://arxiv.org/abs/math/0604095",
                },
            ],
            "boundary": "Dickson second-kind permutation theory and elliptic symmetric-power computations are prior literature; no originality or priority claim is made for the recurrence, congruence phenomena, or packet calculations",
        },
        "resource_contract": {
            "arithmetic": "exact integers only",
            "new_curve_or_field_enumerations": 0,
            "random_samples": 0,
            "external_databases": 0,
            "frozen_q_values": list(q_values),
            "maximum_symmetric_power": max_m,
            "source_histogram_atoms": sum(row["source_histogram_atom_count"] for row in frozen),
            "source_members_represented": sum(row["source_member_count"] for row in frozen),
            "accounted_work_units": guard.total,
            "accounted_work_unit_ledger": dict(sorted(guard.ledger.items())),
            "accounted_work_unit_cap_exclusive": guard.cap,
        },
        "scope_firewall": {
            "scalar_trace_aliasing_is_not_a_full_local_factor_classification": True,
            "constructed_zero_vs_nonzero_aliases_are_resolved_by_full_factors": True,
            "odd_m_5_mod_6_sign_pair_can_still_share_a_full_factor": True,
            "even_sign_pair_full_factor_equality_is_expected": True,
            "q_31_witness_is_not_claimed_to_be_realized_by_curves": True,
            "frozen_histograms_are_transforms_not_new_enumerations": True,
            "source_measure_is_not_uniform_coarse_isomorphism_classes": True,
            "no_literature_priority_claim": True,
            "no_automorphy_zero_free_region_rh_or_grh_claim": True,
        },
        "producer": {
            "script": _relative(Path(__file__)),
            "script_sha256_lf_normalized": _lf_sha256(Path(__file__)),
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


def _write_fixture(path: Path) -> None:
    fixture = build_fixture()
    path.write_text(json.dumps(fixture, indent=2) + "\n", encoding="utf-8")


def _check_fixture(path: Path) -> None:
    expected = build_fixture()
    actual = json.loads(path.read_text(encoding="utf-8"))
    if actual != expected:
        raise SystemExit(f"fixture mismatch: {path}")
    print(
        "elliptic symmetric-power scalar-trace aliasing fixture: OK "
        f"({expected['resource_contract']['accounted_work_units']} accounted units)"
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    actions = parser.add_mutually_exclusive_group(required=True)
    actions.add_argument(
        "--write",
        nargs="?",
        const=str(OUTPUT_PATH),
        metavar="PATH",
        help="write the exact fixture (default: adjacent JSON)",
    )
    actions.add_argument(
        "--check",
        nargs="?",
        const=str(OUTPUT_PATH),
        metavar="PATH",
        help="compare a stored fixture with a fresh exact build",
    )
    arguments = parser.parse_args(argv)
    if arguments.write is not None:
        path = Path(arguments.write)
        _write_fixture(path)
        print(f"wrote {path}")
    else:
        _check_fixture(Path(arguments.check))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
