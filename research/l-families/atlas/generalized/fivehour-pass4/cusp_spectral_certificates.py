"""Directed finite instances of the native cusp spectral/period inequalities.

These certificates invoke the analytic source theorems; they are not a
quadrature of a period matrix or a proof of the growing-parameter theorem.
Run with python-flint 0.9.0. No floating-point sign tests are used.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys

import flint
from flint import arb, ctx


PROOF_COMMIT = "2c309f1196776575942f7f5434dff857d3a922f9"
REL_DIR = "research/l-families/atlas/generalized/fivehour-pass4"
PROOF_FILES = (
    "CUSP_KRONECKER_SPECTRAL_LAW.md",
    "CUSP_PERIOD_MESOSCOPIC_INERTIA.md",
    "CUSP_CERTIFICATE_PREREGISTRATION.md",
)
OPERATOR_WEIGHTS = (96, 192, 384, 768, 1536, 3072, 6144, 12288)
PERIOD_WEIGHTS = (384, 1536, 6144, 24576, 98304)
EPS_DENOMINATORS = (16, 32, 64, 128, 256)
MARGIN_DENOMINATORS = (4, 8, 16)
ALLOWED_BITS = (256, 512)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def pack(value: arb) -> dict:
    require(value.is_finite(), "nonfinite primitive enclosure")
    midpoint, radius, exponent = value.mid_rad_10exp(ctx.dps + 8)
    return {"mid": str(midpoint), "rad": str(radius), "exp10": int(exponent)}


def unpack(box: dict) -> arb:
    require(set(box) == {"mid", "rad", "exp10"}, "invalid ball fields")
    require(type(box["exp10"]) is int, "invalid ball exponent")
    require(abs(box["exp10"]) <= 1000000, "ball exponent cap")
    require(type(box["mid"]) is str and type(box["rad"]) is str, "ball integers")
    require(len(box["mid"]) <= 500 and len(box["rad"]) <= 500, "ball digit cap")
    midpoint, radius = int(box["mid"]), int(box["rad"])
    require(radius >= 0, "negative radius")
    return arb(midpoint, radius) * arb(10) ** box["exp10"]


def exact_floor(value: arb) -> int | None:
    result = value.floor().unique_fmpz()
    return None if result is None else int(result)


def exact_ceil(value: arb) -> int | None:
    result = exact_floor(-value)
    return None if result is None else -result


def constants() -> dict[str, arb]:
    pi = arb.pi()
    a0 = arb(3).sqrt() / 2
    q0 = (-2 * pi * a0).exp()
    r0 = 2 * q0 / (1 - q0) ** 2
    c0 = (arb.const_euler() - (4 * pi).log()) / 2
    u0 = c0 + r0 - a0.log() / 2
    return {"pi": pi, "a0": a0, "r0": r0, "c0": c0, "u0": u0}


def gram_delta(k: int, j: int) -> arb:
    require(type(k) is int and type(j) is int, "integer k,j required")
    require(4 <= k <= 100000 and 1 <= j <= 10000, "work cap")
    pi = arb.pi()
    log_delta = (4 * pi * j).log() + (k - 1) * (2 * pi * j).log()
    log_delta -= arb(k).lgamma()
    log_delta += 4 * pi**2 * j**2 / k
    return log_delta.exp()


def gamma_q(shape: int, argument: arb) -> arb:
    require(type(shape) is int and 1 <= shape <= 100000, "Gamma shape cap")
    require(argument > 0, "positive Gamma argument")
    return argument.gamma_upper(shape, regularized=1)


def gamma_q_finite_sum(shape: int, argument: arb) -> arb:
    """Independent integer-shape formula: a complete finite Poisson sum."""
    require(type(shape) is int and 1 <= shape <= 100000, "Gamma shape cap")
    require(argument > 0, "positive Gamma argument")
    term = arb(1)
    total = term
    for r in range(1, shape):
        term *= argument / r
        total += term
    return (-argument).exp() * total


def completed_zeta(value: arb) -> arb:
    half = value / 2
    return (-half * arb.pi().log()).exp() * half.gamma() * value.zeta()


def operator_indices(k: int) -> list[int]:
    return sorted({1, 2, math.isqrt(k) // 4, k // 96, k // 48, k // 24} - {0})


def operator_cell(k: int, j: int) -> dict:
    c = constants()
    delta = gram_delta(k, j)
    q = gamma_q(k, 4 * c["pi"] * j)
    lower_height = arb(k - 1) / (4 * c["pi"] * j) * q * (1 - delta)
    upper = arb(k - 1) / (24 * j) + c["pi"] / 6 + c["u0"]
    valid = bool(delta < 1 and lower_height >= 3 / c["pi"])
    result = {
        "k": k, "j": j, "delta": pack(delta), "gamma_q": pack(q),
        "lower_height": pack(lower_height), "upper_eigenvalue": pack(upper),
        "lower_status": "CERTIFIED_ANALYTIC_BOUND" if valid else "UNRESOLVED",
        "leading_scale": pack(arb(k) / (24 * j)),
    }
    if valid:
        lower = c["pi"] * lower_height / 6 - lower_height.log() / 2
        lower += c["c0"] - c["r0"]
        require(lower < upper, "contradictory analytic eigenvalue bounds")
        result["lower_eigenvalue"] = pack(lower)
    return result


def period_cell(k: int, epsilon_denominator: int, margin_denominator: int) -> dict:
    require(k in PERIOD_WEIGHTS, "undeclared period weight")
    require(epsilon_denominator in EPS_DENOMINATORS, "undeclared epsilon")
    require(margin_denominator in MARGIN_DENOMINATORS, "undeclared margin")
    c = constants()
    epsilon = arb(1) / epsilon_denominator
    margin = arb(1) / margin_denominator
    beta = 1 - 2 * epsilon
    positive = completed_zeta(2 - 2 * epsilon)
    negative = -completed_zeta(1 - 2 * epsilon)
    require(positive > 0 and negative > 0, "wrong Eisenstein constant-term signs")
    turning = ((negative / positive).log() / beta).exp()
    index_scale = arb(k - 1) / (4 * c["pi"] * turning)
    jminus = exact_floor((1 - margin) * index_scale)
    jplus = exact_ceil((1 + margin) * index_scale)
    height = (1 + margin / 2) * turning
    result = {
        "k": k, "epsilon_denominator": epsilon_denominator,
        "margin_denominator": margin_denominator,
        "C": pack(positive), "D": pack(negative), "turning_height": pack(turning),
        "index_scale": pack(index_scale), "height": pack(height),
        "jminus": jminus, "jplus": jplus,
    }
    if jminus is None or jplus is None:
        result.update(lower_status="UNRESOLVED_INDEX", upper_status="UNRESOLVED_INDEX")
        return result
    require(0 <= jminus <= 10000 and 1 <= jplus <= 10000, "index work cap")
    compact_margin = negative * (epsilon * c["a0"].log()).exp() - positive - c["r0"]
    flag_ratio = (1 + (k - 1 + epsilon) / (4 * c["pi"] * jplus)) ** beta
    flag_margin = negative - positive * flag_ratio - c["r0"]
    result.update(compact_margin=pack(compact_margin), flag_margin=pack(flag_margin))
    upper_valid = bool(compact_margin > 0 and flag_margin > 0)
    result["upper_status"] = "CERTIFIED_ANALYTIC_BOUND" if upper_valid else "UNRESOLVED"
    if upper_valid:
        result["nonnegative_inertia_upper"] = min(k // 12, jplus - 1)
    if jminus == 0:
        result.update(lower_status="TRIVIAL_ZERO", positive_inertia_lower=0)
        return result
    delta = gram_delta(k, jminus)
    q = gamma_q(k - 1, 4 * c["pi"] * jminus * height)
    alpha = (1 - delta) * q
    positive_floor = positive * height ** (1 - epsilon) - negative * height**epsilon - c["r0"]
    negative_ceiling = negative * turning**epsilon + c["r0"]
    lower_margin = positive_floor * alpha - negative_ceiling * (1 - alpha)
    lower_valid = bool(turning >= 1 and delta < 1 and positive_floor > 0 and lower_margin > 0)
    result.update(delta=pack(delta), gamma_q=pack(q), high_cusp_mass=pack(alpha),
                  positive_floor=pack(positive_floor), negative_ceiling=pack(negative_ceiling),
                  lower_margin=pack(lower_margin),
                  lower_status="CERTIFIED_ANALYTIC_BOUND" if lower_valid else "UNRESOLVED")
    if lower_valid:
        result["positive_inertia_lower"] = jminus
    if lower_valid and upper_valid:
        require(jminus <= result["nonnegative_inertia_upper"], "contradictory inertia bounds")
    return result


def source_locks() -> dict:
    here = Path(__file__).resolve()
    root = here.parents[5]
    entries = []
    for name in PROOF_FILES:
        path = f"{REL_DIR}/{name}"
        data = subprocess.check_output(["git", "show", f"{PROOF_COMMIT}:{path}"], cwd=root)
        blob = subprocess.check_output(["git", "rev-parse", f"{PROOF_COMMIT}:{path}"], cwd=root).decode().strip()
        entries.append({"path": path, "git_blob": blob, "sha256": hashlib.sha256(data).hexdigest()})
    return {"proof_commit": PROOF_COMMIT, "proof_files": entries,
            "producer_sha256": hashlib.sha256(here.read_bytes()).hexdigest()}


def build_report(bits: int) -> dict:
    require(type(bits) is int and bits in ALLOWED_BITS, "precision must be 256 or 512")
    previous = ctx.prec
    try:
        ctx.prec = bits
        operator = [operator_cell(k, j) for k in OPERATOR_WEIGHTS for j in operator_indices(k)]
        period = [period_cell(k, e, m) for k in PERIOD_WEIGHTS
                  for e in EPS_DENOMINATORS for m in MARGIN_DENOMINATORS]
        controls = []
        for shape, numerator, denominator in ((1, 1, 3), (2, 5, 2), (8, 7, 1), (32, 21, 1), (96, 80, 1)):
            argument = arb(numerator) / denominator
            library = gamma_q(shape, argument)
            explicit = gamma_q_finite_sum(shape, argument)
            require(library.overlaps(explicit), "independent Gamma formula disagreement")
            controls.append({"shape": shape, "argument": [numerator, denominator],
                             "library": pack(library), "finite_sum": pack(explicit)})
        return {"schema": "native-cusp-analytic-bounds-v1", "precision_bits": bits,
                "arithmetic": "ARB_DIRECTED_REAL_BALLS", "python_flint": flint.__version__,
                "coverage": "complete preregistered Cartesian panels; unresolved cells retained",
                "scope": "finite instances of analytic source inequalities, not direct period quadrature",
                "source": source_locks(), "constants": {k: pack(v) for k, v in constants().items()},
                "operator": operator, "period": period, "gamma_controls": controls}
    finally:
        ctx.prec = previous


def validate_against(actual: dict, expected: dict) -> None:
    require(type(actual) is dict, "report object required")
    require(actual == expected, "report differs from complete primitive reconstruction")


def summary(report: dict) -> dict:
    period = report["period"]
    return {"precision_bits": report["precision_bits"], "operator_cells": len(report["operator"]),
            "period_cells": len(period),
            "period_lower_certified": sum(r["lower_status"] == "CERTIFIED_ANALYTIC_BOUND" for r in period),
            "period_upper_certified": sum(r["upper_status"] == "CERTIFIED_ANALYTIC_BOUND" for r in period),
            "period_both_certified": sum(r["lower_status"] == r["upper_status"] == "CERTIFIED_ANALYTIC_BOUND" for r in period)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bits", type=int, choices=ALLOWED_BITS, default=256)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--emit", type=Path)
    group.add_argument("--check", type=Path)
    args = parser.parse_args()
    report = build_report(args.bits)
    if args.emit is not None:
        args.emit.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    else:
        require(args.check.stat().st_size <= 5000000, "report byte cap")
        actual = json.loads(args.check.read_text(encoding="utf-8"))
        validate_against(actual, report)
    print(json.dumps(summary(report), sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
