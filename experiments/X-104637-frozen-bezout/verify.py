#!/usr/bin/env python3
"""Exact polynomial replay for L-104637."""
from fractions import Fraction as Q
from pathlib import Path
import argparse, hashlib, json


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    out = [Q(0)] * max(len(p), len(q))
    for i, a in enumerate(p):
        out[i] += a
    for i, a in enumerate(q):
        out[i] += a
    return trim(out)


def mul(p, q):
    out = [Q(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return trim(out)


def scale(p, c):
    return trim([c * a for a in p])


def power(p, n):
    out = [Q(1)]
    for _ in range(n):
        out = mul(out, p)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("output", nargs="?", type=Path)
    args = ap.parse_args()

    x = [Q(0), Q(1)]
    two_minus_x = [Q(2), Q(-1)]
    one_minus_x = [Q(1), Q(-1)]
    A = [Q(11, 2), Q(-25, 2), Q(15), Q(-10), Q(7, 2), Q(-1, 2)]

    bezout = add(mul(x, A), scale(mul(two_minus_x, power(one_minus_x, 5)), Q(1, 2)))
    assert bezout == [Q(1)]

    M00 = mul(two_minus_x, A)
    M01 = scale(two_minus_x, Q(1, 2))
    M10 = power(one_minus_x, 5)

    d0 = x
    d1 = mul(two_minus_x, power(one_minus_x, 5))
    n0 = two_minus_x
    n1 = mul(x, power(one_minus_x, 5))

    row0 = add(mul(M00, d0), mul(M01, d1))
    row1 = mul(M10, d0)
    assert row0 == n0
    assert row1 == n1
    assert max(len(M00) - 1, len(M01) - 1, len(M10) - 1) == 6

    checks = {
        "bezout": [str(c) for c in bezout],
        "M00": [str(c) for c in M00],
        "M01": [str(c) for c in M01],
        "M10": [str(c) for c in M10],
        "max_degree": 6,
        "module_row0": True,
        "module_row1": True,
    }
    proof_payload = json.dumps(checks, sort_keys=True, separators=(",", ":")).encode()
    result = {
        "schema": "riemann.l104637.frozen_bezout.v1",
        "verdict": "PASS_L104637_FROZEN_CARRIER_BEZOUT",
        "checks": checks,
        "proof_object_sha256": hashlib.sha256(proof_payload).hexdigest(),
        "scope": {
            "source_module_identity_proved_exact": True,
            "model_space_transport_proved": False,
            "fractrans104635_proved": False,
            "ninety_percent_established": False,
            "rh_established": False,
        },
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(result["verdict"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
