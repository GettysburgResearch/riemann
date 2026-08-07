#!/usr/bin/env python3
"""Exact checker for the Jordan, archimedean, and boundary-trace algebra."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x15412-jordan-arch-boundary.synthetic.v1"


class CertificateError(ValueError):
    pass


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value, 10)
        except ValueError as exc:
            raise CertificateError(f"{name} is not a decimal integer") from exc
    raise CertificateError(f"{name} must be an integer or decimal string")


def frac(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    n = integer(value.get("numerator"), f"{name}.numerator")
    d = integer(value.get("denominator"), f"{name}.denominator")
    if d <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(n, d)


def fj(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def divisors(n: int) -> list[int]:
    if n <= 0:
        raise CertificateError("parent integers must be positive")
    out: list[int] = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
        d += 1
    return sorted(out)


def phi(n: int) -> int:
    result = n
    p = 2
    m = n
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            result -= result // p
        p += 1
    if m > 1:
        result -= result // m
    return result


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")

    # Exact omega=1/2 specialization: J_1 = Euler phi.
    jordan = data.get("jordan")
    if not isinstance(jordan, dict):
        raise CertificateError("jordan must be an object")
    omega = frac(jordan.get("omega"), "jordan.omega")
    if omega != Fraction(1, 2):
        raise CertificateError("this exact regression requires omega=1/2")
    raw_parents = jordan.get("parents")
    if not isinstance(raw_parents, list) or not raw_parents:
        raise CertificateError("jordan.parents must be a nonempty list")
    seen: set[int] = set()
    norm_parent = Fraction(0)
    norm_fiber = Fraction(0)
    jordan_rows: list[dict[str, Any]] = []
    for i, item in enumerate(raw_parents):
        if not isinstance(item, dict):
            raise CertificateError(f"jordan.parents[{i}] must be an object")
        n = integer(item.get("n"), f"jordan.parents[{i}].n")
        if n in seen:
            raise CertificateError("duplicate parent integer")
        seen.add(n)
        amp = frac(item.get("amplitude"), f"jordan.parents[{i}].amplitude")
        dlist = divisors(n)
        jordan_sum = sum(phi(d) for d in dlist)
        if jordan_sum != n:
            raise CertificateError(f"Jordan normalization failed at n={n}")
        contribution = amp * amp
        fiber_contribution = contribution * Fraction(jordan_sum, n)
        norm_parent += contribution
        norm_fiber += fiber_contribution
        jordan_rows.append({
            "n": n,
            "amplitude": fj(amp),
            "sum_phi_divisors": str(jordan_sum),
            "fiber_weight_sum": fj(Fraction(jordan_sum, n)),
        })
    if norm_parent != norm_fiber:
        raise CertificateError("Stinespring norm identity failed")
    claimed_norm = frac(jordan.get("claimed_norm_squared"), "jordan.claimed_norm_squared")
    if claimed_norm != norm_parent:
        raise CertificateError("claimed Jordan norm mismatch")

    conditional = jordan.get("conditional")
    if not isinstance(conditional, dict):
        raise CertificateError("jordan.conditional must be an object")
    n0 = integer(conditional.get("n"), "jordan.conditional.n")
    raw_values = conditional.get("values")
    if not isinstance(raw_values, dict):
        raise CertificateError("jordan.conditional.values must be an object")
    d0 = divisors(n0)
    if set(raw_values) != {str(d) for d in d0}:
        raise CertificateError("conditional values must cover every divisor exactly")
    values = {d: frac(raw_values[str(d)], f"conditional.values[{d}]") for d in d0}
    probabilities = {d: Fraction(phi(d), n0) for d in d0}
    if sum(probabilities.values(), Fraction(0)) != 1:
        raise CertificateError("conditional probabilities do not sum to one")
    mean = sum(probabilities[d] * values[d] for d in d0)
    second = sum(probabilities[d] * values[d] * values[d] for d in d0)
    variance = second - mean * mean
    pair_variance = Fraction(1, 2) * sum(
        probabilities[d] * probabilities[e] * (values[d] - values[e]) ** 2
        for d in d0 for e in d0
    )
    if variance != pair_variance or variance < 0:
        raise CertificateError("Jordan carré-du-champ identity failed")
    for key, actual in (("mean", mean), ("second_moment", second), ("variance", variance)):
        supplied = frac(conditional.get(f"claimed_{key}"), f"conditional.claimed_{key}")
        if supplied != actual:
            raise CertificateError(f"claimed conditional {key} mismatch")

    arch = data.get("archimedean")
    if not isinstance(arch, dict):
        raise CertificateError("archimedean must be an object")
    omega_a = frac(arch.get("omega"), "archimedean.omega")
    u = frac(arch.get("u"), "archimedean.u")
    B = frac(arch.get("beta_channel_moment"), "archimedean.beta_channel_moment")
    if omega_a <= 0 or B <= 0 or u + omega_a - 1 <= 0:
        raise CertificateError("invalid archimedean parameters")
    v = 2 * omega_a * B / (u + omega_a - 1)
    g = B - v
    ell = B + v
    kappa = g / ell
    if abs(kappa) > 1:
        raise CertificateError("archimedean score is not contractive")
    for key, actual in (("volterra_channel_moment", v), ("signed_moment", g),
                        ("positive_majorant_moment", ell), ("score", kappa)):
        supplied = frac(arch.get(f"claimed_{key}"), f"archimedean.claimed_{key}")
        if supplied != actual:
            raise CertificateError(f"claimed archimedean {key} mismatch")

    boundary_arch = data.get("boundary_archimedean")
    if not isinstance(boundary_arch, dict):
        raise CertificateError("boundary_archimedean must be an object")
    omega_b = frac(boundary_arch.get("omega"), "boundary_archimedean.omega")
    B0 = frac(boundary_arch.get("B0"), "boundary_archimedean.B0")
    if omega_b <= 0 or B0 <= 0:
        raise CertificateError("invalid boundary archimedean parameters")
    b0 = B0
    v0 = B0
    g0 = Fraction(0)
    ell0 = 2 * B0
    slope = B0 / (2 * omega_b)
    for key, actual in (("b0", b0), ("v0", v0), ("g0", g0),
                        ("ell0", ell0), ("signed_zero_slope", slope)):
        supplied = frac(boundary_arch.get(f"claimed_{key}"), f"boundary_archimedean.claimed_{key}")
        if supplied != actual:
            raise CertificateError(f"claimed boundary archimedean {key} mismatch")

    boundary = data.get("cauchy_boundary")
    if not isinstance(boundary, dict):
        raise CertificateError("cauchy_boundary must be an object")
    z = frac(boundary.get("z"), "cauchy_boundary.z")
    w = frac(boundary.get("w"), "cauchy_boundary.w")
    if z <= 0 or w <= 0:
        raise CertificateError("Cauchy parameters must be positive")
    cauchy = 1 / (z + w)
    left_derivative = w * cauchy
    right_derivative = z * cauchy
    endpoint = left_derivative + right_derivative
    if endpoint != 1:
        raise CertificateError("Cauchy derivative/endpoint identity failed")
    for key, actual in (("cauchy_gram", cauchy), ("left_derivative", left_derivative),
                        ("right_derivative", right_derivative), ("endpoint_trace", endpoint)):
        supplied = frac(boundary.get(f"claimed_{key}"), f"cauchy_boundary.claimed_{key}")
        if supplied != actual:
            raise CertificateError(f"claimed Cauchy {key} mismatch")

    pole = data.get("pole_zero")
    if not isinstance(pole, dict):
        raise CertificateError("pole_zero must be an object")
    residue = frac(pole.get("arithmetic_residue"), "pole_zero.arithmetic_residue")
    omega_p = frac(pole.get("omega"), "pole_zero.omega")
    Bp = frac(pole.get("B0"), "pole_zero.B0")
    if residue <= 0 or omega_p <= 0 or Bp <= 0:
        raise CertificateError("invalid pole-zero parameters")
    signed_limit = residue * Bp / (2 * omega_p)
    positive_majorant_pole_coeff = 2 * residue * Bp
    polarized_boundary_coeff = signed_limit
    for key, actual in (("signed_limit", signed_limit),
                        ("positive_majorant_pole_coefficient", positive_majorant_pole_coeff),
                        ("polarized_boundary_coefficient", polarized_boundary_coeff)):
        supplied = frac(pole.get(f"claimed_{key}"), f"pole_zero.claimed_{key}")
        if supplied != actual:
            raise CertificateError(f"claimed pole-zero {key} mismatch")

    return {
        "schema": SCHEMA,
        "status": "EXACT_JORDAN_ARCHIMEDEAN_BOUNDARY_ALGEBRA",
        "jordan": {
            "rows": jordan_rows,
            "norm_squared": fj(norm_parent),
            "conditional_mean": fj(mean),
            "conditional_second_moment": fj(second),
            "conditional_variance": fj(variance),
            "pair_carre_du_champ": fj(pair_variance),
        },
        "archimedean": {
            "beta_channel_moment": fj(B),
            "volterra_channel_moment": fj(v),
            "signed_moment": fj(g),
            "positive_majorant_moment": fj(ell),
            "score": fj(kappa),
            "boundary_signed_zero_slope": fj(slope),
        },
        "cauchy_boundary": {
            "gram": fj(cauchy),
            "left_derivative": fj(left_derivative),
            "right_derivative": fj(right_derivative),
            "endpoint_trace": fj(endpoint),
        },
        "pole_zero": {
            "signed_limit": fj(signed_limit),
            "positive_majorant_pole_coefficient": fj(positive_majorant_pole_coeff),
            "polarized_boundary_coefficient": fj(polarized_boundary_coeff),
        },
        "proof_boundary": (
            "exact finite rational algebra only; the regularized full-Phi "
            "Mellin/Volterra metric identity is not certified"
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("certificate root must be an object")
        result = verify(data)
    except (OSError, json.JSONDecodeError, CertificateError) as exc:
        print(f"ERROR: {exc}")
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
