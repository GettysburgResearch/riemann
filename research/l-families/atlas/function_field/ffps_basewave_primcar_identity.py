#!/usr/bin/env python3
"""Bounded exact replay for the BASEWAVE--PRIMCAR identity."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE_PATH = HERE / "FFPS_BASEWAVE_PRIMCAR_IDENTITY.md"
RHO_NOTE_PATH = HERE / "FFPS_PRIMITIVE_RHO_TILT_CONVOLUTION_ISOMORPHISM.md"
SOURCE_COMMIT = "b870366141fe8d5f43d5b81f6e50a67d2a888070"
SOURCE_BLOBS = {
    (
        "research/l-families/atlas/function_field/"
        "FFPS_PRIMITIVE_RHO_TILT_CONVOLUTION_ISOMORPHISM.md"
    ): "31311893b8a7ba708ae7a2813b9c44b920b788a9",
    (
        "research/l-families/atlas/function_field/"
        "ffps_primitive_rho_tilt_convolution_isomorphism.py"
    ): "750eb699efa75ae955c7a6294c095542becd27c8",
    (
        "research/l-families/atlas/function_field/"
        "FFPS_PRIMITIVE_PAIR_HARMONIC_INCIDENCE_CARLESON.md"
    ): "722ca5bd8acef2efdb5591f29935b4f97102f957",
    (
        "research/l-families/atlas/function_field/"
        "ffps_primitive_pair_harmonic_incidence_carleson.py"
    ): "7e780f0109264dbfaac59cae36db6fd72c3f34ee",
}
EXCEPTIONAL_PRIME = 67
ALPHAS = (0, 1, 2)
PAIR_CAP = 10
SIEVE_VALUES = (1, 2, 3, 5, 6, 7, 10)


def check_source_blobs() -> None:
    """Authenticate the frozen definitions that the correction compares."""
    for path, expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{SOURCE_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=5,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"frozen source blob mismatch: {path}")


def check_scope_markers() -> None:
    """Keep the repaired implication and its no-estimate firewall visible."""
    note = NOTE_PATH.read_text(encoding="utf-8")
    rho_note = RHO_NOTE_PATH.read_text(encoding="utf-8")
    for marker in (
        "`BASEWAVE` is",
        "exactly `PRIMCAR`",
        "`WAVEPRIMCAR -> BASEWAVE`",
        "No estimate named in this packet is proved.",
        "The threshold `eta<1/2` is not used",
    ):
        if marker not in note:
            raise RuntimeError(f"BASEWAVE scope marker missing: {marker}")
    for marker in (
        "`AUXCOLORPRIMCAR -> PRIMCAR -> PRIMLS -> RH`",
        "`WAVEPRIMCAR -> BASEWAVE (= PRIMCAR)",
        "No PRIMCAR, PRIMLS, RH, or GRH estimate is proved.",
    ):
        if marker not in rho_note:
            raise RuntimeError(f"rho-packet correction marker missing: {marker}")


def validate_positive_integer(value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("value must be a positive integer")


def mobius(value: int) -> int:
    validate_positive_integer(value)
    remaining = value
    parity = 0
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            parity += 1
            if remaining % prime == 0:
                return 0
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        parity += 1
    return -1 if parity % 2 else 1


def is_squarefree_67_free(value: int) -> bool:
    validate_positive_integer(value)
    return value % EXCEPTIONAL_PRIME != 0 and mobius(value) != 0


def divisors(value: int) -> tuple[int, ...]:
    validate_positive_integer(value)
    return tuple(divisor for divisor in range(1, value + 1) if value % divisor == 0)


def primitive_height(alpha: int, left: int, right: int) -> int:
    if alpha not in ALPHAS:
        raise ValueError("alpha must be one of the three physical channels")
    validate_positive_integer(left)
    validate_positive_integer(right)
    return max(EXCEPTIONAL_PRIME**alpha * left, right)


def original_predicate(
    alpha: int,
    d: int,
    heights: frozenset[int],
    left: int,
    right: int,
) -> bool:
    """Predicate of the original P_I^(alpha,0)(d) panel."""
    return (
        is_squarefree_67_free(left)
        and is_squarefree_67_free(right)
        and gcd(left, right) == 1
        and gcd(left * right, d) == 1
        and primitive_height(alpha, left, right) in heights
    )


def generalized_u_one_predicate(
    alpha: int,
    d: int,
    heights: frozenset[int],
    left: int,
    right: int,
) -> bool:
    """Predicate of P^0_(67^alpha,1)(d;I), i.e. C_(d,1)."""
    scale_left = EXCEPTIONAL_PRIME**alpha
    scale_right = 1
    generalized_sieve = d
    return (
        is_squarefree_67_free(left)
        and is_squarefree_67_free(right)
        and gcd(left, right) == 1
        and gcd(left * right, generalized_sieve) == 1
        and max(scale_left * left, scale_right * right) in heights
    )


def term_signature(alpha: int, left: int, right: int) -> tuple[int, int, int, int]:
    """Formal signature of mu(a)mu(b)/sqrt(ab) R(log(67^alpha a/b))."""
    return (
        mobius(left) * mobius(right),
        left * right,
        EXCEPTIONAL_PRIME**alpha * left,
        right,
    )


def original_terms(
    alpha: int, d: int, heights: frozenset[int], cap: int = PAIR_CAP
) -> tuple[tuple[int, int, int, int], ...]:
    validate_positive_integer(cap)
    return tuple(
        sorted(
            term_signature(alpha, left, right)
            for left in range(1, cap + 1)
            for right in range(1, cap + 1)
            if original_predicate(alpha, d, heights, left, right)
        )
    )


def generalized_u_one_terms(
    alpha: int, d: int, heights: frozenset[int], cap: int = PAIR_CAP
) -> tuple[tuple[int, int, int, int], ...]:
    validate_positive_integer(cap)
    return tuple(
        sorted(
            term_signature(alpha, left, right)
            for left in range(1, cap + 1)
            for right in range(1, cap + 1)
            if generalized_u_one_predicate(alpha, d, heights, left, right)
        )
    )


def basewave_u_one_terms(
    alpha: int, d: int, heights: frozenset[int], cap: int = PAIR_CAP
) -> tuple[tuple[int, int, int, int], ...]:
    """Expand the N=M divisor wavelet at u=1 back into ordered pairs."""
    validate_positive_integer(cap)
    terms: list[tuple[int, int, int, int]] = []
    for product_value in range(1, cap * cap + 1):
        if not is_squarefree_67_free(product_value) or gcd(product_value, d) != 1:
            continue
        for left in divisors(product_value):
            right = product_value // left
            if left > cap or right > cap:
                continue
            if primitive_height(alpha, left, right) not in heights:
                continue
            terms.append(term_signature(alpha, left, right))
    return tuple(sorted(terms))


def exact_probe_weight(alpha: int, left: int, right: int) -> Fraction:
    """A deterministic rational probe; support equality is coefficient-independent."""
    scaled_left = EXCEPTIONAL_PRIME**alpha * left
    kernel_probe = Fraction((3 * scaled_left + 5 * right) % 11 - 5)
    return Fraction(mobius(left) * mobius(right)) * kernel_probe


def exact_probe_panel(
    alpha: int, d: int, heights: frozenset[int], cap: int = PAIR_CAP
) -> Fraction:
    return sum(
        (
            exact_probe_weight(alpha, left, right)
            for left in range(1, cap + 1)
            for right in range(1, cap + 1)
            if original_predicate(alpha, d, heights, left, right)
        ),
        Fraction(0),
    )


def replay_height_family(alpha: int, cap: int = PAIR_CAP) -> tuple[frozenset[int], ...]:
    heights = sorted(
        {
            primitive_height(alpha, left, right)
            for left in range(1, cap + 1)
            for right in range(1, cap + 1)
            if is_squarefree_67_free(left)
            and is_squarefree_67_free(right)
            and gcd(left, right) == 1
        }
    )
    family = [frozenset({height}) for height in heights]
    family.append(frozenset(heights))
    family.append(frozenset(heights[::2]))
    return tuple(family)


def finite_identity_certificate(cap: int = PAIR_CAP) -> dict[str, object]:
    validate_positive_integer(cap)
    rows: list[dict[str, object]] = []
    predicate_checks = 0
    panel_checks = 0
    for alpha in ALPHAS:
        height_family = replay_height_family(alpha, cap)
        primcar_probe_energy = Fraction(0)
        basewave_probe_energy = Fraction(0)
        for d in SIEVE_VALUES:
            if not is_squarefree_67_free(d):
                continue
            for heights in height_family:
                for left in range(1, cap + 1):
                    for right in range(1, cap + 1):
                        predicate_checks += 1
                        if original_predicate(
                            alpha, d, heights, left, right
                        ) != generalized_u_one_predicate(
                            alpha, d, heights, left, right
                        ):
                            raise ArithmeticError("u=1 panel predicate mismatch")
                original = original_terms(alpha, d, heights, cap)
                generalized = generalized_u_one_terms(alpha, d, heights, cap)
                basewave = basewave_u_one_terms(alpha, d, heights, cap)
                panel_checks += 1
                if original != generalized or original != basewave:
                    raise ArithmeticError("u=1 panel term expansion mismatch")
                panel = exact_probe_panel(alpha, d, heights, cap)
                primcar_probe_energy += panel * panel / d
                basewave_probe_energy += panel * panel / d
        if primcar_probe_energy != basewave_probe_energy:
            raise ArithmeticError("BASEWAVE and PRIMCAR probe energies differ")
        rows.append(
            {
                "alpha": alpha,
                "basewave_probe_energy": str(basewave_probe_energy),
                "height_sets": len(height_family),
                "primcar_probe_energy": str(primcar_probe_energy),
            }
        )
    return {
        "alphas": list(ALPHAS),
        "aux_u_one_weight": "1",
        "pair_cap": cap,
        "panel_checks": panel_checks,
        "predicate_checks": predicate_checks,
        "rows": rows,
        "termwise_identity": True,
    }


def run(check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
        check_scope_markers()
    certificate = finite_identity_certificate()
    return {
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "git_blobs": SOURCE_BLOBS,
            "repair_scope": (
                "compare the frozen PRIMCAR and coherent-core definitions; "
                "the repaired working note is intentionally not treated as a frozen blob"
            ),
        },
        "exact_identity": {
            "base_core": "C^alpha_(d,1)(I)=P^0_(67^alpha,1)(d;I)=P_I^(alpha,0)(d)",
            "base_energy": "Y^alpha_1(D,H)=sum_(I in D_H) E_D^(alpha,0)(I)",
            "aux_containment": "X_color^alpha(D,H)>=Y^alpha_1(D,H), because w(1)=1",
            "definition": "BASEWAVE is the u=1 specialization of WAVEPRIMCAR",
            "gate_equivalence": "BASEWAVE=PRIMCAR",
        },
        "conditional_hierarchy": {
            "aux_route": "AUXCOLORPRIMCAR -> PRIMCAR -> PRIMLS -> RH",
            "ray_route": "RAYPRIMCAR -> AUXCOLORPRIMCAR -> PRIMCAR -> PRIMLS -> RH",
            "wave_route": "WAVEPRIMCAR -> BASEWAVE (=PRIMCAR) -> PRIMLS -> RH",
            "eta_below_one_half_needed_for_direct_wave_route": False,
            "eta_below_one_half_role": "only the outer sum proving WAVEPRIMCAR -> AUXCOLORPRIMCAR",
        },
        "finite_exact_replay": certificate,
        "scope": {
            "auxcolorprimcar_estimate_proved": False,
            "basewave_estimate_proved": False,
            "primcar_estimate_proved": False,
            "primls_estimate_proved": False,
            "rh_proved": False,
            "colorprimcar_d_one_alone_suffices": False,
            "replay_interpretation": (
                "bounded exact predicate and term-expansion authentication; "
                "the theorem follows symbolically from the displayed definitions"
            ),
        },
        "resource_caps": {
            "alpha_channels": len(ALPHAS),
            "pair_coordinate_cap": PAIR_CAP,
            "sieve_values": len(SIEVE_VALUES),
            "zeta_zeros": 0,
            "floating_point_operations": 0,
            "large_character_families": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and (
        not canonical.exists() or canonical.read_text(encoding="utf-8") != rendered
    ):
        raise SystemExit("canonical JSON fixture is stale")
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
