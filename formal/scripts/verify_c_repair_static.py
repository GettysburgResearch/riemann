#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FORMAL = ROOT / "formal"


def energy(j: tuple[F, F, F]) -> F:
    v, d1, d2 = j
    return v * d2 - 2 * d1 * d1


def cross(f: tuple[F, F, F], g: tuple[F, F, F]) -> F:
    fv, f1, f2 = f
    gv, g1, g2 = g
    return fv * g2 + gv * f2 - 4 * f1 * g1


def offline(m: F, U: F, B: F) -> tuple[F, F, F]:
    den = U * U + B * B
    return (
        4 * m * U / den,
        4 * m * (B * B - U * U) / den**2,
        8 * m * U * (U * U - 3 * B * B) / den**3,
    )


def critical(V: F) -> tuple[F, F, F]:
    return 2 / V, -2 / V**2, 4 / V**3


def qpoly(k: F, s: F) -> F:
    return 1 - k + 3 * k * s * (2 - s) + k**2 * s**2 * (3 - 2 * s)


def quad2(a: F, b: F, c: F, x: F, y: F) -> F:
    return a*x*x + 2*b*x*y + c*y*y


def quad3(a: F, b: F, c: F, d: F, e: F, f: F, x: F, y: F, z: F) -> F:
    return a*x*x + 2*b*x*y + 2*c*x*z + d*y*y + 2*e*y*z + f*z*z


def main() -> None:
    fixtures = [
        (F(2), F(12), F(1, 3), F(1, 4), F(2)),
        (F(3), F(20), F(1, 2), F(1, 25), F(2)),
        (F(5), F(18), F(2, 3), F(1, 16), F(3)),
    ]
    checked = 0
    for m, U, s, k, B in fixtures:
        assert B*B == k*s*s*U*U
        V = U*(1-s)
        q = offline(m, U, B)
        r = critical(V)
        rhs_cross = 16*m*s*s*qpoly(k, s)/(U**4*(1+k*s*s)**3*(1-s)**3)
        assert cross(q, r) == rhs_cross
        defect = 32*m*m*B*B/(U*U+B*B)**3
        assert energy(q) == -defect
        eps = 2*m*k/(1-k)
        assert defect <= eps*rhs_cross
        checked += 1

    for a, g, d, x, y, z in [
        (F(2), F(1, 3), F(5), F(1), F(2), F(3)),
        (F(0), F(-2), F(7), F(-1), F(4), F(2)),
    ]:
        assert quad3(a, a, g, a, g, d, x, y, z) == quad2(a, g, d, x+y, z)
        assert quad3(a, g, a, d, g, a, x, y, z) == quad2(a, g, d, x+z, y)
        assert quad3(a, g, g, d, d, d, x, y, z) == quad2(a, g, d, x, y+z)
        checked += 3

    statement = (
        FORMAL / "registry" / "deltas" / "C_EXTERNAL_SOURCE_STATEMENTS" /
        "EXT.XI.PLATT_TRUDGIAN.2021.txt"
    )
    actual_hash = hashlib.sha256(statement.read_bytes()).hexdigest()
    lock_text = (FORMAL / "registry" / "deltas" / "C_EXTERNAL_SOURCE_LOCKS.tsv").read_text()
    lean_text = (
        FORMAL / "comparator" / "ChallengeDeps" /
        "XiPickOrderThreeConditional.lean"
    ).read_text()
    assert actual_hash in lock_text
    assert actual_hash in lean_text

    result = {
        "status": "PASS_REVIEWER_C_REPAIR_STATIC",
        "exact_fraction_fixtures": checked,
        "external_statement_sha256": actual_hash,
        "heavy_computation_rerun": False,
        "rh_proved": False,
    }
    out = FORMAL / "reports" / "C_REPAIR_STATIC_REPLAY.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(result["status"], f"fixtures={checked}")


if __name__ == "__main__":
    main()
