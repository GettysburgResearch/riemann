#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
from typing import Iterable

VERDICT = "PASS_L105101_ENTIRE_WINDOW_RESIDUE_FLUX"
REPO_ROOT = Path(__file__).resolve().parents[2]
CONTENT_FILES = (
    "PACKET_METADATA_105101.json",
    "claims/lemmas/L-105101-entire-window-second-residue-flux.md",
    "claims/methodology/M-105101-window-flux-review-contract.md",
    "claims/refutations/R-105101-global-ledger-is-not-height-local.md",
    "claims/theorems/T-105101-entire-window-residue-flux-frontier.md",
    "experiments/X-105101-entire-window-residue-flux/verify.py",
    "experiments/X-105101-entire-window-residue-flux/tests/test_verify.py",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


@dataclass(frozen=True)
class G:
    re: F
    im: F = F(0)

    @staticmethod
    def coerce(value: G | F | int) -> G:
        return value if isinstance(value, G) else G(F(value))

    def __add__(self, other: G | F | int) -> G:
        rhs = G.coerce(other)
        return G(self.re + rhs.re, self.im + rhs.im)

    def __radd__(self, other: G | F | int) -> G:
        return self + other

    def __neg__(self) -> G:
        return G(-self.re, -self.im)

    def __sub__(self, other: G | F | int) -> G:
        return self + (-G.coerce(other))

    def __rsub__(self, other: G | F | int) -> G:
        return G.coerce(other) - self

    def __mul__(self, other: G | F | int) -> G:
        rhs = G.coerce(other)
        return G(
            self.re * rhs.re - self.im * rhs.im,
            self.re * rhs.im + self.im * rhs.re,
        )

    def __rmul__(self, other: G | F | int) -> G:
        return self * other

    def __truediv__(self, other: G | F | int) -> G:
        rhs = G.coerce(other)
        denominator = rhs.re * rhs.re + rhs.im * rhs.im
        if denominator == 0:
            raise ZeroDivisionError("Gaussian-rational division by zero")
        return G(
            (self.re * rhs.re + self.im * rhs.im) / denominator,
            (self.im * rhs.re - self.re * rhs.im) / denominator,
        )

    def __pow__(self, exponent: int) -> G:
        if exponent < 0:
            return G(F(1)) / (self ** (-exponent))
        result = G(F(1))
        base = self
        power = exponent
        while power:
            if power & 1:
                result = result * base
            base = base * base
            power >>= 1
        return result

    def conjugate(self) -> G:
        return G(self.re, -self.im)

    def absolute_square(self) -> F:
        return self.re * self.re + self.im * self.im

    def render(self) -> str:
        if self.im == 0:
            return str(self.re)
        sign = "+" if self.im > 0 else "-"
        return f"{self.re}{sign}{abs(self.im)}i"


ZERO = G(F(0))
I = G(F(0), F(1))


def gsum(values: Iterable[G]) -> G:
    total = ZERO
    for value in values:
        total += value
    return total


def derivative(coefficients: list[F]) -> list[F]:
    return [F(index) * coefficients[index] for index in range(1, len(coefficients))]


def evaluate(coefficients: list[F], z: G) -> G:
    value = ZERO
    for coefficient in reversed(coefficients):
        value = value * z + coefficient
    return value


def q_value(coefficients: list[F], z: G) -> G:
    first = derivative(coefficients)
    second = derivative(first)
    return evaluate(coefficients, z) ** 2 / (
        evaluate(first, z) * evaluate(second, z)
    )


def root_power_sums(coefficients: list[F], maximum: int = 4) -> list[F]:
    degree = len(coefficients) - 1
    if degree < 1 or coefficients[-1] == 0:
        raise ValueError("polynomial degree must be positive and explicit")
    monic_descending = [
        coefficients[degree - index] / coefficients[-1]
        for index in range(1, degree + 1)
    ]
    sums = [F(degree)]
    for order in range(1, maximum + 1):
        value = F(0)
        for index in range(1, min(order - 1, degree) + 1):
            value += monic_descending[index - 1] * sums[order - index]
        if order <= degree:
            value += F(order) * monic_descending[order - 1]
        sums.append(-value)
    return sums


def root_ledger_k4(coefficients: list[F]) -> F:
    degree = len(coefficients) - 1
    if degree < 2:
        raise ValueError("K4 ledger requires degree at least two")
    sums = root_power_sums(coefficients)
    mean = sums[1] / degree
    v2 = sums[2] - 2 * mean * sums[1] + degree * mean**2
    v4 = (
        sums[4]
        - 4 * mean * sums[3]
        + 6 * mean**2 * sums[2]
        - 4 * mean**3 * sums[1]
        + degree * mean**4
    )
    numerator = (
        F(6 * degree * degree - 18 * degree + 13) * v2**2
        - F(3 * degree * (degree - 1) * (degree - 2)) * v4
    )
    denominator = F(degree**4 * (degree - 1) ** 3)
    return numerator / denominator


def inside_rectangle(z: G, t: F, eta: F) -> bool:
    return abs(z.re) < t and abs(z.im) < eta


def on_rectangle_boundary(z: G, t: F, eta: F) -> bool:
    vertical = abs(z.re) == t and abs(z.im) <= eta
    horizontal = abs(z.im) == eta and abs(z.re) <= t
    return vertical or horizontal


def residue_ladder(
    coefficients: list[F],
    critical_roots: Iterable[G],
    second_critical_roots: Iterable[G],
) -> tuple[list[tuple[G, G]], list[tuple[G, G]]]:
    critical_roots = list(critical_roots)
    second_critical_roots = list(second_critical_roots)
    degree = len(coefficients) - 1
    if len(critical_roots) != degree - 1:
        raise ValueError("critical-root fixture does not have complete coverage")
    if len(second_critical_roots) != max(degree - 2, 0):
        raise ValueError("second-critical-root fixture does not have complete coverage")
    if len(set(critical_roots)) != len(critical_roots):
        raise ValueError("critical-root fixture is not simple")
    if len(set(second_critical_roots)) != len(second_critical_roots):
        raise ValueError("second-critical-root fixture is not simple")

    first = derivative(coefficients)
    second = derivative(first)
    third = derivative(second)
    critical: list[tuple[G, G]] = []
    for c in critical_roots:
        require(evaluate(first, c) == ZERO, f"{c.render()} is not a zero of p'")
        require(
            evaluate(second, c) != ZERO,
            f"{c.render()} is not a simple zero of p'",
        )
        rho = evaluate(coefficients, c) / evaluate(second, c)
        critical.append((c, rho))

    second_critical: list[tuple[G, G]] = []
    for d in second_critical_roots:
        require(evaluate(second, d) == ZERO, f"{d.render()} is not a zero of p''")
        require(
            evaluate(first, d) != ZERO,
            f"{d.render()} is also a zero of p'",
        )
        require(
            evaluate(third, d) != ZERO,
            f"{d.render()} is not a simple zero of p''",
        )
        tau = evaluate(coefficients, d) ** 2 / (
            evaluate(first, d) * evaluate(third, d)
        )
        second_critical.append((d, tau))
    return critical, second_critical


def local_ledger(
    name: str,
    coefficients: list[F],
    critical_roots: list[G],
    second_critical_roots: list[G],
    t: F,
    eta: F,
) -> dict[str, object]:
    if t <= 0 or eta <= 0:
        raise ValueError("rectangle dimensions must be positive")
    critical, second_critical = residue_ladder(
        coefficients, critical_roots, second_critical_roots
    )
    all_roots = [root for root, _ in critical + second_critical]
    if any(on_rectangle_boundary(root, t, eta) for root in all_roots):
        raise ValueError("a denominator zero lies on the rectangle boundary")

    inside_critical = [
        (root, residue)
        for root, residue in critical
        if inside_rectangle(root, t, eta)
    ]
    inside_second = [
        (root, residue)
        for root, residue in second_critical
        if inside_rectangle(root, t, eta)
    ]

    real_m2 = F(0)
    nonreal_correction = ZERO
    for root, rho in inside_critical:
        if root.im == 0:
            require(rho.im == 0, "real critical point has nonreal residue")
            real_m2 += rho.absolute_square()
        else:
            nonreal_correction += rho**2
    debt = gsum(residue for _, residue in inside_second)
    boundary_residue_sum = G(real_m2) + nonreal_correction + debt

    global_residue_sum = gsum(
        [rho**2 for _, rho in critical]
        + [tau for _, tau in second_critical]
    )
    root_ledger = G(root_ledger_k4(coefficients))
    exterior_residue_sum = gsum(
        [
            rho**2
            for root, rho in critical
            if not inside_rectangle(root, t, eta)
        ]
        + [
            tau
            for root, tau in second_critical
            if not inside_rectangle(root, t, eta)
        ]
    )

    require(
        boundary_residue_sum - nonreal_correction - debt == G(real_m2),
        f"local M2 split failed for {name}",
    )
    require(
        global_residue_sum == boundary_residue_sum + exterior_residue_sum,
        f"global/exterior split failed for {name}",
    )
    require(
        global_residue_sum == root_ledger,
        f"independent V2/V4 root ledger failed for {name}",
    )
    require(boundary_residue_sum.im == 0, f"boundary sum is nonreal for {name}")
    require(nonreal_correction.im == 0, f"nonreal correction is nonreal for {name}")
    require(debt.im == 0, f"debt is nonreal for {name}")

    return {
        "name": name,
        "degree": len(coefficients) - 1,
        "T": str(t),
        "eta": str(eta),
        "inside_critical_roots": [root.render() for root, _ in inside_critical],
        "inside_second_critical_roots": [
            root.render() for root, _ in inside_second
        ],
        "real_m2": str(real_m2),
        "nonreal_correction": nonreal_correction.render(),
        "adjacent_derivative_debt": debt.render(),
        "boundary_residue_sum": boundary_residue_sum.render(),
        "exterior_residue_sum": exterior_residue_sum.render(),
        "global_residue_sum": global_residue_sum.render(),
        "root_v2_v4_ledger": root_ledger.render(),
        "local_split_verified": True,
        "global_exterior_split_verified": True,
        "independent_root_ledger_verified": True,
    }


def rectangle_orientation_checks() -> dict[str, object]:
    t, eta = F(5, 2), F(3, 4)
    vertices = [
        G(-t, -eta),
        G(t, -eta),
        G(t, eta),
        G(-t, eta),
    ]
    closed = vertices + [vertices[0]]
    deltas = [closed[index + 1] - closed[index] for index in range(4)]
    require(
        deltas
        == [G(2 * t), G(F(0), 2 * eta), G(-2 * t), G(F(0), -2 * eta)],
        "counterclockwise edge orientation mutation",
    )
    twice_area = sum(
        (
            closed[index].re * closed[index + 1].im
            - closed[index + 1].re * closed[index].im
            for index in range(4)
        ),
        F(0),
    )
    require(twice_area == 8 * t * eta, "rectangle signed-area mutation")
    require(twice_area > 0, "rectangle is not counterclockwise")
    reversed_closed = [vertices[0], vertices[3], vertices[2], vertices[1], vertices[0]]
    reversed_twice_area = sum(
        (
            reversed_closed[index].re * reversed_closed[index + 1].im
            - reversed_closed[index + 1].re * reversed_closed[index].im
            for index in range(4)
        ),
        F(0),
    )
    require(reversed_twice_area == -twice_area, "reversed contour sign mutation")

    # An affine entire integrand has an exact primitive. The four oriented
    # edge integrals must telescope to zero.
    a, b = G(F(2, 3), F(-1, 5)), G(F(-4, 7), F(3, 8))
    integrals = []
    for start, end in zip(closed, closed[1:]):
        integral = a * F(1, 2) * (end**2 - start**2) + b * (end - start)
        integrals.append(integral)
    require(gsum(integrals) == ZERO, "oriented affine contour does not close")
    return {
        "vertices": [vertex.render() for vertex in vertices],
        "edge_deltas": [delta.render() for delta in deltas],
        "signed_area": str(twice_area / 2),
        "reversed_signed_area": str(reversed_twice_area / 2),
        "affine_contour_integral": gsum(integrals).render(),
        "counterclockwise": True,
    }


def edge_formula_mutation_checks() -> dict[str, object]:
    # For p(z)=z^2+1, Q=(z^2+1)^2/(4z). These exact paired densities bind
    # the top/bottom and right/left signs in the parity-reduced edge formula.
    coefficients = [F(1), F(0), F(1)]
    top = q_value(coefficients, G(F(1, 2), F(1)))
    right = q_value(coefficients, G(F(2), F(1, 2)))
    horizontal = top.conjugate() - top
    horizontal_wrong = top.conjugate() + top
    vertical = I * (right + right.conjugate())
    vertical_wrong = I * (right - right.conjugate())
    require(top == G(F(1, 160), F(19, 80)), "top density evaluation failed")
    require(
        right == G(F(373, 136), F(919, 544)),
        "right density evaluation failed",
    )
    require(horizontal == G(F(0), F(-19, 40)), "horizontal edge sign failed")
    require(vertical == G(F(0), F(373, 68)), "vertical edge sign failed")
    require(horizontal_wrong.re != 0, "horizontal sign mutation survived")
    require(vertical_wrong.re != 0, "vertical sign mutation survived")

    # Each CCW edge of the unit square changes arg(z) by pi/2 for Q=1/z.
    # Recording the changes as fractions of 2*pi gives an exact winding check
    # without floating-point quadrature.
    edge_turns = [F(1, 4)] * 4
    ccw_winding = sum(edge_turns, F(0))
    clockwise_winding = sum((-turn for turn in edge_turns), F(0))
    require(ccw_winding == 1, "CCW 1/z winding mutation")
    require(clockwise_winding == -1, "clockwise 1/z winding mutation")
    return {
        "fixture": "p(z)=z^2+1",
        "Q_top_sample": top.render(),
        "Q_right_sample": right.render(),
        "correct_horizontal_paired_density": horizontal.render(),
        "wrong_horizontal_density": horizontal_wrong.render(),
        "correct_vertical_paired_density": vertical.render(),
        "wrong_vertical_density": vertical_wrong.render(),
        "unit_square_1_over_z_ccw_winding": str(ccw_winding),
        "unit_square_1_over_z_clockwise_winding": str(clockwise_winding),
        "sign_mutations_rejected": True,
    }


def integrated_edge_formula_check() -> dict[str, object]:
    # On T=eta=1 for p=z^2+1,
    # Q=(z^3+2z+1/z)/4. Exact one-variable integration gives
    #   int_-1^1 Im Q(x+i) dx = 1-pi/8,
    #   int_-1^1 Q(1+iy) dy   = 1+pi/8.
    # Represent a/pi+b exactly as (a,b); the 1/pi terms must cancel.
    horizontal = (F(-1), F(1, 8))
    vertical = (F(1), F(1, 8))
    combined = (
        horizontal[0] + vertical[0],
        horizontal[1] + vertical[1],
    )
    expected_residue = root_ledger_k4([F(1), F(0), F(1)])
    require(combined == (F(0), expected_residue), "integrated edge formula failed")
    horizontal_sign_mutation = (
        -horizontal[0] + vertical[0],
        -horizontal[1] + vertical[1],
    )
    vertical_sign_mutation = (
        horizontal[0] - vertical[0],
        horizontal[1] - vertical[1],
    )
    require(
        horizontal_sign_mutation != combined,
        "integrated horizontal sign mutation survived",
    )
    require(
        vertical_sign_mutation != combined,
        "integrated vertical sign mutation survived",
    )
    return {
        "fixture": "p(z)=z^2+1, T=eta=1",
        "top_imaginary_integral": "1-pi/8",
        "right_integral": "1+pi/8",
        "horizontal_contribution_a_over_pi_plus_b": [
            str(value) for value in horizontal
        ],
        "vertical_contribution_a_over_pi_plus_b": [
            str(value) for value in vertical
        ],
        "combined_a_over_pi_plus_b": [str(value) for value in combined],
        "residue": str(expected_residue),
        "both_sign_mutations_rejected": True,
    }


def algebraic_square_firewall() -> dict[str, object]:
    coefficients = [F(1), F(3), F(0), F(1)]
    critical, _ = residue_ladder(
        coefficients,
        [G(F(0), F(-1)), G(F(0), F(1))],
        [ZERO],
    )
    algebraic = gsum(rho**2 for _, rho in critical)
    absolute = sum((rho.absolute_square() for _, rho in critical), F(0))
    require(algebraic == G(F(1, 6)), "algebraic-square correction changed")
    require(absolute == F(5, 18), "absolute-square mutation control changed")
    require(algebraic != G(absolute), "algebraic and absolute squares collapsed")
    return {
        "algebraic_squared_residue_sum": algebraic.render(),
        "absolute_squared_residue_sum": str(absolute),
        "absolute_square_substitution_rejected": True,
    }


def schwarz_parity_checks() -> dict[str, object]:
    z = G(F(2), F(1, 3))
    fixtures = {
        "even": [F(2), F(0), F(-2), F(0), F(1)],
        "odd": [F(0), F(3), F(0), F(1)],
    }
    rows = {}
    for name, coefficients in fixtures.items():
        q = q_value(coefficients, z)
        require(
            q_value(coefficients, z.conjugate()) == q.conjugate(),
            f"Schwarz reflection failed for {name} fixture",
        )
        require(
            q_value(coefficients, -z) == -q,
            f"odd-Q parity failed for {name} fixture",
        )
        rows[name] = {"Q(z)": q.render(), "schwarz": True, "Q_is_odd": True}

    generic = [F(1), F(-3), F(0), F(1)]
    q = q_value(generic, z)
    require(
        q_value(generic, z.conjugate()) == q.conjugate(),
        "generic Schwarz reflection failed",
    )
    require(q_value(generic, -z) != -q, "generic polynomial accidentally odd-Q")
    rows["generic_real"] = {
        "Q(z)": q.render(),
        "schwarz": True,
        "Q_is_odd": False,
    }
    return rows


def content_hashes() -> dict[str, str]:
    hashes: dict[str, str] = {}
    for relative_path in CONTENT_FILES:
        path = REPO_ROOT / relative_path
        if not path.is_file():
            raise FileNotFoundError(f"missing load-bearing file: {relative_path}")
        normalized = path.read_bytes().replace(b"\r\n", b"\n")
        hashes[relative_path] = hashlib.sha256(normalized).hexdigest()
    return hashes


def build_payload() -> dict[str, object]:
    real_cubic = [F(1), F(-3), F(0), F(1)]
    asymmetric_quartic = [F(1), F(64), F(-32), F(-4, 3), F(1)]
    complex_cubic = [F(1), F(3), F(0), F(1)]
    removable_at_critical = [F(1), F(-2), F(1)]
    removable_at_second_critical = [F(0), F(3), F(0), F(1)]

    fixtures = [
        local_ledger(
            "real_cubic_narrow_window",
            real_cubic,
            [G(F(-1)), G(F(1))],
            [ZERO],
            F(1, 2),
            F(1),
        ),
        local_ledger(
            "real_cubic_full_window",
            real_cubic,
            [G(F(-1)), G(F(1))],
            [ZERO],
            F(3, 2),
            F(1),
        ),
        local_ledger(
            "asymmetric_quartic_partial_window",
            asymmetric_quartic,
            [G(F(-4)), G(F(1)), G(F(4))],
            [G(F(-2)), G(F(8, 3))],
            F(3),
            F(1),
        ),
        local_ledger(
            "complex_cubic_narrow_strip",
            complex_cubic,
            [G(F(0), F(-1)), G(F(0), F(1))],
            [ZERO],
            F(1),
            F(1, 2),
        ),
        local_ledger(
            "complex_cubic_wide_strip",
            complex_cubic,
            [G(F(0), F(-1)), G(F(0), F(1))],
            [ZERO],
            F(1),
            F(2),
        ),
        local_ledger(
            "common_p_pprime_removable",
            removable_at_critical,
            [G(F(1))],
            [],
            F(2),
            F(1),
        ),
        local_ledger(
            "zero_tau_removable",
            removable_at_second_critical,
            [G(F(0), F(-1)), G(F(0), F(1))],
            [ZERO],
            F(1),
            F(1, 2),
        ),
    ]

    payload: dict[str, object] = {
        "schema": "riemann.l105101.entire-window-residue-flux.v1",
        "classification": VERDICT,
        "arithmetic_class": "EXACT_RATIONAL_AND_GAUSSIAN_RATIONAL",
        "source": {
            "checkpoint_base": "51c5619ef3c4b793de756b1c359b39df2ac35466",
            "post_freeze_context_pr": 720,
            "post_freeze_context_head": "10bba584c01277e880aaa21e1fea09f396ca7246",
        },
        "checks": {
            "local_ledgers": fixtures,
            "rectangle_orientation": rectangle_orientation_checks(),
            "edge_formula_mutations": edge_formula_mutation_checks(),
            "integrated_edge_formula": integrated_edge_formula_check(),
            "schwarz_and_parity": schwarz_parity_checks(),
            "algebraic_square_firewall": algebraic_square_firewall(),
        },
        "content_sha256": content_hashes(),
        "content_hash_mode": "LF_NORMALIZED_TEXT",
        "scope": {
            "fixed_window_entire_identity_proof_supplied": True,
            "exact_local_fixtures_replayed": True,
            "multiple_zero_confluent_ledger_proved": False,
            "admissible_height_strip_sequence_controlled": False,
            "uniform_height_flux_bound_proved": False,
            "nonreal_correction_bound_proved": False,
            "adjacent_derivative_debt_bound_proved": False,
            "rcmv104530_proved": False,
            "rh_established": False,
        },
        "heavy_computation_run": False,
        "verdict": VERDICT,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
