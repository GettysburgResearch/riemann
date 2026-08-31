#!/usr/bin/env python3
"""Frozen original-source global minimizer, support margins and literal controls."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from hashlib import sha1, sha256
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFIX = "research/riemann-structures/native-six-hour/"
COMMIT = "a10385170ae8d1555299b6e1ed981e44c5d1c6e5"
PINS = {
    "scout": (
        "native_clipped_path_scout.py",
        "76764bbe7e3a234f57dce2bad86ce11b40915d24",
    ),
    "data": (
        "native_clipped_path.discovery.json",
        "27a69607a27f18b770606827d461b5d3bd147f38",
    ),
    "criterion": (
        "NATIVE_SELF_CONSISTENT_PATH_OPTIMALITY.md",
        "6d907ebd4415ca26b4d7bd95e21244662a497b6f",
    ),
    "preregistration": (
        "NATIVE_CLIPPED_PATH_PREREGISTRATION.md",
        "83b72ddb83b6dae2814438166514ca5fea3a9307",
    ),
    "heldout": (
        "native_monotone_grid.heldout.json",
        "543ab3cf0e4a7dc6f04e05bc781d2a3ed9260e36",
    ),
}
MAX_BYTES = 8 * 1024 * 1024
NOTE = HERE / "GLOBAL_OPTIMAL_NATIVE_ACTIVATION_PATH.md"
TEST = ROOT / "tests/test_native_six_hour_clipped_optimum.py"
FIXTURE = HERE / "native_clipped_path_certificate.json"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def strict_equal(left, right):
    require(canonical(left) == canonical(right), "strict typed global-source replay")


def frozen(name, execute=False):
    path, blob = PINS[name]
    ref = f"{COMMIT}:{PREFIX}{path}"
    size = int(
        subprocess.check_output(["git", "cat-file", "-s", ref], cwd=ROOT, text=True)
    )
    require(0 < size <= MAX_BYTES, "bounded frozen optimal-source artifact")
    raw = subprocess.check_output(["git", "show", ref], cwd=ROOT)
    require(
        len(raw) == size
        and sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest() == blob,
        "exact frozen optimal-source authentication",
    )
    if not execute:
        return raw
    namespace = {
        "__name__": "authenticated_global_optimal_source",
        "__file__": str(HERE / path),
    }
    # Execute only exact declared Git commit/blob-authenticated bytes.
    exec(compile(raw, str(HERE / path), "exec"), namespace)  # noqa: S102
    return SimpleNamespace(**namespace)


def lower_clipped_moments(lam, mu):
    require(
        type(lam) in (int, F) and type(mu) in (int, F),
        "literal exact source parameters",
    )
    lam, mu = F(lam), F(mu)
    require(
        max(
            max(x.numerator.bit_length(), x.denominator.bit_length()) for x in (lam, mu)
        )
        <= 512,
        "bounded exact source parameters",
    )
    require(lam < 0 < lam + mu < 1 and mu > 0, "actual lower-only clipping regime")
    t = -lam / mu
    h = 1 - t
    return (
        mu * h * h / 2,
        mu * h * h * (t + 2) / 6,
        mu * mu * h * h * h / 6,
        F(),
        F(),
        F(),
    )


def validate_discovery(data):
    attempts = data["all16_declared_starts"]
    require(
        len(attempts) == 16
        and data["globally_certified_attempt_indices"] == list(range(16)),
        "all declared starts and outcomes retained",
    )
    require(
        data["floating_steps_are_seed_only"] is True
        and data["full_gamma_identified"] is False
        and data["all_height_path_theorem_claimed"] is False,
        "source scope and seed-only role",
    )
    for attempt in attempts:
        row = attempt["rational_certificate"]
        require(
            row["root_exists_and_unique_in_box"] is True
            and row["global_all_path_source_optimality_certified"] is True,
            "root and full-support certificate both required",
        )
        require(F(row["contraction_upper"]) < 1, "strict contraction")
        for box, image in zip(row["root_box"], row["Krawczyk_image"], strict=True):
            require(
                F(box["lower"])
                < F(image["lower"])
                <= F(image["upper"])
                < F(box["upper"]),
                "whole-box strict Krawczyk inclusion",
            )
        lam, mu = row["root_box"]
        require(
            F(lam["upper"]) < 0
            and F(mu["lower"]) > 0
            and F(lam["lower"]) + F(mu["lower"]) > 0
            and F(lam["upper"]) + F(mu["upper"]) < 1,
            "strict lower-only clipped root",
        )
        require(
            F(row["original_source_c"]["lower"]) > F(3, 2),
            "literal C coefficient coercivity",
        )
        cone = row["full_w_last_support_cone"]
        require(
            F(cone["f"]["lower"]) > F(5, 2)
            and F(cone["d_plus_e_half"]["lower"]) > 2
            and F(cone["d_plus_e"]["lower"]) > 2,
            "full all-path source cone with strict margins",
        )
        actual = row["nearby_rational_actual_path"]
        center = tuple(map(F, attempt["proposed_exact_binary_center"]))
        require(
            tuple(map(F, actual["source_coordinates"]))
            == lower_clipped_moments(*center),
            "independent closed lower-clipped moments and C/2 normalization",
        )
        require(
            len(actual["complete63_source"]) == 63
            and len(actual["complete45_ratio_image"]) == 45,
            "complete literal source and physical ratio replay",
        )
        require(
            F(row["root_energy"]["lower"]) > F(15746, 100)
            and F(row["root_energy"]["upper"]) < F(15748, 100),
            "bounded original optimal-energy enclosure",
        )
    return attempts


def independent_gradient_control(scout, data):
    grid, model = scout.source()
    attempt = data["all16_declared_starts"][0]
    actual = attempt["rational_certificate"]["nearby_rational_actual_path"]
    x = tuple(map(F, actual["source_coordinates"]))
    literal = list(map(F, actual["complete63_source"]))
    field = model.affine.source_field(
        model.curve, model.kernel, literal, model.records, model.ratios
    )
    gradients = []
    for i, column in enumerate(model.columns):
        variation = model.affine.source_field(
            model.curve, model.kernel, column, model.records, model.ratios
        )
        direct = model.affine.inner(model.kernel, variation, field)
        affine = model.cross[i]
        for j in range(6):
            affine = model.kernel.ea(affine, model.kernel.es(model.gram[i][j], x[j]))
        require(
            direct == affine, "literal physical field gives the same original gradient"
        )
        gradients.append(model.kernel.expr_json(direct))
    return {
        "all_six_direct_physical_gradient_expressions": gradients,
        "literal_C_coefficient_is_half_third_expression": True,
        "original_source_metric_replaced": False,
        "nearby_actual_energy": grid.interval_json(
            model.kernel.ei(grid.energy(model, x))
        ),
    }


def build():
    scout = frozen("scout", True)
    frozen("criterion")
    frozen("preregistration")
    data = json.loads(frozen("data"))
    heldout = json.loads(frozen("heldout"))
    strict_equal(scout.discover(), data)
    validate_discovery(data)
    grid_lower = F(heldout["panels"][0]["minimum_energy_interval"]["lower"])
    require(
        all(
            F(row["rational_certificate"]["root_energy"]["upper"]) < grid_lower
            for row in data["all16_declared_starts"]
        ),
        "strict original-energy improvement over complete heldout grid",
    )
    result = {
        "schema": "riemann.native_six_hour.global_optimal_source_certificate.v1",
        "sources": [
            {"commit": COMMIT, "path": PREFIX + path, "blob": blob}
            for path, blob in PINS.values()
        ],
        "complete_frozen_discovery": data,
        "independent_gradient_control": independent_gradient_control(scout, data),
        "authenticated_heldout_grid_energy_lower": str(grid_lower),
        "global_complete_H25_path_optimum": True,
        "unique_oriented_path_image_modulo_pauses": True,
        "coercivity_coefficients_planar_D_F": [3, 4, 5],
        "full_gamma_source_identified": False,
        "all_height_theorem_claimed": False,
        "owned_sha256_lf": {
            path.relative_to(ROOT).as_posix(): sha256(
                path.read_bytes().replace(b"\r\n", b"\n")
            ).hexdigest()
            for path in (Path(__file__), NOTE, TEST)
        },
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.write:
        raw = (
            json.dumps(result, sort_keys=True, indent=2, allow_nan=False) + "\n"
        ).encode()
        require(len(raw) <= MAX_BYTES, "bounded final optimal-source artifact")
        FIXTURE.write_bytes(raw)
    else:
        require(
            FIXTURE.stat().st_size <= MAX_BYTES, "bounded final optimal-source read"
        )
        strict_equal(json.loads(FIXTURE.read_bytes()), result)
    print("PASS original complete H25 global path optimum and exact source controls")


if __name__ == "__main__":
    main()
