#!/usr/bin/env python3
"""Native measures and all nested sites reconstruct a canonical Boolean tuple."""

from __future__ import annotations

import argparse
import json
import subprocess
from collections import Counter
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import product
from math import comb, prod
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NOTE = HERE / "CANONICAL_NATIVE_PREIMAGE.md"
FIXTURE = HERE / "canonical_native_preimage.json"
TEST = ROOT / "tests" / "test_native_six_hour_canonical_preimage.py"
GE_COMMIT = "15967a52e846f1037bb0446db43f3d4a9c3fc821"
GE_PATH = "research/riemann-structures/native-six-hour/geodesic_factor_exchange.py"
GE_BLOB = "c88f87c164ab1ea5504913c00f257f5b030ab854"
OLD = "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc"
FAMILY = "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b"
EXTRA = {
    (
        FAMILY,
        "claims/lemmas/L-106132-boolean-half-source-least-prime-calderon-row.md",
    ): "f393a1d8583c5680b98a4b3e26d9b5a61c8d2b7a",
    (
        FAMILY,
        "claims/lemmas/L-106133-canonical-equal-pair-boolean-source-is-a-beta-half-source-square.md",
    ): "b988b14eb982504a799158eed4c76e7f033c96f0",
    (
        OLD,
        "claims/lemmas/L-102904-endpoint-color-walsh-expansion-has-only-squared-activity-off-the-midpoint.md",
    ): "f0bdbf09e620027eafe9a198350f588edafdd269",
}
MAX_BYTES = 1048576


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def frozen_bytes(commit, path, blob):
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
        ["git", "show", ref],
        cwd=ROOT,
        capture_output=True,
        check=True,
    ).stdout
    require(
        len(raw) == size
        and sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest() == blob,
        "exact frozen Git blob",
    )
    return raw


def geodesic_module():
    raw = frozen_bytes(GE_COMMIT, GE_PATH, GE_BLOB)
    namespace = {
        "__name__": "authenticated_preimage_geodesic",
        "__file__": str(ROOT / GE_PATH),
    }
    # Execute only exact frozen Git bytes after commit/blob authentication.
    exec(compile(raw, str(ROOT / GE_PATH), "exec"), namespace)  # noqa: S102
    return SimpleNamespace(**namespace)


def subsets(labels):
    require(type(labels) is tuple and len(labels) <= 7, "bounded label tuple")
    for bits in product((0, 1), repeat=len(labels)):
        yield tuple(p for p, bit in zip(labels, bits, strict=True) if bit)


def a_u(labels, cutoff):
    require(type(cutoff) is int and 1 <= cutoff <= 2**24, "exact cutoff cap")
    require(
        type(labels) is tuple and len(labels) <= 5 and len(set(labels)) == len(labels),
        "distinct bounded core",
    )
    require(all(type(p) is int and 2 <= p <= 2000000 for p in labels), "label cap")
    return int(not labels) - sum(
        (-1) ** len(part) for part in subsets(labels) if prod(part) <= cutoff
    )


def half_source(labels, cutoff):
    return sum(
        (
            a_u(part, cutoff) * Fraction(-1, 2) ** (len(labels) - len(part))
            for part in subsets(labels)
        ),
        Fraction(),
    )


def half_square(labels, cutoff):
    return sum(
        (
            half_source(part, cutoff)
            * half_source(tuple(p for p in labels if p not in part), cutoff)
            for part in subsets(labels)
        ),
        Fraction(),
    )


