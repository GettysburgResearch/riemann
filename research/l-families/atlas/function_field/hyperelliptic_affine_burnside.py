"""Exact Burnside census for squarefree affine models.

For n=2g+1 and odd prime-power q, this module counts AGL(1,F_q)-orbits
of monic squarefree degree-n polynomials under

    D(T) -> alpha^(-n) D(alpha*T+beta).

It also emits the rational orbit-count generating series across every
polynomial degree.  It evaluates closed divisor sums only and never enumerates
a field, polynomial family, curve, or orbit.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import isqrt
from pathlib import Path


HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = HERE / "hyperelliptic_affine_burnside.json"
NOTE = HERE / "HYPERELLIPTIC_AFFINE_BURNSIDE.md"
TEST = HERE.parents[3] / "tests" / "test_hyperelliptic_affine_burnside.py"
DEFAULT_Q_VALUES = (3, 5, 7, 9, 11, 13, 25)
DEFAULT_MAX_GENUS = 8
DEFAULT_MAX_SERIES_DEGREE = 17
MAX_GENUS = 32
MAX_Q = 1_000_000
MAX_DIVISOR_INSPECTIONS = 20_000
MAX_SERIES_DEGREE = 65
MAX_SERIES_TERM_INSPECTIONS = 20_000


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _lf_sha256(path: Path) -> str:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    return hashlib.sha256(text.encode()).hexdigest()


def prime_characteristic(q: int) -> int:
    """Return the characteristic when q is an odd prime power."""

    if not 3 <= q <= MAX_Q:
        raise ValueError(f"q must lie in [3,{MAX_Q}]")
    for candidate in range(2, isqrt(q) + 1):
        if q % candidate:
            continue
        if any(candidate % d == 0 for d in range(2, isqrt(candidate) + 1)):
            continue
        residue = q
        while residue % candidate == 0:
            residue //= candidate
        if residue != 1:
            raise ValueError("q must be a prime power")
        if candidate == 2:
            raise ValueError("the theorem requires odd q")
        return candidate
    if q == 2:
        raise ValueError("the theorem requires odd q")
    return q


def euler_phi(n: int) -> int:
    result = n
    prime = 2
    residue = n
    while prime * prime <= residue:
        if residue % prime == 0:
            while residue % prime == 0:
                residue //= prime
            result -= result // prime
        prime += 1
    if residue > 1:
        result -= result // residue
    return result


def divisors(n: int) -> list[int]:
    small: list[int] = []
    large: list[int] = []
    for d in range(1, isqrt(n) + 1):
        if n % d:
            continue
        small.append(d)
        if d * d != n:
            large.append(n // d)
    return small + list(reversed(large))


def squarefree_monic_count(q: int, degree: int) -> int:
    """Number of monic squarefree polynomials of the declared degree."""

    if degree < 0:
        raise ValueError("degree must be nonnegative")
    if degree == 0:
        return 1
    if degree == 1:
        return q
    return q**degree - q ** (degree - 1)


def squarefree_nonzero_constant_count(q: int, degree: int) -> int:
    """Monic squarefree polynomials coprime to T."""

    if degree < 0:
        raise ValueError("degree must be nonnegative")
    if degree == 0:
        return 1
    numerator = (q - 1) * (q**degree - (-1) ** degree)
    if numerator % (q + 1):
        raise ArithmeticError("nonzero-constant squarefree count is not integral")
    return numerator // (q + 1)


def scaling_fixed_count(q: int, degree: int, order: int) -> int:
    """Fixed squarefree models for one nontrivial scaling of given order."""

    if order < 2 or (q - 1) % order:
        raise ValueError("order must be a nontrivial divisor of q-1")
    residue = degree % order
    if residue not in (0, 1):
        return 0
    quotient_degree = degree // order
    return squarefree_nonzero_constant_count(q, quotient_degree)


def affine_orbit_series(q: int, maximum_degree: int) -> dict[str, object]:
    """Return coefficients of the exact all-degree rational orbit series."""

    characteristic = prime_characteristic(q)
    if not 0 <= maximum_degree <= MAX_SERIES_DEGREE:
        raise ValueError(
            f"maximum_degree must lie in [0,{MAX_SERIES_DEGREE}]"
        )
    group_order = q * (q - 1)
    nontrivial_orders = [d for d in divisors(q - 1) if d >= 2]
    inspections = (maximum_degree + 1) * len(nontrivial_orders)
    if inspections > MAX_SERIES_TERM_INSPECTIONS:
        raise RuntimeError("orbit-series term-inspection cap exceeded")

    coefficients: list[int] = []
    for degree in range(maximum_degree + 1):
        numerator = squarefree_monic_count(q, degree)
        numerator += q * sum(
            euler_phi(order) * scaling_fixed_count(q, degree, order)
            for order in nontrivial_orders
        )
        if degree % characteristic == 0:
            numerator += (q - 1) * squarefree_monic_count(
                q, degree // characteristic
            )
        if numerator % group_order:
            raise ArithmeticError(
                f"degree-{degree} orbit-series coefficient is not integral"
            )
        coefficients.append(numerator // group_order)
    return {
        "q": q,
        "characteristic": characteristic,
        "maximum_degree": maximum_degree,
        "coefficients_degree_0_up": coefficients,
        "term_inspections": inspections,
    }


def burnside_census(q: int, genus: int) -> dict[str, object]:
    """Return the exact affine orbit count and its fixed-locus decomposition."""

    characteristic = prime_characteristic(q)
    if not 1 <= genus <= MAX_GENUS:
        raise ValueError(f"genus must lie in [1,{MAX_GENUS}]")
    degree = 2 * genus + 1
    group_order = q * (q - 1)
    identity_fixed = squarefree_monic_count(q, degree)

    scaling_rows: list[dict[str, int]] = []
    scaling_total = 0
    inspections = 0
    for order in divisors(q - 1):
        if order < 2:
            continue
        inspections += 1
        if inspections > MAX_DIVISOR_INSPECTIONS:
            raise RuntimeError("divisor-inspection cap exceeded")
        fixed_each = scaling_fixed_count(q, degree, order)
        if not fixed_each:
            continue
        element_count = q * euler_phi(order)
        contribution = element_count * fixed_each
        scaling_total += contribution
        scaling_rows.append(
            {
                "order": order,
                "residue_degree_mod_order": degree % order,
                "quotient_degree": degree // order,
                "scaling_count": euler_phi(order),
                "affine_element_count": element_count,
                "fixed_models_per_element": fixed_each,
                "burnside_numerator_contribution": contribution,
            }
        )

    translation_fixed_each = 0
    translation_total = 0
    if degree % characteristic == 0:
        translation_fixed_each = squarefree_monic_count(
            q, degree // characteristic
        )
        translation_total = (q - 1) * translation_fixed_each

    numerator = identity_fixed + scaling_total + translation_total
    if numerator % group_order:
        raise ArithmeticError("Burnside numerator is not divisible by |AGL(1,q)|")
    orbit_count = numerator // group_order
    stack_cardinality = identity_fixed // group_order
    if stack_cardinality != q ** (degree - 2):
        raise ArithmeticError("affine-stack cardinality is not q^(2g-1)")

    closed_scaling_correction = 0
    for row in scaling_rows:
        order = row["order"]
        quotient_degree = row["quotient_degree"]
        term_numerator = euler_phi(order) * (
            q**quotient_degree - (-1) ** quotient_degree
        )
        if term_numerator % (q + 1):
            raise ArithmeticError("closed scaling correction is not integral")
        closed_scaling_correction += term_numerator // (q + 1)
    closed_translation_correction = 0
    if translation_fixed_each:
        if translation_fixed_each % q:
            raise ArithmeticError("translation correction is not integral")
        closed_translation_correction = translation_fixed_each // q
    closed_orbit_count = (
        q ** (degree - 2)
        + closed_scaling_correction
        + closed_translation_correction
    )
    if orbit_count != closed_orbit_count:
        raise ArithmeticError("fixed-locus and closed divisor-sum counts disagree")

    involution_correction = (q**genus - (-1) ** genus) // (q + 1)
    if not scaling_rows or scaling_rows[0]["order"] != 2:
        raise ArithmeticError("odd-q census lost the universal order-two stratum")
    actual_involution = (
        euler_phi(2)
        * (q**genus - (-1) ** genus)
        // (q + 1)
    )
    if involution_correction != actual_involution:
        raise ArithmeticError("involution correction mismatch")

    orbit_excess = orbit_count - stack_cardinality
    return {
        "q": q,
        "characteristic": characteristic,
        "genus": genus,
        "degree": degree,
        "group_order": group_order,
        "model_count": identity_fixed,
        "affine_stack_cardinality": stack_cardinality,
        "coarse_orbit_count": orbit_count,
        "coarse_orbit_excess": orbit_excess,
        "relative_excess": [orbit_excess, stack_cardinality],
        "universal_involution_correction": involution_correction,
        "lower_order_correction": orbit_excess - involution_correction,
        "fixed_loci": {
            "identity": identity_fixed,
            "nontrivial_scalings": scaling_rows,
            "scaling_contribution_total": scaling_total,
            "nonidentity_translation_count": q - 1,
            "translation_fixed_models_per_element": translation_fixed_each,
            "translation_contribution_total": translation_total,
        },
        "closed_divisor_sum": {
            "stack_term": q ** (degree - 2),
            "scaling_correction": closed_scaling_correction,
            "translation_correction": closed_translation_correction,
            "total": closed_orbit_count,
        },
        "resource_usage": {"divisor_inspections": inspections},
    }


def build_fixture(
    *,
    q_values: tuple[int, ...] = DEFAULT_Q_VALUES,
    maximum_genus: int = DEFAULT_MAX_GENUS,
    maximum_series_degree: int = DEFAULT_MAX_SERIES_DEGREE,
) -> dict[str, object]:
    if not 1 <= maximum_genus <= MAX_GENUS:
        raise ValueError(f"maximum_genus must lie in [1,{MAX_GENUS}]")
    if not q_values:
        raise ValueError("at least one q value is required")
    if not 0 <= maximum_series_degree <= MAX_SERIES_DEGREE:
        raise ValueError(
            f"maximum_series_degree must lie in [0,{MAX_SERIES_DEGREE}]"
        )
    rows = [
        burnside_census(q, genus)
        for q in q_values
        for genus in range(1, maximum_genus + 1)
    ]
    total_inspections = sum(
        int(row["resource_usage"]["divisor_inspections"]) for row in rows
    )
    if total_inspections > MAX_DIVISOR_INSPECTIONS:
        raise RuntimeError("fixture divisor-inspection cap exceeded")
    series = [affine_orbit_series(q, maximum_series_degree) for q in q_values]
    total_series_inspections = sum(int(row["term_inspections"]) for row in series)
    if total_series_inspections > MAX_SERIES_TERM_INSPECTIONS:
        raise RuntimeError("fixture orbit-series inspection cap exceeded")
    rows_by_q_genus = {
        (int(row["q"]), int(row["genus"])): row for row in rows
    }
    for series_row in series:
        q = int(series_row["q"])
        coefficients = series_row["coefficients_degree_0_up"]
        for genus in range(1, maximum_genus + 1):
            degree = 2 * genus + 1
            if degree > maximum_series_degree:
                continue
            if coefficients[degree] != rows_by_q_genus[(q, genus)]["coarse_orbit_count"]:
                raise ArithmeticError("all-degree series lost an odd-degree census")

    genus_two_regression = {
        str(q): burnside_census(q, 2)["coarse_orbit_count"] for q in (3, 5, 7)
    }
    if genus_two_regression != {"3": 29, "5": 132, "7": 349}:
        raise ArithmeticError("genus-two orbit regression failed")

    payload: dict[str, object] = {
        "schema": "riemann.function_field.hyperelliptic_affine_burnside.v1",
        "raw_fixture_id": "FUNCTION_FIELD.HYPERELLIPTIC.ODD_DEGREE.AFFINE_BURNSIDE.V1",
        "rigor_level": "RIGOROUS_ALL_ODD_Q_ALL_FIXED_GENUS_THEOREM",
        "status": "EXACT_CLOSED_BURNSIDE_DIVISOR_SUM",
        "theorem": {
            "family": "monic squarefree D of degree n=2g+1 over F_q",
            "group_action": "D(T)->alpha^(-n)D(alpha*T+beta)",
            "scope": "every odd prime power q and every integer g>=1",
            "affine_stack_cardinality": "q^(2g-1)",
            "coarse_orbit_count": (
                "q^(2g-1) + sum_{d|q-1,d>=2,n mod d in {0,1}} "
                "phi(d)*(q^floor(n/d)-(-1)^floor(n/d))/(q+1) + "
                "1_{p|n}*SF_q(n/p)/q"
            ),
            "nonzero_constant_squarefree_count": (
                "A_m=(q-1)*(q^m-(-1)^m)/(q+1), m>=1"
            ),
            "universal_involution_correction": (
                "(q^g-(-1)^g)/(q+1)"
            ),
            "fixed_genus_asymptotic": (
                "N_(g,q)=q^(2g-1)+(q^g-(-1)^g)/(q+1)+"
                "O_g(q^(floor((2g+1)/3)-1)); relative excess is q^(-g)+lower order"
            ),
            "all_degree_orbit_generating_function": (
                "O_q(u)=[S_q(u)+q*sum_{d|q-1,d>=2}phi(d)*(1+u)*A_q(u^d)"
                "+(q-1)*S_q(u^p)]/[q*(q-1)], where "
                "S_q(u)=(1-q*u^2)/(1-q*u) and "
                "A_q(u)=S_q(u)/(1+u)"
            ),
            "automorphism_resonance_interpretation": (
                "scaling corrections occupy degree classes 0,1 modulo d for d|q-1; "
                "translation corrections occupy multiples of p=char(F_q)"
            ),
            "invariant_average": (
                "uniform equations equal stabilizer-weighted averaging on the declared affine quotient"
            ),
        },
        "proof_skeleton": {
            "scalings": (
                "after translating the fixed point, an order-d scaling fixes exactly "
                "D(S)=S^r*h(S^d), r=n mod d; squarefreeness requires r in {0,1} "
                "and h squarefree with h(0)!=0"
            ),
            "translations": (
                "for beta!=0 in characteristic p, F_q[S]^(S->S+beta)="
                "F_q[S^p-beta^(p-1)S]; fixed degree-n models exist iff p|n, "
                "and composition preserves squarefreeness"
            ),
            "stack": (
                "|H_n(q)|=q^(n-1)(q-1) and |AGL(1,q)|=q(q-1)"
            ),
        },
        "producer": {
            "script": Path(__file__).name,
            "source_sha256_lf_normalized": _lf_sha256(Path(__file__).resolve()),
            "note": NOTE.name,
            "note_sha256_lf_normalized": _lf_sha256(NOTE),
            "test": str(TEST.relative_to(HERE.parents[3])).replace("\\", "/"),
            "test_sha256_lf_normalized": _lf_sha256(TEST),
        },
        "resource_contract": {
            "field_enumeration": "FORBIDDEN_AND_NOT_USED",
            "polynomial_enumeration": "FORBIDDEN_AND_NOT_USED",
            "maximum_q": MAX_Q,
            "maximum_genus": MAX_GENUS,
            "maximum_divisor_inspections": MAX_DIVISOR_INSPECTIONS,
            "observed_divisor_inspections": total_inspections,
            "maximum_series_degree": MAX_SERIES_DEGREE,
            "fixture_series_degree": maximum_series_degree,
            "maximum_series_term_inspections": MAX_SERIES_TERM_INSPECTIONS,
            "observed_series_term_inspections": total_series_inspections,
            "fixture_q_values": list(q_values),
            "fixture_maximum_genus": maximum_genus,
        },
        "genus_two_regression": genus_two_regression,
        "all_degree_orbit_series": series,
        "rows": rows,
        "firewall": (
            "This counts affine presentations retaining the rational branch point at infinity, "
            "not unpointed hyperelliptic curves or the full moduli stack. It proves no "
            "Frobenius equidistribution, L-function moment, number-field transfer, RH, or GRH."
        ),
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    return payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path)
    parser.add_argument("--write", type=Path)
    args = parser.parse_args(argv)
    if args.check and args.write:
        parser.error("--check and --write are mutually exclusive")
    fixture = build_fixture()
    if args.check:
        expected = json.loads(args.check.read_text(encoding="utf-8"))
        if fixture != expected:
            raise SystemExit(f"hyperelliptic Burnside fixture mismatch: {args.check}")
        print(f"OK: exact hyperelliptic Burnside census matches {args.check}")
    elif args.write:
        args.write.write_text(json.dumps(fixture, indent=2) + "\n", encoding="utf-8")
        print(f"WROTE: {args.write}")
    else:
        print(json.dumps(fixture, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
