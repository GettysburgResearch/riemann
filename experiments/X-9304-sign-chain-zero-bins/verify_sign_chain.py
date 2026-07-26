#!/usr/bin/env python3
"""Exact checker for total-count-saturated Hardy-Z sign chains.

No special function and no floating-point arithmetic is used. The checker
verifies a multiplicity-aware total-count ball, exact ordered sample points,
directed nonzero Hardy-Z intervals, complete sign alternation, and every
sign-preserving refinement step.
"""
from __future__ import annotations
import argparse, hashlib, json, string
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

SCHEMA = "riemann.x9304-sign-chain-zero-bins.v1"
PRODUCTION = "RIEMANN_ZETA_DIRECTED"
SYNTHETIC = "SYNTHETIC_MODEL"


class CertificateError(ValueError):
    pass


def exact_int(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer")
    return value


def rat(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = exact_int(value.get("numerator"), f"{name}.numerator")
    denominator = exact_int(value.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def fj(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def interval(value: Any, name: str) -> tuple[Fraction, Fraction]:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    lower = rat(value.get("lower"), f"{name}.lower")
    upper = rat(value.get("upper"), f"{name}.upper")
    if lower > upper:
        raise CertificateError(f"{name} is reversed")
    return lower, upper


def ij(value: tuple[Fraction, Fraction]) -> dict[str, dict[str, int]]:
    return {"lower": fj(value[0]), "upper": fj(value[1])}


def sign(value: tuple[Fraction, Fraction], name: str) -> int:
    lower, upper = value
    if lower > 0:
        return 1
    if upper < 0:
        return -1
    raise CertificateError(f"{name} contains zero and has no certified sign")


def ceil_fraction(value: Fraction) -> int:
    return -((-value.numerator) // value.denominator)


def floor_fraction(value: Fraction) -> int:
    return value.numerator // value.denominator


def unique_integer(value: tuple[Fraction, Fraction], name: str) -> int:
    lower, upper = value
    first = ceil_fraction(lower)
    last = floor_fraction(upper)
    if first != last:
        raise CertificateError(f"{name} does not isolate one integer")
    return first


def canonical_sha(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


def validate_digest(value: Any, name: str) -> str:
    if (
        not isinstance(value, str)
        or len(value) != 64
        or any(character not in string.hexdigits for character in value)
    ):
        raise CertificateError(f"{name} must be a SHA-256 hexadecimal digest")
    return value.lower()


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError("schema mismatch")
    classification = data.get("classification")
    if classification not in (PRODUCTION, SYNTHETIC):
        raise CertificateError("unsupported classification")

    slab = data.get("slab")
    if not isinstance(slab, dict):
        raise CertificateError("slab must be an object")
    slab_lower = rat(slab.get("lower"), "slab.lower")
    slab_upper = rat(slab.get("upper"), "slab.upper")
    if not slab_lower < slab_upper:
        raise CertificateError("slab endpoints must increase")

    total_interval = interval(data.get("total_count_interval"), "total_count_interval")
    total_count = unique_integer(total_interval, "total_count_interval")
    if total_count < 1:
        raise CertificateError("total count must be positive")

    gates = data.get("gates")
    if not isinstance(gates, dict):
        raise CertificateError("gates must be an object")
    if classification == PRODUCTION:
        if gates.get("total_count_status") != "CERTIFIED_TOTAL_ZETA_ZERO_COUNT":
            raise CertificateError("bad total-count gate")
        if gates.get("sign_status") != "CERTIFIED_HARDY_Z_INTERVALS":
            raise CertificateError("bad Hardy-Z sign gate")
        validate_digest(gates.get("total_count_sha256"), "total_count_sha256")
        validate_digest(gates.get("sign_table_sha256"), "sign_table_sha256")

    raw_samples = data.get("samples")
    if not isinstance(raw_samples, list) or len(raw_samples) != total_count + 1:
        raise CertificateError("sample count must equal total count plus one")

    samples: list[dict[str, Any]] = []
    for index, raw in enumerate(raw_samples):
        if not isinstance(raw, dict):
            raise CertificateError(f"samples[{index}] must be an object")
        ordinate = rat(raw.get("t"), f"samples[{index}].t")
        z_interval = interval(raw.get("z_interval"), f"samples[{index}].z_interval")
        z_sign = sign(z_interval, f"samples[{index}].z_interval")
        if not slab_lower < ordinate < slab_upper:
            raise CertificateError("sample lies outside the open slab")
        if samples and not samples[-1]["t"] < ordinate:
            raise CertificateError("samples are not strictly increasing")
        samples.append({"t": ordinate, "z": z_interval, "sign": z_sign})

    for index in range(total_count):
        if samples[index]["sign"] == samples[index + 1]["sign"]:
            raise CertificateError(f"no sign alternation at sample edge {index}")

    bins: list[dict[str, Any]] = []
    for index in range(total_count):
        bins.append(
            {
                "lower": samples[index]["t"],
                "upper": samples[index + 1]["t"],
                "lower_sign": samples[index]["sign"],
                "upper_sign": samples[index + 1]["sign"],
                "steps": 0,
            }
        )

    raw_refinements = data.get("refinements", [])
    if not isinstance(raw_refinements, list):
        raise CertificateError("refinements must be an array")
    seen_indices: set[int] = set()
    for refinement_index, raw in enumerate(raw_refinements):
        if not isinstance(raw, dict):
            raise CertificateError(f"refinements[{refinement_index}] must be an object")
        bin_index = exact_int(
            raw.get("bin_index"), f"refinements[{refinement_index}].bin_index"
        )
        if bin_index < 0 or bin_index >= total_count or bin_index in seen_indices:
            raise CertificateError("invalid or duplicate refinement bin index")
        seen_indices.add(bin_index)
        steps = raw.get("steps")
        if not isinstance(steps, list):
            raise CertificateError("refinement steps must be an array")
        current = bins[bin_index]
        for step_index, step in enumerate(steps):
            if not isinstance(step, dict):
                raise CertificateError("refinement step must be an object")
            ordinate = rat(
                step.get("t"),
                f"refinements[{refinement_index}].steps[{step_index}].t",
            )
            z_interval = interval(
                step.get("z_interval"),
                f"refinements[{refinement_index}].steps[{step_index}].z_interval",
            )
            z_sign = sign(
                z_interval,
                f"refinements[{refinement_index}].steps[{step_index}].z_interval",
            )
            if not current["lower"] < ordinate < current["upper"]:
                raise CertificateError("refinement point is not inside the current bin")
            if z_sign == current["lower_sign"]:
                current["lower"] = ordinate
                current["lower_sign"] = z_sign
            elif z_sign == current["upper_sign"]:
                current["upper"] = ordinate
                current["upper_sign"] = z_sign
            else:
                raise CertificateError("internal sign logic failure")
            if current["lower_sign"] == current["upper_sign"]:
                raise CertificateError("refinement lost opposite endpoint signs")
            current["steps"] += 1

    target_raw = data.get("target_ordinate")
    target = rat(target_raw, "target_ordinate") if target_raw is not None else None
    output_bins: list[dict[str, Any]] = []
    for index, current in enumerate(bins):
        row: dict[str, Any] = {
            "bin_index": index,
            "lower": fj(current["lower"]),
            "upper": fj(current["upper"]),
            "width": fj(current["upper"] - current["lower"]),
            "lower_sign": current["lower_sign"],
            "upper_sign": current["upper_sign"],
            "refinement_steps": current["steps"],
            "exact_zero_count": 1,
            "critical_line": True,
            "simple": True,
        }
        if target is not None:
            distance_square_upper = max(
                (target - current["lower"]) ** 2,
                (target - current["upper"]) ** 2,
            )
            row["distance_square_upper"] = fj(distance_square_upper)
        output_bins.append(row)

    canonical = {
        "schema": SCHEMA,
        "classification": classification,
        "slab": {"lower": fj(slab_lower), "upper": fj(slab_upper)},
        "total_count": total_count,
        "samples": [
            {"t": fj(sample["t"]), "z_interval": ij(sample["z"])}
            for sample in samples
        ],
        "bins": output_bins,
    }
    return {
        **canonical,
        "certificate_sha256": canonical_sha(canonical),
        "verdict": "SATURATED_SIGN_CHAIN_ISOLATES_ALL_ZEROS",
        "proof_boundary": (
            "Finite rational and sign logic only. Production validity depends on "
            "the external directed total-count and Hardy-Z interval gates."
        ),
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        output = verify(json.loads(args.certificate.read_text()))
    except (CertificateError, KeyError, TypeError, json.JSONDecodeError) as error:
        print(json.dumps({"verdict": "REJECTED", "error": str(error)}, indent=2))
        return 2
    text = json.dumps(output, indent=2, sort_keys=True) + "\n"
    print(text, end="")
    if args.output is not None:
        args.output.write_text(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
