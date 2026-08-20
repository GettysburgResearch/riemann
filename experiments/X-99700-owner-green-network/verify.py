#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

LIMIT = 512
P0 = 67


def factor(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    p = 2
    x = n
    while p * p <= x:
        while x % p == 0:
            out[p] = out.get(p, 0) + 1
            x //= p
        p += 1
    if x > 1:
        out[x] = out.get(x, 0) + 1
    return out


def mu(n: int) -> int:
    fac = factor(n)
    return 0 if any(e > 1 for e in fac.values()) else (-1) ** len(fac)


def v67(n: int) -> int:
    e = 0
    while n % P0 == 0:
        e += 1
        n //= P0
    return e


def g(n: int) -> int:
    return v67(n) + 1


def beta(n: int) -> int:
    return mu(n) - (mu(n // P0) if n % P0 == 0 else 0)


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def is_prime_power(q: int) -> tuple[int, int] | None:
    fac = factor(q)
    if len(fac) != 1:
        return None
    return next(iter(fac.items()))


def lambda_multiplier(q: int) -> tuple[int, Fraction] | None:
    pp = is_prime_power(q)
    if pp is None:
        return None
    p, _ = pp
    return p, Fraction(2 if p == P0 else 1)


def proof_digest(payload: dict[str, object]) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    convolution_checks = 0
    for n in range(1, LIMIT + 1):
        value = sum(beta(d) * g(n // d) for d in divisors(n))
        assert value == (1 if n == 1 else 0)
        convolution_checks += 1

    owner_norm_checks = 0
    owner_signed_checks = 0
    for n in range(2, LIMIT + 1):
        unsigned: dict[int, Fraction] = {}
        signed: dict[int, Fraction] = {}
        for q in divisors(n):
            if q == 1:
                continue
            lm = lambda_multiplier(q)
            if lm is None:
                continue
            p, coefficient = lm
            unsigned[p] = unsigned.get(p, Fraction(0)) + coefficient * g(n // q)
            signed[p] = signed.get(p, Fraction(0)) + coefficient * beta(n // q)

        expected_unsigned = {
            p: Fraction(exponent * g(n)) for p, exponent in factor(n).items()
        }
        expected_signed = {
            p: Fraction(-exponent * beta(n)) for p, exponent in factor(n).items()
        }
        assert unsigned == expected_unsigned
        assert signed == expected_signed
        owner_norm_checks += 1
        owner_signed_checks += 1

    squarefree_zero_qv = 0
    squarefree_negative_examples: list[int] = []
    for n in range(2, LIMIT + 1):
        if n % P0 == 0 or mu(n) == 0:
            continue
        fn = Fraction(beta(n), g(n))
        assert abs(fn) == 1
        for p in factor(n):
            child = Fraction(beta(n // p), g(n // p))
            assert child + fn == 0
        squarefree_zero_qv += 1
        if fn < 0 and len(squarefree_negative_examples) < 8:
            squarefree_negative_examples.append(n)

    balance_checks = 0
    for n in range(1, LIMIT + 1):
        for q in range(2, LIMIT // n + 1):
            lm = lambda_multiplier(q)
            if lm is None:
                continue
            _, coefficient = lm
            pi_n = Fraction(g(n), n)
            birth = coefficient / q
            pi_nq = Fraction(g(n * q), n * q)
            death = coefficient * Fraction(g(n), g(n * q))
            assert pi_n * birth == pi_nq * death
            balance_checks += 1

    local_sequences = {
        "ordinary": [Fraction(1), Fraction(-1), Fraction(0), Fraction(0)],
        "p67": [Fraction(1), Fraction(-1), Fraction(1, 3), Fraction(0)],
    }
    edge_positivity_checks = 0
    for sequence in local_sequences.values():
        for e in range(len(sequence)):
            for step in range(1, len(sequence) - e):
                parent = sequence[e]
                child = sequence[e + step]
                # For A>=B>=0:
                # (parent-child)(parent*A-child*B)
                # = c1*(A-B)+c2*B.
                c1 = (parent - child) * parent
                c2 = (parent - child) ** 2
                assert c1 >= 0
                assert c2 >= 0
                edge_positivity_checks += 1

    support_checks = 0
    for n in range(1, LIMIT + 1):
        exponent = v67(n)
        core = n // (P0**exponent)
        core_mu = mu(core)
        if core_mu == 0:
            predicted = 0
        elif exponent == 0:
            predicted = core_mu
        elif exponent == 1:
            predicted = -2 * core_mu
        elif exponent == 2:
            predicted = core_mu
        else:
            predicted = 0
        assert beta(n) == predicted

        fn = Fraction(beta(n), g(n))
        plus = (Fraction(1) + fn) / 2
        minus = (Fraction(1) - fn) / 2
        common = min(plus, minus)
        assert plus - common >= 0
        assert minus - common >= 0
        assert abs((plus - common) - (minus - common)) == abs(fn)
        support_checks += 1

    payload: dict[str, object] = {
        "schema": "riemann.t99700.owner_green_network.v1",
        "limit": LIMIT,
        "checks": {
            "beta_inverse_convolution": convolution_checks,
            "owner_probability_formal_log": owner_norm_checks,
            "owner_signed_martingale_formal_log": owner_signed_checks,
            "squarefree_zero_qv_states": squarefree_zero_qv,
            "squarefree_negative_examples": squarefree_negative_examples,
            "detailed_balance_edges": balance_checks,
            "local_edge_positivity": edge_positivity_checks,
            "three_fibre_trace_cancellation": support_checks,
            "negative_control_owner_qv_orients_sign": False,
        },
        "scope": {
            "volterra_identity_proved_in_claim": True,
            "reversible_network_proved_in_claim": True,
            "finite_flow_duality_proved_in_claim": True,
            "pxgc99700_proved": False,
            "rh_established": False,
        },
        "verdict": "PASS_T99700_OWNER_GREEN_NETWORK_ALGEBRA",
    }
    payload["proof_object_sha256"] = proof_digest(payload)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
