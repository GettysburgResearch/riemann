#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, math
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parent


def mobius(n: int) -> int:
    if n == 1:
        return 1
    x = n
    p = 2
    parity = 0
    while p * p <= x:
        if x % p == 0:
            x //= p
            parity ^= 1
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1 if p == 2 else 2
    if x > 1:
        parity ^= 1
    return -1 if parity else 1


def conv(a: List[int], b: List[int], N: int) -> List[int]:
    out = [0] * (N + 1)
    for d in range(1, min(N, len(a)-1) + 1):
        if not a[d]:
            continue
        for e in range(1, min(N // d, len(b)-1) + 1):
            if b[e]:
                out[d*e] += a[d] * b[e]
    return out


def conv_pow(a: List[int], k: int, N: int) -> List[int]:
    out = [0] * (N + 1)
    out[1] = 1
    for _ in range(k):
        out = conv(out, a, N)
    return out


def packet_A(K: int, V: int, N: int) -> List[int]:
    muV = [0] * (N + 1)
    ones = [0] + [1] * N
    for n in range(1, min(V, N) + 1):
        muV[n] = mobius(n)
    out = [0] * (N + 1)
    for j in range(1, K + 1):
        term = conv(conv_pow(muV, j, N), conv_pow(ones, j-1, N), N)
        coeff = (-1) ** (j - 1) * math.comb(K, j)
        for n in range(1, N + 1):
            out[n] += coeff * term[n]
    return out


def mertens(n: int) -> int:
    return sum(mobius(k) for k in range(1, max(0, n) + 1))


def geometric_difference(D: int, K: int, num: int, den: int) -> int:
    total = 0
    for r in range(K + 1):
        x = D * (num ** r) // (den ** r)
        total += (-1) ** r * math.comb(K, r) * mertens(x)
    return total


def main() -> int:
    cert = json.loads((ROOT / "certificates/synthetic.json").read_text())
    V = int(cert["V"])
    orders = [int(k) for k in cert["orders"]]
    q0 = int(cert["q0"])
    D = int(cert["D"])
    num = int(cert["ratio_numerator"])
    den = int(cert["ratio_denominator"])

    if V < 1 or len(orders) < 2 or min(orders) < 1:
        raise ValueError("invalid V or order sequence")
    if q0 < 2 or D < 1 or not (0 < num < den):
        raise ValueError("invalid fixed-log or ratio parameters")

    recon: Dict[str, Dict[str, int]] = {}
    for K in orders:
        N = V ** K
        A = packet_A(K, V, N)
        mismatches = sum(A[n] != mobius(n) for n in range(1, N + 1))
        fixed_slice_mismatches = sum(
            A[m] != mobius(m) for m in range(1, N // q0 + 1)
        )
        recon[str(K)] = {
            "endpoint": N,
            "mobius_mismatches": mismatches,
            "fixed_log_slice_mismatches": fixed_slice_mismatches,
        }
        if mismatches or fixed_slice_mismatches:
            raise AssertionError(f"order {K} failed exact Mobius reconstruction")

    first = geometric_difference(D, 1, num, den)
    differences = {
        str(K): geometric_difference(D, K, num, den) for K in orders
    }
    if first != mertens(D) - mertens(D * num // den):
        raise AssertionError("first difference normalization failure")
    if all(differences[str(K)] == first for K in orders if K > 1):
        raise AssertionError("control did not separate first and higher differences")

    result = {
        "schema": cert["schema"],
        "verified": True,
        "reconstruction": recon,
        "D": D,
        "first_cell_increment": first,
        "geometric_differences": differences,
        "verdict": "EXACT_FIXED_LOG_SOURCE_IS_MOBIUS_AND_NOT_AUTOMATICALLY_KTH_DIFFERENCED",
        "proof_boundary": (
            "Finite Dirichlet-convolution and integer Mertens algebra only; "
            "no asymptotic estimate or RH conclusion."
        ),
    }
    payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(payload).hexdigest()
    out = ROOT / "results/synthetic-verification.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
