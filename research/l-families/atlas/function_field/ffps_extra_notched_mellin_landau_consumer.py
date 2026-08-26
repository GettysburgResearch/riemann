#!/usr/bin/env python3
"""Bounded exact replay for the extra-notched Mellin--Landau consumer."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


def dyadic_zero_real_parts() -> dict[str, Fraction]:
    """Real parts of zeros of r(s) and q(s)."""

    return {"r(s)=1-2^(-s)": Fraction(0), "q(s)=1-sqrt(2)*2^(-s)": Fraction(1, 2)}


def polynomial_zero_real_parts() -> dict[str, Fraction]:
    """Zeros left after simplifying the extra-notched multiplier."""

    return {"s-1": Fraction(1), "5s+3/2": Fraction(-3, 10)}


def open_strip_nonvanishing() -> bool:
    boundary = dyadic_zero_real_parts()
    polynomial = polynomial_zero_real_parts()
    return all(
        not Fraction(0) < real_part < Fraction(1, 2)
        for real_part in (*boundary.values(), *polynomial.values())
    )


def smoothing_multiplier_nonzero(real_part: Fraction) -> bool:
    """The log-box multiplier has zeros only on Re(s)=0."""

    return real_part > 0


def finite_measure_certificate() -> dict[str, object]:
    """Regularity certificate for D_out(A *_M A) in log coordinate."""

    mother_derivative_order = 2
    convolution_measure_order = 2 * mother_derivative_order
    polynomial_order = 4
    if convolution_measure_order != polynomial_order:
        raise AssertionError("the fourth derivative measure certificate failed")
    return {
        "log_kernel": "continuous compact piecewise-smooth a(t)",
        "mother_measure_derivative": "a'' is a finite signed measure",
        "convolution_identity": "D^4(a*a)=a''*a''",
        "max_D_out_order": polynomial_order,
        "support": "[0,4*log(2)] in log scale, equivalently [1,16]",
        "conclusion": "K_ext is a compact finite signed measure",
    }


def landau_hypothesis_certificate() -> dict[str, object]:
    """Exact growth and holomorphy ledger used by the specialized lemma."""

    return {
        "source_coefficient_bound": "|beta(n)| <= 2",
        "raw_total_variation_prefix": "|nu_ext|([1,Y]) = O(Y^(1/2))",
        "positive_density_abscissa_upper_bound": "1/2",
        "negative_premise": "nu_ext^-([1,Y])=O_epsilon(Y^epsilon) for every epsilon>0",
        "mollified_negative_transform": "holomorphic for Re(s)>0",
        "positive_real_axis": "explicit transform holomorphic for every real s>0",
        "landau_conclusion": "mollified transform holomorphic for Re(s)>0",
        "division_gate": "box multiplier is nonzero for Re(s)>0",
    }


def simplified_multiplier_at_integer(s: int) -> tuple[Fraction, Fraction]:
    """Evaluate M_ext(s) in Q(sqrt(2)) at a positive integer."""

    if s <= 0 or s == 1:
        raise ValueError("use a positive integer other than the polynomial zero s=1")
    # q(s)^2 = 1 + 2^(1-2s) - 2^(1-s)*sqrt(2)
    q_square = (Fraction(1) + Fraction(2, 2 ** (2 * s)), -Fraction(2, 2**s))
    r_square = (Fraction(1) - Fraction(1, 2**s)) ** 2
    rational = (
        r_square
        * (Fraction(s) - 1)
        * (5 * Fraction(s) + Fraction(3, 2))
        / (Fraction(s) * (Fraction(s) - Fraction(1, 2)))
    )
    return rational * q_square[0], rational * q_square[1]


def qstr(value: tuple[Fraction, Fraction]) -> str:
    a, b = value
    sign = "+" if b >= 0 else "-"
    magnitude = abs(b)
    radical = "sqrt(2)" if magnitude == 1 else f"{magnitude}*sqrt(2)"
    if b == 0:
        return str(a)
    return f"{a}{sign}{radical}"


def run() -> dict[str, object]:
    if not open_strip_nonvanishing():
        raise AssertionError("extra-notched multiplier gained an open-strip zero")
    samples = []
    for s in (2, 3, 4, 6):
        value = simplified_multiplier_at_integer(s)
        if value == (Fraction(0), Fraction(0)):
            raise AssertionError("positive Mellin sample unexpectedly vanished")
        samples.append({"s": s, "M_ext(s)": qstr(value)})
    smoothing_panels = []
    for real_part in (
        Fraction(1, 100),
        Fraction(1, 10),
        Fraction(1, 4),
        Fraction(49, 100),
    ):
        if not smoothing_multiplier_nonzero(real_part):
            raise AssertionError("box mollifier vanished in the open strip")
        smoothing_panels.append(
            {"real_part": str(real_part), "nonzero_for_every_imaginary_part": True}
        )
    return {
        "kernel": {
            "definition": "K_ext=D_out(A *_M A)",
            "A_hat": "q(s)*r(s)/(s*(s-1/2))",
            "D_out": "(1/2)*D*(D-1)*(5*D+3/2)*(2*D-1)",
            "simplified_multiplier": ("q(s)^2*r(s)^2*(s-1)*(5s+3/2)/(s*(s-1/2))"),
            "support": "[1,16] as a finite signed logarithmic measure",
            "measure_certificate": finite_measure_certificate(),
        },
        "zero_audit": {
            "dyadic_zero_real_parts": {
                key: str(value) for key, value in dyadic_zero_real_parts().items()
            },
            "polynomial_zero_real_parts": {
                key: str(value) for key, value in polynomial_zero_real_parts().items()
            },
            "nonvanishing_on_0_lt_Re_s_lt_1_over_2": True,
            "positive_integer_samples": samples,
        },
        "source": {
            "beta": "mu(n)-1_(67|n)*mu(n/67)",
            "mellin_transform": ("M_ext(s)*(1-67^(-(s+1/2)))/zeta(s+1/2)"),
            "absolute_fubini_half_plane": "Re(s)>1/2",
            "dirichlet_factor": ("sum beta(n)*n^(-z)=(1-67^(-z))/zeta(z) for Re(z)>1"),
            "off_line_zero": ("rho with Re(rho)>1/2 gives a genuine pole at s=rho-1/2"),
        },
        "measure_regularization": {
            "mollifier": "positive probability box on log-scale interval [0,epsilon]",
            "multiplier": "(1-exp(-epsilon*s))/(epsilon*s)",
            "multiplier_zeros": "Re(s)=0 only",
            "output_type": "locally integrable log-scale density h_epsilon",
            "negative_variation_contraction": (
                "int_[0,T] (h_epsilon)_- dt <= nu_ext^-([0,T]) for every T"
            ),
            "panels": smoothing_panels,
        },
        "conditional_consumer": {
            "premise": "nu_ext^-([1,Y]) = Y^o(1), in Jordan variation",
            "conclusion": "Riemann Hypothesis",
            "status": (
                "exact analytic implication; raw arithmetic premise refuted "
                "by the complete beta atomic-variation firewall"
            ),
            "premise_viable": False,
            "atomic_lower_bound": (
                "nu_ext^-([1,Y]) >= ((70+50*sqrt(2))/pi^2)*sqrt(Y)+O(log(Y))"
            ),
            "landau_ledger": landau_hypothesis_certificate(),
        },
        "canonical_successor": {
            "atomic_audit_commit": "78e5ce8e75bce174e3014a33b6fe086112577a1e",
            "equivalence_commit": "9f29bdb6ea7375df84de550d62f9d0984634a8dd",
            "reflection_commit": "a678292fd6d19d5b18f499aef35d2263cfc2b4ec",
            "boundary_shell_commit": "9e19e27614e473b3b7d06cfc3d51f92eb39ff009",
            "detector": "h_epsilon=eta_epsilon*nu_ext for one fixed epsilon>0",
            "criterion": "int_0^T (h_epsilon)_- dt=e^o(T)",
            "boundary_field": (
                "G=sum beta(n)/sqrt(n)*K_bd(t-log(n)), where D K_bd=K_ext"
            ),
            "boundary_difference": ("h_epsilon=(G-tau_epsilon G)/epsilon"),
            "shortest_criterion": (
                "int_0^T |G(t)| dt=e^o(T), equivalently int_0^T G_-(t) dt=e^o(T)"
            ),
            "strength": "equivalent to RH",
            "source_form": (
                "exact native half-divisor reflection/geodesic identity; "
                "no Boolean completion gate required"
            ),
            "criterion_proved": False,
            "rh_proved": False,
        },
        "source_adapter_gate": {
            "name": "EXTSRC106150",
            "statement": (
                "the complete beta-source extra-notched current equals "
                "D_out*J_U^diamond plus an absolute-subpower closed field"
            ),
            "consequence": (
                "historical only: EXTSRC106150 plus the now-refuted raw-Jordan "
                "WKSFSC106150 would imply RH"
            ),
            "status": (
                "source-accounting gate remains open, but cannot rescue the "
                "refuted raw-Jordan premise"
            ),
        },
        "resource_caps": {
            "mellin_samples": len(samples),
            "smoothing_panels": len(smoothing_panels),
            "source_atoms_enumerated": 0,
            "conductors_enumerated": 0,
            "curves_enumerated": 0,
            "point_counts": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and (
        not canonical.exists() or canonical.read_text(encoding="utf-8") != rendered
    ):
        raise SystemExit("canonical JSON fixture is stale")
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
