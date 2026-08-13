#!/usr/bin/env python3
from fractions import Fraction
import json
from pathlib import Path

from interval_core import (
    PRIMES, MAX_J, DILATION, MAX_BASE, DEN, LOG_TERMS,
    build_log_intervals, build_inverse_sqrt_intervals,
    mul_interval, rational_mul_interval, squarefree_divisors, add_signed,
)


def main() -> None:
    logs = build_log_intervals(MAX_BASE)
    inv_sqrt = build_inverse_sqrt_intervals(MAX_BASE)
    divisors = [(d, mu) for d, mu in squarefree_divisors() if d <= MAX_BASE]
    divisor_map = dict(divisors)

    m_lo = [0] * (MAX_BASE + 1)
    m_hi = [0] * (MAX_BASE + 1)
    l_lo = [0] * (MAX_BASE + 1)
    l_hi = [0] * (MAX_BASE + 1)
    cur_m_lo = cur_m_hi = cur_l_lo = cur_l_hi = 0
    for threshold in range(1, MAX_BASE + 1):
        mu = divisor_map.get(threshold)
        if mu is not None:
            inv_lo, inv_hi = inv_sqrt[threshold]
            cur_m_lo, cur_m_hi = add_signed(
                cur_m_lo, cur_m_hi, inv_lo, inv_hi, mu
            )
            prod_lo, prod_hi = mul_interval(
                inv_lo, inv_hi, logs[threshold][0], logs[threshold][1]
            )
            cur_l_lo, cur_l_hi = add_signed(
                cur_l_lo, cur_l_hi, prod_lo, prod_hi, mu
            )
        m_lo[threshold], m_hi[threshold] = cur_m_lo, cur_m_hi
        l_lo[threshold], l_hi[threshold] = cur_l_lo, cur_l_hi

    rough_a_lo = [0] * (MAX_BASE + 1)
    rough_a_hi = [0] * (MAX_BASE + 1)
    rough_l_lo = [0] * (MAX_BASE + 1)
    rough_l_hi = [0] * (MAX_BASE + 1)
    cur_a_lo = cur_a_hi = cur_b_lo = cur_b_hi = 0
    for n in range(1, MAX_BASE + 1):
        if all(n % prime for prime in PRIMES):
            inv_lo, inv_hi = inv_sqrt[n]
            cur_a_lo += inv_lo
            cur_a_hi += inv_hi
            prod_lo, prod_hi = mul_interval(
                inv_lo, inv_hi, logs[n][0], logs[n][1]
            )
            cur_b_lo += prod_lo
            cur_b_hi += prod_hi
        rough_a_lo[n], rough_a_hi[n] = cur_a_lo, cur_a_hi
        rough_l_lo[n], rough_l_hi[n] = cur_b_lo, cur_b_hi

    def green_interval(n: int, m: int) -> tuple[int, int]:
        threshold = n // m
        log_lo = max(0, logs[n][0] - logs[m][1])
        log_hi = max(0, logs[n][1] - logs[m][0])
        prod_lo, prod_hi = mul_interval(
            log_lo, log_hi, m_lo[threshold], m_hi[threshold]
        )
        return prod_lo - l_hi[threshold], prod_hi - l_lo[threshold]

    def rough_interval(n: int) -> tuple[int, int]:
        prod_lo, prod_hi = mul_interval(
            logs[n][0], logs[n][1], rough_a_lo[n], rough_a_hi[n]
        )
        return prod_lo - rough_l_hi[n], prod_hi - rough_l_lo[n]

    def row_interval(n: int, j: int) -> tuple[int, int]:
        rough_lo, rough_hi = rough_interval(n)
        total_lo, total_hi = rational_mul_interval(
            rough_lo * DEN, rough_hi * DEN, 2, j * (j - 1)
        )
        for m in range(1, j):
            green_lo, green_hi = green_interval(n, m)
            prod_lo, prod_hi = mul_interval(
                green_lo, green_hi, inv_sqrt[m][0], inv_sqrt[m][1]
            )
            term_lo, term_hi = rational_mul_interval(
                prod_lo, prod_hi, -2, j * (j - 1)
            )
            total_lo += term_lo
            total_hi += term_hi

        green_lo, green_hi = green_interval(n, j)
        prod_lo, prod_hi = mul_interval(
            green_lo, green_hi, inv_sqrt[j][0], inv_sqrt[j][1]
        )
        term_lo, term_hi = rational_mul_interval(prod_lo, prod_hi, j + 2, j)
        total_lo += term_lo
        total_hi += term_hi

        green_lo, green_hi = green_interval(n, j + 1)
        prod_lo, prod_hi = mul_interval(
            green_lo, green_hi, inv_sqrt[j + 1][0], inv_sqrt[j + 1][1]
        )
        total_lo -= prod_hi
        total_hi -= prod_lo
        return total_lo, total_hi

    cells_checked = 0
    minimum = None
    scale3 = DEN**3
    for j in range(2, MAX_J + 1):
        for n in range(j + 1, DILATION * j + 1):
            lower, upper = row_interval(n, j)
            cells_checked += 1
            if lower <= 0:
                raise AssertionError((n, j, lower, upper))
            if minimum is None or lower < minimum[0]:
                minimum = (lower, upper, n, j)

    assert cells_checked == 145_860
    assert minimum is not None
    lower, upper, n_min, j_min = minimum
    assert (n_min, j_min) == (67, 66)
    assert Fraction(lower, scale3) > Fraction(1, 525)

    result = {
        "classification": "PASS_GLOBAL_P61_FINITE_EULER_ROW_BASE",
        "claim": "L-91364",
        "directed_integer_cells_checked": cells_checked,
        "rows_checked": 65,
        "finite_window": "j+1 <= N <= 67j, 2 <= j <= 66",
        "minimum_N": n_min,
        "minimum_j": j_min,
        "minimum_lower_rational": f"{lower}/{scale3}",
        "minimum_upper_rational": f"{upper}/{scale3}",
        "minimum_lower_decimal": format(lower / scale3, ".18g"),
        "certified_simple_lower": "1/525",
        "interval_lattice_denominator": str(DEN),
        "log_terms": LOG_TERMS,
        "global_transport": (
            "Use L-91346 with (p,y)=(67,X/67) below 67^2 and "
            "(p,y)=(X/67,67) above 67^2."
        ),
        "open_boundary": (
            "Terminal correction, collar, common-port typing, and common "
            "two-label normalization are not checked here."
        ),
    }
    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(out)


if __name__ == "__main__":
    main()
