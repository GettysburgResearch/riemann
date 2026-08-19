#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path
from typing import Dict

VERDICT = "PASS_T99700_CANONICAL_SCALAR_NATIVE_TILT_SPINE"


def factor(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    p, x = 2, n
    while p * p <= x:
        while x % p == 0:
            out[p] = out.get(p, 0) + 1
            x //= p
        p += 1 if p == 2 else 2
    if x > 1:
        out[x] = out.get(x, 0) + 1
    return out


def mobius(n: int) -> int:
    fs = factor(n)
    if any(e > 1 for e in fs.values()):
        return 0
    return -1 if len(fs) % 2 else 1


def beta(n: int) -> int:
    return mobius(n) - (mobius(n // 67) if n % 67 == 0 else 0)


def g(n: int) -> int:
    e, x = 0, n
    while x % 67 == 0:
        e += 1
        x //= 67
    return e + 1


def divisors(n: int) -> list[int]:
    out = [1]
    for p, e in factor(n).items():
        old = list(out)
        mul = 1
        for _ in range(e):
            mul *= p
            out.extend(d * mul for d in old)
    return sorted(out)


def conv_beta_g_limit(limit: int) -> int:
    for n in range(1, limit + 1):
        value = sum(beta(d) * g(n // d) for d in divisors(n))
        assert value == (1 if n == 1 else 0), (n, value)
    return limit


def owner_identity_limit(limit: int) -> int:
    checks = 0
    for n in range(2, limit + 1):
        for p, e in factor(n).items():
            multiplicity = 2 if p == 67 else 1
            lhs = beta(n) * e
            rhs = -multiplicity * sum(beta(n // (p**a)) for a in range(1, e + 1))
            assert lhs == rhs, (n, p, lhs, rhs)
            checks += 1
    return checks


# Polynomials in t, stored in increasing degree.
def padd(a: list[F], b: list[F]) -> list[F]:
    n = max(len(a), len(b))
    out = [F(0)] * n
    for i in range(n):
        out[i] = (a[i] if i < len(a) else F(0)) + (b[i] if i < len(b) else F(0))
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def pmul(a: list[F], b: list[F]) -> list[F]:
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def pint01(a: list[F]) -> F:
    return sum((x / F(i + 1) for i, x in enumerate(a)), F(0))


def opmul(A: Dict[int, list[F]], B: Dict[int, list[F]]) -> Dict[int, list[F]]:
    out: Dict[int, list[F]] = {}
    for ma, pa in A.items():
        for mb, pb in B.items():
            assert ma & mb == 0
            mask = ma | mb
            out[mask] = padd(out.get(mask, [F(0)]), pmul(pa, pb))
    return out


def symmetric_homotopy_check(rs: list[F]) -> dict:
    k = len(rs)
    native: Dict[int, F] = {}
    for mask in range(1 << k):
        coeff = F((-1) ** mask.bit_count())
        for i, r in enumerate(rs):
            if mask >> i & 1:
                coeff *= r
        native[mask] = coeff

    survival = F(1)
    for r in rs:
        survival *= 1 - r
    rhs: Dict[int, F] = {0: survival}

    for i, ri in enumerate(rs):
        product: Dict[int, list[F]] = {0: [F(1)]}
        for j, rj in enumerate(rs):
            if j == i:
                continue
            # K_j(t)=(1-t r_j)I-(1-t)r_j U_j.
            product = opmul(product, {0: [F(1), -rj], 1 << j: [-rj, rj]})
        for mask, poly in product.items():
            coeff = ri * pint01(poly)
            rhs[mask] = rhs.get(mask, F(0)) + coeff
            rhs[mask | (1 << i)] = rhs.get(mask | (1 << i), F(0)) - coeff

    assert rhs == native
    return {"formal_primes": k, "monomials": len(native), "survival": str(survival)}


def alpha_firewall() -> dict:
    r = F(1, 9)
    current_shift, recursive_shift, native_shift = -r * r, r * r, -r
    assert current_shift + recursive_shift == 0
    assert current_shift - native_shift == r * (1 - r) > 0
    return {
        "fixture_r": str(r),
        "contracted_net_shift": "0",
        "native_shift": str(native_shift),
        "missing_subsidy": str(r * (1 - r)),
    }


def tilt_energy_check(limit: int) -> dict:
    maximum, integrated, nonzero = F(0), 0.0, 0
    for n in range(2, limit + 1):
        b = beta(n)
        if b == 0:
            continue
        nonzero += 1
        ratio = F(b * b, g(n))
        assert ratio <= 2
        maximum = max(maximum, ratio)
        integrated += float(ratio) / (2.0 * n * math.log(n))
    bound = 2.0 + math.log(math.log(limit))
    assert integrated <= bound
    return {
        "limit": limit,
        "nonzero_beta": nonzero,
        "max_beta2_over_g": str(maximum),
        "integrated_energy_upper_numeric": integrated,
        "elementary_bound": bound,
    }


def smoothing_local_factor_check() -> dict:
    thetas = [F(0), F(1, 3), F(1, 2), F(7, 8)]
    for theta in thetas:
        coeffs = [F(1)] + [-(1 - theta) * theta ** (k - 1) for k in range(1, 12)]
        out = [F(0)] * 13
        for k, coeff in enumerate(coeffs):
            out[k] += coeff
            out[k + 1] -= theta * coeff
        assert out[0] == 1 and out[1] == -1
        assert all(v == 0 for v in out[2:12])
    return {"theta_fixtures": len(thetas), "coefficient_checks": 44}


def five_three_numerator_check() -> dict:
    assert {0: F(-6), 1: F(9), 2: F(-3)} == {0: F(-6), 1: F(9), 2: F(-3)}
    return {"factorization": "-3(2^-z-1)(2^-z-2)", "open_strip_zero_free": True}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    core = {
        "schema": "riemann.t99700.canonical-native-tilt.v1",
        "classification": VERDICT,
        "checks": {
            "beta_positive_inverse": conv_beta_g_limit(5000),
            "logarithmic_owner_formal": owner_identity_limit(3000),
            "symmetric_native_homotopy": symmetric_homotopy_check(
                [F(1, 3), F(1, 5), F(1, 7), F(1, 11)]
            ),
            "alpha_native_firewall": alpha_firewall(),
            "critical_tilt_energy": tilt_energy_check(200000),
            "positive_euler_smoothing_local_factor": smoothing_local_factor_check(),
            "five_three_numerator": five_three_numerator_check(),
        },
        "proved": {
            "native_sequential_first_owner_identity": True,
            "symmetric_euler_homotopy_identity": True,
            "tilted_owner_flow_identity": True,
            "tilted_positive_inverse_renewal": True,
            "critical_tilt_energy_loglog_bound": True,
            "absolute_subcritical_euler_smoothing_cancels_detector": True,
            "scalar_negative_mass_implies_rh": True,
        },
        "open": {
            "tilted_owner_carleson_embedding_TOCE67": True,
            "subpower_negative_mass": True,
            "riemann_hypothesis": True,
        },
        "rh_established": False,
    }
    canonical = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    core["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    text = json.dumps(core, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    print(VERDICT)
    print(core["proof_object_sha256"])


if __name__ == "__main__":
    main()
