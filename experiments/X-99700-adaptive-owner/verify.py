#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

VERDICT = "PASS_T99700_ADAPTIVE_LOG_OWNER_HIERARCHY"


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


def mobius(n: int) -> int:
    fs = factor(n)
    if any(e > 1 for e in fs.values()):
        return 0
    return -1 if len(fs) % 2 else 1


def divisors(n: int) -> list[int]:
    ds = [1]
    for p, e in factor(n).items():
        old = list(ds)
        mult = 1
        for _ in range(e):
            mult *= p
            ds += [d * mult for d in old]
    return sorted(ds)


def formal_log(n: int) -> int:
    # Any positive additive prime weights may replace actual logarithms in the
    # algebraic identities. Using the prime itself keeps the replay exact.
    return sum(p * e for p, e in factor(n).items())


def ell(n: int, k: int) -> int:
    return formal_log(n) ** k


def lambda_k(n: int, k: int) -> int:
    return sum(mobius(d) * ell(n // d, k) for d in divisors(n))


def q(n: int) -> int:
    ans = 6 if n == 1 else 0
    ans -= 6 * mobius(n)
    if n % 2 == 0:
        ans += 9 * mobius(n // 2)
    if n % 4 == 0:
        ans -= 3 * mobius(n // 4)
    return ans


def a(n: int) -> int:
    return sum(q(d) for d in divisors(n))


def beta(n: int) -> int:
    return mobius(n) - (mobius(n // 67) if n % 67 == 0 else 0)


def g(n: int) -> int:
    return factor(n).get(67, 0) + 1


def prime_power_divisors(n: int) -> list[int]:
    out = []
    for p, e in factor(n).items():
        qv = 1
        for _ in range(e):
            qv *= p
            out.append(qv)
    return out


def lambda_g(qv: int) -> int:
    fs = factor(qv)
    if len(fs) != 1:
        return 0
    p = next(iter(fs))
    return (2 if p == 67 else 1) * p  # formal log weight


def main() -> None:
    conv_checks = 0
    for n in range(1, 1001):
        want = 0 if n == 1 else (15 if n == 2 else (3 if n == 4 else 6))
        assert a(n) == want
        conv_checks += 1

    lambda_checks = 0
    completion_checks = 0
    for k in range(0, 7):
        for n in range(1, 501):
            lk = lambda_k(n, k)
            assert lk >= 0
            lhs = sum(q(d) * ell(n // d, k) for d in divisors(n))
            rhs = sum(a(d) * lambda_k(n // d, k) for d in divisors(n))
            assert lhs == rhs
            assert rhs >= 0
            lambda_checks += 1
            completion_checks += 1

    counterexamples: dict[str, dict[str, int]] = {}
    source_primes = [2, 3, 5, 7, 11, 13, 17, 19]
    import math
    for k in range(1, 7):
        m = 1
        for p in source_primes[:k]:
            m *= p
        before = lambda_k(m, k)
        after = lambda_k(67 * m, k)
        expected = math.factorial(k)
        for p in source_primes[:k]:
            expected *= p
        assert before == expected
        assert after == 0
        assert after - before == -expected < 0
        counterexamples[str(k)] = {
            "m": m,
            "before": before,
            "after": after,
            "defect": after - before,
        }

    convolution_checks = 0
    owner_checks = 0
    zero_dissipation_checks = 0
    positive_variance_witnesses = 0
    for n in range(1, 10001):
        bg = sum(beta(d) * g(n // d) for d in divisors(n))
        assert bg == (1 if n == 1 else 0)
        convolution_checks += 1
        if n == 1:
            continue
        L = formal_log(n)
        pp = prime_power_divisors(n)
        rhs_g = sum(lambda_g(qv) * g(n // qv) for qv in pp)
        assert g(n) * L == rhs_g
        rhs_b = sum(lambda_g(qv) * beta(n // qv) for qv in pp)
        assert beta(n) * L == -rhs_b
        an = Fraction(beta(n), g(n))
        mean_child = sum(
            Fraction(lambda_g(qv) * g(n // qv), g(n) * L)
            * Fraction(beta(n // qv), g(n // qv))
            for qv in pp
        )
        assert mean_child == -an
        owner_checks += 1
        fs = factor(n)
        if all(e == 1 for e in fs.values()) and fs.get(67, 0) <= 1:
            for qv in pp:
                assert Fraction(beta(n // qv), g(n // qv)) == -an
            zero_dissipation_checks += 1
        second = sum(
            Fraction(lambda_g(qv) * g(n // qv), g(n) * L)
            * Fraction(beta(n // qv), g(n // qv)) ** 2
            for qv in pp
        )
        variance = second - mean_child**2
        assert variance >= 0
        if variance > 0:
            positive_variance_witnesses += 1

    core = {
        "schema": "riemann.t99700.adaptive-owner.v1",
        "classification": VERDICT,
        "q_completion_checks": conv_checks,
        "generalized_lambda_checks": lambda_checks,
        "positive_completion_checks": completion_checks,
        "fixed_order_counterexamples": counterexamples,
        "beta_g_convolution_checks": convolution_checks,
        "owner_eigenfunction_checks": owner_checks,
        "zero_dissipation_squarefree_checks": zero_dissipation_checks,
        "positive_variance_witnesses": positive_variance_witnesses,
        "fixed_order_closure_proved": False,
        "phase_adaptive_carleson_proved": False,
        "rh_established": False,
    }
    canonical = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    core["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    text = json.dumps(core, indent=2, sort_keys=True) + "\n"

    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    print(VERDICT)
    print(core["proof_object_sha256"])


if __name__ == "__main__":
    main()
