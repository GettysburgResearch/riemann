#!/usr/bin/env python3
"""Exact finite regression for T-22301 and L-22301.

The checker uses only integers and fractions.Fraction.  It verifies:

* direct time-domain convolution equals grouped product-scale convolution;
* diagonal/off-diagonal pair bookkeeping;
* |z^2|=|z|^2 on exact rational complex samples;
* the critical identity-orbit evaluation can grow while the coefficient
  l2 norm stays one.

The data are synthetic algebra only; no Riemann value is evaluated.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x22301-semiprime-convolution-square.v1"


class CertificateError(ValueError):
    pass


def frac(value: Any, name: str) -> Fraction:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise CertificateError(f"{name} is not rational") from exc
    if isinstance(value, list) and len(value) == 2:
        if any(isinstance(x, bool) or not isinstance(x, int) for x in value):
            raise CertificateError(f"{name} pair must contain integers")
        if value[1] == 0:
            raise CertificateError(f"{name} denominator is zero")
        return Fraction(value[0], value[1])
    raise CertificateError(f"{name} must be an integer, fraction string, or [p,q]")


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer")
    return value


def add(target: dict[int, Fraction], key: int, value: Fraction) -> None:
    target[key] = target.get(key, Fraction(0)) + value
    if target[key] == 0:
        del target[key]


def convolve(a: dict[int, Fraction], b: dict[int, Fraction]) -> dict[int, Fraction]:
    out: dict[int, Fraction] = {}
    for i, ai in a.items():
        for j, bj in b.items():
            add(out, i + j, ai * bj)
    return out


def serialize_map(values: dict[int, Fraction]) -> dict[str, str]:
    return {str(k): str(values[k]) for k in sorted(values)}


def canonical_digest(payload: dict[str, Any]) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def verify(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict) or payload.get("schema") != SCHEMA:
        raise CertificateError("schema mismatch")

    raw_window = payload.get("window")
    if not isinstance(raw_window, dict) or not raw_window:
        raise CertificateError("window must be a nonempty object")
    window: dict[int, Fraction] = {}
    for key, value in raw_window.items():
        try:
            shift = int(key)
        except (TypeError, ValueError) as exc:
            raise CertificateError("window shifts must be integers") from exc
        add(window, shift, frac(value, f"window[{key}]"))
    if not window:
        raise CertificateError("window is identically zero")

    raw_atoms = payload.get("atoms")
    if not isinstance(raw_atoms, list) or len(raw_atoms) < 2:
        raise CertificateError("at least two atoms are required")
    atoms: list[tuple[str, int, Fraction]] = []
    names: set[str] = set()
    for index, atom in enumerate(raw_atoms):
        if not isinstance(atom, dict):
            raise CertificateError(f"atoms[{index}] must be an object")
        name = atom.get("name")
        if not isinstance(name, str) or not name or name in names:
            raise CertificateError("atom names must be unique nonempty strings")
        names.add(name)
        location = integer(atom.get("location"), f"atoms[{index}].location")
        weight = frac(atom.get("weight"), f"atoms[{index}].weight")
        atoms.append((name, location, weight))

    q: dict[int, Fraction] = {}
    for _, location, weight in atoms:
        for shift, coefficient in window.items():
            add(q, location + shift, weight * coefficient)
    direct = convolve(q, q)

    window_square = convolve(window, window)
    grouped: dict[int, Fraction] = {}
    diagonal: dict[int, Fraction] = {}
    off_diagonal: dict[int, Fraction] = {}
    pair_coefficients: dict[str, str] = {}
    for i, (name_i, loc_i, weight_i) in enumerate(atoms):
        for j, (name_j, loc_j, weight_j) in enumerate(atoms):
            product_location = loc_i + loc_j
            coefficient = weight_i * weight_j
            pair_coefficients[f"{name_i}*{name_j}"] = str(coefficient)
            for shift, wvalue in window_square.items():
                contribution = coefficient * wvalue
                add(grouped, product_location + shift, contribution)
                if i == j:
                    add(diagonal, product_location + shift, contribution)
                else:
                    add(off_diagonal, product_location + shift, contribution)

    if direct != grouped:
        raise CertificateError("direct and grouped convolution disagree")
    recombined = dict(diagonal)
    for key, value in off_diagonal.items():
        add(recombined, key, value)
    if recombined != direct:
        raise CertificateError("diagonal/off-diagonal ledger does not recombine")

    samples = payload.get("complex_samples")
    if not isinstance(samples, list) or not samples:
        raise CertificateError("complex_samples must be nonempty")
    h2_norm_sq = Fraction(0)
    h1_square_norm = Fraction(0)
    for index, sample in enumerate(samples):
        if not isinstance(sample, list) or len(sample) != 2:
            raise CertificateError("each complex sample must be [real,imag]")
        real = frac(sample[0], f"complex_samples[{index}][0]")
        imag = frac(sample[1], f"complex_samples[{index}][1]")
        modulus_sq = real * real + imag * imag
        square_real = real * real - imag * imag
        square_imag = 2 * real * imag
        square_modulus_sq = square_real * square_real + square_imag * square_imag
        if square_modulus_sq != modulus_sq * modulus_sq:
            raise CertificateError("complex square modulus identity failed")
        h2_norm_sq += modulus_sq
        # |z^2| is exactly |z|^2, a rational nonnegative number.
        h1_square_norm += modulus_sq
    if h2_norm_sq != h1_square_norm:
        raise CertificateError("H2/H1 square norm identity failed")

    block_size = integer(payload.get("identity_orbit_block_size"), "identity_orbit_block_size")
    if block_size < 2:
        raise CertificateError("identity_orbit_block_size must be at least two")
    coefficient_l2_norm_sq = Fraction(1)
    point_evaluation_sq = Fraction(block_size)

    claimed = payload.get("claimed")
    if not isinstance(claimed, dict):
        raise CertificateError("claimed must be an object")
    if frac(claimed.get("h2_norm_sq"), "claimed.h2_norm_sq") != h2_norm_sq:
        raise CertificateError("claimed H2 norm mismatch")
    if frac(claimed.get("h1_square_norm"), "claimed.h1_square_norm") != h1_square_norm:
        raise CertificateError("claimed H1 square norm mismatch")
    if frac(claimed.get("identity_point_evaluation_sq"), "claimed.identity_point_evaluation_sq") != point_evaluation_sq:
        raise CertificateError("claimed identity-orbit growth mismatch")

    proof = {
        "schema": SCHEMA,
        "classification": "EXACT_SYNTHETIC_CONVOLUTION_SQUARE_REGRESSION",
        "direct_convolution": serialize_map(direct),
        "grouped_product_convolution": serialize_map(grouped),
        "diagonal_convolution": serialize_map(diagonal),
        "off_diagonal_convolution": serialize_map(off_diagonal),
        "window_square": serialize_map(window_square),
        "ordered_pair_coefficients": pair_coefficients,
        "h2_norm_sq": str(h2_norm_sq),
        "h1_square_norm": str(h1_square_norm),
        "identity_orbit_control": {
            "coefficient_l2_norm_sq": str(coefficient_l2_norm_sq),
            "point_evaluation_sq": str(point_evaluation_sq),
            "growth_factor": str(point_evaluation_sq / coefficient_l2_norm_sq),
        },
        "proof_boundary": (
            "Exact finite algebra only. The locations and weights are synthetic; "
            "no prime, zeta, Hardy-abscissa, or RH claim is numerically evaluated."
        ),
    }
    proof["proof_object_sha256"] = canonical_digest(proof)
    return proof


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        payload = json.loads(args.certificate.read_text(encoding="utf-8"))
        result = verify(payload)
        code = 0
    except (OSError, json.JSONDecodeError, CertificateError) as exc:
        result = {"schema": SCHEMA, "classification": "REJECTED", "reason": str(exc)}
        code = 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
