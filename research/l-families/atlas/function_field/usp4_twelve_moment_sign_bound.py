#!/usr/bin/env python3
"""Bounded exact degree-twelve sign certificate for the USp(4) toy minor.

This is a standalone replay: it recomputes E[F^n], 1 <= n <= 12, from the
C_2 Weyl constant-term formula and then verifies a rational degree-twelve
majorant of 1_{F >= 0}.  It is not a claim of optimality, equidistribution,
or a number-field result.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from fractions import Fraction
from math import comb
from pathlib import Path
from typing import Callable, Mapping, Sequence


Exponent = tuple[int, int]
Laurent = dict[Exponent, int]
HERE = Path(__file__).resolve().parent
Q_SCAN_FIXTURE = HERE / "genus2_q_scan.json"
FROZEN_FIXTURE = HERE / "usp4_twelve_moment_sign_bound.json"
MAX_MOMENT = 12
MAX_LAURENT_PAIR_PRODUCTS = 300_000
MAX_WALL_SECONDS = 3.0
RANGE_MINIMUM = Fraction(-20)
RANGE_MAXIMUM = Fraction(4, 3)
T_OFFSET = Fraction(7, 8)
T_SLOPE = Fraction(3, 32)
POSITIVE_T_START = Fraction(7, 8)
SUPPORT_DEGREE_SIX_UPPER = Fraction(3879608783, 6358302720)
EXPECTED_UPPER = Fraction(
    165373093729595698644691055097919487644206880882919392440503838869,
    318454738700269877013669525120657835305950388794994707229994647552,
)

# p(t)=C*R(t)*(t^2+A*t+B).  The rational roots and all Bernstein data are
# deliberately stored rather than rounded discovery output.
ROOTS = (
    Fraction(-3, 5),
    Fraction(-43, 200),
    Fraction(11, 60),
    Fraction(67, 125),
    Fraction(35, 48),
)
CONTACT = Fraction(241, 250)
QUADRATIC_A = Fraction(
    -292080562756243180434965055025680670918947,
    148806306458197603987574904445814460733375,
)
QUADRATIC_B = Fraction(
    1148458206507100181804601557001496133127912757,
    1190450451665580831900599235566515685867000000,
)
SCALE = Fraction(
    30475531562638869296655340430502801558195200000000000000000000,
    1186336348579339224896093924048013371623867708425949168317,
)
EXPECTED_BERNSTEIN_QUOTIENT = (
    Fraction(29284103937015345717173456893224078486187647520187500, 25288161772367538417118633045985403073041746645871),
    Fraction(399648743065966861121258067290926713037082101908995007422406250, 288279732704779431649750823543667249304599853147505647901031),
    Fraction(5742562070572400321120210988219060015374435551684138935375734375, 3459356792457353179797009882524006991655198237770067774812372),
    Fraction(32091366921109710124405884300961528405947308983721352954445203125, 16143665031467648172386046118445365961057591776260316282457736),
    Fraction(14410055729662610270342264499476281087719057843637322125824218750, 6053874386800368064644767294417012235396596916097618605921651),
    Fraction(69006472017118308528849449627112105665354878292448773935629265625, 24215497547201472258579069177668048941586387664390474423686604),
    Fraction(13764950600633618781637505414837567582002291693596861623142828125, 4035916257866912043096511529611341490264397944065079070614434),
    Fraction(7057739437649792904762485819894074681963185321441071890376890625, 1729678396228676589898504941262003495827599118885033887406186),
    Fraction(86120003693219609724128317545540771095798918896325282042750000, 17649779553353842754066376951653096896199991009030958034757),
    Fraction(1270720865319060519228960515743693354686202365023902317500000, 217898513004368429062547863600655517237036926037419234997),
)


class Budget:
    """Small explicit resource guard for the Laurent replay."""

    def __init__(self, clock: Callable[[], float], deadline: float) -> None:
        self.clock = clock
        self.deadline = deadline
        self.pair_products = 0

    def charge(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("operation charge must be nonnegative")
        self.pair_products += amount
        if self.pair_products > MAX_LAURENT_PAIR_PRODUCTS:
            raise TimeoutError("USp(4) Laurent operation cap exceeded")
        if self.clock() > self.deadline:
            raise TimeoutError("USp(4) exact replay exceeded monotonic wall deadline")


def _clean(polynomial: Mapping[Exponent, int]) -> Laurent:
    return {exponent: value for exponent, value in polynomial.items() if value}


def _add(*polynomials: Mapping[Exponent, int]) -> Laurent:
    result: Laurent = {}
    for polynomial in polynomials:
        for exponent, value in polynomial.items():
            result[exponent] = result.get(exponent, 0) + value
    return _clean(result)


def _scale(polynomial: Mapping[Exponent, int], scalar: int) -> Laurent:
    return _clean({exponent: scalar * value for exponent, value in polynomial.items()})


def _multiply(left: Mapping[Exponent, int], right: Mapping[Exponent, int], budget: Budget) -> Laurent:
    budget.charge(len(left) * len(right))
    result: Laurent = {}
    for (left_x, left_y), left_value in left.items():
        for (right_x, right_y), right_value in right.items():
            exponent = (left_x + right_x, left_y + right_y)
            result[exponent] = result.get(exponent, 0) + left_value * right_value
    return _clean(result)


def _power(polynomial: Mapping[Exponent, int], exponent: int, budget: Budget) -> Laurent:
    if exponent < 0:
        raise ValueError("Laurent exponent must be nonnegative")
    result: Laurent = {(0, 0): 1}
    factor = dict(polynomial)
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = _multiply(result, factor, budget)
        remaining //= 2
        if remaining:
            factor = _multiply(factor, factor, budget)
    return result


def _constant_term(polynomial: Mapping[Exponent, int]) -> int:
    return polynomial.get((0, 0), 0)


def _trace_character() -> Laurent:
    return {(1, 0): 1, (-1, 0): 1, (0, 1): 1, (0, -1): 1}


def _exterior_square_character() -> Laurent:
    return {(0, 0): 2, (1, 1): 1, (1, -1): 1, (-1, 1): 1, (-1, -1): 1}


def _statistic_character(budget: Budget) -> Laurent:
    return _add(
        _power(_trace_character(), 2, budget),
        _scale(_power(_exterior_square_character(), 2, budget), -1),
    )


def _weyl_density(budget: Budget) -> Laurent:
    density: Laurent = {(0, 0): 1}
    for root in ((2, 0), (0, 2), (1, 1), (1, -1)):
        positive = {root: 1}
        negative = {(-root[0], -root[1]): 1}
        density = _multiply(
            density, _add({(0, 0): 1}, _scale(positive, -1)), budget
        )
        density = _multiply(
            density, _add({(0, 0): 1}, _scale(negative, -1)), budget
        )
    return density


def haar_moments(*, clock: Callable[[], float] = time.monotonic, maximum_wall_seconds: float = MAX_WALL_SECONDS) -> tuple[list[int], int]:
    """Recompute all frozen moments with exact integer Laurent arithmetic."""

    if maximum_wall_seconds <= 0 or maximum_wall_seconds > MAX_WALL_SECONDS:
        raise ValueError(f"wall limit must lie in (0,{MAX_WALL_SECONDS}]")
    budget = Budget(clock, clock() + maximum_wall_seconds)
    density = _weyl_density(budget)
    order = _constant_term(density)
    if order != 8:
        raise ArithmeticError(f"unexpected C2 Weyl normalization {order}")
    statistic = _statistic_character(budget)
    current: Laurent = {(0, 0): 1}
    moments: list[int] = []
    for _ in range(MAX_MOMENT):
        current = _multiply(current, statistic, budget)
        numerator = _constant_term(_multiply(current, density, budget))
        if numerator % order:
            raise ArithmeticError("Haar constant term is not divisible by the Weyl order")
        moments.append(numerator // order)
    return moments, budget.pair_products


def _poly_multiply(left: Sequence[Fraction], right: Sequence[Fraction]) -> list[Fraction]:
    if not left or not right:
        return []
    result = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            result[left_index + right_index] += left_value * right_value
    return result


def _poly_eval(coefficients: Sequence[Fraction], value: Fraction) -> Fraction:
    return sum((coefficient * value**index for index, coefficient in enumerate(coefficients)), Fraction(0))


def _poly_derivative(coefficients: Sequence[Fraction]) -> list[Fraction]:
    return [index * coefficients[index] for index in range(1, len(coefficients))]


def _divide_by_linear(coefficients: Sequence[Fraction], root: Fraction) -> tuple[list[Fraction], Fraction]:
    if len(coefficients) < 2:
        raise ValueError("linear division needs a nonconstant polynomial")
    quotient = [Fraction(0) for _ in range(len(coefficients) - 1)]
    quotient[-1] = coefficients[-1]
    for index in range(len(coefficients) - 2, 0, -1):
        quotient[index - 1] = coefficients[index] + root * quotient[index]
    return quotient, coefficients[0] + root * quotient[0]


def _affine_compose(coefficients: Sequence[Fraction], offset: Fraction, slope: Fraction) -> list[Fraction]:
    result = [Fraction(0)]
    affine_power = [Fraction(1)]
    for coefficient in coefficients:
        if len(result) < len(affine_power):
            result.extend(Fraction(0) for _ in range(len(affine_power) - len(result)))
        for index, value in enumerate(affine_power):
            result[index] += coefficient * value
        affine_power = _poly_multiply(affine_power, [offset, slope])
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def _power_to_bernstein(coefficients: Sequence[Fraction]) -> list[Fraction]:
    """Power coefficients in z to same-degree Bernstein coefficients on [0,1]."""

    degree = len(coefficients) - 1
    return [
        sum(
            (coefficients[power] * Fraction(comb(index, power), comb(degree, power)) for power in range(index + 1)),
            Fraction(0),
        )
        for index in range(degree + 1)
    ]


def _fraction_pair(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def _canonical_sha256(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def t_moments(raw_moments: Sequence[int]) -> list[Fraction]:
    if len(raw_moments) != MAX_MOMENT:
        raise ValueError("exactly twelve raw moments are required")
    raw = [Fraction(1), *(Fraction(value) for value in raw_moments)]
    return [
        sum(
            (Fraction(comb(order, power)) * T_OFFSET ** (order - power) * T_SLOPE**power * raw[power] for power in range(order + 1)),
            Fraction(0),
        )
        for order in range(MAX_MOMENT + 1)
    ]


def polynomial_moment(coefficients: Sequence[Fraction], raw_moments: Sequence[int | Fraction]) -> Fraction:
    if len(raw_moments) < len(coefficients) - 1:
        raise ValueError("insufficient raw moments")
    moments = [Fraction(1), *(Fraction(value) for value in raw_moments)]
    return sum((coefficient * moments[index] for index, coefficient in enumerate(coefficients)), Fraction(0))


def majorant_certificate() -> dict[str, object]:
    """Build and replay the exact factorization and Bernstein positivity proof."""

    product = [SCALE]
    for root in ROOTS:
        product = _poly_multiply(product, [root * root, -2 * root, Fraction(1)])
    polynomial_t = _poly_multiply(product, [QUADRATIC_B, QUADRATIC_A, Fraction(1)])
    if len(polynomial_t) != 13:
        raise ArithmeticError("majorant did not have degree twelve")
    if _poly_eval(polynomial_t, POSITIVE_T_START) != 1:
        raise ArithmeticError("majorant fails at the positive endpoint")
    if _poly_eval(polynomial_t, CONTACT) != 1:
        raise ArithmeticError("majorant fails at its interior contact")
    if _poly_eval(_poly_derivative(polynomial_t), CONTACT) != 0:
        raise ArithmeticError("majorant interior contact is not double")
    quotient, remainder = _divide_by_linear(
        [polynomial_t[0] - 1, *polynomial_t[1:]], POSITIVE_T_START
    )
    if remainder:
        raise ArithmeticError("majorant-minus-one did not divide at q")
    quotient, remainder = _divide_by_linear(quotient, CONTACT)
    if remainder:
        raise ArithmeticError("majorant-minus-one did not divide at the first contact")
    quotient, remainder = _divide_by_linear(quotient, CONTACT)
    if remainder:
        raise ArithmeticError("majorant-minus-one did not divide at the double contact")
    quotient_z = _affine_compose(quotient, POSITIVE_T_START, Fraction(1, 8))
    bernstein = _power_to_bernstein(quotient_z)
    if tuple(bernstein) != EXPECTED_BERNSTEIN_QUOTIENT:
        raise ArithmeticError("stored exact Bernstein certificate mismatch")
    if not all(value > 0 for value in bernstein):
        raise ArithmeticError("Bernstein positivity certificate failed")
    quadratic_floor = QUADRATIC_B - QUADRATIC_A * QUADRATIC_A / 4
    if SCALE <= 0 or quadratic_floor <= 0:
        raise ArithmeticError("factorized nonnegativity certificate failed")
    return {
        "polynomial_t": polynomial_t,
        "polynomial_x": _affine_compose(polynomial_t, T_OFFSET, T_SLOPE),
        "quotient_t": quotient,
        "bernstein": bernstein,
        "quadratic_floor": quadratic_floor,
    }


def finite_raw_moments(family: Mapping[str, object]) -> list[Fraction]:
    q = int(family["q"])
    member_count = int(family["member_count"])
    histogram = {int(key): int(value) for key, value in dict(family["K_histogram"]).items()}
    if sum(histogram.values()) != member_count:
        raise ValueError("histogram count mismatch")
    return [
        sum((Fraction(count * value**order, member_count * q ** (2 * order)) for value, count in histogram.items()), Fraction(0))
        for order in range(1, MAX_MOMENT + 1)
    ]


def _finite_bounds(
    polynomial_x: Sequence[Fraction],
) -> tuple[list[dict[str, object]], dict[str, object]]:
    q_scan = json.loads(Q_SCAN_FIXTURE.read_text(encoding="utf-8"))
    payload = dict(q_scan)
    supplied_hash = payload.pop("payload_sha256")
    if supplied_hash != _canonical_sha256(payload):
        raise ValueError("bound q-scan payload hash mismatch")
    rows: list[dict[str, object]] = []
    for family in q_scan["families"]:
        q = int(family["q"])
        raw = finite_raw_moments(family)
        nonnegative_upper = polynomial_moment(polynomial_x, raw)
        negative_lower = 1 - nonnegative_upper
        signs = family["sign_counts"]
        observed_negative = Fraction(int(signs["negative"]), int(family["member_count"]))
        if negative_lower > observed_negative:
            raise ArithmeticError(f"q={q} finite majorant bound failed")
        rows.append(
            {
                "q": q,
                "moment_majorant_nonnegative_upper_bound": _fraction_pair(nonnegative_upper),
                "negative_probability_lower_bound": _fraction_pair(negative_lower),
                "observed_negative_fraction": _fraction_pair(observed_negative),
                "verified_bound_holds": True,
            }
        )
    return rows, {
        "path": "research/l-families/atlas/function_field/genus2_q_scan.json",
        "canonical_sha256": _canonical_sha256(q_scan),
        "payload_sha256": supplied_hash,
    }


def build_fixture(*, clock: Callable[[], float] = time.monotonic, maximum_wall_seconds: float = MAX_WALL_SECONDS) -> dict[str, object]:
    raw, pair_products = haar_moments(clock=clock, maximum_wall_seconds=maximum_wall_seconds)
    if raw != [-1, 3, -11, 56, -374, 3117, -30321, 327688, -3815668, 46998100, -605231862, 8084025096]:
        raise ArithmeticError("unexpected exact C2 Haar moments")
    certificate = majorant_certificate()
    expectation = polynomial_moment(certificate["polynomial_x"], raw)
    if expectation != EXPECTED_UPPER:
        raise ArithmeticError("unexpected degree-twelve Haar expectation")
    if not expectation < SUPPORT_DEGREE_SIX_UPPER:
        raise ArithmeticError("degree-twelve majorant did not improve degree six")
    finite_q_bounds, finite_histogram_source = _finite_bounds(
        certificate["polynomial_x"]
    )
    source_text = Path(__file__).read_text(encoding="utf-8").replace("\r\n", "\n")
    payload: dict[str, object] = {
        "schema": "riemann.atlas.function_field.usp4_twelve_moment_sign_bound.v1",
        "status": "RIGOROUS_EXACT_FINITE_MOMENT_MAJORANT",
        "event": "F>=0",
        "statistic": "F=(Tr U)^2-e_2(U)^2",
        "scope": {
            "haar_statement": "Pr_Haar(F>=0) is at most the stored rational expectation.",
            "not_an_optimality_claim": True,
            "not_an_equidistribution_theorem": True,
            "not_a_number_field_transfer": True,
            "discovery_firewall": "Numerical linear programming nominated the rational factor pattern; acceptance replays only exact rational algebra.",
        },
        "support": {
            "F_interval": [_fraction_pair(RANGE_MINIMUM), _fraction_pair(RANGE_MAXIMUM)],
            "t_coordinate": "t=(3*x+28)/32",
            "t_interval": [_fraction_pair(Fraction(-1)), _fraction_pair(Fraction(1))],
            "nonnegative_event_interval_in_t": [_fraction_pair(POSITIVE_T_START), _fraction_pair(Fraction(1))],
        },
        "weyl_constant_term": {
            "root_system": "C2",
            "positive_roots_as_exponent_pairs": [[2, 0], [0, 2], [1, 1], [1, -1]],
            "formula": "E[f]=CT(f*product_{alpha>0}(1-X^alpha)(1-X^-alpha))/8",
            "density_constant_term": 8,
            "raw_moments_orders_1_through_12": raw,
            "t_moments_orders_0_through_12": [_fraction_pair(value) for value in t_moments(raw)],
            "arithmetic": "exact integer Laurent convolution",
        },
        "majorant": {
            "degree": 12,
            "definition": "P(x)=p((3*x+28)/32)",
            "factorization": {
                "scale": _fraction_pair(SCALE),
                "squared_roots": [_fraction_pair(root) for root in ROOTS],
                "quadratic_low_to_high": [_fraction_pair(QUADRATIC_B), _fraction_pair(QUADRATIC_A), _fraction_pair(Fraction(1))],
                "quadratic_square_completion_floor": _fraction_pair(certificate["quadratic_floor"]),
            },
            "pointwise_statement": "P(x)>=0 on [-20,0], and P(x)>=1 on [0,4/3].",
            "nonnegative_side_proof": "p(t)=C*product(t-r)^2*((t+A/2)^2+B-A^2/4), with C and the stored floor positive.",
            "positive_side_factorization": "p(t)-1=(t-7/8)*(t-241/250)^2*Q(t)",
            "positive_side_bernstein_coordinate": "t=7/8+z/8, z in [0,1]",
            "positive_side_quotient_bernstein_coefficients_degree_9": [_fraction_pair(value) for value in certificate["bernstein"]],
            "positive_side_proof": "All exact Bernstein coefficients of Q are strictly positive; the remaining factors are nonnegative on [7/8,1].",
            "polynomial_x_coefficients_low_to_high": [_fraction_pair(value) for value in certificate["polynomial_x"]],
        },
        "haar_bound": {
            "moment_majorant_nonnegative_upper_bound": _fraction_pair(expectation),
            "negative_probability_lower_bound": _fraction_pair(1 - expectation),
            "support_adapted_degree_six_upper_bound": _fraction_pair(SUPPORT_DEGREE_SIX_UPPER),
            "strict_improvement": _fraction_pair(SUPPORT_DEGREE_SIX_UPPER - expectation),
        },
        "finite_q_bounds": finite_q_bounds,
        "resource_contract": {
            "maximum_moment": MAX_MOMENT,
            "maximum_laurent_pair_products": MAX_LAURENT_PAIR_PRODUCTS,
            "actual_laurent_pair_products": pair_products,
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "random_sampling": False,
            "numerical_integration": False,
            "field_enumeration": False,
            "external_dependencies": False,
        },
        "producer": {
            "source": "research/l-families/atlas/function_field/usp4_twelve_moment_sign_bound.py",
            "source_sha256_lf_normalized": hashlib.sha256(source_text.encode("utf-8")).hexdigest(),
            "finite_histogram_source": finite_histogram_source,
            "runtime_contract": "Python 3.11+ standard library; exact integer and Fraction arithmetic",
        },
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    return payload


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path, help="compare against a checked-in JSON fixture")
    parser.add_argument("--write", type=Path, help="write the exact JSON fixture")
    args = parser.parse_args(argv)
    if args.check and args.write:
        parser.error("--check and --write are mutually exclusive")
    fixture = build_fixture()
    if args.check:
        if json.loads(args.check.read_text(encoding="utf-8")) != fixture:
            raise SystemExit(f"USp(4) twelve-moment fixture mismatch: {args.check}")
        print(f"OK: exact USp(4) twelve-moment fixture matches {args.check}")
        return 0
    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(json.dumps(fixture, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"OK: wrote exact USp(4) twelve-moment fixture {args.write}")
        return 0
    print(json.dumps(fixture, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
