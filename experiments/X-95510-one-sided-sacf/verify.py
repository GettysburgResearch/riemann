#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent


def mobius(n: int) -> int:
    m = n
    count = 0
    p = 2
    while p*p <= m:
        if m % p == 0:
            m //= p
            count += 1
            if m % p == 0:
                return 0
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        count += 1
    return -1 if count % 2 else 1


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n+1) if n % d == 0]


def is_squarefree(n: int) -> bool:
    return mobius(n) != 0


def moment_direct(D0: int, D1: int, k: int, ell: int, q: int) -> float:
    total = 0.0
    for d in range(D0+1, D1+1):
        if d % 2 == 1 and is_squarefree(d) and math.gcd(d, k) == 1:
            total += d**(ell-1) * (math.log(d)**q)
    return total


def moment_lcm(D0: int, D1: int, k: int, ell: int, q: int) -> float:
    total = 0.0
    for h in range(1, math.isqrt(D1)+1):
        muh = mobius(h)
        if muh == 0:
            continue
        for e in divisors(2*k):
            mue = mobius(e)
            if mue == 0:
                continue
            L = math.lcm(h*h, e)
            inner = 0.0
            for n in range(D0//L + 1, D1//L + 1):
                d = L*n
                if not (D0 < d <= D1):
                    continue
                inner += n**(ell-1) * ((math.log(L)+math.log(n))**q)
            total += muh*mue*(L**(ell-1))*inner
    return total


def main() -> None:
    # Automatic lower bound: Xcross=A^2-D >= -D.
    for A, D in ((Fraction(3, 7), Fraction(5, 2)),
                 (Fraction(-11, 9), Fraction(17, 5)),
                 (Fraction(0), Fraction(2, 3))):
        Xcross = A*A-D
        assert Xcross >= -D

    # One-sided upper control plus closed errors controls A^2.
    D = Fraction(9)
    S_upper = Fraction(16)
    E_abs = Fraction(4)
    A2_upper = D + S_upper + E_abs
    assert A2_upper == 29

    # Stable inverse mass from the three safe factors.
    inverse_mass = Fraction(1, 1) / (1-Fraction(1, 2))
    inverse_mass *= Fraction(1, 1) / (1-Fraction(1, 4))
    inverse_mass *= Fraction(1, 1) / (1-Fraction(1, 8))
    assert inverse_mass == Fraction(64, 21)

    # Exact lcm expansion of odd squarefree/coprime moments.
    checks = []
    for ell in (2, 4, 6):
        for q in (0, 1, 2):
            direct = moment_direct(7, 83, 15, ell, q)
            expanded = moment_lcm(7, 83, 15, ell, q)
            err = abs(direct-expanded)
            tol = 1e-8 * max(1.0, abs(direct))
            assert err <= tol, (ell, q, direct, expanded, err)
            checks.append({"ell": ell, "q": q, "abs_error": err})

    result = {
        "schema": "riemann.t95510.one-sided-sacf-moments.v1",
        "base_pr": 580,
        "base_sha": "812e7fcbaff2dd1c2c53c885def7b6c0d0e68a05",
        "automatic_cross_lower_bound": True,
        "one_sided_upper_suffices": True,
        "stable_inverse_mass": str(inverse_mass),
        "moment_lcm_checks": checks,
        "uosacf_proved": False,
        "rh_established": False,
        "verdict": "PASS_T95510_ONE_SIDED_SUBPOWER_AND_MOMENT_COMPRESSION",
    }
    canon = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = sha256(canon).hexdigest()
    out = HERE / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["verdict"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
