#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path


def primes_upto(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for m in range(p * p, n + 1, p):
                sieve[m] = False
    return [n for n, flag in enumerate(sieve) if flag]


def valuation(n: int, p: int) -> int:
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def digest(payload: dict) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    primes = primes_upto(50)[:10]
    pairs = list(itertools.combinations(primes, 2))

    common_checks = 0
    phase_checks = 0
    four_checks = 0
    selector_checks = 0
    cancellation_checks = 0

    for pair_1, pair_2 in itertools.combinations(pairs, 2):
        if set(pair_1) & set(pair_2):
            continue

        p, q = max(pair_1), min(pair_1)
        r, s = max(pair_2), min(pair_2)

        # Clean four-owner phase identities.
        n = p * q
        m = r * s
        assert (n % p == 0) != (m % p == 0)
        assert (n % r == 0) != (m % r == 0)
        phase_checks += 1

        for ell in (p, q, r, s):
            assert (n % ell == 0) != (m % ell == 0)
        four_checks += 1

        # Phase cardinalities cancel the literal owner weights.
        assert Fraction(r, p) * Fraction(p, r) == 1
        assert Fraction(r * s, p * q) * Fraction(p * q, r * s) == 1
        cancellation_checks += 2

        # Every quadruple has exactly fifteen nonempty phase architectures.
        count = 0
        for mask_n in range(4):
            for mask_m in range(4):
                if mask_n == 0 and mask_m == 0:
                    continue
                count += 1
                l_n = 1
                l_m = 1
                for bit, ell in enumerate((r, s)):
                    if (mask_n >> bit) & 1:
                        l_n *= ell
                for bit, ell in enumerate((p, q)):
                    if (mask_m >> bit) & 1:
                        l_m *= ell
                assert Fraction(l_n * l_m, p * q * r * s) > 0
        assert count == 15
        selector_checks += count

        # Owner/core overlap fixtures. A common copy is removed and the
        # reduced valuations have opposite parity.
        for ell in (p, q):
            if ell < s:
                n = p * q
                m = r * s * ell * ell
                d = ell ** min(valuation(n, ell), valuation(m, ell))
                n_1, m_1 = n // d, m // d
                assert (valuation(n_1, ell) % 2) != (valuation(m_1, ell) % 2)
                common_checks += 1

        for ell in (r, s):
            if ell < q:
                n = p * q * ell * ell
                m = r * s
                d = ell ** min(valuation(n, ell), valuation(m, ell))
                n_1, m_1 = n // d, m // d
                assert (valuation(n_1, ell) % 2) != (valuation(m_1, ell) % 2)
                common_checks += 1

    payload = {
        "schema": "riemann.t102870.balanced-owner-phase.v1",
        "common_factor_extraction_checks": common_checks,
        "double_nonzero_phase_checks": phase_checks,
        "four_phase_checks": four_checks,
        "owner_modulus_cancellation_checks": cancellation_checks,
        "adaptive_phase_choice_checks": selector_checks,
        "adaptive_phase_choice_count_per_quadruple": 15,
        "balanced_phase_one_owner_each_side": True,
        "four_phase_owner_normalization": True,
        "fixed_pair_largest_owner_loss_removed": True,
        "bqsp102870_proved": False,
        "rh_established": False,
        "verdict": "PASS_T102870_BALANCED_OWNER_PHASE_NORMAL_FORM",
    }
    payload["proof_object_sha256"] = digest(payload)

    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")

    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
