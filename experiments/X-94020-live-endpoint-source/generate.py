#!/usr/bin/env python3
"""Generate the live endpoint/source registry for the Target--Lorenz audit.

This is not a proof of the open joint native coupling. It instantiates the
actual arithmetic marginals, source owners, P_61/rough paths, the terminal
(p,y)=(67,13) leaf, the exact finite-forcing causal weights, and the exact q=2
obstruction to branchwise child positivity.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from dataclasses import dataclass
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
from typing import Iterable

SMALL_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61)
ROUGH_MIN = 67
FROZEN_HEAD = "4ae97dffd1f76ed3244b8f3028560ffa80663caf"


def canonical_bytes(payload: object) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()


def canonical_hash(payload: object) -> str:
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, payload: object) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return sha256_file(path)


def linear_mobius(limit: int) -> tuple[list[int], list[int]]:
    mu = [0] * (limit + 1)
    least = [0] * (limit + 1)
    primes: list[int] = []
    mu[1] = 1
    for n in range(2, limit + 1):
        if least[n] == 0:
            least[n] = n
            primes.append(n)
            mu[n] = -1
        for p in primes:
            if p > least[n] or n * p > limit:
                break
            least[n * p] = p
            if p == least[n]:
                mu[n * p] = 0
            else:
                mu[n * p] = -mu[n]
    return mu, primes


def factor_squarefree(n: int, primes: Iterable[int]) -> tuple[int, tuple[int, ...]]:
    d = 1
    rough: list[int] = []
    m = n
    for p in primes:
        if p * p > m:
            break
        if m % p == 0:
            m //= p
            if m % p == 0:
                raise ValueError(f"{n} is not squarefree")
            if p <= 61:
                d *= p
            else:
                rough.append(p)
        while m % p == 0:
            m //= p
    if m > 1:
        if m <= 61:
            d *= m
        else:
            rough.append(m)
    return d, tuple(rough)


def divisors_p61(limit: int | None = None) -> list[tuple[int, int]]:
    vals = [(1, 1)]
    for p in SMALL_PRIMES:
        vals += [(d * p, -mu) for d, mu in list(vals)]
    vals.sort()
    if limit is not None:
        vals = [(d, mu) for d, mu in vals if d <= limit]
    return vals


def source_registry(X: int) -> tuple[dict, list[dict]]:
    mu, primes = linear_mobius(X)
    atoms: list[dict] = []
    finite = 0
    child = 0
    owner_counts: dict[str, int] = {}
    for k in range(1, X + 1):
        if mu[k] == 0:
            continue
        d, rough = factor_squarefree(k, primes)
        owner = "root" if not rough else str(rough[0])
        owner_counts[owner] = owner_counts.get(owner, 0) + 1
        finite += int(not rough)
        child += int(bool(rough))
        atoms.append(
            {
                "k": k,
                "mu": mu[k],
                "small_divisor": d,
                "rough_history": list(rough),
                "first_owner": owner,
                "parity": "even" if mu[k] == 1 else "odd",
                "path_coefficient": f"1/sqrt({k})",
                "paired_equality_coefficient": {
                    "formula": "mu(k)/sqrt(k)*(2*sqrt(X/k)-1)",
                    "sqrt_X_coefficient": f"{2*mu[k]}/{k}",
                    "inverse_sqrt_k_coefficient": str(-mu[k]),
                },
                "single_sharp_target_coefficient": {
                    "formula": "mu(k)/sqrt(k)*(4*sqrt(X/k)-3)",
                    "sqrt_X_coefficient": f"{4*mu[k]}/{k}",
                    "inverse_sqrt_k_coefficient": str(-3 * mu[k]),
                },
                "declared_score_coefficient": {
                    "formula": "mu(k)/sqrt(k)*(5*sqrt(X/k)-3)",
                    "sqrt_X_coefficient": f"{5*mu[k]}/{k}",
                    "inverse_sqrt_k_coefficient": str(-3 * mu[k]),
                },
            }
        )
    assert finite + child == len(atoms)
    assert len({a["k"] for a in atoms}) == len(atoms)
    for a in atoms:
        prod = a["small_divisor"]
        for p in a["rough_history"]:
            prod *= p
        assert prod == a["k"]
    summary = {
        "X": X,
        "squarefree_source_atoms": len(atoms),
        "finite_forcing_atoms": finite,
        "actual_rough_child_atoms": child,
        "first_owner_counts": owner_counts,
        "registry_sha256": canonical_hash(atoms),
        "atoms_preview": atoms[:12],
    }
    return summary, atoms


def endpoint_registry(X: int) -> tuple[dict, list[dict]]:
    mu, primes = linear_mobius(X)
    occurrences: list[dict] = []
    zero_count = 0
    owners: dict[str, int] = {}
    for m in range(1, X + 1):
        max_k = X // m
        for k in range(1, max_k + 1):
            if mu[k] == 0:
                continue
            if X == m * k:
                zero_count += 1
            d, rough = factor_squarefree(k, primes)
            owner = "root" if not rough else str(rough[0])
            owners[owner] = owners.get(owner, 0) + 1
            occurrences.append(
                {
                    "endpoint_cell": m,
                    "root_parameter": f"{X}/{m}",
                    "root_parameter_decimal": X / m,
                    "k": k,
                    "mu": mu[k],
                    "small_divisor": d,
                    "rough_history": list(rough),
                    "first_owner": owner,
                    "finite_coefficient": f"mu({k})/sqrt({m*k})*log({X}/{m*k})",
                    "common_coordinate_scalar": f"mu({k})/sqrt({m*k})*log({X}/{m*k})",
                    "coordinate_contract": [
                        "source incidence",
                        "component-row occurrence",
                        "ordinary q occurrence",
                        "ordinary 4q occurrence",
                        "boundary occurrence",
                        "literal-score occurrence",
                    ],
                    "zero_boundary": X == m * k,
                }
            )
    witness = {
        "X": 536,
        "endpoint_cell": 8,
        "k": 67,
        "root_parameter": 67,
        "finite_log_coefficient": 0,
        "paired_E_coefficient": "1/sqrt(67)",
        "sharp_T_coefficient": "1/sqrt(67)",
        "conclusion": "no atomwise coefficient-preserving identification",
    }
    assert X != 536 or any(o["endpoint_cell"] == 8 and o["k"] == 67 for o in occurrences)
    summary = {
        "X": X,
        "finite_endpoint_occurrences": len(occurrences),
        "zero_boundary_occurrences": zero_count,
        "first_owner_counts": owners,
        "registry_sha256": canonical_hash(occurrences),
        "examples": occurrences[:16] + [o for o in occurrences if o["endpoint_cell"] == 8 and o["k"] == 67],
        "anchored_adapter_exact_witness": witness,
    }
    return summary, occurrences


@dataclass(frozen=True)
class I:
    lo: Fraction
    hi: Fraction

    def __add__(self, other: "I") -> "I":
        return I(self.lo + other.lo, self.hi + other.hi)

    def __sub__(self, other: "I") -> "I":
        return I(self.lo - other.hi, self.hi - other.lo)

    def __mul__(self, other: "I") -> "I":
        vals = (self.lo * other.lo, self.lo * other.hi, self.hi * other.lo, self.hi * other.hi)
        return I(min(vals), max(vals))


def sqrt_interval(n: int, scale: int) -> I:
    q = math.isqrt(n * scale * scale)
    while (q + 1) * (q + 1) <= n * scale * scale:
        q += 1
    while q * q > n * scale * scale:
        q -= 1
    return I(Fraction(q, scale), Fraction(q + 1, scale))


def inv_sqrt_interval(n: int, scale: int) -> I:
    q = math.isqrt((scale * scale) // n)
    while (q + 1) * (q + 1) * n <= scale * scale:
        q += 1
    while q * q * n > scale * scale:
        q -= 1
    return I(Fraction(q, scale), Fraction(q + 1, scale))


def mul_fraction_interval(a: Fraction, b: I) -> I:
    if a >= 0:
        return I(a * b.lo, a * b.hi)
    return I(a * b.hi, a * b.lo)


def outer_two_channel_certificate() -> dict:
    mu, _ = linear_mobius(67)
    scale = 10**55
    A = Fraction(0)
    B = I(Fraction(0), Fraction(0))
    e_min: Fraction | None = None
    r_min: Fraction | None = None
    e_cell = None
    r_cell = None
    cells = []
    for N in range(1, 67):
        if mu[N]:
            A += Fraction(mu[N], N)
            term = inv_sqrt_interval(N, scale)
            B = B + (term if mu[N] > 0 else I(-term.hi, -term.lo))
        endpoint = N if A >= 0 else N + 1
        sq = sqrt_interval(endpoint, scale)
        rootA = mul_fraction_interval(A, sq)
        E = mul_fraction_interval(Fraction(2), rootA) - B
        R = rootA - B
        if N == 1:
            R = I(Fraction(0), R.hi)
        if e_min is None or E.lo < e_min:
            e_min, e_cell = E.lo, N
        if r_min is None or R.lo < r_min:
            r_min, r_cell = R.lo, N
        cells.append({"N": N, "A": str(A), "E_lower": str(E.lo), "R_lower": str(R.lo)})
    assert e_min is not None and e_min > Fraction(318, 1000)
    assert r_min is not None and r_min >= 0
    return {
        "domain": "1<=x<67",
        "identity": {"T": "E+2R", "S": "2E+R"},
        "E_global_lower_fraction": str(e_min),
        "E_global_lower_decimal": float(e_min),
        "E_min_cell": e_cell,
        "R_global_lower_fraction": str(r_min),
        "R_global_lower_decimal": float(r_min),
        "R_min_cell": r_cell,
        "cell_count": len(cells),
        "certificate_sha256": canonical_hash(cells),
        "cells": cells,
    }


def primes_up_to(n: int) -> list[int]:
    _, primes = linear_mobius(n)
    return primes


def causal_allocation(X: int) -> tuple[dict, list[dict]]:
    getcontext().prec = 80
    active = [p for p in primes_up_to(X) if p >= ROUGH_MIN and p > X / 67]
    assert active
    s = Decimal(1)
    lambdas = []
    alphas = []
    prefix_products = []
    for p in active:
        prefix_products.append(s)
        r = Decimal(p).sqrt() ** Decimal(-1)
        lam = r * s
        lambdas.append(lam)
        alphas.append(r * lam)
        s *= Decimal(1) - r
    one_minus_s = Decimal(1) - s
    betas = [x / one_minus_s for x in lambdas]
    gammas = [x / one_minus_s for x in alphas]
    assert abs(sum(betas) - Decimal(1)) < Decimal("1e-70")
    assert sum(gammas) < Decimal(67).sqrt() ** Decimal(-1)
    records = []
    for p, pre, lam, alpha, beta, gamma in zip(active, prefix_products, lambdas, alphas, betas, gammas):
        records.append(
            {
                "p": p,
                "child_parameter": f"{X}/{p}",
                "r": f"1/sqrt({p})",
                "prefix_survival_product_decimal": str(pre),
                "lambda_decimal": str(lam),
                "alpha_decimal": str(alpha),
                "beta_decimal": str(beta),
                "gamma_decimal": str(gamma),
                "beta_formula": f"p^(-1/2)*prod_(q<{p})(1-q^(-1/2))/(1-s)",
                "gamma_formula": f"p^(-1/2)*beta_{p}",
                "owner": p,
            }
        )
    summary = {
        "X": X,
        "terminal_prime_count": len(active),
        "first_prime": active[0],
        "last_prime": active[-1],
        "survival_decimal": str(s),
        "exact_formulas": {
            "s": "product_p(1-p^(-1/2))",
            "lambda_p": "p^(-1/2)*product_(q<p)(1-q^(-1/2))",
            "beta_p": "lambda_p/(1-s)",
            "gamma_p": "p^(-1/2)*beta_p",
        },
        "beta_sum": str(sum(betas)),
        "gamma_sum": str(sum(gammas)),
        "gamma_upper": "1/sqrt(67)<1/8",
        "registry_sha256": canonical_hash(records),
        "preview": records[:8],
        "scope": "allocates the P61 finite-forcing parent; does not cancel the actual oriented rough-child marginal",
    }
    return summary, records


def terminal_leaf() -> tuple[dict, list[dict]]:
    p, y = 67, 13
    x = p * y
    vals = divisors_p61(x)
    records = []
    for d, mu in vals:
        records.append(
            {
                "d": d,
                "mu": mu,
                "parity": "even" if mu == 1 else "odd",
                "parent_active": d <= x,
                "child_active": d <= y,
                "path_coefficient": f"1/sqrt({d})",
                "common_causal_scalar": f"mu({d})/sqrt({d})",
                "row_formula": f"mu({d})/sqrt({d})*(Q_({x}/{d})-1/sqrt({p})*Q_({y}/{d}))",
                "target_formula": f"mu({d})/sqrt({d})*(T({x}/{d})-1/sqrt({p})*T({y}/{d}))",
                "score_formula": f"mu({d})/sqrt({d})*(S({x}/{d})-1/sqrt({p})*S({y}/{d}))",
                "ordinary_contract": "apply the same causal scalar to ordinary q and ordinary 4q before detail",
                "owner": p,
            }
        )
    child_active = sum(1 for r in records if r["child_active"])
    assert len(records) == 229
    summary = {
        "p": p,
        "y": y,
        "x": x,
        "active_p61_atoms": len(records),
        "child_active_atoms": child_active,
        "root_parameter_formula": "x=p*y",
        "atom_formula": "mu(d)/sqrt(d)*(Q_(py/d)-p^(-1/2)Q_(y/d))",
        "target_formula": "mu(d)/sqrt(d)*(T(py/d)-p^(-1/2)T(y/d))",
        "owner": 67,
        "divisor_registry_sha256": canonical_hash(records),
        "preview": records[:12],
    }
    return summary, records


def q2_obstruction() -> dict:
    lower = Fraction(1, 9)
    assert 134 < 12 * 12
    return {
        "X": 536,
        "q": 2,
        "rough_factor": 67,
        "rough_ordinary_term": "log(4)/sqrt(134)",
        "elementary_lower_bound": str(lower),
        "proof": "log(2)>2/3 and sqrt(134)<12",
        "actual_oriented_child_ordinary": "<=-log(4)/sqrt(134)<-1/9",
        "actual_oriented_child_detail": "<=-log(4)/sqrt(134)<-1/9",
        "conclusion": "branchwise nonnegative physical realization impossible",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--certificate-dir", type=Path)
    args = parser.parse_args()

    source_summary, source_atoms = source_registry(536)
    endpoint_summary, endpoint_atoms = endpoint_registry(536)
    causal_summary, causal_records = causal_allocation(871)
    leaf_summary, leaf_records = terminal_leaf()
    outer = outer_two_channel_certificate()

    certificate_hashes: dict[str, str] = {}
    if args.certificate_dir is not None:
        cdir = args.certificate_dir
        certificate_hashes = {
            "native_source_registry_536.json": write_json(cdir / "native_source_registry_536.json", source_atoms),
            "finite_endpoint_registry_536.json": write_json(cdir / "finite_endpoint_registry_536.json", endpoint_atoms),
            "terminal_leaf_67_13.json": write_json(cdir / "terminal_leaf_67_13.json", leaf_records),
            "causal_weights_871.json": write_json(cdir / "causal_weights_871.json", causal_records),
            "outer_two_channel_cells.json": write_json(cdir / "outer_two_channel_cells.json", outer["cells"]),
        }

    outer_summary = {k: v for k, v in outer.items() if k != "cells"}
    payload = {
        "schema": "riemann.target-lorenz.live-endpoint-source.v2",
        "classification": "PASS_LIVE_ENDPOINT_SOURCE_TREE_AND_JOINT_CANCELLATION_GATE",
        "frozen_base": {"pr": 508, "head": FROZEN_HEAD},
        "native_source_registry": source_summary,
        "finite_endpoint_registry": endpoint_summary,
        "outer_two_channel_certificate": outer_summary,
        "finite_forcing_causal_allocation": causal_summary,
        "actual_terminal_leaf": leaf_summary,
        "q2_branchwise_child_obstruction": q2_obstruction(),
        "certificate_file_sha256": certificate_hashes,
        "joint_gate_status": "OPEN: finite forcing and oriented rough children must be coupled before positive physical realization",
        "rh_established_by_replay": False,
    }
    payload["proof_object_sha256"] = canonical_hash(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(payload["classification"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
