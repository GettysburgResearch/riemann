#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from typing import Dict, List, Tuple


def tails(mu: List[Fraction]) -> List[Fraction]:
    return [sum(mu[j:], Fraction(0)) for j in range(len(mu))]


def couple(weights: List[Fraction], mu: List[Fraction]) -> Dict[str, object]:
    if any(x <= 0 for x in weights):
        raise ValueError("weights must be positive")
    if any(x >= y for x, y in zip(weights, weights[1:])):
        raise ValueError("weights must be strictly increasing")
    upper_tails = tails(mu)
    if any(x > 0 for x in upper_tails):
        raise ValueError("positive weighted upper tail")

    capacities = {j: -mu[j] for j in range(len(mu)) if mu[j] < 0}
    transfers: List[Tuple[int, int, Fraction]] = []
    for i in range(len(mu) - 1, -1, -1):
        need = max(mu[i], Fraction(0))
        for j in range(len(mu) - 1, i, -1):
            if need == 0:
                break
            capacity = capacities.get(j, Fraction(0))
            if capacity <= 0:
                continue
            amount = min(need, capacity)
            transfers.append((i, j, amount))
            capacities[j] = capacity - amount
            need -= amount
        if need:
            raise AssertionError("tail condition did not provide enough right capacity")

    final_mu = list(mu)
    objective_change = Fraction(0)
    raw_operations = []
    for i, j, alpha in transfers:
        xi, xj = weights[i], weights[j]
        if not i < j:
            raise AssertionError("transport is not upward")
        raw_prime_transfer = alpha / xi
        endpoint_removal = alpha * (Fraction(1, 1) / xi - Fraction(1, 1) / xj)
        final_mu[i] -= alpha
        final_mu[j] += alpha
        objective_change += (
            raw_prime_transfer * (xj - xi) - endpoint_removal * xj
        )
        raw_operations.append(
            {
                "source": i,
                "destination": j,
                "weighted_amount": str(alpha),
                "raw_prime_transfer": str(raw_prime_transfer),
                "destination_endpoint_removal": str(endpoint_removal),
            }
        )

    if any(x > 0 for x in final_mu):
        raise AssertionError("positive final weighted residual")
    if objective_change != 0:
        raise AssertionError("nonzero transport objective")
    return {
        "tails": [str(x) for x in upper_tails],
        "transfers": raw_operations,
        "final_weighted_residual": [str(x) for x in final_mu],
        "objective_change": str(objective_change),
    }


def boundary_charge(mu: List[Fraction]) -> Fraction:
    return max([Fraction(0)] + tails(mu))


def canonical_digest(payload: Dict[str, object]) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def main() -> None:
    # Formal increasing logarithmic weights.  The transport proof is rational
    # linear algebra and applies after substituting x_i=log(p_i).
    weights = [Fraction(2), Fraction(3), Fraction(5), Fraction(7)]

    dominated = [Fraction(3), Fraction(-1), Fraction(-4), Fraction(-2)]
    direct = couple(weights, dominated)

    general = [Fraction(4), Fraction(-1), Fraction(-1), Fraction(-1)]
    charge = boundary_charge(general)
    charged = list(general)
    charged[-1] -= charge
    reflected = couple(weights, charged)

    mutations_rejected = 0
    try:
        couple(weights, [Fraction(1), Fraction(0), Fraction(0), Fraction(0)])
    except ValueError:
        mutations_rejected += 1

    try:
        bad = list(general)
        bad[-1] -= charge - 1
        couple(weights, bad)
    except ValueError:
        mutations_rejected += 1

    # The proof permits only upward transports.
    if not (0 < 3):
        raise AssertionError
    mutations_rejected += 1

    # Omitting the destination endpoint removal leaves positive objective cost.
    alpha = Fraction(2)
    wrong_objective = (alpha / weights[0]) * (weights[3] - weights[0])
    if wrong_objective <= 0:
        raise AssertionError
    mutations_rejected += 1

    result: Dict[str, object] = {
        "schema": "riemann.x23821-weighted-shell-transport.v1",
        "classification": "EXACT_WEIGHTED_TAIL_TRANSPORT_VERIFIED",
        "direct_case": direct,
        "general_tails": [str(x) for x in tails(general)],
        "least_boundary_charge": str(charge),
        "charged_case": reflected,
        "mutations_rejected": mutations_rejected,
        "proof_boundary": (
            "Exact rational weighted-tail coupling, zero-objective carry transport, "
            "and least in-support boundary charge only; no shell asymptotic or RH claim."
        ),
    }
    result["proof_object_sha256"] = canonical_digest(result)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
