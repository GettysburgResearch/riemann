#!/usr/bin/env python3
"""Exact finite diagnostics for STRATIFIED_TWO_SCALAR_A2.md.

These checks concern formal masks, divisor identities, rational exponent
algebra and finite parameter grids. They do not verify theta automorphy,
analytic estimates, actual Gauss sums or an infinite range by enumeration.
All gates use exceptions and remain enabled under python -O.
"""

import argparse
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from pathlib import Path


PROOF_SHA256 = "9b540fe779b6e0f3c64baba04deed6ee380f1d9746035afc3cf9c7fdb0cf3ad5"
PROOF_BYTES = 22168


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def fs(value):
    return str(F(value))


def monomials(beta):
    """Energy exponents, coordinates H,A,B,J,K,R, from Theorem 3.1."""
    p = F(5, 2) - beta
    return [
        (F(1), F(1), F(0), F(0), F(0), F(0)),
        (F(2), F(1), beta-F(3, 2), F(1), F(0), p),
        (F(4, 3), F(4, 3), F(-2, 3), F(0), F(1), 2*beta),
        (F(1), F(0), F(0), F(0), F(0), F(0)),
        (F(0), F(1), F(1), F(0), F(0), F(-3)),
        (F(2, 3), F(2, 3), F(2, 3), F(0), F(0), F(-2)),
    ]


def dot(left, right):
    return sum((x*y for x, y in zip(left, right)), F(0))


def derived_a2_table(beta, tau):
    # Actual A2 child substitutions, one vector per H,A,B,J,K,R.
    substitutions = [
        (F(0), F(0), F(0)),
        (F(-1), F(-2), F(-2)),
        (F(-2), F(-1), F(-2)),
        (F(1), F(1), F(1)),
        (F(1, 3), F(1, 3), F(2, 3)),
        (-2*tau, -tau, -2*tau),
    ]
    exterior = (F(-1), F(-1), F(-3, 2))
    return [tuple(exterior[i] + sum(
        (power*sub[i] for power, sub in zip(term, substitutions)), F(0))/2
        for i in range(3)) for term in monomials(beta)]


def displayed_a2_table(beta, tau):
    return [
        (F(-3, 2), F(-2), F(-5, 2)),
        (F(-1), F(-3, 2), F(-2)),
        (-F(5, 6)-2*beta*tau, -F(11, 6)-beta*tau,
         -F(11, 6)-2*beta*tau),
        (F(-1), F(-1), F(-3, 2)),
        (-F(5, 2)+3*tau, -F(5, 2)+F(3, 2)*tau,
         -F(7, 2)+3*tau),
        (-2+2*tau, -2+tau, -F(17, 6)+2*tau),
    ]