def raw_cone(module, labels):
    require(
        type(labels) is tuple
        and 2 <= len(labels) <= 5
        and len(set(labels)) == len(labels),
        "owner-containing raw support",
    )
    for p in labels:
        module.prime(p)
    records, total, primitive_diagonal = [], Fraction(), Fraction()
    for left in subsets(labels):
        right = tuple(p for p in labels if p not in left)
        left_factors = [module.local(1) for _ in left]
        right_poly = module.polynomial_product(module.local(1) for _ in right)
        site_sum = ()
        for index, site in enumerate(left):
            polynomial = module.polynomial_product(
                [module.derivative(left_factors[index]), right_poly]
                + left_factors[:index]
                + left_factors[index + 1 :]
            )
            site_sum = module.add(site_sum, polynomial)
            integrated = 2 * module.integral(polynomial)
            square_integral = 2 * module.integral(
                module.multiply(polynomial, polynomial)
            )
            require(
                integrated == 2 * Fraction(-1, 2) ** len(labels) / len(labels),
                "independent squarefree site formula",
            )
            records.append(
                {
                    "left": left,
                    "right": right,
                    "site": site,
                    "raw_n": prod(left),
                    "raw_m": prod(right),
                    "integrand": [str(x) for x in polynomial],
                    "integrated_2ds": str(integrated),
                    "square_integral_2ds": str(square_integral),
                }
            )
            total += integrated
            primitive_diagonal += square_integral
        require(
            site_sum
            == module.multiply(
                module.derivative(module.polynomial_product(left_factors)),
                right_poly,
            ),
            "complete derivative chain rule",
        )
    require(total == (-1) ** len(labels), "actual endpoint coefficient")
    colours = []
    for left in subsets(labels):
        colours.append(
            {
                "E_on_left": left,
                "E_on_right": tuple(p for p in labels if p not in left),
                "probability": str(Fraction(1, 2 ** len(labels))),
                "coefficient": (-1) ** len(labels),
            }
        )
    return {
        "labels": labels,
        "K": prod(labels),
        "complete_factor_count": 2 ** len(labels),
        "root_free_left_retained": True,
        "sites": records,
        "coefficient": str(total),
        "primitive_site_diagonal": str(primitive_diagonal),
        "endpoint_colours": colours,
        "colour_probability_diagonal": "1",
        "colour_weighted_counting_diagonal": str(Fraction(1, 2 ** len(labels))),
    }


def side(module, owners, core, cutoff):
    require(
        type(owners) is tuple
        and len(owners) == 2
        and type(core) is tuple
        and 1 <= len(core) <= 3,
        "bounded owner/core lists",
    )
    labels = owners + core
    require(len(set(labels)) == len(labels), "clean distinct prime labels")
    for p in labels:
        module.prime(p)
    depth = len(core) + 2
    beta = Fraction(1, depth * (depth - 1))
    beta_square = Fraction(1, (2 * len(core) + 1) * (2 * len(core) + 2))
    N = prod(owners) * prod(core) ** 2
    histories, cones, branches = [], {}, []
    zero_histories = 0
    for allocation in product(range(3), repeat=len(core)):
        pieces = [
            tuple(p for p, slot in zip(core, allocation, strict=True) if slot == j)
            for j in range(3)
        ]
        A, B, D = pieces
        multiplier = a_u(A, cutoff) * a_u(B, cutoff)
        if not multiplier:
            zero_histories += 1
            continue
        key = ",".join(map(str, owners + D))
        if key not in cones:
            cones[key] = raw_cone(module, owners + D)
        cone = cones[key]
        history_coefficient = (
            multiplier * Fraction(cone["coefficient"]) / comb(depth, 2)
        )
        history_index = len(histories)
        histories.append(
            {
                "A": A,
                "B": B,
                "D": D,
                "a_U_A": a_u(A, cutoff),
                "a_U_B": a_u(B, cutoff),
                "raw_cone": key,
                "raw_product": cone["K"],
                "completion_multiplier_square": str(Fraction(cone["K"], N)),
                "coefficient": str(history_coefficient),
            }
        )
        for order in (owners, owners[::-1]):
            for site_index, site_record in enumerate(cone["sites"]):
                branches.append(
                    {
                        "history": history_index,
                        "owner_order": order,
                        "raw_site": site_index,
                        "integrated_coefficient": str(
                            multiplier * beta * Fraction(site_record["integrated_2ds"])
                        ),
                        "continuous_square_integral": str(
                            multiplier**2
                            * beta_square
                            * Fraction(site_record["square_integral_2ds"])
                        ),
                    }
                )
    coefficient = sum((Fraction(row["coefficient"]) for row in histories), Fraction())
    require(
        coefficient == half_square(core, cutoff) / comb(depth, 2),
        "independent Boolean half-square",
    )
    require(
        coefficient
        == sum(
            (Fraction(row["integrated_coefficient"]) for row in branches), Fraction()
        ),
        "nested actual measures reconstruct histories",
    )
    return {
        "owners": owners,
        "core": core,
        "cutoff": cutoff,
        "N": N,
        "complete_Boolean_partition_count": 3 ** len(core),
        "zero_history_count": zero_histories,
        "histories": histories,
        "raw_cones": cones,
        "nested_sites": branches,
        "beta_per_owner_order": str(beta),
        "coefficient": str(coefficient),
        "diagonals_before_1_over_N": {
            "continuous": str(
                sum(
                    (Fraction(row["continuous_square_integral"]) for row in branches),
                    Fraction(),
                )
            ),
            "integrated_site": str(
                sum(
                    (Fraction(row["integrated_coefficient"]) ** 2 for row in branches),
                    Fraction(),
                )
            ),
            "history": str(
                sum(
                    (Fraction(row["coefficient"]) ** 2 for row in histories), Fraction()
                )
            ),
            "recombined": str(coefficient**2),
        },
    }


