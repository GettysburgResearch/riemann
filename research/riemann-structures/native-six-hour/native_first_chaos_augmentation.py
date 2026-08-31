#!/usr/bin/env python3
"""Complete native local-swap projectors and an actual physical-mask defect."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import pairwise, product
from math import prod
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NOTE = HERE / "NATIVE_FIRST_CHAOS_AUGMENTATION.md"
FIXTURE = HERE / "native_first_chaos_augmentation.json"
TEST = ROOT / "tests" / "test_native_six_hour_first_chaos.py"
GE_COMMIT = "15967a52e846f1037bb0446db43f3d4a9c3fc821"
GE_PATH = "research/riemann-structures/native-six-hour/geodesic_factor_exchange.py"
GE_BLOB = "c88f87c164ab1ea5504913c00f257f5b030ab854"
BOOLEAN_COMMIT = "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b"
BOOLEAN_SOURCES = {
    "claims/lemmas/L-106132-boolean-half-source-least-prime-calderon-row.md": "f393a1d8583c5680b98a4b3e26d9b5a61c8d2b7a",
    "claims/lemmas/L-106133-canonical-equal-pair-boolean-source-is-a-beta-half-source-square.md": "b988b14eb982504a799158eed4c76e7f033c96f0",
}
MAX_BYTES = 1048576


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def frozen_bytes(commit, path, blob):
    require(len(commit) == len(blob) == 40, "parent-frozen source pin required")
    ref = f"{commit}:{path}"
    size = int(
        subprocess.run(
            ["git", "cat-file", "-s", ref],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout
    )
    require(0 < size <= MAX_BYTES, "source byte cap")
    raw = subprocess.run(
        ["git", "show", ref], cwd=ROOT, capture_output=True, check=True
    ).stdout
    require(
        len(raw) == size
        and sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest() == blob,
        "frozen geodesic executable authentication",
    )
    return raw


def geodesic_module():
    raw = frozen_bytes(GE_COMMIT, GE_PATH, GE_BLOB)
    namespace = {"__name__": "authenticated_geodesic", "__file__": str(ROOT / GE_PATH)}
    # Only exact Git bytes authenticated against the frozen commit and blob above execute.
    exec(compile(raw, str(ROOT / GE_PATH), "exec"), namespace)  # noqa: S102
    return SimpleNamespace(**namespace)


def validate_exponents(exponents):
    require(
        type(exponents) is tuple and 1 <= len(exponents) <= 9, "bounded exponent tuple"
    )
    require(
        all(type(e) is int and 1 <= e <= 4 for e in exponents),
        "bounded exact exponents",
    )
    require(prod(e + 1 for e in exponents) <= 4096, "vector dimension cap")


def reflect(vector, exponents, coordinate):
    validate_exponents(exponents)
    require(
        type(coordinate) is int and 0 <= coordinate < len(exponents), "coordinate cap"
    )
    require(len(vector) == prod(e + 1 for e in exponents), "complete vector length")
    require(
        all(type(value) in (int, Fraction) for value in vector),
        "exact vector coefficients",
    )
    stride = prod(e + 1 for e in exponents[coordinate + 1 :])
    e = exponents[coordinate]
    return tuple(
        vector[i + (e - 2 * ((i // stride) % (e + 1))) * stride]
        for i in range(len(vector))
    )


def local_projection(vector, exponents, coordinate, sign=1):
    require(type(sign) is int and sign in (-1, 1), "exact projection sign")
    other = reflect(vector, exponents, coordinate)
    return tuple(
        (Fraction(a) + sign * b) / 2 for a, b in zip(vector, other, strict=True)
    )


def character_projection(vector, exponents, odd=()):
    require(
        type(odd) is tuple and len(set(odd)) == len(odd),
        "distinct character coordinates",
    )
    require(
        all(type(j) is int and 0 <= j < len(exponents) for j in odd),
        "character coordinate cap",
    )
    result = tuple(vector)
    for j in range(len(exponents)):
        result = local_projection(result, exponents, j, -1 if j in odd else 1)
    return result


def norm_square(vector):
    return sum((value * value for value in vector), Fraction())


def allowed_dimensions(exponents):
    validate_exponents(exponents)
    symmetric = tuple(e // 2 + 1 for e in exponents)
    antisymmetric = tuple((e + 1) // 2 for e in exponents)
    mean = prod(symmetric)
    singleton = sum(
        antisymmetric[j] * prod(symmetric[:j] + symmetric[j + 1 :])
        for j in range(len(exponents))
    )
    return {
        "ambient": prod(e + 1 for e in exponents),
        "constant": mean,
        "singleton_total": singleton,
        "allowed_subspace": mean + singleton,
        "actual_native_curve_span_claimed": False,
    }


def vector_control(module, spec, include_mask=False):
    labels, exponents, selected_n = spec
    module.validate_spec(labels, exponents)
    allocations = tuple(product(*(range(e + 1) for e in exponents)))
    vector = tuple(
        module.pattern_data(tuple(sorted(zip(exponents, a, strict=True))))["value"]
        for a in allocations
    )
    endpoints = tuple(
        module.pattern_data(tuple(sorted(zip(exponents, a, strict=True))))["endpoint"]
        for a in allocations
    )
    constant = character_projection(vector, exponents)
    require(constant == endpoints, "all-local augmentation equals endpoint tensor")
    first = []
    remainder = list(vector)
    for i, value in enumerate(constant):
        remainder[i] -= value
    for j in range(len(exponents)):
        component = character_projection(vector, exponents, (j,))
        first.append(
            {"prime": labels[j], "counting_norm_square": str(norm_square(component))}
        )
        for i, value in enumerate(component):
            remainder[i] -= value
    require(not any(remainder), "complete native Walsh spectrum has no higher sectors")
    global_swap = tuple(reversed(vector))
    require(
        constant
        == tuple((a + b) / 2 for a, b in zip(vector, global_swap, strict=True)),
        "global-even equals augmentation only on native range",
    )
    require(
        norm_square(vector)
        == norm_square(constant)
        + sum(Fraction(row["counting_norm_square"]) for row in first),
        "literal coefficient-space Walsh orthogonality",
    )
    K = prod(p**e for p, e in zip(labels, exponents, strict=True))
    result = {
        "dimensions": allowed_dimensions(exponents),
        "constant_norm_square": str(norm_square(constant)),
        "singletons": first,
        "full_counting_norm_square": str(norm_square(vector)),
        "complete_higher_Walsh_residual_zero": True,
        "singletons_claimed_orthogonal_in_scalar_Mellin_measure": False,
        "independent_local_swaps_claimed_scalar_Mellin_operators": False,
    }
    if include_mask:
        physical_n = tuple(
            prod(p**a for p, a in zip(labels, row, strict=True)) for row in allocations
        )
        mask = tuple(8 * n * n > K and n * n < 8 * K for n in physical_n)
        require(mask == tuple(reversed(mask)), "ratio mask preserves global exchange")
        masked = tuple(
            v if keep else Fraction() for v, keep in zip(vector, mask, strict=True)
        )
        augment_after_mask = character_projection(masked, exponents)
        mask_after_augment = tuple(
            v if keep else Fraction() for v, keep in zip(constant, mask, strict=True)
        )
        masked_even = tuple(
            (a + b) / 2 for a, b in zip(masked, reversed(masked), strict=True)
        )
        require(
            mask_after_augment == masked_even, "correct ordered masked augmentation"
        )
        orbit = [
            i
            for i, row in enumerate(allocations)
            if all(a in (0, e) for a, e in zip(row, exponents, strict=True))
        ]
        size, retained = len(orbit), sum(mask[i] for i in orbit)
        a = Fraction(-1, 524288)
        require(size == 512 and 0 < retained < size, "actual noncentral orbit mask")
        require(
            all(
                constant[i] == a and augment_after_mask[i] == a * retained / size
                for i in orbit
            ),
            "exact native orbit mean before and after physical mask",
        )
        defect = sum(
            ((augment_after_mask[i] - mask_after_augment[i]) ** 2 for i in orbit),
            Fraction(),
        )
        require(
            defect == a * a * retained * (1 - Fraction(retained, size)),
            "exact mask defect norm",
        )
        selected_index = physical_n.index(selected_n)
        moved_n = selected_n // (71 * 71)
        moved_index = physical_n.index(moved_n)
        require(
            mask[selected_index] and not mask[moved_index],
            "actual 71-square source move",
        )
        old_weight = Fraction(71 * 401) * Fraction(72, 70) * Fraction(402, 400)
        new_weight = Fraction(71 * 73) * Fraction(72, 70) * Fraction(74, 72)
        require(
            old_weight != new_weight,
            "reselected principal metric is not swap invariant",
        )
        result["actual_ratio_mask"] = {
            "orbit_size": size,
            "retained_count": retained,
            "constant_endpoint": str(a),
            "augment_after_mask": str(a * retained / size),
            "mask_commutator_counting_norm_square_times_K": str(defect),
            "K": K,
            "selected_N": selected_n,
            "selected_M": K // selected_n,
            "moved_N": moved_n,
            "moved_M": K // moved_n,
            "old_principal_weight": str(old_weight),
            "new_principal_weight": str(new_weight),
            "mask_commutes_with_augmentation_on_actual_source": False,
            "mask_after_augmentation_equals_global_even_masked_source": True,
        }
    return result


def activation_control(exponents):
    require(
        type(exponents) is tuple
        and 1 <= len(exponents) <= 4
        and all(type(a) is int and 1 <= a <= 16 for a in exponents),
        "power schedule caps",
    )
    r, total = len(exponents), sum(exponents)
    q = tuple(Fraction(a, total) for a in exponents)
    coefficients = tuple(
        2
        * Fraction(-1, 2) ** r
        * sum((q[j] for j, active in enumerate(subset) if active), Fraction())
        for subset in product((0, 1), repeat=r)
    )
    require(sum(coefficients) == (-1) ** r, "complete squarefree native endpoint")
    expected_norm = Fraction(1, 2**r) * (1 + sum(x * x for x in q))
    require(
        norm_square(coefficients) == expected_norm, "source simplex counting energy"
    )
    return {
        "schedule_powers": exponents,
        "activation_probabilities": [str(x) for x in q],
        "complete_coefficients": [str(x) for x in coefficients],
        "energy_times_K_over_Gamma0_in_separated_case": str(expected_norm),
        "primitive_measure_is_probability": False,
    }


def cutoff_defect(labels, cutoff):
    require(
        type(labels) is tuple and len(labels) <= 6 and len(set(labels)) == len(labels),
        "bounded distinct Boolean labels",
    )
    require(type(cutoff) is int and 1 <= cutoff <= 1024, "exact cutoff cap")
    require(all(type(p) is int and 2 <= p <= 101 for p in labels), "literal label cap")
    total = 0
    for subset in product((0, 1), repeat=len(labels)):
        value = prod(p for p, active in zip(labels, subset, strict=True) if active)
        if value <= cutoff:
            total += (-1) ** sum(subset)
    return int(not labels) - total


def boolean_half(labels, cutoff):
    result = Fraction()
    for subset in product((0, 1), repeat=len(labels)):
        selected = tuple(p for p, active in zip(labels, subset, strict=True) if active)
        result += cutoff_defect(selected, cutoff) * Fraction(-1, 2) ** (
            len(labels) - sum(subset)
        )
    return result


def boolean_control(labels):
    require(
        type(labels) is tuple and 1 <= len(labels) <= 4 and all(p > 64 for p in labels),
        "declared rough-core window",
    )
    r = len(labels)
    coefficients = []
    for subset in product((0, 1), repeat=r):
        left = tuple(p for p, active in zip(labels, subset, strict=True) if active)
        right = tuple(p for p, active in zip(labels, subset, strict=True) if not active)
        f, g = boolean_half(left, 64), boolean_half(right, 64)
        require(
            f == Fraction((-1) ** len(left) - 1, 2 ** len(left)),
            "literal odd half-source",
        )
        coefficients.append(f * g)
    coefficients = tuple(coefficients)
    exponents = (1,) * r
    mean = character_projection(coefficients, exponents)
    highest = character_projection(coefficients, exponents, tuple(range(r)))
    require(
        coefficients == tuple(a + b for a, b in zip(mean, highest, strict=True)),
        "canonical Boolean source has empty and full character only",
    )
    beta = Fraction(1, (r + 1) * (r + 2))
    canonical = 2 * beta * sum(coefficients)
    return {
        "core_labels": labels,
        "U": 64,
        "owner_labels": (2, 3),
        "complete_core_allocations": len(coefficients),
        "half_product_coefficients": [str(x) for x in coefficients],
        "nonzero_core_allocations_per_owner_order": sum(bool(x) for x in coefficients),
        "constant_character_each": str(mean[0]),
        "highest_character_nonzero": any(highest),
        "global_exchange_even": coefficients == tuple(reversed(coefficients)),
        "actual_Beta_integral": str(beta),
        "canonical_two_owner_coefficient": str(canonical),
        "nonzero_literal_term_after_Beta": sorted(
            {str(beta * x) for x in coefficients if x}
        ),
        "physical_product": 6 * prod(labels) ** 2,
        "actual_native_Beta_measure": "(1-theta)dtheta",
        "measure_is_2d_tau": False,
    }


def separated_control():
    primes = (3, 11, 101)
    divisors = sorted(
        prod(p for p, active in zip(primes, flags, strict=True) if active)
        for flags in product((0, 1), repeat=3)
    )
    require(
        all(b * b > 8 * a * a for a, b in pairwise(divisors)),
        "all actual frequency gaps exceed kernel support length",
    )
    return {
        "primes": primes,
        "K": prod(primes),
        "complete_divisors": divisors,
        "minimum_activation": ["1/3"] * 3,
        "minimum_energy_times_K_over_Gamma0": "1/6",
        "maximum_energy_times_K_over_Gamma0": "1/4",
        "unique_minimizing_path_claimed": False,
    }


def replay_equal(candidate, expected):
    require(canonical(candidate) == canonical(expected), "typed canonical replay")


def build():
    module = geodesic_module()
    for path, blob in BOOLEAN_SOURCES.items():
        frozen_bytes(BOOLEAN_COMMIT, path, blob)
    for key in module.SOURCES:
        module.source_bytes(key)
    native = json.loads(module.source_bytes((module.DENSE, module.DENSE_JSON)))
    bindings = {}
    for path in (NOTE, Path(__file__), TEST):
        data = path.read_bytes()
        require(len(data) <= MAX_BYTES, "owned byte cap")
        bindings[path.relative_to(ROOT).as_posix()] = sha256(
            data.replace(b"\r\n", b"\n")
        ).hexdigest()
    result = {
        "schema": "riemann.native_six_hour.first_chaos.v1",
        "geodesic_source": {"commit": GE_COMMIT, "path": GE_PATH, "blob": GE_BLOB},
        "Boolean_sources": [
            {"commit": BOOLEAN_COMMIT, "path": path, "blob": blob}
            for path, blob in BOOLEAN_SOURCES.items()
        ],
        "source_hashes": bindings,
        "zero_chart": vector_control(module, module.zero_spec(), True),
        "held_out_positive_chart": vector_control(module, module.held_out_spec(native)),
        "activation_controls": [
            activation_control(x) for x in ((1, 1, 1), (1, 2, 3), (2, 3, 5))
        ],
        "actual_Boolean_half_source_controls": [
            boolean_control(x) for x in ((71, 73, 79), (71, 73, 79, 83))
        ],
        "separated_native_variational_fixture": separated_control(),
        "full_post_renewal_decoder_identified": False,
        "RH_conclusion": False,
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.write:
        FIXTURE.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    else:
        require(FIXTURE.stat().st_size <= MAX_BYTES, "artifact byte cap")
        replay_equal(json.loads(FIXTURE.read_text(encoding="utf-8")), result)
    print(f"PASS native first-chaos augmentation {result['proof_object_sha256']}")


if __name__ == "__main__":
    main()
