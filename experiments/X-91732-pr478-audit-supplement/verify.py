#!/usr/bin/env python3
"""Fail-closed finite replay for the PR #478 audit supplement on PR #481.

This replay authenticates the newly deposited algebra and elementary constants.
It does not reconstruct the frozen analytic packet, full port demand, or the
endpoint/WSTS consumer, and it does not establish RH.
"""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import hashlib
import json
import math

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent


def causal_coefficients() -> tuple[list[Fraction], list[Fraction], Fraction]:
    r = [Fraction(1, 9), Fraction(1, 10), Fraction(1, 11)]
    survival = Fraction(1)
    lambdas: list[Fraction] = []
    alphas: list[Fraction] = []
    for ri in r:
        lambdas.append(ri * survival)
        alphas.append(ri * lambdas[-1])
        survival *= 1 - ri
    assert survival + sum(lambdas) == 1
    assert sum(alphas) < Fraction(1, 8)
    return lambdas, alphas, survival


def check_actual_mass() -> dict[str, str | bool]:
    _, alphas, _ = causal_coefficients()
    weights = [Fraction(2, 3), Fraction(3, 5), Fraction(7, 11)]
    masses = [Fraction(3, 2), Fraction(5, 4), Fraction(7, 3)]
    ratios = [
        [Fraction(2, 3), Fraction(0), Fraction(1, 5)],
        [Fraction(0), Fraction(3, 4), Fraction(1, 2)],
        [Fraction(4, 5), Fraction(2, 7), Fraction(0)],
    ]
    parent = sum(w * m for w, m in zip(weights, masses, strict=True))
    child_by_prime = [
        sum(weights[s] * masses[s] * ratios[s][i] for s in range(3))
        for i in range(3)
    ]
    assert all(c <= parent for c in child_by_prime)
    recursive = sum(a * c for a, c in zip(alphas, child_by_prime, strict=True))
    assert recursive <= parent * sum(alphas) < parent / 8
    return {
        "alpha_sum": str(sum(alphas)),
        "parent_mass": str(parent),
        "recursive_mass": str(recursive),
        "strict_one_eighth": True,
    }


def check_columns() -> dict[str, str | bool | int]:
    ordinary = Fraction(57, 2)
    detail = ordinary + ordinary / 2
    combined = detail + 200
    assert detail == Fraction(171, 4)
    assert combined == Fraction(971, 4)
    assert 2913**2 < 2 * (16 * 129) ** 2
    assert 178**2 <= 2 * 130**2
    x = Fraction(17)
    assert x / (x + 129) * (1 + Fraction(129, 1) / x) == 1
    assert x / (x + 130) * (1 + Fraction(129, 1) / x) < 1
    return {
        "ordinary": str(ordinary),
        "detail": str(detail),
        "combined": str(combined),
        "relative_constant": 129,
        "strict_denominator": 130,
        "all_columns": True,
    }


def check_root_mass() -> dict[str, str | bool]:
    h66 = sum(Fraction(1, n) for n in range(1, 67))
    assert h66 < 5
    assert 16 * 67 < 33**2
    exp5_lower = sum(Fraction(5**j, math.factorial(j)) for j in range(6))
    assert exp5_lower > 67
    endpoint = Fraction(183, 10)
    fiber = Fraction(165)
    integrated = endpoint * fiber
    assert integrated == Fraction(6039, 2) < 3020
    return {
        "harmonic_66": str(h66),
        "endpoint_measure_upper": str(endpoint),
        "fiber_target_upper": str(fiber),
        "integrated_target_upper": str(integrated),
        "lt_3020": True,
    }


def check_score_scope() -> dict[str, str | bool]:
    t, ratio = Fraction(17), Fraction(8)
    sqrt_x = t * ratio
    tau = t / (t + 130)
    h0 = 4 * sqrt_x + 1000
    log_x = Fraction(7)
    j_native = 4 * sqrt_x + 4 * log_x - 1
    continuum = 4 * sqrt_x - tau * h0
    assert continuum <= 4 * sqrt_x * (1 - tau) < 4290
    native = j_native - tau * h0
    assert native < 4 * log_x + 4290
    return {
        "continuum_shortfall": str(continuum),
        "continuum_bound_lt_4290": True,
        "native_deficit": str(native),
        "native_bound": str(4 * log_x + 4290),
    }


def check_cocycle() -> dict[str, str | bool]:
    beta = [Fraction(1, 20), Fraction(1, 30), Fraction(1, 40)]
    root = [Fraction(1, 2), Fraction(7, 10), Fraction(11, 5)]
    children = [
        [Fraction(1, 3), Fraction(1, 4), Fraction(1, 5)],
        [Fraction(2, 7), Fraction(3, 8), Fraction(4, 9)],
        [Fraction(5, 11), Fraction(6, 13), Fraction(7, 17)],
    ]
    parent = [root[j] + sum(beta[i] * children[i][j] for i in range(3)) for j in range(3)]
    y4 = [Fraction(2), Fraction(3), Fraction(5)]
    lhs = sum(y4[j] * parent[j] for j in range(3))
    rhs = sum(y4[j] * root[j] for j in range(3)) + sum(
        beta[i] * sum(y4[j] * children[i][j] for j in range(3)) for i in range(3)
    )
    assert lhs == rhs and sum(beta) < Fraction(1, 8)
    return {"beta_sum": str(sum(beta)), "paired_identity": str(lhs), "exact": True}


def check_files() -> dict[str, object]:
    paths = [
        "claims/refutations/R-91727-pr478-review-is-locally-correct-but-not-exhaustive.md",
        "claims/lemmas/L-91732-factor67-direct-integrals-have-actual-target-normalized-children.md",
        "claims/lemmas/L-91733-retained-cell-euler-mismatch-closes-all-physical-columns.md",
        "claims/lemmas/L-91734-activation-knot-collars-have-vanishing-score-by-absolute-continuity.md",
        "claims/lemmas/L-91735-square-root-thinning-has-logarithmic-native-cost.md",
        "claims/lemmas/L-91736-actual-mass-children-obey-the-native-slack-cocycle.md",
        "claims/lemmas/L-91737-factor67-retained-root-target-mass-is-below-3020.md",
        "claims/theorems/T-91725-pr478-audit-supplements-corrected-factor67-proposal.md",
        "reports/gpt56-pro/2026-08-15-pr478-audit-supplement.md",
    ]
    for rel in paths:
        text = (ROOT / rel).read_text(encoding="utf-8")
        assert "unproved" in text.lower()
    theorem = (ROOT / paths[7]).read_text(encoding="utf-8")
    assert "PR #482" in theorem
    assert "does not silently claim" in theorem
    return {"checked": len(paths), "pr482_boundary_retained": True}


def main() -> None:
    payload: dict[str, object] = {
        "classification": "PASS_PR478_AUDIT_SUPPLEMENT_ON_PR481_V2",
        "actual_mass": check_actual_mass(),
        "all_columns": check_columns(),
        "root_mass": check_root_mass(),
        "score_scope": check_score_scope(),
        "native_cocycle": check_cocycle(),
        "file_firewalls": check_files(),
        "open_reconstruction_obligations": [
            "concrete post-Hall/post-quantization corrected packet equality",
            "instantiated complete common-port demand",
            "exact Y4 pairing of terminal/base/port corrections",
            "frozen endpoint/WSTS and Mellin-Landau consumer",
        ],
        "rh_established_by_replay": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    out = HERE / "results/verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(payload["classification"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
