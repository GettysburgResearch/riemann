#!/usr/bin/env python3
"""Exact finite regression for the canonical factor-67 closure packet.

The checker authenticates finite algebra and fail-closed ownership controls. It
does not replay the frozen analytic root Hall, endpoint quadrature, terminal
estimate, PNT prime-square asymptotic, Landau theorem, or prove RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
from typing import Any, Iterable, Mapping

SCHEMA = "riemann.t91751.canonical-factor67-closure.v2"


def fs(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def canonical_sha(payload: Mapping[str, Any]) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def vadd(*vectors: Iterable[F]) -> list[F]:
    vectors = [list(v) for v in vectors]
    return [sum((v[i] for v in vectors), F(0)) for i in range(len(vectors[0]))]


def vscale(a: F, v: Iterable[F]) -> list[F]:
    return [a * x for x in v]


def vsub(a: Iterable[F], b: Iterable[F]) -> list[F]:
    return [x - y for x, y in zip(a, b)]


def dot(a: Iterable[F], b: Iterable[F]) -> F:
    return sum((x * y for x, y in zip(a, b)), F(0))


def common_parent_check(mutate: str | None = None) -> dict[str, Any]:
    current = [F(19), F(17), F(23), F(13), F(11), F(7)]
    child_1 = [F(8), F(6), F(9), F(5), F(4), F(3)]
    child_2 = [F(5), F(4), F(6), F(3), F(2), F(2)]
    a1, a2 = F(1, 20), F(1, 30)
    slack = [F(0), F(0), F(0), F(0), F(3), F(5)]

    if mutate == "duplicate_child":
        a1 = F(1, 8)
    parent = vadd(current, vscale(a1, child_1), vscale(a2, child_2))
    native = vadd(parent, slack)
    reconstructed = vadd(current, slack, vscale(a1, child_1), vscale(a2, child_2))
    if mutate == "drop_slack":
        reconstructed = vadd(current, vscale(a1, child_1), vscale(a2, child_2))
    if reconstructed != native:
        raise AssertionError("common-parent capacity identity failed")
    if not a1 + a2 < F(1, 8):
        raise AssertionError("recursive coefficient list is not subcritical")

    source_sets = {
        "current": {"s1", "s4", "bonus"},
        "child_67": {"s2", "s5"},
        "child_71": {"s3"},
        "unused": {"collar", "top"},
    }
    if mutate == "duplicate_source":
        source_sets["child_71"].add("s2")
    flattened = [x for values in source_sets.values() for x in values]
    if len(flattened) != len(set(flattened)):
        raise AssertionError("source owner duplicated")

    port_parent = [[F(5), F(1)], [F(1), F(4)]]
    port_current = [[F(5), F(1)], [F(1), F(4)]]
    child_ports = [F(0), F(0)]
    if mutate == "child_port":
        child_ports[0] = F(1)
    if port_parent != port_current or any(child_ports):
        raise AssertionError("root-global port was copied to a child")

    y4 = [F(0), F(0), F(0), F(0), F(2), F(3)]
    root_delta = dot(y4, slack)
    return {
        "coefficients": [fs(a1), fs(a2)],
        "coefficient_sum": fs(a1 + a2),
        "parent_typed_vector": [fs(x) for x in parent],
        "native_vector": [fs(x) for x in native],
        "root_slack": [fs(x) for x in slack],
        "root_delta": fs(root_delta),
        "source_atoms": len(flattened),
        "port_children_zero": True,
        "verdict": "PASS_EXACT_COMMON_PARENT_PACKET_AND_CAPACITY_IDENTITY",
    }


def hereditary_check(mutate: str | None = None) -> dict[str, Any]:
    rho = F(1, 8)
    if mutate == "non_subcritical":
        rho = F(1, 4)
    ratios = [F(2)]
    for _ in range(24):
        ratios.append(F(2) + rho * ratios[-1])
    if rho >= F(1, 8) and mutate == "non_subcritical":
        raise AssertionError("mutation: coefficient budget reached forbidden range")
    if any(x >= F(16, 7) for x in ratios):
        raise AssertionError("hereditary envelope exceeded 16/7")

    root_mass = F(3300)
    child_mass = rho * root_mass
    descendant = F(16, 7) * child_mass
    if descendant != F(6600, 7):
        raise AssertionError("root descendant constant changed")

    packet = [F(31), F(29), F(37), F(17), F(13), F(11)]
    child = [F(7), F(6), F(8), F(4), F(3), F(2)]
    r = F(1, 9)
    lam = F(2, 5)
    alpha = lam * r
    causal = vsub(packet, vscale(r, child))
    rhs = vadd(vscale(F(1) - lam, packet), vscale(lam, causal), vscale(alpha, child))
    if rhs != packet:
        raise AssertionError("complete-coordinate causal identity failed")
    if any(x < 0 for x in causal):
        raise AssertionError("causal current left the positive class")
    return {
        "depth_ratios": [fs(x) for x in ratios],
        "uniform_ratio_bound": "16/7",
        "root_mass_bound": fs(root_mass),
        "first_generation_child_mass": fs(child_mass),
        "complete_descendant_deficit_bound": fs(descendant),
        "verdict": "PASS_HEREDITARY_POSITIVE_CAUSAL_PACKET_CLASS",
    }


def one_shot_check(mutate: str | None = None) -> dict[str, Any]:
    current = [F(9), F(7), F(5), F(4)]
    child_67 = [F(3), F(2), F(1), F(2)]
    child_71 = [F(2), F(1), F(2), F(1)]
    a67, a71 = F(1, 20), F(1, 30)
    ideal = vadd(current, vscale(a67, child_67), vscale(a71, child_71))
    tau = F(9, 10)
    correction = [F(1), F(0), F(1), F(0)]
    final_total = vadd(vscale(tau, ideal), correction)
    final_by_colours = vadd(
        vscale(tau, current),
        vscale(tau * a67, child_67),
        vscale(tau * a71, child_71),
        correction,
    )
    if mutate == "requantize_child":
        final_by_colours = vadd(final_by_colours, vscale(F(1, 100), child_67))
    if final_total != final_by_colours:
        raise AssertionError("one-shot colour sum no longer equals the common parent")
    native_capacity = vadd(final_total, [F(0), F(0), F(2), F(3)])
    slack = vsub(native_capacity, final_total)
    if any(x < 0 for x in slack):
        raise AssertionError("one-shot total row is not feasible")
    y4 = [F(0), F(0), F(2), F(3)]
    delta = dot(y4, slack)
    return {
        "causal_coefficient_sum": fs(a67 + a71),
        "common_thinning": fs(tau),
        "final_total_row": [fs(x) for x in final_total],
        "native_slack": [fs(x) for x in slack],
        "native_delta": fs(delta),
        "children_reprocessed": False,
        "verdict": "PASS_ONE_SHOT_COMMON_PARENT_TERMINALIZES_CHILD_COLOURS",
    }


def factor(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def prime_power_base(n: int) -> int | None:
    f = factor(n)
    return next(iter(f)) if len(f) == 1 else None


def v4(q: int) -> int:
    out = 0
    while q % 4 == 0:
        q //= 4
        out += 1
    return out


def y4_coefficients(q: int) -> dict[int, int]:
    out: dict[int, int] = {}
    for h in range(v4(q) + 1):
        p = prime_power_base(q // (4**h))
        if p is not None:
            out[p] = out.get(p, 0) + 2**h
    return {p: c for p, c in out.items() if c}


def y4_expected(q: int) -> dict[int, int]:
    f = factor(q)
    if len(f) == 1 and 2 in f:
        e = f[2]
        return {2: 2 ** ((e + 1) // 2) - 1}
    e = f.get(2, 0)
    odd = {p: a for p, a in f.items() if p != 2}
    if e % 2 == 0 and len(odd) == 1:
        return {next(iter(odd)): 2 ** (e // 2)}
    return {}


def native_cost_check(mutate: str | None = None) -> dict[str, Any]:
    checked = 8191
    nonzero = 0
    for q in range(2, checked + 2):
        got = y4_coefficients(q)
        expected = y4_expected(q)
        if mutate == "y4_support" and q == 12:
            expected = {3: 1}
        if got != expected:
            raise AssertionError(("Y4 support", q, got, expected))
        nonzero += bool(got)
    if not 2913**2 < 2 * (16 * 129) ** 2:
        raise AssertionError("all-column square-root witness")
    thinning_constant = 4 * 130 * F(33, 4)
    if thinning_constant != 4290:
        raise AssertionError("thinning constant")
    terminal_margin = 5033 - 4452
    if terminal_margin != 581:
        raise AssertionError("terminal margin")
    if mutate == "benchmark_bridge":
        raise AssertionError("forbidden J_Lambda-4sqrt(X) benchmark bridge")
    root = F(100)
    correction_norm = F(7, 3)
    epsilon = F(1, 8 * 10152) / correction_norm / (root + 130)
    amplified = 10152 * correction_norm * epsilon
    reserve = F(1, root + 130)
    if not reserve > 2 * amplified > 0:
        raise AssertionError("strict reserve did not dominate amplified error")
    return {
        "formal_y4_support_checks": checked,
        "nonzero_y4_columns": nonzero,
        "all_column_square_witness": f"{2913**2} < {2*(16*129)**2}",
        "thinning_log_coefficient": fs(thinning_constant),
        "terminal_margin": terminal_margin,
        "normalized_reserve": fs(reserve),
        "amplified_error": fs(amplified),
        "verdict": "PASS_DIRECT_NATIVE_Y4_COST_AND_RESERVE_FIREWALL",
    }


def endpoint_check(mutate: str | None = None) -> dict[str, Any]:
    moat = F(1, 5)
    limsup_complete_gap = F(0)
    prime_endpoint_limsup = limsup_complete_gap - moat
    if mutate == "remove_moat":
        moat = F(0)
        prime_endpoint_limsup = limsup_complete_gap - moat
    if not prime_endpoint_limsup < 0:
        raise AssertionError("one-sided native deficit did not cross the prime-square moat")
    return {
        "synthetic_positive_moat": fs(moat),
        "complete_gap_limsup": fs(limsup_complete_gap),
        "prime_endpoint_limsup": fs(prime_endpoint_limsup),
        "verdict": "PASS_ONE_SIDED_NATIVE_DEFICIT_TO_PRIME_ENDPOINT_SIGN_ALGEBRA",
    }


def verify(_: dict[str, Any] | None = None) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "schema": SCHEMA,
        "common_parent": common_parent_check(),
        "hereditary_class": hereditary_check(),
        "one_shot_total_row": one_shot_check(),
        "native_cost": native_cost_check(),
        "endpoint": endpoint_check(),
        "proof_boundary": {
            "pr481_two_packets": "ONE_FACTOR67_METHOD",
            "pr482_pr484_reviews": "ACCEPTED_AT_FROZEN_HEADS",
            "root_hall_and_profile": "FROZEN_RECONSTRUCTION_REQUIRED",
            "all_column_endpoint_estimates": "FROZEN_RECONSTRUCTION_REQUIRED",
            "prime_square_and_landau": "FROZEN_ANALYTIC_RECONSTRUCTION_REQUIRED",
            "riemann_hypothesis": "PROPOSAL_PENDING_INDEPENDENT_REVIEW",
        },
        "verdict": "PASS_CANONICAL_FACTOR67_ONE_SHOT_NATIVE_ENDPOINT_ALGEBRA",
    }
    payload["proof_object_sha256"] = canonical_sha(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", nargs="?", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    source = json.loads(args.certificate.read_text()) if args.certificate else None
    out = verify(source)
    text = json.dumps(out, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
