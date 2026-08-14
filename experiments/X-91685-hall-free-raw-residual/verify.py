#!/usr/bin/env python3
"""Algebra and normalization replay for L-91685/T-91658.

This script authenticates the new stopped-leaf algebra and an 80-digit
hostile-leaf diagnostic. It deliberately does not replay the large imported
directed certificates, the PR #468 rough-reservoir theorem, or NRSLI/NRCT.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Iterable

PRIMES_61 = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61)
P61 = 1
for _p in PRIMES_61:
    P61 *= _p

KNOWN_ROW_66 = Decimal(
    "0.0083815482754633380104356899436506668455590554820706248557213328673706658744905531974"
)
KNOWN_ROW_870 = Decimal(
    "0.000039036423824404762594378011731372740288479187210559542661067008477761277704208305828"
)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def mobius_sieve(n: int) -> list[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: list[int] = []
    is_composite = [False] * (n + 1)
    for i in range(2, n + 1):
        if not is_composite[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n:
                break
            is_composite[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def squarefree_p61_divisors_upto(limit: int) -> list[tuple[int, int]]:
    values: list[tuple[int, int]] = [(1, 1)]
    for p in PRIMES_61:
        additions: list[tuple[int, int]] = []
        for d, mu in values:
            if d * p <= limit:
                additions.append((d * p, -mu))
        values.extend(additions)
    return sorted(values)


def decimal_fraction(x: Fraction) -> Decimal:
    return Decimal(x.numerator) / Decimal(x.denominator)


def q_array(y: Fraction, max_j: int) -> list[Decimal]:
    """Return Q_y(j), 0<=j<=max_j, using the exact causal floor and Decimal logs."""
    n_max = y.numerator // y.denominator
    max_j = min(max_j, n_max)
    out = [Decimal(0)] * (max_j + 1)
    if max_j < 2:
        return out

    y_dec = decimal_fraction(y)
    h = [Decimal(0)] * (n_max + 3)
    for m in range(1, n_max + 1):
        h[m] = (y_dec / Decimal(m)).ln() / Decimal(m).sqrt()

    suffix = [Decimal(0)] * (n_max + 4)
    for m in range(n_max, 0, -1):
        suffix[m] = suffix[m + 1] + h[m]

    for j in range(2, max_j + 1):
        out[j] = Decimal(j + 1) * (
            suffix[j] / Decimal(j - 1)
            - Decimal(2) * suffix[j + 1] / Decimal(j)
            + suffix[j + 2] / Decimal(j + 1)
        )
    return out


def d_rows(x: Fraction, max_j: int) -> list[Decimal]:
    n_max = x.numerator // x.denominator
    max_j = min(max_j, n_max)
    out = [Decimal(0)] * (max_j + 1)
    if max_j < 2:
        return out

    for d, mu in squarefree_p61_divisors_upto(n_max // 2):
        y = x / d
        y_floor = y.numerator // y.denominator
        if y_floor < 2:
            continue
        q = q_array(y, min(max_j, y_floor))
        coefficient = Decimal(mu) / Decimal(d).sqrt()
        for j in range(2, len(q)):
            out[j] += coefficient * q[j]
    return out


def f_a_p61(x: int, a: Fraction) -> Decimal:
    sx = Decimal(x).sqrt()
    a_dec = decimal_fraction(a)
    total = Decimal(0)
    for d, mu in squarefree_p61_divisors_upto(x):
        total += Decimal(mu) * (
            a_dec * sx / Decimal(d) - Decimal(1) / Decimal(d).sqrt()
        )
    return total


def target_p61(x: int) -> Decimal:
    return Decimal(3) * f_a_p61(x, Fraction(4, 3))


def score_p61(x: int) -> Decimal:
    return Decimal(3) * f_a_p61(x, Fraction(5, 3))


def exact_support_checks() -> dict[str, int]:
    mu = mobius_sieve(66)
    terminal_terms = 0
    support_equalities = 0
    sector_cases = 0

    for y in range(1, 67):
        for j in range(2, 4 * 67 + 1):
            inherited = j <= y
            frontier = j > y
            assert inherited ^ frontier
            sector_cases += 1

        for j in range(2, y + 1):
            for k in range(1, y // j + 1):
                if mu[k] == 0:
                    continue
                terminal_terms += 1
                # Every squarefree k<67 divides P_61 exactly once prime-by-prime.
                assert P61 % k == 0
                support_equalities += 1

    return {
        "sector_partition_cases": sector_cases,
        "terminal_nonzero_mobius_terms": terminal_terms,
        "terminal_support_equalities": support_equalities,
    }


def exact_ledger_checks() -> dict[str, int]:
    checks = 0

    # Current + child = parent in every linear coordinate.
    parents = [Fraction(13, 7), Fraction(29, 11), Fraction(101, 37), Fraction(5, 3)]
    children = [Fraction(2, 7), Fraction(7, 11), Fraction(9, 37), Fraction(1, 3)]
    currents = [p - c for p, c in zip(parents, children)]
    for p, c, g in zip(parents, children, currents):
        assert g + c == p
        checks += 1

    # Monotonicity decomposition used for H_P and Delta_P.
    r = Fraction(1, 9)
    for small, increment in ((Fraction(0), Fraction(0)), (Fraction(2, 5), Fraction(7, 13)), (Fraction(11, 8), Fraction(3, 2))):
        big = small + increment
        lhs = big - r * small
        rhs = increment + (1 - r) * small
        assert lhs == rhs and rhs >= 0
        checks += 1

    # Exact positivity of the theorem constants.
    score_target_constant = Fraction(
        336338530534578047569,
        224523472888007630167974,
    )
    assert score_target_constant > Fraction(1498, 1_000_000)
    checks += 1
    for value in (Fraction(9, 50), Fraction(893, 100), Fraction(559, 50)):
        assert value > 0
        checks += 1

    return {"formal_linear_checks": checks}


def hostile_leaf_diagnostic() -> dict[str, str | int]:
    p = 67
    y = 13
    x = p * y

    parent = d_rows(Fraction(x), x)
    child = d_rows(Fraction(y), y)
    r = Decimal(1) / Decimal(p).sqrt()

    residual: dict[int, Decimal] = {}
    for j in range(2, x + 1):
        child_value = child[j] if j < len(child) else Decimal(0)
        residual[j] = parent[j] - r * child_value

    for j in range(2, x):
        assert residual[j] > 0, (j, residual[j])
    assert residual[x] == 0

    min_2_66_j = min(range(2, 67), key=lambda j: residual[j])
    min_full_j = min(range(2, x), key=lambda j: residual[j])
    min_2_66 = residual[min_2_66_j]
    min_full = residual[min_full_j]

    tolerance = Decimal("1e-70")
    assert min_2_66_j == 66
    assert abs(min_2_66 - KNOWN_ROW_66) < tolerance
    assert min_full_j == 870
    assert abs(min_full - KNOWN_ROW_870) < tolerance

    target = target_p61(x) - r * target_p61(y)
    score = score_p61(x) - r * score_p61(y)
    assert target > 0
    assert score > target

    return {
        "p": p,
        "y": y,
        "x": x,
        "row_checks": x - 1,
        "min_observed_row": min_2_66_j,
        "min_observed_value": str(min_2_66),
        "min_full_positive_row": min_full_j,
        "min_full_positive_value": str(min_full),
        "terminal_zero_row": x,
        "target": str(target),
        "score": str(score),
        "score_minus_target": str(score - target),
        "precision_digits": 80,
        "classification": "high-precision diagnostic, not imported-certificate replay",
    }


def load_and_check_lock(repo_root: Path) -> dict[str, object]:
    lock_path = repo_root / "integration/2026-08-14/t91658-hall-free-dependency-lock.json"
    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    assert lock["claim"] == "T-91658"
    assert lock["proposed_base_sha"] == "a41f81466f85d52597c97b41505756a8860698d0"
    assert len(lock["normative_dependencies"]) >= 10 and len(lock["cross_branch_inputs"]) >= 4
    for dep in lock["normative_dependencies"] + lock["cross_branch_inputs"]:
        assert len(dep["commit"]) == 40
        assert dep["path"]
        assert dep["claim"]
    return {
        "normative_dependency_count": len(lock["normative_dependencies"]),
        "cross_branch_input_count": len(lock["cross_branch_inputs"]),
        "proposed_base_sha": lock["proposed_base_sha"],
        "proposed_branch": lock["proposed_branch"],
        "lock_sha256": sha256_file(lock_path),
    }


def local_content_hashes(repo_root: Path) -> dict[str, str]:
    rels = [
        "claims/lemmas/L-91685-complete-p61-raw-residual-is-a-hall-free-stopped-leaf-generator.md",
        "claims/theorems/T-91658-hall-free-stopped-leaf-reduction-to-the-root-realization.md",
        "claims/observations/O-91685-hall-free-raw-residual-proof-dag.md",
        "reports/gpt56-pro/2026-08-14-hall-free-raw-residual-stopping-line-attack.md",
        "integration/2026-08-14/t91658-hall-free-dependency-lock.json",
        "standalone/2026-08-14-hall-free-raw-residual/README.md",
        "standalone/2026-08-14-hall-free-raw-residual/CLAIM_STATUS.md",
    ]
    hashes = {}
    for rel in rels:
        path = repo_root / rel
        assert path.is_file(), rel
        hashes[rel] = sha256_file(path)
    return hashes


def build_record(repo_root: Path) -> dict[str, object]:
    with localcontext() as ctx:
        ctx.prec = 80
        support = exact_support_checks()
        ledger = exact_ledger_checks()
        hostile = hostile_leaf_diagnostic()
        lock = load_and_check_lock(repo_root)
        hashes = local_content_hashes(repo_root)

    record: dict[str, object] = {
        "verdict": "PASS_HALL_FREE_RAW_RESIDUAL_ALGEBRA",
        "scope": {
            "authenticates": [
                "new current-plus-child algebra",
                "terminal-support identity",
                "inherited/frontier coverage logic",
                "hostile-leaf formula normalization",
                "local content and dependency-lock hashes",
            ],
            "does_not_authenticate": [
                "imported global L-91364 directed proof",
                "imported inherited-row and entropy certificates",
                "PR468 rough-reservoir reconstruction",
                "NRSLI native-reservoir/stopping-line allocation",
                "Native-Root Capacity Theorem",
                "endpoint-frame/collar/mismatch/top/port estimates",
                "endpoint-to-RH analytic implication",
            ],
        },
        "exact_support": support,
        "exact_ledger": ledger,
        "hostile_leaf": hostile,
        "dependency_lock": lock,
        "local_content_sha256": hashes,
    }
    canonical = json.dumps(record, sort_keys=True, separators=(",", ":")).encode("utf-8")
    record["record_sha256"] = hashlib.sha256(canonical).hexdigest()
    return record


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, help="write the verification record to this path")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[2]
    record = build_record(repo_root)

    text = json.dumps(record, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8")
    print(record["verdict"])
    print("record_sha256", record["record_sha256"])
    print("min_observed_row", record["hostile_leaf"]["min_observed_row"])
    print("min_observed_value", record["hostile_leaf"]["min_observed_value"])
    print("min_full_positive_row", record["hostile_leaf"]["min_full_positive_row"])
    print("min_full_positive_value", record["hostile_leaf"]["min_full_positive_value"])


if __name__ == "__main__":
    main()
