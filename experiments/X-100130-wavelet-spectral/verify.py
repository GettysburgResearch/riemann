#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path

VERDICT = "PASS_T100130_MINIMAL_WAVELET_SPECTRAL_AUDIT"


def factor(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    x = n
    p = 2
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


@dataclass(frozen=True)
class Q2:
    """Exact a+b*sqrt(2)."""

    a: F = F(0)
    b: F = F(0)

    @staticmethod
    def coerce(x: object) -> "Q2":
        return x if isinstance(x, Q2) else Q2(F(x))

    def __add__(self, other: object) -> "Q2":
        o = Q2.coerce(other)
        return Q2(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __neg__(self) -> "Q2":
        return Q2(-self.a, -self.b)

    def __sub__(self, other: object) -> "Q2":
        return self + (-Q2.coerce(other))

    def __rsub__(self, other: object) -> "Q2":
        return Q2.coerce(other) - self

    def __mul__(self, other: object) -> "Q2":
        o = Q2.coerce(other)
        return Q2(
            self.a * o.a + 2 * self.b * o.b,
            self.a * o.b + self.b * o.a,
        )

    __rmul__ = __mul__

    def __pow__(self, n: int) -> "Q2":
        out = Q2(F(1))
        x = self
        k = n
        while k:
            if k & 1:
                out = out * x
            x = x * x
            k //= 2
        return out

    def is_zero(self) -> bool:
        return self.a == 0 and self.b == 0


def check_floor_kernel_cancellation() -> dict:
    q = {1: F(3, 2), 2: F(1, 3), 5: F(7, 4), 9: F(2, 5)}

    def kernel(x: int) -> F:
        return sum((v * (x // j) for j, v in q.items()), F(0))

    checks = 0
    for N in range(1, 257):
        lhs = sum((F(mobius(m)) * kernel(N // m) for m in range(1, N + 1)), F(0))
        rhs = sum((v for j, v in q.items() if j <= N), F(0))
        assert lhs == rhs, (N, lhs, rhs)
        checks += 1
    return {"integer_checks": checks, "zeta_detector_cancelled": True}


def check_wavelet_multiplier() -> dict:
    root2 = Q2(F(0), F(1))
    # (1-sqrt(2)x)(1-x)^2
    coeff = [
        Q2(F(1)),
        -(Q2(F(2)) + root2),
        Q2(F(1)) + 2 * root2,
        -root2,
    ]

    # Double zero at x=1, corresponding to s=0.
    assert sum(coeff, Q2()).is_zero()
    assert sum((Q2(F(k)) * coeff[k] for k in range(4)), Q2()).is_zero()

    # Zero at x=2^(-1/2)=1/sqrt(2), corresponding to s=1/2.
    x = Q2(F(0), F(1, 2))
    assert sum((coeff[k] * (x**k) for k in range(4)), Q2()).is_zero()

    return {
        "operator_coefficients": [
            "1", "-(2+sqrt(2))", "1+2sqrt(2)", "-sqrt(2)"
        ],
        "double_zero_s_0": True,
        "zero_s_half": True,
        "off_line_zero_cancellation": False,
    }


def check_exponent_dictionary() -> dict:
    fixtures = [F(1, 2), F(3, 5), F(2, 3), F(3, 4), F(9, 10)]
    rows = []
    for beta in fixtures:
        sigma = beta + F(1, 2)
        critical_energy_exponent = 2 * beta - 1
        assert sigma - 1 == critical_energy_exponent / 2
        rows.append(
            {
                "zero_real_part": str(beta),
                "energy_abscissa": str(sigma),
                "critical_energy_exponent": str(critical_energy_exponent),
            }
        )
    return {"fixtures": rows, "theta_transfer_exact": True}


def main() -> None:
    payload = {
        "verdict": VERDICT,
        "floor_kernel": check_floor_kernel_cancellation(),
        "wavelet_multiplier": check_wavelet_multiplier(),
        "spectral_exponents": check_exponent_dictionary(),
        "mwoc_unconditionally_proved": False,
        "rh_established": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()

    out = Path(__file__).with_name("results") / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(VERDICT)
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
