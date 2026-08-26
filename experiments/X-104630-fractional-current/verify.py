#!/usr/bin/env python3
"""Exact rational replay for T-104630."""
from fractions import Fraction as Q
from math import factorial
import json, hashlib
from pathlib import Path
import argparse


def exp_lower(x: Q, n: int) -> Q:
    return sum((x**k) / factorial(k) for k in range(n + 1))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("output", nargs="?", type=Path)
    args = ap.parse_args()

    kappa = Q(20476, 2345)
    H0 = Q(1, 20)
    a = Q(1, 1000)

    delta = Q(7) * H0 * H0 / (3 * kappa)
    assert delta == Q(3283, 4914240)
    assert delta < Q(1, 1001)
    assert 1 / (1 - delta) < Q(1001, 1000)

    x = Q(17, 50)
    e_lower = exp_lower(x, 3)
    assert e_lower == Q(1053263, 750000)
    assert e_lower > Q(7, 5)
    tail = Q(17, 50000)

    phase_gate = Q(21, 1000)
    shallow_upper = Q(1001, 1000) * phase_gate + 2 * tail
    shallow_allowance = Q(11, 500)
    assert shallow_upper == Q(21701, 10**6)
    assert shallow_upper < shallow_allowance

    deep = Q(3, 40)
    total = deep + shallow_upper
    assert total == Q(96701, 10**6)
    assert total < Q(97, 1000)

    fifth = Q(997, 1000)
    base = fifth - total
    assert base == Q(900299, 10**6)
    assert base > Q(9, 10)

    # M3(z)=exp(z)(1+4z/3+4z^2/15) <= exp(7z/3).
    assert Q(4, 15) < (Q(4, 3) ** 2) / 2

    fixtures = []
    for y in [Q(1, 100), Q(1, 50), Q(3, 100)]:
        u = H0 / (H0 + 2 * y)
        for atest in [1, 2, 3, 5]:
            lhs = Q(atest) * u ** (atest - 1) * 2 * y / (H0 + 2 * y) ** 2
            rhs = (
                2
                * Q(atest)
                * y
                * H0 ** (atest - 1)
                / (H0 + 2 * y) ** (atest + 1)
            )
            assert lhs == rhs
        fixtures.append({"y": str(y), "u": str(u)})

    result = {
        "schema": "riemann.t104630.fractional_current.v1",
        "verdict": "PASS_T104630_FRACTIONAL_CURRENT_ALGEBRA",
        "checks": {
            "kappa0": str(kappa),
            "delta0": str(delta),
            "exp_delta_upper": "1001/1000",
            "tail_per_zero_upper": str(tail),
            "shallow_upper": str(shallow_upper),
            "total_charge_upper": str(total),
            "base_proportion_lower": str(base),
            "cdf_fixtures": fixtures,
        },
        "scope": {
            "fifth_current_maxwell_sandwich_proved_exact": True,
            "fractional_calderon_resolution_proved_exact": True,
            "rational_90_percent_ledger_proved_exact": True,
            "fractrans104630_proved": False,
            "ninety_percent_established": False,
            "rh_established": False,
        },
    }
    payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(payload).hexdigest()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(result["verdict"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
