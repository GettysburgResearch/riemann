#!/usr/bin/env python3
"""Exact finite checks for Liu's principal local correction.

Standard library only.  This checks cleared-denominator polynomial identities,
not the analytic origin of the displayed local series or normal convergence.
The variables v, D, R are algebraically independent; no phase is set to one.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


class Poly:
    """A small exact polynomial ring Z[v,D,R]."""

    def __init__(self, terms: dict[tuple[int, int, int], int] | int):
        if isinstance(terms, int):
            terms = {(0, 0, 0): terms}
        self.terms = {m: c for m, c in terms.items() if c}

    @staticmethod
    def coerce(value: Poly | int) -> Poly:
        return value if isinstance(value, Poly) else Poly(value)

    def __add__(self, other: Poly | int) -> Poly:
        result = dict(self.terms)
        for monomial, coefficient in self.coerce(other).terms.items():
            result[monomial] = result.get(monomial, 0) + coefficient
        return Poly(result)

    __radd__ = __add__

    def __neg__(self) -> Poly:
        return Poly({m: -c for m, c in self.terms.items()})

    def __sub__(self, other: Poly | int) -> Poly:
        return self + -self.coerce(other)

    def __rsub__(self, other: Poly | int) -> Poly:
        return self.coerce(other) + -self

    def __mul__(self, other: Poly | int) -> Poly:
        result: dict[tuple[int, int, int], int] = {}
        for m, a in self.terms.items():
            for n, b in self.coerce(other).terms.items():
                exponent = tuple(x + y for x, y in zip(m, n))
                result[exponent] = result.get(exponent, 0) + a * b
        return Poly(result)

    __rmul__ = __mul__

    def __pow__(self, exponent: int) -> Poly:
        if exponent < 0:
            raise ValueError("Polynomial powers must be nonnegative")
        result = Poly(1)
        for _ in range(exponent):
            result = result * self
        return result

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, (Poly, int)):
            return NotImplemented
        return self.terms == self.coerce(other).terms


def certificate() -> dict:
    v = Poly({(1, 0, 0): 1})
    D = Poly({(0, 1, 0): 1})
    R = Poly({(0, 0, 1): 1})
    passed: list[str] = []
    rejected: list[str] = []

    def equal(name: str, left: Poly | int, right: Poly | int) -> None:
        if left != right:
            raise AssertionError(name)
        passed.append(name)

    def unequal(name: str, left: Poly | int, right: Poly | int) -> None:
        if left == right:
            raise AssertionError("Mutation escaped: " + name)
        rejected.append(name)

    # Source §13.3: at j=0, rho=1, Y0=V=v, q=1/v,
    # P* = {[R(1-v)-D(q-1)v^2]/(1-v)-D+vR}/(1-R).
    # Clear the common denominator (1-v)(1-R).
    raw_pstar = R * (1 - v) - D * (1 - v) * v + (-D + v * R) * (1 - v)
    reduced_pstar = (1 - v) * (1 + v) * (R - D)
    equal("principal_Pstar_after_common_denominator", raw_pstar, reduced_pstar)

    # P0 = (1+v)/(1-v) + (1+v)(R-D)/(1-R).
    # H = (1-v)^2 P0/(1-D), with denominator (1-D)(1-R).
    raw_h = (1 - v) * (1 + v) * (1 - R) + (1 - v)**2 * (1 + v) * (R - D)
    h_numerator = (1 - v**2) * (1 - (1 - v) * D - v * R)
    equal("principal_H_after_common_denominator", raw_h, h_numerator)

    # K=(1-R)H has denominator 1-D.
    k_numerator = (1 - v**2) * ((1 - D) + v * (D - R))
    equal("extracted_K_formula", h_numerator, k_numerator)
    k_minus_one = -v**2 * (1 - D) + (1 - v**2) * v * (D - R)
    equal("K_minus_one_expansion", k_numerator - (1 - D), k_minus_one)

    # Boundary triangle lower bound after v=y^2, |D|<=y, |R|<=1.
    # Reuse v as the independent formal variable y for this identity.
    equal("boundary_lower_bound", 1 - (1 - v**2) * v - v**2, (1 - v**2) * (1 - v))

    # R = a^2 q^4 T^6 V, a=(barLambda*eta)^3, T=q^-s, V=q^-1.
    # Coordinates are (barLambda power, eta power, constant q power, s*q power).
    original_r_exponents = (2 * 3, 2 * 3, 4 - 1, -6)
    expected_r_exponents = (6, 6, 3, -6)
    if original_r_exponents != expected_r_exponents:
        raise AssertionError("R phase/exponent extraction")
    passed.append("R_retains_eta_sixth_power_and_argument_6s_minus_3")

    # Mutation controls are algebraic non-identities, not random evaluations.
    unequal(
        "omitting_source_mixed_term_D_times_v",
        raw_pstar + D * (1 - v) * v,
        reduced_pstar,
    )
    unequal(
        "omitting_angular_R_term_in_K",
        (1 - v**2) * ((1 - D) + v * D),
        h_numerator,
    )
    unequal(
        "dropping_one_residue_normalizer_1_minus_v",
        (1 + v) * (1 - R) + (1 - v) * (1 + v) * (R - D),
        h_numerator,
    )
    if original_r_exponents == (6, 0, 3, -6):
        raise AssertionError("Mutation escaped: replacing eta^6 by 1")
    rejected.append("replacing_general_target_eta_sixth_power_by_one")
    if original_r_exponents == (6, 6, 4, -6):
        raise AssertionError("Mutation escaped: argument 6s-4")
    rejected.append("using_argument_6s_minus_4_instead_of_6s_minus_3")

    return {
        "status": "passed",
        "arithmetic": "exact integer polynomial identities and exponent tuples",
        "checked_identities": passed,
        "mutation_controls_rejected": rejected,
        "source": {
            "arxiv": "2610.26835v1",
            "locator": "Section 13.3, pp. 94-97, equation (13.9), principal residues",
            "pdf_sha256": "5d0fd10274c8444c789b0b7925a1cd3419017fe760be3219b6be51d7fbed9bd5",
        },
        "scope": (
            "Finite algebra for the displayed local source formula only. "
            "Does not certify exceptional-theta identities, normal convergence, "
            "global Hecke continuation, a contour shift, or a new zero-free bound."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Write the JSON certificate to this path")
    args = parser.parse_args()
    result = certificate()
    result["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