def bilateral(left, right):
    counts, digest = Counter(), sha256()
    total = Fraction()
    for i, a in enumerate(left["nested_sites"]):
        for j, b in enumerate(right["nested_sites"]):
            coefficient = Fraction(a["integrated_coefficient"]) * Fraction(
                b["integrated_coefficient"]
            )
            counts[str(coefficient)] += 1
            total += coefficient
            digest.update((canonical([i, j, str(coefficient)]) + "\n").encode())
    require(
        total == Fraction(left["coefficient"]) * Fraction(right["coefficient"]),
        "full nested bilateral sum",
    )
    return {
        "left": left,
        "right": right,
        "N": left["N"],
        "M": right["N"],
        "history_count": len(left["histories"]) * len(right["histories"]),
        "nested_site_count": sum(counts.values()),
        "nested_coefficient_histogram": dict(sorted(counts.items())),
        "complete_nested_stream_sha256": digest.hexdigest(),
        "coefficient_before_1_over_sqrt_NM": str(total),
        "diagonals_before_1_over_NM": {
            name: str(
                Fraction(value) * Fraction(right["diagonals_before_1_over_N"][name])
            )
            for name, value in left["diagonals_before_1_over_N"].items()
        },
        "common_completed_Mellin_phase": True,
    }


def replay_equal(candidate, expected):
    require(
        canonical(candidate) == canonical(expected),
        "typed canonical fixture comparison",
    )


def build():
    module = geodesic_module()
    inherited = {key: module.source_bytes(key) for key in module.SOURCES}
    for (commit, path), blob in EXTRA.items():
        frozen_bytes(commit, path, blob)
    zero = bilateral(
        side(module, (2, 3), (71, 73, 79), 64), side(module, (5, 7), (401, 421), 64)
    )
    require(
        (zero["N"], zero["M"], zero["history_count"], zero["nested_site_count"])
        == (1005930209094, 997518551435, 24, 3072),
        "original zero chart complete counts",
    )
    native = json.loads(inherited[(module.DENSE, module.DENSE_JSON)])
    labels, _, N = module.held_out_spec(native)
    positive = bilateral(
        side(module, labels[:2], (labels[4], labels[5]), 2**20),
        side(module, labels[2:4], (labels[4], labels[6]), 2**20),
    )
    require(
        positive["N"] == N and positive["coefficient_before_1_over_sqrt_NM"] == "1/9",
        "same-map held-out positive source",
    )
    require(
        zero["diagonals_before_1_over_NM"]
        == {
            "continuous": "29/25200",
            "integrated_site": "1/14400",
            "history": "1/150",
            "recombined": "0",
        },
        "zero chart exact resolutions",
    )
    require(
        positive["diagonals_before_1_over_NM"]
        == {
            "continuous": "1/2025",
            "integrated_site": "1/20736",
            "history": "1/324",
            "recombined": "1/81",
        },
        "positive chart exact resolutions",
    )
    bindings = {}
    for path in (NOTE, Path(__file__), TEST):
        data = path.read_bytes()
        require(len(data) <= MAX_BYTES, "owned byte cap")
        bindings[path.relative_to(ROOT).as_posix()] = sha256(
            data.replace(b"\r\n", b"\n")
        ).hexdigest()
    result = {
        "schema": "riemann.native_six_hour.canonical_preimage.v1",
        "source_hashes": bindings,
        "sources": [{"commit": GE_COMMIT, "path": GE_PATH, "blob": GE_BLOB}]
        + [
            {"commit": key[0], "path": key[1], "blob": value}
            for key, value in (module.SOURCES | EXTRA).items()
        ],
        "zero_chart": zero,
        "held_out_positive_chart": positive,
        "primitive_measure": "2 ds",
        "depth_measure": "(1-theta) dtheta; theta^core_depth remains in the integrand",
        "colour_measure": "independent fair endpoint choices; probability measure",
        "product_collapse_before_owner_extraction": True,
        "primitive_ratio_readout_preserved": False,
        "complete_post_renewal_gamma_identified": False,
        "native_principal_moment_bound_claimed": False,
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
        require(FIXTURE.stat().st_size <= MAX_BYTES, "fixture byte cap")
        replay_equal(json.loads(FIXTURE.read_text(encoding="utf-8")), result)
    print(f"PASS canonical native preimage {result['proof_object_sha256']}")


if __name__ == "__main__":
    main()
