#!/usr/bin/env python3
from fractions import Fraction
from math import isqrt
import json
from pathlib import Path
import sys
import hashlib

sys.set_int_max_str_digits(0)

DEN = 10**70
P0 = 500_000
ROWS = range(2, 67)


def sqrt_interval(n: int):
    lo = isqrt(n * DEN * DEN)
    hi = lo if lo * lo == n * DEN * DEN else lo + 1
    return Fraction(lo, DEN), Fraction(hi, DEN)


def invsqrt_interval(n: int):
    lo, hi = sqrt_interval(n)
    return Fraction(1, hi), Fraction(1, lo)


def log_interval(x: Fraction, terms: int = 220):
    exponent = 0
    y = x
    while y >= 2:
        y /= 2
        exponent += 1
    while y < 1:
        y *= 2
        exponent -= 1

    def base(z: Fraction):
        z2 = z * z
        power = z
        partial = Fraction(0)
        for k in range(terms):
            partial += power / Fraction(2 * k + 1)
            power *= z2
        partial *= 2
        tail = 2 * power / (Fraction(2 * terms + 1) * (1 - z2))
        return partial, partial + tail

    lo, hi = base((y - 1) / (y + 1))
    l2lo, l2hi = base(Fraction(1, 3))
    if exponent >= 0:
        return lo + exponent * l2lo, hi + exponent * l2hi
    return lo + exponent * l2hi, hi + exponent * l2lo


def main():
    delta_lo, _ = log_interval(Fraction(66, 65))
    logp_lo, _ = log_interval(Fraction(P0))
    _, sqrt67p_hi = sqrt_interval(67 * P0)

    minimum = None
    records = []

    for j in ROWS:
        c = Fraction(2, j * (j - 1))
        h_lo = Fraction(0)
        hlog_hi = Fraction(0)

        for m in range(1, j):
            inv_lo, inv_hi = invsqrt_interval(m)
            h_lo += inv_lo
            _, l_hi = log_interval(Fraction(m))
            hlog_hi += inv_hi * l_hi

        sj_lo, sj_hi = sqrt_interval(j)
        sj1_lo, sj1_hi = sqrt_interval(j + 1)
        a_lo = Fraction(j + 2, j) / sj_hi
        a_hi = Fraction(j + 2, j) / sj_lo
        b_lo = Fraction(1, 1) / sj1_hi
        b_hi = Fraction(1, 1) / sj1_lo

        eta_lo = c * (1 + h_lo) - a_hi + b_lo
        assert eta_lo > 0, (j, "eta", eta_lo)

        lj_lo, _ = log_interval(Fraction(j))
        _, lj1_hi = log_interval(Fraction(j + 1))
        K_hi = -4 * c + c * hlog_hi - a_lo * lj_lo + b_hi * lj1_hi
        assert K_hi < 0, (j, "K", K_hi)

        A_lo = (5 * logp_lo - 10) * eta_lo - 22 * c - 5 * K_hi
        assert A_lo > 0, (j, "A", A_lo)

        _, invj_hi = invsqrt_interval(j)
        denominator_lo = 5 - 3 * invj_hi
        assert denominator_lo > 0
        B_hi = 4 * c / denominator_lo

        lhs_lo = delta_lo * A_lo / (50 * sqrt67p_hi)
        rhs_hi = B_hi / Fraction(P0 - 1)
        margin = lhs_lo - rhs_hi
        assert margin > 0, (j, "tail margin", margin)

        record = {
            "row": j,
            "margin_lower": margin,
            "lhs_lower": lhs_lo,
            "rhs_upper": rhs_hi,
            "A_lower": A_lo,
            "B_upper": B_hi,
            "eta_lower": eta_lo,
            "K_upper": K_hi,
        }
        records.append(record)
        if minimum is None or margin < minimum["margin_lower"]:
            minimum = record

    result = {
        "classification": "PASS_CAUSAL_ARITHMETIC_GAP_TAIL",
        "rough_prime_tail_start": P0,
        "rows_checked": len(list(ROWS)),
        "row_range": [2, 66],
        "minimum_gap_ratio": "66/65",
        "minimum_row": minimum["row"],
        "minimum_margin_decimal": float(minimum["margin_lower"]),
        "minimum_lhs_decimal": float(minimum["lhs_lower"]),
        "minimum_rhs_decimal": float(minimum["rhs_upper"]),
        "exact_record_digest_sha256": hashlib.sha256(
            "\n".join(
                f"{r['row']}:{r['margin_lower'].numerator}/{r['margin_lower'].denominator}"
                for r in records
            ).encode("ascii")
        ).hexdigest(),
        "checks": {
            "eta_positive": 65,
            "K_negative": 65,
            "large_Y_bracket_positive": 65,
            "tail_gap_margin_positive": 65,
        },
        "scope": (
            "Exact Fraction arithmetic and directed square-root/logarithm "
            "intervals prove the sufficient arithmetic-gap inequality for "
            "every row 2<=j<=66 at p=500000. Monotonicity of A_j(p) and "
            "(p-1)/sqrt(p) extends it to every real p>=500000. Combined "
            "with L-91359, this proves discrete inner-divisor causal "
            "row-per-score ordering on the unbounded rough-prime tail. "
            "It does not certify the finite corridor 67<=p<500000, the "
            "global even/odd determinant, packet score debt, or RH."
        ),
    }

    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print("minimum row:", result["minimum_row"])
    print("minimum margin:", result["minimum_margin_decimal"])
    print(out)


if __name__ == "__main__":
    main()
