"""Light exact pilot for Diophantine collisions of the Sym^5 scalar trace.

The scalar character is

    E5(t, q) = t^5 - 4*q*t^3 + 3*q^2*t.

This producer enumerates integer traces, not curves or finite fields.  It also
records an exact birational elliptic-curve bridge and a six-step rational-point
sequence.  All finite searches are guarded by an explicit high-level ledger.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Mapping, Sequence


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "elliptic_sym5_collision_diophantine_pilot.json"
NOTE_PATH = HERE / "ELLIPTIC_SYM5_COLLISION_DIOPHANTINE_PILOT.md"
TEST_PATH = ROOT / "tests" / "test_elliptic_sym5_collision_diophantine_pilot.py"
SOURCE_PATH = HERE / "elliptic_symmetric_power_trace_aliasing.json"

SCHEMA = "riemann.function_field.elliptic_sym5_collision_diophantine_pilot.v1"
EXPECTED_SOURCE_SCHEMA = (
    "riemann.function_field.elliptic_symmetric_power_trace_aliasing.v1"
)
EXPECTED_SOURCE_PAYLOAD_SHA256 = (
    "046f76f43a2af3ac296f5c18c258e61f138e122bee38ec618af489e7e3a9e50e"
)

MAX_Q = 2_000
ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE = 500_000
ELLIPTIC_SEQUENCE_MAX_MULTIPLE = 7
LARGE_PRIME = 363_804_984_411_209_881
LARGE_PRIME_MINUS_ONE_FACTORS = {
    2: 3,
    3: 1,
    5: 1,
    7: 2,
    11: 1,
    4_003: 1,
    5_843: 1,
    240_479: 1,
}
LARGE_PRIME_CERTIFICATE_WITNESS = 23

EXPECTED_SEQUENCE_FACTORIZATIONS = {
    2: {31: 1},
    3: {1_021: 1},
    4: {11: 1, 49_811: 1},
    5: {11: 1, 631: 1, 90_281: 1},
    6: {131: 1, 1_171: 1, 3_301: 1, 22_571: 1},
    7: {LARGE_PRIME: 1},
}


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


class ResourceGuard:
    """Exclusive-cap ledger for declared high-level exact operations."""

    def __init__(self, cap: int = ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE) -> None:
        _require_integer("cap", cap)
        if cap <= 0:
            raise ValueError("cap must be positive")
        self.cap = cap
        self.ledger: Counter[str] = Counter()

    @property
    def total(self) -> int:
        return sum(self.ledger.values())

    def charge(self, name: str, units: int = 1) -> None:
        _require_integer("units", units)
        if units < 0:
            raise ValueError("resource charge must be nonnegative")
        if self.total + units >= self.cap:
            raise RuntimeError(
                f"accounted work would meet or exceed exclusive cap {self.cap}"
            )
        self.ledger[name] += units


def e5_trace(t: int, q: int) -> int:
    """Return t^5-4*q*t^3+3*q^2*t, with strict integer inputs."""

    _require_integer("t", t)
    _require_integer("q", q)
    if q <= 0 or q % 2 == 0:
        raise ValueError("q must be positive and odd")
    return t**5 - 4 * q * t**3 + 3 * q**2 * t


def h2(x: int, y: int) -> int:
    _require_integer("x", x)
    _require_integer("y", y)
    return x * x + x * y + y * y


def k4(x: int, y: int) -> int:
    _require_integer("x", x)
    _require_integer("y", y)
    return x**4 + x**3 * y + x * x * y * y + x * y**3 + y**4


def collision_quotient(x: int, y: int, q: int) -> int:
    """Return (E5(x,q)-E5(y,q))/(x-y) as a polynomial."""

    _require_integer("q", q)
    if q <= 0 or q % 2 == 0:
        raise ValueError("q must be positive and odd")
    return k4(x, y) - 4 * q * h2(x, y) + 3 * q * q


def collision_quartic(x: int, y: int) -> int:
    """Return the binary quartic in the discriminant of the q-quadratic."""

    _require_integer("x", x)
    _require_integer("y", y)
    return x**4 + 5 * x**3 * y + 9 * x * x * y * y + 5 * x * y**3 + y**4


def elimination_pair(x: int, y: int, q: int) -> tuple[int, int]:
    """Return ((3q-2H)^2, W); their difference is 3 times the quotient."""

    _require_integer("q", q)
    if q <= 0 or q % 2 == 0:
        raise ValueError("q must be positive and odd")
    return (3 * q - 2 * h2(x, y)) ** 2, collision_quartic(x, y)


def sym5_second_coefficient(t: int, q: int) -> int:
    """The T^2 coefficient of the full degree-six Sym^5 local factor."""

    _require_integer("t", t)
    _require_integer("q", q)
    return (
        q
        * (q - t * t)
        * (3 * q - t * t)
        * (q * q - 3 * q * t * t + t**4)
    )


def sym5_third_coefficient(t: int, q: int) -> int:
    """The T^3 coefficient of the full degree-six Sym^5 local factor."""

    _require_integer("t", t)
    _require_integer("q", q)
    return (
        -(q**3)
        * t
        * (2 * q - t * t)
        * (3 * q - t * t)
        * (q * q - 3 * q * t * t + t**4)
    )


def sym5_local_factor(t: int, q: int) -> tuple[int, ...]:
    """Closed self-reciprocal degree-six factor det(1-Sym^5(Frob)T)."""

    scalar = e5_trace(t, q)
    c1 = -scalar
    c2 = sym5_second_coefficient(t, q)
    c3 = sym5_third_coefficient(t, q)
    return (1, c1, c2, c3, q**5 * c2, q**10 * c1, q**15)


def _is_prime_trial(n: int) -> bool:
    """Exact trial-division primality for the small integers in this packet."""

    _require_integer("n", n)
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def odd_prime_power(q: int) -> tuple[int, int] | None:
    """Return (odd prime, exponent), or None; intended only for q<=MAX_Q."""

    _require_integer("q", q)
    if q < 3 or q % 2 == 0:
        return None
    for p in range(3, math.isqrt(q) + 1, 2):
        if q % p:
            continue
        if not _is_prime_trial(p):
            return None
        residue = q
        exponent = 0
        while residue % p == 0:
            residue //= p
            exponent += 1
        return (p, exponent) if residue == 1 else None
    return (q, 1) if _is_prime_trial(q) else None


def _first_separating_degree(left: Sequence[int], right: Sequence[int]) -> int | None:
    for degree, (left_value, right_value) in enumerate(zip(left, right)):
        if left_value != right_value:
            return degree
    return None


def _collision_class(x: int, y: int) -> str:
    if x == -y:
        return "sign_pair"
    if x == 0 or y == 0:
        return "zero_nonzero"
    return "general"


def discriminant_first_census(
    max_q: int = MAX_Q, *, guard: ResourceGuard | None = None
) -> dict[str, object]:
    """Exhaust all Hasse-admissible x<y by solving the quadratic for q."""

    _require_integer("max_q", max_q)
    if max_q < 3 or max_q > MAX_Q:
        raise ValueError(f"max_q must lie in 3..{MAX_Q}")
    if guard is None:
        guard = ResourceGuard()
    trace_bound = math.isqrt(4 * max_q)
    solutions: set[tuple[int, int, int]] = set()
    square_quartic_pairs = 0
    q_branches_tested = 0
    prime_power_cache: dict[int, tuple[int, int] | None] = {}

    for x in range(-trace_bound, trace_bound + 1):
        for y in range(x + 1, trace_bound + 1):
            guard.charge("census_unordered_trace_pairs")
            quartic = collision_quartic(x, y)
            z = math.isqrt(quartic)
            if z * z != quartic:
                continue
            square_quartic_pairs += 1
            guard.charge("census_square_quartic_pairs")
            for signed_z in (-z, z):
                q_branches_tested += 1
                guard.charge("census_q_branches_tested")
                numerator = 2 * h2(x, y) + signed_z
                if numerator % 3:
                    continue
                q = numerator // 3
                if q < 3 or q > max_q or q % 2 == 0:
                    continue
                if x * x > 4 * q or y * y > 4 * q:
                    continue
                if q not in prime_power_cache:
                    guard.charge("census_prime_power_classifications")
                    prime_power_cache[q] = odd_prime_power(q)
                if prime_power_cache[q] is None:
                    continue
                if collision_quotient(x, y, q) != 0:
                    raise ArithmeticError("discriminant branch lost the collision equation")
                solutions.add((q, x, y))

    grouped: dict[int, list[dict[str, object]]] = {}
    class_counts: Counter[str] = Counter()
    full_factor_equal_count = 0
    for q, x, y in sorted(solutions):
        guard.charge("census_collision_factor_diagnostics")
        prime, exponent = odd_prime_power(q) or (0, 0)
        left_factor = sym5_local_factor(x, q)
        right_factor = sym5_local_factor(y, q)
        first_separation = _first_separating_degree(left_factor, right_factor)
        collision_class = _collision_class(x, y)
        class_counts[collision_class] += 1
        if first_separation is None:
            full_factor_equal_count += 1
        grouped.setdefault(q, []).append(
            {
                "x": x,
                "y": y,
                "scalar_trace": e5_trace(x, q),
                "collision_class": collision_class,
                "signed_discriminant_root_3q_minus_2H": 3 * q - 2 * h2(x, y),
                "full_local_factors_equal": first_separation is None,
                "first_separating_coefficient_degree": first_separation,
            }
        )

    rows = []
    for q in sorted(grouped):
        prime, exponent = odd_prime_power(q) or (0, 0)
        rows.append(
            {
                "q": q,
                "prime_base": prime,
                "prime_power_exponent": exponent,
                "pairs": grouped[q],
            }
        )

    return {
        "max_q_inclusive": max_q,
        "maximum_absolute_trace_examined": trace_bound,
        "enumeration_method": (
            "enumerate x<y once, require W(x,y) square, then test "
            "q=(2H+z)/3 for both signs of z"
        ),
        "unordered_trace_pairs_examined": (2 * trace_bound + 1) * (2 * trace_bound) // 2,
        "square_quartic_pairs": square_quartic_pairs,
        "q_branches_tested": q_branches_tested,
        "collision_pair_count": len(solutions),
        "q_with_collisions_count": len(rows),
        "class_counts": dict(sorted(class_counts.items())),
        "full_local_factor_equal_pair_count": full_factor_equal_count,
        "rows": rows,
    }


Point = tuple[Fraction, Fraction] | None


def elliptic_add(left: Point, right: Point) -> Point:
    """Group law on Y^2=X^3-6X+5."""

    if left is None:
        return right
    if right is None:
        return left
    x1, y1 = left
    x2, y2 = right
    if x1 == x2 and y1 == -y2:
        return None
    if left == right:
        if y1 == 0:
            return None
        slope = (3 * x1 * x1 - 6) / (2 * y1)
    else:
        slope = (y2 - y1) / (x2 - x1)
    x3 = slope * slope - x1 - x2
    y3 = -y1 + slope * (x1 - x3)
    return x3, y3


def elliptic_multiple(multiplier: int) -> Point:
    _require_integer("multiplier", multiplier)
    if multiplier < 0:
        point = elliptic_multiple(-multiplier)
        return None if point is None else (point[0], -point[1])
    q_point: Point = (Fraction(-2), Fraction(3))
    result: Point = None
    for _ in range(multiplier):
        result = elliptic_add(result, q_point)
    return result


def inverse_elliptic_map(point: Point) -> tuple[Fraction, Fraction]:
    """Return (r,w), where w^2=(r+1/r)^2+5(r+1/r)+7."""

    if point is None:
        raise ValueError("the point at infinity is outside this affine inverse map")
    x_coordinate, y_coordinate = point
    denominator = x_coordinate * x_coordinate - 4
    if denominator == 0:
        raise ValueError("X=+/-2 is an exceptional point of this affine inverse map")
    r = (
        -x_coordinate * x_coordinate
        - 2 * x_coordinate
        + 6
        + 2 * y_coordinate
    ) / denominator
    w = -(
        x_coordinate * x_coordinate - 2 * x_coordinate + 4
    ) / denominator
    return r, w


def forward_elliptic_map(r: Fraction, w: Fraction) -> Point:
    """Map the collision quartic quotient to Y^2=X^3-6X+5."""

    if r == 0:
        raise ValueError("r=0 is an exceptional point of this affine map")
    u = r + 1 / r
    if u == -2:
        raise ValueError("u=-2 is the chosen conic base point")
    m = (w - 1) / (u + 2)
    return 2 * m, (r - 1 / r) * (m * m - 1)


def _fraction_record(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def _verified_factorization(
    value: int, expected: Mapping[int, int], *, large_prime_certificate: bool = False
) -> dict[str, int]:
    product = 1
    for prime, exponent in expected.items():
        _require_integer("factor prime", prime)
        _require_integer("factor exponent", exponent)
        if exponent <= 0:
            raise ValueError("factor exponents must be positive")
        if prime == LARGE_PRIME and large_prime_certificate:
            if not verify_large_prime_certificate():
                raise ArithmeticError("large Lucas/Pocklington certificate failed")
        elif not _is_prime_trial(prime):
            raise ArithmeticError(f"declared factor {prime} is not prime")
        product *= prime**exponent
    if product != value:
        raise ArithmeticError("declared factorization has the wrong product")
    return {str(prime): exponent for prime, exponent in sorted(expected.items())}


def verify_large_prime_certificate() -> bool:
    """Verify a full n-1 Lucas/Pocklington certificate for LARGE_PRIME."""

    n = LARGE_PRIME
    factor_product = 1
    for prime, exponent in LARGE_PRIME_MINUS_ONE_FACTORS.items():
        if not _is_prime_trial(prime):
            return False
        factor_product *= prime**exponent
    if factor_product != n - 1:
        return False
    witness = LARGE_PRIME_CERTIFICATE_WITNESS
    if pow(witness, n - 1, n) != 1:
        return False
    return all(
        math.gcd(pow(witness, (n - 1) // prime, n) - 1, n) == 1
        for prime in LARGE_PRIME_MINUS_ONE_FACTORS
    )


def elliptic_sequence(guard: ResourceGuard) -> list[dict[str, object]]:
    """Build the exact nQ sequence for n=2,...,7 and clear each ratio."""

    point: Point = None
    generator: Point = (Fraction(-2), Fraction(3))
    rows: list[dict[str, object]] = []
    for multiple in range(1, ELLIPTIC_SEQUENCE_MAX_MULTIPLE + 1):
        if multiple > 1:
            guard.charge("elliptic_group_additions")
        point = elliptic_add(point, generator)
        if multiple == 1:
            continue
        if point is None:
            raise ArithmeticError("unexpected point at infinity in pilot sequence")
        guard.charge("elliptic_inverse_lifts")
        r, w = inverse_elliptic_map(point)
        x, y = r.numerator, r.denominator
        if y < 0:
            x, y = -x, -y
        signed_z = w * x * y
        if signed_z.denominator != 1:
            raise ArithmeticError("elliptic lift did not clear to integral z")
        z = signed_z.numerator
        if z * z != collision_quartic(x, y):
            raise ArithmeticError("elliptic lift missed the binary quartic")
        candidates = sorted(
            {
                numerator // 3
                for numerator in (2 * h2(x, y) - z, 2 * h2(x, y) + z)
                if numerator % 3 == 0
                and numerator // 3 > 0
                and x * x <= 4 * (numerator // 3)
                and y * y <= 4 * (numerator // 3)
            }
        )
        if len(candidates) != 1:
            raise ArithmeticError("pilot lift did not select a unique Hasse q")
        q = candidates[0]
        if collision_quotient(x, y, q) != 0:
            raise ArithmeticError("pilot lift missed the collision quotient")
        expected = EXPECTED_SEQUENCE_FACTORIZATIONS[multiple]
        guard.charge("declared_factorization_components_verified", len(expected))
        if q == LARGE_PRIME:
            guard.charge(
                "pocklington_modular_exponentiations",
                1 + len(LARGE_PRIME_MINUS_ONE_FACTORS),
            )
            guard.charge(
                "pocklington_small_prime_trial_certificates",
                len(LARGE_PRIME_MINUS_ONE_FACTORS),
            )
        factors = _verified_factorization(
            q, expected, large_prime_certificate=(q == LARGE_PRIME)
        )
        guard.charge("elliptic_sequence_factor_diagnostics")
        left_factor = sym5_local_factor(x, q)
        right_factor = sym5_local_factor(y, q)
        separation = _first_separating_degree(left_factor, right_factor)
        if separation != 2:
            raise ArithmeticError("pilot non-cyclotomic factors must separate at T^2")
        rows.append(
            {
                "multiple": multiple,
                "elliptic_point": {
                    "X": _fraction_record(point[0]),
                    "Y": _fraction_record(point[1]),
                },
                "primitive_traces": [x, y],
                "gcd_of_traces": math.gcd(abs(x), abs(y)),
                "signed_quartic_root": z,
                "q": q,
                "q_factorization": factors,
                "q_is_prime": len(expected) == 1 and next(iter(expected)) == q,
                "hasse_admissible": x * x <= 4 * q and y * y <= 4 * q,
                "both_traces_outside_scalar_zero_fiber": all(
                    trace != 0
                    and trace * trace != q
                    and trace * trace != 3 * q
                    for trace in (x, y)
                ),
                "scalar_trace": e5_trace(x, q),
                "second_coefficients": [
                    sym5_second_coefficient(x, q),
                    sym5_second_coefficient(y, q),
                ],
                "first_separating_coefficient_degree": separation,
            }
        )
    return rows


def _load_source_lock() -> dict[str, object]:
    source = json.loads(SOURCE_PATH.read_text(encoding="utf-8"))
    if source.get("schema") != EXPECTED_SOURCE_SCHEMA:
        raise RuntimeError("prior trace-alias schema lock mismatch")
    if source.get("payload_sha256") != EXPECTED_SOURCE_PAYLOAD_SHA256:
        raise RuntimeError("prior trace-alias payload lock mismatch")
    unhashed = dict(source)
    payload_hash = unhashed.pop("payload_sha256")
    if _canonical_sha256(unhashed) != payload_hash:
        raise RuntimeError("prior trace-alias payload is internally inconsistent")
    return source


def build_fixture(
    max_q: int = MAX_Q,
    *,
    resource_cap: int = ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE,
) -> dict[str, object]:
    """Build the deterministic exact fixture."""

    _require_integer("max_q", max_q)
    _require_integer("resource_cap", resource_cap)
    if max_q != MAX_Q:
        raise ValueError(f"the frozen fixture requires max_q={MAX_Q}")
    guard = ResourceGuard(resource_cap)
    guard.charge("locked_source_payloads_loaded")
    _load_source_lock()

    census = discriminant_first_census(max_q, guard=guard)
    sequence = elliptic_sequence(guard)
    prime_sequence_rows = [row for row in sequence if row["q_is_prime"]]
    for row in prime_sequence_rows:
        q = int(row["q"])
        for trace in row["primitive_traces"]:
            if math.gcd(abs(int(trace)), q) != 1:
                raise ArithmeticError("prime-field Waterhouse case (1) lost coprimality")

    q_minus_one_product = math.prod(
        prime**exponent
        for prime, exponent in LARGE_PRIME_MINUS_ONE_FACTORS.items()
    )
    pocklington_gcds = {
        str(prime): math.gcd(
            pow(
                LARGE_PRIME_CERTIFICATE_WITNESS,
                (LARGE_PRIME - 1) // prime,
                LARGE_PRIME,
            )
            - 1,
            LARGE_PRIME,
        )
        for prime in LARGE_PRIME_MINUS_ONE_FACTORS
    }

    fixture: dict[str, object] = {
        "schema": SCHEMA,
        "normalization": {
            "base_local_factor": "L_E(T)=1-t*T+q*T^2",
            "sym5_scalar_trace": "E5(t,q)=t^5-4*q*t^3+3*q^2*t",
            "collision_domain": (
                "odd prime powers q; unordered distinct integer traces x<y "
                "satisfying x^2,y^2<=4q"
            ),
            "full_factor": "det(1-Sym^5(Frob_q)*T), degree 6",
        },
        "exact_algebra": {
            "factorization": "E5(t,q)=t*(t^2-q)*(t^2-3q)",
            "collision_quotient": "K-4*q*H+3*q^2",
            "H": "x^2+x*y+y^2",
            "K": "x^4+x^3*y+x^2*y^2+x*y^3+y^4",
            "quadratic_discriminant": "4*W",
            "W": "x^4+5*x^3*y+9*x^2*y^2+5*x*y^3+y^4",
            "elimination_identity": "(3q-2H)^2-W=3*(K-4qH+3q^2)",
            "q_recovery": "q=(2H+z)/3 for either signed square root z of W",
            "zero_fiber_over_odd_prime_powers": {
                "q=p^a_with_a_even": "t in {0,+p^(a/2),-p^(a/2)}",
                "q=3^a_with_a_odd": "t in {0,+3^((a+1)/2),-3^((a+1)/2)}",
                "all_other_q": "t=0 only",
            },
            "weighted_scaling": {
                "map": "(x,y,q)->(d*x,d*y,d^2*q)",
                "quotient_weight": "Q(d*x,d*y,d^2*q)=d^4*Q(x,y,q)",
                "trace_weight": "E5(d*t,d^2*q)=d^5*E5(t,q)",
                "prime_tower_consequence": (
                    "a primitive collision at prime p yields collisions at "
                    "q=p^(2k+1) after d=p^k"
                ),
            },
            "full_factor_coefficients": {
                "T2": (
                    "q*(q-t^2)*(3q-t^2)*(q^2-3q*t^2+t^4)"
                ),
                "T3": (
                    "-q^3*t*(2q-t^2)*(3q-t^2)*(q^2-3q*t^2+t^4)"
                ),
                "zero_vs_nonzero": "always separated at T^2",
                "sign_t2_eq_q": "separated at T^3",
                "sign_t2_eq_3q": "full factors equal",
            },
        },
        "elliptic_curve_bridge": {
            "affine_quartic": "v^2=r^4+5r^3+9r^2+5r+1",
            "quartic_polynomial_discriminant": 189,
            "intermediate": {
                "u": "r+1/r",
                "w": "v/r",
                "conic": "w^2=u^2+5u+7",
                "m": "(w-1)/(u+2)",
            },
            "weierstrass_curve": "Y^2=X^3-6X+5",
            "weierstrass_discriminant": 3_024,
            "forward_map": {
                "X": "2m",
                "Y": "(r-1/r)*(m^2-1)",
            },
            "inverse_map": {
                "r": "(-X^2-2X+6+2Y)/(X^2-4)",
                "w": "-(X^2-2X+4)/(X^2-4)",
            },
            "exceptional_points_are_finite": True,
            "infinite_order_certificate": {
                "Q": [-2, 3],
                "two_Q": [5, -10],
                "lutz_nagell_divisor_abs_4A3_plus_27B2": 189,
                "two_Q_y_squared": 100,
                "divides": False,
                "conclusion": (
                    "By Lutz-Nagell, Q is nontorsion; hence the quartic has "
                    "infinitely many rational points. This does not classify "
                    "integral or prime-power collision points."
                ),
            },
            "multiples_2_through_7": sequence,
        },
        "large_prime_certificate": {
            "n": LARGE_PRIME,
            "method": "full n-1 Lucas/Pocklington criterion",
            "n_minus_one_factorization": {
                str(prime): exponent
                for prime, exponent in LARGE_PRIME_MINUS_ONE_FACTORS.items()
            },
            "factor_product": q_minus_one_product,
            "all_factor_primes_by_trial_division_through_sqrt_240479": True,
            "witness": LARGE_PRIME_CERTIFICATE_WITNESS,
            "fermat_residue": pow(
                LARGE_PRIME_CERTIFICATE_WITNESS,
                LARGE_PRIME - 1,
                LARGE_PRIME,
            ),
            "gcd_certificates_by_distinct_prime_factor": pocklington_gcds,
            "verified": verify_large_prime_certificate(),
        },
        "finite_census": census,
        "prime_field_realization_boundary": {
            "criterion": (
                "Waterhouse Theorem 4.1 case (1): |t|<=2sqrt(q) and "
                "gcd(t,p)=1 gives an ordinary elliptic isogeny class over F_q"
            ),
            "realized_rows": [
                {
                    "q": row["q"],
                    "traces": row["primitive_traces"],
                    "hasse_admissible": row["hasse_admissible"],
                    "each_trace_coprime_to_q": all(
                        math.gcd(abs(int(trace)), int(row["q"])) == 1
                        for trace in row["primitive_traces"]
                    ),
                    "separate_curves_exist_over_F_q": True,
                }
                for row in prime_sequence_rows
            ],
            "weighted_odd_exponent_towers_beyond_the_prime_base": {
                "status": "not realized by elliptic traces for these p>3 bases",
                "reason": (
                    "for k>=1 the field size is p^(2k+1) and each scaled "
                    "nonzero trace p^k*t is divisible by p: Waterhouse case "
                    "(1) fails; cases (2) and (3) require even exponent; case "
                    "(4) requires p in {2,3}; case (5) requires trace zero"
                ),
                "scope": (
                    "the scaling theorem is an exact Hasse-lattice/scalar-"
                    "polynomial tower, not an elliptic-curve realization tower"
                ),
            },
            "square_q_zero_fiber_realization": {
                "q=p^(2k)": (
                    "t=+/-sqrt(q) occurs only when p is not 1 mod 3; t=0 "
                    "occurs only when p is not 1 mod 4"
                ),
                "simultaneous_three_point_zero_fiber": (
                    "requires both Waterhouse congruence conditions; the "
                    "algebraic/Hasse zero fiber alone does not imply realization"
                ),
                "q=3^(odd)": (
                    "t=0 and t=+/-sqrt(3q) are Waterhouse cases (5) and (4)"
                ),
            },
            "global_compatible_family_claimed": False,
        },
        "source_lock": {
            "path": _relative(SOURCE_PATH),
            "schema": EXPECTED_SOURCE_SCHEMA,
            "payload_sha256": EXPECTED_SOURCE_PAYLOAD_SHA256,
            "use": (
                "provenance boundary only; all Sym^5 algebra, census rows, and "
                "elliptic-curve calculations are rederived in this packet"
            ),
        },
        "resource_contract": {
            "new_curve_or_field_enumerations": 0,
            "finite_search_kind": "integer trace-pair discriminant sieve",
            "elliptic_group_additions": guard.ledger["elliptic_group_additions"],
            "accounted_work_ledger": dict(sorted(guard.ledger.items())),
            "accounted_work_units": guard.total,
            "accounted_work_unit_cap_exclusive": guard.cap,
            "maximum_q_in_frozen_census": MAX_Q,
            "larger_blind_search_performed_by_producer": False,
        },
        "literature_boundary": {
            "references": [
                {
                    "author": "Elisabeth Lutz",
                    "title": (
                        "Sur l'equation y^2=x^3-Ax-B dans les corps p-adiques"
                    ),
                    "year": 1937,
                    "url": "https://doi.org/10.1515/crll.1937.177.238",
                    "use": "classical torsion criterion only",
                },
                {
                    "author": "William C. Waterhouse",
                    "title": "Abelian varieties over finite fields",
                    "year": 1969,
                    "url": "https://numdam.org/articles/10.24033/asens.1183/",
                    "use": (
                        "Theorem 4.1 cases (1)-(5), local trace realization "
                        "and nonrealization boundaries only"
                    ),
                },
            ],
            "external_priority_search_performed": False,
            "external_novelty_claim": False,
        },
        "scope_firewall": {
            "scalar_collision_is_not_full_factor_equality": True,
            "hasse_admissibility_is_not_curve_realization": True,
            "waterhouse_rows_assert_separate_local_curves_only": True,
            "weighted_prime_power_towers_are_not_curve_realization_towers": True,
            "square_q_zero_fibers_are_not_automatically_realized": True,
            "no_global_compatible_family_or_euler_product_constructed": True,
            "no_integral_point_classification": True,
            "no_claim_of_infinitely_many_prime_q": True,
            "finite_census_claim_stops_at_q_2000": True,
            "positive_rank_is_not_an_integral_or_prime_power_classification": True,
            "project_relative_discovery_not_literature_priority": True,
        },
        "project_relative_results": {
            "theorems": [
                "complete Hasse-admissible odd-prime-power census through q=2000",
                "exact zero-fiber and weighted prime-power scaling laws",
                "birational positive-rank elliptic bridge",
                (
                    "three exact non-cyclotomic prime bases 31, 1021, and "
                    f"{LARGE_PRIME}, each giving a weighted odd-exponent tower"
                ),
            ],
            "bounded_conjecture": (
                "Primitive prime-power general collisions are sparse and are "
                "controlled by integral/arithmetic constraints on the positive-rank "
                "elliptic curve; no completeness beyond q=2000 is asserted."
            ),
        },
        "producer": {
            "script": _relative(Path(__file__).resolve()),
            "script_sha256_lf_normalized": _lf_sha256(Path(__file__).resolve()),
            "note": _relative(NOTE_PATH),
            "note_sha256_lf_normalized": _lf_sha256(NOTE_PATH),
            "test": _relative(TEST_PATH),
            "test_sha256_lf_normalized": _lf_sha256(TEST_PATH),
        },
    }
    fixture["payload_sha256"] = _canonical_sha256(fixture)
    return fixture


def _serialized_fixture() -> str:
    return json.dumps(build_fixture(), indent=2, sort_keys=True) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail unless the stored deterministic JSON equals a fresh build",
    )
    args = parser.parse_args(argv)
    serialized = _serialized_fixture()
    if args.check:
        if not OUTPUT_PATH.exists() or OUTPUT_PATH.read_text(encoding="utf-8") != serialized:
            raise SystemExit("stored Sym^5 collision fixture is stale")
        print(f"verified {OUTPUT_PATH}")
        return 0
    OUTPUT_PATH.write_text(serialized, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
