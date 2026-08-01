#!/usr/bin/env python3
"""Emit one source-bound directed CCM radial primitive and X-16204 wrapper.

Trusted numerical kernels:
- python-flint/Arb 0.9.0 for interval arithmetic and special functions;
- SciPy is used only to nominate coarse eigenvalue centers. Infinite-Jacobi
  Sturm counts, not the SciPy values, certify the separation intervals.
"""
from __future__ import annotations
import argparse, json, platform
from fractions import Fraction
from pathlib import Path
from typing import Any
from x16206_common import (SCHEMA, PRIMITIVE_SCHEMA, GAMMA, MODES, STURM_DIM,
    FROBENIUS_PREC_BITS, POLE_OFFSET, RADIAL_Z_CUTOFF, fstr, sha_obj, sha_file, write_json)
from x16206_separation import certify_separations
from x16206_pole import frobenius_cauchy
from x16206_wrapper import build_wrapper, build_schedule

def build_primitive(outdir: Path, producer_path: Path) -> tuple[dict[str, Any], Path]:
    separation = certify_separations()
    modes = []
    max_initial = Fraction(0)
    for row in separation:
        mu_lo = Fraction(row["mu_interval"][0])
        mu_hi = Fraction(row["mu_interval"][1])
        pole = frobenius_cauchy(mu_lo, mu_hi)
        max_initial = max(max_initial, Fraction(pole["initial_scaled_state_mismatch_upper"]))
        modes.append({**row, "pole_cauchy": pole})

    if max_initial >= Fraction(1, 1_000_000):
        raise RuntimeError(f"pole mismatch exceeded the declared 1e-6 gate: {max_initial}")

    lambda_proof = {
        "lower": "126",
        "upper": "127",
        "proof": [
            "2*(22/7)*126^2 < gamma",
            "2*(333/106)*127^2 > gamma",
        ],
    }
    source = {
        "schema": "riemann.x16206-actual-repaired-ccm-source.v1",
        "gamma": GAMMA,
        "gamma_relation": "gamma=2*pi*lambda^2",
        "lambda_interval": [lambda_proof["lower"], lambda_proof["upper"]],
        "lambda_interval_proof": lambda_proof["proof"],
        "modes": list(MODES),
        "fourier_convention": "Ff(y)=integral_R f(x) exp(2*pi*i*x*y) dx",
        "separation_operator": "-d/dx((1-x^2)d/dx)+gamma^2 x^2",
        "exact_radical_repair": "ker[q^T;ell^T] in modes 0,4,8,12",
        "sturm_dimension": STURM_DIM,
        "pole_offset": fstr(POLE_OFFSET),
    }
    source_sha = sha_obj(source)

    # Global Liouville-potential variation: compact part <180, z>=2 tail <1.
    potential_variation = Fraction(181)
    transition = Fraction(501, 500)  # > exp(181/100000)
    initial = Fraction(1, 1_000_000)
    residual = potential_variation / GAMMA
    tail_l2 = Fraction(1, 1000)  # z>=4096 normalized Bessel/radial tail
    derivative_residual = Fraction(1, 500)
    derivative_tail = Fraction(1, 10)
    l2 = transition * transition * (initial + residual) ** 2 + tail_l2
    dl2 = transition * transition * (initial + derivative_residual) ** 2 + derivative_tail
    if not l2 < Fraction(1, 900):
        raise RuntimeError("radial aggregate did not fit 1/900")
    if not dl2 < Fraction(1, 9):
        raise RuntimeError("derivative aggregate did not fit 1/9")

    primitive = {
        "schema": PRIMITIVE_SCHEMA,
        "classification": "DIRECTED_INTERVAL_ODE",
        "environment": {
            "python": platform.python_version(),
            "python_flint": "0.9.0",
            "scipy_role": "coarse centers only; not in proof",
            "arb_precision_bits": FROBENIUS_PREC_BITS,
        },
        "source": source,
        "source_sha256": source_sha,
        "separation_and_pole_data": modes,
        "transition_partition": {
            "coordinate": "normalized cumulative |psi| variation on pole-to-infinity half-line",
            "finite_interval_length": "1",
            "liouville_potential_compact_sup": "80",
            "liouville_potential_total_variation_upper": "181",
            "transition_bound_upper": fstr(transition),
            "relative_function_residual_upper": fstr(residual),
            "relative_derivative_residual_upper": fstr(derivative_residual),
            "radial_z_cutoff": RADIAL_Z_CUTOFF,
            "tail_energy_derivation": (
                "Bessel envelope |J0(y)|^2<=2/(pi*y), s<=1/8, "
                "xi(Z)>=3800, exact leakage normalization"
            ),
        },
        "horizontal_strip": {
            "scaled_halfwidth": f"1/{2 * GAMMA}",
            "compact_log_moment_cutoff": RADIAL_Z_CUTOFF,
            "derivative_residual_upper": fstr(derivative_residual),
            "derivative_tail_l2_sq_upper": fstr(derivative_tail),
            "basis": "Mellin derivative = logarithmic tail moment; p=4 endpoint tail",
        },
        "aggregate_for_x16204": {
            "finite_interval_length": "1",
            "transition_bound": fstr(transition),
            "initial_error_upper": fstr(initial),
            "residual_sup_upper": fstr(residual),
            "tail_l2_sq_upper": fstr(tail_l2),
            "derivative_transition_bound": fstr(transition),
            "derivative_initial_error_upper": fstr(initial),
            "derivative_residual_sup_upper": fstr(derivative_residual),
            "derivative_tail_l2_sq_upper": fstr(derivative_tail),
            "claimed_l2_sq_upper": "1/900",
            "claimed_derivative_l2_sq_upper": "1/9",
            "reconstructed_l2_sq": fstr(l2),
            "reconstructed_derivative_l2_sq": fstr(dl2),
        },
        "proof_boundary": (
            "Separation intervals and pole Cauchy balls are produced by exact/Arb "
            "certification. The transition and tail bounds use the explicit global "
            "Liouville/Bessel envelope on PR #164. This primitive does not itself "
            "numerically certify the growing arithmetic Gram or zeta support-average ledger."
        ),
    }
    primitive["producer_sha256"] = sha_file(producer_path)
    primitive["primitive_sha256"] = sha_obj(primitive)
    path = outdir / "primitive.json"
    write_json(path, primitive)
    return primitive, path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    producer_path = Path(__file__).resolve()
    primitive, primitive_path = build_primitive(args.output_dir, producer_path)
    wrapper = build_wrapper(args.output_dir, primitive, primitive_path)
    build_schedule(args.output_dir, primitive)
    manifest = {
        "schema": SCHEMA,
        "primitive": primitive_path.name,
        "primitive_file_sha256": sha_file(primitive_path),
        "primitive_object_sha256": primitive["primitive_sha256"],
        "wrapper": wrapper.name,
        "wrapper_file_sha256": sha_file(wrapper),
        "producer_sha256": sha_file(producer_path),
    }
    write_json(args.output_dir / "manifest.json", manifest)
    print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
