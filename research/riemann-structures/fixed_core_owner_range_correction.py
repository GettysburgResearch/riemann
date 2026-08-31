#!/usr/bin/env python3
"""Correct the common-core factor in the fixed-core owner range bound."""

from __future__ import annotations

import argparse
import json
import subprocess
from collections import Counter
from fractions import Fraction
from hashlib import sha1, sha256
from math import gcd, isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NOTE = HERE / "FIXED_CORE_OWNER_RANGE_CORRECTION.md"
FIXTURE = HERE / "fixed_core_owner_range_correction.json"
TEST = ROOT / "tests" / "test_fixed_core_owner_range_correction.py"
OLD = "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc"
FAMILY = "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b"
DENSE = "1fea3c9ce079325d19f5b43c6daa59c76afff921"
DENSE_JSON = "research/riemann-structures/dense_owner_principal_coefficient_family.json"
SOURCES = {
    (
        OLD,
        "claims/lemmas/L-102958-ratioeight-comparability-pays-both-opposite-owner-products.md",
    ): "3b72653ea5f05405c587be165faf7ab2c52c3f2b",
    (
        FAMILY,
        "claims/lemmas/L-106124-fixed-core-bilateral-owner-phase-energy.md",
    ): "8a2ad27963cf61660bb151c20eae2910b1eb4255",
    (
        FAMILY,
        "claims/lemmas/L-106120-bilateral-least-prime-phases-form-a-tensor-kummer-family.md",
    ): "a8d829dc10611adb7bfb4853902bdff0ab02a065",
    (
        FAMILY,
        "claims/theorems/T-106140-wick-centered-additive-kummer-conjunction-frontier.md",
    ): "d5be8e376c88b63de0be19e0d9e8791624e99ae2",
    (
        DENSE,
        "research/riemann-structures/DENSE_OWNER_PRINCIPAL_COEFFICIENT_FAMILY.md",
    ): "c1eeffbc6aa814f860875d58205e97a4d945dc2c",
    (DENSE, DENSE_JSON): "1c289fb3c7d8e959b010267751834ebad6914ec5",
}
MAX_BYTES = 262144


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def integer(value, bits=128):
    require(
        type(value) is int and 0 < value and value.bit_length() <= bits,
        "bounded positive exact integer",
    )
    return value


def source_bytes(key):
    require(key in SOURCES, "frozen source identity")
    ref = f"{key[0]}:{key[1]}"
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
    require(len(raw) == size, "source byte count")
    digest = sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest()
    require(digest == SOURCES[key], "frozen source Git blob")
    return raw


def phase_prime(value):
    integer(value)
    require(3 <= value <= 2000000 and value % 2 == 1, "bounded odd phase prime")
    require(all(value % d for d in range(2, isqrt(value) + 1)), "exact phase primality")
    return value


def gauss_factor(ell, rho):
    ell, rho = phase_prime(ell), phase_prime(rho)
    require(ell != rho, "distinct phases")
    factor = Fraction(ell * rho, (ell + 1) * (rho + 1))
    require(Fraction(9, 16) <= factor < 1, "retained Gauss comparison factor")
    return factor


