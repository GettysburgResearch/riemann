#!/usr/bin/env python3
"""Replay canonical saturation of the already-known opposite-owner count."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from hashlib import sha1, sha256
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NOTE = HERE / "CANONICAL_ANCHOR_DIAGONAL_SATURATION.md"
FIXTURE = HERE / "canonical_anchor_diagonal_saturation.json"
TEST = ROOT / "tests" / "test_canonical_anchor_diagonal_saturation.py"
FAMILY = "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b"
DENSE = "1fea3c9ce079325d19f5b43c6daa59c76afff921"
DENSE_JSON = "research/riemann-structures/dense_owner_principal_coefficient_family.json"
SOURCES = {
    (
        FAMILY,
        "claims/lemmas/L-106092-fixed-fibre-least-discrepancy-phase-energy-is-automatically-long-core.md",
    ): "8dd3a5e54fefe04cc48f1b90e54b5a8266e57476",
    (
        FAMILY,
        "claims/lemmas/L-106093-mellin-polarization-places-the-anchor-inside-one-amplified-family-moment.md",
    ): "cb8665b8cdbe2bc7e6eb223d6bc009e8e4f5a5df",
    (
        FAMILY,
        "claims/lemmas/L-106094-diagonal-anchor-part-of-the-rough-tail-hybrid-moment-is-subpower.md",
    ): "9fea4d5f23feae12d2ac00bbc84b56d6065806fc",
    (
        FAMILY,
        "claims/refutations/R-106095-opposite-owner-dimension-must-be-amplified-before-the-family-square.md",
    ): "8d01e79483827f867c91bdafb56569baae5c99c2",
    (
        FAMILY,
        "claims/refutations/R-106110-q-fixed-source-dual-weight-does-not-pay-opposite-owner-fibres.md",
    ): "019d7e501be0ce6ec8914e5ca505fd61c3923e1f",
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


def integer(value):
    require(
        type(value) is int and 0 < value and value.bit_length() <= 128,
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


def reciprocal_tail_bounds(values):
    require(type(values) is list and 1 <= len(values) <= 32, "bounded tail count")
    values = [integer(value) for value in values]
    require(len(set(values)) == len(values), "distinct tail indices")
    require(10 * max(values) < 11 * min(values), "narrow tail frequency range")
    reciprocal = sum((Fraction(1, value) for value in values), Fraction())
    squared = sum((Fraction(1, value * value) for value in values), Fraction())
    return {
        "indices": values,
        "coherent_lower": str(reciprocal**2),
        "coherent_upper": str(384 * reciprocal**2),
        "atomic_over_Gamma0": str(squared),
        "coherent_lower_over_atomic_without_Gamma0": str(reciprocal**2 / squared),
        "new_native_prime_source_claimed": False,
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
    require(u >= 256 and u & (u - 1) == 0 and horizon == u**6, "dyadic horizon")
    require(u < g < ell < rho and 4 * g < u * u, "live ordered rough core")
    require(gcd(g, ell * rho) == gcd(ell, rho) == 1, "clean common core")
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
                type(row["coefficient"]) is int and row["coefficient"] == 1
                for row in histories
            ),
            "two positive source histories",
        )
    entries = record["entries"]
    require(type(entries) is list and len(entries) == 16, "sixteen source pairs")
    principal_factor = Fraction(ell + 1, ell - 1)
    per_q = {}
    pairs = set()
    details = []
    for item in entries:
        p, q, n, m = (integer(item[key]) for key in ("P", "Q", "N", "M"))
        require((p, q) not in pairs, "distinct arithmetic pair")
        pairs.add((p, q))
        require(
            n == p * (g * ell) ** 2 and m == q * (g * rho) ** 2,
            "actual physical indices",
        )
        require(
            horizon < n < Fraction(11, 10) * horizon
            and horizon < m < Fraction(11, 10) * horizon,
            "common physical shell",
        )
        require(p <= g * ell and q <= g * rho, "full-core owner bounds")
        require(
            gcd(p, q * g * ell * rho) == gcd(q, p * g * ell * rho) == 1,
            "clean cross-owner incidence",
        )
        require(item["positive_branch"] is True, "positive native branch")
        require(
            Fraction(item["coefficient_square"]) == Fraction(1, 81 * n * m)
            and Fraction(item["one_literal_square"]) == Fraction(1, 1296 * n * m),
            "canonical and literal coefficient squares",
        )
        sigma_raw = pow(q, (ell - 1) // 2, ell)
        tau_raw = pow(p, (rho - 1) // 2, rho)
        require(
            sigma_raw in (1, ell - 1) and tau_raw in (1, rho - 1),
            "actual unit quadratic classes",
        )
        sigma, tau = (1 if sigma_raw == 1 else -1), (1 if tau_raw == 1 else -1)
        require(canonical(item["class"]) == canonical([sigma, tau]), "frozen class")
        weight = g * g * ell * q * principal_factor
        direct = weight * Fraction(1, 9 * n) * Fraction(1, 9 * m)
        factor = principal_factor * Fraction(1, 81 * g * g * ell * p * rho * rho)
        require(
            direct == factor, "physical Q cancellation with principal normalization"
        )
        per_q[q] = per_q.get(q, Fraction()) + direct
        details.append(
            {
                "P": p,
                "Q": q,
                "class_sigma": sigma,
                "N": n,
                "M": m,
                "left_coefficient_square": str(Fraction(1, 9 * n)),
                "right_coefficient_square": str(Fraction(1, 9 * m)),
                "principal_weight": str(weight),
                "H_entry_over_Gamma0": str(direct),
            }
        )
    left, right = {p for p, _ in pairs}, {q for _, q in pairs}
    require(
        len(left) == len(right) == 4 and pairs == {(p, q) for p in left for q in right},
        "complete four-by-four owner rectangle",
    )
    direct_total = sum(per_q.values(), Fraction())
    factor_total = (
        len(right)
        * principal_factor
        * Fraction(1, 81 * g * g * ell * rho * rho)
        * sum((Fraction(1, p) for p in left), Fraction())
    )
    require(direct_total == factor_total, "complete direct/factored principal equality")
    require(len(set(per_q.values())) == 1, "every opposite owner has equal weight")
    fixed_q = per_q[min(right)]
    require(direct_total == 4 * fixed_q, "unpaid opposite-owner count equals four")
    return {
        "U": u,
        "Y": horizon,
        "g": g,
        "ell": ell,
        "rho": rho,
        "arithmetic_pairs": len(pairs),
        "literal_histories": 64,
        "opposite_owner_count": len(right),
        "principal_c_ell": str(principal_factor),
        "all_pair_checks": details,
        "per_Q_H_over_Gamma0": [
            {"Q": q, "value": str(value)} for q, value in sorted(per_q.items())
        ],
        "H_direct_over_Gamma0": str(direct_total),
        "H_factorized_over_Gamma0": str(factor_total),
        "H_all_Q_over_one_Q": str(direct_total / fixed_q),
        "literal_left_anchor_over_Gamma0": str(direct_total / 2),
        "literal_both_atom_over_Gamma0": str(direct_total / 4),
        "tail_prime_count_in_fixture": 1,
        "cofinal_tail_coherence_inferred_from_fixture": False,
        "new_prime_search": False,
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
        "schema": "riemann.canonical_anchor_diagonal_saturation.v1",
        "sources": [
            {"commit": key[0], "path": key[1], "git_blob": value}
            for key, value in SOURCES.items()
        ],
        "source_hashes": hashes,
        "native_dense_control": control,
        "reciprocal_tail_controls": [
            reciprocal_tail_bounds(values) for values in ([101], [101, 103, 107, 109])
        ],
        "prior_retractions": ["R-106095", "R-106110"],
        "new_historical_error_claimed": False,
        "restricted_principal_anchor_diagonal_order": "Theta(U/log(U)^8)",
        "restricted_arithmetic_atomic_diagonal_order": "Theta(log(U)^-7)",
        "full_native_gamma_identification_claimed": False,
        "unrestricted_tail_lower_bound_claimed": False,
        "corrected_dual_amplified_moment_refuted": False,
        "RH_conclusion": False,
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    return result


def replay_equal(candidate, expected):
    require(
        canonical(candidate) == canonical(expected), "strict typed canonical replay"
    )


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
        replay_equal(json.loads(FIXTURE.read_text(encoding="utf-8")), result)
    print(f"PASS canonical anchor diagonal {result['proof_object_sha256']}")


if __name__ == "__main__":
    main()
