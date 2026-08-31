#!/usr/bin/env python3
"""Exact native restricted principal energy/diagonal bounds; no quadrature."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NOTE = HERE / "POST_QUOTIENT_PRINCIPAL_READOUT_BARRIER.md"
FIXTURE = HERE / "post_quotient_principal_readout_barrier.json"
TEST = ROOT / "tests" / "test_post_quotient_principal_readout_barrier.py"
NMO = "6dbab098bb057d76748d12e37900efeff571f8a9"
SCB = "1623f1924c62035918a94bcacf2ccad7d3bb6cf7"
FAMILY = "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b"
NMO_PATH = "research/riemann-structures/native_restricted_mellin_observability.json"
SCB_PATH = "research/riemann-structures/subcritical_observed_boolean_block.json"
SOURCES = {
    ("e365528d750fded282bd3f7261898d8455c41e0a", "research/riemann-structures/SOURCE_FIRST_BOOLEAN_PRINCIPAL_ADAPTER.md"):
        "c37145331aedf3c6a4ec0c70577a66da712a5edd",
    (NMO, "research/riemann-structures/LIVE_FIXED_CONDUCTOR_MULTIPLICITY.md"):
        "c9c5f9e7e1ddab7e9a6aff629165a098fdf597a8",
    (NMO, "research/riemann-structures/FIXED_CONDUCTOR_POWER_RANK_BARRIER.md"):
        "3348165d3f9224b7a7348d6557d358bf3ef439f2",
    (NMO, "research/riemann-structures/NATIVE_RESTRICTED_MELLIN_OBSERVABILITY.md"):
        "88989aaa947885df02272c0bb01a31f6d1ac0694",
    (NMO, NMO_PATH): "f6aaa4a5805c9d95c58cfc3c468ea7cbbd390db8",
    (SCB, "research/riemann-structures/SUBCRITICAL_OBSERVED_BOOLEAN_BLOCK.md"):
        "6aa04020b9f4afd538928688be9ed68c01e293ae",
    (SCB, SCB_PATH): "b6464ebbd4560e50d9ad7033d051dc9cddd4a7f4",
    (FAMILY, "claims/lemmas/L-106120-bilateral-least-prime-phases-form-a-tensor-kummer-family.md"):
        "a8d829dc10611adb7bfb4853902bdff0ab02a065",
    (FAMILY, "claims/theorems/T-106140-wick-centered-additive-kummer-conjunction-frontier.md"):
        "d5be8e376c88b63de0be19e0d9e8791624e99ae2",
}
MAX_BYTES = 262144
LOWER = Fraction(25, 2904)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def canonical(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def source_bytes(key):
    require(key in SOURCES, "frozen source identity")
    ref = f"{key[0]}:{key[1]}"
    size = int(subprocess.run(["git", "cat-file", "-s", ref], cwd=ROOT,
                             capture_output=True, text=True, check=True).stdout)
    require(0 < size <= MAX_BYTES, "source byte cap")
    raw = subprocess.run(["git", "show", ref], cwd=ROOT,
                         capture_output=True, check=True).stdout
    require(len(raw) == size, "source byte count")
    digest = sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest()
    require(digest == SOURCES[key], "frozen source Git blob")
    return raw


def kernel_bounds(kernel):
    expected = {
        "gram_upper": 384,
        "norm_constant": ["-288", "0"],
        "norm_log2_coefficient": ["384", "128"],
        "supremum": ["0", "8"],
        "total_variation": ["0", "32"],
        "translation_penalty": "512",
    }
    for key, value in expected.items():
        require(canonical(kernel[key]) == canonical(value), "native kernel primitive")
    root_lower, log_lower = Fraction(707, 500), Fraction(693, 1000)
    atanh_lower = 2 * sum((Fraction(1, (2 * j + 1) * 3 ** (2 * j + 1))
                          for j in range(3)), Fraction(0))
    require(root_lower**2 < 2 and atanh_lower == Fraction(842, 1215)
            and atanh_lower > log_lower, "strict elementary root/log bounds")
    gamma_lower = (384 + 128 * root_lower) * log_lower - 288
    difference_lower = gamma_lower - Fraction(512, 5)
    require(difference_lower > 1, "native pair-difference Gram positivity")
    require(Fraction(4, 384) * Fraction(10, 11)**2 == LOWER,
            "literal-history amplification constant")
    return {"sqrt2_strict_lower": str(root_lower),
            "log2_three_term_strict_lower": str(atanh_lower),
            "log2_weaker_strict_lower": str(log_lower),
            "Gamma0_strict_lower": str(gamma_lower),
            "frequency_difference_strict_radius": "1/5",
            "Gamma_difference_strict_lower": str(difference_lower),
            "Gamma0_upper": 384,
            "energy_over_literal_diagonal_lower_per_pair": str(LOWER),
            "energy_over_literal_diagonal_upper_per_pair": 4}


def panel_bounds(panel):
    require(type(panel) is dict, "native panel mapping")
    horizon, core = panel["horizon"], panel["common_core"]
    require(type(horizon) is int and type(core) is int
            and 1 < horizon and 1 < core and horizon.bit_length() <= 256 and core.bit_length() <= 128,
            "bounded physical horizon/core")
    require(canonical(panel["conductors"]) == "[5,7]", "fixed physical conductors")
    entries = panel["entries"]
    require(type(entries) is list and 1 <= len(entries) <= 16, "bounded native rectangle")
    require(type(panel["literal_history_count"]) is int
            and panel["literal_history_count"] == 4 * len(entries), "four histories per pair")
    require(type(panel["one_sided_boolean_history_sum"]) is int
            and panel["one_sided_boolean_history_sum"] == 2
            and panel["one_sided_equal_pair_share"] == "1/15", "native balanced normalization")
    weight = Fraction(70 * core**2)
    cmin, cmax = Fraction(8, 495 * horizon), Fraction(4, 225 * horizon)
    squares, ratios, indices = [], [], set()
    for row in entries:
        n, m, p, q = (row[key] for key in ("N", "M", "P", "Q"))
        require(all(type(x) is int and 1 < x and x.bit_length() <= 256 for x in (n,m,p,q)),
                "bounded exact physical integers")
        require(n == 25 * core**2 * p and m == 49 * core**2 * q,
                "actual completed physical outputs")
        require(horizon < n < Fraction(11,10)*horizon
                and horizon < m < Fraction(11,10)*horizon, "native physical windows")
        require(type(row["literal_histories_per_mode"]) is int
                and row["literal_histories_per_mode"] == 4
                and row["positive_coefficient_branch_from_histories"] is True,
                "literal positive source branch")
        require(canonical(row["cell"]) == "[1,4]", "common raw residue cell")
        require(type(row["index"]) is list and len(row["index"]) == 2
                and all(type(x) is int and 0 <= x < 16 for x in row["index"]),
                "exact rectangle indices")
        index = tuple(row["index"])
        require(index not in indices, "unique arithmetic pair")
        indices.add(index)
        square = Fraction(row["native_coefficient_square"])
        dual_square = Fraction(row["source_dual_coefficient_square"])
        require(square == Fraction(16, 225**2 * n * m), "actual irrational amplitude square")
        require(square == Fraction(row["left_amplitude_square"])
                * Fraction(row["right_amplitude_square"]), "one-sided source factorization")
        require(cmin**2 < square < cmax**2, "strict positive coefficient interval")
        require(dual_square == (35 * core)**2 * square
                and Fraction(2,35)*dual_square == weight*square,
                "exact principal/source-dual conversion")
        ratio = Fraction(row["ratio_N_over_M"])
        require(ratio == Fraction(n,m) and Fraction(10,11) < ratio < Fraction(11,10),
                "actual Mellin orientation")
        squares.append(square)
        ratios.append(ratio)
    left, right = {i for i,j in indices}, {j for i,j in indices}
    require(indices == set(product(left,right)), "complete selected rectangle")
    pair_ratios = [r/s for r,s in product(ratios,repeat=2)]
    require(all(Fraction(10,11)**2 < r < Fraction(11,10)**2 for r in pair_ratios),
            "all frequency differences in doubled native interval")
    count = len(entries)
    literal_without_gamma = weight * sum(squares, Fraction(0)) / 4
    source_dual_diagonal = Fraction(panel["source_dual_literal_diagonal"])
    require(Fraction(2,35)*source_dual_diagonal == literal_without_gamma,
            "inherited literal diagonal rather than newly centered pair diagonal")
    energy_lower = weight * (count*cmin)**2
    diagonal_upper = 384 * literal_without_gamma
    certified_ratio = energy_lower / diagonal_upper
    require(certified_ratio >= LOWER * count, "actual-panel energy/diagonal lower bound")
    return {"name": panel["name"], "horizon": horizon, "common_core": core,
            "fibre": [core,5,7,1,1], "raw_cell": [1,4],
            "rectangle_shape": [len(left),len(right)], "arithmetic_pairs": count,
            "literal_histories": 4*count, "weight": str(weight),
            "coefficient_branch": "POSITIVE_SYMBOLIC_SQUARE_ROOT",
            "native_coefficient_squares": [str(s) for s in squares],
            "all_frequency_difference_ratio_checks": len(pair_ratios),
            "literal_diagonal_divided_by_Gamma0": str(literal_without_gamma),
            "pair_diagonal_divided_by_Gamma0": str(4*literal_without_gamma),
            "certified_energy_lower": str(energy_lower),
            "certified_literal_diagonal_upper": str(diagonal_upper),
            "certified_energy_over_literal_diagonal_lower": str(certified_ratio),
            "universal_energy_over_literal_diagonal_lower": str(LOWER*count),
            "universal_energy_over_literal_diagonal_upper": 4*count}


def build():
    raw = {key: source_bytes(key) for key in SOURCES}
    native = json.loads(raw[(NMO,NMO_PATH)])
    kernel = json.loads(raw[(SCB,SCB_PATH)])
    require(native["schema"] == "riemann.structures.native_restricted_mellin.v1"
            and native["status"] == "EXACT_RESTRICTED_SOURCE_PROJECTION_AND_SEPARATE_PROOF",
            "frozen NMO source schema; exact bytes authenticated above")
    require(kernel["proof_object_sha256"] ==
            "3385b68dd20c2c10a361eac3afda8aa1f5b3ba767649ed7d7016913650ace388",
            "frozen SCB proof object")
    require(len(native["panels"]) == 2, "inherited panel count")
    hashes = {}
    for path in (NOTE,Path(__file__),TEST):
        data = path.read_bytes()
        require(len(data) <= MAX_BYTES, "local file cap")
        hashes[path.relative_to(ROOT).as_posix()] = sha256(data.replace(b"\r\n",b"\n")).hexdigest()
    result = {"schema": "riemann.post_quotient_principal_readout.v1",
              "sources": [{"commit":key[0],"path":key[1],"git_blob":blob}
                          for key,blob in SOURCES.items()],
              "source_hashes": hashes, "kernel_bounds": kernel_bounds(kernel["kernel"]),
              "panels": [panel_bounds(panel) for panel in native["panels"]],
              "actual_source_coefficients_retained": True,
              "diagonal_resolution": "FOUR_LITERAL_HISTORIES_PER_ARITHMETIC_PAIR",
              "prime_searches": 0, "floating_quadrature_or_logarithms": False,
              "complete_native_gamma_source_bound": False,
              "complete_principal_moment_counterexample": False,
              "absolute_energy_tends_to_zero": True, "RH_conclusion": False}
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
        FIXTURE.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    else:
        require(FIXTURE.stat().st_size <= MAX_BYTES, "artifact cap")
        candidate = json.loads(FIXTURE.read_text(encoding="utf-8"))
        require(canonical(candidate) == canonical(result), "strict canonical replay")
    print(json.dumps({"status":"PASS", "proof_object_sha256":result["proof_object_sha256"]}))


if __name__ == "__main__":
    main()
