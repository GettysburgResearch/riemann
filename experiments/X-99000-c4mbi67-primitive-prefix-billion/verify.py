#!/usr/bin/env python3
"""Exact replay for T-99000.

The default replay independently recomputes the rational enclosure through
100,000, checks the retained 10^9 transcript, checks the sparse dictionary, and
certifies the finite threshold-complex counterexample.  Set FULL=1 in replay.sh
to rerun the complete C++ scan through 10^9.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Dict, List, Tuple

K = 40
SCALE = 1 << K
SCALE2 = SCALE * SCALE
EXPECTED_FULL: Dict[str, str] = {
    "N": "1000000000",
    "K": "40",
    "scale": "1099511627776",
    "nonzero": "759908859",
    "min_lower_num": "1226685126915",
    "min_lower_at": "48433",
    "min_upper_num": "1226685458193",
    "min_upper_at": "48433",
    "final_lower_num": "6792531895707",
    "final_upper_num": "6799371075387",
    "PASS": "YES",
}


def mobius_linear(n: int) -> List[int]:
    mu = [0] * (n + 1)
    lp = [0] * (n + 1)
    primes: List[int] = []
    mu[1] = 1
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if p > lp[i] or i * p > n:
                break
            lp[i * p] = p
            mu[i * p] = 0 if p == lp[i] else -mu[i]
    return mu


def coefficient(mu: List[int], n: int) -> int:
    a = (6 if n == 1 else 0) - 6 * mu[n]
    if n % 2 == 0:
        a += 9 * mu[n // 2]
    if n % 4 == 0:
        a -= 3 * mu[n // 4]
    return a


def invsqrt_floor(n: int, scale: int = SCALE) -> int:
    """Return floor(scale/sqrt(n)) using only integer arithmetic."""
    q = math.isqrt((scale * scale) // n)
    assert q * q * n <= scale * scale
    assert (q + 1) * (q + 1) * n > scale * scale
    return q


def exact_prefix_scan(nmax: int) -> Dict[str, int]:
    mu = mobius_linear(nmax)
    lo = hi = 0
    min_lo = min_hi = 0
    min_lo_n = min_hi_n = 1
    nonzero = 0
    for n in range(1, nmax + 1):
        a = coefficient(mu, n)
        if a:
            nonzero += 1
            q = invsqrt_floor(n)
            if a > 0:
                lo += a * q
                hi += a * (q + 1)
            else:
                lo += a * (q + 1)
                hi += a * q
        if n >= 2:
            if n == 2 or lo < min_lo:
                min_lo, min_lo_n = lo, n
            if n == 2 or hi < min_hi:
                min_hi, min_hi_n = hi, n
    return {
        "N": nmax,
        "nonzero": nonzero,
        "min_lower_num": min_lo,
        "min_lower_at": min_lo_n,
        "min_upper_num": min_hi,
        "min_upper_at": min_hi_n,
        "final_lower_num": lo,
        "final_upper_num": hi,
    }


def sparse_dictionary_check(limit: int = 2000) -> int:
    mu = mobius_linear(limit)
    checks = 0
    for n in range(1, limit + 1):
        # q(1)=0, q(2)=15, q(4)=3, and q(m)=6 otherwise.
        conv = 0
        for d in range(1, int(math.isqrt(n)) + 1):
            if n % d:
                continue
            for e in ({d, n // d} if d * d != n else {d}):
                q = 0 if e == 1 else (15 if e == 2 else (3 if e == 4 else 6))
                conv += mu[n // e] * q
        assert conv == coefficient(mu, n), (n, conv, coefficient(mu, n))
        checks += 1
    return checks


def parse_retained(path: Path) -> Dict[str, str]:
    out: Dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        parts = raw.split()
        if not parts:
            continue
        if parts[0] in {"N", "K", "scale", "nonzero", "min_lower_num", "min_upper_num",
                        "final_lower_num", "final_upper_num", "PASS"}:
            out[parts[0]] = parts[1]
        elif parts[0] == "min_lower":
            out["min_lower_at"] = parts[-1]
        elif parts[0] == "min_upper":
            out["min_upper_at"] = parts[-1]
    return out


def finite_threshold_counterexample(scale_bits: int = 60) -> Tuple[int, int, int]:
    """Enclose the restricted-label F(26) exactly.

    Labels are (threshold cost, square denominator of activity):
      two labels (2,2), one label (2,8), and primes 3,5,7,11,13.
    For a subset, activity is 1/sqrt(product square-denominators).
    Returns (lower_num, upper_num, scale), both bounds strictly negative.
    """
    scale = 1 << scale_bits
    labels = [(2, 2), (2, 2), (2, 8), (3, 3), (5, 5), (7, 7), (11, 11), (13, 13)]
    lo = hi = 0
    for mask in range(1, 1 << len(labels)):
        cost = 1
        den = 1
        card = 0
        for i, (c, d) in enumerate(labels):
            if mask & (1 << i):
                cost *= c
                den *= d
                card += 1
        if cost > 26:
            continue
        q = math.isqrt((scale * scale) // den)
        assert q * q * den <= scale * scale < (q + 1) * (q + 1) * den
        sign = 1 if card % 2 else -1
        if sign > 0:
            lo += q
            hi += q + 1
        else:
            lo -= q + 1
            hi -= q
    assert hi < 0, (lo, hi)
    return lo, hi, scale


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=100_000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    here = Path(__file__).resolve().parent
    retained_path = here / "results" / "cprefix_exact_1e9.txt"
    retained = parse_retained(retained_path)
    for key, expected in EXPECTED_FULL.items():
        assert retained.get(key) == expected, (key, retained.get(key), expected)

    scan = exact_prefix_scan(args.limit)
    assert scan["min_lower_num"] > 0
    if args.limit >= 48_433:
        assert scan["min_lower_num"] == int(EXPECTED_FULL["min_lower_num"])
        assert scan["min_lower_at"] == 48_433
        assert scan["min_upper_num"] == int(EXPECTED_FULL["min_upper_num"])
        assert scan["min_upper_at"] == 48_433

    dictionary_checks = sparse_dictionary_check()
    cx_lo, cx_hi, cx_scale = finite_threshold_counterexample()

    proof_payload = {
        "verdict": "PASS_T99000_PRIMITIVE_PREFIX_BILLION_EXACT_REPLAY",
        "status": {
            "primitive_prefix_through_1e9": True,
            "c4mbi67_global_sign": False,
            "rh_established": False,
        },
        "fast_exact_scan": scan,
        "retained_full_scan": {k: retained[k] for k in sorted(retained)},
        "dictionary_checks": dictionary_checks,
        "finite_pointwise_port_counterexample": {
            "threshold": 26,
            "lower_num": cx_lo,
            "upper_num": cx_hi,
            "scale": cx_scale,
            "upper_is_negative": cx_hi < 0,
        },
    }
    canonical = json.dumps(proof_payload, sort_keys=True, separators=(",", ":")).encode()
    proof_payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()

    text = json.dumps(proof_payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8", newline="\n")
    print(proof_payload["verdict"])
    print(proof_payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
