#!/usr/bin/env python3
"""Bounded replay for the primitive-pair harmonic-incidence reduction."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE_COMMIT = "dd1bd8766"
SOURCE_BLOBS = {
    (
        "research/l-families/atlas/function_field/"
        "FFPS_BOUNDARY_FIELD_PRIMITIVE_PAIR_LARGE_SIEVE_GATE.md"
    ): "2abd49b975837c924009e33912e786b4b720e29c",
    (
        "research/l-families/atlas/function_field/"
        "ffps_boundary_field_primitive_pair_large_sieve_gate.py"
    ): "37ee4b1620c6f601dc68d7b97fb8851508c1b176",
    (
        "research/l-families/atlas/function_field/"
        "ffps_boundary_field_primitive_pair_large_sieve_gate.json"
    ): "beee338489fc23f0e74841162a1f422b99b6c71a",
    "tests/test_ffps_boundary_field_primitive_pair_large_sieve_gate.py": (
        "df06ea3e0da15c83ae0a267c1a37dfedd852ff17"
    ),
}
SOURCE_MODULE_PATH = HERE / "ffps_boundary_field_primitive_pair_large_sieve_gate.py"
REPLAY_CHANNEL = (0, 0)
REPLAY_HEIGHT = 4
REPLAY_LIMIT = 180


def load_source_module():
    spec = importlib.util.spec_from_file_location(
        "primitive_pair_source", SOURCE_MODULE_PATH
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load primitive-pair source module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


SOURCE = load_source_module()
RadicalForm = dict[int, Fraction]


def check_source_blobs() -> None:
    for path, expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{SOURCE_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=2,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"frozen source blob mismatch: {path}")


def validate_channel(alpha: int, gamma: int) -> None:
    if (alpha, gamma) not in SOURCE.CHANNELS:
        raise ValueError("invalid primitive-pair channel")


def layer_strata(alpha: int, gamma: int, height: int) -> dict[int, RadicalForm]:
    """Return exact product-incidence strata at one physical primitive height."""
    validate_channel(alpha, gamma)
    if isinstance(height, bool) or not isinstance(height, int) or height < 1:
        raise ValueError("height must be a positive integer")
    left_scale = SOURCE.EXCEPTIONAL_PRIME**alpha
    right_scale = SOURCE.EXCEPTIONAL_PRIME**gamma
    strata: dict[int, RadicalForm] = {}
    for left in range(1, height // left_scale + 1):
        left_mu = SOURCE.mobius(left)
        if left_mu == 0 or left % SOURCE.EXCEPTIONAL_PRIME == 0:
            continue
        physical_left = left_scale * left
        for right in range(1, height // right_scale + 1):
            right_mu = SOURCE.mobius(right)
            if (
                right_mu == 0
                or right % SOURCE.EXCEPTIONAL_PRIME == 0
                or math.gcd(left, right) != 1
            ):
                continue
            physical_right = right_scale * right
            if max(physical_left, physical_right) != height:
                continue
            correlation = SOURCE.toy_correlation(physical_left, physical_right)
            if correlation == 0:
                continue
            incidence = left * right
            form = strata.setdefault(incidence, {})
            SOURCE.add_radical_term(
                form,
                incidence,
                Fraction(left_mu * right_mu) * correlation,
            )
    return {incidence: form for incidence, form in strata.items() if form}


def add_strata(
    left: dict[int, RadicalForm], right: dict[int, RadicalForm]
) -> dict[int, RadicalForm]:
    result = {incidence: dict(form) for incidence, form in left.items()}
    for incidence, form in right.items():
        result[incidence] = SOURCE.add_forms(result.get(incidence, {}), form)
        if not result[incidence]:
            del result[incidence]
    return result


def block_strata(
    alpha: int, gamma: int, heights: tuple[int, ...]
) -> dict[int, RadicalForm]:
    validate_channel(alpha, gamma)
    result: dict[int, RadicalForm] = {}
    for height in heights:
        result = add_strata(result, layer_strata(alpha, gamma, height))
    return result


def panel_from_strata(strata: dict[int, RadicalForm], sieve: int) -> RadicalForm:
    if (
        isinstance(sieve, bool)
        or not isinstance(sieve, int)
        or sieve < 1
        or SOURCE.mobius(sieve) == 0
        or sieve % SOURCE.EXCEPTIONAL_PRIME == 0
    ):
        raise ValueError("sieve must be squarefree, positive, and 67-free")
    result: RadicalForm = {}
    for incidence, form in strata.items():
        if math.gcd(incidence, sieve) == 1:
            result = SOURCE.add_forms(result, form)
    return result


def harmonic_kernel(limit: int, forbidden: int) -> Fraction:
    if (
        isinstance(limit, bool)
        or not isinstance(limit, int)
        or limit < 1
        or isinstance(forbidden, bool)
        or not isinstance(forbidden, int)
        or forbidden < 1
    ):
        raise ValueError("invalid harmonic-kernel input")
    total = Fraction(0)
    for sieve in range(1, limit + 1):
        if (
            SOURCE.mobius(sieve) != 0
            and sieve % SOURCE.EXCEPTIONAL_PRIME != 0
            and math.gcd(sieve, forbidden) == 1
        ):
            total += Fraction(1, sieve)
    return total


def direct_linear_energy(
    strata: dict[int, RadicalForm], limit: int
) -> tuple[RadicalForm, RadicalForm]:
    linear: RadicalForm = {}
    energy: RadicalForm = {}
    for sieve in range(1, limit + 1):
        if SOURCE.mobius(sieve) == 0 or sieve % SOURCE.EXCEPTIONAL_PRIME == 0:
            continue
        panel = panel_from_strata(strata, sieve)
        linear = SOURCE.add_forms(linear, SOURCE.scale_form(panel, Fraction(1, sieve)))
        energy = SOURCE.add_forms(
            energy,
            SOURCE.scale_form(SOURCE.multiply_forms(panel, panel), Fraction(1, sieve)),
        )
    return linear, energy


def gram_linear_energy(
    strata: dict[int, RadicalForm], limit: int
) -> tuple[RadicalForm, RadicalForm]:
    linear: RadicalForm = {}
    energy: RadicalForm = {}
    for incidence, form in strata.items():
        linear = SOURCE.add_forms(
            linear,
            SOURCE.scale_form(form, harmonic_kernel(limit, incidence)),
        )
        for other_incidence, other_form in strata.items():
            kernel = harmonic_kernel(limit, math.lcm(incidence, other_incidence))
            energy = SOURCE.add_forms(
                energy,
                SOURCE.scale_form(SOURCE.multiply_forms(form, other_form), kernel),
            )
    return linear, energy


def aligned_dyadic_intervals(length: int) -> tuple[tuple[int, int], ...]:
    if isinstance(length, bool) or not isinstance(length, int) or length < 1:
        raise ValueError("length must be a positive integer")
    intervals: list[tuple[int, int]] = []
    size = 1
    while size <= length:
        start = 0
        while start + size <= length:
            intervals.append((start, start + size))
            start += size
        size *= 2
    return tuple(intervals)


def prefix_dyadic_decomposition(
    prefix: int, length: int
) -> tuple[tuple[int, int], ...]:
    if (
        isinstance(prefix, bool)
        or not isinstance(prefix, int)
        or isinstance(length, bool)
        or not isinstance(length, int)
        or length < 1
        or not 0 <= prefix <= length
    ):
        raise ValueError("invalid prefix decomposition input")
    intervals: list[tuple[int, int]] = []
    position = 0
    remaining = prefix
    size = 1 << (remaining.bit_length() - 1) if remaining else 0
    while remaining:
        while size > remaining or position % size:
            size //= 2
        intervals.append((position, position + size))
        position += size
        remaining -= size
        if remaining:
            size = 1 << (remaining.bit_length() - 1)
    return tuple(intervals)


def primorial_through(bound: int) -> int:
    if isinstance(bound, bool) or not isinstance(bound, int) or bound < 1:
        raise ValueError("bound must be a positive integer")
    result = 1
    for candidate in range(2, bound + 1):
        if (
            SOURCE.prime_factors(candidate) == (candidate,)
            and candidate != SOURCE.EXCEPTIONAL_PRIME
        ):
            result *= candidate
    return result


def rho(value: int) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("value must be a positive integer")
    result = Fraction(1)
    for prime in SOURCE.prime_factors(value):
        result *= Fraction(prime, prime + 1)
    return result


def harmonic_cube_certificate(
    strata: dict[int, RadicalForm], modulus: int
) -> dict[str, object]:
    modulus_divisors = SOURCE.divisors(modulus)
    normalizer = sum(
        (Fraction(1, divisor) for divisor in modulus_divisors), Fraction(0)
    )
    mean: RadicalForm = {}
    energy: RadicalForm = {}
    for sieve in modulus_divisors:
        panel = panel_from_strata(strata, sieve)
        mean = SOURCE.add_forms(mean, SOURCE.scale_form(panel, Fraction(1, sieve)))
        energy = SOURCE.add_forms(
            energy,
            SOURCE.scale_form(SOURCE.multiply_forms(panel, panel), Fraction(1, sieve)),
        )
    mean = SOURCE.scale_form(mean, Fraction(1, 1) / normalizer)
    energy = SOURCE.scale_form(energy, Fraction(1, 1) / normalizer)

    tilted_mean: RadicalForm = {}
    for incidence, form in strata.items():
        tilted_mean = SOURCE.add_forms(
            tilted_mean, SOURCE.scale_form(form, rho(incidence))
        )
    if mean != tilted_mean:
        raise ArithmeticError("harmonic mean does not match the rho-tilted panel")

    c67 = Fraction(67, 68)
    c67q = c67
    for prime in SOURCE.prime_factors(modulus):
        c67q *= Fraction(prime, prime + 1)
    if c67q * normalizer != c67:
        raise ArithmeticError("incidence-mass coefficient failed to normalize")

    incidence_energy: RadicalForm = {}
    for sieve in modulus_divisors:
        panel = panel_from_strata(strata, sieve)
        incidence_energy = SOURCE.add_forms(
            incidence_energy,
            SOURCE.scale_form(
                SOURCE.multiply_forms(panel, panel), c67q * Fraction(1, sieve)
            ),
        )
    if incidence_energy != SOURCE.scale_form(energy, c67):
        raise ArithmeticError("harmonic-limit energy coefficient mismatch")

    spectral_energy: RadicalForm = {}
    mode_digests: dict[str, str] = {}
    for mode in modulus_divisors:
        mode_norm = Fraction(1)
        for prime in SOURCE.prime_factors(mode):
            mode_norm *= Fraction(prime, (prime + 1) ** 2)
        mode_sum: RadicalForm = {}
        for incidence, form in strata.items():
            if incidence % mode == 0:
                mode_sum = SOURCE.add_forms(
                    mode_sum,
                    SOURCE.scale_form(form, rho(incidence // mode)),
                )
        mode_digests[str(mode)] = SOURCE.radical_digest(mode_sum)
        spectral_energy = SOURCE.add_forms(
            spectral_energy,
            SOURCE.scale_form(SOURCE.multiply_forms(mode_sum, mode_sum), mode_norm),
        )
    if spectral_energy != energy:
        raise ArithmeticError("incidence derivative spectrum does not match energy")

    centered_energy = SOURCE.subtract_forms(energy, SOURCE.multiply_forms(mean, mean))
    return {
        "centered_energy_digest": SOURCE.radical_digest(centered_energy),
        "energy_digest": SOURCE.radical_digest(energy),
        "incidence_classes": len(modulus_divisors),
        "mean_digest": SOURCE.radical_digest(mean),
        "mode_digests": mode_digests,
        "mode_energy_match": True,
        "normalizer": str(normalizer),
        "rho_tilt_match": True,
        "squarefree_harmonic_coefficient_match": True,
    }


def dyadic_certificate(alpha: int, gamma: int, height: int) -> dict[str, object]:
    validate_channel(alpha, gamma)
    heights = tuple(range(height + 1, 2 * height + 1))
    layers = tuple(layer_strata(alpha, gamma, item) for item in heights)
    family = aligned_dyadic_intervals(len(heights))
    family_set = set(family)
    rows = []
    for prefix in range(len(heights) + 1):
        decomposition = prefix_dyadic_decomposition(prefix, len(heights))
        if any(interval not in family_set for interval in decomposition):
            raise ArithmeticError("prefix used a non-dyadic block")
        direct: dict[int, RadicalForm] = {}
        for layer in layers[:prefix]:
            direct = add_strata(direct, layer)
        rebuilt: dict[int, RadicalForm] = {}
        for start, stop in decomposition:
            block: dict[int, RadicalForm] = {}
            for layer in layers[start:stop]:
                block = add_strata(block, layer)
            rebuilt = add_strata(rebuilt, block)
        if direct != rebuilt:
            raise ArithmeticError("dyadic prefix reconstruction failed")
        rows.append(
            {
                "blocks": [list(interval) for interval in decomposition],
                "prefix": prefix,
            }
        )
    return {
        "family_size": len(family),
        "height_count": len(heights),
        "max_blocks_in_prefix": max(len(row["blocks"]) for row in rows),
        "prefix_rows": rows,
    }


def local_euler_certificate(
    primes: tuple[int, ...] = (2, 3, 5, 7),
) -> list[dict[str, str]]:
    rows = []
    for prime in primes:
        local_rho = Fraction(prime, prime + 1)
        # At the formal variable x, (1-x) * ((1-rho*x)/(1-x)) = 1-rho*x.
        # The stored coefficients check the only nontrivial first-order difference.
        correction_linear = Fraction(1, prime + 1)
        if 1 - local_rho != correction_linear:
            raise ArithmeticError("rho Euler correction mismatch")
        rows.append(
            {
                "prime": str(prime),
                "rho": str(local_rho),
                "correction_linear": str(correction_linear),
            }
        )
    return rows


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    alpha, gamma = REPLAY_CHANNEL
    heights = tuple(range(REPLAY_HEIGHT + 1, 2 * REPLAY_HEIGHT + 1))
    strata = block_strata(alpha, gamma, heights)
    direct_linear, direct_energy = direct_linear_energy(strata, REPLAY_LIMIT)
    gram_linear, gram_energy = gram_linear_energy(strata, REPLAY_LIMIT)
    if direct_linear != gram_linear or direct_energy != gram_energy:
        raise ArithmeticError("finite harmonic incidence Gram identity failed")
    modulus = primorial_through(2 * REPLAY_HEIGHT)
    if any(modulus % incidence for incidence in strata):
        raise ArithmeticError("replay primorial does not contain every incidence")
    cube = harmonic_cube_certificate(strata, modulus)
    dyadic = dyadic_certificate(alpha, gamma, REPLAY_HEIGHT)
    return {
        "conditional_gate": {
            "name": "PRIMCAR",
            "estimate": (
                "sum_(I in aligned dyadic height blocks) sum_(d<=D,sf,67-free) "
                "d^-1 |P_I(d)|^2 <<_epsilon (2DH)^epsilon"
            ),
            "implies_primls": True,
            "conditional_implication_to_rh_proved": True,
            "estimate_proved": False,
            "rh_proved": False,
        },
        "exact_reductions": {
            "dyadic_maximal": {
                "bound": (
                    "sum_(d<=D,squarefree,67-free) d^-1 sup_U |P(d;H,U)|^2 "
                    "<= ceil(log2(N+1)) sum_I E_D(I)"
                ),
                "replay": dyadic,
            },
            "finite_incidence_gram": {
                "energy_digest": SOURCE.radical_digest(direct_energy),
                "energy_match": True,
                "kernel": ("K_D(lcm(e,f))=sum_(d<=D,sf,67-free,(d,lcm(e,f))=1)d^-1"),
                "linear_digest": SOURCE.radical_digest(direct_linear),
                "linear_match": True,
                "strata": len(strata),
            },
            "harmonic_limit": {
                "coefficient": "67/(68*zeta(2))",
                "formula": (
                    "lim_(D->infinity) E_D(I)/log(D)="
                    "67/(68*zeta(2))*E_(nu_Q)|P_I(delta)|^2"
                ),
                "replay": cube,
                "zero_mode": (
                    "B_I=sum_(a,b in I) mu(a)rho(a)mu(b)rho(b)"
                    "/sqrt(ab)*R(log(67^alpha*a/(67^gamma*b)))"
                ),
            },
            "rho_euler_factor": {
                "absolute_correction_half_plane": "Re(s)>0",
                "factorization": (
                    "sum_((n,67)=1)mu(n)rho(n)n^-s="
                    "G_rho(s)/((1-67^-s)zeta(s)) for Re(s)>1"
                ),
                "local_rows": local_euler_certificate(),
            },
        },
        "resource_caps": {
            "channel": list(REPLAY_CHANNEL),
            "dyadic_height": REPLAY_HEIGHT,
            "harmonic_limit": REPLAY_LIMIT,
            "incidence_modulus": modulus,
            "pair_cells_per_layer_at_most": (2 * REPLAY_HEIGHT) ** 2,
            "zeta_zeros": 0,
            "finite_fields": 0,
            "curves": 0,
            "l_functions": 0,
        },
        "scope": {
            "harmonic_limit_uniform_in_height": False,
            "maximal_gate_proved": False,
            "primls_proved": False,
            "rh_or_grh_proved": False,
        },
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "git_blobs": SOURCE_BLOBS,
            "imported_theorem": (
                "primitive-pair shell decomposition, PRIMLS=>RH, and exact "
                "finite Boolean-sieve transform"
            ),
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