def interval_bounds(g, c, d, ell, rho):
    g, c, d = (integer(x) for x in (g, c, d))
    ell, rho = phase_prime(ell), phase_prime(rho)
    require(
        ell != rho and c % ell == d % rho == 0,
        "declared reduced-core phase divisibility",
    )
    require(gcd(c, d) == gcd(g, c * d) == 1, "clean common and reduced cores")
    p_max, q_max = 2 * g * d, 2 * g * c
    exact = ell * rho * ((q_max + ell - 1) // ell) * ((p_max + rho - 1) // rho)
    continuous = (ell + q_max) * (rho + p_max)
    majorant = 9 * g * g * c * d
    require(exact <= continuous <= majorant, "corrected residue-cell bounds")
    return {
        "P_max": p_max,
        "Q_max": q_max,
        "complete_phase_frame_bound": exact,
        "continuous_frame_bound": continuous,
        "nine_g2_cd_bound": majorant,
        "source_weight_after_cancellation": str(Fraction(ell * rho, c * d)),
        "extra_uniform_g_inverse_square": False,
    }


def residue_counts(bound, modulus):
    integer(bound)
    integer(modulus)
    require(bound <= 10000 and 2 <= modulus <= 101, "small residue control cap")
    counts = [0] * modulus
    for n in range(1, bound + 1):
        counts[n % modulus] += 1
    require(max(counts) == (bound + modulus - 1) // modulus, "exact cell capacity")
    return counts


def small_capacity_control(g=3):
    integer(g)
    require(g <= 100 and gcd(g, 35) == 1, "small clean common core")
    bounds = interval_bounds(g, 5, 7, 5, 7)
    q_cells = residue_counts(bounds["Q_max"], 5)
    p_cells = residue_counts(bounds["P_max"], 7)
    actual = 35 * max(q_cells) * max(p_cells)
    old = 35 * max(residue_counts(10, 5)) * max(residue_counts(14, 7))
    require(actual == bounds["complete_phase_frame_bound"], "two-route capacity")
    require(Fraction(actual, old) == g * g, "exact omitted common-core square")
    return {
        "g": g,
        "Q_residue_counts": q_cells,
        "P_residue_counts": p_cells,
        "correct_frame_capacity": actual,
        "reduced_range_capacity": old,
        "capacity_ratio": str(Fraction(actual, old)),
        "integer_rectangle_not_claimed_native_prime_source": True,
    }


def dense_control(native):
    require(
        type(native) is dict
        and native.get("schema")
        == "riemann.dense_owner_principal_coefficient_family.v1",
        "exact frozen dense schema",
    )
    require(
        native.get("full_gamma_source_identified_with_projection") is False,
        "preserved native-source boundary",
    )
    record = native["record"]
    require(type(record) is dict, "dense record")
    u, horizon, g, ell, rho = (
        integer(record[key]) for key in ("U", "Y", "g", "ell", "rho")
    )
    require(
        u >= 256 and u & (u - 1) == 0 and horizon == u**6, "dyadic physical horizon"
    )
    require(g < Fraction(u * u, 4), "live common-core range")
    bounds = interval_bounds(g, ell, rho, ell, rho)
    entries = record["entries"]
    require(
        type(entries) is list and len(entries) == 16, "complete frozen dense pair count"
    )
    require(
        type(record["literal_histories"]) is int and record["literal_histories"] == 64,
        "four literal histories per arithmetic pair",
    )
    for side in ("left_boolean", "right_boolean"):
        rows = record[side]
        require(
            type(rows["balanced"]) is int and rows["balanced"] == 2,
            "actual Boolean coefficient",
        )
        histories = rows["nonzero_balanced_histories"]
        require(
            len(histories) == 2
            and all(
                type(h["coefficient"]) is int and h["coefficient"] == 1
                for h in histories
            ),
            "two inherited positive source histories",
        )
    pairs = set()
    class_counts = Counter()
    witnesses = []
    for item in entries:
        p, q, n, m = (integer(item[key]) for key in ("P", "Q", "N", "M"))
        require((p, q) not in pairs, "distinct arithmetic pair")
        pairs.add((p, q))
        require(
            n == p * (g * ell) ** 2 and m == q * (g * rho) ** 2,
            "actual full-core physical indices",
        )
        require(
            horizon < n < Fraction(11, 10) * horizon
            and horizon < m < Fraction(11, 10) * horizon,
            "common native shell",
        )
        require(
            p <= g * ell
            and q <= g * rho
            and p <= bounds["P_max"]
            and q <= bounds["Q_max"],
            "true parent full-core inequalities",
        )
        require(
            gcd(p, q * g * ell * rho) == gcd(q, p * g * ell * rho) == 1,
            "clean cross-owner source incidence",
        )
        ratio_p, ratio_q = Fraction(p, rho), Fraction(q, ell)
        require(
            ratio_p > Fraction(9, 10) * g and ratio_q > Fraction(9, 10) * g,
            "source owner ranges grow with the common core",
        )
        require(item["positive_branch"] is True, "native positive coefficient branch")
        require(
            Fraction(item["coefficient_square"]) == Fraction(1, 81 * n * m)
            and Fraction(item["one_literal_square"]) == Fraction(1, 1296 * n * m),
            "canonical and four-history coefficient squares",
        )
        sigma_raw = pow(q, (ell - 1) // 2, ell)
        tau_raw = pow(p, (rho - 1) // 2, rho)
        require(
            sigma_raw in (1, ell - 1) and tau_raw in (1, rho - 1),
            "nonzero actual quadratic classes",
        )
        sigma, tau = (1 if sigma_raw == 1 else -1), (1 if tau_raw == 1 else -1)
        require(
            canonical(item["class"]) == canonical([sigma, tau]), "frozen actual class"
        )
        class_counts[(sigma, tau)] += 1
        witnesses.append(
            {
                "P": p,
                "Q": q,
                "P_over_reduced_d": str(ratio_p),
                "Q_over_reduced_c": str(ratio_q),
                "P_over_full_b": str(Fraction(p, g * rho)),
                "Q_over_full_a": str(Fraction(q, g * ell)),
            }
        )
    left, right = {p for p, _ in pairs}, {q for _, q in pairs}
    require(
        len(left) == len(right) == 4 and pairs == {(p, q) for p in left for q in right},
        "all sixteen cross products retained",
    )
    chosen, count = max(sorted(class_counts.items()), key=lambda x: x[1])
    require(4 * count >= len(pairs), "actual class pigeonhole")
    weight = g * g * ell * rho * Fraction(ell + 1, ell - 1) * Fraction(rho + 1, rho - 1)
    principal_lower = weight * Fraction(10, 99 * horizon) ** 2 * count**2
    factor = gauss_factor(ell, rho)
    return {
        "U": u,
        "Y": horizon,
        "g": g,
        "c": ell,
        "d": rho,
        "range_bounds": bounds,
        "all_pair_range_witnesses": witnesses,
        "arithmetic_pairs": len(pairs),
        "literal_histories": 64,
        "class_counts": [
            {"class": list(key), "pairs": value}
            for key, value in sorted(class_counts.items())
        ],
        "selected_actual_class": list(chosen),
        "selected_class_pairs": count,
        "principal_class_energy_lower": str(principal_lower),
        "gauss_factor_relative_to_principal": str(factor),
        "weighted_nonzero_additive_class_lower": str(factor * principal_lower),
        "source_gamma_modulus": "1/9",
        "phase_family_enumerated": False,
        "new_prime_search": False,
        "asymptotic_contradiction_inferred_from_finite_fixture": False,
    }


def build():
    raw = {key: source_bytes(key) for key in SOURCES}
    native = json.loads(raw[(DENSE, DENSE_JSON)])
    control = dense_control(native)
    hashes = {}
    for path in (NOTE, Path(__file__), TEST):
        data = path.read_bytes()
        require(len(data) <= MAX_BYTES, "owned file cap")
        hashes[path.relative_to(ROOT).as_posix()] = sha256(
            data.replace(b"\r\n", b"\n")
        ).hexdigest()
    result = {
        "schema": "riemann.fixed_core_owner_range_correction.v1",
        "sources": [
            {"commit": key[0], "path": key[1], "git_blob": value}
            for key, value in SOURCES.items()
        ],
        "source_hashes": hashes,
        "native_dense_control": control,
        "small_residue_capacity_controls": [
            small_capacity_control(g) for g in (1, 2, 3, 11)
        ],
        "corrected_ranges": "P<=2gd,Q<=2gc",
        "corrected_weighted_bound": "Y^o(1)*ell*rho/(c*d)",
        "old_uniform_extra_g_inverse_square_valid_on_full_range": False,
        "abstract_short_interval_lemma_refuted": False,
        "cofinal_canonical_class_energy_lower": "Omega(log(U)^-8)",
        "full_native_gamma_identification_claimed": False,
        "full_native_moment_refuted": False,
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
        require(FIXTURE.stat().st_size <= MAX_BYTES, "artifact cap")
        require(
            canonical(json.loads(FIXTURE.read_text(encoding="utf-8")))
            == canonical(result),
            "strict typed canonical replay",
        )
    print(
        json.dumps(
            {"status": "PASS", "proof_object_sha256": result["proof_object_sha256"]}
        )
    )


if __name__ == "__main__":
    main()
