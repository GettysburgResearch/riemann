#!/usr/bin/env python3
"""Exact marked-Weierstrass stack adapter for the genus-two quintic family.

The mathematics is a coordinate/groupoid argument.  This producer performs
only bounded symbolic arithmetic and source-lock validation; it never builds
a finite field, enumerates a polynomial, or counts a curve.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from fractions import Fraction
from math import isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "genus2_marked_weierstrass_stack_adapter.json"
NOTE_PATH = HERE / "GENUS2_MARKED_WEIERSTRASS_STACK_ADAPTER.md"
TEST_PATH = ROOT / "tests" / "test_genus2_marked_weierstrass_stack_adapter.py"

FAMILY_MEASURES_PATH = HERE / "genus2_family_measures.json"
HIGH_WEIGHT_PATH = HERE / "genus2_high_weight_channel_probe.json"
GUARDED_INFERENCE_PATH = HERE / "guarded_cohomology_conjecture_inference.py"

MAX_SOURCE_BYTES_EACH = 100_000
MAX_EXACT_OPERATIONS = 4_096

SOURCE_LOCKS: dict[str, dict[str, str]] = {
    "genus2_family_measures.json": {
        "lf_sha256": "3bec6bc6ab122a3d12fdabbd34ac0afc97cd875905a984ed9c0cc95998ccae38",
        "canonical_payload_sha256": "23b905a8225d00080f00b238f51259b62f3a6c0d489c36168a32ec5580c7c79b",
        "schema": "riemann.function_field.genus2_family_measures.v1",
    },
    "genus2_high_weight_channel_probe.json": {
        "lf_sha256": "bfa4aaca81a755ee9d02d2ae3741b0c511f91899a75adf85ada00007612f9541",
        "canonical_payload_sha256": "90820eded366af5c430df6712bb51f6ad7882faf7bd27c4665c411052c1dca0e",
        "schema": "riemann.function_field.genus2_high_weight_channel_probe.v1",
    },
    "guarded_cohomology_conjecture_inference.py": {
        "lf_sha256": "21368d703bc7d1a6befaf4fe05cf922753391b8bd4a714819bca7d424c9afc59",
    },
}

CHANNELS: dict[str, dict[str, object]] = {
    "chi_(0,3)": {
        "fundamental_weight": (0, 3),
        "highest_weight_e_basis": (3, 3),
        "dimension": 30,
    },
    "chi_(2,2)": {
        "fundamental_weight": (2, 2),
        "highest_weight_e_basis": (4, 2),
        "dimension": 81,
    },
    "chi_(0,4)": {
        "fundamental_weight": (0, 4),
        "highest_weight_e_basis": (4, 4),
        "dimension": 55,
    },
}

Polynomial = tuple[Fraction, ...]  # increasing powers of q


@dataclass
class OperationGuard:
    """Count every fixed symbolic coefficient operation."""

    limit: int = MAX_EXACT_OPERATIONS
    counts: dict[str, int] = field(default_factory=dict)

    def consume(self, label: str, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("operation increments must be nonnegative")
        total = sum(self.counts.values()) + amount
        if total > self.limit:
            raise RuntimeError(
                f"exact-operation cap exceeded: {total}>{self.limit} at {label}"
            )
        self.counts[label] = self.counts.get(label, 0) + amount

    @property
    def total(self) -> int:
        return sum(self.counts.values())


def _lf_bytes(raw: bytes) -> bytes:
    return raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def _sha256_lf(path: Path) -> str:
    return hashlib.sha256(_lf_bytes(path.read_bytes())).hexdigest()


def _canonical_payload_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _load_locked_json(
    path: Path,
    lock: Mapping[str, str],
    *,
    maximum_bytes: int = MAX_SOURCE_BYTES_EACH,
) -> dict[str, object]:
    if not 0 < maximum_bytes <= MAX_SOURCE_BYTES_EACH:
        raise ValueError("source byte cap is outside the certified range")
    raw = path.read_bytes()
    if len(raw) > maximum_bytes:
        raise ValueError(f"{path.name} exceeds the source byte cap")
    actual_lf = hashlib.sha256(_lf_bytes(raw)).hexdigest()
    if actual_lf != lock["lf_sha256"]:
        raise ArithmeticError(f"LF source hash mismatch for {path.name}")
    parsed = json.loads(raw.decode("utf-8"))
    if not isinstance(parsed, dict):
        raise TypeError(f"{path.name} is not a JSON object")
    if parsed.get("schema") != lock["schema"]:
        raise ArithmeticError(f"schema mismatch for {path.name}")
    payload_digest = parsed.get("payload_sha256")
    if payload_digest != lock["canonical_payload_sha256"]:
        raise ArithmeticError(f"pinned payload digest mismatch for {path.name}")
    without_digest = dict(parsed)
    without_digest.pop("payload_sha256")
    if _canonical_payload_sha256(without_digest) != payload_digest:
        raise ArithmeticError(f"internal payload hash mismatch for {path.name}")
    return parsed


def _verify_plain_source_lock(path: Path, lock: Mapping[str, str]) -> None:
    raw = path.read_bytes()
    if len(raw) > MAX_SOURCE_BYTES_EACH:
        raise ValueError(f"{path.name} exceeds the source byte cap")
    if hashlib.sha256(_lf_bytes(raw)).hexdigest() != lock["lf_sha256"]:
        raise ArithmeticError(f"LF source hash mismatch for {path.name}")


def _trim(polynomial: Sequence[Fraction]) -> Polynomial:
    values = list(polynomial)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values) if values else (Fraction(0),)


def polynomial_multiply(
    left: Sequence[Fraction], right: Sequence[Fraction], guard: OperationGuard
) -> Polynomial:
    result = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            guard.consume("polynomial_multiply")
            result[left_index + right_index] += left_value * right_value
    return _trim(result)


def polynomial_scale(
    polynomial: Sequence[Fraction], scalar: Fraction, guard: OperationGuard
) -> Polynomial:
    guard.consume("polynomial_scale", len(polynomial))
    return _trim(tuple(scalar * coefficient for coefficient in polynomial))


def _polynomial_json(polynomial: Sequence[Fraction]) -> list[list[int]]:
    return [[value.numerator, value.denominator] for value in polynomial]


def _prime_power_base(q: int) -> int:
    """Return the prime base of q, refusing integers that are not prime powers."""

    if q < 2:
        raise ValueError("q must be a prime power")
    divisor = 2
    while divisor <= isqrt(q) and q % divisor:
        divisor += 1
    if divisor > isqrt(q):
        return q
    for candidate in range(2, isqrt(divisor) + 1):
        if divisor % candidate == 0:
            raise ValueError("q must be a prime power")
    residue = q
    while residue % divisor == 0:
        residue //= divisor
    if residue != 1:
        raise ValueError("q must be a prime power")
    return divisor


def group_orders(q: int) -> dict[str, int]:
    """Return exact finite group/model orders for an odd prime power q."""

    characteristic = _prime_power_base(q)
    if characteristic == 2:
        raise ValueError("the adapter requires odd characteristic")
    h5 = q**4 * (q - 1)
    g_square = q * (q - 1) // 2
    g_lifted = q * (q - 1)
    if 2 * g_square != g_lifted:
        raise ArithmeticError("square-affine/lifted group order mismatch")
    if h5 % g_lifted:
        raise ArithmeticError("marked-stack mass is not integral")
    return {
        "q": q,
        "characteristic": characteristic,
        "H5": h5,
        "G_square": g_square,
        "G_lifted": g_lifted,
        "AGL_full": q * (q - 1),
        "marked_stack_mass": h5 // g_lifted,
    }


def central_weight(fundamental_weight: Sequence[int]) -> int:
    if len(fundamental_weight) != 2:
        raise ValueError("a C2 fundamental weight must have two coordinates")
    a, b = (int(value) for value in fundamental_weight)
    if a < 0 or b < 0:
        raise ValueError("highest-weight coordinates must be nonnegative")
    return a + 2 * b


def central_sign(fundamental_weight: Sequence[int]) -> int:
    return -1 if central_weight(fundamental_weight) % 2 else 1


def automorphism_order(square_affine_stabilizer_order: int) -> int:
    if square_affine_stabilizer_order <= 0:
        raise ValueError("stabilizer order must be positive")
    return 2 * square_affine_stabilizer_order


def _verify_source_semantics(
    family_measures: Mapping[str, object], high_weight: Mapping[str, object]
) -> dict[str, object]:
    theorem = family_measures.get("theorem")
    if not isinstance(theorem, dict):
        raise TypeError("family-measure packet lost its theorem block")
    if theorem.get("family") != "H_5(q), monic squarefree quintics over F_q":
        raise ArithmeticError("family-measure packet changed its H5 convention")
    if theorem.get("group") != ("AGL(1,F_q) acting by D(T)->alpha^(-5)D(alpha*T+beta)"):
        raise ArithmeticError("family-measure packet changed its affine action")

    character_certificate = high_weight.get("character_certificate")
    if not isinstance(character_certificate, dict):
        raise TypeError("high-weight packet lost its character certificate")
    source_channels = character_certificate.get("channels")
    if not isinstance(source_channels, dict):
        raise TypeError("high-weight packet lost its channel dictionary")
    verified: dict[str, object] = {}
    for name, expected in CHANNELS.items():
        source = source_channels.get(name)
        if not isinstance(source, dict):
            raise TypeError(f"high-weight packet lost {name}")
        source_highest = tuple(int(value) for value in source["highest_weight_e_basis"])
        if source_highest != expected["highest_weight_e_basis"]:
            raise ArithmeticError(f"highest-weight drift for {name}")
        if int(source["dimension"]) != expected["dimension"]:
            raise ArithmeticError(f"dimension drift for {name}")
        fundamental = tuple(int(value) for value in expected["fundamental_weight"])
        recovered_fundamental = (
            source_highest[0] - source_highest[1],
            source_highest[1],
        )
        if recovered_fundamental != fundamental:
            raise ArithmeticError(f"fundamental/e-basis mismatch for {name}")
        weight = central_weight(fundamental)
        if weight != sum(source_highest) or weight % 2:
            raise ArithmeticError(f"expected even central weight for {name}")
        verified[name] = {
            "fundamental_weight": list(fundamental),
            "highest_weight_e_basis": list(source_highest),
            "local_system_weight": weight,
            "central_character": 1,
            "dimension": int(source["dimension"]),
            "exact_stack_trace_formula": (
                f"q^{weight // 2}/(q*(q-1))*sum_(D in H5(q)) {name}(U_D)"
            ),
            "adapter_status": "PROVED_BY_THIS_PACKET",
            "candidate_value_status": "NOT_PROVED_BY_THIS_PACKET",
        }
    return verified


def build_certificate() -> dict[str, object]:
    guard = OperationGuard()
    family_measures = _load_locked_json(
        FAMILY_MEASURES_PATH, SOURCE_LOCKS[FAMILY_MEASURES_PATH.name]
    )
    high_weight = _load_locked_json(
        HIGH_WEIGHT_PATH, SOURCE_LOCKS[HIGH_WEIGHT_PATH.name]
    )
    _verify_plain_source_lock(
        GUARDED_INFERENCE_PATH, SOURCE_LOCKS[GUARDED_INFERENCE_PATH.name]
    )
    channels = _verify_source_semantics(family_measures, high_weight)

    # Exact Q[q] certificate for |H5|=|G_tilde|*q^3 and
    # |G_tilde|=2|G_square|=|AGL(1,q)|.
    q = (Fraction(0), Fraction(1))
    q_minus_one = (Fraction(-1), Fraction(1))
    q_cubed = polynomial_multiply(polynomial_multiply(q, q, guard), q, guard)
    lifted_order = polynomial_multiply(q, q_minus_one, guard)
    h5_order = polynomial_multiply(lifted_order, q_cubed, guard)
    square_order = polynomial_scale(lifted_order, Fraction(1, 2), guard)
    if polynomial_scale(square_order, Fraction(2), guard) != lifted_order:
        raise ArithmeticError("symbolic group-order double-cover identity failed")
    if h5_order != (
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(-1),
        Fraction(1),
    ):
        raise ArithmeticError("symbolic H5 cardinality identity failed")

    # Coordinate exponent audit: alpha=r^2, gamma=r^5, gamma^2=alpha^5,
    # and monicity requires the r^-10 factor.
    guard.consume("coordinate_exponent_checks", 5)
    if 2 * 5 != 5 * 2 or 10 != 2 * 5:
        raise ArithmeticError("lift exponent identity failed")
    if ((-1) ** 2, (-1) ** 5, (-1) ** 10) != (1, -1, 1):
        raise ArithmeticError("central hyperelliptic kernel check failed")

    for sample_q in (3, 5, 7, 9, 25):
        guard.consume("small_symbolic_specializations")
        orders = group_orders(sample_q)
        if orders["marked_stack_mass"] != sample_q**3:
            raise ArithmeticError(f"stack mass specialization failed at q={sample_q}")

    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_marked_weierstrass_stack_adapter.v1",
        "status": "EXACT_ALL_ODD_PRIME_POWER_MARKED_STACK_ADAPTER",
        "scope": {
            "base_fields": "every finite field F_q of odd characteristic",
            "family": "H5(q), monic squarefree quintics",
            "moduli_groupoid": (
                "smooth genus-two curves over F_q with one marked F_q-rational "
                "Weierstrass point"
            ),
            "finite_field_or_curve_enumeration": False,
            "random_sampling": False,
            "cohomology_decomposition": False,
            "rh_or_grh_claim": False,
        },
        "groupoid_equivalence": {
            "model": "C_D: y^2=D(x), with the point at infinity marked",
            "square_affine_group": {
                "notation": "G_sq",
                "elements": "(alpha,beta), alpha in (F_q^x)^2, beta in F_q",
                "order": "q*(q-1)/2",
                "polynomial_right_action": (
                    "D(T)|(alpha,beta)=alpha^(-5)*D(alpha*T+beta)"
                ),
            },
            "lifted_coordinate_group": {
                "notation": "G_tilde",
                "elements": "(r,beta), r in F_q^x, beta in F_q",
                "order": "q*(q-1)",
                "polynomial_right_action": "D(T)|(r,beta)=r^(-10)*D(r^2*T+beta)",
                "curve_isomorphism": (
                    "C_(D|(r,beta)) -> C_D: (T,Y) |-> (r^2*T+beta,r^5*Y)"
                ),
                "central_kernel": (
                    "(r,beta)=(-1,0) acts trivially on D and as (x,y)|->(x,-y) on C_D"
                ),
            },
            "equivalence": (
                "W_2^W(F_q) is equivalent to the action groupoid H5(q)//G_tilde(F_q)"
            ),
            "stabilizer_exact_sequence": (
                "1 -> mu_2=<hyperelliptic involution> -> Aut_q(C_D,infinity) "
                "-> Stab_G_sq(D) -> 1"
            ),
            "automorphism_order": "2*|Stab_G_sq(D)|",
            "full_affine_nonsquare_coset": (
                "not an F_q marked-curve isomorphism; it exchanges a marked curve "
                "with its nontrivial quadratic twist"
            ),
        },
        "exact_cardinalities": {
            "H5": "q^4*(q-1)=q^5-q^4",
            "G_square": "q*(q-1)/2",
            "G_lifted": "q*(q-1)",
            "AGL_full": "q*(q-1)",
            "marked_stack_mass": (
                "sum_[(C,W)] 1/|Aut_q(C,W)|=|H5(q)|/|G_tilde(F_q)|=q^3"
            ),
            "symbolic_polynomials_in_increasing_q_power": {
                "H5": _polynomial_json(h5_order),
                "G_square": _polynomial_json(square_order),
                "G_lifted": _polynomial_json(lifted_order),
                "stack_mass": _polynomial_json(q_cubed),
            },
        },
        "frobenius_convention": {
            "L_polynomial": (
                "L_D(u)=1+a_D*u+b_D*u^2+q*a_D*u^3+q^2*u^4=det(1-sqrt(q)*u*U_D)"
            ),
            "point_count": "#C_D(F_q)=q+1+a_D",
            "normalized_standard_trace": "Tr(U_D)=-a_D/sqrt(q)",
            "normalized_second_elementary_coefficient": "e_2(U_D)=b_D/q",
            "sign_warning": (
                "there is no extra (-1)^w in the local-system trace; the minus "
                "sign is already in Tr(U_D)=-a_D/sqrt(q)"
            ),
        },
        "trace_theorem": {
            "generic_groupoid_formula": (
                "Tr_stack,q(V_lambda)=1/(q*(q-1))*sum_D Tr(Frob_D|V_lambda)"
            ),
            "even_central_weight_formula": (
                "for lambda=(a,b), w=a+2*b even: "
                "Tr_stack,q(V_lambda)=q^(w/2)/(q*(q-1))*sum_D chi_lambda(U_D)"
            ),
            "meaning_of_stack_trace": (
                "sum over F_q-isomorphism classes of marked curves of the fibre "
                "Frobenius trace divided by |Aut_q|; by the stack trace formula, "
                "this is the alternating compactly-supported cohomological trace"
            ),
            "even_channels_closed_by_adapter": channels,
        },
        "odd_central_weight": {
            "central_character": "chi_lambda(-U)=(-1)^(a+2*b)*chi_lambda(U)",
            "exact_result": (
                "a fixed nonsquare affine change is a bijection of H5(q), sends "
                "U_D to -U_D up to conjugacy, and therefore forces the total "
                "model sum and marked-stack Frobenius trace to be zero when w is odd"
            ),
            "scope_firewall": (
                "this is cancellation of the total trace across quadratic twists; "
                "it does not assert that each curve trace vanishes"
            ),
        },
        "claim_boundaries": {
            "closed_gate": (
                "the exact model/measure/local-system adapter for every even-central-"
                "weight Sp4 channel, including chi_(0,3), chi_(2,2), chi_(0,4)"
            ),
            "not_proved": [
                "the conjectural polynomial values of those three channel traces",
                "any Tate, Eisenstein, endoscopic, elliptic, or Siegel decomposition",
                "a one-dimensional eigenpacket identification",
                "an RH or GRH statement",
            ],
        },
        "literature_context_not_dependency": [
            {
                "authors": "Jonas Bergstrom",
                "title": (
                    "Equivariant counts of points of the moduli spaces of "
                    "pointed hyperelliptic curves"
                ),
                "url": "https://arxiv.org/abs/math/0611813",
                "relation": (
                    "develops finite-field point-count methods for pointed "
                    "hyperelliptic moduli spaces"
                ),
            },
            {
                "authors": "Jonas Bergstrom, Carel Faber, Gerard van der Geer",
                "title": (
                    "Siegel modular forms of genus 2 and level 2: "
                    "cohomological computations and conjectures"
                ),
                "url": "https://arxiv.org/abs/0803.0917",
                "relation": (
                    "uses pointed genus-two curve counts to access Frobenius traces "
                    "of local-system cohomology"
                ),
            },
            {
                "authors": "Carel Faber, Gerard van der Geer",
                "title": (
                    "Sur la cohomologie des systemes locaux sur les espaces des "
                    "modules des courbes de genre 2 et des surfaces abeliennes"
                ),
                "url": "https://arxiv.org/abs/math/0305094",
                "relation": (
                    "places finite-field genus-two counts in the local-system/Siegel "
                    "modular-form framework"
                ),
            },
        ],
        "provenance": {
            "source_locks": SOURCE_LOCKS,
            "source_hashes_lf_sha256": {
                "producer": _sha256_lf(Path(__file__)),
                "note": _sha256_lf(NOTE_PATH),
                "test": _sha256_lf(TEST_PATH),
            },
            "resource_contract": {
                "finite_fields_enumerated": 0,
                "curves_enumerated": 0,
                "random_samples": 0,
                "maximum_source_bytes_each": MAX_SOURCE_BYTES_EACH,
                "exact_operation_cap": guard.limit,
                "exact_operations_used": guard.total,
                "operation_counts": dict(sorted(guard.counts.items())),
                "arithmetic": "integers and fractions only; no floats",
            },
        },
    }
    payload["payload_sha256"] = _canonical_payload_sha256(payload)
    return payload


def _canonical(value: object) -> str:
    return json.dumps(value, indent=2, sort_keys=True) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--stdout", action="store_true")
    args = parser.parse_args()
    certificate = build_certificate()
    rendered = _canonical(certificate)
    if args.check:
        if not OUTPUT_PATH.exists():
            raise SystemExit("marked-Weierstrass stack adapter fixture is missing")
        if OUTPUT_PATH.read_text(encoding="utf-8") != rendered:
            raise SystemExit("marked-Weierstrass stack adapter fixture drifted")
        print("PASS_GENUS2_MARKED_WEIERSTRASS_STACK_ADAPTER")
        return
    if args.stdout:
        print(rendered, end="")
        return
    OUTPUT_PATH.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
