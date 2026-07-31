#!/usr/bin/env python3
"""Produce an exact rational RH-valid envelope for the finite filter.

This checker intentionally does *not* use a numerical zero table.  Conditional
on RH and the smoothed explicit formula normalization in T-15404, it combines
the published cumulative zero-count estimate of Hasanalizade--Shen--Wong with
elementary transform envelopes.  The resulting bound is coarse but fail-closed.

The cited estimate implies N(T) < 4 T log(T) for T >= e.  Here is the coarse
derivation, included so that the simplification is auditable.  Write
u=log(T)>=1 and discard the negative part of the main term.  Since 2*pi>6,
log(u)<=u, and e>65/24,

    N(T) < T*u/6 + (0.1038 + 0.2573 + 9.3675)*u
         < T*u/6 + 23*T*u/6 = 4*T*u.

The last strict inequality follows from 9.7286 < (23/6)*(65/24).  On dyadic
endpoints this gives the exact integer cumulative majorant

    N(2**b) <= 4*b*2**b.

We deliberately use this cumulative count in every block; no illegal
difference of two upper bounds occurs.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

from filter_core import Q, FilterSpec, qtext, standard_spec


ZERO_COUNT_CITATION = {
    "authors": "E. Hasanalizade, Q. Shen, P.-J. Wong",
    "title": "Counting zeros of the Riemann zeta function",
    "journal": "Journal of Number Theory 235 (2022), 219-241",
    "doi": "10.1016/j.jnt.2021.06.032",
    "arxiv": "https://arxiv.org/abs/2107.06506",
}


def _fingerprint(value: Q) -> dict[str, object]:
    raw = qtext(value)
    return {
        "decimal": float(value),
        "sha256": hashlib.sha256(raw.encode("ascii")).hexdigest(),
        "numerator_digits": len(str(value.numerator)),
        "denominator_digits": len(str(value.denominator)),
    }


def _decimal_ceiling(value: Q, digits: int = 60) -> Q:
    """Return a compact exact decimal rational greater than or equal to value."""
    denominator = 10**digits
    numerator = (value.numerator * denominator + value.denominator - 1) // value.denominator
    return Q(numerator, denominator)


def _box_envelope(spec: FilterSpec, left: int) -> Q:
    value = Q(1)
    for width in spec.widths:
        value *= min(Q(1), Q(2, width * left)) ** 2
    return value


def _all_boxes_active_index(spec: FilterSpec) -> int:
    j = 2
    while any(width * (1 << j) < 2 for width in spec.widths):
        j += 1
    return j


def zero_sum_bound(spec: FilterSpec) -> tuple[Q, dict[str, object]]:
    """Bound the complete nontrivial-zero sum by an exact rational."""
    m = spec.highpass_order
    delta = spec.highpass_delta

    # First positive-ordinate block 0 < gamma <= 4.  HSW gives N(4) < 32.
    first_envelope = Q(3) * min(Q(1), 2 * delta) ** m
    first = Q(2 * 32) * first_envelope  # conjugate ordinates

    tail_start = _all_boxes_active_index(spec)
    finite_blocks: list[dict[str, object]] = []
    finite_total = Q(0)
    for j in range(2, tail_start):
        left = 1 << j
        right = 1 << (j + 1)
        # N(right) <= 4*(j+1)*right.  This is cumulative on purpose.
        count = 4 * (j + 1) * right
        highpass = min(Q(1), delta * left) ** m
        transform = Q(3) * highpass * _box_envelope(spec, left)
        contribution = Q(2 * count) * transform
        finite_total += contribution
        finite_blocks.append(
            {
                "j": j,
                "positive_ordinate_block": [left, right],
                "cumulative_count_majorant": count,
                "transform_envelope": qtext(transform),
                "contribution": qtext(contribution),
                "contribution_decimal": float(contribution),
            }
        )

    # For every j >= tail_start all box bounds are 2/(r*2**j).
    d = len(spec.widths)
    box_constant = Q(1)
    for width in spec.widths:
        box_constant *= Q(2, width) ** 2
    ratio = Q(2) ** (1 - 2 * d)
    j0 = tail_start
    # contribution_j = 48*C*(j+1)*ratio**j
    linear_geometric_sum = (
        ratio**j0 * (Q(j0 + 1) - Q(j0) * ratio) / (1 - ratio) ** 2
    )
    infinite_tail = Q(48) * box_constant * linear_geometric_sum

    total = first + finite_total + infinite_tail
    details: dict[str, object] = {
        "first_block_0_to_4": {
            "positive_count_majorant": 32,
            "contribution": qtext(first),
            "contribution_decimal": float(first),
        },
        "finite_blocks": finite_blocks,
        "tail_start_dyadic_index": tail_start,
        "tail_ratio": qtext(ratio),
        "infinite_tail": qtext(infinite_tail),
        "infinite_tail_decimal": float(infinite_tail),
        "total": qtext(total),
        "total_decimal": float(total),
    }
    return total, details


def _trivial_tail_start(spec: FilterSpec) -> int:
    """Choose K so all algebraic tail factors are active for k > K."""
    k = 1
    while True:
        lam = Q(4 * (k + 1) + 1, 2)  # lambda_(k+1)
        boxes_active = all(width * lam >= 1 for width in spec.widths)
        hp_active = spec.highpass_order == 0 or spec.highpass_delta * lam >= 1
        if boxes_active and hp_active:
            return k
        k += 1


def trivial_zero_bound(spec: FilterSpec) -> tuple[Q, dict[str, object]]:
    """Uniformly bound all trivial-zero terms for x >= max supp(G)."""
    d = len(spec.widths)
    m = spec.highpass_order
    delta = spec.highpass_delta
    k0 = _trivial_tail_start(spec)
    finite = Q(0)
    for k in range(1, k0 + 1):
        lam = Q(4 * k + 1, 2)  # 2k+1/2
        value = min(Q(1), delta * lam) ** m
        for width in spec.widths:
            value *= min(Q(1), Q(1, width * lam)) ** 2
        finite += value

    product_width_sq = Q(1)
    for width in spec.widths:
        product_width_sq *= width * width
    # sum_{k>k0} (2k)^(-2d) <= 2^(-2d) int_k0^inf x^(-2d) dx
    tail = (
        Q(1, product_width_sq)
        * Q(1, 1 << (2 * d))
        * Q(1, (2 * d - 1) * (k0 ** (2 * d - 1)))
    )
    total = Q(1, 1 << (m - 1)) * (finite + tail) if m >= 1 else Q(2) * (finite + tail)
    details: dict[str, object] = {
        "finite_last_index": k0,
        "finite_reduced_sum_fingerprint": _fingerprint(finite),
        "tail_reduced_sum_fingerprint": _fingerprint(tail),
        "pole_and_highpass_prefactor": qtext(Q(1, 1 << (m - 1)) if m >= 1 else Q(2)),
        "total_fingerprint": _fingerprint(total),
    }
    return total, details


def certificate(spec: FilterSpec) -> dict[str, object]:
    zeros, zero_details = zero_sum_bound(spec)
    trivial, trivial_details = trivial_zero_bound(spec)
    internal_total = zeros + trivial
    total = _decimal_ceiling(internal_total)
    support = spec.support_max_interval(96)
    return {
        "classification": "EXACT_RATIONAL_RH_BOUND_CONDITIONAL_ON_T15404_NORMALIZATION",
        "filter": {
            "widths": [qtext(w) for w in spec.widths],
            "base_shift": qtext(spec.base_shift),
            "highpass_delta": qtext(spec.highpass_delta),
            "highpass_order": spec.highpass_order,
            "profile_support_cost": qtext(spec.profile_length),
            "convolution_square_support_cost": qtext(2 * spec.profile_length),
            "support_max_formula": "base_shift + 2*sum(widths) + log(4) + order*delta",
            "support_max_interval": [qtext(support[0]), qtext(support[1])],
            "support_max_decimal": [float(support[0]), float(support[1])],
        },
        "zero_count_source": ZERO_COUNT_CITATION,
        "derived_count_majorant": "N(T) < 4*T*log(T), T>=e; N(2^b) <= 4*b*2^b",
        "nontrivial_zero_bound": zero_details,
        "trivial_zero_bound": trivial_details,
        "B_G": {
            "numerator": str(total.numerator),
            "denominator": str(total.denominator),
            "fraction": qtext(total),
            "decimal": float(total),
            "rounding": "upward decimal ceiling with denominator at most 10^60",
        },
        "internal_exact_sum_fingerprint": _fingerprint(internal_total),
        "validity": (
            "If RH holds, the T-15404 smoothed explicit-formula normalization is "
            "valid, and that formula is extended to this compact C^18 finite spline, "
            "then |Q_G(x)| <= B_G for every x at or beyond the displayed support "
            "threshold. No numerical zero ordinate is used."
        ),
        "proof_boundary": (
            "The rational arithmetic is exact. Publication/source review of the HSW "
            "zero-count estimate, independent review of T-15404, and the finite-C^18-"
            "spline explicit-formula extension remain external analytic dependencies; "
            "repository claim status therefore remains PROPOSED."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dyadic-level", type=int, default=8)
    parser.add_argument("--notches", type=int, default=2)
    parser.add_argument("--highpass-order", type=int, default=8)
    parser.add_argument("--highpass-delta-power", type=int, default=7)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    spec = standard_spec(
        dyadic_level=args.dyadic_level,
        notch_count=args.notches,
        highpass_order=args.highpass_order,
        highpass_delta=Q(1, 1 << args.highpass_delta_power),
    )
    result = certificate(spec)
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