def check_masks_and_rows():
    mask_cases = 0
    for q, f, n, row_rad in product(range(8), repeat=4):
        reduced = q & ~f
        physical_zero = bool(n & (q | f | row_rad))
        relabeled_zero = bool(n & (reduced | f | row_rad))
        require(physical_zero == relabeled_zero, "sixth-power mask mismatch")
        for x, y, z in product(range(8), repeat=3):
            if ((x & y) or (x & z) or (y & z)
                    or ((x | y | z) & (q | f))):
                continue
            child_q, child_f = q | x | y | z, f | z
            require((child_q & ~child_f) == (reduced | x | y),
                    "A2 redundant-overlap identity mismatch")
        mask_cases += 1
    row_cases = overlap_cases = 0
    for valuations in product(range(18), repeat=3):
        quotients = tuple(v//6 for v in valuations)
        remainders = tuple(v % 6 for v in valuations)
        require(all(6*a+b == v for a, b, v in
                    zip(quotients, remainders, valuations)),
                "sixth-power row reconstruction mismatch")
        require(all(0 <= b <= 5 for b in remainders),
                "not sixth-power-free")
        row_cases += 1
        if any(a and b for a, b in zip(quotients, remainders)):
            overlap_cases += 1
    require(overlap_cases > 0, "missing v/k0 overlap negative control")
    return {"mask_cases": mask_cases, "row_valuation_cases": row_cases,
            "v_k0_overlap_cases_retained": overlap_cases}


def check_sixth_free_sieve_algebra():
    cases = 0
    for a in product(range(4), repeat=5):
        p0, maximum = sum(a), max(a)
        height = sum((j+1)*a[j] for j in range(5))
        require(p0 <= height, "P0 exceeds physical height")
        require(2*p0-maximum <= height, "P0 squared over M inequality")
        require(3*p0-maximum <= 2*height, "mixed sieve monomial inequality")
        for column in range(7):
            first = max(F(p0), F(p0+column-maximum),
                        F(p0)+F(2, 3)*column-F(1, 3)*maximum)
            second = max(F(column), F(2*p0))
            envelope = max(F(height), F(column), F(2, 3)*(height+column))
            require(min(first, second) <= envelope,
                    "sixth-power-free sieve exponent envelope")
            cases += 1
    return {"valuation_column_exponent_cases": cases}


def omega_value(t):
    # A rational value-profile with the proof's endpoint/support convention.
    # It tests finite identities only; this piecewise linear profile is not
    # used to claim the smooth derivative estimates in the manuscript.
    if t <= F(1, 2):
        return F(1)
    if t >= 1:
        return F(0)
    return 2-2*t


def squarefree_divisors(exponents, primes):
    for bits in product((0, 1), repeat=len(primes)):
        if any(bit > exponent for bit, exponent in zip(bits, exponents)):
            continue
        norm = 1
        for bit, prime in zip(bits, primes):
            norm *= prime**bit
        yield bits, norm, (-1)**sum(bits)


def check_inverse_cutoffs():
    primes = (7, 13, 19)
    cutoffs = (F(1, 4), F(1, 2), F(1), F(3, 2), F(2),
               F(7), F(13), F(26), F(50), F(1000))
    identities = supported_zero_cases = forbidden_coprime_rejections = 0
    for exponents in product(range(3), repeat=3):
        norm = 1
        for prime, exponent in zip(primes, exponents):
            norm *= prime**exponent
        divs = list(squarefree_divisors(exponents, primes))
        full = sum(mu for _, _, mu in divs)
        expected = int(not any(exponents))
        require(full == expected, "complete cube inverse identity")
        coprime_only = sum(mu for bits, _, mu in divs
                           if not any(bit and exponent-bit for bit, exponent
                                      in zip(bits, exponents)))
        if coprime_only != expected:
            forbidden_coprime_rejections += 1
        for cutoff in cutoffs:
            short = sum((mu*omega_value(F(h)/cutoff)
                         for _, h, mu in divs), F(0))
            long = sum((mu*(1-omega_value(F(h)/cutoff))
                        for _, h, mu in divs), F(0))
            require(short+long == expected, "smooth short/long identity")
            if norm <= cutoff/2:
                require(long == 0, "Nd<=r/2 long support did not vanish")
                supported_zero_cases += 1
            identities += 1
    require(forbidden_coprime_rejections > 0,
            "forbidden (h,b)=1 control did not reject")
    cap_cases = wrong_cap_rejections = 0
    for support_cap, v_norm, parent_r in product((1, 7, 13, 49),
                                                (1, 7, 13, 49), cutoffs):
        cutoff = min(F(2*support_cap), parent_r*v_norm)
        for h in range(1, support_cap+1):
            value = omega_value(F(h)/cutoff)
            if cutoff <= 1:
                require(value == 0, "small-cutoff short part not empty")
            if cutoff == 2*support_cap:
                require(value == 1, "doubled cap did not empty the long part")
            if value != 0:
                require(F(h)/cutoff < 1, "rescaled short support mismatch")
            cap_cases += 1
        if omega_value(F(support_cap)/support_cap) != 1:
            wrong_cap_rejections += 1
    require(wrong_cap_rejections > 0, "undoubled cap control did not reject")
    return {"smooth_divisor_identities": identities,
            "exact_long_support_zero_cases": supported_zero_cases,
            "cap_and_short_support_cases": cap_cases,
            "forbidden_h_b_coprimality_rejections": forbidden_coprime_rejections,
            "undoubled_cap_rejections": wrong_cap_rejections}


def check_exponent_tables():
    betas = {F(n, d) for d in range(2, 33)
             for n in range(d//2+1, d+1)}
    betas.update((F(501, 1000), F(5001, 10000), F(11, 12)))
    table_entries = stratum_entries = 0
    for beta in sorted(betas):
        p, tau = F(5, 2)-beta, (3-2*beta)/(5-2*beta)
        require(F(1, 3) <= tau < F(1, 2), "child cutoff exponent range")
        require(p*tau == (3-2*beta)/2, "critical cutoff identity")
        table = derived_a2_table(beta, tau)
        require(table == displayed_a2_table(beta, tau), "A2 table mismatch")
        for row, values in enumerate(table):
            for column, value in enumerate(values):
                harmonic = (row, column) in ((1, 0), (3, 0), (3, 1))
                require(value == -1 if harmonic else value < -1,
                        "wrong harmonic/convergent A2 classification")
                table_entries += 1
        v_powers = [dot(term, (F(-6), F(0), F(0), F(1), F(1, 3), F(1)))
                    for term in monomials(beta)]
        expected = [F(-6), -F(17, 2)-beta, -F(23, 3)+2*beta,
                    F(-6), F(-3), F(-6)]
        require(v_powers == expected, "sixth-power stratum exponents")
        require(all(v < -1 for v in v_powers), "nonsummable physical strata")
        stratum_entries += len(v_powers)
    old = derived_a2_table(F(11, 12), F(1, 3))[1][0]
    require(old == F(-17, 18) and old > -1,
            "old-cutoff independent-coordinate control did not reject")
    # Clamping a legal small child cutoff to one does not preserve the table.
    beta, tau, r, x = F(11, 12), F(7, 19), F(7, 55), F(2, 5)
    child_r = r-2*tau*x
    require(child_r < 0, "small child cutoff example not small")
    term = monomials(beta)[1]
    parent = dot(term, (F(1, 2), F(1), F(1), F(0), F(0), r))
    clamped_child = dot(term, (F(1, 2), 1-x, 1-2*x, x, x/3, F(0)))
    clamped_norm = -x+(clamped_child-parent)/2
    require(clamped_norm > -x, "clamped-cutoff norm-table control did not reject")
    return {"beta_grid_size": len(betas), "a2_norm_entries": table_entries,
            "stratum_power_entries": stratum_entries,
            "old_cube_root_x_power": fs(old),
            "old_cutoff_control_scope": "independent coordinatewise summation only",
            "clamped_child_cutoff_control": "rejects preservation of the stated norm table"}


def energy_exponents(beta, height, j_power, k_power, r):
    return [dot(term, (height, F(1), F(1), j_power, k_power, r))
            for term in monomials(beta)]


def check_optimization():
    betas = (F(5001, 10000), F(51, 100), F(2, 3), F(3, 4),
             F(11, 12), F(1))
    cases, grid = 0, 20
    for beta in betas:
        p, q = F(5, 2)-beta, 2*beta
        for a in range(grid+1):
            for b in range(grid+1-a):
                height, j_power = p*F(a, 2*grid), p*F(b, grid)
                for fraction in (F(0), F(1, 2), F(1)):
                    k_power = F(2, 3)*j_power*fraction
                    require(j_power+2*height <= p, "infeasible grid point")
                    r2 = (p-2*height-j_power)/(p+3)
                    r3 = (F(4, 3)-F(4, 3)*height-k_power)/(q+3)
                    r = min(r2, r3)
                    require(r2 >= 0 and 0 <= r3 <= F(1, 3),
                            "balancing cutoff admissibility")
                    require(0 <= r <= F(1, 3), "parent cutoff out of range")
                    exponents = energy_exponents(beta, height, j_power, k_power, r)
                    target = 2-3*r
                    e2 = (6-p)/(p+3)+6*height/(p+3)+3*j_power/(p+3)
                    e3 = (4*beta+2)/(q+3)+4*height/(q+3)+3*k_power/(q+3)
                    require(max(exponents) == target == max(e2, e3),
                            "six-term optimization envelope mismatch")
                    require(target <= 2, "diagonal-size consequence failed")
                    cases += 1
    beta, r = F(11, 12), F(7, 55)
    example = energy_exponents(beta, F(1, 2), F(0), F(0), r)
    required = [F(3, 2), F(89, 55), F(47, 30), F(1, 2),
                F(89, 55), F(233, 165)]
    require(example == required and max(example) == F(89, 55),
            "89/55 example failed")
    require(F(31, 19)-F(89, 55) == F(14, 1045), "adjacent saving mismatch")
    require(F(1087, 660)-F(89, 55) == F(19, 660), "raw saving mismatch")
    require((F(5, 2)-beta)/2 == F(19, 24), "row-height range mismatch")
    p = F(5, 2)-beta
    r2, r3 = p/(p+3), F(4, 3)/(2*beta+3)
    require(r2 > F(1, 3) and r3 < F(1, 3),
            "separate R2 upper-bound negative control did not reject")
    require(F(5, 2)-1 == F(9, 2)-3 and 2*F(1) == 2,
            "counting scalar specialization mismatch")
    return {"admissible_rational_parameter_cases": cases,
            "square_root_height_energy_exponents": list(map(fs, example)),
            "optimized_exponent": "89/55", "saving_over_924": "14/1045",
            "saving_over_unstratified_raw": "19/660",
            "unit_label_row_height_range": "19/24",
            "separate_R2_upper_bound_control": "rejected; only the minimum needs the cap"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--proof", required=True, type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    proof = args.proof.read_bytes()
    actual_hash = sha256(proof).hexdigest()
    require(actual_hash == PROOF_SHA256, "proof hash does not match reviewed bytes")
    require(len(proof) == PROOF_BYTES, "proof byte count does not match")
    report = {
        "status": "PASS",
        "proof_sha256": actual_hash,
        "proof_bytes": len(proof),
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": [
            "exact finite formal masks and divisor identities",
            "exact rational valuation and norm-exponent algebra",
            "finite admissible optimization grids, supplemented by the written proof",
            "no analytic theorem, automorphy, actual Gauss sum or full moment certification",
            "all gates use exceptions and remain active under python -O",
        ],
        "masks_and_row_strata": check_masks_and_rows(),
        "sixth_power_free_sieve": check_sixth_free_sieve_algebra(),
        "inverse_and_caps": check_inverse_cutoffs(),
        "a2_and_stratum_exponents": check_exponent_tables(),
        "optimization": check_optimization(),
    }
    rendered = json.dumps(report, indent=2, sort_keys=True)+"\n"
    if args.report:
        args.report.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
