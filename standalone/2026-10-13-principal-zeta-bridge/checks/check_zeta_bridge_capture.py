#!/usr/bin/env python3
"""Exact finite diagnostics for the ordinary-zeta bridge and sparse capture.

This checks arithmetic identities and finite interpolation/counting algebra.
It does not establish any asymptotic derivative bound, grid hypothesis,
arithmetic capture estimate, zero-free region, or Riemann hypothesis.
No floating-point arithmetic, external packages, or Python assert gates.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
import subprocess


BASELINE = "ab98878279cd5614fe79bb94aa916e97c9ee50b4"
SOURCES = {
    "standalone/2026-10-10-sextic-critical-core/LOG_FREE_REPLICATED_SPIKES.md":
        "b59978c1c5d3b5cb904c7f22d675a67bb71b2af512db9f0577e568a04565a86b",
    "standalone/2026-10-10-signed-graph-and-joint-descent/sources/pr926/SAMPLED_MOMENT_CRITERION.md":
        "18bf2fdad438eb21ae3318eba7d42e9c03803b2dd1abc4d8f6448fb3b04499de",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def primes(limit: int) -> list[int]:
    return [n for n in range(2, limit + 1)
            if all(n % d for d in range(2, math.isqrt(n) + 1))]


def mobius(n: int) -> int:
    sign = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        sign = -sign
    return sign


def chi3(n: int) -> int:
    return (0, 1, -1)[n % 3]


def identity(limit: int) -> list[int]:
    values = [0] * (limit + 1)
    values[1] = 1
    return values


def convolution(a: list[int], b: list[int]) -> list[int]:
    require(len(a) == len(b), "convolution truncations differ")
    limit = len(a) - 1
    result = [0] * (limit + 1)
    for n in range(1, limit + 1):
        if a[n]:
            for m in range(1, limit // n + 1):
                if b[m]:
                    result[n * m] += a[n] * b[m]
    return result


def euler_factor(limit: int, norm: int) -> list[int]:
    result = identity(limit)
    if norm <= limit:
        result[norm] -= 1
    return result


def geometric_factor(limit: int, norm: int) -> list[int]:
    result = [0] * (limit + 1)
    power = 1
    while power <= limit:
        result[power] = 1
        power *= norm
    return result


def product_factors(limit: int, norms: list[int], inverse: bool = False) -> list[int]:
    result = identity(limit)
    for norm in norms:
        factor = geometric_factor(limit, norm) if inverse else euler_factor(limit, norm)
        result = convolution(result, factor)
    return result


def eisenstein_prime_ideals(limit: int) -> list[tuple[int, int, int]]:
    """Identities (rational prime, distinct ideal slot, ideal norm)."""
    ideals = []
    for p in primes(limit):
        if p == 3:
            ideals.append((p, 0, p))
        elif p % 3 == 1:
            ideals.extend(((p, 0, p), (p, 1, p)))
        elif p * p <= limit:
            ideals.append((p, 0, p * p))
    return ideals


def arithmetic_checks() -> dict:
    limit = 160
    ideals = eisenstein_prime_ideals(limit)
    all_ids = {(p, slot) for p, slot, _ in ideals}
    norms = {(p, slot): norm for p, slot, norm in ideals}
    variable = [(2, 0), (3, 0), (7, 0), (7, 1), (13, 0), (13, 1)]
    require(set(variable) <= all_ids, "a declared prime ideal is absent")
    integer_mu = [0] + [mobius(n) for n in range(1, limit + 1)]
    character = [0] + [chi3(n) for n in range(1, limit + 1)]
    ideal_mu = product_factors(limit, [norm for _, _, norm in ideals])
    require(convolution(ideal_mu, character) == integer_mu,
            "unrestricted quadratic companion cancellation failed")

    # Every variable ideal is either in S, in the replica support w, or neither.
    # In particular two split ideals with equal norm can be excluded separately.
    assignments = 0
    coefficient_checks = 0
    restoration_only_cases = 0
    for states in itertools.product(range(3), repeat=len(variable)):
        bad = {ideal for ideal, state in zip(variable, states) if state == 1}
        base = {ideal for ideal, state in zip(variable, states) if state == 2}
        require(not bad.intersection(base), "test generated forbidden S/w overlap")
        raw = product_factors(limit, [norm for p, slot, norm in ideals
                                     if (p, slot) not in bad and (p, slot) not in base])
        restoration = product_factors(limit, [norms[key] for key in variable if key in bad])
        restored = convolution(convolution(raw, character), restoration)
        replica = convolution(integer_mu,
                              product_factors(limit, [norms[key] for key in variable if key in base],
                                              inverse=True))
        require(restored == replica, f"restored principal recurrence failed: {states}")
        assignments += 1
        coefficient_checks += limit
        if not base:
            require(restored == integer_mu, "ordinary-mu restoration failed")
            restoration_only_cases += 1

    # Dedicated negative controls: these must fail as coefficient identities.
    controls = {}
    bad_one = {(7, 0)}
    removed_one = product_factors(limit, [norm for p, slot, norm in ideals
                                         if (p, slot) not in bad_one])
    controls["omitted_finite_restoration"] = (
        convolution(removed_one, character) != integer_mu)
    bad_pair = {(7, 0), (7, 1)}
    removed_pair = product_factors(limit, [norm for p, slot, norm in ideals
                                          if (p, slot) not in bad_pair])
    collapsed_restoration = convolution(convolution(removed_pair, character),
                                        euler_factor(limit, 7))
    controls["collapsed_equal_norm_bad_ideals"] = collapsed_restoration != integer_mu
    correct_overlap_row = convolution(convolution(removed_one, character), euler_factor(limit, 7))
    incorrect_overlap_replica = convolution(integer_mu, geometric_factor(limit, 7))
    controls["replica_prime_already_in_S"] = correct_overlap_row != incorrect_overlap_replica
    correct_replica = convolution(integer_mu, geometric_factor(limit, 7))
    squarefree_only = identity(limit)
    squarefree_only[7] = 1
    controls["omitted_replica_prime_powers"] = (
        correct_replica != convolution(integer_mu, squarefree_only))
    doubled_replica = convolution(correct_replica, geometric_factor(limit, 7))
    controls["collapsed_equal_norm_replica_ideals"] = doubled_replica != correct_replica
    controls["unfiltered_ideal_mu_as_integer_mu"] = ideal_mu != integer_mu
    require(all(controls.values()), "an arithmetic negative control did not reject")

    # Local formal products include every split/inert/ramified type and deleted
    # ideal multiplicity. A local degree is rational-prime valuation, not norm.
    local_cases = 0
    degree = 12
    for kind, local_norm_degrees, chi in (
            ("split", (1, 1), 1), ("inert", (2,), -1), ("ramified", (1,), 0)):
        for excluded in itertools.product((False, True), repeat=len(local_norm_degrees)):
            a = [1] + [0] * degree
            for e, deleted in zip(local_norm_degrees, excluded):
                if not deleted:
                    for j in range(degree, e - 1, -1):
                        a[j] -= a[j - e]
            filtered = [sum(a[j] * (chi ** (k - j)) for j in range(k + 1))
                        for k in range(degree + 1)]
            for e, deleted in zip(local_norm_degrees, excluded):
                if deleted:
                    for j in range(degree, e - 1, -1):
                        filtered[j] -= filtered[j - e]
            require(filtered == [1, -1] + [0] * (degree - 1),
                    f"local restored identity failed for {kind}/{excluded}")
            local_cases += 1

    return {
        "truncation_n_le": limit,
        "ideal_status_assignments": assignments,
        "coefficient_equalities": coefficient_checks,
        "restoration_only_cases": restoration_only_cases,
        "local_series_cases": local_cases,
        "local_series_degree": degree,
        "negative_controls_rejected": controls,
    }


def ceil_fraction(x: Fraction) -> int:
    return -((-x.numerator) // x.denominator)


def lagrange_weights(nodes: list[int], t: Fraction) -> list[Fraction]:
    weights = []
    for j, node in enumerate(nodes):
        value = Fraction(1)
        for i, other in enumerate(nodes):
            if i != j:
                value *= (t - other) / (node - other)
        weights.append(value)
    return weights


def interpolation_checks() -> dict:
    gammas = [Fraction(1), Fraction(1, 2), Fraction(2, 3), Fraction(1, 3)]
    patterns = 0
    evaluation_cases = 0
    separation_cases = 0
    reproduction_cases = 0
    for gamma in gammas:
        for m in range(1, 7):
            q = ceil_fraction(4 * m / gamma)
            lower_g = ceil_fraction(gamma * q / 2)
            require(lower_g >= 2 * m, "selected block has too few good nodes")
            if q <= 12:
                good_patterns = [list(nodes)
                                 for g in range(lower_g, q + 1)
                                 for nodes in itertools.combinations(range(q), g)]
            else:
                candidates = set()
                for g in sorted({lower_g, min(q, lower_g + 1), q - 1, q}):
                    if g < lower_g:
                        continue
                    candidates.add(tuple(range(g)))
                    candidates.add(tuple(range(q - g, q)))
                    # Evenly spread and edge-clustered extreme node sets.
                    candidates.add(tuple((j * (q - 1)) // (g - 1) for j in range(g)))
                    left = g // 2
                    candidates.add(tuple(list(range(left)) + list(range(q - (g - left), q))))
                good_patterns = [list(nodes) for nodes in sorted(candidates)]
            for good in good_patterns:
                g = len(good)
                require(g >= lower_g and len(set(good)) == g, "bad test node pattern")
                step = g // m
                selected = [good[(j + 1) * step - 1] for j in range(m)]
                require(len(set(selected)) == m, "selected nodes collide")
                separation = gamma * q / (4 * m)
                for j in range(1, m):
                    require(selected[j] - selected[j - 1] >= separation,
                            "guaranteed good-node spacing failed")
                    separation_cases += 1
                formal_basis_bound = (8 * m / gamma) ** (m - 1) / math.factorial(m - 1)
                explicit_bound = (32 / gamma) ** m
                require(formal_basis_bound <= explicit_bound,
                        "finite explicit Lagrange constant failed")
                tests = sorted({Fraction(0), Fraction(q - 1), Fraction(q - 1, 2),
                                Fraction(1, 2), Fraction(2 * q - 3, 2)})
                for t in tests:
                    weights = lagrange_weights(selected, t)
                    require(sum(abs(w) for w in weights) <= formal_basis_bound,
                            "Lagrange extrapolation bound failed")
                    for power in range(m):
                        require(sum(w * node ** power for w, node in zip(weights, selected)) == t ** power,
                                "polynomial reproduction failed")
                        reproduction_cases += 1
                    # The monic degree-m interpolation remainder is exactly the
                    # node product, including outside the chosen nodes' hull.
                    residual = t ** m - sum(w * node ** m for w, node in zip(weights, selected))
                    node_product = math.prod(t - node for node in selected)
                    require(residual == node_product, "exact monic remainder failed")
                    require(abs(residual) <= q ** m, "block diameter remainder bound failed")
                    evaluation_cases += 1
                patterns += 1

    constant_cases = 0
    incidence_cases = 0
    for denominator in range(1, 17):
        for numerator in range(1, denominator + 1):
            gamma = Fraction(numerator, denominator)
            require(gamma / 2 + gamma / 4 < gamma, "coarse incidence contradiction failed")
            require((1 - gamma / 4) * gamma / 2 + gamma / 4 < gamma,
                    "sharper incidence contradiction failed")
            incidence_cases += 1
            for m in range(1, 81):
                bound = (8 * m / gamma) ** (m - 1) / math.factorial(m - 1)
                require(bound <= (32 / gamma) ** m, "explicit constant range failed")
                q = ceil_fraction(4 * m / gamma)
                require(q <= 5 * m / gamma, "block-length ceiling bound failed")
                constant_cases += 1
    return {
        "node_patterns": patterns,
        "rational_evaluations": evaluation_cases,
        "separation_equalities_or_inequalities": separation_cases,
        "polynomial_reproduction_equalities": reproduction_cases,
        "constant_cases": constant_cases,
        "incidence_fraction_cases": incidence_cases,
        "coverage": "All good-node subsets for declared blocks q<=12; specified edge/spread patterns otherwise.",
    }


def verify_sources(repo: Path | None) -> dict:
    if repo is None:
        return {"baseline_commit": BASELINE, "replayed": False, "expected_sha256": SOURCES}
    observed = {}
    for relative, expected in SOURCES.items():
        result = subprocess.run(["git", "show", f"{BASELINE}:{relative}"],
                                cwd=repo, check=False, capture_output=True)
        require(result.returncode == 0, f"cannot read pinned source {relative}")
        digest = hashlib.sha256(result.stdout).hexdigest()
        require(digest == expected, f"pinned source hash mismatch: {relative}")
        observed[relative] = digest
    return {"baseline_commit": BASELINE, "replayed": True, "observed_sha256": observed}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, help="optional local checkout for exact pinned-source hash replay")
    parser.add_argument("--manuscript", type=Path,
                        default=Path(__file__).with_name("EXACT_ZETA_BRIDGE_AND_SPARSE_CAPTURE.md"))
    parser.add_argument("--report", type=Path,
                        default=Path(__file__).with_name("zeta_bridge_capture_diagnostic.json"))
    args = parser.parse_args()
    require(args.manuscript.is_file(), "manuscript is missing")
    report = {
        "status": "PASS",
        "arithmetic": "exact integers and fractions only",
        "checker_sha256": sha256(Path(__file__)),
        "manuscript_sha256": sha256(args.manuscript),
        "sources": verify_sources(args.repo),
        "local_and_replica_checks": arithmetic_checks(),
        "interpolation_and_incidence_checks": interpolation_checks(),
        "not_certified": [
            "all-order asymptotic regularity",
            "an analytic bound from finite sampling",
            "the arithmetic observation hypothesis (5.3)",
            "any zero-free line or the Riemann hypothesis",
        ],
    }
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "report": args.report.name,
                      "report_sha256": sha256(args.report),
                      "replica_cases": report["local_and_replica_checks"]["ideal_status_assignments"],
                      "interpolation_evaluations": report["interpolation_and_incidence_checks"]["rational_evaluations"]},
                     sort_keys=True))


if __name__ == "__main__":
    main()
